# MedSea Source-Sync Workflow — Reference & Examples

Session-validated patterns from Ch 1-15 and Ch 16-20 syncs (2026-06-20).

## The Three Layers of "100% Match"

The user's repeated corrections made one thing clear: there are THREE distinct
claims people call "100% match", and you must verify all three:

| Layer | Question it answers | Failure mode |
|---|---|---|
| **Topic presence** | "Does every source topic exist in MedSea?" | Reports `len(source) == len(medsea)` and claims done, but 30+ topics are duplicates/extra in MedSea |
| **Section presence** | "Does each topic file have all required `##` sections?" | Reports "100% topics present" but each is only 11 sections instead of 35 |
| **Content presence** | "Do the sections actually contain the items (10 MCQs, 10 SBAs)?" | Reports "100% have MCQ section" but `## MCQs (1)` has just one question |

**Always state which layer you're verifying.** If the user asks for "100% match" and you only verified one layer, the next prompt will be "you didn't add MCQs/SBAs/flashcards/tracker — fix it".

## Source Coverage Quirks (Verified)

| Chapter | MCQ% in source | SBA% in source | Flash% in source | Notes |
|---|---:|---:|---:|---|
| 1 Decision-Making | 100% | 100% | **0%** | Source has no Flashcards at all |
| 2 Therapeutics | 98% | 64% | 11% | Source has limited SBA/Flash |
| 3 Genetics | 100% | 100% | **0%** | Source has no Flashcards |
| 4 Immunology | 100% | 100% | **0%** | Source has no Flashcards |
| 5 Nutrition | 100% | 100% | 100% | Full template |
| 6 Population Health | 4% | 4% | 4% | Bare-bones source |
| 7 Infection Principles | 100% | 100% | 100% | Full template |
| 8 Oncology | 99% | 99% | 99% | Near full |
| 9 Palliative | 89% | 89% | 89% | Mostly full |
| 10 Acute Medicine | 100% | 100% | 100% | Full template |
| 11 Poisoning | 100% | 100% | 100% | Full template |
| 12 Envenomation | 100% | 100% | 31% | Limited Flash |
| 13 Austere | 11% | 11% | 0% | Mostly summaries |
| 14 Infectious | 56% | 56% | 56% | Many shorter topics |
| 15 STI | 100% | 100% | 19% | Limited Flash |
| 16 Cardiology | 96% (Viva) | 16% | 12% | **Uses VIVA not MCQ!** |
| 17 Respiratory | 74% | 74% | 74% | Mix |
| 18 Nephrology | 100% | 100% | 100% | Full |
| 19 Biochemistry | 82% | 82% | 82% | Mostly full |
| 20 Endocrinology | 89% | 89% | 89% | Mostly full |

**Key insight:** When source has 0% Flashcards (Ch 1, 3, 4, 13), MedSea also having
0% is CORRECT — it's source-aligned. Don't generate fake Flashcards. The user
accepted "100% match" for Ch 1-15 even when source was bare.

## The Slug Matching Bug (Recurring Failure)

```python
# BROKEN — naive basename match
src_basename = "5.1-5.4 Genetic Testing Technologies.md"
ms_basename = "3.5.01-genetic-testing-technologies.md"
# Returns False → reports 18 missing topics in Ch 3 (false positive)

# FIXED — strip leading numbers from BOTH sides
def src_slug(bn):
    bn = re.sub(r'^\d+(\.\d+)*[\.\s_-]*', '', bn).strip()  # strips "5.1-5.4 "
    return slugify(bn)

def ms_slug(bn):
    bn = re.sub(r'^\d+\.\d+\.\d+-', '', bn)  # strips "3.5.01-"
    return slugify(bn)
```

**Always test your slug function on at least 5 sample pairs before running on a whole chapter.** If even one mismatch is reported as "missing" when you can see the topic in both directories, the slug function is broken.

## Subdirectory vs Flat MedSea Layout

| Layout | Example path | Slug extraction |
|---|---|---|
| Flat | `chapters/3/diseases/3.5.01-genetic-testing.md` | basename minus `3.5.01-` |
| Nested | `chapters/14/diseases/14.1.46-toxoplasmosis/topic.md` | **parent dir name** minus `14.1.46-` |

The audit script handles both automatically by checking if `basename == 'topic.md'`.

## The "Viva Questions" Pattern in Ch 16

96% of Ch 16 Cardiology source files use `## VIVA QUESTIONS` (or numbered
`## 13. VIVA QUESTIONS`) instead of `## MCQs`. VIVA is the FCPS/MRCP equivalent
format — open-ended questions, no multiple-choice options.

When auditing MCQ coverage in Ch 16, use:

```python
mcq_or_viva = re.compile(r'^##[^#]*\b(?:MCQs?|Viva|VIVA)\b', re.IGNORECASE | re.MULTILINE)
```

Don't accept the user's "MCQs/SBAs/flashcards" as a literal — interpret it as
"exam questions / exam questions with options / exam cards". Viva counts as
exam questions. If you only match literal `MCQs`, you'll report Ch 16 as 64% MCQ
when it's actually 96% MCQ-or-Viva.

## Frontmatter Pattern (Avoid Double-Frontmatter)

When copying source content to MedSea, source files often have their own YAML
frontmatter. If you blindly prepend MedSea frontmatter, you get:

```
---
davidson_chapter: "Chapter 16: Cardiology"
... (MedSea frontmatter)
---

---
tags: [medicine, ...]
... (SOURCE frontmatter, now redundant)
```

**Always strip source frontmatter first:**

```python
def strip_existing_frontmatter(text):
    if text.startswith('---'):
        end = text.find('---', 3)
        if end != -1:
            return text[end+3:].lstrip('\n')
    return text
```

## Topic ID Extraction

`extract_topic_id(ms_path)` must look at the **parent directory** for nested layouts
and **the filename** for flat layouts. Common bug: extracting from `os.path.basename`
when the file is `topic.md` (returns "topic.md" → no ID extracted → "X.X.XX").

```python
def extract_topic_id(ms_path):
    parent = os.path.basename(os.path.dirname(ms_path))
    bn = os.path.basename(ms_path).replace('.md', '')
    if bn == 'topic':
        bn = parent
    m = re.match(r'^(\d+\.\d+\.\d+)', bn)
    return m.group(1) if m else 'X.X.XX'
```

## Source Dedup Pattern

Source has duplicate topic files in different subfolders. Example:
- `/mnt/tb/Medicine/Clinical Therapeutics and Good Prescribing/TDM/Aminoglycosides.md`
- `/mnt/tb/Medicine/Clinical Therapeutics and Good Prescribing/Therapeutic Drug Monitoring/Aminoglycosides.md`

Both are the same content. Without dedup, your audit reports source has 113
topics when it actually has 99 unique. This leads to fake "missing" reports.

```python
seen = set()
unique = []
for sp in all_source_files:
    bn = os.path.basename(sp)
    if bn not in seen:
        seen.add(bn)
        unique.append(sp)
```

## Verification Ritual Before Claiming Done

```bash
# 1. Topic count
python3 scripts/medsea_sync.py audit /mnt/tb/Medicine/Cardiology /mnt/tb/Sea-knowledge/#MedSea/chapters/16-cardiology

# 2. Section coverage table (above)
# 3. Spot-check word overlap on 3-5 random pairs (verify 100% or close)
# 4. Frontmatter sanity check (no double-frontmatter, topic_id correct)
# 5. Rebuild site + Docker
python3 scripts/site/build_site.py
docker build --no-cache -t medsea-site:latest .
docker stop medsea && docker rm medsea
docker run -d --name medsea -p 8855:80 --restart unless-stopped medsea-site:latest

# 6. Verify live site
curl http://localhost:8855/16-cardiology/topics.json | python3 -c "import json,sys; print(len(json.load(sys.stdin)['topics']))"
```

## Notion Sync Pattern (Pending)

The user explicitly asked for Notion sync each time. Notion sync requires:
- `NOTION_API_KEY` env var (or `/root/.hermes/.env` lookup)
- Python script with `urllib.request` (NOT `curl` — Unicode/special chars in titles
  cause shell escaping issues)
- Rate-limit handling (429 → `Retry-After` header → sleep)
- Per-page content update: clear existing blocks, append new ones in chunks
  (Notion has a 100-block limit per request)

`scripts/notion_sync_cardiology.py` is the existing pattern. For Ch 1-15 + Ch 16-20
sync, copy that pattern but iterate over the gapped pairs (445 topics in Ch 16-20,
65 in Ch 1-15).

## Common Pitfall: Timeouts on Bulk Operations

- 374-file write loop in `execute_code`: completes in ~1.5 seconds ✓
- 374-file Notion API call loop: takes 5-15 minutes (rate limits)
- 600+ file Docker rebuild: 5-10 minutes
- Git push of 500+ changed files: 1-3 minutes (can timeout at 60s, use 240s timeout)

Always set explicit `timeout` on terminal commands for ops over 60s.