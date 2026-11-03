# FCPS/MRCP Full Note Template (Validated Pattern)

This template was validated across Cardiology (111 topics) and Rheumatology (10 topics) chapters.

## Frontmatter (YAML)
```yaml
---
tags: [medicine, <specialty>, davidson, fcps, mrcp, <subtopic>]
chapter: <Chapter Name>
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter XX: <Chapter Title>
heading: <Heading Hub Name>
topic_group: <Topic Group Name>
topic: <Disease/Topic Name>
status: full-fcps-mrcp-note
priority: high|critical|medium
cards: 15-25
created: YYYY-MM-DD
modified: YYYY-MM-DD
exam_relevance: [FCPS, MRCP Part 1, MRCP Part 2, PACES]
see_also:
  - "[[Related Topic 1]]"
  - "[[Related Topic 2]]"
---
```

## Required Sections (in order)

1. **Header** — Title + priority callout
2. **Learning Objectives** — Checkbox list, exam-actionable
3. **Definition & Epidemiology** — Table format
4. **Aetiology & Pathophysiology** — Mermaid flowchart + key concepts table
5. **Clinical Features** — Tables for patterns, joint distributions, examination findings
6. **Classification/Criteria** — Current criteria (ACR/EULAR, SLICC, etc.) with scoring tables
7. **Differential Diagnosis** — Table with distinguishing features
8. **Diagnosis/Investigations** — Tables for labs, imaging, synovial fluid, etc.
9. **Management** — Mermaid algorithm + step-by-step tables
10. **Special Populations** — Pregnancy, CKD, elderly, etc.
11. **Complications** — Table
12. **FCPS/MRCP High-Yield Summary** — Dense table
13. **Viva Questions** — Table with scenario + expected answer
14. **Confusions & Mnemonics** — Table + mnemonic section
15. **Mind Map** — Mermaid mindmap
16. **One-Page Revision Card** — Dense table
17. **Spaced Repetition Trackers** — 24h/7d/15d/30d/90d
18. **Self-Test Scorecard** — Section scoring
19. **Local Navigation** — WikiLinks to parent hubs, MOC, hierarchy

## Mermaid Diagram Standards

- **Flowcharts**: LR (left-right) for algorithms, TD (top-down) for cascades
- **Mindmaps**: `mindmap` type
- **Color coding**: Use emoji/status in node labels
- **Keep readable**: Max 5-6 levels deep

## Table Standards

- Markdown pipe tables
- Header row + separator row required
- Max 4-5 columns for readability
- Bold key terms in cells

## Exam Content Density

- Every section must have explicit FCPS/MRCP pearls
- Viva questions must match PACES/FCPS clinical style
- Mnemonics should be original or sourced from standard texts
- One-page card must fit on one screen (mobile-friendly)

## File Naming

- Use Title Case for disease names: `Rheumatoid Arthritis.md`
- Use descriptive names: `Joint examination (GALS).md`
- No special characters except parentheses