# Staging-Dir Leak: `.tmp-hermes-backup` and `.restore-tests`

## Problem (observed)

The backup and restore scripts create per-run staging directories under a top-level temp folder, write artifacts into them, then never clean them up. On a long-running system the staging area silently grows to tens of GB of **unencrypted** artifacts that already have encrypted copies in the final destination.

### Real example found on /mnt/tb

```text
.tmp-hermes-backup/   →  58 GB  (20 sub-dirs from May 29 → Jun 15)
.restore-tests/       →  3.8 GB (1 sub-dir from May 29)
```

`.tmp-hermes-backup/` contains:
- `hermes-archive-<id>/hermes-*.tar.gz` — pre-encryption intermediates
- `hermes-backup-<id>/sqlite/...` — partial in-progress backup state
- All `.tar.gz` files inside are **unencrypted**

`hermes-backups/` already holds the **encrypted** `.tar.gz.gpg` versions. The staging copies are pure redundancy.

## Why this happens

The backup script pattern in `/root/.hermes/scripts/` typically:

1. Creates `mkdir .tmp-hermes-backup/hermes-<id>/`
2. Builds the tarball into that staging dir
3. Encrypts it to the final destination (`hermes-backups/`)
4. **Never removes the staging dir on success or failure**

Same pattern applies to restore operations: `.restore-tests/hermes-restore-<id>/` holds `restore.tar.gz` plus an extracted `.hermes/` tree that nobody references after the test completes.

## Fix (code-level)

Add a final cleanup step to the backup script after the encrypted copy is verified:

```python
import shutil
from pathlib import Path

STAGING_ROOT = Path("/mnt/tb/.tmp-hermes-backup")
STAGING_ROOT_RESTORE = Path("/mnt/tb/.restore-tests")

def cleanup_staging(staging_dir: Path, label: str) -> int:
    """Remove a completed staging dir. Returns bytes reclaimed."""
    if not staging_dir.exists():
        return 0
    # Capture size before deletion for the notification
    total = sum(p.stat().st_size for p in staging_dir.rglob('*') if p.is_file())
    shutil.rmtree(staging_dir, ignore_errors=True)
    print(f"STAGING_CLEANED={label}|{staging_dir.name}|{total}")
    return total
```

Call sites:

```python
# After successful encrypted copy to final destination:
cleanup_staging(staging_archive_dir, label="archive")
cleanup_staging(staging_backup_dir, label="backup")
```

For restore tests, the test harness should call `cleanup_staging` after the test verdict is captured, even on failure (so failed tests don't leak staging either).

## Detection (one-shot audit)

Run periodically to find staging-dir leaks before they grow:

```bash
# Quick: any tmp/hermes-* or restore-tests dirs
du -sh /mnt/tb/.tmp-hermes-backup /mnt/tb/.restore-tests 2>/dev/null

# Detailed: which sub-dirs are biggest and oldest
ls -ltrd /mnt/tb/.tmp-hermes-backup/hermes-* 2>/dev/null | head -10

# Compare staging vs final: unencrypted tarballs already have .gpg copies?
for f in /mnt/tb/.tmp-hermes-backup/hermes-archive-*/*.tar.gz; do
  bn=$(basename "$f")
  ls /mnt/tb/hermes-backups/ 2>/dev/null | grep -q "^${bn}.gpg$" \
    && echo "REDUNDANT: $bn" \
    || echo "ACTIVE:   $bn"
done
```

Expected output during normal operation: zero `REDUNDANT` lines and zero `hermes-archive-*` / `hermes-restore-*` dirs older than the most recent run.

## What to do with an existing leak

Phased cleanup (do not just `rm -rf` everything):

1. **Identify redundant intermediates**: any `.tar.gz` in `.tmp-hermes-backup/hermes-archive-*/` whose name already exists as `.tar.gz.gpg` in `hermes-backups/`. These are pure duplication → safe to delete.
2. **Inspect in-progress state**: `.tmp-hermes-backup/hermes-backup-*/sqlite/` may be ongoing state from a slow or stuck backup. Check `systemctl status hermes-backup` and recent cron logs before touching these.
3. **One-off restore tests**: `.restore-tests/hermes-restore-*/` is a one-time artifact. If the test was completed and the system has been running fine since, the entire restore tree is safe to delete.

Suggested command (after the cross-check confirms redundancy):

```bash
# Redundant unencrypted intermediates only
rm -rf /mnt/tb/.tmp-hermes-backup/hermes-archive-*/

# Old one-off restore test
rm -rf /mnt/tb/.restore-tests/
```

Always announce size reclaimed in the next backup notification so the user can see the leak is being managed.

## Prevention checklist

- [ ] Backup script emits `STAGING_CLEANED=<label>|<dir>|<bytes>` after every successful run
- [ ] Wrapper script surfaces the total bytes reclaimed in the success notification
- [ ] Restore-test harness deletes its staging dir on both success and failure
- [ ] A monthly audit cron runs the detection commands above and posts the size to a notification channel
- [ ] Backup script aborts (and surfaces `STAGING_LEAK_DETECTED`) if the staging dir is unexpectedly large at the start of a run
