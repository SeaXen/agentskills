# Peer valuation and exchange routing

## Purpose
This note captures the lightweight valuation heuristics used by `crypto-analysis` so future sessions can stay fast and token-efficient.

## Relative valuation heuristic
Use a peer-group comparison when the user asks whether a token is undervalued or overvalued relative to similar projects.

### Peer group buckets
- **Meme / community tokens**: compare to DOGE, SHIB, PEPE, BONK, WIF, FLOKI
- **DeFi / protocol tokens**: compare to UNI, AAVE, LINK, CAKE, CRV, MKR, SNX
- **L1 / L2 / infra tokens**: compare to SOL, AVAX, NEAR, APT, SUI, SEI, INJ, ETH
- **Default fallback**: ETH, SOL, AVAX, NEAR, APT, SUI

### Heuristic thresholds
- ratio `< 0.65` → **undervalued**
- ratio `0.65–1.55` → **neutral**
- ratio `> 1.55` → **overvalued**

Interpretation is deliberately coarse: this is a quick screen, not a deep equity-style valuation model.

## Exchange quick check
For major coins, use a lightweight spot check before pulling heavier market data:
- try a Binance `SYMBOLUSDT` 24h ticker
- use it as a fast sanity check for price / 24h change / volume
- skip silently if the pair does not exist

## Output guidance
When the user asks for valuation vs peers:
- lead with the peer stance (`undervalued`, `neutral`, `overvalued`)
- include the ratio and median peer market cap if available
- keep the rest of the report compact for Discord/Telegram

## Important caveat
Peer valuation is only a heuristic. A high-cap chain may still be attractive if it has stronger network effects, treasury, revenue, or ecosystem dominance than the peer set suggests.
