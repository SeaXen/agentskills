#!/usr/bin/env python3
"""
Binance public market-data helper for Hermes crypto research workflows.
Uses public endpoints only. No API key required.

Usage:
  python3 binance_public.py price BTCUSDT
  python3 binance_public.py book BTCUSDT [--limit 10]
  python3 binance_public.py candles BTCUSDT --interval 1h [--limit 24]
  python3 binance_public.py funding BTCUSDT
  python3 binance_public.py oi BTCUSDT
  python3 binance_public.py ticker BTCUSDT
"""

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from typing import Any, Dict, List

SPOT = "https://api.binance.com/api/v3"
FUT = "https://fapi.binance.com/fapi/v1"
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


def cmd_price(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"symbol": symbol})
    data = http_get_json(f"{SPOT}/ticker/price?{q}")
    print_json({"symbol": symbol, "price": to_float(data.get("price"))})


def cmd_book(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"symbol": symbol, "limit": args.limit})
    data = http_get_json(f"{SPOT}/depth?{q}")
    out = {
        "symbol": symbol,
        "last_update_id": data.get("lastUpdateId"),
        "bids": [[to_float(p), to_float(q)] for p, q in (data.get("bids") or [])],
        "asks": [[to_float(p), to_float(q)] for p, q in (data.get("asks") or [])],
    }
    print_json(out)


def cmd_candles(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"symbol": symbol, "interval": args.interval, "limit": args.limit})
    data = http_get_json(f"{SPOT}/klines?{q}")
    rows: List[Dict[str, Any]] = []
    for k in data:
        rows.append({
            "open_time": k[0],
            "open": to_float(k[1]),
            "high": to_float(k[2]),
            "low": to_float(k[3]),
            "close": to_float(k[4]),
            "volume": to_float(k[5]),
            "close_time": k[6],
            "quote_volume": to_float(k[7]),
            "trade_count": k[8],
        })
    print_json({"symbol": symbol, "interval": args.interval, "candles": rows})


def cmd_funding(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"symbol": symbol, "limit": 10})
    data = http_get_json(f"{FUT}/fundingRate?{q}")
    rows = []
    for item in data:
        rows.append({
            "symbol": item.get("symbol"),
            "funding_rate": to_float(item.get("fundingRate")),
            "funding_time": item.get("fundingTime"),
            "mark_price": to_float(item.get("markPrice")),
        })
    print_json({"symbol": symbol, "funding": rows})


def cmd_oi(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"symbol": symbol})
    data = http_get_json(f"{FUT}/openInterest?{q}")
    print_json({
        "symbol": symbol,
        "open_interest": to_float(data.get("openInterest")),
        "time": data.get("time"),
    })


def cmd_ticker(args):
    symbol = args.symbol.upper()
    q = urllib.parse.urlencode({"symbol": symbol})
    spot = http_get_json(f"{SPOT}/ticker/24hr?{q}")
    fut = http_get_json(f"{FUT}/ticker/24hr?{q}")
    out = {
        "symbol": symbol,
        "spot": {
            "last_price": to_float(spot.get("lastPrice")),
            "price_change_pct": to_float(spot.get("priceChangePercent")),
            "volume": to_float(spot.get("volume")),
            "quote_volume": to_float(spot.get("quoteVolume")),
            "high": to_float(spot.get("highPrice")),
            "low": to_float(spot.get("lowPrice")),
        },
        "futures": {
            "last_price": to_float(fut.get("lastPrice")),
            "price_change_pct": to_float(fut.get("priceChangePercent")),
            "volume": to_float(fut.get("volume")),
            "quote_volume": to_float(fut.get("quoteVolume")),
            "high": to_float(fut.get("highPrice")),
            "low": to_float(fut.get("lowPrice")),
        },
    }
    print_json(out)


def main() -> None:
    parser = argparse.ArgumentParser(description="Binance public helper for Hermes")
    sub = parser.add_subparsers(dest="command", required=True)

    p_price = sub.add_parser("price")
    p_price.add_argument("symbol")

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

    p_ticker = sub.add_parser("ticker")
    p_ticker.add_argument("symbol")

    args = parser.parse_args()
    {
        "price": cmd_price,
        "book": cmd_book,
        "candles": cmd_candles,
        "funding": cmd_funding,
        "oi": cmd_oi,
        "ticker": cmd_ticker,
    }[args.command](args)


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as exc:
        sys.exit(f"HTTP error: {exc.code} {exc.reason}")
    except Exception as exc:
        sys.exit(str(exc))
