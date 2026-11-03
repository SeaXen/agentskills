# LiquidRisk phase-1 decision-support bundle

Use this pattern for compact trading/risk dashboards when the user wants the next highest-ROI product pass rather than random feature creep.

## Best phase-1 bundle
Implement these together because they reinforce each other:
1. **Risk status badges** on calculation result cards and saved/portfolio items.
2. **Portfolio summary cards** so the portfolio view has immediate value even with a small dataset.
3. **Always-visible search / filter / sort** controls for saved positions and portfolio lists.
4. **Compact empty states with CTA buttons** instead of blank dark space.
5. **Primary-vs-secondary metric hierarchy plus delta chips** so projected vs baseline changes are glanceable.

## Why this bundle works
- It adds decision support before adding heavy workflow complexity.
- It makes existing folders/tags/saves operational instead of decorative.
- It improves both populated and empty states, so the app stops feeling broken when data is sparse.
- It is high visible value without requiring auth, cloud sync, or a data model rewrite.

## Backend pattern
- Derive a simple `risk_status` from `liq_distance_pct` using stable thresholds.
- Add a human label like `risk_label` alongside the machine status.
- Enrich baseline/projected payloads with derived fields such as leverage multiple and deltas.
- Reuse the same enriched saved-position payloads to build portfolio aggregates.
- Portfolio summary should usually include:
  - positions
  - long/short counts
  - collateral
  - entry notional
  - PnL/ROI snapshot
  - avg liquidation distance
  - avg leverage
  - highest-risk position name/status
  - risk mix counts

## Frontend pattern
- Keep search/filter/sort bars always visible; do not hide them behind click toggles.
- Reuse the same sort model across saved positions and portfolio when possible.
- Split result cards into:
  - **Key metrics**
  - **Supporting metrics**
- Show delta chips on the projected card for values like liq, liq distance, ROI, collateral, entry, and breakeven.
- Empty-state blocks should contain a short explanation plus direct actions like:
  - save current
  - load sample
  - create backup now
- Saved-position cards should surface:
  - coin visual
  - risk badge
  - folder/tag chips
  - exchange badge
  - updated time
  - a few high-signal metrics

## Verification pattern
Minimum verification for this bundle:
- Python tests pass.
- JS syntax checks pass for both source and deployment copies when duplicated (`static/*` and `public/*`).
- Docker rebuild/redeploy succeeds on the canonical port.
- `/api/portfolio`, `/api/backups`, and `/api/health` return coherent data.
- Browser check confirms:
  - risk badges visible
  - summary cards rendered
  - search/filter/sort controls visible
  - empty states are action-oriented
  - backup panel works in both empty and non-empty states
  - no console JS errors

## Specific UI pitfall found here
A summary card can be technically correct but visually cryptic. Example: a `Risk mix` card showing `0/0` without obvious meaning. Prefer labels that read clearly at a glance, not compressed ratios that require interpretation.
