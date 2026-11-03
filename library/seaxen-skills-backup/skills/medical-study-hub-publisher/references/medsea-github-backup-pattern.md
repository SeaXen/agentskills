# MedSea GitHub Backup — Reference Pattern

How to set up GitHub backup for a large local content tree (e.g. the Sea
Knowledge cardiology chapter) so accidental deletion is recoverable in one
command. The live repo is at https://github.com/SeaXen/MedSea and the
local mirror lives at `/mnt/tb/Sea-knowledge/#MedSea/` (co-located with
the content it backs up — see Pitfall 49 in SKILL.md for why co-location
matters).

## When to use this

Any time you have a large local content directory (~hundreds of files, 50MB+)
that you can't easily regenerate from source. Examples:
- The 330-disease Sea Knowledge cardiology tree at `/mnt/tb/Sea-knowledge/`
- A flattened study-notes archive
- Generated render output (md + html + png triples per topic)
- Any local archive you can't afford to lose

The trigger is usually: "if I accidentally `rm -rf` this, I want to recover
in under 5 minutes, not 3 hours."

## Directory layout

```
/mnt/tb/Sea-knowledge/#MedSea/                # local mirror, co-located with live content
├── README.md                                  # repo overview + restore steps
├── .gitignore                                 # __pycache__/, .DS_Store, *.log, /tmp/
├── scripts/
│   ├── build_backup.py                        # takes REPO_ROOT as argv[1] (script-relative)
│   ├── sync.sh                                # uses $(dirname $0)/.. for REPO path
│   ├── restore.sh                             # same — works from any install location
│   └── restore_diseases.py                    # python helper, takes 2 args
└── chapters/
    └── 16-cardiology/                         # one folder per chapter
        ├── manifest.json                      # canonical list + render status
        ├── README.md                          # chapter status + known gaps
        ├── hubs/                              # 14-17 hub-level .md files
        ├── diseases/                          # FLAT-named disease folders (16.N.M-<slug>/)
        │   └── 16.1.25-atherosclerosis-pathogenesis/
        │       ├── topic.md
        │       ├── topic.html
        │       └── topic.png
        └── source/                            # raw markdown from /root/sk-content/ (with duplicates)
```

## Why flat names + manifest, not nested

Git tracks moves/renames cleanly when folder names are deterministic. If
the backup uses the nested hub/disease tree, every time you restructure
the live tree, you have to re-commit thousands of renames. The flat-name
pattern (`16.N.M-<slug>/`) keeps the backup stable across restructures —
the only thing that changes is the manifest, not the disease folders.

**Restore reconstructs the nested tree on demand** by reading the
manifest and copying each `diseases/<flat-folder>/` into
`<DEST>/<hub_num>. <hub_name>/<subnum>. <clean_topic>/`.

## Why co-located under `/mnt/tb/Sea-knowledge/#Name/` (not `/root/Name/`)

First version lived at `/root/MedSea/`. The user immediately asked to move
it under `/mnt/tb/Sea-knowledge/#MedSea/`. Reasons:
- Same mount as the live content — inherits the same storage guarantees
- Visually distinct from chapters via the `#` prefix
- Future backup repos follow the same pattern (`#Medsurg`, `#Paeds`, ...)

## Setup recipe (one-time)

```bash
# 1. Create local mirror (note the # prefix and co-location)
mkdir -p /mnt/tb/Sea-knowledge/#<backup-name>/chapters/<N>-<specialty>/{hubs,diseases,source}

# 2. Build manifest.json from canonical list
python3 scripts/build_backup.py "$REPO_ROOT"

# 3. Init git and create GitHub repo
cd /mnt/tb/Sea-knowledge/#<backup-name>
git init -q
git branch -M main
gh repo create <backup-name> --public \
  --description "..." \
  --source=. --remote=origin --push

# 4. Verify restore works
mkdir -p /tmp/restore_test
bash scripts/restore.sh --target /tmp/restore_test
# Spot-check: hubs, disease counts, sample content
rm -rf /tmp/restore_test

# 5. Add daily auto-backup cron
# schedule="0 2 * * *", workdir=/mnt/tb/Sea-knowledge/#<backup-name>,
# prompt="run scripts/sync.sh, report exit code", deliver=local
```

## sync.sh — script-relative, no hardcoded paths

```bash
#!/bin/bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
SRC="/mnt/tb/Sea-knowledge/16. Cardiology"

echo "[$(date)] Starting backup..."

# Rebuild content from live source (REPO passed so build_backup.py doesn't
# need a hardcoded path)
python3 "$REPO/scripts/build_backup.py" "$REPO"

# Stage and commit
cd "$REPO"
git add -A
if git diff --cached --quiet; then
  echo "[$(date)] No changes"
  exit 0
fi
git commit -m "Backup: $(date +%Y-%m-%d_%H%M)"
git push origin main 2>&1 || echo "[$(date)] Push failed (will retry next run)"
echo "[$(date)] Backup complete"
```

The push-failure tolerance is intentional — if GitHub is down, the
commit is still local and will push on the next successful run.

## restore.sh — script-relative, reconstructs nested tree

```bash
#!/bin/bash
set -euo pipefail

CHAPTER="16"
TARGET="/mnt/tb/Sea-knowledge"   # default
while [[ $# -gt 0 ]]; do
  case $1 in
    --chapter) CHAPTER="$$2"; shift 2 ;;
    --target)  TARGET="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

REPO="$(cd "$(dirname "$0")/.." && pwd)"
CHAPTER_DIR="$REPO/chapters/$CHAPTER-<specialty>"
DEST="$TARGET/16. <Specialty Name>"
mkdir -p "$DEST"

# Step 1: copy hub mds
for hub_md in "$CHAPTER_DIR/hubs/"*.md; do
  [ -f "$hub_md" ] || continue
  cp "$hub_md" "$DEST/"
done

# Step 2: reconstruct nested disease tree from manifest
python3 "$REPO/scripts/restore_diseases.py" "$CHAPTER_DIR" "$DEST"

# Step 3: restore source mds to /root/sk-content/ (re-rendering source)
if [ -d "$CHAPTER_DIR/source" ]; then
  mkdir -p /root/sk-content
  cp -n "$CHAPTER_DIR/source/"*.md /root/sk-content/ 2>/dev/null || true
fi
```

## restore_diseases.py — the manifest-driven copy

Topic-name → folder-name sanitization must handle em-dashes, slashes,
parens, quotes, and backticks — the canonical topic strings have all of
these. The full sanitization:

```python
import json
import shutil
import sys
from pathlib import Path

def main():
    chapter_dir = Path(sys.argv[1])
    dest_root = Path(sys.argv[2])
    manifest = json.loads((chapter_dir / 'manifest.json').read_text())
    hubs = {h['slug']: (h['num'], h['name']) for h in manifest['hubs']}
    restored = 0
    for d in manifest['diseases']:
        src = chapter_dir / d['folder']
        if not src.exists():
            print(f'  missing in backup: {d["folder"]}')
            continue
        hub_info = hubs.get(d['parent_slug'])
        if not hub_info:
            print(f'  unknown hub for {d["folder"]}: {d["parent_slug"]}')
            continue
        hub_num, hub_name = hub_info
        hub_dir = dest_root / f'{hub_num}. {hub_name}'
        hub_dir.mkdir(parents=True, exist_ok=True)
        # Full sanitization: handle em-dashes, slashes, parens, quotes, backticks
        clean = d['topic'].lower()
        for ch in ' /—(),`\'':
            clean = clean.replace(ch, '-')
        while '--' in clean:
            clean = clean.replace('--', '-')
        clean = clean.strip('-')[:80]
        target_dir = hub_dir / f'{d["subnum"]}. {clean}'
        target_dir.mkdir(parents=True, exist_ok=True)
        for f in src.iterdir():
            target = target_dir / f.name
            if target.exists():
                target.unlink()
            shutil.copy2(f, target)
        restored += 1
    print(f'  diseases restored: {restored}')

if __name__ == '__main__':
    main()
```

## Gotchas

- **Never `rm -rf` the live tree during a restructure.** Always have a
  backup BEFORE you start restructuring.
- **Always test the restore** with `--target /tmp/test` after setup.
  Don't find out the restore is broken when you actually need it.
- **Manifest is the source of truth.** If the manifest conflicts with
  the directory, the manifest wins.
- **Public repo is fine for personal study notes** (75MB is well under
  GitHub's 100MB-per-file and 1GB-repo limit). If you need private,
  `--private` instead of `--public` on `gh repo create`.
- **Don't use shell heredoc for Python in `restore.sh`** — the heredoc
  can be silently broken by `set -e`. Use a separate `.py` file.
- **The global `idx` (1..330) doesn't match the per-hub local counter
  (1..N within each hub).** See Pitfall 46 in SKILL.md for the fix.
- **The renderer nests output one level too deep** (Pitfall 41). Always
  flatten before backup, or accept nested slug-named subdirs in the
  backup and document it.
- **Slugs starting with `-` break argparse** (Pitfall 42). Sanitize
  before passing to `render_topic.py --slug`.
- **Always use script-relative paths in scripts** — never hardcode
  `/root/<name>` or `/mnt/tb/...`. The user may move the repo (e.g.
  `/root/MedSea/` → `/mnt/tb/Sea-knowledge/#MedSea/`).
- **Verify background processes actually exited** before relaunching
  (Pitfall 50). Use `notify_on_complete=true` for bounded tasks.