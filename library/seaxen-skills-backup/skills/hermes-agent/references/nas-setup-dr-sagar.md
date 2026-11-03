# NAS Setup: Dr. Sagar (ASUS X455L)

## Environment
- **Device:** ASUS X455L Laptop (repurposed as NAS)
- **RAM:** 8GB
- **OS:** Debian 13 (Trixie) via DietPi
- **Internal IP:** 192.168.0.222

## Services
- **Hermes Dashboard:** Port 9119 (nginx proxy) / 9120 (direct)
- **Graphify:** Port 8081 (static files, `graphify-out/graph.html`)
- **Dashboard (landing page):** Port 9090 (`/var/www/dashboard/index.html`)
- **Portainer:** Port 9000
- **Other app:** Port 8080

## Nginx Reverse Proxy (port 9119)
- `/` → Hermes Dashboard (9120) — auth protected
- Do NOT add Graphify or other static apps here — breaks Hermes SPA routing
- Keep static apps on separate ports

## Dashboard Landing Page (port 9090)
- Simple HTML page linking to all apps
- Served via `python3 -m http.server 9090` from `/var/www/dashboard/`
- Auto-detects hostname via JavaScript for cross-device access

## Automation Patterns
- **qBittorrent:** Requires credentials (default admin/adminadmin failed).
- **Auto-downloading:** Intent to automate downloads (RSS/Watch folder/Arr stack).

## Key Commands
```bash
# Check running services
sudo netstat -tulpn | grep -E 'casaos|qbittorrent|hermes'

# Manage Hermes Service
sudo systemctl status hermes-dashboard
```
