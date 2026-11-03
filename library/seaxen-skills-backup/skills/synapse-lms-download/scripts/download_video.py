"""Download one video from a Synapse LMS lecture page (account-aware, state-tracked)."""
import asyncio
import os
import re
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Make sibling account_lib importable when running from skill/scripts dir
sys.path.insert(0, str(Path(__file__).resolve().parent))
from account_lib import (
    ACCOUNTS_DIR, account_dir, ensure_account, get_password, is_video_downloaded,
    load_state, record_video, save_state, state_path,
)
from Crypto.Cipher import AES
from playwright.async_api import async_playwright

LMS_BASE = "https://lms.synapsepg.org"
CDN = "https://jrgtfb2pnx.tenbytecdn.com"
HEADERS = {
    "Referer": "https://player.vidinfra.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
}

# CLI: download_video.py <account> <lecture_id> [video_index] [output_name]
# Or: download_video.py <lecture_id> ...   (uses default account "sagar")


def _is_account_name(s: str) -> bool:
    """True if s is the stem of a registered account (matching .creds file)."""
    if not ACCOUNTS_DIR.exists():
        return False
    return (ACCOUNTS_DIR / f"{s}.creds").exists() and (ACCOUNTS_DIR / f"{s}.json").exists()


def get_account_from_argv() -> tuple[str, list[str]]:
    """First arg is treated as account name if it's a known account; else treat as lecture_id."""
    if len(sys.argv) < 2:
        print("Usage: download_video.py [<account>] <lecture_id> [video_index] [output_name]", file=sys.stderr)
        print("  Default account: sagar", file=sys.stderr)
        print("  Registered accounts:", ", ".join(list_accounts()) or "(none)", file=sys.stderr)
        sys.exit(1)
    first = sys.argv[1]
    if _is_account_name(first):
        return first, sys.argv[2:]
    # Fallback: default account
    return "sagar", sys.argv[1:]


def sanitize(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


async def fetch_video(lecture_id: str, video_index: int, account: str):
    """Login (using account creds), navigate, click Nth card, capture key + stream info."""
    username = os.environ.get("SYNAPSE_USER")  # optional override
    if not username:
        # read from state
        state = load_state(account)
        username = state["username"]
    password = get_password(account)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()

        captured = {"key": None}
        async def on_resp(r):
            if "kms.vidinfra.com/v1/keys" in r.url:
                try:
                    captured["key"] = await r.body()
                except Exception:
                    pass
        page.on("response", lambda r: asyncio.create_task(on_resp(r)))

        await page.goto(f"{LMS_BASE}/videos/{lecture_id}/lecture", wait_until="domcontentloaded", timeout=30000)
        if "/login" in page.url:
            await page.get_by_placeholder("Enter mobile number").fill(username)
            await page.get_by_placeholder("Type your password").fill(password)
            await page.get_by_role("button", name="Sign In").click()
            await page.wait_for_url(lambda url: "/login" not in url, timeout=30000)
            await page.goto(f"{LMS_BASE}/videos/{lecture_id}/lecture", wait_until="domcontentloaded", timeout=30000)

        cards = page.locator(".student-video-card")
        n = await cards.count()
        titles = []
        for i in range(n):
            titles.append((await cards.nth(i).inner_text()).strip().split("\n")[0])
        print(f"  Found {n} video(s):", file=sys.stderr)
        for i, t in enumerate(titles):
            print(f"    [{i}] {t}{'  <--' if i == video_index else ''}", file=sys.stderr)
        if video_index >= n:
            print(f"ERROR: index {video_index} out of range", file=sys.stderr)
            await browser.close()
            return None
        target_title = titles[video_index]

        await cards.nth(video_index).click()
        for _ in range(20):
            await page.wait_for_timeout(1000)
            if captured["key"]:
                break
        if not captured["key"]:
            print("ERROR: key not captured", file=sys.stderr)
            await browser.close()
            return None

        iframe_url = await page.evaluate("document.querySelector('iframe[title=\"Video Player\"]')?.src || ''")
        await browser.close()
        if not iframe_url:
            return None
        m = re.match(r"https://player\.vidinfra\.com/stream/([^/]+)/default/([^/]+)", iframe_url)
        if not m:
            print(f"ERROR: bad iframe URL: {iframe_url}", file=sys.stderr)
            return None
        return {
            "title": target_title,
            "iframe_content_id": m.group(1),
            "stream_id": m.group(2),
            "key": captured["key"],
        }


def fetch_segments(stream_id, quality="720p"):
    url = f"{CDN}/{stream_id}/{quality}/media.m3u8"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        playlist = resp.read().decode()
    return [int(s) for s in re.findall(r"^segment-(\d+)\.ts\s*$", playlist, re.MULTILINE)]


def _dl(seg_id, stream_id, quality):
    import time
    import urllib.error
    url = f"{CDN}/{stream_id}/{quality}/segment-{seg_id}.ts"
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, headers=HEADERS), timeout=30
            ) as r:
                return seg_id, r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise
            last_err = e
        except Exception as e:
            last_err = e
        if attempt < 2:
            time.sleep(1)
    raise last_err


def download_and_decrypt(segments, stream_id, key, out_path, quality="720p", concurrency=24):
    print(f"  Downloading {len(segments)} segments (concurrency={concurrency})...", file=sys.stderr)
    encrypted = {}
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futs = {pool.submit(_dl, sid, stream_id, quality): sid for sid in segments}
        for i, fut in enumerate(as_completed(futs)):
            try:
                sid, data = fut.result()
                encrypted[sid] = data
            except Exception as e:
                print(f"    ERROR seg {futs[fut]}: {e}", file=sys.stderr)
            if (i + 1) % 200 == 0 or i == len(segments) - 1:
                mb = sum(len(b) for b in encrypted.values()) / 1024 / 1024
                print(f"    Downloaded {i+1}/{len(segments)} ({mb:.1f} MB)", file=sys.stderr)
    print("  Decrypting + writing...", file=sys.stderr)
    last_seg = max(encrypted.keys())
    written = 0
    with open(out_path, "wb") as out:
        for i, seg_id in enumerate(sorted(encrypted.keys())):
            iv = seg_id.to_bytes(16, "big")
            plaintext = AES.new(key, AES.MODE_CBC, iv).decrypt(encrypted[seg_id])
            if seg_id == last_seg:
                pad = plaintext[-1]
                if 1 <= pad <= 16 and plaintext[-pad:] == bytes([pad]) * pad:
                    plaintext = plaintext[:-pad]
            out.write(plaintext)
            written += len(plaintext)
    return written


def probe_duration(path):
    try:
        out = subprocess.check_output([
            "ffprobe", "-v", "error", "-of", "compact=p=0:nk=1",
            "-show_entries", "format=duration", str(path),
        ], text=True).strip()
        return float(out)
    except Exception:
        return None


def remux(in_path):
    out_tmp = in_path.with_suffix(".remux.mp4")
    r = subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(in_path), "-c", "copy", "-movflags", "+faststart", str(out_tmp),
    ], capture_output=True, text=True)
    if r.returncode != 0:
        return False
    in_path.unlink()
    out_tmp.rename(in_path)
    return True


async def main():
    account, rest = get_account_from_argv()
    if len(rest) < 1:
        print("Usage: download_video.py [<account>] <lecture_id> [video_index] [output_name]", file=sys.stderr)
        sys.exit(1)
    lecture_id = rest[0]
    video_index = int(rest[1]) if len(rest) > 1 else 0
    out_name_override = rest[2] if len(rest) > 2 else None

    # Load account state
    state = load_state(account)
    out_dir = Path(state.get("output_dir", f"/mnt/tb/{account}"))
    out_dir.mkdir(parents=True, exist_ok=True)

    info = await fetch_video(lecture_id, video_index, account)
    if not info:
        sys.exit(1)

    # Skip if already downloaded
    if is_video_downloaded(state, info["stream_id"]):
        prev = state["downloaded_videos"][info["stream_id"]]
        print(f"⏭  Already downloaded: {prev['filename']} ({prev['size_bytes']/1024/1024:.1f} MB on {prev['downloaded_at']})", file=sys.stderr)
        print(f"   Delete it from state to re-download, or rm the file.", file=sys.stderr)
        return

    out_name = out_name_override or f"{sanitize(info['title'])}.mp4"
    if not out_name.endswith(".mp4"):
        out_name += ".mp4"
    final_path = out_dir / out_name
    tmp_path = out_dir / f".{out_name}.ts.tmp"

    print(f"\nTitle:    {info['title']}", file=sys.stderr)
    print(f"Stream:   {info['stream_id']}", file=sys.stderr)
    print(f"Output:   {final_path}", file=sys.stderr)

    segments = fetch_segments(info["stream_id"])
    print(f"Segments: {len(segments)}", file=sys.stderr)
    if not segments:
        print("ERROR: no segments", file=sys.stderr)
        sys.exit(1)

    download_and_decrypt(segments, info["stream_id"], info["key"], tmp_path)
    if not remux(tmp_path):
        print(f"  Remux failed; final is MPEG-TS at {tmp_path}", file=sys.stderr)
        final_path = tmp_path
    else:
        print(f"  Remuxed to MP4", file=sys.stderr)
        if tmp_path.exists() and tmp_path != final_path:
            if final_path.exists():
                final_path.unlink()
            tmp_path.rename(final_path)

    size = final_path.stat().st_size
    duration = probe_duration(final_path)
    print(f"\nDONE: {final_path}", file=sys.stderr)
    print(f"Size: {size/1024/1024:.1f} MB", file=sys.stderr)

    # Update state
    record_video(state,
        stream_id=info["stream_id"],
        chapter_id=lecture_id,
        chapter_name=None,  # could fetch if needed
        title=info["title"],
        filename=final_path.name,
        size_bytes=size,
        duration_s=duration,
    )
    save_state(account, state)
    print(f"State updated: {state_path(account)}", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
