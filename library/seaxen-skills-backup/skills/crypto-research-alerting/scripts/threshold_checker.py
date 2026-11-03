#!/usr/bin/env python3
"""
Check a watchlist against live market thresholds.
Outputs JSON when signals exist. Can stay silent when nothing triggers.
No external dependencies required.

Usage:
  python3 threshold_checker.py --watchlist templates/watchlist.yaml
  python3 threshold_checker.py --watchlist templates/watchlist.yaml --silent-if-none
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from watchlist_parser import parse_watchlist_text  # noqa: E402

HEADERS = {"Accept": "application/json", "User-Agent": "HermesAgent/1.0"}


def http_get_json(url: str, timeout: int = 20, retries: int = 2) -> Any:
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < retries:
                time.sleep(1.5 * (attempt + 1))
                continue
            return None
        except Exception:
            return None


def to_float(x: Any) -> Optional[float]:
    try:
        if x is None or x == '':
            return None
        return float(x)
    except Exception:
        return None


def load_watchlist(path: str) -> List[Dict[str, Any]]:
    with open(path, 'r', encoding='utf-8') as f:
        return parse_watchlist_text(f.read()).get('watchlist', [])


def infer_symbol(entry: Dict[str, Any]) -> str:
    symbol = entry.get('symbol') or entry.get('cex_symbol') or entry.get('ticker') or ''
    symbol = str(symbol).upper().strip()
    if not symbol:
        return ''
    if symbol.endswith('USDT') or symbol.endswith('USD'):
        return symbol
    return symbol + 'USDT'


def fetch_binance(symbol: str) -> Dict[str, Any]:
    q = urllib.parse.urlencode({'symbol': symbol})
    ticker = http_get_json(f'https://api.binance.com/api/v3/ticker/24hr?{q}') or {}
    fut_ticker = http_get_json(f'https://fapi.binance.com/fapi/v1/ticker/24hr?{q}') or {}
    funding = http_get_json(f'https://fapi.binance.com/fapi/v1/fundingRate?symbol={symbol}&limit=2') or []
    oi_hist = http_get_json(f'https://fapi.binance.com/futures/data/openInterestHist?symbol={symbol}&period=5m&limit=2') or []
    out = {
        'venue': 'binance',
        'symbol': symbol,
        'price': to_float(ticker.get('lastPrice')),
        'move_24h_pct': to_float(ticker.get('priceChangePercent')),
        'volume_24h': to_float(ticker.get('quoteVolume')),
        'futures_price': to_float(fut_ticker.get('lastPrice')),
        'funding_rate': to_float(funding[-1].get('fundingRate')) if funding else None,
        'oi_latest': to_float(oi_hist[-1].get('sumOpenInterest')) if oi_hist else None,
        'oi_prev': to_float(oi_hist[-2].get('sumOpenInterest')) if len(oi_hist) >= 2 else None,
    }
    if out['oi_latest'] is not None and out['oi_prev'] not in (None, 0):
        out['oi_change_pct'] = (out['oi_latest'] - out['oi_prev']) / out['oi_prev'] * 100.0
    else:
        out['oi_change_pct'] = None
    return out


def fetch_bybit(symbol: str) -> Dict[str, Any]:
    q = urllib.parse.urlencode({'category': 'linear', 'symbol': symbol})
    ticker_data = http_get_json(f'https://api.bybit.com/v5/market/tickers?{q}') or {}
    items = (((ticker_data.get('result') or {}).get('list')) or [])
    item = items[0] if items else {}
    funding_data = http_get_json(f'https://api.bybit.com/v5/market/funding/history?category=linear&symbol={symbol}&limit=2') or {}
    funding_items = (((funding_data.get('result') or {}).get('list')) or [])
    oi_data = http_get_json(f'https://api.bybit.com/v5/market/open-interest?category=linear&symbol={symbol}&intervalTime=5min&limit=2') or {}
    oi_items = (((oi_data.get('result') or {}).get('list')) or [])
    out = {
        'venue': 'bybit',
        'symbol': symbol,
        'price': to_float(item.get('lastPrice')),
        'move_24h_pct': to_float(item.get('price24hPcnt')) * 100.0 if to_float(item.get('price24hPcnt')) is not None else None,
        'volume_24h': to_float(item.get('turnover24h')),
        'funding_rate': to_float(funding_items[0].get('fundingRate')) if funding_items else None,
        'oi_latest': to_float(oi_items[0].get('openInterest')) if oi_items else None,
        'oi_prev': to_float(oi_items[1].get('openInterest')) if len(oi_items) >= 2 else None,
    }
    if out['oi_latest'] is not None and out['oi_prev'] not in (None, 0):
        out['oi_change_pct'] = (out['oi_latest'] - out['oi_prev']) / out['oi_prev'] * 100.0
    else:
        out['oi_change_pct'] = None
    return out


def fetch_coingecko(entry: Dict[str, Any]) -> Dict[str, Any]:
    coin_id = entry.get('coingecko_id') or str(entry.get('ticker', '')).lower()
    if not coin_id:
        return {'venue': 'coingecko'}
    q = urllib.parse.urlencode({
        'vs_currency': 'usd', 'ids': coin_id,
        'order': 'market_cap_desc', 'per_page': 1, 'page': 1,
        'sparkline': 'false', 'price_change_percentage': '24h,7d,30d'
    })
    data = http_get_json(f'https://api.coingecko.com/api/v3/coins/markets?{q}') or []
    item = data[0] if data else {}
    return {
        'venue': 'coingecko',
        'coin_id': coin_id,
        'price': to_float(item.get('current_price')),
        'move_24h_pct': to_float(item.get('price_change_percentage_24h_in_currency')),
        'volume_24h': to_float(item.get('total_volume')),
        'market_cap': to_float(item.get('market_cap')),
        'fdv': to_float(item.get('fully_diluted_valuation')),
    }


def fetch_dexscreener(entry: Dict[str, Any]) -> Dict[str, Any]:
    pair_address = entry.get('pair_address')
    chain_id = entry.get('chain_id')
    token_address = entry.get('token_address')
    query = entry.get('dex_query') or entry.get('ticker')

    data = None
    if pair_address and chain_id:
        data = http_get_json(f'https://api.dexscreener.com/latest/dex/pairs/{urllib.parse.quote(str(chain_id))}/{urllib.parse.quote(str(pair_address))}') or {}
    elif token_address:
        data = http_get_json(f'https://api.dexscreener.com/latest/dex/tokens/{urllib.parse.quote(str(token_address))}') or {}
    elif query:
        data = http_get_json(f'https://api.dexscreener.com/latest/dex/search?q={urllib.parse.quote(str(query))}') or {}
    pairs = data.get('pairs') or []
    if not pairs:
        return {'venue': 'dexscreener'}
    pairs = sorted(pairs, key=lambda p: ((p.get('liquidity') or {}).get('usd') or 0), reverse=True)
    pair = pairs[0]
    liq = pair.get('liquidity') or {}
    price_change = pair.get('priceChange') or {}
    volume = pair.get('volume') or {}
    return {
        'venue': 'dexscreener',
        'chain_id': pair.get('chainId'),
        'pair_address': pair.get('pairAddress'),
        'price': to_float(pair.get('priceUsd')),
        'move_24h_pct': to_float(price_change.get('h24')),
        'liquidity_usd': to_float(liq.get('usd')),
        'fdv': to_float(pair.get('fdv')),
        'market_cap': to_float(pair.get('marketCap')),
        'volume_24h': to_float(volume.get('h24')),
        'buys_24h': ((pair.get('txns') or {}).get('h24') or {}).get('buys'),
        'sells_24h': ((pair.get('txns') or {}).get('h24') or {}).get('sells'),
        'url': pair.get('url'),
    }


def gather_metrics(entry: Dict[str, Any]) -> Dict[str, Any]:
    venues = [str(v).lower() for v in (entry.get('venues') or [])]
    symbol = infer_symbol(entry)
    metrics: Dict[str, Any] = {'ticker': entry.get('ticker'), 'venues': venues}

    if 'binance' in venues and symbol:
        metrics['binance'] = fetch_binance(symbol)
    if 'bybit' in venues and symbol:
        metrics['bybit'] = fetch_bybit(symbol)
    if 'coingecko' in venues:
        metrics['coingecko'] = fetch_coingecko(entry)
    if 'dexscreener' in venues:
        metrics['dexscreener'] = fetch_dexscreener(entry)
    return metrics


def primary_price(metrics: Dict[str, Any]) -> Optional[float]:
    for key in ('binance', 'bybit', 'coingecko', 'dexscreener'):
        price = to_float((metrics.get(key) or {}).get('price'))
        if price is not None:
            return price
    return None


def primary_move_24h(metrics: Dict[str, Any]) -> Optional[float]:
    for key in ('binance', 'bybit', 'coingecko', 'dexscreener'):
        val = to_float((metrics.get(key) or {}).get('move_24h_pct'))
        if val is not None:
            return val
    return None


def primary_liquidity(metrics: Dict[str, Any]) -> Optional[float]:
    return to_float((metrics.get('dexscreener') or {}).get('liquidity_usd'))


def primary_funding(metrics: Dict[str, Any]) -> Optional[float]:
    for key in ('binance', 'bybit'):
        val = to_float((metrics.get(key) or {}).get('funding_rate'))
        if val is not None:
            return val
    return None


def primary_oi_change(metrics: Dict[str, Any]) -> Optional[float]:
    for key in ('binance', 'bybit'):
        val = to_float((metrics.get(key) or {}).get('oi_change_pct'))
        if val is not None:
            return val
    return None


def check_entry(entry: Dict[str, Any]) -> Dict[str, Any]:
    metrics = gather_metrics(entry)
    signals: List[Dict[str, Any]] = []
    notes: List[str] = []

    price = primary_price(metrics)
    move_24h = primary_move_24h(metrics)
    funding = primary_funding(metrics)
    oi_change = primary_oi_change(metrics)
    liquidity = primary_liquidity(metrics)

    price_above = to_float(entry.get('price_above'))
    if price_above is not None and price is not None and price > price_above:
        signals.append({'rule': 'price_above', 'message': f'price {price:.6g} > {price_above}'})

    price_below = to_float(entry.get('price_below'))
    if price_below is not None and price is not None and price < price_below:
        signals.append({'rule': 'price_below', 'message': f'price {price:.6g} < {price_below}'})

    move_thresh = to_float(entry.get('move_24h_abs_threshold_pct'))
    if move_thresh is not None and move_24h is not None and abs(move_24h) >= move_thresh:
        signals.append({'rule': 'move_24h_abs_threshold_pct', 'message': f'24h move {move_24h:.3f}% exceeds {move_thresh}%'})

    funding_thresh = to_float(entry.get('funding_abs_threshold'))
    if funding_thresh is not None and funding is not None and abs(funding) >= funding_thresh:
        signals.append({'rule': 'funding_abs_threshold', 'message': f'funding {funding:.6f} exceeds {funding_thresh}'})

    oi_div_thresh = to_float(entry.get('oi_divergence_threshold_pct'))
    if oi_div_thresh is not None and oi_change is not None and move_24h is not None:
        if (oi_change * move_24h < 0) and (abs(oi_change - move_24h) >= oi_div_thresh):
            signals.append({'rule': 'oi_divergence_threshold_pct', 'message': f'OI change {oi_change:.3f}% diverges from price move {move_24h:.3f}% by >= {oi_div_thresh}%'})

    liq_floor = to_float(entry.get('liquidity_floor_usd'))
    if liq_floor is not None and liquidity is not None and liquidity < liq_floor:
        signals.append({'rule': 'liquidity_floor_usd', 'message': f'liquidity ${liquidity:,.2f} below floor ${liq_floor:,.2f}'})

    resistance = to_float(entry.get('resistance'))
    if resistance is not None and price is not None and price > resistance:
        signals.append({'rule': 'resistance_break', 'message': f'price {price:.6g} broke resistance {resistance}'})

    support = to_float(entry.get('support'))
    if support is not None and price is not None and price < support:
        signals.append({'rule': 'support_break', 'message': f'price {price:.6g} broke support {support}'})

    for raw_rule in (entry.get('alert_thresholds') or []):
        rule = str(raw_rule).strip()
        m = re.search(r'24h move\s*>\s*(\d+(?:\.\d+)?)%', rule, re.I)
        if m and move_24h is not None:
            thresh = float(m.group(1))
            if abs(move_24h) >= thresh:
                signals.append({'rule': 'freeform_24h_move', 'message': f'24h move {move_24h:.3f}% exceeds {thresh}%'})
            continue
        if re.search(r'funding extreme', rule, re.I):
            if funding is not None and abs(funding) >= 0.01:
                signals.append({'rule': 'freeform_funding_extreme', 'message': f'funding {funding:.6f} is extreme by default 0.01 threshold'})
            continue
        if re.search(r'OI diverges from price', rule, re.I):
            if oi_change is not None and move_24h is not None and oi_change * move_24h < 0 and abs(oi_change - move_24h) >= 5:
                signals.append({'rule': 'freeform_oi_divergence', 'message': f'OI change {oi_change:.3f}% diverges from price move {move_24h:.3f}%'})
            continue
        if re.search(r'Price breaks resistance', rule, re.I) and resistance is not None and price is not None and price > resistance:
            signals.append({'rule': 'freeform_resistance_break', 'message': f'price {price:.6g} broke resistance {resistance}'})
            continue
        if re.search(r'Price breaks support', rule, re.I) and support is not None and price is not None and price < support:
            signals.append({'rule': 'freeform_support_break', 'message': f'price {price:.6g} broke support {support}'})
            continue
        if re.search(r'Liquidity drops below threshold', rule, re.I):
            if liq_floor is None:
                notes.append('Liquidity rule present but liquidity_floor_usd not set')
            continue
        if re.search(r'24h volume spikes', rule, re.I):
            notes.append('24h volume spike rule noted but not evaluated without baseline history')
            continue

    return {
        'ticker': entry.get('ticker'),
        'signals': signals,
        'notes': notes,
        'metrics': metrics,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Check watchlist thresholds against live market data')
    parser.add_argument('--watchlist', required=True)
    parser.add_argument('--silent-if-none', action='store_true')
    args = parser.parse_args()

    watchlist = load_watchlist(args.watchlist)
    checked = [check_entry(entry) for entry in watchlist]
    alerts = [item for item in checked if item['signals']]
    out = {
        'watchlist_path': args.watchlist,
        'alert_count': len(alerts),
        'alerts': alerts,
        'checked': checked,
    }
    if args.silent_if_none and not alerts:
        return
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        sys.exit(str(exc))
