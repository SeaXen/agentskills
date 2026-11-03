# Security Hardening + Audit Patterns

Distilled from the TradingX 10/10 audit pass (June 2026). Covers auth middleware, 9-category audit scorecard, low-CPU Docker healthcheck, widget polling optimization, nav grouping, hot-reload scheduler, keyboard shortcuts, and full DB export/import.

## 1. Auth middleware (token gate)

When an audit reveals "zero auth on all 86 API routes," add a single `AUTH_TOKEN` env gate in `middleware.ts`:

```ts
// middleware.ts
function getTokenFromReq(req: Request): string | null {
  const auth = req.headers.get("authorization");
  if (auth?.startsWith("Bearer ")) return auth.slice(7).trim();
  const xToken = req.headers.get("x-auth-token");
  if (xToken) return xToken.trim();
  const url = new URL(req.url);
  const qToken = url.searchParams.get("token");
  if (qToken) return qToken.trim();
  return null;
}

export async function middleware(req: Request) {
  const path = new URL(req.url).pathname;
  const isPublic = path === "/api/health";
  const authToken = process.env.AUTH_TOKEN;
  if (authToken && !isPublic) {
    if (getTokenFromReq(req) !== authToken) {
      return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
    }
  }
  // ... security headers + caching ...
}
```

**Client-side auto-injection** — inject the token into `window.__AUTH_TOKEN__` in `layout.tsx` so `apiFetch()` picks it up:

```tsx
<script dangerouslySetInnerHTML={{
  __html: `${process.env.AUTH_TOKEN ? `window.__AUTH_TOKEN__ = ${JSON.stringify(process.env.AUTH_TOKEN)};` : ""}`
}} />
```

**Critical: gate API routes only, NOT pages.** If you gate page HTML too, the browser gets 401 before the `<script>` can inject the token. The token injection script runs *after* page render — so pages must be public HTML, and only `/api/*` routes require the token:

```ts
// CORRECT — API-only gate
if (authToken && path.startsWith("/api/") && !isPublic) {
  if (getTokenFromReq(req) !== authToken) {
    return NextResponse.json({ ok: false, error: "Unauthorized" }, { status: 401 });
  }
}
// Pages (non-/api/ paths) are always public — the token is injected via <script>
```

If `AUTH_TOKEN` env is not set, the app runs fully open (dev/LAN mode — same as before the fix).

## 2. 9-category audit scorecard

Run these shell probes, score each category out of 10, name gaps explicitly:

```bash
# Feature breadth
find app -name 'page.tsx' | wc -l
find app/api -name 'route.ts' | wc -l

# Code quality
npx tsc --noEmit 2>&1 | grep 'error TS' | wc -l
grep -rn 'TODO\|FIXME\|HACK' app/ lib/ components/ --include='*.ts' --include='*.tsx' | wc -l
grep -rn 'console.log' app/ lib/ components/ --include='*.ts' --include='*.tsx' | grep -v NODE_ENV | wc -l

# Security
grep -c 'AUTH_TOKEN' middleware.ts
npm audit 2>/dev/null | tail -3
grep -rn 'login\|password\|jwt\|session' app/ lib/ --include='*.ts' -l

# Performance
docker stats --no-stream <container>
curl -s -o /dev/null -w '%{http_code} %{time_total}s %{size_download}bytes' http://localhost:PORT/

# Architecture
grep -c '.prepare(' lib/crypto/db.ts   # parameterized queries
grep -rn 'force-dynamic' app/api --include='route.ts' | wc -l

# DX/DevOps
ls .github/workflows/ .eslintrc.json .env.example 2>/dev/null
docker inspect --format='{{.State.Health.Status}}' <container>

# Data integrity
head -5 lib/crypto/encryption.ts
grep -c 'journal_mode = WAL' lib/crypto/db.ts

# Documentation
wc -l README.md .env.example
```

**Honest scoring rule:** if the audit finds unfixed issues, the actual score is "build clean, X issues remain — not 10/10." Never self-grade 10/10 without running these probes.

## 3. Low-CPU Docker healthcheck

User constraint: "if healthcheck make cpu use high interval skip it or optimize." Use 60s interval, not 5s:

```yaml
healthcheck:
  test: ["CMD", "node", "-e", "fetch('http://127.0.0.1:8799/api/health').then(r=>{if(!r.ok)process.exit(1)}).catch(()=>process.exit(1))"]
  interval: 60s
  timeout: 5s
  retries: 5
  start_period: 30s
mem_limit: 512m
memswap_limit: 1g
```

- 60s interval = ~0% CPU overhead (one HTTP GET per minute)
- `node -e "fetch(...)"` = no apt/wget/curl needed in the image
- `mem_limit: 512m` prevents runaway memory growth

## 4. Widget polling optimization

Three layers to cut background CPU/RAM from dashboard widgets:

### Layer 1: `useVisibilityPoll` — skip fetches when tab hidden

```ts
export function useVisibilityPoll(fn: () => void | Promise<void>, intervalMs: number, enabled = true) {
  const fnRef = useRef(fn);
  fnRef.current = fn;
  useEffect(() => {
    if (!enabled || intervalMs < 1000) return;
    let timer = setInterval(() => {
      if (document.hidden) return;  // skip when tab not visible
      void fnRef.current();
    }, intervalMs);
    document.addEventListener("visibilitychange", () => {
      if (!document.hidden) void fnRef.current();  // refetch on focus
    });
    return () => clearInterval(timer);
  }, [intervalMs, enabled]);
}
```

### Layer 2: `useApi` hook — unified fetch + request dedup

```ts
const inflight = new Map<string, Promise<any>>();
export async function apiFetch<T>(url: string, options?: RequestInit) {
  // Dedup GETs: same URL within 200ms → shared promise
  if (method === "GET") {
    const existing = inflight.get(url);
    if (existing) return existing;
    const p = fetch(url, { headers: authHeaders(), cache: "no-store" }).then(r => r.json());
    inflight.set(url, p);
    setTimeout(() => inflight.delete(url), 200);
    return p;
  }
  return fetch(url, { headers: authHeaders(), cache: "no-store" }).then(r => r.json());
}
```

### Layer 3: Settings controls

```ts
// lib/settings.ts
pauseAllRefresh: boolean;       // global kill switch
liveWidgetsRefreshSec: number;  // configurable interval (5-120s, default 15)
```

Usage in widget components:
```ts
const { settings } = useSettings();
const pollMs = Math.max(5000, (settings.liveWidgetsRefreshSec || 15) * 1000);
useVisibilityPoll(load, pollMs, auto && !settings.pauseAllRefresh);
```

## 5. Nav grouping (flat tabs → dropdowns)

When nav exceeds 20 flat tabs, group into 5-7 categories:

```ts
export type NavGroup = { label: string; short: string; items: NavItem[] };
export const NAV_GROUPS: NavGroup[] = [
  { label: "Trading", short: "TRADE", items: [/* 5-7 items */] },
  { label: "Analytics", short: "ANALYTICS", items: [/* ... */] },
  // ...
];
```

CSS-only dropdown (no JS state):
```tsx
<li className="relative group">
  <Link href={grp.items[0].href} className="...border-b-2...">
    {grp.short}
    <svg>chevron</svg>
  </Link>
  <div className="absolute top-full hidden group-hover:block z-50">
    {grp.items.map(item => <Link>...</Link>)}
  </div>
</li>
```

### Pitfall: overflow-x:auto kills dropdowns

**Symptom:** Dropdown menus are `display: none` even on hover. `getComputedStyle` shows `display: none` on the dropdown div despite `group-hover:block` being in the CSS.

**Root cause:** `overflow-x: auto` on the nav container forces `overflow-y` to `clip`/`hidden` (CSS spec: if one axis is `auto` or `scroll`, the other becomes `clip` if it was `visible`). Absolutely-positioned dropdowns extend beyond the nav's box and get clipped.

**Fix:** Use `overflow-x-auto lg:overflow-visible` — allow horizontal scroll on mobile, but let dropdowns escape on desktop:

```tsx
<nav className="px-3 md:px-5 overflow-x-auto lg:overflow-visible ...">
  <ul className="flex items-center gap-0 min-w-max lg:min-w-0 justify-start lg:justify-center">
```

For the last dropdown group (e.g. "Manage" on the right edge), align it right to prevent viewport overflow:

```tsx
<div className="absolute left-0 top-full hidden group-hover:block z-50 ..."
  style={grp.label === "Manage" ? { right: 0, left: "auto" } : undefined}
>
```

**Verify the fix** with a console probe:
```js
// Force-show the last dropdown and measure its right edge
const dd = document.querySelectorAll('nav ul li')[5].querySelector('div');
dd.style.display = 'block';
const r = dd.getBoundingClientRect();
// r.right should be < window.innerWidth
```

## 6. Hot-reload scheduler (no container restart)

Scheduler reads `sync_interval_min` from DB settings. A lightweight 60s ticker re-reads the setting and reschedules the cron task if it changed:

```ts
let currentIntervalMin = 0;
let cronTask: CronTask | null = null;

const checkSchedule = () => {
  const next = resolveIntervalMin();  // reads getSetting("sync_interval_min")
  if (next !== currentIntervalMin) {
    cronTask?.destroy();
    cronTask = cron.schedule(`*/${next} * * * *`, syncAll);
    currentIntervalMin = next;
  }
};
setInterval(checkSchedule, 60_000);  // cheap: one DB read per minute
```

Expose status via `GET /api/scheduler/status` → `{ intervalMin, lastSyncAt, isRunning }`.

## 7. Keyboard shortcuts

`g + key` pattern (Vim-style) for fast navigation:

```ts
const SHORTCUTS: Record<string, string> = {
  "g d": "/", "g t": "/trade", "g p": "/positions",
  "g o": "/orders", "g r": "/trades", "g s": "/settings",
  // ...
};
// Listen for keydown, buffer 2 chars, match against SHORTCUTS
// Skip when typing in input/textarea/select
// Press "?" for help dialog
```

Wire into Topbar with `useKeyboardShortcuts()` hook.

## 8. Full DB export/import

```ts
// GET /api/data/export — dump all tables as JSON
const tables = ["exchanges", "trades", "positions_snapshot", ...];
for (const table of tables) {
  exportData[table] = db.prepare(`SELECT * FROM ${table}`).all();
}

// POST /api/data/import — INSERT OR IGNORE for each row
const tx = db.transaction(() => {
  for (const table of IMPORTABLE) {
    for (const row of body[table]) {
      const cols = Object.keys(row);
      db.prepare(`INSERT OR IGNORE INTO ${table} (${cols.join(", ")}) VALUES (${placeholders})`).run(...values);
    }
  }
});
```

Settings UI: "Export all data" button (downloads JSON) + "Import data" file picker (uploads JSON, confirms before overwrite).
