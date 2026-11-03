# Dashboard port topology: 9119 proxy vs 9120 raw app

Use this when Hermes dashboard appears down but another Hermes-looking dashboard is visible on a different port.

## Durable pattern
- Do not assume the active Hermes-branded page is the main dashboard.
- Verify the intended topology first.
- For Dr. Sagar's NAS-style setup, the expected pattern can be:
  - `9119` = main browser entrypoint via nginx reverse proxy
  - `9120` = raw Hermes dashboard app

## Failure mode seen
A systemd unit tried to run:
- `hermes dashboard --host 0.0.0.0 --port 9119 --skip-build --no-open`

On current Hermes builds this fails when no auth provider is registered, with the key message:
- `Refusing to bind dashboard to 0.0.0.0 — the auth gate engages on non-loopback binds, but no auth providers are registered.`

Implication:
- a direct public/LAN bind on the main dashboard port is not a safe default repair
- `--insecure` should not be assumed to restore old behavior on modern Hermes; it is deprecated/no-op for bypassing auth on non-loopback binds

## Better repair shape
Prefer restoring the split design:
1. raw Hermes dashboard service on an app port such as `9120`
2. nginx on `9119` proxying to `127.0.0.1:9120`
3. verify any auth companion files required by the nginx config (for example `.htpasswd`) before declaring the proxy healthy

## Operator checklist
- confirm the user's intended main dashboard port before touching services
- verify which process owns each relevant port
- separate nginx-proxy failure from raw-dashboard failure
- if an auth file is missing, say so explicitly
- do not confuse a custom dashboard on another port with the main Hermes dashboard
