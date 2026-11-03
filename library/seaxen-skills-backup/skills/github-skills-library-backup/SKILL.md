---
name: github-skills-library-backup
description: Push Hermes skills library to new private GitHub repo.
version: 1.0.0
metadata:
  hermes:
    tags: [github, backup, skills-library, snapshot, devops, mirror]
    category: devops
---

# GitHub skills-library backup (class)

Use when the user wants the entire Hermes skills library pushed to a **new private GitHub repo** as a one-shot snapshot. Distinct from:

- `hermes-backup-watchers` — cron-driven filesystem backup to local TB / GDrive / Mega with rclone. Not git, not GitHub.
- `hermes-git-config-snapshots` — small `~/.hermes/config.yaml` drift detector. Not the whole skills tree.
- `daily-git-sync-cron-variant` (referenced by `hermes-backup-watchers`) — silently mirrors an **already-versioned** local git repo to GitHub. This skill handles **unversioned directory trees** that need `git init` first.

## Trigger phrases

- "I want to backup my skills to GitHub"
- "can I backup it in github new repo"
- "create a new private repo with my skills"
- "push my skills library somewhere safe"
- "make my skills library into a GitHub repo"

## User's default config (SeaXen)

When the user asks for a backup of `/root/.hermes/skills/`, **default to** these settings without re-asking:

| Setting | Default | Why |
|---|---|---|
| Visibility | **private** | Skills library contains personal context |
| License | **MIT** | Per repo convention |
| Cadence | **manual one-shot** | User said "manual" explicitly; cron variant is a future upgrade |
| Source | **full `/root/.hermes/skills/`** | User said "I want hermes other skill too, I mean all skill I have" |
| Wrapper README | included | Top-level `README.md` + `LICENSE` + `.gitignore` |
| INDEX.md | included | Carry the learnables INDEX.md into the mirror |
| Manifest | included | `_verbatim-manifest.json` travels with the tree |

Confirm only if the user explicitly opts into a different setting. Don't re-ask visibility, license, or cadence — the defaults are already what the user wanted last time.

## Pipeline (4 stages)

### Stage 1 — Survey

Before staging anything, gather the real numbers so you can present them in the final report:

```bash
# Total size and file count
du -sh /root/.hermes/skills
find /root/.hermes/skills -type f | wc -l

# Stripped size after typical excludes (dry-run)
rsync -a --dry-run \
  --exclude='.hub' --exclude='.curator_backups' \
  --exclude='*.log' --exclude='__pycache__' --exclude='*.pyc' \
  --exclude='.DS_Store' \
  /root/.hermes/skills/ /tmp/skill-size-test/ 2>&1 | tail -3

# Detect any >50 MB single files (GitHub warning threshold)
find /root/.hermes/skills -type f -size +50M -not -path '*/.git/*'

# Detect any credentials / .env / *.key / *.pem
find /root/.hermes/skills \( -name '.env*' -o -name '*.pem' -o -name '*.key' -o -name 'credentials*' \) -not -path '*/node_modules/*'

# Confirm gh auth + scope
gh auth status
gh api user -q .login
```

If credentials are present, **stop and ask the user** before staging. If a file >100 MB is present, decide whether to strip it (typical: yes — runtime logs).

### Stage 2 — Stage + init

1. Pick a staging dir (e.g. `/tmp/hermes-skills-backup-YYYYMMDD`). Do **not** stage under `/root` — keep staging under `/tmp` so it's outside the source tree.
2. rsync with excludes (this exact flag set is the canonical one, observed working in 2026-08):

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

3. **Hermes runtime state** that rsync pulled but you don't want in the backup — untrack after commit, or add to `.gitignore` BEFORE the initial commit:

- `.archive/` (directory)
- `.bundled_manifest` (file)
- `.curator_state` (file)
- `.usage.json` and `.usage.json.lock` (files)

Add them to `.gitignore` BEFORE `git add .`, or after-commit run `git rm -r --cached -f <path>` then amend the commit. The latter is more reliable when you forget to gitignore up front.

4. Write top-level files. Templates in `references/staging-bundle-pipeline.md`.

5. `git init` + commit:

```bash
cd "$STAGE"
git init -b main
git config user.email "<user-email>"
git config user.name "<user-name>"
git add .
git commit -m "Backup of ~/.hermes/skills on YYYY-MM-DD

- N files, M MB after stripping runtime caches
- N learnable repos, N verbatim leaves
- Hermes main categories: 46
- Latest additions: <list if known>"
```

6. **Bundle only if raw push fails** (see Stage 4). The user corrected this on 2026-08-15:
   "why bundle needed ? raw is not enough?" — the raw git tree on GitHub IS the
   backup. The bundle is a niche offline-restore artifact, not a parallel deliverable.
   Don't build one when raw push works, and don't auto-upload it as a release asset
   unless the user asks.

### Stage 3 — Create private GitHub repo + push

```bash
# Create empty repo first (don't pass --source until after this works)
gh repo create <user>/<repo-name> \
  --private \
  --license MIT \
  --description "Private backup of <user>'s complete Hermes skills library. Mirror of ~/.hermes/skills/."

# Add remote + push from the staging dir
cd "$STAGE"
git remote add origin https://github.com/<user>/<repo-name>.git
git config http.postBuffer 524288000   # 500 MB; raise if needed
git config http.version HTTP/1.1
git config --global http.lowSpeedLimit 0
git config --global http.lowSpeedTime 999999

git push --progress -u origin main
```

If push fails with **HTTP 408** or write completes but the response drops, see Stage 4.

### Stage 4 — Bundle + release (fallback only, not parallel)

GitHub's git backend periodically browns out (HTTP 408, `invalid index-pack output` on clones). **Only** use the bundle path when raw push actually fails — it is not a parallel deliverable and not a "belt and suspenders" improvement.

Build and upload a bundle only after raw push has been confirmed failed (not merely slow):

```bash
cd "$STAGE"
# Build the bundle ONLY if raw push failed
git bundle create /tmp/skills-backup-YYYYMMDD.bundle --all
git bundle verify /tmp/skills-backup-YYYYMMDD.bundle

# Then attach it to a release for download
gh release create vYYYY-MM-DD \
  --repo <user>/<repo-name> \
  --title "Skills Backup YYYY-MM-DD (N repos)" \
  --notes "<summary>" \
  --target main \
  /tmp/skills-backup-YYYYMMDD.bundle#skills-backup-YYYYMMDD.bundle
```

When raw push succeeds, stop at Stage 3. The bundle is a fallback artifact for offline restore, not a second copy that needs its own upload:

```bash
# Restore from bundle (offline / brownout workaround)
git clone /path/to/skills-backup-YYYYMMDD.bundle skills-backup
```

## Restore (anywhere)

```bash
# From git (preferred)
git clone https://github.com/<user>/<repo-name>.git ~/.hermes/skills

# From bundle (offline / brownout workaround)
git clone /path/to/skills-backup-YYYYMMDD.bundle ~/.hermes/skills
```

Hermes will discover the skills on next start.

## Brownout recovery (when GitHub is degraded)

The full pattern — observed during real backups in 2026-08 — is in
`references/github-brownout-recovery.md`. Quick summary:

| Symptom | Cause | Fix |
|---|---|---|
| `git clone ... invalid index-pack output` | GitHub packfile backend dropping data | back off 5-15s, retry single clone, max 3 attempts |
| `git push ... HTTP 408 curl 22` | Long-lived HTTPS connection dropped by GitHub or this host's network | `http.postBuffer=524288000`, `http.version=HTTP/1.1`, retry with longer patience |
| Push data writes succeed but response never returns | Same as 408 but server-side | the data may already be on the server — verify with `gh api repos/<user>/<repo>` size + `git ls-remote` |
| All of the above | GitHub-side brownout | fall back to bundle + `gh release create` |

**Critical pitfall**: do NOT retry aggressively. The brownout pattern observed in 2026-08-15 hit both `git clone` (8 parallel attempts → 5 failed) and `git push` (multi-attempt). Backing off + serial retry succeeded.

## What to NEVER include

Always strip these from the backup (caught during 2026-08-15 audit):

- `.hub/` — Hermes internal index cache (~40 MB, regenerable)
- `.curator_backups/` — old hermes-curator backups (~22 MB)
- `*.log` — runtime logs (one `browser_dashboard.log` was 86 MB; GitHub warns >50 MB)
- `.archive/` — Hermes runtime state
- `.bundled_manifest` — Hermes runtime
- `.curator_state` — Hermes runtime
- `.usage.json*` — Hermes runtime telemetry

Any credentials, `.env`, `*.pem`, `*.key`, or `credentials*` files — stop and ask the user.

## Verification

After successful push:

```bash
# Repo exists and has content
gh repo view <user>/<repo-name> --json name,visibility,diskUsage,defaultBranchRef

# Root has README, LICENSE, INDEX, gitignore
gh api repos/<user>/<repo-name>/contents/ | python3 -c "
import json, sys
files = json.load(sys.stdin)
for f in files:
    if not f.get('size'):
        print(f'  dir/  {f[\"name\"]}')
    else:
        print(f'  file {f[\"name\"]} ({f[\"size\"]} bytes)')
"
```

Tell the user the final state:
- Repo URL
- Visibility (private)
- Total file count + size after strip
- Number of learnable repos included
- Latest additions listed
- How to restore

## Pitfalls

- **Re-asking visibility/license/cadence** — the user's defaults are private + MIT + manual. Confirm only when the user explicitly opts out.
- **Re-asking the repo name** when the user said "a new repo" — propose one and proceed.
- **Staging under `/root`** — keeps the source and staging on the same volume; if the volume fills it can corrupt both. Stage under `/tmp`.
- **Skipping `.gitignore`** — without it, future syncs will try to re-add `.hub`, `.log`, etc.
- **Pushing from the source dir** instead of the staging dir — pollution risk.
- **Forgetting to set `http.postBuffer`** — default 1 MB, will fail any push >1 MB.
- **Forcing retries during GitHub brownout** — slows recovery. Back off and use bundle fallback.
- **Including credentials** in the staging tree — verify with `find ... -name '.env' -o -name 'credentials*'` BEFORE pushing.
- **Auto-uploading the bundle as a release asset** when raw push already succeeded — the bundle is a fallback, not a parallel deliverable. Per user correction 2026-08-15: "why bundle needed ? raw is not enough?" Build the bundle only when raw push fails.
- **Treating the bundle as required** — the raw git tree on GitHub IS the backup. The bundle is a niche offline-restore artifact. Don't keep one around by default.
- **Using `gh repo create --source` without first initing** — fails with "current directory is not a git repository".
- **`gh release create --target <sha>`** with the wrong format — use `--target main` (branch name) not the SHA. SHA caused `HTTP 422: Validation Failed: target_commitish is invalid` on 2026-08-15.

## Related

- `hermes-backup-watchers` — cron-style filesystem backup with notifications
- `hermes-git-config-snapshots` — small config drift detector
- `repo-deep-learn` — manifest reconciliation patterns referenced from this skill
- `sagar-hermes-ops` — Hermes ops meta-skill

## Support files

- `references/staging-bundle-pipeline.md` — exact rsync flags, gitignore template, README template, LICENSE template, bundle verification steps
- `references/github-brownout-recovery.md` — observed failure modes during 2026-08-15 brownout, backoff timing, when to fall back to bundle
- `references/exclude-patterns.md` — full list of what to strip with reasoning per category
