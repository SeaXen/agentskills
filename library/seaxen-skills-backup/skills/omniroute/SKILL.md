---
name: omniroute
description: Install, update, and troubleshoot OmniRoute (AI gateway for multi-provider LLMs) on Docker. Covers container lifecycle, encryption key management, provider configuration, and known issues.
triggers:
  - omniroute
  - "grok-web"
  - "omniroute update"
  - "omniroute docker"
---

# OmniRoute Management

Self-hosted OmniRoute (AI gateway / multi-provider LLM router) running on DietPi at `192.168.0.222:20128`.

## Container Setup

- **Image:** `diegosouzapw/omniroute:latest`
- **Port:** `20128` (host networking)
- **Data volume:** `/mnt/tb/1Apps/omniroute/data:/app/data`
- **Compose file:** `/mnt/tb/1Apps/omniroute/docker-compose.yml`
- **App logs inside container:** `/app/logs/application/app.log`

Standard management:
```bash
cd /mnt/tb/1Apps/omniroute
docker compose ps          # status
docker compose logs -f     # live logs (works fine, logs go to stdout)
docker compose up -d       # start
docker compose restart     # restart
docker compose pull && docker compose up -d  # update
```

## Updating

See `omniroute-safe-update` and `omniroute-update` for backup + safe recreate.

Quick path:
```bash
bash /mnt/tb/1Apps/omniroute/backup.sh
cd /mnt/tb/1Apps/omniroute
docker compose pull
docker compose up -d --force-recreate
```

**Verify:** healthy container; `curl` to `:20128` may return **307** (redirect) — OK. Confirm `provider_connections` count in `storage.sqlite` after recreate.

**Hermes agent:** If foreground `docker compose up` is blocked, run recreate in background and verify separately.

## Free-proxy providers (env-var driven)

OmniRoute ships several "free proxy" providers (`webshare`, `iplocate`, `proxifly`, `1proxy`) configured entirely through env vars read from `data/server.env`. Each provider has its own:

- `FREE_PROXY_<NAME>_API_KEY` (where applicable)
- `FREE_PROXY_<NAME>_ENABLED` (`true`/`false`, default varies)
- `FREE_PROXY_<NAME>_API_URL` / `FREE_PROXY_<NAME>_BASE_URL` / `FREE_PROXY_<NAME>_MAX` (optional tuning)

The provider is enabled by default unless its `*_ENABLED=false` flag is set, **except** providers that require a key (webshare, iplocate) — those print `"Webshare provider disabled (set FREE_PROXY_WEBSHARE_API_KEY to enable)"` until a key is present.

Adding a key → recreate container → next free-proxies sync pulls the new list. UI status moves from `disabled` to `active`.

Full per-provider env-var tables, enable/disable defaults, and the safe edit-recreate-verify workflow: `references/free-proxy-providers-env-vars.md`.

## ⚠️ CRITICAL PITFALL: Encryption Key Loss on Container Recreation

When the container is recreated (stop + rm + new run), OmniRoute may auto-generate **new** `JWT_SECRET` and `STORAGE_ENCRYPTION_KEY`. These keys are written to `/mnt/tb/1Apps/omniroute/data/server.env`.

**Consequences of key mismatch:**
- Browser dashboard shows "Internal Server Error" — the old session cookie was signed with the old `JWT_SECRET`
- Encrypted provider credentials (API keys) may become unreadable
- Users must **clear browser cookies** for the dashboard and re-sign in (first account becomes admin)

**Mitigation:** Before updating, back up `server.env`:
```bash
cp /mnt/tb/1Apps/omniroute/data/server.env /mnt/tb/1Apps/omniroute/data/server.env.bak
```
After recreating, if new keys were generated, restore the old `server.env` and restart.

## Checking Logs

OmniRoute logs to stdout/stderr — `docker compose logs` works:
```bash
cd /mnt/tb/1Apps/omniroute
docker compose logs --tail 100 omniroute
docker compose logs --since 2h omniroute | rg -i 'ROUTING|AUTH|HTTP|error|502|413|429|quota|codex|cx/'
```

**Log noise (usually not the chat failure):** repeated `No credentials for *-search`, `REDIS_URL is not set`, unconfigured Antigravity/Qoder OAuth. Filter these out before concluding the gateway is broken.

## Diagnosing “model X doesn’t work” on `/v1`

Do **not** assume the gateway is down. Run this sequence on the DietPi host (see `references/gateway-api-diagnostic.md`; quick failure rollup: `scripts/summarize-call-log-failures.py`):

1. **Service** — `docker compose ps` → healthy on `:20128`.
2. **Catalog** — `GET /v1/models` → confirm exact model id (e.g. `cx/gpt-5.4` is listed).
3. **Live completion** — `POST /v1/chat/completions` with an OmniRoute API key from `storage.sqlite` (`api_keys` table), `stream: false`, tiny prompt. HTTP 200 = gateway + upstream path OK from server.
4. **Persisted failures** — scan `/mnt/tb/1Apps/omniroute/data/call_logs/YYYY-MM-DD/*.json` for `summary.status >= 400` grouped by `requestedModel` + `provider` (today’s errors may be a *different* model than the user named).
5. **Container logs** — match `ROUTING` (alias → provider model) and `AUTH` (which connection id) for the user’s model string.

### ⚠️ PITFALL: Same “GPT 5.4” name, different providers

| Client model id | Provider | Typical failures |
|-----------------|----------|------------------|
| `cx/gpt-5.4` or `codex/gpt-5.4` | **codex** (OAuth subscription) | Rare; watch **model-sync 502** on startup (`GET .../models`) — chat can still work |
| `chatgpt-web/gpt-5.4-pro` | **chatgpt-web** | **500** / **413** (payload size) — unrelated to `cx/gpt-5.4` |

If the user says “gpt-5.4 on OmniRoute fails”, ask which **full model id** their client sends.

### Client-side causes when server probe passes

- Wrong key (OpenAI/Bynara key instead of OmniRoute `sk-...`) → 401
- Client off LAN (`192.168.0.222` unreachable) → timeout
- Hermes/custom provider default model not set to the requested id

## Cloudflare Quick Tunnel

After container recreation, the old tunnel registration is stale. Go to dashboard → Settings → Cloudflare Quick Tunnel → **Disable → Enable** to get a fresh URL.

## Search providers on LAN / localhost (SearXNG pitfall)

When a search provider in OmniRoute shows:
- `Upstream error`
- `Blocked private or local provider URL`

this is usually **OmniRoute's outbound URL guard**, not the search engine itself.

### What it means

OmniRoute is refusing a provider endpoint on:
- `localhost`
- `127.0.0.1`
- `192.168.x.x`
- other private/LAN ranges

The controlling flag is:
- `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS=true`

Related flag:
- `OMNIROUTE_ALLOW_LOCAL_PROVIDER_URLS` (local/private provider validation behavior)

### Fast diagnosis

1. Open the provider page in OmniRoute and read the exact connection status text.
2. If it says `Blocked private or local provider URL`, inspect the running container env and `/app/data/server.env`.
3. Confirm whether `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS` is unset/false.
4. Only after that, test the target endpoint directly (`curl`/browser) to see whether the service is actually listening.

### ⚠️ PITFALL: Host networking kills port mapping — update ALL references

When switching SearXNG (or any container) from bridged networking (`ports: 8888:8080`) to `network_mode: host`, the container binds directly to its **internal** port (8080). The old external port (8888) becomes dead — nothing listens there.

**All three layers must be updated:**

| Layer | What to change | Example |
|---|---|---|
| Docker compose | `SEARXNG_BASE_URL` env var | `http://host:8080/` (not `:8888`) |
| OmniRoute DB | `provider_connections.provider_specific_data.baseUrl` | `http://127.0.0.1:8080/search` |
| Hermes config | `SEARXNG_URL` in config.yaml + `.env` | `http://127.0.0.1:8080` |

**SQLite fix for OmniRoute provider:**
```sql
UPDATE provider_connections
SET provider_specific_data = json_set(provider_specific_data, '$.baseUrl', 'http://127.0.0.1:8080/search'),
    updated_at = datetime('now')
WHERE provider = 'searxng-search';
SELECT changes();
```
Then `docker compose restart omniroute` to reload.

### ⚠️ PITFALL: OmniRoute API keys block search endpoint

OmniRoute's `/v1/search` endpoint requires `model: "search"` to be in the API key's `allowed_models`. If the key only lists LLM models (e.g. `["BynaraCombo","cx/gpt-5.4"]`), search returns:

```json
{"message": "Model \"search\" is not allowed for this API key", "type": "permission_error", "code": "insufficient_quota"}
```

**Fix:** Add `"search"` to the key's `allowed_models`:
```sql
UPDATE api_keys
SET allowed_models = '["model1","model2","search"]'
WHERE name = 'Hermes';
```
Then restart OmniRoute to reload the key cache.

### OmniRoute /v1/search endpoint

OmniRoute has a **standalone search API** at `POST /v1/search` with automatic failover across 12+ providers:

- serper-search, brave-search, perplexity-search, exa-search, tavily-search
- google-pse-search, linkup-search, searchapi-search, youcom-search
- searxng-search, ollama-search, zai-search, duckduckgo-free

**Request format:**
```json
{
  "query": "search query",
  "provider": "serper-search",  // optional — auto-selects cheapest
  "max_results": 5,
  "search_type": "web" | "news"
}
```

**Auth:** `Authorization: Bearer <omniroute-api-key>`

**Cost-based auto-selection:** picks cheapest available provider. SearXNG ($0) first, then serper ($0.001), brave ($0.005), etc.

**This endpoint is SEPARATE from Hermes' web_search tool.** Hermes does NOT call `/v1/search` by default — it has its own plugin system. A custom plugin is needed to bridge them.

### Important distinction for Hermes

For Hermes' SearXNG plugin, `SEARXNG_URL` must be the **base instance URL**:
- correct: `http://host:port`
- wrong: `http://host:port/search`

Hermes appends `/search?format=json&q=...` itself.

But for OmniRoute's SearXNG provider connection, the URL must include `/search`:
- correct: `http://host:port/search`
- wrong: `http://host:port`

OmniRoute's validator probes `?q=test&format=json` against the provided URL directly.

### Common two-layer failure

It is possible to have **both** problems at once:
1. OmniRoute blocks the private/local provider URL.
2. The target SearXNG endpoint is also not actually listening on that host/port.

Do not stop at the OmniRoute error string — after fixing the allow-private flag, re-test the endpoint directly.

Reference: `references/searxng-private-url-guard.md`

### ⚠️ PITFALL: SearXNG host-network switch changes the working local endpoint

If you move SearXNG from bridged Docker networking with a published port (for example `8888:8080`) to `network_mode: host` to fix outbound engine connectivity, the working local URL usually changes:

- before: `http://127.0.0.1:8888/search`
- after: `http://127.0.0.1:8080/search`

A very common follow-on failure is that OmniRoute's saved `searxng-search` connection still points at the **old** URL. The UI then shows:
- `network issue`
- `Network error`
- `fetch failed`

while the new endpoint itself is actually healthy.

#### Fast diagnosis for this mismatch

1. Test from inside OmniRoute against both candidate URLs.
2. Inspect the saved provider record in `/mnt/tb/1Apps/omniroute/data/storage.sqlite`:
   ```bash
   sqlite3 -header -column /mnt/tb/1Apps/omniroute/data/storage.sqlite \
     "select id, provider, name, test_status, last_error, provider_specific_data from provider_connections where provider='searxng-search';"
   ```
3. Read `provider_specific_data.baseUrl` and compare it to the URL that actually returns HTTP 200.
4. If they differ, update the saved base URL, then retest from the OmniRoute UI.

#### Durable fix

Update `provider_connections.provider_specific_data` so `baseUrl` matches the real endpoint. Example:

```bash
sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "update provider_connections
   set provider_specific_data=json_set(provider_specific_data, '$.baseUrl', 'http://127.0.0.1:8080/search'),
       updated_at=datetime('now')
   where provider='searxng-search';"
```

Then hit **Retest** in the provider UI. A healthy record should move from `error / fetch failed` to `active`, and the page should show `connected`.

## OmniRoute Search API (`/v1/search`)

OmniRoute has a standalone **search API** at `POST /v1/search` that routes across 12 providers with automatic failover (cheapest-first). This is separate from the LLM chat/completions path.

**Providers:** serper, brave, exa, tavily, searxng, google-pse, perplexity, linkup, searchapi, youcom, ollama, zai, duckduckgo-free (fallback only).

**Auth:** Requires an OmniRoute API key with `\"search\"` in `allowed_models`. Without it, returns `permission_error`.

```bash
# Test with auto-select (picks cheapest = searxng at $0)
curl -s -X POST http://127.0.0.1:20128/v1/search \
  -H "Authorization: Bearer $OR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"test","max_results":3}'

# Force specific provider
curl -s ... -d '{"query":"test","provider":"serper-search"}'
```

See `references/omniroute-search-api.md` for full provider table, response format, credential fallbacks, and failover behavior.

### Custom Hermes Plugin: `omniroute-search`

A custom Hermes web search plugin routes `web_search` through OmniRoute's `/v1/search`, giving Hermes automatic failover across all configured search providers (searxng → serper → brave → exa → tavily).

**Files (user plugin — survives Hermes updates):**
- `~/.hermes/plugins/omniroute_search/plugin.yaml`
- `~/.hermes/plugins/omniroute_search/__init__.py`
- `~/.hermes/plugins/omniroute_search/provider.py`

**Backend name:** `omniroute-search`

**Activation:**
```bash
hermes config set web.search_backend omniroute-search
```

**API key discovery:** Auto-discovers from local OmniRoute SQLite DB. No env var needed unless OmniRoute is remote. Falls back to `OMNIRROUTE_API_KEY` env var if set.

**Key advantage over direct SearXNG:** If SearXNG goes down, OmniRoute auto-fails over to serper/brave/exa/tavily. Direct SearXNG has no fallback.

**⚠️ PITFALL: User plugin uses relative imports**
`__init__.py` must use `from .provider import ...` (dot-prefix relative), not `from provider import ...`. Absolute imports fail silently when loaded by user plugin discovery.

See `references/hermes-omniroute-search-plugin.md` for plugin source, architecture, and troubleshooting.
Reference: `references/aceroute-analytics-dashboard.md`
Reference: `references/gateway-api-diagnostic.md`
Reference: `references/hermes-omniroute-search-plugin.md`
Reference: `references/hermes-web-search-backends.md`
Reference: `references/hermes-web-search-config.md`
Reference: `references/omniroute-relay-fix-v3.8.45-6149.md`
Reference: `references/omniroute-search-api.md`
Reference: `references/searxng-deployment.md`
Reference: `references/searxng-endpoint-mismatch.md`
Reference: `references/searxng-engine-performance.md`
Reference: `references/searxng-private-url-guard.md`
Reference: `references/searxng-provider-url-fix.md`
Reference: `references/hermes-omniroute-search-plugin.md`

## SearXNG Deployment (Self-Hosted Search Engine)

SearXNG runs alongside OmniRoute as a local search engine at `192.168.0.222:8080`. It provides free, unlimited web search for both Hermes and OmniRoute.

- **Compose file:** `/mnt/tb/1Apps/searxng/docker-compose.yml`
- **Config:** `/mnt/tb/1Apps/searxng/config/settings.yml`
- **Stats:** `http://192.168.0.222:8080/stats`
- **Dashboard:** `http://192.168.0.222:8080`

See `references/searxng-deployment.md` for the full compose template, optimized settings.yml, and engine reliability data.

### Key facts
- Uses `network_mode: host` (bridged Docker networking breaks outbound HTTPS on this DietPi host)
- 8 engines at 100% reliability: google, bing, brave, qwant, mojeek, yandex, wikipedia, wikidata
- `restart: unless-stopped` handles auto-restart on crash/reboot
- `SEARXNG_BASE_URL` in compose env must match the actual listening port (8080 with host networking)

### PITFALL: SEARXNG_BASE_URL stale after networking change
The `SEARXNG_BASE_URL` environment variable in `docker-compose.yml` must be updated when networking changes. It was originally set to `:8888` but needs to be `:8080` after switching to host networking. If this is wrong, SearXNG still works but some internal URL generation may be incorrect.

### PITFALL: Some engines crash the container
Not all SearXNG engine names exist in every version. Known-broken: `stackoverflow`, `semanticscholar`, `dockerhub`. Adding these to `settings.yml` causes `Restarting (1)`. Always check `docker compose logs searxng` after config changes.

### Hermes ↔ SearXNG ↔ OmniRoute routing
```
Hermes web_search  →  OmniRoute /v1/search (via omniroute-search plugin)
                       → searxng/serper/brave/exa/tavily (auto-failover)
Hermes web_extract →  9router /v1/web/fetch (via omniroute-search plugin)
                       → exa → tavily → jina-reader (fallback)
Hermes model API   →  OmniRoute /v1/chat/completions (http://192.168.0.222:20128/v1)
OmniRoute search   →  SearXNG (via searxng-search provider, baseUrl in SQLite)
Direct SearXNG     →  http://192.168.0.222:8080 (accessible but not primary search path)
AceRoute analytics →  Reads OmniRoute call_logs/ + storage.sqlite + SearXNG stats
                    →  http://192.168.0.222:8866
```

grok-web uses browser session cookies instead of API keys. Current known issue: **validation is broken** (see [OmniRoute#3063](https://github.com/diegosouzapw/OmniRoute/issues/3063), [OmniRoute#5350](https://github.com/diegosouzapw/OmniRoute/issues/5350)).

### Cookie format required by OmniRoute:
```
sso=<value>; sso-rw=<value>
```
- Copy the **full Cookie header** from DevTools → Network → any grok.com request → Request Headers → `Cookie:`
- Paste **without** the `Cookie:` prefix
- **Space after semicolon is required**: `sso=...; sso-rw=...` not `sso=...;sso-rw=...`
- May also need `cf_clearance` and other cookies from the same domain

### If it still fails:
This is the known bug. Use xAI API key or OpenRouter as fallback until OmniRoute patches grok-web.

## AceRoute — Search Analytics Dashboard

AceRoute is a standalone FastAPI dashboard at `http://192.168.0.222:8866` that aggregates search/extract analytics from OmniRoute call logs, SearXNG engine stats, and Hermes debug logs.

```bash
cd /mnt/tb/1Apps/AceRoute
docker compose ps          # status
docker compose up -d       # start
```

See `references/aceroute-analytics-dashboard.md` for API endpoints, data sources, and architecture.

### ⚠️ PITFALL: Free-tier cost calculation must check monthly limits

When building analytics that track search API costs, naive `searches × cost_per_query` shows phantom costs even when usage is within free tiers. Always count current-month usage per provider and compare against `free_monthly` before calculating cost. This must be done in ALL cost calculation paths (overview, providers, costs) or the UI shows inconsistent numbers.

See `references/compact-dark-dashboard-css.md` in the `dashboard-ui-polish` skill for the full pattern (section "Analytics: free-tier-aware cost calculation").

## Filing OmniRoute Issues

Use `gh issue create --repo diegosouzapw/OmniRoute` from the CLI (SeaXen GitHub auth is configured).

**Vercel/Deno relay Proxy Test 500:** upstream generated worker bug — `ReferenceError: resolveRelayTarget is not defined` in `api/relay.js` ([#6149](https://github.com/diegosouzapw/OmniRoute/issues/6149)). **Fixed in v3.8.45** ([PR #6202](https://github.com/diegosouzapw/OmniRoute/pull/6202)) — relay templates now emit `const resolveRelayTarget = ${fn.toString()};` (minification-safe). Workaround until update: skip proxy-pool relays; use `http://127.0.0.1:20128/v1` + external Cloudflare Tunnel. See `references/omniroute-relay-fix-v3.8.45-6149.md`.

**Cloudflare relay deploy (#6416):** misleading `Content-Type` message; real failure was Service Worker vs ESM `export` in worker body. Fix in **PR #6496** (Service Worker syntax + `body_part` metadata). See `learnables/omniroute-system` → `references/cloudflare-relay-6416-bug-evidence.md`.

## Hermes web search integration

See `references/hermes-web-search-config.md` for the full Hermes web search backend cascade, key resolution, and custom plugin pattern. See `templates/omniroute_search_provider.py` for a working OmniRoute → Hermes search bridge plugin.

See `references/9router-web-search-fetch-bridge.md` for the verified 9router web catalog, direct smoke tests, and Hermes default extraction bridge.

## Hermes Debug Logging (`WEB_TOOLS_DEBUG`)

Hermes can log all web_search/web_extract calls to JSON files for external analysis (AceRoute, auditing, replay).

**Enable:**
```bash
# In ~/.hermes/.env
WEB_TOOLS_DEBUG=true
```

**Output:** `web_tools_debug_<UUID>.json` files in `/root/logs/` (or `HERMES_LOGS_DIR` if set).

**What gets logged:** Every `web_search` and `web_extract` tool call — URLs, queries, providers, latencies, results, errors, session IDs, truncation metrics, SSRF blocks.

**Initialization:** `_debug = DebugSession("web_tools", env_var="WEB_TOOLS_DEBUG")` is at module load time (line 319 of `web_tools.py`). Setting the env var after the process starts has NO effect — the DebugSession was already initialized with the old value. A full Hermes restart is required.

**⚠️ PITFALL: .env changes require a Hermes restart.** Environment variables from `.env` are loaded at process start. After editing `.env`, restart the Hermes gateway/session.

**⚠️ PITFALL: OmniRoute search plugin bypasses debug logging.** When `web.search_backend: omniroute-search`, search calls go through the plugin code path, which does NOT call `_debug.log_call()`. Only direct Hermes backends (tavily, exa, searxng, firecrawl, brave-free, ddgs) write debug logs. This means `WEB_TOOLS_DEBUG=true` captures `web_extract` calls (which use Tavily directly) but NOT `web_search` calls (which go through the OmniRoute plugin). To get search debug logs, switch to a direct backend: `web.search_backend: searxng` or `web.search_backend: tavily`.

## Hermes Web Search + Fetch Integration

Hermes can use separate gateway bridges for search and extraction:

```yaml
# ~/.hermes/config.yaml
web:
  search_backend: omniroute-search  # OmniRoute /v1/search
  extract_backend: omniroute-search  # 9router /v1/web/fetch bridge
```

The user plugin at `~/.hermes/plugins/omniroute_search/` supports both capabilities:

```text
web_search  → OmniRoute /v1/search
web_extract → 9router /v1/web/fetch
```

The 9router fetch fallback order is:

```text
Exa → Tavily → Jina Reader
```

It auto-discovers the local 9router API key from `/mnt/tb/1Apps/9router/data/db/data.sqlite`. For remote deployments, set `NINEROUTER_URL` and `NINEROUTER_KEY`; optionally override the order with `NINEROUTER_FETCH_MODELS=exa,tavily,jina-reader`.

9router web model discovery:

```bash
curl "$NINEROUTER_URL/v1/models/web" \
  -H "Authorization: Bearer $NINEROUTER_KEY"
```

Current provider IDs may include `exa/search`, `tavily/search`, `exa/fetch`, `tavily/fetch`, and `jina-reader/fetch`. The actual request uses the provider model name (`exa`, `tavily`, or `jina-reader`).

**Restart requirement:** plugin/config changes load at gateway/session startup. Restart Hermes after changing `config.yaml`, plugin code, or `.env`.

The reusable 9router capability skills are stored under `learnables/9router/skills/`.

**Key must be in `.env` or local DB, not committed to config.yaml.**

## ⚠️ PITFALL: Docker `COPY . .` can use stale build cache

When files are modified on disk but `docker compose build` produces a container with old code, the build cache is reusing a stale `COPY` layer. Symptoms:
- `grep` inside the container shows old code
- New endpoints return 404
- New features don't appear

**Diagnosis:**
```bash
docker exec <container> head -5 /app/app.py  # check timestamp/content
docker exec <container> grep -n 'new_feature' /app/app.py  # should find it
```

**Fix:** `docker compose build --no-cache` then `docker compose up -d --force-recreate`.

**When this happens:** After multiple rapid builds where only source files changed (not requirements.txt or Dockerfile). Docker's layer cache sees the same `COPY . .` instruction and reuses the old layer.

## ⚠️ PITFALL: API keys in docker-compose.yml are visible to anyone with repo access

Inline `environment:` entries with secrets get committed to git. Use `env_file: .env` instead:

```yaml
# docker-compose.yml
services:
  aceroute:
    env_file: .env  # ← secrets stay out of version control
    environment:
      - SEARXNG_URL=http://127.0.0.1:8080  # ← non-secrets can stay inline
```

```bash
# .env (add to .gitignore!)
TAVILY_API_KEY=tvly-dev-...
EXA_API_KEY=...
ACEROUTE_PASSWORD=...
```

Always add `.env` to `.dockerignore` AND `.gitignore` to prevent accidental exposure.

## Combos: Strategies and Account Rotation

OmniRoute combos have **two layers** of routing that are easy to confuse:

1. **Step layer** — combo has N steps. A strategy like "Round Robin" rotates between *steps* (different models/providers).
2. **Account layer** — within a single step set to "dynamic account", the strategy decides which account from the provider's pool gets picked for that request.

### ⚠️ PITFALL: Round Robin with 1 step + dynamic account does NOT rotate accounts

User reports "I have 10 accounts but only 1 is getting hit" with this config:
- Combo: 1 step, model X, dynamic account
- Strategy: Round Robin

Round Robin's tooltip even says: *"Avoid when: Models differ too much in latency or cost. Example: Same model on multiple accounts to spread throughput."* — that example is misleading; Round Robin needs multiple **steps**, not multiple accounts in one step. With 1 step it has nothing to rotate and keeps picking the first available account.

### Right strategy for multi-account quota rotation (1 step, N accounts)

When the goal is "spread requests across all N accounts of one provider, respect their quotas":

- **Least-Used** (recommended as safe default) — picks the account with fewest requests. Uses OmniRoute's local request/token counter, so it works for **every** provider regardless of whether the upstream API exposes remaining-quota in headers. No Provider Quota data required.
- **Reset-Aware RR** — "Balances remaining quota against 5h and weekly resets, then round-robins similar scores." Built for many same-model accounts with quotas resetting on different schedules. **Only effective on subscription providers** like OpenAI Codex that appear in Provider Quota. For API-key-compatible providers like Bynara, this degrades to plain round-robin because OmniRoute has no real quota data to balance against.
- **Headroom** — quota-aware picker, similar caveat to Reset-Aware RR.
- **Intelligent Auto** — multi-factor self-healing pool.

Avoid for this case: **Priority** (drains account #1 first), **Round Robin** (does nothing with 1 step), **Weighted** (needs multiple steps to weight against).

### Provider Quota page only tracks subscription providers (added 2026-07-11)

**Provider Quota** (`/dashboard/omniproxy/provider-quota` in v3.8.42) only tracks **subscription providers** like OpenAI Codex. For API-key-compatible providers like Bynara, the upstream API doesn't expose remaining-quota in response headers, so OmniRoute has nothing to track. Consequence: Reset-Aware RR / Headroom / quota-aware strategies degrade to plain round-robin when used with Bynara-style providers.

For manual per-account usage tracking on Bynara-like providers, use **Analytics** → filter by provider → group by account → see OmniRoute's local request/token counts per account. That's the real "quota" view you can act on.

### Combo decision tree

```
Multiple models in combo?        →  Pick COMBO strategy (Layer 1) for fallback/rotation between them
Multiple accounts, single model? →  Pick ACCOUNT strategy (Layer 2) at the provider pool level
Both?                            →  Pick both: combo strategy chooses model, account strategy chooses account of that model
```

When a user says "I have N accounts of the same model and I want to rotate through all of them", the answer is **always Layer 2**, not the combo strategy dropdown. Stop them before they pick Round Robin at the combo level.

### Combo step semantics (also commonly confused)

Combo steps are a **fallback chain under the active strategy**, not a load balancer. Pinning specific accounts as separate steps means those exact accounts are hit in order — other accounts in the pool never rotate in. For account rotation, use ONE step with "dynamic account", not N steps each pinned to a specific account.

Add a step 2+ only when you want a genuine fallback to a *different* model/provider after the first is exhausted.

### Where to find **account** sticky round-robin (9router parity)

Users from **9router** expect **Profile → Routing Strategy**. On OmniRoute:

- **After PR #6678:** **Dashboard → Settings → Routing** — first card **Routing Strategy** (account RR + sticky, combo RR + combo sticky).
- **Stock image:** same knobs under **Settings → Routing → Combo defaults** (easy to miss); no separate combo sticky default (1) vs account sticky (3) until parity PR.

Per-provider account strategy (9router Connections card): provider detail page when **2+ connections** — `providerStrategies` in settings DB. Details: `learnables/omniroute-system` → `references/9router-sticky-round-robin-parity.md`.

### Where the strategy lives

In the combo editor: Edit Combo → "Strategy" stage (stage 3 of 4). Available strategies (v3.8.42):
Priority, Weighted, Round Robin, Context Relay, fill-first, p2c, Random, Least-Used, Cost-Opt, Reset-Aware RR, reset-window, headroom, Strict Random, Intelligent Auto, LKGP Mode, context-optimized, Fusion.

### Verifying rotation is working

After changing strategy: send 10-15 requests through the combo, then go to **Providers → \<provider\> → Connections** and look at the per-account request counts / last-used timestamps. If spread across many accounts → working. If still pinned to one → try Least-Used or check that connections aren't in Error/Banned state.

## ⚠️ CRITICAL PITFALL: Do NOT sed-patch minified JS chunks to zero out pricing

To make the cost dashboard show $0, the temptation is to sed-replace pricing numbers in `/app/.build/next/server/chunks/*.js` and `/app/.build/next/static/chunks/*.js`. **Don't.**

- A regex like `(input|output|cached|reasoning|cache_write):[0-9]+(\.[0-9]+)?` → `:0` looks safe but matches inside minified identifier contexts. It produces invalid JS or breaks variable references (e.g. `ReferenceError: t is not defined` from `4bd1b696-*.js`).\n- Symptom: `/dashboard/costs` (and other dashboard pages) render \"Internal Server Error\" client-side. Server returns HTTP 200 for the HTML shell; the error appears only after JS hydration.\n- Chat completions / `/v1/chat/completions` keep working — only UI hydration breaks — which masks the cause.\n- Catalog chunks ALSO get reset every `docker compose pull`, so any patch is ephemeral anyway.\n\n**Correct way to show $0 in the dashboard:** zero out pricing in the SQLite DB only. The DB overrides are persistent and cannot break JS.\n```bash\nsqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite \\\n  \"UPDATE model_capabilities SET input_price_per_million=0, output_price_per_million=0, \\\n   cache_read_price_per_million=0, cache_write_price_per_million=0;\"\n```\nDashboard reads pricing from DB at request time → all costs render as $0, no JS edits needed.\n\n**If you already sed-patched chunks and the dashboard is broken:** restore by `docker compose down && docker compose pull && docker compose up -d`. The DB (with zero overrides) is on a host volume and survives untouched.\n\n## Diagnosing dashboard \"Internal Server Error\" — use the browser, not the logs\n\nWhen `/dashboard/*` renders \"Internal Server Error\" but `curl /dashboard/*` returns HTTP 200 with a normal Next.js HTML shell, the failure is in client-side hydration. Server logs will be silent or only show downstream `/api/usage/...` 404s that are themselves symptoms, not causes.\n\nFastest path to ground truth:\n1. `browser_navigate` to the page.\n2. `browser_console` — read the actual `ReferenceError` / `TypeError` with the offending chunk filename and offset.\n3. Map the chunk hash back to the offending edit (`grep` for the changed pattern in `/app/.build/next/static/chunks/<hash>.js`).\n\nDigging through `docker compose logs`, route handlers, and chunk text without first checking the browser console wastes 10+ tool calls — the console gives the answer in one shot.
