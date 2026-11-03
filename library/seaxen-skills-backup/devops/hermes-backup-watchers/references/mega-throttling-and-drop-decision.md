# Mega free-tier throttling and the drop-Mega decision

Use this when a Mega backup is too slow despite the 100 MB speed test showing 3 MB/s, or when deciding whether to keep Mega as a backup destination at all.

## The throttling reality (measured 2026-06-20)

| Workload | Size | Files | Speed | ETA |
|----------|------|-------|-------|-----|
| 100 MiB test | 100 MB | 1 | **3.1 MB/s** | 33s |
| 1.1 GB archive | 1.1 GB | 1 | **~7 KB/s** | 44 hours |
| Plain backup | 6 GB | 10,000+ | **~28 KB/s** | 60 hours |

A 1.1 GB single file uploads ~400× slower than a 100 MB file on the same Mega free-tier account. Plain backup of many small files is also heavily throttled.

The 100 MB speed test gives a **false sense of capability**. Real backups are far slower.

## Why the throttling happens

Mega free tier applies heavy transfer limits once the workload exceeds ~100 MB per request, especially for:
- single files > 100 MB
- many small files in a single rclone session
- uploads in `--transfers=4 --checkers=8` mode

`--mega-hard-delete` and the hard-delete retention work fine — that is a separate code path. The bottleneck is the upload itself.

## Rclone flags that did NOT help

Tried in the audit; none moved the needle on the 1.1 GB upload:
- `--transfers 2 --checkers 4` (calmer)
- `--retries 5 --low-level-retries 10`
- `--timeout 15m --contimeout 60s`
- removed `--fast-list` (avoided memory issues but no speed gain)
- single file (no per-file overhead)

The throttling is at the Mega account level, not the rclone config level.

## Detection: how to know a backup is stuck in Mega throttling

If a backup takes more than ~20 minutes for a file that is **not** several GB, suspect throttling.

Live check during a run:
```bash
# wchar grows slowly, rchar much higher = Mega is the bottleneck
cat /proc/<rclone_pid>/io
```

`wchar` is bytes sent to Mega (TLS layer). If wchar grows < 50 KB/s for a > 1 GB file, Mega is throttling the session.

## Decision rule: when to drop Mega entirely

Drop Mega as a backup destination when:
- The 100 MB test works (3 MB/s) BUT a real-sized backup (≥ 1 GB) uploads at < 100 KB/s
- The upload window would exceed `cron.script_timeout_seconds` even at 21600 (6 h)
- The user already has a reliable 2nd destination (local TB + GDrive)

In that situation, Mega adds complexity (auth, retention, hard-delete, throttling workarounds) without adding real safety — the stale partial backup is not a useful disaster-recovery target.

## What to use instead of Mega for a 3rd free cloud

| Provider | Free quota | Speed | Notes |
|----------|-----------|-------|-------|
| **Backblaze B2** | **10 GB** | **fast, no throttling** | S3-compatible, rclone works directly. Best free option for cloud backup. |
| Google Drive | 15 GB | decent | Already used in this setup |
| Dropbox | 2 GB | OK | Too small for backups |
| OneDrive | 5 GB | OK | Microsoft account friction |

For a 3rd free cloud destination after dropping Mega, **Backblaze B2 is the recommended replacement** (10 GB free, no throttling, S3-compatible, rclone `b2:` backend works out of the box).

## Cleanup actions when dropping Mega

1. Remove the cron job(s): `cronjob(action='remove', job_id='...')`
2. Remove the `[Mega]` section from `~/.config/rclone/rclone.conf`
3. Delete the Mega backup scripts from `~/.hermes/scripts/`
4. Delete the per-job log dir under `~/.hermes/cron/output/<job>/`
5. Optional: revert `cron.script_timeout_seconds` if it was raised only for Mega

## Practical lesson

The 100 MB speed test is not a representative benchmark for any real backup. A 100 MB test pass + 1 GB upload fail is the canonical Mega free-tier pattern. Before investing in Mega scripts and cron jobs, **do a 1 GB upload test** (or larger) to confirm the throttling profile fits the backup size.
