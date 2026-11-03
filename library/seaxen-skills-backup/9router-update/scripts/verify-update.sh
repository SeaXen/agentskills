#!/usr/bin/env bash
# 9router post-update verifier — runs all 7 checks from the skill.
# Exit 0 if all pass, 1 otherwise.
set -u

CONTAINER="${1:-9router}"
PORT="${PORT:-20111}"
PASS=0
FAIL=0
declare -a FAILURES=()

check() {
  local label="$1"
  local actual="$2"
  local expected="$3"
  if [[ "$actual" == *"$expected"* ]]; then
    echo "  ✅ $label"
    PASS=$((PASS+1))
  else
    echo "  ❌ $label"
    echo "      expected: $expected"
    echo "      got:      $actual"
    FAIL=$((FAIL+1))
    FAILURES+=("$label")
  fi
}

echo "=== 9router post-update verifier (container=$CONTAINER, port=$PORT) ==="
echo ""

# 1. Container running
echo "[1/7] Container status"
STATUS=$(docker ps --filter "name=$CONTAINER" --format "{{.Status}}" 2>/dev/null)
check "container up" "$STATUS" "Up "
echo ""

# 2. Health endpoint
echo "[2/7] Health endpoint"
HEALTH=$(curl -s -m 5 "http://127.0.0.1:${PORT}/api/health" 2>&1)
check "health OK" "$HEALTH" '"ok":true'
echo ""

# 3. Version
echo "[3/7] Version from container"
VERSION=$(docker exec "$CONTAINER" cat /app/package.json 2>/dev/null | grep '"version"' | head -1)
check "version field" "$VERSION" '"version"'
echo "  → $VERSION"
echo ""

# 4. Image digest
echo "[4/7] Image digest"
DIGEST=$(docker inspect "$CONTAINER" --format '{{.Image}}' 2>/dev/null | cut -c8-)
check "image present (sha256)" "$DIGEST" ""
echo "  → ${DIGEST:0:24}…"
echo ""

# 5. UI patch in 5497 bundle
echo "[5/7] UI patch in browser bundle (5497 chunk)"
UI_PATCH=$(docker exec "$CONTAINER" sh -c \
  "grep -oE '90d.{0,40}180d.{0,40}365d.{0,40}all' /app/.next/static/chunks/5497-*.js 2>/dev/null | head -c 200" 2>&1)
check "UI has 90D/180D/365D/All" "$UI_PATCH" "90d"
echo ""

# 6. API patch (stats)
echo "[6/7] API patch — stats route"
STATS_PATCH=$(docker exec "$CONTAINER" grep -oE 'today.*24h.*7d.*30d.*60d.*90d.*180d.*365d' \
  /app/.next/server/app/api/usage/stats/route.js 2>/dev/null | head -c 200)
check "stats API has 90d/180d/365d" "$STATS_PATCH" "180d"
echo ""

# 7. API patch (chart)
echo "[7/7] API patch — chart route"
CHART_PATCH=$(docker exec "$CONTAINER" grep -oE 'today.*24h.*7d.*30d.*60d.*90d.*180d.*365d.*all' \
  /app/.next/server/app/api/usage/chart/route.js 2>/dev/null | head -c 200)
check "chart API has 90d/180d/365d/all" "$CHART_PATCH" "365d"
echo ""

echo "=== Summary ==="
echo "  passed: $PASS / 7"
echo "  failed: $FAIL"
if [ "$FAIL" -gt 0 ]; then
  echo "  failing checks:"
  for f in "${FAILURES[@]}"; do
    echo "    - $f"
  done
  echo ""
  echo "  Reminder: hard-refresh browser (Ctrl+Shift+R) on /dashboard/usage"
  exit 1
fi
echo "  ✅ All 7 checks passed. Reminder: hard-refresh browser (Ctrl+Shift+R) on /dashboard/usage"
exit 0
