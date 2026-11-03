"""Topic parser — flexible state machine for MCQ/SBA/Flashcard extraction.

Pure functions only. NO main code (no print, no file I/O at module level) so this
module can be safely imported for testing without side-effects. The orchestrator
extract_questions.py imports `parse_topic` and walks the site/ tree.

Validated against MedSea topic.md format variations (2026-06-21):
  Format A: 1. **stem with no closing **
  Format B: 1. **Q:** stem (closing ** right after Q:)
  Format C: - Q: ... / - **Q:** ... (flashcard variations)
"""
import re, hashlib


def parse_topic(text, chapter_num, chapter_name, chapter_slug, topic_slug):
    """Parse a single topic.md file. Returns (mcqs, sbas, flashes) lists."""
    mcqs = []; sbas = []; flashes = []
    section = None
    cur_q = None
    expecting_options = False
    cur_flash = None

    def push_q(kind):
        nonlocal cur_q, expecting_options
        if cur_q and cur_q.get('stem') and cur_q.get('answer') and cur_q.get('options'):
            if cur_q['answer'] in cur_q['options']:
                qid = hashlib.md5(
                    f"{kind}|{chapter_num}|{topic_slug}|{cur_q['stem'][:80]}".encode()
                ).hexdigest()[:12]
                item = {
                    'id': qid, 'chapter_num': chapter_num, 'chapter_name': chapter_name,
                    'chapter_slug': chapter_slug, 'topic_slug': topic_slug,
                    'question': cur_q['stem'].strip(),
                    'options': cur_q['options'], 'answer': cur_q['answer'],
                }
                if kind == 'mcq': mcqs.append(item)
                else: sbas.append(item)
        cur_q = None; expecting_options = False

    def flush_flash():
        nonlocal cur_flash
        if cur_flash and cur_flash.get('front') and cur_flash.get('back'):
            qid = hashlib.md5(
                f"fc|{chapter_num}|{topic_slug}|{cur_flash['front'][:80]}".encode()
            ).hexdigest()[:12]
            flashes.append({
                'id': qid, 'chapter_num': chapter_num, 'chapter_name': chapter_name,
                'chapter_slug': chapter_slug, 'topic_slug': topic_slug,
                'front': cur_flash['front'].strip(),
                'back': cur_flash['back'].strip(),
            })
        cur_flash = None

    NUM_RE = re.compile(r'^\s*(\d+)\.\s+(.+?)\s*$')
    OPT_RE = re.compile(r'^\s*([A-E])\.\s+(.+?)\s*$')
    # Match: *Answer: X* / **Answer: X** / Answer: X (case-insensitive)
    ANS_RE = re.compile(r'^\s*\**\s*Answer\s*:?\s*\**\s*([A-E])\s*\**\s*$', re.IGNORECASE)

    def extract_stem(line):
        """Pull stem out of various bold formats (A, B, C above)."""
        s = line.strip()
        m = re.match(r'^\d+\.\s+(.*)$', s)
        if not m: return None
        rest = m.group(1).strip()
        if rest.startswith('**'):
            inner = rest[2:]
            if inner.startswith('**'):
                return inner.rstrip(':').rstrip('*').strip()
            qm = re.match(
                r'^(Q|Question)\s*:\s*\**\s*(.*?)\**\s*$', inner, re.IGNORECASE
            )
            if qm: return qm.group(2).strip()
            return inner.rstrip(':').rstrip('*').strip()
        return rest

    for line in text.splitlines():
        # Section detect — only ## level (not ### )
        if line.startswith('## ') and not line.startswith('### '):
            if section in ('mcq', 'sba'):
                push_q(section)
            elif section == 'flash':
                flush_flash()
            h = line[3:].strip().lower()
            if h.startswith('mcq'):
                section = 'mcq'
            elif 'sba' in h:
                section = 'sba'
            elif 'flashcard' in h:
                section = 'flash'
            else:
                section = None
            continue

        if section in ('mcq', 'sba'):
            stripped = line.rstrip()
            # If currently parsing options, try option/answer/blank
            if expecting_options and cur_q:
                m = OPT_RE.match(stripped)
                if m:
                    cur_q['options'][m.group(1)] = m.group(2)
                    continue
                m = ANS_RE.match(stripped)
                if m:
                    cur_q['answer'] = m.group(1).upper()
                    expecting_options = False
                    continue
                if stripped == '':
                    expecting_options = False
                    continue
                # Non-blank non-option non-answer: end current Q, treat as content
                expecting_options = False

            # Try new numbered question (only when not currently parsing options)
            if not expecting_options:
                if re.match(r'^\s*\d+\.\s+', stripped):
                    stem = extract_stem(stripped)
                    if stem and len(stem) > 5:
                        push_q(section)
                        cur_q = {'stem': stem, 'options': {}, 'answer': None}
                        expecting_options = True
                        continue

        elif section == 'flash':
            stripped = line.rstrip()
            # Format A: "- Q: ...\n  A: ..."
            m = re.match(r'^\s*-\s+Q:\s*(.+)$', stripped)
            if m:
                flush_flash()
                cur_flash = {'front': m.group(1).strip(), 'back': None}
                continue
            m = re.match(r'^\s*A:\s*(.+)$', stripped)
            if m and cur_flash:
                cur_flash['back'] = m.group(1).strip()
                continue
            # Format B: "**Q:** ...\n**A:** ..."
            m = re.match(r'^\s*\*\*Q:\*\*\s*(.+)$', stripped)
            if m:
                flush_flash()
                cur_flash = {'front': m.group(1).strip(), 'back': None}
                continue
            m = re.match(r'^\s*\*\*A:\*\*\s*(.+)$', stripped)
            if m and cur_flash:
                cur_flash['back'] = m.group(1).strip()
                continue
            # Format C: "- **Q:** ..." (dash + bold Q)
            m = re.match(r'^\s*-\s+\*\*Q:\*\*\s*(.+)$', stripped)
            if m:
                flush_flash()
                cur_flash = {'front': m.group(1).strip(), 'back': None}
                continue

    if section in ('mcq', 'sba'):
        push_q(section)
    if section == 'flash':
        flush_flash()
    return mcqs, sbas, flashes
