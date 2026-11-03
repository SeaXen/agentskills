#!/usr/bin/env python3
"""
MedSea Source-Sync Audit + Fill Tool
=====================================

The recurring problem: MedSea topic files exist but contain only clinical
content (no MCQs/SBAs/Flashcards/Tracker). Source `/mnt/tb/Medicine/<Chapter>/`
files have all the exam sections. This script:

1. Builds a source↔MedSea slug mapping (handles flat `.md`, nested `topic.md`,
   and source's variant leading-number formats)
2. Deduplicates source by basename (handles `/TDM/` vs `/Therapeutic Drug Monitoring/`)
3. Identifies gapped pairs (source has section MedSea doesn't)
4. Replaces MedSea content with source content + MedSea frontmatter
5. Verifies section coverage after fill

Usage:
    # Audit only (print gaps, don't modify files):
    python3 medsea_sync.py audit <src_folder> <ms_chapter_dir>

    # Fill gaps (replace MedSea content with source):
    python3 medsea_sync.py fill <src_folder> <ms_chapter_dir>

Examples:
    python3 medsea_sync.py audit /mnt/tb/Medicine/Cardiology /mnt/tb/Sea-knowledge/#MedSea/chapters/16-cardiology
    python3 medsea_sync.py fill /mnt/tb/Medicine/Respiratory /mnt/tb/Sea-knowledge/#MedSea/chapters/17-respiratory-medicine

Validates the slug-matching pitfall documented in the SKILL.md "Ch 1-15 / Ch 16-20
MedSea Sync Learnings (2026-06-20)" section.
"""

import os
import re
import sys
import json

# ---------- Slug normalization (the key fix) ----------

def slugify(name: str) -> str:
    """Generic slug: lowercase, strip non-alphanumeric, dash-separated."""
    s = name.lower()
    s = re.sub(r'[()\[\]]', '', s)
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def src_slug(basename: str) -> str:
    """Source filename slug — strips ALL leading-number variants.

    Handles: '1. Fundamentals.md', '2.1 Chlamydia.md', '5.1-5.4 Genetic Testing.md',
    'Cardiomyopathy.md', 'Acute Coronary Syndrome.md'.
    """
    bn = basename.replace('.md', '').replace('_full', '').replace('_Hub', '')
    # Strip leading numbers like '1.', '2.1', '10.', '5.1-5.4', '01_'
    bn = re.sub(r'^\d+(\.\d+)*[\.\s_-]*', '', bn).strip()
    return slugify(bn)


def ms_slug(ms_path: str) -> str:
    """MedSea filename slug — strips '<chapter>.<hub>.<num>-' prefix and '-full'/'hub'.

    Handles flat ('5.4.01-hypersensitivity-allergy.md') AND nested
    ('14.1.46-toxoplasmosis/topic.md') layouts.
    """
    parent = os.path.basename(os.path.dirname(ms_path))
    bn = os.path.basename(ms_path).replace('.md', '')
    # Nested layout: slug is in parent dir name (e.g. '14.1.46-toxoplasmosis')
    if bn == 'topic':
        bn = parent
    bn = bn.replace('-full', '').replace('-hub', '')
    # Strip leading '5.4.01-' style ID prefix
    bn = re.sub(r'^\d+\.\d+\.\d+-', '', bn)
    # Also strip '16.1-' or '17.6.16-' style (varies by chapter)
    bn = re.sub(r'^\d+\.\d+(?:\.\d+)?-', '', bn)
    return slugify(bn)


def extract_topic_id(ms_path: str) -> str:
    """Extract Davidson topic ID from MedSea path. e.g. '16.6.356'."""
    parent = os.path.basename(os.path.dirname(ms_path))
    bn = os.path.basename(ms_path).replace('.md', '')
    if bn == 'topic':
        bn = parent
    m = re.match(r'^(\d+\.\d+\.\d+)', bn)
    if m:
        return m.group(1)
    m = re.match(r'^(\d+\.\d+)', bn)
    if m:
        return m.group(1)
    return "X.X.XX"


# ---------- Source dedup ----------

def dedupe_source(src_root: str):
    """Walk source, dedupe by basename. Source has duplicates like
    /TDM/Aminoglycosides.md and /Therapeutic Drug Monitoring/Aminoglycosides.md.
    """
    skip_markers = ['MOC', 'Roadmap', 'Hierarchy', 'Template', 'README', 'index']
    files = []
    for r, _, fs in os.walk(src_root):
        for f in fs:
            if not f.endswith('.md'):
                continue
            if any(m in f for m in skip_markers):
                continue
            files.append(os.path.join(r, f))
    seen = set()
    unique = []
    for sp in files:
        bn = os.path.basename(sp)
        if bn not in seen:
            seen.add(bn)
            unique.append(sp)
    return unique


def collect_medsea(ms_chapter_dir: str):
    """Walk MedSea diseases/, handle both flat and nested layouts."""
    files = []
    diseases = os.path.join(ms_chapter_dir, 'diseases')
    if not os.path.isdir(diseases):
        return files
    for r, _, fs in os.walk(diseases):
        for f in fs:
            if f.endswith('.md'):
                files.append(os.path.join(r, f))
    return files


# ---------- Section patterns ----------

PATTERNS = {
    # Viva is functionally equivalent to MCQ in source (esp. Ch 16 Cardiology)
    'mcq_or_viva': re.compile(r'^##[^#]*\b(?:MCQs?|Viva|VIVA)\b', re.IGNORECASE | re.MULTILINE),
    'mcq':         re.compile(r'^##[^#]*\bMCQs?\b', re.IGNORECASE | re.MULTILINE),
    'sba':         re.compile(r'^##[^#]*\bSBAs?\b', re.IGNORECASE | re.MULTILINE),
    'flash':       re.compile(r'^##[^#]*\bFlashcards?\b', re.IGNORECASE | re.MULTILINE),
    'track':       re.compile(r'^##[^#]*\b(?:Spaced Repetition|Revision Tracker|24-Hour Recall)', re.IGNORECASE | re.MULTILINE),
    'score':       re.compile(r'^##[^#]*\b(?:Self-Test|Scorecard)\b', re.IGNORECASE | re.MULTILINE),
}


# ---------- Build source index ----------

def build_source_index(unique_src):
    """Build slug → path index for source files. Includes parent-folder variants
    so '/Cardiology/04_Heart_Failure/Acute HF.md' can be matched by parent slug."""
    idx = {}
    for sp in unique_src:
        bn = os.path.basename(sp)
        idx[src_slug(bn)] = sp
        # Also try parent folder name (e.g. '04_Heart_Failure' → 'heart-failure')
        parent = os.path.basename(os.path.dirname(sp))
        if parent and not re.match(r'^\d+$', parent):
            parent_clean = re.sub(r'^\d+_', '', parent).replace('_', ' ')
            idx[slugify(parent_clean)] = sp
    return idx


def build_pairs(unique_src, ms_files, src_index):
    """Match each MedSea to best source."""
    pairs = []
    unmatched_ms = []
    for ms in ms_files:
        ms_slug_str = ms_slug(ms)
        best = None
        if ms_slug_str in src_index:
            best = src_index[ms_slug_str]
        else:
            for src_s, src_p in src_index.items():
                if len(ms_slug_str) >= 6 and (ms_slug_str[:10] in src_s or src_s[:10] in ms_slug_str):
                    best = src_p
                    break
                if ms_slug_str == src_s:
                    best = src_p
                    break
        if best:
            pairs.append({'src': best, 'ms': ms})
        else:
            unmatched_ms.append(ms)
    return pairs, unmatched_ms


# ---------- Frontmatter helpers ----------

def strip_existing_frontmatter(text):
    """Strip leading YAML frontmatter if present."""
    if text.startswith('---'):
        end = text.find('---', 3)
        if end != -1:
            return text[end+3:].lstrip('\n')
    return text


CHAPTER_LABELS = {
    '1': 'Clinical Decision-Making',
    '2': 'Clinical Therapeutics and Good Prescribing',
    '3': 'Clinical Genetics',
    '4': 'Clinical Immunology',
    '5': 'Nutritional Factors in Disease',
    '6': 'Population Health and Epidemiology',
    '7': 'Principles of Infectious Disease',
    '8': 'Oncology',
    '9': 'Palliative Care',
    '10': 'Acute Medicine and Critical Illness',
    '11': 'Poisoning',
    '12': 'Envenomation',
    '13': 'Medicine in Austere Environments',
    '14': 'Infectious Disease',
    '15': 'STI',
    '16': 'Cardiology',
    '17': 'Respiratory Medicine',
    '18': 'Nephrology and Urology',
    '19': 'Clinical Biochemistry and Metabolic Medicine',
    '20': 'Endocrinology',
}


def medsea_frontmatter(ms_path, topic_name, src_path):
    """Build MedSea frontmatter with topic_id extracted from MS path."""
    topic_id = extract_topic_id(ms_path)
    ch_num = topic_id.split('.')[0] if '.' in topic_id else 'X'
    ch_label = CHAPTER_LABELS.get(ch_num, 'Medicine')
    return f"""---
davidson_chapter: "Chapter {ch_num}: {ch_label}"
davidson_topic_id: "{topic_id}"
topic: "{topic_name}"
status: full-fcps-mrcp-note
priority: critical
cards: 20-25
created: 2026-06-20
modified: 2026-06-20
exam_relevance: [FCPS, MRCP Part 1, MRCP Part 2]
source: "{src_path}"
tags: [medicine, davidson, fcps, mrcp]
---

"""


# ---------- Audit ----------

def audit_coverage(files, patterns_to_check):
    """Count how many files have each section."""
    counts = {k: 0 for k in patterns_to_check}
    for p in files:
        try:
            text = open(p).read()
        except Exception:
            continue
        for k, pat in patterns_to_check.items():
            if pat.search(text):
                counts[k] += 1
    return counts


def find_gaps(pairs, patterns_to_check):
    """Find pairs where source has a section MedSea doesn't."""
    gaps = []
    for p in pairs:
        try:
            src_text = open(p['src']).read()
            ms_text = open(p['ms']).read()
        except Exception:
            continue
        missing = []
        for name, pat in patterns_to_check.items():
            if pat.search(src_text) and not pat.search(ms_text):
                missing.append(name)
        if missing:
            gaps.append({**p, 'missing': missing})
    return gaps


# ---------- Main commands ----------

def cmd_audit(src_folder, ms_chapter_dir):
    unique_src = dedupe_source(src_folder)
    ms_files = collect_medsea(ms_chapter_dir)
    src_index = build_source_index(unique_src)
    pairs, unmatched_ms = build_pairs(unique_src, ms_files, src_index)

    print(f"Source: {len(unique_src)} unique files (in {src_folder})")
    print(f"MedSea: {len(ms_files)} files (in {ms_chapter_dir}/diseases)")
    print(f"Matched pairs: {len(pairs)}")
    print(f"Unmatched MedSea: {len(unmatched_ms)}")

    # Coverage stats
    print("\n=== SECTION COVERAGE ===")
    src_counts = audit_coverage(unique_src, PATTERNS)
    ms_counts = audit_coverage(ms_files, PATTERNS)
    ns = len(unique_src)
    nm = len(ms_files)
    print(f"{'Section':<20} {'Source':>12} {'MedSea':>12} {'Diff':>8}")
    for k in PATTERNS:
        s = src_counts[k]
        m = ms_counts[k]
        sp = s * 100 / ns if ns else 0
        mp = m * 100 / nm if nm else 0
        flag = '✓' if abs(sp - mp) <= max(5, ns * 0.05) else '⚠️'
        print(f"  {k:<18} {sp:>5.0f}% ({s:>3}) {mp:>5.0f}% ({m:>3}) {mp-sp:>+6.1f}pp  {flag}")

    # Gaps
    gaps = find_gaps(pairs, PATTERNS)
    print(f"\n=== GAPS (source has, MedSea doesn't) ===")
    print(f"Total gapped pairs: {len(gaps)}")
    by_missing = {}
    for g in gaps:
        for m in g['missing']:
            by_missing[m] = by_missing.get(m, 0) + 1
    print(f"By section: {by_missing}")

    return 0 if not gaps else 1


def cmd_fill(src_folder, ms_chapter_dir):
    unique_src = dedupe_source(src_folder)
    ms_files = collect_medsea(ms_chapter_dir)
    src_index = build_source_index(unique_src)
    pairs, _ = build_pairs(unique_src, ms_files, src_index)
    gaps = find_gaps(pairs, PATTERNS)

    print(f"Found {len(gaps)} gapped pairs. Filling...")
    fixed = 0
    errors = []
    for g in gaps:
        try:
            src_text = open(g['src']).read()
        except Exception as e:
            errors.append((g['ms'], str(e)))
            continue
        topic_name = os.path.basename(g['src']).replace('.md', '')
        src_text_clean = strip_existing_frontmatter(src_text)
        fm = medsea_frontmatter(g['ms'], topic_name, g['src'])
        new_content = fm + src_text_clean
        try:
            with open(g['ms'], 'w') as f:
                f.write(new_content)
            fixed += 1
        except Exception as e:
            errors.append((g['ms'], str(e)))

    print(f"✓ Fixed {fixed} of {len(gaps)} gapped topics")
    if errors:
        print(f"  Errors: {len(errors)}")
        for path, err in errors[:5]:
            print(f"    {os.path.basename(path)}: {err}")
    return 0


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)

    cmd = sys.argv[1]
    src_folder = sys.argv[2]
    ms_chapter_dir = sys.argv[3] if len(sys.argv) > 3 else None

    if not os.path.isdir(src_folder):
        print(f"Source folder not found: {src_folder}")
        sys.exit(2)
    if cmd in ('fill', 'audit') and not ms_chapter_dir:
        print("audit/fill require MedSea chapter dir as 3rd argument")
        sys.exit(2)

    if cmd == 'audit':
        sys.exit(cmd_audit(src_folder, ms_chapter_dir))
    elif cmd == 'fill':
        sys.exit(cmd_fill(src_folder, ms_chapter_dir))
    else:
        print(f"Unknown command: {cmd}. Use 'audit' or 'fill'.")
        sys.exit(2)


if __name__ == '__main__':
    main()