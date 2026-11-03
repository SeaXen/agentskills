# Placeholder Patterns — Detect Incomplete Medical Notes

## Purpose
Identify files that claim to be "complete" but contain placeholder text indicating missing question banks or sections.

## Regex Patterns

```python
PLACEHOLDER_PATTERNS = [
    # Explicit "will be added" statements
    r"would be added in complete version",
    r"would be included in the complete version",
    r"will be added in the complete version",
    r"to be added in complete version",

    # "Full X MCQs + Y SBAs would be..." pattern
    r"Full \d+ MCQs \+ \d+ SBAs would be",
    r"Full 10 MCQs \+ 10 SBAs would be",
    r"Full \d+ MCQs \+ \d+ SBAs would be included",
    r"MCQs \+ \d+ SBAs would be added",

    # "Complete version" references
    r"in the complete version",
    r"in complete version",
    r"once the complete version is",
    r"when the full version is",

    # Incomplete section markers
    r"\[TODO\]",
    r"\[PLACEHOLDER\]",
    r"TO BE COMPLETED",
    r"SECTION INCOMPLETE",
]
```

## Compilation
```python
import re

PLACEHOLDER_REGEX = re.compile("|".join(PLACEHOLDER_PATTERNS), re.IGNORECASE)

def has_placeholder(content: str) -> bool:
    return bool(PLACEHOLDER_REGEX.search(content))
```

## Common False Positives (Safe to Ignore)
- `"Full FCPS/MRCP note completed"` in status line — **this is GOOD, means done**
- `"Date completed: 2026-06-05"` — normal metadata
- `"Sources: ESC Guidelines, Davidson"` — normal citations

## Usage in Audit
```python
def is_truly_complete(content: str) -> bool:
    # Must have all 6 headers
    required = [
        "## Learning Objectives",
        "## Management",
        "## MCQs",
        "## SBA Questions",
        "## Common Viva Questions",
        "## One-Page Revision Summary",
    ]
    if not all(h in content for h in required):
        return False
    
    # Must NOT have placeholders
    if has_placeholder(content):
        return False
    
    return True
```
## Categories of Placeholders

| Category | Pattern Example | Meaning |
|----------|-----------------|---------|
| MCQ/SBA pending | "Full 10 MCQs + 10 SBAs would be added in complete version" | Question banks missing |
| Section pending | "Viva questions would be added in complete version" | Viva section missing |
| Generic | "would be included in the complete version" | Unspecified gaps |
| Template boilerplate | "Full X MCQs + Y SBAs would be included in the complete version" | Copied from template, not customized |
| **Empty numbered block** (plain-header variant) | `## MCQs (10)` followed by `1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10.` | Header present, all questions missing — **insidious because it passes header-anchor checks** |

## Detecting the Empty Numbered Block

```python
def has_empty_numbered_placeholders(content: str) -> bool:
    """Find '1.\\n2.\\n3.\\n...' blocks inside MCQ/SBA sections."""
    # Find each MCQ/SBA section body
    for pattern in [r'## MCQs \(\d+\)(.*?)(?=\n## |\Z)',
                    r'## SBA Questions \(\d+\)(.*?)(?=\n## |\Z)']:
        for m in re.finditer(pattern, content, re.DOTALL):
            body = m.group(1)
            # Count lines that are just "N." (digit + dot + nothing)
            empty_lines = re.findall(r'^\s*\d+\.\s*$', body, re.MULTILINE)
            if len(empty_lines) >= 5:
                return True
    return False
```

This is the most common incomplete pattern in the plain-header variant. The MOC tracker in Davidson Ch 9 marked 6 such files as "Notes Complete ✅" when they were actually missing all MCQs/SBAs.

## Quick Scan Command

```bash
# Find files with explicit "would be added" placeholders
grep -r -i "would be added in complete version" /mnt/tb/Medicine/Cardiology/ --include="*.md"

# Find files with empty numbered MCQ placeholders (plain-header variant)
# Matches files where MCQs section has 5+ bare "N." lines
for f in /mnt/tb/Medicine/**/*.md; do
  if awk '/^## MCQs \(/{flag=1; next} /^## /{flag=0} flag && /^[0-9]+\.$/' "$f" | wc -l | grep -q "^5$"; then
    echo "EMPTY MCQ BLOCK: $f"
  fi
done
```

## Interpretation
- **File with placeholders + missing headers** = skeleton (not started)
- **File with placeholders + all 6 headers** = partial (content done, Q-banks missing)
- **File without placeholders + all 6 headers** = **STILL NOT GUARANTEED COMPLETE** — see empty numbered block check above
- **File without placeholders + all 6 headers + ≥10 filled MCQ items + ≥10 filled SBA items + ≥5 flashcards + ≥10 answer keys** = truly complete

## Integration
Used by `scripts/audit-medical-folder.py` — the `has_placeholder()` check filters out false-complete files.