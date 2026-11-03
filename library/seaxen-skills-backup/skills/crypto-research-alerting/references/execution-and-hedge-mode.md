# Trading Dashboard: Hedge Mode & Execution

## Overview
This reference covers the May 2026 upgrade that transformed the dashboard from read-only research into a full **Futures Trading Dashboard**.

## Execution Bridge
Trade execution is handled by `scripts/binance_trade.py`. 
- **Mechanism**: The browser dashboard sends a POST request to `/api/trade` (on the Python server), which then spawns the trading script.
- **Safety**: A `window.confirm` dialog is required in the browser before any order is sent.

## Hedge Mode Logic
The system now supports simultaneous Long and Short positions.
- **UI**: Toggling "Hedge Mode" in the dropdown shows distinct input fields for Long and Short parameters.
- **Calculation**: Both sides are calculated independently by `risk_calc.py`, but their risk stats are unified in the dashboard view.

## Exchange Data Mapping
The dashboard polls the following venues for real-time validation before trade execution:
- **Binance**: Primary execution target (Futures).
- **Hyperliquid**: Lead indicator for price/funding.
- **MEXC/Bitget**: Alternative liquidity benchmarks.
- **CoinGecko**: Global valuation context.

## Setup Instructions
1. Ensure `BINANCE_API_KEY` and `BINANCE_API_SECRET` are present in a `.env` file in the skill root.
2. Ensure the Binance account is set to **Hedge Mode** in the official app/website if using the Hedge toggle.
3. Access at `http://192.168.0.222:8765`.
