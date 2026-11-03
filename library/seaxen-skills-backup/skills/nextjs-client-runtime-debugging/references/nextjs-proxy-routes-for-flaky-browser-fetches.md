# Next.js proxy routes for flaky browser fetches

Use this pattern when a Next.js dashboard renders but some client-side widgets stay blank or inconsistent even though the public API works elsewhere.

## Case pattern
- App: client-heavy Next.js App Router dashboard.
- Symptom: some widgets loaded, others stayed `-` / `Unavailable` / placeholders.
- Browser console showed no obvious JS exception.
- Direct browser fetches to public endpoints were inconsistent across providers/endpoints.
- Build succeeded, but live UI still had partial failure.

## What fixed it
Move third-party browser fetches behind same-origin Next route handlers.

### Example route split
- `app/api/crypto/route.ts`
  - proxy CoinGecko simple price
  - proxy coin market lookup
  - proxy market table
  - proxy trending
  - proxy chart history
  - proxy global stats
  - proxy fear & greed
- `app/api/network-fees/route.ts`
  - proxy fee endpoints / RPC gas-price calls
  - apply timeout per upstream
  - return best-effort partial results instead of failing the whole widget

## Why it helped
- Removed browser-side CORS / proxy-policy variability from the UI path.
- Centralized timeout, headers, and error handling.
- Made the browser talk only to `/api/*`, which was much more deterministic during verification.
- Allowed graceful partial responses (`Unavailable` for some chains, real values for others) without breaking the whole page.

## Durable implementation notes
1. Add server-side timeout with `AbortController`.
2. Use `cache: 'no-store'` for live dashboard endpoints.
3. Return JSON with per-field fallbacks instead of one hard failure.
4. If one widget seeds shared price state for others, refresh that source first.
5. After proxying, re-test each widget individually:
   - price checker
   - token lookup
   - converter
   - chart
   - market table/mode switch
   - stateful widgets like portfolio or alerts

## Verification pattern that proved the fix
- `npm run build` passed.
- Browser page loaded.
- Market table rendered live rows.
- Trending list populated.
- Chart rendered an SVG.
- Converter returned a non-placeholder value.
- Token lookup returned a real coin.
- Portfolio add worked.
- Alert add worked.
- Network fees returned partial real data where upstreams allowed it.

## Pitfall
Do not conclude "the API is broken" just because browser-side fetch failed. In this case the better lesson was:
- public upstream reachable
- browser path flaky
- same-origin proxy route stabilized the product
