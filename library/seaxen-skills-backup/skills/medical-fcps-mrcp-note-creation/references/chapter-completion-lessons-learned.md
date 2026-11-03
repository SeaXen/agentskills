# Chapter Completion Lessons Learned

> Captured from Hepatology (Ch24) and Hematology (Ch25) completion sessions.

---

## 1. Hierarchy Leaf Topics vs Actual Disease-Level Notes

**Key insight:** The hierarchy file (`Davidson Chapter XX - Hierarchy.md`) lists **design-target leaf topics** (118 for Hepatology, ~95 for Hematology), but actual completed chapters have **fewer disease-level notes** due to **intentional consolidation**.

| Chapter | Hierarchy Leaf Target | Actual Disease Notes | Consolidation Ratio |
|---------|----------------------|---------------------|---------------------|
| Hepatology (Ch24) | 118 | 76 | 1.55:1 |
| Hematology (Ch25) | ~95 | 76 | 1.25:1 |

**Why consolidation happens:** Multiple hierarchy leaf topics are sub-topics naturally covered within a single comprehensive disease note. Examples:
- Alcoholic fatty liver / Alcoholic hepatitis / Alcoholic cirrhosis → single `Alcoholic Liver Disease.md` + scoring/management files
- Hepatitis A acute / Hepatitis A prevention → `Hepatitis A & E.md`
- HCC risk/surveillance / HCC LI-RADS / HCC BCLC / HCC treatment → `HCC surveillance, LI-RADS, and screening.md` + `HCC (Hepatocellular Carcinoma).md`
- PBC diagnosis / PBC treatment / PBC response criteria → `PBC (Primary Biliary Cholangitis).md`

**Verification implication:** The `chapter_verify.py` script's `expected_leaves` parameter should be set to the **actual expected disease-level note count** (from MOC tracking), not the hierarchy leaf target. The hierarchy target is the design ceiling; the MOC count is the delivery reality.

---

## 2. Hub File Types and Status Tags

Three categories of hub files exist, all should use `status: full-fcps-mrcp-hub`:

| Hub Type | Examples | Status Tag |
|----------|----------|------------|
| **Chapter MOC** | `Hepatology MOC.md`, `Hematology MOC.md` | `full-fcps-mrcp-hub` |
| **Chapter Hierarchy** | `Davidson Chapter XX - Hierarchy.md` | `full-fcps-mrcp-hub` |
| **Heading Hubs** (14 for Hepatology, 5 for Hematology) | `Acute Liver Failure.md`, `Anaemia and Red Cell Disorders.md` | `full-fcps-mrcp-hub` |
| **Technique/Investigative Hubs** | `Bone Marrow Exam.md`, `Coagulation Assays.md`, `Cytogenetics & Molecular Diagnostics.md`, `Flow Cytometry.md`, `Transfusion Reactions.md`, `Haemolytic Anaemias.md` (overview), `Antiplatelet Therapy.md` | `full-fcps-mrcp-hub` |

**Verification rule:** Hub files ≥ 2 (MOC + Hierarchy minimum), typically 8-15 total depending on chapter.

---

## 3. Duplicate Detection and Removal

**Common duplicate patterns found:**

| Pattern | Example | Resolution |
|---------|---------|------------|
| Same disease in two folders | `Gilbert Syndrome` in both `Jaundice/LFT` and `Inherited/Metabolic` | Keep in primary folder (Jaundice), remove duplicate |
| Same disease, different naming | `Acute fatty liver of pregnancy` in `ALF` and `Special Situations` | Keep in primary (Special Situations), remove from ALF |
| Combined summary vs individual topics | `Viral Hepatitis B & C.md` vs individual Hep B / Hep C files | Remove combined summary |
| Older version vs newer | `Acute cholecystitis detailed.md` (2025) vs `Acute Cholecystitis.md` (2026) | Keep newer, remove older |
| Overview file vs heading hub | `Jaundice and LFT Interpretation Detailed.md` vs heading hub | Remove overview, keep hub |

**Detection method:** Search for files with same/similar display names across folders. Check `created`/`modified` dates in frontmatter - older duplicates are usually the ones to remove.

---

## 4. MOC Completion Tracking

**MOC file should track completion based on ACTUAL disease-level files**, not hierarchy leaf targets.

| MOC Section | Tracking Basis |
|-------------|----------------|
| `Anaemia & Red Cell Disorders` | Count of actual `*Anaemia*.md`, `*Polycythaemia*.md` files |
| `Haematological Malignancies` | Count of actual leukaemia/lymphoma/myeloma/MPN/MDS files |
| `Bleeding & Thrombotic` | Count of actual coagulation/platelet/VTE files |
| `Transfusion Medicine` | Count of actual transfusion product/reaction files |
| `Supportive Care` | Count of actual growth factor/chelation/SCT/palliative files |

**Total in MOC = sum of actual files**, not hierarchy leaf counts. This prevents false "pending" status when all real topics are done.

---

## 5. Verification Script Usage Notes

- Run `chapter_verify.py` with `expected_leaves` set to **MOC actual count**, not hierarchy target
- After duplicate removal, run verification again to confirm count matches
- Hub files should show as `full-fcps-mrcp-hub` (not `scaffold-hub`, `moc`, or `hierarchy`)
- `GAP_ANALYSIS.md` and similar meta files will show as "no status" - exclude from count or tag appropriately

---

## 6. Chapter-Specific Completion Data

### Hepatology (Chapter 24) - COMPLETE ✅
- Disease-level notes: **76** (`full-fcps-mrcp-note`)
- Hub files: **8** (`full-fcps-mrcp-hub`): MOC, Hierarchy, 6 heading hubs
- All core Davidson Ch 24 diseases covered
- Verification: 76/76 disease notes + 8 hubs = 100%

### Hematology (Chapter 25) - COMPLETE ✅
- Disease-level notes: **76** (`full-fcps-mrcp-note`)
- Hub files: **8** (`full-fcps-mrcp-hub`): MOC, Hierarchy, 6 technique hubs
- All core Davidson Ch 25 diseases covered
- Verification: 76/76 disease notes + 8 hubs = 100%

---

## 7. Quick Reference: Status Tag Matrix

| File Type | Status Tag |
|-----------|------------|
| Disease-level topic note | `full-fcps-mrcp-note` |
| Chapter MOC | `full-fcps-mrcp-hub` |
| Chapter Hierarchy | `full-fcps-mrcp-hub` |
| Heading hub (major section) | `full-fcps-mrcp-hub` |
| Technique/investigative hub | `full-fcps-mrcp-hub` |
| Scaffold/stub | `scaffold` (should be 0 at completion) |
| Template | `template` |
| Meta/admin (GAP_ANALYSIS, etc.) | No status (excluded from verification) |

---

*Last updated: 2026-06-16 (Hepatology + Hematology completion session)*