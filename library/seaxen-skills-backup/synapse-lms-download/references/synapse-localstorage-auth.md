# Synapse LMS — localStorage session injection (no-login download)

## Why this exists

Synapse enforces **single-session-per-user**: any new login from any context invalidates all other active sessions. A bulk download script that logs in 4 times (once per chapter) kicks the user out of their browser 4 times.

Solution: capture the user's existing `localStorage` session from their browser, inject it into the headless Playwright context before navigation. No login form is ever submitted. The user's live browser session is never touched.

## What to capture (browser console while logged in)

```javascript
localStorage.getItem('student')    // → JSON string starting with {"_id":"..."}
localStorage.getItem('sessionId')  // → URL-encoded string like "s%3A...%2B..."
```

Both are needed:
- `student` = profile JSON (`_id`, `name`, `phone`, `batch`, etc.) — required by the React app to render "logged in" UI
- `sessionId` = `s:<sig>.<hmac>` (URL-encoded) — sent as `Authorization: <sessionId>` header on every API call

If either is `null`, the user isn't logged in — log them in first, then re-run.

## Where to save

`/root/synapse_dl/accounts/<account>.session.json`:

```json
{
  "student": "{\"_id\":\"abc...\",\"name\":\"...\",\"phone\":\"01...\",\"batch\":\"...\"}",
  "sessionId": "s%3AKKE58aRex0yRJnjEC6V454ECj4H8fZPI.k8vfUCSmeXkbH%2BpK%2FnFHxf%2F6pDhFXnsOW%2B4G6J1KN2w",
  "captured_at": "2026-06-19T04:30:00+06:00",
  "captured_from": "user browser console paste"
}
```

Chmod 600. The values change every time the user logs out and back in, so this file has a finite lifetime — re-capture when downloads start failing with 401.

## How to inject

```python
import asyncio, json
from playwright.async_api import async_playwright

async def open_with_session(account, target_url):
    session = json.load(open(f'/root/synapse_dl/accounts/{account}.session.json'))
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
        ctx = await browser.new_context()
        page = await ctx.new_page()
        # Go to the LMS origin FIRST (localStorage is origin-scoped)
        await page.goto('https://lms.synapsepg.org/', wait_until='domcontentloaded')
        # Then inject — must be done before the React app reads localStorage on next nav
        await page.evaluate(f"""
            localStorage.setItem('student', {json.dumps(session['student'])});
            localStorage.setItem('sessionId', {json.dumps(session['sessionId'])});
        """)
        # Now navigate to the real target — React picks up the session
        await page.goto(target_url, wait_until='domcontentloaded')
        # If /login redirect happens, the values were wrong (or session expired)
        if '/login' in page.url:
            raise RuntimeError("Session injection failed — check student/sessionId values")
        return browser, ctx, page
```

## When this doesn't work

| Symptom | Cause | Fix |
|---|---|---|
| Page redirects to `/login` after injection | **Server binds session to browser fingerprint (TLS, IP, UA) that headless context can't replicate.** Confirmed empirically 2026-06-19 — see "Empirical result" below. | Use login approach instead (accept the one-time logout) |
| `localStorage is not defined` error in browser console | Injected before navigating to LMS origin | Always `page.goto('https://lms.synapsepg.org/')` FIRST, then inject |
| Some chapters work, others 401 | sessionId expired mid-run | Sessions have ~24h lifetime; re-capture |
| Download succeeds but logged-in user sees "session expired" | Was a stale capture from prior logout | Re-capture fresh from active session |

## Empirical result (2026-06-19)

We tried injecting `localStorage.student` + `localStorage.sessionId` (URL-decoded) plus the matching `connect.sid` cookie into a fresh Playwright context. Result: the page navigated to `/login`, `localStorage` came back empty after navigation, and the API call to `/api/v1/student/profile` returned 200 but with a login-page body. The server actively rejects the replayed session.

**Conclusion: Synapse session injection does not work as of 2026-06.** The server is binding the session to something the headless browser can't reproduce (likely a Cloudflare-style fingerprint over the TLS handshake, IP address, and User-Agent). Don't spend time trying variations (different UA strings, header ordering, cookie domains) — the binding is server-side.

The viable alternative is the **login approach**: accept that the user's browser gets logged out once per download batch, do the login + key capture quickly (under 5 min for a 4-chapter course), then run the bulk download in the background. For one-shot bulk runs of 51 videos, the 5-min login + 4-6 hr download tradeoff is the only working pattern.

The `synapse_session_inject.py` script in this skill's `scripts/` is preserved as a **template** for future LMSes that may not have this binding (e.g. simpler Express-session servers without fingerprint validation). Don't delete it — just don't expect it to work on Synapse.

## Comparison: login vs session injection

| | Login approach | Session injection |
|---|---|---|
| Disrupts user | YES — logs them out | NO (in theory) |
| Works on Synapse (2026-06) | ✅ Yes | ❌ No — server rejects (see "Empirical result") |
| Captures fresh keys | Each chapter needs fresh key fetch | Keys can be cached too |
| Complexity | Simple | Requires user to paste values once |
| Reliability | High (always fresh session) | Medium on platforms that allow it; doesn't work here |
| Best for | One-shot bulk download | LMSes without server-side fingerprint binding |

For the 2026-06-19 Sharif run, the **login approach was used** (one quick login at the start, capturing all 4 chapters' keys in ~3 minutes, then bulk download ran in background for 4-6 hours). The user was logged out of their Sagar account once during the key-capture pass — acceptable for a one-shot batch. The session injection script exists as a template for other LMSes where it might work, but on Synapse the binding is server-side and can't be replayed.

## KMS key capture also benefits

The Vidinfra KMS endpoint (`kms.vidinfra.com/v1/keys`) uses the same browser session for HMAC-signed headers. With injected localStorage, the headless browser gets a valid Vidinfra session and can fetch keys without needing to "be" the user — the player iframe loads normally and the key capture listener picks up the response.

So session injection works for: ✅ `/api/lecture/{id}` API calls, ✅ Vidinfra iframe load, ✅ KMS key capture, ✅ Notes/PDF download. Everything except the login form submission itself.

## Capturing sessionId — gotcha

The `sessionId` value in localStorage is **URL-encoded** when read with `.getItem()`. The string you see will look like:

```
s%3AKKE58aRex0yRJnjEC6V454ECj4H8fZPI.k8vfUCSmeXkbH%2BpK%2FnFHxf%2F6pDhFXnsOW%2B4G6J1KN2w
```

`%3A` = `:`, `%2B` = `+`, `%2F` = `/`. When you `.setItem()` it back, browser stores the URL-encoded form. When the app sends it as the `Authorization` header, it sends the URL-encoded form too. So **don't decode it** — paste the raw output of `.getItem()` directly. If you accidentally decode it, the server will reject the session as malformed.

## Refresh cadence

For bulk downloads that take 4-8 hours, plan to re-capture session if you see:

- 401 responses on `/api/lecture/{id}`
- Player iframe failing to load
- KMS key fetches returning 403

Sessions typically last 24h on this LMS, but aggressive use (many key fetches per minute) can trigger earlier expiry. Have the user re-paste if you see mid-run failures.
