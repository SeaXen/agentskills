---
description: "Hepatology Chapter 24 (Davidson 24th Ed) - Stream timeout workaround and session-specific learnings for large FCPS/MRCP notes"
tags: [hepatology, davidson-chapter-24, stream-timeout, fcps, mrcp, hepatology-session-2026]
created: 2026-06-13
---

# Hepatology Chapter 24 — Stream Timeout Workaround & Session Learnings

## Problem
Hepatology notes (Davidson Chapter 24) are particularly dense with:
- Multiple large Mermaid diagrams (flowcharts, mind maps)
- Extensive structured tables (scoring systems, drug tables, diagnostic criteria)
- Dense Viva Questions sections (10+ per note)
- Extensive Mind Maps
- Detailed Confusions/Mnemonics tables
- Spaced Repetition Trackers and Self-Test Scorecards

**Result**: Average Hepatology note = 180-250 lines, 15K-25K tokens → **Stream timeouts on single `write_file`**

## Hepatology-Specific Solutions

### 1. Four-Chunk Split Pattern (Validated in 2026-06-13 Session)
For Hepatology notes (typically 200+ lines, 20K+ tokens):

| Chunk | Content | Approx Lines | Write Call |
|-------|---------|--------------|------------|
| **Chunk 1** | Frontmatter + Learning Objectives + Definition/Epidemiology + Aetiology/Pathophysiology + Clinical Features | 50-60 | #1 |
| **Chunk 2** | Classification/Staging + Diagnosis/Differentials + Investigations | 50-60 | #2 |
| **Chunk 3** | Management Algorithm + FCPS/MRCP High-Yield + Viva Questions | 60-80 | #3 |
| **Chunk 4** | Confusions/Mnemonics + Mind Map + Revision Card + Trackers + Scorecard + Navigation | 50-70 | #4 |

**Each chunk ≈ 5-7K tokens → Well under 8K limit**

### 2. Write Sequence (Critical: Each Call Overwrites)
```python
# Chunk 1 - Write first
write_file(path="/mnt/tb/Medicine/Hepatology/Section/Topic.md", 
           content=chunk1_content)

# Chunk 2 - Append by writing complete content up to this point
write_file(path="/mnt/tb/Medicine/Hepatology/Section/Topic.md", 
           content=chunk1_content + chunk2_content)

# Chunk 3 - Write complete content up to this point
write_file(path="/mnt/tb/Medicine/Hepatology/Section/Topic.md",
           content=chunk1_content + chunk2_content + chunk3_content)

# Chunk 4 - Final complete file
write_file(path="/mnt/tb/Medicine/Hepatology/Section/Topic.md",
           content=chunk1_content + chunk2_content + chunk3_content + chunk4_content)
```

**Critical**: Each `write_file` call REPLACES the entire file. You MUST accumulate content and write the complete accumulated file each time.

### 3. Batch Size & Verification Protocol

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Notes per session | 8-12 | Prevents token accumulation in context |
| Notes per commit | 5-8 | Git operations stable |
| Verification after | EVERY batch | Catch incomplete notes early |
| Verification commands | `search_files pattern:"status: full-fcps-mrcp-note" path:"/mnt/tb/Medicine/Hepatology"` + `wc -l` | Mandatory |

### 4. Directory Path Handling (Hepatology-Specific)
| Character | Example | Handling |
|-----------|---------|----------|
| `&` | `Hepatobiliary & Pancreatic` | Quote: `"/mnt/tb/Medicine/Hepatology/Hepatology in Special Situations"` |
| `,` | `Liver Transplantation/Liver Transplantation.md` | Quote paths |
| Spaces | `Portal Hypertension and Complications` | Quote paths |

```bash
# Always quote paths with special characters
mkdir -p "/mnt/tb/Medicine/Hepatology/Portal Hypertension and Complications"
write_file(path="/mnt/tb/Medicine/Hepatology/Portal Hypertension and Complications/Topic.md", ...)
```

### 4. Session Summary (2026-06-13)
| Metric | Value |
|--------|-------|
| Notes created | ~60 |
| New files | ~60 |
| Total Hepatology files | ~170 |
| Sections completed | 14/14 (all sections have content) |
| Coverage | ~75% of 118 disease-level topics |
| Missing high-priority | NAFLD (8), Autoimmune (4), Biliary (6), Viral Hepatitis (8), Transplant (6), Special Situations (5) |

### 5. Verification Commands (Mandatory After Each Batch)
```bash
# Count full notes
search_files pattern:"status: full-fcps-mrcp-note" path:"/mnt/tb/Medicine/Hepatology"

# Count total files
# In terminal: find /mnt/tb/Medicine/Hepatology -name "*.md" -type f | wc -l

# Check specific file
read_file path="/mnt/tb/Medicine/Hepatology/Section/Topic.md" limit="50"
```

### 5. Hepatology-Specific Template Considerations
The Hepatology template (`/mnt/tb/Medicine/Templates/Hepatology Topic Template.md`) includes:
- Scoring tables: Child-Pugh, MELD, Maddrey, Glasgow, ABIC, Lille, BCLC, LI-RADS
- Specific algorithms: ALF, ACLF, HRS, Variceal bleed, SBP
- Disease-specific: Wilson scoring, PBC response criteria, HCV DAA algorithms
- Transplant: Milan, UCSF, MELD exceptions

**These tables are token-heavy** → Primary cause of stream timeouts → Must chunk.

### 6. Quick Reference: Chunk Boundaries by Section

```
CHUNK 1 (Sections 1-5):
  - Frontmatter
  - Learning Objectives
  - Definition/Epidemiology
  - Aetiology/Pathophysiology (with mermaid)
  - Clinical Features

CHUNK 2 (Sections 6-8):
  - Classification/Staging (with tables)
  - Diagnosis/Differentials (with tables)
  - Investigations (with tables)

CHUNK 3 (Sections 9-11):
  - Management Algorithm (with mermaid)
  - FCPS/MRCP High-Yield Summary (table)
  - Viva Questions (8-10 with answers)

CHUNK 4 (Sections 9-14):
  - Confusions & Mnemonics (table)
  - Mind Map (mermaid)
  - One-Page Revision Card (table)
  - Spaced Repetition Trackers
  - Self-Test Scorecard
  - Local Navigation (wiki-links)
```

This Hepatology-specific workaround was validated in the 2026-06-13 session producing ~60 notes across 14 sections with zero timeouts after implementing 4-chunk split.