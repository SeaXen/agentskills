# MedSea Notion Chapter Page Discovery

The MedSea workspace is a Notion **database** at ID `3805588e846f808ba23bcf63c89f372e`. Each chapter is a row in that database. Atomic topics and overviews are child pages of each chapter row.

## Discovering chapter page IDs

Do NOT use `/v1/search` — it returns workspace-wide fuzzy matches and the IDs all share the same `3805588e` prefix, which makes them look identical. Instead use the database query endpoint:

```python
import urllib.request, json, time, urllib.error

api_key = "..."  # NOTION_API_KEY from /root/.hermes/.env
db_id = "3805588e846f808ba23bcf63c89f372e".replace("-", "")

def http(method, url, data=None):
    h = {"Authorization": f"Bearer {api_key}",
         "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(int(e.headers.get("Retry-After", "5")))
                continue
            return {"_error": e.code, "_body": e.read().decode()[:300]}
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(5 + attempt * 2)
            continue
    return {"_error": "max_retries"}

# Get chapter row by number
def find_chapter(ch_num):
    body = {"page_size": 100,
            "filter": {"property": "title",
                       "title": {"starts_with": f"Chapter {ch_num}:"}}}
    r = http("POST", f"https://api.notion.com/v1/databases/{db_id}/query", body)
    if r.get("results"):
        # Some chapters have duplicates (e.g. ch 10 Acute Medicine + Acute medicine,
        # ch 12 HIV + Envenomation). Filter to lowercase-MedSea-matched one.
        medsea_slugs = {
            10: "acute-medicine", 12: "envenomation",  # lowercase MedSea match
        }
        target_kw = medsea_slugs.get(ch_num, "").lower()
        for page in r["results"]:
            title = ""
            for prop_name, prop_val in page.get("properties", {}).items():
                if prop_val.get("type") == "title":
                    for t in prop_val.get("title", []):
                        title += t.get("text", {}).get("content", "")
            if target_kw and target_kw in title.lower():
                return page["id"].replace("-", ""), title
        # Fallback to first match
        page = r["results"][0]
        return page["id"].replace("-", ""), title
    return None, None
```

## Creating MOC + Hierarchy pages

The `markdown` field on a page-creation call lets Notion auto-convert MD to blocks:

```python
def create_overview_page(parent_id, title, md_content, icon="🗺️"):
    payload = {
        "parent": {"type": "page_id", "page_id": parent_id.replace("-", "")},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "markdown": md_content,
        "icon": {"type": "emoji", "emoji": icon},
    }
    return http("POST", "https://api.notion.com/v1/pages", payload)
```

## Pre-fetch existing children to skip duplicates

Before creating, list existing child pages under each chapter to avoid creating duplicates:

```python
def fetch_child_pages(chapter_id):
    titles = {}
    cursor = None
    while True:
        path = f"/blocks/{chapter_id}/children?page_size=100"
        if cursor:
            path += f"&start_cursor={cursor}"
        r = http("GET", f"https://api.notion.com/v1{path}")
        if "results" not in r:
            break
        for b in r["results"]:
            if b.get("type") == "child_page":
                t = b.get("child_page", {}).get("title", "").lower().strip()
                titles[t] = b["id"]
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    return titles
```

## Known duplicates in the MedSea Notion DB

| Ch | Multiple pages | Correct one for MedSea |
|----|----------------|------------------------|
| 10 | "Acute Medicine and Critical Illness" + "Acute medicine and critical illness" | lowercase one |
| 12 | "HIV infection and AIDS" + "Envenomation" | Envenomation (matches ch 12 slug) |
| 17 | "Respiratory medicine" (×2) | first one (both same content) |

## Rate limits

- Notion API: ~3 requests/second per token
- First sync run after a long idle period can hit 429 hard → respect `Retry-After`
- Realistic sync rate: ~20-25 pages/min sustained