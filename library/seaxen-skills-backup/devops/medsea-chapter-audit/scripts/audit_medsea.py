#!/usr/bin/env python3
"""
MedSea chapter completeness audit.

Run with:
    python3 audit_medsea.py [chapter_num ...]

If no args, audits all 32 chapters. Outputs a table per chapter with:
- Atomic topic count (all 3 formats)
- Total word count
- MOC + Hierarchy overview presence (both naming variants)
- Git HEAD commit covering the chapter

Exit code 0 if all chapters report 100% complete with MOC + Hier, else 1.

NOTE: this only checks LOCAL + GIT. For Notion sync verification, see
references/notion-chapter-discovery.md and the /tmp/sync_ch*.py scripts.
"""
import os
import re
import subprocess
import sys

MEDSEA = '/mnt/tb/Sea-knowledge/#MedSea'
MED = '/mnt/tb/Medicine'

# Davidson 25th ed chapter → (MedSea chapter slug, source folder name)
CH_MAP = {
    1: ('1-clinical-decision-making', 'Clinical Decision-Making'),
    2: ('2-clinical-therapeutics', 'Clinical Therapeutics and Good Prescribing'),
    3: ('3-clinical-genetics', 'Clinical Genetics'),
    4: ('4-clinical-immunology', 'Clinical Immunology'),
    5: ('5-nutritional-factors', 'Nutritional Factors in Disease'),
    6: ('6-population-health', 'Population Health and Epidemiology'),
    7: ('7-principles-of-infection', 'Principles of Infectious Disease'),
    8: ('8-oncology', 'Oncology'),
    9: ('9-palliative-care', 'Pain and Palliative Care'),
    10: ('10-acute-medicine', 'Acute Medicine and Critical Illness'),
    11: ('11-poisoning', 'Poisoning'),
    12: ('12-envenomation', 'Envenomation'),
    13: ('13-austere-medicine', 'Medicine in Austere Environments'),
    14: ('14-infectious-disease', 'Infectious Disease'),
    15: ('15-sexually-transmitted-infections', 'Sexually Transmitted Infections'),
    16: ('16-cardiology', 'Cardiology'),
    17: ('17-respiratory-medicine', 'Respiratory'),
    18: ('18-nephrology-urology', 'Nephrology and Urology'),
    19: ('19-clinical-biochemistry-and-metabolic-medi', 'Clinical Biochemistry and Metabolic Medicine'),
    20: ('20-endocrinology', 'Endocrinology'),
    21: ('21-diabetes-mellitus', 'Diabetes'),
    22: ('22-gastroenterology', 'Gastroenterology'),
    23: ('23-hepatology', 'Hepatology'),
    24: ('24-haematology-and-transfusion-medicine', 'Hematology'),
    25: ('25-rheumatology-and-bone-disease', 'Rheumatology'),
    26: ('26-dermatology', 'Dermatology'),
    27: ('27-neurology-and-stroke-medicine', 'Neurology'),
    28: ('28-medical-ophthalmology', 'Medical Ophthalmology'),
    29: ('29-medical-psychiatry', 'Medical Psychiatry'),
    30: ('30-maternal-medicine', 'Maternal Medicine'),
    31: ('31-adolescence-transition-and-young-adult-m', 'Adolescent and Transition Medicine'),
    32: ('32-older-adult-medicine-and-frailty', 'Ageing and Disease'),
}


def count_atomic(ch_dir):
    """Count atomic topics supporting all 3 MedSea formats."""
    n = 0
    if not os.path.isdir(ch_dir):
        return 0
    for entry in os.listdir(ch_dir):
        full = os.path.join(ch_dir, entry)
        if os.path.isdir(full):
            if os.path.exists(os.path.join(full, 'topic.md')):
                n += 1  # Format B
            elif any(f.endswith('.md') and f != 'topic.md' for f in os.listdir(full)):
                n += 1  # Format C
        elif entry.endswith('.md') and not entry.startswith('.'):
            n += 1  # Format A
    return n


def total_words(ch_dir):
    """Sum word counts across all atomic topic files."""
    total = 0
    if not os.path.isdir(ch_dir):
        return 0
    for entry in os.listdir(ch_dir):
        full = os.path.join(ch_dir, entry)
        md = None
        if os.path.isdir(full):
            md = os.path.join(full, 'topic.md')
            if not os.path.exists(md):
                for sub in os.listdir(full):
                    if sub.endswith('.md') and sub != 'topic.md':
                        md = os.path.join(full, sub)
                        break
        elif entry.endswith('.md'):
            md = full
        if md and os.path.exists(md):
            with open(md) as f:
                total += len(f.read().split())
    return total


def has_moc_hier(ch_dir, ch_num):
    """Check both naming variants for MOC + Hierarchy overviews."""
    candidates_moc = [f'{ch_num}.0.900-moc', f'{ch_num}.0.900-chapter-moc']
    candidates_hier = [f'{ch_num}.0.901-hierarchy', f'{ch_num}.0.901-chapter-hierarchy']
    has_moc = any(os.path.exists(os.path.join(ch_dir, c, 'topic.md')) for c in candidates_moc)
    has_hier = any(os.path.exists(os.path.join(ch_dir, c, 'topic.md')) for c in candidates_hier)
    return has_moc, has_hier


def chapter_git_commit(ch_dir):
    """Get HEAD commit hash affecting this chapter."""
    r = subprocess.run(
        ['git', '-C', MEDSEA, 'log', '-1', '--format=%h', '--', ch_dir],
        capture_output=True, text=True,
    )
    return r.stdout.strip() or '—'


def audit_chapter(ch_num):
    ch_slug, src_name = CH_MAP[ch_num]
    ch_dir = f'{MEDSEA}/chapters/{ch_slug}/diseases'
    src_dir = f'{MED}/{src_name}'

    atomic = count_atomic(ch_dir)
    words = total_words(ch_dir)
    has_moc, has_hier = has_moc_hier(ch_dir, ch_num)
    commit = chapter_git_commit(f'chapters/{ch_slug}')

    src_count = 0
    if os.path.isdir(src_dir):
        src_count = sum(1 for r, d, fs in os.walk(src_dir)
                        for f in fs if f.endswith('.md'))

    return {
        'ch': ch_num,
        'slug': ch_slug,
        'atomic': atomic,
        'words': words,
        'src_count': src_count,
        'has_moc': has_moc,
        'has_hier': has_hier,
        'commit': commit,
    }


def main():
    chapters = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else list(CH_MAP.keys())
    chapters = [c for c in chapters if c in CH_MAP]

    print(f"{'Ch':<4} {'Atomic':<8} {'Words':<10} {'Src':<6} "
          f"{'MOC':<4} {'Hier':<5} {'Git':<10}")
    print("-" * 60)

    incomplete = []
    for ch in chapters:
        r = audit_chapter(ch)
        print(f"{r['ch']:<4} {r['atomic']:<8} {r['words']:<10} {r['src_count']:<6} "
              f"{'Y' if r['has_moc'] else 'N':<4} {'Y' if r['has_hier'] else 'N':<5} "
              f"{r['commit']:<10}")
        if not (r['has_moc'] and r['has_hier']):
            incomplete.append(r['ch'])

    print()
    if incomplete:
        print(f"❌ Incomplete chapters (missing MOC or Hier): {incomplete}")
        sys.exit(1)
    else:
        print(f"✓ All {len(chapters)} chapters have MOC + Hierarchy.")
        sys.exit(0)


if __name__ == '__main__':
    main()