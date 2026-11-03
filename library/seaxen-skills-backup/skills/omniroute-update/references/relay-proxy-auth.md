# OmniRoute edge relay proxy — auth and test failures

## What edge relays are

OmniRoute can deploy lightweight **relay workers** on Vercel, Deno, or Cloudflare. Traffic flow:

```
Client → https://<relay-host>/  (worker)
       → x-relay-auth: <one-time secret>
       → x-relay-target / x-relay-path → upstream (must be **public** URL)
```

Relays on Vercel/Deno **cannot** reach `http://192.168.0.222:20128` or other LAN origins.

## Error strings

| UI / log message | Meaning |
|------------------|---------|
| `no relay auth token was found` | OmniRoute sent test **without** `x-relay-auth` — usually **missing `STORAGE_ENCRYPTION_KEY` in container env**, not a bad deploy token |
| `the relay rejected the auth token` | Auth header sent but worker secret mismatch — **redeploy relay** from OmniRoute UI |
| `Relay returned HTTP 500` | Worker error — use **decision tree** below (dashboard test hits public ipify, not LAN) |
| `curl` to relay root → **401** | Normal without `x-relay-auth`; proves worker is alive |
| Vercel: `resolveRelayTarget is not defined` | **Upstream** generated `api/relay.js` bug — see `references/vercel-relay-resolveRelayTarget-6149.md` |

Log source: `/app/logs/application/app.log` — component `ProxyTest`.

## Built-in proxy test headers

Dashboard **Test** calls the edge worker with:

- `x-relay-auth` — from decrypted `relayAuthEnc`
- `x-relay-target`: `https://api64.ipify.org`
- `x-relay-path`: `/?format=json`

**500 with Vercel “No outgoing requests”** = worker crashed before fetch (often upstream JS bug), not unreachable `192.168.0.222`.

## Decision tree

| Stage | Result | Meaning |
|-------|--------|---------|
| No auth | 401 | Worker up |
| Auth only | 400 `missing x-relay-target` | Secret OK |
| Full test | 500 | Check Vercel/Deno logs; `ReferenceError` → upstream issue #6149 |
| `KEY_MISSING` in container | — | Add `env_file: ./data/server.env`, recreate |

Decrypt verify: `scryptSync(STORAGE_ENCRYPTION_KEY, "omniroute-field-encryption-v1", 32)`, `enc:v1:` format `iv:ciphertext:authTag`. Run `scripts/probe-edge-relay.sh`.

## Diagnosis (on DietPi host)

```bash
# 1) Key in process env?
docker exec omniroute sh -lc 'test -n "$STORAGE_ENCRYPTION_KEY" && echo KEY_OK || echo KEY_MISSING'

# 2) Key on disk?
test -f /mnt/tb/1Apps/omniroute/data/server.env && echo server.env_exists

# 3) Relays registered?
python3 - <<'PY'
import sqlite3, json
conn = sqlite3.connect("/mnt/tb/1Apps/omniroute/data/storage.sqlite")
for row in conn.execute("select name, type, host, notes from proxy_registry"):
    n = json.loads(row[3] or "{}")
    print(row[0], row[1], row[2], "relayAuthEnc" in n)
PY

# 4) Recent proxy tests
docker exec omniroute tail -20 /app/logs/application/app.log | grep ProxyTest
```

`/api/settings/proxy/test` requires dashboard auth (`AUTH_001` from anonymous curl).

## Fix: compose `env_file`

```yaml
services:
  omniroute:
    env_file:
      - ./data/server.env
```

Recreate container, verify `KEY_OK`, re-test in dashboard.

## 9router vs OmniRoute relay

| | 9router | OmniRoute relay pool |
|---|---------|----------------------|
| Runs | On host (`20111`) | On Vercel/Deno/CF edge |
| Same Vercel API token | Deploy only | Deploy + **encrypted relay secret** in SQLite |
| LAN origin | Works locally | **Fails** on edge unless origin is public (Cloudflare Tunnel hostname) |

## Hermes / local routing

Use `http://127.0.0.1:20128` for OmniRoute on the same host — not the relay URL. Use tunnel hostnames only for remote clients or as **public origin** for relay upstream.

## Cloudflare relay deploy failure

Separate from 401: upload may fail with `Content-Type must be one of: application/javascript...` — OmniRoute → Cloudflare API mismatch; retry deploy or skip CF relay until upstream fixes.