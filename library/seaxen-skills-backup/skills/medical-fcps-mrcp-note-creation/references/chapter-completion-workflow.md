# Chapter Completion Workflow

## Overview
This document captures the repeatable workflow for verifying and completing a Davidson Medicine chapter to FCPS/MRCP standard. Based on the Hepatology (Chapter 24) completion session.

## Prerequisites
- Chapter hierarchy file exists with `expected_leaf_count` documented
- MOC file exists
- All disease-level topic files exist (some may be scaffolds, duplicates, or mis-tagged)

## Step-by-Step Process

### 1. Run Verification Baseline
```bash
python3 ~/.hermes/skills/medical-fcps-mrcp-note-creation/scripts/chapter_verify.py \
  "/mnt/tb/Medicine/<Chapter Name>" <expected_leaf_count>
```
Record the output — note:
- Total topic files found vs expected
- Hub file count (should be ≥2: MOC + Hierarchy)
- Scaffold files remaining
- Files with no status tag

### 2. Fix Hub File Statuses
Update all hub files to `status: full-fcps-mrcp-hub`:
- **MOC file** (e.g., `Hepatology MOC.md`)
- **Hierarchy file** (e.g., `Davidson Chapter 24 - Hepatology Hierarchy.md`)
- **All heading hub files** (one per major section, typically 13-14)
  - Usually located at `/mnt/tb/Medicine/<Chapter>/<Section Name>/<Section Name>.md`
  - Often incorrectly tagged as `full-fcps-mrcp-note` or `scaffold-hub`

```bash
# Example patch for each hub file
patch --path "/mnt/tb/Medicine/Hepatology/Hepatology MOC.md" \
  --old_string "status: moc" --new_string "status: full-fcps-mrcp-hub"
```

### 3. Identify and Remove Duplicates
Common duplicate patterns (check these locations):

| Duplicate Type | Where to Look | Resolution |
|---|---|---|
| Same disease in multiple sections | e.g., Gilbert Syndrome in both `Jaundice and LFT Interpretation/` AND `Inherited and Metabolic Liver Disease/` | Keep the more comprehensive version; remove the other |
| Older (2025) vs newer (2026) versions | Same folder, similar names (e.g., `Acute Cholecystitis.md` vs `Acute cholecystitis detailed.md`) | Keep newer (check `created:` date in frontmatter) |
| Combined summary vs individual topics | e.g., `Viral Hepatitis B & C.md` vs individual `Hepatitis B*.md` + `Hepatitis C*.md` | Remove combined summary; keep individual disease files |
| Overview/detailed in same folder | e.g., `Jaundice and LFT Interpretation Detailed.md` vs hub file | Remove overview; hub already exists |
| Cross-folder functional duplicates | e.g., `HCC surveillance.md` in both `Cirrhosis Complications/` and `Liver Tumours/` | Keep in most logical location (Liver Tumours for HCC) |

Use `read_file` to compare content before deleting.

### 4. Re-run Verification
```bash
python3 ~/.hermes/skills/medical-fcps-mrcp-note-creation/scripts/chapter_verify.py \
  "/mnt/tb/Medicine/<Chapter Name>" <expected_leaf_count>
```

### 5. Verify Pass Criteria
- ✅ Topic notes == expected_leaf_count (e.g., 118 for Hepatology)
- ✅ Hub files ≥ 2 (MOC + Hierarchy + heading hubs)
- ✅ Scaffold files == 0
- ✅ Files with no status == 0

### 6. Git Commit
```bash
cd /mnt/tb/Medicine && git add -A && git commit -m "<Chapter>: Complete Chapter XX Davidson 24th ed
- Fixed hub file statuses
- Removed X duplicate files
- Verified: Y/Y disease-level topics + Z hubs = 100% complete" && git push origin main
```

## Hepatology (Chapter 24) Reference Numbers
- **Expected disease-level topics**: 118
- **Heading hubs**: 14
- **Topic-group hubs**: 42
- **Total hub files after completion**: 15 (MOC + Hierarchy + 13 heading hubs)
- **Sections**: Jaundice/LFT, ALF, Viral Hepatitis, Chronic Liver Disease, Portal HTN, ALD, NAFLD, Autoimmune, DILI, Inherited/Metabolic, Biliary Tract, Liver Tumours, Liver Transplant, Special Situations

## Quick Duplicate Detection Commands
```bash
# Find all files with full-fcps-mrcp-note status
grep -rl "status: full-fcps-mrcp-note" /mnt/tb/Medicine/Hepatology/

# Check for duplicate filenames across subdirectories
find /mnt/tb/Medicine/Hepatology -name "*.md" -exec basename {} \; | sort | uniq -d

# Find files with scaffold status
grep -rl "status: scaffold" /mnt/tb/Medicine/Hepatology/

# Find files with no status tag
find /mnt/tb/Medicine/Hepatology -name "*.md" -exec sh -c 'grep -q "status:" "$1" || echo "$1"' _ {} \;
```

## Common Pitfalls
1. **Don't assume hierarchy count is accurate** — always verify against actual disease-level topics in the hierarchy file
2. **Heading hub files often masquerade as topic notes** — check for files named `<Section Name>.md` in section folders
3. **Case-sensitive duplicates** — `Acute Cholecystitis.md` vs `Acute cholecystitis detailed.md` are different files
4. **Cross-chapter contamination** — Gastroenterology (Ch23) and Hepatology (Ch24) are separate; don't mix
5. **Old 2025 scaffold files** — many folders have both a 2025 scaffold and 2026 full note; keep 2026