---
name: public-google-drive-ingest
description: "Read and mirror publicly shared Google Drive folders and Google Docs without OAuth — batch export to text/PDF for study pipelines and Medicine vault ingest."
version: 1.2.0
author: Hermes
metadata:
  hermes:
    tags: [Google, Drive, Docs, ingest, public, study, Davidson]
    related_skills: [google-workspace, markitdown-ingest, medical-fcps-mrcp-exam-notes]
---

# Public Google Drive ingest

Ingest **public** Drive links (`Anyone with the link`) without signing in or OAuth.

## When to use

- User asks to learn from / read / mirror a **public Drive folder or Doc**
- Multi-part Google Doc libraries (exam notes, shared curricula)
- Building a local mirror under `/mnt/tb/Medicine/External/...`

## When NOT to use (use `google-workspace` instead)

- Private Drive, upload, share changes, or Drive search across the user's account
- Needs Sheets API write or Gmail

## Workflow (summary)

1. Confirm public access (`browser_navigate` or `curl` → 200, list visible items).
2. Resolve **file/folder IDs** from folder HTML or `browser_console` row text (see reference).
3. Export Docs: `https://docs.google.com/document/d/{id}/export?format=txt` (normalize ids: `.split("-0-")[0].rstrip("-")`). Optional **parallel `.docx`**: `export?format=docx` beside each `.txt` when the user wants Word + text.
4. Export PDFs: `https://drive.google.com/uc?export=download&id={id}`
5. Write `INDEX.md` + `SOURCE_DRIVE.md` (canonical link + re-sync) → run batch export → `manifest.json`; pace requests on hot/weak hosts.
6. **Audit** each subfolder before claiming 100% complete (see below).
7. If user asks to **learn from** mirrored notes: scan `.txt` corpus → `AGENT_LEARNED.md` + Mnemosyne; treat as **high-yield overlay**, not a replacement for full Medicine notes.

Full steps, pitfalls, and layout: **`references/public-drive-folder-ingest.md`**. Worked multi-folder example: **`references/abdullah-tanvir-drive-mirror-2026-06-25.md`**.

## Rules

1. **Do not start OAuth setup** if the user only pasted a public link — try anonymous export first.
2. **Verify** exports (size + not HTML login page) before claiming ingest complete.
3. **Report failures per file** in manifest; partial success is honest partial success.
4. On thermally constrained servers, batch in background with delays between subfolders.

## Completion check (do not trust manifest alone)

After batch ingest, run **`scripts/audit_public_folder.py`** per subfolder (or re-list Drive in browser and compare counts). A naive HTML parser often logs **duplicate manifest rows with HTTP 404** while the **correct** doc_id export already succeeded — judge by **unique local `.txt` sizes** vs **live export probe**, not `manifest.json` fail totals.

If `drive_docs > local_unique`, find the missing title (e.g. extra doc like `CARDIOLOGY PHYSIOLOGY` beside `D / CARDIOLOGY 1–7`) and export with `scripts/export_public_doc.py --doc ID:path.txt`.

## Scripts

- `scripts/export_public_doc.py` — single-doc or small batch export from IDs (stdlib only).
- `scripts/audit_public_folder.py` — folder ID vs local dir: exportable count vs unique file sizes.