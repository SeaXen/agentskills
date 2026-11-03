#!/usr/bin/env python3
"""
Detect placeholder/template content in Davidson chapter notes.

Usage:
    python3 detect_placeholders.py /mnt/tb/Medicine/Neurology
    python3 detect_placeholders.py /mnt/tb/Medicine/Neurology --section 02_Headache_Facial_Pain

Looks for these patterns that indicate template-skeleton content:
  - "Option A", "Drug A", "Step 1 B. Step 2" (MCQ/SBA option placeholders)
  - "ACRONYM = Expansion" (Mnemonic placeholder)
  - "based on the management section" (Explanation placeholder)

Files with ANY of these patterns are NOT complete regardless of line count.

Exit 0 = all files clean (no placeholders)
Exit 1 = at least one file has placeholders
"""

import os
import re
import sys
import argparse

PLACEHOLDER_PATTERNS = [
    (r"\bOption [A-D]\b", "MCQ option placeholder"),
    (r"\bDrug [A-E]\b", "Drug option placeholder"),
    (r"\bStep \d B\. Step \d", "SBA option placeholder"),
    (r"ACRONYM.*Expansion", "Mnemonic placeholder"),
    (r"based on the management section", "Generic explanation"),
    (r"based on the investigations section", "Generic explanation"),
    (r"\bClass [A-D]\b", "Class option placeholder"),
    (r"\bFlag \d B\. Flag \d", "Flag option placeholder"),
    (r"\bFactor [A-D]\b", "Factor option placeholder"),
    (r"\bFinding [A-D]\b", "Finding option placeholder"),
    (r"\bDx \d B\. Dx \d", "Diagnosis option placeholder"),
    (r"\bTest [A-D]\b", "Test option placeholder"),
    (r"\bCause [A-E]\b", "Cause option placeholder"),
    (r"\bMnemonic:?\s+\`?ACRONYM", "Generic mnemonic"),
    (r"based on clinical features\.", "Generic explanation"),
    (r"First-line management\.", "Generic explanation"),
]

# Files matching this pattern are HUB files (not disease notes) — skip them
HUB_PATTERN = re.compile(r"Hub|Hierarchy|MOC|Template|Roadmap", re.IGNORECASE)


def detect_placeholders(filepath):
    """Return list of (line_number, pattern_name, matched_text) for a file."""
    matches = []
    try:
        with open(filepath, encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f, start=1):
                for pattern, name in PLACEHOLDER_PATTERNS:
                    if re.search(pattern, line):
                        matches.append((i, name, line.strip()[:80]))
                        break  # one match per line is enough
    except (IOError, OSError):
        pass
    return matches


def is_topic_file(filename):
    """Skip hub/MOC/hierarchy/template files — they're navigation, not disease notes."""
    return not bool(HUB_PATTERN.search(filename))


def main():
    parser = argparse.ArgumentParser(description="Detect placeholder content in Davidson chapter notes")
    parser.add_argument("chapter_dir", help="Path to the chapter folder (e.g., /mnt/tb/Medicine/Neurology)")
    parser.add_argument("--section", help="Limit to a specific section subdirectory", default=None)
    parser.add_argument("--quiet", action="store_true", help="Only print summary, no per-file details")
    args = parser.parse_args()

    if not os.path.isdir(args.chapter_dir):
        print(f"Not a directory: {args.chapter_dir}", file=sys.stderr)
        sys.exit(2)

    total = 0
    flagged = 0

    if args.section:
        roots = [os.path.join(args.chapter_dir, args.section)]
    else:
        # Walk all subdirectories but skip section 00_Index
        roots = []
        for entry in sorted(os.listdir(args.chapter_dir)):
            full = os.path.join(args.chapter_dir, entry)
            if os.path.isdir(full) and not entry.startswith("00_") and not entry.startswith("."):
                roots.append(full)

    files_to_check = []
    for root in roots:
        if not os.path.isdir(root):
            continue
        for entry in sorted(os.listdir(root)):
            if entry.endswith(".md") and is_topic_file(entry):
                files_to_check.append(os.path.join(root, entry))

    for fpath in files_to_check:
        total += 1
        matches = detect_placeholders(fpath)
        if matches:
            flagged += 1
            if not args.quiet:
                rel = os.path.relpath(fpath, args.chapter_dir)
                first_match = matches[0]
                n = len(matches)
                print(f"  ✗ {rel}: {n} placeholder(s) (first: L{first_match[0]} {first_match[1]})")

    print()
    print(f"=== Placeholder Detection Summary ===")
    print(f"Topic files checked: {total}")
    print(f"Files with placeholders: {flagged}")
    print(f"Clean files: {total - flagged}")
    if flagged == 0:
        print()
        print("OK: No placeholder content detected. All files have real clinical content.")
        sys.exit(0)
    else:
        print()
        print(f"WARN: {flagged} files need placeholder replacement.")
        print("Use the pre-scripted subagent batching pattern from references/davidson-ch25-neurology-placeholder-pattern.md")
        sys.exit(1)


if __name__ == "__main__":
    main()
