#!/usr/bin/env bash
# health-check.sh — verify the monitor daemon is alive and DB is fresh.
# Add to cron: */5 * * * * /opt/<APP>/scripts/health-check.sh
# Or wire into your monitoring stack.

set -euo pipefail

APP="${APP_NAME:-<APP_NAME>}"
SERVICE="${SERVICE:-${APP}-collector}"
DB="${DB:-/var/lib/${APP}/${APP}.db}"
MAX_AGE_SEC="${MAX_AGE_SEC:-300}"  # alert if no fresh sample in 5 min
API="${API:-http://127.0.0.1:6677/health}"

# 1. Is the service running?
if ! systemctl --user is-active "$SERVICE" >/dev/null 2>&1 \
   && ! systemctl is-active "$SERVICE" >/dev/null 2>&1; then
    echo "FAIL: $SERVICE is not running"
    exit 1
fi

# 2. Is the web UI responding?
if command -v curl >/dev/null 2>&1; then
    if ! curl -sf -m 5 "$API" >/dev/null; then
        echo "WARN: $API not responding (web service may be down)"
    fi
fi

# 3. Is the DB being written to recently?
if [[ -f "$DB" ]]; then
    last_ts=$(sqlite3 "$DB" "SELECT MAX(ts) FROM samples" 2>/dev/null || echo 0)
    now=$(date +%s)
    age=$((now - last_ts))
    if (( age > MAX_AGE_SEC )); then
        echo "FAIL: $DB last sample is ${age}s old (>${MAX_AGE_SEC}s threshold)"
        exit 1
    fi
    echo "OK: $SERVICE running, DB fresh (last sample ${age}s ago)"
else
    echo "WARN: $DB does not exist yet (collector may be starting up)"
fi
