#!/usr/bin/env bash
# Verify a third-party multi-protocol AI gateway (OpenRouter, OpenModel, Portkey, etc.)
# Usage: verify_third_party_gateway.sh <api-host> <key-file> [--strict]
#
# Exit codes:
#   0 = all critical checks passed
#   1 = DNS / TLS unreachable
#   2 = auth invalid on at least one inference call
#   3 = catalog unreachable but DNS works

set -u
HOST="${1:?usage: $0 <api-host> <key-file>}"
KEY_FILE="${2:?usage: $0 <api-host> <key-file>}"
shift 2
STRICT=0
[[ "${1:-}" == "--strict" ]] && STRICT=1

KEY=$(tr -d '[:space:]' < "$KEY_FILE")
[[ ${#KEY} -lt 8 ]] && { echo "ERROR: key in $KEY_FILE is empty or too short"; exit 1; }

# ---------- 1. DNS check ----------
echo "=== DNS check ==="
RESOLVED=0
for h in "$HOST"; do
  if getent hosts "$h" >/dev/null 2>&1; then
    echo "OK: $h resolves -> $(getent hosts "$h" | head -1)"
    RESOLVED=1
    break
  fi
done
if [[ $RESOLVED -eq 0 ]]; then
  # Try common alternates before declaring dead
  BASE="${HOST#api.}"
  for alt in "api.${HOST#api.}" \
              "${BASE%.app}.ai" "${BASE%.app}.com" "${BASE%.app}.io" \
              "${HOST%.app}.ai" "${HOST%.app}.com" "${HOST%.app}.io"; do
    if [[ "$alt" != "$HOST" ]] && getent hosts "$alt" >/dev/null 2>&1; then
      echo "FAIL: $HOST does NOT resolve, but $alt does. Likely a TLD typo."
      echo "      Re-run with: $0 $alt $KEY_FILE"
      exit 1
    fi
  done
  echo "FAIL: $HOST does not resolve and no obvious alt found."
  exit 1
fi

# ---------- 2. TLS reachability ----------
echo ""
echo "=== TLS / reachability ==="
CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 "https://$HOST/v1/models")
if [[ "$CODE" == "000" ]]; then
  echo "FAIL: TLS / connection failed for https://$HOST/v1/models"
  exit 1
fi
echo "GET /v1/models -> HTTP $CODE"

# ---------- 3. Catalog parse ----------
echo ""
echo "=== Catalog ==="
CATALOG=$(curl -s --max-time 20 -H "Authorization: Bearer *** "https://$HOST/v1/models")
if ! echo "$CATALOG" | python3 -c "import json,sys; json.load(sys.stdin)" 2>/dev/null; then
  echo "FAIL: /v1/models did not return JSON"
  echo "Body: ${CATALOG:0:300}"
  exit 3
fi

# Group models by protocol
echo "$CATALOG" | python3 - <<'PY'
import json, sys
data = json.loads(sys.stdin.read())
models = data.get("data", [])
print(f"Total models: {len(models)}")

by_proto = {}
for m in models:
    protos = tuple(sorted(m.get("supported_protocols", []) or ["unknown"]))
    by_proto.setdefault(protos, []).append(m["id"])

for protos, ids in sorted(by_proto.items(), key=lambda x: -len(x[1])):
    label = "/".join(protos) if protos != ("unknown",) else "no protocol field"
    print(f"  [{label}] ({len(ids)})")
    for i in ids[:5]:
        print(f"    - {i}")
    if len(ids) > 5:
        print(f"    ... and {len(ids)-5} more")
PY

# ---------- 4. Inference probe ----------
echo ""
echo "=== Inference probes ==="

# Pick one OpenAI-protocol and one Anthropic-protocol model
PICKED_OAI=$(echo "$CATALOG" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for m in d.get('data',[]):
    p=m.get('supported_protocols',[])
    if 'chat_completions' in p or 'responses' in p:
        print(m['id']); break
")
PICKED_ANT=$(echo "$CATALOG" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for m in d.get('data',[]):
    p=m.get('supported_protocols',[])
    if 'messages' in p:
        print(m['id']); break
")

OVERALL=0

if [[ -n "$PICKED_OAI" ]]; then
  echo ""
  echo "-- OpenAI-protocol model: $PICKED_OAI --"
  RESP=$(curl -s -X POST \
    -H "Authorization: Bearer *** \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"$PICKED_OAI\",\"max_tokens\":40,\"messages\":[{\"role\":\"user\",\"content\":\"Reply with just the word PONG and nothing else.\"}]}" \
    "https://$HOST/v1/chat/completions")
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X POST \
    -H "Authorization: Bearer *** \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"$PICKED_OAI\",\"max_tokens\":40,\"messages\":[{\"role\":\"user\",\"content\":\"Reply with just the word PONG and nothing else.\"}]}" \
    "https://$HOST/v1/chat/completions")
  echo "HTTP $STATUS"
  echo "$RESP" | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)
    if 'error' in d:
        print('  ERROR:', d['error'])
        sys.exit(2)
    txt = d.get('choices',[{}])[0].get('message',{}).get('content','')
    print('  reply:', repr(txt[:120]))
except Exception as e:
    print('  parse error:', e); sys.exit(2)
" || OVERALL=2
else
  echo "(no OpenAI-protocol model found in catalog)"
fi

if [[ -n "$PICKED_ANT" ]]; then
  echo ""
  echo "-- Anthropic-protocol model: $PICKED_ANT --"
  RESP=$(curl -s -X POST \
    -H "Authorization: Bearer *** \
    -H "Content-Type: application/json" \
    -H "anthropic-version: 2023-06-01" \
    -d "{\"model\":\"$PICKED_ANT\",\"max_tokens\":40,\"messages\":[{\"role\":\"user\",\"content\":\"Reply with just the word PONG and nothing else.\"}]}" \
    "https://$HOST/v1/messages")
  STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X POST \
    -H "Authorization: Bearer *** \
    -H "Content-Type: application/json" \
    -H "anthropic-version: 2023-06-01" \
    -d "{\"model\":\"$PICKED_ANT\",\"max_tokens\":40,\"messages\":[{\"role\":\"user\",\"content\":\"Reply with just the word PONG and nothing else.\"}]}" \
    "https://$HOST/v1/messages")
  echo "HTTP $STATUS"
  echo "$RESP" | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)
    if 'error' in d and d['error'].get('type') == 'authentication_error':
        print('  ERROR:', d['error'].get('message'))
        sys.exit(2)
    txt=''
    for c in d.get('content',[]):
        if c.get('type')=='text': txt=c.get('text','')
    print('  reply:', repr(txt[:120]))
except Exception as e:
    print('  parse error:', e); sys.exit(2)
" || OVERALL=2
else
  echo "(no Anthropic-protocol model found in catalog)"
fi

echo ""
echo "=== Verdict ==="
[[ $OVERALL -eq 0 ]] && echo "PASS: at least one inference call succeeded with the supplied key." \
                   || echo "FAIL: inference calls did not succeed (auth, model, or routing issue)."

exit $OVERALL
