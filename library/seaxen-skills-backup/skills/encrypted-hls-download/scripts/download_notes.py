#!/usr/bin/env python3
"""Download all PDF / file notes from a Synapse LMS chapter.

Tested on Synapse Medical Academy (lms.synapsepg.org). The video side is
covered by `scripts/hls_decrypt.py` — this script handles the OTHER half:
the notes/PDFs that live on the same LMS under a separate URL tab.

Why this exists as a separate script:
- Videos need Playwright + HLS + AES-128 decrypt + remux (heavy).
- PDFs are just static files behind a Bearer-auth API call (light).
- Different tab URL, different API, different file format. Trying to bolt
  one onto the other makes both harder to read.

Usage:
    /root/.venvs/synapse-env/bin/python scripts/download_notes.py <chapter_id> [output_dir]

Defaults:
    output_dir = /mnt/tb/synapse_26/notes
    credentials read from /root/synapse_dl/.creds (first line = password, one line)

If .creds doesn't exist, the script will prompt for username + password and
write them to .creds (chmod 600) for re-use.
"""
import asyncio
import json
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ---- Platform-specific constants (edit for your platform) ----
LMS_BASE      = "https://lms.synapsepg.org"
API_BASE      = "https://api.synapsepg.org"
ASSETS_BASE   = "https://assets.synapsepg.org"
CREDS_FILE    = Path("/root/synapse_dl/.creds")
DEFAULT_OUT   = Path("/mnt/tb/synapse_26/notes")

# Same modern desktop UA used in the video script — some CDNs block default agents
DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
)


def sanitize(name: str) -> str:
    """Make `name` safe to use as a filename on Linux/Windows/macOS."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")


def load_or_prompt_credentials() -> tuple[str, str]:
    """Read username + password from CREDS_FILE if it exists, else prompt and write.

    File format: line 1 = username, line 2 = password. Chmod 600 after write.
    """
    if CREDS_FILE.exists():
        lines = CREDS_FILE.read_text().splitlines()
        if len(lines) >= 2:
            return lines[0].strip(), lines[1].strip()
    # Prompt
    print("Credentials not found at", CREDS_FILE, file=sys.stderr)
    user = input("Username (mobile number): ").strip()
    pwd = input("Password: ").strip()
    CREDS_FILE.parent.mkdir(parents=True, exist_ok=True)
    CREDS_FILE.write_text(f"{user}\n{pwd}\n")
    os.chmod(CREDS_FILE, 0o600)
    print(f"Saved credentials to {CREDS_FILE} (chmod 600).", file=sys.stderr)
    return user, pwd


async def fetch_session_id(lecture_id: str) -> str:
    """Open a headless browser, log in, return localStorage.sessionId.

    The sessionId is the Bearer token used for /api/lecture/{id} calls.
    Session is in localStorage, NOT a real cookie — don't fish for cookies.
    """
    from playwright.async_api import async_playwright

    username, password = load_or_prompt_credentials()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(user_agent=DEFAULT_UA)
        page = await context.new_page()

        # Navigate (redirects to /login if not authed)
        await page.goto(f"{LMS_BASE}/videos/{lecture_id}/lecture",
                        wait_until="domcontentloaded", timeout=30000)
        if "/login" in page.url:
            # Adapt selectors to your LMS
            await page.get_by_placeholder("Enter mobile number").fill(username)
            await page.get_by_placeholder("Type your password").fill(password)
            await page.get_by_role("button", name="Sign In").click()
            await page.wait_for_url(lambda u: "/login" not in u, timeout=30000)

        session_id = await page.evaluate("localStorage.getItem('sessionId')")
        await browser.close()

    if not session_id:
        raise RuntimeError("Login succeeded but localStorage.sessionId is empty.")
    # JSON.stringify wraps the value in quotes; strip them
    return session_id.strip('"').strip()


def fetch_file_list(lecture_id: str, session_id: str) -> list[dict]:
    """GET /api/lecture/{id} and return the fileContents list."""
    url = f"{API_BASE}/api/lecture/{lecture_id}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "Authorization": session_id,
        "Referer": f"{LMS_BASE}/notes/{lecture_id}/lecture",
        "User-Agent": DEFAULT_UA,
    })
    with urllib.request.urlopen(req) as r:
        body = r.read().decode()
    data = json.loads(body)
    files = data.get("data", {}).get("fileContents", [])
    if not files:
        print(f"  (no fileContents in this chapter — might be video-only)",
              file=sys.stderr)
    return files


def _download_one(file_meta: dict, out_dir: Path) -> tuple[str, str, int | str]:
    """Download a single file. Returns (title, status, size_or_error)."""
    title = file_meta.get("title", "untitled")
    key = file_meta.get("key", "")
    if not key:
        return title, "skip", "no key"
    ext = key.rsplit(".", 1)[-1] if "." in key else "bin"
    dest = out_dir / f"{sanitize(title)}.{ext}"
    url = f"{ASSETS_BASE}/{key}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": DEFAULT_UA})
        with urllib.request.urlopen(req) as r:
            dest.write_bytes(r.read())
        return title, "ok", dest.stat().st_size
    except Exception as e:
        return title, "fail", f"{type(e).__name__}: {e}"


async def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    lecture_id = sys.argv[1]
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"=== Login + capture sessionId ===", file=sys.stderr)
    session_id = await fetch_session_id(lecture_id)
    print(f"  Bearer token: {session_id[:40]}...", file=sys.stderr)

    print(f"=== Fetch file list for chapter {lecture_id} ===", file=sys.stderr)
    files = fetch_file_list(lecture_id, session_id)
    print(f"  Found {len(files)} file(s).", file=sys.stderr)
    for f in files:
        print(f"    - {f.get('title', '?')}  [{f.get('key', '?')}]",
              file=sys.stderr)

    if not files:
        sys.exit(0)

    print(f"=== Downloading to {out_dir} (12 workers) ===", file=sys.stderr)
    results = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = {pool.submit(_download_one, f, out_dir): f for f in files}
        for i, fut in enumerate(as_completed(futs), 1):
            title, status, info = fut.result()
            results.append((title, status, info))
            if status == "ok":
                print(f"  [{i}/{len(files)}] ✓ {title}  ({info/1024:.1f} KB)",
                      file=sys.stderr)
            else:
                print(f"  [{i}/{len(files)}] ✗ {title}  {status}: {info}",
                      file=sys.stderr)

    # Summary
    ok = sum(1 for r in results if r[1] == "ok")
    total_bytes = sum(r[2] for r in results if r[1] == "ok")
    print(f"\nDONE: {ok}/{len(results)} files in {out_dir} "
          f"({total_bytes/1024/1024:.1f} MB total)", file=sys.stderr)


if __name__ == "__main__":
    asyncio.run(main())
