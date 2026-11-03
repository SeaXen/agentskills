# Mega Hard-Delete Retention Pattern

## Problem

Mega's rclone backend does not expose trash via `rclone lsd Mega:trash` — the trash directory is not accessible. `rclone backend help mega` confirms no backend commands exist for trash management.

This means:
- Cannot empty trash automatically via rclone
- Old backups deleted via `rclone delete` go to trash (consuming quota)
- Manual trash emptying via web UI is not automatable

## Solution: `--mega-hard-delete`

Mega backend supports `--mega-hard-delete` flag on `rclone delete` — permanently removes files **bypassing trash entirely**.

```bash
rclone delete Mega:Hermes-backups/#plain/old-backup-folder --mega-hard-delete
```

## Verification

```bash
# Test hard delete works
echo "test" > /tmp/test.txt
rclone copy /tmp/test.txt Mega:Hermes-backups/#plain/test.txt
rclone lsf Mega:Hermes-backups/#plain/        # shows test.txt
rclone delete Mega:Hermes-backups/#plain/test.txt --mega-hard-delete
rclone lsf Mega:Hermes-backups/#plain/        # test.txt is gone
```

## Prune Function Template

```python
def prune_old_mega(remote_base: str, prefix: str, suffix: str, keep: int) -> list[str]:
    """Prune old copies for Mega remote using hard delete."""
    try:
        result = subprocess.run(
            ["rclone", "lsf", remote_base, "--files-only", "-R"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            return []
        files = [
            line.strip() for line in result.stdout.strip().splitlines()
            if line.strip().startswith(prefix) and line.strip().endswith(suffix)
        ]
        files.sort(reverse=True)
        removed = []
        for old in files[keep:]:
            try:
                subprocess.run(
                    ["rclone", "delete", f"{remote_base}/{old}", "--mega-hard-delete"],
                    check=True, timeout=300
                )
                removed.append(old)
            except Exception:
                pass
        return removed
    except Exception:
        return []
```

## Comparison: GDrive vs Mega Retention

| Aspect | GDrive | Mega |
|--------|--------|------|
| Trash accessible via rclone | Yes (`--drive-trashed-only`) | No (directory not found) |
| Trash emptying | `rclone delete --drive-trashed-only` | N/A |
| Retention delete | `rclone delete` (moves to trash) | `rclone delete --mega-hard-delete` |
| Manual cleanup needed | Yes (periodic trash empty via web or cron) | **No** — hard delete purges permanently |
| Quota accounting | Trash counts against quota until emptied | Hard delete frees quota immediately |

## Applied in This Setup

- **Plain backup:** `/root/.hermes/scripts/hermes_plain_backup_mega.py` — calls `prune_old_mega()` with `--mega-hard-delete`
- **Archive backup:** `/root/.hermes/scripts/hermes_mega_archive_backup.py` — calls `prune_old_mega()` with `--mega-hard-delete`
- **Cron jobs:**
  - `daily-hermes-mega-plain` at 19:15 (keep 2)
  - `daily-hermes-mega-archive` at 19:45 (keep 2)

## Mega Account Details

- Email: `pelagikx+m1@gmail.com`
- No 2FA (required for automation)
- Total: 50 GiB, Free: 28.55 GiB (after 21.45 GiB used)
- Remote name: `Mega:`
- Backup path: `Mega:Hermes-backups/`