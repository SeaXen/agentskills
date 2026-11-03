# MOC + Hierarchy Overview Pages (X.0.900 / X.0.901)

Pattern validated 2026-06-20 across ch 16, 21-30, and 31-32. Use this when a chapter needs
chapter-level integrated content beyond the atomic topic collection — the kind of "MOC",
"Roadmap", or "Hierarchy" file that sits at the top of each Davidson chapter.

## What the overview pages are

For each chapter X, two overview files live at:

```
chapters/<X-slug>/overview/
├── moc.md               ← MOC (Map of Content)
└── hierarchy.md         ← Topic Hierarchy

chapters/<X-slug>/diseases/
├── X.0.900-chapter-moc/topic.md         ← build_site.py picks these up
└── X.0.901-chapter-hierarchy/topic.md
```

- **Overview source files** in `overview/` are the human-edited source of truth.
- **`diseases/X.0.900-…/topic.md`** are byte-identical copies used by `build_site.py` so the
  pages render on the live site. Keep them in sync.
- **Hub `X.0` is virtual** — added to `manifest.json` as `{num: "X.0", name: "Chapter Overview"}`
  so the sidebar groups these two pages under "Chapter Overview".

## Why `X.0.900` and `X.0.901` (not `X.0.1` / `X.0.2`)

Chapters 21–32 already use `X.0.Y` numbering for their own hub root (e.g., `21.0.1-adolescent-moc`
collides with real topics like `21.0.1-classification-and-diagnosis-of-diabetes-mellitus`). Picking
`900` and `901` guarantees no collision with the existing chapter hub structure regardless of how
many `X.0.X` folders exist.

Same trick applies to special atomic topics added later (e.g., `16.0.902-heart-failure-overview`,
`23.0.902-palliative-care-advanced-liver-disease`).

## Generate, copy, register — the canonical 3-step

```python
import json, shutil
from pathlib import Path

REPO = Path("/mnt/tb/Sea-knowledge/#MedSea")
ch_num = 31
slug = "31-adolescence-transition-and-young-adult-m"

# 1. Source files already exist at chapters/<slug>/overview/{moc,hierarchy}.md
#    (generated from /mnt/tb/Medicine/<Chapter>/<source-moc>.md + hierarchy source)

# 2. Copy into diseases/ so build_site.py picks them up
for sub, name in [("900-chapter-moc", "Chapter MOC (Map of Content)"),
                  ("901-chapter-hierarchy", "Chapter Topic Hierarchy")]:
    target = REPO / "chapters" / slug / "diseases" / f"{ch_num}.0.{sub}"
    target.mkdir(exist_ok=True)
    shutil.copy2(REPO / "chapters" / slug / "overview" / f"{sub.split('-')[1]}.md",
                 target / "topic.md")

# 3. Register in manifest.json
manifest = json.loads((REPO / "chapters" / slug / "manifest.json").read_text())
# Drop any stale X.0 entries
manifest["diseases"] = [d for d in manifest.get("diseases", [])
                        if not d.get("subnum", "").startswith(f"{ch_num}.0.")]
manifest["hubs"] = [h for h in manifest.get("hubs", []) if h.get("num") != f"{ch_num}.0"]

# Add X.0 hub (insertion order matters for sidebar render — insert at index 0)
manifest["hubs"].insert(0, {"num": f"{ch_num}.0", "name": "Chapter Overview",
                            "slug": "chapter-overview", "has_local_md": True})

# Add disease entries (idx negative so they sort first within their hub)
manifest["diseases"].extend([
    {"idx": -1000, "subnum": f"{ch_num}.0.900", "hub_num": f"{ch_num}.0",
     "parent_slug": "chapter-overview", "topic": f"{ch_num}.0.900 Chapter MOC (Map of Content)",
     "slug": "chapter-overview--chapter-moc--900",
     "folder": f"diseases/{ch_num}.0.900-chapter-moc",
     "has_md": True, "has_html": True, "has_png": False, "type": "moc"},
    {"idx": -999, "subnum": f"{ch_num}.0.901", "hub_num": f"{ch_num}.0",
     "parent_slug": "chapter-overview", "topic": f"{ch_num}.0.901 Chapter Topic Hierarchy",
     "slug": "chapter-overview--chapter-hierarchy--901",
     "folder": f"diseases/{ch_num}.0.901-chapter-hierarchy",
     "has_md": True, "has_html": True, "has_png": False, "type": "hierarchy"},
])
manifest["total_diseases"] = len(manifest["diseases"])
manifest["total_hubs"] = len(manifest["hubs"])
(REPO / "chapters" / slug / "manifest.json").write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False))
```

## Template — what MOC.md should contain

Use the validated 9-section template:

1. Frontmatter (`status: full-fcps-mrcp-hub`, `exam_relevance`, `cards`)
2. Header callout (blue_bg): document type, Davidson alignment, target exams, audience
3. Green callout: what this overview is and how to use it
4. Tier 1/2/3 study priority table (80/15/5% mark split)
5. Chapter scope (preserved from source — bullets, not new content)
6. Build summary (heading hub count, topic count, completion %)
7. Heading hubs table (preserved from source)
8. Key themes for FCPS/MRCP (preserved from source — DON'T rewrite)
9. Chapter-specific MCQs (5), SBAs (3), flashcards (15), spaced-repetition tracker (10 rows)
10. Cross-references and tags

**Rule:** preserve source content verbatim where possible. Augment, don't replace. The user
explicitly said "all information from /mnt/tb/Medicine" — if you summarize away HEEADSSS
or Gillick/Fraser bullet points from the source MOC, you've broken the contract.

## Hierarchy file — preserve as-is

The source `Davidson Chapter N - …Hierarchy.md` is already a complete topic map with
cross-references. Don't rewrite it. Strip YAML frontmatter, wrap in a small intro callout,
append the cross-reference footer pointing back to the MOC and source folder.

## Notion sync — the IDs matter

For each chapter root page, also create `Chapter MOC (Map of Content)` and
`Chapter Topic Hierarchy` sub-pages. The IDs for all chapter roots are at:

```
/tmp/overview_chapter_pages.json
```

Build that file by extracting page IDs from `build_site.py`'s `BUILT_CHAPTERS` dict:

```python
import re
from pathlib import Path

content = Path("/mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py").read_text()
pattern = re.compile(
    r'"([\w-]+)":\s*\(\s*"[^"]+",\s*"https://medsea\.notion\.site/[^"]*?([a-f0-9]{32})",'
)

CHAPTER_PAGES = {}
for slug, page_id in pattern.findall(content):
    if slug.startswith(("16-", "21-", "22-", "23-", "24-", "25-",
                         "26-", "27-", "28-", "29-", "30-", "31-", "32-")):
        ch_num = int(slug.split("-")[0])
        CHAPTER_PAGES[ch_num] = page_id
```

## Notion sync script outline (uses native `markdown` field)

```python
# Templates: /tmp/sync_overviews_to_notion.py — extended 2026-06-20 to ch 31+32

SYNC_ITEMS = []
for ch_num in [16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]:
    slug = slug_map[ch_num]
    SYNC_ITEMS.append({"ch_num": ch_num, "slug": slug,
                       "folder": f"{ch_num}.0.900-chapter-moc",
                       "title": "Chapter MOC (Map of Content)", "type": "moc"})
    SYNC_ITEMS.append({"ch_num": ch_num, "slug": slug,
                       "folder": f"{ch_num}.0.901-chapter-hierarchy",
                       "title": "Chapter Topic Hierarchy", "type": "hierarchy"})

# Skip-if-exists pattern (cheap idempotency):
existing = fetch_child_pages(chapter_root_id)
title_lower = title.lower()
if title_lower in existing:
    stats["skipped_existing"] += 1
    continue

# Create with native markdown field:
payload = {
    "parent": {"type": "page_id", "page_id": chapter_root_id},
    "properties": {"title": [{"type": "text", "text": {"content": title}}]},
    "markdown": md_content,
    "icon": {"type": "emoji", "emoji": "🗺️" if type == "moc" else "🌳"},
}
```

`markdown` field auto-converts headings/bullets/tables/callouts to blocks — way faster
than block-by-block JSON construction.

## End-to-end ordering for a NEW chapter

1. Generate MOC + Hierarchy source files at `chapters/<slug>/overview/`
2. Copy into `diseases/X.0.900-…` and `X.0.901-…`
3. Patch `manifest.json` (add X.0 hub + 2 disease entries)
4. `python3 scripts/site/build_site.py` (verify topic count went up by 2)
5. `docker build && docker restart` (verify HTTP 200 on `/X-slug/diseases/X.0.900-chapter-moc/topic.md`)
6. `git add -A && git commit && git push`
7. Add ch_num to `CHAPTER_PAGES` in `/tmp/overview_chapter_pages.json`
8. Run Notion sync script for overview pages only (skip-if-exists makes it idempotent)

## Validation: the 24-site topic count math

After adding both pages to all 12 chapters (16, 21-32), `topics.json` per chapter should grow by 2:

- ch 16: 907 → 909 (already had `X.0.902-heart-failure-overview` for a total of +3)
- ch 21: 238 → 240
- ch 22: 159 → 161
- ...
- ch 32: 39 → 41

If the topic count doesn't grow by exactly 2 (or 3 for ch 16/23 with specials), the manifest
patch didn't take. Re-check the `manifest.json` `total_diseases` field after `build_site.py`.