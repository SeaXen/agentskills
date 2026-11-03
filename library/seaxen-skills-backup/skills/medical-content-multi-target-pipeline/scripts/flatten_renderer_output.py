#!/usr/bin/env python3
"""
Flatten the renderer's nested output structure.

The renderer creates output at:
    <out_dir>/<slug>/<slug>.html
    <out_dir>/<slug>/<slug>.md
    <out_dir>/<slug>/<slug>.png

This script moves them up to:
    <out_dir>/topic.html
    <out_dir>/topic.md
    <out_dir>/topic.png

Usage:
    python3 flatten_renderer_output.py <chapter_dir>
    e.g. python3 flatten_renderer_output.py /mnt/tb/Sea-knowledge/#MedSea/chapters/10-acute-medicine
"""
import sys
import shutil
from pathlib import Path


def flatten_topic_dir(topic_dir):
    """If topic_dir/<slug>/<slug>.{ext} exists, move to topic_dir/topic.{ext}."""
    nested_dirs = [d for d in topic_dir.iterdir() if d.is_dir()]
    if len(nested_dirs) != 1:
        return False
    nested = nested_dirs[0]
    moved = False
    for f in nested.iterdir():
        if not f.is_file():
            continue
        if f.suffix == ".png":
            dest = topic_dir / "topic.png"
        elif f.suffix in (".html", ".md"):
            dest = topic_dir / f"topic{f.suffix}"
        else:
            continue
        if not dest.exists():
            shutil.move(str(f), str(dest))
            moved = True
    # Remove the now-empty nested dir
    if not any(nested.iterdir()):
        nested.rmdir()
    return moved


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <chapter_dir>")
        sys.exit(1)
    chapter_dir = Path(sys.argv[1])
    diseases_dir = chapter_dir / "diseases"
    if not diseases_dir.exists():
        print(f"No diseases dir: {diseases_dir}")
        sys.exit(1)

    flattened = skipped = 0
    for topic_dir in sorted(diseases_dir.iterdir()):
        if not topic_dir.is_dir():
            continue
        if flatten_topic_dir(topic_dir):
            flattened += 1
        else:
            skipped += 1
    print(f"Flattened: {flattened}, Skipped (already flat): {skipped}")


if __name__ == "__main__":
    main()
