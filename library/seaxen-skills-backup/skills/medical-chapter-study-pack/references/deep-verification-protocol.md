# Deep Verification Protocol for Medical Chapter Notes

## Mandatory Before Claiming Chapter Complete

### 1. Template Compliance Check (automated)

Run on chapter directory:

```bash
for f in *.md; do
  if [[ "$f" != *"MOC"* && "$f" != *"Hierarchy"* && "$f" != *"Template"* ]]; then
    checks=( "## MCQs" "## SBA Questions" "## Flashcards" "## Answer Key" "## Must Know" )
    for c in "${checks[@]}"; do
      grep -q "$c" "$f" || echo "$f MISSING: $c"
    done
  fi
done
```

**Required sections per topic file:**
- `## Must Know / Should Know / Nice to Know`
- `## MCQs (10)`
- `## SBA Questions (10)`
- `## Flashcards`
- `## Answer Key with Explanations`

### 2. WikiLink Consistency Check

- All hierarchy/wiki links MUST match exact .md filenames (case, spaces, special chars: `/`, `()`, ` `)
- Common mismatches observed:
  - `[[Septic Shock]]` → file is `Sepsis and Septic Shock.md`
  - `[[Malignant Hyperthermia / Neuroleptic Malignant Syndrome]]` → file is `Malignant Hyperthermia Neuroleptic Malignant Syndrome.md`
  - `[[Early Warning Scores (NEWS2 / MEWS)]]` → file is `Early Warning Scores (NEWS2 MEWS).md`
- Fix hierarchy AND MOC when filename changes

### 3. Batch Quality Degradation Prevention

**Pattern observed:** First batches (1-6 files) get full template; subsequent batches truncate (missing Must Know, MCQs, SBAs, Flashcards, Answer Keys).

**Enforce:** Every batch must pass deep verification before next batch starts. Do not accumulate incomplete notes.

### 4. Verification Checklist Additions

Add to skill's Verification Checklist:
- [ ] Deep verification passed: all files checked for required template sections
- [ ] WikiLink consistency verified: all hierarchy/wiki links match exact .md filenames
- [ ] Batch quality gate: each batch verified for full template compliance before next batch starts

### 5. File Count Reconciliation

- Count unique .md topic files (exclude MOC, Hierarchy, Template)
- Match against hierarchy wiki-link count (deduplicate cross-domain entries like Septic Shock appearing in Shock + Sepsis domains)
- Report: "X unique topics, Y hierarchy entries (Z duplicates)"

---

## Acute Medicine Chapter 9 — Session Evidence

**Files created:** 25 topic files + MOC + Hierarchy
**Initial incomplete:** 13/25 files missing Must Know/MCQ/SBA/Flash/Answer Key
**Fixed:** All 13 upgraded via patch
**WikiLink mismatches fixed:** 3
**Final verification:** All 25 files pass automated check

**Lesson:** First pass created hierarchy + 6 full notes. Second batch (5 notes) truncated. Third batch (10 notes) created 4 new + upgraded 10 but missed deep verification. Fourth batch (remediation) completed all.