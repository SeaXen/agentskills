#!/usr/bin/env bash
# Extract Live Next.js Server Action IDs (40–44 hex) for a given URL.
# Usage: bash extract_action_ids.sh <url> [outdir]
set -euo pipefail
URL="${1:?Usage: extract_action_ids.sh <url>}"
OUT="${2:-/tmp/airtel_chunks}"
mkdir -p "$OUT"
HTML="$OUT/page.html"
echo "== Fetch page =="
curl -s -L "$URL" -o "$HTML"
echo "bytes: $(wc -c < "$HTML")"
echo "== static form/action check (App Router static pages return 0) =="
echo "  <form count: $(grep -c '<form' "$HTML" || true)"
echo "  action= count: $(grep -c 'action=' "$HTML" || true)"
echo "== collect chunk URLs =="
CHUNKS=$(grep -oE '/_next/static/chunks/[A-Za-z0-9_/.-]+\.js' "$HTML" | sort -u)
echo "$CHUNKS" | while read -r c; do
  fn=$(echo "$c" | sed 's#/_next/static/chunks/##')
  curl -s -L "${URL%%/}/_next/static/chunks/${fn#/}" -o "$OUT/$fn" 2>/dev/null || true
done
echo "downloaded: $(ls -1 "$OUT"/*.js 2>/dev/null | wc -l) chunk files"
echo "== extract action IDs =="
grep -rhoE 'createServerReference\)\("[0-9a-f]{40,44}"' "$OUT" \
  | sed -E 's/.*"([0-9a-f]+)"/\1/' | sort -u
