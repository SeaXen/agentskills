# Cron Job Debugging Patterns

## Quick Diagnosis

### 1. List All Jobs
```bash
cronjob(action='list')
```

### 2. Check Recent Output
```bash
ls -la /root/.hermes/cron/output/<JOB_ID>/ | tail -5
cat /root/.hermes/cron/output/<JOB_ID>/<LATEST>.md
```

### 3. Check Session Database
```bash
sqlite3 /root/.hermes/state.db "
  SELECT id, source, model, message_count, started_at
  FROM sessions
  WHERE source='cron'
  ORDER BY started_at DESC LIMIT 10;
"
```

## Common Error Patterns

### Script Not Found
```
Script not found: /root/.hermes/scripts/smart_refresh.py
```
**Fix:** Copy script to `/root/.hermes/scripts/` or correct script name in cron job.

### Module Not Found
```
ModuleNotFoundError: No module named 'personal_dashboard_core'
```
**Fix:** Plugin not available. Use standalone script with direct SQLite (see `references/standalone-scripts.md`).

### Database Unable to Open
```
sqlite3.OperationalError: unable to open database file
```
**Fix:** Create DB directory and run init:
```bash
mkdir -p /root/.hermes/products/hermes-personal-dashboard
python3 init_dashboard_db.py
```

### Discord Delivery Failed
```
delivery error: Discord send failed: Cannot connect to host discord.com:443 ssl:default [Temporary failure in name resolution]
```
**Root cause:** Network/DNS intermittent issue. Script execution succeeded (`last_status: ok`), only notifications failed.
**Action:** No script fix needed. Check network connectivity.

### Script Timeout
```
Script timed out after 120s: /root/.hermes/scripts/plain_gdrive_daily_notify.py
```
**Root cause 1:** GDrive trash massive → `rclone delete` hangs
**Root cause 2:** Hermes cron scheduler timeout (default 120s) < wrapper internal timeout
**Fix:** Increase `cron.script_timeout_seconds` in `/root/.hermes/config.yaml` to 18000 (5h). Or disable trash emptying in backup script.

### OpenRouter API Key Missing
```
OpenRouter watch error: OPENROUTER_API_KEY not found.
```
**Fix:** Add real API key to `/root/.hermes/.env`:
```
OPENROUTER_API_KEY=***
```

### 401 Unauthorized
```
OpenRouter watch error: HTTP 401 while querying OpenRouter.
```
**Fix:** API key invalid/expired. Generate new key at https://openrouter.ai/keys.

## Debugging Workflow

1. **Identify failing jobs** from `cronjob(action='list')` - look for `last_status: error`
2. **Read latest output** in `/root/.hermes/cron/output/<JOB_ID>/`
3. **Run script manually** to see full stderr:
   ```bash
   cd /root/.hermes/scripts && python3 <script>.py
   ```
4. **Check dependencies** - API keys, network, disk space, mounts
4. **Fix root cause** - script, config, or environment
5. **Re-run via cron** to verify:
   ```bash
   cronjob(action='run', job_id='<JOB_ID>')
   ```
6. **Verify output** - should show `Mode: no_agent (script)` and `Status: ok`

## Job-Specific Checks

| Job | Script | Common Issues |
|-----|--------|---------------|
| OpenRouter watch/heartbeat | `openrouter_free_watch.py` | Missing API key, 401, network |
| Daily archive/backup | `*_notify.py` | Discord delivery, rsync failures, timeout |
| GDrive plain backup | `plain_gdrive_daily_notify.py` | **GDrive trash huge (timeout)** |
| Dashboard refresh | `*_dashboard_refresh.py` | Script not found, DB missing |
| Mnemosyne backup | `mnemosyne_backup.py` | Discord delivery |
| Obsidian nightly | `obsidian_nightly_hybrid_full.py` | LLM token cost, skill not found |

## Verification Commands

```bash
# Test script directly
cd /root/.hermes/scripts && python3 hourly_dashboard_refresh.py

# Verify DB state
sqlite3 /root/.hermes/products/hermes-personal-dashboard/cards.db \
  "SELECT id, title, updated_at FROM cards ORDER BY updated_at DESC LIMIT 10;"

# Check next run time
cronjob(action='list') | jq '.jobs[] | select(.enabled) | {id: .job_id, name: .name, next: .next_run_at}'

# Network test
ping -c 2 discord.com
ping -c 2 api.openrouter.ai
```