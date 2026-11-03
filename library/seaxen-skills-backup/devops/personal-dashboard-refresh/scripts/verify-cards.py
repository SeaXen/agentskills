#!/usr/bin/env python3
"""
Verify dashboard cards after refresh.

Usage: python3 verify-cards.py
"""

import sys
import json
from pathlib import Path

PLUGIN_PATH = Path('/root/.hermes/products/hermes-personal-dashboard')
sys.path.insert(0, str(PLUGIN_PATH))

from personal_dashboard_core import connect, list_cards


def main():
    conn = connect()
    cards = list_cards(limit=50)

    if not cards:
        print("No cards found!")
        return 1

    print(f"=== Dashboard Cards ({len(cards)} total) ===\n")

    for c in cards:
        status_emoji = {
            'critical': '🔴',
            'high': '🟠',
            'medium': '🟡',
            'low': '🟢',
        }.get(c['priority'], '⚪')

        print(f"{status_emoji} [{c['id']}]")
        print(f"    Domain: {c['domain']} | Priority: {c['priority']} | Status: {c['status']}")
        print(f"    Title: {c['title']}")
        print(f"    Summary: {c['summary'][:120]}...")
        print(f"    Source: {c['source_label']}")
        print(f"    Why: {c['why_shown'][:100]}...")
        print(f"    Valid until: {c['valid_until']}")

        # Parse payload
        p = c.get('payload', {})
        if isinstance(p, str):
            p = json.loads(p) if p else {}

        if p.get('metrics'):
            print(f"    Metrics:")
            for m in p['metrics']:
                print(f"      - {m['label']}: {m['value']} {m['unit']}")

        if p.get('news_items'):
            print(f"    News items:")
            for item in p['news_items']:
                print(f"      - {item['title']}: {item['summary']}")

        if p.get('sections'):
            print(f"    Sections:")
            for section in p['sections']:
                print(f"      {section['label']}:")
                for item in section['items'][:5]:
                    print(f"        - {item}")
                if len(section['items']) > 5:
                    print(f"        ... and {len(section['items']) - 5} more")

        print()

    # Check for expected cards
    expected = [
        'openrouter-budget-watch',
        'openrouter-heartbeat-alert',
        'openrouter-model-changes',
        'backup-local-archive',
        'backup-gdrive-archive',
        'backup-mnemosyne',
        'obsidian-nightly-log',
        'cron-health-summary',
    ]

    found_ids = {c['id'] for c in cards}
    missing = [eid for eid in expected if eid not in found_ids]
    unexpected = [fid for fid in found_ids if not any(fid.startswith(eid.split('-')[0]) for eid in expected)]

    if missing:
        print(f"⚠️  MISSING expected cards: {missing}")
    else:
        print(f"✅ All {len(expected)} expected cards present")

    if unexpected:
        print(f"ℹ️  Additional cards: {unexpected}")

    return 0


if __name__ == '__main__':
    sys.exit(main())