# 9router proxy-pool false 503 on Cloudflare relay

## Trigger
9router UI/DB showed the active Cloudflare proxy pool as failed:
- `testStatus = error`
- `lastError = "Proxy test failed with status 503"`

But live routed traffic and direct relay probes were still succeeding.

## Root cause
The 9router proxy-pool test endpoint uses a different request shape than normal relay traffic.

Bundled endpoint:
- `/api/proxy-pools/[id]/test`

For `cloudflare`, `vercel`, and `deno` pools it sends:
- `GET <relay-url>`
- `x-relay-target: https://httpbin.org`
- `x-relay-path: /get`

Then it persists:
- `testStatus`
- `lastTestedAt`
- `lastError = d.error || "Proxy test failed with status ${d.status}"`

## Verified behavior
### Active Cloudflare pool
- relay: `https://9router-cf-desibotz.cf1-567.workers.dev`
- exact 9router test shape (`httpbin.org/get`) -> **503**
- real-world relay shape (`api64.ipify.org/?format=json`) -> **200** with JSON IP

### Comparison relays
- older Cloudflare relay `cloudflare-relay-mdhrsagar...workers.dev` with same `httpbin.org/get` test -> **200**
- Vercel relay with same `httpbin.org/get` test -> **200**

## Operational conclusion
A red proxy-pool status in 9router is not enough to conclude the relay is dead.

If the pool type is `cloudflare`/`vercel`/`deno`:
1. reproduce the exact `/api/proxy-pools/[id]/test` request shape
2. separately probe the relay with a real traffic target such as `https://api64.ipify.org/?format=json`
3. check live app logs for successful proxied requests

If `httpbin.org/get` fails but real traffic passes, treat it as a **tester/target mismatch**, not a relay outage.

## Better test target
Prefer a simpler upstream for relay verification, e.g.:
- `x-relay-target: https://api64.ipify.org`
- `x-relay-path: /?format=json`

This better matches the successful live-path checks used during debugging.
