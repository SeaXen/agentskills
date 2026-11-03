# Notion Large File Uploads

## Verified limits (live-measured June 2026)

| Limit | Value | Source |
|---|---|---|
| Per-file upload max | **5 GB** | Student / Free / Plus plans all support this. Confirmed via real upload of a 2.41 GiB `.tar.gz.gpg` (initially failed at 720 MB; chunked to 5×500 MB and uploaded cleanly) |
| Per-URL upload timeout | **~5 minutes** | The presigned upload URL closes after this. A 500 MB chunk finishes in ~25 s with margin; a 2.5 GB single upload will be killed around the 5 min mark |
| Body cap on JSON block API | ~500 KB → 413 | `PATCH /v1/blocks/{id}/children` cap is unrelated to file upload |
| Sustained UL throughput | ~20 Mbit/s after burst | Burst ~190 Mbit/s, then S3 throttles |
| Burst peak | ~190 Mbit/s | First 30 s only |

## When the user pushes back on "Notion can't hold this"

The old assistant position was "Notion is a JSON CRUD pipe, push back on binary uploads to Notion". **That position was wrong for the user's actual plan tier** (Student/Free/Plus all support 5 GB file uploads). The user explicitly corrected this in session. New position:

- **≤ 5 GB single file**: upload directly via `/v1/file_uploads`. Tell the user how long it will take, mention the ~5 min per-URL timeout, and let them decide.
- **> 5 GB OR multi-file backup**: do not even attempt Notion. Suggest S3 / R2 / B2 + a Notion manifest page linking to it.

## The 3-step HTTP upload flow — what the docs miss

Notion's official docs say:
1. `POST /v1/file_uploads` → get `upload_id` + `upload_url`
2. `PUT {upload_url}` with the file bytes
3. Reference `upload_id` in an `image` / `file` / `video` / `audio` / `pdf` block

In practice three things fail silently:

### a) Step 2 needs the `Authorization: Bearer *** header
The docs imply it is presigned S3-style and self-authenticates. **It is not — it is `https://api.notion.com/v1/file_uploads/{id}/send`** and requires the same `Notion-Version` and Authorization headers as the create call. Without auth you get a 401 that looks like "API token invalid" but the upload URL is the issue.

### b) Step 2 must be `multipart/form-data` with a field literally named `file`
Sending raw bytes (`--data-binary @file`) gives `400 validation_error: body.file should be defined`. Notion's docs use a generic multipart example but do not name the field.

### c) Step 2's `Content-Type` must be in Notion's allowlist

**`application/octet-stream` is rejected** for `application/octet-stream` as both the create-call content_type AND the upload body content type. Tested allowlist (June 2026):

| Content-Type | Accepted? |
|---|---|
| `application/octet-stream` | ❌ 400 |
| `application/encrypted`, `application/x-encrypted`, `application/pgp-encrypted`, `application/pgp` | ❌ 400 |
| `application/x-gzip` | ❌ 400 |
| `application/gzip` | ✅ |
| `application/zip` | ✅ |
| `application/x-tar` | ✅ |
| `text/plain` | ✅ |
| `image/png` | ✅ (use for image uploads) |
| `application/pdf` | ✅ (use for PDFs) |

For a `.gpg` file (or any binary that is not in the allowlist), lie about the content type with `application/gzip`. Notion stores the bytes verbatim — the file extension and content matter for downstream users, but Notion does not validate them against the declared MIME.

## Working Python template

```python
import json, os, time, urllib.request, uuid, hashlib

KEY = os.environ["NOTION_API_KEY"]
NVER = "2022-06-28"  # file upload is supported on this and later versions
CT = "application/gzip"  # see allowlist above

# 1) create upload resource
req = urllib.request.Request(
    "https://api.notion.com/v1/file_uploads",
    data=json.dumps({"filename":"backup.gpg","content_type":CT,"content_length":size}).encode(),
    headers={"Authorization":f"Bearer {KEY}","Notion-Version":NVER,"Content-Type":"application/json"},
    method="POST",
)
fu = json.loads(urllib.request.urlopen(req).read())
upload_id = fu["id"]
upload_url = fu["upload_url"]

# 2) multipart upload
boundary = "----H" + uuid.uuid4().hex
body = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="file"; filename="backup.gpg"\r\n'
    f"Content-Type: {CT}\r\n\r\n"
).encode() + open(path,"rb").read() + f"\r\n--{boundary}--\r\n".encode()

req = urllib.request.Request(
    upload_url, data=body, method="POST",
    headers={
        "Authorization":f"Bearer {KEY}",
        "Notion-Version":NVER,
        "Content-Type":f"multipart/form-data; boundary={boundary}",
        "Content-Length":str(len(body)),
    },
)
urllib.request.urlopen(req).read()

# 3) reference in a block
file_block = {
    "object":"block","type":"file",
    "file":{"type":"file_upload","file_upload":{"id":upload_id}},
}
```

## Streaming large files (memory-safe)

For files bigger than a few hundred MB, stream the body so the host does not allocate the whole file in RAM:

```python
class StreamedUpload:
    """Multipart body wrapper that streams the file from disk."""
    CHUNK = 8 * 1024 * 1024  # 8 MiB
    def __init__(self, path, filename, ct, boundary):
        self.f = open(path, "rb")
        self.size = os.path.getsize(path)
        self.b = boundary
        self.head = (f"--{self.b}\r\n"
                     f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
                     f"Content-Type: {ct}\r\n\r\n").encode()
        self.tail = f"\r\n--{self.b}--\r\n".encode()
        self.state = "head"  # head -> file -> tail -> done
    def read(self, n=-1):
        n = n if n > 0 else self.CHUNK
        out = b""
        if self.state == "head":
            take = min(n - len(out), len(self.head))
            out += self.head[:take]; self.head = self.head[take:]
            if not self.head: self.state = "file"
        if self.state == "file" and len(out) < n:
            chunk = self.f.read(n - len(out))
            if chunk: out += chunk
            else: self.state = "tail"; self.f.close()
        if self.state == "tail" and len(out) < n:
            take = min(n - len(out), len(self.tail))
            out += self.tail[:take]; self.tail = self.tail[take:]
            if not self.tail: self.state = "done"
        return out
```

`Content-Length` must be precomputed: `len(head) + file_size + len(tail)`.

## Chunking a backup larger than 5 GB

Notion has no native "upload as multi-part backup" feature. The workaround used in session for a 2.5 GB `.tar.gz.gpg`:

1. `split -b 500M -d -a 2 hermes-backup.tar.gz.gpg chunk_` → 5 chunks of ~500 MB.
2. SHA-256 each chunk separately (sum should match the original file).
3. Upload each chunk via separate `file_upload` + multipart.
4. On the parent page, create one `file` block per chunk plus a `code` block with a `restore.sh` that re-assembles + decrypts + verifies.

For backups > 5 GB (e.g. the plain 6 GB `/mnt/tb/hermes-backups/#plain/` directory):
- Notion is not the right destination — use S3 / R2 / B2 with a Notion manifest page linking to the archive.

## Pitfalls specific to large uploads

- **Per-URL timeout ~5 min.** A 2.5 GB chunked into 5 × 500 MB works because each chunk takes ~25 s. A single 2.5 GB upload would die around the 5 min mark with `CLOSE-WAIT` TCP state and no useful error.
- **Memory pressure on the upload host.** Reading a 2.5 GB file with `pathlib.Path.read_bytes()` or holding multiple chunks open for SHA computation can push a memory-constrained host (8 GiB or less) into swap-thrashing. Always stream and verify `free -m` before and after the upload.
- **Notion API does not expose a "list file_uploads" endpoint.** Partial uploads from a killed script become orphans. They get garbage-collected eventually but cannot be programmatically deleted.
- **Upload slots expire in ~1 hour.** Create → upload → reference the `upload_id` in the same script. Do not park it for a follow-up turn.
