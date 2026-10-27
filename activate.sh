#!/usr/bin/env bash
# ==============================================================================
# AgentSkills Universal Activator Launcher for Linux & macOS
# Author: SeaXen (https://github.com/SeaXen/agentskills)
#
# Usage:
#   ./activate.sh <skill-name>        - Link/activate skill into active workspace
#   ./activate.sh search <keyword>    - Search across all 2,031 reserve skills
#   ./activate.sh remove <skill-name> - Deactivate / unlink skill
#   ./activate.sh categories          - List all 38 functional categories
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

exec "$PYTHON_BIN" "$SCRIPT_DIR/library/activate_skill.py" "$@"
