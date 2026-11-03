#!/usr/bin/env python3
"""
Chapter Completeness Verification Script
========================================
Verifies that a Davidson chapter directory has all required files at the
appropriate status level (full-fcps-mrcp-note for topic notes, full-fcps-mrcp-hub
for MOC/hierarchy).

Usage:
    python3 chapter_verify.py <chapter_dir> <expected_leaf_count>

Example:
    python3 chapter_verify.py "/mnt/tb/Medicine/Population Health and Epidemiology" 27

Output: structured report showing:
- Total .md files
- Files with status: full-fcps-mrcp-note (topic count)
- Files with status: full-fcps-mrcp-hub (hub count: MOC + hierarchy)
- Files with status: scaffold (should be 0)
- Files without any status tag (anomaly)
- Per-file status table
- Final verdict: PASS / FAIL with reasons
"""

import os
import sys
from pathlib import Path


def verify_chapter(chapter_dir: str, expected_leaves: int = None) -> bool:
    chapter_path = Path(chapter_dir)
    if not chapter_path.exists():
        print(f"ERROR: directory not found: {chapter_dir}")
        return False

    # Use rglob to recursively find ALL .md files in subdirectories
    files = sorted([f for f in chapter_path.rglob("*.md")])

    if not files:
        print(f"ERROR: no .md files in {chapter_dir}")
        return False

    # Categorise each file by status
    topic_files = []  # status: full-fcps-mrcp-note
    hub_files = []    # status: full-fcps-mrcp-hub
    scaffold_files = []  # status: scaffold
    no_status_files = []  # no status tag at all

    for f in files:
        try:
            content = f.read_text(errors='replace')
        except Exception as e:
            print(f"WARNING: could not read {f.name}: {e}")
            continue
        # Accept both status tag variants used in the vault
        if "status: full-fcps-mrcp-topic-note" in content or "status: full-fcps-mrcp-note" in content:
            topic_files.append(f)
        elif "status: full-fcps-mrcp-hub" in content or "status: first-pass-full-note-complete" in content:
            hub_files.append(f)
        elif "status: scaffold" in content:
            scaffold_files.append(f)
        else:
            no_status_files.append(f)

    # Print header
    print("=" * 90)
    print(f"CHAPTER COMPLETENESS VERIFICATION: {chapter_path.name}")
    print("=" * 90)
    print(f"  Total .md files:        {len(files)}")
    print(f"  Topic notes:            {len(topic_files)}")
    print(f"  Hub files (MOC+Hier):   {len(hub_files)}")
    print(f"  Remaining scaffolds:    {len(scaffold_files)}")
    print(f"  Files with no status:   {len(no_status_files)}")
    print()

    # Show problems first
    if scaffold_files:
        print(f"  ⚠️  REMAINING SCAFFOLDS ({len(scaffold_files)}):")
        for f in scaffold_files:
            print(f"      • {f.name}")
    if no_status_files:
        print(f"  ⚠️  FILES WITH NO STATUS TAG ({len(no_status_files)}):")
        for f in no_status_files:
            print(f"      • {f.name}")
    print()

    # Show topic files
    print(f"  📚 TOPIC FILES ({len(topic_files)}):")
    for i, f in enumerate(topic_files, 1):
        size = f.stat().st_size
        flag = "✅" if size > 5000 else "⚠️ small"
        print(f"      {i:2}. {flag} [{size:>6}B] {f.name}")
    print()

    # Show hub files
    if hub_files:
        print(f"  📁 HUB FILES ({len(hub_files)}):")
        for f in hub_files:
            print(f"      • {f.name}")
        print()

    # Final verdict
    print("=" * 90)
    passed = True
    if expected_leaves is not None and len(topic_files) != expected_leaves:
        print(f"  ❌ Expected {expected_leaves} topic notes, found {len(topic_files)}")
        passed = False
    if len(hub_files) < 2:
        print(f"  ❌ Expected ≥2 hub files (MOC + hierarchy), found {len(hub_files)}")
        passed = False
    if scaffold_files:
        print(f"  ❌ {len(scaffold_files)} scaffold files remaining (should be 0)")
        passed = False

    if passed:
        print(f"  ✅ CHAPTER 100% COMPLETE")
        if expected_leaves:
            print(f"     {len(topic_files)}/{expected_leaves} disease-level topics at full-fcps-mrcp-note standard")
        print(f"     + {len(hub_files)} hub files (MOC + hierarchy)")
    else:
        print(f"  ⚠️  CHAPTER NOT COMPLETE — see issues above")
    print("=" * 90)
    return passed


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    chapter_dir = sys.argv[1]
    expected = int(sys.argv[2]) if len(sys.argv) > 2 else None
    success = verify_chapter(chapter_dir, expected)
    sys.exit(0 if success else 1)
