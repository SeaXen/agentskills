#!/usr/bin/env python3
"""
Davidson Chapter Build Pipeline — Single-Chapter Renderer + Manifest + Site Sync
==================================================================================

Class-level tool for converting raw Davidson source MDs in /mnt/tb/Medicine/<Chapter>/
into:
  - Rendered PNG infographics (via renderer at /root/sea-knowledge-infographics/render_topic.py)
  - Local Sea-knowledge chapter folder (hub/disease nested structure with PNGs)
  - MedSea chapter backup (chapters/<slug>/{diseases,hubs,manifest.json})
  - manifest.json tracking (chapter/hubs/diseases with names, slugs, parent_slug)

Validated 2026-06-19 across 12 chapters: Ch 19, 21, 23-32 (Davidson 25th Ed).
Built 1461 PNGs across 12 chapters in ~45 minutes wall time (sequential per chapter).

Why this is single-chapter and not multi-chapter:
- Running 12 chapters in ONE Python process hits SIGKILL (exit -9, OOM/timeout)
- The shell wrapper script /tmp/build_final.sh invokes this script per chapter
- Each invocation uses ~300-500MB peak RAM; renderer subprocess is the bottleneck

Usage:
    python3 build_chapter_pipeline.py <ch_num> <ch_name> <source_dir>
    python3 build_chapter_pipeline.py "19" "Clinical Biochemistry and Metabolic Medicine" \\
        "/mnt/tb/Medicine/Clinical Biochemistry and Metabolic Medicine"

Output structure:
    /mnt/tb/Sea-knowledge/<ch>. <Name>/            # local chapter folder
        <ch>.<hub_idx>. <Hub Name>/
            <ch>.<hub_idx>.<disease_idx>. <Disease>/
                <slug>.md
                images/<slug>.png
        <ch> MOC.md
        <ch> Hierarchy.md

    /mnt/tb/Sea-knowledge/#MedSea/chapters/<NN-slug>/
        README.md                          # copy of MOC
        manifest.json                       # hubs + diseases with slugs
        hubs/<slug>.md                      # hub-page MDs
        diseases/<slug>.md                  # TEMPORARY — see restructure_medsea.py

Source structure auto-detection (two distinct layouts):
  - "flat": all disease MDs at top level, hub-pages indicate which diseases belong
    to which hub via "## Disease-Level Topics" tables with backtick-quoted `.md` names
    (e.g. Ch 19 Clinical Biochemistry)
  - "subdirs": diseases in subdirs named by hub, e.g. <Hub>/<Disease>.md
    (e.g. Ch 25 Rheumatology)
  Auto-detect by: if >50% of candidate disease MDs have parent folder != source root
  → use subdir grouping; else → use hub-page table mapping.

Renderer interface:
    python3 /root/sea-knowledge-infographics/render_topic.py \\
        --slug <slug> --title <title> --markdown-file <md> \\
        --out-dir <dir> --tag <chapter_name>

    Output: <out_dir>/<slug>/<slug>.png  (NESTED — must flatten!)
    Also produces <out_dir>/<slug>/<slug>.html and .md (kept as artifacts)

Pitfalls encoded here:
1. Renderer writes PNG to NESTED path (<out>/<slug>/<slug>.png). Must move to
   <out>/<slug>.png and rmtree the nested dir.
2. Renderer hangs on files >400 lines (subprocess 120s timeout catches it).
3. Renderer fails silently on files with non-numeric ## headers (some Ch 19 hubs).
4. Files with "Hierarchy" or "Roadmap" in name are NOT diseases, even if >8KB.
5. Hub-page MDs are <10KB OR have "## Disease-Level Topics" header in first 2KB.
6. Subdir hub MDs (e.g. "Clinical presentation/Clinical presentation.md" if <15KB)
   are HUB OVERVIEWS, not diseases.
7. The MOC/Hierarchy MDs must be detected by name pattern, not just size.

Threshold calibration (validated):
- Disease MD: ≥8000 bytes
- Hub-page MD: <10000 bytes OR contains "## Disease-Level Topics" in first 2KB
- Hub-page in subdir (foldername.md): <15000 bytes
"""
import json
import re
import shutil
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

CH_NUM = sys.argv[1]
CH_NAME = sys.argv[2]
SRC_DIR = Path(sys.argv[3])
LOCAL_DIR = Path(f"/mnt/tb/Sea-knowledge/{CH_NUM}. {CH_NAME}")
MEDSEA_SLUG = f"{int(CH_NUM):02d}-{CH_NAME.lower().replace(' ', '-')[:40]}"
MEDSEA_DIR = Path(f"/mnt/tb/Sea-knowledge/#MedSea/chapters/{MEDSEA_SLUG}")
RENDERER = "/root/sea-knowledge-infographics/render_topic.py"
RENDER_TIMEOUT = 120  # seconds per topic

DIS_MIN_BYTES = 8000
HUB_MAX_BYTES = 10000


def clean(name: str) -> str:
    """URL-safe slug."""
    return re.sub(r'[^A-Za-z0-9]+', '-', name).strip('-').lower()[:60]


def find_tracking_files():
    """Return (moc_md, hier_md, hub_pages dict)."""
    moc_md = hier_md = None
    hub_pages = {}
    for f in sorted(SRC_DIR.iterdir()):
        if not f.is_file() or not f.name.endswith('.md'):
            continue
        nm = f.name
        if 'MOC' in nm and nm.endswith('.md'):
            moc_md = f
        elif 'Hierarchy' in nm and nm.endswith('.md'):
            hier_md = f
        elif f.stat().st_size < HUB_MAX_BYTES and f.parent == SRC_DIR:
            hub_pages[f.stem] = f
        else:
            # Hub-pages misclassified by size: detect by content
            try:
                head = f.read_text(errors='ignore')[:2000]
            except Exception:
                continue
            if 'Disease-Level Topics' in head:
                hub_pages[f.stem] = f
    return moc_md, hier_md, hub_pages


def find_disease_mds(skip_names):
    """Find all disease MDs >DIS_MIN_BYTES that aren't in skip_names."""
    out = []
    for md in sorted(SRC_DIR.rglob('*.md')):
        if md.name in skip_names:
            continue
        if 'Hierarchy' in md.name or 'Roadmap' in md.name:
            continue
        if md.stat().st_size < DIS_MIN_BYTES:
            continue
        # Subdir hub-MD (e.g. "Clinical presentation/Clinical presentation.md" if <15KB)
        rel = md.relative_to(SRC_DIR)
        if md.parent.name + '.md' == md.name and md.stat().st_size < 15000:
            continue
        out.append(md)
    return out


def parse_hub_to_diseases(hub_pages):
    """For each hub-page, extract the disease MDs it lists in its table."""
    hub_to_diseases = OrderedDict()
    for hp_stem, hp_path in hub_pages.items():
        try:
            content = hp_path.read_text(errors='ignore')
        except Exception:
            continue
        # Match `DiseaseName.md` in backticks (flat-source pattern)
        matches = re.findall(r'`([A-Z][^`\n|]*?\.md)`', content)
        stems = [m.replace('.md', '').strip() for m in matches if m.strip()]
        if stems:
            hub_to_diseases[hp_stem] = stems
    return hub_to_diseases


def group_diseases_by_hub(disease_mds, hub_to_diseases):
    """Group disease MDs by their hub. Two layouts:
    - subdirs: parent folder name == hub stem
    - flat: hub_to_diseases table maps disease stem -> hub stem
    Returns OrderedDict(hub_stem -> [md_paths]).
    """
    in_subdirs = sum(1 for m in disease_mds
                     if len(m.relative_to(SRC_DIR).parts) > 1) > len(disease_mds) / 2

    hubs = OrderedDict()
    ungrouped = []
    if in_subdirs:
        for md in disease_mds:
            rel = md.relative_to(SRC_DIR)
            hub_stem = rel.parts[0]
            hubs.setdefault(hub_stem, []).append(md)
    else:
        disease_to_hub = {}
        for hub_stem, stems in hub_to_diseases.items():
            for ds in stems:
                disease_to_hub[ds] = hub_stem
        for md in disease_mds:
            hub_stem = disease_to_hub.get(md.stem)
            if hub_stem:
                hubs.setdefault(hub_stem, []).append(md)
            else:
                ungrouped.append(md)
    if ungrouped:
        hubs['Other Topics'] = ungrouped
    return hubs


def render_topic(disease_md, slug, title, out_dir):
    """Run renderer, flatten nested PNG output. Returns True on success."""
    try:
        r = subprocess.run(
            ['python3', RENDERER,
             '--slug', slug,
             '--title', title,
             '--markdown-file', str(disease_md),
             '--out-dir', str(out_dir),
             '--tag', CH_NAME],
            capture_output=True, text=True, timeout=RENDER_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return False, 'TIMEOUT'
    except Exception as e:
        return False, f'ERR {e}'

    # Renderer outputs to <out>/<slug>/<slug>.png (NESTED)
    png_candidates = list(out_dir.rglob(f'{slug}.png'))
    if not png_candidates:
        return False, r.stderr[:200] if r.stderr else 'NO_PNG'
    png = png_candidates[0]
    final = out_dir / f'{slug}.png'
    if png != final:
        try:
            shutil.move(str(png), str(final))
        except Exception as e:
            return False, f'MOVE {e}'
    # Clean up nested dirs created by renderer
    for d in out_dir.iterdir():
        if d.is_dir():
            shutil.rmtree(d, ignore_errors=True)
    return True, 'OK'


def main():
    print(f'=== Building Ch {CH_NUM}: {CH_NAME} ===')
    print(f'Source: {SRC_DIR}')
    print(f'Local:  {LOCAL_DIR}')
    print(f'MedSea: {MEDSEA_DIR}')

    LOCAL_DIR.mkdir(parents=True, exist_ok=True)
    (MEDSEA_DIR / 'diseases').mkdir(parents=True, exist_ok=True)
    (MEDSEA_DIR / 'hubs').mkdir(parents=True, exist_ok=True)

    moc_md, hier_md, hub_pages = find_tracking_files()
    print(f'MOC:        {moc_md.name if moc_md else "NONE"}')
    print(f'Hierarchy:  {hier_md.name if hier_md else "NONE"}')
    print(f'Hub-pages:  {len(hub_pages)} found')

    skip_names = set()
    if moc_md: skip_names.add(moc_md.name)
    if hier_md: skip_names.add(hier_md.name)
    skip_names.update(n + '.md' for n in hub_pages.keys())

    disease_mds = find_disease_mds(skip_names)
    print(f'Disease MDs: {len(disease_mds)}')

    hub_to_diseases = parse_hub_to_diseases(hub_pages)
    hubs = group_diseases_by_hub(disease_mds, hub_to_diseases)
    print(f'Total hubs: {len(hubs)}')
    for h, mds in hubs.items():
        print(f'  - {h}: {len(mds)} diseases')

    # Copy MOC + Hierarchy
    if moc_md:
        shutil.copy2(moc_md, LOCAL_DIR / f'{CH_NUM} MOC.md')
        shutil.copy2(moc_md, MEDSEA_DIR / 'README.md')
    if hier_md:
        shutil.copy2(hier_md, LOCAL_DIR / f'{CH_NUM} Hierarchy.md')

    manifest = {
        'chapter': f'{CH_NUM}. {CH_NAME}',
        'total_hubs': len(hubs),
        'total_diseases': 0,
        'hubs': [],
        'diseases': [],
    }

    ok = fail = 0
    for hub_idx, (hub_stem, mds) in enumerate(hubs.items(), 1):
        hub_num = f'{CH_NUM}.{hub_idx}'
        hub_slug = clean(hub_stem)[:50]
        hub_folder = LOCAL_DIR / f'{hub_num}. {hub_stem}'
        hub_folder.mkdir(parents=True, exist_ok=True)

        manifest['hubs'].append({
            'num': hub_num, 'name': hub_stem, 'slug': hub_slug, 'has_local_md': True,
        })

        # Copy hub-page MD as overview
        if hub_stem in hub_pages:
            shutil.copy2(hub_pages[hub_stem], hub_folder / f'{hub_slug}.md')
            shutil.copy2(hub_pages[hub_stem], MEDSEA_DIR / 'hubs' / f'{hub_slug}.md')

        for i, md in enumerate(mds, 1):
            disease_num = f'{hub_num}.{i}'
            disease_name = md.stem
            disease_slug = clean(disease_name)[:50]
            disease_folder = hub_folder / f'{disease_num}. {disease_name}'
            disease_folder.mkdir(parents=True, exist_ok=True)

            # Copy MD to local + MedSea (MedSea will be restructured later)
            shutil.copy2(md, disease_folder / f'{disease_slug}.md')
            shutil.copy2(md, MEDSEA_DIR / 'diseases' / f'{disease_slug}.md')

            # Copy any sibling MDs (sub-disease detail)
            if md.parent.is_dir():
                for sub in md.parent.iterdir():
                    if (sub.is_file() and sub.suffix == '.md'
                            and sub != md and sub.stem != md.parent.name):
                        shutil.copy2(sub, disease_folder / sub.name)

            # Render PNG
            images_dir = disease_folder / 'images'
            images_dir.mkdir(exist_ok=True)
            success, msg = render_topic(md, disease_slug, disease_name, images_dir)
            if success:
                ok += 1
            else:
                fail += 1
                if fail < 5:
                    print(f'  RENDER FAIL ({msg}): {disease_name}')

            manifest['diseases'].append({
                'num': disease_num,
                'hub': hub_stem,
                'name': disease_name,
                'slug': disease_slug,
                'parent_slug': hub_slug,
            })

    manifest['total_diseases'] = len(manifest['diseases'])
    print(f'\n=== Done: {ok} rendered, {fail} failed, {len(hubs)} hubs, '
          f'{len(disease_mds)} diseases ===\n')

    with open(MEDSEA_DIR / 'manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)


if __name__ == '__main__':
    main()
