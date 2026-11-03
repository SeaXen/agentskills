# Manifest History Plugin

Hermes **dashboard** sidebar tab for archiving **self-hosted Manifest** routing history past the 30-day dashboard window. **Not** the Manifest LLM router (`providers.manifest` / `auto`).

## Layout (correct format)

```
~/.hermes/plugins/manifest-history/dashboard/manifest.json
~/.hermes/plugins/manifest-history/dashboard/plugin_api.py
~/.hermes/plugins/manifest-history/dashboard/dist/index.js   # telemetry-style SDK UI
~/.hermes/scripts/manifest_history_fetch.py                # prefer .py over bash heredoc
~/.hermes/scripts/manifest_history_fetch.sh                # thin wrapper → venv python
~/.hermes/state/manifest_history_config.json
~/.hermes/data/manifest_history.db
```

Generic dashboard rules: `references/hermes-dashboard-plugin-format.md`.

## UI URL

`http://<host>:9119/manifest-history` after **full dashboard process restart**. `/plugin/manifest-history/` is invalid (SPA redirects home).

## UI style (Dr. Sagar)

Match **`hermes-telemetry`** dashboard plugin: `Card` + `Badge`, tab bar for ranges, `StatCard` grid (`border border-border`, `font-courier` table), `SDK.fetchJSON('/api/plugins/manifest-history/...')`. Do **not** ship a separate `style.css` unless CSP needs it — telemetry uses Tailwind-like utility classes from the host shell.

## Config (`manifest_history_config.json`)

```json
{
  "base_url": "http://192.168.0.222:2099/v1",
  "api_url": "http://192.168.0.222:2099/api/v1/messages",
  "api_key": "mnfst_...",
  "sync_source": "postgres",
  "postgres_container": "mnfst-postgres-1"
}
```

| Field | Notes |
|-------|--------|
| `base_url` | Hermes `custom_providers` / chat — `Authorization: Bearer` + `mnfst_` key |
| `api_url` | Dashboard REST — **not** `/api/v1/history` (404 on self-host) |
| `api_key` | Same `mnfst_` key for chat; **not** sufficient for `/api/v1/messages` alone |
| `sync_source` | **`postgres`** recommended for self-host archive |
| `postgres_container` | Default `mnfst-postgres-1` (compose project `mnfst`) |

## Auth pitfall (why HTTP fetch shows 0 rows)

| Endpoint | Auth | `mnfst_` agent key |
|----------|------|---------------------|
| `POST /v1/chat/completions` | `Authorization: Bearer` | works |
| `GET /api/v1/messages` | `X-API-Key` (dashboard key) | `Invalid API key` with `mnfst_` |
| `/api/v1/history` | — | **404** |

**Archive fix:** `sync_source: postgres` reads `public.agent_messages` via `docker exec … psql`. Rows are routing log metadata (`description`, model, tokens) — not full chat transcripts.

## Docker (LAN / provider DNS)

If custom providers (e.g. `router.bynara.id`) time out inside bridge networking but work on the host, both `manifest` and `postgres` services can use `network_mode: host` in compose. Then set `DATABASE_URL` to `127.0.0.1:5432` (not hostname `postgres`). Distroless manifest image has no shell — debug with host `curl` / `python3`, not `docker exec` tools.

## Fetch script pitfalls

- **Do not** use bash heredoc with `os.environ["CFG"]` without `export CFG` — causes `KeyError: 'CFG'`.
- Use **`manifest_history_fetch.py`** (single file) invoked by venv: `/usr/local/lib/hermes-agent/venv/bin/python3 ~/.hermes/scripts/manifest_history_fetch.py`
- Placeholder `PASTE_LOCAL_mnfst_KEY_HERE` → HTTP sync skips; **postgres sync still works** without a valid key.

## Cron

Job `manifest_history_archive` → script name under `~/.hermes/scripts/` only (Hermes cron rejects other paths).

## API routes

`/health`, `/data`, `/stats`, `/models`, `/models/all`, `/breakdown/models`, `/breakdown/providers`, `/breakdown/cost`, `/export`, `POST /fetch-now` — all under `/api/plugins/manifest-history/`.

| Route | Purpose |
|-------|---------|
| `/models/all` | Every distinct `model` in SQLite (dropdown), not range-filtered |
| `/breakdown/models?include_catalog=true&sort=tokens` | Catalog + usage merge |
| `/breakdown/providers?include_configured=true` | **All** `tenant_providers` from Postgres merged with archive usage |

UI ranges: 24h (`days=1`), 7d, 30d, 90d, 1y, all time (`9999`).

**View tabs (telemetry-style second row):** Overview · Models · Cost · Providers · Messages.

- **Overview:** summary stat cards + **Top models (by token use)**; optional “by cost” block only if any `cost_usd > 0`.
- **Providers:** not “providers that got traffic only” — merge `tenant_providers` (+ `label`, `is_active`) with `agent_messages` aggregates. Unused providers show `0 req` / **Used: no**. Typical: 9 configured, 3 with traffic.
- **Models tab (v1.3.3+):** merge **`tenant_providers.cached_models`** routing catalog (same as Manifest connect sync) with archive usage. Typical **~400+ catalog**, **3 used**. Badge **catalog** vs **yes**. Overview top models = usage-only, sorted by tokens.

## SQLite schema (dashboard parity)

Archive table should store Manifest `agent_messages` fields explicitly (not only JSON metadata):

`input_tokens`, `output_tokens`, `cost_usd`, `status`, `provider`, `agent_name`

UI: telemetry-style columns **When · Status · Model · Provider · Tok in · Tok out · Cost · Note**. Summary cards: Requests, Cost, Tokens in/out, Errors.

**Note column:** `description` in Postgres is often empty — same as Manifest history UI. Fill with `(status) routed <model>` when blank.

**Date filter:** SQL `WHERE replace(created_at, 'Z', '') >= ?` for ISO timestamps.

## Stale UI vs good data

| Check | Good | Stale |
|-------|------|-------|
| `sqlite3 … COUNT(*)` | > 0 | — |
| Tab stat cards | match DB | all `0` |
| Header badges | `api 1.3.x`, `sync: postgres` | missing version / old "API key missing" |
| Fix | — | restart dashboard **9119**, hard refresh |

Do **not** block **Fetch now** on `api_key` when `sync_source` is `postgres`.

## Verify

```bash
/usr/local/lib/hermes-agent/venv/bin/python3 ~/.hermes/scripts/manifest_history_fetch.py
sqlite3 ~/.hermes/data/manifest_history.db 'SELECT COUNT(*), SUM(input_tokens) FROM history;'
/usr/local/lib/hermes-agent/venv/bin/python3 -c "
import importlib.util; from pathlib import Path
spec=importlib.util.spec_from_file_location('m', Path.home()/'.hermes/plugins/manifest-history/dashboard/plugin_api.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
print(m.health()); print(m.stats(days=90))
"
```

Discovery (offline):

```bash
/usr/local/lib/hermes-agent/venv/bin/python3 -c "
import sys; sys.path.insert(0,'/usr/local/lib/hermes-agent')
from hermes_cli.web_server import _discover_dashboard_plugins
print([p['name'] for p in _discover_dashboard_plugins() if 'manifest' in p['name']])
"
```

Live tab: hard refresh or restart dashboard; `plugins.enabled` alone does not mount `plugin_api.py`.

## Providers vs Manifest Settings (operator FAQ)

**Why only 3 providers when Routing shows many?** The old Providers tab counted distinct `provider` values in **`agent_messages`** (actual traffic only). Manifest **`tenant_providers`** can list 9+ entries while only 3 ever routed in the archive window.

**Fix (v1.3.2+):** `breakdown_providers` runs:

```sql
SELECT tp.provider, tp.label, tp.is_active, tp.priority, cp.name, cp.base_url
FROM tenant_providers tp
LEFT JOIN custom_providers cp ON tp.custom_provider_id = cp.id
```

via `docker exec <postgres_container> psql`, then left-joins usage from SQLite. Requires dashboard host can `docker exec` the Manifest Postgres container (`mnfst-postgres-1` by default).

## Data source (user FAQ)

| User action | Reads |
|-------------|--------|
| Refresh / tabs | **SQLite** `~/.hermes/data/manifest_history.db` only |
| Fetch now / cron 03:00 | Postgres `agent_messages` → SQLite upsert |
| Providers tab (configured rows) | Live Postgres `tenant_providers` at request time |
| Models tab (catalog rows) | Live Postgres `cached_models` parse at request time |

Not live Manifest HTTP on every page load (except provider + catalog merges).

## vs Manifest :2099

Native dashboard uses **browser session** + `/api/v1/overview` and live SQL. Hermes tab uses **archive + same Postgres tables** for providers/catalog; it does **not** proxy overview timeseries without session cookie. See `references/manifest-dashboard-2099-parity.md`.