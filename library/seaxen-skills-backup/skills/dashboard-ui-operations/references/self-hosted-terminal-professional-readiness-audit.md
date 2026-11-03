# Self-hosted terminal / operator UI professional-readiness audit

Use this when rating whether a browser terminal, admin console, or LAN dashboard is professional, production-ready, or safe for public exposure.

## Required evidence

### Runtime and core flows
- Confirm the real service user and unit/container state; a terminal running as root changes the entire risk model.
- Probe the live root page, auth status, health/system endpoint, and every critical workflow.
- For terminals, exercise create → write → read → rename → kill in an isolated data directory and tmux/socket namespace.
- Exercise file write/list/download/delete where present.
- Send malformed numeric/query/body inputs and require controlled 4xx responses; a disconnected request thread is a reliability failure.

### Security posture
- Inspect permissions and ownership of `.env`, password/account storage, and session-token files. Secret-bearing files should not be world-readable.
- Identify password hashing: raw SHA-256 is not a password KDF; require Argon2id, scrypt, bcrypt, or appropriately configured PBKDF2 with salts.
- Run a short invalid-login burst to verify throttling/rate limits rather than assuming they exist.
- Check maximum JSON body, upload, transcript/read, and WebSocket frame sizes.
- Check cookie flags, query-string bearer tokens, CORS policy, CSRF/origin handling, and security headers.
- Inspect Docker defaults: runtime user, capabilities, writable secret mounts, `no-new-privileges`, healthcheck, and whether “isolation” claims match compose reality.
- For host terminals, state plainly that credential/session compromise becomes command execution as the service user.

### UI and accessibility
- Score desktop and mobile separately. A good responsive login page does not prove the authenticated workspace is responsive.
- Capture the real authenticated workspace at a phone viewport and measure body/document scroll width; clipped dense toolbars are a concrete mobile failure.
- Count visible controls without associated `<label>`, `aria-label`, or `aria-labelledby`; placeholder-only forms are insufficient.
- Check browser console after navigation and major interactions.

### Reliability and performance
- Run syntax/build/config checks, but do not treat them as functional tests.
- Run a small concurrent read-only probe and report median and p95; single-request latency can hide a small listen backlog or serialized bottleneck.
- Inspect request-size handling, graceful shutdown, structured logs, health checks, and error boundaries.

### Repository and release hygiene
- Check for tests and CI explicitly.
- Compare release tag to `HEAD` (`git rev-list --count <tag>..HEAD`). A release may be valid while main has unreleased changes; report the drift.
- Verify README claims against actual service behavior, Docker mounts, authentication, and license state.

## Rating rule

Give context-specific verdicts when relevant:
- private/personal LAN use
- public open-source beta quality
- internet-exposed production readiness

Weight security, reliability, and automated testing more heavily than screenshots or README polish. Distinguish “professional-looking” from “professionally engineered” and “professionally hardened.”
