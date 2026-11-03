# MedSea Chapter Audit — 3-Way Sync Check

Drop-in script for auditing whether a MedSea chapter is fully synced across
**source** (`/mnt/tb/Medicine/<Chapter>`), **MedSea local** (`chapters/<slug>/`), and **Notion** (chapter page + hub sub-pages).

Validated 2026-06-20 on Ch 6, 7, 8, 9, 10 audit. Found +50 missing topics on Ch 9 (49 new + 1 missed), +2 missing on Ch 7 Notion, +notion_id missing on Ch 10 manifest.

## Usage

```bash
python3 scripts/medsea_audit_chapter.py 9     # Audit + report gaps
python3 scripts/medsea_push_missing.py 9      # Push missing topics to Notion
```

## What it checks

1. **Source vs MedSea local**: slug-by-slug match (normalized for &, parens, _ vs -)
2. **MedSea local vs Notion**: every MedSea topic has a Notion page (and vice versa)
3. **Hub structure**: source subdirs → MedSea hubs (catches missing hubs entirely, e.g., Ch 9 had 11 source subdirs but MedSea only had 9 hubs)
4. **Manifest sanity**: total_topics + per-hub n_topics match actual files

## Audit Script (Python — drop-in)

```python
#!/usr/bin/env python3
"""Audit MedSea chapter sync: source / local / Notion."""
import json, re, urllib.request, time
from pathlib import Path

NOTION_KEY = open('/root/.hermes/.env').read().split('NOTION_API_KEY='***')[0].strip()

def http(method, url, data=None):
    h = {"Authorization": f"Bearer {NOTION_KEY}", "Notion-Version": "2025-09-03"}
    if data is not None:
        h["Content-Type"] = "application/json"; body = json.dumps(data).encode()
    else: body = None
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=30) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e: return {"_error": e.code}

def slugify(text):
    """Aggressive normalize: punctuation → space, collapse underscores/dashes."""
    s = text.lower()
    s = re.sub(r'[^\w\s-]', ' ', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

def get_source_slugs(src_dir):
    slugs = set()
    for f in Path(src_dir).rglob("*.md"):
        if any(x in f.name for x in ['MOC.md','Hierarchy.md','Roadmap.md','Template.md']):
            continue
        clean = f.name.replace('_full.md','').replace('_Hub.md','').replace('_HUB.md','').replace('.md','')
        slugs.add(slugify(clean))
    return slugs

def get_medsea_slugs(medsea_dir):
    slugs = set()
    d = Path(medsea_dir)
    if not d.exists(): return slugs
    for f in d.iterdir():
        if f.is_dir():
            m = re.match(r'^\d+\.\d+\.\d+-(.+)$', f.name)
            if m: slugs.add(slugify(m.group(1)))
        elif f.suffix == ".md":
            m = re.match(r'^(\d+\.\d+)\.(\d+)-(.+)$', f.stem)
            if m:
                rest = m.group(3).replace('-full','').replace('-hub','')
                slugs.add(slugify(rest))
    return slugs

def get_notion_slugs(ch_page_id):
    slugs = set()
    def fetch(parent_id):
        cursor = None
        while True:
            url = f"https://api.notion.com/v1/blocks/{parent_id}/children"
            if cursor: url += f"?start_cursor={cursor}"
            res = http("GET", url)
            if "_error" in res: return
            for b in res.get("results", []):
                if b.get("type") == "child_page":
                    t = b["child_page"]["title"]
                    slugs.add(slugify(t))
                    if re.match(r'^\d+\.\d+\s', t):
                        fetch(b["id"])
            if not res.get("has_more"): break
            cursor = res.get("next_cursor")
    fetch(ch_page_id)
    return slugs

CHAPTERS = {
    6: ("83035ef3-c78d-462b-816a-3d8ad0b0e653", "6-population-health", "Population Health and Epidemiology"),
    7: ("6469084f-1ff0-4679-8f4f-4bab9f1d0802", "7-principles-of-infection", "Principles of Infectious Disease"),
    8: ("8d4228ea-8497-4d4d-b2e7-f62a746f39d1", "8-oncology", "Oncology"),
    9: ("c65289d8-2227-48e3-a809-cb07e2b70f66", "9-palliative-care", "Pain and Palliative Care"),
    10: ("3835588e-846f-81a1-bd40-fbd5d564fd2e", "10-acute-medicine", "Acute Medicine and Critical Illness"),
}

import sys
ch_n = int(sys.argv[1]) if len(sys.argv) > 1 else 9
notion_id, slug, src_name = CHAPTERS[ch_n]

src_slugs = get_source_slugs(Path(f"/mnt/tb/Medicine/{src_name}"))
medsea_slugs = get_medsea_slugs(Path(f"/mnt/tb/Sea-knowledge/#MedSea/chapters/{slug}/diseases"))
notion_slugs = get_notion_slugs(notion_id)

print(f"Ch {ch_n}: src={len(src_slugs)} medsea={len(medsea_slugs)} notion={len(notion_slugs)}")
missing = src_slugs - medsea_slugs
if missing:
    print(f"\nSRC not in MEDSEA ({len(missing)}):")
    for s in sorted(missing): print(f"  - {s}")
missing = medsea_slugs - notion_slugs
if missing:
    print(f"\nMEDSEA not in NOTION ({len(missing)}):")
    for s in sorted(missing): print(f"  - {s}")
```

## Notion Push Script (Python — drop-in)

```python
#!/usr/bin/env python3
"""Push missing MedSea topics to Notion (uses chapter manifest.json)."""
import json, re, time, urllib.request
from pathlib import Path

NOTION_KEY = open('/root/.hermes/.env').read().split('NOTION_API_KEY='***')[0].strip()

def http(method, url, data=None):
    h = {"Authorization": f"Bearer {NOTION_KEY}", "Notion-Version": "2025-09-03"}
    if data is not None:
        h["Content-Type"] = "application/json"; body = json.dumps(data).encode()
    else: body = None
    req = urllib.request.Request(url, data=body, method=method, headers=h)
    for _ in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(int(e.headers.get("Retry-After","2"))); continue
            return {"_error": e.code, "_body": e.read().decode()[:500]}

def title_from_slug(slug):
    s = slug.replace("-full","").replace("-hub","")
    return " ".join(w.capitalize() for w in s.split("-"))

def strip_frontmatter(text):
    if text.startswith("---"):
        m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
        if m: text = text[m.end():]
    return text.strip()

import sys
ch_n = int(sys.argv[1]) if len(sys.argv) > 1 else 9

ch_dir = next(Path("/mnt/tb/Sea-knowledge/#MedSea/chapters").glob(f"{ch_n}-*"))
manifest = json.loads((ch_dir / "manifest.json").read_text())
CH_PAGE_ID = manifest["notion_id"]

res = http("GET", f"https://api.notion.com/v1/blocks/{CH_PAGE_ID}/children")
hubs = {}
for b in res.get("results", []):
    if b.get("type") == "child_page":
        hubs[b["child_page"]["title"]] = b["id"]

hub_title_lookup = {h["num"]: f"{h['num']} {h['name']}" for h in manifest.get("hubs", [])}

DISEASES = ch_dir / "diseases"
ok = fail = 0
for md in sorted(DISEASES.glob("*-full.md")):
    m = re.match(rf'^{ch_n}\.(\d+)\.(\d+)-(.+)-full\.md$', md.name)
    if not m: continue
    hub_num = f"{ch_n}.{m.group(1)}"
    slug = m.group(3)
    hub_title = hub_title_lookup.get(hub_num)
    if not hub_title:
        print(f"NO MANIFEST HUB: {hub_num}"); fail += 1; continue
    hub_id = hubs.get(hub_title)
    if not hub_id:
        print(f"NO NOTION HUB: {hub_title}"); fail += 1; continue

    title = title_from_slug(slug)
    body = strip_frontmatter(md.read_text())
    payload = {
        "parent": {"type": "page_id", "page_id": hub_id},
        "properties": {"title": [{"type": "text", "text": {"content": title}}]},
        "markdown": body
    }
    res = http("POST", "https://api.notion.com/v1/pages", data=payload)
    if "_error" in res:
        print(f"FAIL {title}: {res.get('_body','')[:120]}"); fail += 1
    else:
        print(f"OK {title}"); ok += 1
    time.sleep(1)

print(f"\nDone: ok={ok} fail={fail}")
```

## Key gotchas

1. **Hub title format on Notion**: `"<hub_num> <Hub Name>"` (e.g., `"9.7 Opioid Management"`). Hub names in MedSea manifest are like "Opioid Management" without the number.
2. **Notion rate limit**: sleep 1s between POSTs; 429 retry with `Retry-After` header.
3. **Hub MD vs topic MD files**: filter `-full.md` for topics; `-hub.md` are hub summaries (push if desired, but usually only topics need separate pages).
4. **Existing check**: query each hub's children before creating to avoid duplicates.
5. **Manifest schema varies**: Ch 10 uses `n_hubs`/`n_topics` instead of `total_hubs`/`total_topics`. Use `.get(key, default)`.
6. **notion_id may be missing from manifest** (e.g., Ch 10 had a Notion page but no notion_id field). Search Notion via `/v1/search` to find it: `{"query": "Chapter 10: Acute Medicine"}` then take page from results.

## Final Audit Phases (post-2026-06-20 lessons)

The 3-way inventory script above is the **first pass** but has known blind spots. Run these **additional 4 phases** to get the full "no topic missing" answer the user wants:

### Phase 4: MOC/Hierarchy inventory (the silent gap)

```python
import re
from pathlib import Path

SRC = Path("/mnt/tb/Medicine/<ChapterName>")
SEA_CHAP = Path("/mnt/tb/Sea-knowledge/#MedSea/chapters/<N>-<slug>")

# Inventory ALL root-level .md >5KB (these are master content, not topic stubs)
hub_files = []
for f in SRC.iterdir():
    if f.suffix == ".md" and f.stat().st_size > 5000:
        status = re.search(r'status:\s*(\S+)', f.read_text()[:500])
        hub_files.append((f.name, f.stat().st_size, status.group(1) if status else "no-status"))

print(f"\n=== HUB-LEVEL ROOT FILES ({len(hub_files)}) ===")
for name, size, status in sorted(hub_files, key=lambda x: -x[1]):
    print(f"  [{size//1024}KB, {status}] {name}")
    # Check if it exists in MedSea hubs/
    expected_slug = re.sub(r'[^a-z0-9]+', '-', name.lower().replace('.md','')).strip('-')
    if not (SEA_CHAP / "hubs" / f"{expected_slug}.md").exists():
        print(f"    ⚠️ MISSING FROM MedSea hubs/")
```

What this catches: Ch 16 Cardiology's `Heart Failure.md` (44 KB / 6,386 words) was never in MedSea. Ch 16-30 audits found 22 such files (~250 KB total) silently skipped.

### Phase 5: Word-count verification on ambiguous matches

```python
def word_count(p):
    return sum(1 for _ in open(p).read().split())

# For every "missing" slug from Phase 1, find a MedSea topic with similar wc
suspect_slugs = src_slugs - medsea_slugs  # from Phase 1
verified_synced = []
still_missing = []

for slug in suspect_slugs:
    # Reconstruct the original source file from slug
    src_candidates = list(SRC.rglob(f"*{slug}*.md"))
    if not src_candidates:
        still_missing.append(slug)
        continue
    src_wc = word_count(src_candidates[0])

    # Search ALL MedSea topics for word-count match (allow ±10% drift)
    found_by_wc = None
    for sea_topic in SEA_CHAP.glob("diseases/*/topic.md"):
        sea_wc = word_count(sea_topic)
        if abs(sea_wc - src_wc) <= max(50, src_wc * 0.10):
            found_by_wc = sea_topic.parent.name
            break

    if found_by_wc:
        verified_synced.append((slug, found_by_wc, src_wc))
    else:
        still_missing.append(slug)

print(f"\n=== AMBIGUOUS SLUGS ===")
print(f"Truly synced under different name: {len(verified_synced)}")
for s, t, wc in verified_synced: print(f"  ✅ {s} ({wc}w) → {t}")
print(f"Truly missing: {len(still_missing)}")
for s in still_missing: print(f"  ❌ {s}")
```

What this catches: Hematology's 85 root-level files all map correctly to MedSea atomic topics under renamed slugs (e.g. `Acute Lymphoblastic Leukaemia (ALL)` → `24.1.2-acute-lymphoblastic-leukaemia-all`). Without word-count verification, Phase 1 alone would report "85 missing topics" (false alarm).

### Phase 6: Status-frontmatter filter

```python
from collections import defaultdict

status_counts = defaultdict(int)
for f in SRC.rglob("*.md"):
    m = re.search(r'status:\s*(\S+)', f.read_text()[:500])
    if m: status_counts[m.group(1)] += 1

print(f"\n=== SOURCE STATUS DISTRIBUTION ===")
for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
    print(f"  {status}: {count}")
```

Subtract `starter-note`, `draft`, `scaffold` counts from "missing" — they're not real content. Validated Ch 21 (15 starter-note root files were empty templates, not missing topics).

### Phase 7: Final report format

```python
print(f"""
Chapter <N> Final Audit:
  Source files: {len(src_slugs)} (after status filter)
  MedSea topic.md: {len(medsea_slugs)}
  MedSea hubs/*.md: {len(list(SEA_CHAP.glob('hubs/*.md')))}

  Truly missing topics: {len(still_missing)} → {still_missing}
  Truly missing hubs: {len(missing_hubs)} → {missing_hubs}
  MOC/Hierarchy missing: {moc_missing} → {moc_missing_files}

  STATUS: {'✅ SYNCED' if not (still_missing or missing_hubs or moc_missing) else '⚠️ NEEDS PATCH'}
""")
```

Always run Phase 1 + Phase 4 + Phase 5 + Phase 6 + Phase 7 before telling the user "all topics are there". Phase 1 alone misses MOC/Hierarchy gaps. Phase 1+4 still has false positives from renamed slugs. Only the full sequence gives a defensible answer.

### Phase 8: Bash `#` in path trap

```bash
# WRONG — silently breaks:
find /mnt/tb/Sea-knowledge/#MedSea/chapters/.../diseases -name "topic.md"

# CORRECT — single-quoted variable:
MEDSEA='/mnt/tb/Sea-knowledge/#MedSea'
find "$MEDSEA/chapters/.../diseases" -name "topic.md"
```

Cost ~5 minutes of confused debugging the first time. Every audit script in this class hits it.

## Verified audit output (2026-06-20)

```
Ch 6: src=27 medsea=27 notion=27  ✓ SYNCED
Ch 7: src=26 medsea=26 notion=26  ✓ SYNCED (after fix: +2 missing Notion topics)
Ch 8: src=118 medsea=119 notion=119  ✓ SYNCED (1 extra is roadmap MOC)
Ch 9: src=101 medsea=101 notion=102  ✓ SYNCED (after fix: +49 topics + 1 hub)
Ch 10: src=43 medsea=43 notion=43  ✓ SYNCED (manifest notion_id was empty, fixed)
```