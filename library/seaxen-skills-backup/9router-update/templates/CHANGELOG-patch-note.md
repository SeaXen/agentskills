# 9router updated to v<NEW_VERSION>

Updated to **<NEW_VERSION>** (commit `<SHA>`) at <TIMESTAMP>.

## What changed

- Image: `decolua/9router:latest` @ `<DIGEST>`
- Container: `9router` (healthy, <UPTIME> uptime)
- Backup: `/mnt/tb/1Apps/9router/backups/<BACKUP_TS>/`

## Key upstream changes (v<OLD> → v<NEW>)

<PASTE_RELEVANT_CHANGELOG_SECTION_HERE>

## ⚠️ Action required

Hard-refresh your browser on `/dashboard/usage`:
- **Windows/Linux**: `Ctrl + Shift + R`
- **macOS**: `Cmd + Shift + R`

This clears the cached JS bundle. Without the hard-refresh, you'll keep seeing the old period selector (7d/30d/60d) even though the new bundle is on disk.

## Verify

```bash
bash /root/.hermes/skills/9router-update/scripts/verify-update.sh
```

Expected: 7/7 checks pass.

## If something looks off

```bash
# Tail container logs
docker logs 9router --tail 100

# Re-apply the usage-periods patch (idempotent — safe to re-run)
python3 /mnt/tb/1Apps/9router/patches/apply-usage-periods.py

# Roll back from backup
docker stop 9router && docker rm 9router
docker compose -f /mnt/tb/1Apps/9router/docker-compose.yml up -d
```
