# 3-Way Audit Gotchas (Source / MedSea Local / Notion)

Concrete pitfalls hit during 2026-06-20 audit of Davidson chapters 6–10. Use this when comparing
`/mnt/tb/Medicine/<Chapter>` against `/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>/` against the
Notion chapter page tree.

## 1. MedSea topic layout is NOT uniform

Two on-disk layouts exist in `chapters/<slug>/diseases/`. Detect both:

| Layout | Example | Where it appears |
|---|---|---|
| **Flat** | `9.1.01-foo-full.md` + `9.1.01-foo-full.png` | Ch 1–9, 11–18 (most) |
| **Directory** | `10.1.01-foo/topic.md` + `topic.html` + `topic.png` | Ch 10, sometimes others |

Detection code:

```python
def collect_medsea_topics(ch_dir):
    """Return set of slug strings, handling both layouts."""
    slugs = set()
    diseases = Path(ch_dir) / "diseases"
    for entry in diseases.iterdir():
        if entry.is_dir():
            m = re.match(r'^\d+\.\d+\.\d+-(.+)$', entry.name)
            if m: slugs.add(slugify(m.group(1)))
        elif entry.suffix == ".md":
            m = re.match(r'^(\d+\.\d+)\.(\d+)-(.+)$', entry.stem)
            if m:
                rest = m.group(3).replace("-full", "").replace("-hub", "")
                slugs.add(slugify(rest))
    return slugs
```

**Bug I hit:** first script only handled flat layout and reported Ch 10 as "0 MedSea topics" — the directory layout was invisible to it. Always detect both.

## 2. `manifest.json` schema varies by chapter

Same data, two key conventions exist:

| Schema A (Ch 1–9, 11–18) | Schema B (Ch 10) |
|---|---|
| `total_hubs`, `total_topics`, `hubs[]` with `num`/`name`/`slug`/`n_topics` | `n_hubs`, `n_topics`, `hubs[]` with `num`/`name`/`n_topics` (no slug) |

Defensive reader:

```python
m = json.loads(manifest_path.read_text())
total_hubs = m.get("total_hubs") or m.get("n_hubs", 0)
total_topics = m.get("total_topics") or m.get("n_topics", 0)
# Recompute from filesystem, don't trust these
actual_rendered = len(list((Path(ch_dir) / "diseases").glob("*.md"))) + \
                  sum(1 for p in (Path(ch_dir) / "diseases").iterdir()
                      if p.is_dir() and (p / "topic.md").exists())
```

## 3. Source `_full.md` and `_Hub.md` suffixes

Source uses `TopicName_full.md` for disease files and `Section_Hub.md` for hub stubs.
MedSea renames these. When comparing:

```python
def source_topic_slugs(src_dir):
    out = set()
    for md in Path(src_dir).rglob("*.md"):
        name = md.name
        if any(x in name for x in ["MOC.md", "Hierarchy.md", "Roadmap.md", "Template.md"]):
            continue
        # Strip suffixes
        clean = name.replace("_full.md", ".md").replace("_Hub.md", ".md").replace(".md", "")
        out.add(slugify(clean))
    return out
```

`_Hub.md` files are topic-group scaffolds, NOT separate topics. Don't double-count them.

## 4. Slug normalization: `&` and other punctuation

`&` in source title (e.g., `"N&V"`) can produce different slugs depending on the regex:

| Replacement | Output for "N&V" |
|---|---|
| `re.sub(r'[^\w\s-]', '', s)` (strip) | `"nv"` |
| `re.sub(r'[^\w\s-]', ' ', s)` (space) | `"n v"` → after `[\s_]+→-` → `"n-v"` |

**MedSea filenames use `"nv"` (no hyphen).** Pick the regex that matches MedSea:

```python
def slugify(text):
    s = text.lower()
    s = re.sub(r'[^\w\s-]', '', s)        # strip punctuation (matches MedSea)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')
```

Apply the SAME slugify to source AND MedSea AND Notion before comparing. Otherwise
~10–20% false negatives.

## 5. Notion title format = spaces + TitleCase

Notion displays `"Alfentanil Full"`. MedSea files are `"9.3.01-alfentanil-full.md"`.

```python
def notion_title_to_slug(title):
    s = title.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

def get_chapter_notion_slugs(ch_id):
    slugs = set()
    def walk(parent_id):
        cursor = None
        while True:
            url = f"https://api.notion.com/v1/blocks/{parent_id}/children"
            if cursor: url += f"?start_cursor={cursor}"
            res = http_get(url)
            for b in res.get("results", []):
                if b.get("type") == "child_page":
                    title = b["child_page"]["title"]
                    slugs.add(notion_title_to_slug(title))
                    # Recurse into hub pages (start with "N.M ")
                    if re.match(r'^\d+\.\d+\s', title):
                        walk(b["id"])
            if not res.get("has_more"): break
            cursor = res.get("next_cursor")
    walk(ch_id)
    return slugs
```

## 6. Notion child-page hierarchy: DB → chapter → hub → topic

When pushing topics to Notion, the parent is the **chapter page**, not the database.

```
MedSea DB 3805588e-846f-808b-a23b-cf63c89f372e
└── [child_page] "Chapter 9: Palliative and supportive care"  ← chapter root (in DB)
    └── [child_page] "9.7 Opioid Management"  ← hub page
        └── [child_page] "Equianalgesic Dose Conversion Full"  ← topic page
        └── [child_page] "Opioid Rotation Equianalgesia Full"
        └── ...
```

Topic upload payload:

```python
payload = {
    "parent": {"type": "page_id", "page_id": <chapter_page_id>},  # NOT database_id
    "properties": {"title": [{"type": "text", "text": {"content": topic_title}}]},
    "markdown": topic_md_body  # Notion auto-converts to blocks
}
res = http("POST", "https://api.notion.com/v1/pages",
           headers={"Notion-Version": "2025-09-03", ...})
```

**Why `2025-09-03` here but `2022-06-28` for chapter-DB pages:** DB row creation against the
old `2022-06-28` semantics is what the database was built on. New child-page creation
against an existing page works on `2025-09-03`. If a future API version breaks, the
3-way audit will surface the gap — keep it idempotent.

## 7. `blocks/{id}/children` pagination uses query string

```python
# WRONG — 400 validation_error: "body.page_size should be not present"
body = {"page_size": 100, "start_cursor": cursor}
res = http("POST", url, data=body)

# CORRECT — pagination in URL
url = f"https://api.notion.com/v1/blocks/{page_id}/children"
if cursor: url += f"?start_cursor={cursor}"
res = http("GET", url)
```

The endpoint is documented as `GET /v1/blocks/{block_id}/children` and accepts `start_cursor` /
`page_size` as **query parameters**, not request body fields.

## 8. Manifest declared topics vs actually rendered

When MedSea scaffolds a hub, it writes `manifest.json` with the planned topic count
but only generates MDs for the rendered subset. Trust the filesystem, not the manifest:

```python
def count_rendered_topics(ch_dir):
    diseases = Path(ch_dir) / "diseases"
    flat = sum(1 for f in diseases.glob("*.md"))
    in_dirs = sum(1 for d in diseases.iterdir()
                  if d.is_dir() and (d / "topic.md").exists())
    return flat + in_dirs
```

For Ch 9 (2026-06-20): manifest said `total_topics: 75`, actually rendered was 51.
The gap was hubs 9.7 (6), 9.8 (17), 9.9 (1 of 8) — all scaffolded but never written.

## 9. Quick 3-way diff recipe

```python
src = source_topic_slugs("/mnt/tb/Medicine/<Chapter>")
medsea = collect_medsea_topics("/mnt/tb/Sea-knowledge/#MedSea/chapters/<slug>")
notion = get_chapter_notion_slugs(<chapter_page_id>)

src_only = src - medsea - notion         # in source, missing everywhere
medsea_only = medsea - src - notion      # in MedSea, missing from Notion
notion_only = notion - src - medsea      # in Notion, missing locally (rare)
```

Report all three sets. The user may decide some "missing" items are intentionally
out of scope (renames, deprecated topics).

## 10. Hub-overview files at chapter root (NOT real topics)

Source chapters often have umbrella MD files at the top level of the chapter
folder that are **hub overviews**, not standalone topics:

```
/mnt/tb/Medicine/Endocrinology/
├── Adrenal Disorders.md          ← HUB OVERVIEW, not a topic
├── Adrenal Crisis.md             ← real topic
├── Endocrine Emergencies.md      ← HUB OVERVIEW
├── Thyroid Disorders.md          ← HUB OVERVIEW
└── ...specific disorder MDs...
```

These show up as "missing" in naive 3-way audits but should NOT be added as
topics — MedSea implements them as **hub pages** with the specific disorders
as topic children:

```
Endocrinology
├── 20.4 Adrenal Disorders (hub page) ←─ represents Adrenal Disorders.md
│   ├── 20.4.01 Adrenal Crisis       ←─ represents Adrenal Crisis.md
│   ├── 20.4.02 Adrenal Cushing      ←─ ...
│   └── ...specific disorder topics
├── 20.3 Thyroid Disorders (hub page)
│   └── 20.3.x individual topics
```

**Detection rule** for source files (use BOTH heuristics):

```python
def is_hub_overview_md(name, full_path, chapter_dir):
    """A hub-overview MD is at the chapter root level OR has _Hub/_HUB suffix."""
    fl = name.lower()
    if any(s in fl for s in ["_hub", "_hub.md"]):
        return True
    # Root-level MD = parent directory equals chapter_dir
    if os.path.dirname(full_path) == chapter_dir:
        return True
    return False
```

**Detection rule** for MedSea — read the existing hub structure from
`manifest.json` first. If MedSea already has a hub named e.g. "Adrenal
Disorders" (hub 20.4), the source file `Adrenal Disorders.md` IS represented
and is NOT a missing topic.

Validated 2026-06-20 on Ch 16-20 audit: this filter reduced false-positive
"missing" reports from ~84 to ~7 across Ch 17-20.

## 11. Title-based fuzzy matching (when slugs diverge)

After slug-based matching, some source topics will still appear "missing"
because MedSea renamed or split them. Example:

| Source | MedSea | Slug match? |
|---|---|---|
| `Acid-Base Disorders.md` (overview) | 5 separate topics | NO (slug mismatch) |
| `Urinalysis Interpretation.md` | `Urine Investigations.md` | NO |
| `GFR Estimation and Measurement.md` | `Glomerular Filtration Rate.md` | NO |

To detect these as "effectively covered", use title-based fuzzy matching:

```python
def normalize_words(text):
    """Bag of significant words (4+ chars)."""
    return set(w for w in re.sub(r'[^a-z0-9\s]', ' ', text.lower()).split()
               if len(w) >= 4)

def title_fuzzy_match(src_title, med_titles_dict, threshold=0.6):
    """Find best MedSea topic for src_title using Jaccard + overlap coefficient."""
    src_w = normalize_words(src_title)
    if not src_w:
        return None, 0.0
    best_slug, best_score = None, 0.0
    for med_slug, med_title in med_titles_dict.items():
        med_w = normalize_words(med_title)
        if not med_w:
            continue
        inter = len(src_w & med_w)
        union = len(src_w | med_w) or 1
        jaccard = inter / union
        overlap = inter / min(len(src_w), len(med_w))
        score = max(jaccard, overlap)
        if score > best_score:
            best_score, best_slug = score, med_slug
    return (best_slug, best_score) if best_score >= threshold else (None, best_score)
```

**Threshold guidance** (validated 2026-06-20 on Ch 16-20):

| Threshold | Use case |
|---|---|
| ≥ 0.7 | Strict — only near-exact title overlaps count |
| **0.55–0.60** | Default — catches renames and splits |
| < 0.5 | False positives — usually hub overviews or partial matches |

**Important:** Apply the title-fuzzy match AFTER the slug match and AFTER
the hub-overview filter. If slug match returns a hit, don't even check
title. This prevents wasting effort on topics that are already matched.

## 12. Topic number selection when adding new topics

**Don't blindly use `n+1` of the last topic in one hub.** Two numbering
patterns exist across chapters:

| Pattern | Example | How to pick next number |
|---|---|---|
| **Global sequential** (Ch 11-16) | Ch 16 hub 16.6 ranges 16.6.310–16.6.355+ | Find MAX across ALL hubs in the chapter, then add to the target hub |
| **Per-hub reset** (Ch 17-20) | Ch 18 hub 18.1 starts at 18.1.1 | Find max WITHIN the target hub |

**Decision rule:**

```python
def next_topic_number(chapter_dir, target_hub_num):
    """Return next available <hub>.<N> number for new topics in target_hub."""
    diseases = Path(chapter_dir) / "diseases"
    nums_in_hub = []
    nums_all = []
    for entry in diseases.iterdir():
        m = re.match(r'^(\d+)\.(\d+)\.(\d+)-', entry.name)
        if m:
            hub = f"{m.group(1)}.{m.group(2)}"
            num = int(m.group(3))
            nums_all.append(num)
            if hub == target_hub_num:
                nums_in_hub.append(num)
    if nums_in_hub:
        # Per-hub reset pattern (Ch 17-20)
        return max(nums_in_hub) + 1
    if nums_all:
        # Global sequential pattern (Ch 11-16) — use global max
        return max(nums_all) + 1
    return 1
```

**Validation step before writing**: also grep for collisions:

```bash
ls chapters/<slug>/diseases/ | grep "^<hub_num>\.<candidate_num>-"
```

Empty output = safe to use. Otherwise rename the existing topic first.

Validated 2026-06-20: Ch 16 used `16.6.356-359` (global sequential),
Ch 18 used `18.1.7-8` (per-hub reset). Picking `16.6.1` for Ch 16 would
have collided with `16.6.1-*` in another hub context (the numbering
isn't actually per-hub in Ch 16).

## 13. Notion hub numbering may differ from MedSea hub_num

**Don't trust the skill's chapter→slug mapping table for hub numbers.**
Hub numbering can shift across editions (e.g., Ch 18 was Ch 15 in 24th Ed):

| Source / MedSea hub_num | Notion hub title (live, 2026-06-20) |
|---|---|
| 18.1 (Renal Anatomy, Physiology, Investigations) | **15.1** (legacy 24th-Ed numbering) |
| 16.6 (Cardiac Emergencies) | 16.6 (matches) |

**Always query Notion for the actual hub title before pushing topics:**

```python
def find_hub_by_num_or_name(parent_id, hub_num, hub_name_guess=""):
    """Match hub page by hub_num prefix OR hub_name substring."""
    children = get_children(parent_id)
    for c in children:
        if c.get("type") != "child_page":
            continue
        title = c["child_page"]["title"]
        # Match either by hub number (e.g. "15.1" or "16.6") in leading position,
        # OR by hub name substring (case-insensitive)
        if re.match(rf'^{re.escape(hub_num)}\b', title):
            return c["id"], title
        if hub_name_guess and hub_name_guess.lower() in title.lower():
            return c["id"], title
    return None, None
```

**Never hardcode hub IDs in topic push scripts.** The MedSea local manifest
hub numbers and the Notion hub titles can drift independently over time.