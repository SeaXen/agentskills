#!/usr/bin/env python3
"""Hyperliquid data client for Hermes dashboard."""
import argparse
import json
import requests
import sys

BASE_URL = "https://api.hyperliquid.xyz/info"

def get_meta():
    payload = {"type": "meta"}
    res = requests.post(BASE_URL, json=payload)
    return res.json()

def get_mid_price(coin):
    res = requests.post(BASE_URL, json={"type": "allMids"})
    mids = res.json()
    return mids.get(coin)

def get_funding(coin):
    res = requests.post(BASE_URL, json={"type": "metaAndAssetCtxs"})
    data = res.json()
    meta = data[0]
    ctxs = data[1]
    
    universe = meta.get('universe', [])
    asset_index = next((i for i, asset in enumerate(universe) if asset['name'] == coin), None)
    if asset_index is not None:
        ctx = ctxs[asset_index]
        return {
            'funding': ctx.get('funding'),
            'open_interest': ctx.get('openInterest'),
            'day_volume': ctx.get('dayNtlVlm')
        }
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['price', 'funding', 'full'])
    parser.add_argument('--coin', default='BTC')
    args = parser.parse_args()
    
    coin = args.coin.replace('USDT', '').upper()
    
    if args.action == 'price':
        print(json.dumps({"price": get_mid_price(coin)}))
    elif args.action == 'funding':
        print(json.dumps(get_funding(coin)))
    elif args.action == 'full':
        print(json.dumps({
            "ticker": {"price": get_mid_price(coin)},
            "funding": get_funding(coin)
        }))

if __name__ == "__main__":
    main()
