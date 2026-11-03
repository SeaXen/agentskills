# Cardiology Audit & Completion Workflow

## Situation
Cardiology chapter at `/mnt/tb/Medicine/Cardiology/` had inconsistent tracking:
- MOC claimed 40 complete (mostly skeleton files)
- Hierarchy had 16 ✅ marks
- Reality: 25 truly complete notes (6/6 sections) — **later refined to 22** after removing placebo entries with "would be added in complete version" text
- Duplicate skeleton Pericardial directory existed
- 24 files missing "Common Viva Questions" section

## Audit Method (Reusable for Any Chapter)

### 1. Discover Actual File Structure
```python
# List all main directories and their .md files with sizes
import os
main_dirs = ['Arrhythmias...', 'Cardiomyopathies...', ...]
for d in main_dirs:
    for f in os.listdir(path):
        size = os.path.getsize(filepath)
        # categorize by size and content
```

### 2. Verify Content Completeness (Not Size!)
Check for all 6 required sections:
```python
has_lo = '## Learning Objectives' in content
has_mgmt = '## Management' in content
has_mcq = '## MCQs' in content
has_sba = '## SBA Questions' in content
has_viva = '## Common Viva Questions' in content
has_rev = '## One-Page Revision Summary' in content
score = sum([has_lo, has_mgmt, has_mcq, has_sba, has_viva, has_rev])
# score == 6 = truly complete
```

**Critical**: Check for placeholders that indicate NOT complete:
```python
if 'would be added in complete version' in content:
    # This file is a skeleton despite having 6 sections
    is_complete = False
```

### 2b. Standard Header Names
The 6 required sections MUST use exact header names:
| Required | Exact Header |
|----------|--------------|
| Learning Objectives | `## Learning Objectives` |
| Management | `## Management` |
| MCQs | `## MCQs` |
| SBA Questions | `## SBA Questions` |
| Common Viva Questions | `## Common Viva Questions` |
| One-Page Revision Summary | `## One-Page Revision Summary` |

Files using variant headers (`## Treatment`, `## Viva`, `## One-page summary`, `## Revision`) do NOT count as complete.

### 3. Build Hierarchy ↔ File Mapping
Display names in hierarchy often differ from file names:
| Hierarchy Display | Actual Filename |
|------------------|----------------|
| Atrioventricular block | AV block and conduction disorders.md |
| Monomorphic ventricular tachycardia | Ventricular tachycardia and VF.md |
| Unstable angina | Unstable angina and NSTEMI.md |

Build mapping before cross-referencing.

**Note on duplicate display names**: Some files in different directories share the same display name (e.g., `Cardiogenic shock.md` in both `Heart Failure...` and `Syncope, Shock...`). Count unique display names for tracking, not file count.

### 4. Cross-Validate Tracking Files
```python
# MOC completed
moc_completed = set(re.findall(r'✅ \[\[.*?\|(.*?)\]\]', moc_content))

# Hierarchy completed
for line in hier_content.split('\n'):
    if indent == 4 and '✅' in line:
        # extract display name
        hier_completed.add(display_name)

# Actual complete
actual_complete = set(full_file_names)

# All three must align
assert moc_completed == actual_complete
assert hier_completed.issubset(actual_complete)
```

### 5. Fix Missing Sections in Batch
For 24 files missing Viva:
```python
# Pre-defined viva questions per topic
viva_map = {
    'Hypertrophic cardiomyopathy.md': [...],
    'Mitral stenosis.md': [...],
    # etc.
}
# Insert after Flashcards/Answer key section
# Update both MOC and Hierarchy ✅ marks
```

### 6. Clean Up Duplicate Directories
```bash
rm -rf "/mnt/tb/Medicine/Cardiology/Pericardial | Endocardial |+Inflammatory Cardiac Disease"
```

### 7. Update Tracking Files
- MOC: List only truly complete with `verified 6-section` note and count
- Hierarchy: Mark exact leaf topics that match actual files
- Update counts: "verified 6-section FCPS/MRCP notes: 22"

## Key Principles

1. **Size ≠ Complete** — Always verify sections
2. **Names Differ** — Build explicit hierarchy→file mapping
3. **Sync MOC + Hierarchy** — Update both from single source of truth
4. **Batch Update** — Use scripts for systematic section addition
5. **Conservative Counts** — Report verified numbers, not inflated ones
6. **Watch for Placeholders** — "would be added in complete version" = NOT complete
7. **Exact Header Names** — Variant headers don't count
8. **Deduplicate Display Names** — Multiple files can share a name

## Results for Cardiology
- **Before**: MOC 40, Hierarchy 16, Reality 25 (inflated)
- **After**: MOC 22, Hierarchy 22/103, Reality 22 ✅
- **3 new completed this session**: Essential hypertension, Cardiac tamponade, Mitral regurgitation
- **Remaining**: 81 skeleton/partial files need MCQs+SBAs+Viva+Revision (+Learning Objectives if missing)
- **Duplicate removed**: Yes