#!/usr/bin/env python3
"""Recall stress test — runs real-session queries against /api/recall and
classifies misses as (a) real bug, (b) content gap, or (c) acceptable disagreement.

Usage:
    python3 recall_stress_test.py [--base http://localhost:6065] [--limit 25]

Requires no external deps. Reads expected mapping from a hardcoded list (see
`DEFAULT_EXPECTED` below) or from --expected <json_file>.

The test is intentionally hand-curated rather than auto-generated so the
expected canonicals reflect what a human thinks the right answer is for each
real query. This catches the gap where the recall engine returns "some
canonical" but not the "right" canonical for the user's actual intent.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from typing import Optional


DEFAULT_EXPECTED = {
    # decision
    "what did we decide about the dashboard": "decisions",
    "what convention did we pick for time format": "decisions",
    # fix
    "what was the FTS5 bug fix": "issues-fixes-log",
    "what was the last plugin fix": "issues-fixes-log",
    "Notion API gotcha for sub-pages": "issues-fixes-log",
    "what was the recall performance fix": "issues-fixes-log",
    # ops / setup
    "how my obsidian memory work": "Obsidian Vault Setup",
    "Telegram bot config": "Hermes Operations",
    "Discord channel list": "Hermes Operations",
    "MCP operations overview": "MCP Operations",
    "watchdog cron pattern": "Hermes Operations",
    "auto recall plugin trigger": "Obsidian Vault Setup",
    "Mnemosyne mirror every 6h": "Hermes Operations",
    "how to use the dashboard": "Dashboard",
    # ai providers
    "OpenRouter key fallback": "AI Providers & Models",
    "Bitwarden secrets manager": "AI Providers & Models",
    # medical / study
    "how to do FCPS preparation": "Medical Study System",
    "FCPS nephrology study plan": "Medical Study System",
    "study Davidson chapter 29": "Davidson 24e Study Workflow",
    "fcps/mrcp exam notes": "Medical Study System",
    "how to write a topic file": "Davidson 24e Study Workflow",
    # backup / DR
    "backup schedule for hermes": "Backup & Disaster Recovery",
    "how to restore from DR": "Backup & Disaster Recovery",
    # meta
    "memory architecture of the system": "Memory System Architecture",
    "WordPress publish workflow": "mdsagar.com Content Pipeline",
}


# Classify misses. A miss is (c) acceptable if BOTH top-1 AND expected are
# defensible answers to the query. Add your own acceptable pairs here as
# the system grows — these are the cases where two canonicals legitimately
# overlap (e.g. "FCPS exam notes" could reasonably be Davidson 24e OR
# Medical Study System).
ACCEPTABLE_ALTS = {
    "fcps/mrcp exam notes": ["Medical Study System", "Davidson 24e Study Workflow"],
    "WordPress publish workflow": ["mdsagar.com Content Pipeline", "Academic Assignment Workflow"],
    "Mnemosyne mirror every 6h": ["Hermes Operations", "Mnemosyne Mirror", "Mnemosyne Triples"],
    "auto recall plugin trigger": ["Obsidian Vault Setup", "Hermes Operations"],
    "what is the daily note format": ["AGENT", "issues-fixes-log"],  # AGENT.md lacks a format section yet
    "how my obsidian memory work": ["Obsidian Vault Setup", "Hermes Operations", "Memory System Architecture"],
    "Bitwarden secrets manager": ["AI Providers & Models", "Hermes Operations"],
    "how to use the dashboard": ["Dashboard", "Obsidian Vault Setup", "Hermes Operations"],
}


def _title_match(top: str, expected: str) -> bool:
    """Loose match — 'Hermes Operations' matches 'Hermes Operations.md'."""
    top_l = top.lower().strip().rstrip(".md")
    exp_l = expected.lower().strip().rstrip(".md")
    return exp_l in top_l or top_l in exp_l


def classify_miss(query: str, expected: str, top_title: str) -> str:
    """Returns 'A' (real bug), 'B' (content gap), or 'C' (acceptable disagreement)."""
    alts = ACCEPTABLE_ALTS.get(query, [expected])
    if top_title in alts:
        return "C"
    # Heuristic: if the top-1 is a strong canonical AND the expected canonical
    # is a more specific one, this is a content gap on the specific canonical.
    # (A "real bug" requires the expected canonical to exist and have the
    # answer, but the boost isn't routing there.)
    return "A"


def run_stress_test(base: str, expected: dict[str, str], limit: int = 3) -> dict:
    correct = 0
    misses_by_kind: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    per_query_results: dict[str, list[dict]] = {}

    for q, exp in expected.items():
        url = f"{base}/api/recall?query={urllib.parse.quote(q)}&limit={limit}"
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                d = json.load(r)
        except Exception as exc:
            misses_by_kind["A"].append((q, exp, f"ERROR: {exc}"))
            continue

        results = d.get("results", [])
        per_query_results[q] = results[:limit]
        if not results:
            misses_by_kind["A"].append((q, exp, "(no results)"))
            continue

        top = results[0].get("title", "")
        if _title_match(top, exp):
            correct += 1
        else:
            kind = classify_miss(q, exp, top)
            misses_by_kind[kind].append((q, exp, top))

    n = len(expected)
    return {
        "correct": correct,
        "total": n,
        "miss_rate": round((n - correct) / n, 3) if n else 0,
        "by_kind": {k: list(v) for k, v in misses_by_kind.items()},
        "per_query": per_query_results,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--base", default="http://localhost:6065")
    p.add_argument("--expected", help="JSON file with {query: expected_canonical} mapping")
    p.add_argument("--limit", type=int, default=3, help="results to fetch per query")
    p.add_argument("--json", action="store_true", help="emit JSON instead of human report")
    args = p.parse_args()

    expected = DEFAULT_EXPECTED
    if args.expected:
        with open(args.expected) as f:
            expected = json.load(f)

    r = run_stress_test(args.base, expected, limit=args.limit)

    if args.json:
        print(json.dumps(r, indent=2))
        return 0

    # Human report
    print(f"\n=== Recall stress test ===")
    print(f"Base: {args.base}")
    print(f"Correct: {r['correct']}/{r['total']}  miss rate: {r['miss_rate']*100:.1f}%\n")

    for kind, label in [("A", "real bug — fix boost"),
                        ("B", "content gap — write content"),
                        ("C", "acceptable disagreement — leave alone")]:
        items = r["by_kind"].get(kind, [])
        if not items:
            continue
        print(f"\n[{kind}] {label} ({len(items)}):")
        for q, exp, got in items:
            print(f"  - '{q[:55]}'")
            print(f"      expected: {exp}")
            print(f"      got:      {got}")

    return 0 if r["miss_rate"] < 0.3 else 1


if __name__ == "__main__":
    sys.exit(main())
