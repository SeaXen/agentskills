#!/usr/bin/env python3
"""Download sagar notes for a chapter via /usr/bin/chromium (no playwright-bundled)."""
import asyncio, sys, json, os, re
from pathlib import Path
import urllib.request, urllib.error
sys.path.insert(0, "/root/synapse_dl")
from account_lib import load_state, save_state, get_password, record_note

async def fetch_files(chapter_id, account):
    """Return list of dicts {_id, title, key/url, chapter_name} via scripted login."""
    from playwright.async_api import async_playwright
    state = load_state(account)
    uname = state["username"]; pwd = get_password(account)
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path="/usr/bin/chromium",
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        ctx = await browser.new_context()
        page = await ctx.new_page()
        await page.goto("https://lms.synapsepg.org/", wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(1500)
        await page.get_by_placeholder("Enter mobile number").fill(uname)
        await page.get_by_placeholder("Type your password").fill(pwd)
        await page.get_by_role("button", name="Sign In").click()
        for _ in range(30):
            await page.wait_for_timeout(500)
            sid = await page.evaluate("localStorage.getItem('sessionId')")
            if sid: break
        if not sid:
            print("Login failed"); await browser.close(); return [], ""
        # also get the chapter name from localStorage.allLectures
        ch_name = await page.evaluate(
            """(cid) => {
                const a = JSON.parse(localStorage.getItem('allLectures') || '[]');
                const m = a.find(x => x._id === cid);
                return m ? m.name : '';
            }""",
            chapter_id,
        )
        res = await page.evaluate(
            """async (args) => {
                const r = await fetch(`https://api.synapsepg.org/api/lecture/${args.cid}`, {
                    headers: { 'Authorization': args.sid, 'Accept': 'application/json' }
                });
                return r.ok ? await r.json() : { error: r.status };
            }""",
            {"cid": chapter_id, "sid": sid},
        )
        await browser.close()
    if not isinstance(res, dict) or res.get("error"):
        print(f"API err: {res}"); return [], ch_name
    data = res.get("data") or {}
    files = data.get("fileContents") or []
    if not ch_name:
        ch_name = data.get("name") or data.get("chapterName") or ""
    return files, ch_name

def _sanitize(name):
    cleaned = re.sub(r"[^A-Za-z0-9._ -]+", " ", name).strip().rstrip(".")
    return re.sub(r"\s+", " ", cleaned)

def download_note_file(file_obj, out_path: Path):
    """Download PDF/PPTX via the public S3 URL — no auth needed."""
    url = file_obj.get("url") or ("https://assets.synapsepg.org/" + file_obj["key"]) if file_obj.get("key") else None
    if not url:
        return False, "no url"
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            data = r.read()
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"
    if not data or len(data) < 200:
        return False, f"too small ({len(data)} bytes)"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    return True, len(data)

async def main():
    if len(sys.argv) < 2:
        print("usage: download_sagar_notes.py <chapter_id> [chapter_id2 ...]"); sys.exit(1)
    state = load_state("sagar")
    have = set(state.get("downloaded_notes", {}).keys())
    out_root = Path(state["output_dir"])
    notes_subdir = state.get("notes_subdir", "notes")

    grand_ok, grand_skip, grand_fail = 0, 0, 0
    for chapter_id in sys.argv[1:]:
        print(f"\n=== chapter {chapter_id} ===")
        try:
            files, ch_name = await fetch_files(chapter_id, "sagar")
        except Exception as e:
            print(f"fetch err: {e!r}"); continue
        if not files:
            print("(no files)"); continue
        print(f"chapter_name: {ch_name!r}  total files: {len(files)}")
        # Output dir: state.output_dir / notes_subdir / sanitize(ch_name)
        sub = _sanitize(ch_name) or chapter_id
        chap_dir = out_root / notes_subdir / sub
        for f in files:
            fid = f.get("_id") or f.get("id")
            title = (f.get("title") or "").strip() or f.get("name") or f"untitled_{fid}"
            if not fid: continue
            if fid in have:
                grand_skip += 1
                print(f"  ✓ already have: {title[:55]} ({fid})")
                continue
            base = _sanitize(title)
            ext = (f.get("extension") or "").lower() or ".pdf"
            if not base.lower().endswith(ext):
                base = base + ext
            out_path = chap_dir / base
            ok, info = download_note_file(f, out_path)
            if ok:
                record_note(state,
                           file_id=fid,
                           chapter_id=chapter_id,
                           chapter_name=ch_name,
                           title=title,
                           filename=out_path.name,
                           s3_key=f.get("key", ""),
                           size_bytes=info)
                save_state("sagar", state)
                grand_ok += 1
                have.add(fid)
                print(f"  ✓ {title[:55]}  {info/1024:.0f} KB")
            else:
                grand_fail += 1
                print(f"  ✗ {title[:55]}: {info}")
    print(f"\n=== SAGAR NOTES DONE: new={grand_ok}  skipped={grand_skip}  failed={grand_fail} ===")

asyncio.run(main())
