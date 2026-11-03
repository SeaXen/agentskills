# AceRoute Analytics Dashboard

**URL:** `http://192.168.0.222:8866`
**Location:** `/mnt/tb/1Apps/AceRoute`
**Git:** `SeaXen/AceRoute` (private)
**Docker:** `aceroute` container, `network_mode: host`, `restart: unless-stopped`
**Port:** 8866

## Architecture

```
AceRoute (FastAPI + Chart.js SPA)
├── OmniRoute call_logs  ← search + extract requests
├── OmniRoute SQLite     ← provider health/connections
├── SearXNG /stats       ← engine health
├── Hermes config.yaml   ← backend detection
└── Hermes debug logs    ← web_tools_debug_*.json
```

## API Endpoints (22)

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Dashboard SPA |
| `/api/overview` | GET | Overview stats |
| `/api/providers` | GET | Per-provider stats |
| `/api/costs` | GET | Cost analysis |
| `/api/timeline` | GET | Search volume timeline |
| `/api/queries` | GET | Query analytics |
| `/api/health` | GET | Provider health + SearXNG engines |
| `/api/searxng/engines` | GET | SearXNG engine stats |
| `/api/search-test` | POST | Live search tester (proxies to OmniRoute) |
| `/api/extract-test` | POST | Live extract tester (calls Tavily directly) |
| `/api/errors` | GET | Failed searches |
| `/api/latency-timeline` | GET | Latency trend per provider |
| `/api/zero-results` | GET | Zero-result queries |
| `/api/monthly-summary` | GET | Monthly summary stats |
| `/api/compare` | GET | Provider comparison |
| `/api/export/csv` | GET | CSV export |
| `/api/extract` | GET | Web extract analytics |
| `/api/hermes-activity` | GET | Search vs extract split (Hermes debug) |
| `/api/content-sizes` | GET | Content size analytics (Hermes debug) |
| `/api/domains` | GET | Top extracted domains (Hermes debug) |
| `/api/ssrf-blocks` | GET | SSRF block log (Hermes debug) |
| `/api/truncation` | GET | Truncation report (Hermes debug) |
| `/api/tool-timeline` | GET | Tool call timeline (Hermes debug) |
| `/api/healthz` | GET | Docker healthcheck |

All endpoints support `?from=YYYY-MM-DD&to=YYYY-MM-DD` date filtering.

## Data Sources

### Primary: OmniRoute call_logs
- Path: `/mnt/tb/1Apps/omniroute/data/call_logs/`
- JSON files per request with `summary` (provider, status, duration, model) and `requestBody`/`responseBody`
- Mounted into container as `/data/omniroute/call_logs:ro`

### Secondary: OmniRoute SQLite
- Path: `/mnt/tb/1Apps/omniroute/data/storage.sqlite`
- Provider health, connection status, test results
- Mounted as `/data/omniroute/storage.sqlite:ro`

### Tertiary: Hermes Debug Logs
- Path: `/root/logs/web_tools_debug_*.json` (mounted as `/data/hermes-logs:ro`)
- Only populated when `WEB_TOOLS_DEBUG=true` in `~/.hermes/.env`
- **PITFALL:** OmniRoute search plugin bypasses debug logging. Only direct backends write logs.

### Config Detection
- Mounts `~/.hermes/config.yaml` as `/data/hermes-config.yaml:ro`
- Detects `web.extract_backend` setting
- Checks env vars for TAVILY/EXA/FIRECRAWL API keys

## Dashboard Sections (22)

1. Live Search Tester
2. Live Extract Tester
3. Overview Stats (5 cards)
4. Monthly Summary (4 cards)
5. Search Volume Timeline (7 days)
6. Latency Trend by Provider
7. Provider Breakdown (table)
8. Cost Analysis (chart + monthly projection)
9. Free Tier Usage (progress bars)
10. Cost by Provider (doughnut)
11. Daily Cost (bar chart)
12. Provider Comparison (grouped bar)
13. Provider Health (table)
14. SearXNG Engines (table)
15. Top Queries (list)
16. Recent Queries (table)
17. Error/Failure Log
18. Zero-Result Queries
19. Web Extract Analytics
20. Hermes Activity Split (search vs extract)
21. Content Size Analytics
22. Domain Extraction Map
23. SSRF Block Log
24. Truncation Report
25. Tool Call Timeline

## Theme System

- **Amber Dark** (default): Gold accent `#ffac02`, dark background
- **Tinybird**: Neon green `#00E67A` on `#000000`, Inter/Space Grotesk
- CSS files: `static/themes/default.css`, `static/themes/tinybird.css`
- JS: `static/js/theme.js` with localStorage persistence
- Switchable from header dropdown

## Mobile Responsiveness

- Separate CSS file: `static/css/mobile.css`
- Loaded via `<link media="(max-width:1024px)">` — zero desktop impact
- Three breakpoints: 1024px (tablet), 768px (mobile), 480px (small phones)
- Stacked header, 2-col grids, horizontal-scroll tables, 40px touch targets

## Secrets Management

- `.env` file (gitignored) with `TAVILY_API_KEY`, `EXA_API_KEY`
- Docker compose uses `env_file: .env` directive
- Non-secret env vars stay inline in docker-compose.yml

## Cost Tracking

Free tier limits:
| Provider | Free Monthly | Cost Per Query |
|---|---|---|
| serper | 2500 | $0.001 |
| brave | 1000 | $0.005 |
| exa | 1000 | $0.007 |
| tavily | 1000 | $0.008 |
| searxng | unlimited | $0 |
| duckduckgo | unlimited | $0 |

Only queries exceeding free tier are charged. Calculation done in 3 code paths (overview, providers, costs).

## Docker Deployment

```bash
cd /mnt/tb/1Apps/AceRoute
docker compose up -d --force-recreate  # deploy
docker compose build --no-cache        # force rebuild if stale cache
docker compose logs --tail 50 aceroute # check logs
```

PITFALL: `docker compose restart` does NOT reload `.env` — use `--force-recreate`.
PITFALL: `COPY . .` may use stale cache — use `build --no-cache` if code doesn't update.
PITFALL: Dockerfile needs `curl` for healthcheck (slim images don't include it).
