#!/usr/bin/env python3
"""Reconcile _verbatim-manifest.json against disk truth.

Idempotent. Safe to re-run. Use after large batches of new learnables, or when
the manifest drift count is non-zero.

Drift detection
- Untracked = dirs with SKILL.md not in manifest["repos"] -> ADD with verbatim_count
- Orphans   = manifest["repos"] keys with no dir on disk -> REMOVE (after ls check)

Safety: never deletes an entry without ls-verifying the dir is truly gone.
Case-mismatches like IPTV vs iptv are real, separate repos.

Usage:
    python3 reconcile_manifest.py            # dry-run, prints diff
    python3 reconcile_manifest.py --apply    # write changes
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

LB = Path.home() / ".hermes/skills/learnables"
MANIFEST = LB / "_verbatim-manifest.json"


def _leaf_count(repo_dir: Path) -> int:
    sp = repo_dir / "skills"
    if not sp.is_dir():
        return 0
    return sum(1 for sub in sp.iterdir() if sub.is_dir())


def _new_entry(repo: str, leaf_count: int) -> dict:
    return {
        repo: {
            "summary_card": True,
            "verbatim_count": leaf_count,
            "verbatim_skills": [
                {
                    "name": "reconciled",
                    "path": "skills/",
                    "note": "reconciled from prior session, exact leaf inventory in skills/",
                }
            ],
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if not MANIFEST.exists():
        print(f"manifest not found: {MANIFEST}", file=sys.stderr)
        return 2

    with MANIFEST.open() as f:
        data = json.load(f)

    disk_with_card: set[str] = set()
    disk_dirs: set[str] = set()
    for entry in LB.iterdir():
        if entry.name.startswith("_"):
            continue
        if entry.is_dir():
            disk_dirs.add(entry.name)
            if (entry / "SKILL.md").exists():
                disk_with_card.add(entry.name)

    tracked = set(data["repos"].keys())

    untracked = sorted(disk_with_card - tracked)
    orphans = sorted(tracked - disk_dirs)
    no_card = sorted(tracked - disk_dirs - orphans)  # has dir but no SKILL.md

    print(f"Disk summary cards: {len(disk_with_card)}")
    print(f"Tracked in manifest: {len(tracked)}")
    print(f"Untracked: {len(untracked)}  Orphans: {len(orphans)}  No-card: {len(no_card)}")

    if untracked:
        print("\n== UNTRACKED (will be added) ==")
        for name in untracked:
            lc = _leaf_count(LB / name)
            print(f"  + {name}  ({lc} verbatim leaves)")

    if orphans:
        print("\n== ORPHANS (will be REMOVED — ls-verified missing) ==")
        for name in orphans:
            print(f"  - {name}")
            if not args.apply:
                # In dry-run, force the user to verify by showing what's there
                similar = [d for d in disk_dirs if d.lower() == name.lower()]
                if similar:
                    print(f"      NOTE: case-mismatch? Found similar: {similar}")

    if no_card:
        print("\n== TRACKED BUT NO SKILL.md ==")
        for name in no_card:
            print(f"  ? {name}")

    if not args.apply:
        print("\nDRY-RUN. Pass --apply to write changes.")
        return 0

    # APPLY
    for name in untracked:
        lc = _leaf_count(LB / name)
        data["repos"][name] = _new_entry(name, lc)[name]

    for name in orphans:
        del data["repos"][name]

    with MANIFEST.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {MANIFEST} (now {len(data['repos'])} repos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
