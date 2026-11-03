#!/usr/bin/env bash
set -euo pipefail
SKILL_DIR="/mnt/tb/hermes/skills/research/crypto-research-alerting"
PID_FILE="$SKILL_DIR/browser_dashboard.pid"
LOG_FILE="$SKILL_DIR/browser_dashboard.log"
HOST="${1:-0.0.0.0}"
PORT="${2:-8765}"
WATCHLIST="${3:-$SKILL_DIR/templates/watchlist.yaml}"

if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "Dashboard already running on PID $(cat "$PID_FILE")"
  exit 0
fi

nohup python3 "$SKILL_DIR/scripts/browser_dashboard_server.py" --host "$HOST" --port "$PORT" --watchlist "$WATCHLIST" >> "$LOG_FILE" 2>&1 &
PID=$!
echo "$PID" > "$PID_FILE"
sleep 1
if kill -0 "$PID" 2>/dev/null; then
  echo "Started crypto browser dashboard on http://$HOST:$PORT (PID $PID)"
else
  echo "Failed to start dashboard. Check $LOG_FILE" >&2
  exit 1
fi
