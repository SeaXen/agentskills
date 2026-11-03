#!/usr/bin/env python3
"""
Query the MedSea Notion database to find an existing chapter page.

Use this BEFORE creating a new chapter page to avoid duplicates from
interrupted runs.

Usage:
    python3 search_existing_notion_root.py <dav_num> <chapter_name>
    e.g. python3 search_existing_notion_root.py 10 "Acute medicine and critical illness"

Prints the page ID if found, or "NOT_FOUND" if not.
"""
import os
import sys
import json
import urllib.request
import urllib.error

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
MEDSEA_DB = "3805588e-846f-808b-a23b-cf63c89f372e"


def http(method, url, data=None):
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers={
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    })
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (502, 503, 504, 429):
                import time
                time.sleep(2 ** attempt)
                continue
            return {"_error": e.code, "_body": e.read().decode()[:300]}
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            import time
            time.sleep(2 ** attempt)
            continue
    return {"_error": "max_retries"}


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <dav_num> <chapter_name>")
        print('  e.g. python3 search_existing_notion_root.py 10 "Acute medicine and critical illness"')
        sys.exit(1)
    dav_num = sys.argv[1]
    name = sys.argv[2]
    title = f"Chapter {dav_num}: {name}"

    r = http("POST", f"https://api.notion.com/v1/databases/{MEDSEA_DB}/query",
             data={"filter": {"property": "Name", "title": {"equals": title}}})

    if "_error" in r:
        print(f"API error: {r['_error']}")
        sys.exit(1)
    results = r.get("results", [])
    if not results:
        print("NOT_FOUND")
        sys.exit(0)

    # Print all matches
    for page in results:
        page_id = page["id"]
        url = f"https://app.notion.com/p/SeaHub/{title.replace(' ', '-')}-{page_id.replace('-', '')}"
        print(f"FOUND: {page_id}")
        print(f"URL:   {url}")


if __name__ == "__main__":
    main()
