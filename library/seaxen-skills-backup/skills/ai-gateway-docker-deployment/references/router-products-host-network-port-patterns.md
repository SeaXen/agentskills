# Router products on host networking: port and env-file patterns

Use this when installing OmniRoute/9router/LiteLLM-style gateway products side-by-side on the same Linux host.

## Durable lessons

### 1. `docker compose restart` does NOT reload changed env-file values
If the service uses `env_file:` or `.env` and you change credentials or listen-port vars, a plain restart is insufficient.

Use:
```bash
docker compose up -d --force-recreate --no-deps <service>
```

Then verify with:
```bash
docker exec <container> /bin/sh -lc 'env | sort | grep -E "^(UI_USERNAME|UI_PASSWORD|PORT|HOSTNAME)="'
```

This mattered for LiteLLM UI login: the file was correct on disk, but the live container still had the old environment until recreate.

### 2. Host networking means real port conflicts
With `network_mode: host`, two products cannot share the same listen port.

- bridge mode: host port can differ from container port
- host mode: the app's own listen port must change

Examples:
- OmniRoute on `20128`
- 9router on `20111` or `20129`

For 9router, upstream docs support:
- `PORT=<port>`
- `HOSTNAME=0.0.0.0`

### 3. Verify HTTP and socket binding separately
Do both:
```bash
curl -I http://127.0.0.1:<port>/
ss -ltn '( sport = :<port> )'
```

HTTP may already redirect correctly while your first broad `ss` filter misses the listener because of a bad pattern.

### 4. 9router runtime behavior
Observed install pattern:
- single Docker container is enough
- root path returns `307` redirect to `/dashboard`
- app listens on the configured port after setting `PORT`
- LAN exposure works with `HOSTNAME=0.0.0.0` under host networking

Useful verification:
```bash
curl -s -o /tmp/out -w "%{http_code}\n" http://127.0.0.1:<port>/
docker logs --tail 30 9router
```

Expected signal from logs:
- Next.js local/network URLs on the configured port

### 5. Timezone (`TZ`)

Set `TZ` in compose `environment` (e.g. `Asia/Dhaka`) and **force-recreate**. Verify with:
```bash
docker exec 9router node -e "console.log(Intl.DateTimeFormat().resolvedOptions().timeZone)"
```

### 6. 9router Usage periods beyond 60D

Patch built `.next` via `scripts/apply-9router-usage-periods.py` — ephemeral after image pull. Details: `references/9router-dashboard-customization.md`.

### 7. Same-host vs tunnel API base

| Gateway | Same-box Hermes base URL |
|---------|--------------------------|
| 9router | `http://127.0.0.1:20111/v1` |
| OmniRoute | `http://127.0.0.1:20128/v1` |

Use Cloudflare tunnel hostnames for remote clients only; edge relay workers cannot use LAN origins.
