# Universal Host Terminal and Public Auth Pattern

Use this reference for standalone browser terminal/dashboard apps when the user asks for a **universal terminal**, public access, or a login page instead of browser Basic Auth.

## Core interpretation

For this user, **universal terminal** means a shell that can run real host commands by default:

```text
Browser → host shell
```

A terminal running inside the app Docker container is not universal unless explicitly scoped/labeled:

```text
Browser → Rexterm/container shell
```

Do not paper over this distinction with one-by-one bind mounts. Mounting a few host binaries such as `hermes` can be a useful bridge, but it is not true universal behavior.

## Recommended modes

Expose terminal modes clearly:

1. **Host terminal** — default universal mode; runs commands on the real machine.
2. **Container terminal** — optional; execs into a selected Docker/container context.
3. **Hermes terminal** — optional; starts Hermes-specific shell/context.

Label the active mode in the UI so the operator knows where commands execute.

## Public auth default

When the user asks for public access or an auth page:

- prefer a real in-page login screen, not browser Basic Auth popup
- give the operator an explicit way to create/change their own username and password; do not leave them dependent on a generated admin password only
- support first-run setup when no account exists, plus an authenticated account/settings screen for later changes
- store username/password server-side via `.env` or a server account store
- prefer password hash over raw password, e.g. SHA256 for a simple local app or a stronger KDF when dependencies allow
- issue an HttpOnly SameSite session cookie after login
- do not embed shared API tokens into frontend JS
- WebSocket auth should work via the same session cookie where possible
- keep a logout button
- clear old test sessions/tokens after verification

Good simple implementation pattern:

- if no account store exists, `GET /` shows a `Create account` screen
- `POST /api/auth/setup` creates the first account server-side and starts a session
- `POST /api/auth/account` changes username/password for the current authenticated session
- optional CLI helper such as `scripts/set-auth.sh` prompts for username/password, writes the server account store, clears active sessions, and restarts the host service
- store generated recovery credentials in a private ignored data file only if needed for operator recovery, not as the primary UX

Good simple env shape:

```env
REXTERM_AUTH_REQUIRED=1
REXTERM_AUTH_USERNAME=admin
REXTERM_AUTH_PASSWORD_SHA256=<hash>
REXTERM_AUTH_SESSION_TTL=604800
REXTERM_SHARED_TOKEN=<random legacy/internal token>
```

## Verification checklist

Minimum verification before claiming success:

```text
GET /                      -> 200 and shows login/setup page when unauthenticated
GET /api/health unauth     -> 401
POST /api/auth/setup       -> 200 when no account exists, or blocked once an account exists
POST /api/auth/login       -> 200 and sets cookie
GET /api/health authed     -> 200
POST /api/auth/account     -> 200 for authenticated username/password change
GET /api/terminal/sessions -> 200 after login
browser login              -> terminal UI appears
browser terminal command   -> real command output appears
```

Host-vs-Docker verification before claiming “universal host terminal”:

```text
systemctl status <host-terminal-unit>     -> active running host service
systemctl is-enabled <host-terminal-unit> -> enabled if reboot persistence was requested
ss -ltnp | grep <port>                    -> listener owned by host python/server process, not docker-proxy/container
Docker container check                    -> no container owns the public terminal port unless intentionally in container mode
ExecStart / run script                    -> launches `python3 .../server.py` or equivalent host process, not `docker compose exec`/container shell
```

For public readiness, also verify:

- HTTPS/tunnel path loads the same page
- WebSocket upgrades work through the public route
- login cookie survives refresh
- logout returns to login page
- direct raw port exposure is avoided unless intentionally firewalled

## Security posture

A browser-accessible host terminal is privileged remote shell access. Treat it like SSH in a browser.

Safe default for public use:

```text
Cloudflare Tunnel / HTTPS reverse proxy
→ Rexterm login page
→ host terminal
```

Avoid exposing a raw HTTP terminal port directly to the internet.

If host-shell mode is added, preserve explicit warnings in implementation notes and/or UI: commands run as the service user and can read or destroy host data available to that user.
