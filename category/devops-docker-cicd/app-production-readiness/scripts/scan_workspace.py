#!/usr/bin/env python3
"""Discover every app root in a workspace. Read-only.

Usage:  python scan_workspace.py [workspace_root]
Output: JSON { workspace, apps: [ {name, path, markers, has_readme, has_pkg} ] }
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    APP_MARKERS,
    SKIP_DIRS,
    parse_cli,
    resolve_root,
    root_error,
)

SKIP = SKIP_DIRS | {
    "docs", "vendor", "target", "venv", ".venv", "__pycache__",
}


def is_app(d: Path) -> bool:
    return any((d / m).is_file() for m in APP_MARKERS)


def main() -> int:
    root_arg, _json_mode, want_help = parse_cli(sys.argv[1:])
    if want_help:
        print(__doc__)
        return 0
    ws = resolve_root(root_arg)
    err = root_error(ws)
    if err:
        # This script's contract is JSON output, so stdout must stay parseable
        # even on failure. The human message goes to stderr.
        print(json.dumps({"workspace": str(ws), "count": 0, "apps": [], "error": err}, indent=2))
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    apps = []
    for child in sorted(ws.iterdir()):
        if not child.is_dir() or child.name in SKIP or child.name.startswith("."):
            continue
        if not is_app(child):
            continue
        markers = [m for m in APP_MARKERS if (child / m).is_file()]
        readme = child / "README.md"
        apps.append({
            "name": child.name,
            "path": str(child),
            "markers": markers,
            "has_readme": readme.is_file(),
            "readme_bytes": readme.stat().st_size if readme.is_file() else 0,
            "has_package": (child / "package.json").is_file(),
            "has_env_example": (child / ".env.example").is_file(),
        })

    print(json.dumps({"workspace": str(ws), "count": len(apps), "apps": apps}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
