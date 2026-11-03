---
name: hermes-backup-watchers
description: Use when creating, fixing, or restyling Hermes backup cron jobs that run scripts and post clean Discord/Telegram notifications.
version: 1.5.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, backup, cron, notifications, discord, scripts, silent-on-success, failure-only, git-snapshots]
    related_skills: [hermes-agent, systematic-debugging, hermes-git-config-snapshots]
---

# Hermes Backup Watchers

## Overview

Use this when Hermes backup jobs should run as deterministic script-based cron jobs and send clean, human-scannable notifications instead of raw stdout dumps or LLM-formatted summaries.

This pattern is for backup jobs like daily core backup and weekly full backup. It keeps the backup execution in Python scripts, formats success/failure messages in wrapper scripts, and uses `no_agent: true` cron jobs so notifications are stable and cheap.

## When to Use

- A Hermes backup cron job posts ugly raw `KEY=VALUE` output
- A backup job should notify with emoji, compact sections, and destination labels
- A backup fails because a live cache/temp file disappears during tar creation
- A weekly backup is still prompt-driven and should be converted to deterministic script mode
- The user wants daily and weekly backup alerts to match visually

Do not use this for generic data-watch cron jobs that need LLM summarization. Those should remain agent-driven if reasoning is required.

## Preferred Architecture

### 1. Split execution from notification

Keep two layers:

- **backup script**: does the actual archive/encryption/copy/prune work
- **notify wrapper**: runs the backup script, parses stdout, formats the final message

Example paths:
- `/root/.hermes/scripts/hermes_daily_full_backup.py`
- `/root/.hermes/scripts/daily_full_backup_notify.py`
- `/root/.hermes/scripts/hermes_weekly_full_backup.py`
- `/root/.hermes/scripts/weekly_full_backup_notify.py`

### 2. Prefer cron `script=...` + `no_agent=true`

For stable watcher-style delivery, update the job to use the wrapper script directly:

- `script: daily_full_backup_notify.py`
- `script: weekly_full_backup_notify.py`
- `no_agent: true`
- keep delivery target explicit

This avoids model variability and makes formatting deterministic.

### 2b. Set cron script timeout explicitly for real backups

Hermes cron no-agent scripts are governed by the scheduler timeout, not just the wrapper's internal `subprocess.run(..., timeout=...)` value. The scheduler default is only 120 seconds unless overridden.

For backup jobs, set `cron.script_timeout_seconds` in `~/.hermes/config.yaml` high enough for real archive + encryption + copy latency. Practical baseline:

- daily core backup: at least `600`
- weekly full backup: at least `900`
- if both run under the same Hermes instance, a global `cron.script_timeout_seconds: 900` is the simple safe default

Important pitfall: a wrapper may allow 600s internally while Hermes cron still kills the wrapper at 120s. If a cron alert says `Script timed out after 120s: ...notify.py`, that is a scheduler timeout mismatch, not proof that the backup logic itself failed.

See `references/cron-timeout-vs-wrapper-timeout.md` for details.

### 3. Make live-file backup code resilient

If the backup walks a live Hermes home, transient files can disappear mid-run. The tar builder should not abort on that.

Use a helper like:

```python
def safe_tar_add(tar, src, arcname):
    try:
        tar.add(src, arcname=arcname, recursive=False)
        return True
    except FileNotFoundError:
        print(f'WARN_SKIPPED_MISSING={src}')
        return False
```

Then replace direct `tar.add(...)` calls with `safe_tar_add(...)` and increment counts only on success.

This converts a race-condition crash into a partial-success condition the wrapper can explain cleanly.

### 4. Treat multi-destination copy failures as partial success when at least one save worked

If the archive is created successfully and copied to at least one destination, a later copy failure to another destination should not be reported as a total backup failure.

Preferred behavior in the shared backup code:

- wrap each destination copy in `try/except`
- on success, emit normal lines:
  - `SAVED <path>`
  - `PRUNED <dest>: <removed>`
- on failure, emit a structured warning line instead of aborting immediately:
  - `WARN_DEST_FAILED=<dest>|<ExceptionType>: <message>`
- return success (`0`) if **at least one** destination save succeeded
- return failure only if **no** destination save succeeded

Then update wrapper parsers to treat `WARN_DEST_FAILED=` the same way they treat skipped live files: the message should become `PARTIAL SUCCESS`, not `FAILED`.

## Notification Formatting Pattern

### Success

Use this shape:

```md
## 🌙✅ Hermes Daily Core Backup
`✅ SUCCESS · daily snapshot complete`

- **📦 Archive:** `...`
- **🏷️ Label:** `...`
- **📏 Size:** ...
- **🗂️ Files:** `...`
- **🧠 SQLite snapshots:** `...`

### 💾 Saved destinations
- 💽 Local TB → `...`
- ☁️ Google Drive → `...`

### ♻️ Retention
- Keep last `N` backups
- Pruned this run: `M`
- ...
```

When the user asks for daily / weekly / Mnemosyne notifications to match visually, normalize the exact section headers and spacing across all scripts. Prefer:

- `### 💾 Saved destinations`
- `### ♻️ Retention`
- blank line before each section header
- the same failure headers across scripts:
  - `### 🔎 Failure summary`
  - `### 🛠️ Next checks`

Also align the main backup field labels/icons across daily and weekly wrappers unless the user explicitly wants different ones:

- `📦 Archive`
- `🏷️ Label`
- `📏 Size`
- `🗂️ Files`
- `🧠 SQLite snapshots`

### Partial success

If `WARN_SKIPPED_MISSING=` lines were seen, switch to a warning title/status and add a notice block:

```md
## 🌙⚠️ Hermes Daily Core Backup
`⚠️ PARTIAL SUCCESS · archive completed with transient skipped files`

> ℹ️ Some live cache/temp files disappeared during backup and were skipped on purpose.
> Skipped `N` transient files.
```

Show up to the first 3 skipped paths, then summarize with `+N more`.

### Failure

Use a compact failure summary instead of raw cron noise:

```md
## 🌙❌ Hermes Daily Core Backup Failed
`❌ FAILED · exit code 1`

### 🔎 Failure summary
```text
<tail of output>
```

### 🛠️ Next checks
- Re-run: `python3 /root/.hermes/scripts/hermes_daily_full_backup.py`
- Check timeout and destination mounts
- Inspect Hermes cache/skill churn if missing-file warnings appeared
```

## Parsing Contract

Have the backup script print structured stdout lines the wrapper can parse:

- `SAVED <path>`
- `PRUNED <dest>: <removed>`
- `LABEL=<value>`
- `FILES=<n>`
- `SQLITE_BACKUPS=<n>`
- `ARCHIVE=<filename>`
- `SIZE_BYTES=<n>`
- optional: `WARN_SKIPPED_MISSING=<path>`

The wrapper should parse only these stable fields and ignore irrelevant noise.

### Cron Update Workflow

1. Inspect current jobs:
   - `cronjob(action='list')`
2. Confirm daily/weekly backup jobs and current delivery targets
3. Update prompt-driven weekly jobs to wrapper-script mode:
   - `cronjob(action='update', job_id=..., script='weekly_full_backup_notify.py', no_agent=true, prompt='', skills=[], enabled_toolsets=['terminal'])`
4. Keep schedule and deliver target unchanged unless the user asked otherwise
5. Re-list jobs and verify `script`/`no_agent` fields actually changed

### Passing arguments to no_agent scripts (critical)

The `script` field accepts **only the filename** (e.g. `daily_full_backup_notify.py`).

You **cannot** append arguments like:
```
script: hermes_plain_backup.py --dest /path --keep 8
```

This will be interpreted as a literal filename and fail with "Script not found".

**Correct pattern:**
- Create a thin wrapper script in `/root/.hermes/scripts/` that hardcodes the parameters and calls the main script.
- Example: `plain_local_6h.py` that runs `hermes_plain_backup.py --dest ... --keep 8`
- Then use `script: plain_local_6h.py` in the cron job.

This pattern was required when adding parameterized plain backups alongside the existing archive backups.

## Verification Checklist

- [ ] Backup common code skips transient missing files instead of crashing
- [ ] Daily wrapper prints clean success output
- [ ] Weekly wrapper prints clean success output
- [ ] Failure formatting is compact and readable
- [ ] Partial-success formatting appears when skipped-file warnings exist
- [ ] Daily cron uses wrapper script with `no_agent=true`
- [ ] Weekly cron uses wrapper script with `no_agent=true`
- [ ] Delivery target is still the intended Discord/Telegram channel

## Failure-Only Delivery (Silent on Success)

When a backup runs frequently (e.g. every 6 hours) and the user only wants to be notified when something is wrong, prefer an **agent-driven cron prompt** that posts to a backup channel **only on failure**. This is distinct from the wrapper-script + no_agent pattern above:

| Pattern | When to use |
|---|---|
| wrapper script + `no_agent=true` | back-of-house backups where the formatted message itself is the deliverable (e.g. daily archive summary with destinations / retention / size) |
| wrapper script + `no_agent=true` + **silent-on-success gate** | high-frequency backups (6h/12h) where the user wants silence on success and only a ping on partial/failure. Same script architecture, but the wrapper returns without printing anything unless something is wrong |
| agent-driven cron prompt with `deliver=discord:<channel>` | when the prompt itself needs to reason about output before deciding to ping (e.g. multi-stage pipelines, conditional alerting) |

### Wrapper-Script Silent-on-Success Pattern (added 2026-07-10)

For wrapper scripts that already parse structured stdout, add a single gate at the end of `main()`. The cron runner delivers the wrapper's stdout to Discord — **empty stdout = no delivery**, so we just suppress the success-path `print()`:

```python
try:
    parsed = parse_stdout(proc.stdout)
except Exception as exc:
    print(build_failure_message(2, f"Parse error: {exc}\n\nRaw stdout:\n{proc.stdout}"))
    return 0

# Silent on full success. Notify only if there were skipped/dest failures.
has_partial = bool(parsed["skipped_missing"] or parsed["dest_failures"])
if has_partial:
    print(build_success_message(parsed))
return 0
```

For plain-backup wrappers that parse errors into `parsed["errors"]`:

```python
has_errors = bool(parsed["errors"])
if has_errors:
    print(build_success_message(parsed))
return 0
```

For cleanup/retention jobs (no rich parsed data, just pass/fail per step), return errors instead of printing, then print only on actual errors:

```python
def keep_latest_n(n=KEEP) -> list[str]:
    """Returns list of delete errors. Empty list = success."""
    ...
    errors = []
    for _, name in to_delete:
        code, _, err = run(["rclone", "deletefile", ...])
        if code != 0:
            errors.append(f"{name}: {err}")
    return errors

def main():
    delete_errors = keep_latest_n()
    trash_ok = empty_trash()

    if delete_errors or not trash_ok:
        # Only print if there is actually something to report
        print("\n".join([
            "## ❌ Cleanup Failed",
            f"`{len(delete_errors)}` delete errors",
            ...
        ]))
    return 0
```

**Why this works:** cron `no_agent=true` runs the script, captures stdout, and delivers it verbatim to the configured Discord channel. No stdout = no message. The gate in `main()` is the only thing that needs to change — the entire parsing/messaging stack stays intact.

**Important:** never `print()` debug info on the success path (e.g. `KEEP: 1 archive(s)`) or it will get delivered to Discord. Move all success-path logging to stderr if you need it for debugging.

The failure-only prompt shape (proven on `hermes-config-snapshot-6h`, schedule `0 */6 * * *`):

```
You are a Hermes cron agent. Run <script.sh> [args...].
On success: stay silent — no tool call, no message.
On failure: post ONE concise message to Discord channel <channel_id>:
  ❌ <job-name> FAILED at <UTC ISO timestamp>
  <code: exit code>
  <first 5 lines of stderr/stdout>

Rules:
- Do NOT post to Discord on success.
- Do NOT post twice on failure.
- Do not retry on failure.
- Do not modify any files under <protected path>.
```

Key points:
- **`deliver=discord:<channel_id>`** is set on the cron job — that delivery target is the *agent's home channel* when the prompt needs to send a message, but the prompt is the gate: if it never calls a tool, nothing is delivered.
- The script itself returns exit 0 on success and non-zero on failure. The cron prompt's success-path is "no tool call", which is the cleanest way to get true silence.
- Success-path silence means the channel only ever shows real failures — high signal-to-noise for a `#💾│daily-backup` channel that gets a 6h cadence.
- Watch out for the script accidentally printing success-indicators that the agent interprets as needing acknowledgement; the prompt should explicitly tell the agent which stdout lines count as "success" (e.g. `pushed <path> -> origin/main` or `no committable changes since last snapshot`).

This pattern pairs naturally with a small wrapper script that:
- exits 0 if the underlying work was successful OR a no-op (dedup)
- exits non-zero only on real failures
- prints structured stdout the agent can quote in a failure message

Combine with `workdir=<repo-path>` so the agent's tools resolve git/file operations against the right tree.

### Companion pattern: yaml-lint + drift-watchdog alongside the snapshot cron

The `hermes-git-config-snapshots` skill runs a 6h snapshot cron plus **two** additional watchdog crons that should be wired in parallel:

| Cron | Schedule | Detects |
|---|---|---|
| `hermes-config-snapshot-6h` | `0 */6 * * *` | captures redacted config to git (push) |
| `hermes-yaml-lint-30m` | `*/30 * * * *` | YAML parse errors in `~/.hermes/config.yaml` or `profiles/*/config.yaml` |
| `hermes-drift-watchdog-6h` | `30 */6 * * *` | >50 lines drift since last mirror (catches silent reverts) |

All three deliver to the same Discord channel (id `1509927046258757792`) on failure only. The lint and drift watchdogs are the layer that catches "Hermes silently fell back to .env because config.yaml is malformed" — a failure mode that the snapshot cron alone cannot detect (it copies files, doesn't parse them).

Critical pitfall: if you wire the drift watchdog AFTER a manual restore from an older mirror, the **first tick will report false-positive drift** because the restore itself changed config relative to the most recent mirror. Fix by running `snapshot-all.sh` manually once after the restore to set a clean baseline.

See `hermes-git-config-snapshots` skill for the full pattern and the upstream issue draft.

## Daily-Only Retention Cleanup

Use this when the backup design has been simplified from `daily + weekly` to `daily only` and the user wants old weekly artifacts removed.

Balanced retention for this simplified setup:

- keep last `3` top-level backup archives **per destination**
- delete **all** old weekly backup archives
- keep cron output logs for `7 days`
- keep state snapshot directories for `3 days`

Important details:

1. Apply retention independently to each destination root. A local disk and Google Drive mirror may not contain the exact same archive set.
2. Delete weekly archives by filename/class first, then prune remaining non-weekly archives down to the target count.
3. Do not promise snapshot deletion unless old snapshot directories actually exist. A system may only have one recent `state-snapshots/` directory, in which case nothing should be removed.
4. Verify post-cleanup counts explicitly instead of assuming prune logic worked.

Practical verification targets after a balanced cleanup:

- local backup root: `3` top-level `.tar.gz.gpg` archives
- remote backup root: `3` top-level `.tar.gz.gpg` archives
- cron output older than 7 days: `0`
- remaining snapshot dirs: whatever is within the 3-day window

## One-Shot Verification Commands

Run wrappers directly:

```bash
python3 /root/.hermes/scripts/daily_full_backup_notify.py
python3 /root/.hermes/scripts/weekly_full_backup_notify.py
```

Test the missing-file guard in isolation:

```bash
python3 - <<'PY'
import tarfile, tempfile
from pathlib import Path
import sys
sys.path.insert(0, '/root/.hermes/scripts')
import hermes_backup_common as h

with tempfile.TemporaryDirectory() as td:
    tar_path = Path(td) / 't.tar'
    missing = Path(td) / 'gone.txt'
    with tarfile.open(tar_path, 'w') as tar:
        print(h.safe_tar_add(tar, missing, 'gone.txt'))
PY
```

Test formatting helpers without running a real backup by importing the notify script and calling `build_success_message()` / `build_failure_message()` with synthetic parsed data.

## Common Pitfalls

1. **Leaving weekly backup as an LLM cron prompt.** That reintroduces ugly variable formatting.
2. **Fixing the crash by excluding only one filename.** Better to harden the tar add path generally.
3. **Calling the archive a full failure when only transient cache files vanished.** That should be partial success.
4. **Overwriting cron delivery target accidentally while updating script mode.** Re-check `deliver` after updates.
5. **Parsing stderr/stdout loosely.** Keep the backup script output contract explicit and stable.
6. **Trusting the wrapper's own timeout while ignoring Hermes cron's scheduler timeout.** The scheduler default is 120s; longer-running backup wrappers need `cron.script_timeout_seconds` raised or they will be killed even if the inner backup command allows more time.
7. **Misreading ambiguous cron directives like "12 hourly" as "keep 12, hourly cadence".** The user almost always means **"keep N, run every N units"** (e.g. "12 hourly" → keep 12, every 12 hours). The two dimensions — retention count and schedule cadence — are independent variables, and the natural reading is **both equal**. Before updating a cron job from a short directive, run `cronjob(action='list')` to confirm both fields, and if the directive is ambiguous, ask one clarification question rather than guessing. A wrong schedule can mean 24x more frequent runs (or 12x fewer) than intended — a real cost on Discord noise, quota, or backup coverage gaps.
8. **Reporting file changes imprecisely after a no-op patch.** If a verifier says a file was not modified because `old_string` and `new_string` were identical, treat that as a reporting correction, not as a code defect.
8. **GDrive trash accumulation causing backup timeouts** — the `plain_gdrive_daily_notify.py` job times out after 1200s because `rclone delete --drive-trashed-only` on a massive trash takes too long. Disable trash emptying for daily plain backups or increase `cron.script_timeout_seconds` to 18000. See `references/gdrive-trash-and-retention.md`.
9. **Scheduler timeout vs wrapper timeout mismatch** — Hermes cron's global `script_timeout_seconds` (default 120s) kills scripts even if the wrapper allows more. Always set `cron.script_timeout_seconds` in config.yaml to match the longest-running backup job. See `references/cron-timeout-vs-wrapper-timeout.md`.
10. **Staging-dir leak from `.tmp-hermes-backup` / `.restore-tests`** — Backup and restore scripts create per-run staging directories (e.g. `/mnt/tb/.tmp-hermes-backup/hermes-archive-<id>/`, `.tmp-hermes-backup/hermes-backup-<id>/sqlite/`, `.restore-tests/hermes-restore-<id>/`) but never delete them. On a long-running system this silently accumulates tens of GB of unencrypted intermediates that already have encrypted `.tar.gz.gpg` copies in the final destination. Add a final `cleanup_staging(staging_dir, label)` step to every backup/restore script after the encrypted copy is verified, emit `STAGING_CLEANED=<label>|<dir>|<bytes>` so the wrapper can report bytes reclaimed, and run a monthly audit (`du -sh /mnt/tb/.tmp-hermes-backup /mnt/tb/.restore-tests`) to catch regressions. See `references/staging-dir-leak.md`.
10b. **`hermes-backups/#plain` sprawl on HDD** — six-hour plain cron can leave **8+ × ~7G** trees under `/mnt/tb/hermes-backups/#plain/`. That often exceeds all Docker images combined. Prune by keeping last N folders (user confirms N) before running `docker` cleanup. Cross-check with `references/dietpi-disk-space-audit.md` in `sagar-hermes-ops`.
11. **Using `rclone delete` on a directory leaves empty directories behind** — for plain backups that upload a whole directory tree (e.g. `hermes-plain-2026-06-20_19-15/`) per run, prune MUST use `rclone purge` to remove the directory itself. `rclone delete` only removes files inside, so the empty directory persists and the next retention run re-lists it forever. Visible symptom: quota keeps growing despite prune logs saying `removed: N`. The retention count is fine, the empty dirs are the problem. **Rule:** `purge` for directory targets, `delete` for single files. See `references/mega-hard-delete-retention.md`.
12. **Mega quota can stay high even when Cloud Drive + Rubbish bin look nearly empty** — if MEGA web shows a tiny visible `Hermes-backups` folder (for example ~325 MB), Device Centre is empty, and Rubbish bin is 0 B, but `rclone about Mega:` still reports tens of GB used, treat it as a MEGA-side hidden/orphaned storage or version-history issue, not a visible-folder issue. Do not keep deleting the visible backup folder expecting the quota to reconcile immediately. First verify what is actually visible in Cloud Drive and Device Centre, then compare with `rclone about Mega:`. See `references/mega-visible-size-vs-account-usage.md`.
13. **A Mega plain backup can finish "successfully" while being silently partial** — if MEGA web shows plain backup folders around 150–180 MB but `/root/.hermes` is multi-GB, the plain backup is not a real full copy. Verify with `rclone size Mega:Hermes-backups/#plain/<folder>` and compare its top-level inventory against local `/root/.hermes`. Missing top-level directories like `scripts/`, `sessions/`, `skills/`, `state-snapshots/`, `venvs/`, or a missing `state.db` prove the backup is incomplete even if the cron notification said success. See `references/mega-visible-size-vs-account-usage.md`.
14. **The 100 MB Mega speed test is a misleading benchmark for real backups** — measured 2026-06-20: 100 MB single file uploaded at ~3 MB/s, but a 1.1 GB archive uploaded at ~7 KB/s (44h ETA) and a 6 GB plain backup at ~28 KB/s (60h ETA). Mega free tier throttles single files >100 MB and large rclone sessions heavily. Calmer rclone flags (`--transfers 2 --checkers 4`, no `--fast-list`, added retries) do not fix this — the bottleneck is at the Mega account level. **Decision rule:** if the user already has local TB + GDrive, drop Mega entirely and use `Backblaze B2` (10 GB free, no throttling) for a 3rd cloud destination instead. See `references/mega-throttling-and-drop-decision.md` for the full decision matrix and the cleanup steps.

## Mega Plain Backup Integrity Verification

When a user says the Mega plain backup folders are only ~150–200 MB even though Hermes home is several GB, do not assume compression or MEGA UI rounding. A plain backup should be a directory copy, so that size is a red flag.

Verification sequence:

1. Check visible remote size:
   ```bash
   rclone size Mega:Hermes-backups/#plain/<folder> --json
   ```
2. Compare remote top-level entries to local top-level entries under `/root/.hermes`.
3. Explicitly probe for heavyweight must-exist paths:
   - `state.db`
   - `state-snapshots/`
   - `scripts/`
   - `sessions/`
   - `skills/`
   - `venvs/`
4. If those are missing, report the plain backup as **partial / not trustworthy** even if the cron job reported success.
5. Keep the message blunt: "current Mega plain backup is partial, not a true full backup."

This check matters because a retention/prune fix can coexist with an upload-integrity problem; fixing old-backup deletion does not prove the uploaded folder contents are complete.

- `references/gdrive-trash-and-retention.md` — GDrive trash accumulation causing backup timeouts and retention policies
- `references/cron-timeout-vs-wrapper-timeout.md` — scheduler timeout mismatch pattern for backup wrapper scripts
- `references/rclone-direct-copy-for-gdrive.md` — rclone copy to remote bypassing FUSE for massive GDrive backup speedup
- `references/bws-cli-secrets-for-cron.md` — Bitwarden Secrets Manager CLI pattern for cron subprocesses
- `references/staging-dir-leak.md` — `.tmp-hermes-backup` and `.restore-tests` accumulation pattern, cleanup code, and detection audit
- `references/daily-git-sync-cron-variant.md` — silent `deliver: 'local'` agent-driven cron pattern for mirroring a local git repo (Obsidian vault, configs, knowledge base) to a private GitHub repo on a daily schedule. Distinct from backup-with-notifications: uses `gh` auth, `--ff-only` merge, JSON state file for dashboard visibility, and compact "report ONLY" prompt.
- `references/mega-visible-size-vs-account-usage.md` — MEGA mismatch pattern where Cloud Drive + Rubbish bin look nearly empty but account usage stays high, plus the verification path for catching silently partial Mega plain backups.
- `references/mega-throttling-and-drop-decision.md` — measured Mega free-tier throttling at 100 MB / 1.1 GB / 6 GB scales, why the 100 MB test is misleading, when to drop Mega entirely, and the recommended replacement (Backblaze B2 10 GB free).

## rclone Direct Copy for Cloud Remotes (GDrive, Mega, etc.)

When backing up to cloud remotes via rclone, **bypass FUSE mounts entirely** and use `rclone copy` directly to the remote. FUSE mounts are extremely slow for large file counts (tens of thousands of small files).

### Implementation Pattern

```python
def run_rclone_copy(src: Path, dst_remote: str, backend: str = "generic") -> bool:
    """Copy using rclone directly to remote (bypasses FUSE mount)."""
    # dst_remote like "drseatop_google_drive_1779883937:Hermes-backups/#plain/..."
    # backend: "gdrive" | "mega" | "generic"
    cmd = [
        "rclone", "copy",
        "--exclude", ".cache/**",
        "--exclude", ".venv/**",
        "--exclude", "__pycache__/**",
        "--exclude", "*.log",
        "--exclude", "tmp/**",
        "--fast-list",
        "--transfers", "4",
        "--checkers", "8",
        str(src) + "/",
        dst_remote
    ]
    # Backend-specific flags
    if backend == "gdrive":
        cmd.insert(-2, "--drive-chunk-size")
        cmd.insert(-1, "64M")
    # Mega uses defaults; --mega-hard-delete handled at delete time
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)
    if result.returncode != 0:
        print(f"RCLONE_ERROR={result.stderr.strip()[:500]}")
        return False
    return True
```

### Key rclone Flags by Backend

| Backend | Flags | Purpose |
|---------|-------|---------|
| **GDrive** | `--drive-chunk-size 64M` | Large chunks for faster upload throughput |
| **Mega** | *(uses defaults)* | No special upload flags needed |
| **All** | `--fast-list` | Fewer API calls for large directory listings |
| **All** | `--transfers 4` | Parallel file uploads |
| **All** | `--checkers 8` | Parallel existence checks |
| **All** | `--exclude` patterns | Skip cache/venv/pycache/tmp without walking them |

### Applied Scripts

- `/root/.hermes/scripts/hermes_plain_backup.py` — rewritten to use rclone copy for GDrive destinations
- `/root/.hermes/scripts/hermes_plain_backup_mega.py` — uses rclone copy for Mega with hard-delete pruning
- `/root/.hermes/scripts/hermes_mega_archive_backup.py` — archive backup to Mega with hard-delete
- `/root/.hermes/scripts/hermes_backup_common.py` — added `copy_with_rclone()` and `prune_old_backups_rclone()` used by archive backups

### Performance Impact

- **Before (rsync to FUSE):** Plain backup timed out at 1200s
- **After (rclone copy):** ~55s for local test; GDrive/Mega test completes in minutes not hours

## Mega-Specific: Hard Delete Retention (No Trash Emptying Needed)

Mega's rclone backend **does not expose trash via `rclone lsd Mega:trash`** — the trash directory is not accessible. `rclone backend help mega` confirms no backend commands exist for trash management.

### Solution: `--mega-hard-delete`

## Prune Function Template — Plain Backups (Directory Mode)

For plain backups that upload whole directory trees (e.g. `hermes-plain-2026-06-20_19-15/` containing thousands of files), use **`rclone purge`** not `rclone delete`. `rclone delete` on a directory only removes its files; the empty directory itself remains and the next retention run re-discovers it as a "candidate" forever, so old folders pile up even though prune "succeeded."

```python
def prune_old_mega(remote_base: str, prefix: str, keep: int) -> list[str]:
    """Prune old plain-backup directories on Mega. Use purge, not delete."""
    try:
        result = subprocess.run(
            ["rclone", "lsf", remote_base, "--dirs-only", "-R"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            return []
        dirs = [
            line.strip().rstrip("/")
            for line in result.stdout.strip().splitlines()
            if line.strip().startswith(prefix)
        ]
        dirs.sort(reverse=True)
        removed = []
        for old in dirs[keep:]:
            old_path = f"{remote_base}/{old}"
            try:
                # purge removes the directory AND all its contents.
                # --mega-hard-delete bypasses trash so quota frees immediately.
                subprocess.run(
                    ["rclone", "purge", old_path, "--mega-hard-delete", "--fast-list"],
                    check=True, timeout=600,
                )
                removed.append(f"{old} (purged)")
            except Exception as e:
                print(f"RCLONE_PRUNE_ERROR={old}:{e}")
        return removed
    except Exception:
        return []
```

## Prune Function Template — Archive Files (Single-File Mode)

For archive backups that upload one file per run (`hermes-mega-archive-backup-*.tar.gz.gpg`), `rclone delete` is fine because the target is a single file, not a directory.

```python
def prune_old_mega(remote_base: str, prefix: str, suffix: str, keep: int) -> list[str]:
    """Prune old archive files on Mega. delete is fine for single files."""
    try:
        result = subprocess.run(
            ["rclone", "lsf", remote_base, "--files-only", "-R"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            return []
        files = [
            line.strip() for line in result.stdout.strip().splitlines()
            if line.strip().startswith(prefix) and line.strip().endswith(suffix)
        ]
        files.sort(reverse=True)
        removed = []
        for old in files[keep:]:
            try:
                subprocess.run(
                    ["rclone", "delete", f"{remote_base}/{old}", "--mega-hard-delete"],
                    check=True, timeout=300,
                )
                removed.append(old)
            except Exception:
                pass
        return removed
    except Exception:
        return []
```

**Key rule:** `purge` for directories, `delete` for single files. Mixing them silently breaks retention.

### Key Points

| Aspect | GDrive | Mega |
|--------|--------|------|
| Trash accessible via rclone | Yes (`--drive-trashed-only`) | No (directory not found) |
| Trash emptying | `rclone delete --drive-trashed-only` | N/A |
| Retention delete | `rclone delete` (moves to trash) | `rclone delete --mega-hard-delete` |
| Manual cleanup needed | Yes (periodic trash empty) | **No** — hard delete purges permanently |

### Applied Scripts

- `/root/.hermes/scripts/hermes_plain_backup_mega.py` — plain backup with hard-delete pruning
- `/root/.hermes/scripts/hermes_mega_archive_backup.py` — archive backup with hard-delete pruning
- Wrapper scripts: `mega_plain_daily_notify.py`, `mega_archive_daily_notify.py`

### Cron Jobs Added

| Job | Schedule | Keep | Script |
|-----|----------|------|--------|
| `daily-hermes-mega-plain` | 19:15 Asia/Dhaka | 2 | `mega_plain_daily_notify.py` |
| `daily-hermes-mega-archive` | 19:45 Asia/Dhaka | 2 | `mega_archive_daily_notify.py` |

Both use `no_agent: true` cron with Discord delivery to channel `1509927046258757792`.

## Cloud Archive Size Discipline (Critical for Bounded Quotas)

A local TB archive and a cloud archive **must use different exclude lists**. Local TB can hold a full 5 GB tar; a 50 GiB Mega account cannot afford two 3.5 GB archives plus plain backups.

The existing `hermes_daily_full_backup.py` passes `EXCLUDE_PREFIXES = []` — fine for TB, fatal for cloud. When adapting an existing backup script for a new cloud destination, audit the resulting tar size **before** pointing it at quota.

### Minimum Excludes for Cloud Archives (Mega/anything <100 GiB free)

```python
EXCLUDE_PREFIXES = [
    "venvs", ".venvs",          # python virtualenvs (rebuildable)
    "node_modules",              # npm/pnpm trees (rebuildable)
    "mnemosyne",                 # vector DBs (rebuildable from source)
    "sessions",                  # large conversation logs
    "state-snapshots",           # historical state (regenerable)
    "cache", ".cache",           # temp/cached data
    "bin",                       # downloaded CLIs (re-installable)
]
```

### Estimated Size Impact (5.1 GB hermes home)

| Excluded | Size saved |
|----------|-----------|
| `venvs` + `.venvs` | ~340 MB |
| `node_modules` (under `scripts/mcp-servers/`, `lsp/`) | ~hundreds of MB |
| `mnemosyne` | ~660 MB |
| `sessions` | ~520 MB |
| `state-snapshots` | ~1.2 GB |
| `cache` | ~66 MB |
| `bin` | ~80 MB |

**Before excludes:** 3.5 GB archive × 2 kept = 7 GB consumed.
**After excludes:** ~500 MB archive × 2 kept = 1 GB consumed. ~6 GB reclaimed.

### Detection Signal

If you see a backup failure like:

```
RCLONE_COPY_ERROR=Command 'rclone copy ...' timed out after 3600 seconds
```

on a brand-new cloud destination, the archive is too big for the upload window, not a connectivity issue. Run the archive build to a local temp file and `du -sh` it before pointing at cloud.

## Mega Throughput Baseline — Be Skeptical of the 100 MB Test

Measured 2026-06-20 on a fresh Mega free-tier account:

| Workload | Size | Files | Speed | ETA |
|----------|------|-------|-------|-----|
| 100 MiB single file | 100 MB | 1 | **~3.1 MB/s** | 33s |
| 1.1 GB single file (archive) | 1.1 GB | 1 | **~7 KB/s** | 44 hours |
| Plain backup (multi-GB, 10K+ small files) | ~6 GB | 10,000+ | **~28 KB/s** | 60 hours |

**The 100 MB test is a misleading benchmark.** Real backups (>1 GB or many small files) are throttled 100-400x harder than a single 100 MB test file suggests. Before investing in a Mega backup pipeline, do a 1+ GB upload test — the 100 MB test alone will give a false sense of capability.

`--mega-hard-delete`, hard-delete retention, and the prune code all work correctly. The bottleneck is the upload session itself, not the rclone config. Calmer flags (`--transfers 2 --checkers 4`, no `--fast-list`, added retries) did **not** meaningfully improve the 1.1 GB upload speed.

**Operational consequence:** for a multi-GB backup, even 21600s (6 h) `cron.script_timeout_seconds` is not enough on Mega free tier. The realistic outcome is:
- 5 GB plain backup: takes 50-60 hours (10x the cron window)
- 1.1 GB archive (with hard excludes): takes 40+ hours
- 500 MB archive (very tight excludes): might fit in a cron window

If the user's 2nd cloud destination is already GDrive and they have local TB, **drop Mega entirely** rather than trying to engineer around throttling. See `references/mega-throttling-and-drop-decision.md` for the full decision matrix and cleanup steps.

## Verification Checklist

- [ ] Backup common code skips transient missing files instead of crashing
- [ ] Daily wrapper prints clean success output
- [ ] Weekly wrapper prints clean success output
- [ ] Failure formatting is compact and readable
- [ ] Partial-success formatting appears when skipped-file warnings exist
- [ ] Daily cron uses wrapper script with `no_agent=true`
- [ ] Weekly cron uses wrapper script with `no_agent=true`
- [ ] Delivery target is still the intended Discord/Telegram channel
