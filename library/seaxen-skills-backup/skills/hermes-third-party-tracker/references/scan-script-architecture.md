# Scan Script Architecture

## Script Location

`/root/.hermes/scripts/check_hermes_third_party_updates.py`

## Overview

Single Python script that generates the complete third-party inventory. Runs in ~30-40 seconds. Called by:
- Dashboard "Run live scan" button
- Weekly cron job (`weekly-hermes-third-party-updates`)
- Manual CLI invocation

## Output Files

| File | Purpose |
|------|---------|
| `/root/.hermes/reports/third_party_inventory.json` | Machine-readable, loaded by dashboard |
| `/root/.hermes/reports/third_party_inventory.md` | Human-readable report |
| `/root/.hermes/plugins/third-party-tracker/dashboard/dist/data.json` | Dashboard frontend static data |

## Core Functions

### `inspect_plugins()`

Scans `~/.hermes/plugins/` (excludes `third-party-tracker`):
- If `.git` exists → `git_repo_status()` → `source_type: "git"`
- Else → `source_type: "copied/local"`, extracts URLs from `plugin.yaml`, `pyproject.toml`, `package.json`, `README.md`, `__init__.py`
- Checks for bundled plugin match in Hermes source tree
- Classifies source confidence: `exact_repo`, `candidate_repo`, `related_links`, `unknown`
- `update_status`: `up_to_date` / `update_available` / `detached_or_unknown_branch` / `manual_only`

### `inspect_skills()`

Runs Hermes CLI commands:
- `hermes skills list --source hub` → parses box table
- `hermes skills list --source local` → parses box table
- `hermes skills check` → maps update status per skill
- `hermes skills tap list` → custom taps

Hub skills get `update_check` from `hermes skills check`; local skills always `manual_only`.

### `inspect_hermes_core()`

- `hermes --version` → parses version + update line
- If `~/.hermes/hermes-agent/.git` exists → `git_repo_status()`

### `discover_git_repos_under_home()`

Recursive walk of `~/.hermes/` finding `.git` dirs:
- Excludes: profiles, cache, `__pycache__`, `.venv`, `node_modules`, `.archive`, `state-snapshots`, `backups`, `sessions`, `logs`, `cache`
- Classifies by path:
  - `plugins/*` → `plugin_repo`
  - `scripts/mcp-servers/*` → `mcp_repo`
  - `skills/*` → `skill_repo`
  - `themes/*` → `theme_repo`
  - else → `git_repo`

### `discover_external_git_repos_from_config()`

Reads `config.yaml`, extracts all local paths from `mcp_servers` section, finds git root for each, classifies as `external_git_repo` with `referenced_by` field.

### `discover_git_repos_from_tracker_registry()`

Reads `third_party_tracker_registry.json`, processes `custom_git_repos` entries, finds `.git` at each `local_path` (also checks `path` for backwards compatibility), classifies as `external_git_repo` with `tracker_registry: true`.

**Note:** The registry uses `local_path` as the key for the local git directory. The script was updated (June 2026) to accept both `local_path` and `path` keys for compatibility.

**Fix applied (June 2026):** In `discover_git_repos_from_tracker_registry()`, changed:
```python
path_text = str(entry.get('path') or '')
label = str(entry.get('label') or '')
```
to:
```python
path_text = str(entry.get('path') or entry.get('local_path') or '')
label = str(entry.get('label') or entry.get('name') or '')
```
This supports both the dashboard UI's `local_path` key and legacy `path` key, plus uses `name` as fallback label.

## Git Status Logic (`git_repo_status()`)

```python
# Runs in repo dir:
git remote get-url origin          # → remote URL
git rev-parse --abbrev-ref HEAD    # → branch name
git rev-parse --short HEAD         # → local commit (7 chars)
git status --short                 # → dirty flag

# If branch != HEAD and remote exists:
git ls-remote <remote> refs/heads/<branch>
# → remote HEAD commit (7 chars)
# status = "up_to_date" if matches local, else "update_available"
```

**Status values:**
- `up_to_date`
- `update_available`
- `detached_or_unknown_branch` (on detached HEAD or branch not on remote)
- `check_failed: <error>` (ls-remote failed)
- `no_remote`

## Deduplication Logic

After collecting all repos, script deduplicates by resolved absolute path:

```python
plugin_repo_paths = {resolved_path for p in plugins}
external_repo_paths = {resolved_path for r in external_git}

extra_home_git = [r for r in home_git if r.path not in plugin_repo_paths and r.path not in external_repo_paths]
```

This ensures a repo tracked as a plugin doesn't also appear under "Other git repos under ~/.hermes".

## Summary Counts

Final payload includes:
```python
summary = {
    'git_tracked_plugins': count of plugins with source_type == 'git',
    'manual_plugins': count with update_status == 'manual_only',
    'hub_skills': len(skills['hub']),
    'local_skills': len(skills['local']),
    'git_repos_under_home': len(extra_home_git),
    'external_git_repos': len(external_git),
    'tracker_registry_repos': len(registry_git),
    'hermes_core_updates': 0 or 1,
    'plugin_updates': count of plugins with update_status == 'update_available',
    'skill_updates': count of hub skills with update_check == 'update_available',
    'git_repo_updates': count of extra_home_git with update_available,
    'external_git_repo_updates': count of external_git with update_available,
}
```

## Actionable Items

`actionable` section lists specific items needing attention:
- `hermes_core_updates` — if core has update
- `plugin_updates` — git-tracked plugins with updates
- `skill_updates` — hub skills with updates (runnable: `hermes skills update <name>`)
- `git_repo_updates` — local repos with updates
- `external_git_repo_updates` — external repos with updates
- `manual_plugins` — all manual-only plugins (review only)

## Extending the Scan

To add a new discovery source:

1. Add new function `discover_<source>()` returning list of repo dicts
2. Add to `build_payload()` collection
3. Add to deduplication sets if needed
4. Add to `summary` counts
5. Add to `actionable` if updates should be surfaced

## Cron Job

**Job name:** `weekly-hermes-third-party-updates`
**Schedule:** `0 9 * * 5` (Friday 9 AM, honors config timezone)
**Script:** `/root/.hermes/scripts/weekly_third_party_update_notify.py`

The notify script runs the scan, compares with previous state, and delivers notifications for new updates.

## Performance

- Full scan: ~35-40 seconds
- Slowest parts: `git ls-remote` for each repo (network), `hermes skills check` (CLI subprocess)
- 15-20 repos typical → parallelizable but currently sequential

## Debugging

```bash
# Run with output
python3 /root/.hermes/scripts/check_hermes_third_party_updates.py

# Check JSON output
cat /root/.hermes/reports/third_party_inventory.json | jq '.summary'

# Check specific section
cat /root/.hermes/reports/third_party_inventory.json | jq '.plugins[] | {name, source_type, update_status}'

# Verify git status for one repo
cd /root/.hermes/plugins/cronalytics && git status && git ls-remote origin refs/heads/master
```

## Common Issues

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `check_failed: 0` for plugin | `git ls-remote` returned empty | Check remote URL, network, auth |
| `detached_or_unknown_branch` | Repo on detached HEAD (submodule, vendor) | Normal for vendored deps |
| `manual_only` for git-tracked plugin | `.git` not found at scan time | Verify `.git` exists in plugin dir |
| Skills check empty | `hermes skills check` output format changed | Update `parse_box_table()` regex |
| Scan takes >60s | Network timeout on `git ls-remote` | Check connectivity, increase timeout |
| Registry entries not scanned | Registry uses `local_path` but script expects `path` | Script now supports both keys |
| Registry entries not scanned | Registry uses `local_path` but script expects `path` | Script now supports both keys |