#!/usr/bin/env bash
# deploy_to_medsea.sh — fast-iteration deployment for interactive quiz tools.
#
# Why this script exists:
#   The MedSea container is built with COPY site/ in the Dockerfile — NOT a bind mount.
#   New files added to the host site/ directory do NOT appear in the running container.
#   Two options: full docker build (~5 min) or docker cp + chmod (~3 sec).
#   This script uses the fast option.
#
# CRITICAL: After every docker cp, run chmod -R a+r on the new directories.
#   docker cp preserves restrictive host permissions (often 600); nginx in the
#   container runs as the 'nginx' user and CANNOT read 600 files. Result: 403
#   Forbidden even though the file exists. Validated pitfall 2026-06-21.
#
# Usage:
#   bash deploy_to_medsea.sh                # deploys everything under site/
#   bash deploy_to_medsea.sh --rebuild      # full docker rebuild + restart
#   bash deploy_to_medsea.sh --verify       # just check endpoints

set -euo pipefail

SITE_DIR="/mnt/tb/Sea-knowledge/#MedSea/site"
CONTAINER="medsea"

deploy_fast() {
  echo "=== Fast deployment (docker cp) ==="

  # Deploy the three top-level tools
  for path in exam flashcards assets; do
    if [ -e "$SITE_DIR/$path" ]; then
      echo "  -> copying $path"
      docker cp "$SITE_DIR/$path" "$CONTAINER:/usr/share/nginx/html/$path"
    fi
  done

  # CRITICAL: fix permissions. nginx user (uid 101) can't read 600 files.
  echo "=== Fixing permissions ==="
  docker exec "$CONTAINER" chmod -R a+r \
    /usr/share/nginx/html/exam \
    /usr/share/nginx/html/flashcards \
    /usr/share/nginx/html/assets

  echo "=== Verifying endpoints ==="
  for path in /exam/ /flashcards/ /assets/exam-engine.js /assets/questions.json /; do
    code=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8855$path")
    size=$(curl -s -o /dev/null -w "%{size_download}" "http://localhost:8855$path")
    echo "  http://localhost:8855$path -> $code (${size}b)"
    if [ "$code" != "200" ]; then
      echo "WARNING: $path returned $code"
    fi
  done
}

rebuild_full() {
  echo "=== Full Docker rebuild (compose) ==="
  bash "/mnt/tb/Sea-knowledge/#MedSea/scripts/redeploy.sh"
}

verify_only() {
  for path in /exam/ /flashcards/ /assets/exam-engine.js /assets/questions.json /; do
    code=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8855$path")
    size=$(curl -s -o /dev/null -w "%{size_download}" "http://localhost:8855$path")
    echo "  http://localhost:8855$path -> $code (${size}b)"
  done
}

case "${1:-}" in
  --rebuild) rebuild_full ;;
  --verify)  verify_only ;;
  *)         deploy_fast ;;
esac
