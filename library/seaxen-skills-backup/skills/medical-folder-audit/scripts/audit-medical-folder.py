#!/usr/bin/env python3
"""
Medical Folder Audit Scanner (v2 — multi-variant, real-content aware)

Scans a Medicine folder for FCPS/MRCP topic completeness.
Handles BOTH the emoji-header template (Variant A) and the plain-header
template (Variant B — e.g., Davidson Ch 9).
Verifies real MCQ/SBA/Flashcard content, not just header presence.
Flags MOC topic-count over-claim (MOC count > disk file count).

Usage:
  python3 audit-medical-folder.py [--base /mnt/tb/Medicine] [--chapter "Acute Medicine and Critical Illness"]
  python3 audit-medical-folder.py --report-missing  # check against textbook TOC
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Variant A (emoji) anchor set
EMOJI_ANCHORS = [
    "## 🎯 Learning Objectives",
    "## 🧠 Core Concept",
    "## ❓ MCQs",
    "## 📋 SBAs",
    "## 🎤 Viva Questions",
    "## 🗺️ Mind Map",
]

# Variant B (plain) anchor set — Davidson Ch 9 style
PLAIN_ANCHORS = [
    "## Learning Objectives",
    "## Management",
    "## MCQs (10)",          # with declared count
    "## SBA Questions (10)",  # with declared count
    "## Common Viva Questions",
    "## One-Page Revision Summary",
    "## Flashcards",
    "## Answer Key with Explanations",
]

MIN_ANCHORS_FOR_COMPLETE = 5
MIN_FILL_CHARS = 30  # a "filled" MCQ item must have ≥30 chars of real text
MIN_MCQS = 10
MIN_SBAS = 10
MIN_FLASHCARDS = 5
MIN_ANSWER_KEYS = 10

PLACEHOLDER_PATTERNS = [
    r"would be added in complete version",
    r"would be included in the complete version",
    r"will be added in the complete version",
    r"to be added in complete version",
    r"Full \d+ MCQs \+ \d+ SBAs would be",
    r"Full 10 MCQs \+ 10 SBAs would be",
    r"Full \d+ MCQs \+ \d+ SBAs would be included",
    r"in the complete version",
    r"in complete version",
    r"once the complete version is",
    r"when the full version is",
    r"\[TODO\]",
    r"\[PLACEHOLDER\]",
    r"TO BE COMPLETED",
    r"SECTION INCOMPLETE",
    r"status: scaffold-hub",
    r"status: scaffold-topic",
    r"status: scaffold-disease",
]

COMPLETE_STATUSES = {"full-fcps-mrcp-note", "full-fcps-mrcp-topic-note"}


def detect_variant(content: str) -> str:
    """Detect which template variant a file uses."""
    # Variant B has '## MCQs (10)' with declared count
    if re.search(r"## MCQs \(\d+\)", content) or re.search(r"## SBA Questions \(\d+\)", content):
        return "plain"
    # Variant A has emoji markers
    if any(a in content for a in EMOJI_ANCHORS):
        return "emoji"
    return "unknown"


def get_required_anchors(variant: str) -> List[str]:
    if variant == "plain":
        return PLAIN_ANCHORS
    if variant == "emoji":
        return EMOJI_ANCHORS
    return []


def get_section_body(content: str, header_pattern: str) -> Optional[str]:
    """Extract body of a section given a header regex pattern."""
    m = re.search(rf"^{header_pattern}\s*$(.*?)(?=^\## |\Z)",
                  content, re.MULTILINE | re.DOTALL)
    return m.group(1) if m else None


def count_filled_items(section_body: str, min_chars: int = MIN_FILL_CHARS) -> int:
    """Count numbered items (1. 2. 3.) that have at least min_chars of real text.

    Fix for the regex-on-numbered-list bug: use non-greedy + lookahead
    so '1.\\n2.\\n3.' does NOT count '2.' as content of '1.'.
    """
    if not section_body:
        return 0
    # Non-greedy match terminated by next numbered line or next section
    items = re.findall(
        r"^\s*(\d+)\.\s*(.+?)(?=\n\s*\d+\.|\n##|\Z)",
        section_body, re.MULTILINE | re.DOTALL,
    )
    return sum(1 for _, text in items
               if len(text.strip()) >= min_chars and text.strip() not in {".", ""})


def has_empty_numbered_placeholders(content: str) -> bool:
    """Detect '1.\\n2.\\n3.\\n...' empty-numbered-list pattern inside MCQ/SBA sections."""
    for header in [r"## MCQs \(\d+\)", r"## SBA Questions \(\d+\)"]:
        body = get_section_body(content, header)
        if not body:
            continue
        empty_lines = re.findall(r"^\s*\d+\.\s*$", body, re.MULTILINE)
        if len(empty_lines) >= 5:
            return True
    return False


def count_flashcards(content: str) -> int:
    """Count Q→A pairs in the Flashcards section."""
    body = get_section_body(content, r"## Flashcards")
    if not body:
        return 0
    qs = re.findall(r"Q:\s*(.+)", body)
    return sum(1 for q in qs if len(q.strip()) >= 5 and q.strip() != ":")


def count_answer_keys(content: str) -> int:
    """Count numbered answer keys in the Answer Key section."""
    body = get_section_body(content, r"## Answer Key with Explanations")
    if not body:
        # Also try the emoji variant
        body = get_section_body(content, r"## 🔑 Answer Keys")
    if not body:
        return 0
    items = re.findall(r"^\s*(\d+)\.\s*(.+?)(?=\n\s*\d+\.|\n###|\Z)",
                       body, re.MULTILINE | re.DOTALL)
    return sum(1 for _, text in items
               if len(text.strip()) >= 10 and text.strip() not in {".", ""})


def scan_file(filepath: str) -> Dict:
    """Scan a single .md file and return completeness data."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    status_match = re.search(r"status:\s*(\S+)", content)
    status = status_match.group(1) if status_match else ""
    variant = detect_variant(content)
    required_anchors = get_required_anchors(variant)
    anchor_count = sum(1 for a in required_anchors if a in content)

    has_placeholder = any(re.search(p, content, re.IGNORECASE)
                          for p in PLACEHOLDER_PATTERNS)
    has_empty_block = has_empty_numbered_placeholders(content)

    # Count real content in each required section
    mcq_body = (get_section_body(content, r"## MCQs \(\d+\)")
                or get_section_body(content, r"## ❓ MCQs")
                or "")
    sba_body = (get_section_body(content, r"## SBA Questions \(\d+\)")
                or get_section_body(content, r"## 📋 SBAs")
                or "")
    mcq_count = count_filled_items(mcq_body)
    sba_count = count_filled_items(sba_body)
    fc_count = count_flashcards(content)
    ak_count = count_answer_keys(content)

    has_real_questions = (mcq_count >= MIN_MCQS
                          and sba_count >= MIN_SBAS
                          and fc_count >= MIN_FLASHCARDS
                          and ak_count >= MIN_ANSWER_KEYS)

    is_complete = (
        status in COMPLETE_STATUSES
        and anchor_count >= MIN_ANCHORS_FOR_COMPLETE
        and not has_placeholder
        and not has_empty_block
        and has_real_questions
    )

    return {
        "path": filepath,
        "status": status,
        "variant": variant,
        "anchor_count": anchor_count,
        "has_placeholder": has_placeholder,
        "has_empty_block": has_empty_block,
        "mcq_count": mcq_count,
        "sba_count": sba_count,
        "fc_count": fc_count,
        "ak_count": ak_count,
        "is_complete": is_complete,
        "size": os.path.getsize(filepath),
    }


def scan_folder(base_path: str, chapter: Optional[str] = None) -> List[Dict]:
    """Scan all topic directories. If chapter is given, scan only that directory."""
    results = []
    if chapter:
        dirs = [os.path.join(base_path, chapter)]
    else:
        dirs = [os.path.join(base_path, d) for d in os.listdir(base_path)
                if os.path.isdir(os.path.join(base_path, d))
                and not d.startswith(".")
                and not d.startswith("00_")
                and d != "Templates"]

    for d in dirs:
        if not os.path.exists(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md"):
                continue
            if f in ("Acute Medicine and Critical Illness MOC.md",) or "Hierarchy" in f:
                continue  # skip tracking files
            results.append(scan_file(os.path.join(d, f)))
    return results


def load_moc_completed(moc_path: str) -> Set[str]:
    completed = set()
    if not os.path.exists(moc_path):
        return completed
    with open(moc_path, "r", encoding="utf-8") as f:
        content = f.read()
    completed = set(re.findall(r"✅ \[\[.*?\|(.*?)\]\]", content))
    return completed


def load_moc_claimed_total(moc_path: str) -> Optional[int]:
    """Extract the MOC's claimed topic-count from the Study Tracker row."""
    if not os.path.exists(moc_path):
        return None
    with open(moc_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Look for "| **Total** | **N** |" pattern
    m = re.search(r"\|\s*\*\*Total\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|", content)
    if m:
        return int(m.group(1))
    # Fallback: any | Total | N | row
    m = re.search(r"\|\s*Total\s*\|\s*(\d+)\s*\|", content)
    if m:
        return int(m.group(1))
    return None


def load_hierarchy_completed(hier_path: str) -> Set[str]:
    completed = set()
    if not os.path.exists(hier_path):
        return completed
    with open(hier_path, "r", encoding="utf-8") as f:
        content = f.read()
    for line in content.split("\n"):
        stripped = line.lstrip(" ")
        indent = len(line) - len(stripped)
        if "✅" in line and indent == 4:
            match = (re.search(r"✅ \[\[.*?\|(.*?)\]\]", line)
                     or re.search(r"✅ \[\[([^\]]+)\]\]", line))
            if match:
                completed.add(match.group(1))
    return completed


def report(results: List[Dict], moc_path: Optional[str] = None,
           hier_path: Optional[str] = None) -> None:
    complete = [r for r in results if r["is_complete"]]
    incomplete = [r for r in results if not r["is_complete"]]

    print("=" * 80)
    print("MEDICAL FOLDER AUDIT REPORT (v2 — multi-variant)")
    print("=" * 80)
    print(f"Files scanned: {len(results)}")
    print(f"  Variant A (emoji):   {sum(1 for r in results if r['variant'] == 'emoji')}")
    print(f"  Variant B (plain):   {sum(1 for r in results if r['variant'] == 'plain')}")
    print(f"  Unknown / mixed:     {sum(1 for r in results if r['variant'] == 'unknown')}")
    print()
    print(f"Truly complete: {len(complete)} / {len(results)}")
    print(f"Incomplete:     {len(incomplete)}")
    print()

    if incomplete:
        print("--- INCOMPLETE FILES ---")
        for r in sorted(incomplete, key=lambda x: x["path"]):
            reasons = []
            if r["status"] not in COMPLETE_STATUSES:
                reasons.append(f"status={r['status'] or 'none'}")
            if r["anchor_count"] < MIN_ANCHORS_FOR_COMPLETE:
                reasons.append(f"anchors={r['anchor_count']}")
            if r["has_placeholder"]:
                reasons.append("placeholder")
            if r["has_empty_block"]:
                reasons.append("empty-block")
            if r["mcq_count"] < MIN_MCQS:
                reasons.append(f"mcq={r['mcq_count']}")
            if r["sba_count"] < MIN_SBAS:
                reasons.append(f"sba={r['sba_count']}")
            if r["fc_count"] < MIN_FLASHCARDS:
                reasons.append(f"fc={r['fc_count']}")
            if r["ak_count"] < MIN_ANSWER_KEYS:
                reasons.append(f"ak={r['ak_count']}")
            rel = os.path.basename(os.path.dirname(r["path"])) + "/" + os.path.basename(r["path"])
            print(f"  {rel}")
            print(f"    variant={r['variant']} | {' | '.join(reasons)}")

    # MOC / Hierarchy reconciliation
    if moc_path:
        moc_completed = load_moc_completed(moc_path)
        moc_claimed = load_moc_claimed_total(moc_path)
        disk_completed = {os.path.basename(r["path"]).replace(".md", "")
                          for r in complete}
        print()
        print("--- MOC RECONCILIATION ---")
        print(f"MOC ✅ entries:           {len(moc_completed)}")
        print(f"MOC claimed total:        {moc_claimed if moc_claimed else 'N/A'}")
        print(f"Disk complete files:      {len(disk_completed)}")
        if moc_claimed and moc_claimed > len(results):
            print(f"  ⚠️  MOC OVER-CLAIM: says {moc_claimed} topics, but only {len(results)} files on disk")
            print(f"      Missing: {moc_claimed - len(results)} files")
        if moc_completed != disk_completed:
            added = moc_completed - disk_completed
            removed = disk_completed - moc_completed
            if added:
                print(f"  MOC marks complete but disk says incomplete: {sorted(added)}")
            if removed:
                print(f"  Disk complete but MOC missing: {sorted(removed)}")

    if hier_path:
        hier_completed = load_hierarchy_completed(hier_path)
        disk_completed = {os.path.basename(r["path"]).replace(".md", "")
                          for r in complete}
        print()
        print("--- HIERARCHY RECONCILIATION ---")
        print(f"Hierarchy ✅ entries: {len(hier_completed)}")
        print(f"Disk complete files:  {len(disk_completed)}")
        if hier_completed != disk_completed:
            print(f"  Diff: {sorted(hier_completed ^ disk_completed)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="/mnt/tb/Medicine")
    ap.add_argument("--chapter", default=None,
                    help="Limit scan to one chapter directory (e.g., 'Acute Medicine and Critical Illness')")
    ap.add_argument("--moc", default=None, help="Path to MOC file for reconciliation")
    ap.add_argument("--hier", default=None, help="Path to Hierarchy file for reconciliation")
    args = ap.parse_args()

    # Auto-detect MOC/Hierarchy if not given
    if args.chapter and not args.moc:
        candidate = os.path.join(args.base, args.chapter,
                                 f"{args.chapter} MOC.md")
        if os.path.exists(candidate):
            args.moc = candidate
    if args.chapter and not args.hier:
        candidate = os.path.join(args.base, args.chapter,
                                 f"Davidson Chapter 9 - {args.chapter} Hierarchy.md")
        if not os.path.exists(candidate):
            # try any Hierarchy.md
            for f in os.listdir(os.path.join(args.base, args.chapter)):
                if "Hierarchy" in f:
                    candidate = os.path.join(args.base, args.chapter, f)
                    break
        if os.path.exists(candidate):
            args.hier = candidate

    results = scan_folder(args.base, args.chapter)
    report(results, args.moc, args.hier)


if __name__ == "__main__":
    main()
