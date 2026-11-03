#!/usr/bin/env bash
# Non-destructive "is there an update?" probe.
# Compares local /mnt/tb/1Apps/9router-upstream HEAD against latest upstream tag.
# Reports only — never pulls, restarts, or modifies the running container.
set -u

LOCAL_REPO="${1:-/mnt/tb/1Apps/9router-upstream}"
RUNNING_VERSION=$(docker exec 9router cat /app/package.json 2>/dev/null \
  | python3 -c "import sys,json; print(json.load(sys.stdin).get('version','?'))" 2>/dev/null)

echo "=== 9router version check (no changes) ==="
echo ""
echo "Running:    v${RUNNING_VERSION}"
echo "Local repo: $LOCAL_REPO"
echo ""

if [ ! -d "$LOCAL_REPO/.git" ]; then
  echo "❌ Local repo not found: $LOCAL_REPO"
  exit 1
fi

cd "$LOCAL_REPO"
git fetch origin --tags --force >/dev/null 2>&1
LATEST_TAG=$(git tag --sort=-v:refname 2>/dev/null | head -1)
LATEST_VERSION=${LATEST_TAG#v}

echo "Latest tag: $LATEST_TAG"
echo ""

if [ "$RUNNING_VERSION" = "$LATEST_VERSION" ]; then
  echo "✅ Up to date. No update needed."
  exit 0
fi

# Show commits between running and latest
COMMITS=$(git log "v${RUNNING_VERSION}..${LATEST_TAG}" --oneline 2>/dev/null | wc -l)
echo "📦 Update available: v${RUNNING_VERSION} → ${LATEST_TAG} (${COMMITS} commits)"
echo ""
echo "Recent commits:"
git log "v${RUNNING_VERSION}..${LATEST_TAG}" --oneline 2>/dev/null | head -10
echo ""
echo "Run: cd /mnt/tb/1Apps/9router && bash update.sh"
exit 0
