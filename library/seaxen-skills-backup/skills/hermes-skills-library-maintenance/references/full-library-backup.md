# Full-library backup to GitHub — full reference

## Decision tree

Before staging, confirm 4 parameters with the user:

1. **Visibility**: `private` (default — user owns the curation) or `public` (world benefits)
2. **License wrapper**: `MIT` (permissive), `AGPL-3.0` (copyleft), or per-folder mixed
3. **Scope**: `full` (~80 MB) or `summary-only` (~5 MB, strips verbatim leaves)
4. **Push mode**: `manual` (operator runs), `cron` (scheduled), `pre-commit` (auto)

Defaults: `private MIT full manual`.

## The 86MB trap

`~/.hermes/skills/research/crypto-research-alerting/browser_dashboard.log` is 86 MB.
GitHub will warn (>50MB) and may refuse (>100MB). It MUST be stripped.

Also strip:
- `.hub/` (~40 MB, Hermes internal cache)
- `.curator_backups/` (~22 MB, old curator snapshots)
- `*.log`, `__pycache__/`, `*.pyc`, `.DS_Store`

## Staging

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

## The `gh repo create --source` trap

`gh repo create --source=. --push` does git init internally and assumes an empty
dir. Use the 2-step pattern:

```bash
gh repo create SeaXen/<name> --private --description "..."
cd "$STAGE"
git remote add origin https://github.com/SeaXen/<name>.git
git push -u origin main
```

## Push failures — escalation

| Symptom | Fix |
|---|---|
| HTTP 408 (timeout) | Bump `http.postBuffer=524288000`, `http.version=HTTP/1.1`, retry once |
| Repeated 408 over 5+ minutes | Pause. Check https://www.githubstatus.com — likely GitHub degraded |
| Status page shows incident | **Don't retry** — wait. Bundle instead: `git bundle create /tmp/skills-backup.bundle --all` |
| `gh auth refresh` times out | Same as 408 — same backend |

## Bundle as a portable backup format

```bash
cd "$STAGE"
git bundle create /tmp/skills-backup-$(date +%Y%m%d).bundle --all
git bundle verify /tmp/skills-backup.bundle
# ~29 MB compressed vs ~80 MB working tree
```

Bundles can be cloned via `git clone /tmp/skills-backup.bundle restored/`. They
can also be uploaded via `git push --push-option` workarounds, or simply
shipped to a faster host for retry.

## Confirming what landed

```bash
gh repo view SeaXen/<name> --json diskUsage,defaultBranchRef
# diskUsage should be > 0
# defaultBranchRef.name should be "main"
```

If `diskUsage == 0` after a "successful" push, the data never landed despite
local git reporting success. Check the response, retry, or use bundle.

## Common pitfalls

- `gh repo create --source=. --push` on a non-empty dir: fails with cryptic error. Always 2-step.
- Forgetting `.gitignore`: re-push includes .hub and curator_backups, blows up the repo size. Always write .gitignore first.
- Pushing from inside `~/.hermes/skills/`: orphans the live tree because git init adds .git to the source dir. Always stage to /tmp.
- Pushing during a GitHub brownout: tight retry loops add load and burn bandwidth. Pause and bundle.

## Restore procedure

```bash
git clone https://github.com/SeaXen/<name>.git ~/.hermes/skills
```

Hermes will discover the skills on next start.
