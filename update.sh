#!/usr/bin/env bash
# ==============================================================================
# AgentSkills Automated Updater & Sync for Linux & macOS
# Author: SeaXen (https://github.com/SeaXen/agentskills)
#
# Usage:
#   ./update.sh               # Full update across all skills, library & git push
#   ./update.sh --no-push     # Local update without git push
#   ./update.sh --about       # Vault inventory stats & repository details
#   ./update.sh --find <word> # Global search across all 2,031 skills
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

exec "$PYTHON_BIN" "$SCRIPT_DIR/update.py" "$@"
