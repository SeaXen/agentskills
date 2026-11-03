#!/usr/bin/env python3
"""Extract MCQ/SBA/Flashcard data from MedSea topic.md files into questions.json.

Orchestrator — imports the pure-function parser from parser_lib.

Usage:
    python3 extract_questions.py [SITE_DIR] [OUTPUT_PATH]

Defaults:
    SITE_DIR     /mnt/tb/Sea-knowledge/#MedSea/site
    OUTPUT_PATH  <SITE_DIR>/assets/questions.json

Skips topic.md files that have no MCQ/SBA/Flashcard section. Reports per-chapter
counts at the end. Exit code 0 on success, 1 on error.
"""
import json, re, sys
from pathlib import Path
from datetime import datetime, timezone

# IMPORTANT: import the pure-function parser, not a script with side effects.
# If you put parsing logic in the same file as the main loop, importing the
# module for testing triggers the main code (validated pitfall, 2026-06-21).
try:
    from parser_lib import parse_topic
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from parser_lib import parse_topic


def main():
    site = Path(sys.argv[1] if len(sys.argv) > 1 else '/mnt/tb/Sea-knowledge/#MedSea/site')
    out_path = Path(sys.argv[2] if len(sys.argv) > 2 else site / 'assets' / 'questions.json')
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Index chapters: walk top-level dirs matching "<N>-<slug>"
    TITLE_RE = re.compile(r'<title>(.+?)[\s·].+?</title>')
    chapters = []
    for entry in sorted(site.iterdir()):
        if not entry.is_dir(): continue
        m = re.match(r'^(\d+)-(.+)$', entry.name)
        if not m: continue
        num = int(m.group(1)); slug = entry.name
        name = m.group(2).replace('-', ' ').title()
        idx = entry / 'index.html'
        if idx.exists():
            try:
                t = TITLE_RE.search(idx.read_text(encoding='utf-8', errors='ignore'))
                if t: name = t.group(1).strip()
            except Exception: pass
        chapters.append({'num': num, 'slug': slug, 'name': name})
    print(f"Found {len(chapters)} chapters", flush=True)

    all_mcq, all_sba, all_flash = [], [], []
    stats = {c['num']: {'mcq': 0, 'sba': 0, 'flashcard': 0, 'topics': 0} for c in chapters}

    n_files = 0
    for ch in chapters:
        d = site / ch['slug'] / 'diseases'
        if not d.is_dir(): continue
        for tdir in d.iterdir():
            if not tdir.is_dir(): continue
            md = tdir / 'topic.md'
            if not md.exists(): continue
            # Fast pre-check — skip files that have no relevant section
            try:
                text = md.read_text(encoding='utf-8', errors='ignore')
            except Exception: continue
            if '## MCQs' not in text and '## SBA' not in text and '## Flashcards' not in text:
                continue
            mcqs, sbas, flashes = parse_topic(text, ch['num'], ch['name'], ch['slug'], tdir.name)
            all_mcq.extend(mcqs); all_sba.extend(sbas); all_flash.extend(flashes)
            stats[ch['num']]['mcq'] += len(mcqs)
            stats[ch['num']]['sba'] += len(sbas)
            stats[ch['num']]['flashcard'] += len(flashes)
            stats[ch['num']]['topics'] += 1
            n_files += 1

    chapter_summary = []
    for ch in chapters:
        s = stats[ch['num']]
        if s['topics'] == 0: continue
        chapter_summary.append({
            'num': ch['num'], 'slug': ch['slug'], 'name': ch['name'],
            'mcq_count': s['mcq'], 'sba_count': s['sba'],
            'flashcard_count': s['flashcard'], 'topic_count': s['topics'],
        })

    out = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'version': 2,
        'totals': {
            'mcq': len(all_mcq), 'sba': len(all_sba), 'flashcard': len(all_flash),
            'chapters': len(chapter_summary),
        },
        'chapters': chapter_summary,
        'mcq': all_mcq,
        'sba': all_sba,
        'flashcard': all_flash,
    }

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, separators=(',', ':'))

    print(f"\nDONE. Processed {n_files} topic files.")
    print(f"  chapters:   {len(chapter_summary)}")
    print(f"  mcq:        {len(all_mcq)}")
    print(f"  sba:        {len(all_sba)}")
    print(f"  flashcard:  {len(all_flash)}")
    print(f"  size:       {out_path.stat().st_size/1024:.1f} KB")


if __name__ == '__main__':
    main()
