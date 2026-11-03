# WebSocket trader UI rollout

Condensed lessons from the TradingX live-market migration.

## Architecture split

Use three lanes, not one:
- WebSocket: live price/ticker/order-book transport
- API: orders, balances, history, snapshots, settings, analytics, sync, fallback
- Webhook: inbound signals and outbound notifications only

Do not present webhook as a replacement for live price transport.

## Rollout order that gives value fastest

1. top ticker strip
2. selected-symbol trade ticket
3. watchlist live rows
4. open-position mark price + unrealized PnL
5. spread and spread-quality hint
6. mini order book
7. open-order live distance to market
8. stale/reconnect alerts
9. liquidation-distance visibility

This sequence gives the best trader-facing benefit per unit of complexity.

## Stream implementation pattern

- Prefer one shared browser WebSocket client with fan-out hooks.
- Subscribe/unsubscribe per symbol as components mount/unmount.
- Keep REST snapshot bootstrap so pages can paint immediately.
- Expose stream status to UI:
  - connected / connecting
  - lastMessageAt
  - stale
  - reconnectAttempts
  - mode = live | fallback

## Critical payload pitfall

Bybit public streams can send:
- initial `snapshot`
- later `delta`

Do not treat every frame as a full row.
Merge deltas into cached symbol state before computing:
- last
- bid/ask
- change24h
- high24h
- low24h
- volume24h

If you skip the merge, fields silently zero or drift on partial updates.

## Verification pattern

Minimum honest proof:
1. `npx tsc --noEmit`
2. `npm test`
3. `npm run build`
4. redeploy container
5. terminal-level direct upstream WebSocket check to inspect real payload shape
6. browser/DOM proof that on-page values change over time, not just on initial load

Examples of acceptable proof:
- direct terminal subscription to upstream `wss://...` showing real snapshot + delta frames
- same page sampled twice several seconds apart with changed `Last` / `Bid/Ask`
- DOM text showing `LIVE`, `Spread`, `Signal`, `Mini order book`, `last tick Xs ago`

## Reporting discipline

If there are no open orders or no open positions live:
- verify the columns/badges/wiring
- explicitly say row-level behavior was not visually proven because the page had no data
- do not pretend near-touch alerts, liq distance, or uPnL flash were observed live when there were zero rows

## Build note

In this codebase, Next.js build may emit:
- `ESLint must be installed in order to run during builds...`

If static pages finish and the route table is produced, treat this as a non-blocking build note and say so plainly.
