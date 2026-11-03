---
name: hermes-third-party-tracker
description: Use when working with Hermes third-party tracker — the dashboard plugin and CLI script that inventories external git repos, plugins, skills, and capability layers; runs update scans; and presents a unified update/inventory view.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, dashboard, third-party, tracker, inventory, updates, plugins, skills, git]
    related_skills: [hermes-dashboard-customization, hermes-dashboard-development, sagar-hermes-ops]
---

# Hermes Third-Party Tracker

The third-party tracker is a **dashboard plugin** (`third-party-tracker`) + a **scan script** (`check_hermes_third_party_updates.py`) that gives Hermes a unified view of all external dependencies:

- **Hermes core** — version, git status, update availability
- **Plugins** — git-tracked vs manual/copied, upstream source detection
- **Skills** — hub-installed (checkable/updatable) vs local (manual only)
- **Git repos under `~/.hermes`** — markitdown, mnemosyne, etc.
- **External git repos from MCP config** — MCP servers referenced in `config.yaml`
- **Dashboard registry repos** — custom git repos added via the dashboard UI
- **Pipx/CLI tools** — capability layers like `agent-reach`, `mnemosyne-hermes`

## When to Use

- User wants to see what external dependencies Hermes has
- User wants to check for updates across all external sources
- User installed a new capability layer (agent-reach, mnemosyne-hermes, etc.) and wants it tracked
- User added a new MCP server repo and wants it inventoried
- User wants to run a live scan and refresh the dashboard
- Debugging why a plugin/skill/repo isn't showing in the tracker

## Architecture

| Component | Path | Role |
|-----------|------|------|
| Dashboard plugin | `~/.hermes/plugins/third-party-tracker/` | UI at `/third-party-tracker` |
| Scan script | `~/.hermes/scripts/check_hermes_third_party_updates.py` | Generates inventory JSON/MD |
| Registry file | `~/.hermes/state/third_party_tracker_registry.json` | Custom git repos added via dashboard |
| State file | `~root/.hermes/state/third_party_tracker_state.json` | Scan metadata, timestamps |
| Output JSON | `~/.hermes/reports/third_party_inventory.json` | Machine-readable inventory |
| Output MD | `~/.hermes/reports/third_party_inventory.md` | Human-readable report |
| Static data | `~/.hermes/plugins/third-party-tracker/dashboard/dist/data.json` | Dashboard frontend data |
| Cron job | `weekly-hermes-third-party-updates` | Weekly scan + notification |

## Key Commands

```bash
# Run live scan (updates dashboard immediately)
python3 /root/.hermes/scripts/check_hermes_third_party_updates.py

# View generated reports
cat /root/.hermes/reports/third_party_inventory.md
cat /root/.hermes/reports/third_party_inventory.json

# Check registry
cat /root/.hermes/state/third_party_tracker_registry.json

# Dashboard: open http://<host>:9120/third-party-tracker
```

## Adding a Custom Git Repo to Registry

The dashboard registry tracks **external git repos not auto-discovered** (pipx tools, external capability layers, etc.).

**Via Dashboard UI:**
1. Open `/third-party-tracker` → "View inventory"
2. Scroll to "Future installs / custom git repos" → "ADD EXTERNAL GIT REPO ROOT"
3. Enter absolute path to git repo root → "Add & scan"

**Via CLI (direct JSON edit):**
```bash
# Read current
cat /root/.hermes/state/third_party_tracker_registry.json

# Edit (add to custom_git_repos array)
# Each entry: name, url, local_path (empty if pipx), port (optional), dashboard_url (optional), notes
```

**Example entry for pipx-installed agent-reach:**
```json
{
  "name": "agent-reach",
  "url": "https://github.com/Panniantong/agent-reach",
  "local_path": "",
  "notes": "Agent internet capability layer (14+ platforms). Installed via pipx from git. CLIs: twitter-cli, yt-dlp, bili-cli, gh, mcporter, OpenCLI, rdt-cli, xiaohongshu-mcp. Skill file at /root/.agents/skills/agent-reach/"
}
```

## Auto-Discovery Sources

The scan script auto-discovers from four sources (no manual registry needed):

| Source | What it finds |
|--------|---------------|
| `~/.hermes/plugins/` | Git-tracked plugins (`.git` dir present) |
| `~/.hermes/` (recursive) | Any git repo under Hermes home (excludes profiles, cache, logs) |
| `config.yaml` → `mcp_servers` | Local paths referenced by MCP server configs → finds their git roots |
| Dashboard registry | Custom repos added via UI |

## Update Status Meanings

| Status | Meaning |
|--------|---------|
| `up_to_date` | Local commit == remote HEAD |
| `update_available` | Local commit behind remote HEAD |
| `detached_or_unknown_branch` | On detached HEAD or branch not on remote |
| `check_failed: X` | Git ls-remote failed (network/auth) |
| `manual_only` | No git remote in installed dir (copied folder) |
| `no_remote` | Git repo but no origin remote |

## Common Pitfalls

### Pitfall: Tracker tab missing from dashboard nav (plugin dir still on disk)
The `third-party-tracker` sidebar label (**3rd Party**) appears only when the plugin is in **`plugins.enabled`**, same as other user dashboard plugins. Inventory data can be healthy while the nav item is hidden. Fix: `hermes plugins enable third-party-tracker`; verify `GET /api/dashboard/plugins` lists the name. See `sagar-hermes-ops` → `references/dashboard-user-plugins-enabled-gate.md`.

### Pitfall: Pipx tools don't show git updates
Tools installed via `pipx install git+https://...` have **no local `.git` dir** — the tracker can't auto-check commits. **Fix:** Add to dashboard registry with `local_path: ""` and notes explaining it's pipx-managed. User runs `pipx upgrade <tool>` manually.

### Pitfall: Registry key mismatch — `local_path` vs `path`
The dashboard registry uses `local_path` as the key for the local git directory, but the scan script originally only checked for `path`. **Fixed in scan script** to accept both keys. When editing registry JSON manually, use `local_path` (preferred) or `path` (legacy). The script now reads: `entry.get('path') or entry.get('local_path') or ''`.

### Pitfall: Manual/copied plugins show `manual_only`
Plugins installed as folders without `.git` (e.g., `hermes-achievements`, `mission-control`) can't auto-update. **Fix:** Re-install via `hermes plugins install owner/repo` to get git tracking, or accept manual updates.

### Pitfall: MCP server repos outside `~/.hermes` not tracked
If MCP config references `/mnt/tb/.../mcp-server/`, the scan finds the git root but classifies as `external_git_repo`. This is correct — they're tracked but not "under Hermes home."

### Pitfall: Detached HEAD on mnemosyne vendor repo
`~/.hermes/vendor/mnemosyne` often shows `detached_or_unknown_branch`. This is normal for vendor'd dependencies — not actionable unless you actively maintain that fork.

### Pitfall: Scan script permission denied
Run with `python3 /root/.hermes/scripts/check_hermes_third_party_updates.py` not direct execution (shebang may not be executable).

## Verification Checklist

After adding a new external repo or capability layer:

- [ ] Run live scan: `python3 /root/.hermes/scripts/check_hermes_third_party_updates.py`
- [ ] Verify it appears in `/third-party-tracker` dashboard → "View inventory"
- [ ] Check registry shows correct count: "Registry repos: N"
- [ ] Confirm update status is correct (up_to_date / manual_only / etc.)
- [ ] If pipx tool: verify notes explain manual upgrade path

## References

- `references/agent-reach-integration.md` — agent-reach installation, channel verification, Hermes usage patterns
- `references/groktocrawl-tracker-row.md` — GroktoCrawl registry JSON (Firecrawl v2 stack; eval, typically not installed)
- `references/registry-management.md` — detailed registry JSON schema, dashboard UI steps, CLI edit patterns
- `references/scan-script-architecture.md` — how the scan script works, auto-discovery logic, extending it
- `references/freellmapi-update-pattern.md` — FreeLLMAPI Docker update workflow, why not build locally, registry entry
- `references/mnt-tb-repos.md` — additional git repos on /mnt/tb not yet tracked, recommended registry entries