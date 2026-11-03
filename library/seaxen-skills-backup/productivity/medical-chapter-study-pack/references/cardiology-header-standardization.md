# Cardiology Header Standardization Notes

## Standard Header Names (6 Required)
Must use exact names - variants don't count:

| Required Section | Exact Header | Common Variants (DON'T count) |
|-----------------|--------------|------------------------------|
| Learning Objectives | `## Learning Objectives` | `## Learning objectives`, `## Objectives` |
| Management | `## Management` | `## Treatment`, `## Management and Treatment` |
| MCQs | `## MCQs` | `## MCQs (10)`, `## MCQ Questions` |
| SBA Questions | `## SBA Questions` | `## SBA`, `## SBAs`, `## SBA Questions (10)` |
| Common Viva Questions | `## Common Viva Questions` | `## Viva`, `## Viva Questions`, `## Revision prompts` |
| One-Page Revision Summary | `## One-Page Revision Summary` | `## One-page summary`, `## Revision Summary`, `## One-Page Summary` |

## Placeholder Detection
```python
if 'would be added in complete version' in content:
    is_complete = False
```

## Duplicate Display Names
Two files share "Cardiogenic shock" display name:
- `Heart Failure and Acute Cardiac Decompensation/Cardiogenic shock.md`
- `Syncope, Shock, and Acute Hemodynamic Emergencies/Cardiogenic shock.md`

When tracking unique completed topics, count = 19 unique names, 20 files.

## MOC & Hierarchy Sync Process
1. Read both tracking files
2. Build `display_name -> hierarchy_path` mapping from hierarchy
3. Build `display_name -> filepath` mapping from actual files
4. Verify all 6 sections exist (exact headers) + no placeholder text
5. Update MOC completed list from verified set
6. Update Hierarchy ✅ marks from same verified set
7. Both counts must match

## This Session's Additions
3 files completed with all 6 standard headers:
1. **Essential hypertension** - added SBA Questions (10), expanded MCQs (10), Viva Questions
2. **Cardiac tamponade** - added Learning Objectives  
3. **Mitral regurgitation** - added Learning Objectives

Total complete: 22 unique topics (20 files, 1 duplicate name)