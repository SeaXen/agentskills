# Chapter-by-Chapter Audit Playbook (Ch 11-20 + future)

Validated 2026-06-20 across two full chapter-range syncs (Ch 11-15, Ch 16-20). This is the worked pattern — not theory.

## The 3-step audit loop

```python
# Step 1: enumerate SOURCE non-meta MDs
src_files = walk_with_filter(chapter_dir, exclude=['moc','hierarchy','template','_hub','roadmap'])

# Step 2: enumerate MEDSEA filesystem (detect subdir vs flat pattern)
def medsea_topics(d):
    topics = {}
    for item in os.listdir(d):
        path = os.path.join(d, item)
        if os.path.isfile(path) and item.endswith('.md'):
            topics[normalize(item)] = path         # FLAT
        elif os.path.isdir(path) and os.path.isfile(path + '/topic.md'):
            topics[normalize(item)] = path + '/topic.md'  # SUBDIR
    return topics

# Step 3: classify each source → MATCH / REAL-MISSING / HUB-OVERVIEW
def normalize(stem):
    base = re.sub(r'^\d+[\.\-_]+\s*', '', stem)
    base = re.sub(r'_full$|_hub$|_template$|_roadmap$', '', base, flags=re.IGNORECASE)
    base = base.replace('_', '-')
    return re.sub(r'[^a-z0-9]', '', base.lower())

def fuzzy_match(slug, candidates):
    if slug in candidates: return slug
    matches = [c for c in candidates if (len(slug)>=8 and slug in c) or (len(c)>=8 and c in slug)]
    return min(matches, key=lambda c: abs(len(c)-len(slug))) if matches else None
```

## Per-chapter storage pattern (must respect when ADDING topics)

| Ch | Storage | How to create new topic |
|---|---|---|
| 11, 12, 13, 14, 16, 17 | SUBDIR: `diseases/<prefix>-<slug>/topic.md` | `mkdir + write topic.md` |
| 18, 19, 20 | FLAT: `diseases/<prefix>-<slug>.md` | `write <prefix>-<slug>.md` directly |
| 16 (mixed) | mostly subdir | check surrounding siblings first |

If you put a flat-file topic into a subdir chapter, build_site.py silently skips it (topic doesn't appear on live site, doesn't break anything else but is invisible).

## Real-missing topic count (from 2026-06-20 audit)

| Ch | Source MDs | MedSea | REAL missing | Notes |
|---|---:|---:|---:|---|
| 11 Poisoning | 37 | 37 | **0** | FULL MATCH |
| 12 Envenomation | 13 | 13 | **0** | FULL MATCH |
| 13 Austere | 9 | 9 | **0** | FULL MATCH |
| 14 Infect Dis | 55 | 55→56 | **0** (1 added: PCP) | was missing Pneumocystis |
| 15 STIs | 26 | 26 | **0** | FULL MATCH (numbered + named coexist) |
| 16 Cardiology | 729 | 899→904 | **5** added | Vasovagal, Orthostatic, Cardiac, Risk strat, Ebstein |
| 17 Respiratory | 158 | 149 | **0** | source has 31 hub overviews not represented as topics |
| 18 Nephrology | 54 | 49→51 | **2** added | Urinalysis Interpretation, GFR Estimation |
| 19 Biochem | 33 | 28 | **0** | source has umbrella files split into sub-topics |
| 20 Endocrine | 97 | 87 | **0** | source has umbrella files split into sub-topics |

The "truly missing" pattern is always: clinical specific topic with full content (`status: full-fcps-mrcp-note` in YAML) that has no MedSea equivalent under any fuzzy-matched slug.

## Adding a missing topic — the canonical recipe

```python
import os, re, shutil

def add_topic(chapter_slug, local_prefix, slug, src_md_path, related=None):
    """Add a missing topic from Medicine source to MedSea chapters/."""
    with open(src_md_path) as f:
        md = f.read()
    # Strip YAML frontmatter
    if md.startswith('---\n'):
        end = md.find('\n---\n', 4)
        if end > 0: md = md[end + 5:]
    md = md.lstrip()
    # Strip emoji prefixes from headers (## 🎯 Foo → ## Foo)
    md = re.sub(r'^(##+ )[\U0001F300-\U0001FAFF\u2600-\u27BF]+\s*', r'\1', md, flags=re.MULTILINE)
    # Insert Related: line after first heading if not present
    if 'Related: [[' not in md[:300] and related:
        rel_line = "Related: " + ", ".join(f"[[{r}]]" for r in related) + "\n\n"
        lines = md.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('# '):
                lines.insert(i+2, rel_line.rstrip()); break
        md = '\n'.join(lines)

    # Detect chapter storage pattern
    d = f"/mnt/tb/Sea-knowledge/#MedSea/chapters/{chapter_slug}/diseases"
    siblings = os.listdir(d)
    uses_subdir = any(os.path.isdir(os.path.join(d, s)) and os.path.isfile(os.path.join(d, s, 'topic.md'))
                      for s in siblings if s.startswith(local_prefix[:5]))

    folder_name = f"{local_prefix}-{slug}"
    if uses_subdir:
        os.makedirs(f"{d}/{folder_name}", exist_ok=True)
        with open(f"{d}/{folder_name}/topic.md", 'w') as f: f.write(md)
    else:
        with open(f"{d}/{folder_name}.md", 'w') as f: f.write(md)
    return folder_name
```

## Pushing to Notion — find hub by walking chapter page

The chapter root page IDs are in `build_site.py`'s `BUILT_CHAPTERS`. Walk the chapter page's child_page blocks to find the hub for `hub_num`:

```python
def find_hub(parent_chapter_page_id, hub_num):
    children = notion_get(f"/blocks/{parent_chapter_page_id}/children?page_size=100")
    for c in children["results"]:
        if c.get("type") == "child_page":
            title = c["child_page"]["title"]
            # 25th Ed hub titles look like "16.6 Hub 6" or "16.6 Cardiac Emergencies"
            if title.startswith(f"{hub_num} ") or title.startswith(f"{hub_num}."):
                return c["id"]
    return None
```

Note: Ch 18 in MedSea uses **15.x** numbering (Davidson 24th Ed) — when adding topics to a hub for the new chapter naming scheme, search for both `18.1` AND `15.1` patterns. Notion title prefix matters; trust the live chapter page, not the local slug.

## Topic title prefix when uploading to Notion

```python
title = f"{local_prefix} {humanize(slug)}"  # e.g. "16.6.356 Vasovagal Syncope"
# Strip MD frontmatter for the upload
md = re.sub(r'\*\*Parent Topic:\*\*[^\n]*\n', '', md)
md = re.sub(r'\*\*Status:\*\*[^\n]*\n', '', md)
md = re.sub(r'\*\*Source:\*\*[^\n]*\n', '', md)
md = re.sub(r'\]\(\.\./[^)]*\)', ']', md)

notion_post("/pages", {
    "parent": {"page_id": hub_id},
    "properties": {"title": [{"text": {"content": title}}]},
    "markdown": md,
})
```

## Update manifest after adding

Patch only the relevant keys. Pattern (works for both schemas):
- `total_diseases` (or `n_topics`) += N
- Find the hub entry, update its `disease_count` (or `n_topics`) += N

Or simpler: re-run `python3 scripts/site/build_site.py` — it reads filesystem and writes the new manifest indirectly via `topics.json`. The build script doesn't update manifest.json automatically, so manual patch is still needed.

## Docker rebuild (3.4GB image, 5+ min)

Always use background + notify:

```bash
# /tmp/redeploy_medsea.sh
#!/bin/bash
set -e
cd /mnt/tb/Sea-knowledge/#MedSea
docker build --no-cache -t medsea-site:latest . >> /tmp/redeploy.log 2>&1
docker stop medsea >> /tmp/redeploy.log 2>&1 || true
docker rm medsea >> /tmp/redeploy.log 2>&1 || true
docker run -d --name medsea --restart unless-stopped -p 8855:80 medsea-site:latest >> /tmp/redeploy.log 2>&1
```

Invoke via `terminal(background=true, notify_on_complete=true)`. Wait for notification before verifying live.

## Word-to-word coverage reality check

When the user asks "is MedSea content same as source word-to-word":
- **Topics added via the recipe above** (e.g. the 7 added in Ch 16-20 audit): 100% word overlap. Source is copied verbatim except for frontmatter.
- **Pre-existing MedSea topics** (built before this session): NOT word-to-word. They went through the build pipeline which produced PNG infographics + condensed MD. Source has 10 MCQs + 10 SBAs + flashcards + spaced-rep tracker that the MedSea MD drops.

If user wants pre-existing topics word-to-word, you need to overwrite them via the recipe above. Confirm before doing this — it replaces the existing MedSea-rendered HTML and PNG with the source's MCQs/flashcards structure (no PNG infographic anymore).

## Verification at end of audit cycle

```bash
# 1. Manifest counts match filesystem
for ch in 16-cardiology 17-respiratory-medicine 18-nephrology-urology 19-clinical-biochemistry-and-metabolic-medi 20-endocrinology; do
  cnt=$(curl -s http://localhost:8855/$ch/topics.json | python3 -c "import json,sys; print(len(json.load(sys.stdin)['topics']))")
  echo "$ch: $cnt"
done

# 2. Each new topic has html content (not just stub)
curl -s http://localhost:8855/16-cardiology/topics.json | python3 -c "
import json, sys
d = json.load(sys.stdin)
for t in d['topics']:
    if t['local_prefix'] == '16.6.356':
        print(f'html length: {len(t.get(\"html\",\"\"))}')"

# 3. Git committed + pushed
cd /mnt/tb/Sea-knowledge/#MedSea && git log --oneline -1 && git status -s
```
