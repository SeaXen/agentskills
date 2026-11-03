# TradingX WebSocket phase rollout reference

## Class of task
Upgrade a polling-based crypto dashboard into a trader-usable live market UI without turning the whole app into a heavy all-streams architecture.

## Proven rollout order
1. top ticker strip
2. trade page selected-symbol live ticker
3. watchlist live prices
4. open-position mark-price + unrealized PnL overlay
5. orders page live price + distance-to-market
6. stale timer + `LIVE / FALLBACK` badge
7. mini level-1 order book on the trade page
8. optional reconnect alerts / spread alerts later

## Why this order works
- It lands the biggest latency win first on the pages where the trader is actively looking.
- It keeps CPU/RAM/network impact small compared with a naive "stream everything" approach.
- It preserves the API as the stable fallback/control plane.

## Transport rules
- WebSocket: prices, bid/ask, spread, mark price, mini order book.
- API: balances, orders, history, snapshots, settings, health, analytics, fallback bootstrap.
- Webhook: signals and notifications only.

## Parsing lesson: Bybit tickers
Bybit public WS sends a full `snapshot` then partial `delta` updates.

Critical rule:
- Merge each `delta` into the last known row.
- Do NOT treat `delta` as a full replacement.

If you treat deltas as full rows, fields like these get corrupted or zeroed:
- `lastPrice`
- `highPrice24h`
- `lowPrice24h`
- `volume24h`
- `prevPrice24h`

## Browser stream helper pattern
Use one shared browser-side stream layer with:
- active ticker symbol subscriptions
- active order-book symbol subscriptions
- cached latest ticker per symbol
- cached latest order-book per symbol
- socket reconnect timer
- `lastMessageAt`
- stream status listeners

Status surface should expose:
- `connected`
- `connecting`
- `reconnectAttempts`
- `lastMessageAt`
- derived mode: `live` vs `fallback`
- stale threshold, e.g. ~8s

## UI patterns that worked
### Trade page
- live ticker block
- `LIVE / FALLBACK` badge
- `last tick Xs ago`
- spread absolute + spread percent
- simple spread signal (`Tight` / `Wide`)
- mini level-1 order book (`bids` / `asks`)

### Watchlist
- overlay stream prices onto existing watchlist rows
- preserve scanner/API cache as fallback
- show `LIVE / FALLBACK`

### Positions
- keep API positions snapshot as source of position inventory
- overlay streamed mark price by symbol
- recompute unrealized PnL in the UI
- visually flash the PnL cell on change if desired

### Orders
- keep API as source of open orders list
- overlay live symbol price by order symbol
- compute distance-to-market as simple percent from live price to order price

## Verification recipe
1. `npx tsc --noEmit`
2. `npm test`
3. `npm run build`
4. rebuild/redeploy container properly (build + recreate, not plain restart)
5. verify upstream exchange socket directly from terminal/Node
6. verify the page text from the browser DOM
7. verify values change over time on the same open page

## Terminal validation pattern
Use a direct Node WebSocket probe to the upstream exchange and confirm:
- connect succeeds
- subscription succeeds
- first frame is `snapshot`
- subsequent frames include `delta`
- real fields like `lastPrice`, `bid1Price`, `ask1Price` are present

## DOM validation pattern
When browser snapshots truncate below the fold, inspect:
- `document.body.innerText`
- targeted labels and values
- repeated timed samples from the same open page

Examples of good proof:
- trade page `Last` changed between two samples ~6s apart
- `Spread`, `Signal`, `last tick`, `MINI ORDER BOOK`, `BIDS`, `ASKS` text present live
- orders page new `LIVE` and `DIST` columns present live

## Honest reporting rule
If the environment currently has no open orders or no open positions:
- say the UI/structure/live page wiring is verified
- say row-level dynamic behavior could not be visually proven because the live dataset is empty
- do not overclaim
