# Lightweight Admin Dashboard Production Hardening

Use this runbook for dependency-light dashboards that combine static UI, host/Docker monitoring, mutable configuration, backups, scanners, and privileged actions.

## Threat model first

Treat the dashboard as an administrative control plane, not a normal static site. Docker-socket access is effectively host-admin access even when the process is not root.

Before adding more UI features, verify:

- the listener and every public reverse-proxy route
- authentication status from both LAN and public hostnames
- HTTP status only (not contents) for config, source, `.git`, backups, dotfiles, tests, and arbitrary paths
- every state-changing/API route and its authorization boundary
- runtime user, writable paths, systemd sandbox, and secret file modes

A polished UI does not offset an exposed repository root or unauthenticated privileged API.

## Static surface

Never inherit repository-root serving behavior from a convenience HTTP handler. Route APIs first, then serve only an explicit allowlist such as:

- `/`, `/index.html`
- `/manifest.json`, `/service-worker.js`, `/favicon.ico`
- approved flat `/assets/<name>` files

Return 404 for source, config, backups, `.git`, tests, dotfiles, directory listings, and unknown paths. Prove the deny list with live-handler tests.

## Public fail-closed boundary

If public access is optional, public hostnames must fail closed when credentials are absent. Private/LAN behavior may remain separate if that is an explicit product decision.

When behind Cloudflare or another tunnel/reverse proxy:

- never infer the security boundary from `Host`, `X-Forwarded-Host`, `X-Forwarded-For`, or provider headers alone; they are client-controlled unless the direct peer is trusted
- classify a non-private direct peer as public regardless of the supplied host headers
- ignore every forwarded/provider header unless the direct peer matches an explicit `TRUSTED_PROXIES` IP/CIDR allowlist (empty by default)
- only then use the forwarded host for public/private classification and forwarded client IP for rate limiting
- provide an explicit universal-auth policy such as `REQUIRE_AUTH=1` for deployments that should lock LAN and public access alike
- make the bind address explicit: loopback by default for development, deliberate `0.0.0.0` only for LAN deployments
- keep raw port exposure blocked at the firewall

Regression-test the exact bypass shape: a public `Host` plus a private `X-Forwarded-Host` from an untrusted peer must still be denied. Use the edge access product as defense in depth, not as a substitute for application authorization.

## Authentication and browser controls

- Store a PBKDF2/Argon2/scrypt password hash, not a plaintext password.
- Use cryptographically random session tokens with expiry and logout invalidation.
- Cookies: `HttpOnly`, `SameSite=Strict`, `Secure` on HTTPS/public proxy requests.
- Rate-limit failed logins by trusted client identity, bound the rate-limit map, and cap concurrent request threads before expensive password hashing.
- Reject cross-origin state-changing requests; do not emit wildcard CORS.
- Reject `Transfer-Encoding`, missing/duplicate/invalid `Content-Length`, non-object JSON, and request bodies over a fixed limit before reading them. Close the connection on ambiguous framing to prevent request desynchronization.
- Centralize CSP, frame denial, nosniff, referrer, permissions, and HSTS headers.
- If CSP permits external scripts, remove inline JavaScript and omit `unsafe-inline` from `script-src`.

## Configuration and secrets

Keep mutable state outside the repository, preferably under a systemd `StateDirectory` such as `/var/lib/<app>`.

For config writes:

1. Validate root and important field types, item counts, identifier lengths, and URL lengths.
2. Preserve server-side secret fields when a redacted browser config is saved.
3. Write a same-filesystem temporary file with mode `0600`.
4. Flush and fsync the file.
5. `os.replace` it atomically.
6. chmod the final file and fsync the parent directory.

Browser config responses should redact webhook tokens, bot tokens, chat IDs, private routes, and similar credentials. A boolean such as `credentialsConfigured` can preserve UI state without exposing values. If corrupt config is preserved for recovery, fingerprint the source (mtime/size or hash) and copy each distinct corrupt version only once; otherwise every read can create another recovery file.

## Backup restore: never extract into the app tree

For a configuration-only ZIP restore:

- accept only a strict generated basename
- resolve and confirm the path stays inside the backup directory
- reject symlinks
- require exactly one expected member
- cap declared and actual decompressed size
- read the member into bounded memory; do not call `extract`/`extractall`
- decode JSON, validate schema, and create a rollback backup
- persist through the normal atomic config writer

This also avoids the common deployment bug where restore writes to the source directory while production reads config from `/var/lib`.

## SSRF and scanner policy

Home-server dashboards intentionally probe LAN/loopback services, so a blanket private-IP block may break the product. Instead:

- allow only HTTP/HTTPS
- reject embedded credentials
- resolve DNS before requests
- block cloud metadata, link-local, multicast, unspecified, and reserved targets
- validate every redirect destination
- use short timeouts, bounded workers, bounded results, and bounded caches
- document whether RFC1918 and loopback are intentionally allowed

## Privileged actions

- Use explicit action allowlists.
- Validate Docker container names against live inventory before invoking the CLI.
- Keep prune, delete, and host reboot disabled by default behind a separate opt-in.
- Allowlist readable systemd units and Docker log targets.
- Require confirmation for destructive actions and never exercise them during routine live verification.

## Rootless systemd pattern

Prefer a dedicated system user with:

- `NoNewPrivileges=true`
- empty `CapabilityBoundingSet`/`AmbientCapabilities`
- `ProtectSystem=strict`, private temp/devices, protected proc/kernel/control groups
- restricted namespaces/address families
- `StateDirectory` and narrowly scoped writable paths
- memory/task limits and restrictive umask

If Docker operations are required, add the service user to the Docker group and document that this remains effectively privileged.

Useful pitfalls:

- `ProtectSystem=strict` plus atomic replacement cannot write config in the read-only source tree; move state to `StateDirectory` rather than making the repository writable.
- Include `AF_NETLINK` when host/network discovery or Docker tooling needs it; omitting it can break local address detection.
- An unprivileged service cannot `systemctl restart` itself. With `Restart=on-failure`, return the API response and then exit non-zero from a delayed worker.
- Thread-per-request servers and short-lived thread pools can leave many glibc allocator arenas behind. Set `MALLOC_ARENA_MAX=2` in the unit and verify memory after repeated dashboard refreshes, not only immediately after startup.

## Verification gate

Automate at least:

- static allow/deny paths
- public fail-closed behavior, direct-peer classification, universal-auth mode, and untrusted forwarded-header spoofing
- unauthenticated privileged routes
- security headers and absence of wildcard CORS
- cross-origin POST rejection
- chunked, missing/duplicate `Content-Length`, oversized, and non-object JSON
- config schema and atomic/private writes
- secret redaction/preservation
- login hash and rate limits
- backup traversal/member/size/schema handling
- SSRF targets and redirect validation
- Docker/log allowlists

Then verify live:

- compile/syntax checks and full test suite
- service restart, health, dashboard, config round trip, and safe backup creation
- no new journal tracebacks
- desktop/mobile browser smoke, modal focus/Escape restoration, scanner opt-in, zero console errors
- sensitive-path HTTP denial
- process user, file modes, systemd security score, and memory after repeated refreshes
- staged secret scan, clean Git tree, pushed SHA equality, and CI workflow actions pinned to immutable commit SHAs

If hosted CI cannot execute because of account policy, keep the workflow committed, run the identical commands locally, and report the external limitation without claiming CI passed.

Report literal measurements and remaining boundaries. Do not label the application 10/10 when CI, public authentication setup, privileged Docker access, or maintainability limits remain.