#!/usr/bin/env python3
"""Backfill has_failures + permanently_missing markers from a download log.

Parses a download log file and updates accounts/<name>.json so that
--fix-failures mode (and the main download loop) can find the videos
that need attention. Two kinds of issues are detected:

  - per-segment failures (1 of 3700+ in a single video) → has_failures=True
  - whole-video HTTP 404 (deleted from LMS)            → permanently_missing_videos

Why this exists: a long bulk download started BEFORE the new has_failures /
404-handling patch is loaded in Python memory will print ⚠ warnings and
✗ 404 lines in the log, but won't mark state. Without backfill, --fix-failures
sees nothing to fix and exits silently. This script bridges the gap.

Usage:
    python3 backfill_failures.py <logfile> <account>

The script is idempotent — running it twice with the same input produces the
same state.
"""
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path


def backfill(log_path: str, account: str) -> int:
    log = Path(log_path).read_text(errors="replace").splitlines()

    # Walk through log, track the most recent "↓ [N] Title" (start of video)
    # and the most recent "✓ filename (size MB)" (end of video).
    # If between them there's a "⚠ N/M segments failed" line, that video had failures.
    # If the line is "✗ Title: HTTP 404" instead, the video is permanently missing.
    current_title = None
    current_filename = None
    had_failures = False
    failed_count = None
    is_404 = False

    failed_videos = {}      # filename -> (title, failure_count)
    missing_404 = set()     # titles with 404s
    FAIL_RE = re.compile(r"⚠\s+(\d+)/(\d+)\s+segments failed")
    DOWN_RE = re.compile(r"✓\s+(\S+)\s+\((\d+(?:\.\d+)?)\s*MB\)")
    START_RE = re.compile(r"↓\s+\[\d+\]\s+(.+?)\.\.\.")
    # The error line for 404: "✗ Title: HTTP Error 404: Not Found" OR
    # the new-code path: "✗ Title: HTTP 404 (permanently missing from LMS)".
    # Match anything starting with HTTP 404 / 410 to be tolerant of wording changes.
    ERR_RE = re.compile(r"✗\s+(.+?):\s+HTTP\s+(404|410)", re.IGNORECASE)

    for line in log:
        m_start = START_RE.search(line)
        if m_start:
            current_title = m_start.group(1)
            had_failures = False
            failed_count = None
            is_404 = False
            continue
        m_fail = FAIL_RE.search(line)
        if m_fail:
            had_failures = True
            failed_count = int(m_fail.group(1))
            continue
        m_err = ERR_RE.search(line)
        # rstrip periods to absorb cosmetic title-end dots that differ between
        # the "↓" line and the "✗" line (e.g. "Session...." vs "Session.")
        if m_err and m_err.group(1).strip().rstrip(".") == current_title.rstrip("."):
            is_404 = True
            missing_404.add(current_title)
            current_title = None
            current_filename = None
            continue
        m_down = DOWN_RE.search(line)
        if m_down:
            current_filename = m_down.group(1)
            if had_failures and current_filename:
                failed_videos[current_filename] = (current_title, failed_count)
            had_failures = False
            failed_count = None
            current_title = None

    if not failed_videos and not missing_404:
        print(f"No failed videos found in {log_path}")
        return 0

    if failed_videos:
        print(f"Found {len(failed_videos)} videos with segment failures:")
        for fn, (title, n) in sorted(failed_videos.items()):
            print(f"  - {fn}  ({n} failed segments)  // {title}")

    if missing_404:
        print(f"Found {len(missing_404)} videos permanently missing (HTTP 404):")
        for t in sorted(missing_404):
            print(f"  - {t}")

    state_file = Path(f"/root/synapse_dl/accounts/{account}.json")
    if not state_file.exists():
        print(f"State file not found: {state_file}", file=sys.stderr)
        return 1
    state = json.loads(state_file.read_text())
    videos = state.get("downloaded_videos", {})

    marked = 0
    for fn, (title, n) in failed_videos.items():
        # Find the state entry with this filename
        for sid, info in list(videos.items()):
            if info.get("filename") == fn:
                info["has_failures"] = True
                info["failure_count"] = n
                marked += 1
                break

    state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False))
    print(f"\nMarked {marked}/{len(failed_videos)} state entries with has_failures=True")

    # Also log 404s as permanently missing. The log doesn't carry stream_ids,
    # so we use a hash of the title as a synthetic key. Next run that hits
    # the same title (with its real stream_id) will properly overwrite this
    # entry. The point is to leave a *record* of what was 404, not to
    # actually prevent re-trying — the main download loop will still see
    # the video and try the playlist fetch, which is fast and gives a
    # definitive 404.
    if missing_404:
        permanent = state.setdefault("permanently_missing_videos", {})
        for t in sorted(missing_404):
            fake_sid = "title:" + hashlib.sha1(t.encode()).hexdigest()[:32]
            if fake_sid not in permanent:
                permanent[fake_sid] = {
                    "title": t,
                    "http_code": 404,
                    "failed_at": datetime.now().isoformat(),
                    "note": "synthetic key from log backfill; will be superseded by real stream_id on next run",
                }
        state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False))
        print(f"Logged {len(missing_404)} 404s in permanently_missing_videos (synthetic keys)")

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: backfill_failures.py <logfile> <account>", file=sys.stderr)
        sys.exit(2)
    sys.exit(backfill(sys.argv[1], sys.argv[2]))
