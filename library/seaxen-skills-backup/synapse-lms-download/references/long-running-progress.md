# Long-running download progress — bash + cron recipe

A Synapse full-course sync runs for 2–8 hours. The user wants visibility without sitting in the chat. This is the pattern that works.

## Why bash + no_agent cron (not an LLM-prompted cron)

- **No LLM tokens burned** — the script is pure bash, output is delivered verbatim
- **Deterministic** — the user sees the same format every 15 min, no AI rewriting the same data 8 times
- **Auto-stops noise** — when the download process exits, the script detects via PID file and emits a single "exited" line, then stays silent
- **Discord-friendly** — short status block, fits in a chat message

## The script (place at `~/.hermes/scripts/synapse_progress.sh`)

```bash
#!/bin/bash
# Synapse download progress reporter — every 15 min
# Outputs a status summary; silent if download process is gone

STATE=/root/synapse_dl/accounts/sharif.json
LOG=/root/synapse_dl/sharif_download.log
DEST="/mnt/tb/Syn MD 26"
PIDFILE=/tmp/synapse_dl.pid

# Bail if the download process is no longer running
if [ -f "$PIDFILE" ] && ! kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    echo "⛔ Synapse download process is no longer running (pid $(cat "$PIDFILE") exited)."
    exit 0
fi

# Latest "✓ ... .mp4" line in log
LATEST=$(grep -E "✓ Lecture" "$LOG" 2>/dev/null | tail -1 | sed 's/^[[:space:]]*//')

# Counts from state file
if [ -f "$STATE" ]; then
    VIDS=$(python3 -c "import json; d=json.load(open('$STATE')); print(len(d.get('downloaded_videos',{})))" 2>/dev/null || echo "?")
    NOTES=$(python3 -c "import json; d=json.load(open('$STATE')); print(len(d.get('downloaded_notes',{})))" 2>/dev/null || echo "?")
else
    VIDS="0"; NOTES="0"
fi

# Disk usage
SIZE=$(du -sh "$DEST" 2>/dev/null | cut -f1)
MP4_COUNT=$(find "$DEST" -name "*.mp4" -not -name "*.remux.mp4" 2>/dev/null | wc -l)

# Current download (last "↓ [N] Title" line, with current progress %)
CUR=$(grep -E "^[[:space:]]+↓ \[" "$LOG" 2>/dev/null | tail -1 | sed 's/^[[:space:]]*//')
PROG=$(grep -E "segments \(.*%\)$" "$LOG" 2>/dev/null | tail -1 | sed 's/^[[:space:]]*//')

# Time
NOW=$(date '+%H:%M')

# Uptime of download process
if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    PID=$(cat "$PIDFILE")
    UP=$(ps -o etime= -p "$PID" 2>/dev/null | tr -d ' ' || echo "?")
else
    UP="?"
fi

cat <<EOF
📥 Synapse download progress — ${NOW} (uptime ${UP})

✅ Videos done: ${VIDS}  📝 Notes: ${NOTES}
💾 Disk used: ${SIZE} (${MP4_COUNT} .mp4 files on disk)

🔄 Now downloading:
${CUR}
${PROG}

${LATEST:+📌 Latest finished: ${LATEST}}
EOF
```

chmod +x and test once:
```bash
chmod +x ~/.hermes/scripts/synapse_progress.sh
pgrep -f 'download_nested.py sharif' | head -1 > /tmp/synapse_dl.pid
~/.hermes/scripts/synapse_progress.sh    # should print a status block
```

## Cron job (auto-deliver to Discord every 15 min)

```bash
# Relative path required (must live under ~/.hermes/scripts/)
cronjob action=create name="Synapse download progress" \
  no_agent=true script=synapse_progress.sh \
  schedule="every 15m" deliver=origin
```

**Result:** every 15 min, the script runs, prints the status block, and the gateway delivers it to the Discord channel that originally requested the download. No agent loop, no token usage, no "thinking" between ticks.

## When the download finishes

The script bails silently on every tick after the process exits. To remove the cron job once everything's done:

```bash
cronjob action=remove job_id=333f7234f646   # id from `cronjob action=list`
```

## Why the PID file pattern is bulletproof

- The download is started as a background `terminal(background=true, ...)` — Hermes tracks the pid
- We capture it once at the start with `pgrep -f 'download_nested.py sharif' | head -1 > /tmp/synapse_dl.pid`
- The script checks `kill -0 $pid` on every tick — non-zero return = process gone
- This means the script auto-quiets even if the user kills the process via Hermes `process.kill` or `kill <pid>` from a shell

## Variations

- **Different account name** — change the first 3 vars (`STATE`, `LOG`, `DEST`) to point at the right account
- **Different cadence** — schedule is `every 15m`, `every 30m`, `0 */2 * * *` (every 2h on the hour), etc.
- **Multiple accounts** — make 2 scripts + 2 cron jobs, one per account
- **Custom user-facing label** — change the `📥 Synapse download progress` header to whatever the project is called
