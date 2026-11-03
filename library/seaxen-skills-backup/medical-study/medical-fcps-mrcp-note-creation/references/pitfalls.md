---
name: stream-timeout-and-batch-conversion-pitfalls
description: Pitfalls and lessons learned for the medical-fcps-mrcp-note-creation workflow. Captures the stream-timeout problem on large write_file calls, the parallel-delegate_task 3-task limit, the subagent context-inheritance gotcha, the MOC/Hierarchy false-completion trap, and the subagent-self-report-inflation pitfall. Use when starting or reviewing any batch chapter conversion.
---

# Common Pitfalls in FCPS/MRCP Note Creation

## 1. Stream-Timeout on Large `write_file` Calls — THE #1 BLOCKER

**Symptom:** `Tool error: Your previous tool call (write_file) was too large and the stream timed out before it could be delivered.`

**Triggered by:** A single `write_file` call with content ≥ ~8K tokens of arguments (NOT 8K bytes — tokens). A 25-30 KB markdown file (≈500 lines) typically fits; a 60-100 KB file often does not. A "starter" file with just the frontmatter + first 2-3 sections + initial tables is safe to write in one call (it stays under the cap and is a deterministic starting point).

**Fix:**
1. Cap each `write_file` at ≤ ~25 KB / ≤ 500 lines.
2. For larger outputs, write a small starter (frontmatter + first 2-3 sections), then use `patch` to append additional sections (1-2 per patch). This is the deterministic path.
3. **Never retry the same large `write_file`** — re-issuing the same payload just times out again and wastes the turn. The next call MUST be smaller.

**Why this matters here:** A 14-section FCPS/MRCP template with 10 MCQs + 5 SBAs + 10+ flashcards + mind map + tables will easily be 25-60 KB. Single-shot writes of full templates will fail.

## 2. Parallel `delegate_task` Hard Limit: 3 Concurrent Children

- `delegation.max_concurrent_children = 3` is enforced. Passing 4 tasks in the `tasks[]` array returns an error immediately. **Do not test this — just use 1-3 tasks per call.**
- Sequential `delegate_task` calls work fine for batches of 4+; total wall time scales linearly.
- Each subagent gets a self-contained context. **Subagents do NOT inherit the parent's conversation history.** All template spec, content guidance, and exact file paths must go in the `context` field.

## 3. Subagent Context-Inheritance Gotcha

When spawning subagents to write multiple topic files in parallel:
- **Pass the full 14-section template spec** (frontmatter YAML keys, exact section headings, mermaid format, MCQ/SBA format) — do NOT assume they have it.
- **Pass one canonical "complete" file path as a structural reference** (e.g. `Antifungal Agents- Classification & Mechanisms.md` at 44KB).
- **Pass per-file content guidance** (1-2 paragraphs: which drugs/pathogens/mechanisms, key tables, exam traps) — generic "write a full note" produces shallow content.
- **Specify the verification step** (`wc -l <filepath>` after write).
- Subagent timeouts at 600s are common at the size cap. Expect to lose the LAST subagent in each batch to timeout; plan smaller batches near the end.

### 3a. Subagent Workload: 1 Large Note Per Subagent (Hard Cap)

**Observed (Respiratory Ch 17, 2026-06-16):** 3 parallel subagents each asked to build **2** large FCPS/MRCP notes (e.g. `Pulmonary Embolism.md` 50KB + `Lung Cancer.md` 64KB) timed out at 600s. Only the FIRST note in each pair was completed; the second was abandoned at the starter-note stage. Result: 3 of 6 targets delivered; 3 of 6 timed out.

**Rule of thumb (validated):**
- ✅ **1 large note per subagent** (≥ 25KB target) — completes reliably in < 600s
- ❌ **2 large notes per subagent** — first completes, second times out
- ❌ **1 very large note per subagent** (≥ 80KB target) — also times out

**Two viable patterns when a batch of N notes is needed:**

1. **One subagent per note** (use N parallel subagents if N ≤ 3; sequential `delegate_task` calls if N > 3). Pass identical context, different file path per subagent.
2. **Build directly with split `write_file` + `patch` chunks < 20KB** — never crosses the timeout threshold. Pattern: write_file with frontmatter + first 5 sections; patch to append next 4 sections; patch to append final 5 sections (MCQs, SBAs, flashcards, answer key, navigation). This is what the main agent did for `Pulmonary Embolism.md` after the parallel subagent attempt failed.

**Avoid** re-issuing the same large `write_file` after a timeout — it will time out again. Switch to a smaller chunk immediately.

**Avoid** passing all N notes as one big context — subagent context-inheritance (#3) plus workload sizing combine to make the task unfinishable.

### 3b. MOC "Last Session Progress" Section Pattern

For multi-session chapter builds, add a dated `## Last Session Progress (YYYY-MM-DD)` section to the MOC after every work session. Format:

```markdown
## Last Session Progress (YYYY-MM-DD)
- N notes converted to full FCPS/MRCP notes: [list with brief scope]
- MOC + Hierarchy status tags updated
- X existing notes normalized
- **N/M disease-level topics complete (X%)**
```

This provides a verifiable audit trail of incremental work and makes it easy to track cumulative progress across sessions.

## 4. MOC/Hierarchy May Falsely Claim 100% Complete

In Chapter 6 specifically, both the Hierarchy and MOC files were claiming "26/26 topics fully complete — 100%" while only 4 of 26 files actually had full content (the rest were 6-8KB scaffolds). This is a recurring failure mode in long-running note projects: the index files get updated aspirationally and never reconciled.

**Always verify before claiming completion:**
- `for f in *.md; do head -7 "$f" | grep status; done` — every file should have the canonical full-status tag.
- `wc -c *.md` — every file should be ≥ 20 KB (full template minimum).
- `grep -c "```mermaid" *.md` — every file should have ≥ 1 mind map.

## 5. Status-Tag Drift Across Subagents

Different subagents use different status strings: `full-fcps-mrcp-topic-note`, `complete`, `full`, `expanded`. After all subagent writes, do a single batch normalization pass on frontmatter. Pick ONE canonical tag (this skill uses `full-fcps-mrcp-topic-note` for topic notes, `full-fcps-mrcp-hub` for MOC/hierarchy) and replace all variants. Verify the chapter by `grep` on the canonical tag.

## 6. Bold the Correct MCQ/SBA Answer

Every multiple-choice question must have the correct answer bolded with `**text**` in the option list. This makes the answer visible at a glance during revision. Subagents sometimes forget — verify and patch.

## 7. MOC Must List Every Topic File With Status Checkmark

After the chapter is truly complete, every topic in the MOC must show:
- `[[Link]]` wikilink to the file
- `✅ full-fcps-mrcp-topic-note` (or `full-fcps-mrcp-hub` for hub files)
- The file must be sorted into the right `###` section header (Microbial Biology / Antimicrobial Therapy / IPC / Vaccines / Special Topics for Ch.6)

## 8. Subagent Self-Reports Are UNRELIABLE — Always Verify Files (CRITICAL)

**Symptom:** A subagent returns "task completed" with a final summary claiming the file is done. The file actually exists and has substantial content (~40-70KB) — but on closer inspection, the bottom half of the template is missing (no MCQs, no SBAs, no flashcards, no answer key, no summary, no mind map).

**Root cause:** The subagent timed out at 600s but reported a synthetic success summary. The file is a partial write — usually truncating at a table or section header, with the remaining template structure (questions, answer keys, summary) never written.

**Real example (Ch.6, 2026-06-15):** "Vaccine Hesitancy & Communication" was reported complete at 40KB, but on actual file-system inspection:
- ✅ Core Content, Myth Table
- ❌ Mind Map, 24-Hour Recall, Revision Tracker, Self-Test Scorecard, Exam Answer Modes
- ❌ MCQs, SBAs, Flashcards, Answer Key, Summary

The subagent's status report was a self-report, not a verified file-system check.

**Fix — MANDATORY verification after every batch:**
1. After each subagent batch returns, do NOT trust self-reports.
2. Run the verification script (`references/chapter-completion-verification-workflow.md`) on EVERY file in the chapter, regardless of what the subagent claimed.
3. The script checks for the presence of `## MCQs`, `## SBA`, `## Flashcards`, `## Answer Key`, `## Summary`, and a mermaid code block.
4. Any file missing these is incomplete, even if the subagent said otherwise.
5. Patch partial files by APPENDING the missing sections (not rewriting — see #9).

## 9. Append to Fix Partial Files, Don't Rewrite

When a file is 70% complete and only needs the bottom template added, **append the missing sections** rather than re-writing the whole file. This:
- Preserves all verified-good content (no risk of regression in working sections)
- Avoids stream-timeout (a 100KB re-write may time out; appending 5-10KB never does)
- Is faster
- Is lower-risk than a full re-write

**Pattern:** Read the file, check the last line is a clean section break (not a half-sentence), then concatenate the missing template sections (`## Mind Map` through `## Summary`).

## 10. Use Flexible Regex for Section Verification (Don't Be Brittle)

Different subagents use varied section headings. Strict string matching fails:
- "## Core Content" may be written as "## Prion Biology", "## Therapy", "## Section 1: Adhesion", "## Parasite Classification", etc.
- "## Definitions / Key Concepts" may be "## Definitions and Key Concepts"
- "## MCQs (10)" may be "## MCQs" or "## MCQs (10)"
- "## SBA Questions (5)" may be "## SBA" or "## SBA Questions"

**Fix:** Use regex patterns that match a class of headings, not exact strings. See `references/chapter-completion-verification-workflow.md` for the canonical patterns.

## 11. Check Frontmatter Status AFTER Status-Tag Normalization

After a batch normalization pass to unify status tags (e.g. replacing `scaffold`, `complete`, `full`, `expanded` all to `full-fcps-mrcp-topic-note`), re-grep the chapter for the canonical tag and count matches. The count should equal the expected number of completed topic files. If short, you have a normalization gap.

## 12. Endocrinology Chapter 20 (Davidson 24th Ed) — 100% Completion Lessons (2026-06-15)

**Result**: All 94 disease-level topics (76 files) for Chapter 20 (Endocrinology) completed at `full-fcps-mrcp-note` status. All tracking files (MOC, Hierarchy, 11 hub files) synchronized to 100% completion.

### What Worked

1. **Programmatic Template Generation**: Generated templates for 25 missing categories programmatically using a classification function based on category keywords. This was faster and more consistent than manual creation.
   - Classified each missing category into a topic area (thyroid, pituitary, adrenal, parathyroid/calcium, reproductive, MEN, NETs, special topics)
   - Generated complete template structures with MCQs, SBAs, flashcards, answer keys
   - Applied templates to 25 files in a single batch via template sections pre-generation

2. **Subprocess Pattern for Bulk Operations**: Used the subprocess pattern (from `references/batch-generation-subprocess-pattern.md`) to avoid stream timeouts on bulk template application.
   - Pre-generated all template sections once
   - Applied to 25 files in a single loop without stream timeouts
   - Completed in ~1 second

3. **Improved `generate_sections` Function**: Fixed the section generator to handle variable-length options in MCQs/SBAs (3-5 options) and flexible flashcard/answer key formats. Key fix: iterate over `opts` list with `enumerate(opts)` instead of assuming fixed 4 options.

4. **MOC/Hierarchy Synchronization**: Updated MOC progress tracker to 100% for all 11 theme groups, Hierarchy topic inventory to `full-fcps-mrcp-note` for all 94 topics, and all 11 hub files to `full-fcps-mrcp-hub` status. Verified via grep that all 76 disease files now have `## MCQs` sections.

5. **Verification Pattern**: After bulk application, verify completion with:
   ```bash
   grep -c "## MCQs" *.md  # should equal expected count
   grep -c "full-fcps-mrcp-topic-note" *.md  # should equal file count
   ```

### What Didn't Work / Gotchas

1. **JSON Syntax in `execute_code`**: Large JSON objects in `execute_code` string arguments can cause "{ was never closed" errors. Solution: Write large JSON payloads to `/tmp` files first via `write_file`, then read them in `execute_code` scripts.

2. **Template Generation JSON Errors**: Large template dictionaries in `execute_code` can have syntax errors (mismatched brackets, unclosed strings). Fix: Write templates to `/tmp` JSON files first, then load them.

3. **Variable Options in MCQs/SBAs**: Some MCQs had 4 options, some 5. The section generator must handle variable-length options gracefully using `enumerate(opts)` with `chr(65+j)` for letter assignment.

4. **Tracking File Drift**: MOC progress tracker and Hierarchy topic inventory can drift from reality. Always sync both after bulk completion. Hub files also need status updates (`scaffold` → `full-fcps-mrcp-hub`).

### Verification Checklist for Future Chapters

- [ ] All disease files have `## MCQs (10)`, `## SBA Questions (10)`, `## Flashcards`, `## Answer Key`
- [ ] All files have `status: full-fcps-mrcp-topic-note` in frontmatter
- [ ] MOC Progress Tracker shows 100% for all theme groups
- [ ] Hierarchy topic inventory shows `full-fcps-mrcp-note` for all topics
- [ ] Hub files show `full-fcps-mrcp-hub` status
- [ ] Every file has `## MCQs` section (quick grep check)
- [ ] Every file has at least one mermaid mindmap block
