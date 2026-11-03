#!/usr/bin/env bash
set -euo pipefail
SKILL_DIR="/mnt/tb/hermes/skills/research/crypto-research-alerting"
PID_FILE="$SKILL_DIR/browser_dashboard.pid"
LOG_FILE="$SKILL_DIR/browser_dashboard.log"
if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "running pid=$(cat "$PID_FILE")"
else
  echo "not running"
fi
if [[ -f "$LOG_FILE" ]]; then
  echo "log=$LOG_FILE"
fi
