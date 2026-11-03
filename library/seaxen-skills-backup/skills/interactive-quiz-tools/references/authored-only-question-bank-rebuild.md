# Authored-only question bank rebuild (validated on MedSea, 2026-06-22)

Use this when the live exam/flashcard bank is structurally valid JSON but pedagogically bad: 1-2 word prompts, generic "first-line treatment?" stems, single-option items, or obviously auto-generated junk.

## Trigger

Rebuild from authored content only when one or more of these are true:
- user reports questions are "not real" or missing scenarios
- many MCQs are generic/contextless (`What is the first-line treatment?`, `What is the diagnosis?`)
- items have invalid option counts or missing answers
- flashcards are mostly fragments instead of prompts

## Strategy

Do **not** try to patch the bad live JSON in place. Rebuild from `topic.md` authored sections only:
- `## MCQs`
- `## SBA Questions` / `## SBAs`
- `## Flashcards`
- `## Answer Key with Explanations`

This is a quality-first fallback. It reduces quantity but sharply improves trust.

## Extraction rules that worked

### MCQ keep rules
Keep only items that satisfy **all**:
- 4+ options
- answer key present and answer label exists in options
- stem has at least 5 words
- strip leading `Q:` prefixes
- reject contextless generic stems exactly matching patterns like:
  - `What is the first-line treatment?`
  - `What is the most important complication?`
  - `What is the diagnosis?`
  - `What is the treatment?`
  - `What is the best investigation?`

### SBA keep rules
Keep only items that satisfy **all**:
- 4+ options
- answer key present and valid
- stem has at least 10 words
- prefer scenario-style authored SBAs

### Flashcard keep/normalize rules
- require front >= 3 words and back >= 2 words
- strip leading `Q:` and markdown markers
- normalize fragments into question form:
  - `High extraction drugs list` -> `High extraction drugs list?`
  - `Contact tracing` -> `What is Contact tracing?`
  - plural topic endings (`criteria`, `features`, `signs`, `complications`, etc.) -> `What are the ...?`
- dedupe on normalized front+back

## Answer-key extraction
Do not rely only on bolded options inside the question block. Parse `## Answer Key with Explanations` too.

Working pattern:
- detect `### MCQs` and `### SBAs`
- parse lines like `1. **B** — explanation`
- map question number -> answer label

## MedSea result from this fallback
Initial authored-only rebuild:
- MCQ: 2916
- SBA: 1320
- Flashcards: 3676
- Chapters with authored study content: 16

After stricter cleanup of contextless MCQs + flashcard normalization:
- MCQ: 2754
- SBA: 1320
- Flashcards: 2814
- Chapters: 16

## Quality gates before deploy
Run these checks on the rebuilt JSON and require all to pass:
- MCQ one-option count = 0
- MCQ <4 options count = 0
- MCQ missing answer count = 0
- MCQ leading `Q:` count = 0
- banned generic stem count = 0
- SBA malformed count = 0
- flashcards without question-form front = 0 or consciously accepted

## Live verification pattern
After deploying the rebuilt JSON:
1. verify remote JSON counts with `curl`
2. verify `/exam/` and `/flashcards/` show the cleaned chapter/card availability counts
3. start a real exam and inspect the first runner item visually
4. start a real flashcard session and inspect front/back state

On MedSea the exam runner passed with a real scenario question:
- pregnant abattoir worker with Q fever in pregnancy, real options

The flashcard runner passed with normalized prompt form:
- front: `What is Contact tracing?`
- back: `Ebola 21d, Lassa 17d, CCHF 14d`

## Important consequence
This fallback is **quality-first, not completeness-first**. Expect fewer questions and fewer covered chapters if authored sections are sparse. That is acceptable when the current live bank has lost user trust.
