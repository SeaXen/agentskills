# OmniRoute Vercel relay — `resolveRelayTarget` undefined (July 2026)

## Symptom

- Proxy pool → deploy Vercel relay → **Test** → `✗ Relay returned HTTP 500`
- Log: `[ProxyTest] relay <host>: Relay returned HTTP 500`
- Vercel function log:
  ```
  ReferenceError: resolveRelayTarget is not defined
      at (api/relay.js:98:19)
  ```
- Vercel invocation: **External APIs: No outgoing requests** (crash before fetch)

## Ruled out (operator)

- Vercel deploy token valid (new `*.vercel.app` URL created)
- `STORAGE_ENCRYPTION_KEY` loaded via `env_file: ./data/server.env`
- `relayAuthEnc` decrypts; `x-relay-auth` only → **400** `missing x-relay-target` (not 401)
- Fresh redeploy new hostname → still 500

## Upstream issue

**https://github.com/diegosouzapw/OmniRoute/issues/6149**

Image area: `diegosouzapw/omniroute:latest` (~v3.8.42). Generated worker references `resolveRelayTarget` without defining/importing it.

## Workaround

- Do **not** use OmniRoute Vercel/Deno relay pool until fixed.
- Local API: `http://127.0.0.1:20128/v1`
- Public: user's **Cloudflare Tunnel** → origin `http://127.0.0.1:20128` (not relay worker).

## Local issue draft

`/mnt/tb/1Apps/omniroute/ISSUE-vercel-relay-resolveRelayTarget.md` (used to file #6149).