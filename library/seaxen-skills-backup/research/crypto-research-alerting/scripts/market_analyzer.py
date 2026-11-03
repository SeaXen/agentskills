#!/usr/bin/env python3
"""Score crypto setups and rank a watchlist for the dashboard."""

import argparse
import json
import os
import sys
from typing import Any, Dict, List, Optional

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from threshold_checker import (  # noqa: E402
    gather_metrics,
    load_watchlist,
    primary_funding,
    primary_liquidity,
    primary_move_24h,
    primary_oi_change,
    primary_price,
    to_float,
)


def clamp(n: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, n))


def infer_stance(score: float, risk_score: float) -> str:
    if score >= 72 and risk_score <= 48:
        return 'bullish'
    if score <= 38:
        return 'bearish'
    if risk_score >= 72:
        return 'high-risk'
    return 'neutral'


def score_entry(entry: Dict[str, Any]) -> Dict[str, Any]:
    metrics = gather_metrics(entry)
    price = primary_price(metrics)
    move_24h = primary_move_24h(metrics)
    funding = primary_funding(metrics)
    oi_change = primary_oi_change(metrics)
    liquidity = primary_liquidity(metrics)
    cg = metrics.get('coingecko') or {}
    dex = metrics.get('dexscreener') or {}

    chg7 = to_float(((cg.get('price_change_pct') or {}) if isinstance(cg.get('price_change_pct'), dict) else {}).get('7d'))
    chg30 = to_float(((cg.get('price_change_pct') or {}) if isinstance(cg.get('price_change_pct'), dict) else {}).get('30d'))
    if chg7 is None:
        chg7 = to_float((cg.get('price_change_pct') or {}).get('7d')) if isinstance(cg.get('price_change_pct'), dict) else None
    if chg30 is None:
        chg30 = to_float((cg.get('price_change_pct') or {}).get('30d')) if isinstance(cg.get('price_change_pct'), dict) else None
    market_cap = to_float(cg.get('market_cap')) or to_float(dex.get('market_cap'))
    fdv = to_float(cg.get('fdv')) or to_float(dex.get('fdv'))
    volume = to_float(cg.get('volume_24h')) or to_float(dex.get('volume_24h'))

    momentum = 50.0
    if move_24h is not None:
        momentum += clamp(move_24h * 2.2, -18, 18)
    if chg7 is not None:
        momentum += clamp(chg7 * 0.9, -16, 16)
    if chg30 is not None:
        momentum += clamp(chg30 * 0.35, -10, 10)
    momentum = clamp(momentum, 0, 100)

    liquidity_score = 25.0
    if liquidity is not None:
        if liquidity >= 50_000_000:
            liquidity_score = 95
        elif liquidity >= 10_000_000:
            liquidity_score = 85
        elif liquidity >= 3_000_000:
            liquidity_score = 72
        elif liquidity >= 1_000_000:
            liquidity_score = 60
        elif liquidity >= 250_000:
            liquidity_score = 45
        else:
            liquidity_score = 25
    elif market_cap is not None:
        if market_cap >= 10_000_000_000:
            liquidity_score = 88
        elif market_cap >= 1_000_000_000:
            liquidity_score = 72
        elif market_cap >= 250_000_000:
            liquidity_score = 58
        else:
            liquidity_score = 35

    crowding = 15.0
    if funding is not None:
        crowding += clamp(abs(funding) * 5000, 0, 40)
    if oi_change is not None:
        crowding += clamp(abs(oi_change) * 1.7, 0, 35)
        if move_24h is not None and oi_change * move_24h < 0:
            crowding += 18
    crowding = clamp(crowding, 0, 100)

    valuation_risk = 18.0
    if fdv and market_cap and market_cap > 0:
        ratio = fdv / market_cap
        if ratio >= 4:
            valuation_risk = 80
        elif ratio >= 2.5:
            valuation_risk = 62
        elif ratio >= 1.5:
            valuation_risk = 42
        else:
            valuation_risk = 22

    volume_quality = 45.0
    if volume and market_cap and market_cap > 0:
        vm = volume / market_cap
        if vm >= 0.25:
            volume_quality = 88
        elif vm >= 0.12:
            volume_quality = 74
        elif vm >= 0.05:
            volume_quality = 60
        else:
            volume_quality = 38

    setup_score = clamp(momentum * 0.38 + liquidity_score * 0.24 + volume_quality * 0.18 + (100 - crowding) * 0.12 + (100 - valuation_risk) * 0.08, 0, 100)
    risk_score = clamp(crowding * 0.45 + valuation_risk * 0.25 + (100 - liquidity_score) * 0.2 + max(0.0, 30 - (move_24h or 0)) * 0.1, 0, 100)
    stance = infer_stance(setup_score, risk_score)

    reasons: List[str] = []
    risks: List[str] = []
    if move_24h is not None:
        reasons.append(f'24h move {move_24h:.2f}%')
    if chg7 is not None:
        reasons.append(f'7d move {chg7:.2f}%')
    if liquidity is not None:
        reasons.append(f'DEX liquidity ${liquidity:,.0f}')
    elif market_cap is not None:
        reasons.append(f'market cap ${market_cap:,.0f}')
    if funding is not None and abs(funding) >= 0.01:
        risks.append(f'funding crowded at {funding:.5f}')
    if oi_change is not None and move_24h is not None and oi_change * move_24h < 0:
        risks.append(f'OI diverges from price ({oi_change:.2f}% vs {move_24h:.2f}%)')
    if fdv and market_cap and market_cap > 0 and fdv / market_cap >= 2:
        risks.append(f'FDV/market cap ratio {(fdv / market_cap):.2f}x')
    if liquidity is not None and liquidity < 1_000_000:
        risks.append('thin DEX liquidity')
    if not risks:
        risks.append('no major crowding flag detected')

    return {
        'ticker': entry.get('ticker') or entry.get('symbol'),
        'symbol': entry.get('symbol'),
        'coingecko_id': entry.get('coingecko_id'),
        'stance': stance,
        'setup_score': round(setup_score, 1),
        'risk_score': round(risk_score, 1),
        'momentum_score': round(momentum, 1),
        'liquidity_score': round(liquidity_score, 1),
        'volume_quality_score': round(volume_quality, 1),
        'price': price,
        'move_24h_pct': move_24h,
        'funding_rate': funding,
        'oi_change_pct': oi_change,
        'liquidity_usd': liquidity,
        'market_cap_usd': market_cap,
        'fdv_usd': fdv,
        'reasons': reasons[:4],
        'risks': risks[:4],
        'metrics': metrics,
    }


def build_watchlist_scan(entries: List[Dict[str, Any]]) -> Dict[str, Any]:
    scored = [score_entry(entry) for entry in entries]
    opportunities = sorted(scored, key=lambda x: (x['setup_score'], -x['risk_score']), reverse=True)[:8]
    danger = sorted(scored, key=lambda x: (x['risk_score'], -x['setup_score']), reverse=True)[:8]
    avg_setup = round(sum(x['setup_score'] for x in scored) / len(scored), 1) if scored else 0.0
    avg_risk = round(sum(x['risk_score'] for x in scored) / len(scored), 1) if scored else 0.0
    breadth = {
        'bullish': sum(1 for x in scored if x['stance'] == 'bullish'),
        'neutral': sum(1 for x in scored if x['stance'] == 'neutral'),
        'bearish': sum(1 for x in scored if x['stance'] == 'bearish'),
        'high_risk': sum(1 for x in scored if x['stance'] == 'high-risk'),
    }
    market_regime = 'mixed'
    if breadth['bullish'] >= max(3, breadth['bearish'] + breadth['high_risk']):
        market_regime = 'risk-on'
    elif breadth['high_risk'] + breadth['bearish'] > breadth['bullish'] + breadth['neutral']:
        market_regime = 'defensive'
    return {
        'count': len(scored),
        'average_setup_score': avg_setup,
        'average_risk_score': avg_risk,
        'market_regime': market_regime,
        'breadth': breadth,
        'top_opportunities': opportunities,
        'top_risks': danger,
        'all': scored,
    }


def build_single_entry(args: argparse.Namespace) -> Dict[str, Any]:
    ticker = args.symbol.replace('USDT', '').replace('USD', '') if args.symbol else (args.coin_id or 'coin').upper()
    entry = {
        'ticker': ticker,
        'symbol': args.symbol,
        'coingecko_id': args.coin_id,
        'dex_query': args.dex_query or ticker.lower(),
        'venues': ['binance', 'bybit', 'coingecko', 'dexscreener'],
    }
    return score_entry(entry)


def main() -> None:
    parser = argparse.ArgumentParser(description='Analyze crypto setups and scan a watchlist')
    parser.add_argument('--watchlist')
    parser.add_argument('--symbol')
    parser.add_argument('--coin-id')
    parser.add_argument('--dex-query')
    args = parser.parse_args()

    if args.watchlist:
        entries = load_watchlist(args.watchlist)
        print(json.dumps(build_watchlist_scan(entries), indent=2))
        return
    if args.symbol or args.coin_id:
        print(json.dumps(build_single_entry(args), indent=2))
        return
    raise SystemExit('Provide --watchlist or --symbol/--coin-id')


if __name__ == '__main__':
    main()
