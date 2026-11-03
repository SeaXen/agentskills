---
name: crypto-analysis
description: Use when the user wants a fast but thorough crypto read on a coin/token. Selectively gathers price, market cap, derivatives, liquidity, DeFi TVL, sentiment, fundamentals, and on-chain/protocol context from only the relevant public sources, then returns a compact long/short/neutral bias for 15m, 4h, and 1d.
version: 1.9.1
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [crypto, analysis, market-data, derivatives, defi, tradingview, dexscreener, geckoterminal, coinglass, sentiment, onchain, fundamentals]
    related_skills: [hermes-agent-skill-authoring]
---

# Crypto Analysis

## Overview

This skill turns Hermes into a selective multi-source crypto analyst.
Instead of checking every site for every coin, it decides which sources are relevant and only queries those sources.

The output is designed for quick trading decisions and should follow the compact chat template exactly, including technical bias and confidence every time:
- price and market snapshot
- liquidity / volume / FDV where available
- relative valuation vs similar peers / category when available
- quick exchange spot check when available
- DeFi TVL for protocol tokens
- sentiment / social / narrative context when available
- on-chain / contract context when available
- 15m / 4h / 1d bias
- final `long / short / neutral` verdict
- exact quick-read template with spot check, relative valuation, action, setup, confidence, and optional risk note

## When to Use

Use when the user asks things like:
- “analyze TAO”
- “should I long or short this coin?”
- “give me 15m / 4h / 1d bias”
- “check funding / OI / TVL / liquidity / holders for this token”
- “make this work with public crypto websites and only hit the relevant ones”

Do not use for:
- pure order execution
- portfolio rebalancing
- long-form technical research papers
- non-crypto assets

## Data Source Policy

The skill follows a simple rule:

1. **Always try a baseline price source**
   - CoinGecko first
   - CoinMarketCap as optional fallback/enrichment when a key exists
   - CoinPaprika as an additional no-key fallback when CoinGecko fails or is incomplete

2. **Only query source-specific sites when the token needs them**
   - **DeFiLlama** only for protocol / DeFi / TVL-relevant tokens
   - **DexScreener** and **GeckoTerminal** only for DEX/liquidity-heavy tokens
   - **Coinglass** only when derivatives/funding/OI matter
   - **Messari** for fundamentals / asset metrics when available
   - **LunarCrush** for social and sentiment context when available
   - **Etherscan / BscScan / BaseScan / Arbiscan / PolygonScan / Snowtrace** for contract and holder context when available
   - **TradingView** is used as a chart link, not as a free API dependency
   - **Binance public klines** are the fallback TA source when Hyperliquid candle snapshots are unavailable or too thin

3. **Prefer token-aware routing**
   - L1/L2 / major assets: price + market + exchange + derivatives + on-chain checks
   - DeFi tokens: add TVL/protocol context and fundamentals
   - DEX/meme tokens: add liquidity/DEX pair context and sentiment
   - Perps-heavy tokens: add OI/funding/liquidation context

## Supported Sources

### Baseline
- CoinGecko
- CoinMarketCap (optional key)
- CoinPaprika

### DeFi / protocol context
- DeFiLlama
- Messari (optional key)

### DEX liquidity / pair context
- DexScreener
- GeckoTerminal

### Derivatives
- Coinglass

### Sentiment / social context
- LunarCrush (optional key)
- X Search when the user explicitly asks to search X / x.com / Twitter chatter

### On-chain / contract context
- Etherscan-family explorer APIs (optional keys)

### Exchange / chart context
- TradingView TA MCP when available: prefer `multi_timeframe_analysis` for fast structured 15m / 1h / 4h / 1d / 1W bias and `market_sentiment` for the MCP's built-in social read
- Prefer perp-aware symbols on charting/TA tools when the asset is mainly traded as a perp; for crypto majors and liquid alts, prefer explicit exchange symbols like `BYBIT:BTCUSDT.P`, `BYBIT:ETHUSDT.P`, `BYBIT:SOLUSDT.P` for chart capture when the user is trading perps
- Hyperliquid candle snapshots for 15m / 4h / 1d bias when TradingView TA MCP is unavailable or insufficient
- Binance public kline fallback when Hyperliquid is unavailable
- Binance / Bybit / Coinbase spot cross-checks when relevant
- Bybit perp snapshot for funding / OI when relevant
- TradingView chart MCP for final visual confirmation when available; otherwise provide a TradingView chart URL

## Environment Keys

Optional keys that improve coverage:
- `COINMARKETCAP_KEY`
- `COINGLASS_KEY`
- `MESSARI_KEY`
- `LUNARCRUSH_KEY` or `LUNARCRUSH_API_KEY`
- `ETHERSCAN_KEY`
- `BSCSCAN_KEY`
- `POLYGONSCAN_KEY`
- `ARBISCAN_KEY`
- `BASESCAN_KEY`

The skill still works without keys; it just skips those sources.

## Output Shape

- The skill returns a compact report with:
- current price
- market cap and FDV
- 24h volume and change
- DeFi TVL when relevant
- DEX liquidity when relevant
- sentiment / social score when relevant
- holder count / contract verification when relevant
- OI / funding when relevant
- spot check / exchange consensus when relevant
- relative valuation when relevant
- 15m / 4h / 1d bias with indicator notes
- multi-indicator TA stack (EMA, RSI, MACD, VWAP, ATR, Bollinger, ADX, OBV, volume)
- TradingView TA MCP `multi_timeframe_analysis` output when available, including alignment status and confidence
- TradingView TA MCP `market_sentiment` output when available, clearly labeled low-confidence if post count is zero or the source timed out
- adaptive TA routing by coin type (`auto`, `scalp`, `swing`, `full`)
- exchange consensus / price spread when relevant
- separate Verdict block with verdict, best setup, and invalidation/reclaim notes
- final `long / short / neutral` verdict plus a separate trade action label (`BUY`, `SELL`, `HOLD`) and setup label (`SCALP LONG`, `SWING SHORT`, etc.)
- technical bias line separate from overall verdict
- confidence as a numeric percentage when possible
- optional risk note for memes / low-cap / high-funding setups
- first-line bias summary for fast Discord/Telegram reads
- BTC-style quick read blocks with price, 24h change, market cap, volume, perp funding, technical bias, confidence, timeframe bias, read, levels, verdict, and bias as the default compact/chat format
- trade entry / stop / target when available
- a cross-platform layout that reads cleanly in both Discord and Telegram

- quick-read format reference: `references/quick-read-format.md`
- valuation / exchange routing reference: `references/peer-valuation-and-exchange-routing.md`
- TA engine routing reference: `references/ta-engine-routing.md`
- verdict rendering reference: `references/trade-verdict-labels.md`

## Invocation Pattern

Examples:

```text
Analyze TAO
Analyze Bitcoin with derivatives
Analyze Uniswap with TVL and DeFi context
Analyze PEPE with DEX and sentiment context
```

## Bengali User Support
For Bengali-speaking users, refer to `references/bengali-crypto-analysis-guide.md` for:
- Localized explanations of key metrics (e.g., RSI, MACD, EMA).
- Preferred data sources (CoinGecko, TradingView, Glassnode).
- Structured workflows for technical/fundamental analysis in Bengali/English mix.
- Risk management guidelines tailored to regional preferences.

Default chat behavior:
- For simple requests like `Analyze SOL`, render the BTC-style quick read block unless the user asks for another layout.
- Keep the title short and the wording concise.
- Use plain text requests like the examples above in Discord and Telegram; do not require a visible `/hl` prefix in the chat message.

Optional flags:
- `--layout discord|telegram|compact`
- `--ta_mode auto|scalp|swing|full`
- `--vs_currency usd`
- `--include_derivatives true`
- `--sources coingecko,defillama,cmc,coinpaprika,dexscreener,geckoterminal,coinglass,messari,lunarcrush,etherscan,exchange,fundamentals`

Layout behavior:
- `discord` uses a bold title line and compact bullets
- `telegram` uses a plain title line and simple bullets
- `compact` is the default terminal-friendly style
- avoid markdown tables in chat output; use plain bullets so the message stays readable on mobile
- if an optional source is unavailable, omit that section from the rendered report instead of surfacing a key-missing warning

See `references/discord-telegram-layouts.md` for examples.

## Internal Logic

The script does this in order:

1. Resolve the best CoinGecko id from the user’s input.
2. Fetch CoinGecko baseline data.
3. Infer token type from name, symbol, categories, and common heuristics.
4. Build a selective source list.
5. Pull only the relevant APIs.
6. If TradingView TA MCP is available, call `multi_timeframe_analysis` first for a fast structured directional read across higher and lower timeframes. Use that as the primary TA scaffold unless it is clearly stale or broken.
7. If sentiment is requested or useful, try TradingView TA MCP `market_sentiment`, but treat zero-post / timeout results as weak evidence rather than real neutrality.
8. Compute or enrich with the full indicator stack from the available candles (EMA, RSI, MACD, VWAP, ATR, Bollinger, ADX, OBV, volume) when the MCP output is missing detail, needs verification, or conflicts with price action.
9. Apply a token-type-aware router so majors, memes, DeFi, and perps emphasize different indicators.
10. If TradingView chart MCP is available, fetch a live chart image for final visual confirmation of trend, structure, FVG / order-block context, and obvious invalidation levels.
11. Combine all evidence into a final verdict.

See `references/ta-engine-routing.md` for the TA weighting and verdict routing rules.

## Common Pitfalls

1. **TradingView is not used as a free data API.**
   The skill provides a TradingView link instead.

2. **Not every token has DeFiLlama data.**
   The skill only asks DeFiLlama when it is meaningful.
   For L1 / chain tokens, an empty `tvl` response should be treated as “no TVL signal available,” not as proof of zero TVL.

3. **Not every DEX token has neat CoinGecko coverage.**
   That is why DexScreener and GeckoTerminal are included as fallback liquidity sources.

4. **Derivatives data is meaningless for many tokens.**
   Coinglass is skipped unless the token profile suggests derivatives relevance or the user forces it.

5. **A single source should never decide the trade alone.**
   The final verdict should be interpreted as a bias, not certainty.

6. **Very small-priced assets need dynamic formatting.**
   Showing PEPE-like coins with fixed 4-decimal formatting hides useful price action. The renderer should adapt decimals to the asset price so tiny prices stay readable.

7. **Peer valuation is only a heuristic.**
   Use it as a quick `undervalued / neutral / overvalued` screen, not a deep fundamental model.

9. **Refresh live price immediately before the final answer.**
   If the report mentions support/resistance from social posts, analyst snippets, or older articles, do one final live price check right before rendering. If the live price has already moved through a cited zone, rewrite the final answer around the live price and label the old zone as broken / historical context instead of presenting it as current support.

10. **TradingView TA MCP sentiment can be empty.**
   `market_sentiment` may return zero posts because upstream Reddit/network fetches failed. Treat that as missing data, not true neutral sentiment.

11. **Use X fallback for live social sentiment when MCP sentiment is empty.**
   If `market_sentiment` returns zero posts, times out, or looks stale, fall back to X-native search for current trader chatter when sentiment actually matters to the answer.

12. **TradingView chart MCP is session-based.**
   If chart fetches suddenly fail, the user's TradingView `sessionid` / `sessionid_sign` may have expired or been invalidated by logout.

13. **Use X-native search when the user asked for X specifically.**
   If the user says `search X`, `search x.com`, or asks for Twitter chatter, prefer the platform-native X search tool when available. Generic web search can miss posts, return stale mirrors, or mix in non-X pages.

## Verification Checklist

- [ ] CoinGecko baseline works
- [ ] CoinPaprika fallback exists if needed
- [ ] CoinMarketCap is optional and does not block the report when missing
- [ ] DeFiLlama only appears for relevant tokens
- [ ] DexScreener / GeckoTerminal only appear for relevant tokens
- [ ] LunarCrush appears only when relevant or explicitly requested
- [ ] Explorer on-chain checks appear only when contract data is available and a key exists
- [ ] Coinglass only appears when derivatives are relevant or explicitly requested
- [ ] If TradingView TA MCP is available, `multi_timeframe_analysis` is used or explicitly skipped with reason
- [ ] If sentiment is requested, `market_sentiment` is used and zero-post / timeout output is labeled as inconclusive rather than neutral
- [ ] If sentiment matters and TV MCP sentiment is empty, X-native search is used as fallback or explicitly skipped with reason
- [ ] If TradingView chart MCP is available, a live chart image is fetched for visual confirmation when it materially helps
- [ ] 15m / 4h / 1d bias is shown
- [ ] Final verdict is shown
- [ ] Live price is refreshed immediately before the final render so stale article/social levels are not presented as current
- Binance fallback kicks in when Hyperliquid is thin or fails
- tiny-priced assets render with readable decimals
