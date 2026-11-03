# Standalone calculator: live price + cache-busting pattern

Use this for small self-hosted calculator/trading dashboards where the core math runs locally but the UI wants optional live public market data.

## Durable pattern

### 1) Keep core math local
- Calculator API stays local/server-side.
- Do not make the whole app depend on an external market API just to compute results.

### 2) Split optional live price from core calculator
If the container/server cannot reach the public internet but the browser can:
- keep `/api/calculate` local
- move optional live-price lookup to browser-side fetch against a public API like CoinGecko
- treat the live price as a UI helper, not a hard dependency for calculations

This avoids a dead backend endpoint that always fails in containerized/network-constrained deployments.

## Verification sequence

1. Verify the calculator path separately
   - click Calculate
   - assert a real projected field changes in the DOM
   - assert notes/result text changes, not just that no console error appears

2. Verify live price separately
   - click Price
   - wait long enough for async fetch
   - read the chip/result text from the DOM
   - if it succeeds in browser but not from the container, keep the price feature client-side

3. If the user still reports the old broken behavior while your live browser test passes:
   - suspect stale browser assets first
   - add no-cache headers on static assets and JSON responses
   - instruct hard refresh / reopen page

## Good headers for self-hosted static dashboards
- `Cache-Control: no-store, no-cache, must-revalidate, max-age=0`
- `Pragma: no-cache`
- `Expires: 0`

These are especially useful right after urgent JS fixes where the old bundle made buttons look dead.

## UX rule for trading dashboards
Be explicit about what the fetched price means:
- public API price chip = current public spot/reference price
- not necessarily exchange mark price / contract mark / exact last traded price on the user’s venue

Do not silently overwrite the user's current mark field if it already has a value. Better defaults:
- leave mark untouched unless empty, or
- add an explicit `Use price as Mark` action.

## Pitfalls
- Treating "no console error" as proof that the button works
- Leaving a dead `/api/price` endpoint in place when the real working path is browser-side
- Reporting a feature broken when only the user’s cached JS is stale
- Presenting public spot data as if it were exchange-specific mark price
