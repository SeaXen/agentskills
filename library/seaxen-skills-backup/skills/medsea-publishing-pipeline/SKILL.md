---
name: medsea-publishing-pipeline
description: Build and publish Davidson's Principles & Practice of Medicine chapters to the MedSea platform — local content, MedSea git backup, Notion chapter database, static site, and Docker deployment. Use when adding new chapters, renumbering chapters to a new edition, syncing content across all five targets (local + MedSea + Notion + Website + GitHub), or troubleshooting any stage of the pipeline.
---

# MedSea Publishing Pipeline

End-to-end workflow for publishing Davidson's chapters to the MedSea platform across all 5 targets: local source → renderer PNGs → MedSea git backup → static site → Notion database → Docker container.

## When to Use This Skill

Use when the user asks to:
- Build a new Davidson chapter (Ch 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 still pending)
- Renumber chapters to a new edition (24th → 25th, future 25th → 26th)
- Update topic/sub-topic prefixes after a chapter rename
- Sync content to any or all of: local, MedSea, Notion, website, GitHub
- Debug any stage of the pipeline (renderer hangs, site broken, Notion upload failures, Docker out of date)

## Pipeline Overview

```
/mnt/tb/Medicine/<Chapter>        (raw source MDs, Davidson 24th Ed)
        │
        ▼
[Pre-process] strip frontmatter, auto-number `##` headers
        │
        ▼
[Renderer] /root/sea-knowledge-infographics/render_topic.py
        │ outputs: out_dir/slug/{slug}.{png,html,md}
        ▼
/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/diseases/
        │
        ├──► [Site] build_site.py → /mnt/tb/Sea-knowledge/#MedSea/site/  (static SPA)
        │             │
        │             ▼
        │         [Docker] medsea-site:latest → container `medsea` on :8855
        │             │
        │             ▼
        │         http://192.168.0.222:8855/  (live site)
        │
        ├──► [Notion] upload_chapter.py → MedSea database 3805588e-846f-808b-a23b-cf63c89f372e
        │
        └──► [Git] /mnt/tb/Sea-knowledge/#MedSea/ → github.com/SeaXen/MedSea
              (daily backup cron: medsea-daily-backup at 02:00)
```

## Sync Workflow: `/mnt/tb/Medicine/<Chapter>/` → Live Site

When the user asks to "push Medicine notes to Sea-knowledge / website / git / notion", follow this exact order. Each step has a verified failure mode if skipped.

### Step 0a — Audit Three-Source Completeness (when user says "check if all info is added")

When the user asks "check all chapters N–M and add any missing info", the right workflow is a 3-way comparison BEFORE creating anything:

| Source | What to read | Tool |
|---|---|---|
| `Source` | `/mnt/tb/Medicine/<Chapter>/*.md` + subfolders | `Path.iterdir()` |
| `MedSea local` | `/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/diseases/` | glob `*.md` |
| `Notion mirror` | MedSea DB page tree (chapter page → child_page hubs → child_page topics) | `GET /v1/blocks/{id}/children` |

**Don't trust any single source as ground truth.** Source has the topics in MOC/Hierarchy/Roadmap files that should be skipped. MedSea may have renumbered or restructured. Notion may have stubs from interrupted runs. Audit script pattern (validated 2026-06-20, Davidson Ch 1–5):

```python
def normalize_topic_name(stem):
    """Drop numbers/punctuation/dashes, lowercase, return bag of words >3 chars."""
    import re
    words = re.sub(r"[\d\.\-_]+", " ", stem.lower()).split()
    return frozenset(w for w in words if len(w) > 3)

def is_topic_present(source_words, candidate_topics):
    """Match if ≥2 long words overlap (handles 'mendelian inheritance' ↔ 'mendelian-inheritance')."""
    return any(len(source_words & cand) >= 2 for cand in candidate_topics)
```

Then for each source MD: classify as MATCH (in MedSea), NEEDS-UPLOAD (in source but not MedSea+Notion), or META (MOC/Hierarchy — skip).

**Report findings before adding anything.** The user wants a real comparison, not "I'll add it all". a clean report shows source count vs MedSea count vs Notion count per chapter with the missing list — they may decide some "missing" topics are intentionally out of scope (e.g., HIV chapter left over from 24th Ed renames).

### Step 0b — Upload Missing Topics to Notion (the markdown body field pattern)

For each topic in NEEDS-UPLOAD list, push to Notion using the `markdown` body parameter (NOT block-by-block JSON — too slow and hits rate limits):

```python
def strip_md_for_notion(md):
    """Remove cross-reference links that won't resolve in a standalone Notion page."""
    import re
    md = re.sub(r"\*\*Parent Topic:\*\*[^\n]*\n", "", md)
    md = re.sub(r"\*\*Status:\*\*[^\n]*\n", "", md)
    md = re.sub(r"\*\*Priority:\*\*[^\n]*\n", "", md)
    md = re.sub(r"\*\*Source:\*\*[^\n]*\n", "", md)
    # Strip path-encoded links like (../Clinical%20Genetics%20MOC.md) → just text
    md = re.sub(r"\]\(\.\./[^\)]*\)", "]", md)
    return md

def upload_topic(hub_page_id, title, markdown, api_key):
    payload = {
        "parent": {"page_id": hub_page_id},
        "properties": {"title": [{"text": {"content": title}}]},
        "markdown": markdown,
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")  # ensure_ascii=False for non-ASCII
    req = urllib.request.Request(
        "https://api.notion.com/v1/pages",
        data=body,
        headers={"Authorization": f"Bearer {api_key}",
                 "Notion-Version": "2022-06-28",
                 "Content-Type": "application/json"},
        method="POST",
    )
    return json.loads(urllib.request.urlopen(req).read())
```

**Why `ensure_ascii=False`:** Bangla/Arabic/CJK source MDs would otherwise become `\uXXXX` escapes, doubling request size and breaking Notion's UTF-8 parser.

**Why `Notion-Version: 2022-06-28`:** The 2025-09-03 version splits database/data_source and rejects the old `parent: {page_id}` semantics for some operations. The 2022-06-28 version is what the MedSea DB was built on — stay on it.

### Step 0c — Save to MedSea Local AND Update Manifest

After uploading to Notion, mirror the same MD to MedSea local at `/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/diseases/<local_prefix>-<slug>.md`, then update `manifest.json`:

```python
# Local prefix format: <hub_num>.<topic_num>  e.g. 3.2.01
local_prefix = f"{hub_num}.{topic_num}"
dst = ch_diseases_dir / f"{local_prefix}-{slug}.md"
dst.write_text(strip_md_for_notion(source_md), encoding="utf-8")
```

Then update `manifest.json`: increment `n_topics` on the target hub, add the hub entry if it didn't exist, recompute `total_hubs` and `total_topics`.

**Pitfall — `local_prefix` collision:** If you upload a new topic with `local_prefix=3.2.01` and an existing MedSea file already has `3.2.01-system-based-clinical-genetics.md`, `find_files()` will keep the existing entry and silently shadow your new topic. **Before saving, grep for collisions:**

```bash
ls chapters/<slug>/diseases/ | grep "^<hub_num>\.<topic_num>-"
```

If a collision exists, rename the existing topic to a higher number first (e.g. `3.2.01-system-based-clinical-genetics.md` → `3.7.01-system-based-clinical-genetics.md`) and update its hub entry in `manifest.json`.

**Pitfall — existing hub name mismatch:** Notion may already have a hub called "System-Based Clinical Genetics" for `3.2` (not "Inheritance Patterns" as the source suggests). Always query the hub's actual name before uploading:

```python
def find_hub_page(parent_id, hub_num, hub_name_guess):
    """Walk children of parent chapter page; return matching hub page ID."""
    children = get_children(parent_id)
    for c in children:
        if c["type"] != "child_page":
            continue
        title = c["child_page"]["title"]
        # Match by hub number prefix (e.g. "3.2 Inheritance Patterns" or "3.2 System-Based Clinical Genetics")
        if title.startswith(f"{hub_num} ") or hub_name_guess.lower() in title.lower():
            return c["id"]
    return None
```

If no existing hub matches, create a new one: `POST /v1/pages` with `parent: {page_id: <chapter_id>}` and a simple markdown body like `# 3.2 Inheritance Patterns\n\nThis hub covers ...`.

### Step 0d — Rebuild Site + Docker + Verify

After MedSea local is updated:

```bash
cd /mnt/tb/Sea-knowledge/#MedSea
python3 scripts/site/build_site.py    # regenerates site/<slug>/index.html
bash scripts/redeploy.sh              # compose build + up; 8855:80; see references/docker-compose-named-redeploy.md
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8855/<slug>/
```

Check `build_site.py` output: it reports `<n> hubs, <m> topics`. If `m` matches what you just added, the local file naming was correct. If `m` is lower, you have a `local_prefix` collision (see Pitfall above).

### Step 1 — Identify Truly-Missing Topics (don't blindly re-render)

Source: `/mnt/tb/Medicine/<Chapter>/` (numbered folders 01-16) + `/mnt/tb/Sea-knowledge/#MedSea/chapters/<chapter>/diseases/` (rendered output).

Use **fuzzy matching** to compare slugs (normalize: lowercase, drop non-alphanum, take first 3 keywords, check containment). Expect a **near-match rate of 95-99%** — most "missing" topics already exist under a slightly different name (e.g. `Atherosclerosis_pathogenesis_full` ↔ `16.1.25-atherosclerosis-pathogenesis`). **Only treat as truly missing** what fails all near-match tests.

In the 2026-06-19 cardiology sync: 562/570 Medicine notes matched (98.6%); 3 were truly unique; 6 were near-duplicates.

### Step 2 — Author Sea-Knowledge Style Markdown

For each truly-missing topic, write input markdown in Sea-knowledge style (numbered `## N. Title` sections, `**bold**` for key terms, `||` table format, `> Pearls` block). Existing rendered topics in `chapters/<chapter>/diseases/<prefix>-*/topic.md` are the style template. See `templates/sync_chapter.py` for the full pattern.

### Step 3 — Render → chapters/

Run the renderer for each new topic:
```bash
python3 /root/sea-knowledge-infographics/render_topic.py \
  --slug "cha2ds2-vasc-has-bled" \
  --title "CHA2DS2-VASc & HAS-BLED Scores" \
  --markdown-file /tmp/sync_topics/cha2ds2-vasc-has-bled.md \
  --out-dir /tmp/sync_render
```

**Output naming trap:** the renderer writes `{out_dir}/{slug}/{slug}.{md,html,png}` — but the chapters/ convention is `topic.{md,html,png}`. The sync script MUST rename on copy. Without the rename, `build_site.py` won't pick up the PNGs and the topic silently doesn't render. See Pitfalls below.

### Step 4 — Mirror to ALL Three Storage Layers

The data lives in three places that must stay consistent or `build_backup.py` will silently drop things:

1. `/mnt/tb/Sea-knowledge/#MedSea/chapters/<chapter>/diseases/<prefix>-<slug>/topic.{md,html,png}` — git-tracked rendered output
2. `/mnt/tb/Sea-knowledge/<Chapter>/<hub_folder>/<local-N>. <slug>/topic.{md,html,png}` — local mirror (used as build_backup.py source)
3. `/root/sea-knowledge-infographics/all_disease_topics.json` — canonical list (dictates next-sync indexing)

**Also delete auto-junk topics** like `16.6.328-cross-link:-[[..-00_index-medicine-moc]]...` — these come from MOC auto-scraping and pollute both chapters/ and the canonical list.

### Step 5 — Rebuild Site + Manifest + Run build_backup.py

```bash
python3 /mnt/tb/Sea-knowledge/#MedSea/scripts/build_site.py
python3 /mnt/tb/Sea-knowledge/#MedSea/scripts/build_backup.py /mnt/tb/Sea-knowledge/#MedSea
```

`build_backup.py` validates the canonical list matches what's in chapters/; reports `Copied / Missing md / Missing render` stats.

### Step 6 — Git Commit + Push (with buffer fix)

```bash
cd /mnt/tb/Sea-knowledge/#MedSea
git config http.postBuffer 524288000  # CRITICAL — see Pitfalls
git add -A
git commit -m "Chapter: <summary>"
git push origin main
```

### Step 7 — Notion Upload (Selective, Not Bulk)

For new/changed topics only — don't re-run the bulk uploader. Use `templates/notion_upload_selective.py`. Key differences from the legacy `notion_upload_diseases.py`:
- Uses `Notion-Version: 2022-06-28` (NOT `2025-09-03` — broken for new parents)
- Discovers hub page IDs dynamically via `find_hub_page("Arrhythmias")` instead of hardcoding
- Accepts a topic list rather than iterating the full disease_topics.json

### Step 8 — Docker Redeploy

Use **`bash scripts/redeploy.sh`** (compose, fixed `container_name: medsea`). Do **not** use bare `docker build` + `docker run` — that creates `<none>` images and random container names. User preference: **do not** `docker container prune` or remove unrelated stopped containers unless explicitly asked. See `references/docker-compose-named-redeploy.md`.

### Step 9 — Verify Live

```bash
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8855/<chapter>/
curl -s http://localhost:8855/<chapter>/topics.json | python3 -c "import json,sys; print(len(json.load(sys.stdin).get('topics',[])))"
```

Confirm new slugs appear and any deleted junk is gone.

## Critical Lesson — Renumbering Touches All Sub-Levels

**The single biggest mistake:** renaming the parent chapter folder (e.g., `15. Nephrology` → `18. Nephrology and Urology`) but leaving the topic sub-prefixes in the old format (`15.1.1-clinical-examination-kidney-urinary-tract/` instead of `18.1.1-...`).

The user will notice this on the website and demand a fix. **Always update ALL of:**
1. Parent chapter folder name (in `chapters/`, `site/`, local `Sea-knowledge/`)
2. **Topic subfolder/file prefixes in `chapters/<slug>/diseases/`** (e.g., `15.1.1-name` → `18.1.1-name`)
3. Topic file prefixes in `site/<slug>/diseases/` (regenerates from chapters but explicit verify helps)
4. Subdirectory names in local `/mnt/tb/Sea-knowledge/<Chapter>/<old.N. Name>/` (e.g., `15.1. Renal Anatomy` → `18.1. Renal Anatomy`)

**Two storage patterns for topics** (must handle both in any renumbering script):
- **Subdir pattern** (e.g., nephrology, cardiology): `diseases/15.1.1-name/topic.{md,html,png}` or `diseases/16.1.25-atherosclerosis-pathogenesis/clinical-examination...{md,html,png}`
- **Flat pattern** (e.g., endocrinology, gastroenterology): `diseases/18.1.01-dynamic-testing-principles.{md,png}` — files directly in `diseases/`, no subdir

Reference script: `scripts/renumber_chapters.py` (handles both patterns in one pass).

## Davidson 25th Ed Chapter → MedSea Slug → Source Dir Mapping (live)

| 25th Ed | Title | MedSea slug | Notion Root ID | `/mnt/tb/Medicine` source dir |
|---------|-------|-------------|----------------|-------------------------------|
| 1 | Clinical decision-making | 1-clinical-decision-making | | Clinical Decision-Making |
| 2 | Clinical therapeutics and good prescribing | 2-clinical-therapeutics | | Clinical Therapeutics and Good Prescribing |
| 3 | Clinical genetics | 3-clinical-genetics | | Clinical Genetics |
| 4 | Clinical immunology | 4-clinical-immunology | | Clinical Immunology |
| 5 | Nutritional factors in disease | 5-nutritional-factors | | Nutritional Factors in Disease |
| 6 | Population health and epidemiology | 6-population-health | | Population Health and Epidemiology |
| 7 | Principles of infectious disease | 7-principles-of-infection | | Principles of Infectious Disease |
| 8 | Oncology | 8-oncology | | Oncology |
| 9 | Pain and palliative care | 9-palliative-care | | Pain and Palliative Care |
| 10 | Acute medicine and critical illness | 10-acute-medicine | 3835588e846f81a1bd40fbd5d564fd2e | Acute Medicine and Critical Illness |
| 11 | Poisoning | 11-poisoning | abc75846ef544efcb3b78f00134f50b2 | **`Chapter 7 - Poisoning`** (NOT "Poisoning/" — empty) |
| 12 | Envenomation | 12-envenomation | fce508f973a64d58b48ad1e2d186e39d | Envenomation |
| 13 | Medicine in austere environments | 13-austere-medicine | b9b201cbbecc4eaab3c4b6c958c8ac11 | **`Environmental medicine`** (NOT "Medicine in Austere Environments/" — empty) |
| 14 | Infectious disease | 14-infectious-disease | eb9d6efbe3bb4ccc8302396a8edc57cf | Infectious Disease |
| 15 | Sexually transmitted infections | 15-sexually-transmitted-infections | 19c59a0895cd4ea4bee4e69d90ce37c8 | Sexually Transmitted Infections |
| 16 | Cardiology | 16-cardiology | 8baa010d9cc94c48826136417d383973 | Cardiology |
| 17 | Respiratory medicine | 17-respiratory-medicine | 3855588e846f8189bb8cca4e98407910 | Respiratory |
| 18 | Nephrology and urology | 18-nephrology-urology | 710f215344c34692af7584e89e714ff0 | Nephrology and Urology |
| 19 | Clinical biochemistry and metabolic medicine | 19-clinical-biochemistry-and-metabolic-medi | 184c380212d94c48a17cd879d941e6a3 | Clinical Biochemistry and Metabolic Medicine |
| 20 | Endocrinology | 20-endocrinology | 9db6455d6ae840f0ac29129217d6ccef | Endocrinology |
| 22 | Gastroenterology | 22-gastroenterology | bbfd97790eca482eaed8d47428a642b2 | Gastroenterology |

**⚠️ Source-dir traps (validated 2026-06-21 Ch 11-15 sync):**
- **Ch 11:** the source folder is `Chapter 7 - Poisoning/` (numbered + spaced), NOT `Poisoning/`. The latter is a 1-file stub. Any sync script that hardcodes `Poisoning` will silently get only 1 file instead of 36.
- **Ch 13:** the source folder is `Environmental medicine/` (case-sensitive lowercase "m"), NOT `Medicine in Austere Environments/`. The latter is completely empty. Confirmed 2026-06-21: `ls "/mnt/tb/Medicine/Medicine in Austere Environments/"` returns 0 files; `ls "/mnt/tb/Medicine/Environmental medicine/"` returns 9 source MDs.
- **Ch 19:** the source is `Clinical Biochemistry and Metabolic Medicine` (with "and", not "&"). The MedSea slug is `19-clinical-biochemistry-and-metabolic-medi` (abbreviated without "cal-medicine" at the end — preserves compatibility with existing Notion chapter root ID).

Always query the actual source dir with `ls /mnt/tb/Medicine/` before assuming the folder name from the 25th Ed title. The folder naming convention in `/mnt/tb/Medicine/` is editorial (matches the printed book chapter order), not the chapter title.

Always query the live DB to confirm the 25th Ed page exists before using an ID from this table — the MedSea DB has duplicates (e.g., Ch 10 has both "Acute Medicine and Critical Illness" and "Acute medicine and critical illness" entries). To find a 25th Ed page for a known topic, use the `search_existing_root(dav_num, name)` pattern in `references/notion-medsea-patterns.md`.

(19, 21, 23-32 not yet built — see "Pending Work" below.)

## Renderer Quirks (see references/renderer-quirks.md)

- **Header format:** must be `## N. Title` (numeric-prefixed) or pre-process to add numbers
- **Output path:** `out_dir/slug/{slug}.{png,html,md}` — NOT `out_dir/slug/topic.{ext}`. The script creates a subdir with the slug name.
- **Mermaid blocks:** ```mindmap``` and ```flowchart``` code blocks need explicit `render_mindmap()` / `render_flowchart()` handling in `render_topic.py` — they don't auto-render
- **Unnumbered `##` headers** (e.g., `## 24-Hour Recall Prompts`) caused an infinite loop in `parse_markdown_to_html` — fixed 2026-06-19 to skip/tolerate them
- **Truncation retry:** for files > 200 lines that hang/timeout, retry with truncation to 100-150 lines
- **Re-flatten after build:** the renderer's nested output must be flattened to `diseases/<prefix>-name/topic.{md,html,png}` before `build_site.py` will pick up PNGs

## Asset Optimization — Minify + Responsive WebP (see references/asset-optimization-minify-webp.md)

Final-polish pass for the static site: minify all JS/CSS with `terser` + `clean-css-cli`, generate the three responsive WebP variants (original / -960w / -480w) every PNG needs for the chapter `<picture>` srcset to actually pay off on mobile, debug CSS brace-balance errors that produce phantom minifier warnings, and pre-deploy hygiene.

Reusable scripts:

- `scripts/audit_webp_variants.py` — reports how many `-480w.webp` etc are missing across the site
- `scripts/generate_missing_webp.py` — runs `cwebp -q 80 [-resize W 0]`, idempotent, ~2 files/sec; **always run via `terminal(background=true, notify_on_complete=true)`** — full sweep on 3000 PNGs takes ~75 min

Three quick gotchas embedded in that reference:
- `node_modules/.bin/terser` / `cleancss` shims can `Permission denied`; call `node node_modules/<pkg>/bin/<bin>` directly instead
- `cleancss` warnings like "Unexpected `}` at line 1899" usually mean exactly one stray `}` — confirm with `txt.count('{') vs txt.count('}')`, then delete the orphan brace and rerun
- `terminal(workdir='/mnt/tb/Sea-knowledge/#MedSea/site')` is blocked by the `#`; use `workdir='/root'` and `cd '/mnt/tb/Sea-knowledge/#MedSea/site' && …` at the start of the command instead

## Bulk Notion Content Sync (see references/notion-bulk-sync.md)

Validated drop-in pattern for syncing a chapter's 900+ topic pages to Notion in ~1.5 hours with 0 errors. Covers: title normalization (`CH.HUB.NNN Title` → slug), skip-if-already-good gate (block-count threshold), 6-worker parallel execution, env-based API key loading, and resume-after-kill recovery. Two non-obvious traps documented: (1) direct slug match fails on every topic unless you strip the Notion title prefix, (2) blindly re-uploading all 951 topics takes 3+ hours — the skip gate cuts that by half.

## APPEND-Only Notion Sync — When the Existing Content Is "Stale" Not "Empty" (validated Ch 11-15, 2026-06-21)

**Use this instead of the bulk DELETE+append pattern when Notion pages already have content from a prior sync, but the content is shorter/older than MedSea's current source.** The DELETE+append approach breaks under Notion's rate limits when the prior content has many blocks (each DELETE is a separate API call). Validated: 139 topics × ~400 blocks each in 879s with 0 failures.

**The pattern:**
```python
def md_to_blocks(md, with_header=True):
    blocks = []
    if with_header:
        # Add a clear divider so users can find the new content
        blocks.append({"object": "block", "type": "divider", "divider": {}})
        blocks.append({"object": "block", "type": "callout", "callout": {
            "rich_text": [{"type": "text", "text": {"content":
                "📘 MedSea 100% Content (synced YYYY-MM-DD) — word-for-word match with /mnt/tb/Medicine source. Stale content above this divider is the previous Notion version."}}],
            "icon": {"type": "emoji", "emoji": "📘"},
            "color": "blue_background"
        }})
    # ... rest is the standard md→blocks conversion
    return blocks
```

Then in `process_topic()`: **skip the DELETE step entirely.** Just PATCH the new blocks. The old content stays above; the new 100%-match content is below the divider callout. Trade-off: each page has ~2x the blocks (old + new) — pages are bigger but every page IS complete and 100% match with source.

**Why APPEND-only beats DELETE+append when content is already substantial:**
| Pattern | Per-topic API calls | 100-topic sync | 400-block topics (Ch 11-15) | Failure mode |
|---|---|---|---|---|
| DELETE+append | 400 DELETEs + 4 PATCHes = 404 | 40,400 calls | 11+ hours even at 1 call/s | 429 cascade from parallel DELETEs; thread pool exhausts retries |
| APPEND-only | 4 PATCHes | 400 calls | 15-20 min | None observed in Ch 11-15 sync (139 topics, 0 failures) |

**Safe rate limit:** Use `RATE = 0.4` (2.5 req/s) in the rate limiter, NOT 0.36. The 0.36s sleep was tested and still produced cascading 429s during heavy periods. 0.4s gives safe margin under Notion's 3 RPS burst limit and the 429 backoff kicks in cleanly. Pattern:

```python
import threading
RATE = 0.4
_last = [0]
_lock = threading.Lock()

def http(method, url, data=None, retries=4):
    with _lock:
        wait = RATE - (time.time() - _last[0])
        if wait > 0: time.sleep(wait)
        _last[0] = time.time()
    # ... rest
```

**Match-verification check after APPEND sync** (the old content is still there, so don't claim "100% match" without confirming):
```python
# Get total chars across ALL pages (not just first 100)
r = http("GET", f"/blocks/{page_id}/children?page_size=100")
total = len(r["results"])
chars = sum(len(x.get("text", {}).get("content", "")) for b in r["results"] for x in b.get(b.get("type", ""), {}).get("rich_text", []))
# Pages with MedSea 18K chars + old 12K = ~30K chars is correct (old + new stacked)
# Pages with only 18K means APPEND didn't happen (sync silently failed for that page)
```

**Special-case handling: 2 unmatched topics in Ch 14 + Ch 15.** The clean script's fuzzy title match missed `14.1.55-pneumocystis-pneumonia-pcp` (Notion title is `Pneumocystis Pneumonia (PCP / PJP)` — parens break the `in` containment check) and `15.3.06-syphilis-serology-interpretation` (Notion hub 15.3 had only 5 topics; topic didn't exist). Handle in a separate post-script:
1. For "title with parens" mismatches: append directly to the existing page (page ID discovered via search)
2. For "page doesn't exist": `POST /v1/pages` with `parent: {page_id: <hub_id>}` then PATCH the content blocks. Do this AFTER the main sync so the bulk run isn't blocked by per-topic exception handling.

**Title-paren gotcha (validated 2026-06-21):** The `match_slug_to_notion()` fuzzy check `if title_lc in t or t in title_lc` works for `pneumocystis pneumonia pcp` ↔ `pneumocystis pneumonia pcp / pjp` only AFTER stripping the parens. The raw Notion title keeps `(PCP / PJP)` and breaks the substring match. Fix: pre-normalize the candidate t by removing `\(.*?\)` and `/.*` suffixes before comparison, or use bag-of-words overlap (`len(set(slug_words) & set(t_words)) >= 2`).

See `references/notion-append-only-sync.md` for the full v4 script (139 topics in 879s).

## Full-Note + Mermaid.js Migration (see references/full-note-migration.md)

**Use this instead of `render_topic.py` when the user wants full study notes on the website with real diagrams (no A4 PNG).** Validated 2026-06-20 on Ch 16 Cardiology (570 notes → 899 chapters → 2,957 total topics live).

The pattern: skip the renderer entirely. Migrate Medicine MDs directly into `chapters/<slug>/diseases/`, render client-side with `mermaid@10` CDN, drop all PNGs.

Three required build_site.py patches:
1. `flush_code()` — emit `<pre class="mermaid">` for mindmap/flowchart/graph blocks (replaces styled HTML approximations)
2. `page_footer()` — add `mermaid@10` CDN + `renderMermaidIn()` JS hook + `DOMContentLoaded` auto-render
3. `showTopic()` — call `renderMermaidIn(container)` after `innerHTML = ...` so dynamically-loaded topics also render diagrams

Plus one bug fix: `loadManifest()` must split URL `?topic=16.6.334-foo-bar` on `-` to find `local_prefix=16.6.334` (the full string never matches the manifest).

## Chapter Overview Pages (MOC + Hierarchy) — see references/moc-hierarchy-overview.md and references/audit-gotchas.md

Every chapter synced since 2026-06-20 has two chapter-level overview files: `diseases/X.0.900-chapter-moc/topic.md` (Map of Content) and `diseases/X.0.901-chapter-hierarchy/topic.md`. They render as regular topics grouped under a virtual `X.0` hub. Use the `X.0.900` / `X.0.901` prefix range to avoid collision with the chapter's existing `X.0.Y` folder scheme (which can have hub roots like `21.0.1-classification-and-diagnosis-of-diabetes-mellitus`). Special atomic topics use `X.0.902` and beyond (e.g., `16.0.902-heart-failure-overview`, `23.0.902-palliative-care-advanced-liver-disease`).

**Audit must verify these are present** — counting only atomic topics is NOT sufficient for "100% complete". See `references/audit-gotchas.md` for the slug-format pitfalls (ch 1-9 use flat `diseases/X.Y.Z-slug.md` files; ch 10-32 use subdir `diseases/X.Y.Z-slug/topic.md`), the regex bug that creates orphan `31.31` hubs, and the rule to always verify by content-hash not by name (truncated folder names like `32.6.1-advance-care-planning-and-end-of-life-decision-mak` are byte-identical to source despite the missing "ing").

Pattern: generate source MDs at `chapters/<slug>/overview/{moc,hierarchy}.md`, copy into `diseases/X.0.900-…/topic.md` and `diseases/X.0.901-…/topic.md`, patch `manifest.json` to add `X.0` hub + 2 disease entries, rebuild site. Notion sync uses the chapter root page IDs from `/tmp/overview_chapter_pages.json` (extracted from `build_site.py`'s `BUILT_CHAPTERS`) with native `markdown` field for auto-conversion.

## Docker Port Mapping — nginx Inside Container Listens on 80, NOT 8855

The Dockerfile `EXPOSE 8855` is documentation only. nginx default config listens on **port 80** inside the container. Use:

```bash
docker run -d --name medsea --restart unless-stopped -p 8855:80 medsea-site:latest
```

**NOT** `-p 8855:8855` (leaves the port unmapped → curl returns HTTP 000 even though the container is "Up").

**This pitfall hit twice in one session** (initial deploy + post-rebuild redeploy). Verification step after every container recreate:

```bash
docker ps --format '{{.Names}}\t{{.Ports}}' | grep medsea   # must show "0.0.0.0:8855->80/tcp"
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8855/
```

If `HTTP 000` but container is "Up": port mapping is wrong, not the container.
- **Output naming mismatch (sync trap):** renderer writes `{slug}.{md,html,png}` into `out_dir/{slug}/`. The chapters/ folder convention is `topic.{md,html,png}` inside `diseases/<prefix>-<slug>/`. The sync script must rename on copy — if it doesn't, `build_site.py` silently skips the topic (no PNG found) and the page renders empty on the live site. Confirmed lost in cardiology sync 2026-06-19 before fixing.

### `POST /v1/pages` with `markdown` + `children` in same request → 400
**Pitfall — `Bash` shell strips literal `***` from script files.** When writing a Python script that needs a secret, never use `KEY = "***"` literally — the write_file output and `Bash` heredocs both sanitize it. Always use `KEY = os.environ.get("NOTION_API_KEY", "")` and pass the env at invocation time: `NOTION_API_KEY="$NOTION_API_KEY" python3 script.py`. Validated 2026-06-20 when 5 audit/upload scripts in `/tmp/` failed with HTTP 401 until switched to env-based loading.

**Pitfall — naive slug normalization produces 95%+ false-positive "missing" matches.** First audit reported 601/601 Ch 16 source files as missing in MedSea; only ~5 were actually missing. The failures were slug-normalization artifacts. Required handling:
- Strip `_Hub`, `_Hub.md`, `_full`, `_Template`, `_roadmap`, `MOC`, `Hierarchy` from source filenames (case-insensitive)
- Strip leading numeric prefixes: `01_`, `1.`, `16.1.25-`, etc.
- Normalize underscores→hyphens, drop all non-alphanumeric
- For flat-file source chapters (Ch 19 Biochemistry, Ch 20 Endocrinology, source files like `Acromegaly.md` directly in chapter root), is_hub_overview detection by `root == chapter_dir` is WRONG — these are individual topic MDs, not hub summaries. Use a per-chapter decision or a content-based heuristic (look for the topic title appearing as a real MedSea sub-topic vs being a parent category like "Adrenal Disorders", "Pleural Diseases"). Validated 2026-06-20: Ch 19 went from 5 false missing → 0 false missing once `_Hub` filter applied and flat-file pattern respected.

**Pitfall — MedSea uses different topic storage patterns per chapter:**
- **Subdir pattern** (Ch 11, 12, 13, 14, 16, 17): `diseases/<prefix>-<slug>/topic.{md,html,png}` — folder per topic, files inside. Used by chapters built via the full-note + mermaid.js migration (Ch 16 was the pioneer).
- **Flat pattern** (Ch 18, 19, 20): `diseases/<prefix>-<slug>.{md,html,png}` — files directly in `diseases/`. Used by older chapter builds (Ch 18 Nephrology predates the migration).
- **Mixed flat+subdir** (Ch 16): mostly subdir but a few outliers use flat (e.g. `16.6.310-stemi-primary-pci-<90-min-fibrinolysis-if-pci->120-min/topic.md`).
When creating a new topic, detect the chapter's dominant pattern first (`ls chapters/<slug>/diseases/` — count subdirs vs flat files). Putting a flat-file topic into a subdir-pattern chapter (or vice versa) causes `build_site.py` to silently skip it. Validated 2026-06-20: Ch 18's 2 new Urinalysis/GFR topics were initially created with subdir pattern (matching Ch 14/16); had to convert to flat pattern by `mv "$f/topic.md" "$f.md" && rmdir "$f"`.

**Pitfall — Docker rebuild takes ~5 min for the 1GB+ site/ directory.** Foreground `bash /tmp/redeploy.sh` hits the 300s shell timeout even though the build itself succeeds. Use the background + notify pattern:
```bash
terminal(background=true, notify_on_complete=true)
```
Script body: `set -e` + `docker build --no-cache -t medsea-site:latest . >> log 2>&1` + `docker stop medsea >> log 2>&1 || true` + `docker rm medsea >> log 2>&1 || true` + `docker run -d --name medsea --restart unless-stopped -p 8855:80 medsea-site:latest >> log 2>&1`. Wait for `proc_XXX` completion notification before verifying live. Without `--no-cache`, parent-snapshot cache corruption (NotFound: parent snapshot sha256:...) breaks the rebuild — happened 2026-06-20 on first redeploy attempt after the prior container used a different base layer.

**Pitfall — bulk Notion hub discovery must be lazy + cached.** Walking 17 hubs × 100 children/page × N topics per hub = 1700+ API calls per chapter at Notion's rate limit (~3 req/s) = 10+ min per chapter just to count. Faster approach: read MedSea's local `manifest.json` for `total_diseases` and `hubs[].disease_count` (instant), then only walk Notion's `child_page` tree if you need to verify individual topic presence (e.g., confirm a newly-added topic page was created). The manifest is the filesystem ground truth; Notion is downstream. Validated 2026-06-20 Ch 11-15 audit: 5 chapters × 30 seconds = 2.5 min using manifest counts, vs estimated 30+ min if walking Notion tree.

**Pitfall — Notion topic-page title normalization for slug matching.** Notion stores topic pages as `child_page` blocks under hub pages, with titles like `16.2.251 Anticoagulation in Pregnancy` (chapter.hub.NNN prefix prepended by upload scripts). MedSea file slugs are just `anticoagulation-in-pregnancy`. Direct string match fails on every topic. Canonical normalization:

```python
import re

def clean_notion_title(full_title):
    """Strip 'CH.HUB.NNN ' prefix and lowercase."""
    return re.sub(r"^\d+\.\d+\.\d+\s+", "", full_title).lower().strip()

def match_slug_to_notion(slug, hub_topics_dict):
    """slug='anticoagulation-in-pregnancy', topics={title_lower: page_id}.
    Returns page_id or None."""
    title_lc = slug.replace("-", " ").strip()
    if title_lc in hub_topics_dict:
        return hub_topics_dict[title_lc]
    if slug in hub_topics_dict:
        return hub_topics_dict[slug]
    # Fuzzy: containment either way (handles 'pleural-air-disorders' ↔ 'pleural diseases')
    for t, pid in hub_topics_dict.items():
        if title_lc in t or t in title_lc:
            return pid
    return None
```

Use the cleaned-title map (`/tmp/ch16_20_topics_clean.json` style — title-without-prefix → page_id) for batch Notion syncs. Without normalization, ~95% of topic pages look "not found" and the sync silently skips them all. Validated 2026-06-20 Ch 16-20: 888/889 topics matched after normalization vs 0/889 with naive string match.

**Pitfall — large topic content updates need a "skip if already good" gate.** A bulk Notion content-refresh that blindly deletes + re-appends every page's blocks takes 5-10 sec per topic = 951 topics × 8s = 2+ hours per chapter. The vast majority of pages already have correct content from prior syncs — only re-write pages where the existing content is meaningfully shorter than MedSea. The right threshold check is **block-count ratio**, not "any non-nav blocks exist" (the old trap reported pages with only 5 nav links as "already has content" and skipped pages with 50+ nav links but no real content as "also has content"):

```python
def needs_update(page_id, expected_block_count):
    """Returns True if Notion page has <85% of MedSea's expected block count."""
    existing_ids = get_all_block_ids(page_id)  # paginated GET /blocks/{id}/children
    return len(existing_ids) < int(expected_block_count * 0.85)
```

`expected_block_count` = number of non-empty non-code-fence lines in the MedSea MD. For pages that pass the gate, do the full delete + append. For pages that fail it, skip — trust the existing content (or re-check by content-hash for high-stakes topics). Validated 2026-06-20 Ch 16-20 v5 sync: 487/951 skipped via this gate, total run time dropped from "didn't finish in 3 hours" to ~1.5 hours, with the actual updates targeted at the 363 pages that genuinely needed fixing.

**Pitfall — when fixing a botched Notion hub layout, RENAME the originals, don't create new pages.** If a previous sync left Ch 18 root with hubs labeled `15.1–15.6` (wrong chapter number) but the actual topic content is Ch 18 material, the correct fix is `PATCH /v1/pages/{hub_id}` on each existing hub with a corrected `properties.title` array — NOT `POST /v1/pages` to create `18.1–18.6` next to the wrongly-labeled ones. Three reasons:
1. The original hubs already contain child topic pages. Creating new empty hubs leaves the original (correct content) under the wrong parent and the new (empty) hub visible in nav.
2. Notion does NOT support `DELETE` on a `child_page` block that has children — it archives them, but then the archived page returns 400 (`Can't edit block that is archived`) on any subsequent PATCH, so renaming its children requires first restoring it. The python error `400 validation_error: Can't edit block that is archived. You must unarchive the block before editing` is the symptom.
3. Multiple parallel hubs (15.1 vs 18.1) cause double-listing in the chapter sidebar and double-counting in `count_child_pages()` audits.

Correct fix flow:
```python
# Step 1: Update existing hub titles in-place (e.g. "15.1. Renal Anatomy" → "18.1. Renal Anatomy")
# Step 2: For chapters where root has 0 children (e.g. Ch 19 was empty), create new hubs
# Step 3: Don't try to delete wrongly-numbered duplicates — they were auto-archived by the previous botched sync; let them rot in the archive
```
Validated 2026-06-20: Ch 18 had `15.1–15.6` with topic children. Renamed in place. Ch 19 root was empty → created `19.1–19.7` from manifest. Ch 20 had `18.1–18.11` → renamed to `20.1–20.11`. Skip the obvious "delete and recreate" reflex.

**Pitfall — `tcsetattr: Inappropriate ioctl for device` is a red herring.** When a long-running background Python script is launched via `terminal(background=true)` and then later the wrapper bash logs show `bash: [PID: 1 (255)] tcsetattr: Inappropriate ioctl for device`, the python process did NOT die — the wrapper just lost its controlling terminal. The actual script continues running under its child PID. To verify it's still alive:

```bash
ps -o etime= -p <bash_pid> 2>/dev/null     # shows do_wait — bash waiting on child
pgrep -P <bash_pid>                          # gives the actual python PID
ps -o etime= -p <python_pid> 2>/dev/null     # shows actual python uptime
cat /proc/<python_pid>/io                    # rchar/wchar/syscr grow if working
```

The real progress signal is the script's own checkpoint file (e.g. `/tmp/sync_v5_progress.json`) updated every N items, NOT the bash wrapper log. Always look for the script's own progress file before assuming the sync died. Validated 2026-06-20 Ch 16-20: assumed the bash "tcsetattr" error meant the python was dead; checked `/tmp/sync_v3_progress.json` and saw it had updated to 25/951 with 0 errors — the script was alive and processing fine, just buffered through `tee`.

**Pitfall — website render process overwrites `topic.md` with rendered-infographic version (Ch 16 drift, 2026-06-21).** The Ch 16 chapter was the first to be built with the "Sea Knowledge study infographic" rendering pipeline (HTML-styled study cards). When that render runs, it writes `diseases/<prefix>-<slug>/topic.html` (for browser display) and ALSO overwrites the source `topic.md` with a slimmed rendered-markdown version that includes `<callout icon="🚑" color="red_bg">` tags. The result: working dir has 95-line rendered MD; HEAD still has the 204-line full source MD from commit `85ad30a`. `git status` shows 328 modified + 660 untracked files (HTML+PNG+modified-MD) for Ch 16.

**This is a content-loss hazard:** if a user runs `git add -A && git commit` on Ch 16's working dir without first reviewing, the full source content in HEAD gets replaced with the rendered infographic version on `origin/main`. The website still works (it reads `topic.html`, not `topic.md`), but downstream consumers like Notion sync scripts that read the local `topic.md` lose 50%+ of the content.

**Detection (before committing):**
```bash
git status -s chapters/16-cardiology | wc -l
# If >100 M files in Ch 16 specifically, the render overwrote topic.md
# Spot-check: head -20 chapters/16-cardiology/diseases/16.1.25-.../topic.md
# If it starts with "# Atherosclerosis Pathogenesis\n\n<callout icon=..." it's the rendered version
# Real source starts with "---\ntags: [medicine, cardiology, davidson, fcps, mrcp]..."
```

**Fix (3 options, pick based on intent):**
1. **User wants the rendered version to be canonical** (e.g. for new "infographic" style): commit everything. But document in commit message that HEAD is now the rendered format, not the full source. Notion sync scripts that depend on full content need updating.
2. **User wants to preserve full source** (e.g. they're rendering for the website but the MedSea repo stays the source of truth): `git restore chapters/16-cardiology/diseases/*/topic.md` to revert all MDs to HEAD. Then `git add chapters/16-cardiology/diseases/*/topic.html` and `topic.png` selectively for the website build artifacts you actually want committed. PNGs are regenereable; commit them only if the build is expensive.
3. **Hybrid** (the safest default): keep HEAD as the source, add only the `topic.html` to git (since HTML has the rendered version + a wrapper), and `git restore` all `topic.md` changes. The website still works because the build process generates fresh HTML from MD at deploy time anyway.

**Validated 2026-06-21:** Ch 16 working dir drift was detected during a 4-platform audit. No commit was made; user was notified of the drift before any push. Don't blindly `git add -A` after a render.

**Pitfall — `hub overview` files in `/mnt/tb/Medicine` look like disease topics but aren't individual topics.** Chapter source folders contain 2 types of `.md` files:
1. **Disease topics** — one file per disease (e.g. `Acute Kidney Injury (AKI).md`, `Pneumonia.md`) — these go into `diseases/<X.Y.NN>-<slug>/topic.md`
2. **Hub overviews** — one file per major category (e.g. `Airway Diseases.md`, `Functional Anatomy, Physiology, and Investigations.md`, `Metabolic Medicine.md`) — these summarize a whole hub of sub-topics and should NOT be treated as individual topics

The 3-way audit pattern (see Step 0a) treats both as "topics" and reports the hub overviews as "missing from MedSea". They aren't missing — they were intentionally broken into the per-disease sub-topics that are already in MedSea. Filter the audit's NEEDS-UPLOAD list with a heuristic before adding:

```python
# Hub overviews tend to be SHORT (<2KB) and use broad category names
# Or match: source filename == hub name from the chapter's Hierarchy.md
import re
HUB_OVERVIEW_PATTERNS = [
    r"^Airway Diseases\.md$",
    r"^Pleural Diseases\.md$",
    r"^Pulmonary Vascular Diseases\.md$",
    r"^Respiratory Infections\.md$",
    r"^Thoracic Malignancy\.md$",
    r"^Metabolic Medicine\.md$",  # Ch 19 overview, not a disease
    r"^Acid-Base Disorders\.md$", # Ch 19 overview
    # ... add per chapter
]
def is_hub_overview(filename, source_dir):
    if filename in HUB_OVERVIEW_PATTERNS: return True
    if (source_dir / filename).stat().st_size < 2000: return True  # <2KB usually = overview
    return False
```

Validated 2026-06-21 Ch 17-20 audit: 33 of 38 "missing" topics were hub overviews, not diseases. Only 1-2 per chapter were actual missing disease topics. Don't bulk-add hub overviews as fake topics — it pollutes the diseases/ namespace and breaks `build_site.py` slug parsing.

**When the user asks for "100% match" with `/mnt/tb/Medicine`:** if they want ALL information including hub overviews, sync the overviews to a separate `chapters/<slug>/overview/` directory (not into `diseases/`). Update `manifest.json` with a new "overview" section so the website renders them as chapter-level pages, not as individual disease cards. The `X.0.900-moc` and `X.0.901-hierarchy` prefix scheme already covers chapter-level pages — hub overviews can use `X.0.902-...` through `X.0.999-...` or be added under their respective hub root (`X.Y.0-...`).

**Pitfall — Notion `chapter_page_id` is shared across renames.** When the user renumbered Ch 10 from "Acute Medicine" to "Acute Medicine and Critical Illness", the MedSea DB ended up with two chapter pages (24th and 25th Ed). The 25th Ed page is what BUILT_CHAPTERS points to and where the bulk topic sync lives. The 24th Ed page is orphaned but still in the DB — don't accidentally upload new topics under it. Pattern: query the chapter page's `child_page` list, look for `child_page.title.startswith("N. ")` where N is the Davidson chapter number and the title matches the 25th Ed label exactly. If two match, the one whose `last_edited_time` is most recent AND whose topics.json URL matches `BUILT_CHAPTERS[slug]` is the live one.
| **Docker build cache corruption** | `docker build` fails mid-COPY with `NotFound: parent snapshot sha256:... does not exist` (random non-existent layer hash) | Re-run with `--no-cache`. Forces full rebuild (~5 min for site/ at 1 GB). Cache can corrupt after long sessions with many rebuilds |
| **Wrong storage pattern when adding topics to existing chapter** | Created `diseases/18.1.7-name/topic.md` (subdir pattern) but Ch 18 uses flat `diseases/18.1.7-name.md` — build script silently doesn't pick it up | Before adding, check existing layout: list one sibling in the target chapter and see if files are flat `.md` or inside a subdir with `topic.md`. The flat-vs-subdir split is per-chapter, not global |
| **Topic number collision when picking "next"** | Picked `16.6.1` for Ch 16 expecting per-hub reset; existing topic already has `16.6.1-...` from another hub context — silent shadow | Check the actual MAX across ALL hubs in the chapter before picking. Ch 16 uses global sequential (16.6.310-355+); Ch 17-20 use per-hub reset |
| **Hub-overview MDs at chapter root flagged as "missing topics"** | Source has `Adrenal Disorders.md` at `/mnt/tb/Medicine/Endocrinology/`; audit reports it as missing; MedSea actually represents it as a hub page with specific disorders as topic children | Filter out root-level MDs (parent dir == chapter_dir) AND `_Hub.md` suffix files before slug matching. Title-fuzzy match the rest to catch umbrella files that have been split into sub-topics |
| **Notion hub numbering drift from MedSea** | Source/MedSea hub `18.1` doesn't exist in Notion; actual Notion hub is `15.1` (chapter was renumbered 24th→25th Ed) | Always query Notion for the actual hub titles BEFORE pushing topics. Match by hub number OR by hub name substring. Never hardcode hub IDs |
| **`***` literal in Python scripts gets sanitized on write** | `KEY = "***"` written via `write_file` becomes literal `***` (still HTTP 401); Bash heredoc same problem | Always `KEY = os.environ.get("NOTION_API_KEY", "")` and pass env at invocation. The `***` placeholder pattern doesn't survive sanitization |
| **Hub/slug regex parse wrong → orphan "31.31" hub** | A Notion sync script used `^(\d+)\.(\d+)\.(\d+)-(.+)$` to parse folder names like `31.1.1-foo` — produced hub="31", idx="31", sub="1" instead of hub="31.1", idx="1". Created orphan `31.31 Hub 31.31` and 49 wrongly-bucketed child topics before being killed | Always use the SAME regex as `build_site.py`: `^(\d+\.\d+)\.(\d+)-(.+)$` → hub="X.Y", idx="Z", slug="rest". Test parsing on 2-3 folders BEFORE running bulk sync |
| **Folder name truncation vs full content** | MedSea folder names get truncated at ~50-60 chars during prior sync work (e.g., `32.6.1-advance-care-planning-and-end-of-life-decision-mak` missing "ing"). Slug-comparison falsely reports these as "missing" | Use content-hash comparison (`hash(open(f).read())`) for true presence detection. Truncated-name match against source is unreliable; content match is exact |
| **MOC + Hierarchy overview pages** | All chapters built/updated since 2026-06-20 have chapter-level overview pages: `diseases/X.0.900-chapter-moc/topic.md` (MOC) and `diseases/X.0.901-chapter-hierarchy/topic.md` (Hierarchy). They appear as regular topics in `topics.json` with hub="X.0". Use prefix `900`/`901` to avoid collision with atomic topic indexes | See `references/moc-hierarchy-overview.md` for the template and sync pattern |
| **Orphan pages from failed sync** | Buggy Notion sync left behind orphan hub pages with wrongly-bucketed children. Manual one-by-one deletion is slow and error-prone | Run `scripts/notion_cleanup_orphans.py "31.31"` to search-and-archive all pages with a given title prefix. Confirms before deleting, archives (not hard-deletes) for 30-day recovery |