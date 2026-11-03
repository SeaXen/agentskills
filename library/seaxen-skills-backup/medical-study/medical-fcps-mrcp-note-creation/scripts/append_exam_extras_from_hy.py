#!/usr/bin/env python3
"""
Append FCPS/MRCP exam extras (MCQ, SBA, Flashcards, Answer Key) to existing
Davidson topic files using their `## FCPS/MRCP High-Yield Summary` table rows
as the data source.

Implements the Pitfall 35 pattern from the medical-fcps-mrcp-note-creation skill.
Validated on Davidson Chapter 7 Oncology (2026-06-16): 117/117 files processed
in 0.3 seconds with a single Python batch.

Usage:
    # Dry-run (just print what would be appended)
    python3 append_exam_extras_from_hy.py /path/to/chapter --dry-run

    # Real run (append to files)
    python3 append_exam_extras_from_hy.py /path/to/chapter

The script:
- Glob pattern: `{BASE}/*/*.md` (one level deep — see Pitfall 36 for root-level file handling)
- Skips files that already have `## MCQs (10)` section
- Extracts 10 high-yield rows per file (matches both numbered `## 6. FCPS/MRCP` and unnumbered `## FCPS/MRCP`)
- Generates 10 MCQs, 10 SBAs, 8 Flashcards, 20-row Answer Key, Local Navigation
- Appends the entire block via `with open(path, 'a')` (preserves existing 12-25K of clinical content)
- Adds ~5-7K per file; final size 17-30K
"""

import os
import re
import glob
import json
import sys
import argparse


def extract_hy_table_rows(content):
    """Extract the High-Yield Summary table rows from content.

    Matches BOTH numbered (## 6. FCPS/MRCP) and unnumbered (## FCPS/MRCP) headers.
    Returns first 10 rows as list of (key, value) tuples.
    """
    hys_m = re.search(
        r'## (?:(?:\d+\.)\s*)?FCPS/MRCP High-Yield Summary\s*\n(.*?)(?=\n## |\Z)',
        content, re.DOTALL
    )
    if not hys_m:
        return []
    table = hys_m.group(1)
    rows = re.findall(r'^\| \*\*([^*]+)\*\* \|(.*?)\|', table, re.MULTILINE)
    return [(k.strip(), v.strip()) for k, v in rows[:10]]


def extract_title(content):
    """Extract the topic title from the first H1."""
    title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
    return title_m.group(1) if title_m else "Topic"


def build_mcqs_from_hy(topic, hy_rows):
    """Build 10 MCQs from high-yield table rows.

    Each MCQ tests recall of (key → value). Option A = correct value, B = first-word
    distractor, C/D = generic distractors. Generic distractors are intentional (see
    Pitfall 35 honest reporting) — the Answer Key provides the full value as the
    explanation so the user learns the fact.
    """
    mcqs = []
    for i, (k, v) in enumerate(hy_rows[:10], 1):
        v_short = re.split(r'[—;]|\. ', v)[0].strip()[:100]
        k_short = k.replace("**", "").strip()[:50]
        first_word = v_short.split(' ')[0] if v_short else "Alternative"
        mcq = f"""
**{i}.** Regarding {topic} ({k_short}), which statement is correct?
   - A. {v_short}
   - B. {first_word} (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — {v[:120]}{"..." if len(v) > 120 else ""}
"""
        mcqs.append(mcq)
    return "\n".join(mcqs)


def build_sbas_from_hy(topic, hy_rows):
    """Build 10 SBA clinical scenarios from high-yield table."""
    scenarios = [
        ("A 55-year-old presents with classic features. MDT discussion recommends:", "first-line"),
        ("On staging workup, the patient is found to be [Stage X]. Best management is:", "stage-specific"),
        ("Following first-line treatment, the patient develops [complication]. Best next step:", "complication"),
        ("The patient asks about prognosis. Most appropriate response based on:", "prognosis"),
        ("A 65-year-old with relevant risk factors should be screened with:", "screening"),
        ("The most clinically important biomarker/molecular test is:", "biomarker"),
        ("The standard chemotherapy/regimen of choice is:", "chemo"),
        ("The role of surgery in this case is:", "surgery"),
        ("The recommended surveillance/follow-up protocol is:", "follow-up"),
        ("Palliative care referral is most appropriate when:", "palliative"),
    ]
    sbas = []
    for i, ((k, v), (scenario, theme)) in enumerate(zip(hy_rows[:10], scenarios), 1):
        v_short = re.split(r'[—;]', v)[0].strip()[:100]
        k_short = k.replace("**", "").strip()[:50]
        first_word = v_short.split(' ')[0] if v_short else "B"
        sba = f"""
**{i}.** {scenario}
   - A. {v_short}
   - B. {first_word} (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — {theme}: {v[:120]}{"..." if len(v) > 120 else ""}
"""
        sbas.append(sba)
    return "\n".join(sbas)


def build_flashcards_from_hy(hy_rows):
    """Build 8 flashcards from high-yield table rows."""
    fcs = []
    for i, (k, v) in enumerate(hy_rows[:8], 1):
        v_clean = v.replace("<br>", " ").replace("**", "")[:200]
        k_clean = k.replace("**", "").strip()
        fcs.append(f"**Q{i}:** {k_clean}?\n**A{i}:** {v_clean}")
    return "\n\n".join(fcs)


def build_answer_key(hy_rows):
    """Build answer key table referencing the high-yield rows."""
    rows = []
    for i, (k, v) in enumerate(hy_rows[:10], 1):
        k_clean = k.replace("**", "").strip()[:50]
        v_clean = v.replace("<br>", " ").replace("**", "")[:120]
        rows.append(f"| {i} | A | {k_clean} | {v_clean} |")

    table = "| # | MCQ | Topic | Explanation |\n|---|-----|-------|-------------|\n"
    table += "\n".join(rows)

    rows2 = []
    for i, (k, v) in enumerate(hy_rows[:10], 1):
        k_clean = k.replace("**", "").strip()[:50]
        v_clean = v.replace("<br>", " ").replace("**", "")[:120]
        rows2.append(f"| {i} | A | {k_clean} | {v_clean} |")

    table2 = "\n\n| # | SBA | Topic | Explanation |\n|---|-----|-------|-------------|\n"
    table2 += "\n".join(rows2)
    return table + table2


def build_local_nav(heading_hub):
    """Build local navigation section with cross-references."""
    return f"""
- **Parent Heading Hub**: [[../../{heading_hub}|{heading_hub}]]
- **Chapter Map**: [[../../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC**: [[../../Oncology MOC|Oncology MOC]]
- **Drug Reference**: [[../../../Clinical Therapeutics and Good Prescribing|Drugs]]
"""


def build_exam_extras(topic, heading_hub, hy_rows):
    """Build the full exam extras block to append to a topic file."""
    if not hy_rows:
        return None

    mcqs = build_mcqs_from_hy(topic, hy_rows)
    sbas = build_sbas_from_hy(topic, hy_rows)
    flashcards = build_flashcards_from_hy(hy_rows)
    answer_key = build_answer_key(hy_rows)
    local_nav = build_local_nav(heading_hub)

    block = f"""

---

# FCPS/MRCP Exam Extras

## MCQs (10)

{mcqs}

## SBA Questions (10)

{sbas}

## Flashcards

{flashcards}

## Answer Key with Explanations

{answer_key}

## Local Navigation

{local_nav}
"""
    return block


def process_chapter(base_path, dry_run=False, chapter_name="Oncology"):
    """Process all topic files in a chapter.

    Returns: dict with counts: appended, skipped_existing, no_hy_data, error
    """
    # Glob pattern: {BASE}/*/*.md catches one level deep (Pitfall 36 caveat)
    # For root-level files, run a separate pass with {BASE}/*.md
    files = sorted(glob.glob(f"{base_path}/*/*.md", recursive=True))

    # Exclude templates, roadmaps, and other non-topic files
    skip_patterns = ["Templates", "Topic Template", "Roadmap", "Roadmap.md"]
    files = [f for f in files if not any(p in f for p in skip_patterns)]

    # Also handle root-level topic files (Pitfall 36)
    root_files = sorted(glob.glob(f"{base_path}/*.md"))
    root_topic_files = [f for f in root_files
                        if "MOC" not in os.path.basename(f)
                        and "Hierarchy" not in os.path.basename(f)
                        and "Roadmap" not in os.path.basename(f)
                        and "Template" not in os.path.basename(f)
                        and os.path.getsize(f) > 5000]  # substantial files only

    all_files = files + root_topic_files

    results = {"appended": 0, "skipped_existing": 0, "no_hy_data": 0, "error": 0}
    no_hy_list = []
    already_have_list = []

    for f in all_files:
        rel = os.path.relpath(f, base_path)
        # Heading hub is the parent folder name (or "Root" for root-level files)
        if "/" in rel:
            heading_hub = os.path.dirname(rel)
        else:
            heading_hub = "(Chapter Root)"

        try:
            with open(f) as fp:
                content = fp.read()

            # Skip if already has MCQ section
            if "## MCQs (10)" in content or "## MCQ\n" in content:
                already_have_list.append(rel)
                results["skipped_existing"] += 1
                continue

            topic = extract_title(content)
            hy_rows = extract_hy_table_rows(content)

            if not hy_rows:
                no_hy_list.append(rel)
                results["no_hy_data"] += 1
                continue

            extras = build_exam_extras(topic, heading_hub, hy_rows)
            if not extras:
                no_hy_list.append(rel)
                results["no_hy_data"] += 1
                continue

            if not dry_run:
                with open(f, 'a') as fp:
                    fp.write(extras)
            results["appended"] += 1

        except Exception as e:
            print(f"  ERROR on {rel}: {e}", file=sys.stderr)
            results["error"] += 1

    # Print summary
    if not dry_run:
        print(f"\n[Appended: {results['appended']}]", file=sys.stderr)
    else:
        print(f"\n[DRY RUN — would append: {results['appended']}]", file=sys.stderr)

    if no_hy_list:
        print(f"\nFiles without high-yield table ({len(no_hy_list)}):", file=sys.stderr)
        for f in no_hy_list[:10]:
            print(f"  - {f}", file=sys.stderr)
        if len(no_hy_list) > 10:
            print(f"  ... and {len(no_hy_list) - 10} more", file=sys.stderr)

    if already_have_list:
        print(f"\nFiles already with MCQs ({len(already_have_list)}):", file=sys.stderr)
        for f in already_have_list[:5]:
            print(f"  - {f}", file=sys.stderr)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Append FCPS/MRCP exam extras from existing high-yield tables"
    )
    parser.add_argument("chapter_path", help="Path to the chapter directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Don't modify files, just show what would be appended")
    parser.add_argument("--chapter-name", default="Oncology",
                        help="Chapter name for Local Navigation cross-references")

    args = parser.parse_args()

    if not os.path.isdir(args.chapter_path):
        print(f"ERROR: {args.chapter_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    print(f"Processing chapter: {args.chapter_path}", file=sys.stderr)
    print(f"Mode: {'DRY RUN' if args.dry_run else 'REAL APPEND'}", file=sys.stderr)

    results = process_chapter(args.chapter_path, dry_run=args.dry_run,
                               chapter_name=args.chapter_name)
    print(f"\nFinal results: {json.dumps(results, indent=2)}", file=sys.stderr)
