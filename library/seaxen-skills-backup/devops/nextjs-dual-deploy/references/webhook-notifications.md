# Outbound webhook notifications for self-hosted apps

Pattern for letting a self-hosted app (like Tradingx) push events to a user-configured HTTP endpoint. Captured from the **Tradingx** build at `/mnt/tb/1Apps/Tradingx` v0.3, which fires webhooks on order fills, position changes, and P&L milestones from a self-hosted trading dashboard.

Use this when the app needs to:

- Notify external systems (Slack, Discord, Telegram bot, custom server, n8n, Make.com) when something interesting happens in the app.
- Fire on async events (new row in a DB, scheduled job result, user action) without coupling the user to a specific SaaS provider.
- Survive transient receiver failures without losing events.
- Give the user an in-app audit trail of every delivery attempt.

The pattern is: user configures a single webhook URL in settings → app fires `POST` to that URL on each event → app logs every attempt → user can replay / inspect / clear the log.

## Architecture at a glance

```
┌─────────────────────────────────────────────────────────────────┐
│                          Next.js app                            │
├─────────────────────────────────────────────────────────────────┤
│  lib/crypto/notifications.ts   → notify(), testWebhook(), log  │
│  app/api/notifications/webhook/route.ts   → CRUD config + log  │
│  app/api/notifications/webhook/test/route.ts → one-shot probe   │
│  lib/crypto/scheduler.ts        → fires after each sync        │
│  app/api/exchanges/[id]/sync/  → fires after manual sync      │
│  app/settings/page.tsx         → full UI: URL, threshold, log │
├─────────────────────────────────────────────────────────────────┤
│  SQLite:
│    settings table       → stores webhook_url, pnl_milestone_threshold, pnl_milestone_last
│    webhook_log table    → id, type, url, status, ok, attempt, payload, error, ts
└─────────────────────────────────────────────────────────────────┘
        │
        │  POST + X-TradingX-Event header + JSON body
        ▼
   User's endpoint (Slack / Discord / custom server)
```

## Event envelope (stable contract)

Every event is a single `POST` with:

- **Header `X-TradingX-Event`**: one of `order_fill`, `position_open`, `position_close`, `pnl_milestone` (or `test` for the manual probe).
- **Header `Content-Type: application/json`**
- **Header `User-Agent: TradingX-Webhook/1.0`** (so receivers can identify the source)
- **Body** (JSON, 4 KB max):

```json
{
  "type": "order_fill",
  "ts": "2026-06-21T07:45:28.518Z",
  "data": {
    "app": "tradingx",
    "tradeId": "abc123",
    "exchangeId": "ex_seed",
    "symbol": "BTCUSDT",
    "side": "Buy",
    "qty": 0.05,
    "price": 65000,
    "pnl": 240,
    "ts": 1719000000000
  }
}
```

Receivers should ignore unknown fields (`data` is a freeform `Record<string, any>` per event type) and switch on the `type` field. Never use a `version` field in the body — bump the `User-Agent` and add fields.

## Core API

```ts
// lib/crypto/notifications.ts
import { db, getSetting, setSetting } from "./db";

const MAX_ATTEMPTS = 3;
const RETRY_BACKOFF_MS = [0, 2_000, 8_000];   // immediate, +2s, +8s
const REQUEST_TIMEOUT_MS = 5_000;

export function isEnabled(): boolean {
  return !!getSetting("webhook_url");
}

export function getWebhookUrl(): string | undefined {
  return getSetting("webhook_url");
}

export function setWebhookUrl(url: string) {
  setSetting("webhook_url", url.trim());
}

export function getMilestoneThreshold(): number {
  const v = parseFloat(getSetting("pnl_milestone_threshold") ?? "1000");
  return isNaN(v) ? 1000 : v;
}

export function setMilestoneThreshold(v: number) {
  setSetting("pnl_milestone_threshold", String(Math.max(0, v)));
}

/** Fire-and-forget delivery. Logs every attempt to webhook_log. */
export function notify(type: WebhookEventType, data: Record<string, any>) {
  const url = getWebhookUrl();
  if (!url) return;                        // not configured → silent no-op
  void deliver(url, type, data);           // never block the caller
}

async function deliver(url: string, type: string, data: Record<string, any>) {
  const payload = { type, ts: new Date().toISOString(), data: { ...data, app: "tradingx" } };
  const body = JSON.stringify(payload);

  for (let attempt = 0; attempt < MAX_ATTEMPTS; attempt++) {
    if (RETRY_BACKOFF_MS[attempt] > 0) await sleep(RETRY_BACKOFF_MS[attempt]);
    try {
      const ctrl = new AbortController();
      const t = setTimeout(() => ctrl.abort(), REQUEST_TIMEOUT_MS);
      const res = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "User-Agent": "TradingX-Webhook/1.0",
          "X-TradingX-Event": type,
        },
        body,
        signal: ctrl.signal,
      });
      clearTimeout(t);
      logDelivery({ type, url, status: res.status, ok: res.ok, attempt: attempt + 1, payload: body, error: res.ok ? null : `HTTP ${res.status}` });
      if (res.ok) return;
    } catch (e: any) {
      logDelivery({ type, url, status: 0, ok: false, attempt: attempt + 1, payload: body, error: e?.message ?? "fetch failed" });
    }
  }
}

/** Used by the Settings → "Test webhook" button. Synchronous-ish with latency. */
export async function testWebhook(url: string): Promise<{ ok: boolean; status: number; ms: number; error?: string }> {
  const t0 = Date.now();
  const payload = { type: "order_fill", ts: new Date().toISOString(), data: { app: "tradingx", test: true, message: "Hello from TradingX!" } };
  try {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), REQUEST_TIMEOUT_MS);
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json", "User-Agent": "TradingX-Webhook/1.0", "X-TradingX-Event": "test" },
      body: JSON.stringify(payload),
      signal: ctrl.signal,
    });
    clearTimeout(timer);
    const ms = Date.now() - t0;
    logDelivery({ type: "order_fill", url, status: res.status, ok: res.ok, attempt: 1, payload: JSON.stringify(payload), error: res.ok ? null : `HTTP ${res.status}` });
    return { ok: res.ok, status: res.status, ms };
  } catch (e: any) {
    const ms = Date.now() - t0;
    logDelivery({ type: "order_fill", url, status: 0, ok: false, attempt: 1, payload: JSON.stringify(payload), error: e?.message ?? "fetch failed" });
    return { ok: false, status: 0, ms, error: e?.message ?? "fetch failed" };
  }
}
```

Three rules to keep this safe:

1. **`notify()` is fire-and-forget** — never `await` it from request handlers. The `void deliver(...)` is intentional.
2. **Always retry transient errors, never lose events silently** — but cap at 3 attempts with growing backoff. After that, log + give up. The user can replay manually if needed (or you can add a "re-deliver failed events" feature later).
3. **Always set a timeout** on the fetch. A hung receiver is worse than a dropped event. 5s is a good default; bump for slower endpoints (Slack can sometimes take 10s under load).

## Detecting NEW events (the diff pattern)

The most important pattern: **don't fire on every sync — fire only on NEW events.** The scheduler runs every 10 minutes and re-fetches the same trade window. Naive code would spam the user's webhook with duplicates.

```ts
// In scheduler.ts or manual sync handler:
const fetched = await a.getClosedTrades({ startTime: since, limit: 100 });

// Snapshot existing IDs BEFORE upsert so we can detect newly-arrived rows
const existingIds = new Set(
  listTrades({ exchangeId: c.id, limit: 1000 }).map((t) => t.id),
);
const newCount = detectNewTradeFills(
  c.id,
  fetched.map((t) => ({ id: t.id, symbol: t.symbol, side: t.side, qty: t.qty, price: t.price, pnl: t.pnl, ts: t.ts })),
  existingIds,
);
upsertTrades(fetched, c.id);
```

`detectNewTradeFills()` from `notifications.ts`:

```ts
export function detectNewTradeFills(
  exchangeId: string,
  fetched: Array<{ id: string; symbol: string; side: string; qty: number; price: number; pnl: number; ts: number }>,
  existingIds: Set<string>,
) {
  const newOnes = fetched.filter((t) => !existingIds.has(t.id));
  for (const t of newOnes) {
    notify("order_fill", {
      exchangeId,
      tradeId: t.id,
      symbol: t.symbol,
      side: t.side,
      qty: t.qty,
      price: t.price,
      pnl: t.pnl,
      ts: t.ts,
    });
  }
  return newOnes.length;
}
```

Same pattern for positions — diff old snapshot vs new, fire `position_open` for new keys, `position_close` for keys that disappeared or went to size 0.

## P&L milestone: fire once per threshold crossing

Don't spam the user with a `pnl_milestone` event every sync. Track the last-fired bucket in settings and only fire when crossing a new multiple of the threshold:

```ts
export function maybeFirePnlMilestone(totalRealisedPnl: number) {
  const threshold = getMilestoneThreshold();
  if (threshold <= 0) return;
  const lastKey = "pnl_milestone_last";
  const last = parseFloat(getSetting(lastKey) ?? "0");
  const currentBucket = Math.floor(totalRealisedPnl / threshold);
  const lastBucket = Math.floor(last / threshold);
  if (currentBucket > lastBucket && currentBucket > 0) {
    notify("pnl_milestone", {
      threshold,
      cumulativePnl: totalRealisedPnl,
      bucket: currentBucket,
    });
    setSetting(lastKey, String(currentBucket * threshold));
  }
}
```

Default threshold is 1000 USD. If a user's P&L goes from 950 to 2100 in two trades, they get one notification ("2K reached") not two separate fires.

## Delivery log table (the audit trail)

```sql
CREATE TABLE IF NOT EXISTS webhook_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT NOT NULL,                  -- 'order_fill' | 'position_open' | 'position_close' | 'pnl_milestone'
  url TEXT NOT NULL,
  status INTEGER NOT NULL,              -- HTTP status code (0 = network error / timeout)
  ok INTEGER NOT NULL,                  -- 0 | 1
  attempt INTEGER NOT NULL,             -- 1..3
  payload TEXT,                        -- full JSON body sent
  error TEXT,                          -- null on success, message on failure
  ts TEXT NOT NULL                      -- ISO 8601
);
CREATE INDEX IF NOT EXISTS idx_webhook_log_ts ON webhook_log(ts DESC);
```

The UI shows the last 50 rows in a table (Time / Event / Status / Error). User can clear the log with a single button. **Don't** auto-prune the log — disk is cheap, and a user who comes back after a week wants to see what happened while they were away.

## Settings UI: URL, threshold, test, log

The Settings page needs four things wired:

1. **Webhook URL** text input (with placeholder showing the format).
2. **P&L milestone threshold** number input with helper text ("Fires once per multiple (e.g. 1000 → 1K, 2K, 3K…)").
3. **Save** button (green primary) + **Test** button (secondary, triggers one shot, shows latency inline).
4. **Delivery log** table with columns Time / Event / Status (color-coded 200 ✓ green / error ✗ red) / Error message.

The "Test" button is critical — without it, the user can't tell if their endpoint works until the next real event arrives. Always show the response latency in milliseconds (e.g. `✓ 200 OK · 38ms`) so they can see if their endpoint is slow.

## API routes

```ts
// app/api/notifications/webhook/route.ts
import { clearWebhookLog, getMilestoneThreshold, getWebhookUrl, listWebhookLog, setMilestoneThreshold, setWebhookUrl } from "@/lib/crypto/notifications";
import { fail, ok, readJson, safe } from "@/lib/crypto/api";

export const dynamic = "force-dynamic";

export async function GET() {
  return safe(async () => ok({ url: getWebhookUrl() ?? "", threshold: getMilestoneThreshold(), log: listWebhookLog(50) }));
}

export async function POST(req: Request) {
  return safe(async () => {
    const body = await readJson<{ url?: string; threshold?: number }>(req);
    if (typeof body.url === "string") {
      const trimmed = body.url.trim();
      if (trimmed && !/^https?:\/\//i.test(trimmed)) return fail("URL must start with http:// or https://");
      setWebhookUrl(trimmed);
    }
    if (typeof body.threshold === "number" && !isNaN(body.threshold)) {
      setMilestoneThreshold(Math.max(0, body.threshold));
    }
    return ok({ url: getWebhookUrl() ?? "", threshold: getMilestoneThreshold() });
  });
}

export async function DELETE() {
  return safe(async () => { clearWebhookLog(); return ok({ cleared: true }); });
}
```

```ts
// app/api/notifications/webhook/test/route.ts
import { testWebhook } from "@/lib/crypto/notifications";

export async function POST(req: Request) {
  return safe(async () => {
    const body = await readJson<{ url?: string }>(req);
    const url = body.url?.trim();
    if (!url) return fail("url required");
    if (!/^https?:\/\//i.test(url)) return fail("URL must start with http:// or https://");
    return ok(await testWebhook(url));
  });
}
```

## Verification recipe (the only one that works end-to-end)

You can't test webhooks against real Slack/Discord from a self-hosted server. You need a local listener. Two options:

**Option 1: Public webhook testers**

- [https://webhook.site](https://webhook.site) — paste the URL into the Settings → Test webhook, see the request land in real time.
- [https://requestbin.com](https://requestbin.com) (now pipedream) — similar.

**Option 2: Local netcat/python listener + Docker host trick**

A subtle Docker networking issue: when you run a listener on the **host** (e.g. `python3 -m http.server 9877` in another terminal), the **container** can't reach `127.0.0.1:9877` — that's the loopback of the container, not the host. The container's gateway to the host is at `172.31.0.1` (verify with `docker inspect <name> --format '{{.NetworkSettings.Gateway}}'`).

```bash
# Terminal 1 — host listener that prints every request
cat > /tmp/webhook_listener.py << 'EOF'
import http.server, json
class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n).decode()
        print("=== WEBHOOK RECEIVED ===", flush=True)
        print("Path:", self.path, flush=True)
        print("X-TradingX-Event:", self.headers.get("X-TradingX-Event"), flush=True)
        print("Body:", body, flush=True)
        self.send_response(200); self.send_header("Content-Type","application/json"); self.end_headers()
        self.wfile.write(b'{"ok":true}')
    def log_message(self, *a, **k): pass
http.server.HTTPServer(("0.0.0.0", 9877), H).serve_forever()
EOF
python3 /tmp/webhook_listener.py &

# Terminal 2 — fire from the host (Next.js container) toward the listener
curl -X POST -H "Content-Type: application/json" \
  -d '{"url":"http://172.31.0.1:9877/test"}' \
  http://localhost:8799/api/notifications/webhook/test

# Expect:
#   {"ok":true,"data":{"ok":true,"status":200,"ms":38}}
# And in Terminal 1:
#   === WEBHOOK RECEIVED ===
#   Path: /test
#   X-TradingX-Event: test
#   Body: {"type":"order_fill","ts":"2026-06-21T07:45:28.518Z","data":{"app":"tradingx",...}}
```

This proves the entire path: app → notify() → fetch → host listener → response → log. The same flow works against Slack/Discord/etc. — just point the URL at the real webhook URL.

**Why not just use `host.docker.internal`?** It works on Docker Desktop (Mac/Windows) but **not** reliably on Linux Docker Engine — the default bridge network doesn't always resolve it. The gateway IP `172.31.0.1` (or whatever `docker inspect` reports) always works.

## Common pitfalls

### Don't await `notify()` from request handlers

`notify()` returns `void` (it's `void deliver(...))`. The retry loop takes 0–10s in the worst case. If you `await notify()` from a request handler, the user's HTTP request hangs for 10 seconds on every webhook. Fire-and-forget is mandatory.

### Don't fire on every sync — diff against the existing state

The scheduler re-fetches the same trade window every 10 minutes. If you `notify()` for every row in `fetched`, the user gets the same `order_fill` event 6 times an hour until they unsubscribe. Always diff against `existingIds` before firing.

### Don't store the webhook URL in localStorage

It's a server-side setting. Storing it client-side means each browser session has its own URL, and a user opening a new tab loses their config. Use the SQLite `settings` table (or any server-side store) instead.

### Don't allow `file://` or other dangerous protocols in the URL

The `setWebhookUrl()` validator should reject anything that doesn't start with `http://` or `https://`. `file://` would let an attacker read local files if the fetch implementation ever supported it. `javascript:` and `data:` would execute in the SSR context. Always `if (!/^https?:\/\//i.test(trimmed)) return fail(...)`.

### Don't log the raw body when it contains user secrets

The `webhook_log.payload` column stores the full request body. That's fine for trading events, but if you ever extend to fire on a "user shared their API key" event, redact the body before logging. Easy to forget.

### Bind-mount the data dir or webhook log gets lost on `docker compose down`

The webhook log is SQLite. If you don't bind-mount `./data:/app/data` (or use a named volume), every `docker compose down` wipes the audit trail. This is true for all SQLite-backed state, but the webhook log is especially bad to lose because it's the only place a user can see *why* a notification didn't fire.

### Don't grant withdrawal permission to demo API keys

If the app exposes a "Connect with testnet key" path, that key still shouldn't have withdrawal scope. UI: red warning if the user toggles "Allow withdrawal" on, never default-enabled, and surface the warning next to the testnet toggle too.

## Reference implementation

The Tradingx v0.3 build at `/mnt/tb/1Apps/Tradingx`:

- `lib/crypto/notifications.ts` — full implementation (~250 lines).
- `app/api/notifications/webhook/route.ts` + `app/api/notifications/webhook/test/route.ts` — server surface.
- `app/settings/page.tsx` (search for `NotificationsSection`) — full UI with URL, threshold, Test button, log table, Clear log button.
- `lib/crypto/scheduler.ts` — fires after every periodic sync.
- `app/api/exchanges/[id]/sync/route.ts` — fires after manual sync.

End-to-end verified: starting a local Python listener, pointing the webhook URL at it, and clicking "Test webhook" in the Settings page returns `✓ 200 OK · 38ms` and the listener prints the full payload with the `X-TradingX-Event: test` header.

When extending this to new event types (e.g. `drawdown_breach`, `risk_limit_hit`), add the type to the `WebhookEventType` union, the event handler, and the docs in the UI. Don't change the envelope shape.
