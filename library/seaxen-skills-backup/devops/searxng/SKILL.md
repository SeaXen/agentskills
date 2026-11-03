---
name: searxng
description: Deploy, configure, and optimize a self-hosted SearXNG instance for use with Hermes Agent and OmniRoute. Covers Docker setup, engine configuration, host networking, and integration patterns.
triggers:
  - searxng
  - "self-hosted search"
  - "search engine setup"
  - "SEARXNG_URL"
---

# SearXNG Self-Hosted

Self-hosted SearXNG metasearch engine running on DietPi at `192.168.0.222:8080` (host networking).

## Container Setup

- **Image:** `ghcr.io/searxng/searxng:latest`
- **Port:** `8080` (host networking — no port mapping)
- **Compose file:** `/mnt/tb/1Apps/searxng/docker-compose.yml`
- **Config:** `/mnt/tb/1Apps/searxng/config/settings.yml`
- **Data volume:** `/mnt/tb/1Apps/searxng/data:/var/cache/searxng`
- **Restart:** `unless-stopped`

Standard management:
```bash
cd /mnt/tb/1Apps/searxng
docker compose ps          # status
docker compose logs -f     # live logs
docker compose up -d       # start
docker compose restart     # restart
```

## ⚠️ PITFALL: Host networking changes the port

When using `network_mode: host`, the container binds directly to its internal port (8080). The Docker port mapping (`8888:8080`) is removed. **All references to the old port must be updated:**

1. `SEARXNG_BASE_URL` in docker-compose.yml
2. OmniRoute provider connection in SQLite DB
3. `SEARXNG_URL` in Hermes config.yaml AND .env

## Configuration

### settings.yml — Optimized template

```yaml
use_default_settings: true

general:
  debug: false
  instance_name: "SearXNG"
  enable_metrics: true

search:
  safe_search: 0
  autocomplete: "google"
  default_lang: "auto"
  ban_time_on_fail: 5
  max_ban_time_on_fail: 120
  formats:
    - html
    - json

server:
  secret_key: "<generate with: python3 -c 'import secrets; print(secrets.token_hex(32))'>"
  limiter: false          # false for private/LAN instances
  image_proxy: true
  public_instance: false
  method: "GET"

outgoing:
  request_timeout: 6.0
  max_request_timeout: 12.0
  pool_connections: 100
  pool_maxsize: 30
  enable_http2: true
```

### Recommended engines

These engines are reliable in a self-hosted setup:

**High reliability (100%):** google, bing, wikipedia, wikidata
**Good (85%+):** brave, qwant, mojeek, yandex
**Flaky (avoid):** duckduckgo (CAPTCHA blocked), startpage (parsing errors), yahoo (HTTP errors)

Engine section example in settings.yml:
```yaml
engines:
  - name: google
    engine: google
    shortcut: g
    disabled: false
  - name: bing
    engine: bing
    shortcut: b
    disabled: false
  - name: brave
    engine: brave
    shortcut: br
    disabled: false
  - name: qwant
    engine: qwant
    shortcut: qw
    disabled: false
  - name: mojeek
    engine: mojeek
    shortcut: mj
    disabled: false
  - name: wikipedia
    engine: wikipedia
    shortcut: wp
    disabled: false
  - name: wikidata
    engine: wikidata
    shortcut: wd
    disabled: false
  - name: yandex
    engine: yandex
    shortcut: yx
    disabled: false
```

**Disabled by default (unreliable from LAN):** duckduckgo, startpage, yahoo

**Useful add-ons:** github (code), arxiv (papers), google_scholar (academic), pubmed (medical), npm (node), pypi (python)

### ⚠️ PITFALL: Engine names change between SearXNG versions

`stackoverflow`, `semanticscholar`, `dockerhub` may not exist in all versions. Check with:
```bash
docker exec searxng ls /usr/local/searxng/searx/engines/*.py | head -20
```

If an engine fails to load, SearXNG crashes with `Restarting (1)`. Remove the bad engine entry and restart.

## Dashboard / UI

- **Main:** `http://192.168.0.222:8080` — search UI
- **Preferences:** `http://192.168.0.222:8080/preferences` — per-browser settings
- **Engine stats:** `http://192.168.0.222:8080/stats` — engine reliability, scores, response times

The preferences page saves to browser cookies, not server-side. For permanent config changes, edit `settings.yml` and restart.

## JSON API

```bash
curl "http://127.0.0.1:8080/search?q=test&format=json"
```

Returns `{results: [...], unresponsive_engines: [...]}`.

## Integration: Hermes

Hermes uses SearXNG via the bundled `plugins/web/searxng/` plugin.

**Config:**
```bash
hermes config set SEARXNG_URL http://127.0.0.1:8080
hermes config set web.search_backend searxng  # explicit, or leave empty for auto-detect
```

**⚠️ PITFALL: SEARXNG_URL must be in BOTH config.yaml AND .env**

Hermes' SearXNG plugin resolves the URL via `get_env_value("SEARXNG_URL")`, which reads:
1. `os.environ` (process env)
2. `~/.hermes/.env` (dotenv file)

If you only set it via `hermes config set`, it goes into config.yaml but NOT into .env. The plugin may not find it. **Always also set it in .env:**
```bash
# Set in config.yaml (for hermes tools display)
hermes config set SEARXNG_URL http://127.0.0.1:8080

# Also set in .env (for runtime resolution)
# Edit ~/./.env and add: SEARXNG_URL=http://127.0.0.1:8080
```

For extract, see the dedicated section above — **SearXNG is search-only** and
needs a separate extract provider (tavily/exa/firecrawl).

## SearXNG is search-only — extract needs a separate provider

SearXNG cannot do `web_extract`. If a user sets `web.extract_backend: searxng`
or relies on auto-detect with only `SEARXNG_URL` set, `web_extract` tool calls
will return: *"SearXNG is a search-only backend and cannot extract URL content.
Set web.extract_backend to firecrawl, tavily, exa, or parallel."*

**This is the #1 confusion point** — users deploy SearXNG, set it as the
search backend, and assume extract works too. It doesn't.

### Extract-capable providers (as of 2026)

| Provider | Env Var | Free Tier | Extract pricing |
|---|---|---|---|
| Tavily | `TAVILY_API_KEY` | 1000 calls/mo | 5 basic extracts = 1 credit |
| Exa | `EXA_API_KEY` | 1000 calls/mo | included in search credits |
| Firecrawl | `FIRECRAWL_API_KEY` | 500 credits/mo | 1 credit per extract |
| Parallel | `PARALLEL_API_KEY` | paid only | per-token |

### Configuring extract separately from search

Hermes supports per-capability backend split:
```yaml
# ~/.hermes/config.yaml
web:
  search_backend: searxng      # free, local
  extract_backend: tavily      # paid, but only for extracts
```

This way search is free (SearXNG) and only extract uses a paid provider.

### Auto-detect fallback chain

When `web.extract_backend` is empty, Hermes falls through `_get_backend()`:
1. `TAVILY_API_KEY` → tavily
2. `EXA_API_KEY` → exa
3. `PARALLEL_API_KEY` → parallel
4. `FIRECRAWL_API_KEY` or `FIRECRAWL_API_URL` → firecrawl
5. Tool Gateway (Nous subscriber) → firecrawl
6. Default → firecrawl (will fail without API key)

**⚠️ PITFALL: BRAVE_SEARCH_API_KEY ≠ BRAVE_API_KEY**

Hermes checks `BRAVE_SEARCH_API_KEY`, not `BRAVE_API_KEY`. If the user has
`BRAVE_API_KEY` set (common from OmniRoute), Hermes won't detect it for
auto-detect. Brave is also search-only — it cannot extract.

## Integration: OmniRoute

OmniRoute routes through SearXNG via its `searxng-search` provider.

**Provider connection:** configured in OmniRoute dashboard or SQLite.
**Base URL for OmniRoute:** `http://127.0.0.1:8080/search` (includes `/search` — different from Hermes!)
**Cost:** $0/query, 999,999 free monthly quota

## OmniRoute blocks private/local SearXNG URLs by default

When SearXNG runs on a private IP (e.g., `192.168.0.222`, `127.0.0.1`, `10.x.x.x`), OmniRoute's outbound URL guard blocks the request with: `Blocked private or local provider URL`.

**Fix:** Set `OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS=true` in OmniRoute's docker-compose.yml:
```yaml
environment:
  - OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS=true
```

This is required whenever SearXNG runs on the same LAN as OmniRoute (which is the typical self-hosted setup).

## Bridge networking blocks outbound from SearXNG container

If SearXNG runs with Docker's default bridge networking, it may not reach external engines (Google, Bing, etc.) due to bridge network egress restrictions. Symptoms:
- Direct HTTPS IP probes from inside the container time out
- SearXNG returns 0 results with `unresponsive_engines` errors

**Fix:** Switch to `network_mode: host`:
```yaml
services:
  searxng:
    network_mode: host
    # Remove ports: mapping — host networking binds directly
```

**⚠️ PITFALL:** After switching to host networking, the container binds to port 8080 directly. Remove any `ports:` mapping. Update `SEARXNG_BASE_URL` to use port 8080.

## AceRoute integration

AceRoute (`/mnt/tb/1Apps/AceRoute`, `:8866`) — Search tab **🌐 SearXNG Engines** via `/api/health` → `collect_searxng_engines()`.

Set `SEARXNG_URL` in AceRoute docker-compose (host net: `http://127.0.0.1:8080`).

### ⚠️ PITFALL: `/stats` empty ≠ outage

Page may say **"There is currently no data available."** with HTTP 200 until metasearch traffic exists (`enable_metrics: true`). AceRoute must not show **Unavailable** — fallback to `/config` general engines (`listed` status). See `references/aceroute-engine-stats-fallback.md`.

## Verification checklist

```bash
# 1. Container running
docker ps --filter name=searxng

# 2. Port listening
ss -tlnp | grep :8080

# 3. Direct API test
curl -s "http://127.0.0.1:8080/search?q=test&format=json" | python3 -c "
import sys,json; d=json.load(sys.stdin)
print(f'Results: {len(d.get(\"results\",[]))}, Engines: {sorted(set(r[\"engine\"] for r in d.get(\"results\",[])))}')
"

# 4. OmniRoute test (from container)
docker exec omniroute node -e '
fetch("http://127.0.0.1:8080/search?q=test&format=json",{signal:AbortSignal.timeout(8000)})
.then(async r=>{console.log("HTTP",r.status);const d=await r.json();console.log("Results:",d.results?.length||0);})
.catch(e=>{console.log("FAIL:",e.message);process.exit(1);});
'

# 5. Engine stats
curl -s "http://127.0.0.1:8080/search?q=test&format=json" | python3 -c "
import sys,json; d=json.load(sys.stdin)
for e in d.get('unresponsive_engines',[]): print(f'  DEAD: {e[0]} — {e[1]}')
"
```
