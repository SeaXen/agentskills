# Dashboard auth and API-server notes

Condensed notes from a NAS-style Hermes deployment.

## Key findings

### `--insecure` flag status (June 2026)

- **CLI `--help` says "DEPRECATED / NO-OP"** — this is misleading. The flag **still works**.
- Official docs confirm: `--insecure` allows binding to `0.0.0.0` without authentication.
- Use `--insecure` for LAN-accessible dashboards without auth.
- Two-dashboard setup is possible: one port with auth (official `basic_auth`), one without (`--insecure`).

### Auth behavior

- `basic_auth` in `config.yaml` only kicks in when binding to `0.0.0.0` (non-loopback)
- Localhost bind (`127.0.0.1`) requires no auth — ever
- `--insecure` flag allows `0.0.0.0` bind without auth (LAN accessible, no login)
- Without auth config AND without `--insecure`, dashboard refuses to bind to `0.0.0.0` and crashloops

### Two-dashboard setup (auth + no-auth)

Run two separate systemd services:

```ini
# /etc/systemd/system/hermes-dashboard.service — 9119 with auth
[Service]
ExecStart=/usr/local/bin/hermes dashboard --host 0.0.0.0 --port 9119 --skip-build --no-open

# /etc/systemd/system/hermes-dashboard-9120.service — 9120 no auth
[Service]
ExecStart=/usr/local/bin/hermes dashboard --host 0.0.0.0 --port 9120 --insecure --skip-build --no-open
```

**Cannot run `systemctl` or `hermes` commands from inside the gateway process** — it SIGTERM-propagates to children. Always use a separate SSH shell.

### Verification

```bash
# Auth port → 401
curl -s -o /dev/null -w "%{http_code}" http://192.168.0.222:9119/

# No-auth port → 200 (or 302 redirect → 200)
curl -sL -o /dev/null -w "%{http_code}" http://192.168.0.222:9120/
```

## API server auth

- Hermes API server supports `API_SERVER_KEY` authentication.
- Source inspection showed the gateway config path reading API-server enablement and auth primarily from environment variables:
  - `API_SERVER_ENABLED`
  - `API_SERVER_KEY`
  - `API_SERVER_PORT`
  - `API_SERVER_HOST`
- In this session, a user had `platforms.api_server.key` in `config.yaml`, but the running gateway still logged:
  - `No API key configured (API_SERVER_KEY / platforms.api_server.key). All requests will be accepted without authentication.`
- Practical fix: put `API_SERVER_KEY` in `~/.hermes/.env`, restart the gateway, then verify the warning disappears.

## Verification commands

```bash
hermes gateway status
journalctl --user -u hermes-gateway -n 40 --no-pager | grep -i 'api_server\|API key\|accepted without authentication'
hermes config path
```

## Discord side note from same deployment

When Discord slash commands worked but text messages did not:
- verify live config, not just remembered edits
- confirm `~/.hermes/config.yaml` under `discord:`
- confirm systemd unit uses the expected `HERMES_HOME`
- restart gateway after config changes
