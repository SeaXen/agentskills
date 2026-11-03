#!/usr/bin/env python3
"""
Davidson Chapter Audit — Content-Depth Verifier (Round 2)
=========================================================

Class-level tool for any Davidson chapter under /mnt/tb/Medicine/.

Why this exists (Med Oph Ch 27 lessons, 2026-06-17):

**Round 1 (duplicate-scaffold trap):**
A previous audit of Medical Ophthalmology reported 8/93 mnemonics and 0/93
mind maps "real" — but the actual file content was 100% real. Root cause:
each topic file had BOTH a real topic-specific section in the middle
(e.g. `## 14. Mnemonics`, `## 15. Mind Map`) AND a duplicate generic
scaffold at the END (`## Mnemonics` containing "CRITICAL FEATURES /
FIRST-LINE TREATMENT / RED FLAGS" placeholder text). The audit regex
matched the LAST occurrence, so it kept finding the scaffold and
reporting the real content as missing. Fix: audit the FIRST occurrence.

**Round 2 (metadata-only audit trap):**
After round 1 cleanup, the chapter was declared "100% complete ✅" because
all files had `status: full-fcps-mrcp-note` and `## MCQs (10)` headings.
But 6 systemic-disease files had `## MCQs (1)` and `## SBA Questions (0)`
— section-PRESENCE check passed but section-CONTENT was deficient.
A status check caught 0 of 6 deficient files. A heading check caught
0 of 6. **A content check (count items inside the section) catches 6 of 6.**

This script does both: audits the FIRST occurrence AND counts the
items inside each required section. It is the canonical verifier for
"is this chapter done?" — if it reports 0 ✗ lines, the chapter is done.

Usage:
    python3 chapter_audit.py /path/to/chapter
    python3 chapter_audit.py "/mnt/tb/Medicine/Medical Ophthalmology"

Exit code: 0 if all topic files pass, 1 if any fail (CI-friendly).
"""

import os
import re
import sys
import json

# Generic-scaffold fingerprint that was accidentally appended to topic files
# during batch generation. If we find this block, the file still has duplicate
# junk that needs cleaning.
SCAFFOLD_FINGERPRINT = re.compile(
    r'CRITICAL FEATURES.*?FIRST-LINE TREATMENT.*?RED FLAGS',
    re.S,
)

# MCQ/SBA section regex tolerates numbered (## 18. MCQs) AND unnumbered
# (## MCQs) headings. Both formats are in the Med Oph chapter.
MCQ_SECTION_RE = r'^##\s+(?:\d+\.\s+)?MCQs?\b'
SBA_SECTION_RE = r'^##\s+(?:\d+\.\s+)?SBA\b'

# Item-counting pattern. The Med Oph chapter uses TWO formats for questions:
#   Format A (most common):  1. **Question:** ...
#   Format B (some new files): **1.** Question: ...
# We try BOTH and take the max. Falls back to counting Answer: markers if
# neither pattern matches but the section exists.
ITEM_PATTERN_A = r'^\d+\.\s+\*\*'
ITEM_PATTERN_B = r'^\*\*\d+\.\s+'
ANSWER_MARKER = r'(?m)^\s*\*\*Answer:\s'

# Section pattern + minimum count required to consider the section "complete"
SECTION_DEFINITIONS = {
    'learning_objectives': (r'^##\s+Learning Objectives', 'presence'),
    'mnemonics':           (r'^##\s+(?:\d+\.\s+)?Mnemonics\b', 'mnemonics'),
    'mind_map':            (r'^##\s+(?:\d+\.\s+)?Mind Map\b', 'mind_map'),
    'mcqs':                (MCQ_SECTION_RE, 'mcq'),
    'sbas':                (SBA_SECTION_RE, 'sba'),
    'viva':                (r'^##.*Viva', 'presence'),
    'spaced_repetition':   (r'Spaced Repetition', 'presence'),
    'self_test':           (r'Self-Test', 'presence'),
    'tags':                (r'^#+\s+\d*\.?\s*Tags\s*$', 'presence'),
}

# Minimum thresholds
MIN_MNEMONICS = 2
MIN_MINDMAP_LINES = 8
MIN_MCQS = 10
MIN_SBAS = 10


def first_section_block(content, section_regex):
    """Return the content of the FIRST matching section, or None.

    Uses a bounded-block approach: find section start, then find the
    next level-2 heading, and slice the bounded region. This is more
    reliable than a `.*?(?=^##\s|\Z)` regex when the section has level-3
    headings inside it.
    """
    m = re.search(rf'{section_regex}.*$', content, re.M)
    if not m:
        return None
    start = m.start()
    # Find next level-2 heading after this section (skipping the section's own heading line)
    rest = content[start + 5:]
    next_m = re.search(r'^##\s+', rest, re.M)
    end = start + 5 + next_m.start() if next_m else len(content)
    return content[start:end]


def count_items(block):
    """Count numbered items in a section block. Tries both formats; falls
    back to counting Answer: markers (FCPS/MRCP style)."""
    if not block:
        return 0
    count_a = len(re.findall(ITEM_PATTERN_A, block, re.M))
    count_b = len(re.findall(ITEM_PATTERN_B, block, re.M))
    answer_count = len(re.findall(ANSWER_MARKER, block))
    return max(count_a, count_b, answer_count)


def count_mnemonics(block):
    """Count real topic-specific mnemonics. Returns (count, is_scaffold)."""
    if not block:
        return 0, False
    numbered = len(re.findall(r'^\s*\d+\.\s+\*\*', block, re.M))
    bulleted = len(re.findall(r'^\s*-\s+\*\*', block, re.M))
    total = numbered + bulleted
    is_scaffold = bool(re.search(
        r'(?i)CRITICAL FEATURES|FIRST-LINE TREATMENT|RED FLAGS|placeholder|TBD|TODO',
        block,
    ))
    return total, is_scaffold


def count_mind_map_lines(block):
    """Count non-empty lines in the first mermaid block. Returns (lines, has_mermaid)."""
    if not block or '```mermaid' not in block:
        return 0, False
    m = re.search(r'```mermaid(.*?)```', block, re.S)
    if not m:
        return 0, False
    return len([l for l in m.group(1).splitlines() if l.strip()]), True


def audit_file(path):
    """Return a dict describing one file's section compliance."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    line_count = len(content.splitlines())

    status = 'unknown'
    for line in content.splitlines()[:30]:
        m = re.match(r'^status:\s*(\S+)', line)
        if m:
            status = m.group(1)
            break

    result = {
        'path': path,
        'name': os.path.basename(path),
        'lines': line_count,
        'status': status,
    }

    for key, (pat, kind) in SECTION_DEFINITIONS.items():
        if kind == 'presence':
            # Simple regex on whole content
            result[f'{key}_present'] = bool(re.search(pat, content, re.M))
        else:
            block = first_section_block(content, pat)
            if kind == 'mnemonics':
                count, is_scaffold = count_mnemonics(block)
                result[f'{key}_count'] = count
                result[f'{key}_scaffold'] = is_scaffold
                result[f'{key}_present'] = block is not None and count >= MIN_MNEMONICS and not is_scaffold
            elif kind == 'mind_map':
                mm_lines, has_mermaid = count_mind_map_lines(block)
                result[f'{key}_lines'] = mm_lines
                result[f'{key}_has_mermaid'] = has_mermaid
                result[f'{key}_present'] = has_mermaid and mm_lines >= MIN_MINDMAP_LINES
            elif kind == 'mcq':
                count = count_items(block)
                result[f'{key}_count'] = count
                result[f'{key}_present'] = block is not None and count >= MIN_MCQS
            elif kind == 'sba':
                count = count_items(block)
                result[f'{key}_count'] = count
                result[f'{key}_present'] = block is not None and count >= MIN_SBAS
            else:
                result[f'{key}_present'] = block is not None and len(block.strip()) > 0

    result['has_trailing_scaffold'] = bool(SCAFFOLD_FINGERPRINT.search(content))
    return result


def r_compliant(r):
    """A topic file is compliant iff every required section is present
    with at least its minimum threshold AND no trailing duplicate scaffold."""
    return (
        r['learning_objectives_present']
        and r['mnemonics_present']
        and r['mind_map_present']
        and r['mcqs_present']
        and r['sbas_present']
        and r['viva_present']
        and r['spaced_repetition_present']
        and r['self_test_present']
        and r['tags_present']
        and not r['has_trailing_scaffold']
    )


def main():
    if len(sys.argv) < 2:
        print('Usage: chapter_audit.py <chapter_dir> [--json]')
        sys.exit(2)

    chapter = sys.argv[1]
    if not os.path.isdir(chapter):
        print(f'Not a directory: {chapter}')
        sys.exit(2)

    all_md = []
    for root, _, files in os.walk(chapter):
        for f in files:
            if f.endswith('.md'):
                all_md.append(os.path.join(root, f))

    def is_topic(p):
        base = os.path.basename(p)
        return (
            'Hub' not in base
            and 'Hierarchy' not in base
            and 'MOC' not in base
            and 'Template' not in base
            and 'Roadmap' not in base
        )

    topics = sorted(p for p in all_md if is_topic(p))

    print(f'=== Davidson Chapter Audit (Content-Depth Verifier, Round 2) ===')
    print(f'Chapter: {chapter}')
    print(f'Topic files: {len(topics)}\n')

    results = [audit_file(p) for p in topics]

    # Per-file table — show lines, MCQ, SBA, MM, MN, LO, scaffold status
    print(f"{'LINES':>5}  {'MCQ':>4}  {'SBA':>4}  {'MN':>3}  {'MM':>3}  {'LO':>3}  {'SCAFF':>5}  NAME")
    print('-' * 95)
    for r in sorted(
        results,
        key=lambda x: (not r_compliant(x), x['has_trailing_scaffold'], -x['lines']),
    ):
        mcq = f"{r['mcqs_count']:>3}{'+' if r['mcqs_present'] else '✗'}"
        sba = f"{r['sbas_count']:>3}{'+' if r['sbas_present'] else '✗'}"
        mn = f"{r['mnemonics_count']:>2}{'+' if r['mnemonics_present'] else '✗'}"
        mm = f"{r['mind_map_lines']:>2}{'+' if r['mind_map_present'] else '✗'}"
        lo = '+' if r['learning_objectives_present'] else '✗'
        sc = 'YES' if r['has_trailing_scaffold'] else 'no'
        print(f"{r['lines']:>5}  {mcq:>4}  {sba:>4}  {mn:>3}  {mm:>3}  {lo:>3}  {sc:>5}  {r['name']}")

    n = len(results)
    print()
    print('=== AGGREGATE ===')
    for key in ['learning_objectives', 'mnemonics', 'mind_map', 'mcqs', 'sbas',
                'viva', 'spaced_repetition', 'self_test', 'tags']:
        ok = sum(1 for r in results if r[f'{key}_present'])
        marker = '✅' if ok == n else '✗'
        print(f'  {key:<25} {ok:>3}/{n}  {marker}')
    scaffold_count = sum(1 for r in results if r['has_trailing_scaffold'])
    marker = '✅' if scaffold_count == 0 else '✗'
    print(f'  {"trailing_scaffold_clean":<25} {scaffold_count:>3}/{n}  {marker}')

    failing = [r for r in results if not r_compliant(r)]
    if failing:
        print()
        print(f'=== {len(failing)} FILES NEEDING FIX ===')
        for r in failing:
            missing = []
            if not r['learning_objectives_present']: missing.append('LO')
            if not r['mnemonics_present']: missing.append(f'MN={r["mnemonics_count"]}')
            if not r['mind_map_present']: missing.append(f'MM={r["mind_map_lines"]}')
            if not r['mcqs_present']: missing.append(f'MCQ={r["mcqs_count"]}')
            if not r['sbas_present']: missing.append(f'SBA={r["sbas_count"]}')
            if not r['viva_present']: missing.append('Viva')
            if not r['spaced_repetition_present']: missing.append('SR')
            if not r['self_test_present']: missing.append('Self-Test')
            if not r['tags_present']: missing.append('Tags')
            if r['has_trailing_scaffold']: missing.append('SCAFFOLD')
            print(f"  ✗ {r['name']}: {', '.join(missing)}")

    if '--json' in sys.argv:
        out = [{k: v for k, v in r.items() if k != 'path'} for r in results]
        print()
        print(json.dumps(out, indent=2))

    all_pass = all(r_compliant(r) for r in results)
    sys.exit(0 if all_pass else 1)


if __name__ == '__main__':
    main()
