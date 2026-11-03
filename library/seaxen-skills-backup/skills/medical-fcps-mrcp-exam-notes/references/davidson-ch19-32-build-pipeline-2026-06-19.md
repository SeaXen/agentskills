# Davidson Ch 19, 21, 23-32 Build & Publish Pipeline (2026-06-19)

**Class:** `medical-fcps-mrcp-exam-notes` → "Build & Publish Pipeline" section.

This is the worked example for completing the remaining 12 chapters of Davidson 25th Ed. The 12 chapters were built, uploaded to Notion, rendered into the MedSea static site, and pushed to GitHub in one continuous session.

## Final State

| Ch | Title | Topics | Notion ID | MedSea Slug |
|---|---|---|---|---|
| 19 | Clinical Biochemistry & Metabolic Medicine | 28 | `184c380212d94c48a17cd879d941e6a3` | `19-clinical-biochemistry-and-metabolic-medi` |
| 21 | Diabetes Mellitus | 68 | `e6939ea1fa3d417684fa442a673efdb5` | `21-diabetes-mellitus` |
| 23 | Hepatology | 103 | `b916d8dadff6444ab8431495bf91c539` | `23-hepatology` |
| 24 | Haematology & Transfusion Medicine | 82 | `3b59159ad1ab47f0bd3e1fb51a9bca44` | `24-haematology-and-transfusion-medicine` |
| 25 | Rheumatology & Bone Disease | 71 | `fbf3e71640a44890849068e40a85a5a9` | `25-rheumatology-and-bone-disease` |
| 26 | Dermatology | 361 | `02211b2a0d9f42f4844a043a7c5edde0` | `26-dermatology` |
| 27 | Neurology & Stroke Medicine | 373 | `c76acd09ed434a7885ffa0dd59cecb03` | `27-neurology-and-stroke-medicine` |
| 28 | Medical Ophthalmology | 97 | `ff44045a4cab42f2be7e4b35d4dd606a` | `28-medical-ophthalmology` |
| 29 | Medical Psychiatry | 78 | `9d121dc4548f4f489db76e48579a34e9` | `29-medical-psychiatry` |
| 30 | Maternal Medicine | 109 | `4091353758324bbb9c6a5307754989f5` | `30-maternal-medicine` |
| 31 | Adolescence Transition & Young Adult | 52 | `7a36823752104013a5a37adc48747b5d` | `31-adolescence-transition-and-young-adult-m` |
| 32 | Older Adult Medicine & Frailty | 39 | `ed39c5f1c1714a779458a32c3e8f7a2c` | `32-older-adult-medicine-and-frailty` |
| **Total** | | **1461** | | |

All 32 chapters are live at `http://localhost:8855/` (Docker container `medsea`, port 8855).

## Source Mapping (Davidson 24th Ed → 25th Ed)

The `/mnt/tb/Medicine/` source is Davidson **24th Ed** but contains all the diseases needed for the 25th Ed chapters. Mapping:

| 25th Ed Ch | Source folder |
|---|---|
| 19 Clinical Biochemistry & Metabolic Medicine | `Clinical Biochemistry and Metabolic Medicine/` |
| 21 Diabetes Mellitus | `Diabetes/` |
| 23 Hepatology | `Hepatology/` |
| 24 Haematology & Transfusion Medicine | `Hematology/` |
| 25 Rheumatology & Bone Disease | `Rheumatology/` |
| 26 Dermatology | `Dermatology/` |
| 27 Neurology & Stroke Medicine | `Neurology/` + `Stroke Medicine/` (combined into `/tmp/ch27_combined/`) |
| 28 Medical Ophthalmology | `Medical Ophthalmology/` |
| 29 Medical Psychiatry | `Medical Psychiatry/` |
| 30 Maternal Medicine | `Maternal Medicine/` |
| 31 Adolescence Transition & Young Adult | `Adolescent and Transition Medicine/` |
| 32 Older Adult Medicine & Frailty | `Ageing and Disease/` |

## Two Source Layouts Discovered

| Layout | Examples | Detection |
|---|---|---|
| **flat** (diseases at top level) | Ch 19, Ch 23 | Diseases have `SRC_DIR/parts == 1`. Hub-pages list disease MDs in `## Disease-Level Topics` tables. |
| **subdirs** (diseases in subdirs) | Ch 25, Ch 26, Ch 27 | Diseases have `parts > 1`. Parent folder == hub name. |

The build script auto-detects via `len(parts) > 1` count > 50% of total.

## Pipeline Steps (executed in this order)

### 1. Build each chapter (single-chapter Python invocation)

```bash
# Wrap in shell — running 12 chapters in ONE Python process = SIGKILL (exit -9, OOM)
bash /tmp/build_final.sh
# Inside: build_chapter_pipeline.py "<num>" "<name>" "<src>" for each chapter
```

For Ch 27 specifically, pre-merge the two source dirs:
```bash
mkdir -p /tmp/ch27_combined
cp -r /mnt/tb/Medicine/Neurology/. /tmp/ch27_combined/
cp -r /mnt/tb/Medicine/Stroke\ Medicine/. /tmp/ch27_combined/20_Stroke_Medicine/
```

### 2. Restructure MedSea diseases to nested format

```bash
python3 scripts/restructure_medsea.py
```

Converts `diseases/<slug>.md` → `diseases/<hub>.<idx>-<slug>/topic.md` and copies the corresponding PNG from the local Sea-knowledge folder.

### 3. Update `build_site.py` `BUILT_CHAPTERS` with new entries

Add a tuple per chapter: `(slug, display_name, notion_url, color_hex)`. The notion URL follows the pattern below.

### 4. Rebuild site

```bash
python3 /mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py
# → 2957 topics across 32 chapters
```

### 5. Rebuild Docker image (no cache) and restart container

```bash
docker build --no-cache -t medsea-site:latest /mnt/tb/Sea-knowledge/#MedSea
docker stop medsea && docker rm medsea
docker run -d --name medsea -p 8855:8855 --restart unless-stopped medsea-site:latest
```

The container listens on port **8855** (configured in `docker/nginx.conf`). Mapping `-p 8855:80` does NOT work — must be `-p 8855:8855`.

### 6. Update Notion chapter page public URLs (read-only)

All 12 new chapters already had root pages in Notion from a prior session. To link the website to them, fetch the public URLs:

```python
URL = f"https://medsea.notion.site/Chapter-{ch}-{slug}-{pid.replace('-', '')}"
```

Where `slug` is the title slugified (lowercase, hyphens) and `pid` is the Notion page ID.

### 7. Commit + push to GitHub

```bash
git -C /mnt/tb/Sea-knowledge/#MedSea add -A
git -C /mnt/tb/Sea-knowledge/#MedSea commit -m "..."
git -C /mnt/tb/Sea-knowledge/#MedSea push origin main
```

A 12-chapter commit is ~5400 files / 1.3M insertions and takes ~70 seconds to push.

## Pitfalls Hit (and Fixes)

### ❌ SIGKILL on multi-chapter Python script (exit -9)

Running 12 chapters in ONE Python invocation → exit code -9. The build never started. Cause: combined memory pressure from renderer subprocesses.

**Fix:** Shell wrapper invokes `build_chapter_pipeline.py` per chapter. Each chapter uses ~300-500MB peak RAM, never OOMs.

### ❌ Renderer output nested in `<out>/<slug>/<slug>.png`

The renderer writes PNGs into a subdir matching the slug. The site builder expects flat `<out>/<slug>.png`.

**Fix:** After rendering, `shutil.move()` the nested PNG and `shutil.rmtree()` the nested dir.

### ❌ `/tmp` filled up during long build (6.8GB tmpfs)

`/tmp/rclone` mount + build dirs + ch27_combined took all 6.8GB. `execute_code` started returning `[Errno 28] No space left on device`.

**Fix:**
```bash
rm -rf /tmp/rclone /tmp/ch27_combined /tmp/build_*.log /tmp/upload_*.log /tmp/*.summary
```

Run this BEFORE starting a long batch build.

### ❌ Disease MD threshold too high (12KB) → missed many Ch 26 diseases

Initial threshold of 12KB filtered out 330+ Dermatology MDs that were 8-11KB. Result: 29/358 rendered.

**Fix:** Lower threshold to **8000 bytes**. Dermatology then rendered 348/358 (13 missing due to other issues).

### ❌ Renderer hangs on >400-line MDs

Some long Ch 27 MDs caused renderer subprocess to hang past the 120s timeout.

**Fix:** Per-topic subprocess with 120s timeout. Failures counted in `fail` and reported in the final stats. Hung MDs do NOT block subsequent renders (each is a separate subprocess).

### ❌ Site format mismatch (flat vs nested)

`build_site.py` expects `diseases/<hub>.<idx>-<slug>/topic.{md,png}` (cardiology format). `build_chapter_pipeline.py` writes flat `diseases/<slug>.md`.

**Fix:** `restructure_medsea.py` (this skill's scripts/) handles the move + PNG lookup automatically based on manifest.json.

### ❌ Docker port mapping -p 8855:80 doesn't work

The nginx config listens on port 8855 INSIDE the container. Mapping `-p 8855:80` exposes nothing because there's no process on port 80 inside.

**Fix:** `-p 8855:8855` for both host and container port.

### ❌ Container healthcheck reports unhealthy but site responds

The Docker HEALTHCHECK uses `wget --spider http://localhost:8855/` which works inside container, but the container may report `health: starting` or `unhealthy` while the actual HTTP service responds fine.

**Fix:** Trust `curl http://localhost:8855/` over Docker's healthcheck. The site is healthy if curl returns 200.

### ❌ `grep NOTION_API_KEY /root/.hermes/.env | head -2 | tail -1` needed

The .env file has TWO `NOTION_API_KEY=...` lines (one from initial setup, one from a later update). `grep | head -1` returns the wrong (older) value.

**Fix:** `head -2 | tail -1` to get the second one. Or read both and take the last non-empty value.

### ❌ Notion URL `medsea.notion.site` returns 403 to headless curl

Notion's anti-bot blocks headless HEAD requests. The URL works in real browsers.

**Fix:** Trust the URL pattern `medsea.notion.site/Chapter-<N>-<title-slug>-<id-no-dashes>`. Don't try to verify with curl from the shell.

### ❌ Terminal cwd resets between calls

The shell terminal resets cwd between tool calls. `cd` chains don't persist.

**Fix:** Always use `subprocess.run(['git', '-C', '/full/path', ...])` for git ops. Or pass `workdir=` to terminal calls.

## Notion Public URL Pattern

```python
import re
def make_notion_url(ch_num, title, page_id):
    """title is 'Chapter 19: Clinical biochemistry and metabolic medicine'"""
    slug = re.sub(r'^Chapter \d+: ', '', title)
    slug = re.sub(r'[^A-Za-z0-9]+', '-', slug).strip('-')
    return f'https://medsea.notion.site/Chapter-{ch_num}-{slug}-{page_id.replace("-", "")}'
```

## MedSea Notion DB

- DB ID: `3805588e-846f-808b-a23b-cf63c89f372e`
- API version: `2022-06-28` (NOT `2025-09-03` — that version doesn't exist)
- Key format: starts with `ntn_` (NOT `secret_`)

## Time Budget

| Stage | Time |
|---|---|
| Build Ch 19 (small, 28 topics) | ~2 min |
| Build Ch 26 (large, 361 topics) | ~15 min |
| Build Ch 27 (combined, 373 topics) | ~15 min |
| All 12 chapters sequential | ~45 min |
| Site rebuild | ~1 min |
| Docker rebuild (no cache) | ~5 min |
| Git commit | ~2 min (5400 files) |
| Git push | ~70 sec |
| **Total** | **~55 min** |

## Collapsible Images on Topic Pages (already in JS)

`build_site.py` line 1107-1114 has:
```javascript
const imgHtml = t.png ? `
  <div class="topic-image-toggle collapsed" onclick="toggleTopicImage(this)">
    <span><span class="toggle-icon">▼</span> &nbsp;Show infographic image</span>
    <span style="font-size:12px;color:var(--text-dim)">click to expand</span>
  </div>
  <div class="topic-image-wrap collapsed">
    <div class="topic-image"><img src="..." alt="..."></div>
  </div>` : "";
```

The toggle button + wrapper have `collapsed` class by default. The CSS in `topic-image-wrap.collapsed { display: none; }` hides the PNG until the user clicks. No rebuild needed — feature is already live.

## Final Site Stats

- **32 chapters live** at `http://localhost:8855/`
- **2957 topics** total (1287 from prior chapters + 1461 new + 209 from Ch 10-15)
- **Site size:** ~960 MB (mostly PNGs)
- **Docker image:** `medsea-site:latest` (~3.2GB)
- **GitHub:** https://github.com/SeaXen/MedSea (commit `ef3a246`)
