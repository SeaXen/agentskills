#!/usr/bin/env python3
"""Renumber topic prefix for chapters that were renamed between Davidson editions.

Handles both storage patterns seen in MedSea chapters/:
  A. Subdirs with files inside (e.g. nephrology: diseases/15.1.1-name/topic.{md,html,png})
  B. Files directly in diseases/ (e.g. endo:    diseases/18.1.01-name.md)

Usage:
    # Edit the RENAMES dict at the top, then run:
    python3 renumber_chapters.py

Mapping (chapter folder -> old prefix -> new prefix):
  18-nephrology-urology       15.  -> 18.
  20-endocrinology            18.  -> 20.
  22-gastroenterology         21.  -> 22.
"""
import os
import sys
from pathlib import Path

REPO = Path("/mnt/tb/Sea-knowledge/#MedSea")

# (chapter_dir, old_prefix, new_prefix) - edit per renumbering task
RENAMES = {
    "18-nephrology-urology": ("15.", "18."),
    "20-endocrinology": ("18.", "20."),
    "22-gastroenterology": ("21.", "22."),
}


def renumber_dir(d: Path, old_prefix: str, new_prefix: str) -> tuple[int, int]:
    """Rename entries under d that start with old_prefix to use new_prefix.
    Handles both subdir-pattern (files inside topic subdirs) and flat-pattern
    (files directly in d).
    Returns (renamed_count, error_count).
    """
    if not d.exists():
        return 0, 0
    renamed = 0
    errors = 0

    # Pass 1a: rename files directly in d (flat pattern)
    for f in sorted(d.iterdir()):
        if f.is_dir():
            continue
        if f.name.startswith(old_prefix):
            new_name = new_prefix + f.name[len(old_prefix):]
            new_path = d / new_name
            if not new_path.exists():
                f.rename(new_path)
                renamed += 1
            else:
                print(f"  CONFLICT: {new_path} exists, skipping {f.name}")
                errors += 1

    # Pass 1b: rename files inside each subdir (nested pattern)
    for sub in sorted(d.iterdir()):
        if not sub.is_dir():
            continue
        for f in sorted(sub.iterdir()):
            if f.name.startswith(old_prefix):
                new_name = new_prefix + f.name[len(old_prefix):]
                new_path = sub / new_name
                if not new_path.exists():
                    f.rename(new_path)
                    renamed += 1
                else:
                    print(f"  CONFLICT: {new_path} exists, skipping {f.name}")
                    errors += 1

    # Pass 2: rename subdirs themselves (after their contents are renamed)
    for sub in sorted(d.iterdir(), key=lambda p: p.name):
        if sub.is_dir() and sub.name.startswith(old_prefix):
            new_name = new_prefix + sub.name[len(old_prefix):]
            new_path = d / new_name
            if not new_path.exists():
                sub.rename(new_path)
                renamed += 1
            else:
                print(f"  CONFLICT: {new_path} exists, skipping {sub.name}")
                errors += 1

    return renamed, errors


def main():
    total_renamed = 0
    total_errors = 0
    for chap_dir, (old, new) in RENAMES.items():
        diseases = REPO / "chapters" / chap_dir / "diseases"
        print(f"\n=== {chap_dir}: {old} -> {new} ===")
        rn, err = renumber_dir(diseases, old, new)
        print(f"  Renamed {rn}, errors {err}")
        total_renamed += rn
        total_errors += err
    print(f"\n=== TOTAL: renamed {total_renamed}, errors {total_errors} ===")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
