---
name: medsea-question-bank-audit
description: Use when auditing or rebuilding the MedSea live JSON question bank consumed by /exam/ and /flashcards/. The bank lives in site/assets/questions-{mcq,sba,flashcard,index}.json and is regenerated from authored `## MCQs`, `## SBA Questions`, `## Flashcards` sections inside topic.md files. The trap this skill addresses is parsers that handle only ONE authoring format and silently drop 90+ percent of real authored content. Use also when the user reports questions have no scenario, 1-word prompts, single-option MCQs, flashcards are junk, or many questions with only 1 option. Also covers **autogen** of MCQ/SBA/Flashcard sections from authored prose for chapters that have content but no study sections (see references/autogen-from-authored-content.md).
---

# MedSea Question Bank Audit & Rebuild

## Trigger

Use when the user reports any of:
- Exam or flashcard questions are broken, templated, junk, 1-word prompts, single-option
- Live JSON shows far fewer items than authored source has
- A specific question bank pass needs strict quality enforcement
- After authoring a new batch of MCQ/SBA/Flashcard sections and wanting the live bank rebuilt
- User asks to "fill in the gaps" / "add study material for the empty chapters"
- **User asks for "10/10 rating", "audit everything", "fill all gaps", "make it perfect", or comprehensive QA before production release**
- **User asks for multi-sector ratings (code/bank/UX/performance), performance analysis, or "is everything OK?"**

## The Honest Audit First — measure before fixing

**The single biggest lesson from real audit sessions: never claim the live bank is "clean" or "complete" without measuring the gap between live and source.**

Before writing any parser code:

1. **Count authored blocks** per `## MCQs / ## SBA Questions / ## Flashcards` section across the whole `chapters/*.md` tree (all files, not just `topic.md`).
2. **Count live JSON** items: `len(json.load(open('site/assets/questions-mcq.json')))` etc.
3. **Report the gap honestly.** If source has 60,000 MCQ blocks and live has 2,754, the parser is dropping ~95% — DO NOT report "live is clean" before fixing.

Reporting format the user values:

```
Live bank:    MCQ 2,754   SBA 1,320   FC 2,814   Chapters 16
Source disk:  MCQ ~62,000  SBA ~44,000  FC ~5,100  Chapters 32
Gap:          parser is dropping ~95% of authored material
```

**The user's preference:** report what was sampled, not "I checked everything". They will repeat "check files 1 by 1" if you skip the numbers.

## Six Authoring Formats the Parser MUST Handle

Real-world MedSea topic.md files use **six** distinct MCQ/SBA formats. A parser that handles only one will silently drop everything else. Document each format in `references/authoring-formats.md` for the next rebuild.

| # | Format | Stem | Options | Answer |
|---|--------|------|---------|--------|
| 1 | **Legacy bold-stem** | `1. **stem**` | `A. opt` per line | bolded option: `B. **correct**` |
| 2 | **Plain-stem** | `1. plain stem` | `A. opt` per line | inline `*Answer: B*` or `**Answer: B**` line |
| 3 | **Inline options** | `1. **Question:** stem` | single-line: `**Options:** A. opt B. opt C. opt D. opt E. opt` | `**Answer:** B` |
| 4 | **Bullet-list options** | `1. plain stem` | `- A) opt` or `- A. opt` per line | `**Answer: B** — explanation` |
| 5 | **Factoid (flashcard in disguise)** | `1. **Term** — Topic:` | none (no real options) | none |
| 6 | **Parens-options (ch 31/32 style)** | `1. **stem**` | `A) opt` per line (no bullet, parens not period) | `**Answer: B**` |

**Format 6 is the one that bit the v5 audit (2026-06-22).** Ch 31/32 source topics used `A) text` instead of `A. text`. The legacy parser required `LEGACY_OPT_RE = r'^\s*([A-E])\.\s*(.+?)\s*$'` (period). **Fix: accept both — `r'^\s*([A-E])[.)]\s*(.+?)\s*$'`.** After this single character-class change, +910 MCQs were recovered from ch 31 and ch 32 alone.

**All six exist in MedSea because different chapter authors wrote at different times.** Ch 5/14/16 = format 1. Ch 19/22 = format 2 (`*Answer: X*`). Ch 27/28 = format 3 (inline Options). Ch 17 = format 4 (bullet list). Ch 20 = format 5 (flashcard-only). Ch 31/32 = format 6 (parens options).

### Parser dispatching pattern

```python
PARSERS = (parse_legacy_bold, parse_plain_stem, parse_inline_options, parse_bullet_list)

def pick_best(block: str) -> dict | None:
    """Try all parsers. Prefer the one that returned a real answer."""
    best = None
    for parser in PARSERS:
        item = parser(b)
        if not item or not item.get('stem'):
            continue
        if item.get('answer') in (item.get('options') or {}):
            return item                          # first one with a real answer wins
        if best is None:
            best = item                          # fallback: keep no-answer item
    return best
```

**Pitfall:** if the parser list is `(legacy, plain_stem)` and `legacy` matches a block first but returns `answer=None` while `plain_stem` would have returned `answer='B'`, the legacy win means you lose the answer. **Always loop with an "answer-present wins" check.**

### Numbered-header regex

Headers appear as `## MCQs`, `## MCQs (10)`, `## 18. MCQs (10)` — accept all three:

```python
re.compile(r'^##\s+(?:\d+\.\s+)?MCQs(?:\s*\([^)]*\))?\s*$', re.M)
```

### Option-label regex — accept `.` AND `)`

The audit was bitten by Format 6 (parens options). The single regex change covers both:

```python
LEGACY_OPT_RE = re.compile(r'^\s*([A-E])[.)]\s*(.+?)\s*$')
BULLET_OPT_RE = re.compile(r'^\s*[-*]\s*([A-E])[.)]\s*(.+?)\s*$')
```

Don't forget — `A)` in markdown line-initial position is also valid as a bullet marker (without `-` prefix) in some authored styles. If format 6 has bare `A) text` (no `-` bullet), it's caught by `LEGACY_OPT_RE` not `BULLET_OPT_RE`.

### Inline Options parser trap

When the line is indented (e.g. `   **Options:** A. opt B. opt ...`), `.startswith('**Options:**')` fails. Use `.lstrip().startswith(...)`.

The split regex `\s+(?=[A-E]\.\s)` (just space + lookahead, no preceding-period requirement) works; the more "obvious" `(?<=\.)\s+(?=[A-E]\.\s)` requires lookbehind and breaks on the first option.

## Factoid Routing — DO NOT route MCQ-without-answer to flashcards with first option as back

**Earlier recommendation (now reverted):** the v5 parser used to rescue authored MCQ blocks that lacked an answer key by routing them to flashcards with `front=stem`, `back=first_option`. This was wrong in practice.

**Why it was wrong (the 2026-06-22 audit caught it):**

```python
# WRONG (v5 behaviour — DO NOT use)
if not best.get('answer') and len(best.get('options') or {}) >= 4:
    fact = parse_mcq_as_factoid_block(b) or {
        'q': best['stem'] if best['stem'].endswith('?') else f"{best['stem']}?",
        'a': next(iter(best['options'].values()), ''),  # ← ALWAYS option A
    }
```

The first option in a 4–5 option MCQ is **rarely** the correct answer. Routing 874 such blocks to flashcards produced visibly wrong cards:

| Vignette stem | Back (was option A) | Correct answer |
|---|---|---|
| "A 69-year-old woman has new temporal headache, scalp tenderness, jaw pain while chewing" | "Migraine" | **Giant cell arteritis** |
| "A 68-year-old with diabetes, fever, confusion, neck stiffness, new focal deficit" | "Immediate LP without further assessment" | **CT head first, then LP** |
| "A 20-year-old athlete has exertional syncope and a systolic murmur that becomes louder with Valsalva" | "HCM" | (this one was correct, lucky) |
| "A 45-year-old immunocompromised with fever, headache, ring-enhancing lesion" | "Brain abscess / infection" | **Toxoplasmosis** or **primary CNS lymphoma** |

**The correct policy (post-audit):**

1. **Drop MCQ/SBA blocks that have no answer key.** They are an authoring gap, not content we can re-purpose honestly. Authored blocks without answers cannot become honest study material — there is no way to know which option is correct.

2. **The honest recovery path for factoid-style content** is the `## Flashcards` section (with author-curated Q/A), not rescuing MCQ-shaped blocks. If an author writes a topic with `1. **Term** — Definition` style, that already goes to flashcards via `parse_factoid_block` — that path is correct because the author wrote the answer themselves.

3. **If the rescue pattern must stay** (e.g., to ship a chapter the user needs urgently), add a marker the author must provide — e.g., `**A. correct**` (option A is the answer). Without the marker, drop.

The old code path was rescuing ~3,200 blocks (ch 20 endocrinology alone contributed 1,740 flashcards). After the fix, those 1,740 are gone from flashcards. **Honest gaps: report them, do not paper over them with wrong cards.**

```python
# CORRECT (post-audit behaviour)
if not best.get('answer') and len(best.get('options') or {}) >= 4:
    # MCQ/SBA without answer key — DO NOT route to flashcards with
    # option A as the answer (it would be a wrong, misleading card).
    # Skip these blocks entirely. Authored items without answer keys
    # are an authoring gap, not content we can honestly re-purpose.
    pass
elif quality_ok(best, need_options=4, min_stem_words=10, need_scenario=True):
    sba_rows.append({...})
```

The ch 20 +1,740 "flashcards" turned out to be option-A-as-back of MCQ-without-answer blocks. The chapter now has 10 MCQs (from the few blocks with explicit answer keys) and ~2,700 real flashcards (from `## Flashcards` sections, untouched).

## Autogen-Specific Quality Pitfalls — content that passes the basic filter but is still wrong

The `quality_ok` filter above catches: too few options, missing answer, contextless stem, too-short stem. **Five more failure modes appeared only when autogen (table → MCQ/flashcard) was added** to the pipeline. None of these would show up in authored content but ALL of them appear when an LLM-style extractor pulls Q/A from prose. Apply these in the same `quality_ok` (or as a final post-write filter):

```python
GENERIC_DISTRACTORS = (
    'an unrelated condition not matching',
    'a complication seen late in the disease',
    'a condition that mimics',
    'none of the above',
    'all of the above',
)

def quality_ok(item, *, need_options, min_stem_words, need_scenario):
    stem = (item.get('stem') or '').strip()
    opts = item.get('options') or {}
    ans = item.get('answer')
    if not stem or len(opts) < need_options or not ans or ans not in opts:
        return False
    if len(stem.split()) < min_stem_words:
        return False
    if is_contextless(stem):
        return False
    if need_scenario and len(stem.split()) < 12:
        return False

    # ---- Autogen pitfalls (NEW) ----
    # 1. Table-pipe leakage: markdown table cells (`| foo | bar |`) ended up
    #    in option text because the extractor pulled the first row of a
    #    comparison table as "options". Symptom: option A is `| Column | Value |`.
    if any('|' in (v or '') for v in opts.values()):
        return False

    # 2. Generic placeholder distractors: ≥2 of 4 options are autogen
    #    boilerplate ("An unrelated condition not matching the clinical
    #    picture of X"). Detected by substring match.
    if sum(1 for v in opts.values()
           if any(g in (v or '').lower() for g in GENERIC_DISTRACTORS)) >= 2:
        return False

    # 3. Bold-label residue: option text starts with `**A.**` because
    #    the extractor kept the original `A.` label prefix instead of
    #    stripping it. Symptom: "**A.** Diclofenac + tamsulosin".
    if any(re.match(r'^\s*\*\*[A-E][\.\)]', v or '') for v in opts.values()):
        return False

    # 4. Formal "Q:" / "Question:" prefix on stem: extractor preserved
    #    the markdown `**Q:**` header in the stem text. Symptom:
    #    stem starts with `Q: First-line treatment for X?`.
    if re.match(r'^\s*(\*\*?Q[\.:\)]|\*\*Question[:\)]|\d+\.\s*\*\*?Q[\.:])', stem):
        return False

    return True
```

For flashcards (no options), apply the same pipe + wikilink filter as a final post-write pass:

```python
def flash_ok(c):
    f = (c.get('front') or '').strip()
    b = (c.get('back') or '').strip()
    if not f or not b:
        return False
    # 5a. Pipe-leakage in front or back (table cells)
    if '|' in f or '|' in b:
        return False
    # 5b. Wikilink leakage — autogen picked the MOC link as the "definition"
    if '[[' in f or '[[' in b:
        return False
    # 5c. Back is just a table header row fragment
    if b.startswith('|') or b.endswith('|'):
        return False
    if len(f.split()) < 3 or len(b.split()) < 2:
        return False
    # 5d. Front is a long vignette (>15 words) — that's a factoid-routed
    #     MCQ stem misconverted to a flashcard. Even with the fix above,
    #     some old builds shipped them. Drop them post-write.
    if len(f.split()) > 15:
        return False
    return True
```

### What each pitfall looks like in the live bank

| # | Pitfall | Symptom in option / stem | Real example |
|---|---|---|---|
| 1 | Pipe leakage | `A. \| # \| Slug \| Title \|` | ch 20 endocrinology, autogen MCQs |
| 2 | Generic distractor | `B. An unrelated condition not matching the clinical picture of X` | ch 23, 24, 25 autogen MCQs |
| 3 | Bold-label residue | `A. **A.** Diclofenac + tamsulosin` | ch 14 infectious disease |
| 4 | Q: prefix | `Q: Cuff leak <110 mL suggests:` | none (filter works) |
| 5a | Pipe in FC back | `\| Parameter \| Change \| Clinical Implication \|` | ch 23 hepatology flashcards |
| 5b | Wikilink in FC back | `Related: [[../Rheumatology MOC\|Rheumatology MOC]]` | ch 25 rheumatology |
| 5c | Front vignette >15 words | `A 64-year-old heavy smoker presents with weight loss, hyponatremia, and a central hilar mass...` → `adenocarcinoma` (wrong; correct is **small cell**) | ch 17 respiratory |

**The 5d vignette check is the most important** because it's the failure that ships wrong clinical answers. Long fronts on flashcards are almost always MCQ stems that escaped the parser chain. Drop them on sight.

### Always report the filter wins

After running these filters, report the dropped count per pitfall so the user sees the quality bar working:

```
MCQ bad: pipe=119, generic=380, label_leak=18 → dropped 497
Flashcard bad: pipe=106, wikilink=9, vignette=874 → dropped 989
Final bank: MCQ 11106  SBA 2581  Flashcards 17844  (was 31,531)
```

The drop count IS the proof that the filters work. A user who sees "we removed 497 broken MCQs" trusts the result; a user who sees "we shipped 11,106 MCQs" without the drop count does not.

## Strict Quality Filters — never lower these to make numbers look good

The user explicitly complained about "questions with 1 option", "1-word prompts", "no scenario". Apply these filters:

| Item | min_options | min_stem_words | need_scenario |
|------|-------------|----------------|---------------|
| MCQ  | 4           | 5              | False         |
| SBA  | 4           | 10             | **True**      |
| Flash | n/a         | 3 (front)      | n/a           |

**Contextless-stem blacklist** (drop these as obviously broken):

```python
CONTEXTLESS = {
    'what is the first-line treatment?',
    'what is the most important complication?',
    'what is the diagnosis?',
    'what is the treatment?',
    'what is the best investigation?',
}
```

These are "stems that depend on the topic title" — they only make sense in context. Reject them.

**Always report quality stats after a rebuild:**

```python
quality_stats = {
    'mcq':  {'one_option': N, 'missing_answer': N, 'junk_stem': N},
    'sba':  {'one_option': N, 'missing_answer': N, 'junk_stem': N},
    'flash': {'no_question_mark': N, 'short_front': N},
}
```

Print these and the user will trust the result.

## Scan ALL `*.md` files — not just `topic.md`

**Critical pitfall:** the legacy `rebuild_question_bank_authored.py` (and any audit that uses `find_files()` from `build_site.py`) only walks `topic.md` files. **MedSea has authored MCQ/SBA/Flashcard sections in 868 OTHER `*.md` files** (e.g. `chapters/5-nutritional-factors/diseases/5.4.06-iron-ida-acd-haemochromatosis-full.md`).

**Symptom:** total MCQ blocks across all `*.md` is ~62,000, but a `topic.md`-only rebuild produces ~2,754. The 95% loss is from this single bug.

**Fix:** walk with `Path('chapters').rglob('*.md')` — the rebuilt parser in `site/scripts/rebuild_question_bank_v5.py` does this and recovered ~5,400 additional MCQ blocks.

```python
files = sorted(Path('chapters').rglob('*.md'))
for md_path in files:
    if md_path.parent == Path('chapters'):  # skip meta files at root
        continue
    # ... process
```

## Autogenerating Study Sections for Chapters That Have Content But No Exam Items

When chapters have authored prose (drug/regimen tables, definition blockquotes, clinical features sections) but **no** `## MCQs / ## SBA Questions / ## Flashcards`, you can autogenerate from the body. See **`references/autogen-from-authored-content.md`** for the full pattern. Quick summary:

- Flashcards extracted from "good" 2-col reference tables (Drug/Regimen/Treatment columns). **Anchor questions to the topic title, NOT the section header** — otherwise you get "What is the MELD of MELD-Na?".
- 1 MCQ per topic (definition-based), 1 SBA per topic (features-based).
- Strict table-quality filter: 2-col, col1 short label (≤8 words), col2 substantive (≥3 words). Skip comparison tables (`Compensated vs Decompensated`) and meta/review tables (`FCPS/MRCP High-Yield Summary`, `Viva Questions`).
- The published-vs-source slug matcher is its own bag of bugs — see the reference for the matcher template.

## Before Bulk Autogen — Ask the User

**When the user asks to "fill in the gaps" or "generate MCQs for empty chapters", do NOT silently run the generator over everything.** The 2026-06-22 session had 13 empty chapters (~500 topics, ~5,000 potential items) and the work spanned:

- Per-topic generation (slow, high quality)
- Bulk autogen from authored tables (fast, lower quality)
- Hand-curated MRCP/FCPS exam items (slowest, highest quality)

Before starting, ask one clarifying question with the trade-offs spelled out — speed vs quality vs scope. The user values being asked over being steamrolled. If the user doesn't respond, take the **honest default**: hybrid (autogen from existing prose where available, do NOT fabricate for empty chapters). Surface the empty chapters explicitly so the user can decide whether to author them next.

## Honest Gap Reporting — never claim "all done"

After rebuild, **explicitly list which chapters are still empty and why**:

```
13 chapters still empty (no authored ## MCQs/SBA/Flashcards sections in their topic.md):
  1, 3, 4, 6, 8, 13, 21, 23, 25, 29, 30, 31, 32

  29, 30, 31, 32 — only have hub/overview files; disease sub-topics don't exist yet
  1, 3, 4, 6, 8, 13, 21, 23, 25 — content exists but no exam sections written
```

**This is exactly what the user wants.** The pattern from past sessions: "I checked" or "complete" without chapter-level numbers will be challenged with "check files 1 by 1". Always include the per-chapter breakdown.

## Deploy Verification Gate — never claim "deployed" without this

**The single most expensive mistake in this workflow is claiming "deployed" or "live verified" when the autogen wrote to source files but the live container still serves the old bank.** The 2026-06-23 PasTest scenario autogen produced 1,879 topic files with `## PasTest Scenario SBAs` sections and the agent reported "SBA 2,581→4,275, deployed + live verified" — the audit caught it as a lie. Live site had 0 PasTest items because step 2 (rebuild) and step 3 (docker cp) were skipped.

**The full deploy cycle is FOUR separate steps. Every autogen run must complete all four. Skipping any one is a lie.**

```
1. AUTOGEN    — write to chapters/*.md (source)
2. REBUILD    — python3 site/scripts/rebuild_question_bank_v5.py
3. DEPLOY     — docker cp site/assets/questions-*.json <container>:/usr/share/nginx/html/assets/
   PERSIST    — docker commit <container> medsea-site:latest
4. VERIFY     — bash scripts/verify_live_question_bank.sh
```

**The verification script is the gate.** It compares three sources of truth:
- local JSON on disk
- JSON inside the running container
- JSON served by HTTP on the live port

If any of the three disagree on item count, the script exits non-zero. It does not "warn and continue" — mismatch is a hard failure. Run it after every autogen. Read the output before reporting success.

```bash
# After every autogen, run this single command to ship + verify:
python3 site/scripts/rebuild_question_bank_v5.py && \
  docker cp site/assets/questions-mcq.json medsea:/usr/share/nginx/html/assets/ && \
  docker cp site/assets/questions-sba.json medsea:/usr/share/nginx/html/assets/ && \
  docker cp site/assets/questions-flashcard.json medsea:/usr/share/nginx/html/assets/ && \
  docker cp site/assets/questions-index.json medsea:/usr/share/nginx/html/assets/ && \
  docker commit medsea medsea-site:latest && \
  bash scripts/verify_live_question_bank.sh
```

`verify_live_question_bank.sh` checks (1) local JSON exists and parses, (2) container JSON matches local, (3) HTTP-served JSON matches local, (4) browser-side spot-check of chapter distribution. On any mismatch it prints a red `VERIFY FAILED` and the missing steps, then exits 1.

**If you cannot run `verify_live_question_bank.sh` because docker is unavailable or python3 lacks a required module, do not claim "deployed" anyway.** State the blocker plainly: "autogen wrote to source, but I cannot verify the live container was updated from this environment."

### The three truths that must agree

| Source | What it represents | How to check |
|---|---|---|
| `site/assets/questions-*.json` (host) | What you just built | `ls -la site/assets/questions-*.json` + `python3 -c "import json; print(len(json.load(open('site/assets/questions-sba.json'))))"` |
| `/usr/share/nginx/html/assets/questions-*.json` (container) | What nginx is currently serving | `docker exec medsea stat -c%s /usr/share/nginx/html/assets/questions-sba.json` + `docker exec medsea python3 -c "import json,sys; print(len(json.load(sys.stdin)))" < /usr/share/nginx/html/assets/questions-sba.json` |
| `curl http://<host>:<port>/assets/questions-*.json` (HTTP) | What the browser actually loads | `curl -s http://localhost:8855/assets/questions-sba.json \| python3 -c "import json,sys; print(len(json.load(sys.stdin)))"` |

If the three item counts disagree at any step, the deploy is broken — do not report success. The script `scripts/verify_live_question_bank.sh` automates this three-way check.

### Missing chapter in exam setup / chapter won't start — what it usually means

A chapter chip showing in the filesystem but missing from the live exam setup is usually **not** a frontend bug. In practice it means the chapter contributed **zero rows** to `questions-index.json`, so the UI has nothing to list or start from.

Check these in order:

1. **Index presence** — does `questions-index.json` contain the chapter at all?
2. **Per-chapter counts** — is `sba_count`/`mcq_count`/`flashcard_count` all zero?
3. **Source→published chapter mapping** — does the autogen script know how to map the source chapter folder to the published chapter slug?

Real example from the live audit: `chapters/21-diabetes-mellitus/` existed, but `questions-index.json` omitted chapter 21 entirely because both autogen scripts were missing `Diabetes -> 21-diabetes-mellitus` in `SRC_TO_PUB`. Result: chapter select could not produce a runnable exam for ch 21. Fix was to add the mapping to **both** `autogen_scenario_sbas.py` and `autogen_study_sections.py`, rerun generators, rebuild JSON, and redeploy.

Do not stop at JSON-only proof. Browser-verify the exact user flow:
- `/exam/` shows the chapter chip
- clicking the chapter changes Available count from all-chapters total to a chapter-specific number
- clicking **Start Exam** actually enters the runner

### Style-only SBA pass — when the user wants better SBA phrasing without sacrificing chapter coverage

Sometimes the live SBA bank is numerically fine but a large slice of **autogenerated** SBAs reads too much like textbook prompts:

- `Which of the following features is most specific or characteristic of X?`
- `What is the most appropriate first-line therapy for X?`

If the user asks for **"one more quality pass only on SBA style"**, do not immediately delete these and wipe out whole chapters. Prefer this two-step approach:

1. **Rewrite generic autogenerated stems at rebuild time** into more exam-like wording:
   - `Which of the following features is most specific or characteristic of X?`
     → `In a patient with suspected X, which of the following findings would be most characteristic?`
   - `What is the most appropriate first-line therapy for X?`
     → `A patient presents with X. What is the most appropriate initial management?`
2. **Keep a style gate** for PasTest-autogen items so only allowed stem shapes survive:
   - age-based vignette (`A 65-year-old ...`)
   - rewritten patient/suspected forms above
   - triad-recognition
   - avoid/contraindication
   - landmark-trial

Minimal rebuild helper:

```python
def rewrite_pastest_stem(stem: str, topic_title: str) -> str:
    s = stem.strip()
    feature_prefix = 'Which of the following features is most specific or characteristic of '
    first_line_prefix = 'What is the most appropriate first-line therapy for '
    if s.startswith(feature_prefix):
        subject = s[len(feature_prefix):].rstrip(' ?.') or topic_title
        return f'In a patient with suspected {subject}, which of the following findings would be most characteristic?'
    if s.startswith(first_line_prefix):
        subject = s[len(first_line_prefix):].rstrip(' ?.') or topic_title
        return f'A patient presents with {subject}. What is the most appropriate initial management?'
    return s
```

Apply the rewrite **before** the PasTest style gate in `rebuild_question_bank_v5.py`.

**Why this matters:** a hard drop can make chapters vanish from SBA mode entirely. The rewrite preserves chapter coverage while clearly improving the live stems.

### Honest limits of the rewrite: don't fake a vignette when the source can't back it

The rewrite pass transforms `Which of the following features is most specific or characteristic of X?` into `A patient presents with suspected X. Which of the following findings would be most characteristic?` — even when the source topic body has no real `N-year-old presents with Y` sentence.

This is an improvement, but **don't pretend it's a real PasTest vignette**. The rebuilder has three depth levels:

1. **Real frame** — the source body literally contains `N-year-old <sex> presents with Y`. Build a true vignette.
2. **Real finding** — a `## Clinical Features / Diagnosis / Presentation` section in the source has a short bolded noun phrase. Splice it into the stem.
3. **Neither** — the source is just templated H2 headers (`## Etiology & Pathophysiology`). Fall back to a generic demographic + topic title. **This is the floor, not the ceiling.** A topic stuck at level 3 needs human-authored source prose before it can climb.

The detector for level-3 material is `extract_topic_frame() returning None` AND `_extract_clinical_features() returning []` AND `_real_clinical_frame() returning False`. When all three trigger, **don't ship a fake-vignette rewrite** — keep the previous style rewrite (`A patient presents with suspected X`) and accept that the question reads semi-generic.

Refusing to fake improves correctness. Shipping a stem like `A 55-year-old man presents with features consistent with Etiology & Pathophysiology. Which of the following findings would be most characteristic of Etiology & Pathophysiology?` is technically a "vignette" but it's a textbook complaint being given a wrapper. The user will read it and roll their eyes. Better to ship `A patient presents with Etiology & Pathophysiology. What is the most appropriate initial management?` — still generic, but at least not pretending.

### Upgrading pas test autogen distractors to real clinical alternatives

The autogen sometimes writes placeholder text into the wrong-answer options:

- `An unrelated condition not matching the clinical picture of X`
- `Routine supportive care (fluids, oxygen, monitoring)`
- `Empiric broad-spectrum therapy without specific indication`
- `Standard guideline-directed first-line therapy`

These read like a Mad Libs, not an exam. The autogen already keeps a curated per-chapter `DISTRACTOR_POOLS` dictionary in `autogen_scenario_sbas.py` with **real conditions** (e.g. `Constrictive pericarditis`, `HHS`, `Lactic acidosis`, `Takayasu arteritis`). The rebuilder can swap placeholder text for those real conditions at build time:

```python
def upgrade_pastest_distractors(
        options, answer_letter, ch_dirname) -> dict | None:
    pool = CHAPTER_DISTRACTORS.get(ch_dirname) or []
    if not pool:
        return None
    new_options = dict(options)
    candidates = [k for k in 'BCD' if k != answer_letter
                  and generic_distractor_text(new_options.get(k, ''))]
    if not candidates:
        return None
    chosen = [c for c in pool if c not in chosen
              and c != new_options.get(answer_letter)]
    for letter, cond in zip(candidates, chosen):
        new_options[letter] = cond
    return new_options
```

Rules of thumb:
- Only swap when the option text is still generic (`generic_distractor_text`).
- Never overwrite the correct answer.
- Always preserve the answer letter.
- If the chapter has no curated pool, leave the option alone.

Coverage: 2,486 / 2,486 pas test items now have real clinical alternatives after this pass in the live bank (0.0% placeholder distractors). All 32 chapters have a curated `DISTRACTOR_POOLS` entry. See `references/chapter-distractor-pool-coverage.md` for the full per-chapter status, the missing-pool list, and the canonical Python snippet to re-measure coverage after each rebuild.

### Three failure modes the distractor audit must catch (in order)

A correct answer + four plausible distractors is the MRCP/FCPS minimum. The audit should check three independent failure modes:

1. **Placeholder text in options** — already covered above. Regex over option text against `An unrelated condition not matching…` and friends. Target: 0/12,774.

2. **Same-3-distractor repetition across a chapter** — the autogen picked `pool[0:3]` for every item, so 598/639 Ch 16 Cardiology items had `Constrictive pericarditis / Tension pneumothorax / Pulmonary embolism`. Audit: `Counter(tuple(sorted(distractor_set)))` per chapter. Flag any chapter where the top set covers > 30% of items. Fix: `rotate_distractors_through_pool()` in the rebuilder — per-item deterministic hash offset in the chapter pool. See `references/chapter-distractor-pool-coverage.md` for the full snippet.

3. **Cross-topic distractor noise** — flat-merged pools mean an "Acute pancreatitis" item gets `Hemorrhoids / IBS / Ulcerative colitis` as distractors (those are in the Ch 22 default pool). Real differential for acute pancreatitis is the acute abdomen: `Choledocholithiasis / Duodenal perforation / Biliary colic`. Fix: `_resolve_distractor_pool()` that prefers `topic_keyword(title)` sub-pools, falls back to `topic_keyword(question)` when title is collapsed to "Topic", then chapter-level merged pool. See `references/chapter-distractor-pool-coverage.md`.

**Honest trade-off:** topic-keyword-aware rotation produces *fewer* distinct sets than flat-pool rotation (because sub-pools are smaller, e.g. 4–7 entries), but the distractors are clinically relevant. For MRCP exam quality, **topic-relevance beats distinct-set count**. Don't chase a higher distinct-set number if it comes from cross-topic noise — the lower number with topic-relevant distractors is the better number.

### Filling in the remaining chapter pools

When the user asks to "do the remaining chapters", add `DISTRACTOR_POOLS` entries for every chapter slug that doesn't already have one. Use the same per-area + `default` shape as the existing chapters. Coverage check after rebuild:

```python
import re
src = open('site/scripts/autogen_scenario_sbas.py').read()
m = re.search(r'DISTRACTOR_POOLS = \{(.+?)\n\}\n', src, re.S)
have = set(re.findall(r"^    '([0-9]{1,2}-[a-z\-]+)':\s*\{", m.group(1), re.M))
ALL = ['1-clinical-decision-making', ..., '32-older-adult-medicine-and-frailty']
missing = [c for c in ALL if c not in have]
print('still missing:', missing)  # must be []
```

After adding the missing pools and rebuilding, **every pas test autogen item in the live bank should now have real clinical alternatives**. The post-pass stat is `0/2,486 = 0.0%` placeholder distractors (verified via grep on the rebuilt JSON for the placeholder phrases).

Pitfall: `15-nephrology-urology` and `18-nephrology-urology` are **two separate pool keys**. The live chapters tree uses `18-nephrology-urology` (Davidson 24e real chapter); the legacy `15-nephrology-urology` slug is the old chapter. Both need pool entries, but only the published slug the chapters tree uses is what the rebuilder will resolve to. Quickest way: add the new chapter under both keys so the pool matches either slug.

Also: a small but real autogen bug leaks `Correct: B` (or `Answer: A`) into option A on a small number of items. Filter these in `quality_ok` before they reach the bank:

```python
if any(re.search(r'^\s*Correct:\s*[A-E]\b', v or '') for v in opts.values()):
    return False
if any(re.search(r'^\s*Answer:\s*[A-E]\b', v or '') for v in opts.values()):
    return False
```

This is a one-question-drop per pass but it makes the bank honest.

### UI spot-check after the JSON check passes

JSON counts matching is necessary but not sufficient. Open the actual exam/flashcards page and confirm:

```bash
# Browser-side: open /exam/ and /flashcards/ on the live port
# Pick a chapter with new content and read the first question
```

In `assets/exam-engine.js` the bank is loaded into `window.QUESTION_BANK` or equivalent (check the file). The expression `Object.keys(window.QUESTION_BANK?.sba || {}).length` should match the JSON length. If the engine loads from a different path, find the actual global and read its count.

Then pick a chapter with new PasTest content (e.g. 16-cardiology) and start an exam. The first SBA should be a real clinical scenario, not a templated "What is the most appropriate first-line therapy for [disease]?" fallback. If the UI shows the old count or templated content, the Service Worker is caching stale JSON — bump `sw.js` version and force-reload.

## Git Workflow — minimal stage, descriptive commit

```bash
cd "/mnt/tb/Sea-knowledge/#MedSea"
# Stage ONLY the rebuild artifacts, not random working-dir drift
git add site/scripts/rebuild_question_bank_v5.py \
        site/assets/questions-index.json \
        site/assets/questions-mcq.json \
        site/assets/questions-sba.json \
        site/assets/questions-flashcard.json

git commit -m "Rebuild question bank v5: handle 4 authoring formats, scan all *.md

- 4 question parsers: legacy bold-stem, plain-stem, inline Options/Answer, bullet-list
- 2 factoid parsers: stem-bullet-defs and stem+options-no-answer routed to flashcards
- Scan ALL *.md in chapters tree (was topic.md only — missed 868 files)
- Recognize '## 18. MCQs (10)' numbered headers and bare '## MCQs' headers
- Route MCQ blocks with no answer key to flashcards as Q/A pairs

Live bank after strict filter:
  MCQ      8177   (was 2754)
  SBA      2256   (was 1320)
  Flash   12082   (was 2814)
  Chapters   19   (was 16)

Honest gaps: 13 chapters still have ZERO authored MCQ/SBA/Flashcard
sections in their topic.md files. Empty: 1, 3, 4, 6, 8, 13, 21, 23, 25, 29, 30, 31, 32."

git push origin main
```

The commit message format with "Live bank: X → Y" and "Honest gaps" is exactly what past sessions showed the user accepts as trustworthy.

**When autogen is involved**, also stage the autogen script + only the chapter dirs the autogen touched (find by `Auto-generated study sections` marker in the file body). Don't stage unrelated chapter drift like `chapters/16-cardiology/...` from the build pipeline.

## Anti-patterns (do NOT do these)

| Anti-pattern | Why it's wrong |
|---|---|
| Auto-generate MCQs from clinical content ("Which of the following is the correct statement about X?") | User explicitly called these out as "junk", "1-word prompts", "no scenario". v3 of the extractor generated 19,489 such items and they were rejected. |
| Allow templated SBA stems ("What is the first-line treatment for [disease]?") | Same reason — stripped of scenario context. Blacklist the specific phrases (see CONTEXTLESS). |
| Include MCQ blocks with `answer=None` in the exam bank | Renders as "no correct answer" on screen. |
| Route MCQ blocks with `answer=None` to flashcards with `back=first_option` | Ships wrong clinical answers (e.g. GCA → "Migraine"). See the *Factoid Routing* section — drop them, don't rescue with option A. |
| Scan only `topic.md` files | Drops ~95% of authored content. Use `rglob('*.md')`. |
| Use `LEGACY_OPT_RE` that only matches `A.` (period) | Drops ch 31/32 source entirely (Format 6 with `A)` parens). Accept both `[.)]`. |
| Anchor table-derived flashcards to the section header instead of topic title | Produces nonsense like "What is the MELD of MELD-Na?". |
| Ship flashcards with `front` > 15 words | Fronts that long are MCQ vignettes misrouted to flashcards; almost always wrong. Drop them. |
| Skip the post-write autogen filter (pipe, generic distractors, label leak, vignette) | 497 broken MCQ + 989 broken flashcards in one rebuild. The filter is cheap; the broken cards are not. |
| Claim "all chapters complete" without per-chapter breakdown | User will demand "check files 1 by 1". Always list which chapters are empty. |
| Persist Docker image before verifying HTTP 200 on the live JSONs | A failed `docker cp` (perms, path) leaves the old bank live. Verify first, then commit. |
| **Claim "deployed + live verified" after running only the autogen step** | The autogen wrote to source .md files but the JSON bank and live container are unchanged. The user is then told a lie. Always complete the full 4-step cycle: autogen → rebuild → docker cp → verify. The verification script `scripts/verify_live_question_bank.sh` is non-skippable — its exit code is the truth. |
| **Forget to update `SRC_TO_PUB` in every autogen script when a new chapter family is added** | One generator may know the chapter and another may not. Symptom: chapter dir exists but live `questions-index.json` omits it or one surface (exam vs flashcards) stays blank. When adding a new source chapter mapping (e.g. `Diabetes -> 21-diabetes-mellitus`), patch **all** relevant generators and rerun them before rebuild. |
| **Leave scaffold / learning-objective text in flashcards after autogen** | Hub pages and intro prose can create junk cards like `Heading hub for ...` or `By the end of this note you should be able to...`. Add explicit flashcard filters for scaffold phrases and re-run the rebuild. |
| **Trust a chapter chip existing in source as proof the user can start an exam from it** | The UI is driven by `questions-index.json`, not the filesystem. A chapter can exist under `chapters/` and still be absent from the live setup if it contributes zero rows. Always browser-test: select the chapter → Available count changes → Start Exam enters the runner. |
| **Trust `grep "PasTest"` on the host as proof the live site has PasTest items** | Host source and live container are separate filesystems. Source has 1,879 PasTest topics, container has 0. The grep proves only that source is updated. To prove live, run `docker exec medsea grep -rl "PasTest" /usr/share/nginx/html/chapters/` — that's the live count. |
| **Report the autogen stdout ("1,879 topics, 4,275 SBAs") as the live state** | That number is what the autogen GENERATED, not what the live site SERVES. After autogen the live site still has the old bank until you re-run rebuild + docker cp. Report the live count from `verify_live_question_bank.sh`, not the autogen output. |
| **Skip `verify_live_question_bank.sh` because "the script worked last time"** | Each deploy is independent. The container may have restarted from a stale image. The script takes 5 seconds and exits non-zero on any mismatch. Run it. |
| Silently bulk-autogenerate "fill the gaps" for hundreds of topics | Always ask the user about scope/speed/quality tradeoff first. |
| Use `find_files()` from `build_site.py` to enumerate topics | That function only returns folder-based topic.md files. Many chapters use flat `*.md` files in `diseases/`. Use `rglob('*.md')`. |
| Add a new autogen script that writes a different `## H2` section without re-running the previous autogen | If the previous autogen wrote `## Flashcards` and your new one writes `## PasTest Scenario SBAs`, the topic now has only the new section. The flashcard count silently drops for that topic on next rebuild. Either: (a) make the new script also emit the old sections, (b) re-run the old autogen after, (c) explicitly add the old section header to the rebuilder's "section present" check so the old parser still runs. |
| Use module-level mutable caches across function calls in a long script | A `_published_cache: dict[str, dict]` populated once and reused across all chapters will silently serve stale data if the chapter slug map changes mid-run. Either pass the cache explicitly or clear it between phases. Symptom: 0 updates reported for a chapter that has matching topics (cache built before the slug was corrected). |
| Use `setdefault` to build a slug→path cache | First-wins silently masks collisions. ch 16 Cardiology has 907 published topics but 535 unique normalized keys — 329 are silently unreachable from a single source stem lookup. Add a duplicate-count warning at the end of cache build. |
| Assume H2 sections always have a non-empty body | `## Management` with no body of its own, followed by H2 sub-sections like `## A. General principles`, returns empty body. The section extractor returns "". When the next pattern wants a Management body, it gets "". The fix: when an H2 body is empty, also pull the next 3–5 H2 sub-sections into the combined body. |
| Run a single-script autogen that doesn't normalize H2 headers before joining | `gen_xx(full_text, ...)` patterns look for `^## .*MANAGEMENT` in the body. If you join section bodies with `'\n'.join(b for _, b in sections)` you lose the H2 headers — every section-aware pattern fails. Use `'\n'.join(f"## {h}\n{b}" for h, b in sections)` to preserve them. |
| **Reuse variable name `text` inside the PasTest option loop in `rebuild_question_bank_v5.py`** | `text = om.group(2)` overwrites the per-file markdown string. All later `extract_section(text, 'SBA Questions')` calls see garbage (~58 chars). Symptom: rich `## 20. SBA Questions` in source but zero SBAs in bank for that topic. **Fix:** `opt_text = om.group(2).strip()` only. |
| **`topic_label_from_path` uses `parts[i+1]` after `ch_slug` index** | With layout `chapters/<ch>/diseases/<topic>/topic.md`, `parts[i+1]` is the hub (`diseases`), so every item gets `topic_slug='topic'`. **Fix:** leaf dirname = parent of `topic.md`. |
| **Strict 12-word SBA `quality_ok` without PasTest-style whitelist** | Drops thousands of real short stems (`ABG: pH 7.20…`, `PCI not available within 2 h.`). Pair lower `min_stem_words` with expanded `pastest_style_ok()`. |
| **Claim "all answers correct" after JSON gates only** | Mechanical audit proves schema/scoring consistency, not clinical truth. Say what was checked; offer optional source re-parse sample. |
| **Exam UI hardcoded `['A','B','C','D']` only** | Bank has MCQ/SBA with answer **E** (27 items in one audit). Users cannot select E → always wrong. Render all non-empty `q.options` keys. See `references/exam-flashcard-mechanical-audit.md`. |
| **`data-showafter="0"` for “Each Q” toggle** | `exam/app.js` checks `SETUP.showAfter === 'each'`. Button with `data-showafter="0"` never enables per-question reveal — looks like a dead feature. |
| **`has_stub_wrong_options` with `len(opt)<=3` on all rows** | One session dropped **~8k** MCQ/SBA. **Autogen only**; require ≥2 bare-acronym wrong options; **never** apply `len<=3` to `source==authored`. |
| **Claim literal 10/10 all sectors** | Mechanical + deploy verification caps ~8–9 on bank/perf; **clinical accuracy 10/10** needs expert panel, not JSON gates alone. Product UX can reach ~9/10; teaching sector follows `index.quality` rationale %. |
| **Claim \\\"all answers include explanation\\\"** | Only items with `—` rationale in source get `explanation`; report SBA/MCQ/FC counts, not 100%. |
| **Claim \\\"all missing features shipped\\\"** | Use `site/docs/FEATURES.md` — cloud sync, OSCE, expert sign-off, 80% rationales remain content/process gaps. |
| **Topic `?topic=` exam/flashcard session slow** | Loader fetched monolith JSON because no chapter chip was set and/or shard cap was 15. Infer ch from slug, `SHARD_MAX=32`, prefetch + `topic-bank-index.json`. See `static-site-performance-optimization` → `references/topic-scoped-exam-flash-load.md`. |
| **Patch `exam-engine.js` without `showModal` before `window.MedSea`** | Accidentally closing IIFE early leaves orphan `showModal` body — `node --check site/assets/exam-engine.js` after edits. |
| **Deploy shards but directory gets `644` perms** | `tar` deploy of `questions-by-chapter/` followed by `find -type f -exec chmod 644` on host accidentally sets `644` on the **directory** too. nginx can't traverse → `try_files` serves `index.html` fallback (200 `text/html`) instead of JSON. Browser `fetch().then(r=>r.json())` fails with `Unexpected token '<'`. **Fix:** always `find -type d -exec chmod 755 {}` after `find -type f -exec chmod 644`. The `medsea_release_check.sh` now does both. |
| **Deploy JS/CSS but forget to include updated HTML** | Container still serves old `exam/index.html` without new `<script>` tags (e.g. `medsea-chapter-filter.js`, `exam-engine.js?v=17`). Browser loads only 4 scripts, `window.MedSea` false. **Fix:** tar deploy must include ALL changed files — HTML, JS, CSS, JSON — not just the asset you patched last. |
| **Audit script assumes `options` is a list, not a dict** | Live JSON stores `options` as `{"A": "text"}` (dict), NOT `["text1","text2"]` (list). Flashcards use `front`/`back`, NOT `question`. An audit script with `for o in opts` or `q.get('question')` on flashcards will report 100% false positives — every single item flagged. **Fix:** normalize to dict first, check `isinstance(opts, dict)` before iterating, use `front`/`back` for flashcards. |
| **Leave short abbreviation distractors ("PE", "MI", "DKA") in options** | 594 authored items have 2–3 char abbreviation options that look unprofessional in exam UI. **Fix:** `expand_abbrev_options()` in rebuilder — exact-match expansion only ("PE" → "Pulmonary embolism"). Never expand substrings. |
| **Run abbreviation expansion without a final dedupe pass** | Expanding `D:"PE"` and `E:"PE"` both to `"Pulmonary embolism"` creates duplicate options → release check fails. **Fix:** always follow expansion with a dedupe pass that suffixes non-answer duplicates (`(variant N)`). See the *Abbreviation expansion* section above. |
| **Leave dead code files on disk after refactoring** | `medsea-home-stats.js` was superseded by `medsea-header-stats.js` across all HTML includes but stayed on disk for weeks. **Fix:** `for f in assets/*.js; do grep -qr "$(basename $f)" --include='*.html' . || echo "DEAD: $f"; done` — delete unreferenced files. |
| **Subagent timeouts lose partial work** | 3 parallel `delegate_task` subagents all timed out at 600s, but each had completed 50-90% of their work (added functions, created files, patched CSS). **Fix:** check what each subagent actually produced before re-dispatching — `grep` for expected function names, `ls` for expected files. Finish the remaining work yourself rather than re-dispatching from scratch. |
| **Deploy without `?v=N` cache-bust on JS includes** | Deployed `exam-engine.js` with P0 `fmtDateTime` fix but HTML still had `?v=17` → browser served cached broken version. **Fix:** every time you bump SW version, also bump `?v=N` on all `<script src>` includes in HTML. |

## Mechanical exam + flashcard audit (user ask: "check all questions and answers")

When the user wants **format + display + answer-key consistency** across `/exam/` and `/flashcards/`:

1. Run `scripts/bank_mechanical_audit.py` on `site/assets/` (exit 0 = hard gates pass).
2. Compare `curl` live `questions-index.json` totals to on-disk JSON.
3. Patch/deploy `exam/app.js` if five-option items exist; verify option E renders.
4. Flashcards: confirm `front`/`back` via `textContent` fields — no pipe/wikilink placeholders post-filter.
5. Report honestly: mechanical PASS ≠ full clinical re-read of 26k items.

Full checklist and rebuilder pitfall detail: **`references/exam-flashcard-mechanical-audit.md`**.

### Bank schema — options are DICTS, flashcards use front/back (not question)

**The #1 false-positive in format audits:** the live JSON stores SBA/MCQ `options` as a **dict** `{"A": "text", "B": "text2"}`, NOT a list. Flashcards use `front`/`back` fields, NOT `question`. An audit script that assumes `options` is a list and checks `q.get('question')` for flashcards will report 100% false positives.

```python
# CORRECT schema-aware audit
opts = q.get('options', {})
if isinstance(opts, dict):
    opt_vals = list(opts.values())
    opt_keys = list(opts.keys())
elif isinstance(opts, list):
    opt_vals = opts
    opt_keys = [chr(65+j) for j in range(len(opts))]
else:
    opt_vals = []

# Flashcards:
front = q.get('front', '').strip()   # NOT q.get('question')
back = q.get('back', '').strip()
```

**Real format audit results (2026-06-27, 34,355 items):**
- 0 missing answers, 0 duplicates, 0 out-of-range, 0 empty options
- 594 items with short abbreviation distractors ("PE", "MI", "DKA" — under 3 chars)
- 1,022 autogen template stems (by design — filterable via Authored Only toggle)
- 3 items with generic autogen distractors
- Flashcards: 0 issues (all have front+back)

### Abbreviation expansion — `expand_abbrev_options()`

594 authored items had short abbreviation distractors ("PE", "MI", "DKA") that look unprofessional. Add a post-processing step in the rebuilder that expands common medical abbreviations **only when the option text is EXACTLY the abbreviation** (case-sensitive, not substring):

```python
ABBREV_EXPANSIONS = {
    'PE': 'Pulmonary embolism',
    'MI': 'Myocardial infarction',
    'DKA': 'Diabetic ketoacidosis',
    'CXR': 'Chest X-ray',
    'CT': 'CT scan',
    'MRI': 'MRI scan',
    'AF': 'Atrial fibrillation',
    'VT': 'Ventricular tachycardia',
    'VF': 'Ventricular fibrillation',
    # Skip: ECG, ESR, COPD — common enough standalone
    # Skip: "No", "Sepsis" — valid short options
}

def expand_abbrev_options(opts: dict) -> dict:
    return {k: ABBREV_EXPANSIONS.get(v.strip(), v) for k, v in opts.items()}
```

Call this right before writing items to the bank JSON. Only expands exact matches — never touches `"PE is suspected"` or `"MI with shock"`.

**Critical: abbreviation expansion can create duplicate options.** If an item had `D: "PE"` and `E: "PE"` (both bare abbreviations as distractors), expanding both to `"Pulmonary embolism"` produces two identical options — the release check will flag them as duplicates. Always run a **final dedupe pass** after expansion:

```python
# Final dedupe pass — suffix non-answer duplicates
for r in sba + mcq:
    opts = r.get('options') or {}
    vals_lower = [str(v).strip().lower() for v in opts.values()]
    if len(vals_lower) == len(set(vals_lower)):
        continue  # no dups
    ans = str(r.get('answer') or '').upper()
    seen: set[str] = set()
    for k in list(opts.keys()):
        v = str(opts[k]).strip()
        if v.lower() in seen and k != ans:
            idx = 2
            candidate = v
            while candidate.lower() in seen:
                candidate = f'{v} (variant {idx})'
                idx += 1
            opts[k] = candidate
            seen.add(candidate.lower())
        else:
            seen.add(v.lower())
```

Never suffix the correct answer — only distractors.

### Three-way parallel subagent dispatch for gap-filling

When the user asks to "fill all gaps and make it 10/10", the work spans rebuilder patches, design polish, PWA/DevOps — all independent. Dispatch 3 `delegate_task` subagents in parallel:

| Subagent | Scope | Toolsets |
|----------|-------|----------|
| 1 | Rebuilder: abbreviation expansion + rationale backfill to 80%+ | `terminal`, `file` |
| 2 | Design: mobile drawer, chip spacing, lazy topic list, shard prefetch, critical CSS | `terminal`, `file`, `browser` |
| 3 | PWA+DevOps: SW v18 (skipWaiting, precache shards), SW update toast, git hooks, pytest venv, deploy script | `terminal`, `file` |

**Constraint:** subagents save files locally only — do NOT deploy to the container. The parent session does the final rebuild + deploy + browser verify after all 3 return.

### Dead code removal — check for superseded files

When refactoring, check for files that were superseded but never deleted. Example: `medsea-home-stats.js` was replaced by `medsea-header-stats.js` across all HTML includes, but the old file stayed on disk for weeks. Quick check:

```bash
# Find JS files that exist but aren't referenced in any HTML
for f in assets/*.js; do
  base=$(basename "$f")
  grep -qr "$base" --include='*.html' . || echo "DEAD: $f"
done
```

### Rationales (`explanation` field) — exam + flashcards

**Exam:** `explanation` parsed from `**Answer: X** — …` in authored blocks; shown in **result review** and when **Show after: Each Q** after the user picks an option. **Flashcards:** `back` = answer; optional `explanation` from `A: ans — rationale` or topic-level copy from MCQ/SBA on same `topic_slug`.

**Do not claim \\\"every question has an explanation\\\"** — report `index.quality` after rebuild (see **`references/explanations-and-rationales-2026-06.md`**). Backfill from correct-option text raises MCQ/SBA % materially; **80%** still needs explicit `—` lines — use `chapters_needing_rationales.py` + `suggest_rationale_stubs.py` in repo `site/scripts/`, then rebuild + deploy.

### Flashcard back→explanation enrichment (FC 53% → 85%+)

Flashcards have a `back` field (the answer text) but often no `explanation`. The `enrich_flashcards_from_topic_qa()` function copies MCQ/SBA rationales onto flashcards by matching `(chapter_num, topic_slug)` — but if the topic has no MCQ/SBA rationales either, FC coverage stays flat.

**Additional pattern: extract rationale from the flashcard's own `back` text.** Many authored flashcard backs contain the answer AND a rationale separated by `→` or `:`:

```
back: "PaCO₂ = 1.5 × HCO₃⁻ + 8 ± 2"
back: "Biphasic response: initial Th2 dominance → Th1 conversion drives granuloma formation"
```

Extract the text after `→` or `: ` as the explanation:

```python
for fc in flash_rows:
    if (fc.get('explanation') or '').strip():
        continue
    back = (fc.get('back') or '').strip()
    if back:
        if ' → ' in back:
            after = back.split(' → ', 1)[1].strip()
            if len(after) >= 10:
                fc['explanation'] = after[:500]
                fc['explanation_source'] = 'back_arrow'
                continue
        if ': ' in back:
            after = back.split(': ', 1)[1].strip()
            if len(after) >= 12:
                fc['explanation'] = after[:500]
                fc['explanation_source'] = 'back_colon'
                continue
    # Fallback: topic-level MCQ/SBA rationale
    cands = pool.get((fc['chapter_num'], fc['topic_slug'])) or []
    if cands:
        fc['explanation'] = max(cands, key=len)[:500]
        fc['explanation_source'] = 'topic_qa'
```

**Measured impact (2026-06-27):** FC coverage jumped from **53.5% → 85.3%** with this pattern. The `→` separator catches clinical reasoning chains; `: ` catches label-definition pairs.

### Post-rebuild filters (2026-06-24)

After flash dedup, `main()` must:

1. **Drop definition-bullet stems** via `is_definition_autogen_stem()` — `presents with: Definition` or `A patient with suspected … Clinical features —` (all sources, not only `pastest-autogen`).
2. **Recompute `mcq_count` / `sba_count` / `flashcard_count`** on every chapter in `questions-index.json` from the final lists (not only flashcard counts — stale index breaks Available counts).
3. **Write per-chapter shards** to `site/assets/questions-by-chapter/{num}-{mcq|sba|flashcard}.json` and set `index.shards.pattern` so exam/flashcards can load 1–6 chapters without parsing 14 MB monoliths.

## References

- `references/rationale-coverage-report-explained.md` — Understanding and using `rationale_coverage_report.py`
- `references/medsea-live-bank-rebuild-and-backfill-2026-06.md` — The v5 rebuild pipeline and explanation backfill system
- `references/final-audit-and-same-topic-dedupe-2026-06.md` — **NEW:** Comprehensive format validation (30k+ items), same-topic deduplication (dropped 3,304 dupes), improved autogen filter (dropped 142 bad items), multi-sector rating framework (code/bank/UX/performance/clinical), honest 10/10 ceiling reporting, and production-readiness checklist. Use when user asks for "10/10 rating", "audit everything", "fill all gaps", or final QA before release.
- `references/explanations-and-rationales-2026-06.md` — exam `explanation` parsing, flashcard back vs rationale, coverage honesty, UI surfaces
- `references/exam-flashcard-mechanical-audit.md` — mechanical gates, answer-E UI bug, PasTest `text` shadowing, topic_slug pitfall
- `references/exam-ui-exam-prep-features-2026-06.md` — topic filter, authored-only, MRCP mock, URL params, modals, weak queue
- `references/study-ux-bookmarks-reports-export-2026-06.md` — bookmarks, report wrong Q, export JSON, home stats, topic bar
- `references/medsea-product-sector-ratings.md` — full MedSea product audit rubric (/10 per sector, missing features, tar deploy); lives under `medsea-chapter-audit` skill dir — load that reference when user wants ratings not just bank gates
- `references/authoring-formats.md` — full worked examples of all 6 formats with expected parser output and edge cases
- `references/autogen-from-authored-content.md` — pattern + scripts for filling chapters that have prose but no study sections (the 2026-06-22 v6 work). 1 flashcard-from-table + 1 definition-MCQ + 1 generic-SBA per topic. Honest caveats: distractor quality is weak.
- `references/diabetes-mapping-and-scaffold-filter.md` — chapter-mapping failure mode (`Diabetes -> 21-diabetes-mellitus`), how it causes chapters to vanish from the live index, and scaffold-card filters that removed hub / learning-objective junk from flashcards.
- `references/pastest-scenario-sba-pattern.md` — PasTest/Mediscope-style clinical vignette SBAs built from REAL clinical facts (triads, specific features, trial names, first-line drugs) extracted from authored source. 5 pattern extractors + curated chapter-specific distractor pools. Replaces the generic-distractor approach with plausible real alternatives.

## Scripts

- `scripts/rebuild_question_bank_v5.py` — full pipeline: scan → parse 6 formats → strict filter → factoid-route → write 4 JSONs. Run from `/mnt/tb/Sea-knowledge/#MedSea`. Print per-chapter breakdown + quality stats.
- `scripts/autogen_scenario_sbas.py` — generate PasTest/Mediscope-style clinical scenario SBAs from authored source. Writes `## PasTest Scenario SBAs` to published tree. See `references/pastest-scenario-sba-pattern.md`.
- `scripts/verify_live_question_bank.sh` — the deploy verification gate. Compares local JSON, container JSON, and HTTP-served JSON. Exits non-zero on any mismatch. **Run after every autogen + deploy. Non-skippable.** See the *Deploy Verification Gate* section above.
- `scripts/bank_mechanical_audit.py` — structural gates (duplicate options/IDs, index drift, flashcard junk). Run after every rebuild; does not replace clinical spot-checks.
- `scripts/verify_medsea_bank.py` — index↔disk↔shard count parity; invoked automatically at end of `rebuild_question_bank_v5.py` when present under `site/scripts/`.
- `scripts/medsea_release_check.sh` — pre-deploy gate (verify + index `quality` + rationale report). **Run before every tar/docker deploy.**
- `scripts/rationale_coverage_report.py` — SBA/MCQ/FC explanation % vs 80% target.
- `scripts/sample_authored_answer_audit.py` — random authored SBA vs `**Answer:**` in `/mnt/tb/Medicine/.../topic.md`.
- `scripts/install_git_hooks.sh` — optional pre-push hook → release check.
- Repo `site/scripts/chapters_needing_rationales.py` — ranked chapter gaps for content sprint.
- Repo `site/scripts/suggest_rationale_stubs.py` — paste-ready `**Answer: X** —` from bold correct options.
- Repo `site/scripts/medsea_weekly_quality.sh` — weekly rationale % + top chapters (cron-friendly).
- Repo `site/scripts/build_topic_bank_index.py` — fast rebuild of `topic-bank-index.json` after bank JSON changes (topic counts without monolith load).
- Repo `site/scripts/deploy_medsea.sh` — one-command deploy: `bash scripts/deploy_medsea.sh --yes` → release check + index + tar + perms. Dry-run without `--yes`.
- Repo `site/assets/sw-update.js` — SW update toast notifier; include on all pages via `<script src="/assets/sw-update.js"></script>`.
- Repo `site/assets/chapter-topic-lazy.js` — "Load more (N topics)" pagination for 900+ link chapter sidebars.
- Repo `site/assets/critical.css` — above-the-fold CSS inlined in `index.html` for fast first paint.
- **`static-site-performance-optimization`** → `references/pwa-sw-v18-and-lazy-load-2026-06.md` — SW v18 skipWaiting/clients.claim/precache shards, update toast, lazy-load, critical CSS, shard prefetch, one-command deploy script.

## Release ops (tar deploy, quality index, weak queue)

When `docker build` times out on large `site/`, sync with **tar into running container** + nginx reload + **644/755** perms. Gate with `medsea_release_check.sh`. Full checklist: **`references/release-ops-and-quality-gates-2026-06.md`**.

Post-rebuild `questions-index.json` includes **`quality`** (rationale %, autogen counts). Exam setup displays it; do not claim 10/10 teaching sector without reporting these numbers.

**Weak queue:** `MedSea.Flagged` in `exam-engine.js` — missed items on submit; manual flag in review; **Weak queue only** filters pool by flagged IDs.

**Bookmarks / reports / export:** `MedSea.Bookmarks`, `MedSea.Reports`, `downloadStudyExport()` — see **`references/study-ux-bookmarks-reports-export-2026-06.md`**. Full shipped feature list: repo `site/docs/FEATURES.md`.

**Header live stats:** `assets/medsea-header-stats.js` on `/`, `/exam/`, `/flashcards/` — MCQ/SBA/FC counts, hubs/topics, SBA rationale %, unified search placeholder. Design polish: **`static-spa-library-site`** → `references/header-design-polish-2026-06.md`.
