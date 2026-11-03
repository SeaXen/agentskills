# Dockerized Cloudflare route discovery for SeaDash

Use when SeaDash needs real public URLs but the Cloudflare component is a Dockerized WebUI and does not expose route JSON.

## Durable signals that worked
- Cloudflare ran as container `big-bear-cloudflared-web`.
- The WebUI only exposed token-entry, so it was not an authoritative route source.
- Public host clues were recoverable from app compose/env instead:
  - `HOMEPAGE_ALLOWED_HOSTS` contained `hp.xuup.top`
  - `N8N_HOST` contained `n8n.xuup.top`
  - `WEBHOOK_URL` confirmed `https://n8n.xuup.top/`

## Practical workflow
1. Search CasaOS or app compose files for the live domain/TLD.
2. Extract public hostnames from app-level env vars, not just cloudflared logs.
3. Insert them into `seadash-config.json` under `cloudflare.routes` with `public_url`, `domain`, and `access`.
4. If SeaDash URL discovery is hardcoded for an old suffix like `.eu.org`, broaden it to the real live suffix (here `.top`).
5. Restart SeaDash and verify:
   - `/api/monitor` -> `cloudflare.route_count > 0`
   - `/api/monitor` -> `cloudflare.urls` contains the expected hosts
   - UI body text shows the public hosts

## Example route entries
```json
{
  "cloudflare": {
    "autoDetect": true,
    "routes": [
      {
        "name": "homepage",
        "app": "homepage",
        "container_name": "homepage",
        "public_url": "https://hp.xuup.top",
        "domain": "hp.xuup.top",
        "access": "zero_trust"
      },
      {
        "name": "n8n",
        "app": "n8n",
        "container_name": "n8n",
        "public_url": "https://n8n.xuup.top",
        "domain": "n8n.xuup.top",
        "access": "zero_trust"
      }
    ]
  }
}
```

## Notes
- Route entries may exist before the corresponding containers are running; that is still useful for SeaDash public URL visibility.
- Telegram wiring is a separate step; do not block route completion on missing Telegram credentials.
