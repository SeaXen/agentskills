# Market-context batch pattern for TradingX-style trade surfaces

Use this when the user wants the **next best batch** of crypto/trading features and the highest-ROI move is to improve the trade decision surface rather than create more standalone pages.

## What shipped

A compact market-context route + in-page trade panel:
- route: `/api/market-context?symbol=BTCUSDT`
- panel lives inside `/trade`
- route fuses:
  - internal news feed (`getNews()`)
  - Bybit public ticker endpoint
  - Bybit public open-interest endpoint
  - optional Mobula metadata-based unlock schedule

## Why this was the right move

Compared with building separate news/unlock/open-interest pages, the route-panel pattern:
- keeps the user on the actual execution screen
- uses existing internal data pipelines first
- minimizes new routing and navigation surface
- allows partial success when one provider is missing
- gives immediate trader context with one request per symbol

## Concrete payload shape that proved useful

```ts
{
  symbol,
  baseAsset,
  generatedAt,
  news: { count, items[] },
  unlocks: { available, events[], note },
  openInterest: {
    current,
    currentUsd,
    fundingRate,
    basisPct,
    nextFundingTime,
    price24hPcnt,
    volume24h,
    turnover24h,
    oiDeltaPct,
    series,
  },
  position: { count, side, liqDistPct, nearLiq },
  liquidity: { bias, risk, score, reasons[], basisPct, churnRatio, positionSide, positionLiqDistPct }
}
```

## Heuristic (v2 — still decision-support, not quant)

After the first ship, a better squeeze/crowding score added three more inputs without new pages:
- **Basis** — `(markPrice - indexPrice) / indexPrice * 100` from the same Bybit ticker row
- **OI churn** — `turnover24h / openInterestValue` when 24h price move is flat
- **Liquidation proximity** — reuse exchange adapters (`listExchanges` + `adapterFor` + `getPositions()`), filter to the requested symbol, compute `|mark - liq| / mark`, boost score when ≤8%

Still output `long-squeeze | short-squeeze | balanced` and `low | medium | high` with short reasons.

## Optional-feed rule

Unlock data must not block the route.

Correct behavior:
- if `MOBULA_API_KEY` missing → return `available: false` + explanatory note
- if provider returns no schedule → return empty `events` + explanatory note
- still return usable `news + OI + liquidity` data

Wrong behavior:
- throwing 500 because unlocks are unavailable
- hiding the entire market-context panel because one optional feed failed

## Provider lessons

### Bybit
Public OI/ticker endpoints were enough for a strong first pass.
Useful endpoints:
- `/v5/market/tickers?category=linear&symbol=...`
- `/v5/market/open-interest?category=linear&intervalTime=5min&limit=12&symbol=...`

Probe them directly once before coding so you know the real payload fields.

### Mobula
Unlock schedule should be treated as opportunistic. The practical rule is:
- use it only when `MOBULA_API_KEY` is already configured
- keep the route healthy without it
- prefer an honest UI note over fake or inferred unlock data

## UI placement rule

For this class of feature, put the panel on the trade page next to order preview / order book instead of making the user leave `/trade`.

Good contents:
- compact metrics grid (funding, basis, OI drift, squeeze risk)
- tiny **OI sparkline** from `openInterest.series` (inline SVG; no chart library)
- liquidity bias card + optional “your stack is X% from liq” when `position.count > 0`
- top 2–3 headlines with trade deep-links (`/trade?symbol=...`)
- unlock rows that also deep-link to trade

Trade deep-link helper (news symbols are usually `BTC`, ticket expects `BTCUSDT`):

```ts
function toTradeSymbol(symbol: string): string {
  const s = symbol.trim().toUpperCase();
  if (s.endsWith("USDT") || s.endsWith("USDC") || s.endsWith("USD")) return s;
  return `${s}USDT`;
}
```

Apply on `/news` symbol chips and per-headline symbol tags, not only on `/trade`.

Avoid:
- long article walls
- giant tables
- forcing navigation away from the trade flow

## Verification that mattered

- `npm run typecheck`
- `npm test`
- `npm run build`
- confirm `/api/market-context` appears in build output
- direct terminal probe of Bybit endpoints before finalizing field mapping

## Pitfalls

When adding the panel into a long TSX trade page, helper functions like `timeAgo`, `compactNumber`, `OiSparkline`, and metric subcomponents are easy to forget during patch-based edits. Re-run typecheck immediately after insertion.

**Helper insertion bug (`app/news/page.tsx`):** inserting `toTradeSymbol()` above `timeAgo()` can accidentally delete the `function timeAgo(ts: number)` line and leave the body at module scope (`TS1128`). Re-read the helper block after patch.

**Git push hygiene:** unstage Playwright output before commit: `git add -A && git reset -- test-results/`.
