# Infectious Disease (Davidson Chapter 13) — Live Vault Topic Production Workflow

## Overview
This reference documents the proven workflow for producing full FCPS/MRCP topic notes for Infectious Disease (Davidson Chapter 13) in the user's Obsidian vault at `/mnt/tb/Medicine/Infectious Disease/`.

## User Preferences (from session)
- **Actual file writes required** — not chat output only
- **Full template structure** with all 13+ sections
- **Obsidian-friendly Markdown** with wikilinks, callouts, mermaid diagrams
- **Git commit after each batch** — path-scoped to Infectious Disease folder
- **High-yield first ordering** — sepsis, CAP, TB, meningitis, endocarditis, etc.
- **Status frontmatter**: `status: full-fcps-mrcp-topic-note`
- **Tags**: `[medicine, infectious-disease, davidson, chapter13, <topic>, fcps, mrcp]`

## Topic Production Order (High-Yield First)
1. Sepsis and Septic Shock
2. Fever and Septic Syndrome Approach
3. Infective Endocarditis
4. Community-Acquired Pneumonia (CAP)
5. Hospital-Acquired and Ventilator-Associated Pneumonia (HAP/VAP)
6. Tuberculosis (Pulmonary and Extrapulmonary)
7. Acute Bacterial Meningitis
8. Clostridioides difficile Infection (CDI)
9. Urinary Tract Infections (Complicated, CA-UTI, Pyelonephritis)
10. Intra-abdominal Infections (Secondary Peritonitis, Abscess)
11. Skin and Soft Tissue Infections (SSTI)
12. Febrile Neutropenia
13. HIV Infection and AIDS
14. Sexually Transmitted Infections (STIs)
15. Malaria
16. Fungal Pneumonias
17. Influenza and Respiratory Viruses
18. Tuberculous Meningitis
19. Viral Encephalitis and Meningitis
20. Brain Abscess
21. Antimicrobial Prescribing Principles
22. Infective Diarrhoea and Food Poisoning
23. Cellulitis and Necrotising Fasciitis

## Required Template Sections (All Must Be Present)
1. Frontmatter with tags, davidson_chapter, topic_category, status
2. Related wikilinks + `> [!important]` summary box
3. Learning Objectives
3. Definitions / Core Microbiology / Normal Values
4. Clinical Features / Classification / Aetiology tables
5. Diagnosis / Investigations / Approach Algorithm (mermaid flowchart)
6. Empirical + Targeted Therapy tables with doses/durations
7. Severity Assessment (CURB-65, IDSA/ATS, MASCC, LRINEC, PEDIS, etc.)
8. Complications / Special Situations tables
9. FCPS/MRCP High-Yield Points (bulleted)
10. Common Viva Questions (8-12)
11. Common Confusions / Exam Traps (table)
12. Mnemonics
13. Mind Map (mermaid)
14. Flowchart (mermaid)
15. Suggested Visuals / Video References
16. One-Page Revision Summary (table)
17. 24-Hour Recall Prompts
18. 7/15/30-Day Revision Tracker (checkboxes)
19. Must Know / Should Know / Nice to Know
20. My Weak Points (checkboxes)
21. Self-Test Scorecard
22. Exam Answer Modes (Long/Short/Viva/Ward-Case/Last-Night)
23. Summary (paragraph)
24. MCQs (10) + SBA Questions (10) + Flashcards
25. Answer Key with Explanations

## Git Workflow (Batch Commit)
```bash
cd /mnt/tb/Medicine
git add "Infectious Disease/<Topic1>.md" "Infectious Disease/<Topic2>.md" ...
git commit -m "Infectious Disease: Add <N> full FCPS/MRCP topic notes (high-yield first)

- <Topic1>
- <Topic2>
...

All notes include: learning objectives, diagnosis, empirical/targeted therapy with doses/durations, severity criteria, complications, FCPS/MRCP high-yield points, viva questions, confusions/traps, mnemonics, mind maps, flowcharts, 24h recall, revision trackers, 10 MCQs, 10 SBAs, flashcards, answer keys with explanations.

Updated Infectious Disease MOC with completed topic tracking."
git push origin main
```

## MOC Update Pattern
After each batch, update `Infectious Disease/Infectious Disease MOC.md`:
- Mark completed topics with `✅ full-fcps-mrcp-topic-note`
- Update "Starter Topic Queue" and "All Topic Notes" sections
- Update task checkboxes

## Related Subfolders (Already Complete)
- `HIV Infection and AIDS/` — 11 subtopic notes
- `Sexually Transmitted Infections/` — 9 subtopic notes

## Pitfalls to Avoid
- **Don't stop at chat output** — user expects real `.md` files
- **Don't omit sections** — all 25 sections required
- **Don't use placeholder MCQs/SBAs** — must be 10 each with explanations
- **Don't forget mermaid diagrams** — mind map + flowchart minimum
- **Don't forget wikilinks** — `[[Related Topic]]` format
- **Don't skip git commit** — batch commit expected after each batch
- **Don't guess durations/doses** — use standard guidelines (IDSA, WHO, BASHH, NICE)

## Quality Checks Before Commit
- [ ] All 25 sections present
- [ ] Frontmatter complete with correct tags
- [ ] Wikilinks use `[[...]]` format
- [ ] Mermaid blocks render correctly
- [ ] Tables use proper markdown pipe syntax
- [ ] MCQs: 10 questions, 5 options each, correct answer marked
- [ ] SBAs: 10 clinical scenarios, 5 options each
- [ ] Flashcards in `Q: / A:` format
- [ ] Answer keys match question numbers
- [ ] MOC updated with new topics marked ✅

## Session Patterns That Worked
- **Batch size**: 5-14 topics per session
- **Order**: High-yield first (sepsis, CAP, TB, meningitis, endocarditis)
- **Parallel tracking**: HIV and STI subfolders already had complete subtopic notes
- **User verification**: `wc -l` on files, `git status --short`, live browser check not needed for markdown files

## Cross-References
- See `references/nephrology-live-vault-topic-production.md` for nephrology pattern
- See `references/respiratory-live-vault-topic-production.md` for respiratory pattern
- See `references/cardiology-live-vault-topic-production.md` for cardiology pattern
- See `references/neurology-live-vault-topic-production.md` for neurology pattern
- See `references/gastroenterology-live-vault-topic-production.md` for GI pattern