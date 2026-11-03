# Chapter Audit-by-TOC & Backfill Pattern

## Pattern: When User Asks "Is Chapter X 100% Complete?"

When the user asks "is [chapter] fully complete?" or "is it 100% with all information + questions for exam?", the verification has THREE layers — and Layer 3 (web-TOC backfill) is the one that catches the largest gaps.

## Layer 1: File Inventory (What's Present)

```bash
# Count all markdown files
find "/mnt/tb/Medicine/[Chapter Name]" -name "*.md" -type f | wc -l

# List them
find "/mnt/tb/Medicine/[Chapter Name]" -name "*.md" -type f | sort

# Identify stubs (file exists but <200 lines or <10KB)
find "/mnt/tb/Medicine/[Chapter Name]" -name "*.md" -type f -size -10k
find "/mnt/tb/Medicine/[Chapter Name]" -name "*.md" | xargs -I{} sh -c 'lines=$(wc -l < "{}"); if [ "$lines" -lt 200 ]; then echo "{}: $lines lines"; fi'
```

This catches "files exist but are scaffold-stubs" — the easy case.

## Layer 2: Exam-Component Audit (Is Each File Complete?)

For each file, verify the 8/8 exam components are present (see `chapter-completion-verification-workflow.md`):

```python
import os
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.md') and 'Hierarchy' not in f and 'MOC' not in f:
            with open(os.path.join(root, f)) as fp:
                content = fp.read()
            has_viva = "Viva" in content
            has_mcq = "MCQ" in content
            has_sba = "SBA" in content
            has_mindmap = "Mind Map" in content
            has_summary = "Summary Box" in content
            # etc
```

This catches "file is full-text but missing the 14-section template" — the medium case.

## Layer 3: Official-TOC Backfill (THE CRITICAL ONE — Often Skipped)

**This is the layer most likely to surface major gaps.** The previous chapters' Hierarchy + MOC were built from memory of Davidson, not from the official 24e chapter TOC. Some major sections can be completely absent from the planned structure.

### How to Run Layer 3

```bash
# Step 1: Web search for official chapter TOC
web_search(query="Davidson 24th edition Chapter [N] [Chapter Name] contents")
web_search(query='"Davidson" "[Chapter Name]" Maxwell 2023 OR 2024 "section" headings')

# Step 2: Extract from authoritative sources (Elsevier inspection copy, 
# basicmedicalkey.com, archive.org textbook excerpts)
web_extract(urls=["https://basicmedicalkey.com/[chapter-slug]",
                  "https://inspectioncopy.elsevier.com/book/details/[isbn]"])

# Step 3: Build "expected sections" list from the official TOC
expected_sections = [
    "Section 1: [Title from official TOC]",
    "Section 2: [Title]",
    ...
]

# Step 4: Compare to what's in the Hierarchy file
# Read the hierarchy
# Cross-reference each official section
# Flag missing major sections
```

### Real Example: Davidson Ch2 Clinical Therapeutics (2026-06-15)

**Pre-audit assumption:** Ch2 had 97 topic files covering all of "Prescribing" + "ADRs" + "Interactions" + "TDM" + "Special Populations" + "Drug Development" + "Clinical Context" + "Polypharmacy" + "Medication Safety". Marked 100% complete in commit cd525e9.

**Layer 3 finding:** Web search of Davidson 24e Ch2 official TOC (BasicMedicalKey + Elsevier) revealed a **MAJOR missing section**: **"Principles of Clinical Pharmacology"** — the foundational PD + PK + Factors Influencing Drug Response content (~30% of chapter). This was completely absent from the original structure.

**Result:** 15 new full exam-suite files created (4 PD, 7 PK, 4 Factors), plus 1 master hub. Chapter 2 went from 97 → 114 topic content files. Committed b281cde.

### When to Run Layer 3

**Always run when the user asks "100% complete" or "all topic fully completed" or "all info not scaffold" — the user's intent is comprehensive coverage, and Layer 3 is the only way to confirm that against the actual textbook.**

Specifically trigger Layer 3 when:
- The chapter has been "complete" for >1 session (i.e., user is asking for a re-verification)
- The chapter is foundational (e.g., Therapeutics, Clinical Decision-Making) where missing content is high-impact
- The user phrases the question with "all", "every", "everything", "fully", "100%"

### How to Backfill Efficiently

Once gaps are identified:
1. Create a single **master hub** file at the new section level
2. Build out sub-hub files for each sub-heading (PD, PK, etc.)
3. Build out leaf disease-level notes (one file per topic)
4. Update the chapter Hierarchy to insert the new section
5. Update the chapter MOC with the new files
6. Commit in one batch with a clear commit message

**Real pattern from Ch2 session:** 16 files (1 master + 15 leaf) all in one commit. Each leaf file 17-23 KB. Took ~7 sequential write_file calls (some timed out, retried with smaller scope).

## Output to User

When reporting back, be specific about:
- How many files existed before
- What was missing per Layer 3 (web-TOC backfill)
- How many new files were created
- New total file count + line count + size
- Git commit hash
- Push confirmation

Don't claim "100% complete" without Layer 3 having been run.

## Anti-Patterns to Avoid

❌ **Claiming completion based on file count alone** — files can exist but be stubs, or the structure can miss major sections entirely.

❌ **Trusting the existing Hierarchy as the source of truth** — it was built from memory; the official textbook is the only authoritative source.

❌ **Skipping the "official TOC web search"** — it's tempting to trust your internal knowledge of Davidson, but section naming and structure shift between editions.

❌ **One-file-per-session updates** — when a major section is missing, build it all in one batch and commit. Don't dribble it across multiple sessions.

❌ **Burying the gap in jargon** — when you find a major missing section, say clearly "the original structure was missing X" and explain what you added.
