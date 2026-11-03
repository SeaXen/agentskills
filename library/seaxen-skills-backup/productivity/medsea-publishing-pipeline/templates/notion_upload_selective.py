#!/usr/bin/env python3
"""Upload a select list of topics to Notion MedSea DB.

Validated pattern from cardiology sync 2026-06-19. Differs from the legacy
notion_upload_diseases.py in two ways:
- Uses Notion-Version 2022-06-28 (2025-09-03 breaks new-parent semantics)
- Discovers hub page IDs dynamically via find_hub_page(name) instead of
  hardcoded CARD_HUB_ID/parent_map

Usage:
    1. Define TARGETS = [(prefix, title, hub_name), ...]
    2. Run: python3 notion_upload_selective.py
"""
import json
import sys
import time
import urllib.request
import urllib.error
import uuid
from pathlib import Path

# Working API version (2025-09-03 is BROKEN for new parents)
NV = "2022-06-28"
MEDSEA_DB = "3805588e-846f-808b-a23b-cf63c89f372e"
CARD_HUB_ID = "3825588e846f80cbb9eec8ea437594bc"  # Cardiology root
BASE = "https://api.notion.com/v1"
CHAP = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters/16-cardiology/diseases")

# ---- Topic list (edit per sync) ----
# (prefix-slug, "Display Title", "Hub name to upload under")
TARGETS = [
    # ("16.3.203-cha2ds2-vasc-has-bled", "CHA2DS2-VASc & HAS-BLED Scores", "Arrhythmias"),
    # ("16.6.313-adhf-management", "ADHF Management", "Cardiac Emergencies"),
]

# Load Notion key
KEY = Path("/root/.ndk").read_text().strip()


def call(method, path, payload=None):
    url = f"{BASE}{path}"
    headers = {"Authorization": f"Bearer {KEY}", "Notion-Version": NV}
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
        return e.code, {"_raw": e.read().decode("utf-8", errors="replace")}


def find_hub_page(section_name: str) -> str:
    """Walk CARD_HUB children, return child_page id matching section_name."""
    s, info = call("GET", f"/blocks/{CARD_HUB_ID}/children?page_size=100")
    if s != 200:
        print(f"  ERROR: {info}")
        return None
    for block in info.get("results", []):
        if block.get("type") == "child_page":
            title = block.get("child_page", {}).get("title", "")
            if section_name.lower() in title.lower():
                return block["id"]
    return None


def upload_png(png_path: Path) -> str:
    """3-step file upload (POST metadata → POST bytes → use id in image block).
    Retry on 403 with exponential backoff."""
    fname = png_path.name
    fsize = png_path.stat().st_size
    s, info = call("POST", "/file_uploads",
                    {"filename": fname, "content_type": "image/png",
                     "content_length": fsize})
    if s != 200:
        s, info = call("POST", "/file_uploads",
                        {"filename": fname, "content_type": "image/png"})
        if s != 200:
            raise RuntimeError(f"create_upload failed: {info}")
    upload_id = info["id"]
    upload_url = info.get("upload_url") or f"{BASE}/file_uploads/{upload_id}/send"
    with open(png_path, "rb") as f:
        img_bytes = f.read()
    boundary = uuid.uuid4().hex
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{fname}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode() + img_bytes + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        upload_url, data=body, method="POST",
        headers={"Authorization": f"Bearer {KEY}", "Notion-Version": NV,
                 "Content-Type": f"multipart/form-data; boundary={boundary}"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req) as r:
                r.read()
                return upload_id
        except urllib.error.HTTPError as e:
            if e.code == 403 and attempt < 4:
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"upload_bytes failed: {e.read().decode()[:300]}")
    return upload_id


def create_page_with_image(parent_id, title, md_text, file_upload_id):
    """Create sub-page under parent_id with markdown + appended image block."""
    payload = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "markdown": md_text,
    }
    s, result = call("POST", "/pages", payload)
    if s != 200:
        raise RuntimeError(f"create_page failed for {title}: {result}")
    page_id = result["id"]
    children = [
        {"object": "block", "type": "divider", "divider": {}},
        {"object": "block", "type": "callout",
         "callout": {
             "rich_text": [{"type": "text", "text": {
                 "content": f"Sea Knowledge infographic for {title}."}}],
             "icon": {"type": "emoji", "emoji": "🖼️"},
             "color": "gray_background"}},
        {"object": "block", "type": "image",
         "image": {"type": "file_upload", "file_upload": {"id": file_upload_id}}}
    ]
    s, _ = call("PATCH", f"/blocks/{page_id}/children", {"children": children})
    if s != 200:
        print(f"  WARN: image append failed for {title}")
    return page_id, result.get("url")


def main():
    if not TARGETS:
        print("Nothing to upload — fill in TARGETS first.")
        return

    hubs = {}
    for _, _, hub_name in TARGETS:
        if hub_name not in hubs:
            print(f"Finding hub: {hub_name}...")
            hubs[hub_name] = find_hub_page(hub_name)
            print(f"  → {hubs[hub_name]}")

    missing = [h for h, v in hubs.items() if not v]
    if missing:
        print(f"ERROR: Could not find hubs: {missing}")
        sys.exit(1)

    results = []
    for prefix, title, hub_name in TARGETS:
        chap_dir = CHAP / prefix
        md_path = chap_dir / "topic.md"
        png_path = chap_dir / "topic.png"
        if not md_path.exists() or not png_path.exists():
            print(f"  SKIP: missing {md_path} or {png_path}")
            continue
        print(f"\n--- {prefix}: {title} ---")
        try:
            upload_id = upload_png(png_path)
            page_id, url = create_page_with_image(
                hubs[hub_name], title, md_path.read_text(encoding="utf-8"), upload_id)
            print(f"  ✓ {page_id} → {url}")
            results.append({"slug": prefix, "page_id": page_id, "url": url})
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            results.append({"slug": prefix, "error": str(e)})
        time.sleep(0.5)

    out = Path("/tmp/notion_selective_results.json")
    out.write_text(json.dumps(results, indent=2))
    success = sum(1 for r in results if "page_id" in r)
    print(f"\n=== {success}/{len(results)} uploaded ===\nResults: {out}")


if __name__ == "__main__":
    main()