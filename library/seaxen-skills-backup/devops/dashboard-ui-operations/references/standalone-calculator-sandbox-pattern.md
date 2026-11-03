# Standalone calculator sandbox pattern

Use this for small single-container what-if tools such as liquidation, breakeven, DCA, collateral, or risk calculators.

## Good default shape

- one Docker service
- stdlib or otherwise tiny backend
- static HTML/CSS/JS frontend
- local calculator logic stays server-side if it is core product logic
- optional public enrichment data (for example live coin price) can stay browser-side when it does not require secrets

## UX defaults

- compact top bar, not a large hero
- edge-to-edge cards with low padding
- one dense grid on desktop
- one-column stack on mobile
- keep explanation short; avoid large “what this does” blocks unless the user asked for documentation
- keep sample/example loading as a small utility button, not the visual focus

## Calculator semantics that worked well

- support both **exact mode** and **anchored-estimate mode**
- exact mode = user provides real collateral/effective balance
- anchored-estimate mode = infer collateral from current liquidation anchor + MMR
- label the assumption mode visibly in the UI and response payload
- model scenario steps as an ordered list (`increase_position`, `add_collateral`, `remove_collateral`, `partial_close`)

## Live market data rule

If the container/backend cannot reach the internet but the browser can:
- keep the calculator working without price data
- fetch public non-secret market data from the browser
- use the price as an optional helper, not a dependency for the core calculator
- do not leave a dead backend endpoint in place if the feature is meant to work interactively

## Verification

- unit tests for the calculator math
- container build/restart from the real target path
- `GET /api/health`
- real calculation POST
- browser verification that the compact layout is live
- browser verification that the hero section is truly gone
- browser verification that the live price helper actually updates the UI
