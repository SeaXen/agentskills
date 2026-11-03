---
name: scaffold-to-full-template-batch-conversion
description: Workflow and pitfalls for batch-converting many scaffold .md files to a fixed full-content template (e.g. FCPS/MRCP 14-section) using parallel subagents. Distilled from the Chapter 6 batch where 22 scaffold files were expanded to 25-100KB each in one session.
---

# Scaffold → Full-Template Batch Conversion (with Subagents)

## When to use this pattern
- A chapter folder contains N scaffold files (typically 6-30) with shared topic_category, sharing a fixed 14-section (or similar) content template.
- The task is to upgrade all of them to a uniform full template (status flag flipped from `scaffold` to `full-...-note`) in a single session.
- Each file is large when written (≥20KB target) and has 10 MCQs + 5 SBAs + 10+ flashcards baked in.

## Critical Pitfall: Stream-Timeout on Large `write_file` Calls

**Symptom:** Tool error: *"Your previous tool call (write_file) was too large and the stream timed out before it could be delivered."*

**Triggered by:** Single `write_file` call with content ≥ ~8K tokens of arguments (not 8K bytes — tokens). A 25-30 KB markdown file (≈500 lines) typically fits; a 60-100 KB file often does not.

**Fix (do this from the start):**
1. Cap each `write_file` to ≤ ~25 KB / ≤ 500 lines of content.
2. For larger outputs, write a smaller initial file with the frontmatter + first 2-3 sections, then use `patch` to append additional sections (one or two per patch).
3. Alternative: split the content into 2-3 smaller `write_file` calls that each replace the whole file (each call must include the full intended content but stay under the cap). **Do NOT do this** — `write_file` overwrites. Better: write a small starter, then `patch` to add sections.

**The retry rule:** Never retry the same large `write_file`. If it times out, the next call MUST be smaller. Re-issuing the same payload just times out again and wastes the turn.

## Parallel `delegate_task` Limits

- **Hard limit: 3 concurrent children per `delegate_task` call** (configured by `delegation.max_concurrent_children`). Passing 4 tasks returns an error immediately — don't waste time testing.
- **Each child gets a self-contained context** — subagents do NOT inherit the parent's conversation. Pass full template spec, content guidance, and exact file paths in the `context` field.
- **Use `tasks[]` array** for parallel batches (1-3 tasks), NOT multiple sequential `delegate_task` calls when parallelism is possible.

## Reference File Workflow

1. **Pick one canonical "complete" file as the template model** (e.g. `Antifungal Agents- Classification & Mechanisms.md` at 44KB). Read it once. Pass it as the structural reference in every subagent's context.
2. **Subagent context must include:**
   - Absolute file paths (not just folder names)
   - The complete 14-section template structure (frontmatter YAML keys, exact section headings, mermaid mind map location, MCQ/SBA format, flashcard format)
   - **Content guidance** per file (1-2 paragraphs: which drugs/pathogens/mechanisms to cover, key tables, exam traps) — not just "write a full note"
   - Target size (e.g. 20-30 KB minimum)
   - Final verification step: `wc -l <filename>`

## Status-Tag Normalization

After all subagent writes, do a single batch normalization pass on frontmatter. Different subagents may have used different status strings (`full-fcps-mrcp-topic-note`, `complete`, `full`, `expanded`). Pick one canonical tag (e.g. `full-fcps-mrcp-topic-note`) and use a script (or sequential `patch`) to replace all variants. Verify the chapter by `grep` on the canonical tag.

## Verification

After batch conversion, run a final check that EVERY topic file has:
- Status `full-fcps-mrcp-topic-note` in frontmatter
- 10+ MCQs, 5+ SBAs, 10+ flashcards (search for the section headers)
- A mermaid mind map (` ```mermaid ` code fence)
- A size ≥ 20 KB

Update the chapter's MOC.md and Hierarchy.md to mark the chapter as truly complete (the chapter is often falsely flagged as 100% while files are still scaffolds — this was a specific problem in Ch.6).

## Time/Cost

- Each 25-30 KB file via subagent: ~5-7 minutes wall time, ~100-300K input tokens.
- 22-file batch via 8 sequential `delegate_task` calls (3+3+3+3+3+3+3+2): ~2-3 hours total.
- Subagent timeouts at 600s are common near the size cap — expect to lose the LAST subagent in each batch to timeout. Plan for it: issue smaller batches near the end, or accept the timeout and re-issue the missing file.

## Anti-Patterns to Avoid

- **Do NOT** use a single `write_file` to generate the full 14-section template for a 50KB+ file in one shot. It will time out.
- **Do NOT** ask a subagent to "make all 22 files at once" — they will time out, and you lose all work.
- **Do NOT** trust the MOC/Hierarchy's claim of "100% complete" without verifying each file's status tag and content size.
- **Do NOT** skip the verification `wc -l` step at the end of each subagent task — without it, a silently-truncated file looks done but is missing the back half of the template.
