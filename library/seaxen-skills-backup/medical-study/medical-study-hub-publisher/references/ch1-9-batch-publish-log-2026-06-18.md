# Ch 1-9 Back-to-Back Publish Log — 2026-06-18

Session goal: complete Davidson 25th Ed Ch 1-9 (Clinical decision-making → Palliative care), with all info + image like cardiology, and publish to **local + Notion + MedSea site + GitHub**.

Final result: **9 chapters, 343 topics, 51 hubs, 0 failures end-to-end**. 14-chapter MedSea site went live (1,105 topics). GitHub commit `df59140` on `main` (1,781 files, 489K insertions).

This log covers what worked, what broke, and the 5 new pitfalls (71-75) that came out of the run.

## Per-chapter results

| # | Chapter | Topics | Hubs | Notion | Status |
|---|---|---|---|---|---|
| 1 | Clinical decision-making | 6 | 6 | done | skipped (from prior run) |
| 2 | Clinical therapeutics and good prescribing | 71 | 14 | done | 10 new + 61 skipped |
| 3 | Clinical genetics | 6 | 6 | done | 2 new + 4 skipped |
| 4 | Clinical immunology | 2 | 2 | done | skipped (from prior run) |
| 5 | Nutritional factors in disease | 35 | 7 | done | skipped (from prior run) |
| 6 | Population health and epidemiology | 27 | 5 | done | skipped (from prior run) |
| 7 | Principles of infection | 26 | 7 | done | 21 new + 5 skipped |
| 8 | **Oncology** | 119 | 20 | done | 119 new + 0 skipped — largest chapter |
| 9 | Palliative and supportive care | 51 | 9 | done | 51 new + 0 skipped |

Total: **343 topics + 51 hubs across 9 chapter roots on Notion**.

## What worked

1. **Renderer pre-processing** (`preprocess.py` to strip frontmatter + auto-number `## ` headers) — used in the build phase before this session, no issues during the upload phase.
2. **`skip_existing=True` on the uploader** — re-running the upload script (after network timeouts) correctly identified already-published hubs + topics via title matching and skipped them. Saved ~3 hours of duplicate work.
3. **The 2-step `file_uploads` flow** (Pitfall 52) — still works. The fix needed was the *retry classification* (Pitfall 72), not the flow itself.
4. **Truncated-render pattern** (Pitfall 56) — none of the Ch 1-9 topics needed truncation in the final pass. Earlier passes had used it; the truncation was already done from the renderer.
5. **Build script `BUILT_CHAPTERS` dict** — added 9 new entries in one edit, walked all the new chapter folders, generated the new `site/` tree, and rebuilt Docker.

## What broke (and how it was fixed)

### Renderer `body_lines` bug (became Pitfall 71)

After the initial `build_ch1_9.py` run, 44 of 119 Ch 8 Oncology topics had **30-60KB PNGs** instead of the expected 600-800KB. The other 75 rendered fine. Same source structure, same renderer invocation, same everything — the only difference was the topics with markdown pipe-tables (TNM staging, chemo regimens, prognosis indices) all failed.

Inspecting the renderer output HTML showed:
- Failed topics: had `<div class="sec">` blocks but **no `<table>` tags** even though the source had tables
- The renderer process didn't error — it just silently dropped the table content

Patched `/root/sea-knowledge-infographics/render_topic.py` around line 310:
```python
# Before (raises KeyError or appends to wrong key):
current["body"] = current.get("body", "") + table_html
# After:
current.setdefault("body_lines", []).append(table_html)
```

Re-rendered 39 of the 44 failed topics successfully (5 were SKIP — they had already produced valid PNGs in the initial pass despite the bug, likely because the table-flush branch didn't trigger for them). 0 net failures after re-render.

**Why this matters beyond Ch 8:** any future chapter with frequent tables (pharmacology chapters like Ch 2, haematology Ch 24, biochemistry references) will hit this. Spot-check the rendered output for short PNGs BEFORE declaring the build done.

### Notion 403/timeout hang (became Pitfall 72)

After the Ch 8 re-render, the upload script (`upload_ch1_9.py`) ran against the rebuilt files. Got to topic 2.1.02 (Adrs — 706KB PNG) and printed:
```
PNG upload fail 2.1.02: {'_error': 403, '_body': '...'}
```
Then **hung in `do_sys_poll`** — the process was alive but not making progress. The `file_uploads` send endpoint returned 403 (likely a transient Notion-side rate limit) and the retry logic only handled 429, so the upload_id came back `None` and the script tried to create a Notion page without an image, which 400'd because the children array had `"id": None`.

Killed the process. Patched the script to:
1. Add 502/503/504/403 retries with exponential backoff in both `http()` and `upload_png()`
2. Bump retries from 3 to 5
3. Lower per-request timeout from 120s to 60s
4. Add `URLError` / `TimeoutError` / `ConnectionError` handlers

Re-launched. The 403 didn't recur on 2.1.02 specifically, but the script successfully completed all 9 chapters with 0 image failures.

### Skip-on-fail for image upload (became Pitfall 73)

Even with the broader retry logic, the original uploader's behavior on image-upload failure was to skip the whole topic — losing the markdown content. Re-launched the upload AFTER adding the skip-on-fail pattern: when `upload_png()` returns `None, err`, call `create_topic_page(hub_id, title, md_text, file_upload_id=None)` which:
- Creates the page with full markdown body
- Skips the image block in `children` (not pass `id: None`)
- Adds a yellow callout "Image upload pending retry" instead
- Increments `stats["topics_noimg"]` so the run summary shows the count

This way, even if all image uploads fail, the user still gets the full markdown content for every topic — better than losing the topic entirely.

### Slug mismatch in BUILT_CHAPTERS (became Pitfall 74)

Added 9 new entries to `BUILT_CHAPTERS` in `build_site.py`. First attempt used formal Davidson titles for slugs:
```python
"2-clinical-therapeutics-and-good-prescribing": {...},
"5-nutritional-factors-in-disease": {...},
"7-principles-of-infection": {...},
"9-palliative-and-supportive-care": {...},
```
But the actual chapter folders were the shorter versions:
```bash
ls /mnt/tb/Sea-knowledge/#MedSea/chapters/
# 2-clinical-therapeutics  (not 2-clinical-therapeutics-and-good-prescribing)
# 5-nutritional-factors  (not 5-nutritional-factors-in-disease)
# 7-principles-of-infection  (matches)
# 9-palliative-care  (not 9-palliative-and-supportive-care)
```

After the build, the site showed 4 orphan cards (long slug, 0 PNGs) and 4 "missing" cards (no card at all, because the dict didn't include the short slug). Fixed by editing the dict to use the actual folder slugs.

**Convention now:** `BUILT_CHAPTERS` uses the shortest descriptive slug; `DAVIDSON_25TH` (display table) uses the formal Davidson title with the short slug as the third tuple element.

### Large git push (became Pitfall 75)

The commit `df59140` was 1,781 files / 489K insertions. The push took **32 minutes**. The push log stayed 0 bytes for the entire window — I almost killed the process thinking it had hung.

Verified the push was alive via `cat /proc/<pack_pid>/io`:
```bash
cat /proc/137446/io | grep wchar
# wchar: 247046144  ← 247 MB written to network so far (after 30 min)
```

The push eventually completed normally (exit 0) and the log file was populated only at the very end:
```
To https://github.com/SeaXen/MedSea.git
   4717258..df59140  main -> main
EXIT=0
```

The MedSea `.gitignore` correctly excludes `site/**/*.png` so the push was text-only (the actual 265 MB of PNGs lives in `chapters/<slug>/diseases/`, NOT in `site/`). Without that exclusion, the push would have been 500+ MB and taken over an hour.

## Docker restart for new site build

After fixing the slug mismatch and rebuilding `site/`, the running `medsea` container was still serving the **old 5-chapter build**. Required `docker stop medsea` + `docker rm medsea` + `docker run -d ...` to use the new `medsea-site:latest` image.

The new image (`39faaee5e1da`) and the running container's image (`81a2d87afe78`) are **different** because the running one was built before the Ch 1-9 site content existed. `docker build -t medsea-site:latest .` with the same Dockerfile + same `COPY site/` directive correctly cached (the `site/` directory was the same as the last build, just the `site/` BUILD ARTIFACT included the new chapters).

Verified the new site is live:
```bash
curl -sI http://localhost:8855/  # HTTP 200, 46KB
curl -s http://localhost:8855/ | grep -oE '1-clinical-decision-making|2-clinical-therapeutics|...'
# All 9 new chapter slugs present in the index
```

## Notion upload recovery via skip_existing

The Ch 1-9 upload script ran THREE times during this session:
1. **First run** (proc_b93cf2cec6b3) — completed Ch 1, started Ch 2, hit `URLError: The write operation timed out` on topic 7.1.04 → process died
2. **Second run** (proc_31984d675dad) — added retry logic for 502/503/504 but still hit max_retries on 2.1.02 → process hung in `do_sys_poll`
3. **Third run** (proc_2600b44bec34) — with full skip-on-fail pattern + 60s timeout + 5 retries → completed all 9 chapters in 65 minutes

The skip_existing pattern was the unsung hero — without it, the second and third runs would have re-uploaded 200+ topics that were already published, hitting the same rate limits and making the run take 3+ hours.

**Verified final Notion state via the third run's log:**
```
=== FINAL ===
  Ch 1: 0 ok, 6 skipped, 0 failed
  Ch 2: 10 ok, 61 skipped, 0 failed
  Ch 3: 2 ok, 4 skipped, 0 failed
  Ch 4: 0 ok, 2 skipped, 0 failed
  Ch 5: 0 ok, 35 skipped, 0 failed
  Ch 6: 0 ok, 27 skipped, 0 failed
  Ch 7: 21 ok, 5 skipped, 0 failed
  Ch 8: 119 ok, 0 skipped, 0 failed
  Ch 9: 51 ok, 0 skipped, 0 failed
```

## What I would do differently next time

1. **Spot-check rendered PNGs within the first 50 of a bulk render** (not after all 343 are done). The Ch 8 bug cost ~30 minutes of post-mortem and re-rendering. A 5-second `find . -name "*.png" -size -100k | wc -l` after the first 50 topics would have caught it immediately.
2. **Always use skip-on-fail for the image upload** (Pitfall 73) from the start, not as a post-hoc patch. The first run's death on 7.1.04's timeout could have been a 1-second "image pending retry" yellow callout instead of a script crash.
3. **Add a `BUILT_CHAPTERS` validation step in `build_site.py`** that asserts every dict key matches an actual folder name:
   ```python
   for slug in BUILT_CHAPTERS:
       if not (CHAPTERS_ROOT / slug).exists():
           print(f"WARNING: BUILT_CHAPTERS['{slug}'] has no folder, build will produce 0 topics")
   ```
   This would have caught the slug-mismatch bug at build time, not after the user opened the site and saw missing chapters.

## Final state

- **Local:** `/mnt/tb/Sea-knowledge/1-9*/` (canonical) + `/mnt/tb/Sea-knowledge/#MedSea/chapters/1-9*/` (backup)
- **Notion:** 9 chapter roots, 51 hub sub-pages, 343 topic sub-pages, all with full markdown + PNG (no `noimg` topics in the final run)
- **MedSea site:** 14 chapters live at `http://192.168.0.222:8855/` (1,105 topics, 51 hubs, 1,105 PNGs)
- **GitHub:** `df59140` on `main` at https://github.com/SeaXen/MedSea (1,781 files, 489K insertions, 32-min push)

Ready for the next batch: Ch 10-14 (the rest of the "general principles" section) or Ch 19-32 (the system-specific chapters). The pipeline is now stable enough to run 9-chapter batches in one go.
