---
name: skills-backup-incremental
description: Incremental git sync of ~/.hermes/skills to SeaXen/skills-backup — persistent clone, diff commits, no force-push.
version: 1.0.0
metadata:
  hermes:
    tags: [github, backup, skills-library, incremental, git]
    category: devops
---

# Skills backup — incremental (persistent clone)

Persistent local clone at `/mnt/tb/skills-backup` mirrors `SeaXen/skills-backup` (private).
Future backups are **incremental diffs on top of history**, never fresh snapshots or force-pushes.

## Workflow (every time)

```bash
# 1. Pull latest
git -C /mnt/tb/skills-backup pull --rebase

# 2. Rsync changes from source (same excludes as github-skills-library-backup)
rsync -a \
  --exclude=.hub --exclude=.curator_backups --exclude='*.log' \
  --exclude=__pycache__ --exclude='*.pyc' --exclude=.DS_Store \
  --exclude=.archive --exclude=.bundled_manifest --exclude=.curator_state \
  --exclude='.usage.json*' \
  /root/.hermes/skills/ /mnt/tb/skills-backup/

# 3. Commit only what changed + push
cd /mnt/tb/skills-backup
git add -A
git status --short | head   # review
git commit -m "Skills update YYYY-MM-DD: <what changed>"
git push origin main
```

## Rules

- **Never** `git init` in a temp dir and force-push over this repo again (caused full-snapshot overwrite on 2026-08-22, losing prior history).
- If conflicts appear on pull: resolve manually, do not rebase-abort-and-force.
- Same exclude list as `github-skills-library-backup` (no logs, caches, runtime state, credentials).
- Repo config: user SeaXen / seaxen@users.noreply.github.com (already set).

## Restore

```bash
git clone https://github.com/SeaXen/skills-backup.git ~/.hermes/skills
```

## Related

- `github-skills-library-backup` — original one-shot snapshot pipeline; excludes list source.
