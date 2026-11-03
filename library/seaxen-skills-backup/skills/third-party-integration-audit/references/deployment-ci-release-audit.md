# Deployment, CI, and Release Audit Checks

Use this when an audit spans Dockerfiles, Compose, installers, CI, tests, and release docs. Trace one fresh-install and one upgrade path end-to-end; syntax validation alone is not deployment verification.

## Fresh-install authentication

1. Start from no persisted data and no `.env`.
2. Identify how the first account or setup token is created.
3. Check the server's actual view of client identity. Through Docker port publishing, a host browser commonly appears as a bridge/gateway address, not `127.0.0.1`.
4. Verify the frontend can send any token required by the setup endpoint. Server support for a header is irrelevant if the UI always leaves it blank.
5. Test the documented quick start end-to-end.

A security restriction is still a release-blocking availability bug when it makes first-run setup impossible.

## Compose parity and healthchecks

Compare every variable in `.env.example` and the README with Compose `environment:`. Template values are not automatically passed into a container.

Render Compose with non-default sentinel values and inspect relevant fields. Check:

- application listen port versus healthcheck target
- login/recovery limits
- request/WebSocket limits
- bind and published addresses
- data paths and credentials

A configurable internal port plus a hardcoded healthcheck port creates a permanently unhealthy deployment.

## Test the deployed runtime

If hardening lives in Compose, CI should launch via Compose or reproduce every setting. Plain `docker run` can miss failures involving:

- dropped capabilities and `no-new-privileges`
- PID limits and init
- tmpfs/bind mounts
- persistence and permissions
- healthchecks and overlays

Probe a real capability, not only `/health` or `/auth/me`. For a terminal service: bootstrap/authenticate, create a terminal/tmux session, run a harmless command, and verify output.

## Installer ordering and secure defaults

For remote administration tools:

- default to loopback unless exposure is explicit
- configure firewall/TLS/reverse proxy before starting an all-interface listener
- a warning printed after service startup does not make the preceding bind safe
- assess service-user impact; a browser shell running as root is a remote-root control plane

## Upgrade and persisted-state precedence

Compare installer detection with application precedence. If persisted account/database state overrides environment credentials, the installer must inspect that state before generating or printing replacement credentials. Otherwise it may advertise a password the application never uses.

Also check dirty trees, tag/branch transitions, preserved `.env`, existing bind-mounted data, and legacy migrations.

## Documentation command verification

Resolve helper defaults in every supported mode. Container defaults such as `/data` often make host-mode instructions wrong. Verify that:

- quick starts establish usable auth
- helpers load the same `.env` and data path as the service
- custom service names are respected
- release examples do not pin superseded versions
- changelog/version text matches the intended tag

## Secret and supply-chain pass

- Scan tracked and newly added text; separately inspect changed screenshots/binary assets for sensitive UI data.
- Confirm `.env`, runtime state, recovery codes, sessions, archives, and backups are excluded from Git and Docker context.
- Flag mutable base-image tags and moving Action tags as reproducibility/supply-chain risks; prefer image digests and Action commit SHAs for releases.

## Severity guide

- **Critical:** unauthenticated command execution, real secret exposure, destructive upgrade/data loss.
- **High:** documented fresh install unusable; remote shell insecurely exposed by default; auth bootstrap impossible.
- **Medium:** healthcheck/config mismatch, ignored documented settings, misleading upgrade credentials, CI tests a materially weaker runtime.
- **Low:** reproducibility pinning, release housekeeping, minor documentation drift.
