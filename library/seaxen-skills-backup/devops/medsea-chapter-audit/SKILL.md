---
name: medsea-chapter-audit
description: Use when verifying whether a MedSea chapter (Davidson 24/25th ed medicine notes) is 100% complete across local files, Docker website, GitHub repo, and Notion database. Performs intelligent basename normalization to handle MedSea's prefix-renaming convention (`X.Y.Z-slug` vs source's `X.Y Name.md`) and identifies real vs false-positive gaps.
---

# MedSea Chapter Completeness Audit

## Trigger
- User asks "is chapter N 100% complete?" or "check ch X-Y across local/website/git/notion"
- After a sync session, user wants verification before declaring done
- Periodic audit of MedSea state across all 4 sync targets

## User preference — never claim complete without sampling content

**HARD RULE (learned from user pushback "did you check files or just say blindly?")**: A "100% complete" claim based only on file count + topic-name match is NOT acceptable. The user expects sampled content verification before any completion report.

Minimum sampling before declaring a chapter complete:
1. Read **at least 2 atomic topics per chapter** (head + middle sections) and confirm:
   - File size > 5 KB (real content, not stub)
   - Has Learning Objectives / Mermaid / FCPS table / Viva Q&A structure
   - Word count > 800/topic
2. Verify MOC + Hierarchy overviews are NOT just stubs:
   - MOC > 1 KB with section checklist / cross-links
   - Hierarchy > 1 KB with topic tree / roadmap
3. State **what was sampled**, not "I checked".

If only file counts match but you haven't read content, say: "atomic count matches, content depth unverified — sampled N/M topics".

## What "100% complete" means
For each MedSea chapter, check **four targets** have the same content:

| Target | What to check |
|--------|---------------|
| **Local** MedSea | `/mnt/tb/Sea-knowledge/#MedSea/chapters/{N}-{slug}/diseases/` has atomic topics in **any of 3 formats** (flat `.md`, `topic.md` folder, `{slug}.md` folder) — plus `X.0.900-moc/` + `X.0.901-hierarchy/` overviews (or `-chapter-moc`/`-chapter-hierarchy` for ch 16) |
| **Website** | `http://localhost:8855/{N}-{slug}/` returns HTTP 200, meta shows `X hubs · Y topics` |
| **GitHub** | `git log origin/main` shows the commit hash containing chapter files |
| **Notion** | Notion DB `3805588e846f808ba23bcf63c89f372e` has a row titled "Chapter {N}: ..." with sub-pages for each topic |

## Pitfalls (learned the hard way)
1. **Slug normalization is hard.** MedSea uses `X.Y.Z-slug` while source uses `X.Y Name.md`. My first 5 matching scripts all failed because:
   - Source: `2.10.06 CYP inhibition induction` (space, no leading zero)
   - MedSea: `2.10.06-cyp-inhibition-induction.md` (dashes, lowercase)
   - Plus MedSea sometimes appends `-full` or `-hub` suffixes
   - And source uses `&`, `(`, `)`, `,`, `_` characters MedSea strips

2. **CORRECT matching algorithm:**
   ```python
   def norm(s):
       s = s.lower()
       s = re.sub(r'[^\w\s-]', ' ', s)
       s = re.sub(r'[\s_-]+', '-', s).strip('-')
       return s
   def topic_name_only(s):
       """Strip all leading numeric dash-segments AND '_full'/'-full' suffixes"""
       parts = norm(s).split('-')
       out = [p for p in parts if not p.isdigit() and p not in ('full',)]
       return '-'.join(out)
   ```
   Then compare `topic_name_only(src)` against `topic_name_only(medsea)` sets.

3. **CRITICAL trap: MedSea often has FINER atomic granularity than source.** The MedSea `topic_name_only` matching is correct only when both sides describe the SAME topic. But MedSea may have split a source topic into 3-5 sub-topics:
   - Source: `Hypertension and Cardiovascular Risk States` (single overview topic)
   - MedSea: `resistant-hypertension-spironolactone-renal-denervation`, `hypertensive-emergencies-urgencies`, `coarctation-of-aorta-repair-recoarctation-hypertension` (3 specific subtopics)
   The naive match shows this as "missing" but it's actually **covered** — just with finer granularity. **Reverse the comparison**: for every source topic, check if at least one MedSea topic shares ≥2 significant keywords.

   ```python
   def keywords_match(src_name, medsea_names):
       src_kw = set(w for w in norm(src_name).split('-') if len(w) > 3 and w not in ('full','hub','overview','chapter','davidson'))
       for m in medsea_names:
           m_kw = set(w for w in norm(m).split('-') if len(w) > 3)
           if len(src_kw & m_kw) >= 2:
               return True
       return False
   ```
   Source count 842 vs MedSea 907 for ch 16 = "MedSea has MORE" not "less".

3. **Chapters use THREE formats** (not two):
   - **Format A**: flat `.md` + `.png` in `diseases/` directly (older, ch 1-9, 17-20)
   - **Format B**: `diseases/X.Y.Z-slug/topic.md` + `topic.png` (newer, ch 10-16, 21-32)
   - **Format C**: `diseases/X.Y.Z-slug/{slug}.md` + `{slug}.png` (ch 18 nephrology — folder exists but the `.md` inside is named after the slug, not `topic.md`)
   `build_site.py` handles all three. The audit count must check ALL THREE:
   ```python
   def count_atomic(ch_dir):
       n = 0
       for entry in os.listdir(ch_dir):
           full = os.path.join(ch_dir, entry)
           if os.path.isdir(full):
               if os.path.exists(os.path.join(full, 'topic.md')):  # Format B
                   n += 1
               elif any(f.endswith('.md') and f != 'topic.md' for f in os.listdir(full)):  # Format C
                   n += 1
           elif entry.endswith('.md') and not entry.startswith('.'):  # Format A
               n += 1
       return n
   ```
   My `find -name "topic.md"` missed **49 ch 18 topics** because they're Format C.

4. **MOC/Hierarchy folder naming has TWO variants**:
   - New (ch 1-15): `X.0.900-moc/`, `X.0.901-hierarchy/`
   - Old (ch 16): `X.0.900-chapter-moc/`, `X.0.901-chapter-hierarchy/`
   - Special: `X.0.902-<special-name>/` for integrated topics (Heart Failure, Palliative Care)
   Always check **both variants** when looking for overview folders.

5. **Notion DB root is a database, not a page** (`3805588e846f808ba23bcf63c89f372e`). Use `/databases/{id}/query` with `filter.property.title.starts_with = "Chapter N:"` to find chapter rows. Don't use `/pages/{id}`.

6. **MOC + Hierarchy overview pages are a separate completeness axis** — atomic topics may be 100% but MOC/Hier might be missing for the entire chapter. Always check these independently.

7. **Source for ch 11 (Poisoning) and ch 13 (Austere Medicine) Hierarchy files are in DIFFERENT folders**: `/mnt/tb/Medicine/Chapter 7 - Poisoning/Davidson Chapter 7 - Poisoning Hierarchy.md` and `/mnt/tb/Medicine/Environmental medicine/Davidson Chapter 9 - Environmental Medicine Hierarchy.md`. Don't assume same-parent folder for Hierarchy files.

7. **Git push is slow** — site folder is 1.1 GB. Set `git config http.postBuffer 524288000` and use `nohup ... &` with `tee` to a log file. Real pushes take 5-10 minutes. Don't use foreground `git push` with timeout=60.

8. **Notion rate limit** is 3 req/sec. The error response includes `Retry-After: N` — respect it. First sync run can hit 429 hard if chapter search is involved.

9. **Two ch 12 pages exist in Notion** (HIV + Envenomation); same for ch 10 (Acute Medicine variants). Match by lowercase chapter slug — use the lowercase one for MedSea sync.

10. **"Missing" false positives** (the most common reason for an inflated missing-count report):
    - `Subdir/Subdir.md` files where the filename matches the parent directory name are **hub overviews**, not disease topics. Skip them: `if normalize(filename) == normalize(parent_dir): continue`.
    - `Chapter X Roadmap.md` and `Chapter X MOC.md` files with `status: draft` are **build tracking**, not content. Skip them.
    - Hub overview files in `/mnt/tb/Medicine/Ch X/Subdir/` ARE in MedSea, but in `chapters/{N}/hubs/` or `chapters/{N}/source/` — NOT in `diseases/`. Always check all three locations before declaring anything missing.

11. **Git working-dir drift can produce "all chapters complete" false positives** — the website rebuild can silently overwrite source `.md` files with rendered "infographic" versions, losing 50%+ of content (Ch 16 went from 204 lines to 95 lines). Before any "100% complete" claim, run `git status -s chapters/{N}/` and for each `M ` line, compare HEAD vs working dir char count. If HEAD > 2× working dir, that's drift — revert: `git checkout HEAD -- chapters/{N}/` (use Python for unicode filenames like `≤ ≥ → ü`; bash xargs sends literal `\u2265` text).

12. **Notion root page IDs Ch 21-32** are stored in `medsea-multi-platform-sync/references/notion-root-ids.md`. To verify or extract them, read `site/{N}-{slug}/topics.json` and parse the `notion_url` field (the last 32 hex chars are the page ID). No API call needed.

13. **Ch 22, 23 use mixed file structures** within the same chapter — some topics are Format A (flat `.md` in `diseases/`), some are Format B (`diseases/{slug}/topic.md`). The audit count must include both — `find -name "topic.md"` alone misses Format A, `ls *.md` alone misses Format B.

14. **Topic count discrepancies between source and MedSea are normal** when MedSea splits source topics into more granular sub-topics (e.g. Ch 23 Hepatology: 117 source files → 349 MedSea topics). Reverse-check: for each source topic, find at least one MedSea topic sharing ≥2 significant keywords. If 0 unmapped source topics → "100% complete" even with count mismatch.

## Audit script (the working version)
```python
import os, re
MEDSEA = '/mnt/tb/Sea-knowledge/#MedSea'
MED = '/mnt/tb/Medicine'

def norm(s):
    s = s.lower()
    s = re.sub(r'[^\w\s-]', ' ', s)
    s = re.sub(r'[\s_-]+', '-', s).strip('-')
    return s

def topic_name_only(s):
    parts = norm(s).split('-')
    return '-'.join(p for p in parts if not p.isdigit() and p not in ('full',))

# Per chapter: medsea_set = {topic_name_only(name) for name in all .md/topic.md}
#               src_set    = {topic_name_only(name) for name in source/*.md}
# Real missing = src_set - medsea_set
# (after filtering MOC/Hierarchy/Topic Template/index/config from source)
```

## Support files
- `references/medsea-product-sector-ratings.md` — Full product audit: sector scores /10, missing features backlog, tar deploy checklist, two-pipeline (HTML vs JSON) honesty.
- **Topic exam load perf:** `static-site-performance-optimization` → `references/topic-scoped-exam-flash-load.md` (not chapter completeness — exam UX when `?topic=` is slow).
- `references/notion-chapter-discovery.md` — How to find chapter page IDs in the MedSea Notion database (the root is a database, not a page), and the working code for finding chapter rows, creating overview pages, and pre-fetching duplicates to skip.
- `scripts/audit_medsea.py` — Runnable audit script. Counts atomic topics across all 3 MedSea formats, sums word counts, checks both MOC/Hier naming variants, and reports the git commit covering each chapter. Exits non-zero if any chapter is missing MOC or Hier.

## Report format
Always report:
- Atomic topic count per target (local / website / git / Notion)
- MOC + Hierarchy overview presence (yes/no per chapter) — for BOTH naming variants
- Real gaps (not false positives)
- Per-target verification result with concrete evidence (file paths, HTTP status, commit SHA, Notion page IDs)
- What you actually sampled and read, not "I checked"

## SBA answer-quality audit (separate from completeness)

For the `/exam/` question bank, completeness is one axis. Answer/distractor quality is a separate, often-invisible failure mode. Audit it independently:

**Full product audit (all apps, /10 sectors, missing features):** see `references/medsea-product-sector-ratings.md` — run when user asks for final rating, 10/10 push, or gap list beyond a single chapter. Distinguish **product UX (~9/10)** from **teaching rationales (~7/10)** via `index.quality`.

**Three real failure modes the count-only check hides:**

1. **Placeholder distractor text** — autogen writes `"A related condition in the same clinical area"` / `"A common mimicker with overlapping features"` as wrong-answer options. The audit must check option text against a regex like `(A related condition|A closely related|A complication|A common mimicker|An unrelated (?:mimic|condition)|A different but related trial|A guideline \(not a trial\)|An observational/cohort study|A complication rather than|A related but distinct clinical entity|A closely related condition in the same clinical area|A complication of [A-Z])`. With my fix in `rebuild_question_bank_v5.py:upgrade_pastest_distractors()` + curated `DISTRACTOR_POOLS` per chapter in `autogen_scenario_sbas.py`, target is 0/12,774 placeholder slots.

2. **Same-3-distractor repetition across an entire chapter** — the worst case: 598/639 Ch 16 items all have `Constrictive pericarditis / Tension pneumothorax / Pulmonary embolism` because the autogen picked `pool[0:3]` for every item. Audit: `Counter(tuple(sorted(distractor_set)) for item in chapter)` — flag any chapter where the most common distractor set covers > 30% of items. Fix is in `rotate_distractors_through_pool()`: per-item deterministic hash-based offset in the chapter pool, so each item gets a different 3-distractor window.

3. **Cross-topic distractor noise** — when the rotator uses a flat-merged chapter pool, an "Acute pancreatitis" item can end up with `Hemorrhoids / IBS / Ulcerative colitis` as distractors because those are in the GI chapter's default pool. Fix is `_resolve_distractor_pool()` in the rebuilder: try `topic_keyword(title)` first → fall back to `topic_keyword(question)` (when title is collapsed to "Topic") → fall back to merged pool. This means pancreatic items get pancreatic differential distractors (`Choledocholithiasis / Duodenal perforation / Biliary colic`), not colon differential.

**SBA audit script (working version):**
```python
import json, re
from collections import Counter
with open('site/assets/questions-sba.json') as f:
    data = json.load(f)

# 1. Placeholder distractor slots
PLACEHOLDER_RE = re.compile(
    r'^"(A related condition|A closely related condition|A complication|A common mimicker|'
    r'An unrelated (?:mimic|condition)|A different but related trial|A guideline \(not a trial\)|'
    r'An observational/cohort study|A complication rather than|An unrelated mimic|'
    r'A related but distinct clinical entity|A closely related condition in the same clinical area|'
    r'A complication of [A-Z])', re.IGNORECASE)
ph_count = sum(1 for it in data for v in it['options'].values() if PLACEHOLDER_RE.match(v))
print(f'Placeholder slots: {ph_count} / {len(data)*3}')

# 2. Per-chapter top-set share
for ch in sorted({it['chapter_num'] for it in data}):
    items = [it for it in data if it['chapter_num']==ch and it.get('source')=='pastest-autogen']
    if not items: continue
    sets = Counter(tuple(sorted([v for k,v in it['options'].items() if k != it['answer']])) for it in items)
    top, cnt = sets.most_common(1)[0]
    print(f'Ch {ch}: {len(sets)} distinct / {len(items)} items, top-set {100*cnt/len(items):.1f}%')
```

**Honest trade-off (not a bug):** topic-keyword-aware rotation gives *fewer* distinct sets than flat pool rotation (because sub-pools are smaller, e.g. 4-7 entries), but the distractors are clinically relevant. For MRCP exam quality, topic-relevance wins over distinct-set count.
