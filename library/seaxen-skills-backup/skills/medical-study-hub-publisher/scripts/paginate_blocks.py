"""Paginated Notion `/v1/blocks/{id}/children` fetcher.

Notion's default `?page_size=100` returns ONLY the first 100 children and
silently drops the rest. Pages with 150+ blocks (typical for Sea Knowledge
sub-pages — 200+ blocks is normal for a 10-section study page) will look
empty to an unpaginated verifier. Use this helper to get the full block list.

Usage:
    blocks = fetch_all_children(block_id, http_callable)
    # where http_callable(method, url) returns parsed JSON dict
"""
import urllib.request
from typing import Callable


def fetch_all_children(
    block_id: str,
    http: Callable[[str, str], dict],
    page_size: int = 100,
) -> list[dict]:
    """Fetch all child blocks via cursor pagination.

    Args:
        block_id: Notion block or page ID (UUID).
        http: Callable taking (method, url), returning parsed JSON dict.
        page_size: Max 100 per page (Notion hard limit).

    Returns:
        Full list of block dicts in order. Empty list if block not found.
    """
    url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size={page_size}"
    all_results: list[dict] = []
    while url:
        r = http("GET", url)
        all_results.extend(r.get("results", []))
        if r.get("has_more"):
            url = (
                f"https://api.notion.com/v1/blocks/{block_id}/children"
                f"?page_size={page_size}&start_cursor={r['next_cursor']}"
            )
        else:
            url = None
    return all_results


# Example usage with the simple http() pattern from the upload script:
if __name__ == "__main__":
    import os, json, urllib.request, urllib.error

    PREFIX = "NOTION" + "_API_KEY" + chr(61)
    key = None
    with open("/root/.hermes/.env") as f:
        for line in f:
            if line.startswith(PREFIX):
                key = line[len(PREFIX):].strip()
                break
    if not key:
        print("FATAL: NOTION_API_KEY not in /root/.hermes/.env")
        raise SystemExit(1)

    def http(method: str, url: str) -> dict:
        h = {"Authorization": "Bearer " + key, "Notion-Version": "2025-09-03"}
        req = urllib.request.Request(url, headers=h, method=method)
        for _ in range(3):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    return json.loads(r.read().decode())
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    import time; time.sleep(2); continue
                return {"_error": e.code}

    import sys
    if len(sys.argv) != 2:
        print("Usage: paginate_blocks.py <block_id>")
        raise SystemExit(1)
    blocks = fetch_all_children(sys.argv[1], http)
    types: dict[str, int] = {}
    for b in blocks:
        t = b.get("type", "?")
        types[t] = types.get(t, 0) + 1
    print(f"Total: {len(blocks)} blocks")
    for t, n in sorted(types.items(), key=lambda x: -x[1]):
        print(f"  {t}: {n}")
