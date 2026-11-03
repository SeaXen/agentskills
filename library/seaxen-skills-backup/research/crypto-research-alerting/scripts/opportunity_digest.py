#!/usr/bin/env python3
"""Create a no-model text digest of top crypto opportunities."""

import argparse
import json
from pathlib import Path

from market_analyzer import build_watchlist_scan  # noqa: E402
from threshold_checker import load_watchlist  # noqa: E402

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_DIR / 'templates'
PRESETS = {
    'majors': TEMPLATES_DIR / 'watchlist-majors.yaml',
    'top50-trading': TEMPLATES_DIR / 'watchlist-top50-trading.yaml',
    'ai': TEMPLATES_DIR / 'watchlist-ai.yaml',
    'l1l2': TEMPLATES_DIR / 'watchlist-l1l2.yaml',
    'rwa': TEMPLATES_DIR / 'watchlist-rwa.yaml',
    'memes': TEMPLATES_DIR / 'watchlist-memes.yaml',
}


def build_digest(path: Path, top_n: int) -> dict:
    scan = build_watchlist_scan(load_watchlist(str(path)))
    return {
        'preset': path.stem,
        'market_regime': scan.get('market_regime', 'mixed'),
        'average_setup_score': scan.get('average_setup_score', 0.0),
        'average_risk_score': scan.get('average_risk_score', 0.0),
        'top_opportunities': (scan.get('top_opportunities') or [])[:top_n],
        'top_risks': (scan.get('top_risks') or [])[:top_n],
    }


def format_text(data: dict) -> str:
    lines = [f"## Top opportunities | {data['preset']}", f"Regime: {data['market_regime']} | avg setup {data['average_setup_score']} | avg risk {data['average_risk_score']}", '']
    lines.append('Top setups:')
    for i, item in enumerate(data.get('top_opportunities', []), start=1):
        lines.append(f"{i}. {item.get('ticker')} — setup {item.get('setup_score')} | risk {item.get('risk_score')} | 24h {item.get('move_24h_pct')}% | {', '.join(item.get('reasons') or [])}")
    lines.append('')
    lines.append('Main risks:')
    for i, item in enumerate(data.get('top_risks', []), start=1):
        lines.append(f"{i}. {item.get('ticker')} — risk {item.get('risk_score')} | setup {item.get('setup_score')} | {', '.join(item.get('risks') or [])}")
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Build top opportunity digest')
    parser.add_argument('--preset', default='top50-trading')
    parser.add_argument('--top', type=int, default=5)
    parser.add_argument('--text', action='store_true')
    args = parser.parse_args()
    path = PRESETS.get(args.preset)
    if not path:
        raise SystemExit(f'Unknown preset: {args.preset}')
    data = build_digest(path, args.top)
    print(format_text(data) if args.text else json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
