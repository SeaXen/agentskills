# OmniRoute Free-Proxy Providers — Env-Var Reference

OmniRoute ships several "free proxy" providers that pull rotating proxy lists from external APIs. **All configuration is env-var driven** through `/mnt/tb/1Apps/omniroute/data/server.env` (mounted via `env_file:` in `docker-compose.yml`). There is no UI toggle to enable/disable a free-proxy provider — you set env vars, recreate the container, and the next free-proxies sync picks up the new state.

## Why this matters

The UI surfaces providers with a status like:

- `Webshare provider disabled (set FREE_PROXY_WEBSHARE_API_KEY to enable)`
- `IPLocate provider disabled (opt-in via FREE_PROXY_IPLOCATE_ENABLED=true)`

A common mistake is editing `server.env`, running `docker compose restart`, and seeing the same disabled message. **The container was never recreated**, so the new env var was never loaded. See `devops/docker-safe-update` → "PITFALL: `docker compose restart` does NOT reload `env_file`" for the symptom checklist. Always use:

```bash
cd /mnt/tb/1Apps/omniroute
docker compose up -d --force-recreate --no-deps
```

Verify the var is actually loaded:

```bash
docker inspect omniroute --format '{{range .Config.Env}}{{println .}}{{end}}' | grep FREE_PROXY
```

## Providers (source: `src/lib/freeProxyProviders/*.ts` in omniroute-repo)

### `webshare` — Webshare rotating proxies (paid tier)

| Var | Required | Default | Notes |
|---|---|---|---|
| `FREE_PROXY_WEBSHARE_API_KEY` | **yes** | — | Webshare API key. Without it, provider reports disabled. |
| `FREE_PROXY_WEBSHARE_ENABLED` | no | `true` (when key present) | Set to `false` to disable even if a key is configured. |
| `FREE_PROXY_WEBSHARE_API_URL` | no | `https://proxy.webshare.io/api/v2/proxy/list` | Override for self-hosted Webshare-compatible endpoints. |
| `FREE_PROXY_WEBSHARE_MAX` | no | `DEFAULT_MAX` | Max proxies to pull. |

### `iplocate` — IPLocate geolocation-based free proxies

| Var | Required | Default | Notes |
|---|---|---|---|
| `FREE_PROXY_IPLOCATE_ENABLED` | **yes** | `false` | Opt-in: must be `true` to enable. |
| `FREE_PROXY_IPLOCATE_BASE_URL` | no | `BASE_URL` | Override endpoint. |

### `proxifly` — Proxifly rotating free proxies

| Var | Required | Default | Notes |
|---|---|---|---|
| `FREE_PROXY_PROXIFLY_ENABLED` | no | `true` | Set to `false` to disable. |
| `FREE_PROXY_PROXIFLY_QUANTITY` | no | `DEFAULT_QUANTITY` | Number of proxies to request per sync. |
| `FREE_PROXY_PROXIFLY_ANONYMITY` | no | `DEFAULT_ANONYMITY` | Anonymity filter (`anonymous`, `elite`, etc.). |

### `1proxy` — 1Proxy rotating free proxies

| Var | Required | Default | Notes |
|---|---|---|---|
| `FREE_PROXY_1PROXY_ENABLED` | no | `true` | Set to `false` to disable. |
| `FREE_PROXY_1PROXY_API_URL` | no | `DEFAULT_API_URL` | Override endpoint. |
| `FREE_PROXY_1PROXY_MAX` | no | `DEFAULT_MAX` | Max proxies to pull. |

## Workflow: enable a new free-proxy provider

1. Back up `data/server.env`:
   ```bash
   cp /mnt/tb/1Apps/omniroute/data/server.env \
      /mnt/tb/1Apps/omniroute/data/server.env.bak-$(date +%Y%m%d-%H%M%S)
   ```
2. Add the relevant vars (e.g. Webshare):
   ```
   FREE_PROXY_WEBSHARE_API_KEY=***
   FREE_PROXY_WEBSHARE_MAX=10
   ```
3. Recreate the container so env is reloaded:
   ```bash
   cd /mnt/tb/1Apps/omniroute
   docker compose up -d --force-recreate --no-deps
   ```
4. Verify:
   ```bash
   docker inspect omniroute --format '{{range .Config.Env}}{{println .}}{{end}}' | grep FREE_PROXY_WEBSHARE
   docker ps --filter name=omniroute --format 'table {{.Names}}\t{{.Status}}'
   curl -sI http://127.0.0.1:20128/ | head -1
   ```
5. Trigger a free-proxies sync (via the OmniRoute dashboard or wait for the next scheduled sync).

## Common false alarms

- "I added the key but it still says disabled" → you did `restart`, not recreate.
- "API URL is right but it still fails" → confirm the new endpoint is reachable from the DietPi host first (`curl` directly), then check the provider status in OmniRoute.
- "Provider is `active` in storage but UI shows error" → check provider `last_error` column via sqlite; the error may be from an upstream proxy pool, not the provider itself.
