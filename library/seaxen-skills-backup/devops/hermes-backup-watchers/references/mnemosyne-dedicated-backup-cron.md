# Dedicated Mnemosyne backup cron (`mnemosyne_backup.py`)

Single-script `no_agent` job — no LLM wrapper. Distinct from `daily_full_backup_notify.py` (full Hermes home).

## Paths

- Script: `/root/.hermes/scripts/mnemosyne_backup.py`
- Source DB: `/root/.hermes/mnemosyne/data/mnemosyne.db`
- Dest: `/mnt/tb/hermes-backups/mnemosyne/`
- Retention: `KEEP = 7` (edit constant in script)

## Critical: success must print stdout

For `no_agent: true` cron jobs, **empty stdout = silent delivery** even when `last_status: ok`.

Always end successful runs with a compact multi-line message, e.g.:

```text
✅🧠 Mnemosyne backup OK
🕒 Time: 2026-05-31_02-50-20Z UTC
🗂️ File: mnemosyne-backup-2026-05-31_02-50-20Z.sqlite.gz
📦 Size: 0.44 MB
🔐 SHA256: ef7138e7d4c8d62d...
♻️ Retention: keep last 7 backups
```

## Delivery

- Set `deliver` to explicit Discord channel id, e.g. `discord:1509931712719884389` (`#mnemosyne-backup`).
- `last_status: ok` does **not** prove the user saw a post — verify stdout + channel.

## Verify artifact

```bash
python3 /root/.hermes/scripts/mnemosyne_backup.py
gzip -t /mnt/tb/hermes-backups/mnemosyne/mnemosyne-backup-*.sqlite.gz
sha256sum -c /mnt/tb/hermes-backups/mnemosyne/*.sha256
```

## Relation to daily Hermes full backup

Full daily archive under `hermes_backup_common.py` already includes `mnemosyne/` inside `/root/.hermes`. Dedicated Mnemosyne cron is for **fast point restore** and **separate notifications**, not because full backup misses the DB.