# Termix Docker Deployment Reference

## Context
Dr. Sagar wanted to run Termix (self-hosted SSH/remote desktop management) in Docker on port 30001 with Cloudflare Tunnel, and connect the Windows desktop app to it.

## Correct Docker Image
**`ghcr.io/lukegus/termix:latest`** — NOT `ghcr.io/termix-ssh/termix:latest` (private/denied) or `lukegus/termix:latest` (doesn't exist).

## Working Docker Compose
```yaml
services:
  termix:
    image: ghcr.io/lukegus/termix:latest
    container_name: termix
    restart: unless-stopped
    ports:
      - "30001:8080"     # host:30001 → container:8080 (Termix default internal port)
    volumes:
      - ./data:/app/data
    environment:
      PORT: "8080"
    networks:
      - termix-net

networks:
  termix-net:
    driver: bridge
```

## Key Details
- Termix internal port is **8080** (hardcoded default, configurable via `PORT` env)
- Map any host port (30001 used here) to 8080
- Data persists in `./data` (SQLite DB, SSH hosts, credentials, settings)
- Container health check passes when web UI responds

## Windows App Connection
1. Open Termix Windows app
2. Select **"Custom server URL"**
3. Enter: `http://<server-ip>:30001`
4. Click **Save Configuration**

## Cloudflare Tunnel (HTTP for Web UI)
```bash
cloudflared tunnel --url http://localhost:30001
```
Then in Cloudflare Zero Trust Dashboard → Networks → Tunnels → add public hostname pointing to the tunnel.

## Cloudflare Tunnel (SSH for Actual SSH Connections)
Requires `cloudflared` on client side too. See [Cloudflare SSH docs](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/).

## Verification Steps
```bash
# Check container running
docker compose ps
# Expected: Up (healthy), 0.0.0.0:30001->8080/tcp

# Test web UI
curl -s http://localhost:30001 | head -5
# Expected: <!doctype html> ... <title>Termix</title>
```

## Pitfalls Avoided
1. Wrong image name → `denied` / `pull access denied`
2. Assuming Termix uses port 30001 internally → it uses 8080
3. Not persisting `./data` → lose all config on container recreate
4. Windows app defaults to "Local Server (β)" → must switch to Custom URL