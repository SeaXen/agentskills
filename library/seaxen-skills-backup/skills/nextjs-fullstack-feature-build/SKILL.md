---
name: nextjs-fullstack-feature-build
description: Build multiple fullstack features in a single session for an existing Next.js (App Router) app with API routes, server pages, and a database layer. Use when the user asks for several features at once ("add X, Y, Z", "build me these 5 things", "ship all of these") on an existing Next.js codebase that already has adapters, a db layer, and a UI component library. Covers the parallel build pattern, per-feature verification, and the recurring pitfalls (JSX patch breakage, file-naming collisions, route file rules, docker terminal blocking).
---

# Fullstack Feature Build (Next.js App Router)

When the user asks for **multiple features at once** on an existing Next.js fullstack project, use this pattern. It was validated by building 8 features in one session for TradingX (a crypto trading dashboard) — 8 features, ~2200 lines, 26 files, one commit, one push, all verified live.

## When to use

- User asks for a list of features: "add X, Y, Z"
- User says "build me these N things" or "add the top N quick wins"
- You're extending an existing Next.js + DB + adapter codebase (not a fresh project)
- The features are independent enough to build in parallel

## The Pattern

### 1. Survey the codebase FIRST (10 min that saves an hour)

Before writing any code, run a quick audit:

```bash
# Find existing files of each type you'll be creating
find app/api -name "route.ts" | head -20
find lib/crypto -name "*.ts" | head -20
ls app/
```

Specifically look for:
- **Naming conventions** — kebab-case (`filter-presets.ts`) vs camelCase (`filterPresets.ts`) vs PascalCase. Match the existing style. Don't create duplicates.
- **Helper patterns** — is there already a `useFilterPresets()`, `useAutoRefresh()`, `lib/crypto/X.ts`? Reuse, don't reinvent.
- **Existing endpoints** — the data you need may already be at `/api/X` (e.g. TradingX had `/api/portfolios/combined` that was unused; the new UI just called it).
- **Page patterns** — how are existing pages structured? Header → filters → table? RefreshBar in the corner? Match the convention.

### 2. Enumerate and prioritize

Group features by effort:
- **Quick wins** (2-4h each, single file or small surface): these can be built in parallel without blocking
- **Medium** (4-8h, multi-file): build these next
- **Bigger** (1+ days): flag for next session unless trivial

If the user gave a list, rank by ROI (user impact / effort). Surface the ranked list back to them before starting so they can correct course.

### 3. Build in parallel batches, NOT one-feature-at-a-time

For each feature, the work is:
1. **API route** at `app/api/X/route.ts` (or extend an existing one)
2. **Lib helpers** at `lib/X.ts` (any complex logic)
3. **Page** at `app/X/page.tsx` (or extend an existing page)
4. **Wire-up**: hooks, state, RefreshBar

Build them as 2-3 features in flight at a time. Don't finish A before starting B. Use parallel `write_file` and `patch` calls.

### 4. Per-feature verification, then bundle

Don't run `tsc` after every feature — that wastes time. Build all features, then run the full verification chain ONCE:

```bash
npx tsc --noEmit          # 0 errors required
npm test                  # 66/66 pass required
npm run build             # clean, all pages compile
docker compose build --no-cache tradingx   # rebuild image
docker compose up -d --force-recreate      # deploy
curl -s -o /dev/null -w "%{http_code}\n" "http://host:port/X"  # each new endpoint
```

This is the "10/10 across features + design + performance" pattern: breadth + polish + perf in one pass. NOT iterative MVP-then-add.

### 5. Single bundle commit, single push

Group the related features into ONE commit. Multiple small commits for related features fragment the history and make rollback harder. The commit message should be a structured list of what was added.

```bash
git add -A
git commit -m "feat: 8 new features — ratios, key audit, coingecko, calendar, presets, combined P&L, news, PWA

1. Sharpe / Sortino / Calmar ratios in /api/analytics/summary...
2. API key permission audit (/api/exchanges/audit)...
3. CoinGecko trending + market cap...
4. ...
"
git push origin main
```

### 6. Honest summary

After pushing, list:
- What was added (file count, feature count)
- What was verified (test results, build status, live endpoint checks)
- What is still missing or needs follow-up (be specific, don't claim 10/10)

## Pitfalls (see references/pitfalls.md for full detail)

1. **JSX patch breakage** — when patching deeply nested JSX, multi-line `old_string` patterns can match unexpected locations, leaving dangling tags that won't compile. After any JSX patch, re-read the file or run `tsc --noEmit` to verify. If patches are getting complex, **rewrite the whole file with `write_file`** instead of layering patches.

2. **File-naming collisions** — `find lib/ -name "*.ts"` before creating new files. The same concept can have a kebab-case AND camelCase file (e.g. `filter-presets.ts` and `filterPresets.ts`) — only one will be imported.

3. **Docker terminal blocking** — `docker compose up -d --force-recreate` triggers the "long-running process" detector. Use `terminal(background=true)` and `process(action='wait')` instead, or pipe to a log file.

4. **Next.js route file rules** — only specific exports are allowed in `app/api/X/route.ts` (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`, etc.). Helper functions like `getNews()`, `computeRatios()` MUST live in `/lib` and be imported.

5. **LSP diagnostics vs tsc** — LSP diagnostics can show stale errors from prior reads. Trust `tsc --noEmit` over LSP for ground truth.

6. **Pre-existing type errors** — if `tsc` shows an error in a file you didn't touch, fix it with a minimal `![]` non-null assertion or a 1-line guard. Don't refactor.

7. **Helper functions in route files** — even typescript-only helpers break the Next.js route export contract. Move to `/lib` immediately.

8. **build / dynamic functions** — server pages and pages with `useEffect` need `"use client"` at the top. Missing it causes silent SSR issues.

## Workflow

```
1. Survey   → 2. Plan & rank → 3. Build (parallel) → 4. Verify (tsc, test, build) → 5. Deploy (docker) → 6. Live-verify (curl) → 7. Commit → 8. Push → 9. Honest summary
```

The whole flow for 8 small features should take one session. For larger features, break the bundle into 2-3 sessions.

## Full-app audit scorecard (run before claiming "10/10")

When the user asks "is my app 10/10?" or "check for any more bug", run a **9-category audit** with real shell probes, not vibes:

| Category | What to check | Shell probe |
|----------|--------------|-------------|
| Feature breadth | Page count, API count, adapter count | `find app -name 'page.tsx' \| wc -l` |
| Code quality | Type errors, TODOs, console.logs, ESLint | `npx tsc --noEmit \| grep 'error TS' \| wc -l` |
| Security | Auth gate, CVE patches, rate limiting, SQL injection | `grep -r 'AUTH_TOKEN' middleware.ts`, `npm audit` |
| Performance | Container CPU/RAM, page load time, bundle size | `docker stats --no-stream`, `curl -w '%{time_total}s'` |
| Architecture | Parameterized queries, force-dynamic, adapter pattern | `grep -c '.prepare(' lib/crypto/db.ts` |
| DX/DevOps | CI/CD, ESLint, healthcheck, .env.example | `ls .github/workflows/ .eslintrc.json` |
| UI/UX | Nav structure, PWA, keyboard shortcuts | `grep -c 'NavGroup' lib/nav.ts` |
| Data integrity | Encryption, WAL mode, migrations, export/import | `head -5 lib/crypto/encryption.ts` |
| Documentation | README, .env.example, plan docs | `wc -l README.md .env.example` |

Score each out of 10 with **honest gaps named explicitly**. The user values a verified 7/10 with a real gap list over a claimed 10/10 that the next round reveals as 8. If the user asks "is it 10/10?" twice in a session, you haven't run the audit yet — run it now.

## Security hardening pass (Phase 1 of any 10/10 push)

When the audit reveals security gaps, fix in this order:

1. **Auth middleware** — single `AUTH_TOKEN` env gate in `middleware.ts`/`proxy.ts`. Accept `Authorization: Bearer <token>` and `X-Auth-Token: <token>` for API clients; avoid `?token=<token>` unless there is no alternative because query tokens leak via URLs/logs/history. **Do not inject bearer tokens into browser HTML** (`window.__AUTH_TOKEN__ = ...`) for public exposure. If the user wants an internal/LAN dashboard with no auth, set `AUTH_TOKEN` empty and keep it open; if public auth is required, use a real session/httpOnly-cookie login flow.
2. **CVE patches** — `npm audit` → bump to latest patch version. For Next.js 14.2.x, check `npm view next versions` and pick the latest 14.2.x (e.g. 14.2.35).
3. **Docker healthcheck** — use `node -e "fetch(...)"` (no apt/wget needed). **User constraint: 60s interval, NOT 5s** — high-frequency healthchecks spike CPU on low-power hosts. `mem_limit: 512m` prevents runaway growth.
4. **ESLint** — `.eslintrc.json` with `next/core-web-vitals` + `no-console: warn`. See **ESLint installation pitfalls** below for the two configs that bite every time.
5. **console.log cleanup** — gate with `if (process.env.NODE_ENV !== "production")` or remove.
6. **Security headers** — `X-Frame-Options: DENY`, `Permissions-Policy: camera=(), microphone=()`, `Referrer-Policy: strict-origin-when-cross-origin`.

## Widget polling optimization (low CPU/RAM)

Dashboard widgets that poll every 5s eat CPU on the server and battery on the client. Fix with three layers:

1. **`useVisibilityPoll`** — `setInterval` that skips the fetch when `document.hidden`. Also refetches on `visibilitychange` → visible. Replaces bare `setInterval(load, 5000)`.
2. **`useApi` hook** — unified fetch with in-flight request dedup (same URL within 200ms → shared promise). Auto-attaches `X-Auth-Token` header from `window.__AUTH_TOKEN__`. Replaces 29+ scattered `fetch().then(r => r.json())` patterns.
3. **Settings controls** — `pauseAllRefresh` (kill switch), `liveWidgetsRefreshSec` (configurable interval, default 15s, range 5-120s). Both in Settings → Refresh section.

Pattern: `useVisibilityPoll(load, pollMs, auto && !settings.pauseAllRefresh)` — respects both the user's per-widget toggle and the global pause.

## Nav grouping (when flat tabs exceed 20)

40 flat horizontal tabs is unreadable. Group into 5-7 dropdown categories:

```ts
export const NAV_GROUPS: NavGroup[] = [
  { label: "Trading", short: "TRADE", items: [...] },
  { label: "Analytics", short: "ANALYTICS", items: [...] },
  { label: "Journal", short: "JOURNAL", items: [...] },
  // ...
];
```

Render with CSS `group-hover:block` dropdown (no JS state needed). Each group shows its `short` label in the tab bar; hover reveals the full list. Active state = any item in the group matches the current path.

## User intent: maximize shipped surface per token/time

When the user says some variant of **"complete as much as possible"**, **"use less token and time"**, or otherwise optimizes for batch throughput, do **not** spread effort evenly across all candidate features.

Use this prioritization rule:

1. **Prefer features that already have a live API/data source** and only need UI composition or light route wiring.
2. **Prefer extensions of existing pages/patterns** (existing `PageHeader`, `RefreshBar`, `useAutoRefresh`, existing analytics/funding routes).
3. **Prefer one-batch verification** over per-feature micro-verification.
4. **Defer features with unclear data contracts or broader integration surfaces** until after the fast verified wins are shipped.

In practice this means:
- if `/api/funding` already exists, ship the Funding page now
- if `/api/analytics/correlation` already exists, ship the Portfolio Overlap page now
- if the trade form already exists, add the behavioral gate in-place instead of inventing a broader workflow
- if a feature like a news/unlock overlay depends on multiple feeds, parsing rules, or uncertain placement, it is usually a **second batch** item unless the plumbing already exists cleanly

## Market-context batch pattern for trading UIs

When the next ROI wave is **context around a trade decision** rather than a brand-new standalone tool, prefer one compact server route plus one in-page panel over spinning up multiple new pages.

Pattern that worked well:
1. Add a single route like `/api/market-context?symbol=BTCUSDT`.
2. Aggregate from the **highest-confidence existing/public sources first**:
   - existing internal news pipeline for symbol-tagged headlines
   - exchange public endpoints for funding / open interest / 24h move
   - optional third-party unlock / vesting feed only if a key is already configured
3. Render the result inside the existing trade page as a compact decision panel:
   - funding
   - short-horizon OI drift
   - 24h price change
   - squeeze / crowding heuristic
   - latest relevant headlines
   - token unlock queue / fallback note
4. Keep the unlock feed **gracefully optional**. If the env key is missing or the provider returns no schedule, return a usable note instead of failing the whole panel.

Why this pattern is high-ROI:
- it reuses the current trade surface where the decision is actually made
- it avoids nav/page sprawl for data that is only useful in context
- it lets one route fuse heterogeneous feeds while keeping the UI simple
- it ships useful OI/liquidity context even when the unlock provider is unavailable

Implementation rule:
- treat optional premium feeds as an overlay, not a hard dependency
- the route should still return `news + OI + liquidity` successfully when unlock data is unavailable
- make the fallback explicit in UI text (for example: "Set `MOBULA_API_KEY` to enable token unlock overlay")

Verification rule for this pattern:
- verify the route exists in `next build` output
- verify typecheck/tests/build after inserting the in-page panel
- if using a live public exchange endpoint for OI/funding, probe it directly once from terminal so you know the payload shape before coding the route

Follow-up polish (same batch): inline OI sparkline, `/trade?symbol=` deep-links from news/unlocks, and v2 squeeze scoring (basis + OI churn + adapter-based liq proximity) — see `references/market-context-batch-pattern.md`.

## Keep local UI gates local unless reuse is proven

## Keep local UI gates local unless reuse is proven

For page-specific behavioral controls like a pre-trade checklist modal, prefer **local in-page implementation** when:
- the workflow is tightly coupled to one page (`/trade`)
- the modal needs direct access to page-local state (`side`, `type`, `qty`, `risk`, `rr`, pending action)
- there is no demonstrated second call site yet

Benefits:
- less prop plumbing across files
- less import churn
- faster verification in a batch session

Only extract to `components/X.tsx` when one of these is true:
- reuse is already needed in 2+ places
- the component is large enough to materially hurt readability of the page
- independent testing/story-style iteration is needed

## Large multi-file JSX edits: avoid patch-fragment drift

When doing a high-throughput feature batch with long TSX files:
- prefer a **single coherent patch** or a **whole-file rewrite** over many tiny overlapping JSX patches
- after any structural JSX patch, immediately verify with `tsc --noEmit` or a full build
- if a patch tool shows truncation markers or partial replacement symptoms, stop layering more patches on top of it

Failure mode to avoid:
- dangling closing tags
- duplicated function blocks
- half-applied modal insertion near the bottom of a page

In token/time-optimized sessions, recovering from JSX drift costs more than rewriting the affected page once.

## Subagent parallelism for independent features

When building 3+ non-overlapping features (e.g. new exchange adapters, new pages, new API routes), use `delegate_task` with `tasks: [...]` to build them in parallel. Each subagent gets its own terminal session and file context. Verify all with a single `tsc --noEmit` after they finish — don't poll, just continue working on other features while they run.

Key rule: subagents must NOT touch the same files (e.g. `types.ts`, `index.ts`). Assign shared files to one subagent or do them yourself after the subagents finish.

Subagent timeout (600s) does NOT mean their work failed — file writes may have completed; only their own verification step timed out. Check the filesystem and run `tsc --noEmit` yourself before re-dispatching.

## Hedge mode + 1-click market orders

When adding hedge mode to a trade ticket:

1. **Type extension** — add `hedgeMode?: boolean` and `positionSide?: "Long" | "Short"` to `PlaceOrderRequest` in `types.ts`
2. **API passthrough** — the orders route must forward these fields from the request body to the `PlaceOrderRequest` object
3. **UI** — two-segment toggle: "One-way" vs "Hedge (dual side)". When hedge is selected, show a Long/Short sub-selector. Both fields are sent in the POST body.
4. **1-click market buttons** — separate from the main "Place Order" button. Skip confirmation for speed, but still respect the daily loss limit gate (`riskStatus?.breached` check). Label with ⚡ icon for visual distinction.

```tsx
async function oneClickMarket(s: "Buy" | "Sell") {
  if (riskStatus?.breached) { setMsg({kind:"err", text:"Daily loss limit hit"}); return; }
  // POST with type: "Market", no price, no confirmation
}
```

## SQLite ALTER TABLE race during `next build`

**Symptom:** `npm run build` compiles cleanly but fails in "Collecting page data" with:

```
SqliteError: duplicate column name: expected_price
    at Database.exec (.../better-sqlite3/lib/methods/wrappers.js:9:14)
    ...
Error: Failed to collect page data for /api/dca
```

**Root cause:** Next.js page-data collection runs multiple route workers in parallel against the same SQLite DB file. The classic `if (!hasCol(...)) d.exec(ALTER ...)` pattern races: two workers both see "column missing" via pragma, both attempt the ALTER, the loser throws. SQLite has no `ADD COLUMN IF NOT EXISTS`.

**Fix:** Idempotent helper that swallows only the duplicate-column error:

```ts
const addColIfMissing = (table: string, col: string, ddl: string) => {
  if (hasCol(table, col)) return;
  try {
    d.exec(ddl);
  } catch (e: any) {
    const msg = String(e?.message ?? e);
    if (!/duplicate column name/i.test(msg)) throw e;
  }
};

addColIfMissing("trades", "expected_price", `ALTER TABLE trades ADD COLUMN expected_price REAL;`);
// CREATE INDEX IF NOT EXISTS is already idempotent — leave it outside the helper
```

Same pattern applies to any DDL the runtime might race: only ALTER TABLE ADD COLUMN needs this; CREATE TABLE/INDEX support `IF NOT EXISTS` natively. The race only fires during `next build` page-data collection, not at runtime in production — but it still blocks the build, so fix it.

## SQLite readonly in Docker

**Symptom:** API route returns 500 with `SQLITE_READONLY: attempt to write a readonly database` when the app tries to CREATE TABLE or INSERT on first run.

**Root cause:** Docker `USER node` runs as uid 1000, but the bind-mounted `./data/` directory and DB files are owned by root. The container can read but not write.

**Fix:** `chmod 777` the DB files on the host (or `chown node:node`):

```bash
chmod 777 data/tradingx.db data/tradingx.db-shm data/tradingx.db-wal
docker restart <container>
```

This happens specifically when a new table is created at runtime (e.g. `social_profiles` on first call to `/api/social`). Existing tables that were created during `npm run dev` (running as root) inherit root ownership.

## Reliability hardening pass (error boundaries + retry + rate limiting)

When pushing an app from 8→9.5, add three reliability layers:

### 1. Root error boundary + 404 page

```tsx
// app/error.tsx — catches any unhandled error in any route segment
"use client";
export default function GlobalError({ error, reset }) {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="surface max-w-md p-8 text-center">
        <h2>Something went wrong</h2>
        <p>{error.message}</p>
        {error.digest && <span className="text-xs">Ref: {error.digest}</span>}
        <button onClick={reset}>Try again</button>
        <button onClick={() => window.location.href = "/"}>Go home</button>
      </div>
    </div>
  );
}

// app/not-found.tsx — clean 404
"use client";
export default function NotFound() {
  return <div>404 — <Link href="/">Go to dashboard</Link></div>;
}
```

### 2. Proxy-based retry/backoff for all adapter methods

Instead of editing 8 adapter files to add retry logic, wrap at the factory level with a Proxy:

```ts
// lib/crypto/retry.ts — exponential backoff, only retries 5xx/network/429
export async function withRetry<T>(fn: () => Promise<T>, opts?: RetryOpts): Promise<T> {
  const o = { maxAttempts: 3, baseDelayMs: 500, maxDelayMs: 4000, ...opts };
  for (let attempt = 1; attempt <= o.maxAttempts; attempt++) {
    try { return await fn(); } catch (err) {
      if (attempt === o.maxAttempts || !isRetryable(err)) throw err;
      const backoff = Math.min(o.baseDelayMs * 2 ** (attempt - 1), o.maxDelayMs);
      await delay(backoff + Math.random() * 250); // jitter
    }
  }
}

// lib/crypto/index.ts — wrap adapter with Proxy
function withRetryAdapter(a: ExchangeAdapter): ExchangeAdapter {
  const NETWORK_METHODS = new Set([
    "getTicker", "getAllTickers", "getBalance", "getPositions",
    "placeOrder", "cancelOrder", "closePosition", "setLeverage",
    "applyAdvancedOrderUpdate", /* ... */
  ]);
  return new Proxy(a, {
    get(target, prop) {
      const fn = (target as any)[prop];
      if (typeof fn !== "function" || !NETWORK_METHODS.has(prop as string)) return fn;
      return async (...args: unknown[]) =>
        withRetry(() => fn.apply(target, args), { label: `${a.name}.${prop}` });
    },
  }) as unknown as ExchangeAdapter;
}
```

`isRetryable` checks for: network errors (ECONNRESET, ETIMEDOUT, fetch failed), 429/rate limit, 5xx, "timeout", "try again later". Does NOT retry 4xx (real failures).

### 3. Rate limiter audit — find all unprotected write routes

```bash
# Find all POST/PUT/DELETE/PATCH exports
search_files pattern="export\s+async\s+function\s+(POST|PUT|DELETE|PATCH)" path=app/api
# Find which routes already have withRateLimit
search_files pattern="withRateLimit" path=app/api
# The difference = unprotected routes that need it
```

Convert `export async function POST(req)` → `export const POST = withRateLimit(async (req) => { ... }, { keyPrefix: "X:post", max: 30, windowMs: 60_000 });`. The wrapper returns a 429 Response when exceeded.

**Pitfall:** `withRateLimit` wraps the handler and returns `R | Response`. When the rate limit triggers, it returns a plain `Response` (429), not the handler's return type. TypeScript accepts this because the wrapper's return type is `(...args) => Promise<R | Response>`.

## Testing client modules from Node — extract pure logic to a sibling file

When you want to unit-test logic that currently lives inside a `"use client"`
module (e.g. `lib/useMarketStream.ts` with WebSocket / window globals), do NOT
try to `import` it directly from a `node:test` file. Even with explicit `.ts`
extensions, the import either fails (ESM resolver can't find it because no
`.ts` extension was written) or it loads and crashes on the missing
`WebSocket` / `document` / `window` globals.

**Anti-pattern:**

```ts
// __tests__/websocket.test.ts
import { parseTickerFrame } from "../lib/useMarketStream";  // ❌ fails
```

**Correct pattern — extract pure parsers into a sibling file:**

```ts
// lib/marketStreamParsers.ts  — NO "use client", NO DOM deps, no imports
export function parseTickerFrame(msg, previousRaw = {}) { ... }
export function parseOrderBookFrame(msg) { ... }
export function classifyStreamMode(lastMessageAt, connected, now, staleAfterMs) { ... }

// lib/useMarketStream.ts  — keeps "use client", re-exports for callers
"use client";
import {
  parseTickerFrame, parseOrderBookFrame, classifyStreamMode,
  type StreamTicker, type StreamOrderBook,
} from "./marketStreamParsers";
export { parseTickerFrame, parseOrderBookFrame, classifyStreamMode };
export type { StreamTicker, StreamOrderBook };

// __tests__/websocket.test.ts
import { parseTickerFrame } from "../lib/marketStreamParsers.ts";  // ✓ works
```

Two wins from this refactor:
1. Tests run in pure Node with no browser shim.
2. The parsers stay reusable from server-side code (e.g. an SSR endpoint
   that needs to normalise a Bybit V5 payload) without dragging the
   `"use client"` directive across the import boundary.

Diagnostics / state-snapshot getters that still reach into the live module
state (e.g. `getStreamDiagnostics()`) belong in the `"use client"` module and
should be verified live via a `/diagnostics` page, not unit-tested.

## API integration tests (node:test + fetch)

When the user asks "API test is needed?", add integration tests that hit real HTTP endpoints:

```ts
// __tests__/api.test.ts
import { test, describe } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";

// Load .env manually (node --test doesn't auto-load it)
try {
  const envText = readFileSync(resolve(process.cwd(), ".env"), "utf-8");
  for (const line of envText.split("\n")) {
    const m = line.match(/^([A-Z_]+)=(.*)$/);
    if (m && !process.env[m[1]]) process.env[m[1]] = m[2].replace(/^["']|["']$/g, "");
  }
} catch {}

const BASE_URL = process.env.TEST_BASE_URL ?? "http://localhost:8799";
const AUTH_TOKEN = process.env.AUTH_TOKEN ?? "";

describe("API Integration Tests", { skip: !(await serverUp()) }, () => {
  test("GET /api/health → 200 + healthy", async () => { ... });
  test("Auth: 401 without token", async () => { ... });
  test("Auth: 200 with Bearer token", async () => { ... });
  test("Auth: 200 with X-Auth-Token header", async () => { ... });
  test("Auth: 200 with ?token= query param", async () => { ... });
  test("Rate limit: burst → 429", async () => {
    const results = await Promise.all(
      Array.from({ length: 35 }, () => fetch(url, { method: "POST", body: "{}" }).then(r => r.status))
    );
    assert.ok(results.filter(s => s === 429).length > 0);
  });
  test("GET / → 200 (pages render without auth)", async () => { ... });
});
```

**Pitfall:** When `AUTH_TOKEN` is set, middleware returns 401 for unknown `/api/` routes before Next.js routing can determine it's a 404. Test should accept either 401 or 404 for unknown API routes.

**Pitfall:** The `describe` skip condition must use `await serverUp()` — `node:test` supports top-level await in the describe options.

## Browser push notifications (no VAPID needed)

For same-origin browser notifications when the tab is open (no service worker background push):

```ts
// lib/useBrowserNotifications.ts
export function useBrowserNotifications() {
  const checkAlerts = useCallback(async () => {
    if (document.hidden) return;  // visibility-aware
    const settings = await fetch("/api/settings/runtime").then(r => r.json());
    if (!settings?.data?.browserNotifications) return;  // server-side gate
    if (Notification.permission !== "granted") return;
    const res = await fetch("/api/alerts/check", { method: "POST" });
    const j = await res.json();
    for (const alert of j.data?.results?.filter(r => r.triggered) ?? []) {
      new Notification("🔔 Alert", { body: alert.message, tag: `alert-${alert.id}` });
    }
  }, []);
  useEffect(() => {
    const interval = setInterval(checkAlerts, 30_000);
    return () => clearInterval(interval);
  }, [checkAlerts]);
}
```

Wire into root layout via a client bootstrap component (since `layout.tsx` is a server component):

```tsx
// components/ClientBootstrap.tsx
"use client";
import { useBrowserNotifications } from "@/lib/useBrowserNotifications";
export function ClientBootstrap() { useBrowserNotifications(); return null; }

// app/layout.tsx (server component)
import { ClientBootstrap } from "@/components/ClientBootstrap";
// In <body>: <ClientBootstrap />
```

## AdvancedOrderModal pattern (OCO / Trailing / Partial TP)

When a position-management API already exists (`/api/positions/manage` with `trailingPct`, `breakevenTrigger`, `partials`, `finalStop`, `finalTp`), build a 3-tab modal instead of separate pages:

```tsx
// components/AdvancedOrderModal.tsx
const [tab, setTab] = useState<"oco" | "trailing" | "partial">("oco");
// OCO tab: slPrice + tpPrice inputs → body.finalStop + body.finalTp
// Trailing tab: trailType (pct/abs) + distance + breakevenTrigger
// Partial tab: tiers[] {qty, pnlPct} + finalStop
// All submit to POST /api/positions/manage with the same body shape
```

Key: the modal builds a `Record<string, unknown>` body and populates different fields based on the active tab. The API accepts all fields optionally.

## Mobile responsive table fix

Tables with many columns get clipped on mobile. Wrap in `overflow-x-auto`:

```tsx
<div className="surface overflow-hidden">
  <div className="overflow-x-auto">
    <table className="w-full text-sm">...</table>
  </div>
</div>
```

The outer `overflow-hidden` keeps the surface's rounded corners; the inner `overflow-x-auto` enables horizontal scrolling on mobile.

## Theme system extension (adding a new theme variant)

When the user says "make the theme like [reference website]", the pattern is: extract the reference site's design system via browser_console, then add a new theme variant to the existing CSS variable system. No new framework, no conflict.

### Step 1: Extract the reference site's design

Navigate to the reference site with `browser_navigate`, then use `browser_console` to extract CSS custom properties and computed styles.

**⚠️ CRITICAL — if the user wants DARK mode:** Many SaaS sites default to a LIGHT marketing page. Before extracting, find and click the site's Dark toggle button. If the site has a "showcase" section (e.g. "Flow From Day to Night"), extract from within that dark section. Extracting the wrong variant means you'll build a light theme when the user explicitly asked for dark — this is a costly, frustrating mistake.

```js
// Get CSS variables
const vars = {};
for (const sheet of document.styleSheets) {
  try {
    for (const rule of sheet.cssRules) {
      if (rule.style) for (let i = 0; i < rule.style.length; i++) {
        const prop = rule.style[i];
        if (prop.startsWith('--')) vars[prop] = rule.style.getPropertyValue(prop);
      }
    }
  } catch(e) {}
}

// Get key element colors
const cta = Array.from(document.querySelectorAll('a, button')).find(b => b.textContent.trim() === 'Start free');
const cs = cta ? getComputedStyle(cta) : null;
// cs.backgroundColor, cs.backgroundImage (gradients!), cs.borderRadius, cs.color

// Get body, header, hero, card styles
getComputedStyle(document.body)  // backgroundColor, color, fontFamily
getComputedStyle(document.querySelector('h1'))  // fontSize, fontWeight, color

// Collect unique background colors and text colors used on the page
const bgs = new Set(), colors = new Set();
for (const el of document.querySelectorAll('*')) {
  const s = getComputedStyle(el);
  if (s.backgroundColor !== 'rgba(0, 0, 0, 0)') bgs.add(s.backgroundColor);
  if (s.color !== 'rgb(0, 0, 0)') colors.add(s.color);
}
```

Key things to extract: `--background`, `--foreground`, card/surface bg, accent color, CTA button gradient (`backgroundImage: linear-gradient(...)`), border radius (pill = 9999px), font family.

### Step 2: Back up existing theme files

```bash
mkdir -p backups/pre-new-theme
cp app/globals.css tailwind.config.ts lib/settings.ts components/ThemeApplicator.tsx backups/pre-new-theme/
```

### Step 3: Add the theme variant

The existing TradingX theme system uses `data-theme` attribute on `<html>` + CSS variables in `globals.css`. Adding a variant is additive — no conflict with existing themes:

**a) Widen the settings type:**
```ts
// lib/settings.ts
theme: "dark" | "light" | "system" | "waves";  // add the new variant
```

**b) Add CSS variable block in globals.css:**
```css
:root[data-theme="waves"] {
  color-scheme: light;
  --bg: #ffffff;
  --bg-card: #f2f6ff;
  --fg: #0b163f;
  --accent-1: #1783ff;
  /* ... all the extracted values ... */
  --waves-cta: linear-gradient(90deg, #1783ff, #4ca9ff);  /* theme-specific vars */
  --waves-radius: 12px;
}
```

**c) Add theme-specific component overrides** (chips, buttons, inputs, scrollbar) scoped under `:root[data-theme="waves"]`. These are additive — they only apply when the theme is active.

**d) Update ThemeApplicator** to handle the new theme as a distinct value (not mapped to dark/light). Update the `theme-color` meta tag for the new theme.

**e) Add the button in Settings UI** — just add the variant to the `["dark", "light", "system", "waves"]` array and the label mapping.

### Step 4: Verify

- `tsc --noEmit` — 0 errors (the type widening is the only type change)
- `npm test` — all pass
- `npm run build` — clean
- Deploy, then verify CSS vars are active via `browser_console`:
  ```js
  getComputedStyle(document.documentElement).getPropertyValue('--bg')  // → "#fff"
  document.documentElement.getAttribute('data-theme')  // → "waves"
  ```

### Pitfall: patch tool quote-escaping

When using `patch` with `old_string` or `new_string` containing quotes (e.g., `["dark", "light"]`), the tool can introduce literal `\"` backslashes into the file. The diff looks correct but the file contains `\"dark\"` instead of `"dark"`.

**Fix:** Use `sed` to strip the backslashes:
```bash
sed -i 's/\\"/"/g' app/settings/page.tsx
```

Or avoid the issue entirely by using `write_file` for files with heavy quote content instead of `patch`.

## Honest self-rating (mandatory)

This is the single hardest user preference to honor and the single most common place sessions go wrong. Read carefully.

**Never self-grade 10/10.** Not after a wave of fixes. Not when tests pass and the build is clean. Not when the user asks "is it 10/10?" and you want to give a satisfying answer. 10/10 is a structural claim about an entire app — features, performance, security, reliability, accessibility, ops, docs — and almost nothing measured during a coding session covers all of that.

**When the user asks "so my app is 10/10?" — that is a TEST, not a compliment.** They are checking whether you will overclaim. The correct response is a sector-by-sector scorecard with explicit gaps:

```
| Sector    | Score | Why not 10 |
| Features  | 9/10  | Missing: chart trailing stop, OCO, visual bot builder |
| Security  | 8.5   | 4 npm transitive vulns, no rate limiting on some routes |
| Tests     | 7     | 66 unit tests, 0 API integration tests, no E2E coverage |
| Perf      | 8.7   | Bundle analyzer baseline captured but no Lighthouse run yet |
| Docs      | 7     | README, no ARCHITECTURE.md or DEPLOYMENT.md |
```

A verified 8.7 with a real gap list is more valuable than a claimed 10/10 that the next wave reveals as 8. The user values calibration over enthusiasm.

**When the user says "make it 10/10 in all sectors":** acknowledge it as a direction, not a one-shot achievable target. Reply with the plan: "I'll do the next wave (A, B, C); after that we'll re-score honestly." Then execute and re-score. Do not announce "done — it's 10/10 now" at any point.

**Phrases to avoid:**
- "It's now 10/10"
- "All sectors perfect"
- "Production-ready perfection"
- "Nothing left to fix"

**Phrases that work:**
- "Better. Honest score: 9.0 overall. Gaps remaining: X, Y, Z."
- "Not 10/10 yet. What was fixed: …. What still blocks 10/10: …"
- "Stronger now, but I'm not going to claim perfect. Here's the real scorecard."

Run the 9-category audit probes from `references/security-hardening-and-audit.md`, name the gaps explicitly, and let the user decide if the gaps matter. If you're tempted to round up because the user seems frustrated, round down instead and offer the next concrete wave.

## Next.js 16 migration / performance hardening follow-up

When improving an existing App Router app after a broad audit, do not stop at the obvious frontend fixes. A performance pass often exposes framework-upgrade breakage that only shows up at full `next build` time.

### Pattern that emerged

1. Apply the direct performance wins first:
   - add `images.formats` + `remotePatterns` in `next.config.*`
   - replace external `<img>` usage with `next/image` where practical
   - remove globally eager third-party scripts from `layout.tsx`
   - lazy-load heavy widgets with `next/dynamic` or viewport-gated script injection
   - add short `revalidate` windows to read-heavy public endpoints
2. Then run the full verification chain again, because **framework build errors can surface only after those edits**.
3. If `next build` fails on route handlers after a Next 16 upgrade, audit dynamic route signatures immediately.

### Next 16 route-handler pitfalls

Two concrete breakages are easy to miss:

1. **Re-exporting `dynamic` from another route file is invalid**
   ```ts
   // bad
   export { POST, dynamic } from "../signals/in/route";

   // good
   export const dynamic = "force-dynamic";
   export { POST, GET } from "../signals/in/route";
   ```

2. **Dynamic route params must use `Promise<{...}>` context in App Router handlers**
   Update handlers like:
   ```ts
   type Ctx = { params: Promise<{ id: string }> };

   export async function GET(_req: Request, { params }: Ctx) {
     const { id } = await params;
     ...
   }
   ```
   The same applies to wrapped handlers (`withRateLimit(async (req, { params }) => ...)`).

### TradingView / third-party widget rule

If a heavy chart/widget is only visible on one page section, do **not** load its script in the root layout. Prefer:
- `IntersectionObserver` to arm loading only when near viewport
- one-shot script injection with a stable `data-*` marker to prevent duplicates
- fallback rendering if the vendor script fails

### Honest scoring rule

If the user says "make it 10/10" after an audit, do not claim literal perfection. Implement the measurable fixes, verify them, and then state plainly what remains structural (for example: many `"use client"` pages still need page-by-page server-component review). See the **Honest self-rating (mandatory)** section above for the exact phrasing rules.

### Additional follow-up topics covered in `references/next16-performance-hardening.md`

- `middleware.ts` → `proxy.ts` migration (file rename, function rename, the export-alias anti-pattern that does NOT silence the warning)
- Turbopack NFT "unexpected file in NFT list" warning fix (`serverExternalPackages` + lazy `process.cwd()` + `/* turbopackIgnore: true */` comments)
- `@next/bundle-analyzer` only works under `next build --webpack`, not the default Turbopack build
- React hydration mismatch (#418/#423/#425) from reading `localStorage` during initial render; fix via the `hydrated` flag pattern from `useSettings()`
- Playwright smoke test pattern that captures `pageerror` + `console.error` across critical routes — this is what catches hydration bugs the test suite misses

## Reference

- `references/pitfalls.md` — full detail on each pitfall with the actual errors hit
- `references/recipes.md` — copy-paste patterns: PWA setup, RSS news aggregation, Sharpe/Sortino/Calmar, Cache-Control middleware, useAutoRefresh hook, RefreshBar component, economic calendar projection, CoinGecko wrapper
- `references/security-hardening-and-audit.md` — auth middleware token gate pattern, 9-category audit scorecard shell probes, low-CPU Docker healthcheck, widget polling optimization (useVisibilityPoll + useApi + request dedup), nav grouping pattern, hot-reload scheduler, keyboard shortcuts, full DB export/import
- `references/reliability-and-testing.md` — Proxy-based retry/backoff wrapper, rate limiter audit methodology, API integration test pattern (node:test + .env loading + auth/rate-limit assertions), browser push notification hook, AdvancedOrderModal 3-tab pattern, error boundary + 404 page, mobile responsive table fix, honest scorecard methodology
- `references/theme-extraction-and-css-variables.md` — extracting a competitor's design system from a live website via browser_console (CSS vars, computed styles, gradients, oklab), adding a new theme variant to an existing CSS-variable theme system without conflicts, verification pattern
- `references/eslint-and-migrations.md` — ESLint install + config without missing-plugin errors (`react/no-unescaped-entities` off, `@typescript-eslint/*` rules dropped unless plugin installed); SQLite `ALTER TABLE ADD COLUMN` race during parallel `next build` page-data collection (idempotent `addColIfMissing` helper); Docker compose-vs-`docker run` container name conflict (`docker rm -f` then `compose up -d`)
- `references/next16-performance-hardening.md` — session-specific notes on Next 16 route-handler param migration, invalid `dynamic` re-export fixes, viewport-gated TradingView loading, and image optimization follow-up
- `references/market-context-batch-pattern.md` — compact route + in-page panel pattern for trade-context batches (news + OI + liquidity + optional unlock overlay)
- `references/tradingx-audit-hardening-2026-07.md` — final-audit hardening wave: Next 16 ESLint flat config, no frontend bearer-token injection, RSS timeouts, deployment SHA diagnostics, live redeploy probes, and honest post-wave scoring
- `references/tradingx-10-10-sector-push.md` — repeated “make it 10/10” follow-up wave: quality/security/deployment diagnostics, strict zero-warning lint, resilience UI, mobile/404 Playwright smoke tests, and honest sector scoring
- `references/tradingx-automation-safety-hardening.md` — trading-app automation safety wave: central order execution service, risk-gated bot/signal paths, in-process tick locks, SQLite upsert/stale-position fixes, webhook SSRF guards, analytics correctness, and verified redeploy probes
- `references/cloudflare-warp-guidance.md` — WARP vs WARP+ differences, latency/throughput impact, resource usage, modes, commands, and performance testing pattern (JSX patch breakage, file-naming collisions, docker terminal blocking, route file rules, LSP vs tsc, pre-existing type errors, .next/ stale types, patch quote-escaping, verification reminders)
- `references/recipes.md` — copy-paste patterns: PWA setup, RSS news aggregation, Sharpe/Sortino/Calmar, Cache-Control middleware, useAutoRefresh hook, RefreshBar component, economic calendar projection, CoinGecko wrapper
- `references/security-hardening-and-audit.md` — auth middleware token gate pattern, 9-category audit scorecard shell probes, low-CPU Docker healthcheck, widget polling optimization (useVisibilityPoll + useApi + request dedup), nav grouping pattern, hot-reload scheduler, keyboard shortcuts, full DB export/import
- `references/reliability-and-testing.md` — Proxy-based retry/backoff wrapper, rate limiter audit methodology, API integration test pattern (node:test + .env loading + auth/rate-limit assertions), browser push notification hook, AdvancedOrderModal 3-tab pattern, error boundary + 404 page, mobile responsive table fix, honest scorecard methodology
- `references/theme-extraction-and-css-variables.md` — extracting a competitor's design system from a live website via browser_console (CSS vars, computed styles, gradients, oklab), adding a new theme variant to an existing CSS-variable theme system without conflicts, verification pattern
- `references/eslint-and-migrations.md` — ESLint install + config without missing-plugin errors (`react/no-unescaped-entities` off, `@typescript-eslint/*` rules dropped unless plugin installed); SQLite `ALTER TABLE ADD COLUMN` race during parallel `next build` page-data collection (idempotent `addColIfMissing` helper); Docker compose-vs-`docker run` container name conflict (`docker rm -f` then `compose up -d`)
- `references/next16-performance-hardening.md` — session-specific notes on Next 16 route-handler param migration, invalid `dynamic` re-export fixes, viewport-gated TradingView loading, and image optimization follow-up
- `references/market-context-batch-pattern.md` — compact route + in-page panel pattern for trade-context batches (news + OI + liquidity + optional unlock overlay)
- `references/tradingx-audit-hardening-2026-07.md` — final-audit hardening wave: Next 16 ESLint flat config, no frontend bearer-token injection, RSS timeouts, deployment SHA diagnostics, live redeploy probes, and honest post-wave scoring
- `references/tradingx-10-10-sector-push.md` — repeated “make it 10/10” follow-up wave: quality/security/deployment diagnostics, strict zero-warning lint, resilience UI, mobile/404 Playwright smoke tests, and honest sector scoring
- `references/tradingx-automation-safety-hardening.md` — trading-app automation safety wave: central order execution service, risk-gated bot/signal paths, in-process tick locks, SQLite upsert/stale-position fixes, webhook SSRF guards, analytics correctness, and verified redeploy probes

