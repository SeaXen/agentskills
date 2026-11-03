#!/usr/bin/env python3
"""MEXC public data client for Hermes dashboard."""
import argparse
import json
import requests
import sys

BASE_URL = "https://www.mexc.com/open/api/v2/market"

def get_ticker(symbol):
    symbol = symbol.upper()
    try:
        res = requests.get(f"{BASE_URL}/ticker?symbol={symbol}")
        data = res.json()
        if data.get('code') == 200 and data.get('data'):
            ticker = data['data'][0]
            return {
                'price': ticker.get('last'),
                'change_24h': ticker.get('change_rate'),
                'volume_24h': ticker.get('amount')
            }
    except:
        pass
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('symbol')
    args = parser.parse_args()
    print(json.dumps(get_ticker(args.symbol)))

if __name__ == "__main__":
    main()
