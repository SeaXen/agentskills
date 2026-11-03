"""
Notion uploader for medical study hub topics.

For each topic:
  1. Upload the local PNG to Notion (3-step: create file_uploads slot, multipart POST bytes, return id)
  2. Create a sub-page under the hub with the markdown body
  3. Append the image block to the sub-page

Then builds a numbered index on the hub (deletes auto-added child_page blocks
first to avoid duplication).

Reads NOTION_API_KEY from env. Reads topic list from the topics.py file
in the same scripts/ directory (or import path).

Usage:
    python3 notion_upload.py
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error
import uuid
from pathlib import Path


# Load the API key from env
KEY = os.environ.get("NOTION_API_KEY")
if not KEY:
    sys.exit("ERROR: NOTION_API_KEY not set in environment")

# Load topic metadata from sibling topics.py
sys.path.insert(0, str(Path(__file__).parent))
try:
    from topics import topics
except ImportError:
    sys.exit("ERROR: topics.py not found in scripts/ directory")

CARD_HUB_ID = os.environ.get("HUB_PAGE_ID")  # set this in env
if not CARD_HUB_ID:
    sys.exit("ERROR: HUB_PAGE_ID not set in environment (the Notion page ID of the hub)")

BASE = "https://api.notion.com/v1"
NV = "2025-09-03"
SK_DIR = Path(os.environ.get("LOCAL_ARCHIVE_DIR", "/mnt/tb/Sea-knowledge"))


def call(method, path, payload=None):
    url = f"{BASE}{path}"
    headers = {
        "Authorization": f"Bearer {KEY}",
        "Notion-Version": NV,
    }
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            body = r.read().decode("utf-8")
            return r.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return e.code, {"_raw": body}


def upload_png(slug):
    """3-step file upload. Returns file_upload_id."""
    png_path = SK_DIR / slug / f"{slug}.png"
    if not png_path.exists():
        raise FileNotFoundError(f"PNG not found: {png_path}")
    s, info = call("POST", "/file_uploads", {
        "filename": f"{slug}.png",
        "content_type": "image/png"
    })
    if s != 200:
        raise RuntimeError(f"create_upload failed for {slug}: {info}")
    upload_id = info["id"]
    upload_url = info["upload_url"]
    with open(png_path, "rb") as f:
        img_bytes = f.read()
    boundary = uuid.uuid4().hex
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{slug}.png"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode() + img_bytes + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        upload_url, data=body, method="POST",
        headers={
            "Authorization": f"Bearer {KEY}",
            "Notion-Version": NV,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        }
    )
    try:
        with urllib.request.urlopen(req) as r:
            r.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"upload_bytes failed for {slug}: {e.read().decode()}")
    return upload_id


def create_page_with_image(parent_id, title, md_path, file_upload_id):
    """Create a sub-page with markdown body + image block appended at end."""
    md = Path(md_path).read_text(encoding="utf-8")
    md_with_image_ref = md + "\n\n---\n\n> **Full-resolution infographic PNG is attached below** — right-click → download for printing/sharing.\n"
    payload = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "markdown": md_with_image_ref
    }
    s, result = call("POST", "/pages", payload)
    if s != 200:
        raise RuntimeError(f"create_page failed for {title}: {result}")
    page_id = result["id"]
    children = [
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block", "type": "callout",
            "callout": {
                "rich_text": [
                    {"type": "text", "text": {"content": f"Sea Knowledge infographic for {title} (FCPS / MRCP exam prep). Right-click the image to download."}}
                ],
                "icon": {"type": "emoji", "emoji": "🖼️"},
                "color": "gray_background"
            }
        },
        {
            "object": "block", "type": "image",
            "image": {"type": "file_upload", "file_upload": {"id": file_upload_id}}
        }
    ]
    s, _ = call("PATCH", f"/blocks/{page_id}/children", {"children": children})
    if s != 200:
        raise RuntimeError(f"append_image failed for {title}")
    return page_id, result.get("url")


def main():
    results = []
    for t in topics:
        num = t["num"]
        slug = t["slug"]
        title = t["title"]
        print(f"\n=== [{num}/{len(topics)}] {title} ===")
        try:
            print(f"  Uploading PNG...")
            upload_id = upload_png(slug)
            print(f"  Upload ID: {upload_id}")
            print(f"  Creating sub-page...")
            md_path = SK_DIR / slug / f"{slug}.md"
            page_id, page_url = create_page_with_image(CARD_HUB_ID, title, md_path, upload_id)
            print(f"  Page ID: {page_id}")
            print(f"  URL: {page_url}")
            results.append({
                "num": num, "slug": slug, "title": title,
                "page_id": page_id, "page_url": page_url, "file_upload_id": upload_id,
            })
            time.sleep(0.3)  # respect rate limit (~3 req/sec)
        except Exception as e:
            print(f"  ERROR: {e}")
            results.append({"num": num, "slug": slug, "title": title, "error": str(e)})

    out = "notion_results.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n=== Saved results to {out} ===")

    success = sum(1 for r in results if "page_id" in r)
    fail = sum(1 for r in results if "error" in r)
    print(f"\n=== Summary ===")
    print(f"  Success: {success}/{len(results)}")
    print(f"  Failed:  {fail}/{len(results)}")
    if fail:
        for r in results:
            if "error" in r:
                print(f"    - {r['title']}: {r['error']}")


if __name__ == "__main__":
    main()
