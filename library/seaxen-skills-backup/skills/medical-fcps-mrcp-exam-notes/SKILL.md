---
name: medical-fcps-mrcp-exam-notes
description: "Create FCPS/MRCP exam-oriented medical notes following Davidson Medicine curriculum structure. Full disease-level notes with standardized template including: learning objectives, pathophysiology mermaid diagrams, diagnostic algorithms, management flowcharts, FCPS/MRCP high-yield tables, viva questions, mind maps, one-page revision cards, spaced repetition trackers, self-test scorecards, and local navigation. Follows Davidson 24th Edition chapter hierarchy with topic-group hubs, heading hubs, and disease-level topics."
version: 1.0.0
author: Hermes Agent
license: CC0-1.0
metadata:
  hermes:
    category: productivity
    tags: [medical, exam-preparation, fcps, mrcp, davidson-medicine, medical-notes, exam-preparation, template, davidson-24]
---

# Medical FCPS/MRCP Exam Notes Creation

**Class-level skill for creating FCPS/MRCP exam-oriented medical notes following Davidson Medicine 24th Edition curriculum structure.**

Use this skill when the user wants to create comprehensive, exam-ready medical notes for FCPS (Fellowship of College of Physicians and Surgeons) and MRCP (Membership of Royal College of Physicians) exam preparation, following the Davidson's Principles and Practice of Medicine 24th Edition curriculum structure.

## When to Use This Skill

**Always use when:**
- User wants to create disease-level medical notes for FCPS/MRCP exam preparation
- User wants to build a structured medical notes system following Davidson 24th Edition hierarchy
- User requests "complete the chapter" or "make all topics complete" for a Davidson chapter
- User wants to create a standardized medical notes system with exam-focused content
- User references "Davidson 24th edition" or "FCPS/MRCP" in the context of note creation

**Don't use when:**
- Creating general academic assignments (use `academic-assignment-writing`)
- Creating implementation plans for code (use `writing-plans`)
- Creating general medical notes not tied to FCPS/MRCP exam structure

## Secondary high-yield source: Abdullah Tanvir Drive mirror

Dr. Sagar maintains a **public Google Drive** Davidson 24th review library (Abdullah Tanvir, `#DAVIDSON_REVIEW`) mirrored at:

`/mnt/tb/Medicine/External/Abdullah-Tanvir-Davidson-Drive/` (`.txt` + `.docx`)

**Use it as an exam-frequency overlay** — starred Davidson tables, inline SBA/MCQ with sitting dates — when drafting SBAs or enriching high-yield sections. **Do not** replace `/mnt/tb/Medicine` `full-fcps-mrcp-note` disease files with these table-only exports unless the user explicitly asks to merge.

- Ingest / re-sync: skill `public-google-drive-ingest` → `references/abdullah-tanvir-drive-mirror-2026-06-25.md`
- Agent digest after ingest: `AGENT_LEARNED.md` in the mirror folder
- Drive updates over time → re-run `~/.hermes/scripts/abdullah-tanvir-drive-{ingest,export-docx,cleanup}.py`

All medical notes must follow the **Davidson 24th Edition Chapter Hierarchy**:

```
Chapter (Part) -> Section -> Heading Hub -> Topic-Group Hub -> Disease-Level Topic
```

### Status System (Mandatory)

Every file MUST have a YAML frontmatter with a `status` field:

| Status Value | Meaning |
|--------------|---------|
| `full-fcps-mrcp-note` | Complete disease-level note with all 13 required sections |
| `scaffold-hub` | Navigation/heading/topic-group hub (not a disease note) |
| `true-disease-level-scaffold-built` | Hierarchy/index files |
| `true-disease-level-scaffold-system-validated` | MOC/complete system |

---

## 13 Required Sections (Every Disease Note MUST Have)

Every disease-level note (`status: full-fcps-mrcp-note`) MUST contain ALL 13 sections in this order:

### 1. YAML Frontmatter (Required Fields)

```yaml
---
tags: [medicine, specialty, davidson, disease-key, fcps, mrcp]
davidson_part: "Part X: ..."
davidson_chapter: "Chapter Y: ..."
heading: "Section Heading"
topic_group: "Topic Group Name"
topic: "Disease Name"
status: full-fcps-mrcp-note
priority: critical|high|medium|low
cards: 15-25
created: YYYY-MM-DD
modified: YYYY-MM-DD
exam_relevance: [FCPS, MRCP Part 1, MRCP Part 2, PACES]
see_also:
  - "[[Related Topic 1]]"
  - "[[Related Topic 2]]"
```

### 2. Learning Objectives (Checkbox Format)

```markdown
## Learning Objectives
By the end of this note you should be able to:
- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3
```

### 3. Core Content Sections (Variable by Disease)

- Definition & Epidemiology
- Aetiology & Pathophysiology (with mermaid flowchart)
- Clinical Features
- Classification/Criteria (with tables)
- Diagnosis & Investigations
- Differential Diagnosis
- Management Algorithm (with mermaid flowchart)
- Complications/Prognosis

### 4. FCPS/MRCP High-Yield Summary Table

```markdown
| Topic | Key Points |
|-------|------------|
| ...   | ... |
```

### 5. Viva Questions (MRCP PACES / FCPS Style)

```markdown
| Question | Expected Answer |
|----------|----------------|
```

### 6. Confusions & Mnemonics

```markdown
| Confusion | Clarification |
|-----------|---------------|
```

**Mnemonic section** with at least 3-5 mnemonics

### 7. Mind Map (Mermaid)

```mermaid
mindmap
  root((Disease))
  ...
```

### 8. One-Page Revision Card (Table Format)

```markdown
| Domain | Key Points |
|--------|------------|
```

### Spaced Repetition Trackers (Exact Intervals Required — User Preference)

```markdown
| Review Interval | Date | Score (0-5) | Notes |
|-----------------|------|-------------|-------|
| Day 1 | | | |
| Day 3 | | | |
| Day 7 | | | |
| Day 14 | | | |
| Day 30 | | | |
| Day 90 | | | |
```

### 10. Self-Test Scorecard

```markdown
| Section | Score /5 | Last Attempt |
|---------|----------|--------------|
```

### 11. Local Navigation Section

```markdown
## Local Navigation
- **Parent Heading**: [[../Parent Heading|Parent Heading]]
- **Parent Topic Group**: [[Parent Topic Group]]
- **Chapter Map**: [[../Davidson Chapter X - Hierarchy|Hierarchy]]
- **Chapter MOC**: [[../Specialty MOC|MOC]]
- **Drug Reference**: [[../../Clinical Therapeutics|Drugs]]
- **Related**: [[Related Topic 1]] · [[Related Topic 2]]
```

---

## Infrastructure Files (Must Exist Per Chapter — User's Flat Structure)

Each Davidson chapter folder MUST contain (flat structure, no section subdirectories):

| File | Purpose | Status |
|------|---------|--------|
| `Specialty MOC.md` | Master index with ✅ tracking | `true-disease-level-scaffold-system-validated` |
| `Davidson Chapter X - Hierarchy.md` | Full hierarchy with checkboxes | `true-disease-level-scaffold-built-validated` |
| `Chapter X Roadmap.md` | Study sequence, exam mapping | `true-disease-level-scaffold-built` |
| `Templates/Specialty Topic Template.md` | Standardized template | `status: template` |
| `Chapter X Roadmap.md` | Study sequence | `scaffold` |

### Hierarchy File Must Track:
- Heading hubs count
- Topic-group hubs count
- Disease-level topics count
- Preserved root-level core notes count
- ✅ checkboxes for each completed disease note

### MOC Must Track:
- ✅ checkboxes for each completed disease note
- Counter updated to `Completed scaffold-to-full-note topics (verified full FCPS/MRCP notes: N)`

---

## Template File Requirement

Every chapter MUST have a template at:
`/mnt/tb/Medicine/Specialty/Templates/Specialty Topic Template.md`

The template must contain ALL 13 required sections with placeholder content.

---

### Quality Checklist (Every Disease Note — User's Exact Preferences)

Before marking `status: full-fcps-mrcp-note`, verify:
- [ ] All 13 sections present and complete
- [ ] YAML frontmatter complete with all required fields
- [ ] Learning Objectives with checkboxes
- [ ] Mermaid diagrams for pathophysiology, algorithms, mind maps
- [ ] FCPS/MRCP High-Yield Summary table
- [ ] Viva Questions (PACES/FCPS style) — 8-12 questions
- [ ] Confusions & Mnemonics section with >=3 mnemonics
- [ ] Mind Map (mermaid)
- [ ] One-Page Revision Card (table)
- [ ] Spaced Repetition Trackers (Day 1, Day 3, Day 7, Day 14, Day 30, Day 90)
- [ ] Self-Test Scorecard (sections with /5 scoring)
- [ ] Local Navigation links (all relative paths)
- [ ] Learning Objectives with checkboxes
- [ ] Mermaid diagrams for pathophysiology, algorithms, mind maps
- [ ] FCPS/MRCP High-Yield Summary table
- [ ] Viva Questions (PACES/FCPS style)
- [ ] Confusions & Mnemonics with >=3 mnemonics
- [ ] Spaced Repetition Trackers (Day 1, Day 3, Day 7, Day 14, Day 30, Day 90)
- [ ] Self-Test Scorecard
- [ ] Local Navigation
- [ ] Exam Answer Modes (5 modes: Long Essay, Short Note, Viva, Ward Round, Last-Night)
- [ ] MCQs (10) + SBAs (10) with Answer Keys
- [ ] MCQ/SBA distractors are plausible FCPS/MRCP style

---

### Git Workflow (Mandatory — User's Exact Commit Format)

After completing a batch of 5-10 notes:
```bash
cd /mnt/tb/Medicine/Clinical\ Therapeutics\ and\ Good\ Prescribing
git add -A
git commit -m "Complete Davidson Ch X: [Chapter Name] - N new full-fcps-mrcp-note files + MOC

- [Topic 1]: [Key highlights]
- [Topic 2]: [Key highlights]
...
All notes include: Learning objectives, pathophysiology mermaid diagrams, diagnostic algorithms, management flowcharts, FCPS/MRCP high-yield tables, viva questions, mind maps, one-page revision cards, spaced repetition trackers, self-test scorecards.

Total: X/Y disease-level topics complete. MOC updated with ✅ tracking."
git push
```

---

## Template Creation

When starting a new specialty chapter, FIRST create/update the template:
`/mnt/tb/Medicine/Specialty/Templates/Specialty Topic Template.md`

The template must contain ALL 13 required sections with placeholder content.

---

### Verification Commands (User's Flat Directory Structure)

```bash
# Count completed disease notes
grep -r "status: full-fcps-mrcp-note" /mnt/tb/Medicine/Clinical\ Therapeutics\ and\ Good\ Prescribing --include="*.md" | wc -l

# List files missing status
for f in /mnt/tb/Medicine/Clinical\ Therapeutics\ and\ Good\ Prescribing/**/*.md; do if ! grep -q "status:" "$f" 2>/dev/null; then echo "NO STATUS: $f"; fi; done

# Verify all disease notes have spaced repetition
for f in /mnt/tb/Medicine/Clinical\ Therapeutics\ and\ Good\ Prescribing/**/*.md; do if grep -q "status: full-fcps-mrcp-note" "$f" 2>/dev/null; then if ! grep -q "Spaced Repetition Trackers" "$f" 2>/dev/null; then echo "MISSING Spaced Repetition: $f"; fi; fi; done
### Ch 1-15 / Ch 16-20 MedSea Sync Learnings (2026-06-20)

**Three distinct "100% match" claims the user kept correcting me on — each is a different layer of completeness. NEVER claim "100% match" without specifying which layer.**

| Layer | What it means | How to verify |
|---|---|---|
| **Topic presence** | Every source topic has a MedSea counterpart file | `find` count + slug-match pairs |
| **Section presence** | Each topic file has all required ## sections (MCQ, SBA, Flash, Tracker, Scorecard) | `^##[^#]*\bMCQs?\b` regex per file |
| **Content presence** | Each section has actual items (10 MCQs, 10 SBAs, not just `## MCQs (1)`) | Count numbered items inside bounded section block |

**When the user says "MCQs/SBAs/flashcards/tracker all A to Z word" they mean section presence + content presence** — both. A file with `## MCQs` and only 1 question still fails.

### Slug-matching bug — the recurring failure mode

Source filenames vs MedSea filenames do NOT share a format. Both sides need aggressive normalization:

```python
def src_slug(bn):
    """Source: '5.1-5.4 Genetic Testing Technologies.md' or 'Cardiomyopathy.md' or 'ACD.md'"""
    bn = bn.replace('.md', '').replace('_full', '').replace('_Hub', '')
    # Strip ALL leading-number variants: '1.', '2.1', '10.', '5.1-5.4', '01_' etc.
    bn = re.sub(r'^\d+(\.\d+)*[\.\s_-]*', '', bn).strip()
    return slug(bn)

def ms_slug(bn):
    """MedSea: '5.4.01-hypersensitivity-allergy.md' (flat) or '14.1.46-toxoplasmosis/topic.md' (nested)"""
    if bn == 'topic':
        bn = os.path.basename(os.path.dirname(p))  # nested: slug is in parent dir name
    bn = bn.replace('.md', '').replace('-full', '').replace('-hub', '')
    bn = re.sub(r'^\d+\.\d+\.\d+-', '', bn)  # strip leading '16.1.01-'
    return slug(bn)
```

**Critical:** NEVER match by raw basename — always strip leading numbers and normalize. MedSea uses dashed IDs (`5.4.01`), source uses dotted (`5.1-5.4`) or no prefix. A naive `startswith()` will report everything as missing.

### Subdirectory vs flat MedSea layout — auto-detect

Ch 14, 16, 17 use `<id>-<slug>/topic.md` (nested). Ch 1-13, 18-20 use `<id>-<slug>.md` (flat). The audit script and any sync script must handle BOTH:

```python
for r, d, fs in os.walk(ms_chapter + '/diseases'):
    for f in fs:
        if f.endswith('.md'):
            full = os.path.join(r, f)
            # If inner file is topic.md, the slug is in the parent dir name
            if os.path.basename(full) == 'topic.md':
                bn = os.path.basename(os.path.dirname(full))
            else:
                bn = f.replace('.md', '')
```

### Source Ch 16 uses VIVA QUESTIONS instead of MCQs

96% of Ch 16 source files have `## VIVA QUESTIONS` or `## Common Viva Questions` — NOT `## MCQs`. VIVA is the FCPS/MRCP equivalent of MCQ in source. When counting MCQ coverage, accept BOTH:

```python
mcq_or_viva = re.compile(r'^##[^#]*\b(?:MCQs?|Viva|VIVA)\b', re.IGNORECASE | re.MULTILINE)
```

If you report MCQ% in Ch 16 without counting Viva, you'll say "64% MCQ" when it's actually "96% MCQ-or-Viva" — wrong.

### MedSea frontmatter pattern when copying source content

Source files often have their own YAML frontmatter. Before writing to MedSea, **strip source frontmatter and prepend MedSea frontmatter**:

```python
def strip_existing_frontmatter(text):
    if text.startswith('---'):
        end = text.find('---', 3)
        if end != -1:
            return text[end+3:].lstrip('\n')
    return text

fm = f"""---
davidson_chapter: "Chapter 16: Cardiology"
davidson_topic_id: "{topic_id}"  # extracted from MedSea path
topic: "{topic_name}"
status: full-fcps-mrcp-note
priority: critical
cards: 20-25
created: 2026-06-20
modified: 2026-06-20
exam_relevance: [FCPS, MRCP Part 1, MRCP Part 2]
source: "{src_path}"
tags: [medicine, cardiology, davidson, fcps, mrcp]
---
"""
new_content = fm + strip_existing_frontmatter(src_text)
```

Without this, you'll end up with TWO frontmatter blocks (MedSea's at top, source's right after) and the topic_id will be wrong because the regex didn't extract it from the parent dir name.

### Source dedup pattern

Source has DUPLICATE topic files in different subfolders (e.g., `/TDM/Aminoglycosides.md` and `/Therapeutic Drug Monitoring/Aminoglycosides.md` — same content, different paths). **Dedupe by basename before any matching:**

```python
seen = set()
unique_src = []
for sp in all_source_files:
    bn = os.path.basename(sp)
    if bn not in seen:
        seen.add(bn)
        unique_src.append(sp)
```

Without dedup, you'll count the same topic multiple times in source and report phantom "missing" topics in MedSea.

### The gapping audit pattern

After topic-matching, identify which pairs have content-gap:

```python
patterns = {
    'mcq':   re.compile(r'^##[^#]*\bMCQs?\b', re.IGNORECASE | re.MULTILINE),
    'sba':   re.compile(r'^##[^#]*\bSBAs?\b', re.IGNORECASE | re.MULTILINE),
    'flash': re.compile(r'^##[^#]*\bFlashcards?\b', re.IGNORECASE | re.MULTILINE),
    'track': re.compile(r'^##[^#]*\b(?:Spaced Repetition|Revision Tracker|24-Hour Recall)', re.IGNORECASE | re.MULTILINE),
    'score': re.compile(r'^##[^#]*\b(?:Self-Test|Scorecard)\b', re.IGNORECASE | re.MULTILINE),
}

for src_path, ms_path in pairs:
    src_text = open(src_path).read()
    ms_text = open(ms_path).read()
    for name, pat in patterns.items():
        if pat.search(src_text) and not pat.search(ms_text):
            gaps.append({...})
```

A "gap" = source has the section AND MedSea doesn't. For each gap, copy source content to MedSea (with frontmatter pattern above).

### Source-aligned vs exceed-source

Source has limited SBA/Flashcard coverage in some chapters (Ch 16: 16% SBA, 12% Flash). When source has limited content, MedSea matching source is the correct outcome — DO NOT generate additional content to "exceed" source. The user's "100% match" means match source percentages, not invent new content.

Report coverage as `src_pct% → ms_pct%` so the user can see the alignment, not just "100% ✓".

### Verification ritual for "is this chapter done?"

Before reporting completion on any chapter:

1. **Topic presence** — `len(unique_source) vs len(medsea_files)`, list unmatched both ways
2. **Section coverage** — per-section % in source vs MedSea (use the patterns above)
3. **Spot-check word overlap** on 3-5 random matched pairs: `len(set(src_words) & set(ms_words)) / len(src_words)`
4. **Frontmatter check** — verify MedSea files have `topic_id`, `status: full-fcps-mrcp-note`, no double-frontmatter
5. **Site rebuild** — `python3 scripts/site/build_site.py` + `docker build --no-cache` + restart

Only after all 5 pass should you claim the chapter is done. The user will say "check files 1 by 1" if any step is skipped.

## Critical Session Learnings

### Clinical Immunology Chapter 4 (Davidson 24th Ed) — 2026-06-15

**Complete Chapter Completion — 19 Files Created:**

**Clinical Immunology Chapter 4 (Davidson 24th Ed) — All 19 Files Complete:**

| # | File | Size | Status |
|---|------|------|--------|
| 1 | `Davidson Chapter 4 - Clinical Immunology Hierarchy.md` | 14 KB | `scaffold` |
| 2 | `Clinical Immunology MOC.md` | 21 KB | `scaffold-hub` |
| 3 | `1. Fundamentals of Immunology.md` | 34 KB | `full-fcps-mrcp-note` |
| 4 | `2.1 Primary Immunodeficiencies.md` | 34 KB | `full-fcps-mrcp-note` |
| 5 | `2.2 Secondary Immunodeficiencies.md` | 31 KB | `full-fcps-mrcp-note` |
| 6 | `2.3 Approach to Immunodeficiency.md` | 28 KB | `full-fcps-mrcp-note` |
| 7 | `3.1 Mechanisms of Autoimmunity.md` | 32 KB | `full-fcps-mrcp-note` |
| 8 | `3.2 Systemic Autoimmune Diseases.md` | 35 KB | `full-fcps-mrcp-note` |
| 9 | `3.3 Organ-Specific Autoimmune Diseases.md` | 41 KB | `full-fcps-mrcp-note` |
| 10 | `3.4 Autoimmune Diagnostics.md` | 32 KB | `full-fcps-mrcp-note` |
| 11 | `4.1-4.4 Hypersensitivity & Allergy.md` | 36 KB | `full-fcps-mrcp-note` |
| 11 | `5.1-5.4 Transplant Immunology.md` | 35 KB | `full-fcps-mrcp-note` |
| 12 | `6.1-6.7 Tumour Immunology & Immunotherapy.md` | 35 KB | `full-fcps-mrcp-note` |
| 12 | `7.1-7.6 Immune-Based Therapies.md` | 38 KB | `full-fcps-mrcp-note` |
| 13 | `8.1-8.6 Special Situations Immunology.md` | 37 KB | `full-fcps-mrcp-note` |

**Total: ~600 KB** of detailed FCPS/MRCP content across **19 files**

**Content Coverage Complete (Davidson 24th Ed Chapter 4):**

| Section | Topics Covered |
|---------|----------------|
| **Fundamentals** | Innate/Adaptive Immunity, Complement, Cytokines, HLA, Immune Development |
| **Primary Immunodeficiencies** | IUIS Classification, XLA/CVID/SCID/CGD/Complement/MSMD/Dysregulation |
| **Secondary Immunodeficiencies** | HIV, Drug-induced, Malignancy, Protein Loss, Splenectomy, Critical Illness |
| **Diagnostic Approach** | SPUR/JACKIE, Tiered Testing, Genetic Testing Strategy |
| **Autoimmunity Mechanisms** | Tolerance, Mimicry, Epitope Spreading, HLA, Environmental Triggers |
| **Systemic Autoimmune** | SLE, SSc, Sjögren, IIM, Vasculitis, MCTD, APS, AOSD |
| **Organ-Specific Autoimmune** | RA, SpA, Thyroid, T1DM, Coeliac, Liver, MG, MS, Bullous |
| **Autoimmune Diagnostics** | ANA, ENA, ANCA, Complement, Cryoglobulins, aPL, RF/CCP, Algorithms |
| **Hypersensitivity & Allergy** | Gell & Coombs, Anaphylaxis, Asthma, Rhinitis, Food Allergy, Drug Hypersensitivity, Testing |
| **Transplant Immunology** | HLA, Allorecognition, Rejection/Banff, IS, HSCT/GvHD, Monitoring |
| **Tumour Immunology** | Immunoediting, Checkpoints, CAR-T, Vaccines, Biomarkers, irAEs, Resistance |
| **Immune-Based Therapies** | IVIG, mAbs, JAKi, S1P Mod, BTKi, BCL-2i, Cytokines, Cellular Therapies |
| **Special Situations** | Immunosenescence, Pregnancy, Critical Illness, Obesity, Microbiome, Vaccinology |

**Complete Davidson Chapters Now Finished:**\n- ✅ **Chapter 2**: Clinical Therapeutics &amp; Good Prescribing (32+ files) — COMPLETE\n- ✅ **Chapter 3**: Clinical Genetics (18+ files) — COMPLETE  \n- ✅ **Chapter 4**: Clinical Immunology (19 files) — COMPLETE\n- ✅ **Chapter 9**: Environmental Medicine (10 files) — COMPLETE\n\n**Key Accomplishment:** Complete Chapter 4 (Clinical Immunology) with 19 files (~600 KB), following the exact same Davidson 24th Ed structure and FCPS/MRCP template as previous chapters.

**Stream Timeout Prevention for Large Immunology Notes:**
- Large immunology notes (200+ lines, 20K+ tokens with scoring tables, Mermaid diagrams) cause stream timeouts on single `write_file` calls
- **Solution**: Split large notes into **4-chunk writes per note**:
  - Chunk 1: Frontmatter + Learning Objectives + Definition/Epidemiology + Aetiology/Pathophysiology + Clinical Features
  - Chunk 2: Classification/Staging + Diagnosis/Differentials + Investigations
  - Chunk 3: Management Algorithm + FCPS/MRCP High-Yield + Viva Questions
  - Chunk 4: Confusions/Mnemonics + Mind Map + Revision Card + Trackers + Scorecard + Navigation
- **Each chunk ≈ 5-7K tokens** — well under 8K token limit
- **Verification after EACH batch**: Run `grep` search and `wc -l` after each batch before declaring complete

**Git Workflow for Multi-File Chapters:**
- After completing a batch of 5-10 notes: `git add -A && git commit -m "Descriptive commit message" && git push origin main`
- Commit message format: `"Complete Davidson Ch X: [Chapter Name] - N new full-fcps-mrcp-note files + MOC"`
- Push after each major milestone (chapter completion)

**Complete Davidson Chapters Now Finished:**
- ✅ Chapter 2: Clinical Therapeutics and Good Prescribing (completed earlier)
- ✅ Chapter 3: Clinical Genetics (completed earlier)  
- ✅ Chapter 4: Clinical Immunology (COMPLETED — 19 files)

**Template Consistency Maintained:**
- All 19 files follow the exact same `full-fcps-mrcp-note` template with 13 required sections
- Consistent YAML frontmatter, mermaid diagrams, tables, viva questions, MCQs/SBAs, spaced repetition trackers
- Cross-links between all files via relative wiki-links `[[../Relative/Path]]`

### Clinical Therapeutics Chapter 2 (Davidson 24th Ed) — Completed Earlier

**Complete Chapter 2 — 32+ Files Created:**

**Content Coverage Complete (Davidson 24th Ed Chapter 2):**

| Section | Topics Covered |
|---------|----------------|
| **Principles of Rational Prescribing** | WHO 6-Step Model, P-drug, Evidence-based, Prescription writing, Legal/CD |
| **ADRs** | Classification (Type A-F, HLA), Causality (Naranjo, WHO-UMC, RUCAM), Reporting (Yellow Card), System-specific patterns |
| **Drug Interactions** | PK (Absorption, Distribution, Metabolism-CYP, Excretion), PD, Clinical Significance, High-risk (ARV, AED, Warfarin, DOAC, Immunosuppressants, QT) |
| **Polypharmacy & Deprescribing** | Definition, Consequences, Assessment Tools (STOPP/START v3, Beers, ACB, DBI, FORTA), Barriers, Process |
| **Special Populations** | Renal, Hepatic, Elderly, Pregnancy/Lactation, Paediatrics |
| **Medication Safety** | Error Types, Root Causes (Swiss Cheese), PINCH High-Risk, High-Alert Meds |
| **TDM** | Aminoglycosides (Hartford), Vancomycin (AUC), Digoxin, Lithium, Anticonvulsants, Immunosuppressants, Theophylline |
| **Drug Development & Regulation** | Phases I-IV, MHRA/EMA/FDA, PSUR/PBRER, Signal Detection, Generics/Biosimilars, NICE HTA, CD Schedules |
| **Clinical Contexts** | Pain (WHO Ladder, Opioids), AMS, Palliative (Syringe Drivers), Perioperative |

**Key Accomplishment:** Complete Chapter 2 (Clinical Therapeutics) using the same template and approach.

### Clinical Genetics Chapter 3 (Davidson 24th Ed) — Completed Earlier

**Complete Chapter 3 — 18+ Files Created:**

**Content Coverage Complete (Davidson 24th Ed Chapter 3):**

| Section | Topics Covered |
|---------|----------------|
| **Fundamentals** | DNA/Genes/Genome, Chromosome Structure, Cell Division, Population Genetics (HWE) |
| **Inheritance Patterns** | Mendelian (AD, AR, XL, Y), Non-Mendelian (Mitochondrial, Imprinting, Repeats, Mosaicism, UPD), Multifactorial |
| **Chromosomal Disorders** | Aneuploidy, Translocations, Microdeletions/Microduplications, Instability Syndromes |
| **Single Gene Disorders** | AD (NF1, Marfan, ADPKD, FH), AR (CF, Sickle, Thal, PKU, Wilson), XL (DMD, Haemophilia, G6PD), Mitochondrial, Imprinting (PWS/AS/BWS/SRS) |
| **Genetic Testing** | Cytogenetics, Sanger/MLPA/NGS, Prenatal/PGT, Variant Classification (ACMG) |
| **Pharmacogenetics** | CYP2D6, CYP2C19, TPMT, DPYD, HLA, VKORC1, SLCO1B1, Guidelines (CPIC/DPWG/NHS GMS) |
| **Genetic Counselling** | Principles, Predictive Testing, Reproductive Options, Cascade, Prenatal/PGT
- **Population Screening** | NBS (9 conditions), Antenatal, Carrier Screening, Ethics
- **Ethical/Legal** | Consent (Montgomery), MCA 2005, GINA, Equity, DTC Testing

**Key Accomplishment:** Complete Chapter 3 (Clinical Genetics) with 18+ detailed files using the same template and approach.

### New Workflow Insights (2026-06-15)

**Complete Multi-Chapter Davidson Coverage Achieved:**
- ✅ **Chapter 2**: Clinical Therapeutics & Good Prescribing (32+ files) — COMPLETE
- ✅ **Chapter 3**: Clinical Genetics (18+ files) — COMPLETE  
- ✅ **Chapter 4**: Clinical Immunology (19 files) — COMPLETE
- **Total**: 69+ detailed FCPS/MRCP-ready notes across 3 Davidson chapters

**Git Workflow for Multi-File Chapters:**
- After completing a batch of 5-10 notes: `git add -A && git commit -m "Descriptive commit message" && git push origin main`
- Commit message format: `"Complete Davidson Ch X: [Chapter Name] - N new full-fcps-mrcp-note files + MOC"`
- Push after each major milestone (chapter completion)

**Complete Davidson Coverage So Far:**
- ✅ Chapter 2: Clinical Therapeutics & Good Prescribing (32+ files) — COMPLETE
- ✅ Chapter 3: Clinical Genetics (18+ files) — COMPLETE  
- ✅ Chapter 4: Clinical Immunology (19 files) — COMPLETE
- **Total**: 69+ detailed FCPS/MRCP-ready notes across 3 Davidson chapters

**Template Consistency Maintained Across All Chapters:**
- All 69+ files follow the exact same `full-fcps-mrcp-note` template with 13 required sections
- Consistent YAML frontmatter, mermaid diagrams, tables, viva questions, MCQs/SBAs, spaced repetition trackers
- Cross-links between all files via relative wiki-links `[[../Relative/Path]]`

**Stream Timeout Prevention — Improved Strategy:**\n- Large medical notes (200+ lines, 20K+ tokens) cause stream timeouts on single `write_file` calls\n- **Solution**: Split large notes into **4-chunk writes per note**:\n  - Chunk 1: Frontmatter + Learning Objectives + Definition/Epidemiology + Aetiology/Pathophysiology + Clinical Features\n  - Chunk 2: Classification/Staging + Diagnosis/Differentials + Investigations\n  - Chunk 3: Management Algorithm + FCPS/MRCP High-Yield + Viva Questions\n  - Chunk 4: Confusions/Mnemonics + Mind Map + Revision Card + Trackers + Scorecard + Navigation\n- **Each chunk ≈ 5-7K tokens** — well under 8K token limit\n- **Verification after EACH batch**: Run `grep` search and `wc -l` after each batch before declaring complete\n- **Environmental Medicine Specifics**: Environmental Medicine chapters (like Ch 9) have 8 major sections, each producing 30-40KB files. Split into 4 chunks of ~8-10KB each to stay under 8K token limit. The Climate Change & Health Impacts file (33KB) and Chemical Hazards (41KB) were the largest and required careful chunking.

**Complete Multi-Chapter Workflow Established:**
1. Create/update chapter hierarchy scaffold file
2. Create/update chapter MOC with ✅ tracking
3. Build topic files sequentially using 4-chunk write strategy
4. Verify after each batch with `grep` and `wc -l`
5. Update MOC with ✅ tracking
4. Push to git with descriptive commit message
5. Repeat for next chapter

**Total Project Status: 3 of ~35 Davidson Chapters Complete (Chapters 2, 3, 4)**
- Chapter 2: Clinical Therapeutics (32+ files) ✅
- Chapter 3: Clinical Genetics (18+ files) ✅  
- Chapter 4: Clinical Immunology (19 files) ✅
- Remaining: Chapters 1, 5-35 to be completed

**Verification Protocol After Each Chapter:**
```bash
# Verify all disease notes have full-fcps-mrcp-note status
grep -r "status: full-fcps-mrcp-note" /mnt/tb/Medicine/Chapter_X --include="*.md" | wc -l

# Verify all files have 13 required sections
for f in /mnt/tb/Medicine/Chapter_X/**/*.md; do
  if grep -q "status: full-fcps-mrcp-note" "$f" 2>/dev/null; then
    missing_sections=0
    for section in "Learning Objectives" "Core Concept" "Key Points" "Viva Questions" "Confusions" "Mind Map" "Spaced Repetition" "Self-Test" "Summary" "MCQs" "SBAs" "Answer Keys" "Cross-Links"; do
      if ! grep -q "## $section" "$f" 2>/dev/null; then
        ((missing_sections++))
      fi
    done
    if [ $missing_sections -gt 0 ]; then
      echo "MISSING $missing_sections sections in $f"
    fi
  done
done
```

---

## Stream Timeout Prevention — Decision Tree (updated 2026-06-17, Ch 25 Neurology round 2)

**Lesson 1 — Ch 22 (2026-06-16): DON'T use delegate_task for full-file writes of 25-36KB content.** The sub-agent's own output stream hits the same 8K token ceiling when generating a 30KB+ file with MCQs, SBAs, Flashcards, Mind Maps. "Subagent timed out after 600.0s" with partial output. Direct sequential writes are reliable.

**Lesson 2 — Ch 25 Neurology round 1 (2026-06-17): DO use delegate_task for placeholder-replacement when content generation is the bottleneck.** Pre-scripting all disease-specific facts in the parent and asking the subagent only to do find-and-replace works in 5-10KB per file. Expect 1-3 of 3 parallel dispatches to time out — the timed-out subagents usually completed 50-80% of their work; verify and re-dispatch.

**Lesson 3 — Ch 25 Neurology round 2 (2026-06-17): When the parent agent has ALL the disease-specific facts ready, DIRECT Python in execute_code is FASTER than subagents for placeholder-replacement.**

Speed comparison (41 placeholder files, all real disease-specific content):
- 3 parallel subagents (3 files each): ~10-15 min, with 1-3 timeouts requiring re-dispatch
- Direct execute_code with all content pre-scripted as Python data structures: ~3-5 sec per file, zero timeouts

When to use which:

| Scenario | Approach | Why |
|---|---|---|
| <5 files, content is short, content fits in prompt context | `delegate_task` with full content in prompt | Simpler, parallel |
| 5-15 files, need to generate content from scratch (no template) | `delegate_task` (3-5 files per subagent) | Subagent can generate |
| 15+ files with placeholder-to-real replacement where parent has all facts | **Direct `execute_code` with Python data structures** | **10x faster, no timeouts** |
| Need to write >30KB single file | `write_file` direct, or split into 2-3 chunks if timeout | Subagent generation too slow |
| Files in different directories, no batching needed | Sequential `write_file` | Simplest |

**The fast pattern (Lesson 3 in action):**

```python
# In parent execute_code:
import os, re

CONTENT_DB = {
    "Filename.md": {
        "disease": "Disease Name",
        "hub": "Hub Name",
        "mnemonics": ["mnemonic 1", "mnemonic 2", "mnemonic 3"],
        "mcqs": [
            ("Question text", ["Option A", "Option B", "Option C", "Option D"], "A", "Explanation"),
            # ... 10 MCQs
        ],
        "sbas": [
            ("Scenario", ["Opt A", "Opt B", "Opt C", "Opt D", "Opt E"], "A", "Explanation"),
            # ... 10 SBAs
        ],
        "tags": "#neurology #disease #FCPS #MRCP"
    },
    # ... all files
}

def process_file(fpath, data):
    with open(fpath) as f: c = f.read()
    m_start = c.find("## Mnemonics")
    lnav = c.find("## Local Navigation")
    if m_start == -1 or lnav == -1: return False
    new_content = build_template(data)  # helper that produces standard template
    with open(fpath, "w") as f: f.write(c[:m_start] + new_content)
    return True

for fname, data in CONTENT_DB.items():
    process_file(f"{base}/{fname}", data)
```

**Why this works:** The Python script's content is already in the parent's context. The execute_code runs the script directly without API round-trip delays or 600s timeout pressure. The output is the result of file I/O only.

**Pitfall with direct Python:** each `execute_code` call is a fresh sandbox — module-level variables don't persist. Build the content DB inline in every script (or import from `/tmp/` files written earlier in the session).

**DO NOT use delegate_task for:** full-file writes >30KB, content generation from scratch, multi-section rewrites.
**DO use delegate_task for:** placeholder-to-real-content replacement when parent DOES NOT have all facts ready, audit scripts, web searches, status checks (≤5 files).
**DO use direct execute_code for:** placeholder-to-real-content replacement when parent HAS all facts ready (≥10 files).

## 100% Match Audit Pattern (Ch 1-15, 2026-06-20)

When the user asks **"make 100% match from medicine notes"** or **"sync all information from /mnt/tb/Medicine"**, the goal is: every MedSea topic has the same content as its source MD. The user has been clear (twice): "I said add all a to z" — meaning every section, including MCQs, SBAs, Flashcards, Tracker, Scorecard. Do NOT declare "100% match" until section counts actually match.

**Workflow:**

1. **Index both sides:**
   - Source: walk `/mnt/tb/Medicine/<chapter>/` for all `.md`, dedupe by basename, exclude MOC/Hierarchy/Template/README
   - MedSea: walk `/mnt/tb/Sea-knowledge/#MedSea/chapters/<ch>/diseases/` for all `.md` recursively (handles both flat and `topic.md`-in-subdir layouts)

2. **Match by topic ID + slug:**
   - Extract `topic_id` from source filename leading number pattern (`^\d+(?:\.\d+)*`)
   - Extract `topic_id` from MedSea filename (`\d+\.\d+\.\d+` prefix on dir or filename)
   - Short IDs match when `1.1 == 1.1` even if slugs differ
   - If no ID match, slug-match: lowercase, strip punctuation, strip leading number, strip `_full`/`-full`/`-hub`, normalize dashes
   - Use STRICT threshold (≥80) for content comparison to avoid false positives

3. **Identify gaps per chapter:**
   - Count: source unique vs MedSea total
   - List: source topics with no MedSea match (truly missing)
   - List: matched pairs where MedSea has fewer `## ` sections than source (gapped)
   - List: MedSea topics without source equivalent (extra — usually fine)

4. **Content-presence check (across chapter):**
   - For each MedSea topic file, regex-search for `^##[^#]*\bMCQs?\b`, `\bSBAs?\b`, `\bFlashcards?\b`, `(?:Spaced Repetition|Revision Tracker|24-Hour Recall)`, `(?:Self-Test|Scorecard)`
   - Compute % of topics per chapter with each section
   - Compare to source % — they should match within 1-2%

5. **Fix strategy (in priority order):**
   - **Stripped topics** (MedSea exists but missing exam sections): replace `topic.md` with source content, prepend MedSea YAML frontmatter (preserve topic_id, status, etc.)
   - **Gapped topics** (MedSea smaller than source): same as above
   - **Truly missing topics**: copy source to new MedSea `topic.md` in appropriate directory, update MOC
   - **Hub files** (MedSea has `-hub` suffix): these are intentionally condensed — DO NOT fill, they are navigation pages

6. **Verify after fix:**
   - Section counts should match source per chapter
   - Word-overlap between source and MedSea content should be 95%+ for matched pairs
   - Sample 5 random files per chapter to confirm MCQs/SBAs actually have content (not just headers)

**Slug matching pitfalls (recurring bugs):**

| Source filename | MedSea filename | Match logic |
|---|---|---|
| `1.1 Clinical Reasoning & Diagnostic Process.md` | `1.1.01-clinical-reasoning-diagnostic-process.md` | Strip leading `\d+\.\d+` from source, slug both |
| `5.1-5.4 Genetic Testing Technologies.md` | `3.5.01-genetic-testing-technologies.md` | Strip section range from source ID |
| `NSAIDs (traditional)_full.md` | `9.2.03-nsaids-traditional-full.md` | Strip `_full` and `-full` from slug, drop parens |
| `Sepsis and Septic Shock.md` (no ID) | `14.1.42-sepsis-and-septic-shock/topic.md` | Use parent DIR name (not `topic.md`) as the slug source |
| `Pelvic Inflammatory Disease (PID).md` | `15.1.16-pelvic-inflammatory-disease-pid.md` | Lowercase, drop parens, slug |

The cross-chapter source audit script `scripts/cross_chapter_source_audit.py` automates this — see References table for the worked example.

## Ch 22 (Nutritional Factors) Specific Learnings (2026-06-16)

**Chapter scale (36 topic files, ~1MB total):**
- 36 files across 7 sections (A: Macronutrients 5; B: Fat-soluble vit 4; C: Water-soluble vit 6; D: Minerals 6; E: Nutritional disorders 5; F: Clinical nutrition 4; G: Special topics 6)
- Average 25-36KB per file; ~500-600 lines each
- Total 1.05MB content
- Time: ~3-4 hours continuous work (with delegate_task failures eating ~30 min)

**Status value standardization:**
- Both `complete` and `full-fcps-mrcp-topic-note` are used as completion markers across the corpus (not just `full-fcps-mrcp-note` per the skill's original spec)
- Audit scripts must accept all three: `full-fcps-mrcp-note`, `full-fcps-mrcp-topic-note`, `complete`
- A simple `sed` to standardize after the fact works: `sed -i 's/^status: complete$/status: full-fcps-mrcp-topic-note/' *.md`

**Duplicate file naming pitfall (recurring):**
- Topic files created with slightly different filenames create silent duplicates
- E.g. `Zinc- Acrodermatitis & Wound Healing.md` (original scaffold, ~3KB) vs `Zinc- Acrodermatitis, Wound Healing & Immunity.md` (new, ~31KB)
- Fix: `mv "Zinc- Acrodermatitis & Wound Healing.md" "Zinc- Acrodermatitis & Wound Healing.scaffold.md" && rm "Zinc- Acrodermatitis & Wound Healing.scaffold.md" && mv "Zinc- Acrodermatitis, Wound Healing & Immunity.md" "Zinc- Acrodermatitis & Wound Healing.md"`
- ALWAYS `ls | sort` before creating new files; fuzzy-match for "&" vs "and" duplicates

**MOC update as final step (not incremental):**
- For large chapters (30+ files), wait until ALL files are done before updating MOC
- Avoid 30+ small MOC patches; write the complete MOC once
- Use `write_file` (full overwrite) not `patch` for the MOC final state

## Build & Publish Pipeline (raw MD → Notion + Site + Git)

**Validated 2026-06-19 across Ch 19, 21, 23-32 (12 chapters, 1461 PNGs).** Full worked example: `references/davidson-ch19-32-build-pipeline-2026-06-19.md`.

### When to Use This Section

When the user asks to "complete the chapter", "build chapter X", "render the chapter and upload", or wants to take raw Davidson source MDs from `/mnt/tb/Medicine/<chapter>/` and ship them to:
1. Rendered PNG infographics (via `/root/sea-knowledge-infographics/render_topic.py`)
2. Notion chapter pages (root + sub-pages)
3. MedSea static site (SPA per chapter, `/mnt/tb/Sea-knowledge/#MedSea/site/`)
4. GitHub backup (`https://github.com/SeaXen/MedSea`)
5. Local folder (`/mnt/tb/Sea-knowledge/<ch>. <name>/`)

### Reusable Scripts (in this skill's `scripts/`)

| Script | Purpose |
|---|---|
| `scripts/build_chapter_pipeline.py` | Single-chapter renderer + manifest + site backup. Run ONE chapter per invocation. |
| `scripts/restructure_medsea.py` | After build: flatten → nested `diseases/<hub>.<idx>-<slug>/topic.{md,png}` format that `build_site.py` expects. |

### The Pipeline (executed in order)

```bash
# 1. Build all chapters sequentially (NEVER in one Python process — SIGKILLs)
bash /tmp/build_final.sh   # wraps build_chapter_pipeline.py per chapter

# 2. Restructure MedSea diseases flat → nested
python3 scripts/restructure_medsea.py

# 3. Add new entries to build_site.py BUILT_CHAPTERS dict
#    (slug, display_name, notion_url, color_hex)
#    Public Notion URL: medsea.notion.site/Chapter-<N>-<title-slug>-<id-no-dashes>

# 4. Rebuild site
python3 /mnt/tb/Sea-knowledge/#MedSea/scripts/site/build_site.py

# 5. Rebuild Docker (no cache) + restart with correct port
#    CRITICAL: nginx inside the container listens on port 80 (see docker/nginx.conf),
#    so the host-to-container mapping MUST be `-p 8855:80`. Using `-p 8855:8855`
#    makes docker-proxy fail with "Connection reset by peer" — verified 2026-06-20.
docker build --no-cache -t medsea-site:latest /mnt/tb/Sea-knowledge/#MedSea
docker stop medsea && docker rm medsea
docker run -d --name medsea -p 8855:80 --restart unless-stopped medsea-site:latest

# 6. Commit + push (single large commit; ~5400 files for 12 chapters)
git -C /mnt/tb/Sea-knowledge/#MedSea add -A
git -C /mnt/tb/Sea-knowledge/#MedSea commit -m "Ch 19, 21, 23-32 + site rebuild"
git -C /mnt/tb/Sea-knowledge/#MedSea push origin main
```

### Pitfalls (validated)

| Pitfall | Fix |
|---|---|
| Multi-chapter Python script exits -9 (SIGKILL/OOM) | Shell wrapper invokes script per chapter |
| Renderer outputs to `<out>/<slug>/<slug>.png` (nested) | Move PNG to `<out>/<slug>.png`, `shutil.rmtree()` the nested dir |
| Disease MD threshold 12KB misses many 8-11KB Ch 26 diseases | Use 8000 bytes threshold |
| `diseases/<slug>.md` (flat) breaks `build_site.py` (expects `<hub>.<idx>-<slug>/topic.md`) | Run `scripts/restructure_medsea.py` after build |
| **Docker `-p 8855:8855` returns "Connection reset by peer"** | **Use `-p 8855:80` — nginx inside container listens on port 80, NOT 8855. The docker-proxy translates host 8855 → container 80. Verified 2026-06-20: `-p 8855:8855` made all curl requests fail; `-p 8855:80` served fine.** |
| `/tmp` 6.8GB tmpfs fills with `rclone` + build dirs | `rm -rf /tmp/rclone /tmp/ch27_combined` BEFORE long builds |
| `grep NOTION_API_KEY | head -1` returns wrong key (.env has two lines) | `head -2 | tail -1` |
| Notion `medsea.notion.site` URLs return 403 to headless curl | Don't curl-verify; trust the URL pattern |
| Terminal `cd` doesn't persist between tool calls | Use `subprocess.run(['git', '-C', '/full/path'])` |
| Container healthcheck uses wget which fails in Alpine (no IPv6 routing) | Replace wget with curl in HEALTHCHECK, OR fix nginx to also listen on 8855 |

### Source Layout Auto-Detection (in `build_chapter_pipeline.py`)

Two distinct source layouts:

- **flat:** diseases at top level (e.g. Ch 19, Ch 23). Hub-pages list diseases in `## Disease-Level Topics` tables with backtick-quoted `.md` names. Build script parses the table to map `disease → hub`.
- **subdirs:** diseases in subdirs (e.g. Ch 25, Ch 26). Build script uses parent folder name as hub.

Detection: if >50% of candidate MDs have `len(relative_parts) > 1` → subdirs, else flat.

### Combining Two 24th Ed Chapters into One 25th Ed (Ch 27 Pattern)

Ch 27 (Neurology & Stroke Medicine) in 25th Ed = Ch 25 Neurology + Ch 26 Stroke Medicine from 24th Ed. To build:

```bash
mkdir -p /tmp/ch27_combined
cp -r /mnt/tb/Medicine/Neurology/. /tmp/ch27_combined/
cp -r "/mnt/tb/Medicine/Stroke Medicine" /tmp/ch27_combined/20_Stroke_Medicine/
# Then build from /tmp/ch27_combined/
```

### Notion Public URL Recipe

```python
import re
def make_notion_url(ch_num, title, page_id):
    slug = re.sub(r'^Chapter \d+: ', '', title)
    slug = re.sub(r'[^A-Za-z0-9]+', '-', slug).strip('-')
    return f'https://medsea.notion.site/Chapter-{ch_num}-{slug}-{page_id.replace("-", "")}'
```

MedSea Notion DB: `3805588e-846f-808b-a23b-cf63c89f372e`, API version `2022-06-28`.

### Time Budget (12 chapters)

| Stage | Time |
|---|---|
| Build 12 chapters sequential | ~45 min |
| Restructure + site rebuild | ~2 min |
| Docker rebuild (no cache) | ~5 min |
| Git commit + push | ~3 min |
| **Total** | **~55 min** |

## References

| File | Purpose |
|------|---------|
| `references/davidson-ch5-population-health.md` | Worked example of completing Davidson Ch 5 (27 topics, 29 files) — exact file names, user verification ritual, web cross-check, stream-timeout split strategy |
| `references/davidson-ch22-nutritional-factors.md` | Worked example of completing Davidson Ch 22 (36 topics, ~1MB) — sub-agent (delegate_task) timeout failure mode, duplicate filename pitfall, MOC-update-as-final-step pattern, status standardization (3 values) |
| `references/davidson-24-ch25-hematology-hierarchy.md` | Pre-existing chapter reference |
| `references/verification-protocol.md` | Pre-existing verification reference |
| `references/davidson-ch27-medical-ophthalmology.md` | Worked example of completing Davidson Ch 27 (92 topics) — **duplicate-scaffold pitfall** (real sections in middle vs generic scaffold at end), MOC off-by-one, FIRST-occurrence audit pattern |
| `references/davidson-ch27-medical-ophthalmology-round2.md` | Round 2 of Ch 27: deeper audit caught 6 systemic files with `## MCQs (1)` / `## SBA Questions (0)`; 5 new topics created (Scleritis, Episcleritis, Endophthalmitis, CSCR, Behçet's); hub-level chapter mind map; bounded-block regex pattern; **metadata-only audit trap** |
| `references/davidson-ch25-neurology-placeholder-pattern.md` | Worked example for Ch 25 Neurology (218 topics, 19 sections) — **423-line template-skeleton pitfall** (INVERSE of scaffold trap), **working-dir reverts pitfall** (`git checkout --` to restore), **pre-scripted subagent batching** (overrides the Ch 22 "don't delegate_task" lesson for placeholder-replacement tasks). 7 sections, 164 files completed in one session. |
| `references/davidson-ch25-neurology-round2-placeholder-replacement.md` | Round 2 of Ch 25: completed remaining 41 placeholder files in ~3 minutes using direct `execute_code` with Python data structures (10x faster than subagents). Documents the **direct-Python-vs-subagent decision tree** (Lesson 3), the **execute_code sandbox non-persistence** pitfall, and the **audit-script section-header strict matching** behavior. |
| `references/davidson-ch19-32-build-pipeline-2026-06-19.md` | **Build & Publish Pipeline (NEW 2026-06-19):** Completed Ch 19, 21, 23-32 (12 chapters, 1461 PNGs). Captures the SIGKILL-on-multi-chapter fix (sequential per-chapter), renderer output flattening, source layout auto-detection (flat vs subdirs), Ch 27 combined-source pattern (Neurology + Stroke Medicine), MedSea restructure (flat → nested), Docker port mapping, /tmp tmpfs cleanup, Notion URL recipe, and 32-chapter final site stats. |
| `references/medsea-source-sync-2026-06-20.md` | **NEW 2026-06-20:** Source-sync workflow (Ch 1-15 + Ch 16-20). Three-layer "100% match" framework (topic / section / content presence). Source coverage table for all 20 chapters. Slug-matching bug fix (the recurring failure mode). Subdirectory vs flat MedSea layout. "Viva Questions" pattern for Ch 16. Frontmatter strip-before-prepend. Notion sync pattern reference. |

## Scripts

| File | Purpose |
|---|---|
| `scripts/chapter_audit.py` | **Content-depth verifier** for any Davidson chapter under `/mnt/tb/Medicine/`. Audits the FIRST occurrence of each required section. Counts items INSIDE `## MCQs`, `## SBA`, `## Mnemonics`, `## Mind Map` (tolerates both `1. **Q:**` and `**1.** Q:` formats, falls back to `Answer:` markers). Detects trailing duplicate scaffold (`CRITICAL FEATURES / FIRST-LINE TREATMENT / RED FLAGS`). Per-file table + aggregate counts + failing-file list with which sections are short. Exit 0/1 for CI. Run: `python3 scripts/chapter_audit.py "/mnt/tb/Medicine/Medical Ophthalmology"` |
| `scripts/detect_placeholders.py` | **Placeholder-content detector** that catches files which look complete by section-presence audit but contain `Option A`, `Drug A`, `ACRONYM = Expansion`, "based on the management section" etc. Run alongside `chapter_audit.py` because the audit script checks SECTION PRESENCE, not CONTENT QUALITY. Run: `python3 scripts/detect_placeholders.py /mnt/tb/Medicine/Neurology`. Exit 0 = clean, Exit 1 = placeholders found. Pairs with the `references/davidson-ch25-neurology-placeholder-pattern.md` workflow. |
| `scripts/build_chapter_pipeline.py` | **NEW 2026-06-19:** Single-chapter renderer + manifest + site backup. Run ONE chapter per invocation (multi-chapter Python exits -9 OOM). Reads source MDs from `/mnt/tb/Medicine/<chapter>/`, auto-detects flat vs subdir layout, calls `render_topic.py` per disease, flattens nested PNG output, copies to local Sea-knowledge folder + MedSea chapters backup, writes `manifest.json`. Run: `python3 build_chapter_pipeline.py "26" "Dermatology" "/mnt/tb/Medicine/Dermatology"` |
| `scripts/restructure_medsea.py` | **NEW 2026-06-19:** After build, converts MedSea `diseases/<slug>.md` (flat) to `diseases/<hub>.<idx>-<slug>/topic.{md,png}` (nested) — the format `build_site.py` expects. Looks up PNGs in the local Sea-knowledge folder via `manifest.json` and copies them. Run: `python3 restructure_medsea.py` (no args = all 12 known chapters) or `python3 restructure_medsea.py 26-dermatology` for one. |
| `scripts/medsea_sync.py` | **NEW 2026-06-20:** Source↔MedSea audit and fill tool. `audit <src> <ms_chapter>` prints topic count + per-section coverage (MCQ/SBA/Flash/Tracker/Scorecard) with source-vs-MedSea diff. `fill <src> <ms_chapter>` replaces gapped MedSea topics with source content + MedSea frontmatter. Handles flat + nested MedSea layouts, dedupes source by basename, recognizes `## VIVA QUESTIONS` as MCQ equivalent for Ch 16. Run: `python3 medsea_sync.py audit /mnt/tb/Medicine/Cardiology /mnt/tb/Sea-knowledge/#MedSea/chapters/16-cardiology` |

## "Check Files 1 by 1" User Verification Ritual (Recurring Pattern)

The user has asked **"is X fully complete or just scaffolded? Check files 1 by 1"** after every chapter completion (Diabetes, Endocrinology, Clinical Biochemistry, Population Health & Epidemiology). This is a FIRST-CLASS user pattern, not a one-off.

When the user asks this, the exact sequence that satisfies them:

1. **List every .md file** in the chapter folder with `ls` or `os.listdir`.
2. **For each file**, print: size (bytes), line count, status from frontmatter, file type (TOPIC/HUB).
3. **Section-compliance check** for `status: full-fcps-mrcp-note` files — verify all 14 required sections present (Learning Objectives, Mnemonics, Mind Map, Viva Questions, Spaced Repetition, Self-Test Scorecard, Local Navigation, etc.).
4. **Web-search the chapter** to cross-check hierarchy. Confirm chapter authors. Confirm topic list.
5. **Fix any non-compliant files** via `patch` (single-file upgrade, no rewrite).
6. **Re-run verification** and show before/after numbers.
7. **Show final stats**: total files, full topic notes count, hubs, scaffolds remaining, template compliance, total KB.

The user wants **audit numbers, not just a "done" claim**. They will repeat "check files 1 by 1" until they see:
- Each file listed with status icon
- Section compliance verified mechanically
- A "100% complete, 0 scaffolds" final stat

**Pitfall**: Hierarchy file or MOC may claim "100% complete" with ✅ markers, but actual file content may be missing sections. ALWAYS verify the actual file content, not just the tracking files.

## Auto-Generating MCQ/SBA/Flashcards from Existing Clinical Content (Validated Ch 1-32, 2026-06-21)

When the user asks **"all chapter complete add to exam and flashcard"** or **"add MCQ/SBA/flashcards a to z"**, the goal is full exam prep coverage across all 32 Davidson chapters. Some chapters (e.g. Ch 11, 19, 26) ship with explicit `## MCQs (10)` / `## SBA Questions (5)` / `## Flashcards` sections; others (e.g. Ch 1-9, 17, 20) have rich clinical content but no question sections. The two-pass extractor pattern fills the gap.

### Two-pass extractor (`/tmp/extract_questions.py`)

**Pass 1 — Index all files + collect fact pool:**
- Walk `site/<chapter>/diseases/` for both subdirectory topics (`<topic>/topic.md`) AND flat `.md` files
- For each file, check for explicit `## MCQs` / `## SBA Questions` / `## Flashcards` sections
- Mine a per-chapter fact pool from `## High-Yield Summary`, `## FCPS/MRCP High-Yield`, `## Definitions / Key Concepts` tables for MCQ distractors (deterministic random sample using `random.seed(qid)`)

**Pass 2 — Two output streams:**

1. **Explicit MCQ/SBA/Flashcards** — parse the `## MCQs (N)`, `## SBA Questions (N)`, `## Flashcards` sections using a fast state-machine parser (see parser pattern below). Handles 3 numbered formats:
   - `1. **Question text**` (opens bold, no close — extract after `**`)
   - `1. **Q:** Question text` (closes right after `Q:`)
   - 4-option (A-D) or 5-option (A-E) variants
   - Answer regex: `^\s*\**\s*Answer\s*:?\s*\**\s*([A-E])\s*\**\s*$` (handles `*Answer: X*`, `**Answer: X**`, `Answer: X`)

2. **Auto-generated questions** from clinical content when explicit sections are missing:
   - **Viva Questions table** (`## 9. Viva Questions` / `## Viva`) → Flashcards 1:1 (Q: front, A: back). Cap 10 per topic.
   - **High-Yield Summary table** (`## 8. FCPS/MRCP High-Yield Summary` / `## High-Yield Exam Points` / `## Definitions / Key Concepts`) → MCQs using template `"Which of the following is the correct statement about <topic>?"` with correct = fact_cell, distractors sampled from chapter's fact pool. Cap 8 per topic.
   - **One-Page Revision Card / Definitions table** → Flashcards (`Term? → Definition`). Cap 10 per topic.

### Fast state-machine parser pattern (`/tmp/parser_lib.py`)

Regex backtracking with `(?ms)` over 4,000+ MD files pegged CPU at 95% for 17 minutes without producing output. Rewriting as a line-by-line state machine (`for line in text.splitlines(): if line.startswith('## '): ...`) completed in 12 seconds — 100x faster.

```python
def parse_topic(text, chapter_num, chapter_name, chapter_slug, topic_slug):
    mcqs, sbas, flashes = [], [], []
    section, cur_q, cur_flash = None, None, None
    expecting_options = False

    NUM_RE = re.compile(r'^\s*(\d+)\.\s+\*\*(?:Q:\s*)?(.+?)\*\*\s*$')  # or just stem after **
    OPT_RE = re.compile(r'^\s*([A-E])\.\s+(.+?)\s*$')
    ANS_RE = re.compile(r'^\s*\**\s*Answer\s*:?\s*\**\s*([A-E])\s*\**\s*$', re.IGNORECASE)

    for line in text.splitlines():
        if line.startswith('## ') and not line.startswith('### '):
            # flush prev section
            section = ...  # 'mcq' | 'sba' | 'flash' | None based on line[3:].lower()
            continue
        if section in ('mcq', 'sba'):
            if (m := NUM_RE.match(line)):
                push_q(section)  # flush prev question
                cur_q = {'stem': m.group(2).strip(), 'options': {}, 'answer': None}
                expecting_options = True
            elif (m := OPT_RE.match(line)):
                cur_q['options'][m.group(1)] = m.group(2)
            elif (m := ANS_RE.match(line)):
                cur_q['answer'] = m.group(1).upper()
                expecting_options = False
        elif section == 'flash':
            if (m := re.match(r'^\s*-\s+Q:\s*(.+)$', line)):  # or **Q:** or - **Q:**
                cur_flash = {'front': m.group(1).strip(), 'back': None}
            elif (m := re.match(r'^\s*A:\s*(.+)$', line)) and cur_flash:
                cur_flash['back'] = m.group(1).strip()
                push_flash()
    push_q(section); push_flash()  # flush at EOF
    return mcqs, sbas, flashes
```

### Output schema (`site/assets/questions.json`)

```json
{
  "generated_at": "ISO timestamp",
  "version": 3,
  "totals": {"mcq": 19489, "sba": 2283, "flashcard": 20813, "chapters": 32},
  "chapters": [{"num": 1, "slug": "1-clinical-decision-making", "name": "Clinical Decision-Making",
                "mcq_count": 48, "sba_count": 0, "flashcard_count": 60, "topic_count": 6,
                "auto_generated_topics": 6, "hubs": 0}, ...],
  "mcq":     [{"id": "abc123", "chapter_num": 21, "chapter_name": "Diabetes", "chapter_slug": "...",
               "topic_slug": "21.10.4-...", "question": "Which of the following is the correct statement about <strong>HLA</strong>?",
               "options": {"A": "...", "B": "...", "C": "...", "D": "..."}, "answer": "A",
               "auto_generated": true}, ...],
  "sba":     [same shape],
  "flashcard": [{"id": "...", "front": "What is the primary HLA association with T1DM?",
                 "back": "HLA-DR3/DR4-DQ2/DQ8; DR3/DR4 heterozygous = highest risk (OR 15-20)",
                 "auto_generated": true}, ...]
}
```

### Caveats (be honest with user)

- **Auto-generated MCQs are templated** ("Which of the following is the correct statement about X?") — one correct fact + 3 random other facts from same chapter. Useful for recognition drill, NOT real exam-style clinical vignettes.
- **Distractors are random facts**, not curated plausible-but-wrong answers. They're functional but not high-quality.
- **Real SBAs only from chapters with explicit `## SBA Questions` sections** (mostly Ch 11, 19, 26). To get proper clinical vignettes for all 32 chapters would require generating new content, not just sync.
- **Tell the user the truth**: "auto-generated MCQs at templated quality — broad coverage for recall drill, but not exam-grade SBAs".

### Verified result (32/32 chapters, 2026-06-21)

| Chapters | MCQ | SBA | Flashcards |
|---|---|---|---|
| 11 Poisoning | 0 | 364 | 555 |
| 19 Biochemistry | 504 | 140 | 140 |
| 26 Dermatology | 4,413 | 1,490 | 4,316 |
| Ch 1, 5, 7 (auto-generated only) | 48 / 280 / 200 | 0 | 60 / 350 / 59 |
| **Total** | **19,489** | **2,283** | **20,813** |

DB size: 17 MB JSON. Loads instantly in browser via single fetch.

### Build the exam UI around this DB

The shared `site-header.js` already loads dynamic stats from this JSON. Build pages at `site/exam/index.html` and `site/flashcards/index.html` with the same shared header (logo + stats + search + chapters dropdown). Use `questions.json` as the single source of truth for chapter chips, available counts, and question pools. Persist user history to `localStorage` under key `medsea_exam_history_v1` with shape `{type, title, chapters, total, correct, duration_ms, breakdown: [...], started_at, finished_at}`.

## Integration with Other Skills

| Skill | When to Use Together |
|-------|---------------------|
| `academic-assignment-writing` | For general academic formatting (if not medical exam) |
| `writing-plans` | For creating chapter roadmaps and study sequences |
| `test-driven-development` | For verifying note completeness programmatically |
| `simplify-code` | Not applicable (medical notes, not code) |

---

## FORBIDDEN ACTIONS

| Action | Why |
|------|-----|
| Creating disease notes without all 13 sections | Incomplete for FCPS/MRCP |
| Marking `full-fcps-mrcp-note` without all 13 sections | Incomplete |
| Creating disease notes without mermaid diagrams | Missing algorithms/flowcharts |
- [ ] Missing YAML frontmatter | Identification fails |
| [ ] Missing Local Navigation | Broken cross-references |
| [ ] Missing MOC/MOC update | Tracking broken |
- [ ] **Trusting `status: scaffold` frontmatter blindly** | **CRITICAL PITFALL: Files may have 290–560 lines of full clinical content (MCQs, SBAs, Flashcards, Mind Maps) but frontmatter still says `scaffold`. ALWAYS verify actual content depth with `wc -l` + section grep before assuming scaffold. A 500-line file marked `scaffold` should be promoted to `full-fcps-mrcp-note` with a one-shot `sed` of the frontmatter line.** |
- [ ] **Trusting 423-line template-skeleton files** | **CRITICAL PITFALL (Neurology Ch 25, 2026-06-17):** The INVERSE of the scaffold pitfall. A file can be 423 lines, status: full-fcps-mrcp-note, but contain only placeholder text: "Option A", "Drug A", "Step 1 B. Step 2", "ACRONYM = Expansion". These look complete to size-based audits. **ALWAYS grep for placeholder markers before declaring a chapter complete:** `grep -lE "Option A|Drug A|ACRONYM.*Expansion|Step 1 B. Step 2" /path/to/chapter/**/*.md`. Placeholder content = NOT complete regardless of line count. |
- [ ] **STRIPPED topic pitfall (Ch 14 ID, Ch 2 TDM, Ch 10 ABG — 2026-06-20)** | **CRITICAL PITFALL:** MedSea `topic.md` files exist but contain ONLY the clinical sections (Definition, Aetiology, Clinical Features, Diagnosis, Management) — missing all the exam-prep sections (MCQs, SBAs, Flashcards, Spaced Repetition, Self-Test Scorecard, Mind Map, Viva Questions, FCPS/MRCP High-Yield, Answer Keys, Cross-Links). File is 8-12K chars, source equivalent is 25-40K. The build pipeline produced a "clinical summary" without the exam-prep apparatus. **Detection:** for each MedSea topic, compare section count to source — if MedSea has <15 sections and source has 25+, it's stripped. **Fix:** replace MedSea topic.md with source content (prepend MedSea YAML frontmatter). Verified pattern: 52 Ch 14 topics + 7 Ch 2 TDM topics + 1 Ch 10 ABG all stripped, all fixed with bulk source-copy. |
- [ ] **Working directory may have uncommitted reverts from a previous session** | **PITFALL (Neurology Ch 25, 2026-06-17):** Started session with many files showing as "modified" in `git status` and the diff showed -450+ lines per file (files SHRUNK from full version). The previous session had reverted files via patch but never committed. **First action on any chapter:** run `git status` and `git diff --stat HEAD` — if many files show as "modified" with negative line counts, run `git checkout -- Neurology/` to restore HEAD before auditing. |
| [ ] **Skipping duplicate-file check before batch creation** | When extending a chapter that already has files (e.g. adding Pneumocystis to a folder that already has `Amoebiasis & Giardiasis.md` and `Intestinal Protozoa (Amoebiasis, Giardiasis).md`), ALWAYS run a `ls \| sort` and fuzzy-match for "&" vs "and" duplicates BEFORE writing. Delete the duplicate. |
| [ ] **Reporting "100% complete" without checking actual file content line-by-line** | User explicitly checks each file when they say "Check files 1 by 1". NEVER trust the hierarchy file's "100% complete" claim or MOC ✅ markers alone — verify the actual file content has the required sections. Use the verification script below. |
| [ ] **Auditing LAST occurrence of each section when files have duplicate section names** | **CRITICAL PITFALL (Ch 27 Med Oph, 2026-06-17):** A previous audit reported 8/93 mnemonics and 0/93 mind maps as "real" because it regex-matched the LAST `## Mnemonics` / `## Mind Map` in each file. The actual content had a REAL topic-specific section in the middle AND a duplicate generic scaffold at the end (`CRITICAL FEATURES / FIRST-LINE TREATMENT / RED FLAGS`). The audit kept finding the scaffold. **ALWAYS audit the FIRST occurrence**, and explicitly detect + clean the trailing duplicate scaffold. See `references/davidson-ch27-medical-ophthalmology.md` and `scripts/chapter_audit.py`. |
| [ ] **Trusting a metadata-only audit (status field or section header text) without content check** | **CRITICAL PITFALL (Ch 27 Med Oph round 2, 2026-06-17):** Round 1 cleanup declared "100% complete ✅" after passing the `status: full-fcps-mrcp-note` check. The 6 short systemic files had `## MCQs (1)` and `## SBA Questions (0)` headings — the section-PRESENCE check passed but the section-CONTENT was missing 6 of the 14 required items. A metadata audit catches 0 of 6 deficient files. A status-from-heading audit catches 0 of 6. A content audit (count numbered items inside each section) catches 6 of 6. **Always run a content audit, not a metadata audit.** The `chapter_audit.py` script counts items inside each section. |
| [ ] **Using non-greedy regex with lookahead to rewrite one section at a time in files with mixed level-2 and level-3 headings** | **PITFALL (Ch 27 Med Oph round 2, 2026-06-17):** A regex like `## SBA Questions \(\d+\)\n.*?(?=^##\s|\Z)` looks safe but the non-greedy `.*?` still consumes too much when the next `## ` heading is far away and there are `### ` headings in between. The fix is a **bounded block** approach: find section start, find the next level-2 heading's offset, slice the bounded block, replace. See `references/davidson-ch27-medical-ophthalmology-round2.md` for the working pattern. |
| [ ] **Counting MCQs/SBAs by matching `^\*\*\d+\.\s+` only** | The chapter's actual MCQ format is `1. **Question:** ...` (number-then-bold), not `**1.** Question:` (bold-then-number). Audit regex returns 0 for every file. **Use max of both patterns** OR count by question markers (`Options:`, `Answer:`, `Q:`, `A:`). |
| [ ] **Mixing numbered and unnumbered level-2 section headings in the same chapter** | Files with `## 14. Mnemonics` and `## MCQs` (unnumbered) in the same chapter break audit regexes that match `^##\s+Mnemonics`. Pick one convention per chapter and stick to it. If the chapter is mid-state, accept the breakage and use `(?:\d+\.\s+)?` prefix in audit regexes. |
| [ ] **Reporting "100% complete" without web cross-check** | The user explicitly asked "search web is any topic missing" in the round-2 session. A chapter can be 100% by the in-folder audit and STILL be missing topics the standard curriculum expects. **Always do a 2-3 query web search** for the Davidson chapter TOC + cross-reference with the user's own MOC Tier lists before declaring complete. The 5 missing topics in Ch 27 (Scleritis, Episcleritis, Endophthalmitis, CSCR, Behçet's) were all visible in the user's MOC Tier 2/3 lists but absent as dedicated files. |
| [ ] **Trusting MOC total count without re-counting per-section** | When extending a chapter (adding a topic to an existing section), the MOC progress table can be off by one. Re-count files per section with `find` and update both the per-section column AND the TOTAL row. Ch 27 had Section 11 = 10 topics but MOC said 9. |
| [ ] **Reporting completion from a self-written audit without cross-checking against the file content** | A user-supplied audit that contradicts the file content (8/93 vs the visible real 92/92) is a signal the audit is wrong. Verify the audit, not the content. |

---

## Content-Depth Verification Protocol (MANDATORY before claiming completion)

**Why this matters**: In one session, the user found 14 files in `/mnt/tb/Medicine/HIV Infection and AIDS/` marked `status: scaffold` that actually contained 290–560 lines of full FCPS/MRCP content (MCQs, SBAs, Flashcards, Mind Maps, Mnemonics). The hierarchy file even claimed "15/15 TOPICS FULLY COMPLETE" — but the frontmatter was wrong. A `sed` to flip the status fixed the metadata, but only after I checked the actual file sizes and content.

**When user asks "is X complete? Check files 1 by 1"**, run:

```bash
# 1. Line count per file (catches under-fleshed scaffolds)
for f in /path/to/chapter/*.md; do
  size=$(wc -l < "$f")
  status=$(grep -m1 "^status:" "$f" | head -1)
  echo "$size lines | $status | $(basename "$f")"
done | sort -rn

# 2. Section presence check (catches scaffolds that have one section but not others)
for f in /path/to/chapter/*.md; do
  if grep -q "status: full-fcps-mrcp-note" "$f" 2>/dev/null; then
    missing=""
    for section in "Learning Objectives" "Mind Map" "Spaced Repetition" "Self-Test" "MCQs\|MCQ" "SBAs\|SBA" "Flashcards\|Viva"; do
      if ! grep -qE "$section" "$f" 2>/dev/null; then
        missing="$missing [$section]"
      fi
    done
    if [ -n "$missing" ]; then
      echo "MISSING SECTIONS in $(basename "$f"):$missing"
    fi
  fi
done
```bash
# 3. Quick promote-scaffold-but-actually-full audit
for f in *.md; do
  if grep -q "^status: scaffold$" "$f" 2>/dev/null; then
    lines=$(wc -l < "$f")
    if [ "$lines" -gt 200 ]; then
      echo "CANDIDATE FOR PROMOTION ($lines lines, status=scaffold): $(basename "$f")"
    fi
  fi
done
```

```bash
# 4. Placeholder-content audit (Neurology Ch 25 lesson, 2026-06-17)
# Files may have status: full-fcps-mrcp-note, 423+ lines, all 14 sections present
# but contain placeholder text like "Option A", "Drug A", "ACRONYM"
# This is the INVERSE trap of the scaffold-but-actually-full case above
for d in 01_* 02_* 03_* 04_* 05_* 06_* 07_* 08_* 09_* 10_* 11_* 12_* 13_* 14_* 15_* 16_* 17_* 18_* 19_*; do
  for f in "$d"/*.md; do
    if [ -f "$f" ] && [[ "$(basename "$f")" != *"Hub"* ]]; then
      if grep -qE "Option A|Drug A|ACRONYM.*Expansion|Step 1 B. Step 2|based on the management section" "$f" 2>/dev/null; then
        echo "PLACEHOLDER CONTENT: $f"
      fi
    fi
  done
done
```

**Action**: If a file has `status: scaffold` but ≥200 lines and contains the required sections, promote it:

```bash
# Bulk promote over-fleshed scaffolds
for f in *.md; do
  if grep -q "^status: scaffold$" "$f" 2>/dev/null; then
    sed -i 's/^status: scaffold$/status: full-fcps-mrcp-topic-note/' "$f"
  fi
done
```

**Then report both before and after counts to the user** — the user wants to see the audit numbers, not just a "done" claim.

## Hub Files Get Real Chapter-Level Content (Not Generic Placeholders)

Hub files (`Status: full-fcps-mrcp-hub` — Hierarchy, MOC, Roadmap) serve a
different audience than topic files: they help a student NAVIGATE the
chapter, not learn one disease. A hub file with a generic placeholder
Mnemonics+Mind Map block is a missed opportunity.

**When you create or refresh a hub file, include:**

1. **Cross-topic mnemonics** — 8-10 mnemonics that span the whole chapter
   (e.g. "Red Eye = 5 C's" for ophthalmology, "HLA-B27 = PAIR" for
   spondyloarthropathies, "5-4-3-2-1" for endocrine emergencies).
2. **Chapter-level mind map** — a mermaid `mindmap` with one branch per
   section, listing every topic file in that section. This becomes the
   student's mental map of the chapter.
3. **Cross-references to other chapters** — where the same disease is
   covered more deeply elsewhere (e.g. GCA in both Medical Ophthalmology
   and Rheumatology).

Don't put the same `CRITICAL FEATURES / FIRST-LINE TREATMENT / RED FLAGS`
placeholder in a hub file that you cleaned out of topic files.

## File Size Sweet Spot for Single-File Writes

| File size | Single `write_file` works? | Notes |
|---|---|---|
| <20 KB | ✅ always | Safe to write in one go. |
| 25-30 KB | ✅ usually works | The sweet spot for new disease files. All 5 new Ch 27 files in round 2 were 25-30KB, written in one call, no timeout. |
| 30-35 KB | ⚠️ may timeout on slow connections | If it does, split into 2 chunks (front + back). |
| 35+ KB | ✗ often times out | Apply the 4-chunk rule from the Ch 22 lesson: frontmatter + LO + Def/Aetiology/Clinical / Investigations / Management / Mnemonics+Mind Map+SR+Tags. |

**Don't** reflexively split files into chunks when they're under 30 KB —
that's wasted overhead. Only chunk when the file is too large for the
8K-token argument limit AND/OR the connection is slow.

## Web Cross-Check Before Declaring 100% Complete (User Recurring Ask)

The user repeatedly asks "search web is any topic missing". A
metadata-only audit can say "100%" and the chapter is STILL missing
topics the standard curriculum expects. Before claiming complete:

1. `web_search` for `"Davidson 24th edition chapter [N] [specialty] table of contents"`. Look for the actual section list.
2. Cross-reference with NIH library catalog (`onesearch.nihlibrary.ors.nih.gov`), Elsevier inspection copy, Google Books, ResearchGate paper titles.
3. Compare with the user's own MOC Tier 1/2/3 lists — these usually enumerate the high-yield topics the user wants covered.
4. Create any missing topics as full 14-section files BEFORE running the final content audit.
5. Re-run `chapter_audit.py` and confirm zero ✗.

**This is what caught the 5 missing topics in Ch 27 round 2**: the user's
MOC explicitly listed Scleritis (Tier 3), Endophthalmitis, CSCR (Tier 2),
Behçet's (Tier 3) — but the chapter folder had no dedicated files for any
of them. The 92/92 "complete" claim was technically true (every folder
file was complete) but the chapter as a whole was incomplete.

## Bounded-Block Regex Pattern for One-Section Rewrites

When you need to rewrite one specific section in a file (e.g. upgrading
`## MCQs (1)` to `## MCQs (10)`), do NOT use a regex like
`## MCQs \(\d+\)\n.*?(?=^##\s|\Z)`. The non-greedy `.*?` still consumes
too much when the next `## ` heading is far away and there are `### `
level-3 headings in between.

Use a bounded block instead:

```python
def rewrite_section(filepath, section_pattern, new_content):
    with open(filepath) as f:
        c = f.read()
    m = re.search(r'^##\s+' + section_pattern + r'.*$', c, re.M)
    if not m: return False
    start = m.start()
    # Find next level-2 heading after this section
    next_m = re.search(r'^##\s+', c[start+5:], re.M)
    end = start + 5 + next_m.start() if next_m else len(c)
    new_c = c[:start] + new_content + c[end:]
    with open(filepath, 'w') as f:
        f.write(new_c)
    return True
```

This is reliable across files that have:
- `### ` (level-3) headings inside the bounded block.
- Numbered `## N. Title` and unnumbered `## Title` headings mixed.
- Multi-paragraph section bodies that span many lines.

---

## Cross-Chapter / Cross-Folder Duplicates

Some Davidson topics naturally appear in **two folders** (e.g. HIV/AIDS lives in both Ch 12 dedicated folder and the Ch 11 Infectious Disease syndromic folder; TB meningitis in Ch 13 + Ch 17 Respiratory; STIs in Ch 15 + Ch 13). When completing a chapter:

1. **Check if a dedicated chapter folder already exists** with `ls /mnt/tb/Medicine/ | grep -iE "hiv|ch12"`.
2. **If a topic file exists in BOTH locations**, treat them as cross-references, not duplicates. Both can stay if they cover different angles (e.g. dedicated chapter = deep HIV overview; syndromic = HIV OI in a differential).
3. **For true duplicates** (same topic, same angle, e.g. `Amoebiasis & Giardiasis.md` and `Intestinal Protozoa (Amoebiasis, Giardiasis).md` in the same folder), pick the more complete one and `rm` the other. Check by line count + section grep.

---

## Update Protocol

When this skill needs updating (new requirements, format changes, new Davidson edition):
1. Run verification commands to identify gaps
2. Update the template file first
3. Update existing notes to match new template
4. Update MOC with new checkboxes
5. Update hierarchy checkboxes
6. Commit with descriptive message

---

## Tags

medical, exam-preparation, fcps, mrcp, davidson-medicine, medical-notes, exam-preparation, template, davidson-24