# MedSea Notion Database — API Reference

## The Database

The MedSea chapters are stored in a Notion **DATABASE**, not a workspace or a single page.

- **Database ID**: `3805588e-846f-808b-a23b-cf63c89f372e`
- **Title**: "MedSea" (from database title field)
- **Properties**: Only `Name` (title type)
- **Database URL**: `https://www.notion.so/3805588e846f808ba23bcf63c89f372e`

## Why This Matters

Notion API requires:
- For pages in a database: `parent: {type: "database_id", database_id: "..."}`
- For child pages: `parent: {type: "page_id", page_id: "..."}` (works for sub-pages of database rows)
- For new top-level pages: `parent: {type: "workspace", workspace: true}` does NOT work — must use database or page parent

## Common Pitfalls

### 1. `parent: workspace` fails with 400
```python
# WRONG — Notion API rejects
{"parent": {"type": "workspace", "workspace": True}}

# CORRECT — use the MedSea DB
{"parent": {"type": "database_id", "database_id": "3805588e-846f-808b-a23b-cf63c89f372e"},
 "properties": {"Name": {"title": [{"type": "text", "text": {"content": "Chapter 10: ..."}}]}}}
```

### 2. `child_page` blocks cannot be reparented
Once a sub-page (hub, topic) is created under a page, you CANNOT move it to a different parent via PATCH `/v1/pages`. The API returns 200 but the parent field is silently ignored.

```python
# This succeeds (200) but doesn't actually reparent
http("PATCH", f"/v1/pages/{child_id}", data={"parent": {"type": "page_id", "page_id": new_parent_id}})
# Verify by GETting the page — parent is still the old one
```

**Workaround** for chapter renames: create the NEW chapter page, add a redirect callout at the top of the OLD page, accept that sub-pages stay where they are.

### 3. Hub pages must be created before topic pages
The upload script creates hubs first, then topics as children of hubs. If you create topics before hubs, they'll be orphaned at the chapter root.

### 4. File upload 2-step process
Notion's file upload API is two steps — JSON metadata first, then multipart upload:

```python
# Step 1: Create file upload metadata
create = http("POST", "/v1/file_uploads",
              data={"filename": "topic.png", "content_type": "image/png",
                    "content_length": png_size})
upload_id = create["id"]
upload_url = create["upload_url"]  # or construct: /v1/file_uploads/{id}/send

# Step 2: Send the file as multipart
boundary = f"----NotionBoundary{uuid.uuid4().hex}"
with open(png_path, "rb") as f:
    file_bytes = f.read()
body = (f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="topic.png"\r\n'
        f"Content-Type: image/png\r\n\r\n").encode() + file_bytes + f"\r\n--{boundary}--\r\n".encode()
req = urllib.request.Request(upload_url, data=body, method="POST", headers={
    "Authorization": f"Bearer {API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": f"multipart/form-data; boundary={boundary}"
})
urllib.request.urlopen(req)
```

### 5. 403 retry with backoff for file_uploads
Notion's file_uploads endpoint frequently returns 403 with no retry-after. Add retry logic:

```python
for attempt in range(5):
    try:
        return create_file_upload(...)
    except HTTPError as e:
        if e.code in (502, 503, 504, 403):
            time.sleep(2 ** attempt)
            continue
        raise
```

### 6. Native `markdown` field vs `children` blocks
Notion accepts markdown as a single field for new pages, OR children blocks. **Do NOT combine both** in one POST — pick one:

```python
# Option A: markdown (recommended for content-heavy pages)
{"parent": ..., "properties": ..., "markdown": "# Title\n\nContent..."}

# Option B: blocks (recommended when you need specific block types like callouts)
{"parent": ..., "properties": ..., "children": [...]}
```

If the markdown field is rejected, fall back to children blocks via PATCH after creation.

## Page URL Format

The Notion public URL for a MedSea chapter page is:
```
https://app.notion.com/p/SeaHub/Chapter-{N}-{title-slug}-{id-without-dashes}
```

For example, for Ch 10 with page ID `3835588e-846f-81a1-bd40-fbd5d564fd2e`:
```
https://app.notion.com/p/SeaHub/Chapter-10-Acute-medicine-and-critical-illness-3835588e846f81a1bd40fbd5d564fd2e
```

The `id-without-dashes` is the page UUID with hyphens removed. The slug is the chapter title in kebab-case.

This URL goes in `BUILT_CHAPTERS` in `build_site.py` so the site links work.

## API Version

Use `Notion-Version: 2022-06-28`. Do NOT use newer versions like `2025-09-03` — they have different behavior for `markdown` field and file uploads.

## Environment Variables

```bash
NOTION_API_KEY=secret_xxx  # in /root/.hermes/.env and shell env
```

The Python upload scripts use:
```python
NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
```

## Common Notion API Errors

| Code | Cause | Fix |
|------|-------|-----|
| 400 | Bad parent (e.g., workspace) | Use database_id or page_id |
| 401 | Invalid API key | Check NOTION_API_KEY |
| 403 | Rate limit / file upload throttled | Retry with backoff |
| 404 | Page not found / wrong ID | Verify page ID exists |
| 429 | Rate limit | Honor Retry-After header |
| 502/503/504 | Transient Notion outage | Retry with backoff |

## Useful API Calls

```python
# Query MedSea DB to find chapter page by name
http("POST", "/v1/databases/3805588e-846f-808b-a23b-cf63c89f372e/query",
     data={"filter": {"property": "Name", "title": {"equals": "Chapter 16: Cardiology"}}})

# Get page details
http("GET", f"/v1/pages/{page_id}")

# Get page children (with pagination)
http("GET", f"/v1/blocks/{page_id}/children?page_size=100")
# Follow next_cursor if has_more=True

# Append blocks to page
http("PATCH", f"/v1/blocks/{page_id}/children", data={"children": [...]})
```
