"""Download all PDF/file notes from a Synapse LMS chapter (account-aware, state-tracked)."""
import asyncio
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from account_lib import (
    ACCOUNTS_DIR, get_password, is_note_downloaded, list_accounts, load_state,
    record_note, save_state, state_path,
)
from playwright.async_api import async_playwright

LMS_BASE = "https://lms.synapsepg.org"
API_BASE = "https://api.synapsepg.org"
ASSETS_BASE = "https://assets.synapsepg.org"


def _is_account_name(s: str) -> bool:
    if not ACCOUNTS_DIR.exists():
        return False
    return (ACCOUNTS_DIR / f"{s}.creds").exists() and (ACCOUNTS_DIR / f"{s}.json").exists()


def get_account_from_argv() -> tuple[str, list[str]]:
    if len(sys.argv) < 2:
        print("Usage: download_notes.py [<account>] <chapter_id> [output_dir]", file=sys.stderr)
        print("  Default account: sagar", file=sys.stderr)
        print("  Registered accounts:", ", ".join(list_accounts()) or "(none)", file=sys.stderr)
        sys.exit(1)
    first = sys.argv[1]
    if _is_account_name(first):
        return first, sys.argv[2:]
    return "sagar", sys.argv[1:]


def sanitize(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


async def fetch_files(lecture_id: str, account: str):
    """Login + call /api/lecture/{id} to get fileContents."""
    state = load_state(account)
    username = state["username"]
    password = get_password(account)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(f"{LMS_BASE}/videos/{lecture_id}/lecture", wait_until="domcontentloaded", timeout=30000)
        if "/login" in page.url:
            await page.get_by_placeholder("Enter mobile number").fill(username)
            await page.get_by_placeholder("Type your password").fill(password)
            await page.get_by_role("button", name="Sign In").click()
            await page.wait_for_url(lambda url: "/login" not in url, timeout=30000)
        session_id = await page.evaluate("localStorage.getItem('sessionId')")
        await browser.close()

    result = json.loads(urllib.request.urlopen(urllib.request.Request(
        f"{API_BASE}/api/lecture/{lecture_id}",
        headers={
            "Accept": "application/json",
            "Authorization": session_id,
            "Referer": f"{LMS_BASE}/notes/{lecture_id}/lecture",
        },
    )).read())
    data = result.get("data", {})
    return data.get("fileContents", []), data.get("name")


def download_one(s3_key: str, dest: Path):
    url = f"{ASSETS_BASE}/{s3_key}"
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})) as r:
        dest.write_bytes(r.read())


async def main():
    account, rest = get_account_from_argv()
    if len(rest) < 1:
        print("Usage: download_notes.py [<account>] <chapter_id> [output_dir]", file=sys.stderr)
        sys.exit(1)
    chapter_id = rest[0]
    state = load_state(account)
    default_out = Path(state.get("output_dir", f"/mnt/tb/{account}")) / state.get("notes_subdir", "notes")
    out_dir = Path(rest[1]) if len(rest) > 1 else default_out
    out_dir.mkdir(parents=True, exist_ok=True)

    files, chapter_name = await fetch_files(chapter_id, account)
    print(f"Chapter: {chapter_name or chapter_id}", file=sys.stderr)
    print(f"Files:   {len(files)}", file=sys.stderr)

    downloaded = 0
    skipped = 0
    for f in files:
        file_id = f.get("_id")
        title = f.get("title", "untitled")
        s3_key = f.get("key", "")
        if not file_id or not s3_key:
            print(f"  SKIP (no id/key): {title}", file=sys.stderr)
            continue
        if is_note_downloaded(state, file_id):
            prev = state["downloaded_notes"][file_id]
            print(f"  ⏭  {prev['filename']}  (already on disk: {prev['size_bytes']/1024/1024:.1f} MB)", file=sys.stderr)
            skipped += 1
            continue
        ext = s3_key.rsplit(".", 1)[-1] if "." in s3_key else "bin"
        dest = out_dir / f"{sanitize(title)}.{ext}"
        try:
            download_one(s3_key, dest)
            size = dest.stat().st_size
            record_note(state,
                file_id=file_id,
                chapter_id=chapter_id,
                chapter_name=chapter_name,
                title=title,
                filename=dest.name,
                s3_key=s3_key,
                size_bytes=size,
            )
            save_state(account, state)
            print(f"  ✓ {dest.name}  ({size/1024/1024:.1f} MB)", file=sys.stderr)
            downloaded += 1
        except Exception as e:
            print(f"  ✗ {title}: {e}", file=sys.stderr)

    print(f"\nDownloaded: {downloaded}   Skipped (already had): {skipped}", file=sys.stderr)
    print(f"State: {state_path(account)}", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
