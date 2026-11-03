---
name: personal-dashboard-refresh
description: Refresh Hermes Personal Dashboard from cron outputs, memory, and sessions with high-signal cards. Extends the plugin briefing-curator skill with concrete parsing patterns and scripts.
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Dashboard, Personal, Cron, Refresh, Briefing, Parser]
    extends: hermes-personal-dashboard:briefing-curator
---

# Personal Dashboard Refresh

This skill captures the concrete implementation patterns for refreshing the Hermes Personal Dashboard with high-signal cards. It extends the plugin-provided `hermes-personal-dashboard:briefing-curator` skill with specific cron job output parsing, working scripts, and card templates.

## Operating Rules (supplements briefing-curator)

- **Always use `create_cards=False`** with `refresh_from_hermes_context` — scanner cards are noise
- **Read latest cron output by mtime**, not filename sort
- **Clear all cards first** on full refresh to avoid stale scanner cards
- **Use stable card IDs** per topic for idempotent updates across runs
- **Parse using regex patterns** specific to each cron job's markdown format
- **Cron job `skills` array must use full plugin prefix** — `hermes-personal-dashboard:briefing-curator`, not `briefing-curator`. Omitting the prefix causes Hermes to skip the skill and fall back to raw LLM execution (consuming tokens unnecessarily).

## Refresh Modes

### Full Daily Briefing (no-agent script)
- Job: `766c28ecadaf` (30 7 * * *)
- `no_agent: true`, `script: smart_refresh.py`, `skills: []`
- **No LLM** — pure Python parsing + direct core API calls
- **Creates new cards from scratch** (clears first with `DELETE FROM cards`)
- Runs in <2s, zero token cost
- See `scripts/full-refresh.py` (also `smart_refresh.py` for cron-output-only variant)

### Hourly Frequent Signal Refresh (no-agent script)
- Job: `1226201b634c` (0 * * * *)
- `no_agent: true`, `script: hourly_dashboard_refresh.py`, `skills: []`
- **No LLM** — pure Python parsing + direct core API calls
- **Patches existing cards** (updates `valid_until`, `updated_at`) — does NOT clear
- Runs in <1s, zero token cost
- See `scripts/hourly_dashboard_refresh.py`

### Planning Refresh (no-agent script)
- Job: `e6294690fee6` (Fri 15:00)
- `no_agent: true`, `script: planning_refresh.py`, `skills: []`
- **No LLM** — deterministic planning cards from cron outputs + user profile
- Creates/updates 3 stable planning cards with 2-week validity
- Runs in <1s, zero token cost
- See `scripts/planning_refresh.py`

## Known Cron Jobs & Parsing Patterns

See `references/cron-output-parsing.md` for detailed regex patterns per job.

### Job Map

| Job ID | Name | Schedule | Key Cards | Mode |
|--------|------|----------|-----------|------|
| 461aacc5be37 | OpenRouter Free Model Watch | 18:30 daily | `openrouter-budget-watch`, `openrouter-model-changes` | no_agent (script) |
| 4dd735fb568b | OpenRouter Heartbeat | 18:45 daily | `openrouter-heartbeat-alert` | no_agent (script) |
| ba7107c4fe85 | Daily Local Archive | 18:35 daily | `backup-local-archive` | no_agent (script) |
| 7f1afb4aa1e8 | Daily GDrive Archive | 18:40 daily | `backup-gdrive-archive` | no_agent (script) |
| 6b9cb09f0377 | Daily Mnemosyne Backup | 18:00 daily | `backup-mnemosyne` | no_agent (script) |
| dcb20be29ebb | Obsidian Nightly Log | 23:55 daily | `obsidian-nightly-log` | skill + LLM |
| ba519c48e1d4 | Bitwarden Fetch Watchdog | Every 15 min | `bitwarden-secrets-health` | no_agent (script) |
| 1226201b634c | Personal Dashboard Frequent Signal Refresh | Hourly (min 0) | Patches all active cards | **no_agent (script)** |
| 766c28ecadaf | Personal Dashboard Daily Briefing | 7:30 daily | Full dashboard refresh | **no_agent (script: smart_refresh.py)** |
| e6294690fee6 | Personal Dashboard Planning Refresh | Fri 15:00 | Planning cards | **no_agent (script: planning_refresh.py)** |
| (config) | All cron jobs | various | `cron-health-summary` | script |

## Card Templates

See `templates/` for ready-to-use card structures.
See `references/card-templates.md` for full JSON templates.

### Alert Cards (domain: alerts, section: now)
- Budget over limit → priority: critical
- Missing watched models → priority: high
- **Silent watchdog = healthy** → priority: medium (flips to critical on failure)

### News Cards (domain: news, section: today)
- Model additions/removals → priority: medium

### Project Cards (domain: projects, section: today/watching)
- Backup success → priority: medium (local/gdrive), low (mnemosyne)
- Cron health summary → priority: low
- Obsidian nightly result → priority: low

### Stocks/Crypto Cards (domain: stocks, section: now)
- **Real-time market data** from CoinGecko → priority: high
- Tickers payload with price, 24h/7d change, market cap, volume, ATH distance, dominance
- Valid until next refresh (typically 1h)

### Planning Cards (domain: planning, section: today)
- **Daily cron timeline** from jobs.json → priority: low
- Items array with label (time) and summary

## Scripts

- `scripts/full-refresh.py` — Complete working refresh implementation (daily briefing mode, clears all cards first)
- `scripts/hourly_dashboard_refresh.py` — No-agent hourly frequent signal refresh (patches existing cards, zero tokens)
- `scripts/planning_refresh.py` — No-agent weekly planning refresh (creates 3 planning cards, zero tokens)
- `scripts/verify-cards.py` — Verify card contents after refresh

## Pitfalls

1. **Alphabetical file sort** picks old files — always use `max(files, key=lambda f: f.stat().st_mtime)`
2. **Scanner cards** from `refresh_from_hermes_context(create_cards=True)` pollute dashboard with raw JSON/chats — never use
3. **Emoji markdown** in cron outputs breaks simple regex — use flexible patterns like `Size[^\d]*([\d.]+)\s*(MiB|GiB)`
4. **Size units** vary (MiB vs GiB) — normalize to GiB when > 1000 MiB
5. **Payload key** returned by `list_cards` is `payload` (dict), not `payload_json` (string)
6. **Plugin skill prefix required in cron jobs** — cron job `skills` arrays must use the full plugin-prefixed skill name (e.g., `hermes-personal-dashboard:briefing-curator`), not the bare skill name (`briefing-curator`). Omitting the prefix causes Hermes to skip the skill and fall back to raw LLM execution (consuming tokens).
7. **`personal_dashboard_upsert_card` requires `id` at top level** — not inside `payload`. The tool validates `id` as a required field separate from payload.
8. **Live data for stocks/crypto must be fetched fresh** — scanner context has no real-time prices. Use `web_search` + `web_extract` (CoinGecko) or MCP providers at refresh time.
9. **Set `valid_until` to next refresh time** for time-sensitive cards (e.g., +1h for hourly, +24h for daily) so they auto-expire if refresh fails.
10. **Bitwarden watchdog "silent" = healthy** — only creates alert card on failure. Update healthy card with latest check timestamp each run.
11. **Core API is Python module, not CLI** — The `personal_dashboard_*` operations are functions in `personal_dashboard_core` module, not standalone commands. Use `python3 -c "import sys; sys.path.insert(0, '/root/.hermes/plugins/hermes-personal-dashboard'); import personal_dashboard_core as c; c.upsert_card(...)"` or write scripts. See `references/core_api.md` for full reference.
12. **Deduplication: check existing cards first** — Always call `list_cards()` before creating new cards. Use stable IDs per topic. If duplicates are created, dismiss them with `dismiss_card()` rather than leaving stale cards. The existing stable cards (e.g., `openrouter-budget-watch`, `openrouter-heartbeat-alert`, `cron-health-summary`) have better data and should be preserved over auto-generated ones.
13. **Budget extraction fallback** — OpenRouter watch job may run silently (empty output). Always fall back to heartbeat output for budget data (`monthly $X / limit $Y`). See `parse_openrouter` in `scripts/full-refresh.py` and `extract_budget` in `scripts/hourly_dashboard_refresh.py`.
14. **Hourly refresh patches, doesn't clear** — Frequent signal refresh (`hourly_dashboard_refresh.py`) calls `upsert_card` on existing stable IDs to update `valid_until` and `updated_at` only. It does NOT clear all cards. This preserves historical card data while keeping freshness accurate.
15. **`valid_until` must be ISO-8601 UTC with `Z` suffix** — `personal_dashboard_core.normalize_time()` validates this. Use `datetime.strftime('%Y-%m-%dT%H:%M:%SZ')` format. Raw `isoformat()` produces +00:00 which fails validation.
16. **Plugin core module may be unavailable** — If `hermes-personal-dashboard` plugin is missing/moved, `personal_dashboard_core` cannot be imported. Use standalone scripts with direct SQLite access instead. See `references/standalone-scripts.md`.
17. **Cron job output capture may fail silently** — Jobs may show `last_status: ok` in scheduler but script exit code 1 in output file. Always check `/root/.hermes/cron/output/<JOB_ID>/<latest>.md` for actual result. See `references/cron-debugging.md`.
18. **BWS secrets not injected into cron subprocesses** — Cron scripts run as standalone Python processes and do NOT inherit Bitwarden-injected environment variables from the Hermes gateway. Scripts that need API keys (e.g., OpenRouter) must read from `.env` file or implement BWS CLI fallback. See `references/bws-secrets-in-cron.md`.

## Support Files

- `references/cron-output-parsing.md` — Regex patterns and output formats for all known cron jobs
- `references/card-templates.md` — Ready-to-use card JSON templates with field checklists
- `references/core_api.md` — Complete `personal_dashboard_core` module function reference with usage patterns
- `references/standalone-scripts.md` — Working standalone scripts that bypass plugin core module (direct SQLite)
- `references/cron-debugging.md` — Debugging cron job failures via output files and common error patterns
- `references/bws-secrets-in-cron.md` — BWS secrets handling in cron subprocesses
- `scripts/full-refresh.py` — Complete working refresh implementation (runnable)
- `scripts/hourly_dashboard_refresh.py` — No-agent hourly frequent signal refresh (patches existing cards, zero tokens)
- `scripts/smart_refresh.py` — No-agent daily briefing from cron outputs only (zero tokens)
- `scripts/planning_refresh.py` — No-agent weekly planning refresh (creates 3 planning cards, zero tokens)
- `scripts/verify-cards.py` — Post-refresh verification script