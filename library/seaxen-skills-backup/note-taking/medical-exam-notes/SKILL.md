---
name: medical-exam-notes
description: Standardized workflow for creating high-yield medical exam notes (FCPS/MRCP/USMLE) from authoritative textbooks with structured templates, hierarchy alignment, and exam-focused content
category: note-taking
tags: [medical, exam-notes, fcps, mrcp, davidson, template, spaced-repetition]
---

# Medical Exam Notes — Standardized Creation Workflow

## Purpose
Create consistent, high-yield medical notes aligned to authoritative textbooks (Davidson, Harrison, Kumar & Clark) for postgraduate exam preparation (FCPS, MRCP, USMLE). Each note follows a validated template with pathophysiology diagrams, diagnostic algorithms, management flowcharts, and exam-focused elements.

---

## Trigger Conditions
- Building a new chapter/system from a standard textbook
- Upgrading scaffold notes to full exam-ready notes
- Creating subject-specific note banks for FCPS/MRCP/USMLE
- Any project requiring 10+ structured medical notes with consistent formatting

---

## Prerequisites
- Authoritative textbook edition identified (e.g., "Davidson 24th Edition, Chapter 26: Rheumatology and bone disease")
- Chapter hierarchy mapped (heading hubs → topic groups → disease topics)
- Target exam(s) defined (FCPS, MRCP Part 1/2, PACES, USMLE Step 2/3)
- Git repository initialized for version control

---

## Standard Template (All Notes Must Include)

### 1. Frontmatter (YAML)
```yaml
---
tags: [medicine, specialty, textbook, topic, fcps, mrcp]
chapter: Specialty
textbook_part: Part X
textbook_chapter: Chapter Y: Chapter Title
heading: Heading Hub Name
topic_group: Topic Group Name
topic: Disease/Topic Name
status: scaffold | full-fcps-mrcp-note
priority: critical | high | medium
cards: 15-25
created: YYYY-MM-DD
modified: YYYY-MM-DD
exam_relevance: [FCPS, MRCP Part 1, MRCP Part 2, PACES]
see_also:
  - "[[Related Topic 1]]"
  - "[[Related Topic 2]]"
---
```

### 2. Required Sections (in order)
1. **Learning Objectives** — checkbox list of 6-10 specific, measurable outcomes
2. **Epidemiology/Definition** — concise table with key demographics
3. **Pathophysiology** — mermaid flowchart + key concepts table
4. **Clinical Features** — organized by system/pattern with FCPS/MRCP pearls
5. **Classification Criteria** — current validated criteria (ACR/EULAR, Yamaguchi, Jones, etc.)
6. **Diagnosis/Investigations** — diagnostic algorithm (mermaid) + investigation table
7. **Differential Diagnosis** — comparison table with distinguishing features
8. **Management** — step-up algorithm (mermaid) + drug tables with doses/monitoring
9. **Complications** — table with frequency and detail
10. **Special Populations** — pregnancy, paediatrics, renal/hepatic impairment, elderly
11. **FCPS/MRCP High-Yield Summary** — bullet table of exam-critical points
12. **Viva Questions** — 8-12 questions with expected answers (PACES/FCPS style)
13. **Confusions & Mnemonics** — clarification table + memory aids
14. **Mind Map** — mermaid mindmap of entire topic
15. **One-Page Revision Card** — condensed table for last-minute review
16. **Spaced Repetition Trackers** — 24h/7d/15d/30d/90d with confidence rating
17. **Self-Test Scorecard** — section-by-section scoring
18. **Local Navigation** — wiki-links to parent, siblings, chapter map, MOC, drug/investigation refs

---

## Workflow Steps

### Phase 1: Scaffold & Hierarchy (One-time per chapter)
```
1. Read textbook chapter → extract full hierarchy
2. Create MOC (Map of Content) with:
   - Heading hubs (scaffold-hub)
   - Topic groups (scaffold-hub)
   - Disease topics (scaffold)
   - Core preserved notes (if any)
3. Create chapter roadmap with:
   - Exam weight mapping
   - Recommended study sequence
   - Phase-based timeline
4. Create standard template file
5. Git commit: "Chapter X scaffold system complete"
```

### Phase 2: Batch Note Creation (5-8 notes per commit)
```bash
For each priority topic:
1. Read source textbook section + guidelines (EULAR/ACR, BSR, NICE)
2. Create note using standard template
3. Include ALL 18 sections
4. Validate: mermaid renders, wiki-links resolve, no missing sections
5. **Stream Timeout Prevention**: If note > ~8K tokens, split into 2-3 write_file calls (e.g., frontmatter+sections 1-9, sections 10-18)
6. Batch commit after 5-8 notes with descriptive message (stream timeout safe)
7. Update MOC with ✅ for completed topics
8. Update chapter roadmap progress
```

**Stream Timeout Prevention**: The Hermes write tool has ~8K token limit per call. Large notes (>15K tokens) must be split across multiple write_file calls. Typical FCPS/MRCP note with all 18 sections = 12-20K tokens. Split strategy: first write frontmatter + sections 1-9, second write sections 10-18.

**Critical Session Learnings (Diabetes Chapter 25 / Hepatology 24 / Stroke 29)**:\n- **execute_code with batched write_file calls causes stream timeouts** — even 10 notes in a single execute_code script timed out. Use individual `write_file` calls per note instead of batching in execute_code.\n- **Practical batch size limit**: 5-10 notes per session using individual `write_file` calls; 10+ notes in execute_code triggers stream timeout (~8K token limit per tool call).\n- **Directory creation must be done UPFRONT** — create ALL section directories with `mkdir -p` (quoted paths for special characters like `&`, `,`, `(`) before writing any notes.\n- **File size per write_file**: keep each call under ~8K tokens. For large notes (200+ lines, 15K+ tokens), split into 2-3 write_file chunks:\n  - Chunk 1: Frontmatter + Learning Objectives + Definition/Epidemiology + Aetiology/Pathophysiology + Clinical Features\n  - Chunk 2: Classification/Staging + Diagnosis/Differentials + Investigations\n  - Chunk 3: Management + FCPS/MRCP High-Yield + Viva Questions + Confusions/Mnemonics + Mind Map + Revision Card + Trackers + Scorecard + Navigation\n\n**Hepatology Chapter 24 / Stroke 29 Specific Learnings (Session 2026-06-14)**:\n- **Total coverage**: 143 Hepatology notes (~90% of 158 topics) + 131 Stroke notes (86/86 = 100% complete per MOC)\n- **Hepatology**: 143 files covering 14 sections; Stroke: 131 files covering 86/86 topics (100% complete)\n- **Large note chunking pattern** (4 chunks for hepatology/stroke notes >200 lines):\n  - Chunk 1: Frontmatter + Learning Objectives + Definition/Epidemiology + Aetiology/Pathophysiology + Clinical Features\n  - Chunk 2: Classification/Staging + Diagnosis/Differentials + Investigations\n  - Chunk 3: Management + FCPS/MRCP High-Yield + Viva Questions\n  - Chunk 4: Confusions/Mnemonics + Mind Map + Revision Card + Trackers + Scorecard + Navigation\n- **Verification protocol**: `search_files pattern: \"status: full-fcps-mrcp-note\" path: [chapter_dir]` after each batch; `wc -l` on new files\n- **Git workflow**: Descriptive commits with batch summaries; `git push` after verification\n- **Template usage**: Hepatology-specific template (scoring tables, LI-RADS, BCLC, Child-Pugh/MELD); Stroke-specific template (14-section with stroke-specific imaging/reperfusion/rehab sections)

### Phase 3: Quality Assurance
```bash
- Search for "status: full-fcps-mrcp-note" using search_files → verify count matches MOC
- Check all wiki-links resolve (no broken references)
- Verify mermaid diagrams are syntactically correct
- Ensure consistent drug names, doses, monitoring across notes
- Cross-reference drug/investigation reference notes
```

---

## Priority Ordering (Davidson Rheumatology Example)

### Must Know (Core) — Batch 1
1. Rheumatoid Arthritis
2. Systemic Lupus Erythematosus
3. Osteoarthritis
4. Gout
5. Osteoporosis
6. Septic Arthritis
7. Polymyalgia Rheumatica / GCA
8. Vasculitis (ANCA patterns)
9. Ankylosing Spondylitis
10. Psoriatic Arthritis

### Should Know (High Yield) — Batches 2-3
11-18. Crystal arthropathies, Scleroderma, Sjögren's, Myositis, APS, Osteomalacia, Paget's, Reactive Arthritis, Kawasaki, PMR/GCA overlap, etc.

### Nice to Know (Advanced) — Later
19-25. Behçet's, Relapsing Polychondritis, Still's Disease, IgG4-related, CRPS, Fibromyalgia, etc.

---

## Git Commit Convention
```
Rheumatology: [N] full FCPS/MRCP notes (total [TOTAL])

Completed batch of [N] high-yield topics:
[List topics with section codes]

All notes: Learning objectives, pathophysiology mermaid diagrams, diagnostic algorithms, management flowcharts, FCPS/MRCP high-yield tables, viva questions, mind maps, one-page revision cards, spaced repetition trackers, self-test scorecards.

Total: [TOTAL]/78 disease-level topics complete ([X]%). MOC updated with tracking.
```

---

## MOC Maintenance
- After each batch, update Rheumatology MOC with:
  - Updated count
  - ✅ wiki-links for each completed topic
  - Organized by section (Clinical Approach, Inflammatory, Autoimmune, etc.)
- Update chapter roadmap with completion status

---

## Common Pitfalls & Fixes

| Pitfall | Prevention |
|---------|------------|
| Inconsistent drug doses across notes | Maintain drug reference note; cross-reference during QA |
| Broken wiki-links | Use relative paths `[[../Topic]]`; validate with search after each batch |
| Mermaid syntax errors | Test render in editor; use consistent node IDs |
| Missing sections in template | Checklist validation before commit |
| **MOC drift (count mismatch)** | Automated count via `search_files` for `status: full-fcps-mrcp-note` (not grep — searches rendered content) |
| Duplicate content across notes | Use `see_also` links instead of copying; create shared reference notes |
| **Stream timeout on large write_file** | Split large notes (>8K tokens) into 2-3 write_file calls; max ~15K tokens per note requires 2 writes |
| **Batch commit too large** | Limit to 5-8 notes per commit; 10-15 causes stream timeout on git operations |
| **MOC verification drift** | After each batch, run `search_files` for `status: full-fcps-mrcp-note` and verify count matches MOC |

---

## Support Files
- `references/medical-exam-template.md` — Complete template with all 18 sections
- `references/davidson-24-ch26-hierarchy.md` — Full hierarchy map for Rheumatology
- `references/stream-timeout-workaround.md` — Stream timeout workaround for large notes (>8K tokens), split-write pattern, batch size optimization
- `templates/medical-topic-note.md` — Starter file with frontmatter + section headers
- `scripts/validate-links.py` — Python script to verify all wiki-links resolve (run from chapter root: `python scripts/validate-links.py`)

---

## Quality Checklist (Per Note)
- [ ] All 18 sections present
- [ ] Frontmatter complete with correct status/priority
- [ ] Mermaid diagrams render (flowchart, mindmap)
- [ ] No orphaned wiki-links
- [ ] Drug doses match reference note
- [ ] Viva questions have expected answers
- [ ] Mnemonics are original/verified
- [ ] Spaced repetition tracker has 5 intervals
- [ ] Self-test scorecard has all sections
- [ ] Local navigation includes parent, chapter map, MOC, drug/investigation refs

---

## Scaling Notes
- This workflow scales to any medical specialty (Cardiology, Neurology, Respiratory, etc.)
- Template adapts to different exam targets (USMLE adds more basic science; MRCP adds more clinical scenarios)
- Spacing repetition trackers work with Anki export if needed
- MOC pattern works for any textbook chapter hierarchy