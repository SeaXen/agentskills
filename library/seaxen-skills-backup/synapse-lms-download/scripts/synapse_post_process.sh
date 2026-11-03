#!/bin/bash
# Post-process watchdog — runs every 5 min via cron.
# When the main download process is gone AND there are videos marked
# has_failures, run the post-process script and create a marker file
# so this watchdog only fires once per download.

ACCOUNT="${1:-sharif}"
PIDFILE=/tmp/synapse_dl.pid
STATE=/root/synapse_dl/accounts/${ACCOUNT}.json
MARKER=/root/synapse_dl/.post_process_done

# Bail if main download is still running
if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
    exit 0
fi

# Already done this run?
if [ -f "$MARKER" ]; then
    exit 0
fi

# Any failed videos?
if ! python3 -c "
import json
d=json.load(open('$STATE'))
v=d.get('downloaded_videos',{})
print(sum(1 for x in v.values() if x.get('has_failures')))
" | grep -q '^0$'; then
    echo "🔧 Main download finished. Running post-process to re-download failed videos..."
    bash /root/synapse_dl/post_process.sh "$ACCOUNT" 2>&1
    touch "$MARKER"
    echo "✅ Post-process complete. Watchdog will not run again."
fi
