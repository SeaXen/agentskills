# Daily data sync to private GitHub repo (silent cron variant)

Use this when the user asks "is this repo updated daily?" or wants a local directory (Obsidian vault, config dir, dotfiles, knowledge base) auto-pushed to a private GitHub repo on a schedule. Distinct from the main `hermes-backup-watchers` pattern because:

- **No notifications** — silent cron (`deliver: 'local'`) so the user is not spammed
- **Agent-driven prompt** — not a `no_agent: true` script, because the cron needs to handle git merge, push retry, state writes, and structured logging without verbose output
- **Git-aware** — not a file-copy backup; needs `git add/commit/push` semantics with fast-forward merge

## When to use

- User says "is the SeaXen/foo repo updated daily with my local data?"
- User has a local directory that should mirror to a private GitHub repo nightly
- Existing pattern: `gh` CLI is already authenticated (`gh auth status` succeeds)
- Local directory is already a git repo with a configured `origin` remote
- The data is small enough that daily commits + pushes are cheap (< few hundred MB)

Do **not** use this for:
- Disaster-recovery backups (use the main `hermes-backup-watchers` skill)
- Real-time sync (use git hooks or push triggers)
- Large multi-GB directories (rate limits + clone times)
- Repos where you cannot run `git push` interactively (need a deploy key with push rights)

## Architecture

Three pieces:

1. **Sync script** (`/root/.hermes/scripts/<name>_daily_sync.py`) — does the git work
2. **Cron job** — agent-driven prompt that runs the script and reports a compact result
3. **State file** (`/root/.hermes/state/<name>-sync-state.json`) — last-run info, visible on dashboard

## Sync script pattern

```python
#!/usr/bin/env python3
"""
Daily sync of <source_dir> to <org>/<repo> GitHub repo.
Runs after upstream crons (e.g. 04:00 Asia/Dhaka = after mirror).
"""
from __future__ import annotations
import json, os, shlex, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

VAULT_REPO = Path(os.environ.get("OBSIDIAN_VAULT_PATH", "/root/.hermes/obsedianvault"))
GIT_REMOTE = "origin"
BRANCH = "main"
LOG_PATH = Path("/root/.hermes/cron/output/<name>-daily-sync.log")
STATE_PATH = Path("/root/.hermes/state/<name>-sync-state.json")

def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a") as f:
        f.write(line + "\n")

def git(*args, cwd=None) -> tuple[int, str, str]:
    p = subprocess.run(["git", *args], cwd=str(cwd or VAULT_REPO),
                       capture_output=True, text=True, timeout=120)
    return p.returncode, p.stdout.strip(), p.stderr.strip()

def get_changes() -> tuple[list, list, list]:
    rc, out, _ = git("status", "--porcelain")
    added, modified, deleted = [], [], []
    for line in out.splitlines():
        if not line.strip(): continue
        status = line[:2]
        path = line[3:].strip()
        if " -> " in path:  # rename
            path = path.split(" -> ", 1)[1]
        if status.startswith(("??", "A")): added.append(path)
        elif status.startswith("D"): deleted.append(path)
        elif status.startswith("R"): added.append(path)
        elif status.startswith("M"): modified.append(path)
    return added, modified, deleted

def main() -> int:
    if not VAULT_REPO.exists() or not (VAULT_REPO / ".git").exists():
        log(f"VAULT_REPO not a git repo: {VAULT_REPO}")
        return 2
    rc, branch, _ = git("rev-parse", "--abbrev-ref", "HEAD")
    if rc != 0 or branch != BRANCH:
        log(f"Expected branch {BRANCH}, got {branch!r}")
        return 3
    rc, _, err = git("fetch", GIT_REMOTE, BRANCH)
    if rc != 0:
        log(f"fetch failed (will continue with local + push): {err[:200]}")
    else:
        rc, _, err = git("merge", "--ff-only", f"{GIT_REMOTE}/{BRANCH}")
        if rc != 0:
            log(f"non-ff merge (continue with local + push): {err[:200]}")

    added, modified, deleted = get_changes()
    rc, out, _ = git("ls-files")
    note_count = sum(1 for f in out.splitlines() if f.endswith(".md")) if rc == 0 else 0
    log(f"Changes: +{len(added)} ~{len(modified)} -{len(deleted)}  notes={note_count}")

    if not (added or modified or deleted):
        log("Nothing to commit; sync complete (no-op)")
        save_state(0, 0, 0, note_count, "", True)
        return 0

    rc, _, err = git("add", "-A")
    if rc != 0:
        log(f"git add failed: {err}"); return 4

    today = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")
    bits = []
    if added: bits.append(f"+{len(added)} new")
    if modified: bits.append(f"~{len(modified)} updated")
    if deleted: bits.append(f"-{len(deleted)} removed")
    msg = f"Daily vault sync {today}: " + ", ".join(bits) + f" ({note_count} notes total)"

    rc, _, err = git("commit", "-m", msg)
    if rc != 0:
        if "nothing to commit" in (err or "").lower():
            log("Nothing staged after add; sync complete")
            save_state(0, 0, 0, note_count, "", True)
            return 0
        log(f"git commit failed: {err}"); return 4

    rc, sha, _ = git("rev-parse", "HEAD")
    log(f"Committed: {sha[:8]}  '{msg}'")

    rc, _, err = git("push", GIT_REMOTE, BRANCH)
    if rc != 0:
        log(f"git push failed rc={rc}: {err}")
        save_state(len(added), len(modified), len(deleted), note_count, sha, False)
        return 5
    log("Push successful")
    save_state(len(added), len(modified), len(deleted), note_count, sha, True)
    return 0

def save_state(added, modified, deleted, total, sha, ok):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    state = {"last_sync_utc": datetime.now(timezone.utc).isoformat(),
             "ok": ok, "added": added, "modified": modified, "deleted": deleted,
             "note_count": total, "commit_sha": sha}
    STATE_PATH.write_text(json.dumps(state, indent=2))

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        log(f"FATAL: {e!r}")
        sys.exit(99)
```

## Cron job pattern

Agent-driven prompt that runs the script and reports a compact summary. **Not** `no_agent: true` because git merge / push failures sometimes need LLM judgement, but the prompt is strictly read-only of the script:

```python
cronjob(
    action='create',
    deliver='local',     # silent — no Discord/Telegram spam
    name='<name>-daily-git-sync',
    prompt='''
Run the daily git sync script.

Execute: `python3 /root/.hermes/scripts/<name>_daily_sync.py`

Then report ONLY:
- exit code
- the summary line "Changes: +N ~M -K notes=T (commit=xxxxxxx)" if any commit was made, OR "Nothing to commit; sync complete (no-op)"
- the push status ("Push successful" or "git push failed ...")
- last 5 lines of /root/.hermes/cron/output/<name>-daily-sync.log

DO NOT modify the script, the source directory, or the repo. DO NOT touch other components. If the script fails (non-zero exit), report the error verbatim and stop.

Schedule: daily at 04:00 Asia/Dhaka.
'''.strip(),
    schedule='0 4 * * *',
)
```

## Auth pattern

`gh auth status` must already work for the user:

```bash
gh auth status
# ✓ Logged in to github.com account <user>
#   - Active account: true
#   - Git operations protocol: https
#   - Token: gho_****
```

The git push via HTTPS works because the token is stored in `~/.config/gh/hosts.yml`. SSH keys also work if configured.

If `gh auth status` fails, set up auth first:
```bash
gh auth login --web --git-protocol https
```

## State file pattern

Visible on dashboard via a `/api/cron-status`-style endpoint that reads the state JSON:

```json
{
  "last_sync_utc": "2026-06-17T11:00:00+00:00",
  "ok": true,
  "added": 3,
  "modified": 5,
  "deleted": 0,
  "note_count": 64,
  "commit_sha": "5b6978f9a1b2..."
}
```

The state file location convention: `/root/.hermes/state/<name>-sync-state.json`. Mirrors the existing pattern for `mnemosyne-mirror-state.json` etc.

## Manual trigger pattern

Cron jobs fire at the scheduled time. For on-demand sync, the agent can `cronjob(action='run', job_id=...)` to fire it immediately, OR just `python3 /root/.hermes/scripts/<name>_daily_sync.py` directly.

## Verification checklist

- [ ] Local directory is a git repo with `origin` configured
- [ ] `git push origin main` works manually with current `gh` auth
- [ ] `python3 /root/.hermes/scripts/<name>_daily_sync.py` exits 0 with empty vault
- [ ] `python3 ...` after `touch /tmp/test && mv /tmp/test <vault>/` creates a commit and pushes
- [ ] `cronjob(action='list')` shows the new job with correct schedule
- [ ] State file is created after first run
- [ ] `journalctl --user` shows the cron job firing and exiting cleanly
- [ ] `gh repo view <org>/<repo> --json pushedAt` shows the new commit timestamp
- [ ] No Discord/Telegram notifications (deliver='local')

## Common pitfalls

1. **Using `deliver='discord'` or similar** — spams the channel every day, even on no-op days. Use `deliver='local'` for silent daily sync.

2. **Setting `no_agent: true`** — removes the LLM but the script output is raw git noise. Use agent-driven prompt with strict "report ONLY" instructions instead, so the LLM formats the summary compactly while still being able to interpret non-trivial errors.

3. **Forgetting `merge --ff-only`** — when running on a schedule, the remote may have been pushed to by another machine. Without `--ff-only`, a non-fast-forward merge creates a merge commit, which is not what you want for a daily auto-sync. Either:
   - Always pull before push with `--ff-only` (current pattern), OR
   - Reject the push on conflict and alert the user

4. **Pushing during network outage** — the script's `git push` will fail. Catch the error, write state with `ok: false`, and let the next day's run retry. Don't crash the cron job.

5. **Committing timestamps as "now"** — if your repo uses GitHub Actions or other automation that compares timestamps, ensure the commit message includes `today` (local date) for human readability.

6. **Including `.obsidian/` or other workspace state in commits** — Obsidian's workspace cache files change every minute and will create noisy commits. Add a `.gitignore` that excludes `.obsidian/workspace*`, `.trash/`, etc.

7. **Using `git push --force`** — never force-push for a daily sync. If the fast-forward fails, the script should fail too, not clobber.

8. **No commit message convention** — keep it parseable: `Daily vault sync YYYY-MM-DD: +N new, ~M updated, -K removed (T notes total)`. The dashboard parses this format.

9. **Trying to handle renames as deletes + adds** — git's `--porcelain` already handles renames correctly. The script's `if " -> " in path: path = path.split(" -> ", 1)[1]` extracts the new name. Don't double-count.

10. **Auth token expiry mid-sync** — `gh` tokens can be revoked by GitHub. If the script suddenly fails to push for several days, check `gh auth status` and re-auth if needed.

## CRITICAL v2 fix: detect committed-but-unpushed changes

The original `get_changes()` only inspected `git status --porcelain`, which catches **uncommitted** working-tree changes. If the user already committed locally and just wants to push, the script reports `+0 ~0 -0` and exits as a no-op — the local commit stays unpushed until the user manually runs `git push`.

**Symptom** (this exact failure was hit in production on `obsmemory-daily-git-sync`):

```
[2026-06-17 17:42:33 +0600] Changes: +0 ~0 -0  notes=62
[2026-06-17 17:42:34 +0600] Nothing to commit; sync complete (no-op)
```

But `git log origin/main..HEAD --oneline` shows the local commit is ahead. The push never happened.

**Fix** — change `get_changes()` to also diff against the upstream branch:

```python
def get_changed_files() -> tuple[list[str], list[str], list[int]]:
    """Return (added, modified, deleted) since origin/main (or HEAD if no upstream)."""
    added, modified, deleted = [], [], []
    # 1. Uncommitted working-tree changes
    rc, out, _ = git("status", "--porcelain")
    for line in out.splitlines():
        if not line.strip(): continue
        status = line[:2]
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        if status.startswith(("??", "A")): added.append(path)
        elif status.startswith("D"): deleted.append(path)
        elif status.startswith("R"): added.append(path)
        elif status.startswith("M"): modified.append(path)
    # 2. Committed-but-unpushed changes vs upstream (CRITICAL)
    rc, out, _ = git("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    upstream = out.strip() if rc == 0 and out.strip() else None
    if upstream:
        rc, out, _ = git("diff", "--name-status", f"{upstream}..HEAD")
        if rc == 0:
            for line in out.splitlines():
                if not line.strip(): continue
                parts = line.split("\t", 1)
                if len(parts) != 2: continue
                status, path = parts[0], parts[1].strip()
                if status.startswith("A"): added.append(path)
                elif status.startswith(("M", "C", "T")): modified.append(path)
                elif status.startswith("D"): deleted.append(path)
                elif status.startswith("R"): added.append(path)
    return added, modified, deleted
```

Then in the main flow, **skip `git commit` if there is nothing uncommitted but there ARE upstream-vs-HEAD changes** — go straight to push:

```python
rc, _, err = git("add", "-A")
if rc != 0:
    log(f"git add failed: {err}"); return 4

rc, status_out, _ = git("status", "--porcelain")
has_uncommitted = bool(status_out.strip())

if not (added or modified or deleted):
    log("Nothing to commit; sync complete (no-op)")
    save_state(0, 0, 0, note_count, "", True)
    return 0

msg = commit_message(len(added), len(modified), len(deleted), note_count)
if has_uncommitted:
    rc, _, err = git("commit", "-m", msg)
    if rc != 0:
        log(f"git commit failed: {err}"); return 4
    rc, sha, _ = git("rev-parse", "HEAD")
    log(f"Committed: {sha[:8]}  '{msg}'")
else:
    # Already committed locally, just push
    rc, sha, _ = git("rev-parse", "HEAD")
    log(f"Already committed locally: {sha[:8]} (push only)")

rc, _, err = git("push", GIT_REMOTE, BRANCH)
# ... rest of push handling
```

**Why this matters**:
- `git status --porcelain` only sees the working tree, not the local branch state vs upstream
- A daily sync should always push the latest local state, whether it was committed locally first or not
- Without the fix, **the cron job silently fails to push for an indeterminate period** — until the user notices `origin/main` is behind and pushes manually

**Quick smoke test after the fix**:

```bash
cd <vault> && touch new.md && git add new.md && git commit -m "test"
# Now local is 1 commit ahead of origin
python3 /root/.hermes/scripts/<name>_daily_sync.py
# Expect: "Changes: +1 ~0 -0  notes=N" then "Already committed locally: <sha> (push only)" then "Push successful"
git log origin/main..HEAD --oneline   # should be empty after push
```

The same fix applies to any "git-aware sync" pattern, not just this one.

## Real-world example: obsmemory-daily-git-sync

Applied to the Obsidian vault at `/mnt/tb/hermes/obsedianvault` → `github.com/SeaXen/obsmemory`:

- Schedule: `0 4 * * *` (04:00 Asia/Dhaka, after the Mnemosyne mirror at 03:00)
- Script: `/root/.hermes/scripts/obsmemory_daily_sync.py` (~150 lines)
- Cron job: `obsmemory-daily-git-sync` (`job_id: 490ccac23e62`)
- State: `/root/.hermes/state/obsmemory-sync-state.json`
- Log: `/root/.hermes/cron/output/obsmemory-daily-sync.log`
- Repo: private (verified via `gh repo view` returning 404 from public API)

The dashboard's `/api/cron-status` endpoint reads the state file and shows it in the Cron tab. Operators can see at a glance when the last sync ran, how many files changed, and whether the push succeeded.
