#!/usr/bin/env bash
# ==============================================================================
# The Skill Leaderboard Tracker & Vault Synchronizer for Linux & macOS
# Website: https://www.skillleaderboard.com/
#
# Usage:
#   ./skillleaderboard.sh --trending               # Audit Top 50 Trending skills (7-day growth)
#   ./skillleaderboard.sh --starred                # Audit Top 150 Most Starred skills
#   ./skillleaderboard.sh --trending 50            # Check specific limit
#   ./skillleaderboard.sh --starred 150            # Check specific limit
#   ./skillleaderboard.sh --json                   # Output structured JSON for agents
#   ./skillleaderboard.sh --trending 50 --ingest   # Auto-clone, clean & categorize missing skills
#   ./skillleaderboard.sh --starred 150 --ingest --push # Ingest and git push to GitHub
# ==============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Find python3 or python
if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    echo "❌ Error: Python 3 is required but not installed or not in PATH."
    exit 1
fi

exec "$PYTHON_BIN" "$SCRIPT_DIR/scripts/skillleaderboard.py" "$@"
