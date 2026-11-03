# Dashboard Upgrade Notes

Latest upgrades added:

- analyzer scoring for the current coin
- watchlist scanner with top opportunities and top risks
- notification rules stored in `notification_rules.json`
- browser-side notification checks
- favorites persistence in `favorites.json`
- mini charts from Binance and Bybit 1h candles

Key runtime files:

- `scripts/market_analyzer.py`
- `scripts/browser_dashboard_server.py`
- `assets/dashboard.html`
- `templates/notification-rules.sample.json`

Notes:
- notification rules are browser/local rules, not Telegram alerts yet
- use small presets like `ai`, `majors`, or `l1l2` for faster scans
- `top50-trading` is broader and slower by design
