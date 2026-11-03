#!/usr/bin/env python3
"""
CoinGecko helper for Hermes crypto research workflows.
Uses public API only. No API key required.

Usage:
  python3 coingecko_client.py trending
  python3 coingecko_client.py search <query>
  python3 coingecko_client.py coin <coin_id>
  python3 coingecko_client.py markets [--vs usd] [--per-page 10] [--page 1]
  python3 coingecko_client.py category <category_id> [--vs usd]
  python3 coingecko_client.py categories [--top 20]
"""

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from typing import Any, Dict

BASE = "https://api.coingecko.com/api/v3"
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


def pct_fields(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "change_24h_pct": item.get("price_change_percentage_24h_in_currency") or item.get("price_change_percentage_24h"),
        "change_7d_pct": item.get("price_change_percentage_7d_in_currency"),
        "change_30d_pct": item.get("price_change_percentage_30d_in_currency"),
    }


def cmd_trending(_args):
    data = http_get_json(f"{BASE}/search/trending")
    coins = []
    for row in data.get("coins", []):
        item = row.get("item", {})
        coins.append({
            "name": item.get("name"),
            "symbol": item.get("symbol"),
            "coin_id": item.get("id"),
            "market_cap_rank": item.get("market_cap_rank"),
            "price_btc": item.get("price_btc"),
        })
    print_json({"trending": coins})


def cmd_search(args):
    q = urllib.parse.quote(args.query)
    data = http_get_json(f"{BASE}/search?query={q}")
    results = []
    for item in data.get("coins", [])[:15]:
        results.append({
            "name": item.get("name"),
            "symbol": item.get("symbol"),
            "coin_id": item.get("id"),
            "market_cap_rank": item.get("market_cap_rank"),
        })
    print_json({"query": args.query, "results": results})


def cmd_coin(args):
    coin_id = urllib.parse.quote(args.coin_id)
    params = urllib.parse.urlencode({
        "localization": "false",
        "tickers": "false",
        "market_data": "true",
        "community_data": "false",
        "developer_data": "false",
        "sparkline": "false",
    })
    data = http_get_json(f"{BASE}/coins/{coin_id}?{params}")
    md = data.get("market_data", {})
    out = {
        "id": data.get("id"),
        "symbol": data.get("symbol"),
        "name": data.get("name"),
        "market_cap_rank": data.get("market_cap_rank"),
        "current_price_usd": (md.get("current_price") or {}).get("usd"),
        "market_cap_usd": (md.get("market_cap") or {}).get("usd"),
        "fully_diluted_valuation_usd": (md.get("fully_diluted_valuation") or {}).get("usd"),
        "circulating_supply": md.get("circulating_supply"),
        "total_supply": md.get("total_supply"),
        "max_supply": md.get("max_supply"),
        "ath_usd": (md.get("ath") or {}).get("usd"),
        "atl_usd": (md.get("atl") or {}).get("usd"),
        "price_change_pct": {
            "24h": md.get("price_change_percentage_24h"),
            "7d": md.get("price_change_percentage_7d"),
            "30d": md.get("price_change_percentage_30d"),
            "1y": md.get("price_change_percentage_1y"),
        },
        "volume_usd": (md.get("total_volume") or {}).get("usd"),
        "categories": data.get("categories", [])[:15],
    }
    print_json(out)


def cmd_markets(args):
    params = urllib.parse.urlencode({
        "vs_currency": args.vs,
        "order": "market_cap_desc",
        "per_page": args.per_page,
        "page": args.page,
        "sparkline": "false",
        "price_change_percentage": "24h,7d,30d",
    })
    data = http_get_json(f"{BASE}/coins/markets?{params}")
    rows = []
    for item in data:
        row = {
            "id": item.get("id"),
            "symbol": item.get("symbol"),
            "name": item.get("name"),
            "current_price": item.get("current_price"),
            "market_cap": item.get("market_cap"),
            "market_cap_rank": item.get("market_cap_rank"),
            "fully_diluted_valuation": item.get("fully_diluted_valuation"),
            "volume": item.get("total_volume"),
            "circulating_supply": item.get("circulating_supply"),
            "max_supply": item.get("max_supply"),
        }
        row.update(pct_fields(item))
        rows.append(row)
    print_json({"vs_currency": args.vs, "page": args.page, "rows": rows})


def cmd_category(args):
    cat = urllib.parse.quote(args.category_id)
    params = urllib.parse.urlencode({
        "vs_currency": args.vs,
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h,7d,30d",
        "category": cat,
    })
    data = http_get_json(f"{BASE}/coins/markets?{params}")
    rows = []
    for item in data:
        row = {
            "id": item.get("id"),
            "symbol": item.get("symbol"),
            "name": item.get("name"),
            "current_price": item.get("current_price"),
            "market_cap": item.get("market_cap"),
            "fdv": item.get("fully_diluted_valuation"),
            "volume": item.get("total_volume"),
        }
        row.update(pct_fields(item))
        rows.append(row)
    print_json({"category_id": args.category_id, "vs_currency": args.vs, "rows": rows})


def cmd_categories(args):
    data = http_get_json(f"{BASE}/coins/categories")
    rows = []
    for item in data[: args.top]:
        rows.append({
            "category_id": item.get("id"),
            "name": item.get("name"),
            "market_cap": item.get("market_cap"),
            "volume_24h": item.get("volume_24h"),
            "change_24h_pct": item.get("market_cap_change_24h"),
            "top_3_coins": item.get("top_3_coins") or [],
        })
    print_json({"top": args.top, "categories": rows})


def main() -> None:
    parser = argparse.ArgumentParser(description="CoinGecko helper for Hermes")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("trending")

    p_search = sub.add_parser("search")
    p_search.add_argument("query")

    p_coin = sub.add_parser("coin")
    p_coin.add_argument("coin_id")

    p_markets = sub.add_parser("markets")
    p_markets.add_argument("--vs", default="usd")
    p_markets.add_argument("--per-page", type=int, default=10)
    p_markets.add_argument("--page", type=int, default=1)

    p_cat = sub.add_parser("category")
    p_cat.add_argument("category_id")
    p_cat.add_argument("--vs", default="usd")

    p_categories = sub.add_parser("categories")
    p_categories.add_argument("--top", type=int, default=20)

    args = parser.parse_args()
    {
        "trending": cmd_trending,
        "search": cmd_search,
        "coin": cmd_coin,
        "markets": cmd_markets,
        "category": cmd_category,
        "categories": cmd_categories,
    }[args.command](args)


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as exc:
        sys.exit(f"HTTP error: {exc.code} {exc.reason}")
    except Exception as exc:
        sys.exit(str(exc))
