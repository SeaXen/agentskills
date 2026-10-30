#!/usr/bin/env bash
# ==============================================================================
# The Skill Leaderboard Tracker & Vault Synchronizer for Linux & macOS
# Website: https://www.skillleaderboard.com/
#
# Usage:
#   ./skillleaderboard.sh --trending 50
#   ./skillleaderboard.sh --starred 150
#   ./skillleaderboard.sh --trending 50 --json
#   ./skillleaderboard.sh --trending 50 --ingest
#   ./skillleaderboard.sh --starred 150 --ingest --push
# ==============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    echo "❌ Error: Python 3 is required but not installed or not in PATH."
    exit 1
fi

exec "$PYTHON_BIN" "$SCRIPT_DIR/skillleaderboard.py" "$@"
