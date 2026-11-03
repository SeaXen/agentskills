#!/usr/bin/env python3
"""Inject a captured Synapse localStorage session into a Playwright context.

Use this when you want to download Synapse content WITHOUT triggering a new
login (which would kick the user out of their live browser session).

Setup:
    1. User opens https://lms.synapsepg.org in their browser and logs in.
    2. F12 → Console → run:
           localStorage.getItem('student')
           localStorage.getItem('sessionId')
    3. User pastes both values.
    4. Save to /root/synapse_dl/accounts/<account>.session.json as JSON.

Usage:
    python3 synapse_session_inject.py <account> <target_url>

Example:
    python3 synapse_session_inject.py sagar https://lms.synapsepg.org/videos/abc123/lecture

If the page renders the dashboard (not /login), injection succeeded.
The browser stays open until you Ctrl-C — useful for inspecting or running
further Playwright commands in the same context.
"""
import asyncio
import json
import sys
from pathlib import Path
from playwright.async_api import async_playwright

LMS_ORIGIN = "https://lms.synapsepg.org/"
SESSION_FILE_TEMPLATE = "/root/synapse_dl/accounts/{account}.session.json"


async def open_with_session(account: str, target_url: str):
    session_path = Path(SESSION_FILE_TEMPLATE.format(account=account))
    if not session_path.exists():
        print(f"Session file not found: {session_path}", file=sys.stderr)
        print(f"See scripts/synapse_session_inject.py header for capture steps.", file=sys.stderr)
        sys.exit(1)

    session = json.loads(session_path.read_text())
    if "student" not in session or "sessionId" not in session:
        print(f"Session file missing 'student' or 'sessionId' key.", file=sys.stderr)
        sys.exit(1)

    captured_at = session.get("captured_at", "unknown")
    print(f"Using session captured at: {captured_at}", file=sys.stderr)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=['--no-sandbox'])
        ctx = await browser.new_context()
        page = await ctx.new_page()

        # Step 1: navigate to LMS origin so localStorage is origin-scoped correctly
        await page.goto(LMS_ORIGIN, wait_until='domcontentloaded')
        # Step 2: inject both keys BEFORE the React app reads them
        await page.evaluate(f"""
            localStorage.setItem('student', {json.dumps(session['student'])});
            localStorage.setItem('sessionId', {json.dumps(session['sessionId'])});
        """)
        # Step 3: navigate to the real target — React reads localStorage on init
        await page.goto(target_url, wait_until='domcontentloaded')

        if '/login' in page.url:
            print("✗ Session injection failed — page redirected to /login.", file=sys.stderr)
            print("  Causes: wrong values, expired session, or wrong origin.", file=sys.stderr)
            print("  Fix: re-capture both keys from a fresh login.", file=sys.stderr)
            await browser.close()
            sys.exit(2)

        print(f"✓ Session injected, dashboard loaded: {page.url}", file=sys.stderr)
        print("Browser open. Ctrl-C to close.", file=sys.stderr)
        try:
            # Keep browser open for inspection or further scripted interaction
            await asyncio.Event().wait()
        except KeyboardInterrupt:
            pass
        finally:
            await browser.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    asyncio.run(open_with_session(sys.argv[1], sys.argv[2]))
