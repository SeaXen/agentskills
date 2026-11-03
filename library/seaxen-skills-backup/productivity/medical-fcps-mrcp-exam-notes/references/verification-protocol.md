---
name: medical-fcps-mrcp-exam-notes
file_path: references/verification-protocol.md
---
# Content-Depth Verification Protocol (FCPS/MRCP Notes)

Session-captured lesson (2026-06-13): Trusting `status: scaffold` in frontmatter is dangerous. Files may have 290–560 lines of full content (MCQs, SBAs, Flashcards, Mind Maps) but frontmatter still says `scaffold`. A bulk `sed` to `status: full-fcps-mrcp-topic-note` is the correct remediation.

## When to Run Verification

- User says "is X complete? Check files 1 by 1"
- User says "make it 100% complete" / "fully complete"
- Before declaring a chapter finished
- After resuming a chapter from a previous session
- When the hierarchy file claims "100% complete" but you haven't checked actual content

## Verification Script (Run All Three)

```bash
CHAPTER=/mnt/tb/Medicine/Infectious\ Disease   # adjust path

# 1. Line count per file (catches under-fleshed scaffolds)
echo "=== LINE COUNTS ==="
for f in "$CHAPTER"/*.md; do
  size=$(wc -l < "$f")
  status=$(grep -m1 "^status:" "$f" | head -1)
  echo "$size lines | $status | $(basename "$f")"
done | sort -rn

# 2. Section presence check (catches scaffolds with one section but not others)
echo ""
echo "=== SECTION AUDIT ==="
for f in "$CHAPTER"/*.md; do
  if grep -q "status: full-fcps-mrcp" "$f" 2>/dev/null; then
    missing=""
    for section in "Learning Objectives" "Mind Map" "Spaced Repetition" "Self-Test" "MCQ" "SBA" "Viva"; do
      if ! grep -qE "$section" "$f" 2>/dev/null; then
        missing="$missing [$section]"
      fi
    done
    if [ -n "$missing" ]; then
      echo "MISSING SECTIONS in $(basename "$f"):$missing"
    fi
  fi
done

# 3. Quick promote-scaffold-but-actually-full audit
echo ""
echo "=== CANDIDATES FOR PROMOTION (scaffold status, >200 lines) ==="
for f in "$CHAPTER"/*.md; do
  if grep -q "^status: scaffold$" "$f" 2>/dev/null; then
    lines=$(wc -l < "$f")
    if [ "$lines" -gt 200 ]; then
      echo "$lines lines | $(basename "$f")"
    fi
  fi
done
```

## Bulk Promotion Command

When step 3 finds files:

```bash
cd "$CHAPTER" && for f in *.md; do
  if grep -q "^status: scaffold$" "$f" 2>/dev/null; then
    sed -i 's/^status: scaffold$/status: full-fcps-mrcp-topic-note/' "$f"
  fi
done
# Exclude hierarchy/MOC/template files explicitly:
# For example, only promote if it's NOT named "Davidson Chapter X - Hierarchy.md" or "*MOC.md"
```

**Always report before/after counts to the user** — they want the audit numbers, not just a "done" claim.

## Duplicate Detection (Pre-Batch)

```bash
# Find near-duplicate filenames in the same folder (handles "&" vs "and" differences)
ls "$CHAPTER"/*.md | sed 's|.*/||' | sed 's/\.md$//' | sort -f | \
  awk '{
    norm = tolower($0)
    gsub(/&/, "and", norm)
    gsub(/[^a-z0-9]/, "", norm)
    print norm "\t" $0
  }' | sort | awk -F'\t' '
    { if ($1 == prev) print prev_orig " <-- DUPLICATE WITH --> " $2; prev=$1; prev_orig=$2 }
  '
```

## Cross-Chapter / Cross-Folder Topic Tracking

Some Davidson topics appear in multiple folders. Common cross-folder patterns:

| Topic | Dedicated Chapter | Syndromic Folder |
|-------|-------------------|------------------|
| HIV/AIDS | Ch 12 (HIV Infection and AIDS) | Ch 11 (Infectious Disease) |
| TB / TB Meningitis | Ch 11 | Ch 17 (Respiratory), Ch 28 (Neurology) |
| STIs (Syphilis, Gonorrhoea, HSV) | Ch 15 (STI) | Ch 11 (Infectious Disease) |
| Septic Arthritis, Osteomyelitis | Ch 13 (Rheumatology) | Ch 11 (Infectious Disease) |
| Endocarditis | Ch 13 (Infectious Disease) | Ch 16 (Cardiology) |
| Cryptococcal Meningitis, PCP, Toxo, CMV | Ch 11 (Infectious Disease) | Ch 14 (HIV OIs) |

When completing a chapter:
1. Check if a dedicated folder already exists: `ls /mnt/tb/Medicine/ | grep -iE "hiv|ch12"`
2. If the topic exists in BOTH places, keep both as cross-references (different angles)
3. For true duplicates (same folder, same topic, different filename style), pick the more complete and `rm` the other

## What to Report to the User

After verification, give a structured summary like:

```
✅ VERIFIED: [Chapter] — N files
- 14 disease-level notes promoted scaffold → full-fcps-mrcp-topic-note (had 290-560 lines but wrong frontmatter)
- 2 duplicate files removed (Amoebiasis & Giardiasis.md + HAI duplicate)
- 1 missing topic created (Pneumocystis Pneumonia)
- Total: N/M disease-level topics at full-fcps-mrcp standard with Learning Objectives, MCQs, SBAs, Flashcards, Mind Maps
```
