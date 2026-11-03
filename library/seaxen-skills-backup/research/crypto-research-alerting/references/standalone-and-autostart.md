# Standalone runtime and auto-start

## Key point
The browser dashboard and helper stack can run **without Hermes at runtime**.

What Hermes is useful for:
- packaging the workflow as a skill
- managing future cron/webhook integrations
- making the workflow reusable inside agent sessions

What Hermes is **not** required for:
- running the local browser dashboard
- using the Python helper scripts directly
- using the static HTML frontend served by `browser_dashboard_server.py`

## Minimum files to copy for standalone use
- `scripts/browser_dashboard_server.py`
- `scripts/pro_dashboard.py`
- `scripts/threshold_checker.py`
- `scripts/watchlist_parser.py`
- `scripts/coingecko_client.py`
- `scripts/dexscreener_client.py`
- `scripts/binance_public.py`
- `scripts/bybit_public.py`
- `scripts/risk_calc.py`
- `assets/dashboard.html`
- `templates/watchlist.yaml`
- optional preset files such as `templates/watchlist-majors.yaml`, `templates/watchlist-dex-risk.yaml`, `templates/watchlist-top50.yaml`

## Manual start
```bash
python3 /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/browser_dashboard_server.py --host 0.0.0.0 --port 8765 --watchlist /mnt/tb/hermes/skills/research/crypto-research-alerting/templates/watchlist.yaml
```

Open:
- local: `http://127.0.0.1:8765`
- LAN: `http://<lan-ip>:8765`

## Helper scripts for manual control
Start helper:
```bash
bash /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/start_browser_dashboard.sh 0.0.0.0 8765 /mnt/tb/hermes/skills/research/crypto-research-alerting/templates/watchlist.yaml
```

Stop helper:
```bash
bash /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/stop_browser_dashboard.sh
```

Status helper:
```bash
bash /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/status_browser_dashboard.sh
```

## Persistence after reboot
`nohup ... &` or the start helper keeps the dashboard alive after terminal close, but **not after reboot**.

For auto-start after restart, use a systemd service.

Example service used successfully in-session:
- path: `/etc/systemd/system/cryptohermes-dashboard.service`
- bind: `0.0.0.0:8765`
- restart policy: `Restart=always`

Example unit:
```ini
[Unit]
Description=Crypto Hermes Browser Dashboard
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=/mnt/tb/hermes/skills/research/crypto-research-alerting
ExecStart=/usr/bin/python3 /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/browser_dashboard_server.py --host 0.0.0.0 --port 8765 --watchlist /mnt/tb/hermes/skills/research/crypto-research-alerting/templates/watchlist.yaml
Restart=always
RestartSec=5
User=root
Environment=PYTHONUNBUFFERED=1
StandardOutput=append:/mnt/tb/hermes/skills/research/crypto-research-alerting/browser_dashboard.log
StandardError=append:/mnt/tb/hermes/skills/research/crypto-research-alerting/browser_dashboard.log

[Install]
WantedBy=multi-user.target
```

Enable it:
```bash
systemctl daemon-reload
systemctl enable --now cryptohermes-dashboard.service
```

Verify it:
```bash
systemctl status cryptohermes-dashboard.service --no-pager
curl -fsS http://127.0.0.1:8765/api/health
```

## Top-50 watchlist preset
A new preset file was added:
- `templates/watchlist-top50.yaml`

It is generated from current CoinGecko top-50 market-cap leaders and exposed in the dashboard preset selector as `top50` / `Top 50`.

## Top-50 caveat
CoinGecko top-50-by-market-cap is **not the same as top-50 tradable discretionary trading list**.
It can include:
- stablecoins
- tokenized gold / cash-like assets
- exchange tokens
- unusual institutional / RWA-style entries

If the user wants a cleaner trading watchlist, create a separate preset such as:
- top-50 tradable only
- top-50 altcoins only
- Binance/Bybit majors only
