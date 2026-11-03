#!/usr/bin/env python3
"""
Davidson Chapter Completeness Audit Script
==========================================

Run this BEFORE claiming any Davidson chapter is "fully complete".

It checks the actual filesystem state (which never lies) and produces a
report identifying:
  1. Topic files declared in MOC but missing from disk
  2. Topic files on disk with empty MCQ / SBA / Flashcard / Answer-Key sections
  3. Topic files with status: scaffold (rather than full-fcps-mrcp-topic-note)
  4. MOC tracker claims that don't match reality

Usage:
    python chapter-completeness-audit.py "/mnt/tb/Medicine/Acute Medicine and Critical Illness"

Returns exit code 0 if all topic files are FULLY complete, 1 if any gaps.
"""

import os
import re
import sys
from pathlib import Path


def audit_chapter(chapter_dir: str) -> dict:
    folder = Path(chapter_dir)
    if not folder.exists():
        print(f"ERROR: {chapter_dir} does not exist")
        sys.exit(2)

    md_files = sorted(folder.glob("*.md"))
    topic_files = [
        f for f in md_files
        if f.name != f"{folder.name} MOC.md"
        and not f.name.startswith("Davidson Chapter")
    ]

    report = {
        'folder': str(folder),
        'total_md': len(md_files),
        'topic_files': len(topic_files),
        'full_status': 0,
        'scaffold_status': 0,
        'partial_mcq_sba': [],
        'partial_flashcards': [],
        'missing_topics': [],
    }

    for f in topic_files:
        content = f.read_text(encoding='utf-8')

        if "status: full-fcps-mrcp-topic-note" in content:
            report['full_status'] += 1
        elif "status: scaffold" in content:
            report['scaffold_status'] += 1

        mcq_sec = re.search(r'## MCQs \((\d+)\)(.*?)(?=\n## |\Z)', content, re.DOTALL)
        if mcq_sec:
            body = mcq_sec.group(2)
            items = re.findall(r'^\s*(\d+)\.\s*(.+)', body, re.MULTILINE)
            filled = sum(1 for _, t in items if t.strip() and t.strip() != '.')
            if filled < 10:
                report['partial_mcq_sba'].append((f.name, filled, 'MCQ'))

        sba_sec = re.search(r'## SBA Questions \((\d+)\)(.*?)(?=\n## |\Z)', content, re.DOTALL)
        if sba_sec:
            body = sba_sec.group(2)
            items = re.findall(r'^\s*(\d+)\.\s*(.+)', body, re.MULTILINE)
            filled = sum(1 for _, t in items if t.strip() and t.strip() != '.')
            if filled < 10:
                report['partial_mcq_sba'].append((f.name, filled, 'SBA'))

        fc_sec = re.search(r'## Flashcards(.*?)(?=\n## |\Z)', content, re.DOTALL)
        if fc_sec:
            body = fc_sec.group(1) if fc_sec.lastindex == 1 else fc_sec.group(0)
            qs = re.findall(r'Q:\s*(.+)', body)
            filled = sum(1 for q in qs if q.strip() and q.strip() != ':')
            if filled < 5:
                report['partial_flashcards'].append((f.name, filled))

    moc_file = folder / f"{folder.name} MOC.md"
    if moc_file.exists():
        moc = moc_file.read_text(encoding='utf-8')
        claims = re.findall(r'\*\*Total\*\*\s*\|\s*\*?\*?(\d+)\s*/\s*(\d+)', moc)
        if claims:
            claimed_done, claimed_total = int(claims[0][0]), int(claims[0][1])
            report['moc_claim'] = f"{claimed_done}/{claimed_total}"
            if claimed_total > len(topic_files):
                report['missing_topics'] = claimed_total - len(topic_files)

    return report


def print_report(report: dict) -> int:
    print("=" * 80)
    print(f"CHAPTER COMPLETENESS AUDIT: {report['folder']}")
    print("=" * 80)
    print(f"Total .md files: {report['total_md']}")
    print(f"Topic files (excl. MOC + Hierarchy): {report['topic_files']}")
    print(f"  full-fcps-mrcp-topic-note: {report['full_status']}")
    print(f"  status: scaffold: {report['scaffold_status']}")
    print()

    if 'moc_claim' in report:
        print(f"MOC claims: {report['moc_claim']} done")
        if report['missing_topics'] > 0:
            print(f"  WARNING: {report['missing_topics']} topics declared in MOC but missing from disk")
        if report['full_status'] != report['topic_files']:
            print(f"  Reality: {report['full_status']}/{report['topic_files']} truly full")
        print()

    if report['partial_mcq_sba']:
        print("PARTIAL MCQ/SBA sections:")
        for fname, count, kind in report['partial_mcq_sba']:
            print(f"   {fname:<60} {kind}={count}/10")
        print()

    if report['partial_flashcards']:
        print("PARTIAL Flashcards:")
        for fname, count in report['partial_flashcards']:
            print(f"   {fname:<60} FC={count}")
        print()

    is_complete = (
        report['full_status'] == report['topic_files']
        and not report['partial_mcq_sba']
        and not report['partial_flashcards']
        and not report['missing_topics']
    )

    if is_complete:
        print("CHAPTER IS 100% COMPLETE")
        return 0
    else:
        print("CHAPTER HAS GAPS - see above")
        return 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: chapter-completeness-audit.py <chapter_directory>")
        sys.exit(2)
    report = audit_chapter(sys.argv[1])
    sys.exit(print_report(report))
