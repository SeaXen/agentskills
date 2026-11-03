---
name: medical-content-multi-target-pipeline
description: Build a Davidson chapter (or any structured medical content set) and publish it to ALL FIVE distribution targets — local filesystem, Notion database, static website, GitHub repo, and Docker container. Also covers **auditing & patching existing chapters** (3-way source/MedSea/Notion sync) via `references/medsea-chapter-audit-script.md`. Use when the user asks to "complete chapter N", "upload to notion, website, git and local", "build chapter from /mnt/tb/Medicine/<name>", "audit chapter N sync", "check which topics are missing on Notion", or wants a chapter with full multi-target deployment. Covers the source-MD → render → Notion → site → git → docker pipeline including the renderer quirks (unnumbered ## headers, mermaid mindmap/flowchart, large-file truncation, output nesting), Notion database parent (not workspace), search-existing-root pattern to avoid duplicate pages, 25th Edition Davidson renumbering, and the 5-col static site generation.
version: 1.0.0
author: medsea-pipeline
license: MIT
metadata:
  hermes:
    tags: [medical-study, publishing, pipeline, notion, static-site, git, docker, davidson, multi-target]
    related: [medical-study-hub-publisher, subagent-batch-note-conversion, stream-timeout-and-batch-conversion-pitfalls]
---

# Medical Content Multi-Target Pipeline

## When to Use

Build a medical chapter and deploy to all 5 distribution targets in one pass:
- **Local**: `/mnt/tb/Sea-knowledge/<N. Title>/` (canonical source)
- **MedSea backup**: `/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/`
- **Notion database**: MedSea DB `3805588e-846f-808b-a23b-cf63c89f372e` (NOT workspace)
- **Static site**: 5-col chapter cards, 1287+ topics
- **GitHub**: `https://github.com/SeaXen/MedSea` (commit + push)

Triggered by: "complete chapter N", "upload to notion, website, git and local", "do all topics from <chapter>", "build chapter from /mnt/tb/Medicine/<name>", or any variant that implies a Davidson chapter build with full multi-target deployment.

## The 5 Targets — Verification Checklist

Every chapter build MUST end with all 5 verified:

```
1. LOCAL    — /mnt/tb/Sea-knowledge/<N. Title>/diseases/<hub>/<topic>/topic.{md,html,png}
2. MEDSEA   — /mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/diseases/.../topic.{md,html,png}
3. NOTION   — MedSea DB has chapter page; each topic has sub-page with markdown + image
4. SITE     — /mnt/tb/Sea-knowledge/#MedSea/site/<slug>/index.html (SPA)
5. GITHUB   — Committed and pushed; commit visible at github.com/SeaXen/MedSea
```

(Optionally 6th: Docker container running on port 8855 with the new site baked in.)

## Pipeline Stages (in order)

### Stage 1: Source Discovery

Source lives at `/mnt/tb/Medicine/<Chapter Name>/` (note: this is **Davidson 24th Ed source**; the chapter NUMBERING is **25th Ed** which differs). The mapping is in `references/davidson-25th-ed-mapping.md`.

```python
from pathlib import Path
src = Path("/mnt/tb/Medicine/<Chapter Name>")
md_files = sorted([f for f in src.iterdir() if f.suffix == ".md"])
# Skip MOC, Hierarchy, Roadmap, Chapter Overview files
topics = [f for f in md_files if not any(k in f.name for k in ("MOC", "Hierarchy", "Roadmap", "Chapter", "Davidson"))]
```

### Stage 2: Renderer Pipeline

**Renderer**: `/root/sea-knowledge-infographics/render_topic.py`
**Signature**: `--slug <slug> --title <title> --markdown-file <path> --out-dir <path> --tag <tag>`
**Output**: `<out-dir>/<slug>/<slug>.{html,md,png}` (named by slug, NOT `topic.png`)

**CRITICAL PITFALLS** (see `references/renderer-pitfalls.md` for full details):

1. **Output is NESTED one level deeper than expected**:
   - You pass `--out-dir /path/to/disease_dir`
   - Output goes to `/path/to/disease_dir/<slug>/<slug>.{html,md,png}` (not `disease_dir/<slug>.png`)
   - **Fix**: After render, move files up OR pass `--out-dir <parent_of_disease_dir>`

2. **Unnumbered `## 24-Hour Recall Prompts` headers cause infinite loop** in `parse_markdown_to_html`:
   - The renderer expects `## N. Title` numeric prefix
   - Bare `## Section Name` loops forever
   - **Fix**: Renderer was patched 2026-06-19 to tolerate non-numeric headers
   - **Workaround**: Pre-process MDs to number all `## ` headers (`preprocess_md` in `templates/build_chapter.py`)

3. **Mermaid ` ```mindmap `` and ` ```flowchart `` code blocks not rendered** as visuals:
   - Originally shown as raw code
   - **Fix**: Renderer now has `render_mindmap()` and `render_flowchart()` that produce nested `<ul class="mindmap">` and `<div class="flowchart">` HTML
   - Applied 2026-06-19

4. **Renderer hangs on >400 line MDs**:
   - Symptom: 60s timeout, no output
   - **Fix**: Truncation retry — first attempt full file, on timeout retry with 120-line cap
   - **Tradeoff**: Truncated content is incomplete but PNG renders

5. **Source MDs have YAML frontmatter** that must be stripped before rendering:
   ```python
   if text.startswith("---"):
       end = text.find("\n---", 3)
       if end != -1:
           text = text[end + 4:].lstrip()
   text = re.sub(r"^#\s+.+?\n", "", text, count=1).strip()  # Remove H1
   ```

### Stage 3: Local + MedSea Save

```python
from pathlib import Path
import shutil
chap_local = Path(f"/mnt/tb/Sea-knowledge/{dav_num}. {title}")
chap_medsea = Path(f"/mnt/tb/Sea-knowledge/#MedSea/chapters/{slug}")
for src_png in [output_dir / f"{slug}.png"]:
    shutil.copy2(src_png, chap_local / "diseases" / f"{local_prefix}-{slug}" / "topic.png")
    shutil.copy2(src_png, chap_medsea / "diseases" / f"{local_prefix}-{slug}" / "topic.png")
```

### Stage 4: Notion Upload

**CRITICAL: Notion pages are in a DATABASE, not workspace.**

```python
MEDSEA_DB = "3805588e-846f-808b-a23b-cf63c89f372e"

def create_root_page(dav_num, name):
    payload = {
        "parent": {"type": "database_id", "database_id": MEDSEA_DB},
        "properties": {
            "Name": {"title": [{"type": "text", "text": {"content": f"Chapter {dav_num}: {name}"}}]},
        },
    }
    return http("POST", "https://api.notion.com/v1/pages", data=payload)
```

**Search-existing pattern** (avoid duplicate pages from interrupted runs):

```python
def search_existing_root(dav_num, name):
    r = http("POST", f"https://api.notion.com/v1/databases/{MEDSEA_DB}/query",
             data={"filter": {"property": "Name", "title": {"equals": f"Chapter {dav_num}: {name}"}}})
    if r.get("results"):
        return r["results"][0]["id"]
    return None
```

**Page URL format** (for BUILT_CHAPTERS dict in site):
```
https://app.notion.com/p/SeaHub/Chapter-{N}-{title-slug}-{id-without-dashes}
```

**Notion API limitations learned the hard way**:
- `child_page` blocks CANNOT be reparented via PATCH `/v1/pages` — only top-level page move works
- Sub-pages (hubs, topics) stay where they were created
- Workaround: redirect notice on OLD page pointing to NEW

**File upload 2-step** (for PNG attachments):
1. POST `/v1/file_uploads` with metadata → returns `upload_url`
2. POST multipart to `upload_url` with the file
3. Add 403 retry logic — file_uploads frequently 403 with intermittent backoff

**Common bugs to avoid in upload script**:
- `re` not imported (NameError on `re.match`) — add `import re`
- UnboundLocalError when assigning to dict key in one branch but not local var — always `root_id = ch["root_id"]` after `ch["root_id"] = existing`
- `sys.argv[1]` is a single string — pass chapter numbers one per invocation OR change the filter logic

### Stage 5: Static Site Generation

`scripts/site/build_site.py` in the MedSea repo. Key data structures:

```python
DAVIDSON_25TH = [
    (1,  "Clinical decision-making",           "1-clinical-decision-making"),
    (10, "Acute medicine and critical illness", "10-acute-medicine"),
    # ... all 32 chapters with slug or None for SOON
]

BUILT_CHAPTERS = {
    "<slug>": ("Display Name", "notion_url", "#hexcolor"),
    # Only LIVE chapters (rendered + uploaded) go here
}
```

**Card design v4** (5-col grid, no image, no description):
- `index.html` shows all 32 chapters in `DAVIDSON_25TH`
- LIVE chapters (in `BUILT_CHAPTERS`) are clickable
- SOON chapters are dimmed/disabled
- Per-chapter SPA: left sidebar (hub groups + topic items, search), right pane (header → content → image)
- Topic content is pre-rendered HTML loaded via fetch() from `topics.json` manifest

**`.gitignore`** must exclude `site/**/*.png` (PNGs are duplicates of chapters/*, would bloat repo).

### Stage 6: Git Commit + Push

```bash
git add -A
git -c user.email="drpelagik@gmail.com" -c user.name="SeaXen" commit -m "Ch N: <Title> (X topics)"
git push
```

Pattern: combine renames + new chapters + site updates in ONE commit for atomic deploy.

### Stage 7: Docker Restart (optional 6th target)

```bash
docker build -t medsea-site:latest .
docker stop medsea
docker rm medsea
docker run -d --name medsea --restart unless-stopped -p 8855:8855 medsea-site:latest
```

Container uses `nginx:alpine` base, copies `site/` to `/usr/share/nginx/html/`, listens on 8855, health check via `wget --spider`.

## File / Directory Conventions

| Path | Purpose |
|---|---|
| `/mnt/tb/Medicine/<Chapter>/` | Source MDs (Davidson 24th Ed content) |
| `/mnt/tb/Sea-knowledge/<N. Title>/` | Local chapter — canonical, mirrors MedSea structure |
| `/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/` | Git-tracked MedSea backup |
| `/mnt/tb/Sea-knowledge/#MedSea/site/` | Generated static site (PNGs gitignored) |
| `/mnt/tb/Sea-knowledge/#MedSea/Dockerfile` | nginx:alpine + COPY site/ |
| `/tmp/sk_render/` | Renderer scratch (input MDs staged here) |
| `/tmp/build_ch<N>_<N>.py` | Build pipeline scripts (one per batch) |
| `/tmp/upload_ch<N>_<N>.py` | Notion upload scripts |
| `/root/sea-knowledge-infographics/render_topic.py` | Renderer (DON'T edit unless you understand the side effects) |

## Verification at End

```bash
# 1. Local
ls /mnt/tb/Sea-knowledge/<N. Title>/diseases/*/topic.png | wc -l  # Should equal N topics

# 2. MedSea
ls /mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/diseases/*/topic.png | wc -l

# 3. Notion (query DB)
python3 -c "
import os, json, urllib.request
key = os.environ['NOTION_API_KEY']
r = urllib.request.Request('https://api.notion.com/v1/databases/3805588e-846f-808b-a23b-cf63c89f372e/query',
    data=json.dumps({'filter': {'property': 'Name', 'title': {'equals': 'Chapter N: Title'}}}).encode(),
    method='POST', headers={'Authorization': f'Bearer {key}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'})
print(json.loads(urllib.request.urlopen(r).read())['results'][0]['id'])
"

# 4. Site
ls /mnt/tb/Sea-knowledge/#MedSea/site/<slug>/index.html

# 5. GitHub
git log --oneline | head -3  # Latest commit should mention the chapter
git push  # If unpushed commits
```

## Pitfalls — Full List

1. **Renderer output is nested** — out_dir/slug/slug.{html,md,png} not out_dir/slug.{html,md,png}
2. **Unnumbered `##` headers cause infinite loop** — pre-process to add numeric prefix
3. **Mermaid mindmap/flowchart not rendered** — was fixed 2026-06-19, ensure renderer is updated
4. **Large MDs (>400 lines) hang renderer** — use truncation retry
5. **Notion pages are in DATABASE, not workspace** — `parent: {type: database_id}` not `parent: {type: workspace}`
6. **`child_page` blocks cannot be reparented** — only top-level page move via PATCH
7. **File uploads 403 intermittently** — add retry with exponential backoff
8. **`re` not imported in upload script** — common copy-paste bug
9. **UnboundLocalError on `root_id`** — when finding existing root, also assign to local var
10. **`sys.argv[1]` is single string** — pass chapter numbers one per invocation
11. **`.gitignore` must exclude `site/**/*.png`** — otherwise repo bloats with duplicates
12. **Source MDs are 24th Ed, target is 25th Ed** — chapter numbers differ (see mapping)
13. **DAVIDSON_25TH list needs slugs for LIVE chapters** — None means SOON
14. **5-col card grid breakpoint** — CSS responsive: 5/4/3/2/1 cols at 1200/992/768/576/0
15. **Color per chapter** — assign distinct hex in BUILT_CHAPTERS (use the chapter theme color)
16. **Git push HTTP 408 on large commits** — split into per-commit pushes: `git push origin <sha>:main` succeeds when combined `git push origin main` times out (MedSea site regen often pushes >150K insertions at once)
17. **Source filename suffix `_full.md` ≠ MedSea `-full.md`** — when copying topic MDs from `/mnt/tb/Medicine/<chapter>/` to MedSea flat layout, rename `_full.md` → `-full.md` and `_Hub.md` → `-hub.md`. Source convention is underscore; MedSea is dash
18. **Notion titles use Title Case With Spaces, NOT slugs** — convert "opioid-pharmacology-overview-full" → "Opioid Pharmacology Overview Full" via `" ".join(w.capitalize() for w in slug.replace("-full","").split("-"))`. Hub pages use format `"9.7 Opioid Management"`
19. **Notion child page parent (not database)** — for hub pages under a chapter, use `parent: {type: page_id, page_id: <chapter_page_id>}`. Don't use `database_id` for sub-hubs; that's only for the root chapter entry
20. **3-way audit before claiming sync** — Source vs MedSea local vs Notion. A chapter can pass MedSea-vs-source check but still be missing Notion pages, OR vice versa. Always check all three before reporting complete
21. **Notion API `markdown` field for full content upload** — `POST /v1/pages` with `properties: {title: [...]} + markdown: "<full MD content>"` lets Notion auto-convert MD to blocks. Strip YAML frontmatter first. Verified with 50 Ch 9 topics (2026-06-20); ~2-3s per page including rate-limit sleep
22. **Source naming inconsistency: `_full.md` vs `_Hub.md` vs plain** — some source dirs use `_full.md` (Ch 9 Pain/Palliative), others `_HUB.md` (Ch 9), others plain (Ch 6, Ch 10). Filter logic must handle ALL three: `_full.md`, `_Hub.md`/`_HUB.md`, plain
23. **Source has NESTED subdirectories with topic files at 3+ levels deep** — `/mnt/tb/Medicine/<Chapter>/<Hub>/<SubHub>/<Topic>.md` (verified Ch 2: `Principles of Clinical Pharmacology/Pharmacokinetics/Absorption and Bioavailability.md`). The `rglob("*.md")` pattern still finds them; the bug is in `normalize()` regex. Use `r'^[\d\.\-\s]+'` to strip ALL leading digits/dots/dashes (not just `\d+(\.\d+)?[\s\.\-]*`). Old regex left "1-1-clinical-reasoning" stuck on `1.1 Clinical Reasoning.md`, missing the topic entirely. Verified Ch 1 (6 topics), Ch 3 (12 topics), Ch 4 (12 topics) all appeared missing under old regex but are actually present in MedSea
24. **Source may have DUPLICATE folders with same content under different names** — Ch 2 has `TDM/` + `Therapeutic Drug Monitoring/` (same 7 files), `Clinical Context/` + `Clinical Contexts/`, `Medication Safety/` + `Medication Safety and Errors/`, `Polypharmacy/` + `Polypharmacy and Deprescribing/`. Dedup by slug when comparing, pick longest content version. Without dedup, source count is inflated (112 files → 97 unique topics for Ch 2)
25. **Initial quick audit gives wrong answer for chapters with nested subdirs** — flat slug count comparison (e.g., 71 medsea vs 26 notion for Ch 7) MISSED the nested topics in Ch 2 (26 missing). The user's "final check" caught it. **Always do source-deep audit**: `src.rglob("*.md")`, filter by name patterns only (not size, not depth), dedupe by slug, then compare. Hub-count check (source subdirs vs medsea hubs) catches missing-hub gaps but not missing-topic-in-existing-hub gaps
26. **Notion chapter page ID often missing from manifest even when page exists** — Ch 10's `manifest.json` had no `notion_id` field despite a Notion page existing. If `manifest["notion_id"]` is empty/None, search Notion via `POST /v1/search` with `{"query": "Chapter N: <Title>", "filter": {"property": "object", "value": "page"}}` and use the first result. Patch the manifest after finding it
27. **Per-hub seq allocation when pushing a batch** — when adding N topics across multiple hubs, group by hub number first. For each hub, `next_seq = max(existing_seqs) + 1` then increment per topic in that hub. Don't use a global counter. Verified 2026-06-20 with 26 Ch 2 topics across 4 hubs (2.1, 2.2, 2.4, 2.10)
28. **Slug collision from `&` in source filenames** — `Opioid side effects (constipation, N&V, ...)_full.md` slugifies to `opioid-side-effects-constipation-n-v-respiratory-depression-sedation-pruritus` (because `&` → space → hyphen to `n-v`). MedSea may have it as `opioid-side-effects-constipation-nv-...` (without the dash). Same topic, different slugs — verify the file actually exists before flagging as missing. Found in Ch 9 (file exists at `9.7.03-opioid-side-effects-constipation-nv-...` despite source slug saying `n-v`)
29. **MOC + Hierarchy files are the BIGGEST audit gap — silent skip across every prior sync** — `/mnt/tb/Medicine/<Chapter>/` root contains 2-3 files like `<Chapter> MOC.md` (5-44 KB) and `Davidson Chapter <N> - <Chapter> Hierarchy.md` (5-25 KB). These have `status: full-fcps-mrcp-hub` in frontmatter (the truthful marker) and contain master overviews/hierarchies. **They are NOT atomic topics — they are HUB-level content** that must be (a) added to MedSea's `hubs/` directory, (b) added to the chapter Notion page as a top-level section, (c) listed in `manifest.json` under `hubs`. Every prior audit filtered them out by name pattern (`MOC.md`/`Hierarchy.md`/`Roadmap.md`) and missed ~50 KB of content per chapter. Audit fix: don't filter them — INVENTORY them and report as "hub-level missing". Verified 2026-06-20 across Ch 16-30: 22 such files totaling ~250 KB missed by prior syncs
30. **Hematology is the structural outlier — all topics are root-level files, no subfolders** — every other Davidson chapter has the pattern `Chapter/<SubHub>/<Topic>.md` (Cardiology: `Cardiology/02_Acute_Coronary_Syndromes/STEMI.md`), but Hematology has every topic as a flat root `.md` file (`Hematology/Acute Lymphoblastic Leukaemia (ALL).md`). The audit's "leaf .md files in subfolders" pattern misses Hematology entirely if applied. Audit fix: ALWAYS count **all** `.md` files recursively, then dedup by normalized slug. Hematology verified 100% synced (85 topics, all root-level, all present in MedSea as `24.X.Y-...` atomic dirs) — but only because the audit counted flat; a subdir-only audit would falsely report "Hematology has 0 source topics"
31. **Slug-only comparison inflates false-missing — verify by word count match** — when source topic slug doesn't match any MedSea slug, the topic may still be present with a renamed/different slug. After normalization, check the **content word count**: `wc -w source.md` vs `wc -w medsea_topic.md`. Hematology verified: source `Acute Lymphoblastic Leukaemia (ALL).md` = 2905 words; MedSea `24.1.2-acute-lymphoblastic-leukaemia-all/topic.md` = 2905 words → **same content, different filename = synced**. Use this whenever the slug-only diff flags "missing" but you suspect MedSea has it split/renamed. Catches the case where MedSea's atomic topic is `etiology-degenerative-bicuspid-rheumatic` and source is `Aortic stenosis.md` — the source is the parent overview, MedSea has the atomic sub-slice
32. **Frontmatter `status:` is the authoritative content marker — use it, not file size** — the source taxonomy has 5 distinct statuses that determine sync priority:
    - `full-fcps-mrcp-note` → disease-level topic, MUST be in MedSea as `topic.md`
    - `full-fcps-mrcp-hub` → chapter/section overview, MUST be in `hubs/` or as hub Notion page
    - `first-pass-full-note-complete` → freshly written, treat as full
    - `disease-level-scaffold` / `draft` → in-progress, skip from "missing" count
    - `starter-note` → empty template (header + empty sections), don't sync as content
    Audit fix: `grep -oP "status:\s*\K\S+" file.md` to filter by status before counting. Stops false "missing" reports for empty starter stubs. Validated 2026-06-20 on Ch 21 (15 root `.md` files were `starter-note` placeholders, not real content)
33. **Source folder-name inconsistency breaks naive chapter lookups** — Medicine source uses different folder naming per chapter: `Cardiology` (matches ch title), `Diabetes` (not `Diabetes Mellitus`), `Hematology` (UK spelling, not `Haematology`), `Medical Ophthalmology` / `Medical Psychiatry` / `Maternal Medicine` (multi-word, space-separated, no chapter number prefix). A naive `ls /mnt/tb/Medicine/ | grep "^21"` returns 0 results because no folder starts with "21". Audit fix: maintain an explicit mapping dict `{16: "Cardiology", 21: "Diabetes", 22: "Gastroenterology", 23: "Hepatology", 24: "Hematology", 25: "Rheumatology", 26: "Dermatology", 27: "Neurology", 28: "Medical Ophthalmology", 29: "Medical Psychiatry", 30: "Maternal Medicine"}` and pass the folder name (not the number) to find. The MedSea-side lookup is consistent (always `chapters/<N>-<slug>/diseases/`) but the source side varies
34. **Bash `#` in path silently breaks find when unquoted** — `/mnt/tb/Sea-knowledge/#MedSea/` is a literal folder name (the `#` is part of the name, not a shell comment). `find /mnt/tb/Sea-knowledge/#MedSea/...` in unquoted context can be parsed as `find <comment> MedSea/...` and silently match nothing or report 0 results. Fix: always assign to a variable with single quotes first: `MEDSEA='/mnt/tb/Sea-knowledge/#MedSea'` then use `"$MEDSEA/..."`. Affects every audit script that touches this path. Cost ~5 minutes of confused debugging per session until you internalize the rule
35. **`-hub` suffix is organizational metadata, NOT content** — MedSea topic dirs ending in `-hub` (e.g., `16.1-acs-pathophysiology-hub`, `16.2-acs-emergencies-hub`) are section index pages that link to atomic topics. They should be excluded from "topic missing" counts because they're internal scaffolding, not standalone content. Audit fix: filter `grep -vE "hub$"` from MedSea slug list before comparing. Ch 26 Dermatology had 27 false-missing reports before this filter; all 27 were hubs. Same for Ch 28 Ophth (-13) and Ch 27 Neurology (-57). Confirmed across Ch 21-30 audit 2026-06-20

## Final Audit Checklist (use after every sync)

When the user says "make sure no topic missing" or "final check those chapters", run this 7-point checklist in order. Stop reporting "synced" until all 7 pass:

```bash
# 1. SOURCE FULL INVENTORY (recursive, ALL .md)
SRC="/mnt/tb/Medicine/<ChapterName>"
TOTAL_SRC=$(find "$SRC" -name "*.md" -type f | wc -l)

# 2. MEDSEA FULL INVENTORY (recursive, all topic.md)
SEA='/mnt/tb/Sea-knowledge/#MedSea'  # Note: single-quoted for #
TOTAL_SEA=$(find "$SEA/chapters/<N>-<slug>/diseases" -name "topic.md" -type f | wc -l)

# 3. SLUG-NORMALIZED DIFF (catches case/parens/&-variation)
# Use the slugify() from audit script above. Report "missing" and "extra".

# 4. MOC/HIERARCHY ROOT FILES (the silent gap)
find "$SRC" -maxdepth 1 -name "*.md" -size +5k -type f
# Each one should map to either MedSea hubs/ or be listed as a missing hub

# 5. HUB-COUNT MATCH (source subdirs vs MedSea hubs/)
# Skip for Hematology (no subdirs) and chapters where source uses flat files

# 6. WORD-COUNT VERIFICATION on every "missing" item
# If slug doesn't match but word_count(suspect_medsea_topic.md) == word_count(source.md),
# it's actually synced under a different slug — don't flag

# 7. STATUS-FRONTmatter FILTER on source
# Skip starter-note, draft, scaffold from "missing" report — they're not real content
```

Report the result as: `<Chapter>: src=N total_files, sea=N topic.md, missing_after_norm=K (real content), MOC/Hierarchy missing=K, hubs_delta=K, STATUS: SYNCED or NEEDS_PATCH`

## Auditing & Patching Existing Chapters (Reverse Pipeline)

When a chapter is already built but partially synced (e.g., Ch 9 had 51/101 topics after initial build), use this 3-way audit pattern:

### Step 1: 3-way inventory

```python
from pathlib import Path
import re

SRC = Path("/mnt/tb/Medicine/<Chapter Name>")
MEDSEA = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/diseases")
# Notion: fetched via API, see Stage 4 below

def slugify(text):
    """Aggressive normalize for cross-platform matching."""
    s = text.lower()
    s = re.sub(r'[^\w\s-]', ' ', s)   # punctuation → space (e.g., & → space, parens → space)
    s = re.sub(r'[\s_]+', '-', s)    # whitespace + underscores → dash
    s = re.sub(r'-+', '-', s)        # collapse dashes
    return s.strip('-')

def source_slugs(src_dir):
    slugs = set()
    for f in src_dir.rglob("*.md"):
        if any(x in f.name for x in ['MOC.md','Hierarchy.md','Roadmap.md','Template.md']):
            continue
        clean = f.name.replace('_full.md','').replace('_Hub.md','').replace('_HUB.md','').replace('.md','')
        slugs.add(slugify(clean))
    return slugs

def medsea_slugs(medsea_dir):
    slugs = set()
    for f in medsea_dir.iterdir():
        if f.is_dir():
            m = re.match(r'^\d+\.\d+\.\d+-(.+)$', f.name)
            if m: slugs.add(slugify(m.group(1)))
        elif f.suffix == ".md":
            m = re.match(r'^(\d+\.\d+)\.(\d+)-(.+)$', f.stem)
            if m:
                rest = m.group(3).replace('-full','').replace('-hub','')
                slugs.add(slugify(rest))
    return slugs
```

### Step 2: Identify gap type

Three possible gap categories:

| Gap | Symptom | Fix |
|---|---|---|
| **Missing hub entirely** (e.g., Ch 9 source had 11 subdirs, MedSea had 9 hubs) | Source has more subdirs than MedSea has hubs | Create new hub file in `hubs/` + add topic MDs under it + add hub entry to manifest |
| **Hub exists but topics missing** (e.g., Ch 9.7 had 0 topics under hub 9.7) | Hub file exists with topic table but ✗ marks | Copy source MDs to `diseases/` with proper naming |
| **Single topic missing** (e.g., Ch 9.4 had 7 instead of 8) | Source has 1 more topic than MedSea | Copy single source MD with next available seq number |

### Step 3: Copy & rename

```python
import shutil
SRC_TOPIC = Path("/mnt/tb/Medicine/Ch9/07_Opioid_Management/Equianalgesic dose conversion_full.md")
DEST = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters/9-palliative-care/diseases/9.7.01-equianalgesic-dose-conversion-full.md")
shutil.copy2(SRC_TOPIC, DEST)
# Source already has Related: line + Davidson header — leave intact
```

### Step 4: Push to Notion (child pages, not database)

```python
import json, urllib.request, re, time

def http(method, url, data=None):
    h = {"Authorization": "Bearer <NOTION_API_KEY>", "Notion-Version": "2025-09-03"}
    if data is not None:
        h["Content-Type"] = "application/json"
        body = json.dumps(data).encode()
    else:
        body = None
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(int(e.headers.get("Retry-After","2"))); continue
            return {"_error": e.code, "_body": e.read().decode()[:500]}

def title_from_slug(slug):
    """'opioid-pharmacology-overview-full' → 'Opioid Pharmacology Overview Full'"""
    s = slug.replace("-full","").replace("-hub","")
    return " ".join(w.capitalize() for w in s.split("-"))

def md_strip_frontmatter(text):
    if text.startswith("---"):
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
        if m: text = text[m.end():]
    return text.strip()

# HUB_ID = page_id of existing hub (e.g., 9.7 Opioid Management)
HUB_ID = "<hub_page_id>"

md_body = md_strip_frontmatter(Path("...").read_text())
payload = {
    "parent": {"type": "page_id", "page_id": HUB_ID},
    "properties": {"title": [{"type": "text", "text": {"content": title_from_slug(slug)}}]},
    "markdown": md_body
}
res = http("POST", "https://api.notion.com/v1/pages", data=payload)
# Rate-limit: sleep 0.8-1.5s between requests
```

**Title normalization rule**: Notion titles are Title Case With Spaces, never slugs. Strip `-full`/`-hub` first, then capitalize each dash-separated word.

**For brand-new hubs** (no existing page): create with `parent: {type: page_id, page_id: <CHAPTER_PAGE_ID>}`. Same code as topic creation, just different parent.

### Step 5: Generate PNGs (if needed)

```bash
python3 /root/sea-knowledge-infographics/render_topic.py \
  --slug "opioid-pharmacology-overview" \
  --title "Opioid Pharmacology Overview" \
  --markdown-file /mnt/tb/Sea-knowledge/#MedSea/chapters/9-palliative-care/diseases/9.3.09-opioid-pharmacology-overview-full.md \
  --out-dir /tmp/ch9-render \
  --tag "Palliative Care"
# Output: /tmp/ch9-render/opioid-pharmacology-overview/opioid-pharmacology-overview.png
# Then move/copy to MedSea flat layout destination
```

**Performance**: ~2s per topic. 50 topics = ~1.7 minutes (verified 2026-06-20 on Ch 9 batch).

### Step 6: Update manifest + hub files + rebuild site

```bash
# 1. Update manifest.json — add new hubs, fix topic counts
# 2. Update hubs/*.md — change ✗ to ✓ for MD and PNG columns
# 3. Rebuild site
cd /mnt/tb/Sea-knowledge/#MedSea
python3 scripts/site/build_site.py  # Outputs "Wrote 9-palliative-care/index.html"
```

### Step 7: Commit + Push (per-commit to avoid HTTP 408)

```bash
# Stage in 2 commits for atomic deploy + smaller upload:
# Commit 1: chapters only (smaller, faster)
git add chapters/9-palliative-care/diseases/*.md chapters/9-palliative-care/hubs/*.md \
        chapters/9-palliative-care/manifest.json chapters/10-acute-medicine/manifest.json
git commit -m "Ch 9: +49 topics, 2 new hubs, Ch 10 manifest notion_id"

# Commit 2: PNGs + site regen (larger)
git add chapters/9-palliative-care/diseases/*.png chapters/9-palliative-care/hubs/*.md site/
git commit -m "Ch 9: render PNG infographics (50 topics + 5 hubs) + site rebuild"

# Per-commit push (avoids HTTP 408 on combined push)
git push origin <commit1-sha>:main   # Usually succeeds in ~30s
git push origin <commit2-sha>:main   # Larger — may take 2-10 min for site regen
```

**Per-commit push rationale**: Combined `git push origin main` on a >150K-insertion site regen commit frequently returns HTTP 408 from GitHub's smart-HTTP server. Per-commit pushes (each smaller payload) succeed reliably. See Pitfall 16.

## Related Skills / References
- `medical-study-hub-publisher` — Notion study hub pattern (parent skill for content)
- `subagent-batch-note-conversion` — Python batch pattern for content writing
- `stream-timeout-and-batch-conversion-pitfalls` — generic stream/pitfall knowledge
- `references/davidson-25th-ed-mapping.md` — chapter number mapping 24th → 25th Ed
- `references/medsea-notion-db.md` — Notion API quirks + MedSea DB structure
- `references/renderer-pitfalls.md` — full renderer failure modes
- `references/davidson-25th-ed-pipeline-bulk-build-2026-06-19.md` — Pitfalls 41-49: bulk-build (10+ chapters) patterns — SIGKILL one-chapter-per-process, dual flat/subdir structure detection, hub-page + regex mapping (backtick vs wikilink), merged source dirs, /tmp volatility, collapsible-images-already-implemented
- `references/medsea-question-bank-quality.md` — **Question bank QC workflow** (dedupe, autogen filtering, rationale backfill, abbreviation expansion, format validation, PWA deployment — session 2026-06-27)
- `templates/build_chapter.py` — start-here build script (preprocess + render + save)
- `templates/upload_chapter_notion.py` — start-here Notion upload script
- `scripts/flatten_renderer_output.py` — flatten the nested slug/slug/ → slug/ structure
- `scripts/search_existing_notion_root.py` — query MedSea DB to avoid duplicate pages
- `scripts/audit_chapter_full.py` — corrected 3-way audit (source/MedSea/Notion) with proper slug normalization, dedup of duplicate source folders, and detection of nested subdirectory topics. Use this for the final "no topic missing" check after any chapter build

## Validation
**Proven:** 2026-06-19, Ch 10-15 (Davidson 25th Ed), 182/182 topics
- 6 chapters built: 43+37+13+9+54+26 = 182 PNGs
- 6 chapters uploaded to Notion: 6/6 root pages, 0 failures
- Site rebuilt: 1287 topics across 20 LIVE chapters
- GitHub: commit `4696e0b` pushed (2333 files, 443K insertions)
- GitHub: commit `6ddfdd5` for Notion URL updates (28 files, 48+/48-)
- 2 timeout failures re-rendered with 120-line truncation
- All 5 targets verified before reporting completion
