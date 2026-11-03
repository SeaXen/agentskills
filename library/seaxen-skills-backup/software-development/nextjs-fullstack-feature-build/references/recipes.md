# Recipes — Fullstack Feature Build

Copy-paste patterns that came up in the TradingX 8-feature build. These are battle-tested snippets you can drop into a Next.js fullstack project.

## 1. PWA Setup (manifest + service worker + icons + meta)

**Files:**

- `public/manifest.json` — PWA manifest with shortcuts
- `public/sw.js` — service worker (offline shell + SWR API cache)
- `public/icon-192.png` and `public/icon-512.png` — PNG icons (any 1-color or branded)
- `app/layout.tsx` — register manifest + service worker

**`public/manifest.json`:**

```json
{
  "name": "YourApp — Full Name",
  "short_name": "YourApp",
  "description": "...",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "orientation": "any",
  "background_color": "#0a0a0a",
  "theme_color": "#22c55e",
  "categories": ["finance", "productivity"],
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "shortcuts": [
    { "name": "Positions", "url": "/positions" },
    { "name": "Trades", "url": "/trades" }
  ]
}
```

**`public/sw.js` (offline-first with stale-while-revalidate for APIs):**

```javascript
const CACHE = "yourapp-v1";
const STATIC_CACHE = "yourapp-static-v1";
const PRECACHE_URLS = ["/", "/manifest.json"];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(PRECACHE_URLS).catch(() => {}))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(
      keys.filter((k) => k !== CACHE && k !== STATIC_CACHE).map((k) => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

function isApiReadRequest(req) {
  if (req.method !== "GET") return false;
  const u = new URL(req.url);
  return u.pathname.startsWith("/api/");
}

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  // Static assets: cache-first
  if (url.pathname.startsWith("/_next/static/")) {
    event.respondWith(
      caches.open(STATIC_CACHE).then(async (cache) => {
        const cached = await cache.match(req);
        if (cached) return cached;
        try {
          const fresh = await fetch(req);
          if (fresh.ok) cache.put(req, fresh.clone());
          return fresh;
        } catch { return cached || new Response("offline", { status: 503 }); }
      })
    );
    return;
  }

  // API GETs: stale-while-revalidate
  if (isApiReadRequest(req)) {
    event.respondWith(
      caches.open(CACHE).then(async (cache) => {
        const cached = await cache.match(req);
        const network = fetch(req).then((res) => { if (res.ok) cache.put(req, res.clone()); return res; }).catch(() => null);
        return cached || (await network) || new Response(JSON.stringify({ ok: false, error: "offline" }), { status: 503, headers: { "Content-Type": "application/json" } });
      })
    );
    return;
  }

  // HTML: network-first, fallback to cache
  if (req.mode === "navigate") {
    event.respondWith(
      fetch(req).then((fresh) => { caches.open(CACHE).then((c) => c.put(req, fresh.clone())); return fresh; })
        .catch(async () => {
          const cache = await caches.open(CACHE);
          return (await cache.match(req)) || (await cache.match("/")) || new Response("offline", { status: 503 });
        })
    );
  }
});
```

**`app/layout.tsx` (add to <head>):**

```tsx
<link rel="manifest" href="/manifest.json" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
<meta name="apple-mobile-web-app-title" content="YourApp" />
<link rel="apple-touch-icon" href="/icon-192.png" />
<meta name="mobile-web-app-capable" content="yes" />

{/* at end of body */}
<script dangerouslySetInnerHTML={{ __html: `
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js').catch(() => {});
    });
  }
` }} />
```

Plus `export const metadata` includes `manifest: "/manifest.json"` and `appleWebApp: { capable: true, ... }`.

**Generate placeholder icons** (Python one-liner):

```python
import struct, zlib
def png(w, h, color=(34, 197, 94)):
    raw = b''
    for y in range(h): raw += b'\x00' + bytes(color * w)
    compressed = zlib.compress(raw)
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)) + chunk(b'IDAT', compressed) + chunk(b'IEND', b'')

for size in (192, 512):
    open(f'public/icon-{size}.png', 'wb').write(png(size, size))
open('public/icon-maskable-512.png', 'wb').write(png(512, 512))
```

## 2. Sharpe / Sortino / Calmar

```typescript
function computeRatios(pnls: number[], startingCapital: number) {
  if (pnls.length < 2) return { sharpe: null, sortino: null, calmar: null, annReturn: null, annVol: null, maxDD: null, sampleSize: pnls.length };
  const rf = 0; // crypto
  let equity = startingCapital;
  const returns: number[] = [];
  for (const pnl of pnls) {
    const r = equity > 0 ? pnl / equity : 0;
    returns.push(r);
    equity += pnl;
  }
  const n = returns.length;
  const mean = returns.reduce((s, r) => s + r, 0) / n;
  const variance = returns.reduce((s, r) => s + (r - mean) ** 2, 0) / Math.max(n - 1, 1);
  const stddev = Math.sqrt(variance);
  const downsideReturns = returns.filter((r) => r < 0);
  const downsideDev = Math.sqrt(downsideReturns.length ? downsideReturns.reduce((s, r) => s + r * r, 0) / downsideReturns.length : 0);
  const TRADES_PER_YEAR = 252;
  const annReturn = mean * TRADES_PER_YEAR;
  const annVol = stddev * Math.sqrt(TRADES_PER_YEAR);
  let peak = startingCapital, maxDD = 0, running = startingCapital;
  for (const pnl of pnls) {
    running += pnl;
    if (running > peak) peak = running;
    const dd = peak > 0 ? ((peak - running) / peak) * 100 : 0;
    if (dd > maxDD) maxDD = dd;
  }
  const sharpe = stddev > 0 ? (mean - rf) / stddev * Math.sqrt(TRADES_PER_YEAR) : null;
  const sortino = downsideDev > 0 ? (mean - rf) / downsideDev * Math.sqrt(TRADES_PER_YEAR) : null;
  const calmar = maxDD > 0 ? (annReturn * 100) / maxDD : null;
  return {
    sharpe: sharpe == null ? null : +sharpe.toFixed(2),
    sortino: sortino == null ? null : +sortino.toFixed(2),
    calmar: calmar == null ? null : +calmar.toFixed(2),
    annReturn: +(annReturn * 100).toFixed(2),
    annVol: +(annVol * 100).toFixed(2),
    downsideDev: +(downsideDev * 100).toFixed(2),
    maxDD: +maxDD.toFixed(2),
    sampleSize: n,
  };
}
```

**Interpretation thresholds (in the UI):**
- Sharpe ≥ 1 = good, ≥ 2 = great
- Sortino ≥ 2 = good, ≥ 3 = great
- Calmar ≥ 1 = good, ≥ 3 = great

## 3. RSS News Aggregation

```typescript
// lib/crypto/news.ts
export type NewsItem = {
  id: string; title: string; url: string; source: string;
  publishedAt: number; summary?: string; symbols?: string[];
};

const CACHE_TTL_MS = 5 * 60 * 1000;
let cache: { ts: number; items: NewsItem[] } | null = null;

const FEEDS = [
  { name: "CoinDesk",      url: "https://www.coindesk.com/arc/outboundfeeds/rss/" },
  { name: "The Block",     url: "https://www.theblock.co/rss.xml" },
  { name: "Cointelegraph", url: "https://cointelegraph.com/rss" },
  { name: "Decrypt",       url: "https://decrypt.co/feed" },
];

function parseRssItems(xml: string, sourceName: string): NewsItem[] {
  const out: NewsItem[] = [];
  const itemRe = /<item[\s>]([\s\S]*?)<\/item>|<entry[\s>]([\s\S]*?)<\/entry>/gi;
  let m: RegExpExecArray | null;
  while ((m = itemRe.exec(xml)) != null) {
    const block = m[1] || m[2] || "";
    const get = (re: RegExp) => { const r = re.exec(block); return r ? r[1].trim() : ""; };
    const title = stripHtml(get(/<title[^>]*>([\s\S]*?)<\/title>/i));
    const link = get(/<link[^>]*>([\s\S]*?)<\/link>/i) || get(/<link[^>]*href="([^"]+)"/i);
    const pubDate = get(/<pubDate>([\s\S]*?)<\/pubDate>/i) || get(/<published>([\s\S]*?)<\/published>/i);
    const desc = get(/<description[^>]*>([\s\S]*?)<\/description>/i) || get(/<summary[^>]*>([\s\S]*?)<\/summary>/i);
    if (!title || !link) continue;
    out.push({
      id: `${sourceName}::${link}`,
      title, url: link, source: sourceName,
      publishedAt: pubDate ? Date.parse(pubDate) || Date.now() : Date.now(),
      summary: desc ? stripHtml(desc).slice(0, 280) : undefined,
      symbols: extractSymbols(title + " " + (desc || "")),
    });
  }
  return out;
}

function stripHtml(s: string): string {
  return s.replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, "$1")
    .replace(/<[^>]+>/g, "")
    .replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&nbsp;/g, " ")
    .replace(/\s+/g, " ").trim();
}

const COMMON_TICKERS = new Set(["BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "AVAX", "MATIC", "DOT", "LINK", "TON"]);
function extractSymbols(text: string): string[] {
  const tickers = new Set<string>();
  const dollarRe = /\$([A-Z]{2,6})/g;
  let mm: RegExpExecArray | null;
  while ((mm = dollarRe.exec(text)) != null) tickers.add(mm[1].toUpperCase());
  const bareRe = /\b([A-Z]{3,5})\b/g;
  while ((mm = bareRe.exec(text)) != null) {
    if (COMMON_TICKERS.has(mm[1])) tickers.add(mm[1]);
  }
  return Array.from(tickers);
}

export async function getNews(): Promise<NewsItem[]> {
  if (cache && Date.now() - cache.ts < CACHE_TTL_MS) return cache.items;
  const all = await Promise.all(FEEDS.map(async (f) => {
    try {
      const r = await fetch(f.url, { headers: { "User-Agent": "YourApp/1.0" } });
      return r.ok ? parseRssItems(await r.text(), f.name) : [];
    } catch { return []; }
  }));
  const flat = all.flat();
  const seen = new Set<string>();
  const out: NewsItem[] = [];
  for (const item of flat) {
    const k = item.title.toLowerCase().slice(0, 60);
    if (seen.has(k)) continue;
    seen.add(k);
    out.push(item);
  }
  out.sort((a, b) => b.publishedAt - a.publishedAt);
  cache = { ts: Date.now(), items: out.slice(0, 100) };
  return cache.items;
}
```

## 4. Next.js Middleware: Cache-Control headers

**`middleware.ts`:**

```typescript
import { NextResponse } from "next/server";

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};

export async function middleware(req: Request) {
  const res = NextResponse.next();
  res.headers.set("X-Content-Type-Options", "nosniff");
  res.headers.set("Referrer-Policy", "strict-origin-when-cross-origin");
  const path = new URL(req.url).pathname;
  if (!path.startsWith("/api/")) {
    res.headers.set("Cache-Control", "public, max-age=5, s-maxage=60, stale-while-revalidate=300");
  } else {
    const method = req.method.toUpperCase();
    if (method === "GET") res.headers.set("Cache-Control", "public, max-age=0, s-maxage=10, stale-while-revalidate=30");
    else res.headers.set("Cache-Control", "no-store");
  }
  return res;
}
```

**What you CAN'T do in middleware:** Gzip response body. `res.body` mutation isn't reliably exposed in Edge runtime. To get gzip, you need nginx in front.

## 5. useAutoRefresh hook (drop-in)

```typescript
// lib/useAutoRefresh.ts
export function useAutoRefresh(
  fn: () => Promise<void>,
  intervalMs: number,
  options: { enabled?: boolean } = {}
) {
  const [tick, setTick] = useState(0);
  const [now, setNow] = useState(() => Date.now());
  const [isAuto, setIsAuto] = useState(true);
  const [busy, setBusy] = useState(false);
  const [lastRefreshAt, setLastRefreshAt] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const fnRef = useRef(fn);
  fnRef.current = fn;

  useEffect(() => {
    if (!options.enabled) return;
    let cancelled = false;
    let timer: ReturnType<typeof setTimeout> | null = null;
    const tickOnce = async () => {
      if (cancelled) return;
      setBusy(true);
      try { await fnRef.current(); if (!cancelled) setError(null); }
      catch (e: any) { if (!cancelled) setError(e?.message ?? String(e)); }
      finally { if (!cancelled) { setBusy(false); setLastRefreshAt(Date.now()); setNow(Date.now()); setTick((t) => t + 1); } }
    };
    void tickOnce();
    const loop = () => {
      if (cancelled || !isAuto) return;
      timer = setTimeout(async () => { await tickOnce(); loop(); }, intervalMs);
    };
    if (isAuto) loop();
    return () => { cancelled = true; if (timer) clearTimeout(timer); };
  }, [intervalMs, isAuto, options.enabled]);

  const refresh = async () => {
    setBusy(true);
    try { await fnRef.current(); setError(null); }
    catch (e: any) { setError(e?.message ?? String(e)); }
    finally { setBusy(false); setLastRefreshAt(Date.now()); setNow(Date.now()); setTick((t) => t + 1); }
  };

  return { tick, now, isAuto, setAuto: setIsAuto, refresh, busy, lastRefreshAt, error };
}

export function formatAgo(ts: number | null): string {
  if (ts == null) return "—";
  const s = Math.max(0, Math.floor((Date.now() - ts) / 1000));
  if (s < 5) return "just now";
  if (s < 60) return `${s}s ago`;
  const m = Math.floor(s / 60);
  if (m < 60) return `${m}m ago`;
  const h = Math.floor(m / 60);
  return `${h}h ago`;
}
```

## 6. RefreshBar component (drop-in)

```tsx
// components/RefreshBar.tsx
type Props = {
  busy: boolean; lastRefreshAt: number | null; isAuto: boolean;
  setAuto: (v: boolean) => void; refresh: () => void;
  error?: string | null; intervalMs?: number; className?: string;
};

export function RefreshBar({ busy, lastRefreshAt, isAuto, setAuto, refresh, error, intervalMs, className = "" }: Props) {
  const secs = intervalMs ? Math.round(intervalMs / 1000) : null;
  return (
    <div className={`flex items-center gap-2 text-[11px] text-fg-mute ${className}`}>
      <button onClick={() => void refresh()} disabled={busy} className="surface surface-hover px-2 py-1 rounded font-semibold disabled:opacity-50 inline-flex items-center gap-1.5">
        <span className={`inline-block w-3 h-3 ${busy ? "border-2 border-fg-mute border-t-accent-green rounded-full animate-spin" : ""}`} aria-hidden />
        <span>{busy ? "Refreshing…" : "Refresh"}</span>
      </button>
      <button onClick={() => setAuto(!isAuto)} className={`px-2 py-1 rounded font-semibold ${isAuto ? "bg-accent-greenDim text-accent-green" : "bg-bg-alt text-fg-mute"}`}>
        {isAuto ? "Auto ●" : "Auto ○"}
      </button>
      <span className="text-fg-mute">updated {formatAgo(lastRefreshAt)}</span>
      {secs != null && <span className="text-fg-faint">· every {secs}s</span>}
      {error && <span className="px-2 py-0.5 rounded bg-accent-redDim text-accent-red" title={error}>error</span>}
    </div>
  );
}
```

## 7. Economic Calendar Projection (no API)

When you need to show "next 14 days of macro events" and the actual API is paywalled, project from the standard monthly cadence:

```typescript
function nthWeekday(year: number, month: number, weekday: number, n: number): Date {
  const first = new Date(year, month, 1);
  const offset = ((weekday - first.getDay() + 7) % 7) + (n - 1) * 7;
  return new Date(year, month, 1 + offset);
}
const firstWeekday = (y, m, w) => nthWeekday(y, m, w, 1);
const lastWeekday = (y, m, w) => {
  const last = new Date(y, m + 1, 0);
  return new Date(y, m, last.getDate() - ((last.getDay() - w + 7) % 7));
};
function fmtDate(d: Date) { return d.toISOString().slice(0, 10); }

// CPI: 2nd Tuesday of month @ 08:30
events.push({ date: fmtDate(nthWeekday(y, mo, 2, 2)), time: "08:30", title: "CPI (YoY)", ... });
// NFP: first Friday @ 08:30
events.push({ date: fmtDate(firstWeekday(y, mo, 5)), time: "08:30", title: "Non-Farm Payrolls", ... });
// Core PCE: last Friday @ 08:30
events.push({ date: fmtDate(lastWeekday(y, mo, 5)), time: "08:30", title: "Core PCE", ... });
// FOMC: 15th of every month @ 14:00
events.push({ date: fmtDate(new Date(y, mo, 15)), time: "14:00", title: "FOMC rate decision", ... });
```

UI: include a note "Dates projected from standard monthly cadence — verify with linked source" and link each event to the official URL (BLS, Federal Reserve, etc).

## 8. CoinGecko Free-Tier Wrapper

```typescript
const HEADERS = { "User-Agent": "YourApp/1.0", Accept: "application/json" };
const CACHE_TTL_MS = 60_000;
let cache: { ts: number; data: any } | null = null;

async function cgJson<T = any>(path: string): Promise<T | null> {
  try {
    const r = await fetch(`https://api.coingecko.com/api/v3${path}`, { headers: HEADERS, cache: "no-store" });
    return r.ok ? await r.json() as T : null;
  } catch { return null; }
}

export async function getTopMarkets(limit = 100) {
  if (cache && Date.now() - cache.ts < CACHE_TTL_MS) return cache.data.slice(0, limit);
  const data = await cgJson(`/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=${limit}&page=1&sparkline=true&price_change_percentage=24h`);
  if (!data) return [];
  cache = { ts: Date.now(), data };
  return data;
}
```

Note: CoinGecko free API sometimes blocks default `fetch` User-Agent. Always send a custom one.
