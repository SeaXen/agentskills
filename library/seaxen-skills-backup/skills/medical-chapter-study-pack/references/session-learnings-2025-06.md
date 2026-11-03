# Session Learnings (June 2025 - Infectious Disease/STI/HIV Completion)

## User Workflow Preferences (Davidson Chapter 13/14/15 Completion)

### Folder Structure
- Root: `/mnt/tb/Medicine/`
- Chapter folders: `/mnt/tb/Medicine/Infectious Disease/`, `/mnt/tb/Medicine/HIV Infection and AIDS/`, `/mnt/tb/Medicine/Sexually Transmitted Infections/`
- Topic files: `/mnt/tb/Medicine/<Chapter>/<Topic Name>.md`
- Larger topics can have subfolders: `/mnt/tb/Medicine/HIV Infection and AIDS/<Subtopic>.md`
- Subfolder MOCs: `<Chapter> MOC.md` inside each chapter folder

### Git Workflow
- Batch commits after completing 5-15 topics
- Commit message format: `"Chapter: Add N full FCPS/MRCP topic notes"` with bullet list
- Push to `origin/main` after each batch
- Verify with `git status --short` after push

### MOC Maintenance
- Keep `Infectious Disease MOC.md` updated with completion status
- Mark completed topics with ✅ and `full-fcps-mrcp-topic-note` status
- Subfolder MOCs (HIV, STI) track their own subtopic completion
- Cross-link in `00_Index/Medicine MOC.md` when chapter completes

### Frontmatter Requirements (Validated)
```yaml
---
tags: [medicine, <specialty>, davidson, fcps, mrcp, <subtopic>]
chapter: <Chapter Name>
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter XX: <Chapter Title>
topic_category: <Domain> Domain
status: full-fcps-mrcp-topic-note
---
```

### Content Structure (Validated Pattern - 23/23 topics)
All notes must include these sections in order:
1. Header + priority callout
2. Learning Objectives (checkbox list)
2. Definition & Epidemiology (table)
3. Aetiology/Pathophysiology (mermaid flowchart + tables)
4. Clinical Features (tables for patterns)
4. Classification/Criteria (current criteria with scoring tables)
5. Differential Diagnosis (table with distinguishing features)
6. Diagnosis/Investigations (labs, imaging tables)
7. Management (mermaid algorithm + step-by-step tables with doses/durations)
7. Special Populations (pregnancy, renal, elderly, etc.)
8. Complications (table)
8. FCPS/MRCP High-Yield Summary (dense table)
9. Common Viva Questions (scenario + expected answer)
9. Confusions & Mnemonics (table + mnemonic section)
9. Mind Map (mermaid mindmap)
10. Flowchart (mermaid flowchart)
10. One-Page Revision Card (dense table)
11. Spaced Repetition Trackers (24h/7d/15d/30d)
11. Self-Test Scorecard (section scoring)
12. Local Navigation (WikiLinks to parent hubs, MOC, hierarchy)
13. Exam Answer Modes (Long, Short, Viva, Ward, Last-Night)
13. Must Know/Should Know/Nice to Know
14. Self-Test Scorecard
14. Last-Night-Before-Exam Sheet
14. Summary
15. MCQs (10) + SBAs (10) with explanations
15. Flashcards
15. Answer Keys with Explanations

### Exam Answer Modes Required
- Long Answer Skeleton
- Short Note Skeleton
- Viva One-Liners
- Ward-Case Discussion Points
- Last-Night-Before-Exam Sheet

### Assessment Content
- 10 MCQs with explanations
- 10 SBA Questions with explanations
- Flashcards (Q/A format)
- Answer Keys with Explanations
- Answer Keys with Explanations for SBAs

### Mermaid Standards
- Flowcharts: LR for algorithms, TD for cascades
- Mindmaps: `mindmap` type
- Max 5-6 levels deep
- Use emoji/status in node labels

### Revision Trackers
- 24h, 7d, 15d, 30d checkboxes
- Self-Test Scorecard (5 domains /10 each = /50)
- Must Know / Should Know / Nice to Know tables

### File Output
- Write actual `.md` files to `/mnt/tb/Medicine/...`
- Commit and push after each batch
- Verify with `git status --short` after push

### Cross-Chapter Linking
- HIV/STI subtopics live in their own folders but link from main Infectious Disease MOC
- Subfolder MOCs track their own subtopic completion
- `00_Index/Medicine MOC.md` links to all chapter MOCs