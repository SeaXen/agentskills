# PasTest/Mediscope-Style Scenario SBA Pattern

## Why a new pattern, not the v6 autogen

The v6 autogen (`autogen_study_sections.py`, see `autogen-from-authored-content.md`) produces 1 flashcard from tables + 1 definition-MCQ + 1 generic-SBA per topic. It's good for "fill the gap" with study material, but the SBAs it produces are weak as exam practice:

- Stem: "A patient with suspected X presents with: ... What is the most likely diagnosis?"
- Distractors: "A condition that mimics X", "A complication of X", "An unrelated condition"
- Answer: always the topic title

A real MRCP/FCPS-style SBA tests a **specific clinical fact** extracted from the topic and offers **plausible real alternatives** as distractors. The PasTest pattern extracts those specific facts and pairs them with curated chapter-specific distractor pools.

## The 5 pattern extractors

Each extractor scans a topic's H2 sections and yields one SBA when the pattern is found and the answer is grounded in the source text. They're tried in priority order; the first hit for each topic is used.

### 1. Triad recognition — "Which condition is characterised by A, B, C?"

Match patterns:
- `**Beck's triad**: (hypotension, JVP, muffled heart sounds)` → stem uses the items, answer = topic
- `**Triad**: (fever, rash, arthritis)` → stem uses the items
- Generic: `**X**: (A, B, C)` followed within 200 chars by `triad` or `pathognomonic`

Output: "Which of the following is characterised by the clinical triad: A, B, C?" with 4 options where A = the topic title, B/C/D = 3 real conditions from the chapter's curated distractor pool (e.g. for cardiology: constrictive pericarditis, tension pneumothorax, PE, aortic dissection).

Quality bar: ≥3 items in the list, each ≥3 chars and ≤60 chars, no item is a generic word like "etc" or "other".

**This is the highest-yield extractor** — triads (Beck's, Cushing's, Charcot's, Whipple's) are heavily tested in MRCP PACES and FCPS viva. Tamponade topic with this pattern produces 3-5 SBAs from a single source.

### 2. Specific feature — "Which is specific/characteristic/pathognomonic of X?"

Search Clinical Features / Investigations / Mnemonics / Pitfalls / Differential sections. Match `**bold feature** ... specific|characteristic|pathognomonic|hallmark|diagnostic|key|typical|distinctive`.

Output: "Which of the following features is most specific or characteristic of {topic_title}?" with the bold feature as the answer and 3 generic-but-plausible distractors.

Real example from asthma topic: "**Diurnal PEF variability >20%**" — actual GINA diagnostic criterion, the question is real MRCP-grade content.

### 3. Avoid / contraindicated — "Which of the following should be avoided in X?"

Search Management / Complications / Pitfalls / Special Populations / Drug Interactions sections. Match `avoid|do not use|contraindicated|caution|should not|careful|never` followed by a drug and a clinical context.

Output: "In the management of {topic_title}, which of the following should be avoided (or is contraindicated)?" with the drug as the answer, 3 generic safe-option distractors.

Real example from pericarditis: "**Avoid corticosteroids in idiopathic/viral** (COPE, CORP — increase recurrence)".

Filter on the drug name: skip words like "caution", "drug interactions", "contraindications", "general", "principles", "framework", "section", "chapter", "reference", "see", "box" — these are header words, not drugs.

### 4. Trial recall — "Which trial showed X in condition Y?"

Match `[A-Z][A-Z0-9\-]{1,8} trial` (must be all-caps, not a common medical acronym like NSAID/ICU/CXR). Then look for a finding within ~200 chars: `showed|demonstrated|found|established|confirmed`.

Output: "Which landmark clinical trial provided evidence relevant to the management of {topic_title} (specifically: {finding})?" with the trial name as the answer.

Real example from DVT topic: "CASSINI trial" — actual NEJM 2019 rivaroxaban thromboprophylaxis trial.

### 5. First-line management — "What is the first-line therapy for X?"

Search the Management section. Look for the first sentence/bullet that:
- Contains a bold drug/therapy name (`**DrugName**` or `**DrugName (dose)**`)
- Mentions a clinical context (`for|in|as|with|treat|manage|step|controller|first|initial`)
- Is a positive indication, not "avoid X"

If bold drugs are found: extract up to 2 distinct drug names, join with `+`.
If no bolds found: use the first full sentence from the section (truncated to 120 chars) — useful when the section is bullet-style prose.

Output: "What is the most appropriate first-line therapy for {topic_title}?" with the drug(s) as the answer, 3 generic alternatives.

Real examples:
- Pericarditis: "NSAIDs + colchicine" (COPE, CORP trials)
- COPD acute exacerbation: "Systemic corticosteroids"
- Pneumonia: "give oxygen if hypoxemic" (sentence fallback)
- Asthma: bullet picker fails on tables → 0 SBAs from this pattern (other patterns compensate)

## The distractor pool (chapter-specific)

**The single most important design choice.** Generic distractors ("a condition that mimics X") produce low-quality SBAs. Curated chapter-specific pools of REAL alternative conditions produce high-quality SBAs.

The pool is keyed by `(chapter_slug, topic_keyword)` where `topic_keyword` is derived from the topic title (e.g. "tamponade", "acs", "copd", "pneumonia"). If no specific keyword matches, fall back to `chapter_slug → "default" → GENERIC_DISTRACTORS`.

Example pool for `16-cardiology`:
```python
DISTRACTOR_POOLS['16-cardiology'] = {
    'tamponade':     ['Constrictive pericarditis', 'Tension pneumothorax',
                      'Pulmonary embolism', 'Aortic dissection'],
    'acs':           ['Stable angina', 'Aortic dissection', 'Pericarditis',
                      'Pulmonary embolism'],
    'heart_failure': ['COPD exacerbation', 'Pulmonary embolism',
                      'Cardiac tamponade', 'Constrictive pericarditis'],
    'af':            ['Atrial flutter', 'AVNRT', 'Atrial tachycardia',
                      'Frequent atrial ectopy'],
    'default':       ['Hypertensive heart disease', 'Ischaemic heart disease',
                      'Valvular heart disease', 'Cardiomyopathy'],
}
```

Curated pools exist for: 10-acute-medicine, 11-poisoning, 15-nephrology-urology, 16-cardiology, 17-respiratory-medicine, 18-nephrology-urology, 20-endocrinology, 22-gastroenterology, 23-hepatology, 24-haematology, 25-rheumatology, 26-dermatology, 27-neurology, 28-ophthalmology, 29-psychiatry, 30-maternal, 8-oncology, 4-immunology, 14-infectious-disease, 9-palliative, 12-envenomation. The script falls back to GENERIC_DISTRACTORS for chapters without curated pools.

The pools are 4-condition sets; the script uses the first 3 as distractors. If the topic title matches the first distractor (e.g. topic = "Heart failure", distractor A = "Heart failure"), swap to a different distractor.

## The published-tree matcher (5 layouts, must handle all)

The hardest part of the script. MedSea's published tree has at least 5 layouts:

| Layout | Example |
|---|---|
| Folder + topic.md | `diseases/16.7.48-tamponade-physiology/topic.md` |
| Folder + named .md | `diseases/18.1.3-investigation-renal-urinary-tract-disease/investigation-renal-urinary-tract-disease.md` |
| Direct .md in diseases/ | `diseases/17.1.14-abg-interpretation.md` |
| Numbered prefix on folder | `diseases/16.2.251-anticoagulation-in-pregnancy/` (2+ digit subsections) |
| `_full` suffix duplicates | `Atherosclerosis_pathogenesis.md` and `Atherosclerosis_pathogenesis_full.md` both map to the same published topic |

Matcher rules:
1. **Normalize** the slug: strip `^[\d.]+-?` prefix, strip parentheticals, strip common suffixes (`_full`, `_notes`, `_draft`, `_final`, `_complete`, `_short`, `_extended`, `_summary`), lowercase, drop non-alphanumerics, collapse whitespace. Result is a key.
2. **Build a cache** of `clean_key → Path` from the published tree, supporting all 3 modes (topic.md, named .md in folder, direct .md).
3. **Lookup** the source topic's normalized key in the cache. Exact match wins.
4. **Jaccard fallback**: if no exact match, find the cache entry with highest token Jaccard similarity. Threshold 0.7 — below that, give up.
5. **First-wins setdefault** is acceptable (collisions are usually `_full` vs non-`_full` versions of the same topic pointing to the same published file).

## Source-tree mapping (`SRC_TO_PUB`)

```python
SRC_TO_PUB = {
    'Cardiology':                     '16-cardiology',
    'Hepatology':                     '23-hepatology',
    'Hematology':                     '24-haematology-and-transfusion-medicine',
    'Respiratory':                    '17-respiratory-medicine',
    'Nephrology and Urology':         '18-nephrology-urology',  # NOT 15
    # ...
}
```

**Watch for: ch 15 vs ch 18 nephrology.** The published tree has `15-nephrology-urology/` (1 file, legacy) AND `18-nephrology-urology/` (53 files, the real one). Source `Nephrology and Urology/` maps to `18-nephrology-urology`.

`Poisoning` AND `Chapter 7 - Poisoning` both exist; only `Chapter 7 - Poisoning` has the real content.

## Section detection pitfalls

The pattern extractors look for specific H2 sections (Management, Clinical Features, Mnemonics, etc.). Three traps:

### 1. `## Management` with empty body, followed by H2 sub-sections

```markdown
## Management
## A. General principles
- give oxygen if hypoxemic
## B. Specific therapies
- Drug X for Y
```

A naive section extractor returns empty body for "## Management". The fix: if the matched H2 body is empty, also pull the next 3–5 H2 sub-sections into the combined body.

### 2. Headers lose their H2 marker when section bodies are joined

```python
# WRONG: H2 headers lost
full_text = '\n'.join(b for _, b in sections)
# Section-aware patterns (looking for '## MANAGEMENT') all fail

# RIGHT: preserve H2 markers
full_text = '\n'.join(f"## {h}\n{b}" for h, b in sections)
```

### 3. Section name variations

- `## 6. MANAGEMENT ALGORITHM` (numbered + suffix)
- `## A. General principles` (lettered sub-section)
- `## Management` (bare)
- `## Drug Details Table` (looks like management but is a table)

The `_find_mgt_section` helper must match `management|treatment|therapy|rx` in the header (case-insensitive), not require exact match.

## Bullet vs sentence style for first-line

The first-line extractor needs both modes:

**Sentence style** (e.g. pericarditis): "**NSAIDs** (ibuprofen 600-800mg TDS, aspirin 750-1000mg TDS, indomethacin) + **colchicine 0.5mg BD** (1-3 months) for first episode and recurrence."

- Split on `[.!?]\s+` and `(?<=\n)\s*`
- Keep the first sentence that contains a bold drug + a positive indication (`for|in|as|with|treat|manage|step|controller|first|initial`)
- Extract bold drug names, strip dose in parens

**Bullet style** (e.g. pneumonia): "## A. General principles - give oxygen if hypoxemic - start empiric antibiotics promptly"

- Walk bullet lines, keep the first with a treatment verb (`start|give|use|prescribe|administer|empiric|treat|cover|choose|therapy|antibiotic`)
- If no bold drugs, use the full bullet line truncated to 120 chars

**Table style** (e.g. asthma): "## Chronic (Stepwise, GINA 2024 Track 1 preferred) | Step | Controller | Reliever | ... "

- Replace `|` with space to flatten
- Use sentence mode
- If first column header is "Step" and content is drug regimens, pick the first row's controller drug

## Module-level cache pitfall

If the autogen script uses a module-level cache (e.g. `_published_cache: dict[str, dict[str, Path]]`) and runs across multiple chapters in a loop, the cache from chapter N persists into chapter N+1. If the chapter slug map changes mid-run (e.g. you fix `15-nephrology-urology` → `18-nephrology-urology`), the OLD slug is still in the cache with stale data.

Fix: either clear the cache between chapters (`cache.clear()`), or make the cache keyed by absolute path / by re-computing each chapter. Symptom: 0 updates reported for a chapter that has matching topics, even though the matcher works in isolation.

## Re-run safety

The script appends `## PasTest Scenario SBAs (Clinical Vignettes)` to the published `topic.md`. Re-runs detect the existing section and skip. Safe to re-run after re-fixing the matcher, adding new distractor pools, or improving pattern extractors.

## The flashcard drop regression (LESSON LEARNED)

The previous autogen (`autogen_study_sections.py`) wrote `## MCQs (N generated)`, `## SBA Questions (N generated)`, `## Flashcards (N generated)` to the END of each topic. The new PasTest autogen writes only `## PasTest Scenario SBAs (Clinical Vignettes)` to the END. **A topic that previously had all 4 sections now has only the new one.**

On next rebuild, the v5 parser:
1. Section-check: any of `## MCQs / ## SBA / ## Flashcards / ## PasTest` → continue
2. Extract flashcards from `## Flashcards` section → MISSING for topics that only got the PasTest autogen
3. Result: flashcard count drops by ~50% (8,500 cards lost in the 2026-06-23 session)

**Two fixes:**

1. **Make the new autogen emit all 4 sections** in one pass (best — no drift between autogen runs).
2. **After running the new autogen, also re-run the old autogen** to re-add the missing sections.
3. **Or update the rebuild script to ALSO check for the PasTest section in its section-presence check** (done in v5 already) AND modify the autogen to emit the missing `## Flashcards` placeholder from the topic's actual flashcards (if any).

The cleanest fix is (1) — single combined script. The session ended with option (2) being the recommended follow-up.

## What goes in the live bank

The v5 rebuild script's new section parses `## PasTest Scenario SBAs (Clinical Vignettes)` blocks and adds them to `questions-sba.json` with `source: pastest-autogen`. The question bank gets real PasTest-style SBAs without manual authoring.

If a PasTest block has no `> **Answer: X**` line, the parser skips it (no answer → no honest SBA). If the options are not exactly A/B/C/D, the parser skips it. Quality gate is strict.

## Script

The full implementation is at `scripts/autogen_scenario_sbas.py`. Key design:

- 5 pattern extractors, each returns `{stem, options, answer, source_quote}` or None
- Per-topic loop tries patterns in priority order, takes the first N hits
- Output formatted as a markdown block with **Q1.** stems, A/B/C/D bullet options, and `> **Answer: X** — explanation` at the end
- Source quote is preserved inline for traceability

## Future work

1. **Investigation SBA pattern** (currently missing). Match "first-line investigation: echo" or "diagnosis requires CXR/biopsy/..." → "First-line investigation for X?"
2. **Score interpretation pattern**. Match "CURB-65 ≥3 = admit" or "Wells >6 = high risk" → "A patient has score X. What does this mean?"
3. **Red flag pattern**. Match "red flag features: A, B, C" → "Which is a red flag for X?"
4. **Combined single-script autogen** that emits MCQ + SBA + Flashcards + PasTest in one pass to fix the flashcard-drop regression
