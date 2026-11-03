---
name: omniroute-update
description: Safe update pattern for OmniRoute Docker deployment on DietPi server
tags: [docker, omniroute, update, backup]
---

# OmniRoute Safe Update Pattern

## Context
OmniRoute is a self-hosted AI gateway running as a Docker container at `/mnt/tb/1Apps/omniroute`. Data volume contains encryption keys (`server.env`) and SQLite database (`storage.sqlite`). **Never** `docker rm` without preserving keys — they are auto-generated on first launch and cannot be recovered.

## Safe Update Steps (MUST follow in order)

**Preferred:** `/mnt/tb/1Apps/omniroute/update.sh` (backup + pull + recreate + health poll).

### 1. Backup BEFORE touching anything
```bash
bash /mnt/tb/1Apps/omniroute/backup.sh
```
Saves `server.env` + `storage.sqlite` to `/mnt/tb/1Apps/omniroute/backups/<timestamp>/`

### 2. Pull new image WITHOUT stopping anything
```bash
docker pull diegosouzapw/omniroute:latest
```

### 3. Recreate via compose (preserves volumes + data)
```bash
cd /mnt/tb/1Apps/omniroute && docker compose up -d --force-recreate
```

**Hermes agent pitfall:** Foreground `docker compose up -d` may be rejected as a “long-lived server”. Use `update.sh`, or `background=true` on compose, or **equivalent `docker run`**:

```bash
docker stop omniroute && docker rm omniroute
docker run -d --name omniroute --restart unless-stopped --network host \
  --env-file /mnt/tb/1Apps/omniroute/data/server.env \
  -e OMNIROUTE_ALLOW_PRIVATE_PROVIDER_URLS=true \
  -v /mnt/tb/1Apps/omniroute/data:/app/data \
  diegosouzapw/omniroute:latest
```

Verify: `STORAGE_ENCRYPTION_KEY` set in container; `curl` to `http://127.0.0.1:20128/` — **307** OK while warming; wait for **healthy**.

### 4. Verify
```bash
docker ps --filter name=omniroute --format "table {{.Names}}\t{{.Status}}"
# Check container is healthy
cat /mnt/tb/1Apps/omniroute/data/server.env | head -5
# Check encryption keys still there
sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite "SELECT count(*) FROM provider_connections;"
# Check providers still in DB
```

## CRITICAL RULES
- **NEVER** `docker rm` + recreate without compose
- **NEVER** wipe `/mnt/tb/1Apps/omniroute/data/` — keys are unrecoverable
- **ALWAYS** backup first, even for minor updates
- The `docker-compose.yml` at `/mnt/tb/1Apps/omniroute/docker-compose.yml` ensures volumes persist across recreates
- Encryption keys (`JWT_SECRET`, `STORAGE_ENCRYPTION_KEY`, `API_KEY_SECRET`) are in `data/server.env`
- Browser session cookies become invalid if JWT_SECRET changes (user must re-login)
- **Keep backups minimal** for this user: retain only the latest 1–2 backups, not a large archive. The current `backup.sh` keeps the last 2 backups and removes older ones automatically.

## Cost / Pricing Overrides
- OmniRoute pricing overrides are accessible via HTTP API even when the dashboard UI is flaky.
- Useful endpoints:
  - `GET /api/pricing/models` → provider alias catalog + model lists
  - `GET /api/pricing?includeSources=1` → current pricing + source map
  - `PATCH /api/pricing` with body `{ alias: { modelId: { input, output, cached, reasoning, cache_creation }}}`
- Important alias discovery lesson: dashboard labels may not match API aliases. Example from this environment:
  - Codex dashboard section → API alias `cx`
  - ChatGPT Web dashboard section → API alias `cgpt-web`
- For subscription-backed providers (Codex, ChatGPT Web), setting all 5 rates to `0` via the API is a reliable workaround when analytics should show `$0` cost.
- See `references/pricing-overrides-api.md` for the exact alias-discovery and PATCH workflow.

- **ALWAYS** backup first, even for minor updates
- **Keep only last 2 backups** — auto-delete older ones (user preference: no junk)
- The `docker-compose.yml` at `/mnt/tb/1Apps/omniroute/docker-compose.yml` ensures volumes persist across recreates
- Encryption keys (`JWT_SECRET`, `STORAGE_ENCRYPTION_KEY`, `API_KEY_SECRET`) are in `data/server.env`
- Browser session cookies become invalid if JWT_SECRET changes (user must re-login)

## Lessons Learned (from data-loss incident 2026-06-29)
- `docker stop` + `docker rm` WITHOUT `docker-compose.yml` loses encryption keys if they were auto-generated inside the container
- Never wipe `data/` during recovery — keys are unrecoverable once deleted
- Always backup BEFORE any destructive operation, even if you think it's safe
- The `--force-recreate` flag with compose is the correct way to swap container images
- Browser session cookies become invalid after JWT_SECRET rotation — user must re-login (this is expected, not a bug)

## Backup Retention
Keep only last 2 backups. User explicitly requested minimal retention — old backups are junk after a successful update. The `backup.sh` script auto-deletes backups older than the most recent 2.

## Combo Troubleshooting
OmniRoute combos route AI traffic through configurable strategies. Key things to check when combos misbehave:

### Health Warnings (from Combo Monitoring page)
- **"Quota is nearly exhausted"** — provider accounts running low on quota. Add more providers/models as fallbacks.
- **"Traffic distribution is highly skewed"** — expected when combo has only 1 model. Add more targets to fix.
- **Low success rate** — check provider connectivity, API keys, account status.

### Single-Model Combos Are Pass-Throughs
A combo with only 1 model always routes to that model. It adds ~0 overhead but provides no fallback. To get real routing benefit, add 2+ models.

### Strategies
- **FUSION** — good for provider/model fusion logic, but wrong when the goal is to pool many same-quota accounts as one large quota bucket.
- **PRIORITY** — preferred when the user wants multiple accounts to behave like one pooled subscription/quota source. OmniRoute sticks to one dynamic account until it hits quota/error, then fails over to the next account automatically, including mid-session.
- **INTELLIGENT** — auto-combo with 12-factor scoring (health, quota, cost, latency, etc.)
- See auto-routing catalog for 17 built-in `auto/*` combos (auto, auto/fast, auto/cheap, auto/coding, auto/reliable, auto/free)

### Account Pooling Behavior
When a combo step uses **dynamic account** selection, OmniRoute does **not** round-robin usage evenly across accounts. It is sticky: one account may carry most or all visible usage until quota/error forces failover, then another account takes over. This is expected behavior, not necessarily a bug.

If the user's goal is "10 accounts should act like 1 pooled quota source," use:
- one provider/model target
- dynamic account selection
- **PRIORITY** strategy

Do **not** expect analytics to show perfectly even token distribution across equal-quota accounts.

### Cost Tracking Caveat
Subscription-backed providers/accounts (e.g. Codex subscription, ChatGPT Web cookie-backed access, grok-web-style subscription paths) may still show estimated token cost in OmniRoute analytics even when actual billing is flat-rate/$0. This is a product limitation in OmniRoute cost accounting, not proof of real per-token billing.

### Monitoring Commands
```bash
# Check combo health via logs
docker exec omniroute tail -50 /app/logs/application/app.log | grep -iE "combo|fusion|health|quota"
# Check provider count
sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite "SELECT count(*) FROM provider_connections;"
```

### grok-web Cookie Auth (Known Broken)
`grok-web` cookie validation is broken in OmniRoute (issues #3063, #5350). Do NOT rely on it. Use xAI API key or OpenRouter instead. See `references/grok-web-cookie-setup.md` for details.

## Combos & Routing
See `references/combo-strategies.md` for strategy selection, account pool setup, and auto-combo config.

## Edge relay proxy pool (Vercel / Deno / CF)

- `references/relay-proxy-auth.md` — 401 vs 500 decision tree, `env_file`, decrypt notes
- `references/vercel-relay-resolveRelayTarget-6149.md` — upstream `api/relay.js` bug ([#6149](https://github.com/diegosouzapw/OmniRoute/issues/6149))
- `scripts/probe-edge-relay.sh` — host-side probe (same headers as dashboard Test)

Compose **must** include `env_file: - ./data/server.env` or relay tests show `no relay auth token`. If key is loaded and Test still **500** with Vercel `resolveRelayTarget is not defined`, skip built-in relays; use `http://127.0.0.1:20128/v1` and external Cloudflare Tunnel.

## Infrastructure
- Container name: `omniroute`
- Image: `diegosouzapw/omniroute:latest`
- Port: 20128 (host networking)
- Data volume: `/mnt/tb/1Apps/omniroute/data:/app/data`
- Compose file: `/mnt/tb/1Apps/omniroute/docker-compose.yml`
- Backup script: `/mnt/tb/1Apps/omniroute/backup.sh`
- Update script: `/mnt/tb/1Apps/omniroute/update.sh`
- Logs inside container: `/app/logs/application/app.log`
