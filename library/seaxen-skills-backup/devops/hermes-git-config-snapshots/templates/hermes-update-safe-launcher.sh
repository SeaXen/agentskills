#!/usr/bin/env bash
# Install to /usr/local/bin/hermes-update-safe (see hermes-git-config-snapshots skill).
# Do NOT copy scripts/hermes-update-safe.sh here — its HERE= resolves wrong from /usr/local/bin.
set -euo pipefail
REPO="${HERMES_SNAPSHOT_REPO:-/root/.hermes-config-snapshots}"
REAL="${REPO}/scripts/hermes-update-safe.sh"
if [ ! -x "$REAL" ]; then
  echo "FATAL: missing ${REAL}" >&2
  exit 1
fi
exec "$REAL" "$@"