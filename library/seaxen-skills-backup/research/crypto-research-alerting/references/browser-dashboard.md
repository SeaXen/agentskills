# Browser Dashboard

## What it is
A local browser UI for the `crypto-research-alerting` skill.

It shows:
- CoinGecko overview
- DEXScreener top pairs
- Binance / Bybit market context
- risk sizing
- alert summary
- raw JSON for debugging

## Start it
```bash
python3 /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/browser_dashboard_server.py
```

Custom port:
```bash
python3 /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/browser_dashboard_server.py --port 8787
```

Custom watchlist:
```bash
python3 /mnt/tb/hermes/skills/research/crypto-research-alerting/scripts/browser_dashboard_server.py \
  --watchlist /path/to/watchlist.yaml
```

## Open in browser
- Default URL: `http://127.0.0.1:8765`

## API endpoints
- `/api/health`
- `/api/watchlist`
- `/api/alerts`
- `/api/dashboard`

## Notes
- This is a local browser dashboard, not a remote hosted service.
- It stays read-only.
- The server is a thin bridge that calls the skill's existing Python helper scripts.
- For best DEX results, use a specific `dex_query`, `token_address`, or `pair_address` in the watchlist.
