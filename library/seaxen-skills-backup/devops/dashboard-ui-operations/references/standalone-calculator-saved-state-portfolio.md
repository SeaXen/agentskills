# Standalone calculator saved-state, reset, and portfolio patterns

Use this when a compact trading calculator already has core math and live-price helpers, but the user now wants the app to behave like a reusable position workspace rather than a one-shot calculator.

## Durable patterns

### 1) Reset-for-new-coin is a first-class workflow
If the operator switches symbols often, stale entry/fill/target values are more dangerous than blank inputs.

Good reset behavior:
- clear coin-specific numeric fields tied to the previous symbol
- keep durable preferences like side, margin mode, and price source
- reset adjustments to a safe default row
- if a fresh price was already fetched, optionally reseed Mark/fill/target from that price

Bad behavior:
- silently carrying over old SOL position values into a WIF scenario
- fully nuking all preferences when the user only wanted a clean symbol change

### 2) Promote named saves to server-side state when persistence matters
Browser-local saves are fine for convenience. They are not enough once the user expects:
- cross-reload durability at the app level
- one canonical saved-position list
- portfolio aggregation across saves
- import/export backup and restore

Good minimum server surface:
- `GET /api/saves`
- `POST /api/saves`
- `DELETE /api/saves/<name>`
- `GET /api/saves/export`
- `POST /api/saves/import`

Store the full form payload plus adjustment steps, not only a few headline numbers.

### 3) Portfolio should reuse saved-position payloads, not invent a second model
When the user asks for a portfolio tab, do not fork the logic.

Better pattern:
- reuse the same saved form payloads
- run each saved position through the same calculator engine
- aggregate totals from those computed states
- show both portfolio totals and per-position summaries

High-value totals:
- positions
- collateral
- entry notional
- projected PnL @ mark
- projected ROI @ mark
- target PnL
- target ROI
- liq distance %

### 4) Import/export JSON should be explicit and boring
For saved-position backup/restore, boring is good.

Recommended semantics:
- export returns a JSON object keyed by save name
- import accepts the same shape
- import reports how many saves were imported
- overwrite-on-name is fine if documented and predictable

This gives the user a simple backup/migration path without adding database complexity.

### 5) Exchange symbol mapping needs an explicit table
Compact trading apps hit symbol mismatches fast.

Do not rely only on `SYMBOLUSDT` string concatenation.
Use an explicit map for common special cases and memecoins, for example:
- `WIF`
- `1000PEPE`
- `1000BONK`
- `1000FLOKI`
- `BRETT`

Verify the mapping live by checking the rendered source chip, not only helper code.

### 6) Verify the saved-state path live, not only by unit tests
Minimum live pass:
1. create a save
2. confirm it appears in the UI list
3. switch to portfolio and confirm totals update
4. export JSON and inspect the response shape
5. import a test save and confirm it appears in portfolio/listing
6. delete the temporary verification save so the app is left clean

## Practical implementation notes

- Server-side JSON file storage is a good first durable step when the app is single-user or low-complexity.
- Keep no-cache headers on static assets/JSON after frontend feature additions so stale browser bundles do not masquerade as broken save/import buttons.
- When computing portfolio totals, preserve honest null/zero handling for metrics like target ROI if a target exit is not set.
- If the container cannot reach public market APIs, keep the portfolio/save system server-side and move only optional live-price fetching to the browser.
