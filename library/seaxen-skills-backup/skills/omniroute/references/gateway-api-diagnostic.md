# OmniRoute gateway API diagnostic (DietPi)

Host: `192.168.0.222:20128`  
Data: `/mnt/tb/1Apps/omniroute/data`

## 1. Container

```bash
cd /mnt/tb/1Apps/omniroute
docker compose ps
docker compose logs --since 2h omniroute | rg 'ROUTING|AUTH|HTTP|502|413|500|codex|cx/'
```

## 2. Models list

```bash
curl -sS http://192.168.0.222:20128/v1/models | python3 -c "
import sys,json
d=json.load(sys.stdin)
ids=[m['id'] for m in d.get('data',[])]
for q in ('cx/gpt-5.4','codex/gpt-5.4','chatgpt-web/gpt-5.4'):
    print(q, 'YES' if q in ids or any(q in i for i in ids) else 'NO')
"
```

## 3. Completion smoke test (server-side)

Uses the `Hermes` API key from SQLite (adjust `name=` if needed):

```bash
APIKEY=$(sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "SELECT key FROM api_keys WHERE name='Hermes' LIMIT 1;")
curl -sS -m 120 -w "\nHTTP:%{http_code}\n" \
  http://192.168.0.222:20128/v1/chat/completions \
  -H "Authorization: Bearer $APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"cx/gpt-5.4","messages":[{"role":"user","content":"Reply ok"}],"max_tokens":16,"stream":false}'
```

Expect: HTTP 200 and assistant content. If this passes but the user's laptop fails → network or client key, not OmniRoute.

## 4. Today's failed calls (aggregate)

```bash
python3 <<'PY'
import json,glob
from collections import Counter
from datetime import date
base=f"/mnt/tb/1Apps/omniroute/data/call_logs/{date.today().isoformat()}"
fail=[]
for path in glob.glob(base+"/*.json"):
    try:
        s=json.load(open(path)).get("summary",{})
        if (s.get("status") or 0) >= 400:
            fail.append((s.get("requestedModel"), s.get("provider"), s.get("status")))
    except Exception:
        pass
for k,c in Counter(fail).most_common(20):
    print(c, k)
PY
```

## 5. Codex connections

```bash
sqlite3 /mnt/tb/1Apps/omniroute/data/storage.sqlite \
  "SELECT substr(id,1,8), substr(email,1,40), is_active, test_status, substr(last_error,1,80)
   FROM provider_connections WHERE provider='codex';"
```

## Expected healthy log lines (cx/gpt-5.4)

```
POST /v1/chat/completions | cx/gpt-5.4
ROUTING: cx/gpt-5.4 → codex/gpt-5.4
AUTH: Using codex account: <connection-prefix>...
```

Optional: `🌊 [STREAM] CODEX | gpt-5.4 | ... | complete`