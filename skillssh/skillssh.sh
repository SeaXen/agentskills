#!/usr/bin/env bash
# ==============================================================================
# skills.sh Vault Tracker & Ingestion Tool for Linux & macOS
# Website: https://www.skills.sh/
#
# Usage:
#   ./skillssh.sh --check
#   ./skillssh.sh --check --min-installs 500k
#   ./skillssh.sh --sync
#   ./skillssh.sh --sync --push
#   ./skillssh.sh --sync --repo owner/repo
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

exec "$PYTHON_BIN" "$SCRIPT_DIR/skillssh.py" "$@"
