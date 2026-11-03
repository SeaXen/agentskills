---
name: 9router-self-hosted
description: Operate and contribute to decolua/9router on self-hosted Docker (host network, SQLite data). Covers timezone, Usage & Analytics periods, built-in tunnel port pitfalls, and upstream PR workflow.
---

# 9Router (self-hosted)

Local deployment pattern on TB/DietPi: **`/mnt/tb/1Apps/9router`**, image `decolua/9router:latest`, **`PORT: "20111"`**, `network_mode: host`, data at `./data`.

Hermes / LAN API base: **`http://127.0.0.1:20111/v1`** (fastest on same host).

## Proper update (upstream image)

```bash
/mnt/tb/1Apps/9router/update.sh
python3 /mnt/tb/1Apps/9router/patches/apply-usage-periods.py   # until PR #2361 merges
```

`update.sh`: backup `data/` + compose → `backups/<timestamp>/`, `docker pull`, recreate with host network + `PORT=20111` + `TZ=Asia/Dhaka`, wait for `/api/health`.

**Hermes pitfall:** foreground `docker compose up -d` may be blocked; `update.sh` uses equivalent `docker run`.

**Verify:** `docker inspect 9router --format '{{index .Config.Labels "org.opencontainers.image.revision"}}'`

Usage table sorting vs period PR: `references/usage-table-sorting-upstream.md`.

## Timezone (Asia/Dhaka)

Node/UI timestamps follow container `TZ`. Add to compose `environment`:

```yaml
TZ: Asia/Dhaka
```

Recreate container after change. `date` in shell may still show UTC if image lacks `tzdata`; **Node** `Intl.DateTimeFormat().resolvedOptions().timeZone` is the check that matters.

## Usage & Analytics periods

Stock UI caps at **60D**. Extended periods (**90D, 180D, 365D, All**) require source changes — see upstream PR **https://github.com/decolua/9router/pull/2361** (`src/lib/usagePeriods.js` centralizes UI + API + `usageRepo.js`).

**Until merged:** ephemeral in-container patch on running image (lost on pull/recreate):

```bash
python3 /mnt/tb/1Apps/9router/patches/apply-usage-periods.py
```

The local patcher dynamically discovers hashed Next.js usage bundles. Do not hard-code the bundle filename: upstream image updates change it and otherwise leave the browser UI at 60D even if server chunks are patched. Hard-refresh `/dashboard/usage` after apply.

## Built-in tunnel vs compose port

Tunnel enable flow may health-check **20128** while compose sets **20111** → 60s timeout. Prefer **external Cloudflare Tunnel** to `http://192.168.0.222:20111` (or `127.0.0.1:20111` if cloudflared is co-located). Do not point tunnel at `/v1` only — origin is app **root**.

## Proxy-pool relays (Cloudflare / Vercel / Deno)

9router's proxy pools mask your real IP from AI providers by forwarding requests through edge relay workers. Config lives in the `proxyPools` SQLite table.

**Deployed relays** (from `proxyPools`):

| Relay | URL | Type | Status |
|-------|-----|------|--------|
| cloudflare-relay-mdhrsagar | `https://cloudflare-relay-mdhrsagar.md-hrsagar.workers.dev` | cloudflare | ✅ active |
| vercel-relay | `https://vercel-relay-ioncaav1z-searex.vercel.app` | vercel | ✅ active |
| ~~Deno~~ | ~~`https://9router-hrsea7.hrsea7.deno.net`~~ | deno | ❌ **SUSPENDED 2026-07-07** (see `references/proxy-relay-platform-ban-risk.md`) |

### Relay latency benchmarks (measured from DietPi host, Jul 2026)

**Endpoint ping (TCP/TLS only, no API call):**

| Relay | Avg Connect | Avg TTFB | Cold start |
|-------|-----------|---------|-------------|
| Direct Bynara | ~10ms | ~350ms | No |
| **Cloudflare** | ~11ms | **~46ms** (warm) | No ✅ |
| Deno | ~168ms | **~510ms** | Yes ❌ |
| Vercel | ~15ms | **~617ms** (cold) / **~184ms** (warm) | Yes ❌ |

**Full API call (bynara/mistral-medium-3-5 via OmniRoute + relay, streaming ON):**

| Metric | Range | Avg |
|--------|-------|-----|
| TTFB (first token) | 1.35–2.02s | ~1.75s |
| Total response | 1.52–4.16s | ~2.40s |
| Relay hop overhead (OmniRoute `x-omniroute-latency-ms`) | 156–245ms | ~191ms |
| Bynara model processing (estimated) | 1.3–1.8s | — |
| **Relay overhead % of total** | — | **~10–15%** |

**Key findings:**
- Cloudflare relay = fastest hop (~46ms), no cold start. Use as primary.
- Deno = moderate (~510ms), cold starts. Use as backup.
- Vercel = worst cold start (~1.5s first hit, ~184ms warm). Use only for IP diversity.
- Streaming ON vs OFF: streaming TTFB ~1.75s vs non-streaming ~6–7s. Always enable streaming.
- AI provider processing time (1.3–1.8s) dwarfs relay overhead (~190ms).
- OmniRoute reports relay hop latency in `x-omniroute-latency-ms` response header.

### Testing relay latency

```bash
# Quick endpoint ping (no API key needed)
for i in 1 2 3; do
  curl -s -o /dev/null -w "TTFB: %{time_starttransfer}s | TOTAL: %{time_total}s\n" \
    https://cloudflare-relay-mdhrsagar.md-hrsagar.workers.dev/
done

# Full API call with timing (via OmniRoute)
curl -s -w "\nTTFB: %{time_starttransfer}s | TOTAL: %{time_total}s\n" \
  http://192.168.0.222:20128/v1/chat/completions \
  -H "Authorization: Bearer <omniroute-key>" \
  -H "Content-Type: application/json" \
  -d '{"model":"bynara/mistral-medium-3-5","messages":[{"role":"user","content":"Say hello"}],"max_tokens":20,"stream":true}'
```

### Multi-account risk — relay platform vs upstream LLM provider

**Risk on the relay platform (CF/Vercel):**
- 1–2 extra accounts per platform: low risk.
- 5–10 accounts: medium risk (pattern detection).
- 10+ accounts: high risk (almost certainly flagged).
- Same GitHub OAuth / email domain / credit card across accounts = instant link → all banned.

**Risk on the upstream LLM provider (Anthropic/OpenAI/Antigravity/Codex):**
This is the **higher** risk and easy to miss. Upstream providers detect proxy-style usage patterns and return `403 violation of Terms of Service` — they can ban your account outright. See [9router issue #365](https://github.com/decolua/9router/issues/365) and [#375](https://github.com/decolua/9router/issues/375).
- They care about: request volume per key, request rate, user-agent fingerprint consistency, IP diversity pattern, geo-from-key mismatch.
- 9router's `x-relay-target` headers + rotating accounts *can* trigger TOS heuristics. Not "if" but "when" if you scale.
- Mitigation: rotate API keys, keep usage per key under soft personal limits, prefer provider-allowed SDK usage over raw proxy forwarding where possible.
- AI providers are more likely to ban **API keys/accounts** for TOS patterns than relay platforms are to ban for traffic volume.

### Platform ban risk — Cloudflare & Vercel vs Deno

See `references/proxy-relay-platform-ban-risk.md` for full sourced analysis. Summary:

| Platform | LLM-proxy TOS risk | What happens if you trip it |
|---|---|---|
| **Cloudflare Workers** | 🟢 Near-zero — they sell Workers AI + AI Gateway | Throttled at 100k req/day, then invoiced on Paid plan ($5/mo). Not banned. |
| **Vercel Functions** | 🟢 Near-zero — they sell AI SDK + LiteLLM host | Throttled, asked to upgrade to Pro ($20/mo), or invoiced. Hobby = non-commercial only. |
| **Deno Deploy** | ❌ **High — no AI product, no revenue incentive** | `503 SUSPENDED` (final, no appeal). Caps return 429, payment returns 402, SUSPENDED = policy. |
| **Upstream Anthropic/OpenAI** | ⚠️ **Higher than any relay platform** | `403 violation of Terms of Service` — can ban your account/keys for proxy usage patterns. See 9router issue #365. |

**Do not deploy a 9router proxy pool on Deno Deploy.** The Deno relay hrsea7 was permanently suspended 2026-07-07. Use Cloudflare Workers (primary) + Vercel (secondary). For a 3rd fallback, prefer a paid $1–5/mo VPS (Railway, Fly.io) where there's no LLM-proxy stigma.

### ⚠️ PITFALL: relay-watchdog silently green when relay is suspended

The bash watchdog (`/root/.hermes/scripts/relay-watchdog.sh`, cron `e94d76abd485`) used to treat *any* HTTP response code as alive. That meant **Deno's `503 SUSPENDED` was masked as healthy** for hours/days before manual discovery.

**Symptoms:**
- Watchdog never alerts
- Actual API calls through 9router fail with 5xx
- User only finds out when OmniRoute/Claude Code/Cursor errors hit

**Fix (already applied):** the script now treats any `5xx` response as `❌ SUSPENDED | HTTP 503 (likely account/project suspension)` and alerts immediately. 2xx/3xx/4xx are still considered alive (4xx is normal — `400 Missing x-relay-target header` is the expected bare-req fingerprint).

**Rule for any future relay monitor:** bare `GET /` returning `4xx` = alive. Bare `GET /` returning `5xx` = **the relay platform just killed your app, alert now**. Never treat 5xx as "up but erroring".

### Querying proxy pool config from SQLite

```bash
sqlite3 /mnt/tb/1Apps/9router/data/db/data.sqlite "SELECT * FROM proxyPools;"
```

Each row: `id | priority | status | config_json | created_at | updated_at`. The `config_json` contains `name`, `proxyUrl`, `type` (cloudflare/vercel/deno), `strictProxy`, `lastTestedAt`, `lastError`.

## Routing Strategy (Profile) vs OmniRoute

9router **Profile → Routing Strategy** is where users expect **account Round Robin**, **Sticky Limit**, **Combo Round Robin**, and **Combo Sticky Limit** (`comboStickyRoundRobinLimit`, default 1). Per-provider overrides: **Providers → Connections** (`providerStrategies`).

OmniRoute equivalent (after upstream **PR #6678**): **Settings → Routing** (top card) + provider detail for multi-account overrides. Before that PR, users report sticky RR "not in settings" because knobs lived under combo defaults.

Cross-gateway map: skill `omniroute-system` → `references/9router-sticky-round-robin-parity.md`. Do not confuse 9router **account** RR with OmniRoute combo-step Round Robin (1 step + RR does not rotate accounts — see `devops/omniroute` Combos).

## Upstream contributions

Fork **`decolua/9router`**, default branch **`master`** (not `main`). Tests from repo root:

```bash
npx vitest run --config tests/vitest.config.js tests/unit/<file>.test.js
```

(`tests/package.json` may expect `/tmp/node_modules`; repo-root `npx vitest` is reliable.)

See `references/usage-analytics-extended-periods.md`, `references/usage-table-sorting-upstream.md`, `references/proxy-relay-latency-benchmarks.md`, `references/proxy-relay-platform-ban-risk.md`, and **`references/update-sh-script.md`** (the canonical update.sh reference). OmniRoute sticky RR parity: `omniroute-system` → `references/9router-sticky-round-robin-parity.md`. For upstream PR workflow see `github-operations` → `references/contributing-to-third-party-repos.md`.

## Session / login lifetime (read from compiled bundle)

9router's login session is **much shorter** than OmniRoute's:

- **JWT lifetime:** 24 hours (not 30 days like OmniRoute)
- **No auto-refresh middleware** — `auth_token` simply expires after 24h
- **Cookie has no `maxAge`** → browser session cookie (dies when browser closes)
- **Brute-force lockout is harsh:** 5 wrong passwords → escalating lockout `[5min, 20min, 1h, 5h]`

**Source evidence** — found at `/app/.next/server/chunks/8658.js` (module `33792` exports):
```js
async function q(a={}){
  return new d.P({authenticated:!0,...a})
    .setProtectedHeader({alg:"HS256"})
    .setIssuedAt()
    .setExpirationTime("24h")     // ← 24 hours, NOT 30 days
    .sign(o);
}
async function t(a,b,c={}){
  let d=await q(c);
  a.set("auth_token",d,{
    httpOnly:!0,
    secure:p(b),
    sameSite:"lax",
    path:"/"                      // ← no maxAge → session cookie
  });
}
```

**Fast-logout on 9router is normal/expected**, not a bug. Two real reasons you'll see it:
1. Browser session cookie dies on browser close
2. 24h hard expiry, no rolling refresh

**Mitigations:**
- Keep browser/tab open if you want to stay logged in past 24h
- For OmniRoute-style 30-day rolling sessions, point Hermes at OmniRoute instead (`custom:omniroute` provider, `base_url: http://192.168.0.222:20128/v1`)
- Avoid wrong passwords — lockout escalates to 5h