# Plain-Header Template Variant (Davidson Ch 9 Style)

This is the **second template variant** used in `/mnt/tb/Medicine/`. It exists in parallel to the v2 emoji template documented in `fcps-mrcp-template-v2.md`.

## Where It Appears

- Davidson 24e **Chapter 9: Acute Medicine and Critical Illness** (full chapter)
- Possibly other chapters written in the same session/wave — verify with the audit script's variant detector before assuming.

## Full 14-Section Structure

The section set is similar to v2, but headers are **plain `##`** (no emoji) and several section names differ:

| # | Section Header (exact text) | Notes |
|---|---|---|
| 1 | Frontmatter | `status: full-fcps-mrcp-topic-note` (this variant uses `-topic-note`, not `-note`) |
| 2 | `## Learning Objectives` | Plain header |
| 3 | `## Core Concept / Definition / Classification` | Free-form, often merged |
| 4 | `## Pathophysiology / Etiology / Causes` | Free-form numbered or named |
| 5 | `## Clinical Features` | |
| 6 | `## Investigations` | |
| 7 | `## Management` | |
| 8 | `## FCPS/MRCP High-Yield Points` | Plain header, not `## ⚡ FCPS/MRCP High-Yield Summary` |
| 9 | `## Common Viva Questions` | Plain header, not `## 🎤 Viva Questions` |
| 10 | `## Common Confusions / Exam Traps` | |
| 11 | `## One-Page Revision Summary` | Plain header |
| 12 | `## Mnemonics` | Often includes Mermaid mindmap |
| 13 | `## MCQs (10)` | **Header declares count** |
| 14 | `## SBA Questions (10)` | **Header declares count** |
| 15 | `## Flashcards` | |
| 16 | `## Answer Key with Explanations` | Single combined key for both MCQs and SBAs |

The count `(10)` in headers 13–14 makes the declared question count discoverable by regex — use `r'## MCQs \((\d+)\)'` to extract it.

## Detection Heuristics (for audit script)

A file uses the plain-header variant iff it contains `## MCQs (10)` OR `## SBA Questions (10)` (with the parens-count pattern). If those anchors are present, switch to plain-header checks; otherwise fall back to emoji anchors.

Required anchors for plain-header variant:
- `## Learning Objectives`
- `## Management`
- `## MCQs (10)` (with content — see below)
- `## SBA Questions (10)` (with content)
- `## Common Viva Questions`
- `## One-Page Revision Summary`
- `## Flashcards`
- `## Answer Key with Explanations`

## Real-Content Check (the critical bit)

The **header presence** check is not enough. You must verify each section has actual content:

```python
def count_filled_items(section_body: str, min_chars: int = 30) -> int:
    """Count numbered items (1. 2. 3.) that have at least min_chars of real text."""
    # Match "N. <text>" where text is non-empty and longer than threshold
    items = re.findall(r'^\s*(\d+)\.\s*(.+)', section_body, re.MULTILINE)
    return sum(1 for _, text in items if len(text.strip()) >= min_chars and text.strip() not in {'.', ''})

def has_empty_placeholders(section_body: str) -> bool:
    """Detect the '1.\n2.\n3.\n...' empty-numbered-list pattern."""
    lines = [l.strip() for l in section_body.split('\n') if l.strip()]
    numbered = [l for l in lines if re.match(r'^\d+\.$', l)]
    return len(numbered) >= 5  # 5+ bare numbers in a row = empty placeholder block
```

A file is **truly complete** iff:
- Frontmatter `status` is `full-fcps-mrcp-note` OR `full-fcps-mrcp-topic-note`
- All required anchors present (variant-appropriate)
- MCQ section: ≥10 filled items (each ≥30 chars)
- SBA section: ≥10 filled items (each ≥30 chars)
- Flashcard section: ≥5 Q→A pairs with non-empty Q and A
- Answer Key section: ≥10 numbered keys

## Common Pitfall: Empty Placeholder Block

The most insidious incomplete pattern in this variant is a block like:

```
## MCQs (10)
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
```

This has the `## MCQs (10)` header (so header-anchor check passes), but every question is missing. A naive `re.findall(r'^\d+\.\s*(.+)', body)` will pick up the next number-line as the "content" of the current line and report "5/10 filled" instead of "0/10". **Always validate the count against ground-truth files before trusting the script.**

Fix: use lookahead `(?=\n\s*\d+\.|\n##|\Z)` to terminate each item properly, OR require `len(text.strip()) >= 30` to filter out digit-only "content".

## Example Complete File

`/mnt/tb/Medicine/Acute Medicine and Critical Illness/Hypovolaemic Shock.md` — 261 lines, 8.5KB, all 14 plain-header sections present, 10/10 MCQs + 10/10 SBAs with full question text, 8 flashcards, full answer key.

## Example Partial File (looks complete, isn't)

`/mnt/tb/Medicine/Acute Medicine and Critical Illness/Acid-Base and Electrolyte Emergencies.md` — 494 lines, 22KB, full clinical content with Mermaid diagrams and tables, BUT the MCQ/SBA/Flashcard/Answer-Key sections are all empty numbered placeholders. The MOC tracker marked it "Notes Complete ✅" because header presence was checked but content wasn't.

## Migration Path

If a chapter needs to migrate from plain-header to emoji-header variant (or vice versa), it's a `## sed` job over the 14 known headers. See `references/header-standard.md` for the full mapping. Not recommended unless the user explicitly asks.
