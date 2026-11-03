#!/usr/bin/env python3
"""Flatten the nested slug-named subdirs that render_topic.py creates.

The renderer outputs <out-dir>/<slug>/<slug>/<slug>.{md,html,png} instead of
<out-dir>/<slug>/<slug>.{md,html,png}. This script walks an output root and
moves the inner files up one level, then removes the now-empty inner dir.

Usage:
    python3 flatten_renders.py <output_root>

Idempotent: safe to re-run; if no inner slug-dir exists, it does nothing.
"""
import sys
from pathlib import Path
import shutil


def flatten(root: Path) -> int:
    moved = 0
    for hub_dir in root.iterdir():
        if not hub_dir.is_dir():
            continue
        for disease_dir in hub_dir.iterdir():
            if not disease_dir.is_dir():
                continue
            for nested in list(disease_dir.iterdir()):
                if not nested.is_dir():
                    continue
                for f in nested.iterdir():
                    target = disease_dir / f.name
                    if target.exists():
                        target.unlink()
                    f.rename(target)
                    moved += 1
                nested.rmdir()
    return moved


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_root>", file=sys.stderr)
        sys.exit(2)
    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"ERROR: {root} is not a directory", file=sys.stderr)
        sys.exit(2)
    moved = flatten(root)
    print(f"Flattened {moved} files under {root}")


if __name__ == "__main__":
    main()
