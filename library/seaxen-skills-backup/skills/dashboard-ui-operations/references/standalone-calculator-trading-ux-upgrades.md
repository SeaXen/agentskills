# Standalone calculator trading UX upgrades

Use this when a small self-hosted calculator/sandbox already works but the user wants it to behave more like a practical trading pad than a raw formula form.

## Durable patterns

### 1) Price-source semantics must be explicit
Do not show a generic "live price" without saying what it is.

Good operator-facing choices:
- **CoinGecko** → public spot reference
- **Binance** → last traded price for `SYMBOLUSDT`
- **Bybit** → mark price for `SYMBOLUSDT`

Label the chip with both the price and the source class, e.g.:
- `SOL 63.77 USD (-6.49%) · CoinGecko spot`
- `SOLUSDT 63.90 USD (-6.80%) · Binance last`
- `SOLUSDT 63.84 USD (...) · Bybit mark`

The point is not brand decoration. The point is preventing the operator from confusing spot, last, and mark.

### 2) Support both convenience and control for Mark updates
If the user wants fetched prices to drive the Mark field, support two distinct UX paths:
- **Price** can auto-fill Mark when the user explicitly asked for that convenience
- **Use as Mark** remains available as a separate button so the operator can re-apply a fetched value deliberately after switching source or symbol

This avoids forcing one workflow on everyone.

### 3) Put high-value trading metrics on the main cards
For compact calculators, do not bury the useful trading readouts in notes.

Promote these into the baseline/projected cards when the underlying inputs exist:
- `Liq dist %`
- `PnL @ mark`
- `ROI @ mark`
- `Target exit`
- `PnL @ target`
- `ROI @ target`

These are usually more actionable than repeating raw collateral text or long explanatory prose.

### 4) DCA ladder beats repeated manual reruns
When the user is exploring add-margin / add-notional scenarios, provide a small built-in ladder rather than forcing repeated data entry.

Good default ladder:
- `+$5`
- `+$10`
- `+$20`
- `+$50`

For each row, show at least:
- added notional
- projected qty
- projected entry
- projected breakeven
- projected liquidation
- liq distance %

Seed the ladder from the current increase-position assumptions:
- fill price
- leverage
- collateral effect if used

### 5) Separate last snapshot from named saves
There are two different save needs.

#### A. Last snapshot
- lightweight convenience
- browser-local is fine
- used for quick resume after reload

#### B. Named saved positions
- explicit user presets
- must save the full form plus the adjustment steps
- should support one-click **load**, **update**, and **delete**
- if persistence is only browser-local, say so honestly

Do not pretend localStorage presets are cross-device/server state.

### 6) Browser-first live verification shape
For these calculator upgrades, verify in the browser, not only by API response.

Minimum checks:
1. fetch price from each intended source or at least one live source
2. confirm the chip text changes
3. confirm Mark changes if auto-fill is enabled
4. run Calculate and confirm projected metrics update
5. confirm the DCA ladder renders all expected rows
6. create a named save and confirm the save appears as a clickable preset
7. reload the page and confirm the saved entry or snapshot still exists if browser-local persistence is expected

## Practical implementation notes

- Keep the core calculator logic server-side if it already works; optional public-market enrichments can stay browser-side.
- If the container/server cannot reach public APIs but the browser can, move optional live-price fetching to the browser rather than keeping a dead backend endpoint.
- Use no-cache headers after JS/UI fixes if the user was previously seeing stale bundles.
- For exchange selectors, normalize symbols conservatively (for example `SOL` -> `SOLUSDT` on Binance/Bybit) and label assumptions in the UI.

## What to avoid

- A single ambiguous "Price" source with no source label
- Silent Mark overwrites when the user did not ask for it
- Notes-heavy UI where key numbers are hidden below the fold
- Calling browser-local saved presets "saved positions" without clarifying scope
