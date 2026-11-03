#!/usr/bin/env python3
"""
DEXScreener helper for Hermes crypto research workflows.
Uses public API only. No API key required.

Usage:
  python3 dexscreener_client.py search <query>
  python3 dexscreener_client.py token <token_address>
  python3 dexscreener_client.py pair <chain_id> <pair_address>
  python3 dexscreener_client.py boosts [--top 20]
"""

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from typing import Any, Dict, List

BASE = "https://api.dexscreener.com/latest/dex"
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


def normalize_pair(pair: Dict[str, Any]) -> Dict[str, Any]:
    txns = pair.get("txns") or {}
    volume = pair.get("volume") or {}
    price_change = pair.get("priceChange") or {}
    liquidity = pair.get("liquidity") or {}
    base = pair.get("baseToken") or {}
    quote = pair.get("quoteToken") or {}
    return {
        "chain_id": pair.get("chainId"),
        "dex_id": pair.get("dexId"),
        "pair_address": pair.get("pairAddress"),
        "url": pair.get("url"),
        "labels": pair.get("labels") or [],
        "pair_created_at": pair.get("pairCreatedAt"),
        "base_token": {"address": base.get("address"), "symbol": base.get("symbol"), "name": base.get("name")},
        "quote_token": {"address": quote.get("address"), "symbol": quote.get("symbol"), "name": quote.get("name")},
        "price_usd": pair.get("priceUsd"),
        "price_native": pair.get("priceNative"),
        "liquidity_usd": liquidity.get("usd"),
        "fdv": pair.get("fdv"),
        "market_cap": pair.get("marketCap"),
        "txns": txns,
        "volume": volume,
        "price_change_pct": price_change,
        "boosts_active": ((pair.get("boosts") or {}).get("active")),
    }


def sort_pairs(pairs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(
        pairs,
        key=lambda p: ((p.get("liquidity_usd") or 0), (p.get("volume") or {}).get("h24") or 0),
        reverse=True,
    )


def cmd_search(args):
    q = urllib.parse.quote(args.query)
    data = http_get_json(f"{BASE}/search?q={q}")
    pairs = [normalize_pair(p) for p in data.get("pairs") or []]
    print_json({"query": args.query, "pairs": sort_pairs(pairs)[:20]})


def cmd_token(args):
    token = urllib.parse.quote(args.token_address)
    data = http_get_json(f"{BASE}/tokens/{token}")
    pairs = [normalize_pair(p) for p in data.get("pairs") or []]
    print_json({"token_address": args.token_address, "pairs": sort_pairs(pairs)})


def cmd_pair(args):
    chain = urllib.parse.quote(args.chain_id)
    pair = urllib.parse.quote(args.pair_address)
    data = http_get_json(f"{BASE}/pairs/{chain}/{pair}")
    pairs = [normalize_pair(p) for p in data.get("pairs") or []]
    print_json({"chain_id": args.chain_id, "pair_address": args.pair_address, "pairs": pairs})


def cmd_boosts(args):
    data = http_get_json("https://api.dexscreener.com/token-boosts/top/v1")
    rows = []
    for item in data[: args.top]:
        rows.append({
            "chain_id": item.get("chainId"),
            "token_address": item.get("tokenAddress"),
            "amount": item.get("amount"),
            "total_amount": item.get("totalAmount"),
            "description": item.get("description"),
            "url": item.get("url"),
        })
    print_json({"top": args.top, "boosts": rows})


def main() -> None:
    parser = argparse.ArgumentParser(description="DEXScreener helper for Hermes")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search")
    p_search.add_argument("query")

    p_token = sub.add_parser("token")
    p_token.add_argument("token_address")

    p_pair = sub.add_parser("pair")
    p_pair.add_argument("chain_id")
    p_pair.add_argument("pair_address")

    p_boosts = sub.add_parser("boosts")
    p_boosts.add_argument("--top", type=int, default=20)

    args = parser.parse_args()
    {
        "search": cmd_search,
        "token": cmd_token,
        "pair": cmd_pair,
        "boosts": cmd_boosts,
    }[args.command](args)


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as exc:
        sys.exit(f"HTTP error: {exc.code} {exc.reason}")
    except Exception as exc:
        sys.exit(str(exc))
