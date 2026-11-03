#!/usr/bin/env python3
"""
Clean up Notion orphan pages left behind by a failed/buggy sync run.

Pattern validated 2026-06-20 after a hub/slug regex bug created an orphan
"31.31 Hub 31.31" with 49 wrongly-bucketed child topics under it.

Usage:
    python3 scripts/notion_cleanup_orphans.py "31.31"

Or scan for ALL pages matching a bad prefix pattern:
    python3 scripts/notion_cleanup_orphans.py --scan "31.31"
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

# Load API key from env (see SKILL.md pitfall: never literalize secrets)
api_key = os.environ.get("NOTION_API_KEY")
if not api_key:
    # Try reading from .env (without writing secrets to source code)
    try:
        with open("/root/.hermes/.env") as f:
            for line in f:
                if line.startswith("NOTION_API_KEY"):
                    api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    except Exception:
        pass

if not api_key:
    print("❌ NOTION_API_KEY not set in environment", file=sys.stderr)
    sys.exit(1)


def http(method, url, data=None):
    h = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            txt = e.read().decode()
            if e.code == 429:
                wait = int(e.headers.get("Retry-After", "5"))
                print(f"  429 rate-limited, sleeping {wait}s")
                time.sleep(wait)
                continue
            return {"_error": e.code, "_body": txt[:300]}
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(5 + attempt * 2)
    return {"_error": "max_retries"}


def archive_page(page_id):
    """Archive (soft-delete) a Notion page."""
    r = http("PATCH", f"https://api.notion.com/v1/pages/{page_id}", {"archived": True})
    return "_error" not in r


def find_pages_by_title_prefix(prefix, max_results=20):
    """Search Notion for pages whose title starts with the given prefix."""
    found = []
    r = http("POST", "https://api.notion.com/v1/search", {
        "query": prefix,
        "filter": {"property": "object", "value": "page"},
        "page_size": max_results,
    })
    if "results" not in r:
        return found
    for page in r["results"]:
        title_obj = page.get("properties", {}).get("title", {})
        if title_obj.get("type") == "title":
            title = "".join(t.get("plain_text", "") for t in title_obj.get("title", []))
            # Exact startswith check (not substring — search is fuzzy)
            if title.startswith(prefix):
                found.append({
                    "id": page["id"].replace("-", ""),
                    "title": title,
                })
    return found


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 notion_cleanup_orphans.py <title-prefix>")
        print("       python3 notion_cleanup_orphans.py '31.31'")
        print("       python3 notion_cleanup_orphans.py '21.0.1-diabetes-moc'")
        sys.exit(1)

    prefix = sys.argv[1]

    print(f"🔍 Searching Notion for pages starting with: {prefix!r}")
    matches = find_pages_by_title_prefix(prefix)
    if not matches:
        print("  No matches found.")
        sys.exit(0)

    print(f"\n📋 Found {len(matches)} page(s) to archive:")
    for m in matches:
        print(f"  - {m['id'][:20]} | {m['title'][:60]}")

    print(f"\n⚠️  About to archive {len(matches)} pages. Continue? [y/N]")
    response = input().strip().lower()
    if response != "y":
        print("Aborted.")
        sys.exit(0)

    archived = 0
    for m in matches:
        print(f"  Archiving {m['title'][:50]}...", end=" ")
        if archive_page(m["id"]):
            print("✅")
            archived += 1
        else:
            print("❌")
        time.sleep(0.5)

    print(f"\n✅ Archived {archived}/{len(matches)} pages")
    print("Note: archived pages are in Notion's trash and can be restored within 30 days.")


if __name__ == "__main__":
    main()