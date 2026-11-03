# Multi-App Dashboard Landing Page

## Pattern
When you have many apps on different ports, create a simple HTML landing page on a new port with links to all apps.

## Implementation
```bash
mkdir -p /var/www/dashboard
# Write index.html with grid of app cards
cd /var/www/dashboard && python3 -m http.server 9090
```

## Key Design Decisions
- **Dark theme** — matches Hermes dashboard aesthetic
- **Auto-detect hostname** — JavaScript replaces `//HOST:` with `//<actual-host>:` so links work from any device
- **No auth** — landing page is public, individual apps have their own auth
- **Separate port** — doesn't interfere with existing nginx configs

## What to Include
- Docker apps (Portainer, Open WebUI, Jellyfin, etc.)
- Group by category with emoji icons

## Nginx Alternative
If you want a unified entry point via nginx, create a **separate server block** on a new port — don't add static file proxies inside the Hermes dashboard server block.

## Example
See `/var/www/dashboard/index.html` for a working template.
