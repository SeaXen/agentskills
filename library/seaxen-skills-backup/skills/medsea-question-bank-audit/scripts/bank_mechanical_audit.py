#!/usr/bin/env python3
"""Mechanical quality gates for MedSea questions-*.json (no clinical re-read)."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

VALID = set("ABCDEF")


def load_assets(assets_dir: Path):
    def j(name):
        with open(assets_dir / f"questions-{name}.json", encoding="utf-8") as f:
            return json.load(f)

    return j("sba"), j("mcq"), j("flashcard"), j("index")


def audit_choice(it: dict) -> list[str]:
    p: list[str] = []
    stem = (it.get("question") or "").strip()
    opts = it.get("options") or {}
    ans = (it.get("answer") or "").strip().upper()
    if not isinstance(opts, dict):
        return ["options_not_dict"]
    if not stem:
        p.append("empty_stem")
    if len(opts) < 4:
        p.append(f"opts_lt4:{len(opts)}")
    letters = sorted(opts.keys())
    for L in letters:
        if L not in VALID:
            p.append(f"bad_letter:{L}")
        if not (opts.get(L) or "").strip():
            p.append(f"empty_opt_{L}")
    vals = [(opts[k] or "").strip() for k in letters if (opts.get(k) or "").strip()]
    if len(vals) != len(set(vals)):
        p.append("duplicate_options")
    if not ans:
        p.append("missing_answer")
    elif ans not in opts:
        p.append(f"answer_not_in_opts:{ans}")
    return p


def audit_fc(c: dict) -> list[str]:
    p: list[str] = []
    f, b = (c.get("front") or "").strip(), (c.get("back") or "").strip()
    if not f or not b:
        p.append("empty")
    if "|" in f or "|" in b:
        p.append("pipe")
    if "[[" in f or "[[" in b:
        p.append("wikilink")
    if re.match(r"^\s*Flashcard\s+\d+\s+question", f, re.I):
        p.append("placeholder")
    if len(f.split()) < 3:
        p.append("short_front")
    if len(b.split()) < 2:
        p.append("short_back")
    if not c.get("chapter_num"):
        p.append("no_chapter")
    return p


def main() -> int:
    root = Path(__file__).resolve().parents
    # site/assets when script lives under MedSea site/scripts; skill copy: pass ASSETS=...
    assets = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    if not (assets / "questions-sba.json").exists():
        # try MedSea default
        guess = Path("/mnt/tb/Sea-knowledge/#MedSea/site/assets")
        if (guess / "questions-sba.json").exists():
            assets = guess
        else:
            print("Usage: bank_mechanical_audit.py [path/to/site/assets]", file=sys.stderr)
            return 2

    sba, mcq, fc, idx = load_assets(assets)
    fail = 0

    for kind, rows in (("sba", sba), ("mcq", mcq)):
        bad = sum(1 for r in rows if audit_choice(r))
        dup = len(rows) - len({r.get("id") for r in rows})
        e_ans = sum(1 for r in rows if (r.get("answer") or "").upper() == "E")
        print(f"{kind}: n={len(rows)} structural_bad={bad} dup_ids={dup} answer_E={e_ans}")
        if bad or dup:
            fail += 1

    fc_bad = sum(1 for c in fc if audit_fc(c))
    fc_dup = len(fc) - len({c.get("id") for c in fc})
    print(f"flashcard: n={len(fc)} bad={fc_bad} dup_ids={fc_dup}")
    if fc_bad or fc_dup:
        fail += 1

    drift = 0
    for ch in idx.get("chapters", []):
        n = ch["num"]
        cs = sum(1 for x in sba if x.get("chapter_num") == n)
        cm = sum(1 for x in mcq if x.get("chapter_num") == n)
        cf = sum(1 for x in fc if x.get("chapter_num") == n)
        if cs != ch.get("sba_count") or cm != ch.get("mcq_count") or cf != ch.get("flashcard_count"):
            drift += 1
    print(f"index_chapter_drift: {drift}")
    print(f"index_totals: {idx.get('totals')}")
    if drift:
        fail += 1

    print("RESULT:", "PASS" if fail == 0 else "FAIL")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())