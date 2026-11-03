# Notion Patterns — MedSea Database

Validated Notion API patterns for the MedSea database (`3805588e-846f-808b-a23b-cf63c89f372e`). Read this before uploading or reparenting chapter pages.

## Database Identity

- **Database ID:** `3805588e-846f-808b-a23b-cf63c89f372e` (MedSea, holds all 32 chapter pages + extras)
- **Title property name:** `Name` (NOT `title`) — type `title`
- **Working API version:** `Notion-Version: 2022-06-28`. The newer `2025-09-03` version changes parent semantics for databases and breaks the patterns below.

## Chapter Page Creation

Always set `parent: {type: database_id, database_id: <db>}` and the `Name` property:

```python
payload = {
    "parent": {"type": "database_id", "database_id": MEDSEA_DB},
    "properties": {
        "Name": {"title": [{"type": "text", "text": {"content": f"Chapter {N}: {Title}"}}]},
    },
}
```

`parent: {type: workspace, workspace: True}` is REJECTED by the API. `parent: {type: page_id}` is for child-pages of an existing page, not for adding a row to a database.

## Search-Existing Before Create (Pitfall — Duplicate Pages)

The MedSea DB has accumulated duplicates from the 24th→25th Ed renumbering. As of 2026-06-19:
- Ch 10 has 2 pages: "Acute Medicine and Critical Illness" (NEW) + "Acute medicine and critical illness" (OLD 24th)
- Ch 12 has 2 pages: "Envenomation" (NEW 25th) + "HIV infection and AIDS" (OLD 24th — this was Ch 12 in 24th)
- Ch 26 has 2 pages: "Dermatology" (OLD 24th) + "Stroke medicine" (OLD 24th) — both stale

**Always search the DB before creating a new chapter root page.** Use database query with title-equals filter:

```python
r = http("POST", f"https://api.notion.com/v1/databases/{MEDSEA_DB}/query",
         data={"filter": {"property": "Name", "title": {"equals": f"Chapter {N}: {Title}"}}})
if r.get("results"):
    return r["results"][0]["id"]  # reuse existing
```

Without this, every retry creates a duplicate. The duplicate pages don't break the API but clutter the DB and confuse the user.

## Public Notion URL (for website integration)

Once a page is shared to the public web, its public URL follows the format:

```
https://medsea.notion.site/Chapter-{N}-{Title-with-hyphens}-{ID-no-dashes}
```

Title segments use hyphens, no spaces, no commas, no apostrophes. The ID is the 32-char hex (UUID without dashes).

Example: page ID `8baa010d-9cc9-4c48-8261-36417d383973` (Ch 16 Cardiology) becomes:

```
https://medsea.notion.site/Chapter-16-Cardiology-8baa010d9cc94c48826136417d383973
```

The `medsea.notion.site` form is the custom-domain mirror; `www.notion.so/...` and `app.notion.com/p/...` are all equivalent. Verified HTTP 200 on multiple chapters.

**For the MedSea site `BUILT_CHAPTERS` dict:** use the public `medsea.notion.site` URL (not the internal `app.notion.com/p/SeaHub/...` URL). The internal form requires the user to be logged in to the Notion workspace.

## Page Exists vs Page Has Content (Verification Trap)

**Hit hard on 2026-06-20.** `GET /v1/pages/{chapter_id}` returns 200 with full metadata even if the page has zero content blocks. The user asked "is Notion fully synced?" and I had to discover — by querying the database AND walking all `blocks/{id}/children` recursively — that every chapter page was an empty stub (36 chapter pages, 0 topic sub-pages).

**The right way to verify Notion content depth:**

```python
# Step 1: Query the database for chapter pages (proves they exist in DB)
db_result = notion_post(f"/databases/{MEDSEA_DB}/query", {"page_size": 100})
chapter_pages = db_result.get("results", [])
print(f"Chapter pages in DB: {len(chapter_pages)}")

# Step 2: For each chapter, walk blocks/{chapter_id}/children paginated
# Topic sub-pages are represented as child_page blocks
def count_child_pages(page_id):
    total = 0
    cursor = None
    while True:
        path = f"/blocks/{page_id}/children?page_size=100"
        if cursor: path += f"&start_cursor={cursor}"
        children = notion_get(path)
        if "results" not in children: break
        total += sum(1 for b in children["results"] if b.get("type") == "child_page")
        if not children.get("has_more"): break
        cursor = children.get("next_cursor")
    return total

for page in chapter_pages:
    n = count_child_pages(page["id"])
    print(f"  - {page_title}: {n} child pages")
```

**Signals of "page exists but is a stub":**
- `GET /v1/pages/{id}` succeeds → page exists
- `POST /v1/databases/{db}/query` returns the row → it's in the DB
- `GET /v1/blocks/{id}/children` returns `{"results": [], "has_more": false}` → 0 child_pages = empty
- Last-modified time is from the initial stub creation, not the recent sync → confirms no real upload

**The mistake to avoid:** Trusting a successful Notion-Version 2022-06-28 chapter-page-create call as proof the chapter is "synced". A chapter page is just a container — the topic sub-pages and content blocks are what users see.

A self-contained verification script that runs all 6 checks (local + chapters + site + docker live + notion + git) is in `scripts/verify_all_targets.py` — run it after every sync.

## File Uploads — 3-Step Pattern (validated 2026-06-19)

```python
# Step 1: create upload metadata
create = http("POST", "https://api.notion.com/v1/file_uploads",
              data={"filename": path.name, "content_type": "image/png",
                    "content_length": path.stat().st_size})
upload_id = create["id"]
upload_url = create.get("upload_url") or f"https://api.notion.com/v1/file_uploads/{upload_id}/send"

# Step 2: POST multipart (boundary required, 'file' part required)
boundary = f"----NotionBoundary{uuid.uuid4().hex}"
with open(path, "rb") as f: fb = f.read()
body = (f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n").encode() + fb + f"\r\n--{boundary}--\r\n".encode()
req = urllib.request.Request(upload_url, data=body, method="POST",
    headers={"Authorization": f"Bearer {KEY}", "Notion-Version": "2022-06-28",
             "Content-Type": f"multipart/form-data; boundary={boundary}"})

# Step 3: use upload_id in an image block
image_block = {"type": "image", "image": {"type": "file_upload", "file_upload": {"id": upload_id}}}
```

### 403 Rate-Limit Retry + Skip-On-Fail

`file_uploads` endpoint returns 403 transiently on heavy load. Pattern:
- Retry 5× with exponential backoff (1s, 2s, 4s, 8s, 16s)
- If still failing after retries, **skip the image** and create the page with a yellow-background "Image upload pending retry" callout block instead. Don't fail the whole chapter upload.

## child_page Reparent — API Limitation

`PATCH /v1/pages/{id}` with a new `parent: {page_id: ...}` returns HTTP 200 for top-level pages BUT silently does nothing for `child_page` blocks (which are how Notion represents sub-pages inside a parent page). This was hit on the cardiology move (2026-06-19): the top-level Cardiology page moved successfully, but the 17 hub pages and 330 topic sub-pages stayed on the old parent.

**Workarounds:**
- Add a redirect callout block at the top of the old page: "This chapter has moved to [new URL]"
- For full migration: re-upload topics to the new root (existing `upload_chapter.py` skips existing children, so this re-attaches them via the database-child pattern)
- Notion's drag-and-drop in the UI moves child_page blocks correctly; only the API is limited

## Common Failure Modes

| Symptom | Cause | Fix |
|---------|-------|-----|
| `validation_error: parent.type should be either 'page_id' or 'database_id'` | Used `workspace` parent | Use `database_id` for DB rows, `page_id` for child pages |
| New chapter page created, but it has no children | Created with `page_id` parent instead of `database_id` | Re-create with `database_id` parent; archive the old one |
| `403 Forbidden` on file_uploads | Rate limit | Retry with backoff, then skip-on-fail |
| PATCH reparent returns 200 but child_pages don't move | API limitation | Use UI drag-drop OR redirect callout on old page |
| Duplicate chapter pages after retry | No search-existing check | Always query DB for `Chapter N: Title` before create |
