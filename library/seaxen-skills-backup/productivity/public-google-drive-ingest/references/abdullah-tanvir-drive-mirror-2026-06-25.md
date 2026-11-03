# Abdullah Tanvir Davidson 24th — public Drive mirror (2026-06-25)

Worked end-to-end ingest of a **multi-folder public Drive library** that **updates on Drive** (local mirror goes stale).

## Canonical source

- **URL:** https://drive.google.com/drive/folders/176ujvDTak-o6b6i14mYfXjrwYgBt5hFh
- **ID:** `176ujvDTak-o6b6i14mYfXjrwYgBt5hFh` (label `1 DAVIDSON`)
- **Mirror:** `/mnt/tb/Medicine/External/Abdullah-Tanvir-Davidson-Drive/`
- **Catalog:** `INDEX.md`, `SOURCE_DRIVE.md`, `AGENT_LEARNED.md`, `manifest.json`

## Scale (verified)

- 12 specialty subfolders + `_ROOT_MISC` (16 Google Docs + 1 PDF)
- **79** Google Docs → **79** `.txt` + **79** `.docx` (user wants **both** formats)
- ~31 MB on disk after docx export

## Re-sync (persisted scripts)

Drive is live; re-run when Abdullah updates notes:

```bash
python3 ~/.hermes/scripts/abdullah-tanvir-drive-ingest.py
python3 ~/.hermes/scripts/abdullah-tanvir-drive-export-docx.py
python3 ~/.hermes/scripts/abdullah-tanvir-drive-cleanup.py
```

Scripts copy from session templates; keep folder IDs + `ROOT_DOCS` map inside ingest script.

## Export URLs

```text
txt:  https://docs.google.com/document/d/{DOC_ID}/export?format=txt
docx: https://docs.google.com/document/d/{DOC_ID}/export?format=docx  # verify PK\x03\x04
pdf:  https://drive.google.com/uc?export=download&id={FILE_ID}
```

## Docx pairing strategy

Match each doc to existing `.txt` by **txt export byte size** in folder, then write `same_stem.docx`. `_ROOT_MISC` uses hard-coded `ROOT_DOCS` stem → doc_id map.

## Cleanup pitfalls

- Duplicate exports from repeated ingest passes → dedupe by **content SHA256**, keep largest file per hash.
- Ugly filenames from HTML (`D_*_strong_span_*`) → rename to `RHEUMATOLOGY_N`, `CARDIOLOGY_N`, etc.
- Manifest **fail rows** from wrong folder-id pairing ≠ missing files — audit with `find … -name '*.txt' | wc -l` vs live folder doc count.

## “Learn from notes” (agent digest)

After mirror complete, scan all `.txt` for `#DAVIDSON_REVIEW`, star counts, SBA/MCQ density; write **`AGENT_LEARNED.md`** + Mnemosyne (overlay role, not replacement for `/mnt/tb/Medicine` full notes). Corpus DNA: table-first, exam-date tags, Davidson table numbers (`26.1`).

## Thermal pacing

On DietPi / hot laptops: `sleep 1.5` per doc, `sleep 15` between specialty folders; long jobs `background=true` + `notify_on_complete=true`.

## User asks

| Ask | Action |
|-----|--------|
| Remember Drive link | `SOURCE_DRIVE.md` + Mnemosyne canonical slot |
| Keep txt + docx | Never drop txt; export docx alongside |
| Learn from download | `AGENT_LEARNED.md` scan + memory |