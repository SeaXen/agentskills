#!/usr/bin/env python3
"""Normalize ugly Synapse filenames in chapter-wise folders + sync state."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path("/mnt/tb/synapse_26_by_chapter")
FLAT = Path("/mnt/tb/synapse_26")
STATE = Path("/root/synapse_dl/accounts/sagar.json")

# Exact renames (old basename -> new basename) applied in chapter tree + flat + notes/
EXACT = {
    "Endocrinology -02 .mp4.mp4": "Endocrinology-02.mp4",
    "Environmental Medicine, Oncology, Pain _ palliative care, Ageing and disease.mp4": "Environmental_Oncology_Palliative_Ageing.mp4",
    "Gastroenterology - 02(ব_ক_ অ_শ).mp4": "Gastroenterology-02-part2.mp4",
    "Respiratory Medicine -01.mp4.mp4": "Respiratory-Medicine-01.mp4",
    "An Introduction to Arrhythmias .mp4.mp4": "Introduction_to_Arrhythmias.mp4",
    "Environmental_Medicine_Oncology_Pain_and_palliative_care_Ageing_and_disease_PDF.pdf": "Environmental_Oncology_Palliative_Ageing.pdf",
    "Nutritional_factors_in_disease_pdf.pdf": "Nutritional_factors_in_disease.pdf",
    "Infectious_disease_HIV_STI_davidson_pdf.pdf": "Infectious_disease_HIV_STI.pdf",
    "Rheumatology_davidson_pdf.pdf": "Rheumatology.pdf",
    "Endocrinology_PDF.pdf": "Endocrinology.pdf",
    "Nephrology_01_Class_PDF.pdf": "Nephrology-01.pdf",
    "Nephrology_2_Class_PDF.pdf": "Nephrology-02.pdf",
    "Gastroenterology_Class_PDF_by_Dr._Rafsan.pdf": "Gastroenterology_Class_Dr_Rafsan.pdf",
    "Hepatology_Class_pdf.pdf": "Hepatology_Class.pdf",
    "Hepatology_Extra_Note_by_Dr._Jabir.pdf": "Hepatology_Extra_Dr_Jabir.pdf",
    "Hematology_Class-Pdf.pdf": "Hematology_Class.pdf",
    "Hematology_class-2_PDF.pdf": "Hematology_Class-02.pdf",
    "Haematology-and-transfusion-medicine_Class_PDF.pdf": "Haematology_Transfusion_Class.pdf",
    "Medical_Psychiatry_class_notes.pdf": "Medical_Psychiatry.pdf",
    "Acute_medicine_critical_illness_Adolescent_and_transition_medicine.pdf": "Acute_Medicine_Adolescent_Transition.pdf",
    "Stroke_Medicine_Diabetes_Mellitus.pdf": "Stroke_Medicine_Diabetes.pdf",
    "Respiratory_Medicine_Davidson_pdf_2.pdf": "Respiratory_Medicine_Davidson-02.pdf",
    "Respiratory_medicine_Davidson_pdf.pdf": "Respiratory_Medicine_Davidson.pdf",
    "An-Introduction-to-Arrhythmias.mp4": "Introduction_to_Arrhythmias.mp4",
}


def auto_normalize(name: str) -> str | None:
    """Heuristic cleanup when not in EXACT map."""
    if name in EXACT:
        return EXACT[name]
    stem, dot, ext = name.rpartition(".")
    if not ext:
        return None
    new_stem = stem
    changed = False
    # double .mp4 in stem
    if re.search(r"\.mp4$", new_stem, re.I):
        new_stem = re.sub(r"\.mp4$", "", new_stem, flags=re.I)
        changed = True
    # spaces -> nothing for videos, underscore for pdfs
    if " " in new_stem or "," in new_stem:
        if ext.lower() == "mp4":
            new_stem = re.sub(r"[^A-Za-z0-9._()-]+", "-", new_stem)
            new_stem = re.sub(r"-+", "-", new_stem).strip("-")
        else:
            new_stem = re.sub(r"[^A-Za-z0-9._()-]+", "_", new_stem)
            new_stem = re.sub(r"_+", "_", new_stem).strip("_")
        changed = True
    # trailing _pdf / _PDF in stem
    if re.search(r"_(pdf|PDF)$", new_stem):
        new_stem = re.sub(r"_(pdf|PDF)$", "", new_stem)
        changed = True
    if re.search(r"_davidson_pdf$", new_stem, re.I):
        new_stem = re.sub(r"_davidson_pdf$", "", new_stem, flags=re.I)
        changed = True
    if not changed:
        return None
    new_name = f"{new_stem}.{ext}"
    return new_name if new_name != name else None


def target_name(path: Path) -> str | None:
    name = path.name
    if name in EXACT:
        return EXACT[name]
    return auto_normalize(name)


def rename_in_dir(directory: Path, renames: list[tuple[Path, Path]]) -> None:
    if not directory.is_dir():
        return
    for f in sorted(directory.iterdir()):
        if not f.is_file() or f.name.startswith("."):
            continue
        new = target_name(f)
        if not new or new == f.name:
            continue
        dst = f.with_name(new)
        if dst.exists() and dst.stat().st_size != f.stat().st_size:
            print(f"SKIP conflict: {f} -> {dst} (exists, different size)")
            continue
        renames.append((f, dst))


def apply_renames(renames: list[tuple[Path, Path]]) -> None:
    for src, dst in renames:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            src.unlink()
            print(f"dupe-removed: {src.name}")
        else:
            src.rename(dst)
            print(f"renamed: {src} -> {dst.name}")


def update_state(renames_map: dict[str, str]) -> None:
    if not STATE.exists():
        return
    data = json.loads(STATE.read_text())
    n = 0
    for bucket in ("downloaded_videos", "downloaded_notes"):
        for entry in data.get(bucket, {}).values():
            old = entry.get("filename")
            if old in renames_map:
                entry["filename"] = renames_map[old]
                n += 1
    STATE.write_text(json.dumps(data, indent=2) + "\n")
    print(f"state updated: {n} filename fields")


def main() -> int:
    renames: list[tuple[Path, Path]] = []
    for chapter in sorted(ROOT.iterdir()):
        if chapter.is_dir():
            rename_in_dir(chapter, renames)
    rename_in_dir(FLAT, renames)
    rename_in_dir(FLAT / "notes", renames)

    renames_map: dict[str, str] = {}
    for src, dst in renames:
        renames_map[src.name] = dst.name

    if not renames:
        print("Nothing to normalize.")
        return 0

    apply_renames(renames)
    update_state(renames_map)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())