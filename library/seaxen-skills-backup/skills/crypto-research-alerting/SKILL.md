---
name: crypto-research-alerting
description: "High-performance multi-exchange research and execution dashboard for crypto traders. Integrates real-time price, funding, and order execution for Binance, Bybit, MEXC, Bitget, and Hyperliquid into a single browser-based UI with Hedge Mode support."
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [crypto, trading, market-data, coingecko, dexscreener, binance, bybit, risk, alerts]
    related_skills: [hermes-agent, webhook-subscriptions, polymarket, blogwatcher]
---

# Crypto Research + Alerting

## Overview

This skill defines a **safe, practical crypto workflow** for Hermes centered on:

- **CoinGecko** for broad market and category discovery
- **DEXScreener** for fast token / pair / DEX momentum checks
- **Binance (Read/Trade)**: Major CEX market data and direct Futures order execution.
- **Bybit (Read/Trade)**: Futures market structure and upcoming execution support.
- **MEXC & Bitget**: Public price feed integration for low-cap and alternative liquidity.
- **Hyperliquid**: High-speed L2 mid-prices and funding rate discovery.
- **Multi-Exchange Terminal Overlay**: Layered UI (Analysis, Trading, Scanner, Settings) with live Binance position tracking and cross-exchange price feeds (Binance, Bybit, MEXC, Bitget, Hyperliquid).
- **Execution Engine**: Direct Futures order placement (BUY/SELL) with auto-calculated risk sizing and Hedge Mode (Dual-Side) support.
- **Key Management**: Local-only API key storage and management via the dashboard UI for Binance, Bybit, and Hyperliquid.

The design goal is **10/10 usefulness with minimal financial risk**. Prefer public APIs and read-only access. Do not grant withdrawal permissions. Do not enable trading unless the user explicitly wants execution and understands the risk.

## When to Use

Use this skill when the user wants to:

- Manage a multi-paged professional terminal for analysis and active trading
- Research coins, narratives, sectors, categories, and market breadth
- Compare spot / perp conditions across Binance, Bybit, MEXC, Bitget, and Hyperliquid
- Execute trades directly from a calculated risk model
- Monitor live open positions and PnL alongside research

Do **not** use this skill for:

- Automated live execution with fund-moving permissions
- Copy-trading based solely on social hype
- Blindly trading illiquid meme tokens without liquidity / FDV / unlock review
- Any workflow that assumes a public API response is enough without cross-checking

## Safety Model

### Levels of access

1. **Public read-only**
   - No API keys needed
   - Safest default
   - Use for prices, candles, order books, funding, OI, sector scans, liquidity checks

2. **Account read-only**
   - API key allowed only if it can **view** balances / positions / orders / history
   - Use for portfolio review and journaling
   - Do not enable trading or withdrawals

3. **Execution access**
   - Outside this skill's safe default
   - Only consider after explicit user approval and a separate execution-specific workflow

### Non-negotiable rules

- Prefer **public endpoints first**
- If using exchange API keys, require **read-only** permissions only
- Keep **withdrawals OFF**
- Keep **trading OFF** unless the user explicitly asks for live execution later
- Prefer **IP whitelisting** for any account API key
- Treat micro-cap and fresh-launch tokens as hostile until liquidity / holder / unlock / contract checks pass
- Never treat social momentum as sufficient due diligence

## Data Sources and What Each Is Best For

### CoinGecko
Best for:
- market cap ranking
- category / sector comparisons
- ATH/ATL context
- circulating vs max supply context
- exchange-independent market overview

Use CoinGecko when the user asks:
- "What are the top AI coins by market cap?"
- "Which narratives are outperforming this week?"
- "Compare SOL, ETH, BNB, TON"
- "Show fully diluted valuation vs current market cap"

Key fields to prioritize:
- price
- 24h / 7d / 30d change
- market cap
- FDV
- circulating supply
- max supply
- volume / market cap ratio

### DEXScreener
Best for:
- fastest token pair discovery
- new pairs / momentum checks
- DEX liquidity and recent activity
- comparing chain-specific pair behavior

Use DEXScreener when the user asks:
- "Is this token real or just hype?"
- "Which pair has the most liquidity?"
- "How much volume did this pair do in the last 24h?"
- "What chain is getting the best liquidity for this ticker?"

Key fields to prioritize:
- pair address
- chain
- DEX name
- liquidity
- FDV / market cap if shown
- 5m / 1h / 6h / 24h price change
- buys vs sells
- tx count
- age of pair

### Binance read-only
Best for:
- major CEX price discovery
- spot and futures market data
- order book / depth context
- funding / open interest review
- optional account portfolio review using read-only keys

Use Binance when the user asks:
- "Check BTCUSDT funding and depth"
- "Compare spot vs perp behavior"
- "Show my read-only Binance balances"
- "Review my recent closed positions"

### Bybit read-only
Best for:
- futures-heavy market read
- perp data cross-check against Binance
- optional account review if using read-only keys
- alternative exchange perspective when Binance conditions differ

Use Bybit when the user asks:
- "Compare BTC perps between Binance and Bybit"
- "Show the cleaner liquidation / funding setup"
- "Review read-only Bybit exposure"

## Proactive Research & Dashboard Recovery

When assisting the user with crypto research, especially if they mention a "dashboard":
- Always check if the dashboard service is running (default port `8765`).
- If the user cannot access `http://192.168.0.222:8765/`, verify the server is listening on `0.0.0.0` (not just `127.0.0.1`) to allow LAN access.
- Be proactive in identifying identifying relevant research tools (Binance, Bybit, DEXScreener) even if the user doesn't explicitly ask for a check; they prefer an agent that stays grounded in current live data.
- Note that the user's hardware (Asus X455L, 8GB RAM, no dGPU) means scripts should be lightweight (standard Python via CLI/HTTP is preferred over heavy UI frameworks).

## Standard Workflow

### 1. Start broad
For a new idea, begin with:
- CoinGecko market-cap and category context
- major narrative peers
- 24h / 7d / 30d performance
- FDV and supply structure

### 2. Check tradability
Then inspect:
- DEXScreener liquidity and active pair quality
- exchange availability on Binance / Bybit
- spread / volume / order book depth
- signs of one-sided retail chase

### 3. Build the trade thesis
Answer clearly:
- why this asset now?
- what invalidates the thesis?
- what event / level matters?
- is this scalp, swing, or position trade?

### 4. Size risk before entry
Always compute:
- account size
- max % risk per trade
- entry
- stop
- target(s)
- reward:risk
- dollar loss if stopped

### 5. Set alerts
Create alerts around:
- thesis invalidation
- breakouts / breakdowns
- funding extremes
- unusual OI changes
- sudden liquidity collapse
- strong relative strength vs BTC / ETH / SOL benchmark

## Pre-Trade Checklist

Before approving a setup, check:

- [ ] What category / narrative is this in?
- [ ] Is the asset outperforming or lagging peers?
- [ ] Is spot leading or are perps overheated?
- [ ] Is liquidity sufficient for intended size?
- [ ] What is the nearest invalidation level?
- [ ] What is the exact stop, not a vague idea?
- [ ] Is the reward:risk at least acceptable for the setup?
- [ ] Any unlock / listing / macro catalyst nearby?
- [ ] Is this a liquid major, mid-cap, or dangerous micro-cap?
- [ ] Do not enter if the stop is undefined

## Risk Calculator / Position Sizing

### Core formula

For long or short planning:

- `risk_amount = account_equity × risk_percent`
- `stop_distance = abs(entry - stop)`
- `position_size_units = risk_amount / stop_distance`
- `position_notional = position_size_units × entry`

### Example

- account equity: $10,000
- risk per trade: 1%
- entry: 105
- stop: 100
- risk amount: 100
- stop distance: 5
- size: 20 units
- notional: 20 × 105 = 2,100

### Practical rules

- 0.25% to 0.5% risk for high-volatility / low-confidence setups
- 0.5% to 1.0% risk for normal swing setups
- avoid >1% risk unless the user specifically uses aggressive sizing
- reduce size when liquidity is thin or slippage is likely
- use smaller size for fresh listings, memes, or low-liquidity DEX pairs

### What to report back

Whenever sizing a trade, return:
- account equity used
- risk % used
- entry
- stop
- stop distance
- max loss if stopped
- size in units
- approximate notional
- R multiple to each target

## Read-Only Exchange Guidance

### Binance read-only account mode
If the user wants account visibility:
- allow only reading balances, positions, orders, and history
- disable spot/futures trading permissions
- disable withdrawals
- prefer IP whitelist
- test with harmless account endpoints first

### Bybit read-only account mode
Same principles:
- read-only scope only
- no withdrawals
- no order placement permissions
- IP restrictions if available
- verify key permissions before trusting the integration

### If the user only needs research
Do **not** request API keys.
Use public market data only.

## Alert Workflow

There are two good Hermes-native alert patterns.

### Pattern A: Scheduled watcher with cronjob
Use when polling is enough.
Examples:
- check BTC funding every hour
- watch a list of DEX pairs for liquidity drop
- summarize top gainers every morning

Design rules:
- make cron prompts fully self-contained
- specify exact sources and thresholds
- define what counts as "send nothing"
- keep output short and actionable
- for script-driven jobs, prefer `scripts/threshold_checker.py --silent-if-none`

Example prompt shape:

```text
Check BTC, ETH, SOL, and BNB market state.
Use CoinGecko for broad context, DEXScreener for DEX momentum if relevant, and Binance/Bybit public data for exchange context.
Only notify me if one of these happens:
1. 24h move > 8%
2. funding becomes extreme
3. liquidity on the main DEX pair drops sharply
4. open interest diverges strongly from price
If nothing important changed, stay silent.
```

### Pattern B: Webhook-triggered alert
Use when an external service or script pushes events.
Examples:
- TradingView webhook
- custom scanner
- exchange-specific notifier
- on-chain bot or mempool watcher

For this, combine Hermes with the `webhook-subscriptions` skill.

Recommended webhook payload fields:
- symbol
- venue
- timeframe
- price
- trigger_reason
- threshold
- supporting context

Then tell Hermes to:
- summarize what happened
- compare with prior thesis
- suggest whether this is action-worthy or noise

## Helper Scripts

The skill now includes real helper scripts under `scripts/`.

### Available scripts
- `scripts/coingecko_client.py`
  - `trending`
  - `search <query>`
  - `coin <coin_id>`
  - `markets --vs usd --per-page 10 --page 1`
  - `category <category_id>`
  - `categories --top 20`

- `scripts/dexscreener_client.py`
  - `search <query>`
  - `token <token_address>`
  - `pair <chain_id> <pair_address>`
  - `boosts --top 20`

- `scripts/binance_public.py`
  - `price BTCUSDT`
  - `book BTCUSDT --limit 10`
  - `candles BTCUSDT --interval 1h --limit 24`
  - `funding BTCUSDT`
  - `oi BTCUSDT`
  - `ticker BTCUSDT`

- `scripts/hyperliquid_client.py`
  - public mid-price, funding, OI, and volume discovery
- `scripts/mexc_client.py`
  - public price and 24h ticker feed
- `scripts/bitget_client.py`
  - public futures price and funding feed
- `scripts/binance_trade.py`
  - direct trade execution for Binance Futures; requires keys in `.env`

- `scripts/risk_calc.py`
  - `size --equity 12000 --risk-pct 0.75 --entry 2.45 --stop 2.31 --target 2.70 --target 2.95`

- `scripts/watchlist_parser.py`
  - `templates/watchlist.yaml` -> structured JSON

- `scripts/threshold_checker.py`
  - `--watchlist templates/watchlist.yaml`
  - `--watchlist templates/watchlist.yaml --silent-if-none`

- `scripts/pro_dashboard.py`
  - one command for CoinGecko overview + DEX scan + Binance/Bybit perp context + risk sizing + alert summary

- `scripts/market_analyzer.py`
  - current-coin analyzer with setup/risk scoring
  - watchlist scanner with top opportunities and top risks

- `scripts/sector_strength.py`
  - no-token grouped-sector strength summary

- `scripts/opportunity_digest.py`
  - Telegram-ready top-opportunities digest without any model

- `scripts/daily_market_brief.py`
  - no-model daily market brief built from scanner + sector data

- `scripts/notification_digest.py`
  - no-token price-alert digest for cron/manual sending; silent mode supported

- `scripts/browser_dashboard_server.py`
  - local browser server for the dashboard UI

- `scripts/start_browser_dashboard.sh`
  - start helper; defaults to `0.0.0.0:8765` for LAN access

- `scripts/stop_browser_dashboard.sh`
  - stop helper for the browser dashboard

- `scripts/status_browser_dashboard.sh`
  - quick running/not-running status check

- `assets/dashboard.html`
  - browser UI for market snapshot, risk, alerts, analyzer, scanner, favorites, mini charts, notification rules, preset selector, and auto-refresh

- `templates/notification-rules.sample.json`
  - starter notification rules for price-above / price-below checks

- references/standalone-and-autostart.md
  - manual non-Hermes runtime, helper commands, reboot persistence, systemd autostart, and top-50 preset caveats
- references/execution-and-hedge-mode.md
  - operational guide for the Binance execution bridge, multi-exchange data mapping, and hedge mode logic

### Usage notes
- These scripts are **read-only** except `risk_calc.py`, which is local math only.
- Prefer them when you want deterministic structured output instead of free-form reasoning.
- Start with public market-data scripts before requesting any exchange account API keys.

## Manual Terminal Research (Bypassing Bot Detection)

When search engines (Google/DuckDuckGo) block browser tools or scripts, use manual terminal commands to fetch raw news data.

### 1. Direct Exchange API Price/Movers
Use Binance or CoinGecko public APIs via `curl`.
- **Binance 24h Ticker:** `curl -s "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"` (use `grep -oP '"priceChangePercent":"\K[^"]+'` to extract %)
- **CoinGecko 24h Change:** `curl -s "https://api.coingecko.com/api/v3/coins/bitcoin" | grep -oP '"price_change_percentage_24h":\K[^,]+'`

### 2. Industry RSS Feeds (High Signal, Low Scraping Friction)
RSS feeds are often unblocked and provide cleaner headlines than search engines.
- **Decrypt:** `curl -s "https://decrypt.co/feed" | grep -oP '<title>\K[^<]+'`
- **The Block:** `curl -s "https://www.theblock.co/rss.xml" | grep -oP '<title>\K[^<]+'`
- **CoinTelegraph:** `curl -s "https://cointelegraph.com/rss" | grep -oP '<title>\K[^<]+'`

### 3. Extracting Context from RSS
To get descriptions/reasons without opening a browser:
```bash
# Find a headline and show the next 20 lines (usually contains <description>)
curl -s "https://decrypt.co/feed" | grep -A 20 "Headline Keyword" | grep -oP '<description>\K[^<]+'
```

### 4. Search Engine Fallbacks
- If Google blocks, try **DuckDuckGo** (`https://duckduckgo.com/?q=...`).
- If DDG also blocks via browser, try to grep the HTML source via `curl -L` if they don't use heavy JS, though this is rarely successful.

## Browser Dashboard

The skill also includes a real local browser dashboard.

What it gives you:
- form inputs for symbol, CoinGecko ID, DEX query, watchlist, and risk inputs
- market snapshot cards
- DEX top-pairs table
- risk model panel
- alerts panel
- raw JSON panel for debugging
- dynamic symbol preset selector populated from the trading-focused watchlist, not a tiny hardcoded list
- watchlist preset selector
- top-50 watchlist preset generated from CoinGecko market-cap leaders
- trading-focused top-50 preset filtered toward exchange-listed, non-stablecoin names
- searchable preset dropdown fed from the selected watchlist preset
- grouped watchlist presets for AI, L1/L2, RWA, and Memes only
- browser symbol preset filtering that hides meme/stable-like entries while explicitly keeping DOGE and PEPE
- a searchable symbol preset input that filters the dropdown live
- symbol preset options sourced from the currently selected watchlist preset; default the page to `top50-trading` so the symbol dropdown is rich on first load
- analyzer panel with setup score, risk score, stance, reasons, and risks for the current coin
- **Multi-Page Layout**: Tabbed navigation for Analysis, Trading, Scanner, and Settings to avoid a "haphazard" UI
- **Trading Panel**: Direct BUY/SELL buttons for one-tap execution based on the calculated risk model
- **Live Positions**: Real-time position and PnL tracking for Binance Futures
- **Hedge Mode Toggle**: Switches the entire UI to dual-direction inputs (Long vs Short)
- **API Key Manager**: Input and save keys for Binance, Bybit, and Hyperliquid locally to `.env` from the browser
- **Execution Controls**: UI hooks for Close All, Break-Even SL, and Scale-In TP Grid
- watchlist scanner panels for top opportunities and top risks
- notification rules with price-above / price-below checks and browser notification hooks
- favorites persistence and quick reload buttons
- mini charts from Binance and Bybit 1h candles
- no-token sector summary, daily brief, top-opportunity digest, and price-alert digest flows
- auto-refresh every 15s / 30s / 60s / 5m
- reference notes for preset curation, grouped-watchlist contents, browser refresh/cache pitfalls, and standalone/autostart behavior

### Preset curation rules
When updating dashboard presets for active trading use:
- do not leave the symbol dropdown as a short hardcoded list if a richer preset watchlist already exists
- prefer loading symbol options dynamically from the active watchlist preset; if the page needs a good first-run default, point the watchlist preset at `top50-trading`
- support a live search box for the symbol preset dropdown once the list grows beyond a handful of names
- exclude stablecoins, cash-like/tokenized-yield assets, and obvious non-trading placeholders from symbol presets
- exclude meme-heavy entries by default, but keep explicitly-approved exceptions such as DOGE and PEPE when the user wants them visible
- grouped watchlists can intentionally re-include excluded names when the group itself is theme-specific (for example `memes` may include SHIB and other meme names even if the default trading preset hides them)
- after changing preset generation, restart the dashboard service and verify the rendered dropdown in-browser, not only via file inspection
- if the browser still shows an old short dropdown after edits, do a hard refresh; stale browser cache can preserve the old failed state

Start it with:
```bash
python3 /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/browser_dashboard_server.py
```
Then open:
```text
http://127.0.0.1:8765
```

For LAN access, use the helper script:
```bash
bash /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/start_browser_dashboard.sh
```
This defaults to `0.0.0.0:8765`, so other devices on the same network can use `http://<your-lan-ip>:8765`.

Stop it with:
```bash
bash /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/stop_browser_dashboard.sh
```

Important runtime notes:
- the dashboard stack runs on plain Python and does **not** require Hermes at runtime
- `nohup` / helper-script startup survives terminal close but does **not** survive a reboot
- for auto-start after restart, use a systemd service; see `references/standalone-and-autostart.md`

This stays read-only. The browser UI calls the local helper scripts through a small local HTTP server.

## Prompt Recipes

### CoinGecko scan
"Use CoinGecko-style market analysis. Compare the top 10 coins in the AI category by market cap, 7d performance, FDV, and volume/market-cap ratio. End with the 3 strongest and 3 weakest setups."

### DEXScreener pair quality
"Evaluate this token on DEXScreener-style criteria: chain, main pair, liquidity, age, 24h volume, buy/sell balance, and whether the pair looks tradable or dangerous."

### Binance/Bybit perp comparison
"Compare BTC perpetuals using public Binance and Bybit-style metrics: mark price, funding, open interest, and whether price/OI/funding align bullishly or look crowded."

### Position sizing
"Account equity is 12,000 USDT. Risk 0.75% on a long entry at 2.45 with stop at 2.31 and targets 2.70 / 2.95. Calculate size, notional, max loss, and reward:risk to each target."

### Alert summary
"Summarize whether this alert matters or is noise. Include: what changed, why it matters, invalidation level, and what I should watch next."

## Watchlist Structure

Maintain watchlists with these fields:
- ticker
- category / narrative
- venue(s)
- thesis
- invalidation
- key support
- key resistance
- desired entry zone
- stop zone
- alert thresholds
- notes on liquidity / catalysts

Recommended structured fields for automation:
- `symbol` for CEX symbols like `BTCUSDT`
- `coingecko_id` for deterministic CoinGecko lookups
- `dex_query` for DEXScreener searches
- `token_address`, `chain_id`, `pair_address` for direct DEX targeting
- `price_above`, `price_below`
- `move_24h_abs_threshold_pct`
- `funding_abs_threshold`
- `oi_divergence_threshold_pct`
- `liquidity_floor_usd`

If the user has many assets, group by:
- majors
- high-beta majors
- narrative leaders
- DEX punts / high-risk ideas
- event-driven trades
- broad market-cap presets such as top-50

Caution: a market-cap-based top-50 preset can include stablecoins, gold-backed assets, exchange tokens, and other names that are useful for monitoring but not ideal as a pure discretionary trading list.

### 7. Dual-Direction / Hedge Mode Support
The dashboard and risk calculator now support **Hedge Mode** (simultaneous Long and Short positions).
- **Toggle:** Use the "Mode" dropdown in the Controls to switch to Hedge.
- **Calculator:** In Hedge Mode, separate inputs for `Long Entry/Stop` and `Short Entry/Stop` appear. The `risk_calc.py` and `pro_dashboard.py` scripts then calculate and return both sides.
- **Exposure:** The risk table will display Long and Short stats side-by-side for unified perspective on net risk.

## Common Pitfalls

1. **Confusing market cap and FDV.**
A token can look cheap by current market cap and still be expensive by FDV if unlock pressure is large.

2. **Ignoring liquidity.**
A setup is not tradable at the desired size if liquidity is thin or concentrated in one fragile pair.

3. **Treating perp enthusiasm as bullish by default.**
High positive funding plus rising OI can mean a crowded long, not strength.

4. **Using read-only keys incorrectly.**
If account access is needed, verify the key truly cannot trade or withdraw.

5. **No invalidation level.**
If the stop is undefined, the trade plan is incomplete.

6. **Oversizing meme and low-float tokens.**
Use smaller risk for anything illiquid, newly launched, or socially manipulated.

7. **Alert spam.**
Bad alerts are too frequent and too vague. Use thresholds and silence rules.

8. **Relying on one venue only.**
Cross-check CoinGecko, DEXScreener, and at least one major exchange perspective before strong conclusions.

9. **Assuming top-50 market cap equals top-50 tradable setups.**
Market-cap presets are good for breadth monitoring, but they may include stablecoins, tokenized gold, exchange tokens, and other assets that are not ideal for an active trading watchlist.

## Verification Checklist

- [ ] Workflow is read-only by default
- [ ] Public data is used unless account visibility is truly needed
- [ ] Any account API key is read-only, no trading, no withdrawals
- [ ] Trade thesis includes entry, invalidation, and time horizon
- [ ] Position size is calculated before discussing execution
- [ ] Alerts specify thresholds and silence behavior
- [ ] Liquidity, FDV, and crowding are checked before endorsing a setup

## One-Shot Recipes

### Recipe: Safe first-pass token review
1. Use CoinGecko to place the token in market-cap and category context
2. Use DEXScreener to inspect pair quality and liquidity
3. Check whether Binance or Bybit listing / perp context changes the read
4. Summarize thesis, invalidation, and risk tier

### Recipe: Read-only portfolio review
1. Pull balances / positions from a read-only exchange key if the user has one
2. Group holdings by majors / alts / high-risk names
3. Highlight concentration risk
4. For each position, define what price or thesis event matters next
5. Propose alerts instead of immediate action

### Recipe: Morning market brief
1. Broad market snapshot from CoinGecko
2. DEX momentum scan from DEXScreener
3. Binance / Bybit funding and OI crowding check
4. Top three opportunities
5. Top three risks
6. Alert-worthy levels for the session

## Related skills

- `nextjs-dual-deploy` (with `references/exchange-integration-pattern.md`) — for **execution-capable** standalone Next.js apps that go beyond this skill's read-only model: encrypted exchange API key storage (AES-256-GCM), HMAC-signed REST adapters (Bybit + Binance), SQLite trade history, auto-sync via `node-cron`, live positions/orders widgets, and place-order/cancel flows. Use that when the user wants to **store API keys, place orders, and run inside Docker**. This skill stays read-only by design.
