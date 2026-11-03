# Parallel Directory Format Pitfall — "Two Sets of Subdirs in One Chapter"

## Problem
Some chapters have **two parallel sets of section subdirectories** coexisting in the same chapter root:

```
/mnt/tb/Medicine/Cardiology/
├── 01_Cardiac_Investigations/         ← new (hierarchy-aligned)
├── 02_Acute_Coronary_Syndromes/
├── ...
├── Adult Congenital Heart Disease and Cardiac Shunts/   ← old (preserved)
├── Arrhythmias and Cardiac Conduction Disorders/
├── ...
```

This happens when:
- A previous batch created the old format (named with spaces, no numbering)
- The user later asked to align with the hierarchy file (numbered prefixes)
- The old format was never deleted because some files had valuable manually-written content

## How to Detect

1. List the chapter root: `ls /mnt/tb/Medicine/<Chapter>/`
2. Look for directories with TWO naming patterns:
   - `<NN>_<Underscored_Name>/` (new format, hierarchy-aligned)
   - `<Name with spaces>/` (old format, manually created)
3. Count full-fcps-mrcp-note files in each set — old format usually has 5-15, new format has hundreds of scaffolds

## Resolution Strategy (Cardiology 2026-06-15)

**Do NOT delete old format.** Preserve the 111 manually-written full notes.

1. **Identify the new-format directory list** (matches `^\d+_` regex)
2. **Map hierarchy sections to new-format directories** via `section_to_dir` dict
3. **Map hierarchy sections to old-format directory names** for reference
4. **For the user's "100% complete" goal, work in the new format**
5. **Preserve old format as additional reference material**
6. **Update MOC** to show both: "New format: 564 / Old format: 111 / Total: 675"

## Mapping Cheatsheet (Cardiology)

| New Format Dir | Old Format Dir |
|----------------|----------------|
| 01_Cardiac_Investigations | Clinical Assessment, Hemodynamics, and Cardiac Investigations |
| 02_Acute_Coronary_Syndromes | Ischaemic Heart Disease and Acute Coronary Syndromes |
| 03_Chronic_Coronary_Syndromes | (none — new section) |
| 04_Heart_Failure | Heart Failure and Acute Cardiac Decompensation |
| 05_Valvular_Heart_Disease | Valvular Heart Disease and Murmur Syndromes |
| 06_Infective_Endocarditis | (rolled into Pericardial old) |
| 07_Pericardial_Diseases | Pericardial, Endocardial, and Inflammatory Cardiac Disease |
| 08_Arrhythmias | Arrhythmias and Cardiac Conduction Disorders |
| 08_Cardiac_Devices_EP | (new section) |
| 09_Cardiomyopathies | Cardiomyopathies and Myocardial Disease |
| 10_Adult_Congenital_Heart_Disease | Adult Congenital Heart Disease and Cardiac Shunts |
| 11_Pulmonary_Hypertension | (new section) |
| 12_Aortic_Diseases | (new section) |
| 13_Systemic_Cardiac | (new section) |
| 14_Hypertension_CV_Risk | Hypertension and Cardiovascular Risk States |
| 15_Special_Populations | (new section) |
| 16_Cardiac_Emergencies | Syncope, Shock, and Acute Hemodynamic Emergencies |

## Orphan Scaffold Pattern

When a chapter has both old and new formats, you may find **orphan scaffold files** in the new-format dirs that don't match the hierarchy's topic names:

```
13_Systemic_Cardiac/
├── Rheumatoid_Arthritis_pericarditis_nodules_vasculitis.md   ← orphan
├── SLE_pericarditis_Libman_Sacks_endocarditis_accelerated_CAD.md   ← orphan
└── ...
```

These are usually topics with **longer descriptive filenames** that get truncated/normalized in the hierarchy's clean topic list. They are NOT in the organized topic list but are still valid disease topics worth covering.

**Fix**: Run a second batch upgrade to convert all orphan scaffolds to full notes. Don't delete them — they add value (more specific topic variants).

## How to Detect Orphans

```python
import json
from pathlib import Path
import re

base = Path("/mnt/tb/Medicine/Cardiology")
new_dir_pattern = re.compile(r'^\d+_')

# Load organized (hierarchy-aligned) topics
with open("/tmp/cardio_topics_organized.json") as f:
    organized = json.load(f)

topic_paths = set(t["path"] for t in organized)

orphans = []
for d in base.iterdir():
    if d.is_dir() and new_dir_pattern.match(d.name) and d.name != 'Templates':
        for f in d.glob("*.md"):
            if str(f) not in topic_paths:
                # Read frontmatter to extract original topic
                content = f.read_text()
                topic_match = re.search(r'^topic:\s*"?([^"\n]+)"?', content, re.MULTILINE)
                if topic_match:
                    orphans.append({
                        "path": str(f),
                        "topic": topic_match.group(1).strip(),
                        # ... other frontmatter fields
                    })

print(f"Found {len(orphans)} orphan scaffolds")
```

## Pitfall: Don't Merge Old and New

The user's mental model is "Cardiology folder". When they ask for 100% coverage, they mean the new hierarchy-aligned structure. The old format is bonus material. Reporting "111 full + 564 full = 675" is honest; reporting "Cardiology has X" without context is misleading.

## Cross-Reference Sections to Check

For each new-format directory, check if there's a corresponding old-format directory with manually-written content. If so, preserve it but build out the new format to match the hierarchy.
