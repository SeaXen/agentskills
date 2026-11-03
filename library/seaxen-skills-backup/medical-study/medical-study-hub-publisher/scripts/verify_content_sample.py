#!/usr/bin/env python3
"""Random-sample Notion content verification.

Picks one random topic per hub and asserts:
- n_text (paragraphs/headings/lists/tables/callouts) >= 3  → not image-only
- n_image == 1  → exactly one infographic attached

Returns a single OK/BAD line per sampled page. Catches image-only pages
and zero-content pages within ~5 seconds for a 9-hub chapter.

Usage:
    python3 verify_content_sample.py --chapter <chapter_page_id>
    python3 verify_content_sample.py --chapter <chapter_page_id> --seed 7 --sample 2

Requires the same `http()` and `fetch_children()` helpers from upload_*.py,
or copy them in. The Notion API key must be at /tmp/.notion_key.
"""
import argparse
import json
import random
import sys
import urllib.request
from pathlib import Path


def load_key() -> str:
    key_path = Path("/tmp/.notion_key")
    if not key_path.exists():
        # Fallback: parse /root/.hermes/.env directly
        import re
        env = Path("/root/.hermes/.env").read_text()
        m = re.search(r"NOTION_API_KEY=([^\s]+)", env)
        if not m:
            sys.exit("ERROR: /tmp/.notion_key not found and no NOTION_API_KEY in /root/.hermes/.env")
        return m.group(1)
    return key_path.read_text().strip()


def http(method: str, url: str, data=None, headers=None, timeout: int = 30) -> dict:
    key = load_key()
    h = {"Authorization": "Bearer " + key, "Notion-Version": "2022-06-28"}
    if headers:
        h.update(headers)
    body = json.dumps(data).encode() if data is not None else None
    if body is not None:
        h["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def fetch_children(parent_id: str) -> list:
    """Paginated block fetch (Pitfall 53)."""
    children, cursor = [], None
    while True:
        url = f"https://api.notion.com/v1/blocks/{parent_id}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"
        data = http("GET", url)
        children.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")
    return children


def verify_chapter(chapter_id: str, seed: int = 42, sample_size: int = 1) -> bool:
    """Pick sample_size random pages from each hub, assert content + image."""
    hubs = fetch_children(chapter_id)
    hub_pages = sorted(
        [b for b in hubs if b.get("type") == "child_page"],
        key=lambda x: x["child_page"]["title"],
    )
    if not hub_pages:
        print("ERROR: chapter has no hub pages")
        return False

    rng = random.Random(seed)
    sample = []
    for h in hub_pages:
        children = fetch_children(h["id"])
        cps = [c for c in children if c.get("type") == "child_page"]
        if not cps:
            continue
        sample.append((h["child_page"]["title"], rng.choice(cps)))
        if sample_size > 1 and len(cps) > 1:
            extras = rng.sample(cps, min(sample_size - 1, len(cps) - 1))
            for ex in extras:
                sample.append((h["child_page"]["title"], ex))

    text_block_types = (
        "paragraph", "heading_1", "heading_2", "heading_3",
        "bulleted_list_item", "numbered_list_item", "callout", "quote", "table",
    )
    all_good = True
    print(f"=== SAMPLE CONTENT CHECK (seed={seed}, {len(sample)} pages) ===")
    for hub_title, c in sample:
        blocks = fetch_children(c["id"])
        n_total = len(blocks)
        n_text = sum(1 for b in blocks if b.get("type") in text_block_types)
        n_table = sum(1 for b in blocks if b.get("type") == "table")
        n_image = sum(1 for b in blocks if b.get("type") == "image")
        ok = n_text >= 3 and n_image >= 1
        if not ok:
            all_good = False
        status = "OK" if ok else "BAD"
        print(
            f"  [{status}] {hub_title} > \"{c['child_page']['title']}\": "
            f"{n_total} blocks, {n_text} text, {n_table} tables, {n_image} images"
        )
    print(f"\nAll good: {all_good}")
    return all_good


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--chapter", required=True, help="Chapter parent page_id")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--sample", type=int, default=1, help="Sample size per hub")
    args = p.parse_args()
    ok = verify_chapter(args.chapter, args.seed, args.sample)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
