# Deep Verification Checklist for Chapter Completeness

## Purpose
Prevent "claiming complete" when files are actually incomplete. Learned from session where 10/21 Acute Medicine notes were missing full template sections despite frontmatter claiming `status: full-fcps-mrcp-topic-note`.

## When to Run
- Before declaring a chapter "complete"
- After any batch update claiming multiple topics finished
- Before git commit/push for chapter folders

## Verification Steps

### 1. Template Completeness Check (per file)
**Required sections in every `status: full-fcps-mrcp-topic-note` file:**
```bash
grep -E "## MCQs|## SBA Questions|## Flashcards|## Answer Key|## Must Know" <file>
```
All 5 must return true. Missing any = not complete.

### 2. WikiLink Consistency (Hierarchy ↔ Files)
**Extract all wiki-links from hierarchy:**
```bash
grep -o '\[\[.*\]\]' hierarchy.md | sort -u
```
**Extract all actual .md filenames (topic files only):**
```bash
ls *.md | grep -vE "(MOC|Hierarchy|Template)" | sed 's/\.md$//' | sed 's/^/[[/; s/$/]]/'
```
**Compare sets** — every hierarchy link must match an actual file. Report mismatches.

### 3. MOC ✅ Marker Accuracy
Count ✅ in MOC starter queue vs actual files with full template.
```bash
grep -c "✅" MOC.md
```
Must equal count of verified complete topic files.

### 4. Hierarchy Domain Coverage
Count wiki-links in hierarchy per domain vs actual files.
Domains missing files = incomplete chapter coverage.

### 4. File Count Sanity
```bash
ls *.md | wc -l
```
Should equal: topic files + MOC + Hierarchy + (Template if present)

## Automated Verification Script Pattern
```bash
# Quick template check across chapter folder
for f in *.md; do
  if [[ "$f" != *"MOC"* && "$f" != *"Hierarchy"* ]]; then
    missing=()
    grep -q "## MCQs" "$f" || missing+=("MCQs")
    grep -q "## SBA Questions" "$f" || missing+=("SBA")
    grep -q "## Flashcards" "$f" || missing+=("Flashcards")
    grep -q "## Answer Key" "$f" || missing+=("AnswerKey")
    grep -q "## Must Know" "$f" || missing+=("MustKnow")
    if [ ${#missing[@]} -gt 0 ]; then
      echo "$f MISSING: ${missing[*]}"
    fi
  fi
done
```

## Red Flags (Never Trust Without Verification)
- Frontmatter `status: full-fcps-mrcp-topic-note` without section check
- MOC claiming "21/20 complete" without file-by-file audit
- Hierarchy with 26 links but 25 files (duplicate entry = dual-domain topic)
- User says "do next 10" and all 10 created but not verified

## Lesson from Acute Medicine Session
- 10 notes created in batch had only 1/3 template sections (Must Know, MCQs, SBAs, Flashcards, Answer Key missing)
- 3 WikiLink mismatches: Septic Shock (dual-domain), MH/NMS (slash), NEWS2 (slash)
- MOC claimed 21/20 complete; actual verified = 25/25 after remediation
- **Root cause**: No verification step between writing and claiming complete

## Required Before "Chapter Complete" Declaration
1. ✅ All hierarchy links have matching .md files
2. ✅ All .md topic files pass 5-section template check
3. ✅ MOC ✅ count matches verified file count
4. ✅ Hierarchy status line updated with accurate count
5. ✅ Git status clean for chapter folder only