# Data-page auto-refresh: hook + RefreshBar pattern

The single biggest gap you will find on any self-hosted data dashboard you
audit: pages mount, fetch once, then never update again unless the user
manually reloads. For dashboards that show prices, positions, bot status,
alerts, or wallet balances this is a real bug — the user sees stale data
and either doesn't notice or has to hard-reload every minute. This file
captures the fix that worked across a 27-page dashboard with 16 data
pages and the related bugs that surfaced during the audit.

## When you need this

- Auditing a dashboard and pages render stale data on tab return.
- Adding any new page that calls a `/api/...` endpoint and displays the
  result. **If the page is data-driven, it must auto-refresh.** A page
  without a refresh button or setInterval is a regression.
- The user explicitly complains "no refresh button", "prices don't update",
  "funding tab doesn't load on mount", "DCA bots went stale".

## The two pieces

### 1. `useAutoRefresh(fn, intervalMs, opts?)` — shared hook

Pure, no external deps. Lives next to other lib helpers, e.g.
`lib/useAutoRefresh.ts`.

**Returns:** `{ tick, now, isAuto, setAuto, refresh, busy, lastRefreshAt, error }`

- fires `fn()` once on mount
- fires every `intervalMs` while `isAuto` is true (default true)
- `refresh()` is a manual trigger that resets the timer and increments `tick`
- `busy` is true while a refresh is in flight — show a spinner on it
- `lastRefreshAt` is the timestamp of the last attempt (success or fail)
- `error` is the last thrown error string, or null
- `tick` is incremented on every refresh — use it as a `useEffect` dep
  inside the component if you need to react to refetched data
- `now` is `Date.now()` refreshed on the same interval — useful for "Xm
  until next funding" labels

**Critical implementation detail:** the hook must keep `fn` in a ref
(`fnRef.current = fn` on every render) and call `fnRef.current()` from
the timer. Otherwise stale closures capture state values from the moment
the timer was scheduled.

### 2. `<RefreshBar busy lastRefreshAt isAuto setAuto refresh error intervalMs />`

Visual indicator. Goes in the page header next to the title.

- **Manual Refresh button** with spinner — primary affordance, the user
  expects this on every data page
- **Auto/Manual toggle** — let the user pause polling when they want
  (saves bandwidth, avoids races during manual edits)
- **"updated 3s ago"** timestamp — shows data is actually live
- **error pill** — if last fetch failed, surface it inline so user knows
  the data is stale
- **"· every 30s"** caption — sets expectations

The bar must NOT replace the page title — put it next to the title in a
flex row, not instead of it.

## Interval calibration (by data velocity, not by guess)

| data class | interval | why |
|---|---|---|
| prices / live tickers / bot status | 15–30 s | user expects recent |
| wallet balances / alerts / rules / journal | 60 s | user-action driven |
| attribution / monthly aggregates / slow reports | 120–300 s | heavy; refetch on filter change |

If the server route already has an in-process cache (e.g. 15 s on
`/api/scanners?kind=funding`), set the client interval to **2× the
server cache** so every other refresh actually bypasses the cache.

## Pattern for tabs that fetch on switch

If a page has tabs and each tab triggers a different API call (e.g.
Scanner's Movers / Funding / Arb), the page feels broken when:

1. User lands on the page, sees tab 1 (default).
2. Clicks tab 2. Sees a loading spinner.
3. Clicks back to tab 1 — re-fetches from scratch.

**Fix:** pre-load all tabs in parallel on mount and keep them in state.
Tab switches become instant. Auto-refresh refreshes all tabs in parallel
in the same interval. Use `Promise.all([...])` and a `loadedTab` map so
the UI can show "no data" only on the very first load.

## Bugs that surfaced during the audit (real, not theoretical)

These were found in a working dashboard with 27 pages and verified live
before fixing. They are class-level bugs, not one-offs.

### Bug A: `findExchangeId()` async race

```ts
const _exchangeIdCache: Record<string, string> = {};
function findExchangeId(name: string): string {
  if (!_exchangeIdCache[name]) {
    _getExchanges();          // fire-and-forget; returns a promise
    return "";                // returns empty SYNCHRONOUSLY
  }
  return _exchangeIdCache[name];
}
```

When the user clicks "Close position" right after page load, the cache
is empty, the async fetch is still in flight, and `findExchangeId` returns
`""` immediately. The close request is sent with `exchangeId: ""` and
silently fails (or worse, closes the wrong position on the wrong exchange).

**Fix:** hydrate the cache inside the polling `load()` function so it's
warm before any action button is enabled.

```ts
async function load() {
  void _getExchanges();          // warm the cache
  const r = await fetch("/api/positions", ...);
  // ... rest of load
}
```

### Bug B: Column header lies about content

A table with `<th>Time</th>` showing `t.id.slice(0, 12)` and the actual
timestamp wedged into a final column with no header. Caught by visual
inspection during audit — the user knew the time was wrong, didn't know
why.

**Fix:** always render one column per header. Add a dedicated ID column
when you add a Time column (or vice versa). If a row has more fields than
the header has columns, you're either missing a header or hiding a column.

### Bug C: API defaults dead on first request

A wallet-tracking page calling `cloudflare-eth.com` and `eth.llamarpc.com`
as defaults — both returned `-32603` / `521` errors and silently broke
the feature. The user didn't notice until the audit because the UI
gracefully rendered an empty state.

**Fix:** for every external API call, write the **first 3 fallbacks
inline** in code. Test each fallback once at startup. Never rely on a
single URL default.

## Detection recipe (next audit)

When auditing any data dashboard, scan for these three signals:

```bash
# Pages without auto-refresh (no useAutoRefresh or setInterval)
grep -L "useAutoRefresh\|setInterval" app/*/page.tsx

# Pages using a sync helper that calls an async function (race pattern)
grep -rn "function.*async\|=> async" app/ | grep -v "async function"

# Pages that show stale data on tab return
# Manual: open each page in a browser, switch tabs, return — data should
# still be fresh.
```

A page that fails any of these checks has a real bug. Fix it before
claiming done.

## Verification standard

After applying auto-refresh to a batch of pages, verify live:

```bash
# 1. Every page returns 200
for p in / /scanner /alerts /wallets /trades; do
  curl -s -o /dev/null -w "%{http_code} %{time_total}s $p\n" http://HOST:PORT$p
done

# 2. RefreshBar HTML actually renders (not silently dropped in build)
curl -s http://HOST:PORT/scanner | grep -oE "(Refresh|Auto|Updated)" | sort -u

# 3. Server cache works as designed (cache hit should be faster than cold)
T1=$(date +%s%N); curl -s "URL" > /tmp/a.json
T2=$(date +%s%N); curl -s "URL" > /tmp/b.json
T3=$(date +%s%N)
echo "cold: $(( (T2-T1)/1000000 ))ms warm: $(( (T3-T2)/1000000 ))ms"
md5sum /tmp/a.json /tmp/b.json   # should match if cache hit
```

If any page 5xx's or the HTML doesn't contain "Refresh", the auto-refresh
isn't wired correctly. Do not ship.