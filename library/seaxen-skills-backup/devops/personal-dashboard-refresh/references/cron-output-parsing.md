# Cron Output Parsing Patterns for Hermes Personal Dashboard

## Known Cron Jobs and Output Formats

### OpenRouter Free Model Watch (461aacc5be37)
**Schedule**: 30 18 * * * (daily 18:30)
**Output**: Markdown with structured fields

```markdown
# Cron Job: openrouter-free-model-and-charge-watch
**Job ID:** 461aacc5be37
**Run Time:** 2026-06-10 08:42:55
**Mode:** no_agent (script)

---

OpenRouter free-model watch alert
Checked: 2026-06-10T02:42:55.808336+00:00

Summary
- Severity: WARN
- Account: monthly $0.1120 / limit $0.1000 | daily $0.0000 | remaining limit $0.0000 | free tier no
- Free models: live 27 | new 1 | removed 1
- Watched set: available 3/6 | free 3/6
```

**Key regex patterns**:
- `Severity:\s*(\w+)`
- `Account:\s*([^\n]+)` → extract `monthly \$([\d.]+) / limit \$([\d.]+)`
- `Free models:\s*live\s*(\d+)`
- `Watched set:\s*available\s*(\d+)/(\d+)\s*\|\s*free\s*(\d+)/(\d+)`
- `New free models:\s*([^\n]+)`
- `Removed free models:\s*([^\n]+)`

### OpenRouter Heartbeat (4dd735fb568b)
**Schedule**: 45 18 * * * (daily 18:45)
**Output**: Similar format to watch, includes "Missing watched models" section

**Additional regex**:
- `Missing watched models:\s*([^\n]+)`

### Daily Local Archive (ba7107c4fe85)
**Schedule**: 35 18 * * * (daily 18:35)
**Output**: Emoji markdown format

```markdown
## 🌙✅ Hermes Daily Local Archive
`✅ SUCCESS · local daily archive complete`

- **📦 Archive:** `hermes-daily-full-backup-2026-06-09_18-35-31.tar.gz.gpg`
- **🏷️ Label:** `daily-full`
- **📏 Size:** 2068.40 MiB (2.02 GiB)
- **🗂️ Files:** `52311`
```

**Key regex patterns**:
- `SUCCESS|FAILED|script failed|timed out` (case-insensitive)
- `Size[^\d]*([\d.]+)\s*(MiB|GiB)`
- `Files[^\d]*(\d+)`
- `Archive[^`]*\`([^`]+)\``

### Daily GDrive Archive (7f1afb4aa1e8)
**Schedule**: 40 18 * * * (daily 18:40)
**Output**: Same format as local archive

### Daily Mnemosyne Backup (6b9cb09f0377)
**Schedule**: 0 18 * * * (daily 18:00)
**Output**: Similar emoji markdown format

```markdown
## 🧠✅ Mnemosyne Backup
`✅ SUCCESS · mnemosyne snapshot complete`

- **🕒 Timestamp:** `2026-06-09_12-00-30Z UTC`
- **🗂️ File:** `mnemosyne-backup-2026-06-09_12-00-30Z.sqlite.gz`
- **📦 Size:** 3.71 MiB (0.00 GiB)
```

### Obsidian Nightly Log (dcb20be29ebb)
**Schedule**: 55 23 * * * (daily 23:55)
**Output**: Collector text + agent response

Key signal: `"No durable items to log."` indicates no actionable vault changes.

### Bitwarden Fetch Watchdog (ba519c48e1d4)
**Schedule**: Every 15 minutes (interval)
**Output**: Minimal markdown, silent on success

```markdown
# Cron Job: bitwarden-fetch-watchdog
**Job ID:** ba519c48e1d4
**Run Time:** 2026-06-11 09:49:40
**Mode:** no_agent (script)
**Status:** silent (empty output)
```

**Key regex patterns**:
- `Status:\s*silent\s*\(empty output\)` -> healthy (no card needed, or "healthy" status card)
- `Status:\s*failed|error` -> alert card with priority: critical
- `Run Time:\s*([0-9\-: ]+)` -> last check timestamp

**Card pattern**: `bitwarden-secrets-health` (alerts, section: now, priority: medium when healthy, critical on failure)

## Implementation Notes

1. **Always use latest file by mtime**, not alphabetical sort
2. **Clear all cards first** on full refresh to avoid scanner noise accumulation
3. **Stable card IDs** per topic: `openrouter-budget-watch`, `backup-local-archive`, etc.
4. **Domain mapping**: alerts (budget, heartbeat), news (model changes), projects (backups, cron health)
5. **Priority mapping**: budget over limit → critical, missing watched models → high, backup success → medium/low
6. **Scanner cards** (from `refresh_from_hermes_context` with `create_cards=True`) produce noise — always use `create_cards=False` and manually curate
7. **Valid until**: Set to next daily refresh (e.g., `2026-06-11T07:30:00Z` for 7:30 AM daily briefing)

## Working Refresh Script Pattern

See `scripts/full-refresh.py` for a complete working implementation.

## Budget Extraction Fallback (Critical Pattern)

The OpenRouter Free Model Watch job (`461aacc5be37`) often produces **silent/empty output** (marked "silent (empty output)" in its cron log). The budget data (`monthly $X / limit $Y`) is **always present in the Heartbeat job output** (`4dd735fb568b`).

**Always parse budget from heartbeat as fallback:**

```python
def extract_budget(text):
    m = re.search(r'monthly\s*\$([\d.]+)\s*/\s*limit\s*\$([\d.]+)', text)
    if m:
        return float(m.group(1)), float(m.group(2))
    return None, None

# Primary: watch job
or_budget_current, or_budget_limit = extract_budget(openrouter_text)
# Fallback: heartbeat job (always has budget data)
if or_budget_current is None:
    or_budget_current, or_budget_limit = extract_budget(heartbeat_text)
```

This pattern is used in `scripts/hourly_dashboard_refresh.py` and `scripts/full-refresh.py`.