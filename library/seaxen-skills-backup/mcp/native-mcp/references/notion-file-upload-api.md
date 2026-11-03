# Notion File Upload API — gotchas from a real upload session

**TL;DR:** The Notion File Upload endpoint is the Notion API itself (not S3), it requires an `Authorization` header on the upload POST, body must be `multipart/form-data` with a `file` field, `content_type` is allowlisted (raw `application/octet-stream` is rejected), and per-request body cap is ~500 KB.

## The two-step flow

1. **Create the resource** — `POST /v1/file_uploads` with metadata. Returns `{id, upload_url, status: "pending"}`.
2. **Send the bytes** — `POST {upload_url}` with the file body as `multipart/form-data` with a `file` field. Returns `{status: "uploaded", file: {url, expiry_time}}`.
3. **Attach to a page** — create a `file` block referencing `file_upload: {id}`.

```python
# Step 1: create resource
fu = notion_post("/v1/file_uploads", {
    "filename": "backup.tar.gz",
    "content_type": "application/gzip",   # MUST be in Notion's allowlist
    "content_length": size,
})
# Step 2: send the file body
# Critical: upload_url is the Notion API itself, not S3. Needs Authorization.
r = urllib.request.Request(fu["upload_url"], data=multipart_body, method="POST",
    headers={
        "Authorization": "Bearer " + TOKEN,
        "Notion-Version": NOTION_VERSION,
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    })
```

## Gotcha 1 — `upload_url` requires `Authorization` header

`upload_url` looks like `https://api.notion.com/v1/file_uploads/<id>/send` — it's the Notion API, NOT a presigned S3 URL. The Authorization header is required. Without it you get `401 API token is invalid`.

Symptoms: 401 with `{"object":"error","code":"unauthorized"}` even though your token works for `/v1/users/me`.

Fix: include `Authorization: Bearer <token>` AND `Notion-Version: <date>` on the upload POST.

## Gotcha 2 — `content_type` is allowlisted

Notion rejects several common content types at upload time, including `application/octet-stream`, `application/x-encrypted`, `application/pgp-encrypted`, `application/pgp`, `application/x-gzip`.

Verified-accepted types (June 2026):
- `text/plain`
- `application/pdf`
- `image/png`
- `application/zip`
- `application/x-tar`
- `application/gzip`

For a binary `.gpg` file that doesn't match any allowlist, use `application/gzip` as a "close enough" type — Notion stores the bytes regardless and the original filename + magic bytes are what matter for the consumer.

Error symptom: `HTTP 400 validation_error: File upload has an invalid or unsupported content type of 'application/octet-stream'`.

## Gotcha 3 — Body must be `multipart/form-data` with a `file` field

Posting raw bytes (no multipart envelope) returns `HTTP 400 body.file should be defined, instead was undefined`.

A `Content-Type: application/octet-stream` body of the raw file is what some docs suggest, but at least current Notion API requires multipart. Use this envelope:

```
--BOUNDARY
Content-Disposition: form-data; name="file"; filename="your-filename.ext"
Content-Type: application/gzip

<binary bytes here>
--BOUNDARY--
```

For large files, stream the file body via a custom reader so memory stays bounded:

```python
class StreamMultipart:
    def __init__(self, path, filename, content_type, boundary):
        self.f = open(path, "rb"); self.size = os.path.getsize(path)
        self.boundary = boundary; self.filename = filename
        self.content_type = content_type
        self.header = (f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
            f'Content-Type: {content_type}\r\n\r\n').encode()
        self.footer = f'\r\n--{boundary}--\r\n'.encode()
        # ... read() returns header + file + footer
```

## Gotcha 4 — ~500 KB per-request body cap

A single PATCH/upload larger than ~500 KB returns `HTTP 413 PayloadTooLargeError: Request body too large`.

Strategy for multi-MB files: **chunk the file on disk** before uploading, send each chunk as its own `file_upload`:

```bash
split -b 500M -d -a 2 backup.tar.gz.gpg chunk_
# 5 × 500 MiB chunks for a 2.5 GiB file
```

Each chunk becomes a separate `file` block in Notion. Plus a `restore.sh` block that re-assembles and decrypts:

```bash
cat chunk_* > backup.tar.gz.gpg
gpg --output backup.tar.gz --decrypt backup.tar.gz.gpg
tar -xzf backup.tar.gz
```

## Gotcha 5 — Display speed can be misleading

When uploading via a Python `data=` argument to `urllib.request.urlopen`, the bytes may be **buffered locally** while the remote socket is in `CLOSE-WAIT`. You see "200 Mbit/s" in your progress bar but only ~720 MB ever reaches the server before Notion's socket hangs.

Detection: `ss -tnp | grep python` shows the local→remote socket state. If it's `CLOSE-WAIT` while you're still pumping bytes, the server has sent `FIN` and your local TCP buffer is just draining — not actually transmitting.

Fix: instrument I/O via `/proc/<pid>/io` (`read_bytes` from the file + `write_bytes` to the socket should match), not just the Python-side counter.

## Complete working example (small file)

```python
import os, json, uuid, urllib.request, urllib.error

NOTION_VERSION = "2022-06-28"
TOKEN = os.environ["NOTION_TOKEN"]

# Step 1
req = urllib.request.Request(
    "https://api.notion.com/v1/file_uploads",
    data=json.dumps({
        "filename": "notes.md",
        "content_type": "text/plain",
        "content_length": 42,
    }).encode(),
    headers={"Authorization": "Bearer " + TOKEN, "Notion-Version": NOTION_VERSION},
    method="POST")
fu = json.loads(urllib.request.urlopen(req).read())

# Step 2
boundary = "----" + uuid.uuid4().hex
body = (f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="notes.md"\r\n'
        f"Content-Type: text/plain\r\n\r\n"
        "Hello from Notion file upload.\n"
        f"\r\n--{boundary}--\r\n").encode()
req = urllib.request.Request(
    fu["upload_url"], data=body, method="POST",
    headers={"Authorization": "Bearer " + TOKEN, "Notion-Version": NOTION_VERSION,
             "Content-Type": f"multipart/form-data; boundary={boundary}"})
urllib.request.urlopen(req).read()

# Step 3 — attach to a parent page
req = urllib.request.Request(
    "https://api.notion.com/v1/blocks/<PARENT>/children",
    data=json.dumps({"children": [{
        "object": "block", "type": "file",
        "file": {"type": "file_upload", "file_upload": {"id": fu["id"]}}
    }]}).encode(),
    headers={"Authorization": "Bearer " + TOKEN, "Notion-Version": NOTION_VERSION,
             "Content-Type": "application/json"},
    method="PATCH")
urllib.request.urlopen(req).read()
```

## Diagnostics checklist

When a Notion file upload is failing or slow, check these in order:

1. Token works for `/v1/users/me`? (separate from upload POST)
2. `content_type` in allowlist? (try `application/gzip` for binary)
3. `Authorization` header on upload POST? (Notion's own API, not S3)
4. Body size under 500 KB? (chunk if larger)
5. Body is `multipart/form-data` with `file` field? (not raw bytes)
6. TCP socket state — `ss -tnp` should show `ESTABLISHED`, not `CLOSE-WAIT`
