# Davidson Ch 27 — Medical Ophthalmology, Round 2 (2026-06-17)

**Continuation of the Ch 27 work, after the duplicate-scaffold cleanup in
round 1.** This session caught a second, deeper class of gap that the
previous audit had missed even after cleanup, plus added 5 missing topics
and 5 hub-level improvements.

## What the user asked

> "All disease level topic is covered? So Medical Ophthalmology all topic
> fully completed? Check files 1 by 1, also search web is any topic missing,
> fully complete if anything missing"

Two requests fused:
1. **Mechanical file-by-file audit** (per the recurring "Check files 1 by 1"
   user pattern).
2. **Authoritative cross-check** that the chapter is comprehensive vs the
   actual Davidson 24th Ed Medical Ophthalmology scope.

## What the audit found that round 1 missed

After round 1 (cleaned duplicate scaffolds, added 7 LOs), the chapter was
flagged "92/92 full-fcps-mrcp-note ✅". Round 2 audit — with a stricter
MCQ/SBA counter — found:

| Component | Round 1 claim | Round 2 actual |
|---|---|---|
| MCQs ≥ 10 | 92/92 ✅ | **86/92** ✗ (6 systemic files had 1 MCQ + 0 SBAs) |
| SBAs ≥ 10 | 92/92 ✅ | **86/92** ✗ |
| Mnemonics (real) | 92/92 ✅ | **86/92** ✗ (6 systemic files had no Mnemonics) |
| Mind Maps (real) | 92/92 ✅ | **86/92** ✗ (6 systemic files had no Mind Map) |
| Spaced Repetition | 92/92 ✅ | **86/92** ✗ (6 systemic files had no SR) |

**Root cause:** The 6 systemic-disease files in `12_Systemic_Disease_Manifestations/`
(Ankylosing Spondylitis, HIV, Hypertension, RA, Sarcoidosis, Syphilis — all
"Ocular" suffixed) were created in an earlier session that used a
**stricter, lighter template** — only Definition, Management, FCPS/MRCP
Summary, Viva Questions. They had `## MCQs (1)` and `## SBA Questions (0)`
instead of 10/10. They had no Mnemonics, no Mind Map, no Spaced Repetition.

The `## MCQs (1)` header itself was a clue: if a file declares "1" in its
section heading, the audit can match on that, but the more reliable check
is "how many numbered items are inside the section".

**Lesson:** A chapter's MOC progress tracker can say "100% complete" with
✅ markers and the file can still be missing 6+ of the 14 required sections
if the completion check was metadata-only. **Always run a section-content
audit, not just a status-field audit.**

## Five missing high-yield topics

Cross-checking against the user's own MOC Tier 1/2/3 lists, and against
the standard Davidson 24th Ed + Kanski + MRCP curriculum, 5 topics were
absent as dedicated files:

| Topic | Folder | Reason it was missing |
|---|---|---|
| **Scleritis** | 07 Uveal Tract | Was only mentioned in RA file as subsection |
| **Episcleritis** | 07 Uveal Tract | Only mentioned in "The Red Eye (Approach)" |
| **Endophthalmitis** | 08 Retina & Vitreous | High-yield FCPS/MRCP topic, not in original batch |
| **Central Serous Chorioretinopathy** | 08 Retina & Vitreous | In MOC Tier 2 but no dedicated file |
| **Behçet's Disease (Ocular)** | 12 Systemic Disease | In MOC Tier 3 but no dedicated file |

**Web search confirmation:** Queries for "Davidson 24 ophthalmology
scleritis episcleritis endophthalmitis Behçet central serous" confirmed
all 5 are standard topics. Cross-referenced with Kanski, Oxford Handbook,
and Moorfields Private's "Ocular Manifestations of Systemic Disorders"
guide.

**New files created:** 25-30KB each, all 14 sections. Single-file
`write_file` calls — no chunking needed at this size.

## Six systemic files upgraded

For each of the 6 short files:
- Replaced `## MCQs (1)` with 10 topic-specific MCQs (5-option, plausible
  distractors, FCPS/MRCP style, with explanations).
- Replaced `## SBA Questions (0)` with 10 SBAs (scenario stem + expected
  answer + brief reasoning).
- Inserted `## Mnemonics` (5 each, topic-specific), `## Mind Map`
  (mermaid, 8+ lines, topic-specific), `## One-Page Revision Card`,
  `## Spaced Repetition Trackers` before the existing `## Tags`.

**Result:** 6 files went from 270-290 lines → 425-465 lines. All section
counters now ≥ minimum thresholds.

## Script bugs discovered while writing the upgrade script

### Bug 1: Non-greedy regex over-matching across numbered sections

When I tried to replace `## SBA Questions (0)` in a file whose body looked
like this:

```markdown
## Summary
...
## MCQs (1)
1. ...
## SBA Questions (0)
N/A
## Flashcards
...
## Answer Key with Explanations
### MCQs
### SBAs
## Self-Test Scorecard
## Exam Answer Modes
## Tags
```

…the regex `## SBA Questions \(\d+\)\n.*?(?=^##\s|\Z)` looked like it would
stop at the first `## `, but the file ALSO had `### ` (level-3) headings
inside "Answer Key with Explanations". And because some files in the
chapter had `## 7. Section Title` style numbered headings (level 2 with
a number prefix), the lookahead `(?=^##\s|\Z)` matched but the
non-greedy `.*?` still captured too many sections downstream before
hitting that next `## `.

**Fix:** Use a **bounded block** approach with explicit `next_m` search
on the next level-2 heading, instead of a `.*?` regex.

```python
m = re.search(r'^##\s+SBA Questions.*$', c, re.M)
if m:
    start = m.start()
    next_m = re.search(r'^##\s+', c[start+5:], re.M)  # next level-2 heading
    end = start + 5 + next_m.start() if next_m else len(c)
    block = c[start:end]
    # do replacement only on this bounded block
```

This pattern (find section start, find next level-2 heading, slice,
replace) is the reliable way to rewrite one section at a time in files
that have both level-2 and level-3 headings.

### Bug 2: MCQ/SBA counter regex format mismatch

The audit counted "how many questions in the MCQ section" by looking for
lines matching `^\*\*\d+\.\s+`. But the actual MCQ format in the chapter
was:

```markdown
## 18. MCQs (10)

1. **Question:** Which cranial nerve innervates the superior oblique?
   **Options:** A. CN II B. CN III C. CN IV ...
```

The numbered item starts with `1. **`, not `**1. **` — so my audit regex
returned 0 for every file. **Fix:** try both formats and take the max:

```python
mcq_count = max(
    len(re.findall(r'^\*\*\d+\.\s+', block, re.M)),   # **1.** format
    len(re.findall(r'^\d+\.\s+\*\*', block, re.M)),   # 1. ** format
)
```

**General lesson:** When writing audit regexes for medical notes, expect
BOTH numbering conventions. A more durable check: look for the question
markers (`Options:`, `Answer:`, `Explanation:`, `Q:`, `A:`) instead of
relying on the number format.

### Bug 3: Numbered section headings

The new files I created use `## 18. MCQs (10)`, `## 19. SBA Questions (10)`
etc. — a level-2 heading with a section number prefix. The round-1 audit
only matched `^##\s+MCQs` which fails when the heading is `## 18. MCQs`.

**Fix:** `^##\s+(?:\d+\.\s+)?MCQs?` (optional number prefix).

**General lesson:** When generating medical notes, use EITHER all-numbered
(`## 1. ...`, `## 2. ...`) or all-unnumbered (`## Definition`, `## MCQs`)
section headings. Don't mix. The existing chapter mixes both, which is
what triggered the bug.

## Hub-level chapter mind map

Replaced the generic `## Mnemonics` + `## Mind Map` block in the
**Hierarchy file** (which is a hub, not a topic file) with:

- 10 cross-topic mnemonics spanning the whole chapter
  (e.g. "Red Eye = 5 C's", "AAU = Always Acute, Unilateral",
  "HLA-B27 = PAIR", "EVS: Vitrectomy if Light Perception",
  "CSCR = CorticoSteroid Cause Retinopathy")
- A 97-node mermaid mind map with one branch per section

This is a deliberate pattern: **hub files** (Hierarchy, MOC) deserve
**real chapter-level content**, not the same generic placeholder used
inside topic files. They serve different readers (chapter navigator
vs. topic studier).

## Five new disease files — what they look like

| File | Lines | Mermaid lines | MCQs | SBAs | Key teaching points |
|---|---|---|---|---|---|
| Scleritis | 621 | 50+ | 10 | 10 | Watson classification, T-sign, phenylephrine, scleromalacia perforans, PUK |
| Episcleritis | 577 | 40+ | 10 | 10 | Mobile vs fixed nodule, blanching, never vision-threatening |
| Endophthalmitis | 631 | 40+ | 10 | 10 | EVS protocol, coag-neg Staph, endogenous Candida, P. acnes |
| Central Serous Chorioretinopathy | 600 | 45+ | 10 | 10 | Steroid trigger, inkblot/smokestack, pachychoroid, PDT |
| Behçet's Disease (Ocular) | 659 | 50+ | 10 | 10 | HLA-B51, vasculitis A&V, pathergy, anti-TNF |

**All written in single `write_file` calls of ~28-30KB each. No chunking,
no stream timeouts.** The 4-chunk rule (from round-1 / Ch 22 lesson)
applies only at 35KB+. The sweet spot for single-file medical notes is
25-30KB.

## The "claim 100% complete" trap, again

Before this session, the MOC and the previous commit message both said
"100% complete". Both were wrong. The trap is:

1. A metadata-only audit (count files with `status: full-fcps-mrcp-note`)
   says N/N.
2. A status-from-frontmatter audit (look for `## MCQs (10)` in heading)
   also says N/N.
3. A **content audit** (count actual numbered items inside the section,
   check for required sub-sections) catches 6 files as deficient.

**Always run a content audit, not just a metadata audit.** The chapter
verification protocol in the parent skill covers this, but the protocol's
section-presence check (`grep -q "## Mind Map"`) is too coarse — it should
also count items inside the section.

**Enhanced audit check (added to chapter_audit.py round 2):**

```python
# Count items INSIDE each required section, not just section presence
for f in topic_files:
    mcq_items = count_items_in_section(f, r'(?:\d+\.\s+)?MCQs?', r'^\*\*\d+\.|^\d+\.')
    sba_items = count_items_in_section(f, r'(?:\d+\.\s+)?SBA', r'^\*\*\d+\.|^\d+\.')
    mm_lines  = count_mermaid_lines(f, r'(?:\d+\.\s+)?Mind Map')
    if mcq_items < 10 or sba_items < 10 or mm_lines < 8:
        print(f"  ✗ {f}: MCQ={mcq_items} SBA={sba_items} MM={mm_lines}")
```

The `chapter_audit.py` script now does this. The user's verification
ritual is to ask for this report — and the agent should not declare
"complete" until the report shows zero ✗ lines.

## Cross-check workflow before claiming 100%

The user's prompt included "search web is any topic missing". Concretely:

1. `web_search` for "Davidson 24th edition chapter [X] [specialty] table of
   contents". Look for the actual section list.
2. Cross-reference with NIH library catalog, Elsevier inspection copy,
   Google Books, ResearchGate paper titles.
3. If a topic is in Davidson's TOC but not in the chapter folder, create it.
4. If a topic is in the chapter MOC Tier list but not as a dedicated file,
   create it.
5. **Re-run the content audit** and confirm zero ✗.

For Ch 27, web search confirmed Scleritis, Episcleritis, Endophthalmitis,
CSCR, and Behçet's are all in the standard coverage. None were in the
folder as dedicated files. Created 5 new files.

## Final commit pattern

```bash
git add -A
git commit -m "Medical Ophthalmology: 97/97 A-Z 100% COMPLETE (5 new topics + 6 systemic files upgraded)

**5 new high-yield disease-level notes created (full 14-section FCPS/MRCP template each):**
1. Scleritis (07 Uveal Tract) — anterior 95% (diffuse, nodular, necrotising ± inflammation)...
2. Episcleritis (07 Uveal Tract) — superficial vascular plexus; benign, self-limiting, recurrent...
3. Endophthalmitis (08 Retina & Vitreous) — coag-neg Staph 70% (post-cataract); EVS protocol...
4. Central Serous Chorioretinopathy (08 Retina & Vitreous) — young male, type A, steroids...
5. Behçet's Disease (Ocular) (12 Systemic) — classic triad oral + genital + uveitis...

**6 systemic disease files upgraded** with 10/10 MCQs + 10/10 SBAs + Mnemonics + Mind Map + ...
[list each]

**Hierarchy file** updated: 92 → 97 disease-level topics; ...
**MOC** updated: 92 → 97; added Tier 2/3 references for new topics; ...

**FINAL: 97/97 full-fcps-mrcp-note**, all 14 required sections complete in every file.
Zero duplicate scaffolds remaining. 52,964 lines | 2.26 MB total."
```

## Final state

```
======================================================================
  FINAL 100% AUDIT — Medical Ophthalmology (Davidson Ch 27)
======================================================================
  Total disease topic files:     97
  Duplicate scaffold remaining:  0  ✅

  Learning Objectives:            97/97  ✅
  Real Mnemonics (≥2):            97/97  ✅
  Real Mind Maps (≥8 lines):      97/97  ✅
  MCQs (≥10):                     97/97  ✅
  SBAs (≥10):                     97/97  ✅
  Viva Questions:                 97/97  ✅
  Spaced Repetition Trackers:     97/97  ✅
  Self-Test Scorecard:            97/97  ✅
  Tags:                           97/97  ✅

  Total content:  52,964 lines  |  2.26 MB
======================================================================
```
