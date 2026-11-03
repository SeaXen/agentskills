# Additional Git Repos on /mnt/tb (Not Yet Tracked)

These repos exist on the system but are outside `/root/.hermes/` so they're not auto-discovered by the scan script. They should be added to the tracker registry for weekly update scans.

## Repos Found

| Repo | Path | Remote | Branch | Purpose |
|------|------|--------|--------|---------|
| Rexterm | `/mnt/tb/1Apps/Rexterm` | `https://github.com/SeaXen/rexterm.git` | main | Terminal project |
| graphify | `/mnt/tb/1Apps/graphify` | `https://github.com/safishamsi/graphify` | v8 | Graphify dashboard |
| liquidrisk | `/mnt/tb/1Apps/liquidrisk` | `https://github.com/SeaXen/liquidrisk.git` | main | Trading risk tool |
| Medicine | `/mnt/tb/Medicine` | `https://github.com/SeaXen/medicine-notes.git` | main | Medical notes |
| pyhox | `/mnt/tb/1Apps/pyhox` | *(no remote)* | — | Local only |

## Recommended Registry Entries

Add these to `third_party_tracker_registry.json` under `custom_git_repos`:

```json
{
  "name": "rexterm",
  "url": "https://github.com/SeaXen/rexterm.git",
  "local_path": "/mnt/tb/1Apps/Rexterm",
  "notes": "Terminal project by SeaXen. Main branch."
},
{
  "name": "graphify",
  "url": "https://github.com/safishamsi/graphify",
  "local_path": "/mnt/tb/1Apps/graphify",
  "notes": "Graphify dashboard (v8 branch). Dashboard on port 6080."
},
{
  "name": "liquidrisk",
  "url": "https://github.com/SeaXen/liquidrisk.git",
  "local_path": "/mnt/tb/1Apps/liquidrisk",
  "notes": "Trading risk tool by SeaXen. Main branch."
},
{
  "name": "medicine-notes",
  "url": "https://github.com/SeaXen/medicine-notes.git",
  "local_path": "/mnt/tb/Medicine",
  "notes": "Medical notes repo by SeaXen. Main branch."
}
```

**Note:** `pyhox` has no remote — skip or add with empty URL if local tracking desired.

## Why Track These

- All are active projects with upstream GitHub repos
- Weekly scan will detect `update_available` when upstream has new commits
- Currently invisible to the tracker (dashboard shows "Registry repos: 3" but these 4 are missing)
- Adding them centralizes update visibility in the third-party tracker dashboard

## After Adding

1. Update `updated_at` timestamp: `date +%s`
2. Run live scan: `python3 /root/.hermes/scripts/check_hermes_third_party_updates.py`
3. Verify dashboard shows "Registry repos: 7" (was 3)
4. Check each shows correct `update_status` (`up_to_date` or `update_available`)