# Hermes Desktop Remote Connection

## How it works

The Hermes Desktop app (macOS/Windows/Linux) connects to a **remote `hermes dashboard` process**, not the gateway directly.

**Connection flow:**
1. REST handshake: `GET /api/status` on the dashboard URL
2. WebSocket: live chat/events stream

## Server-side setup

The `hermes dashboard` must be running and reachable on the remote machine:

```bash
hermes dashboard --host 0.0.0.0 --port 9119 --skip-build --no-open
```

**With auth (recommended for public/LAN access):**
```yaml
# config.yaml
dashboard:
  basic_auth:
    username: sagar
    password_hash: scrypt$...  # generate with hash_password()
    session_ttl_seconds: 86400  # 24 hours; 0 = 12h default
```

**Without auth (LAN only, or behind a tunnel):**
```bash
hermes dashboard --host 0.0.0.0 --port 9120 --insecure --skip-build --no-open
```

Keep the dashboard running via systemd.

## Client-side (Desktop app on another PC)

1. Install: `hermes desktop`
2. On first launch, choose "Connect to remote backend"
3. Enter URL: `http://192.168.0.222:9119` (or your CF tunnel URL)
4. Enter credentials if auth is enabled

## For PCs outside the LAN

Use **Tailscale** or **Cloudflare Tunnel**:
- Tailscale: bind dashboard to `--host <tailscale-ip>`, connect via `http://<tailscale-ip>:9119`
- Cloudflare Tunnel: tunnel port 9119, connect via your CF URL

## Session TTL

- `session_ttl_seconds: 0` → 12 hours (default)
- `session_ttl_seconds: 86400` → 24 hours  
- `session_ttl_seconds: 604800` → 7 days

After TTL expires, user must re-enter password.

## Cloudflare Tunnel behavior

- New IP address: works fine, CF Tunnel doesn't care about IP
- New device/browser: same, just get the hermes login prompt
- No additional login needed beyond hermes basic_auth

## Important notes

- Desktop app is a **thin client** — all AI processing happens on the server
- Sessions are **shared** across CLI, TUI, dashboard, and desktop
- Keep `hermes gateway` running separately for messaging channels (Telegram/Discord)
- The dashboard (port 9119) and gateway (port 8642) are **separate processes**

## Verified

- 2026-06-24: Server on `192.168.0.222:9119` with `basic_auth`, session TTL 24h
- Desktop app connects successfully from LAN with username/password
- CF Tunnel on 9119 → works from new IP/device with same credentials
