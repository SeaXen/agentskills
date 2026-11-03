"""Sync ALL courses for an account: list new chapters, download all missing videos and notes.

Usage:
  download_all.py <account>           # sync all courses/chapters
  download_all.py <account> --dry-run # just list what would be downloaded
  download_all.py <account> --videos-only
  download_all.py <account> --notes-only
"""
import asyncio
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from account_lib import (
    ACCOUNTS_DIR, get_password, is_note_downloaded, is_video_downloaded,
    list_accounts, load_state, record_note, record_video, save_state, state_path,
)
from playwright.async_api import async_playwright

LMS_BASE = "https://lms.synapsepg.org"
API_BASE = "https://api.synapsepg.org"
ASSETS_BASE = "https://assets.synapsepg.org"
CDN = "https://jrgtfb2pnx.tenbytecdn.com"
HEADERS = {
    "Referer": "https://player.vidinfra.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
}


def sanitize(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


async def login_and_get_session(account: str) -> tuple[str, str, dict]:
    """Returns (username, sessionId, browser context ref to be closed)."""
    state = load_state(account)
    username = state["username"]
    password = get_password(account)
    # We need a single browser context that we keep alive to reuse
    # Caller is responsible for closing
    return username, password, state


async def fetch_lecture_meta(lecture_id: str, session_id: str) -> dict:
    return json.loads(urllib.request.urlopen(urllib.request.Request(
        f"{API_BASE}/api/lecture/{lecture_id}",
        headers={
            "Accept": "application/json",
            "Authorization": session_id,
            "Referer": f"{LMS_BASE}/notes/{lecture_id}/lecture",
        },
    )).read()).get("data", {})


async def fetch_all_lectures_for_account(account: str) -> list[dict]:
    """Login, then iterate over localStorage.allLectures to find every chapter."""
    username, password, state = await login_and_get_session(account)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(f"{LMS_BASE}/", wait_until="domcontentloaded", timeout=30000)
        if "/login" in page.url:
            await page.get_by_placeholder("Enter mobile number").fill(username)
            await page.get_by_placeholder("Type your password").fill(password)
            await page.get_by_role("button", name="Sign In").click()
            await page.wait_for_url(lambda url: "/login" not in url, timeout=30000)
            await page.goto(f"{LMS_BASE}/", wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(2000)
        # Pull allLectures from localStorage
        lectures_json = await page.evaluate("localStorage.getItem('allLectures') || '[]'")
        all_lectures = json.loads(lectures_json)
        await browser.close()
    return all_lectures


async def get_video_info_for_chapter(lecture_id: str, account: str):
    """Open the lecture page, click each card, capture stream info + key for each."""
    state = load_state(account)
    username = state["username"]
    password = get_password(account)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()

        results = []
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
        for i in range(n):
            captured["key"] = None
            title = (await cards.nth(i).inner_text()).strip().split("\n")[0]
            await cards.nth(i).click()
            for _ in range(15):
                await page.wait_for_timeout(1000)
                if captured["key"]:
                    break
            iframe_url = await page.evaluate("document.querySelector('iframe[title=\"Video Player\"]')?.src || ''")
            if not iframe_url:
                print(f"    [{i}] {title}: no iframe, skip", file=sys.stderr)
                continue
            m = re.match(r"https://player\.vidinfra\.com/stream/([^/]+)/default/([^/]+)", iframe_url)
            if not m:
                continue
            stream_id = m.group(2)
            results.append({
                "video_index": i,
                "title": title,
                "stream_id": stream_id,
                "key": captured["key"],
            })
            # Close modal for next click
            close_btn = page.locator('button[aria-label="Close"]').first
            if await close_btn.count() > 0:
                try:
                    await close_btn.click(timeout=2000)
                    await page.wait_for_timeout(500)
                except Exception:
                    pass
        await browser.close()
    return results


def fetch_segments(stream_id, quality="720p"):
    url = f"{CDN}/{stream_id}/{quality}/media.m3u8"
    with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS)) as r:
        playlist = r.read().decode()
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


def download_video_segments(segments, stream_id, key, out_path, concurrency=24):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from Crypto.Cipher import AES
    encrypted = {}
    failures = []
    total = len(segments)
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futs = {pool.submit(_dl, sid, stream_id, "720p"): sid for sid in segments}
        for i, fut in enumerate(as_completed(futs)):
            try:
                sid, data = fut.result()
                encrypted[sid] = data
            except Exception as e:
                sid = futs[fut]
                failures.append(sid)
                print(f"      ERR seg {sid}: {e}", file=sys.stderr)
            done = i + 1
            if done % 200 == 0 or done == total:
                mb = sum(len(b) for b in encrypted.values()) / 1024 / 1024
                pct = 100.0 * done / total
                print(
                    f"      {done}/{total} segments ({mb:.1f} MB, {pct:.1f}%)  failures={len(failures)}",
                    file=sys.stderr,
                )
    if not encrypted:
        raise RuntimeError("no segments downloaded")
    if failures:
        print(
            f"      ⚠ {len(failures)}/{total} segments failed; output may have a short gap",
            file=sys.stderr,
        )
    last_seg = max(encrypted.keys())
    written = 0
    with open(out_path, "wb") as out:
        for seg_id in sorted(encrypted.keys()):
            iv = seg_id.to_bytes(16, "big")
            plain = AES.new(key, AES.MODE_CBC, iv).decrypt(encrypted[seg_id])
            if seg_id == last_seg:
                pad = plain[-1]
                if 1 <= pad <= 16 and plain[-pad:] == bytes([pad]) * pad:
                    plain = plain[:-pad]
            out.write(plain)
            written += len(plain)
    return written


def remux(path):
    out_tmp = path.with_suffix(".remux.mp4")
    r = subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(path), "-c", "copy", "-movflags", "+faststart", str(out_tmp),
    ], capture_output=True, text=True)
    if r.returncode != 0:
        return False
    path.unlink()
    out_tmp.rename(path)
    return True


def probe_duration(path):
    try:
        out = subprocess.check_output([
            "ffprobe", "-v", "error", "-of", "compact=p=0:nk=1",
            "-show_entries", "format=duration", str(path),
        ], text=True).strip()
        return float(out)
    except Exception:
        return None


def download_note_file(s3_key: str, dest: Path):
    url = f"{ASSETS_BASE}/{s3_key}"
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})) as r:
        dest.write_bytes(r.read())


async def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    account = sys.argv[1]
    args = sys.argv[2:]
    dry_run = "--dry-run" in args
    videos_only = "--videos-only" in args
    notes_only = "--notes-only" in args

    state = load_state(account)
    out_dir = Path(state.get("output_dir", f"/mnt/tb/{account}"))
    out_dir.mkdir(parents=True, exist_ok=True)
    notes_dir = out_dir / state.get("notes_subdir", "notes")
    notes_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== Synapse LMS sync: account={account} ===", file=sys.stderr)
    print(f"Output: {out_dir}", file=sys.stderr)
    print(f"Current state: {len(state['downloaded_videos'])} videos, {len(state['downloaded_notes'])} notes", file=sys.stderr)

    # Step 1: fetch all chapters from localStorage
    print("\nStep 1: fetching all chapters...", file=sys.stderr)
    chapters = await fetch_all_lectures_for_account(account)
    print(f"Found {len(chapters)} chapters in account:", file=sys.stderr)
    for c in chapters:
        n_v = len(c.get("videoContents") or [])
        n_f = len(c.get("fileContents") or [])
        marker = ""
        if n_v == 0 and n_f == 0:
            marker = " (empty)"
        print(f"  {c['_id']}  {c['name']!r}  videos={n_v}  files={n_f}{marker}", file=sys.stderr)

    # Step 2: for each chapter with videoContents, fetch live video list and download missing
    if not notes_only:
        print("\nStep 2: syncing videos per chapter...", file=sys.stderr)
        for c in chapters:
            if not c.get("videoContents"):
                continue
            print(f"\n  Chapter: {c['name']} ({c['_id']})", file=sys.stderr)
            try:
                videos = await get_video_info_for_chapter(c["_id"], account)
            except Exception as e:
                print(f"    ERROR listing videos: {e}", file=sys.stderr)
                continue
            for v in videos:
                if is_video_downloaded(state, v["stream_id"]):
                    print(f"    ⏭  [{v['video_index']}] {v['title']}: already downloaded", file=sys.stderr)
                    continue
                if dry_run:
                    print(f"    → [{v['video_index']}] {v['title']}: would download (stream {v['stream_id'][:8]}...)", file=sys.stderr)
                    continue
                print(f"    ↓ [{v['video_index']}] {v['title']}...", file=sys.stderr)
                try:
                    segments = fetch_segments(v["stream_id"])
                    out_name = f"{sanitize(v['title'])}.mp4"
                    final_path = out_dir / out_name
                    tmp_path = out_dir / f".{out_name}.ts.tmp"
                    download_video_segments(segments, v["stream_id"], v["key"], tmp_path)
                    if not remux(tmp_path):
                        raise RuntimeError("ffmpeg remux failed")
                    if tmp_path.exists() and tmp_path != final_path:
                        if final_path.exists():
                            final_path.unlink()
                        tmp_path.rename(final_path)
                    size = final_path.stat().st_size
                    duration = probe_duration(final_path)
                    record_video(state,
                        stream_id=v["stream_id"],
                        chapter_id=c["_id"],
                        chapter_name=c["name"],
                        title=v["title"],
                        filename=final_path.name,
                        size_bytes=size,
                        duration_s=duration,
                    )
                    save_state(account, state)
                    print(f"      ✓ {out_name} ({size/1024/1024:.1f} MB)", file=sys.stderr)
                except Exception as e:
                    print(f"      ✗ {v['title']}: {e}", file=sys.stderr)

    # Step 3: for each chapter with fileContents, download missing
    if not videos_only:
        print("\nStep 3: syncing notes per chapter...", file=sys.stderr)
        from download_notes import fetch_files as fetch_notes_files
        for c in chapters:
            if not c.get("fileContents"):
                continue
            print(f"\n  Chapter: {c['name']} ({c['_id']})", file=sys.stderr)
            try:
                files, _ = await fetch_notes_files(c["_id"], account)
            except Exception as e:
                print(f"    ERROR listing files: {e}", file=sys.stderr)
                continue
            for f in files:
                file_id = f.get("_id")
                title = f.get("title", "untitled")
                s3_key = f.get("key", "")
                if not file_id or not s3_key:
                    continue
                if is_note_downloaded(state, file_id):
                    print(f"    ⏭  {title}: already downloaded", file=sys.stderr)
                    continue
                if dry_run:
                    print(f"    → {title}: would download", file=sys.stderr)
                    continue
                ext = s3_key.rsplit(".", 1)[-1] if "." in s3_key else "bin"
                dest = notes_dir / f"{sanitize(title)}.{ext}"
                try:
                    download_note_file(s3_key, dest)
                    size = dest.stat().st_size
                    record_note(state,
                        file_id=file_id,
                        chapter_id=c["_id"],
                        chapter_name=c["name"],
                        title=title,
                        filename=dest.name,
                        s3_key=s3_key,
                        size_bytes=size,
                    )
                    save_state(account, state)
                    print(f"    ✓ {dest.name} ({size/1024/1024:.1f} MB)", file=sys.stderr)
                except Exception as e:
                    print(f"    ✗ {title}: {e}", file=sys.stderr)

    # Final summary
    total = sum(v["size_bytes"] for v in state["downloaded_videos"].values()) + sum(v["size_bytes"] for v in state["downloaded_notes"].values())
    print(f"\n=== Sync complete ===", file=sys.stderr)
    print(f"Videos: {len(state['downloaded_videos'])}  Notes: {len(state['downloaded_notes'])}", file=sys.stderr)
    print(f"Total: {total/1024/1024/1024:.2f} GB", file=sys.stderr)
    print(f"State: {state_path(account)}", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
