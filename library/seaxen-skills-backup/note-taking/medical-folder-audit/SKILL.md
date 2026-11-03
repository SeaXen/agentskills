---
name: medical-folder-audit
description: Audit and synchronize medical study folders (FCPS/MRCP format) — verify completion status, fix tracking files (MOC, Hierarchy), standardize headers, remove duplicates, and align all sources to a single source of truth.
category: note-taking
tags: [medicine, fcps, mrcp, audit, synchronization, tracking]
---

# Medical Folder Audit Skill

## Purpose
Systematically audit medical study folders to verify which topics are truly "complete" (full FCPS/MRCP format with all 6 sections + real question banks) vs skeleton/partial, and synchronize MOC/Hierarchy tracking files to match reality.

## Triggers
- User asks to "check folder and tell me how many topics left"
- User says "fix all, truly mark which actually complete"
- User requests synchronization of MOC and Hierarchy files
- Periodic audit of study material completeness

## Core Concept: "Complete" Definition

A topic is **truly complete** iff the .md file contains its full template WITH real content (not placeholders) in every required section — including the MCQ/SBA/Flashcard question banks.

**Two template variants exist in `/mnt/tb/Medicine/`** — both must be detected:

### Variant A — Emoji Header Template (v2, the "current" canonical)
Used in: Clinical Decision-Making, Cardiology, most newer chapters. 14 sections prefixed with emoji: `## 🎯 Learning Objectives`, `## 🧠 Core Concept`, `## ❓ MCQs`, `## 📋 SBAs`, `## 🎤 Viva Questions`, `## 🗺️ Mind Map`, etc. See `references/fcps-mrcp-template-v2.md`.

### Variant B — Plain Header Template
Used in: **Davidson Ch 9 (Acute Medicine and Critical Illness)**, some other chapters. 14 sections with **plain `##` headers** (no emoji), numbered like `## MCQs (10)`, `## SBA Questions (10)`, `## Flashcards`, `## Answer Key with Explanations`, `## Common Viva Questions`, `## One-Page Revision Summary`. See `references/plain-header-template.md`.

**A correct audit script must accept BOTH variants** — checking only emoji anchors will mark every Ch 9 file as incomplete, even if they're 100% done. See pitfall #10 below.

**Common to all variants**: file must have (a) frontmatter with one of the accepted completion statuses: `status: full-fcps-mrcp-note` OR `status: full-fcps-mrcp-topic-note` OR `status: complete` (ALL three are used across different chapters — standardize on `full-fcps-mrcp-topic-note` going forward, but accept all three in audit scripts), AND (b) all required template sections, AND (c) **real content in MCQ/SBA/Flashcard/Answer-Key sections** (not just header presence).

## Standard Workflow

### 1. Inventory & Scan
```bash
# Find all .md files in topic directories
find /path/to/Medicine -type f -name "*.md" | sort

# For each file, check template anchors (BOTH variants — see Pitfall #10) + placeholder absence
# Record: display name, directory, size, has_all_template_anchors, has_real_question_content
```

### 2. Cross-Reference Tracking Files
- **MOC**: Extract `✅ [[path|display name]]` entries AND the MOC's claimed topic-count row
- **Hierarchy**: Extract leaf topics (indent=4) with `✅` marks
- **Disk**: Files with all template anchors + no placeholders + real MCQ/SBA/Flashcard content

### 3. Reconcile & Fix
| Source | Action |
|--------|--------|
| File complete, not in MOC/Hierarchy | Add `✅` entry |
| File incomplete, in MOC/Hierarchy | Remove `✅` entry |
| Duplicate skeleton directories | **Remove** (keep only main) |
| Missing standard headers | Add exact header names (variant-appropriate) |
| Placeholder content present | Mark incomplete, do NOT count |
| MOC topic-count row > actual disk file count | Fix row count; flag missing files for creation |

### 4. Header Standardization
Enforce exact header names (case-sensitive). For the **plain-header variant** (Davidson Ch 9 style):
- `## Learning Objectives` (not "objectives", "Learning objectives")
- `## Management` (not "Treatment", "Medical Treatment", "Pharmacological Therapy")
- `## MCQs (10)` (header must declare count)
- `## SBA Questions (10)` (header must declare count)
- `## Flashcards` (not "Flash Cards", "FCards")
- `## Answer Key with Explanations` (not "Answer Key", "Keys")
- `## Common Viva Questions` (not "Viva Questions", "Viva", "Revision prompts")
- `## One-Page Revision Summary` (not "One-page summary", "Revision Summary")

For the **emoji variant** (v2): see `references/header-standard.md`.

### 5. Update Tracking Files
- **MOC**: Replace "Completed scaffold-to-full-note topics" list with verified entries
- **Hierarchy**: Update `✅` marks on leaf topics (indent=4) only
- Both must match disk reality exactly
- **MOC's total-count row** (e.g., `| **Total** | **36** |`) must equal actual disk file count for the chapter

### 6. Missing-Topic Cross-Check (after #1–#5)
For each chapter, verify the MOC's topic list covers what the textbook actually has:
- Web-search `"<textbook> <edition> chapter <N> table of contents"` or check the publisher's listing
- Compare disk files + MOC entries against the official TOC
- Any textbook-listed topic with no file = **missing**, must be scaffolded
- Examples found in real audits:
  - Davidson Ch 9 (24e): ARDS and Raised Intracranial Pressure were in MOC but had no file
  - Always trust the textbook's TOC, not the MOC's own list

## Common Pitfalls
1. **Size threshold trap**: >5KB ≠ complete. Many complete files are <5KB (Atrial flutter 2.7KB). Must check headers.
2. **Duplicate display names**: "Cardiogenic shock" exists in both HF and Syncope folders → 2 files, 1 unique topic. MOC/Hierarchy track unique topics.
3. **Topic-group vs leaf**: Topic-group hubs (e.g., "Supraventricular arrhythmias") are NOT disease-level topics. Don't count them in 103 hierarchy total.
4. **Placeholder blindness**: Files with 4 sections + "MCQs would be added later" are INCOMPLETE.
5. **Header drift**: "## Treatment" instead of "## Management" breaks automated checks.
6. **Viva section gap**: Many otherwise-complete files lack "## Common Viva Questions".
7. **Tracking file lag**: MOC and Hierarchy files often show "`📋 Planned`" status even when all topic files are genuinely complete with `full-fcps-mrcp-note` frontmatter and all 14 sections. Always verify tracking files against disk reality, not just trust their status marks.
8. **Hierarchy over-claim**: Hierarchy files may mark **all leaf topics as `✅` complete** (e.g., "26/26 TOPICS FULLY COMPLETE — 100%") while disk reality shows only a subset have `full-fcps-mrcp-*` status. This happened in Chapter 6 where Hierarchy claimed 26/26 but only 4/26 files had complete status. **Always scan disk files directly**; never trust Hierarchy/MOC completion percentages.
9. **Frontmatter status drift**: Files may have `status: full-fcps-mrcp-note` but tracking files not updated. Check both.
10. **Template variant blindness** (found in Davidson Ch 9 audit, June 2026): The audit script's emoji-anchored template check (`## 🎯 Learning Objectives`, `## ❓ MCQs`, etc.) FAILS on Davidson Ch 9 files which use plain headers (`## Learning Objectives`, `## MCQs (10)`, `## SBA Questions (10)`, `## Flashcards`, `## Answer Key with Explanations`, `## Common Viva Questions`, `## One-Page Revision Summary`). If you audit only with emoji anchors, every Ch 9 file shows "incomplete" — wrong by 100%. **Always detect both variants**, or auto-detect by checking which anchors are present in the chapter.
11. **Empty numbered placeholders masquerading as complete** (found in Davidson Ch 9, June 2026): A file with `## MCQs (10)` followed by lines `1.`, `2.`, `3.`, …, `10.` (all empty) is NOT complete. The HEADER is present but the QUESTIONS are missing. A regex like `r'^\d+\.\s*(.+)'` on the MCQ section body will catch the next-numbered line as the "content" of the previous line — see pitfall #12. **Real content check**: require at least N chars of text per numbered item (e.g., 30+ chars), or require the line to NOT be a single `.` or digit+dot.
12. **Regex-on-numbered-list bug**: When matching `\d+\.\s*(.+)` over an empty placeholder block like `1.\n2.\n3.`, the regex will match the next number-line as the "content" of the current line. Result: a file with 10 empty placeholders reports "5/10 MCQs filled" instead of "0/10". The fix: anchor the content to be either a newline-terminated block ending at a number-prefixed line, or use a lookahead like `(?=\n\s*\d+\.|\n##|\Z)` combined with `.+?` (non-greedy). Always verify regex output against ground-truth files before trusting the count.
13. **MOC topic-count over-claim** (found in Davidson Ch 9 MOC, June 2026): The MOC tracker row claimed `36/36 Topics / 36/36 Scaffolded / 36/36 Notes Complete` while only 30 topic .md files existed on disk. The "36" included two MOC-listed topics (ARDS, Raised Intracranial Pressure) that had no file at all. **Always check `moc_count == disk_file_count`** in addition to the per-file completion flag. The MOC's own "✅" checkmarks inside the body can also be over-confident.
14. **Missing-topic detection requires external source-of-truth**: A folder can be "complete on disk" while missing topics that the textbook actually covers. For Davidson Ch 9, the MOC listed ARDS and Raised Intracranial Pressure — both standard FCPS/MRCP topics — but neither had a file. **Cross-check disk topic list against the official textbook table of contents** (web-search the chapter TOC, or the publisher's listing, or a reliable index). Don't trust the MOC's own list as the source of truth.
15. **Hierarchy file topic inventory can be stale** (found in Davidson Ch 20 Endocrinology, June 2026): The Hierarchy file listed all 94 topics with `status: scaffold` in its inventory tables, while all 87 corresponding disease-level files on disk had `status: full-fcps-mrcp-note` with complete 14-section Davidson template (mermaid mind maps, MCQ/SBA banks, viva questions, flashcards, mnemonics, revision trackers). The Hierarchy's own claims were 100% behind reality. **Always verify Hierarchy topic inventory status against actual file frontmatter**, not just trust the Hierarchy's own tables.
16. **MOC progress tracker can be entirely disconnected from reality** (found in Davidson Ch 20 Endocrinology MOC, June 2026): The MOC's progress tracker table showed 0% completion for all 11 theme groups (0/94 topics complete), while disk reality was 87/87 disease-level files complete (100%). **Always scan disk files directly** to compute actual completion percentages; never trust MOC summary tables.
17. **Template variants extend beyond the two known ones** (found in Davidson Ch 20 Endocrinology, June 2026): Endocrinology files use the **14-section Davidson standard template** (which includes mermaid mind maps, viva/MCQs/SBAs, flashcards, mnemonics, mind maps, revision trackers, self-test scorecards, and local navigation — more than the original 6-section or 14-section emoji/plain variants). **Detection logic must be flexible**: check for the presence of a substantial subset of expected sections (e.g., ≥10/14) rather than exact header matching, since chapter-specific template extensions exist.

18. **Duplicate filenames from scaffold-to-completion file renaming drift** (found in Davidson Ch 22, June 2026): When completing a chapter, the original scaffold file may have a slightly different filename than the later completed file. E.g. original scaffold = `Zinc- Acrodermatitis & Wound Healing.md` (~3KB, 169 lines); completed = `Zinc- Acrodermatitis, Wound Healing & Immunity.md` (~31KB, 503 lines). Both files coexist silently. Hierarchy/MOC only link to one. Fix: identify the small (scaffold) file and the large (completed) file, then `mv scaffold_file scaffold_file.tmp && rm scaffold_file.tmp && mv completed_file scaffold_file_name`. ALWAYS run `ls | sort` and check file size before/after completion. Reference: Ch 22 Nutritional Factors Disease-level fix.

19. **Agent session-end completion claim can be 2× too low by ignoring pre-existing complete files** (found in Davidson Ch 17 Respiratory, 2026-06-16): After a work session converted 9 root-level starter notes to full FCPS/MRCP notes, the agent's session summary claimed "26/115 = 23% complete" — counting only what it had just added. The file-by-file audit revealed the actual number was 52/115 (45%) because **38 disease-level notes in subdirectories were already complete** (e.g. ABPA, Sarcoidosis, IPF, Tuberculosis, Pneumothorax subtypes) from a prior session but had not been re-counted.

**Symptoms:**
- MOC/Hierarchy "Suggested first full-note conversion queue" lists only ~11 hub files marked ✅
- Subdirectory disease-level files are also complete (have `## MCQs`, `## SBA`, `## Answer Key`, ≥10KB, 27+ sections) but are not yet marked in MOC
- Agent reports the "delta" of what it just added instead of the actual state

**Fix — MANDATORY file-by-file audit when user asks "how much is done":**
1. Run the `scripts/audit-medical-folder.py` script (or inline audit in `execute_code`) over ALL .md files
2. Count truly-complete files by disk state, not by delta from this session
3. Report `actual_complete / total` honestly
4. Update MOC's "Suggested first full-note conversion queue" to mark ALL truly complete files with ✅ (not just the ones from this session)

**Trigger phrasing to watch for (user signals that demand full re-audit, not delta summary):**
- "check all files 1 by 1"
- "is the chapter fully complete with information or just scaffolded"
- "how many topics are actually done"
- "honest progress report"
- "don't trust the MOC" / "verify against disk"

20. **Header-claim vs body-content mismatch in MCQ/SBA sections** (found in Davidson Ch 17 Respiratory, 2026-06-16, on 24 files): A file with `## MCQs (10)` header but only **5 numbered questions** in the body is INCOMPLETE even though the header satisfies a simple "section exists" check. Similarly, a file with `## SBA Questions (10)` header but only 5 questions is incomplete. The 24 files in Ch 17 matched this pattern — they had been partially completed in a prior session, the headers were correct, but the question banks were truncated.

**Detection regex (validated):**
```python
# MCQ: section must have ≥ 8 numbered questions (header says (10) but allow 8+ tolerance)
mcq_m = re.search(r"## MCQs? \(?10?\)?[^\n]*\n(.*?)(?=\n## [^#]|\Z)", content, re.DOTALL | re.IGNORECASE)
q_count = len(re.findall(r"^\d+\.\s+\S", mcq_m.group(1), re.MULTILINE))
real_mcq = q_count >= 8
```

**For Answer Key** (which often holds the answers when MCQ/SBA sections are answer-stripped):
```python
ak_m = re.search(r"## Answer Key[^\n]*\n(.*?)(?=\n## |\Z)", content, re.DOTALL | re.IGNORECASE)
a_count = len(re.findall(r"^\d+\.\s+\*\*[A-E]\.|### MCQs|### SBAs", ak_m.group(1), re.MULTILINE))
real_ak = a_count >= 5
```

**Fix:** When a file is found to have header but only partial body content, **append the missing questions** (don't rewrite the whole file). 5 MCQs + 5 SBAs + answer-key entries can usually be appended in 1-2 patches of <10KB each.

20a. **Hierarchy can have duplicate topic entries in different parent groups** (found in Davidson Ch 17 Respiratory, 2026-06-16, same day): A user re-asked "is it complete" after the previous session claimed 100% complete. The second audit revealed **114/115 (99.1%)** because the hierarchy had TWO entries for the same topic in different parent groups:
```
- [[Functional Anatomy, Physiology, and Investigations/Indications for invasive ventilation in respiratory disease|Indications for invasive ventilation in respiratory disease]]
- [[Respiratory Failure and Ventilatory Support/Indications for intubation in respiratory disease|Indications for intubation in respiratory disease]]
```
The first session built the second one (in Respiratory Failure folder) and left the first one (in Functional Anatomy folder) as a 1.6KB stub. Both are separate disease-level topics in the hierarchy (item 13 and item 101) and both need files.

**Detection:**
```python
import re
def find_duplicates_in_hierarchy(hierarchy_path, topic_name):
    with open(hierarchy_path) as f:
        content = f.read()
    matches = []
    for line in content.split("\n"):
        m = re.search(r"\[\[([^\]]+)\|([^\]]+)\]\]", line)
        if m and (topic_name in m.group(1) or topic_name in m.group(2)):
            matches.append((m.group(1), m.group(2)))
    return matches
```

**Symptoms of the bug:**
- MOC and Hierarchy show "100% complete" with all ✅ marks
- One file is reported as "STUB" by the audit
- User keeps asking "is it complete" or "are all topics done"
- The "stub" topic name appears in TWO places in the hierarchy

**Fix:** When audit reports a stub, search the hierarchy for the same topic name in other parent groups. If found, the topic is duplicated in the hierarchy and the user expects BOTH files to be complete.

26. **Multi-location completeness — check ALL output directories, not just one** (found in Davidson Ch 17-20 sync audit, 2026-06-21): MedSea chapter folders have THREE possible output locations for the same source content, and an audit that only checks ONE will report false "missing" topics:
   - `chapters/{N}/diseases/{slug}/topic.md` — Ch 16, 19 use this format
   - `chapters/{N}/diseases/{slug}/{slug}.md` — Ch 17, 18, 20 use this format (note: same name as dir, NOT `topic.md`)
   - `chapters/{N}/source/*.md` — Ch 17, 18, 20 flat .md files (e.g. `ARDS.md`)
   - `chapters/{N}/hubs/*.md` — auto-generated hub manifests for ALL chapters (these are DIFFERENT content from source hub overviews in `/mnt/tb/Medicine/{Ch}/{Subdir}/`)

A topic "missing" from one location is often present in another with a different filename. The agent once reported "33 missing hub overviews" for Ch 17-20 because it only checked `source/` vs `/mnt/tb/Medicine/{Ch}/` flat files. Reality: the disease topics were in `source/` with byte-for-byte match (0 mismatches across all 51 files in Ch 18), the hub overviews were in `hubs/` as auto-generated manifests, and the "missing" files were either duplicates with different names or hub-level overviews that MedSea has equivalents for.

**Detection — the correct completeness check** (MedSea local vs `/mnt/tb/Medicine`):
```python
# For each .md in source, check it exists in MedSea local
n = 0; mismatch = 0
for src_file in pathlib.Path("/mnt/tb/Medicine/{Chapter}").glob("*.md"):
    if "Hierarchy" in src_file.name or "MOC" in src_file.name:
        continue
    name = src_file.name
    local_file = Path(f"/mnt/tb/Sea-knowledge/#MedSea/chapters/{ch-slug}/source/{name}")
    if local_file.exists():
        if src_file.stat().st_size != local_file.stat().st_size:
            mismatch += 1
        n += 1
print(f"{n} matched, {mismatch} byte-mismatches")
```

If the count of `*.md` flat files in `source/` MATCHES `/mnt/tb/Medicine/{Ch}/*.md` (excluding Hierarchy/MOC), the disease topics are 100% synced. Don't conclude "X files missing" without first checking this byte-equality.

**Symptoms of the bug:**
- Agent reports "X files missing" but user says "is it 100%?"
- Re-checking reveals all topics are present, just in different filenames
- `comm -23` between normalized filenames shows large "missing" sets but byte-equality check shows 0 mismatches

**Fix:** Before claiming missing files, ALWAYS run the byte-equality check (every source .md in `/mnt/tb/Medicine` top-level should be present in `chapters/{N}/source/` with identical size). The 1-2% of files that are truly missing are real (e.g., Ch 14's `Metabolic Bone Disease` disease topic is genuinely absent from MedSea local — needs to be created). But a "33 missing" claim is almost always a filename mismatch, not actual content loss.

20b. **Non-ASCII character handling in file paths** (found in Davidson Ch 17, 2026-06-16): When `write_file` is called with a path containing non-ASCII characters (e.g., `Indications for invasive ventilation`), the `resolved_path` returned in the tool output may appear garbled, but the actual file on disk is correctly named. **Verify with `os.listdir()` or `glob.glob()` rather than relying on the resolved_path string.** Don't re-write the file based on a garbled resolved_path — it may already be correct.

20c. **Patch-and-merge for missing sections** (found in Davidson Ch 17, 2026-06-16): When a file is missing a single section (e.g., `## Answer Key with Explanations`), use `content.replace("## Summary", "## Answer Key with Explanations\n\n...new content...\n\n## Summary", 1)` to insert. **Watch for malformed double-header artefacts** like `## ## Summary` if the replacement string has a leading `##` — fix with `content.replace("## ## Summary", "## Summary")` and verify the section list with a regex audit.

21. **Confirm source-of-truth directory BEFORE auditing** (found in Davidson Ch 16 Cardiology, 2026-06-19): User said "check all of my cardiology topic in there" referring to a 3-system setup (`apps/website + notion + git repo`). The agent initially audited `/mnt/tb/Sea-knowledge/` because that path was the one linked to the GitHub MedSea repo. User had to redirect: *"I mean medicine note from /mnt/tb/medicine"*.

**Why this happened:** `/mnt/tb/Sea-knowledge/` (the apps/website + GitHub mirror) and `/mnt/tb/Medicine/` (the Obsidian study vault) are both cardiology-heavy. The naming overlap is confusing. The user was talking about the STUDY source (`/mnt/tb/Medicine/`), not the render/publishing source.

**Fix:** Before auditing, ALWAYS confirm which directory is canonical for the user's intent:
- `/mnt/tb/Medicine/<chapter>/` → Obsidian study vault, source-of-truth for FCPS/MRCP notes (the typical target for "is my chapter complete")
- `/mnt/tb/Sea-knowledge/<chapter>/` → Sea Knowledge style render pipeline (topic.md → topic.html → topic.png), used for the static website + Vercel
- GitHub `SeaXen/MedSea` → mirrors `/mnt/tb/Sea-knowledge/` (NOT `/mnt/tb/Medicine/`)

When the user mentions multiple systems ("apps + Notion + git"), ask which one they want audited, or list all three and report each one's sync state.

22. **Three-source sync-status reporting** (found in Davidson Ch 16 Cardiology, 2026-06-19): User framed the task around THREE systems — apps/website + Notion + GitHub. The audit must report sync status for each:
- **Local study source** (`/mnt/tb/Medicine/`) → source of truth for content, manual editing
- **GitHub backup** (`SeaXen/MedSea`) → mirrors `/mnt/tb/Sea-knowledge/`, not `/mnt/tb/Medicine/`. Auto-backup is via cron running `scripts/sync.sh`
- **Notion / Vercel** → publishing targets, no automatic sync from `/mnt/tb/Medicine/`

When the user says "all three", report:
1. Content state in each
2. Whether sync is configured (cron job, sync.sh, manual)
3. Lag between source-of-truth and mirrors (last-commit date vs last-edit date)

Pitfall: assuming `/mnt/tb/Medicine/` is mirrored to GitHub when it isn't. The MedSea repo explicitly mirrors `/mnt/tb/Sea-knowledge/` per its README.

23. **Numbered vs legacy folder duplication** (found in Davidson Ch 16 Cardiology, 2026-06-19): The chapter had BOTH:
- **Canonical numbered**: `01_Cardiac_Investigations/`, `02_Acute_Coronary_Syndromes/`, …, `16_Cardiac_Emergencies/` — 570 full notes
- **Legacy long-named**: `Clinical Assessment, Hemodynamics, and Cardiac Investigations/`, `Heart Failure and Acute Cardiac Decompensation/`, etc. — 111 full notes (shorter, older)

Both cover the same topics. Detection pattern:
```python
import re
def detect_folder_duplication(base):
    numbered = [d for d in base.iterdir() if re.match(r'^\d{2}_', d.name)]
    legacy = [d for d in base.iterdir() if d.is_dir() and not re.match(r'^\d{2}_', d.name) and d.name != 'Templates']
    # Compute topic-coverage overlap via filename keyword matching
    # If legacy files match canonical file keywords ≥70%, flag as duplication
```

**Recommendation in audit report:** "Delete the legacy long-named folders — they're superseded by the canonical numbered set. Total: ~111 redundant notes removed." Don't auto-delete without user confirmation, but flag clearly.

24. **Format compliance is a separate dimension from content completeness** (found in Davidson Ch 16 Cardiology, 2026-06-19): Existing pitfalls check "is the file complete?" (frontmatter + 14 sections + real MCQ/SBA). Add a SECOND dimension: **does it meet template format standards?**

For Davidson Ch 16 Cardiology (numbered folders, n=570 full notes):
- Content complete (frontmatter + 14 sections + MCQ + Viva + Mnemonics): **100%** ✅
- Has Mermaid diagrams: **10%** (74/570) ⚠️ — hierarchy rules require mermaid for algorithms/pathophysiology
- Has Markdown tables: **3%** (26/570) ⚠️ — hierarchy rules require tables for differentials/staging/investigations
- Has Differential Diagnosis section: **84%** (sampled)

**Detection regex (validated on Cardiology corpus):**
```python
has_mermaid = "```mermaid" in text
has_table = "|---|" in text or "| --- |" in text  # Markdown table separator
has_diff = bool(re.search(r"##.*[Dd]ifferential", text))
```

**Audit report structure:**
```
Content completeness: X/Y (NN%)
Format compliance:
  Mermaid diagrams: X/Y (NN%)
  Markdown tables:  X/Y (NN%)
  Mnemonics:        X/Y (NN%)
  Differential dx:  X/Y (NN%)
```

This separates "is the content real?" from "is it exam-friendly?" — both matter for FCPS/MRCP. The Cardiology chapter scored 100% on the first but only 10% on Mermaid — a meaningful gap that wouldn't show up in the existing audit logic.

25. **MOC progress table lags reality** (found in Davidson Ch 16 Cardiology, 2026-06-19): The MOC's Progress Tracker table showed:
> `570 disease-level notes / 549 real / 6 stubs / 115 hubs = 679 total`

Reality on disk:
> `682 full-fcps-mrcp-note / 11 starter stubs / 145 hubs = 838 total`

The MOC was last updated 2026-06-16 (3 days stale). The actual content grew past the MOC's snapshot. Always:
1. Re-compute completion percentages from disk
2. Report `MOC claimed | Disk reality | delta`
3. Recommend updating MOC table after every batch

```python
def report_moc_lag(moc_path, base_dir):
    """Returns (claimed_count, disk_count, delta) for the chapter"""
    moc_text = open(moc_path).read()
    # Extract claimed total from table row like "| **TOTAL** | **679** |"
    m = re.search(r"\*\*TOTAL\*\*.*?\*\*(\d+)\*\*", moc_text)
    claimed = int(m.group(1)) if m else None
    disk_count = sum(1 for _ in Path(base_dir).rglob("*.md"))
    return claimed, disk_count, disk_count - (claimed or 0)
```

## Support Scripts
See `scripts/audit-medical-folder.py` for a reusable scanner. The v3 script (updated 2026-06-16):
- Auto-detects Variant A (emoji) vs Variant B (plain) per file
- Accepts BOTH `status: full-fcps-mrcp-note` AND `status: full-fcps-mrcp-topic-note` (Ch 17 lesson)
- Verifies real MCQ/SBA/Flashcard/Answer-Key content (not just header presence) — with the 8+ question threshold from pitfall #20
- Catches the empty-numbered-placeholder pattern (`1.\n2.\n3.\n...`)
- Catches the "header says 10 but body has 5" partial-content pattern
- Flags MOC topic-count over-claim (`MOC claimed > disk files`) and MOC delta-over-claim (pitfall #19)

## References
- `references/fcps-mrcp-template-v2.md` — **Variant A** 14-section FCPS/MRCP template (emoji headers) with detection heuristics
- `references/plain-header-template.md` — **Variant B** 14-section FCPS/MRCP template (plain headers, e.g., Davidson Ch 9) with detection heuristics and the empty-placeholder block detector
- `references/fcps-mrcp-template.md` — legacy 6-section template (for reference only)
- `references/header-standard.md` — exact header specifications
- `references/placeholder-patterns.md` — regex patterns to detect incomplete files, **including the empty-numbered-block pattern**
- `references/davidson-ch20-endocrinology-audit-2026.md` — Endocrinology audit case (3 pitfalls: stale hierarchy, MOC progress disconnected, template variant)
- `references/davidson-ch22-audit-2026.md` — Nutritional Factors audit case (duplicate filename Zinc, status value drift across 3 values, delegate_task sub-agent failure mode)
- `references/davidson-ch17-respiratory-audit-2026.md` — Respiratory audit case (agent delta-overclaim, header-vs-body mismatch, status tag variants `full-fcps-mrcp-note` vs `full-fcps-mrcp-topic-note`)
- `references/davidson-ch17-respiratory-second-pass-2026-06-16.md` — Same-day second-pass audit case (duplicate hierarchy entries, "is X complete?" user-claim verification, web-search validation pattern, non-ASCII filename handling, patch-with-Answer-Key fix)
- `references/davidson-ch16-cardiology-audit-2026-06-19.md` — Cardiology audit case (3-source routing mistake `/mnt/tb/Sea-knowledge/` vs `/mnt/tb/Medicine/`, numbered vs legacy folder duplication, format compliance check, MOC lag)

## Output Format
Always report:
```
Complete files: X
Unique completed topics: Y (accounting for duplicates)
MOC tracked: Z
Hierarchy tracked: W
All match: true/false
```

## Integration Notes
- Works with Obsidian vault structure
- Compatible with `medical-chapter-study-pack` skill for batch creation
- Run after each batch of new notes to keep tracking honest