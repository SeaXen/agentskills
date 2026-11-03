## Verify pattern
- Prefer live verification of reachable routes rather than assuming defaults.
- Distinguish direct Hermes port from any reverse proxy / auth layer.
- If a proxy returns `401`, explain that it is the protected entry and that direct Hermes may still be reachable on its own port.

## Answer shape
- Direct Hermes dashboard: `http://<host-or-ip>:<port>/`
- Chat: `http://<host-or-ip>:<port>/chat`
- If reverse proxy exists, also list proxy URL(s) and whether auth is required.

## Session example
Observed working pattern:
- Hermes bound to `0.0.0.0:9120`

Operational takeaway:
- Tell the user to use the raw Hermes port for immediate LAN access.
- Mention the proxy URL separately as the authenticated/protected entry.

## Portal OAuth Registration (manual workaround)
See `references/portal-dashboard-oauth-registration.md` for the pattern when `hermes dashboard register` fails but portal website registration exists.
