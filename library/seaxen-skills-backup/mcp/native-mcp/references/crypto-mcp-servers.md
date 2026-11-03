# Crypto / Blockchain MCP Servers — Hermes Compatibility Reference

## Tested Servers (May 2026)

| MCP | Repo | Install | Transport | Tools | Free? |
|-----|------|---------|-----------|-------|-------|
| DexScreener | `janswist/mcp-dexscreener` | git clone + npm | stdio | 8 | ✅ No key |
| crypto-data-mcp | `Wh0FF24/crypto-data-mcp` | git clone + uv + wrapper | stdio | 5 | ✅ No key |
| CoinGecko | Official | `--url` only | HTTP | 2 | ✅ No key |
| Bybit | `sammcj/bybit-mcp` | git clone + npm + build | stdio | 12 | ✅ Public API (no key for market data) |
| Alpha Vantage | `berlinbra/alpha-vantage-mcp` | git clone + uv + wrapper | stdio | 12 | ⚠️ Needs free API key |
| **graph-polymarket** | `PaulieB14/graph-polymarket-mcp` | pre-built at `/mnt/tb/hermes/scripts/mcp-servers/graph-polymarket-mcp/` | stdio | 31 | ✅ Free; 10/31 work without `GRAPH_API_KEY` |
| **crypto-news** | local wrapper | pre-built at `/mnt/tb/hermes/scripts/mcp-servers/crypto-news-mcp/` | stdio | 2 | ✅ 100% free, no key (RSS) |
| **cryptopanic-mcp-server** | `kukapay/cryptopanic-mcp-server` | pre-built at `/mnt/tb/hermes/scripts/mcp-servers/cryptopanic-mcp-server/` | stdio | 1 | ⚠️ Needs CryptoPanic API key |
| **defillama** | `dcSpark/mcp-server-defillama` | git clone + npm + build → `node dist/index.js` | stdio | 7 | ✅ No key (TVL, chain TVL, protocols, token prices, stablecoins) |
| **coinmarketcap** | `longmans/coin_api_mcp` (uvx from git) | uvx | stdio | 3 | ✅ Free 333 calls/day Hobbyist tier |
| **crypto-feargreed** (kukapay) | `kukapay/crypto-feargreed-mcp` | uvx from git (pre-built) | stdio | 3 | ✅ No key (Alternative.me API) |
| **coinglass** | `GPSxtreme/mcp-coinglass` | git clone + pnpm + build | stdio | 7 | ❌ **PAID ONLY** — all endpoints return `401 Upgrade plan` on free tier |

## Important Pitfalls

### 1. CoinGecko SSE endpoint does NOT work with Hermes
- ❌ `https://mcp.api.coingecko.com/sse` — connects then session terminates
- ✅ `https://mcp.api.coingecko.com/mcp` — HTTP transport, works

### 2. crypto-data-mcp is NOT on PyPI
- `uvx crypto-data-mcp` → fails "package not found"
- Must clone from GitHub, run `uv sync`, create wrapper script

### 3. `hermes mcp add` is always interactive
- Pipe `printf 'y\n'` (not `echo -e "Y\n"`) for non-interactive confirmation in shell automation
- For URL-based servers with auth, may need `printf 'n\ny\n'` to skip the auth prompt

### 4. Wrapper scripts fix npm args issues
- Direct: `hermes mcp add X --command node --args /path/index.js` → may fail
- Wrapper: Create `run.sh` → `exec node index.js` → point Hermes at wrapper

### 5. Alpha Vantage import path
- ❌ `uv run src/alpha_vantage_mcp/server.py` → ImportError (relative import)
- ✅ `uv run python -m alpha_vantage_mcp.server` → works
- Wrapper must use: `exec uv run python -m alpha_vantage_mcp.server`

### 6. Enabling disabled servers via config edit
When `hermes mcp add` saves a server as disabled (connection failed), edit config directly with Python:
```python
import yaml
p = '/mnt/thermes/config.yaml'
with open(p) as f:
    cfg = yaml.safe_load(f)
cfg['mcp_servers']['SERVER_NAME']['enabled'] = True
cfg['mcp_servers']['SERVER_NAME']['env']['API_KEY'] = 'real_key'
with open(p, 'w') as f:
    yaml.dump(cfg, f, default_flow_style=False, allow_unicode=True)
```
Config key is `mcp_servers` (not `mcp` or `servers`).

### 7. `hermes mcp add --env KEY=*** saves literal "test-key" when no real value
The CLI's `--env KEY=*** substitutes `*** → `test-key` and saves it to config.yaml. Fix one of two ways:
- **Preferred:** Omit the `--env` flag entirely at install time. The server still works for any tool that doesn't need the key (e.g. graph-polymarket's 10 REST-based tools, all of crypto-news).
- **Cleanup:** `sed -i '/^  <name>:$/,/^    enabled: true$/{ /^    env:$/,/^      KEY: test-key$/d }' /root/.hermes/config.yaml`

### 8. Coinglass is paid-only — never install on free tier
The `GPSxtreme/mcp-coinglass` MCP connects fine and discovers 7 tools, but every tool call returns `401 "Upgrade plan"` on the free API key. Don't install unless the user has a paid plan. Symptoms: `mcp test` passes, but a real call like `COINGLASS_FUNDING_RATE(symbol="BTC")` returns:
```json
{"code":"401","msg":"Upgrade plan"}
```
**Alternative free data sources for the same use cases:**
- Open interest / funding → `mcp_bybit_get_ticker` (Bybit MCP, free public data)
- Liquidations → `crypto-liquidations` (kukapay, free, no key)
- Long/short ratio → not free anywhere reliable; TradingView-TA proxies indicators

### 9. Always `hermes mcp list` BEFORE adding a new MCP
Multiple MCPs serve the same purpose with different names:
- Fear & Greed: both `crypto-feargreed` (kukapay) and `feargreed` (any clone) — pick one
- News: `crypto-news` (RSS) vs `cryptopanic-mcp-server` (needs API key)
- DEX data: `dexscreener` (any token/pair) vs `crypto-data` (basic only)

Always `hermes mcp list` first. The pre-built `crypto-feargreed` is at `/mnt/tb/hermes/scripts/mcp-servers/crypto-feargreed-mcp/` and points to a uvx-from-git config that already works — don't clone again.

### 10. DefiLlama MCP install pattern (dcSpark)
The official DefiLlama MCP (`https://mcp.defillama.com/mcp`) requires a paid API plan. For free use:
- `npx -y @supernova123/defillama-mcp-server` → works but is **deprecated** by author
- `npx -y @mcp-dockmaster/mcp-server-defillama` → 404, package name wrong
- `npx -y @iflow-mcp/dcspark-mcp-server-defillama` → exists but thin wrapper
- **Best: clone dcSpark repo, build, run from dist/**
```bash
cd /mnt/tb/hermes/scripts/mcp-servers
git clone --depth 1 https://github.com/dcSpark/mcp-server-defillama.git defillama-src
cd defillama-src && npm install && npm run build
# Wrapper script
cat > /mnt/tb/hermes/scripts/mcp-servers/defillama-mcp/run.sh <<'EOF'
#!/usr/bin/env bash
exec node /mnt/tb/hermes/scripts/mcp-servers/defillama-src/dist/index.js
EOF
chmod +x /mnt/tb/hermes/scripts/mcp-servers/defillama-mcp/run.sh
printf 'y\n' | hermes mcp add defillama --command /mnt/tb/hermes/scripts/mcp-servers/defillama-mcp/run.sh
```
7 tools: protocols, protocol_tvl, chain_tvl, token_prices, historical_prices, stablecoins, stablecoin_data.

## Server Details

### DexScreener MCP
- **Tools**: getLatestTokenProfiles, getLatestBoostedTokens, getMostActiveBoostedTokens, checkTokenOrders, getPairByChainAndAddress, searchPairs, getTokenPools, getPairsByToken
- **Best for**: On-chain token discovery, new pair scanning, DEX analytics

### crypto-data-mcp
- **Tools**: get_price, get_prices, get_market_overview, get_token_info, get_historical_prices
- **Best for**: Clean price queries, batch prices, market snapshots

### CoinGecko MCP (HTTP)
- **Tools**: execute (JS sandbox), search_docs
- **Best for**: Flexible CoinGecko API queries via JS execution

### Bybit MCP
- **Tools**: get_instrument_info, get_kline, get_ml_rsi, get_market_info, get_market_structure, get_order_blocks, get_order_history, get_orderbook, get_positions, get_ticker, get_trades, get_wallet_balance
- **Public API**: All market data tools work without API key
- **Account tools** (positions, wallet, order history): need read-only API key
- **Safety**: No trading/withdrawal capability — read-only MCP
- **Chart generation**: WebUI includes "Chart Integration: Auto-generate charts when AI mentions price data" (DEV_PLAN.md) — charts render from `get_kline` OHLCV data
- **Install location**: `/root/.hermes/scripts/mcp-servers/bybit-mcp/` — already cloned, built, but **disabled** in Hermes config (missing credentials)
- **To enable**: Add `BYBIT_API_KEY` + `BYBIT_API_SECRET` + `BYBIT_USE_TESTNET=false` to env (via Bitwarden or `.env`), then `hermes mcp enable bybit`

### Alpha Vantage MCP
- **Tools**: get-stock-quote, get-company-info, get-crypto-exchange-rate, get-time-series, get-historical-options, get-crypto-daily, get-crypto-weekly, get-crypto-monthly, get-earnings-calendar, get-historical-earnings, get-realtime-options, get-etf-profile
- **Best for**: Stocks, ETFs, options, earnings, forex, crypto
- **Free tier**: 25 requests/day, 5 requests/min
- **API key**: Get free key at https://www.alphavantage.co/support/#api-key
- **Wrapper must use**: `exec uv run python -m alpha_vantage_mcp.server`

### Polymarket — graph-polymarket-mcp (recommended)
- **Tools**: 31 — search, live prices, orderbook, price history, on-chain analytics
- **10 REST-based tools work without any key** (hit public Gamma/CLOB APIs):
  - `search_markets`, `get_market_info`, `list_polymarket_events`, `get_polymarket_event`
  - `get_live_prices`, `get_live_spread`, `get_live_orderbook`
  - `get_price_history`, `get_last_trade`, `get_clob_market`, `search_markets_enriched`
- **21 on-chain subgraph tools need free `GRAPH_API_KEY`** (sign up at https://thegraph.com/studio/ — 100k queries/month free):
  - `get_market_data`, `get_account_pnl`, `get_user_positions`, `get_top_traders`
  - `get_market_open_interest`, `get_oi_history`, `get_global_stats`, `get_daily_stats`
  - `get_market_positions`, `get_market_resolution`, `get_disputed_markets`, `get_trader_profile`
  - `get_recent_activity`, `get_orderbook_trades`, `get_trader_usdc_flows`, `get_global_open_interest`
  - `list_subgraphs`, `get_subgraph_schema`, `query_subgraph`, `get_market_revisions`
- **Install pattern**: `printf 'y\n' | hermes mcp add graph-polymarket --command /mnt/tb/hermes/scripts/mcp-servers/graph-polymarket-mcp/run.sh`
- **Alternative MCPs (also free, fewer tools):** `pab1it0/polymarket-mcp` (8 tools), `berlinbra/polymarket-mcp` (3 tools), `iqai/mcp-polymarket` (npm, supports trading)
- **No-MCP path:** built-in `research/polymarket` skill — direct REST API via Gamma/CLOB/Data

### crypto-news (RSS, 100% free) — recommended for news
- **Tools**: `get_crypto_news(source, limit)`, `list_sources()`
- **Sources**: CoinDesk, Cointelegraph, The Block, Decrypt, Bitcoin Magazine, CryptoSlate
- **Cost**: 100% free — public RSS feeds, no auth, no rate limits
- **Run command**: `uv run --with feedparser --with mcp[cli] python server.py`
- **Install**: `printf 'y\n' | hermes mcp add crypto-news --command /mnt/tb/hermes/scripts/mcp-servers/crypto-news-mcp/run.sh`

### cryptopanic-mcp-server (Kukapay)
- **Tools**: `get_crypto_news(kind, num_pages)`
- **Cost**: Free tier available, needs CryptoPanic API key
- **Pre-built**: `/mnt/tb/hermes/scripts/mcp-servers/cryptopanic-mcp-server/`

### DefiLlama MCP (dcSpark) — recommended for DeFi TVL
- **Tools**: `defillama_get_protocols`, `defillama_get_protocol_tvl`, `defillama_get_chain_tvl`, `defillama_get_token_prices`, `defillama_get_historical_prices`, `defillama_get_stablecoins`, `defillama_get_stablecoin_data`
- **Best for**: DeFi TVL tracking, protocol/chain analytics, token prices, stablecoin data
- **Cost**: 100% free, no key, no rate limits (DefiLlama public API)
- **Why not the official**: `https://mcp.defillama.com/mcp` requires paid API plan and uses credits per query
- **Install pattern**: see pitfall #10 above (clone + build, then `node dist/index.js`)

### CoinMarketCap MCP (longmans/coin_api_mcp) — free tier
- **Tools**: `listing-coins`, `get-coin-info`, `get-coin-quotes`
- **Best for**: CMC-ranked listings, coin descriptions, market quotes
- **Cost**: 333 calls/day free Hobbyist tier — plenty for daily use
- **Wrapper pattern** (executable name is `coin-api`, not `coin-api-mcp`):
```bash
#!/usr/bin/env bash
export COINMARKETCAP_API_KEY="${COINMARKETCAP_KEY}"
exec uvx --from git+https://github.com/longmans/coin_api_mcp coin-api
```
- **Pip warning to ignore**: standalone test errors with `I/O operation on closed file` — that's expected (no stdio client connected). It works through Hermes.

### crypto-feargreed (kukapay) — already pre-built
- **Tools**: `get_current_fng_tool`, `get_historical_fng_tool(days)`, `analyze_fng_trend(days)`
- **Source**: Alternative.me Fear & Greed Index
- **Cost**: 100% free, no key
- **Pitfall**: tool names have `_tool` suffix — `get_current_fng` will fail with "Unknown tool"
- **Pre-built**: `/mnt/tb/hermes/scripts/mcp-servers/crypto-feargreed-mcp/` — already wired with `uvx --from git+...`

### Coinglass MCP — **DO NOT INSTALL** without paid plan
- All 7 tools return `401 Upgrade plan` on free API key
- Removing an already-installed coinglass: `hermes mcp remove coinglass` (no separate `disable` subcommand)
- The free Coinglass free plan has zero endpoint access for this MCP

## Other MCPs Installed (Non-Crypto)

| MCP | Source | Tools | Key |
|-----|--------|-------|-----|
| weather | `@dangahagan/weather-mcp` (npm) | 5 — forecast, current, alerts, location, status | None |
| hackernews | `devabdultech/hn-mcp` (npm) | 9 — stories, comments, search, users | None |
| discord | `barryyip0625/mcp-discord` (git + npm) | 43 — messages, channels, roles, webhooks | Bot token for write |

## Untested but Notable
- `bobtista/solscan_mcp_server` — Solana via Solscan Pro (free tier: 10M req/month)
- `karacurt/blockscout-mcp-server` — EVM chain explorer
- `AbdelStark/bitcoin-mcp` — Bitcoin + Lightning
- `Bankless/onchain-mcp` — EVM contracts (stale, no longer maintained)
- `kukapay/crypto-feargreed-mcp` — Fear & Greed index
- `kukapay/crypto-sentiment-mcp` — multi-source sentiment
- `nirholas/free-crypto-news` — 200+ sources, no auth (npm: `@anthropic-ai/mcp-server-crypto-news`)

## TradingView MCP Servers (Charting Focus)

| Server | Source | Chart Access | Cost | Auth |
|--------|--------|--------------|------|------|
| tradingview-mcp | `atilaahmettaner/tradingview-mcp` | Structured data (indicators, price, Pine Script), **no chart images** | Free self-hosted; hosted at `pro.cryptosieve.com` = freemium | Optional TradingView session |
| TradingView Chart MCP | LangDB / LobeHub | **Chart images** (screenshots) | Free server | Requires TradingView `sessionid` cookie |
| Desktop Bridge | Open-source | Reads **your open charts** in TradingView Desktop app | Free, runs locally | Local desktop session |

**Key distinction**: The MCP servers themselves are free/open-source. Costs come from:
- TradingView premium subscription (for advanced indicators/data)
- Hosted connector services (e.g., `pro.cryptosieve.com`) may have usage tiers
- Your own TradingView account (free tier works for basic chart images via session cookie)

## Pre-Installed MCP Discovery (CRITICAL first step)

**Before searching the web for MCP servers, ALWAYS check the local install directory first.** In this environment, several MCP servers are pre-cloned and pre-built but disabled — agents have been burned by suggesting external installs when the binary was already on disk.

```bash
# Step 1: list what's already installed locally
ls /mnt/tb/hermes/scripts/mcp-servers/

# Step 2: check which are enabled in config
grep -A 3 "mcp_servers:" /root/.hermes/config.yaml | grep -E "^\s+\w+:"

# Step 3: only search for new MCPs if local options don't fit
```

The local install dir at `/mnt/tb/hermes/scripts/mcp-servers/` typically contains: `alpha-vantage-mcp`, `bybit-mcp`, `coingecko-mcp`, `coinglass-mcp`, `coinmarketcap-mcp`, `crypto-data-mcp`, `crypto-news-mcp`, `crypto-feargreed-mcp`, `cryptopanic-mcp-server`, `defillama-mcp`, `defillama-src`, `graph-polymarket-mcp`, `hn-mcp`, `mcp-dexscreener`, `notebooklm-mcp`, `tradingview-chart-mcp`, `weather-mcp`, `feargreed-src` (source clone).

Each has a `run.sh` wrapper (or `main.py` for Python ones). Inspect the wrapper's contents before adding to Hermes — the exact command + env vars needed are visible in `run.sh`.

**Activation recipe (non-interactive):**
```bash
# 1. Confirm a run.sh exists
ls /mnt/tb/hermes/scripts/mcp-servers/<name>/run.sh

# 2. Add it (auto-confirm with printf 'y\n')
printf 'y\n' | hermes mcp add <name> --command /path/to/run.sh

# 3. If env vars needed, append --env KEY=value (avoid ${} bash expansion in values)
printf 'y\n' | hermes mcp add <name> --command /path/to/run.sh --env KEY=value

# 4. Verify connection + tool discovery
hermes mcp test <name>

# 5. Start a new session — tools appear as mcp_<name>_<tool>
```
