# User Preference: No Auth on Internal Dashboards

**Date:** 2026-07-01
**Context:** AceRoute analytics dashboard (port 8866, LAN-only)

## The preference

The user explicitly rejects HTTP Basic Auth (and any browser-prompt-based auth) on internal/self-hosted dashboards on LAN.

**User's exact words:** "do not need auth, remove it. this type of auth annoying ask every time refresh, if need make like only pass ask when enter like login page, and not ask for restart or ip/device change etc, or otherwise remove it, cause here nothing to hide or secure"

## Rules

1. **Do not add auth** to internal dashboards (ports on 192.168.x.x / localhost) unless the user explicitly asks for it.
2. If auth IS needed later, use a **login page with session cookies** — NOT HTTP Basic Auth (which has no session persistence and re-prompts on every refresh, IP change, or device switch).
3. For public-facing dashboards, ask first.

## Why HTTP Basic Auth is bad for dashboards

- Browser shows a native dialog on EVERY page load/refresh
- No "remember me" that survives IP changes or browser restarts reliably
- No logout button
- No session persistence across tabs
- Annoying on mobile (keyboard popup on every navigation)
- Credentials sent in base64 on every request (no session token pattern)

## What to use instead (if auth is ever needed)

- FastAPI: `starlette.middleware.sessions.SessionMiddleware` + cookie-based login form
- Or: reverse proxy auth (nginx `auth_request`, Cloudflare Access, etc.)
- Or: simple token in URL query param / header for API-only access
