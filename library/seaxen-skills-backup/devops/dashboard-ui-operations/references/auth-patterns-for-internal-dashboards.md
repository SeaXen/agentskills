# Auth Patterns for Internal Dashboards

## HTTP Basic Auth is browser-hostile for dashboards

The browser's native Basic Auth prompt (the `WWW-Authenticate: Basic` popup):
- Re-asks on EVERY page refresh
- Re-asks on IP/device change
- Re-asks after browser restart (no session persistence)
- Has no "remember me" option in most browsers
- Cannot be styled or customized
- Blocks all AJAX/fetch calls with 401 until credentials are re-entered

**User feedback:** "this type of auth annoying ask every time refresh"

## When to skip auth entirely

For internal dashboards on a private LAN (not exposed to internet):
- Nothing sensitive to protect (analytics, monitoring, status)
- User explicitly says "nothing to hide or secure"
- Network-level security (VPN, firewall) already restricts access

**Decision rule:** If the dashboard is LAN-only and the user doesn't ask for auth, don't add it. If you add it and the user complains, remove it immediately.

## If auth IS needed

Use session-based login (cookie/JWT), NOT HTTP Basic Auth:
- Login page with form → set session cookie → redirect to dashboard
- Session cookie persists across refreshes
- Logout button clears session
- Middleware checks session cookie, not Authorization header

For FastAPI:
```python
from fastapi import Request
from starlette.middleware.sessions import SessionMiddleware

app.add_middleware(SessionMiddleware, secret_key="...")

@app.post("/login")
async def login(request: Request):
    # validate credentials
    request.session["user"] = "admin"
    return RedirectResponse("/", status_code=302)

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path in ("/login", "/api/healthz", "/static/"):
        return await call_next(request)
    if not request.session.get("user"):
        return RedirectResponse("/login")
    return await call_next(request)
```
