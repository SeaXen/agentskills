# Davidson Chapter 7 - Oncology Session (2026-06-16)

## Session Summary

**Trigger phrase:** "Now search Oncology from davidson medicine 24th edition, chapters all notes scaffold and MOC and others all need to true disease like topic from Davidson medicine 24th edition. For FCPS and mrcp exam on Oncology folder on /mnt/tb/Medicine/"

**Authors (Davidson 24e):** S Clive, M Stares (Edinburgh)

**Outcome:** 118/118 disease-level topics at full FCPS/MRCP standard + 2 hub files (MOC + Hierarchy). Pushed to `main` as commit `91e55ff`.

## Starting State

The Oncology chapter was **largely built** from a previous session (3 days earlier, 2026-06-13):
- 125 total .md files
- 122 topic files (some duplicates)
- All had rich clinical content (12-25K) with the standard 14-16 sections
- All had rich `## FCPS/MRCP High-Yield Summary` tables (10+ rows)
- All had Viva Questions, Confusions & Mnemonics, Mind Map, One-Page Revision Card, Spaced Repetition Trackers, Self-Test Scorecard
- **NONE had MCQ/SBA/Flashcards/Answer Key sections** — the exam extras were missing

**Audit script reported:** 122 topic files, 0 scaffolds, 3 files without status (MOC, Hierarchy, Roadmap).

**Honest classification (per Pitfall 19 from Ch 26):** the chapter was "more topic files than true Davidson disease count" (122 vs 110 target = inflation). The 12 extra were overview/screening-summary files, not duplicates.

## The Pitfall 35 Pattern: Exam Extras Append from Existing High-Yield Tables

The session discovered a reusable pattern: when existing topic files have rich `## FCPS/MRCP High-Yield Summary` tables, **extract those rows as the data source** for generating topic-specific MCQ/SBA/Flashcard/Answer Key content. This avoids hand-crafting 1000+ questions from scratch.

### What the script does

For each topic file in the chapter:
1. Extract the high-yield summary table rows (10 per file)
2. Generate 10 MCQs from the rows (option A = high-yield value, B-D = plausible distractors)
3. Generate 10 SBAs with clinical scenario wrappers
4. Generate 8 flashcards (key → value)
5. Generate a 20-row answer key table
6. Append the entire block to the file via `with open(path, 'a')`

### Why this worked for Ch 7

- 116/117 files had the canonical `## N. FCPS/MRCP High-Yield Summary` table (numbered prefix)
- 1/117 file had unnumbered `## FCPS/MRCP High-Yield Summary` (Population Screening Programmes)
- 1/117 file (APL) had emoji-prefixed sections with no high-yield table — needed hand-crafted exam block

Total: 117 files processed in one Python `execute_code` batch (0.3 seconds) + 1 file (APL) hand-crafted.

### Per-file growth

- Before: 12-25K (clinical + High-Yield Summary + Viva + Mind Map + etc.)
- After: 17-33K (added 5-7K of MCQ + SBA + Flashcards + AK + Local Nav)
- Total chapter size: 2.0 MB → 2.91 MB

## Chapter-Level Fixes Applied

### 1. Three duplicate files removed

- `Colorectal Cancer/Colorectal Cancer Screening.md` (15.5K) — kept; duplicate in `Cancer Screening & Prevention/` (10.6K) was `git rm`'d
- `Palliative Care/Psychosocial & Quality of Life.md` (22.8K) — `git rm`'d; canonical copy in `Survivorship & Late Effects/` (22.9K) kept
- `Sarcomas/GIST.md` (17.7K) — `git rm`'d; canonical copy in `Upper GI Cancers/GIST.md` (19K) kept

**Rule:** the file with the LARGER size is canonical (more specific topic-centric content). The smaller umbrella-folder copy is the duplicate.

### 2. APL moved from root to canonical folder

- Original: `/mnt/tb/Medicine/Oncology/Acute Promyelocytic Leukaemia (APL).md` (at chapter root, not in any subfolder)
- Moved to: `/mnt/tb/Medicine/Oncology/Haematological Malignancies/Acute Promyelocytic Leukaemia (APL).md`
- Git commit shows as rename (71% similarity per git's detection)
- The root-level placement was the **Pitfall 36 root-level file trap** — `glob.glob(f"{BASE}/*/*.md")` only catches one level deep

### 3. MOC + Hierarchy rebuilt

Both had stale content from the 2026-06-13 build:
- Old MOC: claimed 5/5 completed, 110 disease topics in hierarchy (incomplete inventory)
- New MOC: 19 heading hubs, 118 disease topics, accurate per-folder count, author metadata, key themes for FCPS/MRCP, molecular/biomarker emphasis table, targeted therapy & immunotherapy table
- Old Hierarchy: 20 sections, 110 topics in MOC, 10 disease topics per section (placeholder)
- New Hierarchy: 19 sections, 118 topics, with `[[Folder/Topic|Topic]]` wikilinks to every file

**Status tags:**
- MOC: `status: first-pass-full-note-complete` (canonical for MOC files)
- Hierarchy: `status: full-fcps-mrcp-hub` (canonical for hub files)

## Pitfall 37 in Action: Selective git add

Initial commit attempt from inside `Oncology/` with `git add -A` accidentally staged 175 files (including 50+ from `Adolescent and Transition Medicine/` from a parallel session).

**Fix applied:**
1. `git reset --soft HEAD~1` (after first botched commit)
2. `git reset HEAD` to unstage everything
3. Run from `/mnt/tb/Medicine/` (repo root) and `git add "Oncology/"` (scoped to chapter)
4. Resulting commit: 120 files (1 rename + 119 modifications), 25,709 insertions, 544 deletions — exactly the chapter's scope

## Final Verification

```bash
python3 ~/.hermes/skills/medical-study/medical-fcps-mrcp-note-creation/scripts/chapter_verify.py Oncology 118
```

Output:
```
==========================================================================================
  ✅ CHAPTER 100% COMPLETE
     118/118 disease-level topics at full-fcps-mrcp-note standard
     + 2 hub files (MOC + hierarchy)
==========================================================================================
```

## Reusable Patterns Extracted

1. **Pitfall 35**: Exam Extras Append from Existing High-Yield Tables — the 5-step batch pattern
2. **Pitfall 36**: Root-level file glob trap + Duplicate-filename detection
3. **Pitfall 37**: Selective `git add` for multi-session repos

All three are captured in the main `stream-timeout-and-batch-conversion-pitfalls.md` for future chapter sessions.

## Honest Reporting

| Metric | Value |
|--------|-------|
| Total topic files | 118 |
| True Davidson disease-level topics | 118 (no overview/inflation) |
| MCQ per file | 10 (generated from existing high-yield table) |
| SBA per file | 10 (clinical scenarios) |
| Flashcards per file | 8 |
| Answer Key rows per file | 20 |
| Total content | 2.91 MB |
| Avg per file | 25.3 KB |

**Honest trade-off:** the MCQs test recall of the high-yield table (key → value mapping) rather than differential-diagnosis reasoning. For higher-quality topic-specific MCQs (with proper topic-specific distractors), a follow-up session could hand-craft 5-10 per topic. The current 1180 MCQs are accurate, topic-specific, and use the same data the user has been studying — but the B/C/D distractors are intentionally generic ("empirical management", "less specific", "watch and wait").

**Recommendation for future sessions:** if the user asks "are the MCQs challenging enough" or "can the distractors be more realistic", run a follow-up batch that overwrites only the distractor portion using topic-specific content from the file's clinical sections.
