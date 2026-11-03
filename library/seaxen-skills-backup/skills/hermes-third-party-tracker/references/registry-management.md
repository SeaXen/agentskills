# Third-Party Tracker Registry Management

## Registry File

**Path:** `/root/.hermes/state/third_party_tracker_registry.json`

**Schema:**
```json
{
  "custom_git_repos": [
    {
      "name": "string",           // Required: display name
      "url": "string",            // Required: GitHub URL
      "local_path": "string",     // Optional: absolute path to local clone (empty for pipx tools)
      "port": "number",           // Optional: dashboard port if applicable
      "dashboard_url": "string",  // Optional: full dashboard URL
      "notes": "string"           // Optional: context/install notes
    }
  ],
  "updated_at": "number"          // Unix timestamp
}
```

## Adding Entries

### Via Dashboard UI (Recommended)

1. Open `http://<host>:9120/third-party-tracker`
2. Click **"View inventory"**
3. Scroll to **"Future installs / custom git repos"** section
4. Enter absolute path to git repo root in **"ADD EXTERNAL GIT REPO ROOT"**
5. Click **"Add & scan"**

**Auto-discovered:** The scan script picks up the `.git` dir and adds to registry automatically on next scan.

### Via CLI (Direct JSON Edit)

For pipx tools, external capability layers, or repos not auto-discovered:

```bash
# Backup first
cp /root/.hermes/state/third_party_tracker_registry.json /root/.hermes/state/third_party_tracker_registry.json.bak

# Edit with jq or cat
cat > /root/.hermes/state/third_party_tracker_registry.json <<'EOF'
{
  "custom_git_repos": [
    {
      "name": "FreeLLMAPI",
      "url": "https://github.com/tashfeenahmed/freellmapi",
      "local_path": "/root/freellmapi",
      "port": 3055,
      "dashboard_url": "http://192.168.0.222:3055",
      "notes": "OpenAI-compatible proxy for free LLM tiers. Docker install on server."
    },
    {
      "name": "agent-reach",
      "url": "https://github.com/Panniantong/agent-reach",
      "local_path": "",
      "notes": "Agent internet capability layer. Installed via pipx from git."
    }
  ],
  "updated_at": 1780065000
}
EOF
```

**Note:** `updated_at` should be current Unix timestamp (`date +%s`).

### Verification

After edit, run live scan:
```bash
python3 /root/.hermes/scripts/check_hermes_third_party_updates.py
```

Check dashboard → "View inventory" → "Dashboard registry: N custom repos"

## Registry Entry Types

| Type | `local_path` | Update Tracking | Example |
|------|--------------|-----------------|---------|
| Local git clone | `/absolute/path` | Auto (git ls-remote) | FreeLLMAPI at `/root/freellmapi` |
| Pipx tool | `""` (empty) | Manual only (`pipx upgrade`) | agent-reach, mnemosyne-hermes |
| Docker service | `""` or path | Manual only | Services without git |
| External capability | `""` | Manual only | Any non-git install |

## Auto-Discovery vs Registry

| Source | How It's Found | Registry Needed? |
|--------|----------------|------------------|
| `~/.hermes/plugins/*` (git) | Scan script walks `.git` dirs | No |
| `~/.hermes/` recursive (git) | Scan script walks all `.git` | No |
| `config.yaml` → `mcp_servers` local paths | Scan script extracts paths, finds git roots | No |
| Pipx tools (`pipx list`) | **Not auto-scanned** | **Yes** |
| Docker containers | Not scanned | Only if dashboard needed |
| External capability layers | Not scanned | **Yes** |

## Common Patterns

### Pattern: Pipx Capability Layer (agent-reach, mnemosyne-hermes)
```json
{
  "name": "tool-name",
  "url": "https://github.com/owner/repo",
  "local_path": "",
  "notes": "Brief description. Update: pipx upgrade tool-name"
}
```

### Pattern: Local Git Clone with Dashboard
```json
{
  "name": "service-name",
  "url": "https://github.com/owner/repo",
  "local_path": "/root/service-name",
  "port": 3055,
  "dashboard_url": "http://192.168.0.222:3055",
  "notes": "Service description. Docker: docker compose up -d"
}
```

### Pattern: MCP Server Repo (Already Auto-Discovered)
MCP servers under `/root/.hermes/scripts/mcp-servers/` or `/mnt/tb/hermes/scripts/mcp-servers/` are auto-discovered via `config.yaml` references. **Don't add to registry** unless they're outside those paths.

## Updating Registry Timestamp

After any edit, update `updated_at`:
```bash
# Using jq
jq --arg ts "$(date +%s)" '.updated_at = ($ts | tonumber)' \
  /root/.hermes/state/third_party_tracker_registry.json > /tmp/registry.json && \
  mv /tmp/registry.json /root/.hermes/state/third_party_tracker_registry.json

# Or manual
# Replace the number with `date +%s` output
```

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| "Registry repos: 0" but entries exist | `updated_at` not updated / scan not run | Run live scan script |
| Entry shows but not in dashboard | Dashboard cached old data | Hard refresh browser, or re-run scan |
| `local_path` not resolving | Path doesn't exist or no `.git` | Verify `ls -la /path/.git` |
| Pipx tool shows "manual_only" | Expected — no local git | Accept manual updates via `pipx upgrade` |

## Dashboard UI Buttons

| Button | Action |
|--------|--------|
| **"Add & scan"** | Adds entered path to registry, runs scan |
| **"Copy registry paths"** | Copies all registered paths to clipboard |
| **"Export registry"** | Downloads registry JSON |
| **"Export state"** | Downloads state JSON (timestamps, metadata) |
| **"Run live scan"** | Re-runs full inventory scan immediately |