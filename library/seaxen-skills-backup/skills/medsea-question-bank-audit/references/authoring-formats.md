# Authoring Formats — Worked Examples

Reference content extracted from the 2026-06-22 MedSea question bank audit. Each format below is a **real** block pulled from MedSea's authored `topic.md` files, with the parser that handles it and the expected output.

---

## Format 1 — Legacy bold-stem

**Where it appears:** Ch 5 (Nutritional Factors), Ch 14 (Infectious Disease), Ch 16 (Cardiology), Ch 26 (Dermatology) — most authored chapters.

**Raw block:**

```
1. **Typical latency between streptococcal pharyngitis and PSGN:**
   A. 1–3 days
   B. **1–3 weeks**
   C. 1–3 months
   D. 3–6 weeks
   E. Immediate
```

**Recognition rules:**
- First line: `1. ` + `**` ... `**` + optional `:` or `?` at end
- Subsequent lines: `A.` through `E.`, one option per line
- The correct option is the one wrapped in `**...**` (bolded at both ends)
- No `Answer:` line needed — the bolded option IS the answer

**Parser output:**
```python
{
    'stem': 'Typical latency between streptococcal pharyngitis and PSGN',
    'options': {
        'A': '1–3 days',
        'B': '1–3 weeks',
        'C': '1–3 months',
        'D': '3–6 weeks',
        'E': 'Immediate',
    },
    'answer': 'B',   # the option whose text was wrapped in **
}
```

**Common pitfalls:**
- Some options end with `**` but don't start with `**` (e.g. `A. **bold start`). Parser should treat `**` anywhere in the option text as a sign this might be the answer — but only commit to it if no other option is fully bolded.
- Some blocks have `A.` lines without leading spaces, others have `   A.` indented 3 spaces. Regex must allow leading whitespace.

---

## Format 2 — Plain-stem with inline Answer

**Where it appears:** Ch 19 (Biochemistry), Ch 22 (Gastroenterology) — most "newer" authored chapters.

**Raw block:**

```
1. **Hyponatraemia is defined as serum sodium:**
   A. <130 mmol/L
   B. <135 mmol/L
   C. <140 mmol/L
   D. <125 mmol/L
   *Answer: B*
```

**Variant:** some blocks use `**Answer: B**` (double-asterisk) instead of `*Answer: B*` (single-asterisk). Both must work:

```python
ANSWER_LINE_RE = re.compile(r'\*{1,2}Answer:\s*([A-E])\*{1,2}', re.I)
```

**Recognition rules:**
- First line: `1. ` + `**...**` (bold stem) — same as Format 1
- BUT: no option is bolded; instead there's a trailing `*Answer: B*` or `**Answer: B**` line

**Parser output:** identical shape to Format 1, with `answer` extracted from the trailing line.

**Common pitfalls:**
- The legacy parser matches the block first and returns `answer=None` because no option is bolded. **The pick_best() loop must keep trying other parsers** — `parse_plain_stem_block` will return the correct `answer='B'`.
- Some blocks have `**Answer: B** — explanation...` with extra explanation after the letter. The regex should extract just `[A-E]`, not the whole explanation.

---

## Format 3 — Inline Options/Answer (single-line)

**Where it appears:** Ch 27 (Neurology), Ch 28 (Medical Ophthalmology).

**Raw block:**

```
1. **Question:** The most common cause of viral conjunctivitis is:
   **Options:** A. HSV B. VZV C. Adenovirus D. Enterovirus E. EBV
   **Answer:** C
   **Explanation:** Adenovirus is the most common cause of viral conjunctivitis, particularly in epidemics.
```

**Recognition rules:**
- First line: `1. **Question:** <stem>`
- Second line: `**Options:** A. text B. text C. text D. text E. text` — all on ONE line, space-separated
- Third line: `**Answer:** <letter>`
- Optional: `**Explanation:** <text>` (do not parse)

**Parser output:** same shape as Format 1, with `answer` extracted from `**Answer:**` line.

**Common pitfalls (these bit the audit multiple times):**

1. **The `**Options:**` line may be indented** (e.g. `   **Options:** ...`). Use `.lstrip().startswith(...)` not `.startswith(...)`.

2. **The split regex must NOT require lookbehind for a period.** The naive `(?<=\.)\s+(?=[A-E]\.\s)` fails because the first option starts at position 0 with no preceding period. Use `\s+(?=[A-E]\.\s)` — split on spaces followed by an option letter + period + space.

3. **Multiple `**Answer:**` lines may appear** (rare, e.g. when the author re-asked the same question). Take the FIRST one.

4. **`**Question:**` prefix may or may not have a colon.** Accept both `**Question:** stem` and `**Question** stem`.

5. **Some blocks have explanation text following the answer line.** The parser must stop processing options when it sees `**Answer:**` or any other H2-like marker.

---

## Format 4 — Bullet-list options

**Where it appears:** Ch 17 (Respiratory Medicine) — the largest authored chapter.

**Raw block:**

```
1. A 65-year-old man with chronic LV failure presents with bilateral lower-zone dullness and dyspnoea. CXR shows blunted costophrenic angles bilaterally. Thoracentesis is performed: pleural protein 1.8 g/dL, serum protein 6.5 g/dL; pleural LDH 90 U/L, serum LDH 200 U/L, ULN serum LDH 200 U/L. Which is the most appropriate interpretation?
   - A) Exudate by Light's criteria — investigate for malignancy
   - B) Transudate by Light's criteria — consistent with heart failure
   - C) Indeterminate — repeat thoracentesis
   - D) Complicated parapneumonic effusion
   - E) Chylothorax

   **Answer: B** — Protein ratio 1.8/6.5 = 0.28 (≤0.5); LDH ratio 90/200 = 0.45 (≤0.6); pleural LDH 90 < ⅔ × 200 = 133. **All 3 Light's criteria negative = transudate**; consistent with heart failure.
```

**Recognition rules:**
- First line: `1. <plain stem>` — no bold on stem
- Subsequent lines: `- A) opt` or `- A. opt` (markdown bullet list)
- Trailing line: `**Answer: B** — <explanation>` (single or double asterisks)

**Parser output:** same shape, with `answer` extracted from the `**Answer: B**` line.

**Common pitfalls:**
- The bullet regex MUST accept both `- A)` and `- A.` (some authors use parens, some use periods). Regex: `r'^\s*[-*]\s*([A-E])[.)]\s*(.+?)\s*$'`
- The stem is plain (no bold). Some blocks have indented stems (e.g. `1. <stem>` followed by `\n   - A) opt`). The stem regex should not require bold.
- Explanation text after `**Answer: B**` may contain `**bold**` fragments. Strip them after extracting the letter.

---

## Format 5 — Factoid (flashcard in disguise)

**Where it appears:** Ch 20 (Endocrinology) — entire `## MCQs` section uses this format. Also partial in Ch 11, Ch 12, Ch 29, Ch 30.

**Raw block:**

```
1. **BMD T-score <=-2.5 at hip/spine (WHO)** — Osteoporosis definition:
2. **T-score -1.0 to -2.5** — Osteopenia definition:
3. **Hip (femoral neck) and lumbar spine (L1-L4)** — Osteoporosis DXA site:
```

**Recognition rules:**
- First line: `1. ` + `**...**` (the answer/fact) + ` — ` or ` - ` or `: ` (em-dash, hyphen, or colon) + topic/question
- No options, no `Answer:` line

**Parser output (as flashcard):**
```python
{
    'q': 'Osteoporosis definition?',   # turn topic into question (add ? if missing)
    'a': 'BMD T-score <=-2.5 at hip/spine (WHO)',  # the bold part
}
```

**Common pitfalls:**
- The factoid regex requires `\*\*X\*\*\s*[—\-:]\s*Y` — must accept em-dash, hyphen, and colon as the separator.
- The "question" part must be at least 2 words; otherwise drop the factoid (too short to be useful as a flashcard).
- These should be tagged `source: 'authored-factoid'` so they can be distinguished from real `## Flashcards` items.

---

## Format 6 — Parens options (ch 31/32 style, post-2026-06-22 audit)

**Where it appears:** Ch 31 (Adolescent Medicine), Ch 32 (Older Adult Medicine) — added after v5 audit found 910 MCQs being silently dropped.

**Raw block:**

```
1. Which of the following is true regarding DSM-5 criteria in Eating disorders - anorexia nervosa?
   A) Restriction -> low weight; intense fear of gaining weight; body image disturbance
   B) Restricting; Binge-eating/purging (compensatory behaviours)
   C) Adult <18.5; adolescent <5th centile (less reliable than weight history)
   D) 0.5-1% F; M:F = 1:10; peak onset 13-18 yrs
   **Answer: A**
```

**Difference from Format 1:**
- Stem is plain (not bold) — looks more like Format 2
- Options use `A)` parens, NOT `A.` periods
- `**Answer: A**` on a separate line

**Recognition rules:**
- First line: `1. <plain stem>` (no bold)
- Subsequent lines: `A) opt`, `B) opt`, etc. — parens, no bullet marker
- Trailing line: `**Answer: X**`

**Parser output:** same shape as Format 1, with `answer` extracted from the trailing line.

**The fix that matters:**
The original `LEGACY_OPT_RE` was `r'^\s*([A-E])\.\s*(.+?)\s*$'` (period required). It silently dropped every Format-6 block. **Fix: accept both `.` and `)` — `r'^\s*([A-E])[.)]\s*(.+?)\s*$'`.**

This single character-class change recovered 910 MCQs from ch 31 + ch 32 in the 2026-06-22 audit. **Without it, ch 31 and ch 32 had `mcq_count: 0` in the live bank** despite hundreds of authored MCQs sitting in the source tree.

**Pitfall:** Format 6 uses bare `A)` without a bullet marker, so `BULLET_OPT_RE` (which requires `[-*]\s*` prefix) does NOT match it. The block is caught by `LEGACY_OPT_RE` only.

---

## The 5th-Format Fallback: MCQ-shaped with no answer key

**A special case discovered in Ch 20 / Ch 14 / Ch 22**: the block looks like Format 1 (stem + A/B/C/D options) but NO option is bolded and there's no `Answer:` line.

```
1. **Acute coronary syndrome definition:**
   A. Plaque rupture with thrombosis
   B. Stable angina
   C. Variant angina
   D. Microvascular angina
```

The "right answer" is implicit (presumably A), but the author didn't mark it. The author intended this as study material, not a real MCQ.

**Two valid responses:**

1. **Drop silently** — easy, but you lose real authored facts.
2. **Rescue as flashcard** — `q = stem + "?"`, `a = options['A']`. Tag `source: 'authored-factoid'`. This recovered ~3,200 items in the 2026-06-22 audit.

**Pattern (use AFTER the 4 real-MCQ parsers have failed to find an answer):**

```python
if not best.get('answer') and len(best.get('options') or {}) >= 4:
    fact = parse_mcq_as_factoid_block(b) or {
        'q': best['stem'] if best['stem'].endswith('?') else f"{best['stem']}?",
        'a': next(iter(best['options'].values()), ''),
    }
    if fact.get('q') and fact.get('a'):
        flash_rows.append({...})
```

---

## YAML Frontmatter — not a question format, but a parser trap

Authored topic.md files start with a YAML frontmatter block:

```
---
tags: [hepatology, autoimmuneliver, aih, treatment, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 10: Clinical Biochemistry and Metabolic Medicine
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - Hyponatraemia is the most common electrolyte disorder..."
see_also: ["Hypernatraemia", "SIADH", "Diabetes Insipidus", "Potassium Disorders", "Acid-Base Disorders"]
created: 2026-06-15
modified: 2026-06-15
---
```

**Why this matters for "first meaningful sentence" extraction:** the naive `first_meaningful_sentence()` that just walks lines and skips empty ones will pick `tags: [hepatology, ...]` as the first sentence, or `exam_relevance: "..."` (which looks like a real sentence with a colon at the end).

**Fix:**
1. **Fence-skip `---` blocks** — flip an `in_frontmatter` flag on `---` lines.
2. **Whitelist known frontmatter keys** to skip even outside fences: `tags:`, `davidson_`, `status:`, `priority:`, `chapter:`, `heading:`, `exam_relevance:`, `see_also:`, `created:`, `modified:`, `id:`, `aliases:`.
3. **Skip `- [ ]` checkbox items** — they're in Learning Objectives sections and look like real sentences but aren't definitions.
4. **Skip lines starting with `#` (any header level)** — they're headers, not body content.

Without this, MCQs in ch 30 (Maternal Medicine) had definitions starting with `examrelevance: "FCPS/MRCP exam — key topic in maternal medicine."` — total nonsense as a definition.

---

## Headers — accept all 3 variants

```python
# All three of these are valid H2 headers for an MCQ section:
## MCQs
## MCQs (10)
## 18. MCQs (10)

# Regex:
re.compile(r'^##\s+(?:\d+\.\s+)?MCQs(?:\s*\([^)]*\))?\s*$', re.M)
```

The `(?:\d+\.\s+)?` part allows the leading chapter-local number. The `(?:\s*\([^)]*\))?` allows the count suffix like `(10)`.

**Same pattern for `## SBA Questions` and `## Flashcards`.**

---

## Numbered block splitter

A single MCQ section can contain many blocks. Split them by their leading number:

```python
NUM_BLOCK_RE = re.compile(r'(?m)^(?=\d+\.\s+)')
blocks = re.split(NUM_BLOCK_RE, section.strip())
```

This is a **lookahead-only split** — the number stays attached to its block, not pulled out as a separator. Each block can then be tested with the 5 parsers in order.

---

## Why one parser is never enough

The legacy `rebuild_question_bank_authored.py` only knew Format 1. Result:

- Live MCQ: **2,754**
- Source MCQ blocks: **~62,000**
- **Loss rate: ~95.5%**

After adding all 6 formats + scanning all `*.md`:

- Live MCQ: **11,603**
- **Recovered: ~8,800 additional MCQ blocks** (5,400 from v5 + 910 from v6 format-fix + ~2,500 from autogen in v6)

Same script, same quality filter. Just wider parser coverage.

**Always count the gap first.** If you don't measure, you can't claim "complete".
