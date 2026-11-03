#!/usr/bin/env python3
"""
Bybit public market-data helper for Hermes crypto research workflows.
Uses public endpoints only. No API key required.

Usage:
  python3 bybit_public.py ticker BTCUSDT
  python3 bybit_public.py book BTCUSDT [--limit 10]
  python3 bybit_public.py candles BTCUSDT --interval 60 [--limit 24]
  python3 bybit_public.py funding BTCUSDT
  python3 bybit_public.py oi BTCUSDT --interval 5min [--limit 10]
  python3 bybit_public.py instruments [--symbol BTCUSDT]
"""

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from typing import Any, Dict, List

BASE = "https://api.bybit.com/v5/market"
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
            raise


def print_json(obj: Any) -> None:
    print(json.dumps(obj, indent=2))


def to_float(x: Any) -> Any:
    try:
        return float(x)
    except Exception:
        return x


def ensure_ok(data: Dict[str, Any]) -> Dict[str, Any]:
    if data.get("retCode") not in (0, "0", None):
        raise RuntimeError(f"Bybit error: {data.get('retMsg')}")
    return data


def cmd_ticker(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"category": "linear", "symbol": symbol})
    data = ensure_ok(http_get_json(f"{BASE}/tickers?{q}"))
    items = data.get("result", {}).get("list", [])
    if not items:
        raise RuntimeError("No ticker data returned")
    item = items[0]
    print_json({
        "symbol": symbol,
        "last_price": to_float(item.get("lastPrice")),
        "index_price": to_float(item.get("indexPrice")),
        "mark_price": to_float(item.get("markPrice")),
        "funding_rate": to_float(item.get("fundingRate")),
        "open_interest": to_float(item.get("openInterest")),
        "open_interest_value": to_float(item.get("openInterestValue")),
        "turnover_24h": to_float(item.get("turnover24h")),
        "volume_24h": to_float(item.get("volume24h")),
        "price_change_24h_pct": to_float(item.get("price24hPcnt")),
        "high_24h": to_float(item.get("highPrice24h")),
        "low_24h": to_float(item.get("lowPrice24h")),
    })


def cmd_book(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"category": "linear", "symbol": symbol, "limit": args.limit})
    data = ensure_ok(http_get_json(f"{BASE}/orderbook?{q}"))
    result = data.get("result", {})
    print_json({
        "symbol": symbol,
        "timestamp": result.get("ts"),
        "bids": [[to_float(p), to_float(q)] for p, q in (result.get("b") or [])],
        "asks": [[to_float(p), to_float(q)] for p, q in (result.get("a") or [])],
    })


def cmd_candles(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"category": "linear", "symbol": symbol, "interval": args.interval, "limit": args.limit})
    data = ensure_ok(http_get_json(f"{BASE}/kline?{q}"))
    rows: List[Dict[str, Any]] = []
    for k in data.get("result", {}).get("list", []):
        rows.append({
            "start_time": int(k[0]),
            "open": to_float(k[1]),
            "high": to_float(k[2]),
            "low": to_float(k[3]),
            "close": to_float(k[4]),
            "volume": to_float(k[5]),
            "turnover": to_float(k[6]),
        })
    print_json({"symbol": symbol, "interval": args.interval, "candles": rows})


def cmd_funding(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"category": "linear", "symbol": symbol, "limit": 10})
    data = ensure_ok(http_get_json(f"{BASE}/funding/history?{q}"))
    rows = []
    for item in data.get("result", {}).get("list", []):
        rows.append({
            "symbol": item.get("symbol"),
            "funding_rate": to_float(item.get("fundingRate")),
            "funding_rate_timestamp": item.get("fundingRateTimestamp"),
        })
    print_json({"symbol": symbol, "funding": rows})


def cmd_oi(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"category": "linear", "symbol": symbol, "intervalTime": args.interval, "limit": args.limit})
    data = ensure_ok(http_get_json(f"{BASE}/open-interest?{q}"))
    rows = []
    for item in data.get("result", {}).get("list", []):
        rows.append({
            "symbol": item.get("symbol"),
            "open_interest": to_float(item.get("openInterest")),
            "timestamp": item.get("timestamp"),
        })
    print_json({"symbol": symbol, "interval": args.interval, "open_interest": rows})


def cmd_instruments(args):
    params = {"category": "linear"}
    if args.symbol:
        params["symbol"] = args.symbol.upper()
    q = urllib.parse.urlencode(params)
    data = ensure_ok(http_get_json(f"{BASE}/instruments-info?{q}"))
    rows = []
    for item in data.get("result", {}).get("list", []):
        rows.append({
            "symbol": item.get("symbol"),
            "status": item.get("status"),
            "base_coin": item.get("baseCoin"),
            "quote_coin": item.get("quoteCoin"),
            "launch_time": item.get("launchTime"),
            "funding_interval": item.get("fundingInterval"),
            "price_filter": item.get("priceFilter"),
            "lot_size_filter": item.get("lotSizeFilter"),
        })
    print_json({"rows": rows})


def main() -> None:
    parser = argparse.ArgumentParser(description="Bybit public helper for Hermes")
    sub = parser.add_subparsers(dest="command", required=True)

    p_ticker = sub.add_parser("ticker")
    p_ticker.add_argument("symbol")

    p_book = sub.add_parser("book")
    p_book.add_argument("symbol")
    p_book.add_argument("--limit", type=int, default=10)

    p_candles = sub.add_parser("candles")
    p_candles.add_argument("symbol")
    p_candles.add_argument("--interval", required=True)
    p_candles.add_argument("--limit", type=int, default=24)

    p_funding = sub.add_parser("funding")
    p_funding.add_argument("symbol")

    p_oi = sub.add_parser("oi")
    p_oi.add_argument("symbol")
    p_oi.add_argument("--interval", default="5min")
    p_oi.add_argument("--limit", type=int, default=10)

    p_inst = sub.add_parser("instruments")
    p_inst.add_argument("--symbol")

    args = parser.parse_args()
    {
        "ticker": cmd_ticker,
        "book": cmd_book,
        "candles": cmd_candles,
        "funding": cmd_funding,
        "oi": cmd_oi,
        "instruments": cmd_instruments,
    }[args.command](args)


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as exc:
        sys.exit(f"HTTP error: {exc.code} {exc.reason}")
    except Exception as exc:
        sys.exit(str(exc))
