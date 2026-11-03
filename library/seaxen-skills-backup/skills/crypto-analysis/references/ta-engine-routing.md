# TA engine routing

## Purpose
This note describes how `crypto-analysis` turns raw candles and exchange checks into a compact trading bias without becoming noisy.

## Routing modes
- **auto**: balanced default; favors 4h and 1d slightly more than 15m
- **scalp**: boosts 15m heavily; best for short intraday entries
- **swing**: boosts 4h and 1d; best for trend-following or multi-day holds
- **full**: computes every available indicator, but still only surfaces the key drivers

## Coin-type weighting
- **major / L1 / L2**: emphasize trend confirmation
  - EMA 20/50, VWAP, MACD, ADX, RSI
- **meme / volatile small caps**: emphasize volatility and participation
  - RSI, Bollinger width, ATR, volume ratio, OBV, liquidity
- **DeFi / protocol tokens**: emphasize trend plus category context
  - EMA, VWAP, RSI, TVL / valuation, volume
- **perps-heavy tokens**: emphasize derivatives confirmation
  - Bybit/Coinglass funding, OI, liquidation pressure, then TA
- **alt / mixed tokens**: balanced default weighting

## Indicator sequence
1. Pull candles from Hyperliquid.
2. If unavailable or thin, fall back to Binance klines.
3. Compute EMA 20/50, RSI, MACD, VWAP, ATR, Bollinger, ADX, OBV, and volume ratio.
4. Score each timeframe.
5. Combine 15m / 4h / 1d with timeframe weights.
6. Adjust confidence and risk notes with exchange consensus, funding, OI, liquidity, FDV, and valuation signals.

## Exchange logic
- **Binance**: primary fast spot check
- **Bybit**: spot confirmation + perp snapshot when relevant
- **Coinbase**: clean major-coin sanity check
- **Exchange consensus** appears only when at least two valid spot checks exist
- **Price spread** above a small threshold should become a risk flag, not a verdict by itself

## Interpretation rules
- Never let one indicator decide the trade alone.
- Use price action + trend + exchange confirmation before calling long/short.
- If exchange data and TA disagree, prefer neutral unless the higher-timeframe structure is clear.
- Treat peer valuation as a heuristic, not a fundamental model.

## Output discipline
- Keep the bias line first.
- Show only the most relevant 2–4 driver signals per timeframe.
- Hide noisy sections when data is missing.
- Use dynamic price formatting for tiny-priced assets so values remain readable.
