# Manifest self-hosted Docker + LAN — Jun 2026 (DietPi host)

Worked example for installing Manifest beside Hermes on Dr. Sagar's server. Complements cloud `app.manifest.build` in `references/manifest-auto-routing-jun-2026.md`.

## Why self-host

- Provider API keys stored in **local Postgres**, not Manifest SaaS.
- Same OpenAI-compatible API: `POST /v1/chat/completions` with `model: auto` (or `manifest/auto`).
- Docs: https://manifest.build/docs/self-hosted.md , index https://manifest.build/docs/llms.txt

## Install layout (this host)

| Item | Value |
|---|---|
| Install dir | `/mnt/tb/1Apps/manifest/` (default: new self-hosted apps under `/mnt/tb/1Apps/<name>`) |
| Compose project | `name: mnfst` |
| Image | `manifestdotbuild/manifest:latest` |
| Postgres volume | `manifest_pgdata` |
| LAN URL | `http://192.168.0.222:2099` |
| Public URL | `https://mf.xuup.top` (Cloudflare tunnel → `:2099`) |
| API base for Hermes | `http://192.168.0.222:2099/v1` |
| Operator notes | `/mnt/tb/1Apps/manifest/URLS.md` |

## Host network mode (custom providers can't reach internet from bridge)

If Manifest **Routing** custom providers time out from the container (e.g. `No response from https://router.bynara.id/v1/models within 5 s`) but the **host** resolves the URL, switch both services to `network_mode: host`:

1. `manifest` service: remove `ports:` mapping; add `network_mode: host`.
2. `postgres` service: `network_mode: host`; set `DATABASE_URL` to `postgresql://manifest:PASSWORD@127.0.0.1:5432/manifest` (not hostname `postgres`).
3. Remove custom `networks:` blocks from compose; restart stack.

Verify: `docker inspect mnfst-manifest-1 --format '{{.HostConfig.NetworkMode}}'` → `host`.

**Manifest UI "Fetch models" on custom provider:** probe may return **HTTP 401** even when API key is saved — the probe often hits `/v1/models` without the key. **Manual model list + chat** may still work; 401 on fetch alone is not proof the provider is dead.

## LAN exposure (required)

Default compose binds **`127.0.0.1:2099` only**. For LAN:

1. In `docker-compose.yml`, change manifest `ports` to:
   ```yaml
   ports:
     - "${PORT:-2099}:${PORT:-2099}"
   ```
2. In `.env`:
   ```env
   BETTER_AUTH_SECRET=<openssl rand -hex 32>
   MANIFEST_ENCRYPTION_KEY=<separate openssl rand -hex 32>
   BETTER_AUTH_URL=http://192.168.0.222:2099
   PORT=2099
   MANIFEST_TELEMETRY_DISABLED=1
   ```
3. `docker compose up -d` from install dir.

**Login "Invalid origin"** → `BETTER_AUTH_URL` must match the exact URL in the browser (host + port), **unless** you use Pattern B below for LAN + `mf.xuup.top`.

## LAN + public URL (`mf.xuup.top`)

Better Auth allows **one** `BETTER_AUTH_URL`. For **both** LAN and tunnel:

- Keep `BETTER_AUTH_URL=http://192.168.0.222:2099`
- Cloudflare tunnel hostname `mf.xuup.top` → service `http://192.168.0.222:2099`
- Set **HTTP Host header** (origin) to `192.168.0.222:2099` — **not** `mf.xuup.top`

See `dashboard-ui-operations` → `references/better-auth-single-trusted-origin-multi-network.md` (Pattern B).

Register the public URL in SeaDash `seadash-config.json` under `cloudflare.routes` and `custom_apps` when the user asks to "add" a public hostname.

## First boot verification

```bash
curl -sS -o /dev/null -w '%{http_code}\n' http://127.0.0.1:2099/api/v1/health   # expect 200
curl -sS -o /dev/null -w '%{http_code}\n' http://192.168.0.222:2099/setup        # expect 200
curl -sS -o /dev/null -w '%{http_code}\n' https://mf.xuup.top/api/v1/health      # expect 200 (use curl or User-Agent: curl in scripts)
docker compose ps   # manifest + postgres healthy
```

**Pitfall:** Python `urllib` default User-Agent can get **HTTP 403** on `mf.xuup.top` while `curl` returns 200. Use `User-Agent: curl/8.0` (or `hermes-verify`) in ad-hoc probes.

Health 200 does **not** prove login works — test signup after Host-header tunnel config.

## Hermes wiring

```yaml
providers:
  manifest-local:
    api: http://192.168.0.222:2099/v1
    api_key: mnfst_...    # from self-hosted dashboard — NOT the cloud mnfst_ key
    default_model: auto
    name: Manifest Local
```

```bash
timeout 90 hermes chat -Q -q "Reply with exactly: PONG." \
  --provider manifest-local -m auto --max-turns 0 2>&1 | tail -10
```

Until **Routing** has at least one provider, chat returns **M101** (not Hermes misconfig).

## Local LLM from container

Compose sets `OLLAMA_HOST=http://host.docker.internal:11434` and `extra_hosts: host-gateway`. Bind Ollama on the host to `0.0.0.0` and add Ollama as a provider in Manifest Routing.

## Ops

```bash
cd /mnt/tb/1Apps/manifest
docker compose logs -f manifest
docker compose pull && docker compose up -d
docker compose exec -T postgres pg_dump -U manifest manifest > manifest-backup-$(date +%F).sql
```

## Thermal note (this laptop/server)

`docker compose pull` on i3-class hardware can run hot — pace with short gaps if the user reports thermal issues; install is one-time.

## Cloud vs self-host keys

| | Cloud | Self-hosted |
|---|---|---|
| Manifest agent key | `mnfst_` from app.manifest.build | New `mnfst_` from local dashboard |
| Upstream OpenAI/OpenRouter/etc. | Stored on Manifest cloud | Stored in local DB (encrypted with `MANIFEST_ENCRYPTION_KEY` or `BETTER_AUTH_SECRET`) |
| Hermes `providers:` entry | `https://app.manifest.build/v1` | `http://<lan-host>:2099/v1` |

Keep cloud and local as **separate** provider entries if both are used.