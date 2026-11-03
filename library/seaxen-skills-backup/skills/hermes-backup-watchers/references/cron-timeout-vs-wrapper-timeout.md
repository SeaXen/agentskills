# Cron Scheduler Timeout vs Wrapper Script Timeout

## The Mismatch

Hermes cron jobs with `no_agent: true` have **two timeout layers**:

1. **Wrapper script timeout** — `subprocess.run(cmd, timeout=...)` inside the Python script
2. **Hermes scheduler timeout** — Global setting in `config.yaml: cron.script_timeout_seconds`

The scheduler timeout **wins**. If the scheduler timeout is reached, the entire script process is killed, even if the inner subprocess had more time allocated.

## Default Values

| Layer | Default | Where Set |
|-------|---------|-----------|
| Scheduler | **120 seconds** | `~/.hermes/config.yaml` → `cron.script_timeout_seconds` |
| Wrapper (`hermes_daily_full_backup.py`) | 600s | Script default |
| Wrapper (`hermes_weekly_full_backup.py`) | 900s | Script default |
| Wrapper (`hermes_plain_backup.py`) | 14400s | Script default |

## Failure Mode

**Symptom**: Cron output shows:
```
Script timed out after 120s: /root/.hermes/scripts/daily_full_backup_notify.py
```

**But** the backup script itself allowed 600s. The 120s is the scheduler default.

## Fix

Edit `~/.hermes/config.yaml`:
```yaml
cron:
  script_timeout_seconds: 18000  # 5 hours — safe for all backup types
```

**Critical**: This config is in the protected `config.yaml`. The user must edit it directly or use `hermes config set`.

## Verification

After increasing timeout, verify cron jobs no longer show "Script timed out after 120s":

```bash
# Check recent cron output
cat /root/.hermes/cron/output/<JOB_ID>/<latest>.md
```

Should show backup completion, not timeout.

## Related Scripts

| Script | Default Timeout | Notes |
|--------|-----------------|-------|
| `hermes_daily_full_backup.py` | 600s | Core daily backup |
| `hermes_weekly_full_backup.py` | 900s | Weekly full backup |
| `hermes_plain_backup.py` | 14400s | Plain rsync backup (local + GDrive) |
| `daily_full_backup_notify.py` | 600s | Wrapper calls backup script |
| `weekly_full_backup_notify.py` | 900s | Wrapper calls backup script |
| `plain_local_6h_notify.py` | 14400s | Plain local wrapper |
| `plain_gdrive_daily_notify.py` | 14400s | Plain GDrive wrapper |

## Pitfall

**Don't just fix the wrapper timeout**. If you only increase `subprocess.run(timeout=...)` in the Python script, the scheduler will still kill at 120s. Both must be aligned.

## Best Practice

1. Set global `cron.script_timeout_seconds` to the maximum any cron job needs (e.g., 18000s for GDrive plain backup with trash)
2. Keep individual script timeouts at or below the global value
3. For GDrive daily plain backup: either disable trash emptying OR accept the 5-hour global timeout

## Related

- `references/gdrive-trash-and-retention.md` — GDrive trash causing timeout
- `deterministic-backup-cron-formatting.md` — wrapper script pattern