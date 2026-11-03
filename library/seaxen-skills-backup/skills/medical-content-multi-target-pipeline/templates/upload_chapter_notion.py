#!/usr/bin/env python3
"""
MedSea Notion upload pipeline — TEMPLATE.

Use this as a starting point for uploading a Davidson chapter to the MedSea Notion database.

Key concepts:
- MedSea DB ID: 3805588e-846f-808b-a23b-cf63c89f372e
- Search-existing pattern: avoid duplicate root pages from interrupted runs
- File uploads 2-step: metadata + multipart POST
- 403 retry with exponential backoff

Validated: Ch 10-15 upload 2026-06-19, 182/182 topics, 0 failures.
"""
import os, sys, json, re, time, uuid, urllib.request, urllib.error
from pathlib import Path

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
NOTION_VERSION = "2022-06-28"
MEDSEA_DB = "3805588e-846f-808b-a23b-cf63c89f372e"

# (dav_num_25th_ed, slug, name_25th_ed)
# Pre-populate root_id once known to skip creation on rerun
CHAPTERS = [
    # {"dav_num": 10, "slug": "10-acute-medicine", "name": "Acute medicine and critical illness",
    #  "root_id": "3835588e-846f-81a1-bd40-fbd5d564fd2e"},
    # Add your chapter here
]


def http(method, url, data=None, return_raw=False):
    """Notion API HTTP wrapper with retry."""
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url, data=body, method=method, headers={
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    })
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                if return_raw:
                    return r.read()
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            txt = e.read().decode()
            if e.code == 429:
                wait = int(e.headers.get("Retry-After", "3"))
                time.sleep(wait)
                continue
            if e.code in (502, 503, 504, 403):
                time.sleep(2 ** attempt)
                continue
            return {"_error": e.code, "_body": txt[:500]}
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            time.sleep(2 ** attempt)
            continue
    return {"_error": "max_retries"}


def search_existing_root(dav_num, name):
    """Query MedSea DB for an existing chapter page with the given name."""
    r = http("POST", f"https://api.notion.com/v1/databases/{MEDSEA_DB}/query",
             data={"filter": {"property": "Name", "title": {"equals": f"Chapter {dav_num}: {name}"}}})
    if isinstance(r, dict) and r.get("results"):
        return r["results"][0]["id"]
    return None


def create_root_page(dav_num, name):
    """Create a chapter page in the MedSea DB."""
    payload = {
        "parent": {"type": "database_id", "database_id": MEDSEA_DB},
        "properties": {
            "Name": {"title": [{"type": "text", "text": {"content": f"Chapter {dav_num}: {name}"}}]},
        },
    }
    r = http("POST", "https://api.notion.com/v1/pages", data=payload)
    if "_error" in r:
        return None, r
    return r["id"], r


def upload_png(path):
    """2-step file upload: create metadata, then send file."""
    create = http("POST", "https://api.notion.com/v1/file_uploads",
                  data={"filename": path.name, "content_type": "image/png",
                        "content_length": path.stat().st_size})
    if "_error" in create:
        return None, create
    upload_id = create["id"]
    send_url = create.get("upload_url") or f"https://api.notion.com/v1/file_uploads/{upload_id}/send"
    boundary = f"----NotionBoundary{uuid.uuid4().hex}"
    with open(path, "rb") as f:
        fb = f.read()
    body = (f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
            f"Content-Type: image/png\r\n\r\n").encode() + fb + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(send_url, data=body, method="POST", headers={
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": f"multipart/form-data; boundary={boundary}"
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return upload_id, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return None, {"_error": e.code, "_body": e.read().decode()[:300]}


def get_or_create_hub(root_id, hub_num, hub_name, existing_hubs):
    """Find existing hub or create new."""
    target_title = f"{hub_num} {hub_name}"
    for h in existing_hubs:
        title = h.get("child_page", {}).get("title", "")
        if title.startswith(f"{hub_num} ") and hub_name.lower() in title.lower():
            return h["id"], "existing"
    payload = {
        "parent": {"type": "page_id", "page_id": root_id},
        "properties": {"title": [{"type": "text", "text": {"content": target_title}}]}
    }
    r = http("POST", "https://api.notion.com/v1/pages", data=payload)
    if "_error" in r:
        return None, r
    return r["id"], "created"


def fetch_children(block_id):
    """Fetch all child pages of a block with pagination."""
    out = []
    cursor = None
    while True:
        url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"
        r = http("GET", url)
        if "_error" in r:
            return r
        out.extend(r.get("results", []))
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    return out


def create_topic_page(hub_id, title, md_content, png_path=None):
    """Create a topic page under a hub with markdown content + optional image."""
    children = []
    if png_path:
        # Try upload, skip on failure
        upload_id, _ = upload_png(png_path)
        if upload_id:
            children.append({
                "type": "image",
                "image": {"type": "file_upload", "file_upload": {"id": upload_id}},
            })
    # Try with markdown first
    payload = {
        "parent": {"type": "page_id", "page_id": hub_id},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "markdown": md_content,
    }
    if children:
        payload["children"] = children
    r = http("POST", "https://api.notion.com/v1/pages", data=payload)
    if "_error" in r:
        # Fallback: markdown only, no children
        payload2 = {k: v for k, v in payload.items() if k != "children"}
        r = http("POST", "https://api.notion.com/v1/pages", data=payload2)
        if "_error" in r:
            return None, r
        page_id = r["id"]
        if children:
            http("PATCH", f"https://api.notion.com/v1/blocks/{page_id}/children", data={"children": children})
        return r.get("url"), r
    return r.get("url"), r


def upload_chapter(ch, skip_existing=True):
    """Upload a single chapter to Notion."""
    medsea_chap = Path(f"/mnt/tb/Sea-knowledge/#MedSea/chapters/{ch['slug']}")
    diseases_dir = medsea_chap / "diseases"
    if not diseases_dir.exists():
        return {"ok": False, "error": "no diseases dir"}

    if not ch.get("root_id"):
        # Search for existing root first
        existing = search_existing_root(ch["dav_num"], ch["name"])
        if existing:
            ch["root_id"] = existing
            root_id = existing
            print(f"  Found existing root: {existing}", flush=True)
        else:
            root_id, r = create_root_page(ch["dav_num"], ch["name"])
            if not root_id:
                return {"ok": False, "error": r}
            ch["root_id"] = root_id
            print(f"  Created root: {root_id}", flush=True)
    else:
        root_id = ch["root_id"]
        print(f"  Using existing root: {root_id}", flush=True)

    # Fetch existing children
    existing = fetch_children(root_id)
    if isinstance(existing, dict) and "_error" in existing:
        existing = []
    existing_hubs = [c for c in existing if c.get("type") == "child_page"]
    print(f"  Root has {len(existing_hubs)} existing children", flush=True)

    # Group topics by hub
    hub_groups = {}
    for topic_dir in sorted(diseases_dir.iterdir()):
        if not topic_dir.is_dir():
            continue
        m = re.match(r"^(\d+)\.(\d+)\.(\d+)-(.+)$", topic_dir.name)
        if not m:
            continue
        dav_num, hub_num, idx, name = m.groups()
        md_file = topic_dir / "topic.md"
        if not md_file.exists():
            continue
        hub_groups.setdefault(int(hub_num), []).append((int(idx), name, md_file))

    stats = {"topics_ok": 0, "topics_failed": 0, "topics_skipped": 0, "hubs_created": 0}
    for hub_num in sorted(hub_groups):
        # Get/create hub
        hub_name = f"Hub {hub_num}"
        hub_id, status = get_or_create_hub(root_id, hub_num, hub_name, existing_hubs)
        if not hub_id:
            print(f"  Hub {hub_num} failed: {hub_id}", flush=True)
            continue
        if status == "created":
            stats["hubs_created"] += 1
        # Upload topics
        for idx, name, md_file in hub_groups[hub_num]:
            title = name.replace("-", " ").title()
            png_path = md_file.parent / "topic.png"
            md_content = md_file.read_text(encoding="utf-8", errors="replace")
            url, r = create_topic_page(hub_id, title, md_content, png_path if png_path.exists() else None)
            if url:
                stats["topics_ok"] += 1
                print(f"  OK  {ch['dav_num']}.{hub_num}.{idx:02d}", flush=True)
            else:
                stats["topics_failed"] += 1
                print(f"  FAIL {ch['dav_num']}.{hub_num}.{idx:02d}: {r}", flush=True)
            time.sleep(0.5)  # Rate limit

    return {"ok": True, "stats": stats, "root_id": ch.get("root_id")}


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    overall = {}
    for ch in CHAPTERS:
        if only and str(ch["dav_num"]) != only and ch["slug"] != only:
            continue
        print(f"\n{'='*60}\nCh {ch['dav_num']}: {ch['name']}\n{'='*60}", flush=True)
        result = upload_chapter(ch)
        overall[ch["dav_num"]] = result.get("stats", {})
        if result.get("root_id"):
            ch["root_id"] = result["root_id"]
            print(f"  ROOT ID: {result['root_id']}", flush=True)

    print("\n=== FINAL ===", flush=True)
    for dav_num, stats in overall.items():
        print(f"  Ch {dav_num}: ok={stats.get('topics_ok', 0)}, failed={stats.get('topics_failed', 0)}", flush=True)


if __name__ == "__main__":
    main()
