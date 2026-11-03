# Static web root and privileged API audit

Use this checklist when rating or exposing a self-hosted dashboard that serves static files and administrative APIs from one Python/Node process.

## Critical failure pattern

A dashboard can protect `/api/*` correctly and still leak everything if its static server serves the repository or working directory. Python `SimpleHTTPRequestHandler` is especially dangerous when the process starts inside the project directory: dotfiles, source, runtime config, backups, and Git metadata may all be reachable outside the API auth gate.

Do not infer safety from `/api/auth/status`. Probe the static surface separately.

## Required read-only probes

Test status/content type without printing secret bodies:

- `/seadash-config.json`, `/config.json`, `/.env`
- `/server.py`, `/app.py`, `/package.json`
- `/.git/HEAD`, `/.git/config`
- `/backups/`, `/backup/`, directory indexes
- likely database/log paths

A `200`, redirect to a file, or directory listing is a critical finding. Authentication middleware limited to `/api/` does not protect these paths.

Also verify:

1. Listener scope: loopback, LAN IP, or `0.0.0.0`.
2. Public route reachability and whether Cloudflare Access/reverse-proxy auth actually challenges requests.
3. Effective privilege of the service user.
4. Unauthenticated POST capabilities: config replacement, Docker actions, prune, backup restore, service restart, tunnel restart, reboot.
5. CORS, CSRF/origin checks, body limits, rate limits, and security headers.
6. Config/backup file permissions and whether API responses return credential-bearing config.

Never invoke destructive actions during an audit. Establish reachability and authorization from code plus harmless status probes.

## Rating rule

A publicly reachable, unauthenticated dashboard with root-level Docker/system actions is not production-ready regardless of visual polish. Cap public professional-readiness at about 2–4/10 until contained. Report a separate private-LAN/design score so good UI work is not conflated with security.

If the static root exposes config/source/Git/backups, rate security at critical severity even when current credential fields happen to be empty: future credentials and internal topology will leak automatically.

## Remediation order

1. Contain immediately: remove the public route or require Cloudflare Access.
2. Replace repository-root serving with an explicit static allowlist (`index.html`, manifest, service worker, favicon, assets only).
3. Deny dotfiles, source, config, backups, logs, and directory listing before auth logic.
4. Require authorization for every privileged API; separate read-only and admin capabilities.
5. Bind narrowly and run under a dedicated, hardened service user where feasible.
6. Move secrets to environment/secret storage, set config permissions to `0600`, and redact config API output.
7. Add origin/CSRF checks, restricted CORS, body/schema limits, secure cookies, rate limiting, security headers, atomic config writes, and strict backup path containment.
8. Add regression tests proving sensitive static paths return 403/404 and privileged POSTs return 401/403 when unauthenticated.

## Audit-reporting pitfall

Do not give a blended 8/10 because design and performance are strong. One unauthenticated public root-action path is a release-blocking defect. Lead with it, revise any earlier rating explicitly if discovered later, and distinguish “professional-looking” from “professional production-grade.”

## Dual-trust access pattern: LAN-open, public fail-closed

For personal dashboards where the owner explicitly wants passwordless LAN access but also has a public reverse-proxy hostname, do not force one global auth mode onto both surfaces.

A practical default is:

- classify `localhost`, loopback, RFC1918/private IPs, and approved `.local` hosts as trusted-local;
- classify DNS hostnames and forwarded public hosts as public;
- preserve passwordless access only for trusted-local requests;
- require a valid session for public-host requests;
- if public credentials are not configured, return `403/503` rather than silently treating auth as disabled;
- use `X-Forwarded-Host` only from a trusted reverse proxy, or configure an explicit public-host allowlist;
- keep `/api/health` minimal and public only when a reverse proxy needs it.

This preserves the user's low-friction LAN workflow while preventing an accidental Cloudflare route from converting “auth disabled” into “root admin API open to the Internet.” It is containment, not a substitute for Cloudflare Access or proper application authentication.

## Regression-test pattern

Before implementing hardening, write failing tests for pure security helpers and then integration-test the real handler:

1. Static allowlist rejects source, runtime config, `.git`, backup directories, tests, and dependency manifests.
2. Required frontend files still return `200`.
3. Public hostname without configured auth fails closed.
4. Private/loopback hostname retains the intended LAN policy.
5. Wildcard CORS is absent and security headers are present.
6. Cross-origin POST is rejected.
7. Oversized/non-object JSON is rejected before body processing.
8. Backup names require the generated basename format.
9. Config writes are atomic and result in mode `0600`.
10. Client config output redacts secret-bearing fields without erasing stored secrets on later saves.

Use harmless requests only. Never test reboot, prune, restore, or container stop against the live service.

## Safe deployment boundary

Code hardening and live service hardening are separate changes. A systemd rollout may migrate config to `/var/lib/<app>`, install a unit or drop-in under `/etc/systemd/system`, change filesystem visibility, and restart the service. Treat that as an explicit deployment boundary:

- prepare and test code first on an alternate/local instance;
- show the exact unit, migration paths, and restart scope;
- request one focused confirmation for the system-level rollout;
- do not bundle unrelated cleanup or destructive operations into that confirmation;
- if confirmation is denied or times out, stop at the verified code state and report precisely what remains unapplied;
- never claim the hardened unit or migrated config is live until `systemctl show`, file permissions, API probes, and sensitive-path probes verify it.

For atomic config writes under `ProtectSystem=strict`, place runtime data under a dedicated writable state directory such as `/var/lib/<app>` instead of granting write access to the source tree.
