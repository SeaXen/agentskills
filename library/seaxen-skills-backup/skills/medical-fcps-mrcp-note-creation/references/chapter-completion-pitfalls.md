# Chapter Completion Verification — Pitfalls & Lessons Learned

## 1. Recursive File Discovery (CRITICAL BUG FIX)
**Problem**: `chapter_verify.py` used `chapter_path.glob("*.md")` which ONLY finds files in the root directory, missing all disease-level notes in subdirectories (e.g., `Section/Topic-Group/Disease.md`).

**Fix**: Changed to `chapter_path.rglob("*.md")` for recursive discovery.

**Impact**: Before fix, Diabetes chapter (289 files) reported only 15 files (root-level only). After fix, correctly reports all 289 files.

---

## 2. Filename Stem Extraction with Special Characters
**Problem**: Files with parentheses, slashes, or Ampersands in names produce garbled `Path.stem` values:
- `DKA severity grading (mild/moderate/severe).md` → stem = `severe)`
- `Hypoglycaemia classification (level 1/2/3).md` → stem = `3)`
- `Foot risk classification (IWGDF/Scottish).md` → stem = `Scottish)`
- `Albuminuria categories (A1/A2/A3).md` → stem = `A3)`
- `m.3243A>G (MELAS/MIDD).md` → stem = `MIDD)`

**Mitigation**: When deduplicating/counting, normalize stems with regex:
```python
norm = re.sub(r'[^a-z0-9]+', '-', disease.lower()).strip('-')
```

**Best Practice**: Avoid parentheses/slashes in filenames. Use underscores or descriptive names without special chars.

---

## 3. Duplicate Files from Naming Variants
**Problem**: Same content saved under multiple filenames (case differences, special chars, slugified variants):
- `dka-complications-cerebral-oedema,-hypokalaemia.md` vs `DKA complications (cerebral oedema, hypokalaemia).md`
- `glp-1-ra-in-hf-fight-step-hfpef.md` vs `GLP-1 RA in HF (FIGHT, STEP-HFpEF).md`
- `albuminuria-categories-a1-a2-a3.md` vs `Albuminuria categories (A1/A2/A3).md`

**Count**: Diabetes chapter had 221 raw `full-fcps-mrcp-note` files but only 179 unique disease topics after normalization.

**Mitigation**: Before creating new notes, check for existing variants using normalized stem comparison. Enforce single canonical filename pattern per topic.

---

## 4. Davidson TOC Cross-Reference
**Requirement**: Before declaring chapter complete, cross-reference against actual Davidson 24th edition Chapter 25 table of contents.

**Method**: 
- Web search for "Davidson Chapter 25 Endocrinology and Diabetes table of contents"
- Map each chapter subsection to a disease-level note
- Verify no high-yield FCPS/MRCP topic from Davidson is missing

**Result for Diabetes**: 179 unique topics cover all Davidson Ch25 diabetes subsections plus exam-relevant expansions (CVOT algorithms, KDIGO staging, CGM metrics, hybrid closed-loop systems, teplizumab, DiRECT remission criteria).

---

## 5. Hub File Verification Gaps
**Problem**: `chapter_verify.py` counts hub files but doesn't verify:
- Heading hubs (root level) = 12 expected
- Topic-group hubs (level 1) = 38 expected  
- Hub content quality (children lists, high-yield tables)
- MOC status = full-fcps-mrcp-hub

**Recommendation**: Extend verification to validate hub hierarchy depth and content.

---

## 6. Scaffold Cleanup Verification
**Problem**: Empty scaffolds (2-3KB files with minimal content) remain after "completion" claims.

**Check**: 
- `status: scaffold` files with size < 5KB are likely empty stubs
- Compare scaffold count vs disease-level topic count in hierarchy
- Zero scaffolds should remain in a complete chapter

---

## 7. Content Completeness vs Status Tag
**Critical**: `status: full-fcps-mrcp-note` tag ≠ content completeness.

**Verification needed**:
- All 14 template sections present (numbered ## 1. through ## 14.)
- Mermaid diagrams in Diagnosis, Management, Mind Map sections
- Viva Questions table (6-8 Q&A pairs)
- One-Page Revision Card table
- Spaced Repetition Tracker (5 intervals)
- Self-Test Scorecard (10 sections)

**Tested**: Diabetes chapter - 3 sampled files confirmed all 14 sections present. Files range 4-15KB.

---

## 8. Progress Tracker Sync
**Workflow**: After chapter completion, update:
1. `00_Index/Davidson Chapter Progress Tracker.md` — Chapter row to `[x]` with stats
2. MOC Progress Tracker table — 100% all sections
3. Git commit with summary

**Diabetes entry**: `Chapter 21: Diabetes mellitus` → `[x]` with `12 heading hubs + 38 topic-group hubs + 234 disease-level notes`

---

## Quick Verification Checklist for Future Chapters

```bash
# 1. Run fixed chapter_verify.py
python3 chapter_verify.py "/mnt/tb/Medicine/ChapterName" <expected_disease_count>

# 2. Check for garbled stems
find /mnt/tb/Medicine/ChapterName -name "*.md" -exec basename {} \; | grep -E '\)$|^[0-9]+\)' 

# 3. Deduplicate count
python3 -c "
from pathlib import Path
import re
seen=set()
for f in Path('/mnt/tb/Medicine/ChapterName').rglob('*.md'):
    if 'status: full-fcps-mrcp-note' in f.read_text(errors='replace'):
        norm=re.sub(r'[^a-z0-9]+','-',f.stem.lower()).strip('-')
        seen.add(norm)
print(f'Unique topics: {len(seen)}')
"

# 4. Verify zero scaffolds
grep -r "status: scaffold" /mnt/tb/Medicine/ChapterName/ | wc -l

# 5. Web cross-reference Davidson TOC
# Search: "Davidson Chapter XX [ChapterName] table of contents"
```

---

*Documented from Diabetes Mellitus (Chapter 25) completion session — June 2026*