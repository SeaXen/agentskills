# Incremental updates to an existing backup repo (v1 → v2 → v3)

The base skill covers **initial creation**. This reference covers the **much more common case**: the user added new skills, wants them pushed to the same `SeaXen/skills-backup` repo that already has a prior commit on `main`.

Observed in production on 2026-08-15 when pushing v2 (192 repos) and v3 (202 repos) on top of v1 (184 repos).

## The core mistake: re-init loses history

The naive loop is:

```bash
rm -rf /tmp/hermes-skills-backup-20260815
rsync from /root/.hermes/skills/
git init -b main
git add . && git commit
git push -u origin main
```

This produces a commit with no parent — `git push` then fails with **non-fast-forward** because remote has the previous commit. Trying `git push --force` is destructive (drops remote history) and the safety layer often blocks it.

## The right loop (no force, no history loss)

```bash
STAGE=/tmp/hermes-skills-backup-YYYYMMDD
mkdir -p "$STAGE"

# Step 1: rsync current skills tree
rsync -a \
  --exclude='.hub' --exclude='.curator_backups' \
  --exclude='*.log' --exclude='__pycache__' --exclude='*.pyc' \
  --exclude='.DS_Store' \
  /root/.hermes/skills/ "$STAGE/"

# Step 2: write README/LICENSE/.gitignore (idempotent — overwrites existing)

# Step 3: reuse existing .git if present (so we keep history); otherwise init
cd "$STAGE"
if [ ! -d .git ]; then
  git init -b main
  git config user.email "..."
  git config user.name "..."
fi

# Step 4: rebase-style update on top of remote main
git fetch origin main
git checkout origin/main -- .   # overlay remote snapshot
git reset origin/main           # move HEAD to remote main (keeps it as parent)
git status                       # shows the new content as modifications

# Step 5: commit the deltas
git add -A
git commit -m "Backup v3: +repo1, +repo2, ..."

# Step 6: push (clean fast-forward, no force)
git push -u origin main
```

The key move is `git checkout origin/main -- .` + `git reset origin/main` — it overlays the remote tree and resets HEAD to the remote commit, so `git add -A && git commit` produces a new commit whose parent is the remote `main`. The push is then a textbook fast-forward.

If there are conflicts on README.md / manifest (which happens when both local and remote touched them), accept the local content — the local version reflects the current state of `/root/.hermes/skills/`, which is what we want in the mirror.

## Bundle release: keep old, add new

When iterating, **don't reuse the same release tag** — `gh release create v2026-08-15` fails with "a release with the same tag name already exists". Instead:

```bash
# Option A: append a new asset to the existing release (preserves v1 bundle)
gh release upload v2026-08-15 --repo SeaXen/skills-backup \
  /tmp/skills-backup-YYYYMMDD.bundle#skills-backup-YYYYMMDD-v3.bundle \
  --clobber

# Option B: create a new tag for each push
gh release create vYYYY-MM-DD-v3 --repo SeaXen/skills-backup \
  --title "Skills Backup YYYY-MM-DD (v3, N repos)" \
  --notes "..." \
  --target main \
  /tmp/skills-backup-YYYYMMDD.bundle#skills-backup-YYYYMMDD-v3.bundle
```

Option A is simpler and keeps the bundle history in one place. Option B is cleaner for users who want each push as its own version.

## Verification

After a clean fast-forward:

```bash
gh api repos/<user>/<repo-name>/git/refs/heads/main
# returns {"ref":"refs/heads/main", "object":{"sha":"<new sha>"}}
```

Cross-check the sha matches your local `git log -1 --format=%H` before claiming success.

## Pitfalls

- **`git push --force`** — destructive. The safety layer often blocks it (correctly). Use the rebase-style update instead.
- **`git rebase --abort` after conflicts** — if you tried rebase and got conflicts, aborting drops your v3 commit. Re-apply with `git checkout <your-sha> -- . && git reset origin/main` instead.
- **Empty `--target <sha>` for `gh release create`** — use `--target main` (branch name). SHA causes `HTTP 422: Validation Failed`.
- **Reusing release tags** — `gh release create v2026-08-15` after v2026-08-15 exists fails. Use `gh release upload` to add an asset, or create a new tag.
- **Bundle uploaded with same name as existing asset** — fails silently. Always use a distinct filename (`#skills-backup-YYYYMMDD-v3.bundle`).
- **Forgetting to update the local manifest** before re-staging — the remote will claim N repos but the source tree has N+k. Re-run the manifest update step from `repo-deep-learn` first.
