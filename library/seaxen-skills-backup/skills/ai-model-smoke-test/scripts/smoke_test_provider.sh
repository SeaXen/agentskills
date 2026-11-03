#!/usr/bin/env bash
# Smoke-test all models in a provider's cache, with quota-aware retries.
# Usage: smoke_test_provider.sh <provider>
# Example: smoke_test_provider.sh google-gemini-cli
#
# Exits 0 if at least one model works, 1 if all fail, 2 on setup error.
set -uo pipefail

PROVIDER="${1:-}"
CACHE="${HOME}/.hermes/provider_models_cache.json"

if [[ -z "$PROVIDER" ]]; then
  echo "usage: $0 <provider>" >&2
  exit 2
fi
if [[ ! -f "$CACHE" ]]; then
  echo "Cache not found: $CACHE" >&2
  exit 2
fi

# Extract model list
MODELS=$(python3 - "$PROVIDER" "$CACHE" <<'PY' 2>/dev/null
import json, sys
provider, cache = sys.argv[1], sys.argv[2]
data = json.load(open(cache))
if provider not in data:
    sys.exit(f"provider {provider} not in cache")
for m in data[provider]['models']:
    print(m)
PY
)
if [[ -z "$MODELS" ]]; then
  echo "No models found for $PROVIDER in cache." >&2
  exit 2
fi

echo "=== $PROVIDER: smoke-testing $(echo "$MODELS" | wc -l) cached model(s) ==="
echo

declare -a ROWS=()
overall_exit=1

for model in $MODELS; do
  printf "--- %s ---\n" "$model"
  output=$(timeout 90 hermes chat -Q \
    -q "Reply with exactly: PONG. Nothing else." \
    --provider "$PROVIDER" \
    -m "$model" \
    --max-turns 0 2>&1 | tail -10)

  if echo "$output" | grep -Eq '(^|[[:space:]])PONG[.!]?[[:space:]]*$|^PONG$'; then
    echo "OK: works"
    ROWS+=("$model | works")
    overall_exit=0
  elif echo "$output" | grep -qi "quota exhausted\|429"; then
    wait_s=$(echo "$output" | grep -oE "reset after [0-9]+s" | grep -oE "[0-9]+" || echo 10)
    echo "QUOTA: waiting ${wait_s}s then retrying once..."
    sleep $((wait_s + 5))
    output=$(timeout 90 hermes chat -Q \
      -q "Reply with exactly: PONG. Nothing else." \
      --provider "$PROVIDER" \
      -m "$model" \
      --max-turns 0 2>&1 | tail -10)
    if echo "$output" | grep -Eq '(^|[[:space:]])PONG[.!]?[[:space:]]*$|^PONG$'; then
      echo "OK: works (after quota wait)"
      ROWS+=("$model | works (after wait)")
      overall_exit=0
    else
      echo "FAIL: still failing after wait"
      ROWS+=("$model | quota-blocked")
    fi
  elif echo "$output" | grep -Eqi "404|retired|not found|not available"; then
    echo "FAIL: retired/404"
    ROWS+=("$model | retired/404")
  elif echo "$output" | grep -Eqi "not logged in|unauthorized|401|403|auth"; then
    echo "FAIL: auth"
    ROWS+=("$model | auth")
  else
    echo "UNKNOWN:"
    echo "$output" | head -3
    ROWS+=("$model | unknown")
  fi
  sleep 2  # don't hammer sibling models on tight per-minute quotas
done

echo
echo "=== SUMMARY ($PROVIDER) ==="
printf '  %s\n' "${ROWS[@]}"

exit $overall_exit
