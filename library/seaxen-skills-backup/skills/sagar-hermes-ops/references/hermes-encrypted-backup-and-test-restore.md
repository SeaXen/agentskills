# Hermes encrypted backup and test-restore

Use when Dr. Sagar wants disaster-recovery protection for the live Hermes home or wants proof that a backup is actually restorable.

## Recommended shape
- Treat `/root/.hermes` as the real live Hermes home unless `samefile` checks prove otherwise.
- If another visible path like `/mnt/tb/hermes` points to the same data, verify with `realpath` / `samefile` before calling it a second copy.
- Prefer a **single-file encrypted archive** over live-folder sync for portability and restore safety.
- Good default format: `hermes-backup-YYYY-MM-DD_HH-MM-SS.tar.gz.gpg`
- Keep retention low and explicit: usually last 2-3 backups.
- For clock-specific daily runs, use a fixed cron expression, not `every 24h`.

## What to preserve
A full-home backup of `~/.hermes` preserves the important Hermes state:
- `config.yaml`
- `.env`
- `auth.json`
- `state.db`
- `sessions/`
- `skills/`
- `plugins/`
- `cron/`
- `memories/`

## Why archive+encrypt beats live sync here
- single portable artifact
- easier retention pruning
- safer migration to another VPS
- does not rely on cloud mounts supporting symlinks or SQLite-heavy live access

## Google Drive / FUSE pitfall
If a cloud/FUSE mount rejects symlink creation with `Input/output error`, do not try to make it a live Hermes alias. Use it as a backup destination only.

## Manual restore proof pattern
A backup is not "verified" just because `tar` created a file. Prove restoreability:

1. Pick the latest `.tar.gz.gpg` backup.
2. Restore into a throwaway directory like `/tmp/hermes-restore-test-<timestamp>/`.
3. Decrypt and extract there.
4. Verify expected files/dirs exist under restored `.hermes/`.
5. Point Hermes at the restored home with `HERMES_HOME=<restored> hermes ...`.
6. Check at least:
   - `hermes config path`
   - `hermes config env-path`
   - `hermes profile list`
   - `hermes cron list`
7. Report clearly that this is a **point-in-time snapshot**, so differences from current live state after backup creation are expected.

## Interpretation rule
If restored Hermes commands work and the expected state files exist, call the backup **restorable** even if file sizes or counts differ from the current live tree. That mismatch usually means the live system changed after the backup timestamp.

## Do not overclaim
- Do not call the restored tree byte-identical to current live state unless the backup was taken immediately before comparison.
- Do not claim a cloud mount can be a live alias when symlink creation fails.
- Do not recommend GitHub as the normal destination for multi-GB secret backups.
