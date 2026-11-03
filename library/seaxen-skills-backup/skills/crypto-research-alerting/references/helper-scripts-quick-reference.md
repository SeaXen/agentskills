# Helper Script Quick Reference

## CoinGecko
```bash
python3 scripts/coingecko_client.py trending
python3 scripts/coingecko_client.py search render
python3 scripts/coingecko_client.py coin solana
python3 scripts/coingecko_client.py category artificial-intelligence
```

## DEXScreener
```bash
python3 scripts/dexscreener_client.py search bonk
python3 scripts/dexscreener_client.py token <token_address>
python3 scripts/dexscreener_client.py pair solana <pair_address>
python3 scripts/dexscreener_client.py boosts --top 10
```

## Binance public
```bash
python3 scripts/binance_public.py price BTCUSDT
python3 scripts/binance_public.py ticker BTCUSDT
python3 scripts/binance_public.py funding BTCUSDT
python3 scripts/binance_public.py oi BTCUSDT
python3 scripts/binance_public.py candles BTCUSDT --interval 4h --limit 20
```

## Bybit public
```bash
python3 scripts/bybit_public.py ticker BTCUSDT
python3 scripts/bybit_public.py funding BTCUSDT
python3 scripts/bybit_public.py oi BTCUSDT --interval 15min --limit 20
python3 scripts/bybit_public.py candles BTCUSDT --interval 60 --limit 24
```

## Risk calculator
```bash
python3 scripts/risk_calc.py size --equity 12000 --risk-pct 0.75 --entry 2.45 --stop 2.31 --target 2.70 --target 2.95
```

## Safety
- Public APIs first
- No trading or withdrawals
- Read-only account keys only if truly needed later
- Cross-check DEX and CEX data before acting
