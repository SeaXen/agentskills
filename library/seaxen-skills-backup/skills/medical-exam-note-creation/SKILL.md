---
name: medical-exam-note-creation
description: Create FCPS/MRCP exam-ready medical notes following the standardized template. Covers hepatology, cardiology, neurology, respiratory, and other specialties from Davidson's Principles and Practice of Medicine.
tags: [medical, fcps, mrcp, davidson, exam-prep, note-creation]
---

# Medical Exam Note Creation Skill

## Purpose
Create comprehensive, FCPS/MRCP exam-ready disease-level notes following the standardized Davidson Chapter template. Applicable to Hepatology, Cardiology, Neurology, Respiratory, Oncology, and other specialties.

## When to Use
- Building out Davidson chapter hierarchies with disease-level notes
- Creating FCPS/MRCP exam preparation materials
- Converting hierarchy scaffolds into full exam-ready notes

## Standard Template Structure (MANDATORY for every note)

Every disease-level note MUST include all 14 sections:

1. **Frontmatter** - tags, davidson_part, davidson_chapter, status, priority, exam_relevance, see_also, created, modified
2. **Learning Objectives** - 5-6 checkbox objectives
3. **Definition & Epidemiology** (or Pathophysiology) - table format
4. **Clinical Features / Presentation** - table format
5. **Classification / Staging / Grading** - table with scoring systems
6. **Diagnosis & Investigations** - table + Mermaid flowchart for algorithm
7. **Differential Diagnosis** - table with distinguishing features
7. **Management** - tables + Mermaid algorithm flowchart
8. **FCPS/MRCP High-Yield Summary** - bullet table of must-know facts
9. **Viva Questions** - 8-12 questions with expected answers
10. **Confusions & Mnemonics** - table + mnemonic
11. **Mind Map** - Mermaid diagram (mindmap syntax)
12. **One-Page Revision Card** - condensed table
13. **Spaced Repetition Trackers** - 6-interval table (Day 1, 3, 7, 14, 30, 90)
14. **Self-Test Scorecard** - 8-10 sections with /5 scoring
15. **Exam Answer Modes** - 5 modes table: Long Essay, Short Note, Viva, Ward Round, Last-Night
16. **MCQs (10) + SBAs (10) with Answer Keys** - FCPS/MRCP style
17. **Local Navigation** - wiki-links to parent, hierarchy, MOC, drugs, related topics

## Content Standards

### Tables
- Use Markdown tables with header rows
- Include units in column headers
- Align columns with pipes

### Mermaid Diagrams
- Use `flowchart TD` for algorithms
- Use `mindmap` for topic overviews
- Keep node labels concise (≤3 words)

### Viva Questions
- 8-12 questions per note
- Mix: definitions, criteria, management, differentials
- Answers must be precise, exam-ready, with key numbers

### Confusions & Mnemonics
- Table format: Confusion | Clarification
- Mnemonic: ACRONYM with each letter expanding to key fact

## Content Standards

### Tables
- Use Markdown tables with header rows
- Include units in column headers
- Align columns with pipes

### Mermaid Diagrams
- Use `flowchart TD` for algorithms
- Use `mindmap` for topic overviews
- Keep node labels concise (≤3 words)

### Viva Questions
- 8-12 questions per note
- Mix: definitions, criteria, management, differentials
- Answers must be precise, exam-ready, with key numbers

### Confusions & Mnemonics
- Table format: Confusion | Clarification
- Mnemonic: ACRONYM with each letter expanding to key fact

### Spaced Repetition Trackers
- 6 intervals: 24h, 3d, 7d, 14d, 30d, 90d
- 8-12 sections for scorecard, each /5

### Exam Answer Modes (5 modes per note)
| Mode | Prompt | Key Points |
|------|--------|------------|
| Long Essay | "Describe..." | Comprehensive structured answer |
| Short Note | "Write short note on..." | Key points only, bulleted |
| Viva | "What is...?" | Precise, numbered, key numbers |
| Ward Round | "Patient has X, action?" | Practical step-by-step |
| Last-Night | "Exam tomorrow, key facts?" | Ultra-condensed, mnemonics |

### MCQs & SBAs
- 10 MCQs + 10 SBAs per note
- FCPS/MRCP style with plausible distractors
- Answer keys provided

## Workflow

### Phase 1: Hierarchy Review
```bash
# Extract disease-level topics from hierarchy
grep "^\s*- \[" hierarchy.md
```

### Phase 2: Check Existing Files
```bash
# Check which topics already exist
find chapter_dir -name "*.md" | grep -v -iE "overview|template|hierarchy|hub|moc"
```

### Phase 3: Batch Creation (5-10 notes per session)
- Prioritize HIGH exam_relevance topics first
- Use template, fill all 13 sections
- Verify cross-links in Local Navigation

### Phase 4: Verification
```bash
# Count total files
find chapter_dir -name "*.md" | grep -v -iE "overview|template|hierarchy|hub|moc" | wc -l
```

## File Organization

```
Chapter Directory/
├── Davidson Chapter XX - Chapter Name Hierarchy.md
├── Chapter Name MOC.md
├── Section 1/
│   ├── Topic A.md
│   ├── Topic B.md
├── Section 2/
│   ├── Topic C.md
└── Templates/
    └── Chapter Name Topic Template.md
```

## Quality Checks

- [ ] All 13 sections present
- [ ] Frontmatter complete with exam_relevance
- [ ] Tables have units in headers
- [ ] Mermaid diagrams render correctly
- [ ] Viva questions have precise expected answers
- [ ] Local Navigation links correct (relative paths)
- [ ] No placeholder text remaining
- [ ] Cross-links to related topics use wiki-style `[[...]]`

## Pitfalls to Avoid

| Pitfall | Prevention |
|---------|------------|
| Missing sections | Use checklist of 13 sections |
| Placeholder text | Fill all sections before saving |
| Broken wiki-links | Use relative paths from file location |
| Missing units in tables | Include units in column headers |
| Broken Mermaid | Test syntax: `flowchart TD` or `mindmap` |
| Broken wiki-links | Use `[[../Section/Topic]]` format |

## Specialty-Specific Notes

### Hepatology
- Priority: ALF, cirrhosis complications, viral hepatitis, HCC, transplant
- Key scores: Child-Pugh, MELD, Maddrey, Lille, LI-RADS, BCLC
- Key algorithms: TG18 (cholecystitis/cholangitis), King's College, CLIF-C ACLF

### Cardiology
- Priority: ACS, HF, arrhythmias, valvular, hypertension
- Key scores: GRACE, TIMI, CHA2DS2-VASc, HAS-BLED, CHADS2
- Key algorithms: ACS pathway, HF management, AF rate/rhythm control

### Neurology
- Priority: Stroke, epilepsy, MS, movement disorders, headache
- Key scores: NIHSS, mRS, ASPECTS, HAS-BLED
- Key algorithms: Stroke pathway, status epilepticus, SAH management

### Endocrinology (Davidson Chapter 20)
- **Hierarchy Source**: Davidson 24th Edition Chapter 20 — 94 disease-level topics across 11 theme groups
- **Priority Groups**:
  1. **Highest**: Diabetic emergencies (DKA/HHS/Hypoglycaemia), Adrenal crisis, Thyroid storm, Myxoedema coma, Pituitary apoplexy, Hypocalcaemic tetany
  2. **High**: Cushing syndrome/disease, Acromegaly, Prolactinoma, Phaeochromocytoma, Primary aldosteronism, Primary hyperparathyroidism, MEN syndromes
  3. **Standard**: Thyroid disorders (Graves, nodular, cancer), Adrenal insufficiency, Diabetes pharmacotherapy, Reproductive endocrinology, Osteoporosis, Lipid disorders
- **Key Scores**: Burch-Wartofsky (thyroid storm), KDIGO (CKD-MBD), ATA risk stratification (DTC), MEN RET codon stratification
- **Key Algorithms**: Water deprivation test (DI/SIADH), OGTT for acromegaly, 1mg DST/HS cortisol (Cushing), TSH suppression targets (DTC), RET codon-based thyroidectomy timing (MEN2)
- **Chapter Structure**: 11 theme groups (General Principles, HPA, Thyroid, Adrenal, Parathyroid/Calcium, Reproductive, MEN, NETs, Emergencies, Special Topics, Pituitary Disorders)
- **Template Variation**: Used 14-section compact template (excludes MCQs/SBAs/Scorecards/Answer Modes for faster creation; add on demand)
- **File Organization**: Single flat directory with 94 topic files + 13 hub/scaffold files (MOC, Hierarchy, 11 theme hubs)
- **Stream Timeout Prevention**: Split large notes (>8K tokens) into multiple write_file calls; keep each under ~8K tokens
- **Hierarchy File**: `Davidson Chapter 20 - Endocrinology Hierarchy.md` contains full 94-topic inventory with status tracking

---

## Session Completion Checklist

After each session:
- [ ] Update hierarchy with ✅ for completed topics
- [ ] Update MOC progress tracker
- [ ] Git commit with descriptive message
- [ ] Note next 5-10 priority topics for next session

## Chapter Completeness Audit Protocol (Critical)

**Never trust MOC progress trackers.** They are routinely stale or wrong. Before claiming any chapter is "fully complete" or "100%", run a filesystem audit. This is the single most common source of user frustration with batch completion claims.

**Audit script**: `scripts/chapter-completeness-audit.py` (see skill directory). Usage:
```bash
python scripts/chapter-completeness-audit.py "/mnt/tb/Medicine/<Chapter Directory>"
```

**Reference**: `references/acute-medicine-chapter-9-completion-2026-06-15.md` — full session log showing the MOC-overclaim pattern (claimed 36/36, actually 24/32), the three gap classes, and pitfalls hit.

**What the audit catches**:
1. **MOC overclaim**: MOC says "36/36 complete" but only 30 files on disk, 6 of those with empty MCQ/SBA sections. Real completion: 24/30.
2. **Missing topic files**: MOC declares a topic (e.g., "ARDS", "Raised Intracranial Pressure") but no file exists for it.
3. **Partial files**: Topic file has full clinical content but empty `## MCQs (10)` section showing just `1.\n2.\n3.\n...\n10.\n` placeholders.
4. **Wrong status flag**: File has full content + completed MCQs but frontmatter still says `status: scaffold` instead of `status: full-fcps-mrcp-topic-note`.

**Honest completion criteria** — a topic is FULLY complete when ALL are true:
- File exists in chapter directory
- Frontmatter has `status: full-fcps-mrcp-topic-note`
- `## MCQs (10)` section has 10 fully-written questions (not just numbered placeholders)
- `## SBA Questions (10)` section has 10 fully-written questions
- `## Flashcards` section has ≥5 fully-written Q/A pairs
- `## Answer Key with Explanations` has answers for all 10 MCQs + 10 SBAs

## Reference: Round 2 Content-Depth Upgrade (Ch 8, 2026-06-16)

If a chapter reports 100% complete per `chapter_verify.py` but the user asks "is it actually with information or just scaffolded", run a **content-depth audit** (not just section-presence):

- **Templated phrases** to detect: "presents with characteristic features as defined in", "is a key topic in", "is recognised by its pathophysiology", "Always consider the full differential when assessing a patient"
- **Threshold**: `Clinical Features >800c` AND `Investigation/Management >800c` AND `not templated` = FULLY topic-specific
- **Bulk upgrade pattern**: build a flat `topic_data` dict (clinical_features, investigations, management, viva, differentials) per topic, then regex-replace the templated sections in one Python pass. See `references/pitfalls-38-41-round2-content-upgrade.md` in the related skill `medical-fcps-mrcp-note-creation` for the full 5-step pattern + 2-pass fix (Pass 1: replace sections; Pass 2: strip transitional opening like "X presents with characteristic features as defined in Davidson 24e Ch X.").

## Gap-Completion Workflow (When User Says "100% Complete")

When user says "fully complete all remaining" or "100% complete" for a chapter that audit shows is partial:

1. **Run the audit script first** — get honest list of (a) missing files declared in MOC but not on disk, (b) files with empty MCQ/SBA/Flashcard/Answer-Key sections despite having clinical content, (c) files with `status: scaffold` that have full content but were never flipped.

2. **For each missing file declared in MOC** → create new full 14-section topic note using individual `write_file`. NEVER batch in `execute_code`. Practical limit 1-2 new topics per session due to size.

3. **For each partial file with empty MCQ/SBA sections** → use `patch` with the exact placeholder string. The reliable placeholder signature is:
```
## MCQs (10)
1.
2.
...
10.

## SBA Questions (10)
1.
...
10.

## Flashcards
- Q:
  A:
- Q:
  A:
- Q:
  A:

## Answer Key with Explanations
### MCQs
1.
...
10.

### SBAs
1.
...
10.
```
Replace with 10 fully-written MCQs + 10 SBAs + 8-12 flashcards + complete answer key. Replacement string is large (~150-180 lines) so use a single `patch` per file.

4. **For each file with wrong status** → run `sed -i 's/status: scaffold$/status: full-fcps-mrcp-topic-note/'` on specific files. Check first with `grep -l "status: scaffold$"` because some scaffold files are legitimately scaffolds (MOC, hierarchy) and should NOT be flipped.

5. **Update MOC and Hierarchy** to honest counts. The 32/32 number is correct for Acute Medicine Ch 9; the previous "36/36" was a 12% overclaim.

6. **Verification before claiming complete**:
```bash
search_files pattern="status: full-fcps-mrcp-topic-note" target=content path=[chapter]
# Plus the audit script — both must agree
```

7. **Common partial-file MCQ content patterns** (use as fill-in-the-blank reference for these high-yield topics):
   - **Acid-base / electrolytes**: ABG interpretation stepwise + Winter's + MUDPILES + hyperK ladder + correction limits
   - **Shock**: classify by type (cool/warm + JVP) + lactate target + EGDT
   - **ACS**: STEMI criteria + PCI/fibrinolysis timing + GRACE + DAPT + mechanical complications
   - **AKI**: KDIGO + FENa + AEIOU + CRRT vs IHD + HRS treatment
   - **ALF**: King's College + paracetamol + cerebral oedema + INR rule
   - **DKA/HHS**: criteria + FRII 0.1 U/kg/h + K⁺ protocol + cerebral oedema + resolution criteria
   - **ARDS**: Berlin 2012 + TV 6 mL/kg PBW + prone/PROSEVA + NMJ/ACURASYS + ECMO
   - **ICP**: Monro-Kellie + Cushing's triad + herniation + mannitol + 3% saline

## Pitfalls When Filling Partial Files

- **Garbled SBA answer keys**: When writing answer keys with multiple-choice options, the `^answer` line can become "**A. Correct**" but if you write a calculation explanation inline, the `+` and `-` patch markers can collide. Always end each answer key line with a clear `— Reason` separator and avoid inline math that could be misread as patch syntax.
- **Duplicate stub sections**: After patching, the old "### SBAs\n1.\n2.\n..." stub can be left at file end if your `old_string` was anchored only at the start. Always `tail -20` the file after patching to verify no leftover empty stub.
- **Wrong-sed risk**: `sed -i 's/status: scaffold$/'` will also flip the MOC and hierarchy files. Always check the audit script's `scaffold_status` count BEFORE and AFTER sedding — it should decrease by exactly the number of files you intended to flip.