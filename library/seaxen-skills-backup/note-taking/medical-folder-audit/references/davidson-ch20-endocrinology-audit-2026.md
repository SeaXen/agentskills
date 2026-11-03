# Davidson Chapter 20 Endocrinology — Audit Case Study (June 2026)

## Summary
- **Folder**: `/mnt/tb/Medicine/Endocrinology/`
- **Textbook**: Davidson's Principles and Practice of Medicine, 24th Edition, Chapter 20: Endocrinology
- **Expected topics (per Hierarchy)**: 94 disease-level topics across 11 theme groups
- **Actual disk files**: 87 disease-level files + 13 hub/tracking files = 100 total

## Findings
| Metric | Hierarchy / MOC Claim | Disk Reality |
|--------|----------------------|--------------|
| Total topics listed | 94 | 87 disease files |
| Completion % (MOC tracker) | 0% (all 11 groups) | 100% (87/87 files `full-fcps-mrcp-note`) |
| Template used | Not specified | 14-section Davidson standard (extended) |
| Question banks | Not checked | MCQ/SBA/Viva/Flashcards present in all files |

## Key Discrepancies
1. **Hierarchy inventory tables**: All 94 topics marked `status: scaffold` — completely stale
2. **MOC progress tracker**: 0% for all theme groups — entirely disconnected from reality
3. **Hub files**: Correctly `scaffold-hub` but internal tables reference outdated statuses

## Template Variant Detected
**14-section Davidson Standard (Extended)** — All disease-level files contain:
- Learning Objectives
- Definition & Epidemiology
- Aetiology / Pathophysiology
- Clinical Features
- Diagnosis / Investigation Algorithm
- Differential Diagnosis
- Management (Medical/Surgical/Emergency)
- Special Situations (Pregnancy, Elderly, CKD, etc.)
- Monitoring & Follow-up
- Exam Pearls (FCPS/MRCP)
- Confusions & Mnemonics
- Mermaid Mind Map
- One-Page Revision Card
- Spaced Repetition Trackers + Self-Test Scorecard
- Local Navigation

**Plus**: MCQ/SBA question banks, Viva questions, Flashcards embedded in relevant sections

## Root Cause
Tracking files (MOC, Hierarchy) were created as scaffolds at folder inception and never updated as disease-level files were completed. The completion workflow updates individual topic files but not the aggregate trackers.

## Fix Applied
- Verified all 87 disease files have `status: full-fcps-mrcp-note` and complete 14-section content
- Confirmed 7/10 "missing" hierarchy topics exist as files with minor naming differences (e.g., "Pheochromocytoma/Paraganglioma" → `Phaeochromocytoma-Paraganglioma.md` — UK/US spelling)
- 3 hierarchy topics are subsumed into existing files (Non-Functioning Adenoma → `Pituitary Adenomas- Non-Functioning.md`, Bronchial/Kulchitsky NETs → `Bronchial NETs.md`, WHO 2019 Grading → `WHO 2019 NET Grading.md`)
- Bonus files not in hierarchy: `Iodine Deficiency & Excess.md`, `Thyroid in Pregnancy.md`, `Thyroid Eye Disease.md`

## Lessons for Future Audits
1. **Always scan disk files directly** — compute completion from file frontmatter + section count, never trust MOC/Hierarchy summary tables
2. **Cross-reference hierarchy topic list to actual files** using fuzzy matching (handle spelling differences, abbreviation styles)
3. **Expect chapter-specific template extensions** — Davidson Ch 20 uses a richer 14-section template than the standard 6-section or emoji/plain variants
4. **Track "hub" files separately** — they are correctly `scaffold-hub` but their internal inventory tables drift
5. **Update tracking files as a batch** — after confirming disk reality, update MOC progress tracker + Hierarchy inventory in one pass