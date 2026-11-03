# Next.js + React Audit Gotchas

A condensed catalog of bugs that escape `tsc --noEmit`, unit tests, and even production build — but that live HTTP probes catch. Distilled from real audit cycles on a self-hosted Next.js trading dashboard. Use this when running the 7-phase live audit (Step 9 of `requesting-code-review`).

---

## 1. `JSON.stringify(NextResponse)` returns `"{}"`

**Symptom:** An API route returns HTTP 200 with `Content-Type: application/json` and a body of `{}`. Every consumer sees empty data.

**Root cause:** `safe()` returns a `NextResponse` object. Calling `JSON.stringify(NextResponse)` invokes NextResponse's toJSON-less prototype and yields `{}`.

**Anti-pattern:**
```ts
const result = await safe(async () => { ... });
return new Response(JSON.stringify(result), {
  status: result.ok ? 200 : 500,           // result.ok is undefined — always 500
  headers: { "Content-Type": "application/json" },
});
```

**Fix:** Mutate headers on the response object, don't rewrap it.
```ts
const response = await safe(async () => { ... });
response.headers.set("Content-Type", "application/json");
response.headers.set("Cache-Control", "public, max-age=5");
return response;
```

**How to detect during audit:**
```bash
# Hit every endpoint and grep for empty JSON bodies
for path in /api/health /api/market?symbol=BTCUSDT /api/scanner /api/positions; do
  body=$(curl -s "http://host$path")
  if [ "$body" = "{}" ] || [ "$body" = "[]" ]; then
    echo "EMPTY BODY: $path"
  fi
done
```

---

## 2. Status code: DELETE missing resource → 404, not 400

**Symptom:** `DELETE /api/rules/[id]` for a non-existent id returns 400 with `{ error: "rule not found" }`.

**Root cause:** Helper function uses `fail("not found")` which defaults to status 400.

**Convention:**
- **400 Bad Request** → the request itself is malformed (missing field, bad JSON, invalid enum value).
- **404 Not Found** → the request is well-formed but refers to a resource that doesn't exist.
- **409 Conflict** → the request is valid but conflicts with current state (already deleted, duplicate key).

**Anti-pattern:**
```ts
const r = deleteRule(id);
if (!r) return fail("rule not found");   // 400
```

**Fix:**
```ts
const r = deleteRule(id);
if (!r) return fail("rule not found", 404);
```

**How to detect during audit:**
```bash
# Hit DELETE/PATCH endpoints with obviously-bad ids
curl -s -o /dev/null -w "%{http_code}\n" -X DELETE http://host/api/rules/DOESNOTEXIST
# Expected: 404. If 400, the route is using fail() without an explicit status.
```

---

## 3. Stored XSS via user-provided URL in `href` / `src`

**Symptom:** A form accepts a URL field. After save, the rendered HTML contains `href="javascript:alert(1)"` or `src="data:text/html,…"`. Clicking executes attacker JS in the user's session.

**Anti-pattern:**
```tsx
<a href={userInput}>view</a>
<img src={userUrl} />
```

**Fix — whitelist `https?://` only:**
```tsx
const url = userInput?.trim() ?? "";
const safe = /^https?:\/\//i.test(url) ? url : null;
return safe ? <a href={safe} target="_blank" rel="noreferrer noopener">view</a> : null;
```

**Why sanitize at render, not at input:** Storing the raw value preserves data fidelity (the user might fix a typo later, or paste a relative path that's valid in some other context). Sanitize at every render boundary — don't trust any user-controlled string going into `href`, `src`, `action`, `formAction`, `srcdoc`, or any attribute that can fetch/execute.

**How to detect during audit:**
```bash
# Insert a known-malicious URL into the system via POST
curl -X POST http://host/api/journal \
  -H "Content-Type: application/json" \
  -d '{"title":"xss probe","body":"x","screenshot":"javascript:alert(1)"}'

# Fetch the rendered page and grep for any surviving dangerous scheme
curl -s http://host/journal | grep -E 'href="(javascript|data:text/html)' && echo "XSS PRESENT"
```

---

## 4. Background worker defined but never started

**Symptom:** Engine exists for trailing stops / breakeven / alert polling / scheduled sync. Code path exists, tests cover the math. At runtime, none of it fires.

**Anti-pattern:**
```ts
// lib/crypto/position-manager.ts
export function startPositionManager(intervalMs = 5000) {
  setInterval(() => tick().catch(() => {}), intervalMs);
}

// lib/crypto/boot.ts  — boot chain never calls startPositionManager
export function ensureStarted() {
  startScheduler();   // only this
}
```

**Fix:** Audit `boot.ts` (or equivalent service entry) and verify every exported `start*` function is wired.
```bash
# Find every start* export
grep -rn "^export function start" lib/

# Verify each is called from boot
grep "startScheduler\|startPositionManager\|startAlertPolling\|startDcaBotEngine\|startGridBotEngine" lib/crypto/boot.ts
```

If a `start*` is exported but not invoked, treat it as **dead code at runtime**, not "available infrastructure".

---

## 5. Env-gated loop that nobody turned on

**Symptom:** A periodic loop is defined and started, but inside the start function there's an early-return gate keyed on an env var that's never set.

**Anti-pattern:**
```ts
export function startAlertPolling(intervalMs = 60_000) {
  if (process.env.ALERT_AUTOPOLL !== "1") return;   // silent no-op
  setInterval(() => checkAlerts(), intervalMs);
}
```

The developer meant this as a debug toggle ("off by default"), but it shipped with the env var unset, so the loop never fires.

**Fix:** Remove the env gate (or invert: turn it into an opt-out: `if (process.env.ALERT_AUTOPOLL === "0") return`).

**How to detect during audit:**
```bash
# Find every process.env gate inside start* functions
grep -rn "process\.env\." lib/ | grep -v ".test\." | head

# For each gate, verify the env var is set somewhere in deploy config
grep -rn "ALERT_AUTOPOLL" docker-compose.yml Dockerfile .env* 2>/dev/null
# If only the source mentions it and deploy doesn't, the gate is silently disabling the feature.
```

---

## 6. Inverted loading-state ternary after `useEffect` → `useAutoRefresh` refactor

**Symptom:** After migrating a page from `useEffect(() => load(), [])` to a shared `useAutoRefresh(load, N)` hook, the empty state permanently shows on the steady state, and rows only appear during the brief refresh moment.

**Anti-pattern:**
```tsx
const ar = useAutoRefresh(loadData, 60_000);

// Bug: shows "No entries" when NOT loading, only shows entries while loading.
{busy ? <Loading/> : entries.length === 0 ? <Empty/> : <List entries={entries}/>}
```

**Fix — explicit 3-state:**
```tsx
{busy && entries.length === 0 ? <Loading/> :
 !busy && entries.length === 0 ? <Empty/> :
 <List entries={entries}/>}
```

**Why this happens:** The old `useEffect` pattern sets `loading=true` only during the initial fetch and `loading=false` after. The new `useAutoRefresh` pattern sets `busy=true` on every refresh, including the auto-refresh ticks that happen *after* data is loaded. So the ternary's "busy ? Loading : List" branch fires whenever the auto-refresh starts, hiding the list briefly each time.

---

## 7. AdvancedOrderUpdate type drift — fields that aren't there

**Symptom:** `tsc` error: `Object literal may only specify known properties, and 'side' does not exist in type 'AdvancedOrderUpdate'`.

**Root cause:** The `AdvancedOrderUpdate` config type only carries the *trailing/TP/SL parameters*, not the position identity. Position identity (side, entryPrice, size, exchangeId, symbol) lives in the ManagedState wrapper that holds the config.

```ts
// Correct: identity lives on the wrapper, only TP/SL/trailing live in config
managePosition({
  exchangeId, symbol, side, entryPrice, size, marketType,  // identity
  config: {
    symbol,                                              // just for logging
    trailingPct, trailingDistance,
    breakevenTrigger,
    partialQty: [50], tp: [2.0],                         // arrays, not "partials"
    finalStop,
  },
});
```

Common mistakes to avoid:
- `side` in config (it's on the wrapper)
- `entryPrice`/`size` in config (it's on the wrapper)
- `trailing: true` boolean (config uses `trailingPct` or `trailingDistance` directly)
- `partials: [{pct, pnlPct}]` (config uses parallel arrays `partialQty` and `tp`)

---

## 8. `useAutoRefresh` refactor leaves stale `load` reference

**Symptom:** Page filters by `range` query param. After switching range, the page shows the old data because the auto-refresh closure captured the initial `range`.

**Root cause:** The `useAutoRefresh(fn)` hook uses `fnRef.current = fn` on each render so the latest closure is always used — but the **interval timer fires on its own schedule**, not when `range` changes. So switching `range` doesn't trigger a fetch until the next tick (could be up to `intervalMs` later).

**Fix:** Trigger an immediate refresh when the dependency changes.
```tsx
const ar = useAutoRefresh(loadData, 120_000);
useEffect(() => { ar.refresh(); }, [range]);
```

Or use the hook's `tick` value as a `useEffect` dep so derived state recomputes on every refresh:
```tsx
const filtered = useMemo(() => ..., [data, range, ar.tick]);
```

---

## 9. "Build passes" ≠ "Works in production"

**Symptom:** `npm run build` exits 0. App boots. But `/api/market` returns `{}`, `/api/scanners?kind=funding` returns the wrong shape, the trade page errors on submit.

**Root cause:** Build only proves compilation and SSR rendering. It does not exercise:
- Runtime API integrations (Bybit public endpoints, RPC fallbacks, OAuth dance)
- Status code paths (4xx, 5xx branches never built)
- Real DOM hydration (server-rendered HTML may differ from client expectations)
- Cross-route behavior (auth, shared DB connections)

**How to detect:** Add a smoke-test script that hits every API + every page after each build. If the script doesn't exist, the deploy claim is just "it compiled" — not "it works".

---

## Quick audit checklist (use after every "10/10" claim)

```bash
# 1. tsc clean
npx tsc --noEmit

# 2. tests pass
npm test --silent

# 3. build clean
rm -rf .next && npm run build 2>&1 | tail -5

# 4. live API probes (no empty {} bodies)
for path in /api/health /api/scanner /api/scanners?kind=funding /api/alerts /api/positions /api/market?symbol=BTCUSDT; do
  body=$(curl -s "http://host$path" | head -c 200)
  echo "$body" | grep -qE '^\{?\s*\}?$|^$' && echo "EMPTY: $path"
done

# 5. live page probes (no 500s)
for p in / /scanner /dca /grid /alerts /wallets /journal /rules /positions /orders; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "http://host$p")
  [ "$code" != "200" ] && echo "BAD $code: $p"
done

# 6. container logs (no crash on boot)
docker logs <container> --tail 30 | grep -iE "error|cannot|undefined" && echo "CHECK LOGS"

# 7. security — XSS probe (insert malicious URL via POST, fetch rendered page)
curl -s -X POST http://host/api/journal -H "Content-Type: application/json" \
  -d '{"title":"xss probe","screenshot":"javascript:alert(1)"}'
curl -s http://host/journal | grep -E 'href="(javascript|data:text/html)' && echo "XSS PRESENT"
```

If any of the 7 phases fails, do not write "fixed" or "X/10". Fix the failure, re-run the phase, then re-run the full audit.