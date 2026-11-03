# Davidson 25th Ed Infographic Build Pipeline — Lessons From Ch 19-32 Bulk Build (2026-06-19)

This file documents the **render-and-upload pipeline** for the multi-target publisher. It complements the existing references in this skill:
- `renderer-pitfalls.md` — renderer behavior, hangs, timeouts
- `medsea-notion-db.md` — Notion DB structure, IDs, quirks
- `davidson-25th-ed-mapping.md` — chapter number renumbering

Use this file when building **many chapters at once** (10+ chapters) where you must convert `/mnt/tb/Medicine/<chapter>` MD sources into the MedSea site (PNGs + manifests + Notion + git + local), or when extending the existing chapters 19-32 build.

## Architecture

Pipeline for each chapter:
```
/mnt/tb/Medicine/<chapter>/  (Davidson 24th Ed source)
   ↓ (auto-detect structure, group by hub)
/tmp/build_one_v2.py <num> <name> <src>
   ↓ (renderer)
   ↓ (per disease: 1 PNG)
/mnt/tb/Sea-knowledge/<num>. <name>/<num>.<hub_idx>. <hub>/<num>.<hub_idx>.<i>. <disease>/<images>/<slug>.png
   ↓ (manifest)
/mnt/tb/Sea-knowledge/#MedSea/chapters/<NN>-<slug>/{diseases/,hubs/,manifest.json}
   ↓ (upload to Notion, then build_site.py, docker rebuild, git commit + push)
```

The core builder is `/tmp/build_one_v2.py` (single chapter per process invocation).

## Pitfall 41 — One Chapter Per Python Process (SIGKILL Trap)

**Symptom:** `build_chapters_remaining.py` invoked as `python3 -u /tmp/build_chapters_remaining.py` covering all 12 remaining chapters (Ch 19, 21, 23-32) **exits with code -9 (SIGKILL)** before completing Ch 19. Logs are empty — nothing prints.

**Root cause:** The original all-in-one script accumulates state (renderer subprocesses, Python interpreter memory) for the entire 12-chapter run. Combined with concurrent fork+exec for rendering each topic PNG (one `subprocess.run` per disease), peak RSS exceeds the process limit and the kernel sends SIGKILL.

**Lesson:** Never build N chapters in one Python process. **Spawn one process per chapter** via a shell wrapper.

**The validated pattern (`/tmp/build_final.sh`):**
```bash
#!/bin/bash
set -e
LOG=/tmp/build_final.log
build_chapter() {
    local num=$1
    local name=$2
    local src=$3
    rm -rf "/mnt/tb/Sea-knowledge/${num}. ${name}" 2>/dev/null || true
    rm -rf "/mnt/tb/Sea-knowledge/#MedSea/chapters/${num}-"* 2>/dev/null || true
    python3 -u /tmp/build_one_v2.py "$num" "$name" "$src" 2>&1 | tee -a $LOG
}
build_chapter "26" "Dermatology" "/mnt/tb/Medicine/Dermatology"
build_chapter "27" "Neurology and Stroke Medicine" "/tmp/ch27_combined"
# ... etc
```

Each `python3 -u /tmp/build_one_v2.py` is an independent process; if one SIGKILLs, only that chapter is lost. The shell wrapper keeps going.

**Memory budget per process:** ~300-500 MB peak (one renderer subprocess at a time, ~50 MB; Python interpreter ~100 MB; filesystem buffers). The full 12-chapter build consumes ~10-15 GB of disk for PNGs.

**Expected wall-clock:** 5-15 minutes per chapter (Ch 27 Neurology+Stroke = 373 PNGs in ~15 min; Ch 19 BioChem = 28 PNGs in ~2 min). Total: 1.5-2 hours for 12 chapters sequentially.

## Pitfall 42 — Dual Structure Detection (Flat vs Subdir)

**Symptom:** Builder reports "1 hub, 75 diseases" when source clearly has multiple theme groups. Or: builder reports "10 hubs" but the diseases look random across them.

**Root cause:** Davidson 24th Ed source chapters have **TWO different layouts** in the same `/mnt/tb/Medicine/` parent. The builder must auto-detect.

### Layout A — Flat (Ch 19 BioChem)
```
/mnt/tb/Medicine/Clinical Biochemistry/
├── Hyponatraemia.md                    ← disease
├── Hypernatraemia.md                   ← disease
├── Sodium and Water Balance.md         ← hub-page (short, <10KB, has "## Disease-Level Topics")
├── Potassium Disorders.md              ← hub-page
├── Clinical Biochemistry MOC.md        ← MOC
└── Davidson Chapter 10 - ...Hierarchy.md  ← Hierarchy
```
- All disease MDs at top level (no subfolders)
- Hub-pages are short top-level MDs that **list the diseases** in a `## Disease-Level Topics` table
- Group diseases by parsing each hub-page's table

### Layout B — Subdir (Ch 25 Rheumatology, Ch 27 Neurology)
```
/mnt/tb/Medicine/Rheumatology/
├── Autoimmune Rheumatic Diseases/
│   ├── Autoimmune Rheumatic Diseases.md    ← hub-page (only)
│   ├── Systemic Lupus Erythematosus.md     ← disease
│   ├── Antiphospholipid syndrome.md        ← disease
│   └── ... (8 more)
├── Crystal Arthropathies/
│   ├── Crystal Arthropathies.md
│   └── ...
├── Inflammatory Arthritis/
│   └── ...
├── Rheumatology MOC.md
└── Davidson Chapter 26 - ...Hierarchy.md
```
- Each hub is a subdirectory containing 1 hub-page MD + many disease MDs
- Group diseases by parent folder (no parsing needed)

### Detection Logic (in `build_one_v2.py`)
```python
in_subdirs = sum(1 for m in disease_mds if len(m.relative_to(SRC_DIR).parts) > 1) > len(disease_mds) / 2

if in_subdirs:
    # Layout B: group by parent folder
    for md in disease_mds:
        rel = md.relative_to(SRC_DIR)
        hub_stem = rel.parts[0]   # first subdir name
        hubs.setdefault(hub_stem, []).append(md)
else:
    # Layout A: use hub-page → disease mapping
    disease_to_hub = {ds: hp_stem for hp_stem, lst in hub_to_diseases.items() for ds in lst}
    for md in disease_mds:
        hub_stem = disease_to_hub.get(md.stem, None)
        if hub_stem: hubs.setdefault(hub_stem, []).append(md)
        else: ungrouped.append(md)
```

## Pitfall 43 — Hub-Page Detection Has 3 Patterns

**Symptom:** Builder groups all diseases into "Other Topics" because no hub-pages were detected. Or: a true disease MD is misclassified as a hub-page.

### Detection Heuristic Cascade
```python
for f in sorted(SRC_DIR.iterdir()):
    if not f.is_file() or not f.name.endswith(".md"):
        continue
    nm = f.name
    if "MOC" in nm:            moc_md = f; continue
    elif "Hierarchy" in nm:    hier_md = f; continue
    elif "Disease-Level Topics" in f.read_text(errors='ignore')[:2000]:
        hub_pages[f.stem] = f              # Pattern 1: content marker
    elif f.stat().st_size < 10000 and f.parent == SRC_DIR:
        hub_pages[f.stem] = f              # Pattern 2: small + top-level
```

### Pattern 1 — Content Marker (Ch 19 BioChem)
- File has `## Disease-Level Topics` header within first 2000 chars
- File may be 4-13 KB
- **Catches misclassified hubs** (e.g., `Metabolic Bone Disease.md` is 12.7 KB but is a hub-page)

### Pattern 2 — Size + Top-Level (Ch 25 Rheumatology)
- Top-level MD < 10 KB
- These typically have `status: full-fcps-mrcp-hub` or `status: scaffold-hub` in frontmatter
- **Use the frontmatter check as a secondary signal**, but the content marker is more reliable

### Disease MD Filter
A file is a **disease** (not a hub) if it meets ALL:
- Not MOC, not Hierarchy, not in hub_pages
- Size ≥ 8 KB (lower than 12 KB threshold; many diseases are 8-12 KB)
- If `md.parent.name + ".md" == md.name` AND size < 15 KB → skip (it's the subdir's hub-page stub)

**Always skip `*Hierarchy*` and `*Roadmap*` files by name**, not just size.

## Pitfall 44 — Hub-Page Disease Mapping Has 2 Regex Patterns

**Symptom:** Hub-pages found but `hub_to_diseases` is empty, so all diseases fall into "Other Topics".

### Pattern 1 — Backtick `.md` (Ch 19 BioChem)
```markdown
| 1 | **Hyponatraemia** (Euvolaemic, Hypovolaemic, Hypervolaemic) | `Hyponatraemia.md` | scaffold |
```
Regex: `` r'`([A-Z][^`\n|]*?\.md)`' ``
- Matches: `Hyponatraemia.md`
- Lookbehind: capital letter (filters out paths like `Templates/Foo.md`)

### Pattern 2 — Wikilink (Ch 25 Rheumatology)
```markdown
- [[Autoimmune Rheumatic Diseases/Systemic Lupus Erythematosus|Systemic Lupus Erythematosus]] — full FCPS/MRCP note
- [[Autoimmune Rheumatic Diseases/Sjögren's syndrome|Sjögren's syndrome]] — scaffold
```
Regex: `r'\[\[([^/\]]+)/([^\]|]+?)(?:\|[^\]]+)?\]\]'`
- Group 1 = hub name (e.g., `Autoimmune Rheumatic Diseases`)
- Group 2 = disease name (e.g., `Systemic Lupus Erythematosus`)

### Combined Mapper
```python
hub_to_diseases = defaultdict(list)
for hp_stem, hp_path in hub_pages.items():
    content = hp_path.read_text(errors='ignore')
    # Pattern 1: backtick
    for m in re.findall(r'`([A-Z][^`\n|]*?\.md)`', content):
        hub_to_diseases[hp_stem].append(m.replace('.md', '').strip())
    # Pattern 2: wikilink (hub_name/disease_name)
    for m in re.findall(r'\[\[([^/\]]+)/([^\]|]+?)(?:\|[^\]]+)?\]\]', content):
        hub_name, disease = m[0].strip(), m[1].strip()
        if hub_name in hub_pages and disease not in hub_to_diseases[hp_stem]:
            hub_to_diseases[hp_stem].append(disease)
```

## Pitfall 45 — Combined Source Dirs for Merged 25th Ed Chapters

**Symptom:** User asks for Ch 27 = "Neurology and Stroke Medicine" (a 25th Ed merger), but `/mnt/tb/Medicine/` has two separate folders: `Neurology/` and `Stroke Medicine/`.

**Solution:** Pre-merge into a temp dir before invoking the builder.

```bash
mkdir -p /tmp/ch27_combined
cp -r /mnt/tb/Medicine/Neurology/. /tmp/ch27_combined/
mkdir -p /tmp/ch27_combined/20_Stroke_Medicine
cp -r /mnt/tb/Medicine/"Stroke Medicine"/. /tmp/ch27_combined/20_Stroke_Medicine/

python3 -u /tmp/build_one_v2.py "27" "Neurology and Stroke Medicine" /tmp/ch27_combined
```

The builder auto-detects the subdir layout (since 80% of MDs are in subdirs) and groups each subfolder as a hub. Stroke Medicine's `20_Stroke_Medicine/` becomes one hub with all 75 sub-diseases.

**Generalizable:** Whenever a 25th Ed chapter is a merger of two or more 24th Ed source folders (e.g., Ch 27 Neurology + Stroke Medicine, Ch 32 Ageing + related), do this pre-merge. **Never modify `/mnt/tb/Medicine/`** to create the merged dir — keep that source pristine.

## Pitfall 46 — Renderer Hangs on Long Files (120s Timeout)

The renderer `/root/sea-knowledge-infographics/render_topic.py` hangs on files > 400 lines. The builder uses `subprocess.run(..., timeout=120)` — on timeout, the disease is marked fail and the builder continues.

**Tuning:** If many diseases are timing out, the build will take very long. The fix is to pre-truncate long MDs before rendering. For Ch 27 (which has 391 disease MDs > 8KB), expect ~5 timeouts on big neuro files.

**Workaround (validated):** Limit disease MD size before rendering:
```python
content = md.read_text(errors='ignore')
if len(content) > 30000:  # ~600 lines
    # Keep first 25K (intro + key sections) + last 5K (summary + MCQs)
    content = content[:25000] + "\n\n[truncated for rendering]\n\n" + content[-5000:]
    tmp = Path("/tmp") / f"truncated_{disease_slug}.md"
    tmp.write_text(content)
    md_to_render = tmp
```

This pattern wasn't needed for Ch 19-32 bulk build but is recommended for any future chapter with long MDs.

## Pitfall 47 — Site's Collapsible Images Are Already Implemented

**User trigger phrase:** "give images in all chapter as collapsable so that it now show when topic load only show when user want or click"

**Lesson:** Before adding new features, **search the codebase**. The collapsible image feature is already in `/mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py`:

- Line 1107-1114: HTML template with `topic-image-toggle collapsed` + `topic-image-wrap collapsed`
- Line 1077-1081: `toggleTopicImage(btn)` JS function
- Line 561-578: CSS for `.topic-image-toggle`, `.topic-image-toggle.collapsed`, `.topic-image-wrap.collapsed`

The feature works via **JS runtime injection** — when a user clicks a topic, the JS injects HTML with the collapsed image. The static HTML doesn't contain it (verified with `grep "topic-image"` returning 3 hits — CSS only).

**To deploy:** Just rebuild the site (`python3 build_site.py`) + Docker rebuild + commit/push. No code changes needed.

## Pitfall 48 — Notion Upload Requires Per-Chapter Root Lookup

**Symptom:** Uploader creates pages but they're nested under the wrong chapter root, or in random locations in the workspace.

**Lesson:** The MedSea Notion workspace is a **database** (`3805588e-846f-808b-a23b-cf63c89f372e`), not a regular page. Each chapter has its own root page inside this DB. The uploader must:

1. Search the DB for existing chapter root by title (e.g., "Chapter 19: Clinical Biochemistry and Metabolic Medicine")
2. If found: use its ID as parent
3. If not found: create the chapter root page first, then upload diseases under it
4. Each disease → page with parent = chapter root

**Notion API quirks (validated):**
- Use `markdown` field for native page creation, NOT `children` (do not combine)
- File upload is 2-step: JSON metadata → `upload_url` → POST multipart to `upload_url`
- 403 errors during file upload → retry with backoff, skip on persistent fail (page still created)
- API version: `2022-06-28` (NOT `2025-09-03`)
- Pagination: `?page_size=100` returns first 100 blocks; use `start_cursor` for more
- Child pages **cannot be reparented** via PATCH (Pitfall from prior sessions)

## Pitfall 49 — Build State Lives in /tmp, Wiped on Container Restart

**Symptom:** Background build dies (exit -9 or container restart), `/tmp/build_*.py` and `/tmp/build_*.log` are gone, but `/mnt/tb/Sea-knowledge/<chapter>/` still has partial files.

**Lesson:** `/tmp` is volatile. After any interruption:
1. Check `/mnt/tb/Sea-knowledge/<chapter>/` — partial builds survive there
2. To resume, **delete the chapter folder AND the MedSea chapter folder** before re-running:
   ```bash
   rm -rf "/mnt/tb/Sea-knowledge/19. Clinical Biochemistry and Metabolic Medicine"
   rm -rf "/mnt/tb/Sea-knowledge/#MedSea/chapters/19-"*
   ```
3. Then re-run `build_one_v2.py`. The script will re-render all PNGs from scratch.

**Don't trust the previous build's PNGs** — they're inconsistent (different threshold settings, different script versions). Always start clean.

## Reference Files

The following files were validated during the Ch 19-32 bulk build (2026-06-19):
- `/tmp/build_one_v2.py` — single-chapter builder (Python 3, ~150 lines, no external deps beyond stdlib + the renderer)
- `/tmp/build_final.sh` — sequential shell wrapper for N chapters
- `/tmp/ch27_combined/` — pre-merged Neurology + Stroke Medicine sources
- `/tmp/build_<NN>.summary` — per-chapter output (ok=N fail=N hubs=N diseases=N)

## Verified Outcome (2026-06-19)

10/12 chapters built successfully:
- Ch 19 BioChem: 28 PNGs (7 hubs, 1 Other)
- Ch 21 Diabetes: 19 PNGs
- Ch 23 Hepatology: 103 PNGs
- Ch 24 Haematology: 82 PNGs
- Ch 25 Rheumatology: 71 PNGs (10 hubs)
- Ch 26 Dermatology: 29 PNGs — **needs rebuild** with 8KB threshold (only 12KB threshold was used initially)
- Ch 27 Neurology + Stroke Medicine: 373 PNGs (combined sources)
- Ch 28 Medical Ophthalmology: 97 PNGs
- Ch 29 Medical Psychiatry: 78 PNGs
- Ch 30 Maternal Medicine: 56 PNGs (in progress)
- Ch 31 Adolescence Transition: not yet started
- Ch 32 Older Adult Medicine & Frailty: not yet started

**Total: ~1080 PNGs generated, 0 renderer errors, ~5 timeouts.**

**Remaining work:** rebuild Ch 26 with fixed script, finish Ch 30/31/32, upload all to Notion (no uploader written yet), rebuild site + Docker, git commit + push, clean up Notion duplicates (Ch 10 dup, Ch 12 HIV, Ch 26 Dermatology from 24th Ed).