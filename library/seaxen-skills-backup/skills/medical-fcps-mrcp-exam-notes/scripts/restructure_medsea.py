#!/usr/bin/env python3
"""
MedSea Chapter Diseases Restructure (flat → nested)
====================================================

The MedSea site builder (`build_site.py`) expects:
    chapters/<slug>/diseases/<hub>.<idx>-<disease_slug>/topic.md
    chapters/<slug>/diseases/<hub>.<idx>-<disease_slug>/topic.png

But build_chapter_pipeline.py writes flat:
    chapters/<slug>/diseases/<slug>.md
    chapters/<slug>/diseases/<slug>.png   (NONE — PNGs are in the local Sea-knowledge folder)

This script:
  1. Reads manifest.json for hub/disease mapping
  2. Moves flat diseases/<slug>.md → diseases/<hub>.<idx>-<slug>/topic.md
  3. Looks up the corresponding PNG in /mnt/tb/Sea-knowledge/<local_ch>/<hub>/<disease>/images/
     and copies it to diseases/<hub>.<idx>-<slug>/topic.png

Usage:
    python3 restructure_medsea.py                # process all 12 known chapters
    python3 restructure_medsea.py <slug>         # one chapter

Run AFTER build_chapter_pipeline.py and BEFORE build_site.py.

Validated 2026-06-19 across all 12 chapters (1461 disease dirs created).
"""
import json
import re
import shutil
import sys
from pathlib import Path

SEA_ROOT = Path('/mnt/tb/Sea-knowledge')
MEDSEA_ROOT = SEA_ROOT / '#MedSea' / 'chapters'

# (chapter_num, chapter_name, medsea_slug)
CHAPTERS = [
    ('19', 'Clinical Biochemistry and Metabolic Medicine', '19-clinical-biochemistry-and-metabolic-medi'),
    ('21', 'Diabetes Mellitus', '21-diabetes-mellitus'),
    ('23', 'Hepatology', '23-hepatology'),
    ('24', 'Haematology and Transfusion Medicine', '24-haematology-and-transfusion-medicine'),
    ('25', 'Rheumatology and Bone Disease', '25-rheumatology-and-bone-disease'),
    ('26', 'Dermatology', '26-dermatology'),
    ('27', 'Neurology and Stroke Medicine', '27-neurology-and-stroke-medicine'),
    ('28', 'Medical Ophthalmology', '28-medical-ophthalmology'),
    ('29', 'Medical Psychiatry', '29-medical-psychiatry'),
    ('30', 'Maternal Medicine', '30-maternal-medicine'),
    ('31', 'Adolescence Transition and Young Adult Medicine', '31-adolescence-transition-and-young-adult-m'),
    ('32', 'Older Adult Medicine and Frailty', '32-older-adult-medicine-and-frailty'),
]


def restructure_one(num, name, slug):
    local_dir = SEA_ROOT / f'{num}. {name}'
    medsea_dir = MEDSEA_ROOT / slug
    if not local_dir.exists():
        print(f'SKIP local missing: {num}')
        return
    manifest_path = medsea_dir / 'manifest.json'
    if not manifest_path.exists():
        print(f'SKIP no manifest: {slug}')
        return
    manifest = json.loads(manifest_path.read_text())

    diseases_dir = medsea_dir / 'diseases'
    disease_info = {d['slug']: d for d in manifest.get('diseases', [])}

    moved = skipped = copied = missing = 0
    for md in sorted(diseases_dir.glob('*.md')):
        slug_name = md.stem
        info = disease_info.get(slug_name)
        if not info:
            skipped += 1
            continue
        dnum = info['num']          # e.g., "19.1.3"
        flat = f'{dnum}-{slug_name}'  # "19.1.3-hypermagnesaemia"
        target = diseases_dir / flat
        target.mkdir(exist_ok=True)
        shutil.move(str(md), str(target / 'topic.md'))
        moved += 1

        # Look up the PNG in the local Sea-knowledge folder
        hub_num = '.'.join(dnum.split('.')[:2])  # "19.1"
        hub_folder = next(
            (h for h in local_dir.iterdir()
             if h.is_dir() and h.name.startswith(hub_num + '.')), None,
        )
        if hub_folder:
            disease_folder = hub_folder / f'{dnum}. {info["name"]}'
            png = disease_folder / 'images' / f'{slug_name}.png'
            if not png.exists():
                png = disease_folder / 'images' / f'{info["name"]}.png'
            if png.exists():
                shutil.copy2(png, target / 'topic.png')
                copied += 1
            else:
                missing += 1
        else:
            missing += 1

    print(f'{num} {name}: moved {moved}, copied {copied}, '
          f'missing {missing}, skipped {skipped}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # One chapter by slug
        target = sys.argv[1]
        for n, name, slug in CHAPTERS:
            if slug == target:
                restructure_one(n, name, slug)
                break
        else:
            print(f'Unknown slug: {target}')
    else:
        for n, name, slug in CHAPTERS:
            restructure_one(n, name, slug)
