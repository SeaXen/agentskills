# OmniRoute Relay Fix — v3.8.45 / PR #6149 / PR #6202

## Issue
Vercel, Deno, and Cloudflare relay deployments from OmniRoute Dashboard → System → Proxy Pool fail:
- **Vercel/Deno**: Deploy succeeds, but **Proxy Test** returns **HTTP 500** with `ReferenceError: resolveRelayTarget is not defined` at `api/relay.js:98`
- **Cloudflare**: Deploy **fails** with `Cloudflare Worker upload failed: Content-Type must be one of: application/javascript, text/javascript, multipart/form-data`

## Root Cause (Vercel/Deno)
The relay worker generator embedded the shared `resolveRelayTarget` SSRF guard as a bare `${fn.toString()}` declaration, while the worker body called the hardcoded literal name `resolveRelayTarget`. SWC minification mangled the source function's name, so the deployed worker defined `<mangled>` but still called `resolveRelayTarget` → `ReferenceError`.

## Fix in v3.8.45 (PR #6202)
Both Vercel and Deno relay templates now emit:
```js
const resolveRelayTarget = ${fn.toString()};
```
The `const` name is a template literal, immune to minification. This ensures the function name survives SWC and the worker can resolve the target correctly.

Regression guard: `tests/unit/relay-minified-fn-6149.test.ts` (4 tests).

## Cloudflare Relay Status
The changelog **does not mention** the Cloudflare `Content-Type` upload error. That issue remains **unfixed** in v3.8.45.

## Verification Steps
1. Pull the fixed image:
   ```bash
   docker pull diegosouzapw/omniroute:v3.8.45
   ```
2. Recreate container:
   ```bash
   docker compose down && docker compose up -d
   ```
3. Redeploy Vercel/Deno relays from OmniRoute UI → System → Proxy Pool.
4. Run **Proxy Test** — should now pass (no 500).
5. Cloudflare relay: still expect deploy failure until a separate fix lands.

## Workaround (until v3.8.45+ is running)
- Skip built-in relay deploy.
- Use direct origin (`http://127.0.0.1:20128/v1`) or external Cloudflare Tunnel (`9router.xuup.top` or similar).
- For public access, point OmniRoute providers to a **public origin** (tunnel hostname), not a private LAN IP.

## References
- Issue: [diegosouzapw/OmniRoute#6149](https://github.com/diegosouzapw/OmniRoute/issues/6149)
- PR (fix): [diegosouzapw/OmniRoute#6202](https://github.com/diegosouzapw/OmniRoute/pull/6202)
- Release: v3.8.45 — 2026-07-06
