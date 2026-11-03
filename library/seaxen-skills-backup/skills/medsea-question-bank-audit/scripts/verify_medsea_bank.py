#!/usr/bin/env python3
"""MedSea question bank verifier — run after rebuild_question_bank_v5.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
# When run from skill copy: ASSETS may be wrong; allow env override
import os
if os.environ.get('MEDSEA_ASSETS'):
    ASSETS = Path(os.environ['MEDSEA_ASSETS'])


def main() -> int:
    errors: list[str] = []
    sba = json.loads((ASSETS / 'questions-sba.json').read_text())
    mcq = json.loads((ASSETS / 'questions-mcq.json').read_text())
    fc = json.loads((ASSETS / 'questions-flashcard.json').read_text())
    idx = json.loads((ASSETS / 'questions-index.json').read_text())
    VALID = set('ABCDEF')

    def check_choice(rows, kind):
        ids = []
        for r in rows:
            iid = r.get('id', '')
            if iid in ids:
                errors.append(f'{kind} duplicate id {iid}')
            ids.append(iid)
            ans = (r.get('answer') or '').strip().upper()
            opts = r.get('options') or {}
            if not ans and kind != 'flashcard':
                errors.append(f'{kind} {iid} missing answer')
            elif ans and ans not in opts:
                errors.append(f'{kind} {iid} answer {ans} not in options')
            if kind != 'flashcard':
                vals = [(opts[k] or '').strip() for k in opts if (opts[k] or '').strip()]
                if len(vals) != len(set(vals)):
                    errors.append(f'{kind} {iid} duplicate option text')

    check_choice(sba, 'sba')
    check_choice(mcq, 'mcq')
    for c in fc:
        if not (c.get('front') or '').strip() or not (c.get('back') or '').strip():
            errors.append(f'fc {c.get("id")} empty')

    for c in idx.get('chapters', []):
        n = c['num']
        cs = sum(1 for x in sba if x.get('chapter_num') == n)
        cm = sum(1 for x in mcq if x.get('chapter_num') == n)
        cf = sum(1 for x in fc if x.get('chapter_num') == n)
        if cs != c.get('sba_count') or cm != c.get('mcq_count') or cf != c.get('flashcard_count'):
            errors.append(f'index mismatch ch{n}')

    shard_dir = ASSETS / 'questions-by-chapter'
    if shard_dir.is_dir():
        for kind, rows in [('sba', sba), ('mcq', mcq), ('flashcard', fc)]:
            by = {}
            for r in rows:
                by.setdefault(r['chapter_num'], []).append(r)
            for num, chunk in by.items():
                p = shard_dir / f'{num}-{kind}.json'
                if not p.exists():
                    errors.append(f'missing shard {p.name}')
                else:
                    got = json.loads(p.read_text())
                    if len(got) != len(chunk):
                        errors.append(f'shard count {p.name} {len(got)} != {len(chunk)}')

    print(f'Bank: SBA {len(sba)} MCQ {len(mcq)} FC {len(fc)}')
    if errors:
        print(f'FAIL {len(errors)} issues:')
        for e in errors[:40]:
            print(' ', e)
        return 1
    print('PASS — structural checks OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())