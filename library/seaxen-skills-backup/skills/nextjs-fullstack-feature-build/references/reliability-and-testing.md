# Reliability + Testing Patterns

Distilled from the TradingX 8.7→9.3 push (June 2026). Covers error boundaries, Proxy-based retry/backoff, rate limiter audit, API integration tests, browser push notifications, AdvancedOrderModal, and mobile responsive table fixes.

## 1. Root error boundary + 404 page

Next.js App Router calls `app/error.tsx` automatically when any route segment throws an unhandled error. Without it, users see a white screen.

```tsx
// app/error.tsx
"use client";
import { useEffect } from "react";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("[GlobalError]", error.message, error.digest);
  }, [error]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-bg-base px-4">
      <div className="surface max-w-md w-full p-8 text-center space-y-4">
        <div className="text-4xl">⚠️</div>
        <h2 className="text-lg font-semibold">Something went wrong</h2>
        <p className="text-sm text-fg-faint">{error.message}</p>
        {error.digest && <span className="text-xs opacity-60">Ref: {error.digest}</span>}
        <div className="flex gap-3 justify-center">
          <button onClick={reset} className="px-4 py-2 rounded-lg bg-accent text-white">Try again</button>
          <button onClick={() => (window.location.href = "/")} className="px-4 py-2 rounded-lg border">Go home</button>
        </div>
      </div>
    </div>
  );
}
```

```tsx
// app/not-found.tsx — clean 404
"use client";
import Link from "next/link";
export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="surface max-w-sm p-8 text-center">
        <div className="text-5xl font-bold">404</div>
        <h2>Page not found</h2>
        <Link href="/" className="inline-block px-4 py-2 rounded-lg bg-accent text-white">Go to dashboard</Link>
      </div>
    </div>
  );
}
```

## 2. Proxy-based retry/backoff (no per-adapter edits)

**Problem:** 8 exchange adapters, each with 14 network methods. Adding retry to each file = 112 edits.

**Solution:** Wrap at the factory level with a `Proxy`. The Proxy intercepts property access on the adapter, and for known network methods, returns a wrapped version with retry.

```ts
// lib/crypto/retry.ts
export type RetryOpts = {
  maxAttempts?: number;
  baseDelayMs?: number;
  maxDelayMs?: number;
  label?: string;
};

const DEFAULTS: Required<RetryOpts> = {
  maxAttempts: 3,
  baseDelayMs: 500,
  maxDelayMs: 4000,
  label: "unknown",
};

function isRetryable(err: unknown): boolean {
  if (err instanceof RetryableError) return err.retryable;
  const msg = String(err instanceof Error ? err.message : err).toLowerCase();

  // Network errors
  if (msg.includes("econnreset") || msg.includes("enotfound") || msg.includes("etimedout") ||
      msg.includes("econnrefused") || msg.includes("fetch failed") || msg.includes("network")) {
    return true;
  }
  // Rate limits
  if (msg.includes("429") || msg.includes("rate limit") || msg.includes("too many requests")) {
    return true;
  }
  // Server errors
  if (/\b5\d{2}\b/.test(msg) || msg.includes("internal server error") ||
      msg.includes("service unavailable") || msg.includes("bad gateway") ||
      msg.includes("gateway timeout")) {
    return true;
  }
  // Common exchange transient messages
  if (msg.includes("server error") || msg.includes("timeout") || msg.includes("try again later")) {
    return true;
  }
  return false;
}

export async function withRetry<T>(fn: () => Promise<T>, opts?: RetryOpts): Promise<T> {
  const o = { ...DEFAULTS, ...opts };
  let lastErr: unknown;
  for (let attempt = 1; attempt <= o.maxAttempts; attempt++) {
    try {
      return await fn();
    } catch (err) {
      lastErr = err;
      if (attempt === o.maxAttempts || !isRetryable(err)) throw err;
      const backoff = Math.min(o.baseDelayMs * Math.pow(2, attempt - 1), o.maxDelayMs);
      const jitter = Math.floor(Math.random() * 250);
      await delay(backoff + jitter);
    }
  }
  throw lastErr;
}
```

```ts
// lib/crypto/index.ts — factory wraps adapter with Proxy
function withRetryAdapter(a: ExchangeAdapter): ExchangeAdapter {
  const NETWORK_METHODS = new Set([
    "getTicker", "getAllTickers", "fetchFundingRate", "fetchFundingHistory",
    "testConnection", "getBalance", "getPositions", "getOpenOrders",
    "getClosedTrades", "placeOrder", "cancelOrder", "closePosition",
    "setLeverage", "applyAdvancedOrderUpdate",
  ]);
  return new Proxy(a, {
    get(target, prop) {
      const fn = (target as any)[prop];
      if (typeof fn !== "function" || typeof prop !== "string") return fn;
      if (!NETWORK_METHODS.has(prop)) return fn;
      // Return wrapped version with correct `this` binding
      return async (...args: unknown[]) => {
        return withRetry(() => fn.apply(target, args), {
          label: `${a.name}.${prop}`,
          maxAttempts: 3,
        });
      };
    },
  }) as unknown as ExchangeAdapter;
}

export function adapterFor(connectionId: string): ExchangeAdapter {
  // ... decrypt creds, create adapter ...
  return withRetryAdapter(adapter);
}
```

**Key:** `fn.apply(target, args)` — NOT `fn.apply(receiver, args)`. The Proxy's `get` trap receives `receiver` as the third arg, but using `receiver` as `this` would cause infinite recursion (Proxy → get → wrapped fn → Proxy → get...). Use `target` (the original adapter).

## 3. Rate limiter audit — find unprotected write routes

```bash
# Step 1: Find ALL routes with POST/PUT/DELETE/PATCH exports
search_files pattern="export\s+async\s+function\s+(POST|PUT|DELETE|PATCH)" path=app/api target=content

# Step 2: Find which routes already import withRateLimit
search_files pattern="withRateLimit" path=app/api target=content

# Step 3: The files in step 1 but NOT in step 2 = unprotected routes
```

**Conversion pattern** — from plain function to rate-limited export:

```ts
// BEFORE
export async function POST(req: Request) {
  return safe(async () => { /* ... */ });
}

// AFTER
import { withRateLimit } from "@/lib/crypto/ratelimit";
export const POST = withRateLimit(async (req: Request) => {
  return safe(async () => { /* ... */ });
}, { keyPrefix: "X:post", max: 30, windowMs: 60_000 });
```

**For routes with params** (e.g. `app/api/grid/[id]/route.ts`):

```ts
export const PATCH = withRateLimit(async (req: Request, ctx: { params: Promise<{ id: string }> }) => {
  return safe(async () => {
    const { id } = await ctx.params;
    // ...
  });
}, { keyPrefix: "grid:patch", max: 20, windowMs: 60_000 });
```

**Rate limit tiers** (per-route defaults):
- Order placement: 30/min (high-frequency but expensive)
- CRUD operations: 20/min
- Delete operations: 10/min (destructive, lower tolerance)
- Import/backup: 5/min (very expensive)
- Settings: 10/min (low frequency)

## 4. API integration tests (node:test + fetch)

### Loading .env in node:test

`node --experimental-strip-types --test` does NOT auto-load `.env`. Load it manually:

```ts
import { readFileSync } from "node:fs";
import { resolve } from "node:path";

try {
  const envPath = resolve(process.cwd(), ".env");
  const envText = readFileSync(envPath, "utf-8");
  for (const line of envText.split("\n")) {
    const m = line.match(/^([A-Z_]+)=(.*)$/);
    if (m && !process.env[m[1]]) {
      process.env[m[1]] = m[2].replace(/^["']|["']$/g, "");
    }
  }
} catch { /* .env not found — tests skip auth-gated cases */ }
```

### Server availability check

```ts
async function serverUp(): Promise<boolean> {
  try {
    const r = await fetch(`${BASE_URL}/api/health`, { signal: AbortSignal.timeout(2000) });
    return r.ok;
  } catch { return false; }
}

describe("API Integration Tests", { skip: !(await serverUp()) }, () => { ... });
```

### Auth method tests (all 3 methods)

```ts
test("Auth: 401 without token", async (t) => {
  if (!AUTH_TOKEN) { t.skip("AUTH_TOKEN not set"); return; }
  const r = await fetch(`${BASE_URL}/api/exchanges`, { cache: "no-store" });
  assert.equal(r.status, 401);
});

test("Auth: 200 with Bearer token", async (t) => {
  if (!AUTH_TOKEN) { t.skip(); return; }
  const r = await fetch(`${BASE_URL}/api/exchanges`, {
    headers: { Authorization: *** ${AUTH_TOKEN}` },
  });
  assert.equal(r.status, 200);
});
// Same for X-Auth-Token header and ?token= query param
```

### Rate limit burst test

```ts
test("Rate limit: burst → 429", async (t) => {
  if (!AUTH_TOKEN) { t.skip(); return; }
  // Send 35 rapid POSTs (limit is 30/min)
  const results = await Promise.all(
    Array.from({ length: 35 }, () =>
      fetch(`${BASE_URL}/api/orders`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: *** ${AUTH_TOKEN}` },
        body: JSON.stringify({}),
      }).then((r) => r.status).catch(() => 0),
    ),
  );
  const rejected = results.filter((s) => s === 429).length;
  assert.ok(rejected > 0, "At least some should be rate-limited");
});
```

### Page rendering tests (no auth needed)

```ts
test("GET / → 200 (pages render without auth)", async () => {
  const r = await fetch(`${BASE_URL}/`);
  assert.equal(r.status, 200);
});
```

### 404 test pitfall

When `AUTH_TOKEN` is set, middleware returns 401 for ANY `/api/` route (including nonexistent ones) before Next.js routing can 404. Test must accept either:

```ts
test("unknown API route → 401 or 404", async () => {
  const r = await fetch(`${BASE_URL}/api/nonexistent-12345`);
  assert.ok(r.status === 401 || r.status === 404);
});
```

## 5. Browser push notifications (same-origin, no VAPID)

For notifications when the tab is open (no service worker background push needed):

```ts
// lib/useBrowserNotifications.ts
"use client";
import { useEffect, useCallback, useRef } from "react";

const POLL_INTERVAL_MS = 30_000;

export function useBrowserNotifications() {
  const lastCheckRef = useRef<number>(0);

  const checkAlerts = useCallback(async () => {
    if (document.hidden) return;  // visibility-aware
    const now = Date.now();
    if (now - lastCheckRef.current < 20_000) return;  // dedup
    lastCheckRef.current = now;

    try {
      // Check server-side setting first
      const settingsRes = await fetch("/api/settings/runtime", { cache: "no-store" });
      const settings = await settingsRes.json();
      if (!settings?.data?.browserNotifications) return;

      if (typeof Notification === "undefined") return;
      if (Notification.permission !== "granted") return;

      // Poll for triggered alerts
      const res = await fetch("/api/alerts/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({}),
        cache: "no-store",
      });
      const j = await res.json();
      if (!j?.ok) return;

      const triggered = j.data?.results?.filter((r: any) => r.triggered) ?? [];
      for (const alert of triggered) {
        new Notification("🔔 TradingX Alert", {
          body: alert.message,
          tag: `alert-${alert.id}`,  // dedup by alert ID
        });
      }
    } catch { /* silent fail */ }
  }, []);

  useEffect(() => {
    const interval = setInterval(checkAlerts, POLL_INTERVAL_MS);
    return () => clearInterval(interval);
  }, [checkAlerts]);
}

export async function requestNotificationPermission(): Promise<boolean> {
  if (typeof Notification === "undefined") return false;
  if (Notification.permission === "granted") return true;
  if (Notification.permission === "denied") return false;
  return (await Notification.requestPermission()) === "granted";
}
```

**Wire into root layout** (server component can't use hooks, so use a client bootstrap):

```tsx
// components/ClientBootstrap.tsx
"use client";
import { useBrowserNotifications } from "@/lib/useBrowserNotifications";
export function ClientBootstrap() {
  useBrowserNotifications();
  return null;
}

// app/layout.tsx
import { ClientBootstrap } from "@/components/ClientBootstrap";
// In <body>:
//   <ClientBootstrap />
//   <Topbar />
//   <main>{children}</main>
```

## 6. AdvancedOrderModal (3-tab modal for OCO / Trailing / Partial TP)

When a position-management API already exists (`/api/positions/manage`), build a modal with tabs instead of separate pages:

### Body construction pattern

```tsx
const body: Record<string, unknown> = {
  exchangeId, symbol: position.symbol, side: position.side,
  entryPrice: position.entryPrice, size: position.size, marketType: "linear",
};

if (tab === "oco") {
  body.finalStop = parseFloat(slPrice) || undefined;
  body.finalTp = parseFloat(tpPrice) || undefined;
} else if (tab === "trailing") {
  if (trailType === "pct") body.trailingPct = parseFloat(trailPct);
  else body.trailingDistance = parseFloat(trailDist);
  if (beTrigger) body.breakevenTrigger = parseFloat(beTrigger);
} else if (tab === "partial") {
  body.partials = tiers
    .filter(t => parseFloat(t.qty) > 0 && parseFloat(t.pnlPct) > 0)
    .map(t => ({ pct: parseFloat(t.qty), pnlPct: parseFloat(t.pnlPct) }));
  if (finalStop) body.finalStop = parseFloat(finalStop);
}
```

### Type-safe tiers state

```tsx
const [tiers, setTiers] = useState<Array<{ qty: string; pnlPct: string }>>([
  { qty: "50", pnlPct: "2.0" }, { qty: "50", pnlPct: "4.0" }
]);
```

### Validation before submit

```tsx
if (tab === "partial") {
  if (!body.partials || !(body.partials as unknown[]).length) {
    setMsg({ kind: "err", text: "Add at least one TP tier" });
    setBusy(false); return;
  }
}
```

## 7. Mobile responsive table fix

Tables with 10+ columns get clipped on mobile. Wrap in `overflow-x-auto`:

```tsx
<div className="surface overflow-hidden">
  <div className="overflow-x-auto">
    <table className="w-full text-sm">
      {/* 12+ columns */}
    </table>
  </div>
</div>
```

- Outer `overflow-hidden`: keeps the surface's rounded corners, prevents visual bleed
- Inner `overflow-x-auto`: enables horizontal scrolling on mobile, no scrollbar on desktop

## 8. Performance — visibility-aware setInterval

Replace bare `setInterval(load, 5000)` with visibility checks:

```tsx
// BEFORE (wastes CPU when tab hidden)
const t = setInterval(load, 5000);

// AFTER (pauses when tab hidden)
const t = setInterval(() => {
  if (!document.hidden) load();
}, 10_000);
```

Or use the existing `useVisibilityPoll` hook if available:
```tsx
useVisibilityPoll(load, 10_000);
```

**Interval tuning guide:**
- Position ticker: 5s (real-time trading data)
- Orders list: 10s (moderate frequency)
- Analytics/summary: 60s (expensive query, low urgency)
- Portfolio combined: 60s (multi-exchange aggregation)
- Browser notification check: 30s (lightweight, visibility-aware)

## 9. Honest scorecard methodology

When the user asks "is it 10/10?", run the 9-category audit from `security-hardening-and-audit.md` and present results as:

```
| Sector    | Score | Why not 10 |
| Features  | 9/10  | Missing: visual bot builder, real copy-trading |
| Security  | 8.5   | 4 npm transitive vulns (can't fix without Next 16) |
| Tests     | 7     | 66 unit, 0 API integration tests |
| Overall   | 8.7   | Strong, not perfect |
```

**Rules:**
- Never self-grade 10/10. The maximum honest score is 9.5.
- Name every gap explicitly with effort estimate to fix it.
- If the user asks twice, run the audit probes again — don't repeat the claim.
- Distinguish "can fix in this session" (API tests, rate limiting, error boundaries) from "multi-day build" (visual bot builder, Next 16 migration).
