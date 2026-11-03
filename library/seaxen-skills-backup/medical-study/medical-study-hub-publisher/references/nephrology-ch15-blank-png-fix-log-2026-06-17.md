# Nephrology Ch. 15 — Blank PNG Fix + Notion Roundtrip (2026-06-17)

Session that took the Chapter 15 Nephrology & Urology study hub from
"49 blank PNGs published to Notion" to "49 populated PNGs with correct
content, all on live Notion, all backed up to MedSea". Also extended the
medical-study-hub-publisher skill with three new pitfalls (51, 52, 53).

## What went wrong

1. **First render produced 49 blank PNGs.** Nephrology source at
   `/mnt/tb/Medicine/Nephrology and Urology/` used raw `## Learning Objectives`,
   `## Aetiology`, `## Clinical Features` headers. `render_topic.py`'s
   `parse_markdown_to_html` only creates `sec` blocks from `^## \d+\. ` —
   so every section was silently dropped. PNGs came out at 30-50KB (header
   + footer only, no body), HTML had 0 `<div class="sec">` blocks.

2. **First upload of 49 blank PNGs to Notion** succeeded but the images
   were empty. Discovered when the user reported "all images are blank".

3. **Verification after the fix was wrong.** Wrote a verifier using
   `?page_size=100` and reported "0 images on 6 hub 15.1 pages". The
   images were actually there — just past block 100. Notion's default
   page_size returns only the first 100 children and silently drops the
   rest. Pages with 150+ blocks (Sea Knowledge sub-pages routinely have
   200+) need `start_cursor` pagination.

4. **Notion file_uploads send endpoint kept returning 400.** First
   attempt used raw bytes with `Content-Type: image/png`. The endpoint
   requires `multipart/form-data` with a `file` field, like a browser
   file upload. Built the multipart body manually with a uuid boundary.

5. **Duplicate sub-pages in hub 15.1.** Original block-import flow had
   created 6 sub-pages with rich Notion block content. The upload script
   then created 4 new sub-pages with just images (because title comparison
   was case-sensitive: "Clinical Examination of the Kidney and Urinary
   Tract" vs my "Clinical Examination Kidney Urinary Tract"). Deleted the
   4 dups; replaced their images onto the 6 originals.

## What worked

1. **Pre-processor pattern** (`scripts/preprocess_headers.py`): strip
   frontmatter + auto-number `## ` headers sequentially. 30 lines of
   regex. Re-rendered all 49 topics in <2 min.

2. **Notion file_uploads with multipart**: full helper in the upload
   script. After fixing, 49/49 uploads succeeded in 90 seconds.

3. **Paginated verifier** (`scripts/paginate_blocks.py`): `start_cursor`
   loop until `has_more=False`. Caught the false "0 images" report.

4. **Image-block dedup** on hub 15.1: kept the most recently created
   image with matching caption, deleted the rest. Pages went from
   2-3 image blocks each down to 1.

5. **Build backup script per chapter**: `scripts/build_backup_nephro.py`
   mirrors `build_backup.py` (cardiology) structure with nephrology hub
   list. Produces 49 disease folders + manifest + README in
   `chapters/15-nephrology-urology/`. Committed and pushed to
   `https://github.com/SeaXen/MedSea` (commit `39ad2fb`).

## Final state

- **Notion**: 6 hub parent pages + 49 sub-pages, 49/49 with embedded
  infographic image, all populated (no blanks)
- **Local archive**: `/mnt/tb/Sea-knowledge/15. Nephrology and Urology/`
  with 6 hub folders + 49 disease folders, each containing `<slug>.md`,
  `<slug>.html`, `<slug>.png` (500-730KB each, 20-30 sec-blocks)
- **MedSea backup**: `/mnt/tb/Sea-knowledge/#MedSea/chapters/15-nephrology-urology/`
  with 49 disease folders, manifest.json, README.md, source/*.md
- **GitHub**: pushed at `https://github.com/SeaXen/MedSea` commit `39ad2fb`
- **Live Notion URL**: https://app.notion.com/p/searex/Chapter-15-Nephrology-and-urology-710f215344c34692af7584e89e714ff0

## Lessons (now in SKILL.md as Pitfalls 51-53)

1. **Always pre-process unfamiliar source.** The renderer requires
   `## N. Title` headers. Raw source with `## Section Name` silently
   produces blank PNGs. Diagnosis: PNG < 80KB and 0 `sec` blocks.
2. **Notion file_uploads send endpoint = multipart/form-data with `file`
   field, NOT raw bytes.** Build the multipart body manually.
3. **Paginate `/blocks/{id}/children` with start_cursor when page has
   >100 blocks.** Sea Knowledge sub-pages have 200+ blocks routinely.

## Key files added to the skill

- `scripts/preprocess_headers.py` — strip frontmatter + auto-number
  `## ` headers (Pitfall 51)
- `scripts/paginate_blocks.py` — `start_cursor` loop for Notion block
  fetches (Pitfall 53)
- This reference log

## Key files NOT modified (kept the existing pattern)

- `scripts/render_topic.py` — renderer itself wasn't changed; the
  pre-processor sits in front of it. Future option: patch the renderer
  to accept `## Section Name` headers and auto-number them, but the
  pre-processor pattern is reusable and works for any new chapter.
- `scripts/notion_upload.py` — kept the original 3-step flow but the
  `notion` skill and SKILL.md now warn about the multipart requirement
  via Pitfall 52.
