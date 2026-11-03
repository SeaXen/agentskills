---
name: hermes-skills-library-maintenance
description: Reconcile manifest, INDEX, GitHub backup for skill library.
version: 0.1.0
metadata:
  hermes:
    tags: [Learnables, Skills, Backup, GitHub, Manifest, INDEX]
    category: productivity
---

# Hermes skills library maintenance

Operational hygiene for a grown `~/.hermes/skills/` tree. Three recurring tasks:
1. Reconcile the verbatim manifest against disk truth
2. Regenerate `INDEX.md` for the learnables subtree
3. Back up the whole library to a private GitHub repo

Each runs occasionally (weekly, on-demand, before/after large sessions). None of them are research or commit — they are library ops.

---

## When to use

- User asks "how many skills do I have?" or "give me an index"
- User asks to back up / mirror / clone / publish the full skill library
- Manifest drift suspected (count of `SKILL.md` files ≠ `len(_verbatim-manifest.json)`)
- After a large batch of new learnables

---

## Task 1 — Reconcile the manifest

The manifest at `~/.hermes/skills/learnables/_verbatim-manifest.json` drifts whenever:
- A learnable was created before the manifest schema was adopted
- A repo dir was renamed or merged (manifest has old key, disk doesn't)
- A prior commit missed an entry

### Symptom of drift
`len(manifest["repos"]) != count of dirs with SKILL.md` under `~/.hermes/skills/learnables/`.

### Procedure
1. Build `disk_with_card = {d for d in os.listdir(LB) if not d.startswith("_") and SKILL.md present}`
2. Build `tracked = set(manifest["repos"].keys())`
3. **Untracked** = `disk_with_card - tracked` — add entries with actual `verbatim_count` (read each `skills/` dir)
4. **Orphans** = `tracked - disk_with_card` — manifest keys with no dir on disk
5. For orphans: `ls <name>` to confirm. Case-mismatches (`IPTV` vs `iptv`) are two real repos, NOT duplicates — check before deleting
6. Add untracked with schema:
   ```json
   {"summary_card": true, "verbatim_count": N, "verbatim_skills": [{"name": "...", "path": "skills/.../SKILL.md", "note": "reconciled from prior session"}]}
   ```
7. Re-verify: `disk_with_card == tracked`. Now drift = 0

### Reference
`references/manifest-reconciliation.md` — full Python snippet, idempotent and safe to re-run.

---

## Task 2 — Regenerate INDEX.md

Users will ask "how many skills do I have?". `INDEX.md` answers in one file.

### Procedure
1. List all dirs under `~/.hermes/skills/learnables/`, skip `_*`
2. Per-dir, compute:
   - `has_card` (SKILL.md present)
   - `leaf_count` (count of `skills/<name>/` dirs)
   - `size` (one-shot `du -sh */ | sort -hr`)
   - `category` (heuristic on the name — see below)
3. Group by category, sort groups by size desc
4. Emit one Markdown table per category: `| repo | 📄 | 🔢 N | size |`
5. Append a section noting **other** skill locations (`/root/.hermes/skills/<cat>/SKILL.md` outside learnables) — users want both counts together

### Categorization heuristics
Suggested (not enforced):
- `agent`, `hermes`, `headroom`, `reasonix`, `jarvis`, `kimchi` → Agent Frameworks
- `coolify`, `self-host`, `kudu`, `superfile`, `thefuck`, `BlueVein`, `polymarket` → Self-hosted Tools & DevOps
- `design`, `taste`, `impeccable`, `humanizer`, `creative`, `manim`, `p5js` → Design & UI
- `system-prompts`, `anthropics`, `claude-skills`, `mattpocock` → Skills & Meta-Skills
- Everything else → "Other"

These heuristics miscategorize ~10% of dirs (often exactly the items the user cares about); always show the "Other" group so nothing is silently dropped.

### Sample output shape
```
# Learnables Index

Auto-generated. **186** repos in `/root/.hermes/skills/learnables/`.

| Repo | Card | Verbatim | Size |
|---|:-:|:-:|:-:|
| `9router` | · | 🔢 3 | 32K |
| ...

## By the numbers
- Total repos: 186
- Summary cards: 184
- Verbatim leaf dirs: 262
- Disk: 69 MB

## Other skill locations (Hermes main)
`/root/.hermes/skills/` has 46 top-level categories with 215 SKILL.md files (excluding learnables)...
```

---

## Task 3 — Back up the full library to a private GitHub repo

When the user wants disaster-recovery backup of the whole `~/.hermes/skills/`, not just one repo.

### Confirm 4 parameters before staging
- **Visibility**: private vs public
- **License**: MIT (wrapper) vs AGPL-3.0 vs per-folder mixed
- **Scope**: full mirror (~80 MB) vs summary-only (~5 MB)
- **Push mode**: manual vs cron vs pre-commit hook

If unspecified, default to `private MIT full manual`.

### Strip runtime caches before any git work
These are regenerable and one of them (`research/crypto-research-alerting/browser_dashboard.log`) is 86 MB which GitHub will refuse:
- `.hub/` — Hermes index cache (~40 MB)
- `.curator_backups/` — old curator snapshots (~22 MB)
- `*.log` — runtime logs
- `__pycache__/`, `*.pyc` — Python bytecode
- `.DS_Store` — macOS metadata

### Stage to a clean dir
Never `git init` directly inside `~/.hermes/skills/` — that orphans the live tree.

```bash
STAGE=/tmp/hermes-skills-backup-$(date +%Y%m%d)
mkdir -p "$STAGE"
rsync -a \
  --exclude='.hub' \
  --exclude='.curator_backups' \
  --exclude='*.log' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.DS_Store' \
  /root/.hermes/skills/ "$STAGE/"
```

### Write top-level scaffolding
- `README.md` — what's in here, what was stripped, restore command
- `LICENSE` — MIT wrapper with note that per-repo licenses preserved
- `.gitignore` — same excludes (keeps future pushes clean)

### Commit + push
```bash
cd "$STAGE"
git init -b main
git add .
git -c user.email=... -c user.name=... commit -m "Backup of ~/.hermes/skills on YYYY-MM-DD"
gh repo create SeaXen/<name> --private --description "..."
git remote add origin https://github.com/SeaXen/<name>.git
git push -u origin main
```

**Note**: `gh repo create --source=. --push` will fail because it does git init internally and assumes an empty dir. Create the repo first, then push separately.

### Push failures
Be ready for HTTP 408 on large pushes (~80 MB can time out on this host's network):

1. Bump `http.postBuffer` to 524288000
2. Set `http.version HTTP/1.1`
3. **If still failing**, create a bundle:
   ```bash
   git bundle create /tmp/skills-backup.bundle --all  # ~29 MB compressed
   git bundle verify /tmp/skills-backup.bundle
   ```
4. Bundle can be cloned via `git clone /tmp/skills-backup.bundle restored/`
5. If GitHub itself is degraded (check https://www.githubstatus.com), **pause** — retries add load

### Confirm what landed
```bash
gh repo view SeaXen/<name> --json diskUsage,defaultBranchRef
# diskUsage > 0 means data is there
```

---

## Pitfalls

- **Do not** `git init` directly inside `~/.hermes/skills/` — orphans the live tree. Always stage to `/tmp/`.
- **Do not** auto-delete "orphan" manifest entries without `ls`-verifying the dir is truly gone. Case-mismatches are real repos.
- **Do not** retry `git push` in a tight loop during a GitHub brownout — adds load, gets 408. Check status page, then bundle.
- **Do not** include `research/crypto-research-alerting/browser_dashboard.log` — 86 MB, GitHub will warn and may refuse.
- **Do not** assume "do you best" means "do everything" — for `/learn` it means full research+commit; for backups it means confirm 4 params first.

---

## Verification

After each task, verify the actual artifact on disk:

```bash
# Task 1 — manifest matches reality
python3 -c "import json,os; m=json.load(open(os.path.expanduser('~/.hermes/skills/learnables/_verbatim-manifest.json'))); d=[x for x in os.listdir(os.path.expanduser('~/.hermes/skills/learnables')) if not x.startswith('_') and os.path.exists(os.path.expanduser(f'~/.hermes/skills/learnables/{x}/SKILL.md'))]; print('manifest:', len(m['repos']), 'disk:', len(d), 'drift:', set(m['repos'])^set(d))"

# Task 2 — INDEX.md exists and is recent
ls -la ~/.hermes/skills/learnables/INDEX.md

# Task 3 — push landed
gh repo view SeaXen/<name> --json diskUsage
```

---

## Cross-references

- `learnables-workflow` (research + commit phase) — Phase F.1/2/3 above complement the F.5 commit
- `designmd-store` — sibling file-store task under `/mnt/tb/#Sea/Designmd/` (different backup target, same mirroring pattern)
- `repo-deep-learn` — source of the operator-100% standard this library embodies

---

## Support files

- `references/manifest-reconciliation.md` — full Python snippet, idempotent
- `references/index-regeneration.md` — full snippet + categorization edge cases
- `references/full-library-backup.md` — full script with GitHub push workarounds
- `scripts/reconcile_manifest.py` — re-runnable reconciliation, idempotent
- `scripts/regenerate_index.py` — re-runnable INDEX generator
- `scripts/backup_skills_to_github.py` — end-to-end backup (stage + strip + commit + push)
