#!/usr/bin/env python3
"""Rebuild the MCQ / SBA / Flashcard bank from authored chapters.

Reads from chapters/<chapter>/.../*.md (ALL markdown files in each
chapter tree, not just topic.md), parses five known authoring formats,
applies strict quality filters, and emits the four JSON files consumed
by the live site:

  - questions-index.json
  - questions-mcq.json
  - questions-sba.json
  - questions-flashcard.json

Supported formats per question block:
  1. Legacy bold-stem:        1. **stem** + A./B./C. + **B. correct**
  2. Plain-stem + Answer:     1. **stem** + A./B./C. + *Answer: B* line
  3. Inline Options/Answer:   1. **Question:** stem + **Options:** A. opt B. opt ... + **Answer:** B
  4. Bullet-list options:     1. plain stem + - A) opt / - B) opt + **Answer: B** — explanation
  5. Factoid (flashcard):     1. **Answer term** — Topic/Question:     (rescued as flashcard)

Blocks with stem + 4+ options but no answer key are also rescued as
flashcards via the parse_mcq_as_factoid_block fallback.

Run from /mnt/tb/Sea-knowledge/#MedSea. Prints per-chapter bank
breakdown and quality stats after each run.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path('/mnt/tb/Sea-knowledge/#MedSea')
CHAPTERS_ROOT = ROOT / 'chapters'
SITE = ROOT / 'site' / 'assets'

# ---------------------------------------------------------------------------
# Regex
# ---------------------------------------------------------------------------

NUM_BLOCK_RE = re.compile(r'(?m)^(?=\d+\.\s+)')
TAG_RE = re.compile(r'<[^>]+>')
INLINE_OPT_RE = re.compile(r'\b([A-E])\.\s+([^\nA-E]+?)(?=\s+[A-E]\.\s+|\s*$)', re.S)
LEGACY_OPT_RE = re.compile(r'^\s*([A-E])\.\s*(.+?)\s*$')
BULLET_OPT_RE = re.compile(r'^\s*[-*]\s*([A-E])[.)]\s*(.+?)\s*$')
ANSWER_LINE_RE = re.compile(r'\*{1,2}Answer:\s*([A-E])\*{1,2}', re.I)
ANSWER_INLINE_RE = re.compile(r'^\*\*([A-E])\.\s+', re.I)


def strip_md(s: str) -> str:
    if not s:
        return ''
    s = html.unescape(s)
    s = TAG_RE.sub('', s)
    s = s.replace('**', '').replace('__', '').replace('`', '')
    s = re.sub(r'\[(.*?)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def extract_section(md: str, header: str) -> str:
    """Capture text from `## <Header>` (optionally numbered and with a count
    suffix like `## 18. MCQs (10)`) up to the next H2."""
    pat = re.compile(
        rf'^##\s+(?:\d+\.\s+)?{re.escape(header)}(?:\s*\([^)]*\))?\s*$(.*?)(?=^## |\Z)',
        re.S | re.M,
    )
    m = pat.search(md)
    return m.group(1).strip() if m else ''


def parse_factoid_block(block: str) -> dict | None:
    """Format: 1. **Answer term** — Topic/Question:

    Authored factoids sometimes placed under ## MCQs / ## SBA Questions
    in chapters that haven't yet been written as full MCQs. Routed to
    the flashcard bank.
    """
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    if not lines:
        return None
    m = re.match(r'^\d+\.\s+\*\*(.+?)\*\*\s*[—\-:]\s*(.+?)\s*:?\s*$', lines[0])
    if not m:
        return None
    answer = strip_md(m.group(1))
    question = strip_md(m.group(2))
    if len(answer.split()) < 1 or len(question.split()) < 2:
        return None
    q = question if question.endswith('?') else f'{question}?'
    return {'q': q, 'a': answer}


def parse_mcq_as_factoid_block(block: str) -> dict | None:
    """Recover MCQ blocks that have stem + 4–5 options but NO answer key.

    Routes them to the flashcard bank as a Q/A pair where the question
    is the stem and the answer is the first option.
    """
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    if not lines:
        return None
    m0 = re.match(r'^(\d+)\.\s+\*\*(.+?)\*\*\s*:?\s*$', lines[0])
    if not m0:
        return None
    stem = strip_md(m0.group(2))
    options = []
    for ln in lines[1:8]:
        mm = LEGACY_OPT_RE.match(ln)
        if mm:
            options.append(strip_md(mm.group(2)))
    if len(options) < 4:
        return None
    if len(stem.split()) < 2:
        return None
    q = stem if stem.endswith('?') else f'{stem}?'
    return {'q': q, 'a': options[0]}


def parse_legacy_block(block: str) -> dict | None:
    """Format: 1. **stem**   then A. opt / B. opt / ...  with **B. correct**."""
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    m0 = re.match(r'^(\d+)\.\s+\*\*(.+?)\*\*\s*$', lines[0])
    if not m0:
        return None
    stem = strip_md(m0.group(2))
    options: dict[str, str] = {}
    answer: str | None = None
    for ln in lines[1:]:
        m = LEGACY_OPT_RE.match(ln)
        if not m:
            continue
        label, raw = m.group(1), m.group(2)
        is_bold = raw.lstrip().startswith('**') and raw.rstrip().endswith('**')
        text = strip_md(raw)
        options[label] = text
        if is_bold and not answer:
            answer = label
    if not answer:
        for ln in lines[1:]:
            if re.match(r'^\s*\*\*[A-E]\.\s+', ln) or re.match(r'^\s*[A-E]\.\s*\*\*', ln):
                m2 = re.search(r'^\s*([A-E])\.', ln)
                if m2:
                    answer = m2.group(1)
                    break
    return {'stem': stem, 'options': options, 'answer': answer}


def parse_plain_stem_block(block: str) -> dict | None:
    """Format: 1. plain stem (no bold) then A. opt / B. opt / ... / E. opt
    with the correct answer rendered as **B. text** or in a trailing
    `**Answer: B**` / `*Answer: B*` line."""
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    m0 = re.match(r'^(\d+)\.\s+(.+)$', lines[0])
    if not m0:
        return None
    if len(lines) < 2:
        return None
    first_opt = LEGACY_OPT_RE.match(lines[1])
    if not first_opt:
        return None
    stem = strip_md(m0.group(2))
    options: dict[str, str] = {}
    answer: str | None = None
    for ln in lines[1:]:
        m = LEGACY_OPT_RE.match(ln)
        if not m:
            if 'Answer:' in ln:
                am = re.search(r'Answer:\s*([A-E])', ln, re.I)
                if am and not answer:
                    answer = am.group(1).upper()
            continue
        label, raw = m.group(1), m.group(2)
        is_bold = raw.lstrip().startswith('**')
        text = strip_md(raw)
        options[label] = text
        if is_bold and not answer:
            answer = label
    return {'stem': stem, 'options': options, 'answer': answer}


def parse_inline_block(block: str) -> dict | None:
    """Format: 1. **Question:** stem  then **Options:** A. opt B. opt ... **Answer:** B."""
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    m0 = re.match(r'^(\d+)\.\s+\*\*Question:\*\*\s*(.+)$', lines[0])
    if not m0:
        return None
    stem = strip_md(m0.group(2))
    options: dict[str, str] = {}
    answer: str | None = None
    options_text = ''
    for ln in lines[1:]:
        stripped = ln.lstrip()
        if stripped.startswith('**Options:**'):
            options_text += ' ' + stripped[len('**Options:**'):].strip()
        elif options_text:
            options_text += ' ' + stripped.strip()
        if stripped.startswith('**Answer:**'):
            m = re.match(r'\*\*Answer:\*\*\s*([A-E])', stripped)
            if m:
                answer = m.group(1)
            break
    if options_text:
        segments = re.split(r'\s+(?=[A-E]\.\s)', options_text)
        for seg in segments:
            m = re.match(r'([A-E])\.\s+(.+)$', seg.strip(), re.S)
            if m:
                options[m.group(1)] = strip_md(m.group(2))
    return {'stem': stem, 'options': options, 'answer': answer}


def parse_bullet_block(block: str) -> dict | None:
    """Format: 1. plain stem then - A) opt / - B) opt ... **Answer: B** — ..."""
    lines = [ln.rstrip() for ln in block.splitlines() if ln.strip()]
    m0 = re.match(r'^(\d+)\.\s+(.+)$', lines[0])
    if not m0:
        return None
    stem_raw = m0.group(2)
    has_bullet = any(BULLET_OPT_RE.match(ln) for ln in lines[1:5])
    if not has_bullet:
        return None
    stem = strip_md(stem_raw)
    options: dict[str, str] = {}
    answer: str | None = None
    for ln in lines[1:]:
        m = BULLET_OPT_RE.match(ln)
        if m:
            options[m.group(1)] = strip_md(m.group(2))
            continue
        am = ANSWER_LINE_RE.search(ln)
        if am and not answer:
            answer = am.group(1).upper()
    return {'stem': stem, 'options': options, 'answer': answer}


# ---------------------------------------------------------------------------
# Quality filters
# ---------------------------------------------------------------------------

CONTEXTLESS_STEMS = {
    'what is the first-line treatment?',
    'what is the most important complication?',
    'what is the diagnosis?',
    'what is the treatment?',
    'what is the best investigation?',
}


def is_contextless(stem: str) -> bool:
    s = stem.strip().lower()
    return s in CONTEXTLESS_STEMS


def quality_ok(item: dict, *, need_options: int, min_stem_words: int,
               need_scenario: bool) -> bool:
    if not item:
        return False
    stem = item.get('stem', '').strip()
    opts = item.get('options') or {}
    ans = item.get('answer')
    if len(opts) < need_options:
        return False
    if not ans or ans not in opts:
        return False
    if len(stem.split()) < min_stem_words:
        return False
    if is_contextless(stem):
        return False
    if need_scenario and len(stem.split()) < 12:
        return False
    return True


# ---------------------------------------------------------------------------
# Flashcards
# ---------------------------------------------------------------------------

def normalize_fc_front(q: str) -> str:
    q = re.sub(r'^Q:\s*', '', q, flags=re.I).strip()
    q = q.replace('**', '').strip()
    if q.endswith('?'):
        return q
    low = q.lower()
    plurals = (
        'criteria', 'features', 'signs', 'symptoms', 'causes', 'complications',
        'indications', 'contraindications', 'drugs', 'steps', 'stages', 'types',
        'findings', 'risk factors', 'principles', 'uses', 'options',
    )
    if low.endswith(' list'):
        base = q[:-5].strip()
        return f'What are the {base}?' if base else 'What are the key items?'
    if any(low.endswith(x) for x in plurals):
        return f'What are the {q}?'
    if low.startswith(('how ', 'why ', 'when ', 'which ', 'what ', 'name ', 'list ', 'define ', 'describe ')):
        return q if q.endswith('?') else q + '?'
    return f'What is {q}?'


FC_RE = re.compile(r'(?ms)^[-*]\s*Q:\s*(.+?)\n\s*A:\s*(.+?)(?=^[-*]\s*Q:|\Z)')


def parse_flashcards(section: str) -> list[dict]:
    if not section.strip():
        return []
    out: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for q, a in FC_RE.findall(section):
        q2 = normalize_fc_front(strip_md(q))
        a2 = strip_md(a)
        if len(q2.split()) < 3 or len(a2.split()) < 2:
            continue
        key = (q2.lower(), a2.lower())
        if key in seen:
            continue
        seen.add(key)
        out.append({'q': q2, 'a': a2})
    return out


# ---------------------------------------------------------------------------
# Chapter detection
# ---------------------------------------------------------------------------

def chapter_from_path(p: Path) -> tuple[int, str, str] | None:
    """Return (chapter_num, chapter_name, chapter_slug) from path."""
    parts = p.parts
    try:
        i = parts.index('chapters')
    except ValueError:
        return None
    if i + 1 >= len(parts):
        return None
    ch_dir = parts[i + 1]
    m = re.match(r'^(\d{1,2})-(.+)$', ch_dir)
    if not m:
        return None
    return int(m.group(1)), m.group(2), ch_dir


def chapter_label(num: int, slug: str) -> str:
    pretty = slug.split('-', 1)[1].replace('-', ' ').title() if '-' in slug else slug
    return f'Ch {num}: {pretty}'


def topic_label_from_path(p: Path, ch_slug: str) -> tuple[str, str]:
    parts = p.parts
    try:
        i = parts.index(ch_slug)
    except ValueError:
        i = -1
    sub = None
    if i >= 0 and i + 1 < len(parts):
        sub = parts[i + 1] if not parts[i + 1].endswith('.md') else None
    stem = p.stem
    pretty = re.sub(r'^\d+(?:\.\d+)*-', '', stem)
    pretty = pretty.replace('-', ' ').strip().title() or stem
    topic_slug = re.sub(r'[^a-z0-9]+', '-', stem.lower()).strip('-')
    return topic_slug, pretty


def qid(prefix: str, ch: int, topic: str, idx: int, body: str) -> str:
    return hashlib.sha1(f'{prefix}|{ch}|{topic}|{idx}|{body}'.encode('utf-8')).hexdigest()[:12]


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build() -> tuple[list, list, list, dict]:
    mcq_rows: list[dict] = []
    sba_rows: list[dict] = []
    flash_rows: list[dict] = []
    chapter_counts: dict[int, dict] = {}

    files = sorted(CHAPTERS_ROOT.rglob('*.md'))
    print(f'Scanning {len(files)} markdown files under chapters/')

    for md_path in files:
        if md_path.parent == CHAPTERS_ROOT:
            continue
        try:
            text = md_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        if not any(h in text for h in ('## MCQs', '## SBA Questions', '## Flashcards')):
            continue
        chinfo = chapter_from_path(md_path)
        if not chinfo:
            continue
        ch_num, ch_slug_short, ch_dirname = chinfo
        ch_label = chapter_label(ch_num, ch_dirname)
        topic_slug, topic_title = topic_label_from_path(md_path, ch_dirname)
        counts = chapter_counts.setdefault(ch_num, {
            'num': ch_num, 'name': ch_label, 'slug': ch_dirname,
            'mcq_count': 0, 'sba_count': 0, 'flashcard_count': 0,
        })

        # MCQs
        mcq_sec = extract_section(text, 'MCQs')
        if mcq_sec:
            blocks = re.split(NUM_BLOCK_RE, mcq_sec.strip())
            for b in blocks:
                b = b.strip()
                if not re.match(r'^\d+\.\s+', b):
                    continue
                best = None
                for parser in (parse_legacy_block, parse_plain_stem_block,
                               parse_inline_block, parse_bullet_block):
                    item = parser(b)
                    if item is None or not item.get('stem'):
                        continue
                    if item.get('answer') and item.get('answer') in (item.get('options') or {}):
                        best = item
                        break
                    if best is None:
                        best = item
                if best is not None:
                    if not best.get('answer') and len(best.get('options') or {}) >= 4:
                        fact = parse_mcq_as_factoid_block(b) or {
                            'q': best['stem'] if best['stem'].endswith('?') else f"{best['stem']}?",
                            'a': next(iter(best['options'].values()), ''),
                        }
                        if fact.get('q') and fact.get('a'):
                            flash_rows.append({
                                'id': qid('fc', ch_num, topic_slug,
                                          len(flash_rows) + 1, fact['q']),
                                'chapter_num': ch_num,
                                'chapter_name': ch_label,
                                'chapter_slug': ch_dirname,
                                'topic_slug': topic_slug,
                                'topic_title': topic_title,
                                'front': fact['q'],
                                'back': fact['a'],
                                'source': 'authored-factoid',
                            })
                            counts['flashcard_count'] += 1
                    elif quality_ok(best, need_options=4, min_stem_words=5,
                                    need_scenario=False):
                        mcq_rows.append({
                            'id': qid('mcq', ch_num, topic_slug,
                                      len(mcq_rows) + 1, best['stem']),
                            'chapter_num': ch_num,
                            'chapter_name': ch_label,
                            'chapter_slug': ch_dirname,
                            'topic_slug': topic_slug,
                            'topic_title': topic_title,
                            'question': best['stem'],
                            'options': best['options'],
                            'answer': best['answer'],
                            'source': 'authored',
                        })
                        counts['mcq_count'] += 1
                    continue
                fact = parse_factoid_block(b) or parse_mcq_as_factoid_block(b)
                if fact is not None and fact.get('q') and fact.get('a'):
                    flash_rows.append({
                        'id': qid('fc', ch_num, topic_slug,
                                  len(flash_rows) + 1, fact['q']),
                        'chapter_num': ch_num,
                        'chapter_name': ch_label,
                        'chapter_slug': ch_dirname,
                        'topic_slug': topic_slug,
                        'topic_title': topic_title,
                        'front': fact['q'],
                        'back': fact['a'],
                        'source': 'authored-factoid',
                    })
                    counts['flashcard_count'] += 1

        # SBAs
        sba_sec = extract_section(text, 'SBA Questions')
        if sba_sec:
            blocks = re.split(NUM_BLOCK_RE, sba_sec.strip())
            for b in blocks:
                b = b.strip()
                if not re.match(r'^\d+\.\s+', b):
                    continue
                best = None
                for parser in (parse_legacy_block, parse_plain_stem_block,
                               parse_inline_block, parse_bullet_block):
                    item = parser(b)
                    if item is None or not item.get('stem'):
                        continue
                    if item.get('answer') and item.get('answer') in (item.get('options') or {}):
                        best = item
                        break
                    if best is None:
                        best = item
                if best is not None:
                    if not best.get('answer') and len(best.get('options') or {}) >= 4:
                        fact = parse_mcq_as_factoid_block(b) or {
                            'q': best['stem'] if best['stem'].endswith('?') else f"{best['stem']}?",
                            'a': next(iter(best['options'].values()), ''),
                        }
                        if fact.get('q') and fact.get('a'):
                            flash_rows.append({
                                'id': qid('fc', ch_num, topic_slug,
                                          len(flash_rows) + 1, fact['q']),
                                'chapter_num': ch_num,
                                'chapter_name': ch_label,
                                'chapter_slug': ch_dirname,
                                'topic_slug': topic_slug,
                                'topic_title': topic_title,
                                'front': fact['q'],
                                'back': fact['a'],
                                'source': 'authored-factoid',
                            })
                            counts['flashcard_count'] += 1
                    elif quality_ok(best, need_options=4, min_stem_words=10,
                                    need_scenario=True):
                        sba_rows.append({
                            'id': qid('sba', ch_num, topic_slug,
                                      len(sba_rows) + 1, best['stem']),
                            'chapter_num': ch_num,
                            'chapter_name': ch_label,
                            'chapter_slug': ch_dirname,
                            'topic_slug': topic_slug,
                            'topic_title': topic_title,
                            'question': best['stem'],
                            'options': best['options'],
                            'answer': best['answer'],
                            'source': 'authored',
                        })
                        counts['sba_count'] += 1
                    continue
                fact = parse_factoid_block(b)
                if fact is not None and fact.get('q') and fact.get('a'):
                    flash_rows.append({
                        'id': qid('fc', ch_num, topic_slug,
                                  len(flash_rows) + 1, fact['q']),
                        'chapter_num': ch_num,
                        'chapter_name': ch_label,
                        'chapter_slug': ch_dirname,
                        'topic_slug': topic_slug,
                        'topic_title': topic_title,
                        'front': fact['q'],
                        'back': fact['a'],
                        'source': 'authored-factoid',
                    })
                    counts['flashcard_count'] += 1

        # Flashcards (real, authored)
        fc_sec = extract_section(text, 'Flashcards')
        if fc_sec:
            for i, c in enumerate(parse_flashcards(fc_sec), 1):
                flash_rows.append({
                    'id': qid('fc', ch_num, topic_slug, i, c['q']),
                    'chapter_num': ch_num,
                    'chapter_name': ch_label,
                    'chapter_slug': ch_dirname,
                    'topic_slug': topic_slug,
                    'topic_title': topic_title,
                    'front': c['q'],
                    'back': c['a'],
                    'source': 'authored',
                })
                counts['flashcard_count'] += 1

    index = {
        'version': 5,
        'generated_from': 'authored chapters/*.md (all formats, all files)',
        'totals': {
            'mcq': len(mcq_rows),
            'sba': len(sba_rows),
            'flashcard': len(flash_rows),
            'chapters': sum(1 for c in chapter_counts.values()
                            if (c['mcq_count'] + c['sba_count'] + c['flashcard_count']) > 0),
        },
        'chapters': [chapter_counts[k] for k in sorted(chapter_counts)
                     if (chapter_counts[k]['mcq_count']
                         + chapter_counts[k]['sba_count']
                         + chapter_counts[k]['flashcard_count']) > 0],
    }
    return mcq_rows, sba_rows, flash_rows, index


def main() -> None:
    mcq, sba, flash, index = build()

    print('\nPer-chapter bank after strict filter:')
    print(f"{'#':>3} {'slug':<48} {'MCQ':>6} {'SBA':>6} {'FC':>6}")
    for c in index['chapters']:
        print(f"{c['num']:>3} {c['slug'][:48]:<48} {c['mcq_count']:>6} {c['sba_count']:>6} {c['flashcard_count']:>6}")
    print()
    print('Totals:', json.dumps(index['totals'], indent=2))

    def stats(rows, kind):
        one_opt = sum(1 for r in rows if len(r.get('options') or {}) == 1)
        no_ans = sum(1 for r in rows if not r.get('answer'))
        if kind == 'flashcard':
            no_q = sum(1 for r in rows if '?' not in r.get('front',''))
            short = sum(1 for r in rows if len((r.get('front') or '').split()) < 3)
            return {'one_option': one_opt, 'missing_answer': no_ans,
                    'no_question_mark': no_q, 'short_front': short}
        return {'one_option': one_opt, 'missing_answer': no_ans}
    print('\nQuality stats:')
    print('  MCQ      :', stats(mcq, 'mcq'))
    print('  SBA      :', stats(sba, 'sba'))
    print('  Flashcard:', stats(flash, 'flashcard'))

    (SITE / 'questions-mcq.json').write_text(
        json.dumps(mcq, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-sba.json').write_text(
        json.dumps(sba, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-flashcard.json').write_text(
        json.dumps(flash, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (SITE / 'questions-index.json').write_text(
        json.dumps(index, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print('\nWrote: questions-index.json, questions-mcq.json, questions-sba.json, questions-flashcard.json')


if __name__ == '__main__':
    main()
