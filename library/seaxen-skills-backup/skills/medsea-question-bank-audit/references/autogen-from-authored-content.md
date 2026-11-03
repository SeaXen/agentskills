# Autogenerating Study Sections from Authored Topic Content

When chapters have authored prose (`## Definition`, `## Clinical Features`, drug/regimen tables) but **no** `## MCQs / ## SBA Questions / ## Flashcards` sections, you can fill the gap by walking the source topics and appending generated study sections to the published tree.

This is the pattern used by `site/scripts/autogen_study_sections.py` (10 chapters filled, 582 topic files updated, ~6,700 additional flashcards + ~3,400 additional MCQs to the live bank in 2026-06-22).

## When to use autogen vs hand-authored

| Situation | Use autogen? |
|---|---|
| Chapter has substantive authored prose + drug/regimen tables + clear definition blockquotes | **Yes** — high yield, low risk |
| Chapter has only stubs / hub-and-spoke MOCs | **No** — no source to anchor on, would be fabrication |
| Chapter has authored MCQs without answer keys | **No** for MCQ (would have to guess); **Yes** for flashcards (rescue as Q→first option) |
| Chapter has no source folder at all (`/mnt/tb/Medicine/<name>` missing) | **No** — user must author Davidson content first |

Always be **explicit** in the summary about which chapters got autogen vs which need hand-authored source. User pattern from past sessions: silently filling half and reporting "complete" gets challenged with "check files 1 by 1".

## The three sub-parsers (in priority order)

### 1. Flashcards from "good" 2-col reference tables

Tables look like:

```
| Drug         | Dose                          |
| Azathioprine | 1-2 mg/kg/day (Start 50mg)    |
| Budesonide   | 9 mg/day (non-cirrhotic only)  |
```

Each row becomes `What is the {label} of {topic_title}?` → answer = col2.

**Required table quality filters (the autogen script enforces these):**

- **2 columns only** (not 3+ wide reference tables)
- **Col 1 is a short label** (≤ 8 words). If it's a sentence, it's not a "drug row", skip.
- **Col 2 is substantive** (≥ 3 words). Single-word cells like "Absent" / "Present" for "Compensated vs Decompensated" comparison tables must be rejected — they have no semantic meaning in isolation.
- **Col 1 header must be a noun** like Concept, Drug, Regimen, Treatment, Investigation, Sign, Feature, Criterion, Cause, Risk Factor, Complication, Side Effect, Indication, Contraindication, Monitoring, Test, Mechanism, Dose, Agent, Medication.
- **Col 1 header must NOT be** Aetiology, Etiology, Compensated, Decompensated, Stage, Phase, Time, Day, Severity, Grade, Class — these are comparison-table headers, not drug/concept rows.
- **Skip meta/review tables by header keyword**: `FCPS/MRCP High-Yield Summary`, `Viva Questions`, `Mind Map`, `One-Page Revision Card`, `Spaced Repetition Tracker`, `Self-Test Scorecard`, `Confusions & Mnemonics`, `Quick Recap`. These duplicate the per-row tables already mined.

**Critical: anchor questions to the overall topic title, NOT the table's section header.**

```python
# WRONG:  Q: "What is the MELD of MELD-Na?"
# (the topic_title is the chapter/topic, not the section header)
# RIGHT:  Q: "What is the MELD of cirrhosis?"
```

Pass `topic_title=topic_title` into `make_flashcards_from_table()` and use it as the topic context.

### 2. Definition-based MCQs (1 per topic)

Look for a blockquote definition in this priority:

1. `> **Histological Definition**: ...` (most reliable — Davidson-style authored topics)
2. `> **Clinical Definition**: ...`
3. First meaningful sentence (after stripping frontmatter / checkboxes / wikilinks / `---` dividers / `## H` headers / `| ... |` table separators)

Build: `Which of the following best describes {topic_title}?` → correct = the definition, distractors = generic ("an unrelated condition...", "a complication late in the disease course...", "a condition that mimics...").

**Limit to 1 MCQ per topic.** Generating multiple definition-MCQs from the same body gives the same Q with the same A — boring and inflated.

### 3. SBAs (1 per topic)

Look for clinical features section (`## Clinical Features`, `## Clinical`, `## Presentation`, `## Definition`, `## Classification`, or `## Aetiology`).

Extract 2–3 fact bullets. **Skip lines that look like definitions** (`**...Definition**: ...`) — they're not clinical features, they're definitions. The autogen script skips any line containing "definition" + `:` or "is" in first 30 chars.

Build: `A patient with suspected {topic_title} presents with: F1; F2; F3. What is the most likely diagnosis?` → correct = `{topic_title}`, distractors = category-adjacent ("a condition that mimics...", "a complication of...", "an unrelated condition...").

**Pitfall:** if features section is mostly raw table syntax like `| Aetiology | Features |`, the SBA scenario reads like garbage. Either filter table rows out of the features pull or pre-detect that the section is a table and skip.

## The slug matcher — biggest source of bugs

Source tree layout and published tree layout **do not match**:

| Source | Published |
|---|---|
| `Medicine/Hepatology/Autoimmune Liver Disease/AIH treatment.md` (folder/topic.md) | `chapters/23-hepatology/diseases/23.1.21-aih-treatment/topic.md` |
| `Medicine/Clinical Immunology/3.4 Autoimmune Diagnostics.md` (flat file) | `chapters/4-clinical-immunology/diseases/4.3.04-autoimmune-diagnostics.md` (flat file in diseases/) |
| `Medicine/Medical Psychiatry/Anxiety and Stress-Related Disorders.md` (flat) | `chapters/29-medical-psychiatry/diseases/29.0.1-anxiety-and-stress-related-disorders/topic.md` (folder) |

The matcher needs:

1. **Walk both `topic.md` files AND direct `*.md` files** in the published tree (some chapters use flat files in `diseases/`, others use folder/topic.md).
2. **Strip numeric prefix from BOTH sides** (`23.1.21-aih-treatment` → `aih-treatment`).
3. **Exact-match first** (after numeric-prefix strip).
4. **Jaccard-token fallback** ≥ 0.6 for the rest. Split slug into tokens; score = intersection / union.
5. **Skip MOC/hierarchy/roadmap files** by name pattern — they match many things.

Without the direct-`*.md` walk, ch 4 and ch 8 silently matched ZERO files (they use flat `.md` files in `diseases/`, not `topic.md` folders).

## Quality gating before commit

After autogen + rebuild:

```bash
python3 site/scripts/rebuild_question_bank_v5.py 2>&1 | tail -20
```

Print **per-chapter breakdown + quality stats** every time:

```
Totals: {mcq: 11603, sba: 2581, flashcard: 18824, chapters: 27}
Quality stats:
  MCQ      : {one_option: 0, missing_answer: 0, ...}
  SBA      : {one_option: 0, missing_answer: 0, ...}
  Flashcard: {no_question_mark: 0, short_front: 426, ...}
```

If `one_option > 0` or `missing_answer > 0`, **something is wrong with the parser** — investigate before shipping.

## Honest caveats to surface to user

1. **Autogen flashcards are good** (real Q→real A from authored text).
2. **Autogen MCQs are definition-based only** (1 per topic) — teach the definition, not exam-style clinical reasoning.
3. **Autogen SBAs use generic category-adjacent distractors** ("a condition that mimics X") — useful as study material, weak as MRCP/FCPS practice.
4. **Chapters with no source content** (1, 3, 6, 13, 21 in 2026-06-22) **cannot be filled by autogen** — user must author Davidson disease topics first.
5. **Chapters where source MCQs lack answer keys** (ch 20 endocrinology) — autogen routes them to flashcards, not to MCQs. A future pass can hand-curate the answer keys.

## Commit hygiene

The autogen pass creates `M chapters/<N>/diseases/.../topic.md` for every file modified. Stage **only the chapters the autogen actually touched** (find by `Auto-generated study sections` marker in the file body), plus the script + JSON outputs:

```bash
git add site/scripts/autogen_study_sections.py \
        site/assets/questions-*.json

# For each chapter that got autogen-updated:
for ch in 4-clinical-immunology 8-oncology 20-endocrinology 23-hepatology \
         24-haematology-and-transfusion-medicine 25-rheumatology-and-bone-disease \
         28-medical-ophthalmology 29-medical-psychiatry 30-maternal-medicine \
         32-older-adult-medicine-and-frailty; do
    git add "chapters/$ch"
done
```

Do NOT stage `chapters/16-cardiology/` etc. if those changes are unrelated drift from the build pipeline. Stage selectively — the script's author message is more useful if only meaningful changes are in it.
