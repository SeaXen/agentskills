# Hermes + Obsidian Memory Vault Pattern

Use when the user wants Obsidian to improve Hermes memory, reduce repeated context, or create a graph/dashboard over agent work.

## Architecture

Use a three-tier memory model:

1. **Hot memory** — Hermes `USER.md` / `MEMORY.md`; small, curated, auto-injected.
2. **Warm memory** — vault orientation/context files read on demand.
3. **Cold memory** — long-form notes, decisions, fixes, research, daily logs.

Do **not** auto-dump every chat into Obsidian. It creates low-quality memory. Save only:
- decisions
- completed/verifiable fixes
- research conclusions
- project state changes
- reusable medical/technical knowledge

## Recommended Vault Structure

```text
AGENT.md
Dashboard.md
README.md
Daily/                    # YYYY-MM-DD.md append-only important events
System/Assistant/         # context.md, preferences.md, environment.md, issues-fixes-log.md
Memory/                   # decisions.md, distilled durable memory
Knowledge/                # reusable guides and domain notes
Work/                     # active project notes
Personal/                 # finance/health/personal context
People/                   # contact/entity notes
Inbox/                    # unclassified incoming notes
Journal/                  # briefs and summaries worth keeping
```

## Required Entry Files

- `AGENT.md` — vault orientation and session-start protocol.
- `Dashboard.md` — human-facing command center.
- `System/Assistant/context.md` — current state and active work.
- `System/Assistant/preferences.md` — user style/domain preferences.
- `System/Assistant/environment.md` — stable host/service/path facts.
- `Memory/decisions.md` — durable decisions table/template.
- `System/Assistant/issues-fixes-log.md` — technical failures/fixes with verification.

## Dataview Setup

Dataview is useful for a live dashboard. Install into the vault:

```bash
VAULT=/path/to/vault
PLUGIN_DIR="$VAULT/.obsidian/plugins/dataview"
mkdir -p "$PLUGIN_DIR"
base='https://github.com/blacksmithgu/obsidian-dataview/releases/download/0.5.70'
for f in main.js manifest.json styles.css; do
  curl -fsSL "$base/$f" -o "$PLUGIN_DIR/$f"
done
python3 - <<'PY'
from pathlib import Path
import json, os
obs=Path(os.environ.get('VAULT', '/path/to/vault'))/'.obsidian'
obs.mkdir(parents=True, exist_ok=True)
app=obs/'app.json'
data=json.loads(app.read_text()) if app.exists() else {}
data['safeMode']=False
app.write_text(json.dumps(data, indent=2)+'\n')
comm=obs/'community-plugins.json'
plugins=json.loads(comm.read_text()) if comm.exists() else []
if 'dataview' not in plugins:
    plugins.append('dataview')
comm.write_text(json.dumps(plugins, indent=2)+'\n')
PY
```

Note: release tag and manifest version may differ upstream; verify files exist and `community-plugins.json` includes `dataview`.

## Dashboard Dataview Blocks

```markdown
### Recent Daily Notes
```dataview
LIST
FROM "Daily"
SORT file.name DESC
LIMIT 14
```

### Active Items
```dataview
LIST
FROM ""
WHERE contains(file.tags, "#active")
SORT file.mtime DESC
```

### Decisions
```dataview
TABLE date, status, outcome
FROM "Memory"
WHERE contains(file.tags, "#decision")
SORT date DESC
```

### Issues / Fixes
```dataview
TABLE status, system, severity
FROM "System/Assistant"
WHERE contains(file.tags, "#issue") OR contains(file.tags, "#fix")
SORT file.mtime DESC
```
```

## Moving Vaults

When moving a vault:
1. Move/rsync old vault to new path.
2. Update `OBSIDIAN_VAULT_PATH` in Hermes environment config.
3. Patch markdown references to the old absolute path.
4. Verify with file listing and read `AGENT.md` from the new path.
5. Update durable memory with the new vault path.

Keep spelling exactly as requested by the user, even if unconventional (example: `obsedianvault`).
