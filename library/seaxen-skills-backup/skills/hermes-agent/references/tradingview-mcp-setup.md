# TradingView MCP Setup for Hermes

Two distinct TradingView MCP servers exist, with different setup requirements:

## 1. tradingview-ta (atilaahmettaner/tradingview-mcp) — TA/Backtesting Framework

**Source:** `uvx tradingview-mcp` (works via uvx)

**Features:** 73 tools — technical analysis, backtesting, Pine Script generation/optimization, multi-timeframe analysis, market scanners, sentiment, paper trading, risk tools.

**Setup:**
```bash
hermes mcp add tradingview-ta --command uvx --args "tradingview-mcp"
```
(no auth needed for basic Yahoo Finance data)

---

## 2. tradingview-chart (ertugrul59/tradingview-chart-mcp) — Chart Screenshots

**Source:** GitHub repo (NOT on PyPI/uvx) — requires local installation.

**Features:** `get_tradingview_chart_image(ticker, interval)` → returns chart screenshot (base64 or direct URL).

**Prerequisites:**
- Python 3.10+
- Chromium + chromedriver (matching version)
- TradingView account with session cookies

**Installation:**
```bash
git clone https://github.com/ertugrul59/tradingview-chart-mcp /mnt/tb/hermes/scripts/mcp-servers/tradingview-chart-mcp
cd /mnt/tb/hermes/scripts/mcp-servers/tradingview-chart-mcp
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
# Ensure chromedriver is installed (apt-get install chromium chromium-driver)
```

**Required Cookies (both mandatory):**
| Cookie | Example |
|--------|---------|
| `sessionid` | `f6ed4tfe1efagatsf1jnnru0yov1ftzi` |
| `sessionid_sign` | `v3:RTofZowdFbfNGWQa5CWGnH7DE+kzzMXobS/MfwYkDRo=` |

Get from browser DevTools → Application → Cookies → `www.tradingview.com` (may need to check `.tradingview.com` too).

**Hermes Config (under `mcp.servers`):**
```yaml
tradingview-chart:
  command: /mnt/tb/hermes/scripts/mcp-servers/tradingview-chart-mcp/.venv/bin/python
  args:
    - /mnt/tb/hermes/scripts/mcp-servers/tradingview-chart-mcp/main_optimized.py
  enabled: true
  env:
    TRADINGVIEW_SESSION_ID: "your_sessionid"
    TRADINGVIEW_SESSION_ID_SIGN: "your_sessionid_sign"
    MCP_SCRAPER_HEADLESS: "true"
    MCP_SCRAPER_USE_SAVE_SHORTCUT: "true"
```

**Test:**
```bash
hermes mcp test tradingview-chart
# Should show: ✓ Connected, Tools discovered: 2 (get_tradingview_chart_image, get_performance_stats)
```

---

## Common Pitfalls

| Issue | Fix |
|-------|-----|
| `uvx tradingview-chart-mcp` fails | Package doesn't exist on PyPI — must clone GitHub repo |
| Connection fails: `No such file or directory: 'python'` | Use full venv python path in config |
| Tools not discovered | Ensure both `sessionid` AND `sessionid_sign` are set |
| Selenium/Chrome errors | Install `chromium` and `chromium-driver` matching versions |
| YAML corruption from `hermes config set` | Edit config.yaml directly or use Python YAML library for nested structures |

---

## Quick Test Commands

After setup and session restart:
```bash
# Chart screenshot
get_tradingview_chart_image ticker="SOLUSDT" interval="1h"

# TA analysis (tradingview-ta)
coin_analysis symbol="BTCUSDT"
multi_timeframe_analysis symbol="BTCUSDT"
backtest_strategy ...
market_sentiment symbol="BTC"
```