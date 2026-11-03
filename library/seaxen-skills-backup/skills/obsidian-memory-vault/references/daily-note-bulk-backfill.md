# Daily Note Bulk Backfill — Safe Pattern

How to backfill N days of missing `Daily/YYYY-MM-DD.md` notes from
`session_search` and `sessions.json` evidence without breaking vault health.

## When to use

- User discovers the vault has a multi-day gap (e.g. last daily note is
  2026-06-04, today is 2026-06-17) and asks to backfill.
- The cron nightly log was running but producing nothing (strict "no write"
  bias) for several days.
- The vault has 13+ days of session activity in `sessions.json` and
  `session_search` that the user wants captured as honest daily stubs.

## Required inputs

- `sessions.json` at `~/.hermes/sessions/sessions.json` (group sessions by
  Dhaka day, filter to Sagar's user_name, dedupe by display name, sort by
  time).
- `session_search` for cluster queries (e.g. "codex pool", "hermes
  dashboard port", "obsidian nightly cron", "liq risk") to identify
  durable decisions and fixes per day.
- The vault path (`/mnt/tb/hermes/obsedianvault`).

## The 4-step safe pattern

### Step 1: Collect session activity per day

```python
import json, subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

sessions = json.loads(Path("/root/.hermes/sessions/sessions.json").read_text())
dha = timezone(timedelta(hours=6))
by_day = {}
for meta in sessions.values():
    if not isinstance(meta, dict):
        continue
    ts = meta.get("updated_at")
    if not ts: continue
    dt = datetime.fromisoformat(ts)
    if dt.tzinfo is None: dt = dt.replace(tzinfo=timezone.utc)
    if not (since <= dt < until): continue
    origin = meta.get("origin") or {}
    if origin.get("user_name") not in {"Sagar", "Dr. Sagar", None}: continue
    by_day.setdefault(dt.astimezone(dha).strftime("%Y-%m-%d"), []).append({
        "time": dt.astimezone(dha).strftime("%H:%M"),
        "display": (meta.get("display_name") or "").strip(),
        "platform": meta.get("platform"),
    })
```

For each day, dedupe by `display.lower()` and keep the earliest time per
unique session title.

### Step 2: Identify durable items via session_search

For each cluster topic (Hermes ops, Codex pool, dashboard, MCP, medical
study, etc.), run a focused `session_search` query. Only attribute a
decision or fix to a specific day if you can point to a session that
happened on or before that day AND the action took effect that day.

Be conservative:
- If a decision was made on day A but you only learned about it on day B,
  attribute to day A (when the action happened), not day B.
- If you cannot pin a fix to a specific day, leave it out of the daily
  note and put it in the aggregate `issues-fixes-log.md` only.
- Do not infer decisions from session titles alone — titles like
  "#cardiology" don't tell you what was decided.

### Step 3: Write daily notes with the "Imported —" prefix

For each day in the gap, write `Daily/YYYY-MM-DD.md` using the standard
format (Focus, Log, Decisions, Fixes, Next). Prefix every durable bullet
that came from a backfill with `Imported — ` so the user can tell
historical imports from fresh writes.

```markdown
# 2026-06-13

#daily

## Focus
- Codex credential pool expansion, session DB cleanup, and cron delivery reliability.

## Log
- 17:13 — Activity in #cron.

## Decisions
- Imported — Added new openai-codex credential via `hermes auth add openai-codex --label <unique> --no-browser` (not `hermes login`, which overwrites the default slot). Pool now has 3 entries: `pottege`, `inheler`, `openai-codex-oauth-4`. Round-robin confirmed in config.

## Fixes
- Imported — Cron delivery reliability fix in `/usr/local/lib/hermes-agent/cron/scheduler.py`: added 3-attempt retry with exponential backoff (1s, 2s, 3s), retryable error detection for transient issues (DNS, connection reset, 429/502/503/504), and Telegram fallback when Discord fails. Also added missing `import time`.
```

Empty sections (Decisions/Fixes/Next) should still be present with no
bullet — keeps the format consistent and makes it easy to add to later.

### Step 4: Update aggregate notes and add Daily Note Index

After all daily notes are written:

1. Append a `## YYYY-MM-DD backlog` section to `Memory/decisions.md` with
   the durable decisions that don't fit any single day's note.
2. Append a `## YYYY-MM-DD backlog` section to
   `System/Assistant/issues-fixes-log.md` with the durable fixes.
3. **Critical:** add a "Daily Note Index" section to `AGENT.md` listing
   every daily note as a `[[YYYY-MM-DD]]` wikilink:

```markdown
## Daily Note Index
Backfilled from session_search on YYYY-MM-DD. All daily notes should be
reachable from this index to avoid orphan flags.

- [[2026-05-05]]
- [[2026-05-10]]
...
- [[2026-MM-DD]]
```

Without this index, every new daily note shows up as an orphan in
`/api/memory-health` and the score drops by ~1 point per orphan. The
index brings the count back to 0.

## Verification

After the backfill pass, run these checks and report the deltas:

```bash
# List all daily notes
ls /mnt/tb/hermes/obsedianvault/Daily/ | sort

# Check that the new daily notes contain "Imported —" prefixes
grep -c "Imported —" /mnt/tb/hermes/obsedianvault/Daily/2026-06-13.md

# Re-check memory health — orphans should be 0, score should recover
curl -s http://127.0.0.1:6065/api/memory-health | python3 -m json.tool

# Test that recall finds the new daily notes
curl -s "http://127.0.0.1:6065/api/recall?query=codex+pool+round+robin&limit=3"
```

Expected results after a clean backfill:

- `notes` count up by N (the N new daily notes)
- `links` count up by N+ (the index adds N links, the daily notes add M cross-links)
- `orphans` count = 0 (the index eliminates them)
- `overall_score` recovers to near the pre-backfill baseline (or slightly better)
- `recall` hit rate stable or improved (more notes = more chances to match, but also more candidates)

## What NOT to do

- **Do not skip the index.** A backfill without the index looks broken
  in `/api/memory-health` even though the content is correct.
- **Do not write 50+ notes in one go without re-checking health.** The
  orphan count can mask real link problems. After ~10 notes, re-run
  health and fix any unexpected orphan notes that aren't on your list.
- **Do not fabricate sessions to fill quiet days.** A day with 0
  sessions should get a stub with `Log: no notable vault or session
  activity`, not invented activity.
- **Do not backfill aggregate notes with bulk imports without
  grouping.** Put a `## YYYY-MM-DD backlog` heading per backfill batch
  so future readers can see what came from when.
- **Do not overwrite existing daily notes.** If `Daily/2026-06-04.md`
  already exists, leave it alone and skip that day. Append-only.

## Why "Imported —" prefix matters

Future readers (and future you) need to distinguish:

- Fresh nightly captures: ordinary bullets
- Backfilled from session_search: `Imported — ...`
- Backfilled from another vault or import: `Imported from X — ...`

The prefix is cheap to add, easy to grep, and lets you bulk-delete
backfilled content if you ever decide a backfill was wrong without
losing the fresh captures.
