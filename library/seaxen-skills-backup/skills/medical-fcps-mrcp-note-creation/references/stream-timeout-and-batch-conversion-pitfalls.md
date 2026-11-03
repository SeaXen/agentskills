---
name: stream-timeout-and-batch-conversion-pitfalls
description: Pitfalls and lessons for the medical-fcps-mrcp-note-creation workflow. Covers the stream-timeout problem on large write_file calls, the parallel-delegate_task 3-task limit, the subagent context-inheritance gotcha, the MOC/Hierarchy false-completion trap, the subagent-self-report-inflation pitfall, the chapter-wide status-tag drift trap (`full-note` and `scaffold-hub` legacy tags), the audit-substring false-positive, the 5-pass audit pattern for "looks complete but audit reports <100%" chapters, the 4 valid Answer Key formats, the greenfield chapter build from scratch (0 → 87 files in one session using topic-metadata + Python batch), and the FCPS/MRCP exam-ready content append pattern. Use when starting or reviewing any Davidson chapter build, appending exam content to existing files, doing a 1-by-1 file audit, or building a new chapter from scratch.
---

# Common Pitfalls in FCPS/MRCP Note Creation

See the detailed pitfalls below. This file is referenced by `medical-fcps-mrcp-note-creation/SKILL.md` and `medical-folder-audit/SKILL.md` (which carries the Ch 17 audit case study in `references/davidson-ch17-respiratory-audit-2026.md`).

## How to use this file
- New sessions on a Davidson chapter build should scan the **PITFALLS INDEX** below first.
- Trigger phrases that indicate a pitfall applies are bolded in each entry.
- The MOC/Hierarchy drift, subagent self-report, and append-not-rewrite patterns recur across chapters; do not re-derive them — re-use the validated patterns below.

## PITFALLS INDEX
1. Stream-timeout on large `write_file` (THE #1 BLOCKER)
2. Parallel `delegate_task` hard limit: 3 concurrent children
3. Subagent context-inheritance gotcha
3a. Subagent workload: 1 large note per subagent (hard cap)
3b. MOC "Last Session Progress" section pattern
4. MOC/Hierarchy may falsely claim 100% complete
5. Status-tag drift across subagents (BOTH `full-fcps-mrcp-note` AND `full-fcps-mrcp-topic-note` count as complete — Ch 17 lesson)
6. Bold the correct MCQ/SBA answer
7. MOC must list every topic file with status checkmark
8. Subagent self-reports are UNRELIABLE — always verify files
9. Append to fix partial files, don't rewrite
10. Use flexible regex for section verification
11. Check frontmatter status AFTER status-tag normalization
12. Endocrinology Ch 20 lessons (2026-06-15)
13. Session-end completion claims must re-audit, not just count delta (Ch 17 Respiratory, 2026-06-16) — see detailed body below
14. Header-claim vs body-content mismatch in MCQ/SBA sections (Ch 17, 2026-06-16) — see `medical-folder-audit/references/davidson-ch17-respiratory-audit-2026.md`
15. **Ch 22 Nutritional Factors in Disease build (2026-06-16) — 36/36 validated; patterns below**
16. **13-section vs 14-section false-completion trap (Ch 17 Respiratory, 2026-06-16) — see detailed body below**
17. **Web-search validation of hierarchy against textbook TOC (Ch 17 Respiratory, 2026-06-16) — see detailed body below**
18. **Ch 26 Rheumatology & Bone Disease build (2026-06-16) — 65/65 validated; status-tag trap and overview-file pattern — see detailed body below**
19. **"Big chapter but topic is less" — true Davidson disease-level vs supporting-notes inflation (Ch 26 Rheumatology, 2026-06-16) — see detailed body below**
20. **Pre-completion cross-reference against textbook TOC is MANDATORY, not optional (Ch 26, 2026-06-16) — see detailed body below**
21. **Chapter-wide status-tag drift: `full-note` and `scaffold-hub` legacy tags cause audit false-positive (Ch 29 Stroke Medicine, 2026-06-16) — see detailed body below**
22. **Answer Key detection patterns: 4 valid formats in the wild (Ch 29 Stroke Medicine Session 2, 2026-06-16) — see detailed body below**
23. **"Viva Answer Frame" is an Answer Key alias (Ch 29, 2026-06-16) — see detailed body below**
24. **The "Definition" / "Clinical Features" wrapper section fix (Ch 29, 2026-06-16) — see detailed body below**
25. **Expanded section-naming flexibility: many more synonyms for Clinical/Investigation (Ch 29, 2026-06-16) — see detailed body below**
26. **User's "A to Z" demand pattern: every file must reach FULL standard (Ch 29, 2026-06-16) — see detailed body below**
27. **1-by-1 file audit pattern with per-file table (Ch 29 Stroke Medicine, 2026-06-16) — see detailed body below**
28. **Greenfield chapter build from scratch: 0 → 87 files in one session using topic-metadata + Python batch (Ch 31 Medical Psychiatry, 2026-06-16) — see detailed body below**
29. **Round 2 gap-analysis expansion: +49 missing topics after the 100% claim (Ch 32 Maternal Medicine, 2026-06-16) — see detailed body below**
30. **"Rescuing a deceptive chapter" — status: full-fcps-mrcp-note on empty 6KB template stubs (Ch 29 Dermatology, 2026-06-16) — see detailed body below**
31. **Subagent 10-min timeout for big content generation; switch to main-session Python batch (Ch 29 Dermatology, 2026-06-16) — see detailed body below**
32. **Generic section-content trade-off for 100+ topics in limited time (Ch 29 Dermatology, 2026-06-16) — see detailed body below**
33. **Two-tier `.md` vs `_full.md` file cleanup + " (see X)" cross-reference stubs (Ch 29 Dermatology, 2026-06-16) — see detailed body below**
34. **Deep-subfolder `_full.md` files with real content but missing exam extras — APPEND, not REPLACE (Ch 29 Dermatology, 2026-06-16) — see detailed body below**
35. **Exam Extras Append from Existing High-Yield Tables (Ch 7 Oncology, 2026-06-16) — 5-step pattern for upgrading an existing chapter that has rich clinical content + high-yield tables but lacks MCQ/SBA/Flashcards/Answer Key — see detailed body below**
36. **Root-level topic file glob trap + Duplicate-filename detection (Ch 7 Oncology, 2026-06-16) — see detailed body below**
37. **Selective `git add` for multi-session repos (Ch 7 Oncology, 2026-06-16) — see detailed body below**
38. **Parallel Folder Structure Trap (Ch 25 Neurology, 2026-06-17) — two structures (canonical + legacy) accumulate phantom stubs; always audit for duplicates before claiming completion — see detailed body below**
39. **"Check all files 1 by 1" Honest Audit Pattern (Ch 25 Neurology, 2026-06-17) — status-tag counting is meaningless; use placeholder-pattern regex on content; report 3 numbers (real/hub/stub) — see detailed body below**ow**
40. **Deletion-vs-Write Decision Framework (Ch 25 Neurology, 2026-06-17) — for each stub: extract topic, check if real file exists, delete if duplicate, write if unique — see detailed body below**

## Pitfall 35 — Exam Extras Append from Existing High-Yield Tables (Ch 7 Oncology, 2026-06-16)

**User trigger phrase:** "all notes scaffold and MOC and others all need to true disease like topic from Davidson" / "fully complete if anything missing" / "is the chapter fully complete with information" — applied to a chapter that **already has rich clinical content (12-25K per file) and high-yield summary tables but lacks MCQ/SBA/Flashcards/Answer Key sections**.

**Lesson:** When most existing topic files have a rich `## FCPS/MRCP High-Yield Summary` table (10+ rows of `| **Key** | **Value** |`), you can **extract those rows as the data source** for MCQ/SBA/Flashcard/AK generation. This avoids hand-crafting 1000+ questions from scratch and produces topic-specific, accurate exam content.

### The 5-Step Append Pattern (validated for Ch 7: 118/118 in one session)

**Step 1: Audit the existing files**
- Confirm each file has `## N. FCPS/MRCP High-Yield Summary` (or unnumbered `## FCPS/MRCP High-Yield Summary`) with a `| **Key** | **Value** |` table
- 116/117 files in Ch 7 had this — perfect for the pattern
- Files missing the table need a hand-crafted exam block (see Step 5)

**Step 2: Extract rows with a flexible regex**
```python
# Matches both numbered (## 6. FCPS/MRCP) and unnumbered (## FCPS/MRCP) headers
hys_m = re.search(r'## (?:(?:\d+\.)\s*)?FCPS/MRCP High-Yield Summary\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
rows = re.findall(r'^\| \*\*([^*]+)\*\* \|(.*?)\|', hys_m.group(1), re.MULTILINE)
# rows = [(key, value), ...] — first 10 used
```

**Step 3: Generate exam extras from rows**
For each (key, value) row, generate:
- 1 MCQ: "Regarding {topic} ({key}), which statement is correct?" with A=value, B-C as plausible distractors
- 1 SBA: same shape with clinical scenario wrapper
- 1 Flashcard: "Q: {key}? A: {value}"
- 1 Answer Key row referencing the high-yield fact

**Step 4: APPEND to the file with `with open(path, 'a')`**
- Preserves the 12-25K of clinical content
- Adds 5-7K of exam extras
- Final file size: 17-30K per topic
- One Python `execute_code` call processes all 100+ files in ~0.3 seconds

**Step 5: Hand-craft blocks for files without high-yield tables**
- Older chapter files may use a different template (e.g., emoji-prefixed sections, no numbered prefix)
- For these, write a custom exam block from the file's own clinical content
- 1-5 files in a chapter typically need this — manageable as one-off edits

### Critical Section-Heading Regex Variation

Ch 7 files used **TWO** formats for the High-Yield Summary header:
- Numbered: `## 6. FCPS/MRCP High-Yield Summary` (116 files)
- Unnumbered: `## FCPS/MRCP High-Yield Summary` (1 file: Population Screening Programmes)

A regex that only matches `## \d+\.?\s*FCPS/MRCP` will MISS the unnumbered variant. **Always use the flexible regex above** that matches both via `(?:(?:\d+\.)\s*)?`.

### The Generic MCQ Distractor Trade-Off

The Pitfall 35 pattern generates distractors as `B. {v_short.split(' ')[0]} (less specific)`, `C. Empirical broad approach`, `D. No intervention required`. This is intentionally generic because the script processes 100+ topics in one batch and cannot write topic-specific distractors for each.

**Honest reporting:** The MCQs test recall of the high-yield table (key → value mapping) rather than differential-diagnosis reasoning. The Answer Key section provides the full value as the explanation, so the user learns the fact. For higher-quality topic-specific MCQs, hand-craft 5-10 per topic in a follow-up session.

## Pitfall 36 — Root-Level Topic File Glob Trap + Duplicate-Filename Detection (Ch 7 Oncology, 2026-06-16)

### Root-level file trap

`glob.glob(f"{BASE}/*/*.md", recursive=True)` only catches files **one level deep** in subfolders. If a topic file is at the chapter **root** (e.g., `Oncology/Acute Promyelocytic Leukaemia (APL).md` was at root, not in `Haematological Malignancies/`), the script silently skips it.

**Detection:**
```python
# Check for root-level .md files
for f in glob.glob(f"{BASE}/*.md"):  # NOTE: single *, not recursive
    size = os.path.getsize(f)
    if size > 5000:  # substantial file, not MOC/Template
        print(f"Root-level topic file: {os.path.basename(f)}")
```

**Fix:** Move to canonical subfolder (e.g., `APL.md` → `Haematological Malignancies/Acute Promyelocytic Leukaemia (APL).md`) AND process with the append script. The git commit will show as a rename + modify.

### Duplicate-filename detection

After Round 1 builds across multiple sessions, a chapter can have **3-5 duplicate filenames in different subfolders** that survived earlier cleanup waves. In Ch 7:
- `Colorectal Cancer Screening.md` (in `Colorectal Cancer/` AND `Cancer Screening & Prevention/`)
- `Psychosocial & Quality of Life.md` (in `Palliative Care/` AND `Survivorship & Late Effects/`)
- `GIST.md` (in `Sarcomas/` AND `Upper GI Cancers/`)

**Detection:**
```python
import os, glob
from collections import Counter
all_topics = []
for f in glob.glob(f"{BASE}/*/*.md", recursive=True):
    all_topics.append(os.path.basename(f))
dups = [t for t, c in Counter(all_topics).items() if c > 1]
if dups:
    print(f"DUPLICATES: {dups}")
```

**Fix:** `git rm` the duplicate in the less-canonical folder. Use the file with the LARGER size as the canonical one (it's the more specific topic-centric note). The umbrella-folder copy is usually the smaller, less-specific version.

## Pitfall 37 — Selective `git add` for Multi-Session Repos (Ch 7 Oncology, 2026-06-16)

When the `/mnt/tb/Medicine/` repo has parallel sessions touching other chapters, `git add -A` from inside `Oncology/` will still stage **all** unstaged files anywhere in the repo (e.g., `Adolescent and Transition Medicine/`, `Medical Ophthalmology/`).

**Bad pattern (catches other sessions' work):**
```bash
cd /mnt/tb/Medicine/Oncology
git add -A  # ← this stages files OUTSIDE Oncology!
git commit -m "Oncology: ..."  # accidentally includes 50+ files from other chapters
```

**Good pattern (scoped to one chapter):**
```bash
cd /mnt/tb/Medicine
git add "Oncology/"  # ← scoped to the chapter directory
git commit -m "Oncology: ..."  # only this chapter's files
```

**Always verify the commit scope before pushing:**
```bash
git log -1 --stat | grep "files changed"
# Should show ~120 files (the chapter's full count), not 200+
```

If the commit accidentally includes other chapters' files, `git reset --soft HEAD~1` and re-stage with the scoped pattern. The committed-but-undesired changes are preserved in the working tree (because `--soft`).

**Lesson:** always run from the **repo root**, never from inside the chapter subfolder, when staging changes for a specific chapter commit.

## Reference Files (Updated)

- `references/davidson-chapter-26-rheumatology-completion-checklist.md` — full list of 53 true Davidson Ch 26 diseases, 20 supporting notes, 8 commonly-missed diseases, classification heuristic, and reporting template. Reusable pattern for any Davidson chapter.
- `references/davidson-chapter-29-stroke-medicine-session-2026-06-16.md` — Ch 29 Session 1 build log: 116-file status-tag sweep pattern, 10-file SAH section build, duplicate root-file detection, MOC-count drift. Reusable for any chapter that combines `full-note` + `scaffold-hub` legacy tags.
- `references/davidson-chapter-29-stroke-medicine-session-2-2026-06-16.md` — Ch 29 Session 2 build log: 25 files brought from 72.2% to 100% FULL FCPS/MRCP standard. 4 valid Answer Key formats (Pitfall 22), Viva Answer Frame alias (Pitfall 23), wrapper section fix (Pitfall 24), expanded section-naming flexibility (Pitfall 25), user's "A to Z" demand pattern (Pitfall 26), 1-by-1 file audit pattern (Pitfall 27). Reusable for any chapter that needs A-to-Z completion.
- `references/davidson-chapter-31-medical-psychiatry-build-2026-06-16.md` — Ch 31 Medical Psychiatry build log: empty folder to 66/66 (100%) in one session using topic-metadata + Python batch creation (Pitfall 28), 19 heading hubs from scratch, 19 subfolder structure. Reusable for any new Davidson chapter build.
- `references/davidson-chapter-32-maternal-medicine-build-2026-06-16.md` — Ch 32 Maternal Medicine Round 1 build log: 22 organ-system hubs + 60 disease topics + 1 hierarchy + 1 MOC = 84 files in one session. Confirms the topic-metadata + Python batch pattern is **chapter-structure agnostic**.
- `references/davidson-chapter-32-maternal-medicine-round-2-missing-topics-2026-06-16.md` — Ch 32 Round 2 gap-analysis log (Pitfall 29): the 49 commonly-missed Maternal Medicine topics that the user added via "search web is any topic missing" follow-up. Includes a reusable pre-flight checklist for any future pregnancy/obstetric chapter build (the "scope lesson": the chapter is broad — medical disorders, obstetric complications, fetal medicine, labour/delivery, postpartum).
- `references/davidson-chapter-7-oncology-session-2026-06-16.md` — Ch 7 Oncology session log: 118/118 in one session via the **"Exam Extras Append from Existing High-Yield Tables" pattern (Pitfall 35)**. 117 files processed via Python batch; 1 file (APL) hand-crafted. 3 duplicates removed; APL root-level file moved to canonical folder. Reusable for any existing Davidson chapter that has rich HY tables but lacks exam extras.
- `references/davidson-chapter-25-neurology-parallel-structure-cleanup-2026-06-17.md` — Ch 25 Neurology session log: 188 duplicate template stubs deleted from parallel "Chapter 28" structure after 1-by-1 audit (Pitfalls 38, 39, 40). The audit pattern (regex-based placeholder detection) and the 4-step deletion-vs-write decision framework. Reusable for any chapter that has accumulated parallel folder structures from prior template-generation rounds.

## Pitfall 38 — Parallel Folder Structure Trap (Ch 25 Neurology, 2026-06-17)

**Symptom:** A chapter folder contains TWO parallel structures:
- Canonical (e.g., `00_Index/` through `19_Paraneoplastic_Neurological_Syndromes/`) with REAL content (15-25K each)
- Legacy/duplicate (e.g., root-level `Epilepsy/`, `Movement Disorders/`, `Epilepsy.md`, `Movement Disorders.md` stub files) with PLACEHOLDER content (1-3K each, "Option A B. Option B" patterns)

The legacy structure was created in an earlier session by a different template (e.g., Davidson Chapter 28 stub generator) and was never cleaned up. Both structures exist in parallel, creating 188+ phantom files that look "complete" (`status: full-fcps-mrcp-note` or `status: scaffold-hub`) but are duplicates of real content in the canonical structure.

**Detection (always run before claiming completion):**
```python
# Check for parallel folder structures
import os
from pathlib import Path
base = Path("/mnt/tb/Medicine/<Chapter>")
# List all top-level items
for item in sorted(base.iterdir()):
    if item.is_dir() and not item.name[:2].isdigit():
        print(f"Potential parallel structure: {item.name}")
# Also list top-level .md files (these are legacy if there are numbered subfolders)
for f in sorted(base.glob("*.md")):
    if not any(x in f.name for x in ["MOC", "Hierarchy", "Roadmap"]):
        print(f"Root-level .md: {f.name}")
```

**Fix:** Run the audit (Pitfall 39) and the deletion-vs-write decision framework (Pitfall 40). Do NOT mark the chapter complete until BOTH structures are audited and the legacy structure is either deleted (if duplicates) or filled with real content (if unique topics).

## Pitfall 39 — "Check all files 1 by 1" Honest Audit Pattern (Ch 25 Neurology, 2026-06-17)

**User trigger phrase:** "is X fully complete with information or just scaffolded check /mnt/tb/Medicine/, check all files 1 by 1" / "honestly mark and fully complete 100%"

**The #1 trap:** Counting files with `status: full-fcps-mrcp-note` and reporting "X/249 = 100% complete" without verifying the CONTENT is real. The status tag is just a string; the content is what matters.

**The audit pattern (mandatory before any completion claim):**

```python
import re
from pathlib import Path

# Placeholder patterns — these indicate template/scaffold content
PLACEHOLDER_PATTERNS = [
    "Option 1 B. Option 2",      # Generic MCQ distractor
    "Drug A B. Drug B",            # Generic treatment MCQ
    "Test A B. Test B",            # Generic investigation MCQ
    "Variable depending on the specific condition",  # Generic epidemiology
    "Comprehensive clinical note for",  # Template intro line
    "disease-scaffold",            # Legacy template tag
    "status: scaffold",            # Honest scaffold status
    "Option A B. Option B",         # Generic MCQ without 1, 2, 3
]

# Audit function
def is_real_content(path, content):
    has_status = "status: full-fcps-mrcp-note" in content
    has_template_intro = "Comprehensive clinical note for" in content
    has_generic_epidemiology = "Variable depending" in content
    placeholder_count = sum(content.count(p) for p in PLACEHOLDER_PATTERNS)
    # Real content: has status tag, NO template intro, NO generic epidemiology, <3 placeholder hits
    return has_status and not has_template_intro and not has_generic_epidemiology and placeholder_count < 3
```

**Why this works:** The status tag is easy to flip (just text replacement). The placeholder patterns are harder to fake because real clinical content has drug names, doses, genetics, imaging, and trial references — not "Option A B. Option B" patterns.

**Reporting template:**
```
=== POST-CLEANUP AUDIT ===
Real topic files (with full clinical content): <N>
Real hub files: <N>
Leftover stubs: <N>
Total: <N>
```

**Always report 3 numbers**, not just one. A claim of "X/249 = 100%" without distinguishing real vs scaffold is meaningless.

## Pitfall 40 — The Deletion-vs-Write Decision Framework (Ch 25 Neurology, 2026-06-17)

**User trigger phrase:** "check all 187 stub carefully if it really exist then delete if not then write it properly"

When there are stubs (placeholders) to clean up, the workflow is:

**Step 1: For each stub, extract its topic**
```python
# Stubs use 3 possible topic fields in frontmatter
topic, topic_group, heading = None, None, None
for line in content.split("\n"):
    if line.strip().startswith("topic:"):
        topic = line.split(":", 1)[1].strip()
    elif line.strip().startswith("topic_group:"):
        topic_group = line.split(":", 1)[1].strip()
    elif line.strip().startswith("heading:"):
        heading = line.split(":", 1)[1].strip()
```

**Step 2: Check if a real file exists with that topic in the canonical structure**
- Build a map of all real files: `{normalized_topic: path}`
- Use fuzzy matching (normalize by removing non-alphanumeric, lowercase, check if either is substring of the other with length > 4)

**Step 3: If real file exists → DELETE the stub (it's a duplicate)**
- Reason: keeping the stub creates confusion (two structures, hard to find the real one)
- Risk: accidentally delete real content — always verify the canonical version exists and is real first

**Step 4: If no real file exists → WRITE the stub with real content**
- Use the same template as the canonical structure
- Include real clinical content (drug doses, genetics, imaging, management)
- Don't repeat the template-only patterns (those are the issue)

**Step 5: Clean up empty directories**
After deleting stubs, run `rmdir` on empty subdirectories.

**Step 6: Re-audit and report the 3 numbers**
- Real topic files
- Real hub files
- Leftover stubs (= 0)
- Total

**Lesson:** When the user says "delete if it really exists, write if not" — they are explicitly asking for a binary decision per file. Don't batch-delete blindly. Don't batch-write blindly. Decide per file: does real content exist somewhere? Yes → delete. No → write.

**Verified outcome (Ch 25 Neurology, 2026-06-17):**
- 188 stubs analyzed
- 188 deleted (all duplicates of canonical content)
- 0 written
- 7 empty directories removed
- Final: 354 files = 293 real topics + 61 hubs + 0 stubs (clean)

## Templates

- `templates/Neurology Topic Template.md` — Neurology-specific 14-section template with anatomical localisation, neuroimaging/neurophysiology/CSF investigation tables, DVLA/driving guidance, and FCPS/MRCP viva questions. Used for Davidson Chapter 25 (Neurology) build.
- `templates/Dermatology Topic Template.md` — Dermatology-specific template.
