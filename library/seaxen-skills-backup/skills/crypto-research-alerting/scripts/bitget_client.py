#!/usr/bin/env python3
"""Bitget public data client for Hermes dashboard."""
import argparse
import json
import requests
import sys

BASE_URL = "https://api.bitget.com/api/v2/mix/market"

def get_ticker(symbol):
    symbol = symbol.upper()
    try:
        # Using Mix (Futures) ticker
        res = requests.get(f"{BASE_URL}/ticker?symbol={symbol}")
        data = res.json()
        if data.get('code') == '00000' and data.get('data'):
            ticker = data['data'][0]
            return {
                'price': ticker.get('lastPr'),
                'change_24h': ticker.get('change24h'),
                'funding_rate': ticker.get('fundingRate')
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
