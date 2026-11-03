# Respiratory Ch 17 — Render & Publish Log (2026-06-17/18)

## What was built

Davidson **Chapter 17: Respiratory medicine** — full Sea Knowledge study hub.

- **Source:** `/mnt/tb/Medicine/Respiratory/` (162 .md files)
- **Output:** `/mnt/tb/Sea-knowledge/17. Respiratory/` (10 hubs, 149 disease-level topics, 145 PNGs)
- **Notion hub URL:** `https://app.notion.com/p/searex/Chapter-17-Respiratory-medicine-d4fe7d456ca4481581e806ebe9e177cf`

## Hub mapping (10 hubs, 149 topics)

| Hub | Topics | Hubs name |
|---|---|---|
| 17.1 | 17 | Functional Anatomy, Physiology, and Investigations |
| 17.2 | 11 | Symptom Approach to Respiratory Disease |
| 17.3 | 7 | Upper Airway and Sleep-Related Breathing Disorders |
| 17.4 | 27 | Airway Diseases |
| 17.5 | 22 | Respiratory Infections |
| 17.6 | 16 | Pleural Diseases |
| 17.7 | 10 | Pulmonary Vascular Diseases |
| 17.8 | 13 | Interstitial and Diffuse Parenchymal Lung Diseases |
| 17.9 | 14 | Respiratory Failure and Ventilatory Support |
| 17.10 | 12 | Thoracic Malignancy |

## Pipeline used (re-validated 2026-06-18)

1. **Manifest** — `python3 /tmp/build_resp_manifest.py` maps 162 source files to 10 hubs via:
   - Subdirectory files: `Respiratory/<Hub Name>/...` → direct mapping
   - Root-level files: explicit dict in `build_resp_manifest.py` (e.g. `Asthma.md` → 17.4)
   - Skips: MOC, Roadmap, Hierarchy, hub-level `.md` files (10 of each)
   - Output: `Total topics: 149` (162 - 13 skipped)

2. **Preprocess** — `python3 /tmp/preprocess_resp.py` strips frontmatter and auto-numbers `## ` headers to `## 1. Title`, `## 2. Title`, etc. (Pitfall 51 fix). Output: `/root/resp-content/<slug>.md` (149 files).

3. **Render** — `python3 /tmp/render_resp_v3.py` runs `render_topic.py` per topic with:
   - 30s timeout, 2 parallel workers, process group kill (Pitfall 56)
   - Auto-truncation to first 100 lines for sources > 30KB
   - Skip-existing logic for re-runs
   - Result: **84 OK + 32 skip + 33 fail** in 622s (first pass), then **29 OK** in 38s (retry pass with 100-line truncation), then **4 OK** (final retry for the 4 originally-missing: pneumothorax, abg, oxygen, spirometry)
   - **Total: 145 PNGs + 4 retried = 149/149 topics rendered**

4. **Flatten** — `python3 /tmp/flatten_resp.py` (no-op for respiratory, renderer output was already flat)

5. **Publish to Notion** — `python3 /tmp/upload_resp_v2.py`:
   - **Step 1:** Create 10 hub parent pages under `d4fe7d456ca4481581e806ebe9e177cf` (all CREATED successfully, verified via Notion API)
   - **Step 2:** For each topic, upload PNG + create sub-page with `markdown` field + append image block
   - **Upload script v1 crashed on first upload** with `urllib.error.URLError: <urlopen error The write operation timed out>` — fixed in v2 with:
     - 180s timeout for the multipart send step (was 120s)
     - Retry logic for `URLError`/`TimeoutError`/`ConnectionError` (was 4xx/5xx only)
     - 1.5s sleep between topics (was 1.0s)
   - **Upload v2 started (proc_6f1d7c6116bb)** but interrupted at session tool-call limit before completion

## Key new pitfalls encountered

- **Pitfall 56** — Chromium hangs on long content (400+ lines / 30+ KB). Fix: truncate + process-group kill.
- **Pitfall 57** — Build N hub parent pages FIRST before uploading topics (the respiratory chapter started with 0 children on the user's hub page).
- **Pitfall 58** — Title fuzzy matching needed when matching by re-derived slug-title misses "of the" / "in" prepositions in the original Notion page title.

## What's still pending

- Re-run `/tmp/upload_resp_v2.py` to complete the 149 topic uploads
- Verify final state: 10 hubs each with ~15 sub-pages containing 100-300 blocks each (paginated verification required — Pitfall 53)
- Commit MedSea backup update for the new chapter (`build_backup_resp.py` needs to be written, mirroring `build_backup_nephro.py`)
- User said "yes git push" earlier (about the nephrology commit) — this respiratory build hasn't been pushed yet

## Scripts produced

- `/tmp/build_resp_manifest.py` — manifest builder
- `/tmp/preprocess_resp.py` — header numberer
- `/tmp/render_resp.py` — first render attempt (chromium hung, killed)
- `/tmp/render_resp_v2.py` — render with hard timeout + skip-existing
- `/tmp/render_resp_v3.py` — render with truncation + 2-worker parallelism
- `/tmp/render_resp_retry.py` — retry failed topics with 100-line truncation
- `/tmp/flatten_resp.py` — flatten nested folders (no-op for resp)
- `/tmp/upload_resp.py` — first upload (v1, crashed with write timeout)
- `/tmp/upload_resp_v2.py` — robust upload with retries and 180s multipart timeout

## Lessons for the next chapter build

1. **Start with hub creation**, not topic creation. Build N hub parent pages first, then create topics under them.
2. **Use truncation from the start** — don't waste a 30-min render batch discovering chromium hangs. Threshold of 30KB is reliable.
3. **Use the `markdown` field on page create** (Pitfall 54) so topics land with full content from the first attempt, no need for the recreate-with-full-content pattern.
4. **The fuzzy title matcher (Pitfall 58)** is needed if you ever re-derive titles from slugs after a Notion import. Skip it if you preserve the original H1 from the source.
5. **Upload script needs 180s+ timeout for the multipart send step.** 120s occasionally hits the Notion server processing floor (~2.5s/request) on slow connections.