#!/usr/bin/env python3
"""Compute no-model sector strength summaries for grouped crypto watchlists."""

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_DIR / 'templates'

from market_analyzer import build_watchlist_scan  # noqa: E402
from threshold_checker import load_watchlist  # noqa: E402

SECTORS = {
    'majors': TEMPLATES_DIR / 'watchlist-majors.yaml',
    'ai': TEMPLATES_DIR / 'watchlist-ai.yaml',
    'l1l2': TEMPLATES_DIR / 'watchlist-l1l2.yaml',
    'rwa': TEMPLATES_DIR / 'watchlist-rwa.yaml',
    'memes': TEMPLATES_DIR / 'watchlist-memes.yaml',
    'top50-trading': TEMPLATES_DIR / 'watchlist-top50-trading.yaml',
}

LABELS = {
    'majors': 'Majors',
    'ai': 'AI',
    'l1l2': 'L1/L2',
    'rwa': 'RWA',
    'memes': 'Memes',
    'top50-trading': 'Top 50 Trading',
}


def sector_snapshot(name: str, path: Path) -> Dict[str, Any]:
    entries = load_watchlist(str(path))
    scan = build_watchlist_scan(entries)
    rows = scan.get('all') or []
    moves = [float(x['move_24h_pct']) for x in rows if x.get('move_24h_pct') is not None]
    avg_move = round(sum(moves) / len(moves), 2) if moves else 0.0
    composite = round(scan.get('average_setup_score', 0.0) - 0.35 * scan.get('average_risk_score', 0.0) + 1.5 * avg_move, 2)
    leaders = [x.get('ticker') for x in (scan.get('top_opportunities') or [])[:3]]
    return {
        'sector_key': name,
        'sector': LABELS.get(name, name),
        'count': scan.get('count', 0),
        'average_setup_score': scan.get('average_setup_score', 0.0),
        'average_risk_score': scan.get('average_risk_score', 0.0),
        'average_move_24h_pct': avg_move,
        'market_regime': scan.get('market_regime', 'mixed'),
        'breadth': scan.get('breadth', {}),
        'leaders': leaders,
        'composite_score': composite,
    }


def build_summary(keys: List[str]) -> Dict[str, Any]:
    sectors = [sector_snapshot(k, SECTORS[k]) for k in keys if k in SECTORS]
    ranked = sorted(sectors, key=lambda x: (x['composite_score'], x['average_setup_score']), reverse=True)
    strongest = ranked[0] if ranked else None
    weakest = ranked[-1] if ranked else None
    return {
        'sectors': ranked,
        'strongest_sector': strongest,
        'weakest_sector': weakest,
        'generated_at': int(os.path.getmtime(__file__)),
    }


def format_text(data: Dict[str, Any]) -> str:
    lines = ['## Sector strength summary']
    strongest = data.get('strongest_sector')
    weakest = data.get('weakest_sector')
    if strongest:
        lines.append(f"Strongest: {strongest['sector']} | setup {strongest['average_setup_score']} | 24h {strongest['average_move_24h_pct']}%")
    if weakest:
        lines.append(f"Weakest: {weakest['sector']} | setup {weakest['average_setup_score']} | 24h {weakest['average_move_24h_pct']}%")
    lines.append('')
    for row in data.get('sectors', []):
        lines.append(f"- {row['sector']}: setup {row['average_setup_score']}, risk {row['average_risk_score']}, 24h {row['average_move_24h_pct']}%, regime {row['market_regime']}, leaders {', '.join(row['leaders']) if row['leaders'] else 'n/a'}")
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Compute sector strength summaries')
    parser.add_argument('--sector', action='append', help='One or more sector keys to include')
    parser.add_argument('--text', action='store_true', help='Print text summary instead of JSON')
    args = parser.parse_args()
    keys = args.sector or ['majors', 'ai', 'l1l2', 'rwa', 'memes']
    data = build_summary(keys)
    if args.text:
        print(format_text(data))
    else:
        print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
