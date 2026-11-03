#!/usr/bin/env python3
"""Organize Synapse downloads into chapter-wise folders.

Usage:
    python3 organize_by_chapter.py <source_dir> <target_dir>
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

VIDEO_KEYWORD_MAP = [
    ("Ch11_Ch12_Ch28_Poisoning_Envenomation_Ophthalmology", ["poisoning", "envenomation", "medical ophthalmology"]),
    ("Ch18_Nephrology", ["renal tubule", "bartter", "gitelman", "liddle syndrome"]),
    ("Ch19_Clinical_Biochemistry", ["clinical biochemistry", "clinical_biochemistry", "metabolic medicine"]),
    ("Ch16_Cardiology", ["cardiology", "arrhythmia", "ecg", "heart failure", "valve", "coronary"]),
    ("Ch17_Respiratory_Medicine", ["respiratory", "pulmonary", "lung", "chest", "breath", "pneumonia", "copd", "asthma"]),
    ("Ch20_Endocrinology", ["endocrinology", "diabetes"]),
    ("Ch22_Gastroenterology_Hepatology", ["gastroenterology", "hepatology"]),
    (
        "Ch08_Oncology_Palliative_Environmental_Ageing",
        [
            "environmental medicine",
            "environmental",
            "oncology",
            "palliative",
            "pain",
            "ageing",
            "acute medicine",
            "critical illness",
            "adolescent",
            "nutritional factors",
            "nutrition",
        ],
    ),
    ("Ch14_Infectious_Disease", ["infectious disease", "infectious", "hiv"]),
    ("Ch15_STIs", ["sti", "stis", "sexually transmitted"]),
    ("Ch25_Rheumatology", ["rheumatology", "bone disease", "vasculitis"]),
    ("Ch27_Neurology", ["neurology", "stroke"]),
    ("Ch24_Haematology", ["hematology", "haematology"]),
    ("Ch18_Nephrology", ["nephrology", "urology"]),
    ("Ch29_Psychiatry", ["psychiatry"]),
    ("Ch00_Orientation", ["orientation", "davidson session", "feedback session"]),
    (
        "Ch32_Geriatrics",
        ["frailty", "geriatric", "geriatric", "continence", "cognitive", "falls", "syncope"],
    ),
    ("Ch00_Orientation", ["orientation"]),
]

NOTE_KEYWORD_MAP = [
    ("Ch11_Ch12_Ch28_Poisoning_Envenomation_Ophthalmology", ["poisoning", "envenomation", "medical ophthalmology"]),
    ("Ch18_Nephrology", ["renal tubule", "bartter", "gitelman", "liddle syndrome"]),
    ("Ch19_Clinical_Biochemistry", ["clinical biochemistry", "clinical_biochemistry", "metabolic medicine"]),
    ("Ch16_Cardiology", ["cardiology", "arrhythmia", "ecg", "heart failure", "valve", "coronary"]),
    ("Ch17_Respiratory_Medicine", ["respiratory", "pulmonary", "lung", "chest", "breath", "pneumonia", "copd", "asthma"]),
    ("Ch20_Endocrinology", ["endocrinology", "diabetes"]),
    ("Ch22_Gastroenterology_Hepatology", ["gastroenterology", "hepatology"]),
    (
        "Ch08_Oncology_Palliative_Environmental_Ageing",
        ["environmental", "nutrition", "nutritional", "acute medicine", "critical illness", "adolescent"],
    ),
    ("Ch14_Infectious_Disease", ["infectious disease", "infectious", "hiv"]),
    ("Ch15_STIs", ["sti", "stis", "sexually transmitted"]),
    ("Ch25_Rheumatology", ["rheumatology", "bone disease"]),
    ("Ch27_Neurology", ["stroke"]),
    ("Ch24_Haematology", ["hematology", "haematology"]),
    ("Ch18_Nephrology", ["nephrology", "urology"]),
    ("Ch29_Psychiatry", ["psychiatry"]),
    (
        "Ch32_Geriatrics",
        ["falls", "syncope", "frailty", "geriatric", "continence", "cognitive", "legal", "ethics", "nutrition and hydration"],
    ),
]
DEFAULT_FOLDER = "Ch00_Unsorted"


def classify(name: str, keyword_map: list[tuple[str, list[str]]]) -> str:
    lower = name.lower()
    for folder, keywords in keyword_map:
        for kw in keywords:
            if re.search(rf"(?<![a-z]){re.escape(kw)}(?![a-z])", lower):
                return folder
    return DEFAULT_FOLDER


def safe_move(src: Path, dst: Path) -> str:
    if not src.exists() or not src.is_file():
        return "missing"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        if src.stat().st_size == dst.stat().st_size:
            src.unlink()
            return "dupe-removed"
        stem = dst.stem
        suffix = dst.suffix
        i = 2
        while True:
            alt = dst.with_name(f"{stem}__dup{i}{suffix}")
            if not alt.exists():
                shutil.move(str(src), str(alt))
                return f"moved-as-{alt.name}"
            i += 1
    shutil.move(str(src), str(dst))
    return "moved"


def iter_files(path: Path, suffixes: set[str]) -> list[Path]:
    return sorted(
        [p for p in path.iterdir() if p.is_file() and p.suffix.lower() in suffixes and not p.name.startswith(".")],
        key=lambda p: p.name.lower(),
    )


def main() -> int:
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <source_dir> <target_dir>")
        return 1

    src_dir = Path(sys.argv[1]).expanduser().resolve()
    tgt_dir = Path(sys.argv[2]).expanduser().resolve()
    tgt_dir.mkdir(parents=True, exist_ok=True)

    moved_any = False

    video_files = iter_files(src_dir, {".mp4", ".mkv"})
    if video_files:
        print(f"=== Videos: {len(video_files)} ===")
        for src in video_files:
            folder = classify(src.name, VIDEO_KEYWORD_MAP)
            dst = tgt_dir / folder / src.name
            result = safe_move(src, dst)
            moved_any = moved_any or result.startswith("moved") or result == "dupe-removed"
            print(f"  {src.name[:70]:70} -> {folder}/  [{result}]")

    note_sources = []
    notes_dir = src_dir / "notes"
    if notes_dir.is_dir():
        note_sources.extend(iter_files(notes_dir, {".pdf"}))
    note_sources.extend(iter_files(src_dir, {".pdf"}))

    if note_sources:
        print(f"\n=== Notes: {len(note_sources)} ===")
        seen = set()
        for src in note_sources:
            if src in seen:
                continue
            seen.add(src)
            folder = classify(src.name, NOTE_KEYWORD_MAP)
            dst = tgt_dir / folder / src.name
            result = safe_move(src, dst)
            moved_any = moved_any or result.startswith("moved") or result == "dupe-removed"
            print(f"  {src.name[:70]:70} -> {folder}/  [{result}]")

    exam_files = iter_files(src_dir, {".json"})
    if exam_files:
        print(f"\n=== Exams: {len(exam_files)} ===")
        for src in exam_files:
            dst = tgt_dir / src.name
            result = safe_move(src, dst)
            moved_any = moved_any or result.startswith("moved") or result == "dupe-removed"
            print(f"  {src.name:70} -> root  [{result}]")

    md_files = iter_files(src_dir, {".md"})
    if md_files:
        print(f"\n=== Markdown: {len(md_files)} ===")
        for src in md_files:
            folder = classify(src.name, NOTE_KEYWORD_MAP)
            dst = tgt_dir / folder / src.name
            result = safe_move(src, dst)
            moved_any = moved_any or result.startswith("moved") or result == "dupe-removed"
            print(f"  {src.name[:70]:70} -> {folder}/  [{result}]")

    print("\n=== Final layout ===")
    for folder in sorted([p for p in tgt_dir.iterdir() if p.is_dir()], key=lambda p: p.name.lower()):
        count = len([p for p in folder.iterdir() if p.is_file() and not p.name.startswith(".")])
        print(f"  {folder.name}/  ({count} files)")

    remaining_root = sorted([p.name for p in src_dir.iterdir() if p.is_file() and not p.name.startswith(".")])
    if remaining_root:
        print(f"\nRemaining files in source root: {remaining_root}")
    elif moved_any:
        print("\nSource root is clean.")
    else:
        print("\nNothing new to organize.")

    normalize = Path(__file__).resolve().parent / "normalize_chapter_filenames.py"
    if normalize.exists():
        import subprocess

        print("\n=== Normalizing filenames ===")
        subprocess.run([sys.executable, str(normalize)], check=False)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
