# GDrive Trash Accumulation & Retention Policies

## Problem

The `plain_gdrive_daily_notify.py` cron job times out after 1200s (scheduler default). Root cause: **GDrive trash is massive** — `rclone delete --drive-trashed-only` takes extremely long (likely hundreds/thousands of trashed files from prior backups).

### Evidence

```bash
# rclone ls drseatop_google_drive_1779883937: --drive-trashed-only
# → times out after 60s
```

The backup script calls `empty_gdrive_trash()` which runs:
```python
subprocess.run([
    "rclone", "delete", "drseatop_google_drive_1779883937:",
    "--drive-trashed-only", "--drive-use-trash=false", "-q"
], check=False, timeout=300)
```

This 300s timeout inside the script + rclone's slow iteration = total timeout.

## Solutions

### Option A: Disable Trash Emptying (Recommended for Daily Plain Backups)

Edit `/root/.hermes/scripts/hermes_plain_backup.py` and comment out the `empty_gdrive_trash(dest_base)` call for daily plain backups. The daily backup doesn't need fresh trash emptying — weekly cleanup is sufficient.

### Option B: Increase Cron Script Timeout (Config Required)

In `/root/.hermes/config.yaml`:
```yaml
cron:
  script_timeout_seconds: 18000  # 5 hours instead of 1200s
```
**Note**: This requires user action since `config.yaml` is protected from agent writes.

### Option C: Manual Trash Cleanup

Run a one-time aggressive cleanup:
```bash
rclone delete drseatop_google_drive_1779883937: \
  --drive-trashed-only --drive-use-trash=false -v \
  --drive-server-side-across-configs
```
This may take hours. Run in a `screen`/`tmux` session.

### Option D: Separate Trash Cleanup Cron

Create a dedicated weekly cron for trash emptying with very long timeout, separate from daily backup cron.

## Retention Policies (Current)

| Backup Type | Schedule | Retention | Script |
|-------------|----------|-----------|--------|
| Daily Local Archive | 18:35 | Keep 3 | `daily_local_archive_notify.py` |
| Daily GDrive Archive | 18:40 | Keep 2 | `daily_gdrive_archive_notify.py` |
| Daily Mnemosyne | 18:00 | Keep 7 | `mnemosyne_backup.py` |
| Plain Local 6h | Every 6h | Keep 1 | `plain_local_6h.py` |
| Plain GDrive Daily | 21:00 | Keep 1 | `plain_gdrive_daily_notify.py` |

## Cron Timeout Configuration

The Hermes cron scheduler has a **global** `script_timeout_seconds` (default 120s) that applies to ALL `no_agent: true` scripts. Individual script timeouts (e.g., `subprocess.run(timeout=...)`) do NOT override this — the scheduler kills the process at the global limit.

### Current State (config.yaml)
```yaml
cron:
  script_timeout_seconds: 1200  # 20 minutes
```

### Required for Backups
- Daily core backup: ≥ 600s
- Weekly full backup: ≥ 900s
- GDrive plain daily (with trash): ≥ 18000s (or disable trash)

### Fix
User must edit `~/.hermes/config.yaml`:
```yaml
cron:
  script_timeout_seconds: 18000
```

## References

- `references/cron-timeout-vs-wrapper-timeout.md` — scheduler timeout vs wrapper timeout pattern
- Backup scripts: `/root/.hermes/scripts/hermes_{daily,weekly}_full_backup.py`
- Wrapper scripts: `/root/.hermes/scripts/{daily,weekly}_full_backup_notify.py`
- Plain backup: `/root/.hermes/scripts/hermes_plain_backup.py`