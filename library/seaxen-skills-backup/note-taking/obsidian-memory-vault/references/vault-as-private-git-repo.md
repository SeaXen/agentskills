# Vault as Private Git Repo — Reference

Working pattern for backing up `/mnt/tb/hermes/obsedianvault` to a private
GitHub repo. Tested 2026-06-17 with `SeaXen/obsmemory` (61 notes, 67 files,
private, ~140 KB).

## One-shot setup

```bash
# From inside the vault
cd /mnt/tb/hermes/obsedianvault

# Initialize git (vault is NOT already a git repo by default)
git init -b main
git config user.name "Sagar"
git config user.email "drpelagik@gmail.com"

# Add a .gitignore BEFORE first commit
# (see template below)

# First commit
git add -A
git commit -m "Initial commit: ObsMemory vault (N notes, M links, K canonicals)"

# Create private GitHub repo and push in one step
gh repo create obsmemory --private \
  --description "Hermes-obsidian memory vault — curated, durable, AI-recall-enabled." \
  --source=. --remote=origin --push
```

## .gitignore template

Required exclusions for any Obsidian vault:

```gitignore
# Per-device Obsidian config (can leak device IDs)
.obsidian/workspace*
.obsidian/cache
.obsidian/themes

# Trash (Obsidian's local trash)
.trash/

# System / editor
.DS_Store
Thumbs.db
*.swp
*.swo
*~

# Editor / IDE
.idea/
.vscode/

# Backup files
*.bak
*.backup
*.orig

# Large binaries (anything > 5MB)
*.pdf
*.zip
*.tar.gz

# API keys / secrets (defense in depth)
*.key
*.pem
*.env
secrets.*
credentials.*

# Per-device layout cache (regenerable)
.obsidian-dashboard-layout.json
```

## README template (safe — no wikilink false positives)

When writing a README inside the vault, **never** use `[[wikilink]]` syntax
inside backticks. The dashboard's wikilink parser scans every markdown file
in the vault including the README, and a `[[AGENT.md]]` example will be
flagged as a real broken link. Use prose instead:

```markdown
## Wikilink convention

Wikilinks are resolved by title, not by path. Use `[[AGENT]]`, never
`AGENT.md` or full paths.

## Structure

```
.
├── AGENT                  # Vault orientation (start here)
├── Dashboard              # Main command center
├── Daily                  # 30+ daily notes, one per working day
├── Knowledge              # 12 canonical reference notes
├── System/Assistant       # Core logs (issues-fixes-log, context, preferences)
├── Memory                 # Long-term durable memory (decisions.md)
├── Inbox                  # Pending imports / quick capture
├── Work                   # Active project notes
├── People                 # Person / contact notes
└── Personal               # Personal / non-work
```
```

After creating README.md, ALWAYS verify broken links:

```bash
curl -s http://localhost:6065/api/memory-health | python3 -c "
import sys, json
d = json.load(sys.stdin)
broken = d.get('broken_links', [])
print(f'broken: {len(broken)}')
for b in broken: print(' ', b)
"
```

Expected: `broken: 0`. If non-zero, the README has a wikilink example.

## Verification after push

```bash
# Should return 404 (private, no auth from public API)
curl -s -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/OWNER/REPO
# Expected: 404

# Confirms isPrivate: true via gh CLI auth
gh repo view OWNER/REPO --json name,isPrivate,description,url
# Expected: "isPrivate": true, url: https://github.com/OWNER/REPO
```

## Mirror notes (.gitignore or commit?)

For vaults with auto-generated mirror notes (e.g. `Knowledge/Mnemosyne Mirror.md`),
decide explicitly:

- **Commit them**: deterministic content, no real value in regenerating
  from git checkout, lets reviewers see what cron produced
- **Gitignore them**: keeps `git status` quiet on cron runs, but new clones
  need to regenerate (requires running the mirror script + having Mnemosyne access)

For most users, commit them. The downside (noisy diffs on cron runs) is
manageable. The upside (every clone has the latest mirror immediately) is real.

Pattern if you DO gitignore them:

```gitignore
# Auto-generated mirror notes (regenerate on clone)
Knowledge/Mnemosyne Mirror.md
Knowledge/Mnemosyne Triples.md
```

Add a note to README: "After cloning, run `python3 scripts/mnemosyne_to_vault.py`
to regenerate mirror notes."

## README wikilink false-positive pitfall (real bug from 2026-06-17)

Timeline:
1. Created `README.md` with example `[[AGENT]] not [[AGENT.md]]` to document
   the wikilink convention.
2. Committed + pushed. Health score still 98.3 (no immediate visual change).
3. Restarted dashboard service to re-scan vault.
4. `/api/memory-health` returned `broken_links: [{'source': 'README', 'target': 'AGENT.md', 'exists': False}]`.

The README example was inside backticks but the dashboard's wikilink
parser doesn't respect backtick fences — it scans for `[[X]]` patterns
anywhere in any `.md` file. The fix: change the README example from
`[[AGENT]] not [[AGENT.md]]` to `[[AGENT]] not by full path`.

This is captured as Pitfall 33 in the SKILL.md. **Read it before writing
any documentation inside a vault with a wikilink scanner.**
