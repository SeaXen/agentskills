---
name: medical-study-hub-publisher
description: Convert a medical chapter's source notes (e.g. /mnt/tb/Medicine/Cardiology) into a Notion study hub — a parent page with a numbered clickable index, plus N sub-pages each containing a 10-section Sea Knowledge study writeup, comparison tables, exam pearls, and an embedded A4 portrait infographic PNG. Use when the user asks to "do all topics from [chapter]", "publish a study hub", "build a Notion index for [specialty]", or "convert these notes into a study site with infographics".
version: 1.3.0
author: community
license: MIT
metadata:
  hermes:
    tags: [medical-study, notion, publishing, pipeline, infographics, study-hub]
    related: [notion, subagent-batch-note-conversion, medical-fcps-mrcp-note-creation]
---

# Medical Study Hub Publisher

End-to-end pipeline that takes a chapter folder of medical source notes and produces a Notion study hub: a parent page with a numbered clickable index, plus N sub-pages each containing a 10-section study writeup + an embedded A4 portrait infographic PNG. Local archive of `.md` + `.html` + `.png` per topic is saved to `/mnt/tb/Sea-knowledge/` (or similar).

**Validated:** 2026-06-17, Davidson Chapter 16 Cardiology — 16 sub-pages + hub with numbered index (~17 min), then expanded to 330 disease-level sub-pages under 17 numbered hubs (~3 hours, including recovery from a destructive mistake). 2026-06-17, Davidson Chapter 15 Nephrology — 6 hubs, 49 sub-pages with full PNG roundtrip after fixing two renderer+Notion pitfalls (Pitfall 51, 52). 2026-06-18, Davidson Chapter 17 Respiratory — 10 hubs, 149 topics, end-to-end clean (no duplicates, no image-only pages) using the truncated-render + 2-step page+image pattern. 2026-06-18, Davidson Chapter 18 Endocrinology — 11 hubs, 87 topics, **0 failures, 0 duplicates** end-to-end. 2026-06-18, Davidson Chapter 21 Gastroenterology — 9 hubs, 147 topics, **0 failures, 0 duplicates** end-to-end. Three-chapter back-to-back run (resp + endo + gastro) proves the pipeline is stable. 2026-06-18, **Phase 7 (Static Site)** added: built `medsea-site` from the 5 published chapters — Docker (nginx:alpine) on port 8855 + Vercel config, 768 HTML pages, 760 PNGs, no-JS SPA with hub/topic navigation and Notion deep links. Co-located at `/mnt/tb/Sea-knowledge/#MedSea/site/`. **2026-06-18, Phase 7 v2 redesign:** header stats bar + 32-chapter dropdown + chapter SPA (sidebar topic list + main topic pane) + topics.json manifest. See `references/medsea-static-site-v2-spa-redesign-log-2026-06-18.md`. **2026-06-18, Ch 1-9 back-to-back batch** (Clinical decision-making, therapeutics, genetics, immunology, nutritional factors, population health, principles of infection, oncology, palliative care) — 9 chapters, 343 topics, 51 hubs, **0 failures end-to-end**, fixed a real renderer bug (table flush `body` → `body_lines` — Pitfall 71), added 403/timeout retry logic for `file_uploads` (Pitfall 72), added skip-on-fail pattern (Pitfall 73), and confirmed the 14-chapter MedSea static site (1,105 topics) and GitHub backup workflow (Pitfalls 74, 75). See `references/ch1-9-batch-publish-log-2026-06-18.md`.

## When to use this skill

Trigger on any of:
- "do all topics from [chapter]" / "publish all topics from [specialty]"
- "build a Notion study hub" / "make a study site with infographics"
- "convert these notes into a Notion index with images"
- "I want a numbered index of [N topics] on Notion with one infographic each"

The user almost always wants: (1) a hub page with a clean numbered index, (2) one sub-page per topic with the full content, (3) a one-page A4 portrait infographic per topic, (4) the source files saved locally.

## Pipeline (7 phases)

```
[source notes folder]                                [user's local archive]
   e.g. /mnt/tb/Medicine/Cardiology/                   e.g. /mnt/tb/Sea-knowledge/
                │                                                ▲
                ▼                                                │
  Phase 1: Identify canonical topic list                        │
   - Read chapter MOC / Hierarchy / Roadmap if present          │
   - Or: list the numbered sub-folders (01_*, 02_*, ...)        │
   - Or: ask the user which scope you want                     │
                │                                                │
                ▼                                                │
  Phase 2: Generate 10-section markdown per topic               │
   - 3 parallel subagents via delegate_task                     │
   - Each gets: the IHD example + 4-6 source folders            │
   - Output: /root/sk-content/<slug>.md                         │
                │                                                │
                ▼                                                │
  Phase 3: Render each markdown to HTML + PNG                   │
   - render_topic.py (see scripts/)                             │
   - **If source uses `## Learning Objectives` style headers,   │
     run preprocess.py first (Pitfall 51)**                     │
   - Output: <archive>/<slug>/<slug>.{md,html,png}  ───────────┘
                │
                ▼
  Phase 4: Publish to Notion (3-step per topic)
   - Upload PNG via file_uploads + multipart (Pitfall 52)
   - Create sub-page with markdown body (Pitfall 54)
   - **markdown + children cannot coexist in one POST (Pitfall 60)**
   - Append image block via PATCH /children (separate call)
   - **Always paginate `/blocks` queries with start_cursor (Pitfall 53)**
   - **A custom `http()` helper that returns a parsed dict is NOT a context manager (Pitfall 59)**
                │
                ▼
  Phase 5: Build the numbered index on the hub page
   - Delete auto-added child_page blocks (avoid duplication)
   - Add numbered_list_item with mention-page blocks
```

## Phase 1 — Identify the canonical topic list

The user's chapter folder almost always has the canonical list already, in one of these forms:
- A `*MOC.md` or `*Hierarchy.md` at the chapter root (Davidson chapters use this — `Davidson Chapter 16 - Cardiology Hierarchy.md` lists 16 sections)
- A `*Roadmap.md` (the user's "Chapter 16 Cardiology Roadmap.md" lists 12 high-yield topics)
- Numbered sub-folders (`01_Cardiac_Investigations/`, `02_Acute_Coronary_Syndromes/`, ...)

Build a `topics.py` file with `[{num, slug, title, source_dir, subdir}, ...]`. Preserve Davidson's numbering if present — the user expects it.

```python
topics = [
    {"num": 1, "slug": "cardiac-investigations",
     "title": "Cardiac Investigations",
     "source_dir": "/mnt/tb/Medicine/Cardiology/01_Cardiac_Investigations",
     "subdir": "01_cardiac_investigations"},
    # ... 15 more
]
```

## Phase 2 — Generate 10-section markdown per topic

Use the 3-parallel-subagent pattern from `subagent-batch-note-conversion`. Distribute topics across 3 batches (5-6 topics each). Each subagent needs:

1. **The IHD example** at `/root/ihd_content.md` (or your reference) — read it to learn the exact format
2. **The 4-6 source folder paths** for their batch
3. **The format spec** (10 sections, 6000-13000 chars per topic, 12 exam pearls, comparison tables, etc.)
4. **The output path**: `/root/sk-content/<slug>.md`

### The 10-section structure (don't deviate)

```
1. Introduction / Definition
2. Pathophysiology / Mechanism
3. Classification / Types / Spectrum
4. Clinical Features / Presentation
5. Investigations / Diagnosis
6. Differential Diagnosis   ← use a TABLE
7. Complications
8. Management / Treatment   ← use a TABLE for dosing/strategy
9. Secondary Prevention / Long-term
10. Exam Pearls & High-Yield ← 12 bullet points + Clinical Significance callout
```

### Markdown formatting rules (strict)

- `# Title` first, then `## 1. Section Title` through `## 10. ...`
- `### Sub-Heading` for subsections
- Bullet lists with `- `, numbered lists with `1. `
- `**bold**` for key terms, `*italic*` sparingly
- `> callout text` for callout blocks (NOT inside lists)
- Pipe tables: `| col1 | col2 |` with header row separator
- `---` for dividers between sections
- Inline `code` for drug doses, lab values, criteria thresholds

Quality bar: each topic must have specific drug names + doses, criteria (e.g. NYHA classes, Killip class, Sgarbossa), and FCPS/MRCP-style pearls. Use tables for differential diagnosis and management strategy.

## Phase 3 — Render to HTML + PNG

Use `render_topic.py` (in this skill's `scripts/`). It takes a markdown file, parses it into Sea Knowledge style sections, renders to HTML, and screenshots via headless Chromium to a PNG.

```bash
python3 scripts/render_topic.py \
  --slug "cardiac-investigations" \
  --title "Cardiac Investigations" \
  --markdown-file /root/sk-content/cardiac-investigations.md \
  --out-dir /mnt/tb/Sea-knowledge
```

Outputs `<out-dir>/<slug>/<slug>.{md,html,png}`.

**CRITICAL — `render_topic.py` only recognises `## N. Title` numeric headers (Pitfall 51).** If your source markdown uses `## Learning Objectives`, `## Aetiology`, etc., the renderer silently produces blank PNGs. Always run a pre-processor (see Pitfall 51) before bulk rendering unfamiliar sources.

**Important: the IHD reference is 7.9K chars and fits one A4 page. Topics with 10-13K chars will produce a 1.5-2.5 A4-page tall PNG — that's fine, the renderer auto-grows the page height.** Don't try to fit content into a fixed-height A4 by truncating; let the page grow.

**Visual style — Sea Knowledge palette** (hard-coded in the HTML template, edit `render_topic.py`'s `:root` CSS if you need to tweak):
- Rose: `#c09db1` / deep `#996677` / soft `#f3dde4`
- Cream: `#faf1d0` / deep `#e0b13f`
- Sage: `#bfc3a6` / deep `#8a9a72`
- Coral: `#f68773` / deep `#d65a4a`
- Paper: `#fdf8ee`, ink: `#3b2a32`

The 10 sections are wrapped in a `.sec` card with rose-soft gradient header. The page header has the brand logo (wave/anchor SVG) + "CARDIOLOGY" tag + topic name. Footer has the brand + topic + version.

## Phase 4 — Publish to Notion

Use `notion_upload.py` (in this skill's `scripts/`). For each topic, three calls per topic:

```python
# 1. Create the file upload slot
upload_id = upload_png(slug)   # 3-step: create slot, multipart POST bytes, return id

# 2. Create the sub-page with markdown body
page_id, page_url = create_page_with_image(
    parent_id=HUB_ID,
    title=topic_title,
    md_path=local_md_path,
    file_upload_id=upload_id
)

# 3. Append the image block
# (the create_page_with_image helper does this in the same call)
```

The 3-step file upload has a documented Notion API gotcha (Pitfall 52): step 2 must be `multipart/form-data` with field name `file`, and the `Notion-Version` header is required on the upload URL too. The `upload_png()` helper in `notion_upload.py` handles this.

**Always paginate `/blocks/{id}/children` queries with `start_cursor` when the page has more than 100 blocks (Pitfall 53).** Single `?page_size=100` returns only the first 100 children. Sea Knowledge sub-pages have 150-300 blocks each — without pagination, verification scripts will silently report "0 image blocks" and you'll think the upload failed when it actually succeeded.

**Rate limit:** Notion API is ~3 requests/second. Add a 300ms sleep between topics.

## Phase 5 — Build the numbered index on the hub

After all N sub-pages are created:

1. Get the hub's current children: `GET /v1/blocks/{HUB_ID}/children` (paginate if > 100!)
2. Find and **delete** every `child_page` block (they were auto-added when sub-pages were created — you don't want them AND a manual index)
3. Add a numbered index as `numbered_list_item` blocks where each item's rich_text is a `mention` of the sub-page:

```json
{
  "object": "block",
  "type": "numbered_list_item",
  "numbered_list_item": {
    "rich_text": [
      {"type": "mention", "mention": {"type": "page", "page": {"id": "<sub_page_id>"}}},
      {"type": "text", "text": {"content": "  —  Sea Knowledge infographic + study notes"}}
    ]
  }
}
```

4. Optionally append a callout header + divider + footer description (these go to the END, not the top — Notion API is append-only)

The full numbered-index pattern is in the `notion` skill's "Build a study hub with a numbered index" section.

## Phase 6 — Disease-level expansion (when N > ~50)

When the user wants disease-level granularity (one sub-page per disease, ~100-500 topics per chapter), the flat hub/disease layout gets unwieldy. Add a numbered hub layer:

```
/mnt/tb/Sea-knowledge/
└── 16. Cardiology/                  ← chapter (e.g. "16." prefix)
    ├── 16.1. Acute Coronary Syndromes/   ← hub (e.g. "16.1")
    │   ├── 16.1.1. atherosclerosis-pathogenesis/   ← disease (e.g. "16.1.1")
    │   │   ├── atherosclerosis-pathogenesis.md
    │   │   ├── atherosclerosis-pathogenesis.html
    │   │   └── atherosclerosis-pathogenesis.png
    │   ├── 16.1.2. plaque-rupture-and-thrombosis/
    │   └── ... (30 more)
    ├── 16.2. Adult Congenital Heart Disease/
    └── ... (16 more hubs)
├── xtra/                             ← duplicates / broken slugs
└── README.md                         ← structure status
```

### 6a. Identify the canonical disease list

Source the ground-truth list from one of:
- A `*MOC.md` or `*Hierarchy.md` at the chapter root (Davidson chapters use `Davidson Chapter 16 - Cardiology Hierarchy.md`)
- A flat `all_disease_topics.json` (build it once via `build_batches.py` — see scripts/) with shape:
  ```json
  [
    {"idx": 1, "parent_slug": "cardiac-investigations", "parent_num": 1,
     "hub": "Clinical Assessment", "topic": "Cardiovascular history taking",
     "slug": "cardiac-investigatio--cardiovascular-history-taking--001",
     "source_file": "..."}
  ]
  ```
- If neither exists, enumerate `*/<topic>.md` files in each chapter sub-folder

**Build the prefix→hub map** (slug prefixes don't always match hub folder names exactly):
```python
PREFIX_TO_HUB = {
    'acute-coronary-syndr':  'acute-coronary-syndromes',
    'adult-congenital-hea':  'adult-congenital-heart-disease',
    'cardiac-disease-in-s':  'special-populations',  # often differs!
    'diseases-of-aorta-pe':  'aortic-diseases',       # often differs!
    # ... etc
}
```

### 6b. Generate content in parallel batches

For 100-500 topics, `subagent-batch-note-conversion` is too slow. Use the **3-parallel-subagent × N-wave** pattern:
- Wave 1: 3 subagents × 5-6 topics each (~10 min) — first attempt
- After wave 1 returns, dispatch wave 2 for topics still missing
- **Time budget per wave: 10 minutes max**, otherwise subagents are still running when the parent's "next-step" planning kicks in
- If wave 1 times out, fall back to writing remaining topics **directly in the parent context** (slower per-topic but reliable)

### 6c. Render with subagent or in-loop

For 100+ topics, subagent-based rendering is faster but flaky. Use **single-process in-loop rendering** with a 120s per-render timeout:

```python
for topic in canonical_list:
    disease_dir = hub_dir / f'{hub_num}.{counter}. {topic_name}'
    disease_dir.mkdir(exist_ok=True)
    shutil.copy2(source_md, disease_dir / f'{topic_name}.md')

    try:
        subprocess.run(
            ['python3', 'render_topic.py',
             '--slug', topic_name, '--title', topic_title,
             '--markdown-file', str(md_path),
             '--out-dir', str(disease_dir)],
            timeout=120
        )
    except subprocess.TimeoutExpired:
        log_to_xtra(topic)  # see Pitfall 44
```

### 6d. Publish in waves

Notion rate-limit is ~3 req/sec, but `POST /pages` + file upload = 3 calls per topic. For 330 topics, that's ~1000 API calls = 5-10 minutes if non-blocking, but full-process often OOMs at ~150 topics. Split into waves of 50-100:

```bash
python3 notion_upload_diseases.py 0 100   # wave 1
python3 notion_upload_diseases.py 100 200 # wave 2
python3 notion_upload_remaining.py        # catches any failures
```

Each wave should print success/failure per topic and write a results JSON for the next wave to skip.

## Phase 7 — Static site generator (when user asks for a website)

When the user says "make a website", "deploy", "see all at once", or "like hermes telemetry" — they want a browsable static site that mirrors the Notion study hub, runs in Docker, and deploys to Vercel. The site is built from the same `chapters/` tree, so it's a derived view of Phase 3 output (no extra content generation needed).

**Site location:** `/mnt/tb/Sea-knowledge/#<backup-name>/site/` — co-located with the chapter tree. The `#` prefix is a literal hash character, **not a shell comment**; always quote the path or it gets eaten by shell globbing (`find /mnt/tb/Sea-knowledge/#MedSea` → "no such file or directory"). Workarounds:
- Use single-quoted paths: `cd "/mnt/tb/Sea-knowledge/#MedSea"`
- Or `cd` from a parent dir: `cd /mnt/tb/Sea-knowledge && cd '#MedSea'`
- The build script should hardcode the path as a Python string, never build it from shell tokens

**Three deliverables (all from one Python generator script):**

1. **`site/index.html`** — landing page with one card per chapter (color accent strip, stats: hubs/topics/PNGs, 4 thumbnail preview images, primary CTA → chapter page + secondary CTA → Notion hub URL)
2. **`site/<chapter-slug>/index.html`** — chapter SPA (sidebar + main pane). The SPA loads `<chapter-slug>/topics.json` once, then renders topics instantly into the right pane when clicked from the sidebar
3. **`site/<chapter-slug>/diseases/<topic-slug>/{topic.md,topic.png}`** — source PNG + MD per topic (download buttons in topic detail)

**Phase 7 v2 redesign (2026-06-18):** moved stats into a sticky header pill bar, added a 32-chapter Davidson dropdown (5 LIVE + 27 SOON), removed the landing-page hero, restructured chapter pages as SPAs with sidebar topic list. See `references/medsea-static-site-v2-spa-redesign-log-2026-06-18.md` for the redesign details + Pitfalls 65-70.

**Generator pattern** (`scripts/site/build_site.py`, ~700 lines v1 / ~1046 lines v2, self-contained — no JS framework, no npm):
- `PAGE_CSS` constant with all styling inlined (`:root` CSS vars for the dark theme + chapter accent color override)
- `find_files()` walks `chapters/<slug>/diseases/` and accepts two on-disk patterns: (A) `<hubnum>.<idx>-<slug>/{topic,slug}.{md,png,html}` (cardiology, nephrology) and (B) `<hubnum>.<idx>-<slug>.{md,png}` flat (respiratory, endo, gastro)
- `render_md_to_html()` is a small ~80-line Markdown→HTML converter: handles `## N.`, `> ` callouts, pipe tables, bullet/ordered lists, `**bold**` `*italic*` `` `code` ``, Obsidian-style `<callout>` tags (stripped), and YAML frontmatter (stripped)
- `chapter_summary()` returns `n_topics`, `n_pngs`, `n_hubs`, `by_hub`, `hub_names` (from `manifest.json`)
- `write_index()` / `write_chapter_spa()` / `write_topic_page()` are pure string-templating functions; output goes to `site/`
- `copy_assets()` copies PNGs and MDs into the `site/` tree, preserving the source's folder/flat structure so PNG URLs in the HTML resolve

**PNG-URL convention in the HTML:** always absolute paths (`/16-cardiology/diseases/...`) so navigation links work regardless of the current page's directory. nginx `try_files` handles directory-`index.html` lookups so URLs can drop the trailing `.html` and `/16-cardiology/` works the same as `/16-cardiology/index.html`.

**Dockerfile** (root of repo, ~15 lines):
```dockerfile
FROM nginx:alpine
COPY site/ /usr/share/nginx/html/
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8855
HEALTHCHECK --interval=30s --timeout=3s CMD wget -q --spider http://localhost:8855/ || exit 1
CMD ["nginx", "-g", "daemon off;"]
```
- Use `nginx:alpine` (small, fast, healthcheck via `wget --spider`)
- `EXPOSE 8855` is for documentation only — the actual port binding happens at `docker run -p 0.0.0.0:8855:8855`
- Bind to `0.0.0.0` (not `127.0.0.1`) for LAN access

**`docker/nginx.conf`** (key parts):
```nginx
server {
  listen 8855;
  root /usr/share/nginx/html;
  gzip on;
  gzip_types text/plain text/css application/javascript image/svg+xml;
  location ~* \.(png|jpg|jpeg|webp|svg)$ { expires 7d; add_header Cache-Control "public, max-age=604800, immutable"; }
  location ~* \.html$ { expires 1h; add_header Cache-Control "public, max-age=3600"; }
  location / { try_files $uri $uri/ $uri/index.html /index.html; }
  server_tokens off;
}
```

**Vercel** (`vercel.json`):
```json
{
  "version": 2, "cleanUrls": true, "trailingSlash": false,
  "builds": [{"src": "site/**", "use": "@vercel/static"}],
  "headers": [
    {"source": "/(.*)\\.(png|jpg|webp|svg)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800, immutable"}]},
    {"source": "/(.*)\\.html", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600"}]}
  ]
}
```
- `cleanUrls: true` strips `.html` from URLs (matches the docker convention)
- No build step — Vercel just serves the `site/` directory as-is

**.gitignore for the binary content** — `site/` includes 760 PNGs (~265 MB). Don't commit them to git; the chapters/ tree already has them under `chapters/<slug>/diseases/`. Add to `.gitignore`:
```
site/**/*.png
site/**/*.jpg
site/**/*.webp
```
Keep `site/index.html`, `site/<chapter>/index.html`, `site/topics.json`, and `site/README.md` tracked (they're tiny and document the structure).

**Build + run sequence:**
```bash
cd /mnt/tb/Sea-knowledge/#MedSea
python3 scripts/site/build_site.py    # ~2-3 min for 5 chapters
docker build -t medsea-site:latest .  # ~30s (nginx:alpine cached)
docker stop medsea; docker rm medsea
docker run -d --name medsea -p 0.0.0.0:8855:8855 --restart unless-stopped medsea-site:latest
curl -s -o /dev/null -w "HTTP %{http_code} - %{size_download}b\n" http://127.0.0.1:8855/
```

**Vercel deploy:**
```bash
cd /mnt/tb/Sea-knowledge/#MedSea
vercel deploy --prod   # uses vercel.json, serves site/ statically
```

**Design tokens (use these for the chapter accent strip — match the dark-theme aesthetic of Hermes Telemetry):**
- Background gradient: `linear-gradient(135deg, #0a0e1a 0%, #0f1729 100%)`
- Surfaces: `#111827` (cards), `#1f2937` (nested), `#2d3748` (borders)
- Text: `#e5e7eb` (primary), `#9ca3af` (dim)
- Accent (default): `#38bdf8` (cyan)
- Per-chapter accents: 15=cyan `#06b6d4`, 16=red `#ef4444`, 17=emerald `#10b981`, 18=violet `#a855f7`, 21=amber `#f59e0b`
- Hero gradient text: `linear-gradient(135deg, #38bdf8 0%, #a855f7 50%, #ec4899 100%)` with `-webkit-background-clip: text`
- Stats numerals: monospace `'JetBrains Mono', 'SF Mono', Menlo`
- Card top-accent strip: `::before` with `height: 3px; background: var(--accent-color, var(--accent))`

**Why include this phase in the skill (not a separate skill):** it's the natural completion of the chapter build — without a way to browse all chapters, the user can't get the "at a glance" view they want. The static site is a derived view of the same `chapters/` tree, so no content duplication. The `find_files()` + `render_md_to_html()` patterns are reusable for any future documentation site built from markdown.

## Verification (mandatory)

After publishing, verify each sub-page by reading back via `/pages/{id}/markdown`:

```python
import re
ok = 0
for r in results:
    pid = r['page_id']
    s, data = call("GET", f"/pages/{pid}/markdown")
    md = data.get("markdown", "")
    h2 = len(re.findall(r"^## \d+\.", md, re.M))
    has_image = "X-Amz-Signature" in md
    if h2 >= 8 and has_image and len(md) > 5000:
        ok += 1
print(f"{ok}/{len(results)} pages OK")
```

**Don't trust the `child_page` block count** — use `/markdown` to verify content. The `/blocks/{id}/children` endpoint may return 404 for fresh pages created via the `markdown` field (delayed async indexing). The `/markdown` endpoint is reliable.

**Don't trust a single `?page_size=100` query either** (Pitfall 53). Sea Knowledge sub-pages have 150-300 blocks; an unpaginated query returns the FIRST 100, missing the image block. Always loop with `start_cursor` until `has_more=False`.

**Random-sample spot check (fastest verification, ~5 sec for 9-hub chapter):**
```python
import random
random.seed(42)
sample = []
for h in hub_pages:
    children = fetch_children(h['id'])
    cps = [c for c in children if c.get("type") == "child_page"]
    if cps:
        sample.append((h['child_page']['title'], random.choice(cps)))

all_good = True
for hub_title, c in sample:
    blocks = fetch_children(c['id'])  # paginated
    n_text = sum(1 for b in blocks if b.get("type") in
                 ('paragraph','heading_1','heading_2','heading_3',
                  'bulleted_list_item','numbered_list_item','callout','quote','table'))
    n_image = sum(1 for b in blocks if b.get("type") == "image")
    if n_text < 3 or n_image < 1:
        all_good = False
print(f"All good: {all_good}")
```
This catches image-only pages and zero-content pages within seconds. See `scripts/verify_content_sample.py` for the full pattern.

**Deduplication check (catches stale copies from re-runs):**
```python
from collections import Counter
for h in hub_pages:
    children = fetch_children(h['id'])
    cps = [c for c in children if c.get("type") == "child_page"]
    titles_lower = [c['child_page']['title'].lower() for c in cps]
    cnt = Counter(titles_lower)
    dups = {t: n for t, n in cnt.items() if n > 1}
    if dups:
        # archive older duplicates: keep newest by last_edited_time
        groups = defaultdict(list)
        for c in cps:
            groups[c['child_page']['title'].lower()].append(c)
        for title, pages in groups.items():
            if len(pages) > 1:
                sorted_pages = sorted(pages, key=lambda p: p.get('last_edited_time', ''))
                for stale in sorted_pages[:-1]:
                    archive_page(stale['id'])  # PATCH /pages/{id} with archived:true
```
Stale duplicates usually come from a prior run that was killed mid-batch — the script must be idempotent (Pitfall 57).

## Pitfalls / Lessons learned

### ❌ Don't try to insert blocks at the TOP of the hub
Notion's `PATCH /v1/blocks/{id}/children` only supports an `after` parameter (no `before` / `position: 0`). New blocks always go to the end. If you add a callout header + numbered index, they'll appear AFTER the auto-added child_page blocks. Workaround: delete the auto child_page blocks first, then add the index — the index becomes the hub's primary content.

### ❌ Don't make a sub-page AND a manual `link_to_page` block for the same page
The auto-added child_page block on the parent already serves as the link. Adding a manual one duplicates it. Pick one path: either rely on the auto child_page listing (simple but unordered), or delete them and build a clean numbered index (cleaner UX, more code).

### ❌ Don't try to fit 10-13K char content into a single A4 page
The renderer auto-grows the page height. Truncating content to fit A4 destroys the quality. A 2-page-tall infographic is fine — the user gets one continuous image they can scroll/zoom.

### ❌ Don't skip the content-quality audit after subagent round
Subagents can produce templated placeholders even when told to be specific. The validation regex from `subagent-batch-note-conversion` (checking for "Drug A B. Drug B C." patterns) is reusable here.

### ⚠️ The 10-section structure is the user's spec
The user expects 10 sections in this exact order. Deviating (e.g. adding an 11th "References" section, or merging Differential with Investigations) breaks the visual rhythm of the study hub. Stick to the spec.

### ⚠️ Save the reference scripts alongside the output
Future sessions will need `render_topic.py`, `notion_upload.py`, and `topics.py` to add more chapters. Don't put them in `/tmp/`. The user keeps their work in `/root/sea-knowledge-infographics/` and the archive in `/mnt/tb/Sea-knowledge/`.

### ❌ `render_topic.py` nests output one level too deep (Pitfall 41)
Calling `render_topic.py --out-dir <D> --slug <S> --markdown-file <M>` produces:
```
<D>/<S>/<S>/<S>.{md,html,png}
```
NOT `<D>/<S>/<S>.{md,html,png}` as you might expect. The script creates a slug-named subdir inside the slug-named output dir, then puts files inside that. After a bulk render batch, you MUST flatten — write `scripts/flatten_renders.py` and run it on the output root. Without this, the disease folder only has the original `md` and looks "incomplete" to a structural verifier.

```python
# flatten_renders.py pattern
for hub_dir in OUT_ROOT.iterdir():
    for disease_dir in hub_dir.iterdir():
        for nested in disease_dir.iterdir():
            if nested.is_dir():
                for f in nested.iterdir():
                    target = disease_dir / f.name
                    if target.exists(): target.unlink()
                    f.rename(target)
                nested.rmdir()
```

### ❌ Slugs starting with `-` break argparse (Pitfall 42)
Some canonical disease slugs start with `-` (e.g. `cardiac-emergencies---adhf-management--313` derives topic name `-adhf-management` from the `--` separator). Calling `render_topic.py --slug "-adhf-management"` makes argparse interpret it as a flag. **Always sanitize before passing to `--slug`**:

```python
slug = raw_slug.lstrip('-').replace('--', '-').rstrip('-')
```

The same sanitization must be applied when the topic name becomes a folder name — leading hyphens break shell tab-completion and look ugly in the directory listing.

### ❌ Chromium hangs on a small fixed set of slugs (Pitfall 43)
On this machine, headless Chromium consistently hangs (no output, no exit) on:
- `adhf-management` (cardiac-emergencies topic)
- `cross-link-00-index-medicine-moc-00-index-davidson-chapter-r` (cardiac-emergencies cross-link topic)

Even with 300s timeout, these never return. If a topic hits the 90s soft timeout, **move it to `/mnt/tb/Sea-knowledge/xtra/`** as `md`-only and document in the chapter README. Don't keep retrying — the chromium process leaks GPU memory and can OOM the system on subsequent runs.

### ❌ Never `rm -rf` an entire hub folder during restructuring (Pitfall 44 — SEVERE)
During the Phase 6 restructure (flat 330-disease folder → numbered hub/disease tree), I had a `bash` script that was supposed to clean up an empty `16. Cardiology ` directory (with a trailing space) but the shell-glob expansion broke on the space and the command targeted the live, populated `16. Cardiology/` directory. Result: all 330 disease folders + 17 hub folders were deleted.

**Lesson (carry this everywhere, not just for Sea Knowledge):**
- **NEVER** `rm -rf` a directory without first running `ls -A <target>` to verify it matches your intent
- **NEVER** use shell `rm` with a glob/expansion when the path contains a space — use Python `shutil.rmtree()` or `pathlib.Path` with explicit quoting
- **ALWAYS** have a source-of-truth backup that lets you rebuild from scratch (e.g. keep `/root/sk-content/` as the canonical markdown source; treat `/mnt/tb/Sea-knowledge/` as a derived output)
- **Test the rm command on an empty mock first** if the target is large
- If you do delete by accident, **stop immediately**, identify the canonical source, and rebuild — don't keep modifying the broken state

Recovery worked because `/root/sk-content/` had all 330 mds; rendered 309/330 successfully on retry, plus 21 re-renders with sanitized slugs brought it to 328/330 (the 2 chromium-hangers were accepted as md-only in `xtra/`).

### ⚠️ Orphan background processes will collide with re-launched scripts (Pitfall 45)
If a background `python3 script.py | tee log` process appears to die but the inner Python process is still running, the next `python3 script.py > log 2>&1` will run **concurrently** with the orphan. Two processes writing to the same directory tree = silent data loss (one moves files while the other is creating them).

After every background-process launch, verify it actually exited:
```bash
ps aux | grep <script_name> | grep -v grep
```
If a process is orphaned, `kill -9 <pid>` it before relaunching. This caught me — I lost 30 seconds to a 2-process race condition during the 330-topic recovery.

### ❌ Canonical `idx` is global, disease folder counter is per-hub local (Pitfall 46)
The `all_disease_topics.json` canonical list has a **global** `idx` field running 1..330 across the whole chapter. But disease folders in the numbered tree use a **per-hub local counter** starting at 1 within each hub:
```
global idx 1-24   → cardiac-investigations    → local counter 1-24   → folders 16.7.1..16.7.24
global idx 25-54  → acute-coronary-syndromes  → local counter 1-30   → folders 16.1.1..16.1.30
global idx 71-102 → heart-failure             → local counter 1-32   → folders 16.11.1..16.11.32
```
Don't compute `expected_prefix = f"{num}.{d['idx']}."` — it'll be `16.11.71.` for heart-failure topic 1, but the actual folder is `16.11.1.`. Always translate global idx → local counter:
```python
hub_diseases = [dd for dd in canonical if dd['parent_slug'] == parent_slug]
local_counter = next((i for i, dd in enumerate(hub_diseases, start=1)
                      if dd['idx'] == d['idx']), None)
expected_prefix = f"{num}.{local_counter}."
```
If you skip this step, the script will silently find 0 disease folders and you'll waste an iteration debugging.

### ❌ Leading-hyphen disease folder names break `ls` and tools (Pitfall 47)
After Pitfall 42 sanitization, the `slug` passed to `render_topic.py` is clean. But the **folder name** (built as `f"{num}.{counter}. {clean_topic}"`) still has a leading space + hyphen when the original topic starts with `-`:
```
folder: "16.6.4. -adhf-management"
```
This breaks:
- `ls` output (visually ugly)
- `find -name` patterns (leading `-` looks like a flag)
- Some shell tools that don't quote properly
- The renderer leaves a stale `adhf-management/` nested dir inside the leading-hyphen folder

**Fix:** after rendering, rename the folder to remove the leading `" -"`:
```python
# cleanup_16_6.py pattern
for disease_dir in hub_path.iterdir():
    if disease_dir.name.startswith('16.6.'):  # or any hub with leading-hyphen topics
        new_name = disease_dir.name.replace('. -', '. ')
        if new_name != disease_dir.name:
            disease_dir.rename(disease_dir.parent / new_name)
```
Apply this same sanitization when computing folder names from canonical topic strings — the rule is: **no folder name should ever start with `-`**.

### ⚠️ User's folder-numbering convention: `<chapter>.<hub>.<disease>` (rule)
The user's exact request was: *"move them to /mnt/tb/Sea-knowledge/16. Cardiology and create folder of topic like 16.1 of all 16 hub then move to sub topic with folder like 16.1.1, 16.1.2 like this and move unnecessary/duplicate topic to /mnt/tb/Sea-knowledge/xtra"*.

This is a **named convention**, not negotiable:
- Chapter root: `/mnt/tb/Sea-knowledge/16. Cardiology/` (note the trailing space in the empty marker folder, then renamed)
- Hub folders: `16.1. <Hub Display Name>`, `16.2. <Hub Display Name>`, ... (sorted numerically, not alphabetically — `16.1, 16.2, ..., 16.10, 16.11, ...` not `16.1, 16.10, 16.11, 16.2`)
- Disease folders: `16.N.<local-counter>. <topic-slug>` where `local-counter` is **per-hub local** (resets to 1 in each hub — see Pitfall 46)
- Junk: anything that doesn't fit the canonical 330 → `/mnt/tb/Sea-knowledge/xtra/`

**Don't invent your own numbering scheme** (e.g. alphabetical hubs, or chapter-level counter for diseases). The user is explicit about this pattern and uses it for cross-references in the Notion hub.

### ⚠️ Always set up a GitHub backup for any large local content tree (Pitfall 48)
After the Pitfall 44 incident, the user explicitly asked: "create and upload those files in a repo MedSea so that if you unfortunately delete those can restore". This is a one-line request that needs a real GitHub backup pattern.

**Local mirror location:** `/mnt/tb/Sea-knowledge/#<backup-name>/` — NOT `/root/<backup-name>/`. The user later asked to "change local backup on /mnt/tb/Sea-knowledge/#MedSea", explicitly moving it from `/root/MedSea/` to be co-located with the live content. The `#` prefix marks it as a sibling of the live chapters, and putting it under `/mnt/tb/Sea-knowledge/` (the same mount as the content it backs up) means the backup inherits the same storage guarantees as the original.

**Pattern** (see `references/medsea-github-backup-pattern.md` for full template):
```
/mnt/tb/Sea-knowledge/#MedSea/      # local mirror (co-located with live content)
├── README.md                      # structure + restore instructions
├── .gitignore                     # exclude __pycache__/, .DS_Store, etc.
├── scripts/
│   ├── build_backup.py            # takes REPO_ROOT as argv[1] (script-relative)
│   ├── sync.sh                    # uses $(dirname $0)/.. for REPO path
│   ├── restore.sh                 # same — works from any install location
│   └── restore_diseases.py        # python helper for hub-nested restore
└── chapters/<N>-<specialty>/
    ├── manifest.json              # canonical list + render status
    ├── README.md
    ├── hubs/                      # hub-level .md files
    ├── diseases/                  # flat-named disease folders (16.N.M-<slug>/)
    │   └── 16.N.M-<topic-slug>/
    │       ├── topic.md
    │       ├── topic.html
    │       └── topic.png
    └── source/                    # raw markdown from /root/sk-content/
```

**Why flat-named backup (`16.N.M-<slug>/`) + manifest-driven restore:**
- Git tracks moves/renames cleanly when folder names are deterministic
- Avoids the "folders moved during push" problem that nested backups have
- `manifest.json` records the canonical hub↔disease mapping, so restore can reconstruct the nested tree on demand
- Single source of truth: if the manifest conflicts with the directory, the manifest wins

**Setup checklist (do this ONCE per content domain):**
1. `mkdir -p /mnt/tb/Sea-knowledge/#<backup-name>/chapters/<N>-<specialty>/{hubs,diseases,source}` (note `#` prefix)
2. Write the canonical list to `manifest.json` (every disease entry has `idx`, `subnum`, `parent_slug`, `topic`, `folder`, `has_md`, `has_html`, `has_png`)
3. `cd /mnt/tb/Sea-knowledge/#<backup-name> && git init -q && git branch -M main`
4. `gh repo create <backup-name> --public --source=. --remote=origin --push`
5. Write `sync.sh` (rebuild + commit + push) and `restore.sh` (pull + reconstruct nested tree). **Use script-relative paths** (`REPO="$(cd "$(dirname "$0")/.." && pwd)"`) so the scripts work from any install location — don't hardcode `/root/MedSea` or `/mnt/tb/Sea-knowledge/#MedSea` in script bodies.
6. Add a daily cron: `0 2 * * *` runs `sync.sh`, `deliver: local` (so you get a quiet success report, not a chat ping). Set the cron `workdir` to the backup dir.

**`restore.sh` pattern** — uses the manifest to rebuild the nested tree:
```bash
python3 scripts/restore_diseases.py "$CHAPTER_DIR" "$DEST"
# where restore_diseases.py reads manifest.json and copies each
# diseases/<flat-folder> into <DEST>/<hub_num>. <hub_name>/<subnum>. <clean_topic>/
```

**Test the restore** with `--target /tmp/test_restore` before you trust it. Verify:
- Hubs are in correct subfolders
- Diseases are in their parent hub
- md/html/png counts match expectations
- The `xtra/` files are NOT in the live tree (they're only in `/root/sk-content/`)

### ⚠️ For Bash heredocs with Python inside `set -e`, extract Python to a separate file
Bash heredocs that pass Python via `python3 << EOF ... EOF` are fragile — `set -e` plus the heredoc terminator can cause the Python block to be printed but not executed (the heredoc just becomes a no-op). Always:
- Write Python helpers to a separate `scripts/<name>.py` file
- Call them from bash as `python3 scripts/<name>.py "$ARG1" "$ARG2"`
- Take args via `sys.argv`, not stdin

This is what I did with `scripts/restore_diseases.py` in MedSea — it made `restore.sh` reliable where the inline heredoc version was silently broken.

### ❌ Don't put the GitHub backup under `/root/` — co-locate it with the content (Pitfall 49)
The first version of MedSea lived at `/root/MedSea/`. The user immediately asked to "chenage local backup on /mnt/tb/Sea-knowledge/#MedSea" — moving it under the same mount as the live content it backs up.

**Why this matters:**
- `/mnt/tb/` (ext4, 916GB) is the user's primary content mount. `/root/` is on the system disk and may be smaller, on tmpfs, or have different backup/disk-rotation policies.
- If `/mnt/tb/` is the canonical place for Sea Knowledge content, the backup should be on the **same mount** so a mount failure takes both down together (and a successful mount means the backup is also available).
- The `#` prefix visually distinguishes it as a non-content artifact while keeping it adjacent. Other future backup repos (e.g. `#Medsurg`, `#Paeds`) follow the same pattern.

**Pattern for any future content-tree backup:**
```bash
# WRONG: split across mounts
mkdir -p /root/<backup-name>

# RIGHT: co-located with content, prefixed to mark as non-chapter
mkdir -p /mnt/tb/Sea-knowledge/#<backup-name>/
```

The cron job that runs the backup should set `workdir` to this location, and scripts should use `$(dirname "$0")/..` to resolve their own location — never hardcode `/root/...` or `/mnt/tb/...` in script bodies.

### ⚠️ When `bg + tee log` doesn't show output, the python child may still be running (Pitfall 50)
`background=true` with `2>&1 | tee /tmp/log` reports exit_code 0 from the wrapper, but the actual `python3` child process may still be running. If you relaunch based on the apparent exit, two processes will write to the same directory tree simultaneously — silent data loss.

**Detection + cleanup pattern:**
```bash
# After any background launch, verify the child actually died
ps aux | grep <script_name> | grep -v grep
# If a child is orphaned:
kill -9 <pid>
# Then relaunch
```

**Better: avoid the issue entirely** by using `notify_on_complete=true` for long-running bounded tasks. The system pings you once on exit, eliminating the need to poll. Reserve bare `background=true` for long-lived processes that never exit (servers, watchers).

For 30-min chapter uploads (149 topics × ~10s each), the right pattern is:
```bash
# foreground run
python3 -u upload.py > /tmp/upload.log 2>&1; echo "EXIT=$?" >> /tmp/upload.log
```
with `timeout=600+` and `notify_on_complete=true`. The session tool will block until the upload finishes or its 10-min foreground cap hits. If 10 min isn't enough, you'll get a notification and can resume.

### ❌ Renderer requires `## N. Title` numeric headers — raw source produces blank PNGs (Pitfall 51)
`render_topic.py`'s `parse_markdown_to_html` only creates `sec` blocks from headers matching `^## \d+\. `. Source files with `## Learning Objectives`, `## Aetiology`, `## Clinical Features`, etc. produce **blank PNGs** — header + footer only, no body sections. The script doesn't error, it just silently drops every non-numeric section. This bit me hard on Chapter 15 (Nephrology) after the cardiology pipeline worked — the first upload published 49 blank images to Notion because the nephrology source used raw `## Section Name` headers, not the cardiology `## 1. Section Name` format that the renderer expects.

**Diagnosis:** PNG size 30-60KB → 90% chance it's this bug. Spot-check with the rendered HTML and grep for `<div class="sec">` — if 0, the headers were never recognized.

**Fix — pre-processor (write to /tmp/preprocess.py):**
```python
import re
from pathlib import Path

def preprocess(src_path, out_path):
    raw = src_path.read_text()
    # 1. Strip YAML frontmatter
    raw = re.sub(r'^---\n.*?\n---\n', '', raw, flags=re.DOTALL)
    # 2. Auto-number `## ` headers (but not `### `)
    counter = 0
    out_lines = []
    for line in raw.splitlines():
        m = re.match(r'^## (?!#)(.+)$', line)
        if m:
            counter += 1
            out_lines.append(f'## {counter}. {m.group(1)}')
        else:
            out_lines.append(line)
    out_path.write_text('\n'.join(out_lines))

# Run for an entire chapter:
src_dir = Path('/mnt/tb/Medicine/Nephrology and Urology')
dst_dir = Path('/root/nephro-content'); dst_dir.mkdir(exist_ok=True)
for src in src_dir.glob('*.md'):
    preprocess(src, dst_dir / src.name)
```

Run pre-process BEFORE re-rendering. Verify the pre-processed file has `## 1. `, `## 2. `, etc. headers before passing to `render_topic.py`. Cardiology source already lived in `/root/sk-content/` (pre-processed); nephrology was raw. **Always check the renderer output size and HTML body block count before declaring a render successful** — PNG >200KB and `>10` `<div class="sec">` blocks = good. PNG <60KB and 0 `sec` blocks = this bug.

**Detection shortcut:** `ls -la <output>.png` — real content is 400-800KB; blank is 30-60KB. If you see 49 PNGs all under 80KB after a bulk render, stop and re-render after pre-processing.

### ❌ Notion `file_uploads` send endpoint requires multipart/form-data, not raw bytes (Pitfall 52)
When uploading PNGs to Notion via the `/v1/file_uploads` + `upload_url` flow, the send endpoint rejects raw bytes with HTTP 400 `body.file should be defined`. The endpoint expects a real `multipart/form-data` request with a `file` field, like a browser file upload — not just the PNG bytes with `Content-Type: image/png`.

**The correct send pattern (build multipart body manually with uuid boundary):**
```python
import uuid
def upload_png(path):
    # 1. Create slot
    create = http("POST", "https://api.notion.com/v1/file_uploads",
                  data={"filename": path.name, "content_type": "image/png",
                        "content_length": path.stat().st_size})
    upload_id = create["id"]
    send_url = create.get("upload_url") or f"https://api.notion.com/v1/file_uploads/{upload_id}/send"

    # 2. Build multipart/form-data with `file` field
    boundary = f"----NotionBoundary{uuid.uuid4().hex}"
    with open(path, "rb") as f: fb = f.read()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode() + fb + f"\r\n--{boundary}--\r\n".encode()

    h = {"Authorization": "Bearer " + key, "Notion-Version": "2025-09-03",
         "Content-Type": f"multipart/form-data; boundary={boundary}"}
    req = urllib.request.Request(send_url, data=body, method="POST", headers=h)
    with urllib.request.urlopen(req, timeout=120) as resp:
        r = json.loads(resp.read().decode())
    return r.get("id", upload_id)
```

**Symptoms of the wrong approach:**
- `HTTP 400: body.file should be defined` — you sent raw bytes instead of multipart
- `HTTP 400: body failed validation` — usually the boundary was malformed
- `HTTP 415 Unsupported Media Type` — you forgot the Content-Type header

**Embedding the file_upload:** once the slot returns `{id, status: "uploaded"}`, embed via `image.type="file_upload"` + `image.file_upload.id`:
```python
{"type": "image", "image": {
    "type": "file_upload",
    "file_upload": {"id": upload_id},
    "caption": [{"type": "text", "text": {"content": title[:200]}}]}}
```

**Two-step file_uploads trap:** a single-step `POST /v1/file_uploads` with multipart body directly attached to that endpoint (instead of the two-step create+send flow) returns HTTP 400 with a vague validation error. Always do step 1 (JSON metadata) → step 2 (multipart bytes to the returned `upload_url`).

### ❌ `?page_size=100` returns ONLY the first 100 children — pagination is mandatory (Pitfall 53)
Notion's `GET /v1/blocks/{id}/children?page_size=100` returns the first 100 children and **silently drops the rest**. If the page has 150+ blocks (which Sea Knowledge sub-pages routinely do — 200+ blocks is normal for a 10-section study page), any image block beyond position 100 is invisible to an unpaginated verifier.

This bit me on the nephrology hub 15.1 verification: 6 sub-pages had been pre-existing from a prior Notion block-import flow and contained 150+ blocks each. The image block (appended later) landed at position 100-150 — so my single-`page_size=100` verifier reported "0 image blocks per page" and I thought the upload had failed. It hadn't — the images were there, just past block 100.

**Correct paginated pattern:**
```python
def fetch_all(bid):
    url = f"https://api.notion.com/v1/blocks/{bid}/children?page_size=100"
    all_results = []
    while url:
        r = http("GET", url)
        all_results.extend(r.get('results', []))
        if r.get('has_more'):
            url = f"https://api.notion.com/v1/blocks/{bid}/children?page_size=100&start_cursor={r['next_cursor']}"
        else:
            url = None
    return all_results
```

**Symptom:** verifier says "0 images" but a manual `ls` of local PNGs shows the files exist and aren't blank. Or: the published Notion page renders fine in a browser but your verification script reports failure. Always paginate when the page has more than 100 blocks, and always count via the paginated `len(blocks) > 100` check.

**Bonus: image-block deduplication.** When you upload + replace an image on a page that already has one, you may end up with 2-3 image blocks (old + new + a leftover). The dedup pattern: keep the most recently created image block with a matching caption, delete the rest:
```python
images = [b for b in blocks if b.get("type") == "image"]
if len(images) > 1:
    captioned = [(b['id'], b.get('image', {}).get('caption', [{}])[0].get('text', {}).get('content', ''))
                 for b in images]
    # keep the most recent with matching caption, delete the rest
    keep_id = next((bid for bid, cap in reversed(captioned) if cap.startswith(expected[:30])), None)
    for bid, _ in captioned:
        if bid != keep_id:
            http("DELETE", f"https://api.notion.com/v1/blocks/{bid}")
```

### ❌ Pages created with only image blocks = "image-only pages" — use the `markdown` body field, not block append (Pitfall 54)
Notion's `POST /v1/pages` accepts a `markdown` field in the payload that the API auto-converts to blocks (including tables, callouts, code, headings, bullets, numbered lists). This is the ONLY clean way to get rich content onto a page from external markdown. The `PATCH /v1/blocks/{id}/children` block-append API requires you to construct every block in JSON by hand — easy to skip body content if you only meant to append the image.

**This bit me on Chapter 15 Nephrology** when I used an ad-hoc uploader (`/tmp/upload_nephro_v3.py`) that did:
1. Create sub-page with `properties.title` only (no `markdown` field)
2. PATCH children to append just one `image` block

Result: 43/49 Notion pages were **image-only** — header bar + one image + nothing else. The 6 surviving pages from a prior import had full content but the 43 new ones were just `["image"]`. User reported: "many topic only image not text in notion".

**Fix pattern (delete + recreate with markdown field):**
```python
# 1. Identify image-only pages
def is_image_only(page_id):
    blocks = fetch_all(page_id)  # paginated (Pitfall 53!)
    types = [b.get('type') for b in blocks]
    return len(blocks) <= 2 and 'image' in types

# 2. For each image-only page:
#    a. Read the .md source from local archive
#    b. DELETE the existing page (DELETE /v1/blocks/{page_id})
#    c. Re-upload PNG (file_uploads slot expired after 1hr anyway)
#    d. Create new sub-page with `markdown` field = full .md content
#    e. PATCH the new page to append: divider + callout + image block

create_payload = {
    "parent": {"type": "page_id", "page_id": hub_id},
    "properties": {"title": [{"type": "text", "text": {"content": title}}]},
    "markdown": md_content + "\n\n---\n\n> **Infographic PNG attached below** — right-click to download for printing/sharing.\n"
}
r = http("POST", "https://api.notion.com/v1/pages", data=create_payload)
page_id = r["id"]
# then PATCH image block
```

**Why delete + recreate (not just PATCH append text blocks):**
- PATCHing markdown-converted blocks manually is fragile (you have to re-parse the markdown into Notion's block JSON: paragraphs, tables, callouts, etc. — easy to lose structure)
- The `markdown` field is only available at page CREATION, not via PATCH append
- A blank/empty page is worthless; losing the page_id URL is acceptable when the user just published the chapter

**Symptom of this bug:** User opens the Notion page → sees the header bar, then an image, then nothing. A quick `is_image_only(page_id)` check across all 49 pages reveals which ones are broken.

**Detection before upload (preventive):** After the `POST /v1/pages` call, immediately fetch the new page's children and assert the block count > 5 (real 10-section content = 100-300 blocks):
```python
r = http("POST", "https://api.notion.com/v1/pages", data=create_payload)
new_page_id = r["id"]
time.sleep(2)  # brief delay for Notion to index
blocks = fetch_all(new_page_id)
assert len(blocks) > 5, f"page {new_page_id} only has {len(blocks)} blocks — markdown field may have been ignored"
```

**Why this happened despite the skill's correct `notion_upload.py`:** The skill ships a working `notion_upload.py` that uses the `markdown` field. But ad-hoc uploaders written for one-off tasks (often in `/tmp/`) may skip it. **Always use or copy `scripts/notion_upload.py` (this skill) for any Notion publish — don't reinvent with hand-rolled `create_subpage` + `append_image` patterns.**

**Title-matching pitfall when re-uploading:** When the script matches existing Notion pages to local source by title, naive `word.capitalize()` ("Clinical Examination Kidney Urinary Tract") misses prepositions like "of the" / "in" that the original Notion page preserved ("Clinical Examination of the Kidney and Urinary Tract"). 4 of 49 pages in hub 15.1 were missed this way. **Two fixes:**
1. Preserve the original source title verbatim instead of re-deriving it from the slug
2. Or do fuzzy title matching: `title.lower().replace(' of ', '').replace(' in ', '')` before comparison
3. Or query the Notion page directly by ID rather than by title match

### ❌ Bash display layer redaction can corrupt Python source containing `***` (Pitfall 55)
When the user provides an env-var value that includes a literal `***` pattern (often as a redaction marker for an actual secret), bash + certain terminal rendering layers can substitute the pattern in source code as it's written, **breaking the literal string the script was meant to read**.

**Symptom:** Python script that reads `line.split('NOTION_API_KEY=*** ends up with `line.startswith("NOTION_API_KEY=*** — the `***` was substituted by the display layer to the literal value, and the rest of the source line is corrupted (unclosed string, syntax error).

**Workaround — build the prefix programmatically so the literal `***` never appears in source:**
```python
PREFIX = "NOTION" + "_API_KEY" + chr(61)   # chr(61) = '='
key = None
with open('/root/.hermes/.env') as f:
    for line in f:
        if line.startswith(PREFIX):
            key = line[len(PREFIX):].strip()
            break
```

**Same trick for any other secret-shaped value:** `SECRET_HEADER=*** + ": Bearer "` instead of embedding it inline. Build the string at runtime from non-sensitive pieces + an indexed lookup.

**How to detect this is happening:** If your script's source has `line.startswith("NOTION_API_KEY=*** and not line.startswith("#"):` and a syntax error complains about line 24 having an unterminated string, this is the cause. Rewrite the literal pattern using `+` concatenation or `chr()` to avoid the embedded `***` in the source.

### ❌ Chromium hangs (no exit) when source markdown exceeds ~400 lines (Pitfall 56)
`render_topic.py` opens the rendered HTML in headless Chromium and takes a full-page screenshot. For source markdown > ~400 lines (or > ~30 KB on disk), Chromium's page height grows past several A4-pages-worth of pixels and **the renderer process never returns** — even with a 300s timeout. The first sign is `subprocess.communicate(timeout=...)` hanging past 90s with no stdout/stderr and a process that doesn't respond to SIGTERM.

**Symptoms:**
- `render_topic.py` subprocess hangs at 100% CPU, no output, no exit
- Killing the Python wrapper leaves orphan Chromium processes holding GPU memory
- Re-running the same topic immediately works fine — confirms it's a transient page-size problem, not content corruption

**Two-part workaround (use both):**

**1. Truncate long source markdown to the first ~100 lines with a `[Truncated]` footnote** (the first 100 lines reliably render to one tall A4 page without hanging):
```python
def make_truncated_md(src_md: Path, max_lines: int = 100) -> Path:
    text = src_md.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if len(lines) <= max_lines:
        return src_md
    # Try to cut at the next `## ` section header after the midpoint, so we
    # don't slice in the middle of a section.
    cut = max_lines
    for i in range(max_lines, min(len(lines), max_lines + 50)):
        if lines[i].startswith("## ") and i > max_lines // 2:
            cut = i
            break
    truncated = "".join(lines[:cut]) + f"\n\n*[Content truncated for rendering — see {src_md.name} for full text]*\n"
    out = Path(f"/tmp/resp-trunc-{src_md.stem}.md")
    out.write_text(truncated, encoding="utf-8")
    return out
```

**2. Always kill the entire process group on timeout** (Chromium is a child of `render_topic.py`, so SIGTERM to the Python parent leaves Chromium alive):
```python
import os, signal, subprocess
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        preexec_fn=os.setsid)  # new process group
try:
    stdout, stderr = proc.communicate(timeout=30)
except subprocess.TimeoutExpired:
    try: os.killpg(proc.pid, signal.SIGKILL)  # kill the whole group
    except ProcessLookupError: pass
    proc.wait(timeout=5)
```

**Pipeline pattern (use this for any chapter with >50% topics > 30KB):**
```python
TIMEOUT_SECS = 30
TRUNCATE_THRESHOLD = 30_000  # bytes
TRUNCATE_LINES = 100

def run_render(slug, src_md, hub_dir, renderer):
    src_size = src_md.stat().st_size
    actual_md = (make_truncated_md(src_md, TRUNCATE_LINES)
                 if src_size > TRUNCATE_THRESHOLD else src_md)
    cmd = ["python3", renderer, "--slug", slug, "--title", title_from_slug(slug),
           "--markdown-file", str(actual_md), "--out-dir", str(hub_dir),
           "--tag", "Respiratory"]
    # ... subprocess.Popen with setsid + os.killpg timeout, as above
```

Run two pipelines sequentially: first pass with truncation to get 90%+ of topics rendered; second pass re-tries the 5-10% that hung despite truncation (those are usually topics with deeply nested tables or massive inline code blocks — keep the truncated version, accept a small failure rate).

**Detection shortcut:** if a render batch shows `ok=10 skip=20 fail=0` followed by `ok=10 skip=21 fail=9`, the `fail=9` are all chromium hangs. Don't increase the timeout past 60s — they won't finish. Truncate and retry.

**Why this doesn't conflict with the auto-grow-page-height behavior noted in the Phase 3 section:** the renderer auto-grows page height, but Chromium's GPU process crashes or hangs on pages past ~8000px tall (the 400-line × 20-px/line estimate). Truncation caps the page height to one section's worth of content; the full source is still preserved locally in `<hub>/<slug>/<slug>.md` for the user to read in their markdown editor.

### ❌ Creating N hub parent pages before uploading topics — required for multi-hub chapters (Pitfall 57)
When building a multi-hub chapter (10+ hubs, like Davidson Ch 17 Respiratory with 10 heading hubs and 149 topics), the canonical pattern is:

1. **Create the chapter-level parent page** (the user's link) — usually already exists.
2. **Create N hub parent pages under it**, one per topic group. Each hub page has its own `markdown` body describing the hub + a numbered list of its topics. The chapter-level page auto-gets a `child_page` block for each hub.
3. **Create topic sub-pages under each hub**, using the hub's `page_id` as `parent.page_id`.

If you skip step 2 and try to create all 149 topics directly under the chapter page, you get an unmanageable flat list of 149 sub-pages on the chapter page — no grouping, no clean per-hub indexes, no ability to add a hub-level header/footer.

**Creation pattern (use the `markdown` field — Pitfall 54):**
```python
def create_hub_page(chapter_id, hub_num, hub_name):
    title = f"{hub_num}. {hub_name}"
    md = (f"# Davidson Chapter 17 — {hub_name}\n\n"
          f"Sea Knowledge study notes for {hub_name}.\n\n"
          f"Hub ID: {hub_num}\n\nTopics: see child pages below.\n")
    return http("POST", "https://api.notion.com/v1/pages", data={
        "parent": {"type": "page_id", "page_id": chapter_id},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "markdown": md,
    })["id"]
```

**Always check for existing hubs first** to make the script re-runnable:
```python
hub_ids = {}
existing = [b for b in fetch_children(CHAPTER_HUB_ID) if b.get("type") == "child_page"]
for c in existing:
    title = c.get("child_page", {}).get("title", "")
    for h in HUBS:
        if title.startswith(f"{h['num']}. {h['name']}"):
            hub_ids[h['num']] = c["id"]
            break
for h in HUBS:
    if h['num'] in hub_ids: continue
    hid = create_hub_page(CHAPTER_HUB_ID, h['num'], h['name'])
    hub_ids[h['num']] = hid
    time.sleep(1)
```

This is also what makes a re-run safe — the script won't create duplicate hub pages if it crashes and restarts mid-batch.

**Topic-to-hub mapping** comes from the manifest built in Phase 1 (the `hub_num` field on each topic). Without that field, you'd have to infer the hub from the topic's parent folder name or prefix — error-prone, especially when hub folder names have spaces (`"17.4. Airway Diseases"`).

### ❌ Naive title comparison misses prepositions ("of the", "in", "and") when re-uploading (Pitfall 58)
When the script needs to find an existing Notion page that corresponds to a local topic (e.g. to swap a blank PNG for a real one, or to replace image-only content with full markdown), simple slug-based title reconstruction misses any prepositions the original Notion page preserved:

| Local slug | Naive `word.capitalize()` | Real Notion title |
|---|---|---|
| `clinical-examination-kidney-urinary-tract` | "Clinical Examination Kidney Urinary Tract" | "Clinical Examination **of the** Kidney **and** Urinary Tract" |
| `blood-tests-renal-disease` | "Blood Tests Renal Disease" | "Blood Tests **in** Renal Disease" |

**Two fixes, in order of preference:**

1. **Preserve the original source title verbatim in the manifest** when building it. Read the first `# H1` line of the source `.md` — that's usually the canonical title with all prepositions intact. Store it as `topic['title']` and use that for all Notion API calls, never re-derive from the slug.

2. **If you can't preserve, do fuzzy word-overlap matching** instead of strict string comparison:
   ```python
   def find_page_by_slug(children, target_title):
       target_words = set(target_title.lower().split())
       best, best_score = None, 0
       for c in children:
           if c.get("type") != "child_page": continue
           existing = c.get("child_page", {}).get("title", "").lower()
           overlap = len(target_words & set(existing.split()))
           if overlap >= max(2, len(target_words) // 2) and overlap > best_score:
               best, best_score = c, overlap
       return best
   ```

The word-overlap pattern is what the nephrology hub 15.1 retry script used to find the 4 missed pages (where my naive `title.lower() == candidate.lower()` had failed). Without it, 4/49 pages were silently skipped and stayed image-only.

**Symptom:** script reports `NO EXISTING PAGE: <title>` for topics that visibly exist on Notion. Re-running won't fix it (the title comparison is deterministic). The fix is the fuzzy matcher above.

### ❌ Custom `http()` helper that returns a parsed dict is NOT a context manager (Pitfall 59)
When writing an ad-hoc uploader, it's tempting to wrap `urllib.request.urlopen` in a helper that parses the response and returns a dict:

```python
def http(method, url, data=None, ...):
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())
```

This returns a `dict`, not a context manager. **Don't use it with `with`:**

```python
# WRONG — TypeError: 'dict' object does not support the context manager protocol
with http("GET", url) as r:
    data = json.loads(r.read().decode())
```

Call it as a plain function and assign the result:
```python
# RIGHT
data = http("GET", url)
```

**Symptom:** `'dict' object does not support the context manager protocol` — typically a TypeError in `fetch_children()` or similar helper. The fix is to convert all `with http(...) as r:` to plain `data = http(...)`.

**Note:** the canonical `notion_upload.py` in this skill's `scripts/` uses `with urllib.request.urlopen(req) as r:` (the real context manager) and then `r.read().decode()` to get the body — that's correct because `urlopen` is a real context manager. The bug only appears when you write your own `http()` helper that hides the urlopen behind a `return` statement. The two patterns are easy to mix up.

### ❌ Notion rejects `markdown` + `children` in the same `POST /v1/pages` call (Pitfall 60)
Notion's `POST /v1/pages` payload accepts either a `markdown` field OR a `children` array — never both. The exact error from the API is:

```
HTTP 400 validation_error: Cannot specify 'markdown' together with 'content' or 'children'. Use one content format per request.
```

This is a sister pitfall to Pitfall 54 (use `markdown` to avoid image-only pages). The skill's `notion_upload.py` correctly does it in 2 steps:

```python
# Step 1: create page with markdown (rich content)
create_payload = {
    "parent": {...},
    "properties": {"title": [...]},
    "markdown": md_content,  # ← full content
}
r = http("POST", "https://api.notion.com/v1/pages", data=create_payload)
page_id = r["id"]

# Step 2: append the image block (separate call)
img_block = {"type": "image", "image": {"type": "file_upload",
            "file_upload": {"id": file_upload_id}}}
http("PATCH", f"https://api.notion.com/v1/blocks/{page_id}/children",
     data={"children": [img_block]})
```

**The wrong way** — combining both in one POST (404 page returned with explicit error):
```python
# WRONG
payload = {
    "parent": {...},
    "properties": {"title": [...]},
    "markdown": md_content,
    "children": [img_block],  # ← 400 error: cannot combine with markdown
}
r = http("POST", "https://api.notion.com/v1/pages", data=payload)
```

**Why this matters in practice:** when writing a fresh uploader, the natural instinct is "create the page with everything at once" — including the image. Don't. The two-step pattern is mandatory, and the error message is exact enough that a quick test catches it immediately.

**Symptom:** all topics fail with HTTP 400 + the exact message above. Re-read the helper — the fix is to remove `children` from the create payload and PATCH them afterward.

### ⚠️ User's standard chapter workflow: "complete fully" + "double check" (rule)
The user uses a stable pattern across chapter requests:
1. Provide Notion hub URL (`https://app.notion.com/p/searex/Chapter-NN-Topic-<32-hex-id>`)
2. Specify the source folder (`/mnt/tb/Medicine/<Specialty>` or `/mnt/tb/medicine <specialty>` — note both casings appear)
3. Expect end-to-end completion: manifest → preprocess → render → upload → verify → backup → push
4. After completion, say something like *"complete fully and double check so that no empty image or text in both local or notion"*

**The "double check" step is mandatory** — the user explicitly wants verification that:
- Local: every topic has a PNG (size > 50KB, no blanks) and a MD
- Notion: every topic has rich content (>= 3 text blocks), exactly 1 image, no duplicates, no image-only pages

A complete chapter with no verification doesn't satisfy the user. The two-key-check pattern is:
```bash
# Local audit
cd /mnt/tb/Sea-knowledge/<chapter> && find . -name "*.png" -size +50k | wc -l  # should == topic count
find . -name "*.png" -size -50k | wc -l                                          # should == 0

# Notion audit (run the verify_content_sample.py + dedup check)
python3 /tmp/verify_<chapter>.py
```

When the user says "complete fully" without specifying a chapter, it's still safe to interpret as the full 5-phase pipeline — they will correct you if they want a different scope.

### ❌ Paths with `#` get eaten by shell globbing and some write tools (Pitfall 61)
The user's chapter backup lives at `/mnt/tb/Sea-knowledge/#MedSea/` — the `#` prefix is a literal hash character (it marks the directory as a non-chapter backup artifact, visually). However, `#` starts a shell comment in bash, so:

```bash
# WRONG — `#MedSea` is parsed as a comment and the path becomes empty
cd /mnt/tb/Sea-knowledge/#MedSea
# bash sees: cd /mnt/tb/Sea-knowledge/   (with a trailing /)
# bash error: cd: /mnt/tb/Sea-knowledge/: No such file or directory

# WRONG — even with `mkdir -p`, the path is corrupted
mkdir -p /mnt/tb/Sea-knowledge/#MedSea/site/scripts
# The `#MedSea/...` part is dropped; only `site/scripts` is created

# RIGHT — single-quote the path, or split the cd
cd "/mnt/tb/Sea-knowledge/#MedSea"
cd /mnt/tb/Sea-knowledge && cd '#MedSea'
```

**Symptom:** `cp`, `mv`, `mkdir` silently produce no output but don't create the expected files. `find` reports "no such file or directory" for files you just wrote.

**Same trap in `write_file` tool:** some shell-bridged write calls interpret the `#` in the target path as a comment delimiter, and the file ends up at the wrong path or not at all. **Workaround:** before writing, run `mkdir -p` from a parent directory and pass the path as a single quoted string. Verify the file landed where expected by running `ls` on the parent dir immediately after.

**Best practice for build scripts:** hardcode the path as a Python string in a `.py` file (which can quote freely), not as a bash string. Then invoke with `python3 scripts/site/build_site.py` from the parent directory.

### ❌ `***` literals in source code get redacted by display layers (Pitfall 62)
A continuation of Pitfall 55: when writing Python source that compares strings containing `***` (e.g. the redacted value of a secret in an env file, or any sentinel pattern), the bash + terminal display layer can substitute the literal `***` with the actual value, breaking the source.

**Symptoms in this session:**
- Python regex `re.search(r'NOTION_API_KEY=*** env_text)` → `SyntaxError: unterminated string literal` at column 27 (the `***` was substituted with a real key, leaving an unclosed string)
- heredoc `python3 << EOF` blocks with `***` patterns → either syntax error or the heredoc becomes a no-op (printed but not executed)
- `write_file` tool paths containing `***` → file written with content missing the asterisks

**Workarounds (use whichever fits):**
1. **Build the sentinel at runtime from non-sensitive pieces:**
   ```python
   sentinel = "NOTION" + "_API_KEY" + chr(61)   # '='
   m = re.search(sentinel + r'(.+)', env_text)
   ```
2. **Read the key from a file written by a separate, simple script** that doesn't contain the literal `***`:
   ```bash
   # /tmp/load_key.py (no asterisks in source)
   import re
   m = re.search(r'NOTION' + '_API_KEY' + '=' + r'(.+)', open('/root/.hermes/.env').read())
   open('/tmp/.notion_key', 'w').write(m.group(1) if m else '')
   ```
3. **Pass the key via an environment variable** (set from the parent context, not embedded in source):
   ```bash
   export NOTION_KEY=$(awk -F'=' '/^NOTION_API_KEY/ {print $2; exit}' /root/.hermes/.env)
   python3 -c "import os; print(os.environ['NOTION_KEY'][:5])"
   ```
4. **Use `awk -F` to extract to a file** without passing the value through any Python heredoc:
   ```bash
   awk -F'NOTION_API_KEY=*** '/^NOTION_API_KEY/ {print $2; exit}' /root/.hermes/.env > /tmp/.notion_key
   ```

**Detection:** if a `python3 -c "..."` or `<< EOF` block suddenly has a syntax error on a line containing `***`, this is the cause. Switch to one of the workarounds above.

### ❌ Long foreground commands hit a session budget; use `background=true, notify_on_complete=true` (Pitfall 63)
The terminal tool has a per-command foreground timeout that can't be raised past a few minutes (the tool's own harness enforces this regardless of `timeout=`). For 25+ minute tasks (149-topic Notion upload, 5-chapter batch render, etc.), the foreground command will be **blocked** with: *"BLOCKED: Command timed out without user response. The user has NOT consented to this action."*

**The right pattern for long-running tasks:**
```python
# terminal(background=true, notify_on_complete=true)
{background: true, command: "python3 -u upload.py > log 2>&1; echo EXIT=$? >> log", notify_on_complete: true}
```
The `notify_on_complete=true` flag tells the system to ping you once when the process finishes, so you can keep working on other things and only context-switch back when the upload is done. **Without `notify_on_complete`, the process runs silently and you'll never know it finished** (just an idle PID in `process list`).

**Forbidden:** `nohup python3 ... &`, `disown`, `setsid` shell wrappers around the foreground command — the harness explicitly rejects these as "shell-level background wrappers". The `background=true` parameter is the only supported way to run async work.

**Forbidden (system):** `subprocess.Popen` inside an `execute_code` block that doesn't have a quick exit — the executor runs in a separate context and can't report back to the parent.

**If `background=true` is also blocked:** ask the user via `clarify` tool with choices to explicitly consent. The system requires user approval for long-running async work that the user can't see executing.

**For Docker:** `docker run -d ...` starts a long-running container, which the system also gates behind user consent. Use `clarify` to get approval before `docker run` for the first time, then subsequent runs (already-built images) are usually fine.

### ❌ Docker container start requires user consent via `clarify` (Pitfall 64)
`docker run -d ...` starts a long-running container with a system service. The terminal tool's safety harness **blocks the command** with: *"BLOCKED: Command required approval (docker restart/stop/kill (container lifecycle)) and was approved by the user."* — the approval flow is non-interactive when the harness is satisfied, but it can also block entirely with *"BLOCKED: Command timed out without user response. The user has NOT consented to this action."*

**The right pattern for first-time container start:**
1. Don't try `docker run` directly
2. Use the `clarify` tool with choices to explicitly request user consent: "Docker container `<name>` will be started on port `<N>`. Approve?"
3. The user responds with approval (often adding "and also support lan" → bind to `0.0.0.0` not `127.0.0.1`)
4. Re-run `docker run` — it usually goes through with the user consent recorded

**Subsequent runs** of an already-approved container start usually go through automatically (the harness remembers approval for the session).

**For first-time container with LAN access:** include the bind address in the consent request: `-p 0.0.0.0:8855:8855` not `-p 127.0.0.1:8855:8855`. The user explicitly asked for LAN support in this session.

**Don't bypass:** `nohup docker run -d ... &` doesn't work — the docker command itself is what gets blocked, not just the shell wrapper. Same for any `docker stop` / `docker rm` / `docker exec` lifecycle command.

### ❌ Don't put the build script inside `site/` if `site/` gets `rmtree()`'d (Pitfall 65)
The Phase 7 v1 build script originally lived at `scripts/site/build_site.py` (one level under the repo root). When the build does `if SITE.exists(): shutil.rmtree(SITE)` at the start of `main()`, the entire `site/` tree — including any nested `scripts/` — gets deleted before the build script can run again.

**Fix:** keep `scripts/site/` as a sibling of `site/`, not a child:
```
/mnt/tb/Sea-knowledge/#MedSea/
├── scripts/site/build_site.py    ← outside site/
├── site/                          ← gets rmtree'd safely
└── site/README.md                 ← re-created by build script (Pitfall 66)
```

**Symptom that bit me:** the v1 build's own source lived at `scripts/site/build_site.py`. When v2's `main()` ran `shutil.rmtree(SITE)`, it deleted the directory the build script itself lived under, so re-running the build was impossible without manual `write_file` recovery.

**Verification after fix:** `ls -la scripts/site/build_site.py site/index.html` must show the build script OUTSIDE the `site/` tree.

### ❌ `rmtree(SITE)` deletes `site/README.md` along with everything else (Pitfall 66)
The README documents how to build + deploy the site. It's tracked in git and committed to the repo at `site/README.md`. But `shutil.rmtree(SITE)` at the top of `main()` deletes it along with everything else.

**Fix:** re-create the README at the top of `main()` after the rmtree. Store the README content as a Python constant (`_README_MD = """..."""`) inside `build_site.py` so the build is self-contained and doesn't depend on any pre-existing files.

```python
_README_MD = """# MedSea Static Site

Auto-generated by `scripts/site/build_site.py`.
...
"""

def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    (SITE / "README.md").write_text(_README_MD)  # ← re-create immediately
    ...
```

Same pattern works for any other small "framework" files in `site/` — favicons, `robots.txt`, PWA `manifest.json`, etc.

### ❌ Inline event-handler strings inside f-strings need `{{`/`}}` doubling for literal braces (Pitfall 67)
The build script generates a `<script>` block inside a Python f-string. JS code has `{` and `}` for blocks/objects. To produce a literal `{` in the output, you must double them in the f-string source: `{{` → `{`, `}}` → `}`.

```python
# WRONG — f-string treats { as expression delimiter; SyntaxError at compile
html += f"""
<script>
function showTopic(localPrefix) {
  const el = document.querySelector(`[data-topic="${localPrefix}"]`);
}
</script>
"""

# RIGHT — literal braces in JS become {{ and }} in f-string source
html += f"""
<script>
function showTopic(localPrefix) {{
  const el = document.querySelector(`[data-topic="${{localPrefix}}"]`);
}}
</script>
"""
```

**Pitfall-within-pitfall:** if you forget to double ONE brace (e.g. the closing one), Python raises `SyntaxError: f-string: invalid syntax` at compile time. The error is unhelpful — it points at the line of the f-string but doesn't tell you which brace you missed.

**Symptom:** after editing an f-string that contains JS code, the Python script suddenly fails to even import with an `f-string: invalid syntax` error. Search the f-string for any single `{` or `}` that should be doubled. The `__` pattern in `\${{...}}` is the tell: it's both an f-string escape (`{{` → `{`) AND a JS template-literal interpolation (`${...}` → interpolated value).

### ❌ Don't compose complex JS expressions as inline `onclick="..."` (Pitfall 68)
My first pass at prev/next buttons had:
```html
<button onclick="location.href='/${{MANIFEST.topics[Math.max(0, MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix) - 1)].local_prefix && MANIFEST.topics[Math.max(0, MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix) - 1)].local_prefix}}?topic=' + (MANIFEST.topics[Math.max(0, MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix) - 1)].local_prefix)">← Prev</button>
```
— unmaintainable, full of bugs, and the `&&` short-circuit produces `undefined` when at index 0.

**Fix:** extract to a named function in the same `<script>` block:
```js
function navigateTopic(dir) {
  if (!MANIFEST || !CURRENT_TOPIC) return;
  const i = MANIFEST.topics.findIndex(x => x.local_prefix === CURRENT_TOPIC.local_prefix);
  const ni = i + dir;
  if (ni < 0 || ni >= MANIFEST.topics.length) return;
  showTopic(MANIFEST.topics[ni].local_prefix);
}
```
Then buttons just call `navigateTopic(-1)` / `navigateTopic(1)`.

**Rule:** any JS that needs more than ~10 chars of logic goes in a named function. Don't inline complex logic in `onclick="..."`.

### ❌ `?topic=<local_prefix>` URL param must match the exact key in `topics.json` (Pitfall 69)
A user testing `?topic=16.1.25` for Cardiology works because `local_prefix` for that topic is exactly `16.1.25`. But for Respiratory, `local_prefix` is `17.1.01` (leading zero). Direct URL entry with `?topic=17.1.1` will NOT match the manifest key.

**Why the leading-zero inconsistency:** the chapter build pipelines use different local-counter conventions:
- Cardiology: `16.1.25` (no leading zero on counter)
- Respiratory: `17.1.01` (2-digit zero-padded counter)

Both are valid, but the user has to know the exact prefix per chapter to use direct URLs.

**Solution options:**
1. Make `local_prefix` URL-safe and stable (always zero-pad to 2 digits: `16.1.025` — but breaks the existing convention)
2. Or: search the manifest for the closest matching prefix on load (fuzzy)
3. Or: accept that the URL uses the canonical `local_prefix` as-is — document the convention

Currently: option 3. Sidebar clicks always use the right prefix because they read `data-topic` from the rendered link, so direct URL entry is the only risk.

### ❌ Browser snapshot / vision tools were down during v2 verification (Pitfall 70)
The vision model returned `Error code: 400 - Unknown Model` repeatedly, and the user's reference image couldn't be auto-described. Worked around by:
- Using `browser_console(expression='document.querySelector(".topic-detail h1")?.textContent')` to verify topic content loaded
- Using `curl -s http://localhost:8855/...` + grep for class counts
- Capturing screenshots anyway (`browser_vision` returned them even when vision analysis failed) and sharing via `MEDIA:` paths

**Rule for "vision is down" sessions:** the user's previous request style is clear enough that text interpretation is usually fine. Don't block on vision; proceed with browser-console DOM probes and trust the user's text feedback. Note the limitation in the final response so the user knows to send more specific feedback if needed.

## Related skills / files

- `notion` — for the 3-step file upload, color format, child_page auto-addition, and the numbered-index pattern
- `subagent-batch-note-conversion` — for the 3-parallel-subagent pattern and content-quality audit
- `medical-fcps-mrcp-note-creation` — for the source-note folder conventions
- `scripts/render_topic.py` — markdown → HTML → PNG renderer (with `## N. Title` requirement — Pitfall 51)
- `scripts/notion_upload.py` — Notion 3-step file upload + page creation (multipart — Pitfall 52)
- `scripts/preprocess_headers.py` — strips frontmatter + auto-numbers `## ` headers (Pitfall 51)
- `scripts/paginate_blocks.py` — paginated Notion block fetcher (Pitfall 53)
- `scripts/verify_content_sample.py` — random-sample verification with text/table/image counts (catches image-only pages)
- `scripts/topics.py` — topic list template
- `scripts/flatten_renders.py` — fixes the renderer's nested output (Pitfall 41)
- `scripts/truncate_long_sources.py` — truncates sources > ~30KB to ~100 lines for safe rendering (Pitfall 56)
- `scripts/process_group_render.py` — subprocess wrapper with setsid + os.killpg for safe chromium kills (Pitfall 56)
- `scripts/site/build_site.py` — static site generator v1+v2 (Phase 7): walks `chapters/`, copies PNGs + MDs, writes `index.html` + per-chapter SPA + per-topic pages with embedded CSS, no JS framework
- `templates/sea-knowledge-style-template.html` — the reusable HTML/CSS template (port of `render_topic.py`'s HTML_TEMPLATE constant)
- `references/cardiology-ch16-session-log-2026-06-17.md` — 16-hub session walkthrough
- `references/cardiology-ch16-disease-expansion-log-2026-06-17.md` — 330-disease expansion + rm-rf recovery walkthrough
- `references/nephrology-ch15-blank-png-fix-log-2026-06-17.md` — Renderer header format + Notion multipart/pagination gotchas
- `references/respiratory-ch17-render-and-publish-log-2026-06-17.md` — 10-hub/149-topic chapter build with truncation + hub-first pattern (Pitfalls 56, 57, 58)
- `references/endo-gastro-batch-log-2026-06-18.md` — Back-to-back 3-chapter batch (respiratory, endo, gastro) confirming the pipeline is now stable; lessons Pitfall 59, 60 + verification random-sample pattern
- `references/medsea-static-site-build-log-2026-06-18.md` — Phase 7 static site v1 (Docker on port 8855 + Vercel); lessons Pitfalls 61-64 (`#` in shell paths, `***` redaction, long-task blocking, Docker consent flow)
- `references/medsea-static-site-v2-spa-redesign-log-2026-06-18.md` — Phase 7 v2 redesign: header stats + 32-chapter dropdown + SPA sidebar+main layout + topics.json manifest; lessons Pitfalls 65-70 (build script location, README preservation, f-string brace doubling, inline onclick bloat, local_prefix URL matching, vision-down verification)
- `references/medsea-github-backup-pattern.md` — how to set up the GitHub backup repo (MedSea) for any large local content tree, with sync.sh + restore.sh + manifest.json pattern
- `references/ch1-9-batch-publish-log-2026-06-18.md` — 9-chapter back-to-back batch (Ch 1-9) using skip_existing to recover from network timeouts; lessons Pitfalls 71-75 (renderer `body_lines` bug, 403 retry, skip-on-fail pattern, BUILT_CHAPTERS slug match, large git push monitoring)
- `references/davidson-25th-edition-chapter-map.md` — 24th→25th edition chapter rename map (15→18, 18→20, 21→22) with the 32-chapter canonical list. Also documents the four newer pitfalls (76, 78, 79, 80) found while building Ch 10-15: Notion reparenting limitation, renderer infinite-loop on unnumbered `##` headers, mermaid mindmap/flowchart rendering, and the 2-level-deep renderer output requiring a flatten step.

### ❌ `render_topic.py` table flush bug — `current["body"]` should be `current["body_lines"]` (Pitfall 71 — REAL BUG, FIXED)
The renderer's table-flush code (around line 310 in `render_topic.py`) tries to append the rendered table HTML to `current["body"]`, but the `current` dict's key is `body_lines` (a list of strings). This raises `KeyError: 'body'` inside the table-rendering branch — for topics WITHOUT tables, the branch is never hit, so the bug stays invisible. For topics WITH tables (oncology, pharmacology, anything with markdown pipe-tables), the renderer **silently produces a short/broken PNG** instead of erroring out.

**Symptom:** ~40% of Ch 8 Oncology topics rendered as 30-60KB PNGs (vs 600-800KB normal) because their TNM-staging / chemotherapy-regimen tables triggered the bug. Other Ch 8 topics with the same source structure rendered fine — confusing.

**Detection:** spot-check PNG sizes after a bulk render. 600-800KB = healthy. 30-60KB = either Pitfall 51 (blank headers — no `## N. `) or this pitfall (table flush). Diff by inspecting the HTML body for `<table>` tags:
```python
from pathlib import Path
for png in Path("/mnt/tb/Sea-knowledge/8. Oncology").rglob("*.png"):
    if png.stat().st_size < 100_000:
        html = png.with_suffix(".html")
        if html.exists():
            body = html.read_text()
            n_sec = body.count('<div class="sec">')
            n_tbl = body.count('<table>')
            print(f"{png.parent.name}: {png.stat().st_size//1024}KB, {n_sec} sec, {n_tbl} tbl")
```

**Fix — patch the renderer (one-line change):**
```python
# /root/sea-knowledge-infographics/render_topic.py around line 310
# WRONG (raises KeyError or appends to wrong key):
#     current["body"] = current.get("body", "") + table_html
# RIGHT (append to the list that the renderer actually uses):
current.setdefault("body_lines", []).append(table_html)
```

The fix is in `render_topic.py` itself, not in the calling script. Re-render any failed topics after patching.

**Why this didn't surface in cardiology / resp / endo / gastro:** those chapters rarely use markdown pipe-tables in topic bodies. Oncology's TNM staging tables, chemotherapy regimens, and prognosis indices are table-heavy — that's why Ch 8 hit it hard. **For any future chapter with frequent tables (pharmacology, haematology, biochemistry, anything quantitative), always spot-check the renderer output for blank/short PNGs before declaring the build done.**

### ❌ Notion `file_uploads` 403/timeout retries — 429 retry isn't enough (Pitfall 72)
The original uploader's retry logic only handled HTTP 429 (with `Retry-After` header). Notion's `file_uploads` send endpoint also returns **HTTP 403 (rate limit, not auth)** and **silent `URLError` / `TimeoutError`** when the upload URL is slow or the network drops. With 3 retries and only 429 handling, a single 403 on topic 2.1.02 (the first 700KB PNG) hangs the whole pipeline.

**Symptom:** the upload script gets to one specific topic, prints `PNG upload fail 2.1.02: {'_error': 403, '_body': '...'}` or hangs in `do_sys_poll` (sleeping on a socket), and stops making forward progress. Subsequent topics never get a chance.

**Fix — broaden the retry classification (both `http()` and `upload_png()`):**
```python
# In http() helper — extend the exception handler:
except urllib.error.HTTPError as e:
    txt = e.read().decode()
    if e.code == 429:
        wait = int(e.headers.get("Retry-After", "3"))
        time.sleep(wait); continue
    if e.code in (502, 503, 504, 403):  # ← add 403 + transient HTTP
        time.sleep(2 ** attempt); continue
    return {"_error": e.code, "_body": txt[:500]}
except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
    time.sleep(2 ** attempt); continue  # ← network-level retry
```

```python
# In upload_png() — same broadening:
for attempt in range(5):  # bump from 3 to 5
    try:
        with urllib.request.urlopen(req, timeout=60) as r:  # 60s, not 120s
            ...
    except urllib.error.HTTPError as e:
        if e.code == 429:
            time.sleep(int(e.headers.get("Retry-After", "3"))); continue
        if e.code in (502, 503, 504, 403):
            time.sleep(2 ** attempt); continue
        return None, {"_error": e.code, ...}
    except (urllib.error.URLError, TimeoutError, ConnectionError):
        time.sleep(2 ** attempt); continue
```

**Detection while a script is running:** the process is alive (`ps` shows it), the log stopped printing new OKs minutes ago, and `cat /proc/<pid>/wchan` shows `do_sys_poll` (Python is sleeping on a socket). That's the hang-on-timeout signature. Kill it (`kill <pid>`) and restart — the script's `skip_existing=True` will pick up where it left off.

**Why 60s timeout, not 120s:** the send endpoint is supposed to be fast. If a 700KB PNG hasn't uploaded in 60s, the connection is dead. Letting it hang for 120s × 3 retries = 6 minutes per failed topic. 60s × 5 retries with exponential backoff (1+2+4+8+16 = 31s) caps each topic at ~2 minutes of recovery attempts.

### ⚠️ Skip-on-fail pattern — create the page even if image upload fails (Pitfall 73)
When the PNG upload fails after exhausting retries (Pitfall 72), the original uploader marked the topic as `topics_failed` and **skipped the page creation entirely** — losing the markdown content too. The user ended up with a hub page missing several topics, even though the markdown was already on disk and ready to publish.

**Better pattern: create the page with markdown, skip the image:**
```python
upload_id, err = upload_png(png_file)
if not upload_id:
    # Image upload failed — create page without image, retry images later
    print(f"  PNG skip {topic_prefix}: {err.get('_error', 'err')}", flush=True)
    url, res = create_topic_page(hub_id, title, md_text, file_upload_id=None)
    if not url:
        stats["topics_failed"] += 1
        print(f"  PAGE fail {topic_prefix}: {res}", flush=True)
        continue
    stats["topics_noimg"] = stats.get("topics_noimg", 0) + 1
    stats["topics_ok"] += 1
    print(f"  OK(noimg) {topic_prefix} {title[:40]}", flush=True)
    time.sleep(0.8)
    continue
```

The `create_topic_page` helper needs to handle `file_upload_id=None` — when it's None, **skip the image block** in the `children` array (don't pass `"id": None` to Notion — that returns 400). Add a yellow callout instead:
```python
def create_topic_page(hub_id, title, md_content, file_upload_id):
    if file_upload_id:
        children = [divider, callout, image_block]
    else:
        children = [callout_yellow("Sea Knowledge page for {title}. Image upload pending retry.")]
    # rest of payload construction unchanged
```

**Why this is better than failing the whole topic:**
- The markdown is the high-value content; the PNG is the visual aid. A page with full markdown + "image pending" callout is much more useful than a missing page.
- After the run, do a separate `attach_pending_images.py` pass that scans for `topics_noimg` entries and re-tries the image upload via PATCH children append.
- The skip-on-fail pattern keeps the pipeline moving at the same pace (no per-topic stall) and bounds the failure to one recoverable resource (PNG), not the whole topic.

**Important:** bump the per-topic sleep from 0.5s to 0.8s when working with 700KB+ PNGs. The 0.5s rate was fine for 200-300KB Cardiology PNGs but consistently hits 403 on Notion's `file_uploads` for the larger Oncology PNGs.

### ❌ `build_site.py` BUILT_CHAPTERS slug must match the actual chapter folder name (Pitfall 74)
The static-site generator's `BUILT_CHAPTERS` dict keys are used both to:
1. Walk `chapters/<slug>/diseases/` for the PNG + MD pairs
2. Generate the `<a href="<slug>/">` URLs in `site/index.html`

If the dict has `2-clinical-therapeutics-and-good-prescribing` (the long formal name) but the actual folder is `2-clinical-therapeutics` (shorter name), the site silently shows the chapter as missing — `find_files()` returns 0 topics because the path doesn't exist. The site `index.html` still renders the card with the long slug, so the user sees a card but clicks through to a 404.

**Detection:** after every `python3 build_site.py`, audit each chapter's topic count:
```bash
for ch in /mnt/tb/Sea-knowledge/#MedSea/site/*/; do
  n_pngs=$(find "$ch" -name "*.png" 2>/dev/null | wc -l)
  echo "$(basename $ch): $n_pngs PNGs"
done
# 1-clinical-decision-making: 6 PNGs   ← expected
# 2-clinical-therapeutics: 71 PNGs      ← expected
# 2-clinical-therapeutics-and-good-prescribing: 0 PNGs  ← BUG: orphan slug
```

**Fix:** keep the BUILT_CHAPTERS dict in sync with the actual folder slugs. The convention is: **use the shortest descriptive slug**, e.g. `2-clinical-therapeutics` not `2-clinical-therapeutics-and-good-prescribing`. The display name (in `DAVIDSON_25TH` table) can keep the formal name; only the URL slug needs to match the folder.

**Two separate dicts in `build_site.py`:**
```python
# URL/folder slugs (must match chapters/<slug>/ folders exactly)
BUILT_CHAPTERS = {
    "1-clinical-decision-making": {...},
    "2-clinical-therapeutics": {...},  # ← short slug
    ...
}

# Display names (formal Davidson titles, can include "and good prescribing")
DAVIDSON_25TH = [
    (1, "Clinical decision-making", "1-clinical-decision-making"),
    (2, "Clinical therapeutics and good prescribing", "2-clinical-therapeutics"),
    ...
]
```

When you rename a chapter folder, grep `build_site.py` for the old slug and update BOTH dicts. A mismatch in either direction = missing chapter on the site.

### ⚠️ Large git push (1000+ files, 200+ MB) takes 20-40 minutes — don't panic (Pitfall 75)
Pushing 1,781 files / 489K insertions / ~265 MB of PNGs to GitHub from this machine takes **25-40 minutes** end-to-end. The push log stays **0 bytes** for the entire duration because `git-remote-https` writes the pack via stdin, not stdout. The `pack-objects` child process chews CPU and network for the whole window.

**Don't mistake silence for failure.** When the push log is empty but the process is alive:
```bash
# Check the process is actually pushing
ps aux | grep "git pack" | grep -v grep
# If you see "pack-objects --all-progress-implied" running, the push is alive.

# Check progress via /proc/<pid>/io
cat /proc/<pack_pid>/io | grep wchar
# wchar: 247046144  ← 247 MB written to network so far
```

When `wchar` stops growing and the process exits, the push is done. The log file gets populated only at the very end (the `To <url> ... main -> main` line + `EXIT=$?`).

**Why this matters:** a naive check `cat /tmp/push.log` will return empty for 30+ minutes. If you kill the process based on that, you lose the entire push and have to start over. The right wait pattern is:
1. Launch the push in background with `notify_on_complete=true` (Pitfall 63)
2. Don't poll the log file directly
3. If you must verify progress, check `wchar` from `/proc/<pid>/io` (cheap, instant)
4. The system will notify you when the push completes

**For pushes <500 MB / <1000 files:** foreground is fine (5-10 min). For anything larger, background + notify is mandatory.

**Pre-check before pushing:** the MedSea `.gitignore` excludes `site/**/*.png` etc — the site/ build is derived from chapters/, and the chapters/ tree has all the PNGs. If your `.gitignore` is missing the PNG exclusions, you'll push the PNGs in BOTH `chapters/` and `site/`, doubling the push size to 500+ MB. Verify:
```bash
git status --porcelain | grep -E '\.png$' | head -5
# Should be empty (or only show the README/manifest tracked PNGs, if any)
```
