# Alert Workflow Quick Reference

## Files
- `scripts/watchlist_parser.py` — parse watchlist YAML-like template into JSON
- `scripts/threshold_checker.py` — evaluate live thresholds and optionally stay silent
- `scripts/pro_dashboard.py` — one-command dashboard combining market context, risk, and alerts

## Watchlist parser
```bash
python3 scripts/watchlist_parser.py templates/watchlist.yaml
```

## Threshold checker
Normal output:
```bash
python3 scripts/threshold_checker.py --watchlist templates/watchlist.yaml
```

Silent if nothing triggered:
```bash
python3 scripts/threshold_checker.py --watchlist templates/watchlist.yaml --silent-if-none
```

## Pro dashboard
```bash
python3 scripts/pro_dashboard.py \
  --symbol BTCUSDT \
  --coin-id bitcoin \
  --dex-query btc \
  --watchlist templates/watchlist.yaml \
  --equity 12000 \
  --risk-pct 0.75 \
  --entry 2450 \
  --stop 2310 \
  --target 2700 \
  --target 2950
```

## Recommended structured watchlist fields
- `symbol`: CEX symbol like `BTCUSDT`
- `coingecko_id`: stable CoinGecko coin id like `bitcoin`
- `dex_query`: DEXScreener search term
- `token_address`: token address if known
- `chain_id`: chain for direct pair lookup
- `pair_address`: direct DEX pair address
- `price_above`, `price_below`
- `move_24h_abs_threshold_pct`
- `funding_abs_threshold`
- `oi_divergence_threshold_pct`
- `liquidity_floor_usd`

## Silent mode behavior
Use `--silent-if-none` for cron/watcher jobs when you want no message at all unless a signal triggers.
