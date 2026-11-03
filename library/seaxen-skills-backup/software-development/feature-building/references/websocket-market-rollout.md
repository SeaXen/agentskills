# WebSocket market rollout notes

Use for crypto/trader-facing dashboards where live prices matter but a full app-wide streaming rewrite is unnecessary.

## Proven rollout shape

Phase 1:
- top ticker strip
- trade ticket selected-symbol live ticker
- keep REST `/api/market` as bootstrap + fallback

Phase 2:
- watchlist live price overlay
- positions live mark-price overlay
- positions live unrealized PnL recompute
- trade-page spread + simple spread-quality signal
- UI stream badge: `LIVE` / `FALLBACK`

## Bybit payload lesson

Bybit public linear ticker stream sends:
- one `snapshot`
- then many partial `delta` frames

Correct parser behavior:
- cache the last raw row per symbol
- merge incoming delta into cached row
- derive display fields from the merged row

Wrong behavior:
- treating each delta like a full record
- result: zero/mixed `last/high/low/volume`

## Verification pattern

Minimum proof for a live-stream feature:
1. `npx tsc --noEmit`
2. `npm test`
3. `npm run build`
4. direct upstream terminal WebSocket probe
5. live browser DOM proof that the target values exist
6. second DOM sample after delay proving the values changed over time

## Important honesty rule

If a streamed positions feature is deployed but there are no live open positions at verification time, report it as structurally shipped but not visually proven on a real row yet.
