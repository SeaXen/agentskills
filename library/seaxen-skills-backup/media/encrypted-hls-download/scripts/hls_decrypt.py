#!/usr/bin/env python3
"""Reusable encrypted HLS download + decrypt + remux pipeline.

Tested on Synapse Medical Academy (lms.synapsepg.org -> player.vidinfra.com ->
kms.vidinfra.com -> jrgtfb2pnx.tenbytecdn.com), 2h6m / 833 MB output, true
MP4 container, H.264 720p + AAC, AES-128-CBC per-segment decryption.

Edit the constants in `main()` for the target platform, OR import the
functions and pass them your own. The pipeline is:

    1. Playwright headless login -> click video tile -> intercept KMS response
       to capture the 16-byte AES-128 key.
    2. Fetch the media playlist -> parse segment list (handles CRLF).
    3. Concurrent download of all .ts segments (ThreadPoolExecutor, 24 workers).
    4. AES-128-CBC decrypt each segment with IV = segment_number (16-byte BE)
       per HLS spec default. Strip PKCS7 padding from the last segment.
    5. Concat in order to a .ts intermediate, then ffmpeg stream-copy into a
       true .mp4 container with faststart. ffprobe-verify after.

Prereqs (install once):
    uv venv /root/.venvs/hls-env --python 3.13
    uv pip install --python /root/.venvs/hls-env/bin/python playwright pycryptodome
    /root/.venvs/hls-env/bin/python -m playwright install chromium
"""
import asyncio
import re
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ---------- Defaults (edit for your platform) ----------
DEFAULT_LMS_URL     = "https://lms.synapsepg.org/videos/<lecture-id>/lecture"
DEFAULT_USERNAME    = ""  # ask the user
DEFAULT_PASSWORD    = ""  # ask the user; pass via env / prompt, do not hardcode in committed code
DEFAULT_VIDEO_TITLE = ""  # the text on the clickable video tile
DEFAULT_KEY_SERVER  = "kms.vidinfra.com"          # substring match in the captured response URL
DEFAULT_CDN         = "https://<your-cdn-host>"   # the .ts segment host
DEFAULT_STREAM_ID   = ""                          # the per-video UUID in the m3u8 path
DEFAULT_QUALITY     = "720p"
DEFAULT_OUTPUT      = "/root/hls-output.mp4"
DEFAULT_BROWSER_UA  = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
)
DEFAULT_PLAYER_REFERER = "https://player.vidinfra.com/"
DEFAULT_HEADERS = {
    "Referer": DEFAULT_PLAYER_REFERER,
    "User-Agent": DEFAULT_BROWSER_UA,
}


# ---------- Phase 1: capture AES-128 key via headless browser ----------
async def capture_key(
    lms_url: str,
    username: str,
    password: str,
    video_title: str,
    key_server_substr: str = DEFAULT_KEY_SERVER,
    user_agent: str = DEFAULT_BROWSER_UA,
    max_wait_s: int = 30,
) -> bytes:
    """Open a headless browser, log in, click the video tile, capture the key
    server's response body. Returns the raw key bytes (16 for AES-128)."""
    from playwright.async_api import async_playwright

    captured: dict = {"data": None}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()

        async def on_response(r):
            if key_server_substr in r.url and "/keys" in r.url:
                try:
                    captured["data"] = await r.body()
                except Exception:
                    pass

        page.on("response", lambda r: asyncio.create_task(on_response(r)))

        # 1. Navigate (will redirect to login if needed)
        await page.goto(lms_url, wait_until="domcontentloaded", timeout=30000)
        if "/login" in page.url:
            # Adapt the selectors to your LMS's login form
            await page.get_by_placeholder("Enter mobile number").fill(username)
            await page.get_by_placeholder("Type your password").fill(password)
            await page.get_by_role("button", name="Sign In").click()
            await page.wait_for_url(lambda u: "/login" not in u, timeout=30000)

        # 2. Open lecture page
        await page.goto(lms_url, wait_until="domcontentloaded", timeout=30000)
        tile = page.locator(f'text="{video_title}"').first
        await tile.wait_for(state="visible", timeout=10000)
        await tile.click()

        # 3. Wait for the key
        for _ in range(max_wait_s):
            await page.wait_for_timeout(1000)
            if captured["data"]:
                break
        await browser.close()

    if not captured["data"]:
        raise RuntimeError(
            f"No key captured from {key_server_substr} after {max_wait_s}s. "
            "Check the video_title matches an actually-clickable element."
        )
    return captured["data"]


# ---------- Phase 2: fetch segment list ----------
def fetch_segments(cdn_base: str, stream_id: str, quality: str,
                   headers: dict = DEFAULT_HEADERS) -> list[int]:
    """Fetch the media playlist, return list of segment indices."""
    url = f"{cdn_base}/{stream_id}/{quality}/media.m3u8"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as r:
        playlist = r.read().decode()
    # CRLF-safe: \s* handles \r\n line endings (the spec default)
    return [int(s) for s in re.findall(r"^segment-(\d+)\.ts\s*$", playlist, re.MULTILINE)]


# ---------- Phase 3: download + decrypt + concat ----------
def _fetch_one(seg_id: int, cdn_base: str, stream_id: str, quality: str,
               headers: dict) -> tuple[int, bytes]:
    u = f"{cdn_base}/{stream_id}/{quality}/segment-{seg_id}.ts"
    req = urllib.request.Request(u, headers=headers)
    with urllib.request.urlopen(req) as r:
        return seg_id, r.read()


def download_and_decrypt(
    segments: list[int],
    key: bytes,
    output_path: str,
    cdn_base: str,
    stream_id: str,
    quality: str = DEFAULT_QUALITY,
    headers: dict = DEFAULT_HEADERS,
    concurrency: int = 24,
) -> int:
    """Concurrent download + AES-128-CBC decrypt + concat. Returns bytes written."""
    from Crypto.Cipher import AES

    print(f"Downloading + decrypting {len(segments)} segments "
          f"(concurrency={concurrency})...", file=sys.stderr)

    enc: dict[int, bytes] = {}
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futs = {pool.submit(_fetch_one, s, cdn_base, stream_id, quality, headers): s
                for s in segments}
        for fut in as_completed(futs):
            try:
                sid, data = fut.result()
                enc[sid] = data
            except Exception as e:
                print(f"  ERROR on segment {futs[fut]}: {e}", file=sys.stderr)
            if len(enc) % 200 == 0 or len(enc) == len(segments):
                mb = sum(len(b) for b in enc.values()) / 1024 / 1024
                print(f"  Downloaded {len(enc)}/{len(segments)} ({mb:.1f} MB)",
                      file=sys.stderr)

    written = 0
    last = segments[-1]
    with open(output_path, "wb") as out:
        for sid in sorted(enc.keys()):
            # HLS spec: default IV = media sequence number as 16-byte big-endian
            cipher = AES.new(key, AES.MODE_CBC, sid.to_bytes(16, "big"))
            dec = cipher.decrypt(enc[sid])
            if sid == last:
                pad = dec[-1]
                if 1 <= pad <= 16 and dec[-pad:] == bytes([pad]) * pad:
                    dec = dec[:-pad]
                    print(f"  Stripped {pad} bytes PKCS7 padding from last segment",
                          file=sys.stderr)
            out.write(dec)
            written += len(dec)
    print(f"Wrote {written/1024/1024:.1f} MB to {output_path} (raw, MPEG-TS container)",
          file=sys.stderr)
    return written


# ---------- Phase 4: remux MPEG-TS to true MP4 container ----------
def remux_to_mp4(ts_path: str) -> str:
    """Stream-copy the .ts output into a true .mp4 container with faststart.
    No re-encode, completes in seconds. Replaces the .ts with the .mp4.
    Returns the final .mp4 path."""
    src = Path(ts_path)
    tmp = src.with_suffix(".remux.mp4")
    r = subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(src), "-c", "copy", "-movflags", "+faststart",
        str(tmp),
    ], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  remux FAILED: {r.stderr.strip()}", file=sys.stderr)
        print(f"  Keeping MPEG-TS output at: {src}", file=sys.stderr)
        return str(src)
    final = src.with_suffix(".mp4")
    src.unlink()
    tmp.rename(final)
    print(f"  Remuxed to true MP4: {final}  "
          f"({final.stat().st_size/1024/1024:.1f} MB)", file=sys.stderr)
    return str(final)


# ---------- Orchestrator ----------
def main():
    # ---- EDIT THESE ----
    lms_url     = DEFAULT_LMS_URL
    username    = DEFAULT_USERNAME
    password    = DEFAULT_PASSWORD    # Or load from env / prompt
    video_title = DEFAULT_VIDEO_TITLE
    cdn         = DEFAULT_CDN
    stream_id   = DEFAULT_STREAM_ID
    output      = DEFAULT_OUTPUT
    # --------------------

    Path(output).parent.mkdir(parents=True, exist_ok=True)

    print("=== Phase 1: capture AES key ===", file=sys.stderr)
    key = asyncio.run(capture_key(lms_url, username, password, video_title))
    key_path = output + ".key.bin"
    Path(key_path).write_bytes(key)
    print(f"  Key: {len(key)} bytes -> {key_path}", file=sys.stderr)
    assert len(key) == 16, f"Expected 16-byte AES-128 key, got {len(key)}"

    print("=== Phase 2: fetch segment list ===", file=sys.stderr)
    segments = fetch_segments(cdn, stream_id, DEFAULT_QUALITY)
    print(f"  {len(segments)} segments", file=sys.stderr)

    # Write to .ts intermediate so the remux produces a .mp4 with the same base name
    intermediate = str(Path(output).with_suffix(".ts"))
    print("=== Phase 3: download + decrypt + concat ===", file=sys.stderr)
    download_and_decrypt(segments, key, intermediate, cdn, stream_id)

    print("=== Phase 4: remux to true MP4 ===", file=sys.stderr)
    final = remux_to_mp4(intermediate)

    print(f"\nDONE: {final}  ({Path(final).stat().st_size/1024/1024:.1f} MB)",
          file=sys.stderr)
    print("Verify: ffprobe -v error -show_format -show_streams " + final,
          file=sys.stderr)


if __name__ == "__main__":
    main()
