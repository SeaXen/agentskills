# Preset curation notes

## Default browser behavior
- Set the browser dashboard watchlist preset default to `top50-trading` so the symbol preset dropdown is populated with a useful trading list on first load.
- Load symbol preset options dynamically from the currently selected watchlist preset instead of keeping a tiny hardcoded symbol list in HTML.
- Add a text input above the symbol preset dropdown for live filtering once the list grows beyond a handful of names.

## Trading-focused top-50 rules
Use `watchlist-top50-trading.yaml` for the broad discretionary trading universe.

Core rules:
- keep exchange-listed, liquid names
- exclude stablecoins and cash-like/tokenized-yield assets
- exclude gold-backed / treasury-like assets from the default trading preset
- exclude meme-heavy names by default except explicitly approved exceptions

Explicit keep exceptions:
- DOGE
- PEPE

Examples hidden from the default trading symbol dropdown:
- SHIB
- MemeCore (`M`)
- United Stables (`U`)
- stablecoins / gold / tokenized-cash names

## Grouped watchlists
Grouped watchlists are allowed to override the stricter default trading filter because they are thematic by design.

Current grouped presets:
- `ai`: TAO, RENDER, WLD, NEAR, ICP
- `l1l2`: ETH, SOL, ADA, AVAX, SUI, DOT, TON, ATOM, ARB, POL, APT, ALGO, XLM, HBAR, NEAR
- `rwa`: ONDO, WLFI, ALGO, LINK, AVAX, XLM
- `memes`: DOGE, PEPE, SHIB, M

## Verification
After editing preset logic:
1. restart `cryptohermes-dashboard.service`
2. verify `/api/health` includes the new preset keys
3. verify `/api/watchlist?watchlist_preset=<name>` returns the intended entries
4. verify in-browser that the symbol dropdown actually reflects the expected options
5. if the browser still shows an old list, hard-refresh the page because cache can retain stale state
