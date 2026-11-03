---
name: post-batch-verification-append-fix-pattern
description: Pattern for verifying subagent output and fixing partial files by appending missing template sections. Captures the self-report-inflation trap, flexible regex verification, and append-vs-rewrite decision framework. Use after any batch chapter conversion or delegate_task run that produced large content.
---

# Post-Batch Verification & Append-Fix Pattern

## When to Use This Pattern
Use this after any:
- `delegate_task` call that wrote 5+ large markdown files
- Batch chapter conversion of scaffolds → full templates
- Subagent batch where any individual task runs near 600s timeout

## Step 1: Don't Trust Self-Reports

Subagent final summaries may say "task completed successfully" but the actual file may be truncated, missing bottom template sections, or have inconsistent content. Treat every subagent self-report as a *hypothesis to verify*, not a *fact to record*.

**Real examples from Davidson Ch.6 (2026-06-15):**
- Subagent reported "Vaccine Hesitancy & Communication.md completed at 40KB" — file was actually 40KB but missing MCQs, SBAs, flashcards, summary, mind map (the bottom half of the template).
- 2-3 other subagents timed out at 600s but reported synthetic "completed" summaries without all sections.

## Step 2: Run Flexible Regex Verification

Use a verification script (not strict string matching) on every file. The script should:
1. Check for `## MCQs` (or `## MCQs (10)`)
2. Check for `## SBA` (or `## SBA Questions`)
3. Check for `## Flashcards`
4. Check for `## Answer Key` (or `## Answer Key with Explanations`)
5. Check for `## Summary`
6. Check for at least one ` ```mermaid ` code block
7. Check file size ≥ 20KB (sanity check)
8. Check status frontmatter is the canonical tag

**Flexible regex patterns** (don't be brittle — subagents vary headings):

```python
required_patterns = {
    "Learning Objectives": r"^##\s+Learning Objectives",
    "Definitions/Key Concepts": r"^##\s+(Definitions|Definitions\s+and\s+Key\s+Concepts)",
    "Core Content (any variant)": r"^##\s+(Core Content|.+Content|Section \d|Pathogen|Therapy|Biology|Structure|Epidemiology|.+Biology)",
    "Mind Map (mermaid)": r"```mermaid",
    "MCQs (10)": r"^##\s+MCQs\s*\(?10\)?",
    "SBA (5)": r"^##\s+SBA",
    "Flashcards": r"^##\s+Flashcards",
    "Answer Key": r"^##\s+Answer Key",
    "Summary": r"^##\s+Summary",
}
```

## Step 3: Append-Fix vs Re-Write Decision

When a file is incomplete, decide between:

| Approach | When to use | Why |
|----------|-------------|-----|
| **APPEND** the missing bottom sections | File is 60-90% complete, just missing `## Mind Map` through `## Summary` | Preserves good content, avoids stream-timeout, lower risk |
| **Re-write** the whole file | File is <50% complete, has content quality issues throughout, or has wrong structure | Cleaner but risks regression; cap at ≤25KB per call |

**Default to append when possible.** The append pattern:

```python
# 1. Read current content
with open(fpath, 'r') as f:
    content = f.read()

# 2. Verify it ends cleanly (not mid-sentence)
if not content.rstrip().endswith(('|', '.', '`', '}', ']', '---')):
    print(f"WARNING: {fpath} may not end cleanly - inspect before appending")

# 3. Append the missing template sections
append_block = """

---

## High-Yield FCPS/MRCP Points
[content]

## Mind Map
```mermaid
[content]
```

... [continue with all missing sections]

## Summary
[content]
"""

# 4. Write back
with open(fpath, 'w') as f:
    f.write(content + append_block)
```

## Step 4: Verify After Fix

Re-run the regex verification script on the patched file. Confirm:
- All required sections now present
- File size increased by 5-15KB
- Status frontmatter unchanged (still `full-fcps-mrcp-topic-note`)

## Step 5: Don't Trust Subagent Counts Either

If a subagent batch reports "5 files complete" but verification shows 3 of 5 are partial:
- Do NOT count the 5 as complete
- Re-delegate the failed files OR append-fix them directly (faster)
- Track actual completion count, not reported count

## Canonical Status Tags

Use ONE tag per file type:
- `full-fcps-mrcp-topic-note` — individual topic note (14-section template)
- `full-fcps-mrcp-hub` — MOC, hierarchy, or chapter index
- `full-fcps-mrcp-note` — disease-level topic (older chapters use this, no `topic-` infix)
- `scaffold` — partial content (working draft)

After status-tag normalization (replacing `complete`/`full`/`expanded` variants to canonical), re-grep to confirm count.

## Reference Implementation

The full verification script (Python) is in `scripts/chapter_verify.py` and the workflow that wraps it is in `references/chapter-completion-verification-workflow.md`.

## Summary

The single most important rule: **Subagent self-reports are unreliable. Always verify with regex checks on every file. Patch partial files by appending missing sections, not by rewriting.**
