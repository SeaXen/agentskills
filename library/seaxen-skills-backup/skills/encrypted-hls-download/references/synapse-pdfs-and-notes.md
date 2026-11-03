# Synapse LMS — downloading notes, PDFs, and other files

Synapse and similar LMSes (vidinfra-backed Bangladeshi medical / coaching platforms) store **non-video** content in a separate tab with a different backend. The video tab is HLS+AES-encrypted (covered by the main skill). The notes tab is **plain HTTP file downloads** — no encryption, no key server, no segments. Much simpler.

## URL pattern

The same `chapter_id` works across tabs:

| Tab | URL | Backend |
|---|---|---|
| Videos | `https://lms.synapsepg.org/videos/{chapter_id}/lecture` | HLS stream, AES-128 |
| Notes / PDFs | `https://lms.synapsepg.org/notes/{chapter_id}/lecture` | Direct file URLs |
| Live classes | `https://lms.synapsepg.org/live/{...}` | (varies) |

If you land on the wrong tab (e.g. on `/videos/{id}/lecture` looking for PDFs), the page will show "No Video Available". Navigate to `/notes/{id}/lecture` to see the PDFs.

## API endpoint (same Bearer as the video flow)

The lecture API returns BOTH `videoContents` and `fileContents` for any chapter — so a single API call tells you what's in both tabs:

```bash
sessionId=$(...extract from localStorage...)

curl -sS \
  -H "Authorization: $sessionId" \
  -H "Accept: application/json" \
  -H "Referer: https://lms.synapsepg.org/notes/{chapter_id}/lecture" \
  "https://api.synapsepg.org/api/lecture/{chapter_id}"
```

Response shape:

```json
{
  "status": "200",
  "data": {
    "_id": "6a251ab2585213c2b6778499",
    "name": "Davidson's Notes",
    "videoContents": ["..."],
    "fileContents": [
      {
        "_id": "6a33c313c488c1c2bf67bdae",
        "title": "Gastroenterology Class PDF by Dr. Rafsan",
        "key": "directory/775210851440.pdf",
        "type": "file",
        "isPublished": false,
        "isAvailable": false,
        ...
      },
      ...
    ]
  }
}
```

**The `isPublished: false` / `isAvailable: false` fields are misleading** — files are still downloadable from the CDN even when these are false. They appear to be LMS-side flags, not access-control flags. Don't filter on them; just attempt the download.

## File download

Each `fileContents[i].key` is an S3-style path. The CDN base is `https://assets.synapsepg.org/`:

```bash
curl -sS -o "Gastroenterology_Class_PDF_by_Dr._Rafsan.pdf" \
  "https://assets.synapsepg.org/directory/775210851440.pdf"
```

- **No Authorization header needed** — the CDN serves the file as a static object.
- **No Referer check** observed (unlike the HLS CDN).
- **No special User-Agent required** — a plain `curl` User-Agent works.

But add a real `User-Agent` to be safe; some CDNs block default `python-urllib` agents.

## Filename hygiene

The `title` field has characters that break filesystems (spaces, slashes, em-dashes, non-ASCII Bangla). Sanitize before writing:

```python
import re
def sanitize(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")
```

Keep the original extension from the `key` field (`.pdf`, `.pptx`, `.docx`, etc.).

## Differences from the video flow (don't conflate)

| | Videos | Notes / PDFs |
|---|---|---|
| Auth | Playwright + Bearer + signed headers | Bearer only |
| Encryption | AES-128-CBC per segment | None |
| Storage | HLS segments in `.ts` + key server | Single file on CDN |
| Per-chapter count | Usually 1-5 | Can be 10-50 |
| Need remux? | Yes (MPEG-TS → MP4) | No — files are pre-formatted |
| Need Playwright? | Yes (for key capture) | No (just a single Bearer-auth API call) |
| Approx. size | 500 MB – 2 GB each | 100 KB – 70 MB each |

## Reusable script

`scripts/download_notes.py` in this skill handles the full flow:
- Playwright login (for the Bearer token)
- API call to enumerate files
- Parallel download of all files in a chapter
- Sanitized filenames
- Per-file error handling (one bad file doesn't break the rest)
- Reports total downloaded size at the end

Usage:
```bash
/root/.venvs/synapse-env/bin/python scripts/download_notes.py <chapter_id> [output_dir]
```

Default output dir: `/mnt/tb/synapse_26/notes/` (or override).

## Why this matters: don't declare "course done" after videos

A real Synapse course (verified June 2026): 2 video lectures + 16 PDFs in the same chapter. If you only download the 2 videos, you miss 199 MB of study material. The user will (rightfully) say "there are some pdf/notes too" and you'll have to do a second pass.

**Always probe for both `videoContents` and `fileContents` on every chapter you handle.** Either by hitting the API for each chapter, or by navigating the notes tab to confirm "No Notes Available" before declaring done.

## Other platforms

The same tab-split pattern is common in other South Asian coaching LMSes. If you see a URL like `/videos/{id}` next to `/notes/{id}` or `/files/{id}`, this recipe probably applies with minimal changes — just swap the API host and CDN base.
