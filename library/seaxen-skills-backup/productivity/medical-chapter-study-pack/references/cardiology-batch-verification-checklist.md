# Cardiology Batch Completion Verification Checklist

## Use After Every Cardiology Batch

**CRITICAL RULE**: Never claim "batch complete" until ALL items below are verified.

---

### 1. File Writes Verified
- [ ] All new `.md` files created with `write_file` (not just described)
- [ ] Each file verified on disk with `read_file` or `ls`
- [ ] Status frontmatter updated: `status: full-fcps-mrcp-note`
- [ ] Updated timestamp: `updated: {{Date}}`
- [ ] Tags include `fcps, mrcp` and relevant topic tags

### 2. MOC Updated
- [ ] `Cardiology MOC.md` updated with ✅ for each completed topic
- [ ] Completed count incremented in header
- [ ] Links use correct Obsidian wiki-link format: `[[Path/Topic|Display Name]]`
- [ ] Format consistent: `- ✅ [[Link|Name]] — full FCPS/MRCP note completed`

### 3. Hierarchy Updated
- [ ] `Davidson Chapter 16 - Cardiology Hierarchy.md` updated
- [ ] ✅ markers added at correct indentation level
- [ ] No duplicate entries introduced
- [ ] Topic-group hubs correctly reflect completions

### 4. Session Resume Updated
- [ ] `Cardiology Channel Session Resume 2026-05-06.md` updated
- [ ] Completed items marked with `— ✅ COMPLETED`
- [ ] Queue reordered with next targets at top
- [ ] Compact prompt and recommended command refreshed

### 5. Git Workflow
- [ ] `git add` with explicit file paths (Cardiology/ + 00_Index/)
- [ ] `git commit` with descriptive message: `feat(cardiology): add N full FCPS/MRCP notes (Topic1, Topic2, ...)`
- [ ] `git push` successful
- [ ] `git status --short -- Cardiology/ '00_Index/...'` shows clean

### 6. Final Verification
- [ ] `grep -r "status: scaffold$" /mnt/tb/Medicine/Cardiology/ --include="*.md"` returns expected count (should decrease)
- [ ] `grep -r "status: full-fcps-mrcp-note" /mnt/tb/Medicine/Cardiology/ --include="*.md" | wc -l` returns expected count (should increase)

---

## Common Pitfalls to Avoid

1. **Claiming completion without file writes** — User explicitly corrected this: "you just messed up every thing"
2. **Missing MOC/hierarchy updates** — ✅ markers must be added, not just described
3. **Forgetting git push** — Batch not complete until pushed
4. **Not verifying git status clean** — Must run scoped status check
5. **Batch size mismatch** — If user says "next N", complete exactly N

---

## Quick Verification Commands

```bash
# Check remaining scaffolds
grep -r "status: scaffold$" /mnt/tb/Medicine/Cardiology/ --include="*.md" | wc -l

# Check completed count
grep -r "status: full-fcps-mrcp-note" /mnt/tb/Medicine/Cardiology/ --include="*.md" | wc -l

# Check git status (Cardiology scoped)
git status --short -- Cardiology/ '00_Index/Cardiology Channel Session Resume 2026-05-06.md'
```

---

## Template Notes

Each full FCPS/MRCP note must include all sections:
- Learning Objectives
- Definition
- Pathophysiology (table)
- Clinical Features (table)
- Diagnostic Algorithm (mermaid flowchart)
- Diagnostic Criteria/Thresholds (table)
- Management (tables by category)
- Drug Interactions/Contraindications (table)
- Procedures (with indications/contraindications)
- Complications of Mismanagement
- Red Flags
- Prognosis (table)
- Topic Correlation (wiki-links)
- Special Situations
- FCPS/MRCP High-Yield Points
- Common Viva Questions
- Common Confusions/Exam Traps
- Mnemonics
- Mind Map
- Suggested Visuals/Video References
- One-Page Revision Summary
- 24-Hour Recall Prompts
- 7/15/30-Day Revision Tracker
- Must/Should/Nice-to-Know
- My Weak Points (checkboxes)
- Self-Test Scorecard
- Exam Answer Modes