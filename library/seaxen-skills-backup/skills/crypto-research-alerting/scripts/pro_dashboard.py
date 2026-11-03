#!/usr/bin/env python3
"""Pro dashboard workflow for Hermes with Hedge Mode support."""
import argparse
import json
import os
import subprocess
import sys
import time
from typing import Any, Dict, List, Optional

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable

def run_json(script_name: str, args: List[str]) -> Optional[Any]:
    path = os.path.join(SCRIPT_DIR, script_name)
    proc = subprocess.run([PY, path] + args, capture_output=True, text=True)
    if proc.returncode != 0:
        return {'error': proc.stderr.strip() or proc.stdout.strip(), 'script': script_name}
    text = proc.stdout.strip()
    return json.loads(text) if text else None

def summarize_alerts(alerts: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not alerts: return {'summary': 'No alert output', 'high': 0, 'medium': 0, 'low': 0}
    if alerts.get('alert_count', 0) == 0: return {'summary': 'No signals triggered', 'high': 0, 'medium': 0, 'low': 0}
    summary = []
    severity_counts = {'high': 0, 'medium': 0, 'low': 0}
    for item in alerts.get('alerts', []):
        lines = [sig.get('message') for sig in item.get('signals', [])]
        sev = 'low'
        for sig in item.get('signals', []):
            rule = str(sig.get('rule', '')).lower()
            msg = str(sig.get('message', '')).lower()
            if any(k in f'{rule} {msg}' for k in ('support_break', 'liquidity', 'funding', 'divergence', 'price_below')):
                sev = 'high'; break
            if any(k in f'{rule} {msg}' for k in ('resistance', 'move_24h', 'price_above')):
                sev = 'medium'
        severity_counts[sev] += 1
        summary.append({'ticker': item.get('ticker'), 'messages': lines, 'severity': sev})
    return {'summary': f"{severity_counts['high']} high-priority alert(s)" if severity_counts['high'] else 'Signals triggered', 'items': summary, **severity_counts}

def build_summary(data: Dict[str, Any]) -> Dict[str, Any]:
    symbol = data.get('symbol')
    cg = data.get('coingecko') or {}
    dex = data.get('dexscreener') or {}
    binance = data.get('binance') or {}
    bybit = data.get('bybit') or {}
    risk = data.get('risk') or {}
    alert_summary = data.get('alert_summary') or {}
    binance_ticker = (binance.get('ticker') or {}) if isinstance(binance, dict) else {}
    binance_funding = (binance.get('funding') or {}) if isinstance(binance, dict) else {}
    bybit_ticker = (bybit.get('ticker') or {}) if isinstance(bybit, dict) else {}
    bybit_funding = (bybit.get('funding') or {}) if isinstance(bybit, dict) else {}
    dex_top_pair = (((dex.get('pairs') or [None])[0]) or {}) if isinstance(dex, dict) else {}
    return {
        'symbol': symbol,
        'market_snapshot': {
            'coingecko_price_usd': cg.get('current_price_usd'),
            'coingecko_market_cap_usd': cg.get('market_cap_usd'),
            'dex_top_pair_liquidity_usd': dex_top_pair.get('liquidity_usd'),
            'binance_24h_pct': ((binance_ticker.get('spot') or {}).get('price_change_pct')),
            'bybit_24h_pct': bybit_ticker.get('price_change_24h_pct'),
            'binance_funding': ((binance_funding.get('funding') or [{}])[-1].get('funding_rate')) if binance_funding.get('funding') else None,
            'bybit_funding': ((bybit_funding.get('funding') or [{}])[0].get('funding_rate')) if bybit_funding.get('funding') else None,
            'mexc_price': (data.get('mexc') or {}).get('price'),
            'bitget_price': (data.get('bitget') or {}).get('price'),
            'hl_price': ((data.get('hyperliquid') or {}).get('ticker') or {}).get('price'),
            'hl_funding': ((data.get('hyperliquid') or {}).get('funding') or {}).get('funding'),
        },
        'risk_defined': 'mode' in risk or 'position_units' in risk,
        'alert_summary': alert_summary.get('summary'),
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', default='BTCUSDT')
    parser.add_argument('--coin-id')
    parser.add_argument('--dex-query')
    parser.add_argument('--watchlist')
    parser.add_argument('--equity', type=float)
    parser.add_argument('--risk-pct', type=float)
    parser.add_argument('--risk-amount', type=float)
    parser.add_argument('--entry', type=float)
    parser.add_argument('--stop', type=float)
    parser.add_argument('--target', type=float, action='append')
    parser.add_argument('--mode', default='one-way')
    parser.add_argument('--short-entry', type=float)
    parser.add_argument('--short-stop', type=float)
    parser.add_argument('--short-target', type=float, action='append')
    args = parser.parse_args()
    symbol = args.symbol.upper()
    coin_id = args.coin_id or symbol.replace('USDT', '').lower()
    dex_query = args.dex_query or symbol.replace('USDT', '')
    out = {'generated_at': int(time.time()), 'symbol': symbol}
    out['coingecko'] = run_json('coingecko_client.py', ['coin', coin_id])
    out['dexscreener'] = run_json('dexscreener_client.py', ['search', dex_query])
    out['binance'] = {
        'ticker': run_json('binance_public.py', ['ticker', symbol]),
        'funding': run_json('binance_public.py', ['funding', symbol]),
        'oi': run_json('binance_public.py', ['oi', symbol]),
        'candles': run_json('binance_public.py', ['candles', symbol, '--interval', '1h', '--limit', '24']),
    }
    out['bybit'] = {
        'ticker': run_json('bybit_public.py', ['ticker', symbol]),
        'funding': run_json('bybit_public.py', ['funding', symbol]),
        'oi': run_json('bybit_public.py', ['oi', symbol, '--interval', '5min', '--limit', '10']),
        'candles': run_json('bybit_public.py', ['candles', symbol, '--interval', '60', '--limit', '24']),
    }
    out['mexc'] = run_json('mexc_client.py', [symbol])
    out['bitget'] = run_json('bitget_client.py', [symbol])
    out['hyperliquid'] = run_json('hyperliquid_client.py', ['full', '--coin', symbol])
    if args.equity is not None:
        risk_args = ['size', '--equity', str(args.equity), '--mode', args.mode]
        if args.risk_pct: risk_args += ['--risk-pct', str(args.risk_pct)]
        if args.risk_amount: risk_args += ['--risk-amount', str(args.risk_amount)]
        if args.entry and args.stop:
            risk_args += ['--entry', str(args.entry), '--stop', str(args.stop)]
            for t in args.target or []: risk_args += ['--target', str(t)]
        if args.mode == 'hedge' and args.short_entry and args.short_stop:
            risk_args += ['--short-entry', str(args.short_entry), '--short-stop', str(args.short_stop)]
            for t in args.short_target or []: risk_args += ['--short-target', str(t)]
        out['risk'] = run_json('risk_calc.py', risk_args)
    if args.watchlist:
        alerts = run_json('threshold_checker.py', ['--watchlist', args.watchlist])
        out['alerts'] = alerts
        out['alert_summary'] = summarize_alerts(alerts)
    out['summary'] = build_summary(out)
    print(json.dumps(out, indent=2))

if __name__ == '__main__':
    main()
