#!/usr/bin/env bash
# One-time setup for the synapse-lms-download skill.
# Creates the venv at a PERSISTENT location (NOT /tmp, which is tmpfs and gets
# wiped between sessions), installs deps, and downloads Chromium for Playwright.
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# PERSISTENT venv location. /tmp is tmpfs on this host and is wiped between
# sessions, so do NOT put the venv there. Use $HOME/.venvs (shared across
# skills) or the skill's own .venv dir (also persistent since the skill lives
# in /root/.hermes/skills/).
VENV_DIR="${SYNAPSE_VENV_DIR:-$HOME/.venvs/synapse-env}"
PYTHON_BIN="${PYTHON_BIN:-python3.13}"

if [[ ! -d "${VENV_DIR}" ]]; then
  echo "==> Creating venv at ${VENV_DIR}"
  uv venv "${VENV_DIR}" --python "${PYTHON_BIN}"
fi

echo "==> Installing deps into venv"
uv pip install --python "${VENV_DIR}/bin/python" \
  playwright \
  pycryptodome \
  yt-dlp

echo "==> Installing Chromium for Playwright"
"${VENV_DIR}/bin/python" -m playwright install chromium

# Make sure the venv bin is executable
chmod +x "${VENV_DIR}/bin/"* 2>/dev/null || true

# Ensure account directory exists
ACCOUNTS_DIR="${SYNAPSE_ACCOUNTS_DIR:-$HOME/synapse_dl/accounts}"
mkdir -p "${ACCOUNTS_DIR}"

cat <<EOF

✅ Setup complete.

Venv:        ${VENV_DIR}
Accounts:    ${ACCOUNTS_DIR}

Quick start:
  # 1. Register an account (one per LMS login):
  ACCT=sagar
  printf '%s' 'YOUR_LMS_PASSWORD' > ${ACCOUNTS_DIR}/\${ACCT}.creds
  chmod 600 ${ACCOUNTS_DIR}/\${ACCT}.creds

  # 2. Seed the state file (see SKILL.md Quickstart for the one-liner)

  # 3. Run:
  ${VENV_DIR}/bin/python ${SKILL_DIR}/download_all.py \${ACCT} --dry-run
  ${VENV_DIR}/bin/python ${SKILL_DIR}/download_all.py \${ACCT}

NOTE: Do NOT put the venv in /tmp — /tmp is tmpfs and gets wiped between
sessions on this host. See SKILL.md pitfall #14.
EOF
