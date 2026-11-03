# Connecting Hermes Desktop App to a Remote Gateway

**Status:** The official docs page "Web Dashboard → Connecting Hermes Desktop to a remote backend" returns 404 (as of 2025). This reference captures the working pattern.

## Architecture

```
Windows Desktop App  ──(WebSocket + REST)──►  Remote Gateway (port 9119)
                                                      │
                                                      └──►  Dashboard UI (optional, port 9120)
```

The **Desktop app talks to the Gateway** (WebSocket at `/api/ws`, REST at `/api/...`), NOT the Dashboard. The Dashboard is a separate web UI on a different port.

## Configuration

### Option 1: Environment Variable (simplest)

```powershell
# PowerShell (run once, or add to Windows Environment Variables)
$env:HERMES_GATEWAY_URL = "https://your-domain.com:9119"
hermes desktop
```

### Option 2: Config File

`%USERPROFILE%\.hermes\config.yaml`:
```yaml
gateway:
  url: "https://your-domain.com:9119"
```

## The Auth Problem

The Desktop app **does not have a built-in UI for HTTP Basic Auth** on the gateway URL.

### Workarounds (ranked by practicality)

| Approach | How | Caveats |
|----------|-----|---------|
| **Embed creds in URL** | `https://user:pass@your-domain.com:9119` | Works but creds visible in process list / shell history |
| **Remove 401 from gateway port** | Keep 401 on dashboard (9120) only; restrict gateway via Tailscale / WireGuard / Cloudflare Tunnel / SSH bastion | **Recommended** — Basic Auth on WebSocket upgrades is flaky across proxies |
| **SSH tunnel** | `ssh -L 9119:localhost:9119 user@server` then `HERMES_GATEWAY_URL=http://localhost:9119` | Zero exposed ports, works with any auth on remote side |

## Recommended Pattern

```
Port 9119 (Gateway):  NO auth, exposed only via Tailscale/VPN/SSH tunnel
Port 9120 (Dashboard): Your nginx 401 auth is fine here — it's just a browser UI
Desktop App:          Connects via secure tunnel to 9119
```

## Quick Test

```powershell
$env:HERMES_GATEWAY_URL = "https://your-domain.com:9119"
hermes desktop
```

If it connects, you'll see remote sessions, skills, config — everything synced.

## Related

- `references/dashboard-tui-proxy-chat-troubleshooting.md` — debugging WebSocket issues through nginx
- `references/nas-setup-dr-sagar.md` — NAS/LAN exposure patterns
- `references/two-port-dashboard-pattern.md` — reverse proxy vs raw Hermes app