# Standalone Dashboard Scripts (No Plugin Required)

## Context

The `hermes-personal-dashboard` plugin was symlinked to `/tmp/hermes-personal-dashboard` which got cleaned up. The `personal_dashboard_core` module became unavailable, breaking cron jobs that depended on it.

## Solution: Standalone Scripts with Direct SQLite

Created three standalone scripts that work **without the plugin**:
- `/root/.hermes/scripts/hourly_dashboard_refresh.py` — Hourly frequent signal refresh (patches existing cards)
- `/root/.hermes/scripts/smart_refresh.py` — Daily briefing from cron outputs only (creates new cards)
- `/root/.hermes/scripts/planning_refresh.py` — Weekly planning refresh (creates 3 planning cards)

All scripts:
- Use direct SQLite access to `/root/.hermes/products/hermes-personal-dashboard/cards.db`
- Reimplement `upsert_card`, `record_refresh`, `utc_now`, `parse_time` locally
- No dependency on `personal_dashboard_core` module
- Zero AI tokens (`no_agent: true`)
- Run in <2 seconds

## Database Schema

```sql
CREATE TABLE cards (
    id TEXT PRIMARY KEY,
    domain TEXT NOT NULL,
    title TEXT NOT NULL,
    summary TEXT,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    source_label TEXT,
    why_shown TEXT,
    valid_until TEXT,
    updated_at TEXT,
    payload_json TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE refresh_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_key TEXT NOT NULL,
    status TEXT NOT NULL,
    summary TEXT,
    payload_json TEXT,
    started_at TEXT DEFAULT (datetime('now')),
    ended_at TEXT
);

CREATE TABLE evidence (...);
CREATE TABLE context_items (...);
```

## Cron Job Configuration

| Job ID | Name | Schedule | Script | Mode |
|--------|------|----------|--------|------|
| `1226201b634c` | Frequent Signal Refresh | `0 * * * *` | `hourly_dashboard_refresh.py` | `no_agent: true` |
| `766c28ecadaf` | Daily Briefing | `30 7 * * *` | `smart_refresh.py` | `no_agent: true` |
| `e6294690fee6` | Planning Refresh | `0 15 * * 5` | `planning_refresh.py` | `no_agent: true` |

All have `skills: []`, `model: null`, `provider: null`.

## Initialization

Run once before first use:
```bash
python3 /root/.hermes/scripts/init_dashboard_db.py
```

Or manually:
```python
import sqlite3
conn = sqlite3.connect('/root/.hermes/products/hermes-personal-dashboard/cards.db')
# Run CREATE TABLE statements above
```

## Key Differences from Plugin Core

| Aspect | Plugin Core | Standalone Scripts |
|--------|-------------|-------------------|
| Import | `from personal_dashboard_core import upsert_card` | Local `upsert_card()` function |
| Timestamp format | `utc_now()` → `2026-06-11T05:28:34Z` | Same |
| Validation | `normalize_time()` validates ISO-8601 | Same format required |
| `valid_until` | Must be `YYYY-MM-DDTHH:MM:SSZ` | Must use `strftime('%Y-%m-%dT%H:%M:%SZ')` |
| Payload | Dict with `ai_curated`, `relevance_score` | Same structure |

## Timestamp Format Critical

**Wrong**: `datetime.isoformat()` → `2026-06-11T05:00:00+00:00` (fails validation)
**Correct**: `datetime.strftime('%Y-%m-%dT%H:%M:%SZ')` → `2026-06-11T05:00:00Z` (passes)

All standalone scripts use the correct format.

## Usage

```bash
# Hourly
python3 /root/.hermes/scripts/hourly_dashboard_refresh.py

# Daily
python3 /root/.hermes/scripts/smart_refresh.py

# Weekly
python3 /root/.hermes/scripts/planning_refresh.py
```

## Pitfalls

1. **Plugin module unavailable** — Don't import `personal_dashboard_core`. Use local reimplementations.
2. **Timestamp format** — Must use `strftime('%Y-%m-%dT%H:%M:%SZ')`, not `isoformat()`.
3. **Database path** — Hardcoded to `/root/.hermes/products/hermes-personal-dashboard/cards.db`. Must exist.
4. **Cron output paths** — Scripts read from `/root/.hermes/cron/output/<JOB_ID>/`. Paths must match actual cron jobs.
5. **OpenRouter data** — Watch job may run silently (empty output). Fall back to heartbeat for budget data.

## Related Files

- `scripts/hourly_dashboard_refresh.py` — Hourly patcher
- `scripts/smart_refresh.py` — Daily briefing from cron outputs
- `scripts/planning_refresh.py` — Weekly planning cards
- `scripts/init_dashboard_db.py` — Database initialization
- `references/cron-output-parsing.md` — Regex patterns for cron outputs
- `references/card-templates.md` — Card JSON templates