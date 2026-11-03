# Public Google Drive folder ingest (no OAuth)

Use when the user shares a **public** Drive link (`Anyone with the link`) and wants content read, summarized, or mirrored locally — especially multi-doc study libraries (e.g. Davidson review notes).

OAuth (`google-workspace` + `google_token.json`) is **not required** for this path. Prefer OAuth only when links are private, or when you need Drive API search/upload.

## Decision tree

| Situation | Approach |
|-----------|----------|
| Public **folder** with Google Docs | List items → export each doc as text (below) |
| Public **single** Google Doc | `export?format=txt` |
| Public **PDF** in Drive | `uc?export=download&id=FILE_ID` |
| Native Doc without export URL | Same export endpoint; fails → try browser or OAuth |
| Private / org-restricted | Stop; ask user to share publicly or set up OAuth |
| Large binary | May hit virus-scan HTML; try `drive.usercontent.google.com/download?id=ID&confirm=t` |

## Folder inventory (reliable order)

1. **`browser_navigate`** to the folder URL — confirm rows (names, types).
2. **`curl -sL`** the same URL with a browser `User-Agent` → save HTML.
3. **Parse file IDs** from HTML: for each visible title, search `html.find(title)` and read ±300–700 chars; extract `1[a-zA-Z0-9_-]{25,44}`; normalize with `clean_id`: `.split("-0-")[0].rstrip("-")`.
   - Only accept segments that mention `Google Docs`, `document`, or `vnd.google-apps.document` — otherwise you may pair a title with a **folder** id and get manifest 404 noise while a parallel parse already succeeded.
4. If HTML is incomplete (localized UI, lazy load), **`browser_console`** evaluate:
   ```javascript
   [...document.querySelectorAll('[role="row"]')].map(r => r.innerText.replace(/\s+/g,' ').trim())
   ```
5. Map subfolder names to folder IDs the same way (search name → nearest id).

**Pitfall:** Avoid shell `grep` patterns with escaped hostnames (`docs\.google\.com`) on hosts that flag them — use Python `re.findall` or `search_files` instead.

## Export URLs

```text
Google Doc → plain text:
https://docs.google.com/document/d/{DOC_ID}/export?format=txt

Google Doc → Word (keep alongside .txt when user wants both):
https://docs.google.com/document/d/{DOC_ID}/export?format=docx
(verify: starts with `PK`, size usually > 5 KB)

PDF / binary:
https://drive.google.com/uc?export=download&id={FILE_ID}
```

Verify export: body length > 500 bytes and not `<!DOCTYPE` HTML.

## Batch mirror layout (Medicine / MedSea)

```text
/mnt/tb/Medicine/External/<SourceName>/
  INDEX.md          # human catalog
  manifest.json     # machine catalog (paths, doc_id, status)
  <SUBFOLDER>/      # one Drive subfolder each
    *.txt
    *.docx          # optional parallel export (same basename as .txt)
  _ROOT_MISC/       # docs sitting in parent folder
  SOURCE_DRIVE.md   # canonical URL + re-sync commands (when Drive updates)
  AGENT_LEARNED.md  # optional agent digest after user asks to "learn from" mirror
```

Write **`INDEX.md` immediately** after cataloging; run batch export in **background** with `notify_on_complete` and **pace** folder fetches (`sleep 30` between subfolders on thermally constrained hosts).

## Manifest fields

Per file: `title`, `doc_id`, `path`, `bytes`, `status` (`ok` | `cached` | `not_plain_text` | error string).

## Completion audit

Do **not** declare 100% ingest from `manifest.json` fail counts alone — duplicate parser passes can log 404 for wrong ids while good exports are already on disk.

Per subfolder:

```bash
python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/public-google-drive-ingest/scripts/audit_public_folder.py \
  FOLDER_ID /mnt/tb/Medicine/External/<Source>/<SUBFOLDER>
```

Expect: `drive_docs == exportable == local_unique`. If `drive_docs > local_unique`, export the missing doc(s) with `export_public_doc.py`.

## Example catalog (Abdullah Tanvir Davidson 24th)

- Parent: `176ujvDTak-o6b6i14mYfXjrwYgBt5hFh` (`1 DAVIDSON`) — 12 specialty subfolders + `_ROOT_MISC` (chapters/pearls/PDF).
- Mirror: `/mnt/tb/Medicine/External/Abdullah-Tanvir-Davidson-Drive/` with `INDEX.md` + `manifest.json`.
- Style: `#DAVIDSON_REVIEW`, FCPS SBA/MCQ tags; Docs export as UTF-8 text (often Bengali header + English body).

## Related

- Authenticated Drive: `google-workspace` → `$GAPI drive download`
- PDF text after download: `ocr-and-documents` / `markitdown-ingest`
- FCPS note conversion: `medical-fcps-mrcp-exam-notes`