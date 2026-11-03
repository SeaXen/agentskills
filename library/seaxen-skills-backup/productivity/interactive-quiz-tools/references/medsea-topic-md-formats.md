# MedSea topic.md — MCQ/SBA/Flashcard Format Variations

**Catalogue of every format variation found in MedSea topic.md files (validated 2026-06-21).** Use this BEFORE writing a new parser — confirm whether the source chapter matches an existing format or introduces a new one.

## Why this matters

The MedSea corpus has 1,400+ topic.md files. A single regex pattern handles at most 60% of them. The state-machine parser in `scripts/parser_lib.py` handles ALL three formats below. If you find a new format, add it to this catalogue AND to the parser.

## Format A — "no closing bold" (Ch 19 Biochemistry)

The most common format in chapters built before 2026-06-17. Stem line opens with `**` but never closes.

```markdown
## MCQs (10)
1. **Hyponatraemia is defined as serum sodium:
   A. <130 mmol/L
   B. <135 mmol/L
   C. <140 mmol/L
   D. <125 mmol/L
   *Answer: B*

2. **Which is NOT a Schwartz-Bartter criterion for SIADH?
   A. Serum Na⁺ <135 mmol/L
   B. Serum osmolality <275 mOsm/kg
   C. Urine osmolality >100 mOsm/kg
   D. Hypervolaemia
   *Answer: D*
```

**Detecting this format:**
- Stem line: `1. **text:` (note: no closing `**` at end)
- 4 options (A-D) with `*Answer: X*` (single asterisk wrap)
- Flashcard: `- Q: ...\n  A: ...` (no bold)

**Parser rule (in `parser_lib.py`):**
```python
# Format A stem extraction
def extract_stem(line):
    s = line.strip()
    m = re.match(r'^\d+\.\s+(.*)$', s)
    if not m: return None
    rest = m.group(1).strip()
    if rest.startswith('**'):
        # Format A: opens ** but no close. Strip trailing colons + stray *
        inner = rest[2:]
        return inner.rstrip(':').rstrip('*').strip()
    return rest
```

## Format B — "**Q:** prefix" (Ch 26 Dermatology, Ch 27 Neurology)

Used in chapters built with the Sea Knowledge study infographic pipeline. Stem line uses `**Q:**` to mark the question type, then text follows.

```markdown
## MCQs (5)
1. **Q:** Which of the following is a key feature of Congenital ichthyosiform erythroderma?
   A. Autosomal recessive
   B. Always self-limiting
   C. Caused by bacterial infection only
   D. Restricted to palms and soles only
   E. No investigation needed
   **Answer: A**
```

**Detecting this format:**
- Stem line: `1. **Q:** text` (`**` opens, `Q:**` closes, then text follows with NO closing `**`)
- **5 options** (A-E), not 4
- Answer: `**Answer: A**` (double asterisk wrap, both sides)
- Flashcard: `- **Q:** ...\n  **A:** ...` (bold Q: prefix)

**Parser rule (in `parser_lib.py`):**
```python
# Format B stem extraction
def extract_stem(line):
    s = line.strip()
    m = re.match(r'^\d+\.\s+(.*)$', s)
    if not m: return None
    rest = m.group(1).strip()
    if rest.startswith('**'):
        inner = rest[2:]
        if inner.startswith('**'):
            return inner.rstrip(':').rstrip('*').strip()
        # Format B: **Q:** text — strip the Q: prefix
        qm = re.match(r'^(Q|Question)\s*:\s*\**\s*(.*?)\**\s*$', inner, re.IGNORECASE)
        if qm: return qm.group(2).strip()
        return inner.rstrip(':').rstrip('*').strip()
    return rest
```

## Format C — variations (Ch 11 Poisoning, Ch 32 Ageing)

Inconsistent — some files use `## VIVA QUESTIONS` instead of `## MCQs`, some use 4 options, some 5, some use `*Answer:*` (note the trailing colon). The parser's flexibility is what catches these.

**Common variations:**
- `## VIVA QUESTIONS (5)` — header is "VIVA" not "MCQ" (Ch 16 source originally, but mixed in Ch 11 too)
- `*Answer:* B` — colon after `Answer`, letter is on same line
- `1. **Scenario:** ...` — stem prefixed with `Scenario:` for SBA questions
- `1. **Q:** ...\n   **A:** ...` — Q and A on same line in some flashcard files

**Parser rule (handles all of these via flexibility):**
- The section detector uses `h.startswith('mcq')` for MCQ — also matches "MCQs", "MCQ", and case-insensitive matches for `## VIVA QUESTIONS` IF the heading is also `VIVA`-prefixed (currently the parser only matches MCQ+SBA by exact word, so Viva gets MISSED). **Pitfall:** if you find VIVA QUESTIONS sections with question data, extend the section detector to also match 'viva' OR pre-rename those sections to `## MCQs` in source.
- The ANS_RE regex accepts `*Answer: X*`, `**Answer: X**`, `*Answer:* X`, `Answer: X` — all of these work because of `\**\s*Answer\s*:?\s*\**\s*([A-E])\s*\**\s*` (optional asterisks on each side, optional colon, optional trailing space).

## When to extend the parser

Add a new format to `parser_lib.py` ONLY when you find a topic.md file where:
1. The current parser returns 0 questions for a file you know has questions (use `python3 -c "from parser_lib import parse_topic; print(parse_topic(open('FILE').read(), 1, 'X', 's', 't'))"` to test)
2. The current parser drops options (e.g. the file has 5 options but only 3-4 are captured)
3. The current parser treats a non-question as a question (false positives)

**Don't add a format for:**
- Files where the question is in a non-standard section (e.g. `## Cases` instead of `## MCQs`) — those are by design not MCQ pools
- Files where the answer uses Roman numerals (I/II/III instead of A/B/C) — convert in source instead
- Files where the stem contains a numbered list (e.g. "1. **What are the 4 causes?   1. X  2. Y  3. Z  4. W**") — these are not interactive MCQs, they're enumerated content

## Per-chapter format summary (validated 2026-06-21)

| Chapter | Format | A-E? | VIVA? | Notes |
|---|---|---|---|---|
| Ch 10 Acute Medicine | A | 4 | No | Few topics with MCQs |
| Ch 11 Poisoning | C (mixed) | varies | Yes (some files) | 364 SBAs, 0 MCQs — most files only have SBAs |
| Ch 12 Envenomation | A | 4 | No | Flashcards only, no MCQ/SBA |
| Ch 14 Infectious Disease | A | 4 | No | 28 topics with flashcards only |
| Ch 15 STI | A | 4 | No | Flashcards only |
| Ch 16 Cardiology | A | 4 | Yes (96% — VIVA QUESTIONS heading) | 57 topics, 450 cards, 0 MCQ/SBA in MDs — Viva not parsed currently |
| Ch 18 Nephrology | A | 4 | No | Flashcards only |
| Ch 19 Biochemistry | A | 4 | No | 28 topics, full MCQ+SBA+Flash, 280+140+140 |
| Ch 22 Gastroenterology | A | 4 | No | Flashcards only |
| Ch 24 Haematology | A | 4 | No | 1 topic |
| Ch 26 Dermatology | B | 5 (mostly) | No | 385 topics, 1355+1490+1950 (largest chapter) |
| Ch 27 Neurology | B | 5 (mostly) | No | 370 topics, 141+64+1767 |
| Ch 28 Ophthalmology | A | 4 | No | 97 topics, 537 cards, 0 MCQ/SBA in MDs |
| Ch 29 Psychiatry | A | 4 | No | 94 topics, 0 questions in MDs |
| Ch 30 Maternal | A | 4 | No | 110 topics, 0 questions in MDs |
| Ch 31 Adolescence | A | 4 | No | 53 topics, 0 questions in MDs |
| Ch 32 Ageing | A | 4 | No | 40 topics, 0 questions in MDs |

**Chapters with 0 questions in MDs are content gaps** — the topic.md files have clinical content but no MCQ/SBA/Flashcard sections. Filling these is a separate task (requires generating questions, not just sync).

**Ch 16 + Ch 11 VIVA QUESTIONS** are NOT being parsed by the current extractor. If you need those questions in the pool, either:
- Pre-rename the section in source: `sed -i 's/^## VIVA QUESTIONS/## MCQs/' chapters/16-cardiology/diseases/*/topic.md`
- OR extend the section detector: `elif h.startswith('viva') or 'viva' in h: section = 'mcq'  # treat Viva as MCQ for parsing`

## Validation commands

```bash
# Test the parser on a specific file
python3 -c "
import sys; sys.path.insert(0, '/root/.hermes/skills/productivity/interactive-quiz-tools/scripts')
from parser_lib import parse_topic
text = open('PATH_TO_TOPIC.md').read()
mcq, sba, fc = parse_topic(text, 1, 'X', 's', 'test')
print(f'mcq={len(mcq)} sba={len(sba)} fc={len(fc)}')
if mcq: print('Q1:', mcq[0]['question'][:80], 'options:', list(mcq[0]['options'].keys()))
"

# Find topic.md files that should have questions but parse to 0
# (run after extract_questions.py completes)
python3 -c "
import json, os, re
d = json.load(open('/mnt/tb/Sea-knowledge/#MedSea/site/assets/questions.json'))
extracted = set((q['chapter_num'], q['topic_slug']) for q in d['mcq']+d['sba']+d['flashcard'])
# Find topic.md files that mention MCQ/SBA/Flashcard in their headers
candidates = []
for root, dirs, files in os.walk('/mnt/tb/Sea-knowledge/#MedSea/site'):
    if 'topic.md' in files:
        path = os.path.join(root, 'topic.md')
        text = open(path).read()
        if re.search(r'^## (MCQs|SBA|Flashcards)', text, re.MULTILINE):
            m = re.match(r'/mnt/tb/Sea-knowledge/#MedSea/site/(\d+)-([^/]+)/diseases/([^/]+)/', path)
            if m:
                ch_num = int(m.group(1))
                topic_slug = m.group(3)
                if (ch_num, topic_slug) not in extracted:
                    candidates.append(path)
print(f'Files with section headers but 0 extracted questions: {len(candidates)}')
for p in candidates[:10]: print(' ', p)
"
```
