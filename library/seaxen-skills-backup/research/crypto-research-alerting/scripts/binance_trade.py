#!/usr/bin/env python3
"""Execute trades on Binance Futures."""
import os
import sys
import json
import argparse
import hashlib
import hmac
import time
import requests
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env'))
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = "https://fapi.binance.com"

def get_signature(params):
    query_string = "&".join([f"{k}={v}" for k, v in params.items()])
    return hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def execute_order(params):
    params['timestamp'] = int(time.time() * 1000)
    params['signature'] = get_signature(params)
    headers = {'X-MBX-APIKEY': API_KEY}
    res = requests.post(f"{BASE_URL}/fapi/v1/order", params=params, headers=headers)
    return res.json()

def get_positions():
    params = {'timestamp': int(time.time() * 1000)}
    params['signature'] = get_signature(params)
    headers = {'X-MBX-APIKEY': API_KEY}
    res = requests.get(f"{BASE_URL}/fapi/v2/positionRisk", params=params, headers=headers)
    data = res.json()
    if isinstance(data, list):
        return [p for p in data if abs(float(p.get('positionAmt', 0))) > 0]
    return []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", nargs="?", default="trade")
    parser.add_argument("--symbol")
    parser.add_argument("--side", choices=["BUY", "SELL"])
    parser.add_argument("--type", default="MARKET")
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--positionSide", default="BOTH", choices=["BOTH", "LONG", "SHORT"])
    parser.add_argument("--price", type=float)
    args = parser.parse_args()

    if args.action == "positions":
        print(json.dumps(get_positions()))
        return

    params = {
        "symbol": args.symbol.upper(),
        "side": args.side,
        "type": args.type,
        "quantity": args.quantity,
        "positionSide": args.positionSide
    }
    if args.price:
        params["price"] = args.price
        params["timeInForce"] = "GTC"
        
    print(json.dumps(execute_order(params)))

if __name__ == "__main__":
    main()
