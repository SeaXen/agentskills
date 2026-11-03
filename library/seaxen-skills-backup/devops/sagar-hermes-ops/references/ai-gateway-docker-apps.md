# AI Gateway / Account Manager Docker Apps

Three AI gateway/router tools installed as Docker containers on this host (192.168.0.222). All use `--network host` so they're accessible on LAN IP directly.

## Antigravity Manager (:8045)

**Repo:** `lbjlaq/Antigravity-Manager` (v4.2.8)  
**Image:** `lbjlaq/antigravity-manager:latest` (412 MB)  
**What:** Converts Google/Anthropic web session tokens (OAuth) into standard API endpoints. Auto-rotates accounts on 429s, routes between free/pro/ultra tiers.  
**License:** CC-BY-NC-SA-4.0 (non-commercial)

```bash
docker run -d --name antigravity-manager \
  --network host \
  -e API_KEY=<your-invented-key> \
  -e WEB_PASSWORD=<your-password> \
  -v ~/.antigravity_tools:/root/.antigravity_tools \
  lbjlaq/antigravity-manager:latest
```

| Item | Value |
|------|-------|
| Web UI | `http://192.168.0.222:8045` |
| API base | `http://192.168.0.222:8045/v1` |
| Web login | `WEB_PASSWORD` env var |
| API key | `API_KEY` env var (you invent it) |
| Data | `/root/.antigravity_tools/` |

**Account storage:** `accounts/` dir (individual JSON files), `accounts.json` (index), `gui_config.json`, `proxy_logs.db`, `security.db`, `token_stats.db`.

**Adding accounts:** Prefer Web UI. App reads `accounts.json` index on every request, not by scanning `accounts/` dir. Manual file replacement requires `docker restart antigravity-manager` to reconcile index + DBs.

**Restart:** `docker restart antigravity-manager` (~3s, data persists in volume)

## OmniRoute (:20128)

**Repo:** `diegosouzapw/OmniRoute` (v3.8.37)  
**Image:** `diegosouzapw/omniroute:latest` (354 MB base, 788 MB web)  
**What:** AI gateway aggregating 231+ providers (50+ free). RTK+Caveman token compression (15-95%). MCP server (87 tools). MIT licensed.

```bash
# secrets must be long: JWT_SECRET >= 32 chars, API_KEY_SECRET >= 16 chars
# shell can truncate secrets with special chars - use single quotes or $(cat file)
JWT=$(openssl rand -base64 48)
APIKEY=$(openssl rand -hex 32)

docker run -d --name omniroute \
  --network host \
  -e JWT_SECRET="$JWT" \
  -e API_KEY_SECRET="$APIKEY" \
  -e INITIAL_PASSWORD=<dashboard-password> \
  -e DATA_DIR=/app/data \
  -v /mnt/tb/1Apps/omniroute/data:/app/data \
  --restart unless-stopped \
  diegosouzapw/omniroute:latest
```

| Item | Value |
|------|-------|
| Dashboard | `http://192.168.0.222:20128` |
| API base | `http://192.168.0.222:20128/v1` |
| Login | `INITIAL_PASSWORD` env var |
| Data | `/mnt/tb/1Apps/omniroute/data/` (HDD) |

**Pitfalls:**
1. **Secrets too short.** JWT_SECRET min 32 chars, API_KEY_SECRET min 16. Container crashes on startup with "Invalid web runtime environment" if too short.
2. **Data dir ownership.** Container runs as UID 1000 (node user). Host dir must be `chown -R 1000:1000`.
3. **Dashboard is a heavy SPA.** 21 MB JS across 769 files. First load slow (~30s+ over LAN). Browser cache makes subsequent loads fast. Server responds in 0.03s — not a backend issue.
4. **OAuth providers** (Antigravity, Qoder, Gemini CLI) need separate OAuth client secrets. API-key providers work out of the box.
5. **No Redis by default.** In-memory rate limiter. Redis opt-in via `REDIS_URL`.

**Image variants:** `:latest` (base, no Chromium) vs `:latest-web` (+Chromium/Playwright for web-cookie providers).

## Comparison

| | Antigravity | OmniRoute | Manifest |
|---|---|---|---|
| Port | 8045 | 20128 | 2099 |
| How | OAuth web sessions to API | 231+ providers aggregated | Your own API keys |
| Free models | Via web session | 50+ free providers | No (you pay) |
| Token compression | No | Yes (15-95%) | No |
| Dashboard | Basic | Full | Basic |
| Risk | ToS violation | Lower (aggregator) | None (your keys) |
