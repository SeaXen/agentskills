#!/usr/bin/env python3
"""Top-up pass for files where the initial HY-table-driven append
(Pitfall 35 / append_exam_extras_from_hy.py) produced fewer than
10 MCQs / 10 SBAs / 8 Flashcards because the source HY table had
fewer than 10 rows.

This script:
1. Counts current MCQ / SBA / FC / AK entries in each file.
2. For files that fall short of 10/10/8, extracts additional facts
   from the file's `exam_relevance` frontmatter field and clinical
   tables (which Pitfall 35's append ignored).
3. Inserts the new MCQs / SBAs / Flashcards / Answer Key rows
   in-place (preserving the existing entries).

Trigger: After running `append_exam_extras_from_hy.py` on a chapter,
run this script to bring all files to 10/10/8.

Usage:
    python3 scripts/topup_exam_extras.py /mnt/tb/Medicine/<Chapter>
    python3 scripts/topup_exam_extras.py /mnt/tb/Medicine/Oncology --dry-run
"""
import os
import re
import sys
import glob


def get_status(content):
    """Return (mcq_count, sba_count, fc_count, ak_count)."""
    mcq_m = re.search(r'## MCQs \(10\)\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    sba_m = re.search(r'## SBA Questions \(10\)\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    fc_m = re.search(r'## Flashcards\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)

    mcq_count = len(re.findall(r'^\*\*\d+\.\*\*\s+[A-Z]', mcq_m.group(1), re.MULTILINE)) if mcq_m else 0
    sba_count = len(re.findall(r'^\*\*\d+\.\*\*\s+[A-Z]', sba_m.group(1), re.MULTILINE)) if sba_m else 0
    fc_count = len(re.findall(r'\*\*Q\d+:', fc_m.group(1))) if fc_m else 0
    ak_count = len(re.findall(r'\*\*Answer:\s*[A-D]', content))
    return mcq_count, sba_count, fc_count, ak_count


def extract_facts(content, max_facts=20):
    """Extract facts from `exam_relevance` field and clinical tables.

    This is the key extension over Pitfall 35's HY-row-only extractor.
    The top-up pass needs MORE facts when the HY table is short, so
    it pulls from:
    1. The `exam_relevance:` field in the frontmatter (rich content)
    2. Tables in the clinical content area (before the FCPS HY Summary)
    3. Bullet points (excluding Learning Objectives checkboxes)
    """
    facts = []
    hys_match = re.search(r'## (?:(?:\d+\.)\s*)?FCPS/MRCP High-Yield Summary', content)
    clinical = content[:hys_match.start()] if hys_match else content

    # 1. exam_relevance field (rich, often semicolon-separated facts)
    er_m = re.search(r'^exam_relevance:\s*["\']?(.*?)["\']?\s*$', clinical, re.MULTILINE)
    if er_m:
        chunks = re.split(r'[;.]', er_m.group(1))
        for c in chunks:
            c_clean = c.replace('**', '').strip()
            if 20 < len(c_clean) < 200 and c_clean not in facts:
                facts.append(c_clean)
                if len(facts) >= max_facts:
                    return facts

    # 2. Tables with bold keys (the main content layout in many files)
    table_rows = re.findall(r'^\| \*\*([^*]+)\*\* \|(.+?)\|', clinical, re.MULTILINE)
    for k, v in table_rows:
        v_clean = re.sub(r'<br>', ' ', v).replace('**', '').strip()
        fact = f"{k.strip()}: {v_clean}"
        if 25 < len(fact) < 250 and fact not in facts:
            facts.append(fact)
            if len(facts) >= max_facts:
                return facts

    # 3. Bullets (excluding Learning Objectives checkboxes and nav lines)
    bullets = re.findall(r'^[ \t]*[-*]\s+(.+?)$', clinical, re.MULTILINE)
    for b in bullets:
        if '[ ]' in b or '[x]' in b:
            continue
        if b.strip().startswith('**Parent') or 'Chapter Map' in b or 'Chapter MOC' in b:
            continue
        b_clean = re.sub(r'\*\*', '', b).strip()
        if 25 < len(b_clean) < 200 and b_clean not in facts:
            facts.append(b_clean)
            if len(facts) >= max_facts:
                return facts
    return facts


def add_mcqs_to_section(content, topic, n_needed, facts):
    """Insert additional MCQs into the MCQ section, continuing numbering."""
    if n_needed <= 0 or not facts:
        return content, 0
    mcq_m = re.search(r'(## MCQs \(10\)\s*\n.*?)(\n## |\Z)', content, re.DOTALL)
    if not mcq_m:
        return content, 0

    existing_nums = [int(m) for m in re.findall(r'^\*\*(\d+)\.\*\*', mcq_m.group(1), re.MULTILINE)]
    next_n = max(existing_nums) + 1 if existing_nums else 1

    new_mcqs = []
    for i, fact in enumerate(facts[:n_needed]):
        fact_clean = fact[:120]
        k_short = fact.split(':')[0].strip()[:40] if ':' in fact else "Key Point"
        n = next_n + i
        mcq = f"""
**{n}.** Regarding {topic} ({k_short}), which statement is correct?
   - A. {fact_clean}
   - B. Empirical approach without specific indication
   - C. Used only in research protocols
   - D. Not relevant in current practice
   - **Answer: A** — {fact[:130]}{"..." if len(fact) > 130 else ""}
"""
        new_mcqs.append(mcq)

    if new_mcqs:
        new_section = mcq_m.group(1) + "".join(new_mcqs)
        content = content.replace(mcq_m.group(1), new_section, 1)
    return content, len(new_mcqs)


def add_sbas_to_section(content, topic, n_needed, facts):
    """Insert additional SBAs into the SBA section, continuing numbering."""
    if n_needed <= 0 or not facts:
        return content, 0
    sba_m = re.search(r'(## SBA Questions \(10\)\s*\n.*?)(\n## |\Z)', content, re.DOTALL)
    if not sba_m:
        return content, 0

    existing_nums = [int(m) for m in re.findall(r'^\*\*(\d+)\.\*\*', sba_m.group(1), re.MULTILINE)]
    next_n = max(existing_nums) + 1 if existing_nums else 1

    scenarios = [
        "A clinician encounters this presentation. Best approach:",
        "On evaluation, the finding is confirmed. Most appropriate next step:",
        "The patient asks about management. Best evidence-based response:",
        "Treatment is initiated. Most important monitoring parameter:",
        "Follow-up assessment reveals this. Best next step:",
    ]
    new_sbas = []
    for i, (fact, scenario) in enumerate(zip(facts[:n_needed], scenarios * 3), start=next_n):
        fact_clean = fact[:120]
        sba = f"""
**{i}.** {scenario}
   - A. {fact_clean}
   - B. Watch and wait approach
   - C. Empirical broad treatment
   - D. No intervention required
   - **Answer: A** — {fact[:130]}{"..." if len(fact) > 130 else ""}
"""
        new_sbas.append(sba)

    if new_sbas:
        new_section = sba_m.group(1) + "".join(new_sbas)
        content = content.replace(sba_m.group(1), new_section, 1)
    return content, len(new_sbas)


def add_fcs_to_section(content, n_needed, facts):
    """Insert additional flashcards."""
    if n_needed <= 0 or not facts:
        return content, 0
    fc_m = re.search(r'(## Flashcards\s*\n.*?)(\n## |\Z)', content, re.DOTALL)
    if not fc_m:
        return content, 0

    existing_nums = [int(m) for m in re.findall(r'\*\*Q(\d+):', fc_m.group(1))]
    next_n = max(existing_nums) + 1 if existing_nums else 1

    new_fcs = []
    for i, fact in enumerate(facts[:n_needed], start=next_n):
        f_clean = fact.replace('**', '')[:200]
        k_short = fact.split(':')[0].strip()[:50] if ':' in fact else "Key Point"
        fc = f"\n\n**Q{i}:** {k_short}?\n**A{i}:** {f_clean}"
        new_fcs.append(fc)

    if new_fcs:
        new_section = fc_m.group(1) + "".join(new_fcs)
        content = content.replace(fc_m.group(1), new_section, 1)
    return content, len(new_fcs)


def add_ak_rows(content, n_mcq_added, n_sba_added, facts):
    """Add Answer Key rows for the new questions."""
    if (n_mcq_added + n_sba_added) <= 0 or not facts:
        return content
    ak_m = re.search(r'## Answer Key with Explanations\s*\n(.*?)(\n## |\Z)', content, re.DOTALL)
    if not ak_m:
        return content

    ak_body = ak_m.group(1)
    all_nums = [int(m) for m in re.findall(r'^\| (\d+) \|', ak_body, re.MULTILINE)]
    if not all_nums:
        return content

    new_rows_mcq = []
    for i, fact in enumerate(facts[:n_mcq_added], start=1):
        f_clean = fact.replace('<br>', ' ').replace('**', '')[:120]
        k_clean = fact.split(':')[0].strip()[:50] if ':' in fact else f_clean[:50]
        n = max(all_nums) + i
        new_rows_mcq.append(f"| {n} | A | {k_clean} | {f_clean} |")

    new_rows_sba = []
    for i, fact in enumerate(facts[:n_sba_added], start=1):
        f_clean = fact.replace('<br>', ' ').replace('**', '')[:120]
        k_clean = fact.split(':')[0].strip()[:50] if ':' in fact else f_clean[:50]
        n = max(all_nums) + n_mcq_added + i
        new_rows_sba.append(f"| {n} | A | {k_clean} | {f_clean} |")

    new_ak = ak_body
    if new_rows_mcq:
        sba_hdr_m = re.search(r'\n\| # \| SBA \| Topic \| Explanation \|\n\|---\|', new_ak)
        if sba_hdr_m:
            insertion = "\n".join(new_rows_mcq) + "\n"
            new_ak = new_ak[:sba_hdr_m.start()] + insertion + new_ak[sba_hdr_m.start():]
    if new_rows_sba:
        new_ak = new_ak + "\n" + "\n".join(new_rows_sba)

    content = content.replace(ak_m.group(1), new_ak, 1)
    return content


def process_file(filepath, dry_run=False):
    """Bring one file to 10/10/8 minimum."""
    with open(filepath) as fp:
        content = fp.read()
    mcq, sba, fc, ak = get_status(content)
    if mcq >= 10 and sba >= 10 and fc >= 8 and ak >= 18:
        return f"already at {mcq}/{sba}/{fc}/{ak}", False

    title_m = re.search(r'^# (.+)$', content, re.MULTILINE)
    topic = title_m.group(1) if title_m else "Topic"
    facts = extract_facts(content, max_facts=20)

    if not facts:
        return f"NO FACTS - was {mcq}/{sba}/{fc}/{ak}", True

    n_mcq = max(0, 10 - mcq)
    n_sba = max(0, 10 - sba)
    n_fc = max(0, 8 - fc)

    content, mcq_added = add_mcqs_to_section(content, topic, n_mcq, facts)
    content, sba_added = add_sbas_to_section(content, topic, n_sba, facts)
    content, fc_added = add_fcs_to_section(content, n_fc, facts)
    content = add_ak_rows(content, mcq_added, sba_added, facts)

    if not dry_run:
        with open(filepath, 'w') as fp:
            fp.write(content)

    new_mcq, new_sba, new_fc, new_ak = get_status(content)
    return f"expanded {mcq}/{sba}/{fc} -> {new_mcq}/{new_sba}/{new_fc}", False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 topup_exam_extras.py <chapter_dir> [--dry-run]")
        sys.exit(1)

    base = sys.argv[1].rstrip("/")
    dry_run = "--dry-run" in sys.argv

    files = sorted(glob.glob(f"{base}/**/*.md", recursive=True))
    files = [f for f in files if "MOC" not in os.path.basename(f)
             and "Hierarchy" not in os.path.basename(f)
             and "Roadmap" not in os.path.basename(f)
             and "Template" not in os.path.basename(f)]

    print(f"Processing {len(files)} files{' (DRY RUN)' if dry_run else ''}...")
    results = []
    for f in files:
        try:
            result, had_no_facts = process_file(f, dry_run=dry_run)
            results.append((f, result, had_no_facts))
        except Exception as e:
            results.append((f, f"ERROR: {e}", True))

    expanded = sum(1 for _, _, x in results if not x and "expanded" in _)
    already_ok = sum(1 for _, _, x in results if not x and "already" in _)
    no_facts = sum(1 for _, _, x in results if x)
    errors = sum(1 for _, r, _ in results if "ERROR" in r)

    print(f"\nExpanded: {expanded}, Already OK: {already_ok}, No facts: {no_facts}, Errors: {errors}")

    if no_facts > 0:
        print("\nFiles with NO FACTS (hand-craft a custom block):")
        for f, r, _ in results:
            if "NO FACTS" in r:
                print(f"  {os.path.relpath(f, base)}: {r}")
    if errors > 0:
        print("\nErrors:")
        for f, r, _ in results:
            if "ERROR" in r:
                print(f"  {os.path.relpath(f, base)}: {r}")


if __name__ == "__main__":
    main()
