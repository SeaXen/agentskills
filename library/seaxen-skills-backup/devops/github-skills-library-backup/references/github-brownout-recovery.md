# GitHub brownout recovery (observed patterns from 2026-08-15)

Real-world recovery notes from a single backup session on 2026-08-15. Use these when raw `git clone` or `git push` is hitting GitHub's git backend while `githubstatus.com` shows green.

## Symptoms observed

| Symptom | Where | Recovered by |
|---|---|---|
| `git clone --depth 1 ... invalid index-pack output` | clone phase | back off, retry, eventually worked after 5+ min |
| `git push --progress ... HTTP 408 curl 22` | push phase | `http.postBuffer=524288000` + `http.version=HTTP/1.1` |
| Push data writes succeed (100% objects sent) but response never returns | push phase | `git ls-remote` confirmed data actually arrived |
| `gh auth refresh ... timed out after 180s` | auth phase | came back when brownout ended |

## Critical lessons

### 1. The status page lies (or at least lags)

`https://www.githubstatus.com/api/v2/status.json` returned `{"indicator":"none","description":"All Systems Operational"}` while `git clone` was failing on 5 of 8 parallel attempts. Don't trust it as the sole signal — **trust your tool errors**.

### 2. Don't retry aggressively

When 5 of 8 parallel clones failed, the natural instinct was "retry the failures". That made things worse — GitHub's packfile backend was already degraded; 8 more parallel clones piled on top. Better pattern:

1. Stop all parallel work
2. Sleep 5-15 seconds
3. Run **one** test clone serially
4. If that succeeds, run the rest one at a time (not in parallel)
5. If that fails, drop to bundle-only mode

### 3. The push "failed" but the data arrived

Three back-to-back `git push` attempts in the 2026-08-15 session all returned `HTTP 408` after writing 100% of the pack to the wire. Verified with `gh repo view <user>/<repo-name> --json diskUsage,defaultBranchRef` — `defaultBranchRef.name == "main"` meant the push had actually succeeded; the response just dropped. So:

```bash
# Before assuming a failed push means a failed push:
gh api repos/<user>/<repo-name>/git/refs/heads/main
gh repo view <user>/<repo-name> --json diskUsage,defaultBranchRef
```

### 4. Bundle + release works when push doesn't

`gh release create` uploads through a different code path (HTTP multipart, not the git protocol). When the git backend is degraded, the release backend often still works. The bundle file is also smaller than the raw push payload, so even partial brownouts tend to complete.

```bash
# This worked after 3 raw push 408s:
gh release create v2026-08-15 \
  --repo SeaXen/skills-backup \
  --target main \
  /tmp/skills-backup-20260815.bundle#skills-backup-20260815.bundle
```

(The release upload itself can still take several minutes for a 29 MB bundle — that's expected, not a hang.)

### 5. CWD can stick in a deleted directory

When a `terminal` command's working directory gets deleted mid-execution (e.g. you `rm -rf` a clone in another tool call while a bash process is still inside it), subsequent `terminal` calls can inherit that broken CWD. Symptom:

```
bash: line 3: cd: /root/<deleted-dir>: No such file or directory
exit code 126
```

Workarounds in priority order:

1. Use `execute_code` instead of `terminal` (it does NOT inherit CWD the same way)
2. Pass `workdir=` explicitly on every `terminal` call
3. Prepend `cd / && ...` to your command

### 6. Long-running tool calls can drop Hermes Discord

Per user memory (2026-08-14): "stop doing this every time you do this hermes discord get offline — long-running network tests (WARP connect/disconnect cycles, multi-minute speedtests) make Hermes Discord appear offline on this host. Avoid these tests unless explicitly asked and warned first."

This applies to **any** multi-minute network operation on this host, including:

- `git push` of large bundles (3-5 minutes is normal)
- `gh release create` with large assets (similar)
- `gh auth refresh` while GitHub is degraded (timed out at 180s in our session)

**Mitigation:** run these in **background** (`terminal(background=true, notify_on_complete=true)`), so they don't block the heartbeat. Don't run multiple long network operations concurrently.

## Recovery checklist

When `git push` returns 408, work through this in order:

```bash
# Step 1: verify it didn't actually succeed
gh api repos/<user>/<repo-name>/git/refs/heads/main

# Step 2: if not pushed, sleep 10s and retry with the configs
git config http.postBuffer 524288000
git config http.version HTTP/1.1
git push --progress -u origin main

# Step 3: if still failing, drop to bundle + release
gh release create vYYYY-MM-DD --repo <user>/<repo-name> \
  --target main \
  /tmp/skills-backup-YYYYMMDD.bundle#skills-backup-YYYYMMDD.bundle

# Step 4: report to user honestly — "raw push failed, but bundle uploaded via release"
```

## What I will NOT do

Per the user's 2026-08-14 correction: I will NOT run network speedtests, WARP connect/disconnect cycles, or other multi-minute network probes unless explicitly asked. If a backup is stuck, I report status to the user and wait for their "retry" signal rather than thrashing.
