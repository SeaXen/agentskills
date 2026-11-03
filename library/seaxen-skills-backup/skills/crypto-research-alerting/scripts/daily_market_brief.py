#!/usr/bin/env python3
"""Generate a no-model daily market brief from existing watchlists and scores."""

import argparse
import json
from pathlib import Path

from market_analyzer import build_watchlist_scan  # noqa: E402
from threshold_checker import load_watchlist  # noqa: E402
from sector_strength import build_summary as build_sector_summary  # noqa: E402

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATES_DIR = SKILL_DIR / 'templates'
PRESETS = {
    'majors': TEMPLATES_DIR / 'watchlist-majors.yaml',
    'top50-trading': TEMPLATES_DIR / 'watchlist-top50-trading.yaml',
    'ai': TEMPLATES_DIR / 'watchlist-ai.yaml',
    'l1l2': TEMPLATES_DIR / 'watchlist-l1l2.yaml',
    'rwa': TEMPLATES_DIR / 'watchlist-rwa.yaml',
}


def build_brief(path: Path, top_n: int) -> dict:
    scan = build_watchlist_scan(load_watchlist(str(path)))
    sectors = build_sector_summary(['majors', 'ai', 'l1l2', 'rwa'])
    opps = (scan.get('top_opportunities') or [])[:top_n]
    risks = (scan.get('top_risks') or [])[:top_n]
    strongest = sectors.get('strongest_sector') or {}
    weakest = sectors.get('weakest_sector') or {}
    takeaways = []
    if strongest:
        takeaways.append(f"{strongest.get('sector')} leads with setup {strongest.get('average_setup_score')} and 24h move {strongest.get('average_move_24h_pct')}%.")
    if weakest:
        takeaways.append(f"{weakest.get('sector')} is lagging at {weakest.get('average_move_24h_pct')}% average 24h move.")
    if opps:
        takeaways.append(f"Best current setup: {opps[0].get('ticker')} with setup {opps[0].get('setup_score')}.")
    if risks:
        takeaways.append(f"Main danger name: {risks[0].get('ticker')} with risk {risks[0].get('risk_score')}.")
    return {
        'preset': path.stem,
        'market_regime': scan.get('market_regime', 'mixed'),
        'average_setup_score': scan.get('average_setup_score', 0.0),
        'average_risk_score': scan.get('average_risk_score', 0.0),
        'breadth': scan.get('breadth', {}),
        'top_opportunities': opps,
        'top_risks': risks,
        'sector_summary': sectors,
        'takeaways': takeaways,
    }


def format_text(data: dict) -> str:
    lines = [f"## Daily market brief | {data['preset']}", f"Regime: {data['market_regime']} | avg setup {data['average_setup_score']} | avg risk {data['average_risk_score']}", '']
    lines.append('Key takeaways:')
    for row in data.get('takeaways', []):
        lines.append(f"- {row}")
    lines.append('')
    lines.append('Top opportunities:')
    for item in data.get('top_opportunities', []):
        lines.append(f"- {item.get('ticker')}: setup {item.get('setup_score')} | risk {item.get('risk_score')} | reasons: {', '.join(item.get('reasons') or [])}")
    lines.append('')
    lines.append('Risk names:')
    for item in data.get('top_risks', []):
        lines.append(f"- {item.get('ticker')}: risk {item.get('risk_score')} | warnings: {', '.join(item.get('risks') or [])}")
    lines.append('')
    strongest = data.get('sector_summary', {}).get('strongest_sector') or {}
    weakest = data.get('sector_summary', {}).get('weakest_sector') or {}
    lines.append(f"Strongest sector: {strongest.get('sector', 'n/a')}")
    lines.append(f"Weakest sector: {weakest.get('sector', 'n/a')}")
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Build daily market brief without an LLM')
    parser.add_argument('--preset', default='top50-trading')
    parser.add_argument('--top', type=int, default=4)
    parser.add_argument('--text', action='store_true')
    args = parser.parse_args()
    path = PRESETS.get(args.preset)
    if not path:
        raise SystemExit(f'Unknown preset: {args.preset}')
    data = build_brief(path, args.top)
    print(format_text(data) if args.text else json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
