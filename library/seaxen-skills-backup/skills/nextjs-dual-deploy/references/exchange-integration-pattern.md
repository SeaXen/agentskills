# Authenticated multi-exchange integration on Next.js

Reference architecture for adding real exchange (or any signed-REST third-party) integrations on top of the `nextjs-dual-deploy` shell. Captured from the **Tradingx** build at `/mnt/tb/1Apps/Tradingx`, which integrated Bybit + Binance + OKX + Bitget + MEXC with encrypted API key storage, auto-imported historical trades, and surfaced live positions and orders in the dashboard.

Use this when the app needs to:

- Store user-supplied API credentials for a third-party service at rest.
- Sign requests to multiple endpoints of that service (HMAC-SHA256 is the common case).
- Display live data from those endpoints in a Next.js dashboard.
- Auto-sync state on a schedule (cron-style) without managing an external worker.
- Allow the user to place side-effecting requests (orders, posts, deploys) with the same stored credentials.

## Architecture at a glance

```
┌─────────────────────────────────────────────────────────────────┐
│                         Next.js app                              │
├─────────────────────────────────────────────────────────────────┤
│ app/api/exchanges/route.ts     → POST creates encrypted record  │
│ app/api/exchanges/[id]/test/route.ts → smoke-tests creds        │
│ app/api/exchanges/[id]/sync/route.ts → manual import trigger    │
│ app/api/positions/route.ts     → aggregate open positions       │
│ app/api/orders/route.ts        → list + place orders             │
│ app/api/market/route.ts        → public ticker (no auth)         │
│ app/api/alerts/route.ts        → user-defined alerts CRUD        │
│ app/api/alerts/check/route.ts  → evaluate alert conditions       │
│ app/api/scanner/route.ts       → top movers/losers/volume        │
│ app/api/watchlist/route.ts     → user watchlist CRUD             │
│ app/api/attribution/route.ts   → PnL by tag/exchange/symbol      │
├─────────────────────────────────────────────────────────────────┤
│ lib/crypto/                                                       │
│   types.ts          — ExchangeAdapter interface + DTOs          │
│   encryption.ts     — AES-256-GCM with env-var master key       │
│   db.ts             — better-sqlite3 schema + queries           │
│   http.ts           — fetch wrapper, HMAC helpers                │
│   bybit.ts          — ExchangeAdapter implementation            │
│   binance.ts        — ExchangeAdapter implementation            │
│   okx.ts            — ExchangeAdapter (passphrase required)    │
│   bitget.ts         — ExchangeAdapter (passphrase + paptrading) │
│   mexc.ts           — ExchangeAdapter (no passphrase)          │
│   alerts.ts         — alert engine + history + auto-poll        │
│   index.ts          — adapterFor(id) factory                    │
│   scheduler.ts      — node-cron background sync                 │
│   boot.ts           — idempotent startScheduler()               │
│   warmup.ts         — import-this-to-trigger-boot side-effect   │
└─────────────────────────────────────────────────────────────────┘
                  │
                  ▼  HTTPS + HMAC headers
       Bybit / Binance / OKX / Bitget / MEXC / <your service>
```

The `okx.ts` / `bitget.ts` / `mexc.ts` adapters all implement the same `ExchangeAdapter` interface as `bybit.ts` and `binance.ts`. The factory dispatches on `conn.name`. The UI, API routes, and scheduler all use `adapterFor(connectionId)` — they never import a specific adapter directly.

## Core contracts

### Adapter interface (`lib/crypto/types.ts`)

Every exchange implements the same `ExchangeAdapter` interface. Public market data and private authenticated calls share one type so the UI doesn't care which exchange is wired up:

```ts
export interface ExchangeAdapter {
  name: ExchangeName;
  getTicker(symbol: string): Promise<Ticker>;
  getAllTickers(): Promise<Ticker[]>;
  testConnection(): Promise<{ ok: boolean; permissions?: { read: boolean; trade: boolean; withdraw: boolean }; error?: string }>;
  getBalance(): Promise<AccountBalance>;
  getPositions(): Promise<Position[]>;
  getOpenOrders(symbol?: string): Promise<Order[]>;
  getClosedTrades(opts: { startTime: number; endTime?: number; limit?: number; symbol?: string }): Promise<ClosedTrade[]>;
  placeOrder(req: PlaceOrderRequest): Promise<PlaceOrderResult>;
  cancelOrder(symbol: string, orderId: string): Promise<{ ok: boolean; error?: string }>;
  closePosition(symbol: string, side: "Buy" | "Sell", qty: number): Promise<PlaceOrderResult>;
  setLeverage(symbol: string, leverage: number): Promise<{ ok: boolean; error?: string }>;
}
```

Adding a sixth exchange is a single new file in `lib/crypto/<name>.ts` plus a line in `index.ts`:

```ts
case "okx": return new OkxAdapter(creds);
case "bitget": return new BitgetAdapter(creds);
case "mexc": return new MexcAdapter(creds);
```

Don't forget to update the `ExchangeName` union in `lib/crypto/types.ts` and the `asExchangeName()` validator in `lib/crypto/api.ts` — both are exhaustive over the set of exchanges and break the build if a new variant is added without updating them.

### Factory (`lib/crypto/index.ts`)

```ts
export function adapterFor(connectionId: string): ExchangeAdapter {
  const conn = getExchange(connectionId);          // decrypts lazily via getExchange()
  if (!conn) throw new Error(`Exchange connection not found: ${connectionId}`);
  const creds: ExchangeCredentials = {
    apiKey: decrypt(conn.apiKeyCipher),
    apiSecret: decrypt(conn.apiSecretCipher),
    passphrase: conn.passphraseCipher ? decrypt(conn.passphraseCipher) : undefined,
    testnet: conn.testnet,
  };
  switch (conn.name) {
    case "bybit": return new BybitAdapter(creds);
    case "binance": return new BinanceAdapter(creds);
    case "okx": return new OkxAdapter(creds);
    case "bitget": return new BitgetAdapter(creds);
    case "mexc": return new MexcAdapter(creds);
    default: throw new Error(`Unsupported exchange: ${conn.name}`);
  }
}
```

Centralized in one file so adding an exchange is one switch arm. The UI never sees plaintext credentials — only the cipher flows through the API.

The **passphrase field** is used by **OKX and Bitget**. MEXC doesn't need one. The schema's `passphrase_cipher TEXT` column is nullable; the factory only decrypts it if it's set.

## AES-256-GCM at-rest encryption

`lib/crypto/encryption.ts` — keeps API keys encrypted on disk, with a dev-friendly fallback so a fresh install doesn't need env-var setup.

```ts
const ALG = "aes-256-gcm";
const IV_LEN = 12;   // 96 bits per NIST SP 800-38D
const TAG_LEN = 16;

function getKey(): Buffer {
  const env = process.env.ENCRYPTION_KEY;
  if (env && env.length === 64) return Buffer.from(env, "hex");      // 32-byte hex
  if (env) return scryptSync(env, "tradingx-salt", 32);              // hash arbitrary
  // Dev fallback — auto-generate and persist a key file
  const keyFile = path.join(process.cwd(), "data", ".encryption-key");
  if (fs.existsSync(keyFile)) return Buffer.from(fs.readFileSync(keyFile, "utf8").trim(), "hex");
  fs.mkdirSync(path.dirname(keyFile), { recursive: true });
  const k = randomBytes(32);
  fs.writeFileSync(keyFile, k.toString("hex"), { mode: 0o600 });
  console.warn("[tradingx] ENCRYPTION_KEY not set — generated a dev key at", keyFile);
  return k;
}

export function encrypt(plain: string): string {
  const iv = randomBytes(IV_LEN);
  const cipher = createCipheriv(ALG, getKey(), iv);
  const enc = Buffer.concat([cipher.update(plain, "utf8"), cipher.final()]);
  const tag = cipher.getAuthTag();
  return Buffer.concat([iv, tag, enc]).toString("base64");  // packed iv|tag|cipher
}

export function decrypt(cipherB64: string): string {
  const buf = Buffer.from(cipherB64, "base64");
  const iv = buf.subarray(0, IV_LEN);
  const tag = buf.subarray(IV_LEN, IV_LEN + TAG_LEN);
  const enc = buf.subarray(IV_LEN + TAG_LEN);
  const decipher = createDecipheriv(ALG, getKey(), iv);
  decipher.setAuthTag(tag);
  return Buffer.concat([decipher.update(enc), decipher.final()]).toString("utf8");
}
```

Key rules:

- **GCM, not CBC.** GCM provides authenticated encryption (integrity + confidentiality). If you store API secrets in CBC, an attacker can flip ciphertext bits and you won't notice.
- **Random IV per encryption call.** Never reuse an IV with the same key — destroys GCM's security guarantee.
- **32-byte key from env var** (`ENCRYPTION_KEY=...`). The 64-character hex form is canonical.
- **Dev fallback that warns.** If no env var is set, generate a key file under `data/` and log loudly. Production deployments set the env var; the dev path is for `npm run dev` only.
- **Mask in UI.** Never round-trip plaintext to the client. List responses include only `maskedKey: "abc…xyz"` (first 4 + last 4 chars).

**`docker-compose.yml` env override for prod:**

```yaml
environment:
  - ENCRYPTION_KEY=${ENCRYPTION_KEY:?must be set in prod — generate with: openssl rand -hex 32}
```

## SQLite schema (`lib/crypto/db.ts`)

`better-sqlite3` is synchronous and zero-config — perfect for a single-container dashboard app. Schema migrations run on first DB access via the `migrate()` function:

```sql
CREATE TABLE exchanges (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  label TEXT NOT NULL,
  testnet INTEGER NOT NULL DEFAULT 0,
  api_key_cipher TEXT NOT NULL,
  api_secret_cipher TEXT NOT NULL,
  passphrase_cipher TEXT,
  perm_read INTEGER DEFAULT 1,
  perm_trade INTEGER DEFAULT 0,
  perm_withdraw INTEGER DEFAULT 0,
  created_at TEXT NOT NULL,
  last_sync_at TEXT,
  last_sync_status TEXT,
  last_sync_error TEXT
);

CREATE TABLE trades (
  id TEXT NOT NULL, exchange_id TEXT NOT NULL,
  order_id TEXT, symbol TEXT NOT NULL, side TEXT NOT NULL,
  qty REAL NOT NULL, price REAL NOT NULL,
  fee REAL DEFAULT 0, fee_currency TEXT, pnl REAL DEFAULT 0,
  ts INTEGER NOT NULL, imported_at TEXT NOT NULL, raw TEXT,
  PRIMARY KEY (exchange_id, id),                    -- dedup on re-sync
  FOREIGN KEY (exchange_id) REFERENCES exchanges(id) ON DELETE CASCADE
);
CREATE INDEX idx_trades_ts ON trades(ts DESC);

CREATE TABLE positions_snapshot (
  id TEXT PRIMARY KEY,                              -- `${exchange_id}:${symbol}:${side}`
  exchange_id TEXT NOT NULL, symbol TEXT NOT NULL, ...
  ts INTEGER NOT NULL, snapshot_at TEXT NOT NULL
);
```

Two design choices worth highlighting:

1. **Composite primary key on trades** `(exchange_id, id)` — the same trade ID can exist across multiple connections if the user wires up two accounts. `INSERT OR REPLACE` dedupes automatically.
2. **`raw JSON column`** stores the full exchange payload. When the adapter mapping misses a field (new exchange feature), you can backfill later without re-fetching.

**Beyond the bare exchange tables**, a serious trading dashboard adds four more tables for the "differentiator" features:

```sql
-- Per-trade labels for attribution (e.g. "breakout", "scalp", "fomo")
CREATE TABLE trade_tags (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  trade_id TEXT NOT NULL,
  exchange_id TEXT NOT NULL,
  tag TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  UNIQUE(trade_id, exchange_id, tag)
);

-- User-defined alerts (price/funding/PnL/drawdown)
CREATE TABLE alerts (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,           -- 'price' | 'funding' | 'pnl' | 'drawdown'
  symbol TEXT,                  -- nullable for portfolio-wide alerts
  threshold REAL NOT NULL,
  direction TEXT NOT NULL,      -- 'above' | 'below' | 'equals'
  enabled INTEGER NOT NULL DEFAULT 1,
  note TEXT,
  last_value REAL,
  last_checked_at INTEGER,
  last_triggered_at INTEGER,
  trigger_count INTEGER DEFAULT 0,
  created_at INTEGER NOT NULL
);
CREATE TABLE alert_history (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  alert_id TEXT NOT NULL,
  value REAL NOT NULL,
  message TEXT,
  ts INTEGER NOT NULL,
  FOREIGN KEY (alert_id) REFERENCES alerts(id) ON DELETE CASCADE
);

-- User watchlist (symbols not yet traded)
CREATE TABLE watchlist (
  id TEXT PRIMARY KEY,
  symbol TEXT NOT NULL,
  exchange TEXT,
  note TEXT,
  sort_order INTEGER DEFAULT 0,
  created_at INTEGER NOT NULL
);
```

## HMAC request signing pattern

The five exchanges use HMAC-SHA256 with different conventions:

| Exchange | What you sign | Where it goes |
|---|---|---|
| Bybit V5 | `timestamp + apiKey + recvWindow + payload` | `X-BAPI-SIGN` header |
| Binance USDⓈ-M | `query string with timestamp + recvWindow` | `signature` query param |
| OKX V5 | `timestamp + method + path + body` | `OK-ACCESS-SIGN` header |
| Bitget V2 | `timestamp + method + path + query/body` | `ACCESS-SIGN` header (passphrase via `ACCESS-PASSPHRASE`) |
| MEXC | `timestamp + apiKey + recvWindow + query/body` | signature query/body param |

The `http.ts` helper covers all of these:

```ts
export function hmacSha256Hex(secret: string, payload: string): string {
  return createHmac("sha256", secret).update(payload).digest("hex");
}

export class HttpError extends Error {
  constructor(public status: number, public body: string, public url: string) { ... }
}

export async function http<T>(url: string, init: RequestInit = {}, timeoutMs = 15000): Promise<T> {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), timeoutMs);     // always set a timeout
  try {
    const res = await fetch(url, { ...init, signal: ctrl.signal });
    const text = await res.text();
    if (!res.ok) throw new HttpError(res.status, text, url);
    try { return JSON.parse(text) as T; } catch { return text as any; }
  } finally { clearTimeout(t); }
}
```

Always set `timeoutMs` on authenticated calls — the exchange can stall mid-request, and you don't want a hung request to consume a Node worker forever.

**Demo/sandbox flags** vary too:

- **Bybit** swaps the base URL (`api-testnet.bybit.com` vs `api.bybit.com`).
- **Binance** swaps the base URL (`testnet.binancefuture.com` vs `fapi.binance.com`).
- **OKX** uses the same base URL with a header (`x-simulated-trading: 1`) — but only on accounts that have "simulated trading" enabled in their dashboard.
- **Bitget** uses the same base URL with a header (`paptrading: 1`) — applied automatically when the user creates the key in demo mode.
- **MEXC** has **no futures testnet** — demo mode for MEXC means a small mainnet position only.

## Public-market fallback when no auth is wired up

A subtle UX trap: if `/api/market?symbol=BTCUSDT` requires an authenticated adapter, the trade ticket page can't show live prices until the user adds an API key. That's hostile. Solve it with a public fallback:

```ts
// app/api/market/route.ts
export async function GET(req: Request) {
  const symbol = new URL(req.url).searchParams.get("symbol");
  const conns = listExchanges();
  const target = conns[0];                                  // any connected

  if (symbol) {
    if (target) return ok(await adapterFor(target.id).getTicker(symbol));
    return ok(await bybitPublicTicker(symbol));              // direct REST, no auth
  }
  if (target) return ok({ tickers: await adapterFor(target.id).getAllTickers() });
  return ok({ tickers: await bybitAllTickers() });           // public bulk fetch
}
```

`bybitPublicTicker()` is a thin wrapper around `https://api.bybit.com/v5/market/tickers?category=linear&symbol=BTCUSDT` with no signing. Result: the trade ticket, portfolio widget, and dashboard ticker all show live BTC/ETH/etc. the moment the page loads, even before the user connects an account.

## Background scheduler (`lib/crypto/scheduler.ts`)

For periodic re-sync of historical trades and position snapshots. Two-step boot to avoid spawning multiple timers:

```ts
// boot.ts — single-start guard
let _started = false;
export function ensureStarted() {
  if (_started) return;
  _started = true;
  try { startScheduler(); } catch (e) { console.error("scheduler boot failed", e); }
}

// warmup.ts — side-effect import
import "server-only";
import { ensureStarted } from "./boot";
ensureStarted();

// scheduler.ts
import * as cron from "node-cron";

let started = false;
export function startScheduler() {
  if (started) return;
  started = true;
  const intervalMinutes = parseInt(process.env.SYNC_INTERVAL_MIN ?? "10", 10);

  const syncAll = async () => {
    for (const c of listExchanges()) {
      try {
        setSyncResult(c.id, "running");
        const a = adapterFor(c.id);
        const pos = await a.getPositions();
        savePositionSnapshot(c.id, pos);
        const last = getLatestTradeTs(c.id) || (Date.now() - 7 * 86400_000);
        const since = Math.max(last, Date.now() - 30 * 86400_000);
        const fetched = await a.getClosedTrades({ startTime: since, limit: 100 });
        if (fetched.length > 0) upsertTrades(fetched, c.id);
        setSyncResult(c.id, "ok");
      } catch (e) {
        setSyncResult(c.id, "error", e?.message ?? "sync failed");
      }
    }
  };

  setTimeout(syncAll, 3000);                                 // first run shortly after boot
  cron.schedule(`*/${Math.max(intervalMinutes, 1)} * * * *`, syncAll);
}
```

Then trigger the boot by importing `warmup` from any API route that's likely to be hit early:

```ts
// app/api/trades/route.ts
import "@/lib/crypto/warmup";   // starts the scheduler on first import
```

The boot is **idempotent** — even if `warmup` is imported from many routes, the scheduler starts once. Don't try to put `setInterval` directly inside a Next.js route handler — the runtime can re-instantiate handlers and you'll get duplicate timers.

## Live widget pattern (auto-refresh + hover-to-cancel)

Dashboard widgets that show real-time data without overwhelming the user:

```tsx
"use client";
import { useEffect, useState } from "react";

export function OpenOrdersWidget() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [auto, setAuto] = useState(true);

  useEffect(() => {
    const load = async () => {
      const r = await fetch("/api/orders", { cache: "no-store" });
      const j = await r.json();
      if (j.ok) setOrders(j.data.orders);
    };
    load();
    if (!auto) return;
    const t = setInterval(load, 5000);                      // 5s for positions/orders
    return () => clearInterval(t);
  }, [auto]);

  return (
    <div className="surface p-4">
      {/* ... */}
      <button onClick={cancel} className="opacity-0 group-hover:opacity-100">
        cancel
      </button>
      <div className="flex justify-between">
        <label><input type="checkbox" checked={auto} onChange={...} />live</label>
        <button onClick={load}>refresh</button>
      </div>
    </div>
  );
}
```

Three rules:

1. **`cache: "no-store"`** on every fetch. Next.js's default fetch cache would otherwise return stale data.
2. **Always include a "live" toggle and a manual refresh button.** Auto-refresh is great until the user wants to read a number without it jumping.
3. **Hover-to-reveal cancel buttons** keep the UI clean. Inline always-visible buttons crowd the widget.

## The "differentiator" layer above bare exchange integration

A serious crypto dashboard needs more than just connected exchanges — it needs the features that make the user come back every day. Add these on top of the adapter pattern once the basics work:

### 1. Alerts engine (`lib/crypto/alerts.ts`)

```ts
export async function checkAlerts(opts: { alertId?: string }): Promise<{
  checked: number;
  triggered: number;
  results: Array<{ id: string; kind: string; symbol: string | null; value: number | null; triggered: boolean; message?: string }>;
}> {
  // 1. Load all enabled alerts
  // 2. For each one, fetch the current value (public market endpoint, funding, or trade stats)
  // 3. Compare against threshold + direction ('above' / 'below' / 'equals')
  // 4. If it crossed since last check, record alert_history + bump trigger_count + fire webhook notification
  // 5. Update last_value, last_checked_at, last_triggered_at
}
```

The **cross-detection logic** is the subtle bit — fire on transition, not every time the condition holds:

```ts
function didCross(alert: Alert, newValue: number): boolean {
  if (alert.lastValue == null) {
    // First check — trigger if condition already matches
    return matchDirection(alert.direction, newValue, alert.threshold);
  }
  const wasOnTriggerSide = matchDirection(alert.direction, alert.lastValue, alert.threshold);
  const isOnTriggerSide = matchDirection(alert.direction, newValue, alert.threshold);
  return wasOnTriggerSide !== isOnTriggerSide && isOnTriggerSide;
}
```

Expose via:
- `POST /api/alerts` (CRUD)
- `POST /api/alerts/[id]` PATCH/DELETE
- `POST /api/alerts/check` (manual evaluation)
- Optional `startAlertPolling()` interval (env-gated with `ALERT_AUTOPOLL=1`)

### 2. Watchlist (`app/api/watchlist/route.ts`)

Simple CRUD on a `watchlist` table. The watchlist page fetches live prices from a public market cache so it works without any exchange connected:

```tsx
// On the watchlist page, fetch both /api/watchlist and /api/scanner
const map: Record<string, Ticker> = {};
for (const t of [...sj.data.gainers, ...sj.data.losers, ...sj.data.volume]) {
  map[t.symbol] = t;   // symbol → last/change/volume
}
```

### 3. Scanner (`app/api/scanner/route.ts`)

Cache a public bulk ticker fetch for 15 s, then expose `gainers` / `losers` / `volume` arrays of the top 20 each. Filter illiquid symbols (< 50k USDT turnover) so the scanner doesn't show junk.

```ts
const CACHE_TTL_MS = 15_000;
let cache: { ts: number; payload: ScannerPayload } | null = null;
```

### 4. Attribution by tag/exchange/symbol (`app/api/attribution/route.ts`)

Single SQL aggregation that joins `trade_tags` + `trades` + `exchanges`:

```sql
SELECT tt.tag AS groupKey,
       COUNT(*) AS trades,
       SUM(CASE WHEN t.pnl > 0 THEN 1 ELSE 0 END) AS wins,
       SUM(CASE WHEN t.pnl < 0 THEN 1 ELSE 0 END) AS losses,
       COALESCE(SUM(t.pnl), 0) AS pnl,
       COALESCE(SUM(t.fee), 0) AS fees
FROM trade_tags tt
JOIN trades t ON t.id = tt.trade_id AND t.exchange_id = tt.exchange_id
WHERE t.pnl IS NOT NULL AND t.ts >= ?
GROUP BY tt.tag ORDER BY pnl DESC;
```

Expose three views (by tag, by exchange, by symbol) with a `?range=7d|30d|90d|ytd|all` filter. Tagging happens inline on each row of the trades page — an `+ tag` button opens a tiny input, `Enter` saves, click-existing-tag removes.

### 5. Webhook event for fired alerts

Add `"alert"` to the `WebhookEventType` union in `lib/crypto/notifications.ts` so the existing webhook delivery pipeline can fan out alerts to Slack / Discord / Telegram with the same retry/backoff machinery that orders and positions use.

## API surface (the minimum useful set)

```ts
// exchanges
GET    /api/exchanges                       // list (masked keys)
POST   /api/exchanges                       // create (encrypts before storing)
GET    /api/exchanges/[id]                  // one (masked)
PATCH  /api/exchanges/[id]                  // update label/permissions
DELETE /api/exchanges/[id]                  // delete (trades are kept via ON DELETE CASCADE)
POST   /api/exchanges/[id]/test             // smoke-test API key
POST   /api/exchanges/[id]/sync?days=30     // manual historical import

// market data (works without auth via public fallback)
GET    /api/market?symbol=BTCUSDT           // one ticker
GET    /api/market                          // all tickers

// account + positions + orders
GET    /api/balance                         // aggregated across all connections
GET    /api/positions                       // open positions (all exchanges)
POST   /api/positions/close                 // close one
GET    /api/orders                          // open orders
POST   /api/orders                          // place new
POST   /api/orders/cancel                   // cancel by id

// analytics
GET    /api/analytics/summary               // win rate, total PnL, etc.

// alerts + watchlist + scanner + attribution (the differentiator layer)
GET    /api/alerts?history=1                // list alerts + recent history
POST   /api/alerts                          // create alert (rate-limited)
PATCH  /api/alerts/[id]                     // update threshold/enabled/etc.
DELETE /api/alerts/[id]                     // delete
POST   /api/alerts/check                    // manually evaluate all enabled
GET    /api/scanner                         // top 20 gainers/losers/volume
GET    /api/watchlist                       // list entries
POST   /api/watchlist                       // add symbol
PATCH  /api/watchlist/[id]                  // update note/sort
DELETE /api/watchlist/[id]                  // remove
GET    /api/attribution?range=30d           // PnL by tag/exchange/symbol
POST   /api/trade-tags                      // tag a trade
DELETE /api/trade-tags                      // untag a trade
GET    /api/trade-tags?tradeId=&exchangeId= // list tags for a trade
```

Each route handler follows the same envelope pattern:

```ts
return safe(async () => {
  // ... do work ...
  return ok({ ... });                        // 200 + JSON
  // or
  return fail("message", 400, { ... });      // 4xx/5xx + JSON error
});
```

The `safe()` wrapper catches thrown errors and emits `{ ok: false, error: msg }` so the client never sees an HTML stack trace.

## Common pitfalls

### Failing to pre-create `/app/data` for non-root container user

If you store SQLite at `/app/data/app.db` and run the container as `nextjs` (uid 1001), the first request that opens the DB will fail with `EACCES` on `mkdir /app/data`. Pre-create in the Dockerfile:

```dockerfile
RUN mkdir -p /app/data && chown -R nextjs:nodejs /app/data
USER nextjs
```

If you're using a host-mounted volume (`./data:/app/data`), the host directory's ownership can also block writes. Pre-`chown` on the host:

```bash
sudo chown -R 1001:1001 ./data     # match nextjs uid in container
```

Or use a named Docker volume (`tradingx-data:/app/data`) — Docker manages ownership automatically.

**After fixing permissions, also restart the container** — `better-sqlite3` caches the file handle at first `db()` call and won't pick up the new permissions until you do. See the main SKILL.md pitfall "SQLITE_READONLY after fixing file permissions — the stale-handle trap" for the full diagnostic recipe.

### `crypto.subtle` is browser-only; use `node:crypto` in API routes

Server-side `app/api/*/route.ts` files run in Node, not the browser. Use `node:crypto`:

```ts
import { createCipheriv, createDecipheriv, randomBytes } from "node:crypto";
```

Don't import from `crypto.subtle` — that throws at runtime in the Node runtime.

### The browser's `confirm()` dialog blocks subsequent browser tool calls

When using browser automation tools to click "Delete" buttons, the `confirm()` dialog often blocks the page without being dismissable. Two fixes:

1. Use a non-blocking UI (e.g., a modal with explicit buttons) for destructive actions.
2. For verification, delete records via direct DB access or `curl -X DELETE` instead of through the UI.

Don't assume your browser tool can dismiss native `confirm()` dialogs reliably.

### Timeouts on tests against real exchanges

`curl` to your local app while the app is mid-call to a slow exchange can time out. Two mitigations:

- Set `--max-time 10` (or lower) on every `curl` so a hung exchange call doesn't freeze your verification loop.
- Treat a 500 from the app as "exchange timed out" rather than "app is broken" — check the app logs to confirm.

### Adding a new exchange: the type-union leak

When you add a sixth `ExchangeName` literal, three things break typecheck until you update them:

1. `lib/crypto/types.ts` — `ExchangeName` union literal.
2. `lib/crypto/api.ts` — `asExchangeName(x)` validator (returns the literal type).
3. `app/api/signals/route.ts` — `SignalBody.exchange` literal in the inbound webhook schema.
4. `app/settings/page.tsx` — example JSON in the webhook docs section.

`grep -rn "bybit.*binance.*okx" --include='*.ts' --include='*.tsx'` finds all of them. Add the new literal in each place.

## Reference implementation

The canonical example is `/mnt/tb/1Apps/Tradingx`:

- 21 pages, ~36 API routes, 5 exchange adapters (Bybit + Binance + OKX + Bitget + MEXC), AES-256-GCM encryption, SQLite, node-cron scheduler, Docker on port 8799.
- `lib/crypto/{types,encryption,db,http,bybit,binance,okx,bitget,mexc,alerts,index,scheduler,boot,warmup}.ts` — the full architecture in one folder.
- `app/api/{exchanges,market,positions,orders,balance,trades,analytics,alerts,alerts/check,scanner,watchlist,attribution,trade-tags,portfolios,journal,goals,backtest,reviews,signals,notifications}/` — server surface.
- `app/{exchanges,positions,orders,trade,trades,trade-entry,analytics,daily-review,missed-trades,milestones,portfolios,journal,goals,backtest,alerts,watchlist,scanner,attribution,...}/page.tsx` — UI uses one shared `<Topbar />` chrome with no sidebar.

When adapting this pattern to a new domain (stocks, social media, cloud providers), the shape stays the same:

1. Define an `Adapter` interface for your service.
2. Implement one file per service variant.
3. Encrypt credentials with AES-256-GCM (or equivalent at-rest encryption).
4. Use SQLite (or any embedded DB) for connection state + imported data.
5. Provide a public fallback for read-only market/ticker endpoints.
6. Schedule incremental sync via `node-cron` from a server-only warmup module.
7. Add the differentiator layer (alerts, watchlist, scanner, attribution) once the basics work.
8. UI: live widgets with `cache: "no-store"`, auto-refresh toggle, hover-to-reveal actions.