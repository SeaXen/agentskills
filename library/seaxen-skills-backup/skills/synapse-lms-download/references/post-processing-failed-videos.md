# Post-processing failed videos — re-download pattern

A long bulk download (2-8 hours) will produce a handful of videos with 1-2 failed CDN segments each. Those files are *technically* playable but have a 5-10s audio/video gap that can desync subtitles or feel jarring. The user will say "those failed ones, re-download one more time and delete old" — so we need a clean post-process.

This is the pattern that handles it: **track failures in state, then run a one-shot re-download pass at the end.**

## The two failure scopes (different handling)

| Scope | Cause | Handling |
|---|---|---|
| Per-segment failure (1 of 3700+) | CDN blip / network timeout | Retry-able. Track in state with `has_failures=true`, re-download once at end. |
| Whole-video HTTP 404 | Video removed from LMS | Not retry-able. Mark in `permanently_missing_videos` and skip forever. |

The trick: **one state field per video** (`has_failures: true/false`) is the single source of truth. The download loop sets it on completion; the post-process loop reads it.

## State schema additions

Add two fields to the `downloaded_videos` entry and one new top-level key:

```json
{
  "downloaded_videos": {
    "<stream_id>": {
      "...": "...existing fields...",
      "has_failures": true,
      "failure_count": 1
    }
  },
  "permanently_missing_videos": {
    "<stream_id>": {
      "title": "Back up Lecture No:04 Neurophysiology",
      "http_code": 404,
      "failed_at": "2026-06-19T02:18:00+06:00"
    }
  }
}
```

## The download loop (download_nested.py) — what's added

```python
# In download_and_decrypt: return failure count, log persistently
def download_and_decrypt(segments, stream_id, key, out_path, ...):
    encrypted, failed = {}, []
    # ... existing download with 3x retry per segment ...
    
    if failed:
        # Persistent log for backfill / debugging
        with open("/root/synapse_dl/failed_segments.log", "a") as f:
            f.write(f"[{datetime.now().isoformat()}] stream_id={stream_id} "
                    f"out={out_path} failures={len(failed)}/{len(segments)}\n")
    
    # ... decrypt and write .ts.tmp ...
    return written, len(failed)


# In the main video loop, before re-downloading:
for v in videos:
    if is_video_downloaded(state, v["stream_id"]):
        continue
    # NEW: skip videos marked as permanently missing
    if state.get("permanently_missing_videos", {}).get(v["stream_id"]):
        print(f"⏭  {v['title']}: permanently missing (skipping)", file=sys.stderr)
        continue
    
    # NEW: resume from disk if final .mp4 already exists (crashed run recovery)
    final_path = chapter_dir / f"{sanitize(v['title'])}.mp4"
    if final_path.exists() and final_path.stat().st_size > 1024 * 1024:
        record_video(state, ..., has_failures=False, failure_count=0)
        save_state(account, state)
        print(f"✓ {final_path.name} (resumed)", file=sys.stderr)
        continue
    
    # ... download with try/except, mark state ...
    try:
        segments = fetch_segments(v["stream_id"])
        _, fail_count = download_and_decrypt(segments, v["stream_id"], v["key"], tmp_path, ...)
        # ... remux + rename ...
        record_video(state, ..., has_failures=fail_count > 0, failure_count=fail_count)
    except urllib.error.HTTPError as e:
        # NEW: 404 on whole video → permanent skip
        state.setdefault("permanently_missing_videos", {})[v["stream_id"]] = {
            "title": v["title"], "http_code": e.code, "failed_at": now()
        }
        save_state(account, state)
    except Exception as e:
        # ... existing transient error handling ...
```

## The --fix-failures mode (added to download_nested.py)

A one-shot mode that:
1. Reads state for all `has_failures=true` entries
2. Deletes the .mp4 + any orphan `.ts.tmp` / `.remux.mp4` siblings
3. Removes the entry from `downloaded_videos`
4. Falls through to the normal download loop, which re-downloads them

```python
if fix_failures:
    to_fix = [(sid, info) for sid, info in state.get("downloaded_videos", {}).items()
              if info.get("has_failures")]
    if not to_fix:
        print("✓ No failed videos to fix.")
        return
    print(f"=== Fix-failures pass: {len(to_fix)} videos to re-download ===")
    for sid, info in to_fix:
        old_path = out_root / info["subpath"] / info["filename"]
        print(f"  ✗ Deleting {old_path.name} ({old_path.stat().st_size/1024/1024:.1f} MB)")
        old_path.unlink(missing_ok=True)
        for suffix in [".ts.tmp", ".remux.mp4"]:
            (out_root / info["subpath"] / f".{info['filename']}{suffix}").unlink(missing_ok=True)
        del state["downloaded_videos"][sid]
    save_state(account, state)
    # Fall through to the main download loop
```

The re-download runs with the **new** per-segment retry logic (3x with 30s timeout), so most failures clear up on the second pass.

## Backfill from log (for runs started before the feature shipped)

If the bulk download is **already running with the old code** (no `has_failures` marker being written to state), you still have the failure data in the log file. A separate script parses it:

```python
# backfill_failures.py — walk the log, find ⚠ lines and the ✓ line right after them
FAIL_RE = re.compile(r"⚠\s+(\d+)/(\d+)\s+segments failed")
DOWN_RE = re.compile(r"✓\s+(\S+)\s+\((\d+(?:\.\d+)?)\s*MB\)")
START_RE = re.compile(r"↓\s+\[\d+\]\s+(.+?)\.\.\.")

# Walk line by line. Track current_title from "↓ [N] Title..." lines.
# When "⚠ N/M segments failed" appears, set had_failures=True.
# When "✓ filename" appears next, if had_failures, mark this filename as failed.
# Then update state: for each (filename, n) pair, find the state entry with
# matching filename and set has_failures=True, failure_count=n.
```

Why this matters: a 6-hour bulk run started before the patch ships doesn't get the new state-marking logic. Without the backfill, --fix-failures sees nothing to fix and exits silently.

## End-to-end post_process.sh

```bash
#!/bin/bash
set -e
cd /root/synapse_dl

ACCOUNT="${1:-sharif}"
LOG="/root/synapse_dl/${ACCOUNT}_download.log"

echo "===== Post-processing for $ACCOUNT ====="

# Step 1: catch any failures the in-memory old code missed
/root/.venvs/synapse-env/bin/python3 /root/synapse_dl/backfill_failures.py "$LOG" "$ACCOUNT"
echo

# Step 2: re-download the failed ones (with retries)
/root/.venvs/synapse-env/bin/python3 /root/synapse_dl/download_nested.py "$ACCOUNT" --fix-failures 2>&1
echo

echo "===== Done ====="
echo "Final state:"
python3 -c "
import json
d = json.load(open('/root/synapse_dl/accounts/${ACCOUNT}.json'))
v = d.get('downloaded_videos', {})
n_total = len(v)
n_failed = sum(1 for x in v.values() if x.get('has_failures'))
print(f'  Videos: {n_total} total, {n_failed} still marked as has_failures')
print(f'  Notes: {len(d.get(\"downloaded_notes\", {}))}')
print(f'  Permanently missing: {len(d.get(\"permanently_missing_videos\", {}))}')
"
```

## Watchdog cron — auto-trigger after main download exits

The main download can finish at any hour. A 5-min cron job polls the PID file and runs post-process the moment the main process is gone:

```bash
#!/bin/bash
# /root/.hermes/scripts/synapse_post_process.sh

ACCOUNT="${1:-sharif}"
PIDFILE=/tmp/synapse_dl.pid
STATE=/root/synapse_dl/accounts/${ACCOUNT}.json
MARKER=/root/synapse_dl/.post_process_done

# Bail if main download still running
if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    exit 0
fi

# Already done this run?
if [ -f "$MARKER" ]; then
    exit 0
fi

# Any failed videos left?
if ! python3 -c "
import json
d=json.load(open('$STATE'))
print(sum(1 for x in d.get('downloaded_videos',{}).values() if x.get('has_failures')))
" | grep -q '^0$'; then
    echo "🔧 Main download finished. Running post-process to re-download failed videos..."
    bash /root/synapse_dl/post_process.sh "$ACCOUNT" 2>&1
    touch "$MARKER"
    echo "✅ Post-process complete. Watchdog will not run again."
fi
```

Register:
```bash
cronjob action=create name="Synapse post-process watchdog" \
  no_agent=true script=synapse_post_process.sh \
  schedule="every 5m" deliver=origin
```

The `.post_process_done` marker file prevents infinite retries if --fix-failures still leaves failures (e.g., the network is genuinely broken). Manual intervention is required to clear the marker and re-run.

## Operational flow (the full sequence)

1. `download_nested.py <account>` — start bulk download (background)
2. `cron "every 15m"` — `synapse_progress.sh` reports status
3. (during run) `has_failures` markers get written to state automatically
4. Bulk download finishes → exits
5. `cron "every 5m"` — `synapse_post_process.sh` detects exit, runs `post_process.sh`
6. `post_process.sh` backfills from log (catches anything old code missed), then runs `--fix-failures`
7. `--fix-failures` deletes failed mp4s and re-downloads with 3x retry
8. Watchdog marker set; subsequent cron ticks are silent
9. `cronjob action=remove` both cron jobs once user confirms everything is clean

## Pitfalls

- **The watchdog marker (`/root/synapse_dl/.post_process_done`) is a guard, not a guarantee.** If --fix-failures still leaves failures (e.g., 2-of-51 still failing after a second pass), the marker is set and the user must manually re-run `post_process.sh` after deleting the marker. Don't try to make the watchdog infinitely retry — silent infinite loops are worse than manual intervention.
- **Filename parsing in `backfill_failures.py` is regex-fragile.** The `✓ filename (size MB)` line format is stable, but if you ever change the success log format, the backfill silently misses failures. Add a unit test that the regex matches a real `✓` line from your log.
- **Resume-from-disk only fires when the file is >1MB.** Below that threshold the script will re-download. 1MB is a safe lower bound for "definitely a real video, not a partial .ts.tmp".
- **`del state["downloaded_videos"][sid]` then `save_state` then fall through to main loop = clean re-download.** Don't do it in the opposite order (save with bad state, then delete from disk) — a crash in between leaves an inconsistent state.
