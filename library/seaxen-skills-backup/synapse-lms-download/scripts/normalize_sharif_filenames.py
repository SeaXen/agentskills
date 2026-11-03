#!/usr/bin/env python3
"""Normalize ugly Sharif Synapse filenames in /mnt/tb/Syn MD 26 and sync accounts/sharif.json.

Use after `download_nested.py sharif` when LMS titles create:
- `.mp4` or `..mp4`
- trailing dots before the extension
- `_PDF...pdf` / `_pdf.pdf`
- punctuation-heavy names that sanitize badly
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/mnt/tb/Syn MD 26")
STATE = Path("/root/synapse_dl/accounts/sharif.json")

EXACT = {
    "Lecture_No_10_Abdomen..mp4": "Lecture_No_10_Abdomen.mp4",
    "Abdomen_Full_Lecture_Slide_PDF...pdf": "Abdomen_Full_Lecture_Slide.pdf",
    ".mp4": "Residency_BCS_Preparation.mp4",
    "Inferior_Extremity_Lecture_PDF..pdf": "Inferior_Extremity_Lecture_PDF.pdf",
}


def auto_normalize(name: str) -> str | None:
    if name in EXACT:
        return EXACT[name]
    stem, dot, ext = name.rpartition(".")
    if not ext:
        return None
    new_stem = stem
    changed = False
    if re.search(r"\.mp4$", new_stem, re.I):
        new_stem = re.sub(r"\.mp4$", "", new_stem, flags=re.I)
        changed = True
    if re.search(r"\.\.+$", new_stem):
        new_stem = re.sub(r"\.\.+$", "", new_stem)
        changed = True
    if ext.lower() == "pdf" and re.search(r"_(pdf|PDF)+$", new_stem):
        new_stem = re.sub(r"_(pdf|PDF)+$", "", new_stem)
        changed = True
    if not changed:
        return None
    if ext.lower() == "mp4":
        new_stem = re.sub(r"[^A-Za-z0-9._()-]+", "-", new_stem)
        new_stem = re.sub(r"-+", "-", new_stem).strip("-")
    else:
        new_stem = re.sub(r"[^A-Za-z0-9._()-]+", "_", new_stem)
        new_stem = re.sub(r"_+", "_", new_stem).strip("_")
    new_name = f"{new_stem}.{ext}"
    return new_name if new_name != name else None


def iter_files(root: Path):
    for p in sorted(root.rglob("*")):
        if p.is_file() and not p.name.startswith("."):
            yield p


def main() -> int:
    renames: list[tuple[Path, Path]] = []
    for src in iter_files(ROOT):
        new_name = EXACT.get(src.name) or auto_normalize(src.name)
        if not new_name or new_name == src.name:
            continue
        dst = src.with_name(new_name)
        if dst.exists() and dst.stat().st_size != src.stat().st_size:
            print(f"SKIP conflict: {src} -> {dst}")
            continue
        renames.append((src, dst))

    if not renames:
        print("Nothing to normalize.")
        return 0

    rename_map = {}
    for src, dst in renames:
        if dst.exists():
            src.unlink()
            print(f"dupe-removed: {src.name}")
        else:
            src.rename(dst)
            print(f"renamed: {src} -> {dst.name}")
        rename_map[src.name] = dst.name

    if STATE.exists():
        data = json.loads(STATE.read_text())
        changed = 0
        for bucket in ("downloaded_videos", "downloaded_notes"):
            for entry in data.get(bucket, {}).values():
                old = entry.get("filename")
                if old in rename_map:
                    entry["filename"] = rename_map[old]
                    changed += 1
        STATE.write_text(json.dumps(data, indent=2) + "\n")
        print(f"state updated: {changed} filename fields")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
