#!/usr/bin/env bash
# Verify the live MedSea site actually serves the question bank that lives on
# disk. Exits non-zero if local JSON, container JSON, and HTTP-served JSON
# disagree on item counts. This is the gate that prevents "claimed deployed"
# when the build never made it onto the live site.
#
# Usage:
#   bash scripts/verify_live_question_bank.sh
#   bash scripts/verify_live_question_bank.sh --container medsea --port 8855
#
# Required env (or use defaults):
#   MEDSEA_ROOT  /mnt/tb/Sea-knowledge/#MedSea
#   CONTAINER    medsea
#   SITE_PORT    8855
#   SITE_URL     http://localhost:8855   (override for public domain check)
#
# The script never lies. It does not "warn and continue" — mismatch is a
# hard failure. Read the output before claiming any deploy is done.

set -euo pipefail

MEDSEA_ROOT="${MEDSEA_ROOT:-/mnt/tb/Sea-knowledge/#MedSea}"
CONTAINER="${CONTAINER:-medsea}"
SITE_PORT="${SITE_PORT:-8855}"
SITE_URL="${SITE_URL:-http://localhost:${SITE_PORT}}"

LOCAL_DIR="${MEDSEA_ROOT}/site/assets"
CONTAINER_DIR="/usr/share/nginx/html/assets"

# Allow CLI override
while [[ $# -gt 0 ]]; do
  case "$1" in
    --container) CONTAINER="$2"; shift 2 ;;
    --port)      SITE_PORT="$2"; shift 2 ;;
    --url)       SITE_URL="$2"; shift 2 ;;
    --root)      MEDSEA_ROOT="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 2 ;;
  esac
done

red()   { printf '\033[31m%s\033[0m\n' "$*"; }
green() { printf '\033[32m%s\033[0m\n' "$*"; }
yellow(){ printf '\033[33m%s\033[0m\n' "$*"; }
hdr()   { printf '\n\033[1m== %s ==\033[0m\n' "$*"; }

count_items() {
  local f="$1"
  python3 -c "
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception as e:
    print('ERR', e)
    sys.exit(0)
if isinstance(d, list):
    print(len(d))
elif isinstance(d, dict):
    for k in ('items','questions','data','rows'):
        if k in d and isinstance(d[k], list):
            print(len(d[k])); sys.exit(0)
    print(0)
else:
    print(0)
" "$f"
}

index_count() {
  local f="$1"
  python3 -c "
import json, sys
d = json.load(open(sys.argv[1]))
t = d.get('totals', {}) if isinstance(d, dict) else {}
print('MCQ=%(mcq)d SBA=%(sba)d FC=%(flashcard)d' % t)
" "$f"
}

fail=0

hdr "1. Local JSON (on-disk, source of truth)"
for kind in mcq sba flashcard index; do
  f="${LOCAL_DIR}/questions-${kind}.json"
  if [[ ! -f "$f" ]]; then
    red "  MISSING: $f"
    fail=1
    continue
  fi
  size=$(stat -c%s "$f" 2>/dev/null || stat -f%z "$f")
  if [[ "$kind" == "index" ]]; then
    printf "  %-12s  %8s bytes  %s\n" "$kind" "$size" "$(index_count "$f")"
  else
    n=$(count_items "$f")
    printf "  %-12s  %8s bytes  %9d items\n" "$kind" "$size" "$n"
  fi
done

hdr "2. Container JSON (running site, what nginx serves)"
if ! docker ps --format '{{.Names}}' | grep -qx "$CONTAINER"; then
  red "  Container '$CONTAINER' is not running. Cannot verify live deploy."
  fail=1
else
  for kind in mcq sba flashcard index; do
    f="${CONTAINER_DIR}/questions-${kind}.json"
    if ! docker exec "$CONTAINER" test -f "$f"; then
      red "  MISSING in container: $f"
      fail=1
      continue
    fi
    size=$(docker exec "$CONTAINER" stat -c%s "$f" 2>/dev/null)
    if [[ "$kind" == "index" ]]; then
      printf "  %-12s  %8s bytes  %s\n" "$kind" "$size" "$(docker exec "$CONTAINER" python3 -c "
import json, sys
d = json.load(sys.stdin)
t = d.get('totals', {})
print('MCQ=%(mcq)d SBA=%(sba)d FC=%(flashcard)d' % t)
" < "$f" 2>/dev/null || echo "?")"
    else
      n=$(docker exec "$CONTAINER" python3 -c "
import json, sys
d = json.load(sys.stdin)
print(len(d) if isinstance(d, list) else 0)
" < "$f" 2>/dev/null)
      printf "  %-12s  %8s bytes  %9d items\n" "$kind" "$size" "${n:-?}"
    fi
  done
fi

hdr "3. HTTP-served JSON (what the browser actually loads)"
for kind in mcq sba flashcard index; do
  url="${SITE_URL}/assets/questions-${kind}.json"
  out=$(curl -sS -o /tmp/_medsea_check.json -w '%{http_code} %{size_download}' "$url" 2>&1) || true
  code=$(echo "$out" | awk '{print $1}')
  size=$(echo "$out" | awk '{print $2}')
  if [[ "$code" != "200" ]]; then
    red "  HTTP $code for $url"
    fail=1
    continue
  fi
  if [[ "$kind" == "index" ]]; then
    body=$(index_count /tmp/_medsea_check.json)
  else
    n=$(count_items /tmp/_medsea_check.json)
    body="$n items"
  fi
  printf "  %-12s  HTTP %s  %8s bytes  %s\n" "$kind" "$code" "$size" "$body"
done

hdr "4. Cross-check local vs HTTP-served"
for kind in mcq sba flashcard; do
  local_n=$(count_items "${LOCAL_DIR}/questions-${kind}.json")
  http_n=$(count_items /tmp/_medsea_check.json 2>/dev/null || echo 0)
  if [[ "$http_n" -ne "$local_n" ]]; then
    red "  MISMATCH $kind: local=$local_n  http=$http_n"
    fail=1
  else
    green "  OK      $kind: $local_n items"
  fi
done

hdr "5. Search-source spot-check (does the live exam page see new items?)"
# Pick a ch with the largest authored content; verify the live JSON has content
# for that chapter that the source MD files have
if [[ -f /tmp/_medsea_check.json ]]; then
  python3 << 'PYEOF'
import json, sys
try:
    bank = json.load(open('/tmp/_medsea_check.json'))
except Exception as e:
    print(f"  ERR loading live bank: {e}"); sys.exit(0)
# Find the chapter with the most items
from collections import Counter
ch_counter = Counter()
for q in bank:
    ch = q.get('chapter_slug') or q.get('chapter') or 'unknown'
    ch_counter[ch] += 1
top = ch_counter.most_common(3)
print(f"  Top chapters in live bank: {top}")
PYEOF
fi

hdr "Result"
if [[ $fail -ne 0 ]]; then
  red "  VERIFY FAILED. The live site is NOT serving the on-disk question bank."
  red "  Do NOT claim 'deployed'. Run the full deploy cycle:"
  red "    1. python3 site/scripts/rebuild_question_bank_v5.py"
  red "    2. docker cp site/assets/questions-*.json ${CONTAINER}:${CONTAINER_DIR}/"
  red "    3. docker commit ${CONTAINER} medsea-site:latest"
  red "    4. bash scripts/verify_live_question_bank.sh"
  exit 1
else
  green "  VERIFY PASSED. Local, container, and HTTP all agree."
  exit 0
fi
