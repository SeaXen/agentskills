# Diabetes mapping + scaffold-card cleanup

Session-derived MedSea rebuild notes.

## What broke

`chapters/21-diabetes-mellitus/` existed, but chapter 21 was absent from the live `questions-index.json`, so the user could not reliably start an exam from that chapter.

## Root cause

Both autogen scripts were missing the source→published mapping:

- `Diabetes -> 21-diabetes-mellitus`

Files that needed the same mapping:
- `site/scripts/autogen_scenario_sbas.py`
- `site/scripts/autogen_study_sections.py`

If only one generator gets the mapping, one surface may populate while another stays blank.

## Verified fix sequence

1. Add `Diabetes -> 21-diabetes-mellitus` to both autogen scripts.
2. Re-run `autogen_scenario_sbas.py`.
3. Re-run `autogen_study_sections.py` if flashcards/MCQs are still absent for ch 21.
4. Re-run `rebuild_question_bank_v5.py`.
5. `docker cp` the four JSON files into `medsea:/usr/share/nginx/html/assets/`.
6. `docker commit medsea medsea-site:latest`.
7. Verify over HTTP and in the browser.

## Flashcard junk patterns found and filtered

These were generated from hub/scaffolding material and should be dropped in `parse_flashcards()`:

- backs starting with `Heading hub for`
- backs starting with `By the end of this note`
- backs containing `disease-level topic(s)`
- fronts longer than 15 words (usually broken vignette/MCQ carryover)
- any pipe / wikilink leakage (`|`, `[[`)

## Live result after cleanup

- Ch 21: `sba_count = 137`
- Ch 21: `flashcard_count = 873`
- all 32 chapters present in live `questions-index.json`
- selecting Ch 21 in `/exam/` changed Available count and **Start Exam** entered the runner successfully

## Why this matters

A missing chapter in exam setup is usually an **index-generation / mapping** problem, not a frontend rendering problem. Check `questions-index.json` before debugging the UI.
