# OmniRoute grok-web Cookie Setup

## Status: BROKEN (as of 2026-06-29)
- Issue [#3063](https://github.com/diegosouzapw/OmniRoute/issues/3063) — validation rejects valid cookies
- Issue [#5350](https://github.com/diegosouzapw/OmniRoute/issues/5350) — same, opened by user

## How grok-web works
grok-web is a **cookie-based** provider — it wraps Grok Web's session auth instead of using an API key.
Requires: `sso` + `sso-rw` cookies from a logged-in grok.com browser session.

## Steps (when it's working)
1. Sign in to grok.com in browser
2. Open DevTools → Network tab
3. Click any request to grok.com
4. Find `Cookie:` in Request Headers
5. Copy the **full Cookie header value** (without `Cookie:` prefix)
6. OmniRoute Dashboard → Providers → Grok Web (Subscription)
7. Paste into session cookie field
8. Check connection

## Cookie format
Expected: `sso=<value>; sso-rw=<value>`
With space after semicolon. May also need `cf_clearance` and other cookies.

## Known issues
- grok-web validation is broken — rejects valid cookies with 403 anti-bot or "Invalid SSO cookie"
- Also needs `cf_clearance` from Cloudflare — expires and breaks validation
- Cookie-based auth is inherently flaky; API key (`xAI` provider) is the stable alternative
- OAuth provider for SuperGrok subscriptions is requested (issue #2760) but not yet implemented

## Alternative: xAI API key
Add as regular `xAI` provider in OmniRoute. Models: `grok-3`, `grok-4`, `grok-code-fast`.
Does NOT use subscription (SuperGrok) — uses API credits instead.
