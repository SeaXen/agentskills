# OmniRoute Pricing Overrides via API

Use this when the Pricing dashboard is too flaky for repetitive edits.

## Endpoints
- `GET /api/pricing/models`
  - Returns provider aliases and model catalog.
- `GET /api/pricing?includeSources=1`
  - Returns current pricing map and source map.
- `PATCH /api/pricing`
  - Accepts one or more provider-alias pricing override objects.

## Alias discovery
Dashboard display names may differ from API aliases.

Observed in this environment:
- Codex dashboard section -> API alias `cx`
- ChatGPT Web dashboard section -> API alias `cgpt-web`

## Example: set all models for a provider alias to zero
```python
import requests
base='http://127.0.0.1:20128'
models=requests.get(base+'/api/pricing/models').json()
alias='cx'
ids=[m['id'] for m in models[alias]['models']]
override={mid:{'input':0,'output':0,'cached':0,'reasoning':0,'cache_creation':0} for mid in ids}
requests.patch(base+'/api/pricing', json={alias: override})
```

## Example used successfully
```python
import requests
base='http://127.0.0.1:20128'
models=requests.get(base+'/api/pricing/models').json()
for alias in ['cx','cgpt-web']:
    ids=[m['id'] for m in models[alias]['models']]
    override={mid:{'input':0,'output':0,'cached':0,'reasoning':0,'cache_creation':0} for mid in ids}
    r=requests.patch(base+'/api/pricing', json={alias: override})
    print(alias, r.status_code)
```

## Direct SQLite fallback (when API + UI both unreliable)

Pricing lives in `key_value` table, namespace `pricing`, keyed by provider alias.

- Short aliases observed: `anthropic`, `cgpt-web`, `cx`.
- The full `provider_connections.provider` slug is **also a valid key** for pricing entries
  (e.g. `openrouter`, `nvidia`, `cohere`, `openai-compatible-chat-<uuid>`).
- Each key's value is a JSON dict: `{ model_id: {input, output, cached, reasoning, cache_creation} }`.
- `sqlite3` CLI is NOT inside the OmniRoute container. Run Python on the host against
  `/mnt/tb/1Apps/omniroute/data/storage.sqlite` directly.

### Zero ALL pricing across every active provider

```python
import sqlite3, json
conn = sqlite3.connect('/mnt/tb/1Apps/omniroute/data/storage.sqlite')
cur = conn.cursor()
ZERO = {"input":0,"output":0,"cached":0,"reasoning":0,"cache_creation":0}

# 1. Zero existing pricing entries
cur.execute("SELECT key, value FROM key_value WHERE namespace='pricing'")
for k, v in cur.fetchall():
    d = json.loads(v)
    for m in d: d[m] = dict(ZERO)
    cur.execute("UPDATE key_value SET value=? WHERE namespace='pricing' AND key=?", (json.dumps(d), k))

# 2. Add zero entries for every synced model under every active provider slug
cur.execute("SELECT DISTINCT provider FROM provider_connections WHERE is_active=1")
active = [r[0] for r in cur.fetchall()]
cur.execute("SELECT key, value FROM key_value WHERE namespace='syncedAvailableModels'")
provider_models = {}
for k, v in cur.fetchall():
    ps = k.split(':',1)[0]
    for m in json.loads(v):
        if isinstance(m, dict) and 'id' in m:
            provider_models.setdefault(ps, set()).add(m['id'])
for ps in active:
    if ps not in provider_models: continue
    cur.execute("SELECT value FROM key_value WHERE namespace='pricing' AND key=?", (ps,))
    row = cur.fetchone()
    d = json.loads(row[0]) if row else {}
    for m in provider_models[ps]: d[m] = dict(ZERO)
    cur.execute("INSERT OR REPLACE INTO key_value(namespace,key,value) VALUES (?,?,?)",
                ('pricing', ps, json.dumps(d)))
conn.commit()
```

### Pre-flight backup (mandatory)
```bash
cp /mnt/tb/1Apps/omniroute/data/storage.sqlite \
   /mnt/tb/1Apps/omniroute/data/storage.sqlite.bak-before-zeropricing-$(date +%Y%m%d-%H%M%S)
```

### Caveats
- Newly synced models from providers will arrive with their default upstream price.
  This bulk-zero is a snapshot, not a policy — rerun the script after any provider sync
  to keep new entries at 0, or build a cron/middleware override.
- Tables `tier_assignments` and `model_intelligence` exist but were empty in this env;
  pricing source of truth is `key_value` namespace `pricing`.

## Verification pattern
```python
import requests
base='http://127.0.0.1:20128'
models=requests.get(base+'/api/pricing/models').json()
pricing=requests.get(base+'/api/pricing?includeSources=1').json()['pricing']
for alias in ['cx','cgpt-web']:
    ids=[m['id'] for m in models[alias]['models']]
    pdata=pricing.get(alias,{})
    ok=all(pdata.get(mid)=={'input':0,'output':0,'cached':0,'reasoning':0,'cache_creation':0} for mid in ids)
    print(alias, len(ids), ok)
```
