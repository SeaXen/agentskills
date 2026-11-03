#!/usr/bin/env bash
set -euo pipefail
SKILL_DIR="/mnt/tb/hermes/skills/research/crypto-research-alerting"
PID_FILE="$SKILL_DIR/browser_dashboard.pid"

if [[ ! -f "$PID_FILE" ]]; then
  echo "No PID file found. Dashboard may not be running."
  exit 0
fi

PID="$(cat "$PID_FILE")"
if kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  sleep 1
  if kill -0 "$PID" 2>/dev/null; then
    kill -9 "$PID" || true
  fi
  echo "Stopped crypto browser dashboard (PID $PID)"
else
  echo "Process $PID was not running"
fi
rm -f "$PID_FILE"
