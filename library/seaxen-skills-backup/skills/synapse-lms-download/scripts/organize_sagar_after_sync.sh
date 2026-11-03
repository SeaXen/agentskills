#!/usr/bin/env bash
set -euo pipefail

SRC=${1:-/mnt/tb/synapse_26}
DST=${2:-/mnt/tb/synapse_26_by_chapter}

/root/.venvs/synapse-env/bin/python \
  /root/.hermes/skills/synapse-lms-download/scripts/organize_by_chapter.py \
  "$SRC" "$DST"
