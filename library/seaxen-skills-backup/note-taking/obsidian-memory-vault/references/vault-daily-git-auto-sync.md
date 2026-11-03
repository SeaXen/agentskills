# Vault Daily Git Auto-Sync — Reference

Working pattern for keeping a private GitHub vault repo in sync with the
live Obsidian vault every day. Built and tested 2026-06-17 with
`SeaXen/obsmemory` (private, 62 notes).

## Why this exists

Manually pushing the vault every few days works for a one-time backup,
but it drifts silently. A daily cron gives:

- **Audit trail** — every change to the vault gets a dated commit
- **Offsite backup** — if the local disk dies, every note is on GitHub
- **Diff visibility** — `git log` becomes "what changed in the vault"
- **Cross-device sync** — clone on a new machine and you have the full vault

## Setup (one-shot)

### 1. The sync script

Save as `/root/.hermes/scripts/obsmemory_daily_sync.py`. The script:

1. Verifies vault is a git repo on the right branch with a remote
2. Fetches + fast-forward merges from origin (non-destructive)
3. Detects changes in BOTH the working tree AND committed-but-unpushed
   (Pitfall A — see below)
4. Stages and commits with a dated summary message:
   `Daily vault sync YYYY-MM-DD: +N new, ~M updated, -K removed (T notes total)`
5. Pushes to `origin main`
6. Writes result to `/root/.hermes/state/obsmemory-sync-state.json`
7. Logs to `/root/.hermes/cron/output/obsmemory-daily-sync.log`

Key implementation points:

```python
def get_changed_files():
    """Return (added, modified, deleted) files vs upstream."""
    added, modified, deleted = [], [], []
    # 1. Working tree (uncommitted)
    rc, out, _ = git("status", "--porcelain")
    for line in out.splitlines():
        status, path = line[:2], line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if status.startswith(("??", "A", "R")):
            added.append(path)
        elif status.startswith("D"):
            deleted.append(path)
        elif status.startswith("M"):
            modified.append(path)

    # 2. Committed-but-unpushed (Pitfall A — see below)
    rc, up, _ = git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    if rc == 0 and up.strip():
        rc, out, _ = git("diff", "--name-status", f"{up.strip()}..HEAD")
        for line in out.splitlines():
            parts = line.split("\t", 1)
            if len(parts) != 2:
                continue
            status, path = parts[0], parts[1].strip()
            if status.startswith("A"):
                added.append(path)
            elif status.startswith(("M", "C", "T")):
                modified.append(path)
            elif status.startswith("D"):
                deleted.append(path)
            elif status.startswith("R"):
                added.append(path)
    return added, modified, deleted
```

```python
# Pitfall B — skip empty commit when already committed locally
rc, status_out, _ = git("status", "--porcelain")
has_uncommitted = bool(status_out.strip())
if has_uncommitted:
    git("commit", "-m", msg)
else:
    sha = git("rev-parse", "HEAD").stdout.strip()
    log(f"Already committed locally: {sha[:8]} (push only)")
```

Full script (~200 lines) lives at `/root/.hermes/scripts/obsmemory_daily_sync.py`.

### 2. Hermes cron job

Use the `cronjob` tool with a model-light prompt:

```python
cronjob(action='create',
  name='obsmemory-daily-git-sync',
  schedule='0 4 * * *',   # 04:00 Asia/Dhaka daily
  prompt='''Run the Obsidian vault → private GitHub repo daily sync.

Execute: `python3 /root/.hermes/scripts/obsmemory_daily_sync.py`

Report ONLY:
- exit code
- the summary line "Changes: +N ~M -K notes=T ..." if any commit was made, OR "Nothing to commit; sync complete (no-op)"
- "Push successful" or "git push failed ..."
- last 5 lines of /root/.hermes/cron/output/obsmemory-daily-sync.log

DO NOT modify the script, the vault, or the repo. DO NOT touch Mnemosyne.
If the script fails, report the error verbatim and stop.''',
  deliver='local')
```

`deliver='local'` keeps the run quiet (no Discord spam) unless you want
to be told every day. Switch to `'origin'` or `'all'` if you want a
daily "sync ok" notification.

### 3. Verify end-to-end

```bash
# Dry-run the script
python3 /root/.hermes/scripts/obsmemory_daily_sync.py
echo "exit=$?"
cat /root/.hermes/state/obsmemory-sync-state.json

# Confirm origin got the new commit
cd /mnt/tb/hermes/obsedianvault && git log --oneline origin/main | head -3

# Confirm the dashboard Cron tab shows ✓ ok for obsmemory-daily-git-sync
# Open http://localhost:6065/ → Cron tab
```

## Schedule

Run **after** other vault-maintenance crons so the sync sees the latest
state. Suggested order on a single host:

| Time  | Cron                                                       |
|-------|------------------------------------------------------------|
| 02:00 | nightly high-signal log (vault digest)                     |
| 03:00 | Mnemosyne → vault mirror (if used)                          |
| 04:00 | **obsmemory daily git sync** (this pattern)                 |

`0 4 * * *` (04:00 Asia/Dhaka daily) is the default. Adjust by timezone.

## State inspection

The state file `/root/.hermes/state/obsmemory-sync-state.json` is the
last-run summary. The dashboard `/api/cron-status` reads it back so
the Cron tab can show "✓ ok / ✗ fail" and the commit SHA inline:

```json
{
  "last_sync_utc": "2026-06-17T11:43:19.703506+00:00",
  "ok": true,
  "added": 1, "modified": 0, "deleted": 0,
  "note_count": 62,
  "commit_sha": "5b6978f8dcff486366ac995abd5c7d0b5f18c660"
}
```

The Cron tab panel renders:
- `Last sync` (UTC timestamp)
- `Commit` (short SHA)
- `Changes` (color-coded `+`/`~`/`-`)
- `Notes total`
- `Status` (green `pushed ok` or red `push failed`)
- `Remote` (`github.com/OWNER/REPO (private)`)

## Two pitfalls I actually hit (2026-06-17)

### Pitfall A — `git status --porcelain` does NOT show committed-but-unpushed changes

A first version of the script only called `git("status", "--porcelain")`.
That returns NOTHING for files already committed locally but not yet
pushed. So when I added a note manually (committing it locally with
`git commit`) and then ran the sync, the script reported "Nothing to
commit; sync complete (no-op)" — even though origin was behind by one
commit.

**Fix**: `get_changed_files()` must look at BOTH the working tree AND
`git diff <upstream>..HEAD`. The two passes catch the full delta.

### Pitfall B — empty `git commit` failure when files were already committed

If the change is "committed locally but unpushed", `git add -A` is a
no-op and `git commit -m "..."` fails with empty stderr and exit code 1.
`--allow-empty` would help, but the cleaner pattern is to detect the
no-op and skip the commit step entirely.

**Fix**: check `git status --porcelain` after `git add -A`. If empty,
skip `git commit` and go straight to `git push`. Get the SHA via
`git rev-parse HEAD` regardless.

```python
rc, status_out, _ = git("status", "--porcelain")
has_uncommitted = bool(status_out.strip())
if has_uncommitted:
    rc, _, err = git("commit", "-m", msg)
    ...
else:
    rc, sha, _ = git("rev-parse", "HEAD")
    log(f"Already committed locally: {sha[:8]} (push only)")
```

## What to do if the sync fails

| Symptom                                            | Likely cause                | Fix                                                       |
|----------------------------------------------------|------------------------------|-----------------------------------------------------------|
| `git push failed rc=...` with auth error          | gh token expired            | `gh auth login --with-token`                              |
| `non-ff merge` after fast-forward                  | remote diverged             | `git -C vault pull --rebase origin main` then re-run     |
| `nothing to commit; sync complete (no-op)` but you made changes | Pitfall A — script only checks working tree | Already fixed; upgrade the script. |
| Cron job exits with 0 but state file missing       | STATE_PATH dir doesn't exist | mkdir -p `/root/.hermes/state/` (script does it but check) |
| Log file grows without bound                       | No log rotation             | Add a `logrotate` rule or rotate manually each month     |

## Variations

**Two-device sync.** The script is one-way (vault → remote). If you also
edit the vault on another machine and push from there, you need to pull
before the script runs. Add to the script:

```python
rc, _, err = git("pull", "--ff-only", GIT_REMOTE, BRANCH)
if rc != 0:
    log(f"pull failed (non-ff or conflict): {err}")
    # Don't abort — try to push what we have; the conflict will surface there
```

**Multi-vault.** Point `OBSIDIAN_VAULT_PATH` at each vault and register
one cron per vault with different `name` and `LOG_PATH`/`STATE_PATH`.
Use `name='obsmemory-<vault-slug>-daily-git-sync'` to keep the Cron
tab readable.

**Public repo.** Drop `--private` from `gh repo create`. The rest of
the script doesn't care; `git push` works the same way.

## Shipping non-vault code through the vault repo

The daily sync catches ANY change in the vault working tree, including
non-note files. Use this to back up code artifacts (dashboard script,
helper scripts, config templates) alongside the notes, so a fresh
clone of the private repo restores both.

Pattern (tested 2026-06-17 with `obsidian_dashboard.py`):

1. Pick a subdir of the vault for the code: `dashboard/`, `scripts/`, `config/`.
2. Copy the live file in (e.g. `cp /mnt/tb/hermes/obsidian_dashboard.py vault/dashboard/`).
3. Add a `README.md` next to it explaining what the file is, what it depends on, and how to run it.
4. `git add` and `commit` with a meaningful message. The next daily sync auto-pushes it.
5. To update: edit the live file, restart the service (`systemctl --user restart <name>`), then `cp` the updated file into the vault subdir. Daily sync pushes the new version overnight.

**Pitfall — legacy hidden folder collision.** If the same file was
previously tracked in a hidden subdir (e.g. `.dashboard/obsidian_dashboard.py`)
the daily sync will keep tracking it as a duplicate. Add the legacy
path to `.gitignore` AND `git rm --cached <legacy-path>` to untrack it
in one atomic commit. Without the `git rm --cached`, the file stays in
the repo history forever (visible at the old path on older commits).
Real example: `.dashboard/obsidian_dashboard.py` (303KB duplicate) →
`git rm --cached` + add `.dashboard/` to `.gitignore` + commit
"untrack legacy duplicate, real one is /dashboard/".

**Verification:**
```bash
# Confirm the file is on the remote
gh api repos/OWNER/REPO/contents/dashboard 2>/dev/null | python3 -c "import json,sys; [print(f['name'], f['size'], 'bytes') for f in json.load(sys.stdin)]"
# Should list README.md and obsidian_dashboard.py
```

## Pairs with

- **`references/vault-as-private-git-repo.md`** — one-shot setup,
  `.gitignore`, README template, and verification commands. Do that
  first, then add this daily-sync cron.
