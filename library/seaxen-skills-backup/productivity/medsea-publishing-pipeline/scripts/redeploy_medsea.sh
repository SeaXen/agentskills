#!/usr/bin/env bash
# Thin wrapper — canonical redeploy lives in the MedSea repo.
set -euo pipefail
exec bash "/mnt/tb/Sea-knowledge/#MedSea/scripts/redeploy.sh"