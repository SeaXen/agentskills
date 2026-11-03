# Medical Chapter Production Workflow (v2.0)

## Two-Phase Scaffold → Full Note Production

This document captures the battle-tested workflow for producing FCPS/MRCP medical chapter notes, refined through Cardiology Chapter 16 and Rheumatology Chapter 26 production.

---

## Phase 1: Scaffold Build (One-Time Per Chapter)

### 1.1 Extract Davidson TOC Structure
- Use Davidson 24th Edition chapter TOC as authoritative source
- Map to 3-tier hierarchy:
  - **10 Heading Hubs** (top-level sections)
  - **20 Topic-Group Hubs** (mid-level categories)
  - **78-103 Disease-Level Topics** (leaf nodes)
  - **8-12 Preserved Root-Level Core Notes** (pre-existing broad topics)

### 1.2 Create Scaffold Files
**Hub files** (`status: scaffold-hub`):
- 10 Heading Hub files (e.g., `Cardiology.md`, `Inflammatory Arthritis.md`)
- 20 Topic-Group Hub files (e.g., `Seronegative spondyloarthritis overview.md`)
- **Do NOT upgrade to full notes** — serve as navigation hubs

**Disease-level scaffolds** (`status: scaffold`):
- One .md file per leaf topic in hierarchy
- Minimal YAML frontmatter with `status: scaffold`
- Template sections as placeholders
- **Do NOT write full content** — just scaffold structure

**Meta files**:
- `Chapter XX <Subject> Roadmap.md` — study sequence, exam weights
- `<Subject> MOC.md` — master index with completion tracking
- `<Subject> Hierarchy.md` — full hierarchy with ✅ tracking
- `<Subject> Channel Session Resume.md` — continuation prompt
- `Templates/<Subject> Topic Template.md` — standardized scaffold template

### 1.3 Initial Git Commit
```bash
git add <SubjectDir>/ .md files
git commit -m "feat(<subject>): scaffold build — N heading hubs, M topic groups, K disease scaffolds"
git push
```

---

## Phase 2: Batch Upgrade (Iterative)

### 2.1 Batch Selection
- Read Session Resume → pick next 5-10 topics from prioritized queue
- Prioritize by FCPS/MRCP exam yield (see Roadmap Must/Should/Nice tiers)
- Always read Resume first to get exact next targets

### 2.2 Full Note Production (Per Topic)
**Replace scaffold with full note**:
1. Read scaffold file
2. Replace `status: scaffold` → `status: full-fcps-mrcp-note`
3. Write complete note following template (templates/fcps-mrcp-note-template.md)
4. **All 6 mandatory sections must have real content** (no placeholders)

### 2.3 Mandatory Sections (6 Required)
| Section | Minimum Content |
|---------|-----------------|
| `## Learning Objectives` | 5+ bulleted objectives |
| `## Management` | Tables + mermaid flowchart |
| `## MCQs` | 10 questions with explanations |
| `## SBA Questions` | 10 questions with explanations |
| `## Common Viva Questions` | 8+ numbered questions |
| `## One-Page Revision Summary` | Concise bullet summary |

**Optional but Recommended Sections**:
- Definition, Pathophysiology, Clinical Features, Differential Diagnosis
- Drug Interactions / Contraindications / Comorbidity Cautions
- Procedures / Indications / Contraindications
- Complications / Red Flags / Prognosis
- FCPS/MRCP High-Yield Points, Common Viva Questions, Confusions/Traps
- Mnemonics, Mind Map, Suggested Visuals/Video References
- 24-Hour Recall, 7/15/30-Day Tracker, Must/Should/Nice to Know
- Self-Test Scorecard, My Weak Points, Exam Answer Modes

### 2.4 Update Tracking Files (Per Batch)
**MOC** (`<Subject> MOC.md`):
- Add `  - ✅ [[Path|Topic]] — full FCPS/MRCP note completed` under correct heading
- Update "verified full FCPS/MRCP notes: XX" count in header

**Hierarchy** (`<Subject> Hierarchy.md`):
- Add `✅` prefix to disease-level items (indent=4)
- Update topic-group hubs with `✅` when ALL children complete
- Remove duplicate entries (some topics appear in multiple parents)

**Resume** (`<Subject> Channel Session Resume.md`):
- Mark completed with `— ✅ COMPLETED`
- Update suggested next queue
- Refresh "Recommended safe next command"

### 2.4 Git Workflow (Per Batch)
```bash
# Path-scoped to ChapterDir + Resume only
git add <SubjectDir>/<new_full_notes> <Subject>/MOC.md <Subject>/Hierarchy.md 00_Index/Resume.md
git commit -m "feat(<subject>): add N full FCPS/MRCP notes (topic1, topic2, ...)"
git push
```

**Rules**:
- **Scope commits** to chapter directory + Resume file only
- **Commit message format**: `feat(<subject>): add N full FCPS/MRCP notes (topic1, topic2, ...)`
- **Never** commit unrelated files in chapter batch
- **Push immediately** after commit
- **Verify clean**: `git status --short -- <SubjectDir>/ 00_Index/Resume.md` → clean

---

## Quality Gates (Non-Negotiable)

| Gate | Check |
|------|-------|
| **Placeholder text** | Zero tolerance: "would be added later", "placeholder", "TBD" = INCOMPLETE |
| **6 mandatory sections** | All must have real content |
| **MOC/Hierarchy sync** | Counts match `grep "status: full-fcps-mrcp-note" <SubjectDir> --include="*.md" -r | wc -l` |
| **Resume accuracy** | Queue matches actual remaining scaffolds |
| **Git clean** | `git status --short -- <SubjectDir>/ 00_Index/Resume.md` = clean |

---

## Pitfalls & Hard Lessons Learned

### 1. Stream Timeout on Large Writes
**Problem**: Single `write_file` >8K tokens times out.
**Solution**: Write files individually or in small batches (3-5 files per turn).

### 2. False Completion Claims
**Problem**: Agent claimed "batch complete" without actual file writes.
**Solution**: Only mark ✅ after `write_file` succeeds AND file verified on disk.

### 3. Missing Hub Files
**Problem**: Agent tried to upgrade topic-group hubs (`scaffold-hub`) to full notes.
**Rule**: 20 topic-group hubs + 10 heading hubs = `scaffold-hub` = NEVER upgrade.

### 4. Root-Level Core Notes
**Problem**: Agent tried to upgrade 12 preserved root notes.
**Rule**: 8-12 root core notes are legacy — keep as-is, don't upgrade unless explicitly asked.

### 5. Duplicate Hierarchy Entries
**Problem**: Same topic (e.g., "Cardiogenic shock") appears in multiple parent groups.
**Fix**: Clean up duplicates before adding ✅ markers; keep one definitive entry.

### 6. MOC/Hierarchy Drift
**Problem**: Counts in MOC/Hierarchy don't match actual full notes on disk.
**Fix**: After each batch, run verification:
```bash
grep -r "status: full-fcps-mrcp-note" <SubjectDir>/ --include="*.md" -l | wc -l
```

### 7. Resume Drift
**Problem**: Queue in Resume doesn't match actual remaining scaffolds.
**Fix**: After each batch, regenerate queue from actual remaining `status: scaffold` files.

---

## Template Reference
See `templates/fcps-mrcp-note-template.md` for standardized note structure with all required sections and mermaid diagram patterns.

---

## Verification Commands Cheat Sheet

```bash
# Count full notes
grep -r "status: full-fcps-mrcp-note" <SubjectDir>/ --include="*.md" -l | wc -l

# Count remaining scaffolds
grep -r "status: scaffold$" <SubjectDir>/ --include="*.md" -l | wc -l

# List incomplete topics
grep -r "status: scaffold$" <SubjectDir>/ --include="*.md" -l | sort

# Verify git clean
git status --short -- <SubjectDir>/ <Subject>Resumefile.md

# Check MOC count vs disk count
grep -c "✅" <Subject>/MOC.md  # should match grep count above
```