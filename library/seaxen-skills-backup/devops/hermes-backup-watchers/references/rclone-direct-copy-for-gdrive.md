# rclone Direct Copy for GDrive Backups

## Problem

Backing up 4.9GB of small files (Hermes home: ~50K files) via rsync to the rclone FUSE mount (`/mnt/drseatop_google_drive_1779883937/...`) is **extremely slow** — the plain daily backup timed out after 1200s (scheduler limit) without completing.

## Solution: rclone Copy Direct to Remote

Use `rclone copy` directly to the remote (e.g., `drseatop_google_drive_1779883937:Hermes-backups/#plain/...`) instead of rsync to the FUSE mount. This bypasses FUSE entirely and uses rclone's native GDrive API with parallel transfers.

### Key rclone Command

```bash
rclone copy /root/.hermes/ drseatop_google_drive_1779883937:Hermes-backups/#plain/hermes-plain-2026-06-13_01-00 \
  --exclude ".cache/**" \
  --exclude ".venv/**" \
  --exclude "__pycache__/**" \
  --exclude "*.log" \
  --exclude "tmp/**" \
  --fast-list \
  --transfers 4 \
  --checkers 8 \
  --drive-chunk-size 64M
```

### Flag Reference

| Flag | Value | Why |
|------|-------|-----|
| `--fast-list` | (boolean) | Fewer LIST API calls for large dirs |
| `--transfers` | 4 | Parallel uploads (4 files at once) |
| `--checkers` | 8 | Parallel existence checks |
| `--drive-chunk-size` | 64M | Large chunks = fewer API round trips |
| `--exclude` | patterns | Skip cache/venv/pycache without walking |
| `-P` / `--progress` | (boolean) | For manual runs; omit in scripts |

### Python Implementation

```python
def run_rclone_copy(src: Path, dst_remote: str) -> bool:
    cmd = [
        "rclone", "copy",
        "--exclude", ".cache/**",
        "--exclude", ".venv/**",
        "--exclude", "__pycache__/**",
        "--exclude", "*.log",
        "--exclude", "tmp/**",
        "--fast-list",
        "--transfers", "4",
        "--checkers", "8",
        "--drive-chunk-size", "64M",
        str(src) + "/",
        dst_remote
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)
    if result.returncode != 0:
        print(f"RCLONE_ERROR={result.stderr.strip()[:500]}")
        return False
    return True
```

### Retention (Pruning) via rclone

```python
def prune_old_rclone(remote_base: str, keep: int) -> List[str]:
    # List dirs on remote
    result = subprocess.run(
        ["rclone", "lsf", remote_base, "--dirs-only", "-R"],
        capture_output=True, text=True, timeout=60
    )
    dirs = [line.strip().rstrip("/") for line in result.stdout.strip().splitlines() 
            if line.strip().startswith("hermes-plain-")]
    dirs.sort(reverse=True)
    
    removed = []
    for old in dirs[keep:]:
        old_path = f"{remote_base}/{old}"
        subprocess.run(["rclone", "delete", old_path, "--fast-list"], check=True, timeout=300)
        removed.append(f"{old} (deleted via rclone)")
    return removed
```

## Results

| Metric | Before (FUSE) | After (rclone direct) |
|--------|---------------|----------------------|
| Local test (config.yaml) | ~5s | ~5s |
| Plain backup (4.9GB) | **Timeout 1200s** | **~3-5 minutes estimated** |
| GDrive archive (encrypted) | Timeout with trash | **~2-3 minutes estimated** |

## Related

- `references/gdrive-trash-and-retention.md` — trash accumulation timeout solution (async non-blocking)
- `references/cron-timeout-vs-wrapper-timeout.md` — scheduler timeout config required
- Scripts: `hermes_plain_backup.py`, `hermes_backup_common.py`