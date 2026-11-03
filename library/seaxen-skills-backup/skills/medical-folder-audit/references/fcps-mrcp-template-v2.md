# FCPS/MRCP Template v2 — 14-Section Structure (Current)

This is the canonical template used for all Davidson chapter topic notes in `/mnt/tb/Medicine/`.

## Full Template Structure

Every complete topic file MUST contain these 14 sections with real content:

### 1. Frontmatter
```yaml
---
# Topic title
**Parent Topic:** [Link to MOC] → [Link to Hierarchy]
**Status:** `full-fcps-mrcp-note`
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — specific exam focus)
**Source:** Davidson 24th Ed Ch X; additional sources
---
```

### 2. `## 🎯 Learning Objectives`
- Checkbox-driven learning objectives
- Each objective starts with action verb

### 3. `## 🧠 Core Concept`
- High-level summary with **Mermaid flowchart/diagram**
- Single key principle boxed

### 4. Numbered Content Sections (`## 1️⃣`, `## 2️⃣`, etc.)
- 2-7 sections covering the topic in depth
- Tables, mermaid diagrams, worked examples
- Mechanism, diagnosis, management details

### 5. `## Practical Algorithm`
- **Mermaid flowchart** for clinical decision-making
- Step-by-step approach (History → Exam → Test → Thresholds)

### 6. `## ⚡ FCPS/MRCP High-Yield Summary`
- Condensed table: Concept → Key Points
- 6-8 rows covering exam-critical facts

### 7. `## 🎤 Viva Questions (Expected Answers)`
- Table: # | Question | Expected Answer
- **10+ questions** with detailed expected answers
- Covers definitions, calculations, clinical scenarios

### 8. `## 🧩 Confusions & Mnemonics`
- Table: Confusion → Clarification
- **Mnemonic** for the topic (e.g., DIAGNOSTIC REASONING)

### 9. `## 🗺️ Mind Map`
- **Mermaid mindmap** of the topic structure
- Visual hierarchy from core concept to details

### 10. `## 📅 Spaced Repetition Tracker`
- Review schedule table: Day 1, 3, 7, 14, 30, 90
- Score column (0-5) + Notes column

### 11. `## 📝 Self-Test Scorecard`
- Section-wise scoring table
- Max score per section + Total

### 12. `## 💬 Exam Answer Modes`
- Table: Format | Prompt | Key Points
- **5 modes**: Long Essay, Short Note, Viva, Ward Round, Last-Night

### 13. `## ❓ MCQs` + `## 🔑 Answer Keys`
- **10 MCQs** with explanations in options
- **Answer Key table** mapping Q# → Answer

### 14. `## 📋 SBAs` (shared Answer Keys)
- **5 SBAs** with clinical scenarios + explanations
- Uses same Answer Keys section

### 15. `## 🔗 Cross-Links`
- Wiki-links to related topics in other files/chapters

---

## Detection Heuristics (for audit script)

| Anchor | Purpose |
|--------|---------|
| `status: full-fcps-mrcp-note` | Frontmatter — authoritative |
| `## 🎯 Learning Objectives` | Section 2 |
| `## 🧠 Core Concept` | Section 3 |
| `## ❓ MCQs` | Section 13 |
| `## 📋 SBAs` | Section 14 |
| `## 🎤 Viva Questions` | Section 7 |
| `## 🗺️ Mind Map` | Section 9 |

**Rule**: File is complete iff `status == full-fcps-mrcp-note` AND ≥5 of 6 content anchors present AND no placeholder patterns.

---

## Placeholder Patterns (Incomplete Markers)

These patterns indicate a scaffold/incomplete file:
- `would be added in complete version`
- `would be included in the complete version`
- `Full <n> MCQs + <n> SBAs would be`
- `status: scaffold-hub`
- `status: scaffold-topic`
- `status: scaffold-disease`

---

## Example Complete File
`/mnt/tb/Medicine/Clinical Decision-Making/1.1 Clinical Reasoning & Diagnostic Process.md` — 497 lines, 27KB, all 14 sections present, `status: full-fcps-mrcp-note`