#!/usr/bin/env python3
"""
Parse the skill's lightweight YAML-like watchlist template into JSON.
No external dependencies required.

Usage:
  python3 watchlist_parser.py templates/watchlist.yaml
"""

import argparse
import json
import re
import sys
from typing import Any, Dict, List


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.startswith('[') and value.endswith(']'):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(x.strip()) for x in inner.split(',')]
    low = value.lower()
    if low == 'true':
        return True
    if low == 'false':
        return False
    if low in ('null', 'none'):
        return None
    if re.fullmatch(r'-?\d+', value):
        try:
            return int(value)
        except Exception:
            pass
    if re.fullmatch(r'-?\d+\.\d+', value):
        try:
            return float(value)
        except Exception:
            pass
    return value


def parse_watchlist_text(text: str) -> Dict[str, Any]:
    entries: List[Dict[str, Any]] = []
    current: Dict[str, Any] = {}
    current_list_key = None

    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith('#'):
            continue
        if raw.strip() == 'watchlist:':
            continue

        indent = len(raw) - len(raw.lstrip(' '))
        stripped = raw.strip()

        if stripped.startswith('- '):
            content = stripped[2:].strip()
            if indent <= 2 and content.startswith('ticker:'):
                if current:
                    entries.append(current)
                current = {}
                current_list_key = None
                key, value = content.split(':', 1)
                current[key.strip()] = parse_scalar(value)
            else:
                if not current_list_key:
                    continue
                current.setdefault(current_list_key, []).append(parse_scalar(content))
            continue

        if ':' not in stripped:
            continue
        key, value = stripped.split(':', 1)
        key = key.strip()
        value = value.strip()
        parsed = parse_scalar(value)
        if parsed == "":
            current[key] = []
            current_list_key = key
        else:
            current[key] = parsed
            current_list_key = None

    if current:
        entries.append(current)

    return {'watchlist': entries}


def main() -> None:
    parser = argparse.ArgumentParser(description='Parse lightweight YAML-like watchlist to JSON')
    parser.add_argument('path')
    args = parser.parse_args()
    with open(args.path, 'r', encoding='utf-8') as f:
        text = f.read()
    print(json.dumps(parse_watchlist_text(text), indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        sys.exit(str(exc))
