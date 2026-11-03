# Back-to-back 3-chapter batch (2026-06-18) — Respiratory + Endocrinology + Gastroenterology

## What was built in one session

Three full Davidson Sea Knowledge chapters, end-to-end, with the same pipeline.

| Chapter | Source | Topics | Hubs | Render | Upload | Duplicates | Image-only |
|---|---|---|---|---|---|---|---|
| 17. Respiratory | `/mnt/tb/Medicine/Respiratory/` | 149 | 10 | 149/149 | 149/149 | 6 (archived) | 0 |
| 18. Endocrinology | `/mnt/tb/Medicine/Endocrinology/` | 87 | 11 | 87/87 | 87/87 | 1 test page (archived) | 0 |
| 21. Gastroenterology | `/mnt/tb/Medicine/Gastroenterology/` | 147 | 9 | 147/147 | 147/147 | 0 | 0 |

Total: **383 topics across 30 hubs**, zero image-only pages, all backed up to `SeaXen/MedSea` on GitHub.

## Pattern that made this work

The 5-phase pipeline (manifest → preprocess → render → upload → verify → backup) was reused **without modification** for endo and gastro. The respiratory build was the test case that validated each phase, and the subsequent two were near-perfect executions.

For the next chapter (e.g. hepatology, neurology), the same scripts work with only two changes:
1. `build_<chapter>_manifest.py` — different hub definitions
2. `upload_<chapter>.py` — different `CHAPTER_HUB_ID` (the user's Notion URL slug)

Everything else (renderer, preprocessor, verifier, backup builder) is reusable.

## Source layout variation (gotcha for next chapter)

The three chapters had three different source layouts:

| Chapter | Layout | Notes |
|---|---|---|
| Respiratory | flat (162 .md at chapter root + MOC + Roadmap + 11 hierarchy files) | Required manual hub assignment dict |
| Endocrinology | flat (100 .md at chapter root + MOC + 11 hub parent files) | Same pattern as resp; explicit `HUBS` list with disease names |
| Gastroenterology | nested (9 hub folders each with 16-19 .md + 9 hub parent files at root) | Walk subfolders to find diseases; use folder name as hub name |

The `build_*_manifest.py` scripts differ in HOW they enumerate source files but produce the same output shape: `manifest["topics"] = [{hub_num, hub_name, title, slug, src_path, kind}, ...]`. The downstream pipeline (preprocess / render / upload) consumes only this manifest shape.

**For the next chapter:** check the source layout FIRST and pick the right enumeration pattern. Don't assume flat = resp pattern or nested = gastro pattern without looking.

## Per-chapter timing

| Phase | Respiratory | Endocrinology | Gastroenterology |
|---|---|---|---|
| Build manifest | ~10s | ~5s | ~5s |
| Preprocess (strip + autonumber) | ~3s | ~3s | ~3s |
| Render (4 parallel, 60s timeout) | ~3 min (1 retry pass for 29 fails) | ~3 min (no retries) | ~3.5 min (no retries) |
| Flatten | ~0s (already flat) | ~0s (already flat) | ~0s (already flat) |
| Upload (2-step file_uploads + 2-step page+image) | ~30 min (had 1 transient 400) | ~10 min (had 2 retried bugs, see below) | ~22 min (clean) |
| Verify (paginated block count) | ~5s for all 10 hubs | ~5s for all 11 hubs | ~5s for all 9 hubs |
| MedSea backup + push | ~1 min + push time | ~1 min + push time | ~1 min + push time |
| **Total** | ~35 min | ~13 min | ~26 min |

The respiratory upload was slow because the file_uploads send step occasionally hit 60+ seconds on Notion's server side; later uploads used 300s timeout and averaged ~10s/topic.

## Bugs fixed during the endo build (carried forward to gastro)

1. **Pitfall 59: `with http(...) as r:`** — the endo uploader's first version used `with http(...) as r:` where `http()` returns a parsed dict (not a context manager). All 87 topic uploads failed silently. Fixed by changing to plain `data = http(...)` calls. The fix is captured in the skill as Pitfall 59.

2. **Pitfall 60: `markdown` + `children` together** — the endo uploader's first version tried to pass `markdown` field AND `children` array in the same `POST /v1/pages` call. Notion returned HTTP 400 with the exact message *"Cannot specify 'markdown' together with 'content' or 'children'. Use one content format per request."*. Fixed by splitting into 2 calls: page create with markdown, then PATCH /children for the image. The fix is captured in the skill as Pitfall 60.

3. **File uploads 2-step trap** — initial endo uploader tried `POST /v1/file_uploads` with multipart body directly. Got HTTP 400. Fixed by doing step 1 (JSON metadata) → step 2 (multipart bytes to the returned `upload_url`). This was already in the skill as Pitfall 52 but had been re-discovered in a different form.

After these three fixes (and adding the 300s timeout for the upload step), the gastro chapter was clean end-to-end: 0 failures, 0 duplicates, 0 image-only pages.

## Verification pattern (now in the skill)

After each chapter, the verification script `verify_content_sample.py` (added to the skill) does:
1. Fetch all hub pages (paginated)
2. For each hub, pick 1 random topic page
3. Fetch the topic's blocks (paginated)
4. Count: text blocks (paragraph/heading/list/callout/table) + image blocks
5. Assert: n_text >= 3 AND n_image == 1

The output: `[OK] 18.1. General Principles > "Dynamic Testing Principles": 182 blocks, 149 text, 26 tables, 1 images`

This catches image-only pages (n_text < 3) and zero-image pages (n_image < 1) within ~5 seconds. The deduplication check is a separate loop using `Counter(titles)` on lowercase titles.

**The full verify script:** `scripts/verify_content_sample.py` in the skill.

## Scripts produced (saved in skill's `scripts/` for future reuse)

- `build_endo_manifest.py`, `build_gastro_manifest.py` — manifest builders for the two new source layouts
- `preprocess_endo.py`, `preprocess_gastro.py` — same preprocessor as resp (no changes needed)
- `render_endo.py`, `render_gastro.py` — same renderer pattern (4 workers, 60s timeout, 100-line retry)
- `upload_endo.py`, `upload_gastro.py` — same uploader pattern with the 3 bug fixes
- `verify_endo.py`, `verify_gastro.py`, `check_endo_content.py`, `check_gastro_content.py` — verification scripts
- `cleanup_endo.py` — script to archive stale duplicates
- `build_endo_backup.py`, `build_gastro_backup.py` — MedSea backup builders
- `verify_content_sample.py` — reusable random-sample verification (now in skill's `scripts/`)

## GitHub backup status (SeaXen/MedSea)

Three new commits pushed (post-respiratory, post-endo, post-gastro):
- `e16581e` (respiratory, 59MB)
- `337016c` (endocrinology, 55MB)
- `dcXXXXX` (gastroenterology, 53MB)

Each backup includes:
- `chapters/<N>-<specialty>/manifest.json` — canonical topic list
- `chapters/<N>-<specialty>/diseases/<N>.<hub>.<local-counter>-<slug>/` — flat-named folders with md+html+png
- `chapters/<N>-<specialty>/hubs/<N>-<hub-name>.md` — hub index files
- `chapters/<N>-<specialty>/source/` — original source mds (preserves subfolder structure for gastro)

## Key takeaways for the next chapter

1. **The 5-phase pipeline is now stable.** Respiratory was the test case; endo and gastro validated it. The same scripts will work for hepatology, neurology, etc. with only manifest + chapter_id changes.

2. **Three Notion API pitfalls to avoid up front** (already in the skill, but worth re-reading):
   - `http()` returns dict, not context manager (Pitfall 59)
   - `markdown` + `children` cannot coexist in one POST (Pitfall 60)
   - File uploads are 2-step (Pitfall 52)

3. **Source layout dictates the manifest builder.** Check the chapter root before writing the manifest script — flat files (resp/endo) need explicit hub mapping, nested folders (gastro) need a directory walk.

4. **Random-sample verification is the fastest sanity check.** 5 seconds for a 9-hub chapter to catch image-only or zero-content pages. Run it after every upload, before declaring success.

5. **The user always asks for "complete fully and double check" after a chapter.** Build the verification into the post-upload step automatically; don't wait to be reminded.

6. **The skill's `notion_upload.py` was correct from the start** — the ad-hoc uploaders written for each chapter were where the bugs lived. The lesson: **always reuse the skill's scripts (or close copies) for any new chapter**, don't reinvent with hand-rolled uploaders.
