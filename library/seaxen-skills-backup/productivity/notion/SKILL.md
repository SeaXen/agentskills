---
name: notion
description: "Notion API + ntn CLI: pages, databases, markdown, Workers."
version: 2.0.0
author: community
license: MIT
platforms: [linux, macos, windows]
prerequisites:
  env_vars: [NOTION_API_KEY]
metadata:
  hermes:
    tags: [Notion, Productivity, Notes, Database, API, CLI, Workers]
    homepage: https://developers.notion.com
---

# Notion

Talk to Notion two ways. Same integration token works for both — pick by what's available.

◆ **`ntn` CLI** — Notion's official CLI. Shorter syntax, one-line file uploads, required for Workers. macOS + Linux only as of May 2026 (Windows support "coming soon"). **Default when installed.**
◆ **HTTP + curl** — works everywhere including Windows. **Default fallback** when `ntn` isn't installed.

## Setup

### 1. Get an integration token (required for both paths)

1. Create an integration at https://notion.so/my-integrations
2. Copy the API key (starts with `ntn_` or `secret_`)
3. Store in `~/.hermes/.env`:
   ```
   NOTION_API_KEY=ntn_your_key_here
   ```
4. **Share target pages/databases with the integration** in Notion: page menu `...` → `Connect to` → your integration name. Without this, the API returns 404 for that page even though it exists.

### 2. Install `ntn` (preferred path on macOS / Linux)

```bash
# Recommended
curl -fsSL https://ntn.dev | bash

# Or via npm (needs Node 22+, npm 10+)
npm install --global ntn

ntn --version    # verify
```

**Skip `ntn login` — use the integration token instead.** This works headlessly, no browser needed:
```bash
export NOTION_API_TOKEN=$NOTION_API_KEY      # ntn reads NOTION_API_TOKEN
export NOTION_KEYRING=0                       # don't try to use the OS keychain
```

Add those exports to your shell profile (or to `~/.hermes/.env`) so every session inherits them.

### 3. Choose path at runtime

```bash
if command -v ntn >/dev/null 2>&1; then
  # use ntn
else
  # fall back to curl
fi
```

Windows users: skip step 2 entirely until native `ntn` ships — Path B works fine. If you want CLI ergonomics now, install `ntn` inside WSL2.

## API Basics

`Notion-Version: 2025-09-03` is required on all HTTP requests. `ntn` handles this for you. In this version, what users call "databases" are called **data sources** in the API.

## Path A — `ntn` CLI (preferred, macOS / Linux)

### Raw API calls (shorthand for curl)
```bash
ntn api v1/users                                  # GET
ntn api v1/pages parent[page_id]=abc123 \         # POST with inline body
  properties[title][0][text][content]="Notes"
ntn api v1/pages/abc123 -X PATCH archived:=true   # PATCH; := is non-string (bool/num/null)
```

Syntax notes:
- `key=value` — string fields
- `key[nested]=value` — nested object fields
- `key:=value` — typed assignment (booleans, numbers, null, arrays)

### Search
```bash
ntn api v1/search query="page title"
```

### Read page metadata
```bash
ntn api v1/pages/{page_id}
```

### Read page as Markdown (agent-friendly)
```bash
ntn api v1/pages/{page_id}/markdown
```

### Read page content as blocks
```bash
ntn api v1/blocks/{page_id}/children
```

### Create page from Markdown
```bash
ntn api v1/pages \
  parent[page_id]=xxx \
  properties[title][0][text][content]="Notes from meeting" \
  markdown="# Agenda

- Q3 roadmap
- Hiring"
```

### Patch a page with Markdown
```bash
ntn api v1/pages/{page_id}/markdown -X PATCH \
  markdown="## Update

Shipped the prototype."
```

### Query a database (data source)
```bash
ntn api v1/data_sources/{data_source_id}/query -X POST \
  filter[property]=Status filter[select][equals]=Active
```

For complex queries with `sorts`, multiple filter clauses, or compound logic, pipe JSON in:
```bash
echo '{"filter": {"property": "Status", "select": {"equals": "Active"}}, "sorts": [{"property": "Date", "direction": "descending"}]}' | \
  ntn api v1/data_sources/{data_source_id}/query -X POST --json -
```

### File uploads (one-liner — biggest CLI win)
```bash
ntn files create < photo.png
ntn files create --external-url https://example.com/photo.png
ntn files list
```

Compare to the 3-step HTTP flow (create upload → PUT bytes → reference).

### Useful env vars
| Var | Effect |
|---|---|
| `NOTION_API_TOKEN` | Auth token (overrides keychain) — set this to your integration token |
| `NOTION_KEYRING=0` | File-based creds at `~/.config/notion/auth.json` instead of OS keychain |
| `NOTION_WORKSPACE_ID` | Skip the workspace picker prompt |

## Path B — HTTP + curl (cross-platform, default on Windows)

All requests share this pattern:

```bash
curl -s -X GET "https://api.notion.com/v1/..." \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json"
```

On Windows the `curl` shipped with Windows 10+ works as-is. PowerShell users can also use `Invoke-RestMethod`.

### Search
```bash
curl -s -X POST "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"query": "page title"}'
```

### Read page metadata
```bash
curl -s "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03"
```

### Read page as Markdown (agent-friendly)

Easier to feed to a model than block JSON.

```bash
curl -s "https://api.notion.com/v1/pages/{page_id}/markdown" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03"
```

### Read page content as blocks (when you need structure)
```bash
curl -s "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03"
```

### Create page from Markdown

`POST /v1/pages` accepts a `markdown` body param.

```bash
curl -s -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"page_id": "xxx"},
    "properties": {"title": [{"text": {"content": "Notes from meeting"}}]},
    "markdown": "# Agenda\n\n- Q3 roadmap\n- Hiring\n\n## Decisions\n- Ship MVP Friday"
  }'
```

### Patch a page with Markdown
```bash
curl -s -X PATCH "https://api.notion.com/v1/pages/{page_id}/markdown" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"markdown": "## Update\n\nShipped the prototype."}'
```

### Create page in a database (typed properties)
```bash
curl -s -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"database_id": "xxx"},
    "properties": {
      "Name": {"title": [{"text": {"content": "New Item"}}]},
      "Status": {"select": {"name": "Todo"}}
    }
  }'
```

### Query a database (data source)
```bash
curl -s -X POST "https://api.notion.com/v1/data_sources/{data_source_id}/query" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "filter": {"property": "Status", "select": {"equals": "Active"}},
    "sorts": [{"property": "Date", "direction": "descending"}]
  }'
```

### Create a database
```bash
curl -s -X POST "https://api.notion.com/v1/data_sources" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"page_id": "xxx"},
    "title": [{"text": {"content": "My Database"}}],
    "properties": {
      "Name": {"title": {}},
      "Status": {"select": {"options": [{"name": "Todo"}, {"name": "Done"}]}},
      "Date": {"date": {}}
    }
  }'
```

### Update page properties
```bash
curl -s -X PATCH "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"properties": {"Status": {"select": {"name": "Done"}}}}'
```

### Append blocks to a page
```bash
curl -s -X PATCH "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{
    "children": [
      {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": "Hello from Hermes!"}}]}}
    ]
  }'
```

### File uploads (3-step flow)

Step 1 and 3 are JSON. Step 2 is the gotcha — see "File uploads — the docs are wrong about the 3-step flow" in Pitfalls below for the full multipart pattern.

```bash
# 1. Create upload slot
curl -s -X POST "https://api.notion.com/v1/file_uploads" \
  -H "Authorization: Bearer [YOUR_NOTION_TOKEN]" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json" \
  -d '{"filename": "photo.png", "content_type": "image/png"}'
# -> returns { "id": "<upload_id>", "upload_url": "https://api.notion.com/v1/file_uploads/<id>/send" }

# 2. POST bytes to upload_url as multipart/form-data with field "file".
#    The Notion-Version header is REQUIRED on this request. The 3-step docs
#    in the API reference omit that and use --data-binary, which gives
#    "body.file should be defined". See Pitfalls for the working pattern.

# 3. Reference {upload_id} in a block, e.g. an image block:
#    {"type":"image","image":{"type":"file_upload","file_upload":{"id":"<upload_id>"}}}
```

Upload slots expire 1 hour after creation — create, upload, and reference the `upload_id` in the same session. Don't park it for a follow-up turn.

## Property Types

Common property formats for database items:

- **Title:** `{"title": [{"text": {"content": "..."}}]}`
- **Rich text:** `{"rich_text": [{"text": {"content": "..."}}]}`
- **Select:** `{"select": {"name": "Option"}}`
- **Multi-select:** `{"multi_select": [{"name": "A"}, {"name": "B"}]}`
- **Date:** `{"date": {"start": "2026-01-15", "end": "2026-01-16"}}`
- **Checkbox:** `{"checkbox": true}`
- **Number:** `{"number": 42}`
- **URL:** `{"url": "https://..."}`
- **Email:** `{"email": "user@example.com"}`
- **Relation:** `{"relation": [{"id": "page_id"}]}`

## API Version 2025-09-03 — Databases vs Data Sources

- **Databases became data sources.** Use `/data_sources/` endpoints for queries and retrieval.
- **Two IDs per database:** `database_id` and `data_source_id`.
  - `database_id` when creating pages: `parent: {"database_id": "..."}`
  - `data_source_id` when querying: `POST /v1/data_sources/{id}/query`
- Search returns databases as `"object": "data_source"` with the `data_source_id` field.

## Notion Workers (advanced, requires `ntn`)

Workers are TypeScript programs Notion hosts for you. One worker can expose any combination of:
- **Syncs** — pull data from external APIs into a Notion database on a schedule (default 30 min).
- **Tools** — appear as callable tools inside Notion's Custom Agents.
- **Webhooks** — receive HTTP events from external services (GitHub, Stripe, etc.) and act in Notion.

**Plan / platform gating:**
- CLI works on all plans. **Deploying Workers requires Business or Enterprise.**
- `ntn` is macOS/Linux only as of May 2026. Windows users need WSL2 or to wait for native support.
- Free through August 11, 2026; metered on Notion credits after.

### Minimal Worker

```bash
ntn workers new my-worker      # scaffold
cd my-worker
# Edit src/index.ts
ntn workers deploy --name my-worker
```

`src/index.ts`:
```typescript
import { Worker } from "@notionhq/workers";

const worker = new Worker();
export default worker;

worker.tool("greet", {
  title: "Greet a User",
  description: "Returns a friendly greeting",
  inputSchema: { type: "object", properties: { name: { type: "string" } }, required: ["name"] },
  execute: async ({ name }) => `Hello, ${name}!`,
});
```

### Webhook capability

```typescript
worker.webhook("onGithubPush", {
  title: "GitHub Push Handler",
  execute: async (events, { notion }) => {
    for (const event of events) {
      // event.body, event.rawBody (for signature verification), event.headers
      console.log("got delivery", event.deliveryId);
    }
  },
});
```

After deploy: `ntn workers webhooks list` shows the URL Notion generates. Treat that URL as a secret — anyone with it can POST events unless you add signature verification.

### Worker lifecycle commands

```bash
ntn workers deploy
ntn workers list
ntn workers exec <capability-key> -d '{"name": "world"}'
ntn workers sync trigger <key>            # run a sync now
ntn workers sync pause <key>
ntn workers env set GITHUB_WEBHOOK_SECRET=...
ntn workers runs list                     # recent invocations
ntn workers runs logs <run-id>
ntn workers webhooks list
```

When asked to build a Worker, scaffold with `ntn workers new`, write the code in `src/index.ts`, set any secrets with `ntn workers env set`, and deploy. Notion's docs at https://developers.notion.com/workers cover the full API surface.

## Notion-Flavored Markdown (used by `/markdown` endpoints)

Standard CommonMark plus XML-like tags for Notion-specific blocks. Use **tabs** for indentation.

**Blocks beyond CommonMark:**
```
<callout icon="🎯" color="blue_bg">
	Ship the MVP by **Friday**.
</callout>

<details color="gray">
<summary>Toggle title</summary>
	Children indented one tab
</details>

<columns>
	<column>Left side</column>
	<column>Right side</column>
</columns>

<table_of_contents color="gray"/>
```

**Inline:**
- Mentions: `<mention-user url="..."/>`, `<mention-page url="...">Title</mention-page>`, `<mention-date start="2026-05-15"/>`
- Underline: `<span underline="true">text</span>`
- Color: `<span color="blue">text</span>` or block-level `{color="blue"}` on the first line
- Math: inline `$x^2$`, block `$$ ... $$`
- Citations: `[^https://example.com]`

**Colors:** `gray brown orange yellow green blue purple pink red`, plus `*_background` variants for backgrounds (`gray_background`, `blue_background`, etc. — **not** `*_bg`; the API rejects `gray_bg` / `blue_bg` with a `validation_error`).

Headings 5/6 collapse to H4. Multiple `>` lines render as separate quote blocks — use `<br>` inside a single `>` for multi-line quotes.

## Choosing the Right Path

| Task | mac / Linux | Windows |
|---|---|---|
| Read/write pages, search, query databases | `ntn api ...` | curl |
| Read a page for an agent to summarize | `ntn api v1/pages/{id}/markdown` | curl `/markdown` endpoint |
| Upload a file | `ntn files create < file` | 3-step HTTP flow |
| One-off API exploration | `ntn api ...` | curl |
| Build a sync / webhook / agent tool hosted by Notion | `ntn workers ...` | WSL2 + `ntn workers ...` |

## Measured API limits and performance (live-measured June 2026)

Numbers from a real `api.notion.com` probe — treat them as ballpark, Notion doesn't publish exact limits and they shift silently:

| Limit / metric | Measured value | Source |
|---|---|---|
| **Per-request body cap** | **~500 KB → HTTP 413 `PayloadTooLargeError`** | `PATCH /v1/blocks/{id}/children` with 100 blocks × 8 KB = 668 KB request → 413. 100 blocks × 5 KB = 338 KB → 200. Cap sits between. Safe budget: **≤ ~300 KB / request**. |
| Max blocks per `PATCH /v1/blocks/{id}/children` | 100 | Public docs + 200 above that |
| Max chars per `rich_text` segment | 2000 | Public docs; split longer strings across multiple segments or blocks |
| UL throughput (sustained, request-only) | **~1 Mbit/s (~120 KiB/s)** | 1.35 MB over 4 sequential PATCHes = 11.2 s wall |
| UL throughput (single PATCH, ~500 KB) | ~6 Mbit/s (~780 KiB/s combined wire) | 478 KB request in 1.85 s |
| DL throughput | **~12 Mbit/s (~1.45 MiB/s)** | 1.18 MB read in 0.82 s |
| Per-request server processing floor | **~2.5 s** for writes | Even a 100 KB PATCH takes ~1.9 s; ~independent of payload size below cap |
| Latency: TCP + TLS handshake | ~58 ms | One-time per connection |
| ICMP ping (`api.notion.com`) | ~3 ms | Datacenter-to-datacenter routing |

**Implication:** Notion's API is a JSON CRUD pipe optimized for interactive use, not bulk transfer. Below the body cap, **server processing time dominates**, not bandwidth. To upload 1 MB you need ~3 sequential PATCHes → ~7-8 s. To upload 100 MB you're looking at ~15 minutes and you'll be nowhere near the API rate limit (~3 req/s) — the per-request latency is your real ceiling.

Reproduction recipes + raw measurement logs: `references/api-limits.md`. Reusable manifest-page builder: `scripts/build_manifest.py`. **Large file uploads (5 GB cap, 3-step HTTP flow, content-type allowlist, chunking pattern)**: `references/file-uploads-large-files.md`.

## Notion is not a file vault — push back on large binary uploads

If the user asks to "upload my backup / VM image / video / dataset to Notion", **don't just do it**. The math:

- A 2.5 GB `.tar.gz.gpg` after base64 → ~3.3 GB ASCII → ~1.7 M Notion blocks → ~17,000 PATCH requests → **~12 hours of API calls**, blowing through the workspace block-count cap (Notion Free ~100K blocks, Plus ~1 M).
- A 6 GB directory tree is the same problem × 2.4, plus Notion pages don't have a meaningful "file tree" concept.
- Even if it finishes, **you can't reliably reconstruct the bytes** from a Notion page — and you've filled the workspace with junk blocks.

**Push-back workflow that works:**

1. State the size in concrete numbers (GB, not "large").
2. Show the math (blocks, requests, hours, caps).
3. Offer 2-3 sensible alternatives via `clarify`:
   - **Manifest page** — single page with filename, size, SHA-256, mtime, top-level listing, top-N largest files. ~2-50 KB upload, near-instant, useful for tracking. Reusable template: `scripts/build_manifest.py`.
   - **Upload just the readable parts** — text files, configs, key documents. Skip binaries.
   - **Use a real object store** — S3/R2/B2 + Notion page with the link + checksums. This is what you actually want for offsite backup.
4. Wait for the user to pick. Most often they wanted a manifest or a real backup destination; Notion was a confused default.

This is a first-class skill signal: **a request that doesn't fit the tool deserves a measured refusal with alternatives, not silent multi-hour execution**.

## Pitfalls

### `markdown` body field and `children` are mutually exclusive in the same `POST /v1/pages` call

`POST /v1/pages` accepts either a `markdown` body parameter OR a `children` block array — **not both** in the same call. Combining them returns:

```json
{"object":"error","status":400,"code":"validation_error",
 "message":"Cannot specify 'markdown' together with 'content' or 'children'. Use one content format per request."}
```

**Working pattern** — send `markdown` in the create call, then PATCH to append any extra blocks:

```python
# 1) Create the page with markdown body
payload = {
    "parent": {"page_id": hub_id},
    "properties": {"title": [{"text": {"content": "16.1.25 Atherosclerosis"}}]},
    "markdown": md_content,            # auto-converts to blocks
}
req = urllib.request.Request(
    "https://api.notion.com/v1/pages",
    data=json.dumps(payload).encode(),
    headers={"Authorization": f"Bearer {api_key}", "Notion-Version": "2022-06-28",
             "Content-Type": "application/json"},
    method="POST")
page = json.loads(urllib.request.urlopen(req).read())
page_id = page["id"]

# 2) PATCH to append any extra blocks (callout header, image, divider)
extras = [{"object": "block", "type": "callout", "callout": {
    "rich_text": [{"type": "text", "text": {"content": "Sea Knowledge full study note"}}],
    "icon": {"type": "emoji", "emoji": "🫀"},
    "color": "red_background"
}}]
req = urllib.request.Request(
    f"https://api.notion.com/v1/blocks/{page_id}/children",
    data=json.dumps({"children": extras}).encode(),
    headers={"Authorization": f"Bearer {api_key}", "Notion-Version": "2022-06-28",
             "Content-Type": "application/json"},
    method="PATCH")
urllib.request.urlopen(req).read()
```

Page is created with the markdown body; appended blocks land at the end (the append-only API has no `position: 0`; see below). For bulk uploads of hundreds of pages, this two-step pattern is **much faster** than building blocks by hand and is the pattern used in MedSea's `scripts/notion_sync_cardiology.py`. Validated 2026-06-20 on 899 Ch 16 cardiology topics, 0 failures.

### Bash + curl + multi-line JSON + masked API keys is fragile

When the Notion API key is stored in an env file (e.g. `/mnt/tb/hermes/.env`) and pulled in via `source`, building a Notion write call in a bash heredoc/inline string can hit:

- **"URL rejected: Malformed input to a URL function"** — bash parsing the `Authorization: Bearer ...` header or `https://...` URL inside a here-string
- **401 "API token is invalid"** when the env var expansion silently failed (the curl ran with an empty/wrong bearer)
- **python `-c` multi-line block syntax errors** from unescaped quotes/Bangla text in a single `-c` argument

**Reliable workaround — drive the whole request from Python `urllib`:**
```python
import json, os, urllib.request

api_key = os.environ['NOTION_API_KEY']   # must be sourced first
with open('/tmp/payload.json') as f:
    payload = json.load(f)

req = urllib.request.Request(
    "https://api.notion.com/v1/pages",
    data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": "2025-09-03",
        "Content-Type": "application/json",
    },
    method="POST",
)
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
```
No shell-quoting, no masked tokens leaking into `curl --data-binary @file`, and Unicode (Bangla, Arabic, etc.) is preserved by `ensure_ascii=False`. Reach for this when the request body contains non-ASCII or multi-line strings.

### Verify after write — read back via `/markdown`

After `POST /v1/pages` (or `PATCH /v1/pages/{id}/markdown`), confirm the content actually landed by reading it back:
```bash
GET https://api.notion.com/v1/pages/{id}/markdown
```
The response body has a `markdown` field you can grep for expected substrings. Don't trust a successful POST status code alone — Notion's `markdown` body field silently drops unsupported tags and you only notice when the user opens the page.

### File uploads — the docs are wrong about the 3-step flow

The skill body above shows `curl -s -X PUT "{upload_url}" --data-binary @photo.png` for step 2. That fails in practice. Two things the docs don't tell you:

1. **The `Notion-Version` header is required on the upload URL too**, not just on the create-upload call. Without it you get `400 missing_version` and the docs blame "malformed headers".
2. **The upload body must be `multipart/form-data` with a field literally named `file`** — *not* raw bytes. Sending raw PNG bytes gives `400 body.file should be defined`.

Working Python pattern:

```python
import json, os, urllib.request, uuid

KEY = os.environ['NOTION_API_KEY']
img_path = '/path/to/photo.png'
img_bytes = open(img_path, 'rb').read()

# 1) Create the upload slot
req = urllib.request.Request(
    "https://api.notion.com/v1/file_uploads",
    data=json.dumps({"filename": "photo.png", "content_type": "image/png"}).encode(),
    headers={"Authorization": f"Bearer {KEY}",
             "Notion-Version": "2025-09-03",
             "Content-Type": "application/json"},
    method="POST",
)
upload_info = json.loads(urllib.request.urlopen(req).read())
upload_url = upload_info["upload_url"]
upload_id  = upload_info["id"]

# 2) Multipart POST the bytes to upload_url
boundary = uuid.uuid4().hex
body = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="file"; filename="photo.png"\r\n'
    f"Content-Type: image/png\r\n\r\n"
).encode() + img_bytes + f"\r\n--{boundary}--\r\n".encode()

req = urllib.request.Request(
    upload_url, data=body, method="POST",
    headers={"Authorization": f"Bearer {KEY}",
             "Notion-Version": "2025-09-03",
             "Content-Type": f"multipart/form-data; boundary={boundary}"},
)
urllib.request.urlopen(req).read()   # status should now be "uploaded"

# 3) Reference upload_id in an image block
image_block = {
    "object": "block", "type": "image",
    "image": {"type": "file_upload", "file_upload": {"id": upload_id}},
}
```

Upload slots expire in 1 hour; create → upload → reference in the same session, don't park the `upload_id` for a follow-up turn.

### Per-request body cap ~500 KB → HTTP 413

`PATCH /v1/blocks/{id}/children` and `POST /v1/pages` both reject request bodies between roughly 500 KB and 1.9 MB with:

```json
{"object":"error","code":413,"name":"PayloadTooLargeError","message":"Request body too large."}
```

The exact threshold is undocumented and not the same as `rich_text` 2000-char limit or the 100-block-per-call cap — it's a flat byte cap on the JSON body after serialization.

**Workarounds:**

- **Batch below the cap** — keep each PATCH ≤ ~300 KB to leave margin. For 100 blocks that's ~3 KB/block.
- **Split large block payloads** — instead of one paragraph with a 100 KB string, split into multiple shorter blocks.
- **Use the `markdown` body field** — `POST /v1/pages` accepts `"markdown": "..."` and Notion handles long strings internally; this is the easiest escape hatch for "one giant text blob" uploads.
- **For real bulk data, stop using Notion** — see "Notion is not a file vault" above.

Diagnose by `print(len(json.dumps(body).encode()))` before sending. If it's over 300 KB, split.

### `rich_text` content field has a 2000-char hard cap

Each item in a `rich_text` array (per block, per property) is limited to **2000 characters** in its `text.content` field. Longer → HTTP 400 `validation_error: body.children[N].paragraph.rich_text[0].text.content should be ≤ 2000 characters`.

**Workarounds:**

- **Split into multiple `rich_text` segments** within the same block. They're rendered contiguously, so visually identical to one long string.
- **Split into multiple blocks** for very long content.
- **For Python builders**, the safe pre-flight check:
  ```python
  def rt(text, cap=1900):
      if len(text) > cap: text = text[:cap-3] + "..."
      return [{"type":"text","text":{"content":text}}]
  ```
  Keep 1900 as the working limit (with 100-char headroom for safety after JSON escaping).

### Rate limit is ~3 req/s *average* — but per-request latency is the real ceiling

Public docs say ~3 req/s. In practice the **2-3 second per-request server processing** dominates long before rate limits kick in. Don't fan out 50 parallel requests — Notion will rate-limit you AND each request still takes 2-3 s server-side. For bulk uploads, sequential is fine; for reads of a paginated endpoint, sequential with `start_cursor` is the official pattern.

### `POST /v1/pages` with `parent: page_id` auto-adds a `child_page` block

When you create a new page via `POST /v1/pages` with `parent: {"page_id": "X"}`, the parent page **automatically** gets a `child_page` block pointing at your new page. If you then also `PATCH /v1/blocks/{X}/children` to add a `link_to_page` block for the same page, you'll see it listed twice on the parent.

If the user's "hub" page is already auto-listing sub-pages as `child_page` entries (most Notion pages do this), **don't** also add a manual `link_to_page` — pick one. For consistent ordering with other entries, the manual approach is sometimes still wanted, but you'll need to either:

- Delete the auto-generated `child_page` block after creation (it has its own block id you can find via `GET /v1/blocks/{X}/children`), or
- Skip the manual block entirely and let the auto-`child_page` entry appear wherever Notion places it (usually at the bottom).

### Appending blocks always puts them at the end

`PATCH /v1/blocks/{id}/children` has an optional `after` parameter, but no `before` / `position: 0`. You can't insert a new block above the first existing block in one call — workarounds:

- For "image at the top of the page": append the image block, then tell the user to drag it. (Notion's drag-to-reorder is the only path.)
- For programmatic reordering: fetch the existing first child, then `PATCH` the new children with `after` set to a placeholder — actually not supported. Real solution: re-create the page if order matters.

Acceptable workflow: append the image at the end and document the position in the page intro so the user knows where to find it.

### You cannot reparent a page that exists as a `child_page` block

If a page appears as a `child_page` block on a parent (which happens automatically when you `POST /v1/pages` with `parent: {page_id: X}`), the API **does not let you move it** to a different parent via `PATCH /v1/pages/{id}` with a new `parent`. The PATCH returns 200 OK, but the page's parent on subsequent GETs is unchanged.

**What doesn't work (verified June 2026):**
- `PATCH /v1/pages/{id}` with `{"parent": {"page_id": "new_id"}}` — returns 200, parent unchanged
- `PATCH /v1/pages/{id}` with `{"parent": {"database_id": "new_id"}}` — returns 200, parent unchanged
- `POST /v1/pages/{id}/move` — endpoint does not exist

**What works:**
- **`PATCH /v1/blocks/{old_parent_id}/children`** to **DELETE the `child_page` block** (each `child_page` block has its own block id retrievable via `GET /v1/blocks/{old_parent_id}/children`), then **recreate the page** with `POST /v1/pages` + the new parent + the `markdown` body. This loses the page id and breaks any existing links/mentions.
- For a page in a **database** (parent is a `database_id`): the database row's properties can be edited freely, but the row itself is locked to that database. To "move" it: create a new row in the target database with the same properties, then delete the original.
- For a page that was **manually created** (not via API) and is just a regular page (not a `child_page` of a database row), `PATCH /v1/pages/{id}` with a new `page_id` parent **does** work. The limitation is specifically about `child_page` blocks created by the API auto-add mechanism.

**Workaround for "move all sub-pages too"**: the user wanted the cardiology hub moved from page A to page B, with all 17 sub-hubs and 330 disease sub-pages reparented under B. The top-level move returned 200 but did nothing. The sub-pages were never going to be reparentable in a single call. The pragmatic answer: **add a redirect callout at the top of the OLD page** (`<callout>...moved to [NEW_URL]...</callout>`) and let the user re-create or drag sub-pages manually via the Notion UI. This is a real API limitation, not a bug — the only "fix" is Notion adding a `move` endpoint.

**Verify the move actually happened** — never trust a 200 OK from a PATCH that includes a `parent` field. Always `GET /v1/pages/{id}` after and check the `parent` field of the response matches what you intended.

### Callout / column / details colors use full `_background` suffix

`color: "gray_bg"` → `400 validation_error: body.children[N].callout.color should be ... "gray_background", "blue_background", ...`. The full set of valid colors (verify against current API docs — this list can change):

```
default, gray, brown, orange, yellow, green, blue, purple, pink, red,
default_background, gray_background, brown_background, orange_background,
yellow_background, green_background, blue_background, purple_background,
pink_background, red_background
```

Notion-flavored Markdown in the `markdown` body field accepts the short `_bg` form (e.g. `<callout color="red_bg">`) — but the JSON blocks API requires the full `_background` form. If you author content via the markdown field, callouts render fine; if you build the same callout as a JSON block, use the long form.

### Build a study hub with a numbered index (validated June 2026)

Pattern for "create N sub-pages under a hub and add a clickable numbered index to the hub" — used for the Davidson Chapter 16 cardiology hub, 16 sub-pages, ~5 min end-to-end.

1. **Create each sub-page** with `POST /v1/pages` + `parent: {page_id: HUB_ID}` + `markdown` body. The hub will auto-get a `child_page` block for each one. **Do not** also add a manual `link_to_page` block — it duplicates. (See the `child_page` auto-addition pitfall above.)

2. **Build the numbered index** as `numbered_list_item` blocks where each item's rich_text includes a `mention` of the sub-page. This is the cleanest clickable index — the mentions render as inline page links in the Notion UI:

```json
{
  "object": "block",
  "type": "numbered_list_item",
  "numbered_list_item": {
    "rich_text": [
      {"type": "mention", "mention": {"type": "page", "page": {"id": "<sub_page_id>"}}},
      {"type": "text", "text": {"content": "  —  short description"}}
    ]
  }
}
```

3. **Append the numbered index** to the hub via `PATCH /v1/blocks/{HUB_ID}/children`. Use batches of ~16 to stay under the 100-block-per-call cap.

4. **Optional cleanup**: if you also want to add a callout header or divider at the *top* of the hub, append it now — but the append-only API means the new blocks go to the **end**, not the top. Either:
   - Accept the layout (callout/index/auto-child-pages, in that order), or
   - Delete the auto-added `child_page` blocks (find them with `GET /v1/blocks/{HUB_ID}/children`, filter on `type: "child_page"`, then `DELETE`) before adding the index, so the index becomes the hub's primary content. The sub-pages still exist; only their auto-entries on the hub are removed.

The deletion path is the cleaner UX (no duplicate "16 sub-pages" twice on the hub), and is the approach the cardiology hub used.

### Verify image + content landed by reading the page back via `/markdown`

For pages created with the `markdown` field, `GET /v1/blocks/{id}/children` may return 404 (the new page's child blocks are indexed under a delayed async job in some cases) — but `GET /v1/pages/{id}/markdown` always returns the full content including embedded image references as signed S3 URLs. Use `/markdown` for verification:

```python
s, data = call("GET", f"/pages/{page_id}/markdown")
md = data["markdown"]
# Spot-checks
assert len(md) > 5000, f"page too small: {len(md)} chars"
assert "X-Amz-Signature" in md, "image not embedded"
import re
h2_count = len(re.findall(r"^## \d+\.", md, re.M))
assert h2_count >= 8, f"only {h2_count} H2 sections found"
```

This is more reliable than the block-children endpoint for fresh pages created via the `markdown` field.

## Notes

- See `references/mcp-troubleshooting.md` for a quick workflow to separate standard Notion API readiness from Hermes Notion MCP readiness when a user says "it was already connected".
- Page/database IDs are UUIDs (with or without dashes — both accepted).
- Rate limit: ~3 requests/second average. The CLI doesn't bypass this.
- The API cannot set database **view** filters — that's UI-only.
- Use `"is_inline": true` when creating data sources to embed them in a page.
- Always pass `-s` to curl to suppress progress bars (cleaner agent output).
- Pipe JSON through `jq` when reading: `... | jq '.results[0].properties'`.
- Notion also ships an MCP server now (`Notion MCP`, ~91% more token-efficient on DB ops than the previous version) — wire it via Hermes' MCP support if you want streaming Notion access from inside a session, but the paths above are enough for most one-shot tasks.

## Host-specific credential notes (June 2026)

- `NOTION_API_KEY` / `NOTION_API_TOKEN` not in shell env by default — must be sourced from Bitwarden
- Bitwarden Secrets Manager (BWS) token (`BWS_ACCESS_TOKEN`) is present but only works with `bws` CLI, not the regular `bw` CLI
  - Regular `bw` login `--apikey` expects a vault API key (client_id + client_secret), not a BWS token
  - `bws` CLI not installed on this host; install from GitHub releases if needed: https://github.com/bitwarden/sdk-sm/releases
- MCP Notion script (`/mnt/tb/hermes/scripts/mcp-notion.sh`) reads `NOTION_TOKEN` from env var (Bitwarden-injected) with fallback to `/mnt/tb/hermes/.env`
  - Verified June 2026: `/mnt/tb/hermes/.env` contains a working `NOTION_TOKEN` (50-char integration token, `ntn_...` format). The line `NOTION_API_KEY=` may also be present as an alias. `source /mnt/tb/hermes/.env` then export `NOTION_TOKEN` (or `NOTION_API_KEY`) and you can POST to `api.notion.com` directly without further setup.
  - The `Notion-Version` header in this environment is `2022-06-28` (the older stable API). Both versions accept basic page/block CRUD — the 2025-09-03 split between `database_id` / `data_source_id` is the main behavior change.
- For one-shot page creation, simplest path: ask user to paste the integration token (`ntn_...` or `secret_...`) and target parent page ID, then use curl/ntn directly
