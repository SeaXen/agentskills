# Chain-token source routing notes

Use this when analyzing L1 / chain tokens such as TON, SOL, or other protocol-native assets.

## Routing heuristic
- Always start with CoinGecko baseline market data.
- Cross-check with a liquid spot or perp venue when available.
- Use DeFiLlama only if the token is a protocol/DeFi asset with meaningful TVL data.
- For chain tokens, DeFiLlama may return a `category: Chain` entry with empty `tvl` arrays; treat this as **no TVL signal available**, not as zero TVL.

## TON-style example
- CoinGecko id: `the-open-network`
- Binance symbol: `TONUSDT`
- Useful exchange checks: spot 24h, futures 24h, funding, open interest, and recent klines.
- TON can present strong market-cap/liquidity context even when protocol TVL is unavailable.

## Practical note
- In the final read, separate:
  - market/price context
  - derivatives context
  - chain/protocol context
- Do not force a TVL section if the source only returns empty arrays.
