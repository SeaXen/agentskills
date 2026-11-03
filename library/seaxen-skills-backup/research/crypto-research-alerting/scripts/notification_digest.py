#!/usr/bin/env python3
"""Generate Telegram-ready price notification text without any model/API token."""

import argparse
import json
import time
from pathlib import Path

from threshold_checker import gather_metrics, primary_price  # noqa: E402

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
RULES_PATH = SKILL_DIR / 'notification_rules.json'
SAMPLE_PATH = SKILL_DIR / 'templates' / 'notification-rules.sample.json'


def load_rules() -> dict:
    if not RULES_PATH.exists() and SAMPLE_PATH.exists():
        RULES_PATH.write_text(SAMPLE_PATH.read_text(encoding='utf-8'), encoding='utf-8')
    try:
        data = json.loads(RULES_PATH.read_text(encoding='utf-8'))
    except Exception:
        data = {'rules': []}
    if not isinstance(data, dict):
        data = {'rules': []}
    data.setdefault('rules', [])
    return data


def save_rules(data: dict) -> None:
    RULES_PATH.write_text(json.dumps(data, indent=2), encoding='utf-8')


def current_price(symbol: str, coin_id: str) -> float | None:
    ticker = symbol.replace('USDT', '').replace('USD', '')
    entry = {
        'ticker': ticker,
        'symbol': symbol,
        'coingecko_id': coin_id or ticker.lower(),
        'dex_query': ticker.lower(),
        'venues': ['binance', 'bybit', 'coingecko', 'dexscreener'],
    }
    return primary_price(gather_metrics(entry))


def evaluate(data: dict) -> dict:
    now = int(time.time())
    matches = []
    dirty = False
    for rule in data.get('rules', []):
        if not isinstance(rule, dict) or not rule.get('enabled', True):
            continue
        symbol = str(rule.get('symbol', '')).strip().upper()
        if not symbol:
            continue
        coin_id = str(rule.get('coin_id', '')).strip()
        price = current_price(symbol, coin_id)
        threshold = rule.get('value')
        try:
            threshold = float(threshold)
        except Exception:
            continue
        if price is None:
            continue
        cond = str(rule.get('condition', '')).strip()
        hit = (cond == 'price_above' and price > threshold) or (cond == 'price_below' and price < threshold)
        if not hit:
            continue
        cooldown = int(rule.get('cooldown_minutes', 30) or 30) * 60
        last_fired = int(rule.get('last_fired_at') or 0)
        if last_fired and now - last_fired < cooldown:
            continue
        rule['last_fired_at'] = now
        dirty = True
        matches.append({
            'name': rule.get('name') or f'{symbol} {cond} {threshold}',
            'symbol': symbol,
            'price': price,
            'condition': cond,
            'threshold': threshold,
            'notes': rule.get('notes') or '',
            'triggered_at': now,
        })
    if dirty:
        save_rules(data)
    return {'match_count': len(matches), 'matches': matches}


def format_text(payload: dict) -> str:
    if not payload.get('match_count'):
        return ''
    lines = ['## Price alerts triggered']
    for item in payload.get('matches', []):
        lines.append(f"- {item['symbol']}: {item['name']} | price {item['price']:.6g} | rule {item['condition']} {item['threshold']}")
        if item.get('notes'):
            lines.append(f"  note: {item['notes']}")
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate notification digest for cron or manual sending')
    parser.add_argument('--text', action='store_true')
    parser.add_argument('--silent-if-none', action='store_true')
    args = parser.parse_args()
    payload = evaluate(load_rules())
    if args.text:
        text = format_text(payload)
        if text or not args.silent_if_none:
            print(text)
    else:
        if payload.get('match_count') or not args.silent_if_none:
            print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
