# Header Standard for FCPS/MRCP Medical Notes

## Exact Required Headers (case-sensitive, no variants)

| # | Canonical Header | Forbidden Variants | Notes |
|---|------------------|---------------------|-------|
| 1 | `## Learning Objectives` | `## Objectives`, `## Learning objectives`, `## LEARNING OBJECTIVES` | Must be plural, capitalized |
| 2 | `## Management` | `## Treatment`, `## Medical Treatment`, `## Pharmacological Therapy`, `## Therapy`, `## Management and Treatment` | Single word "Management" |
| 3 | `## MCQs` | `## MCQs (10)`, `## MCQ Questions`, `## MCQs (10)`, `## Multiple Choice Questions` | Exactly "MCQs" |
| 4 | `## SBA Questions` | `## SBAs`, `## SBA`, `## SBA Questions (10)`, `## Single Best Answer`, `## SBAs (10)` | Full phrase "SBA Questions" |
| 5 | `## Common Viva Questions` | `## Viva Questions`, `## Viva`, `## Revision prompts`, `## Common Viva` | Full phrase |
| 6 | `## One-Page Revision Summary` | `## One-page summary`, `## One-Page Summary`, `## Revision Summary`, `## Revision`, `## Summary` | Full phrase |

## Placement Rules
- Headers must be level-2 (`## `)
- Order must follow the table above
- No extra blank headers between them
- Content under each header starts immediately after

## Regex for Automated Verification

```python
REQUIRED_HEADERS = [
    "## Learning Objectives",
    "## Management",
    "## MCQs",
    "## SBA Questions",
    "## Common Viva Questions",
    "## One-Page Revision Summary",
]

# Check all present
all(h in content for h in REQUIRED_HEADERS)

# Detect forbidden variants (flag for fixing)
FORBIDDEN = {
    "## Objectives": "## Learning Objectives",
    "## Treatment": "## Management",
    "## MCQs (10)": "## MCQs",
    "## SBAs": "## SBA Questions",
    "## Viva Questions": "## Common Viva Questions",
    "## One-page summary": "## One-Page Revision Summary",
}
```

## Placeholder Detection Patterns

Flag files containing these as **incomplete**:

```python
PLACEHOLDER_PATTERNS = [
    r"would be added in complete version",
    r"would be included in the complete version",
    r"Full \d+ MCQs \+ \d+ SBAs would be",
    r"MCQs \+ \d+ SBAs would be added",
]
```

## File Naming Convention
- Use display name as filename: `Atrial fibrillation.md`
- Directory = topic group: `Arrhythmias and Cardiac Conduction Disorders/`
- Avoid special chars: `|`, `+`, `;`, `:`, `?`, `*`

## Display Name Extraction
For MOC/Hierarchy links: `[[path/Display Name|Display Name]]`
- Display name = human-readable topic title
- Path = directory + display name (spaces preserved)

---

## Quick Fix Commands

```bash
# Fix common header variants in all .md files
find /path/to/Medicine -name "*.md" -exec sed -i 's/## Objectives/## Learning Objectives/Ig' {} +
find /path/to/Medicine -name "*.md" -exec sed -i 's/## Treatment/## Management/Ig' {} +
find /path/to/Medicine -name "*.md" -exec sed -i 's/## MCQs (10)/## MCQs/Ig' {} +
find /path/to/Medicine -name "*.md" -exec sed -i 's/## SBAs/## SBA Questions/Ig' {} +
find /path/to/Medicine -name "*.md" -exec sed -i 's/## Viva Questions/## Common Viva Questions/Ig' {} +
find /path/to/Medicine -name "*.md" -exec sed -i 's/## One-page summary/## One-Page Revision Summary/Ig' {} +
```

---

## Validation Checklist

When reviewing a file, verify:
- [ ] All 6 exact headers present
- [ ] No forbidden variants
- [ ] No placeholder text
- [ ] 10 MCQs with explanations inline
- [ ] 10 SBAs with explanations inline
- [ ] 8+ Viva questions
- [ ] One-page revision summary (4-5 bullets)
- [ ] Flashcards section
- [ ] Answer key with explanations
- [ ] Status line at bottom with date and sources