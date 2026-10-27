#!/usr/bin/env python3
"""Check a README against the production README standard. Read-only.

Usage:  python check_readme.py [app_root]
Exit 0: passes | Exit 1: required items missing
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    emit,
    is_remote_asset,
    parse_cli,
    readme_image_sources,
    resolve_readme_asset,
    resolve_root,
    root_error,
)

REQUIRED_SECTIONS = [
    ("title", r"^#\s+\S"),
    ("screenshot section", r"(?im)^##+\s*.*(screenshot|gallery|screenshots)"),
    ("features", r"(?im)^##+\s*.*(feature|highlights|what it does|capabilities)"),
    ("quick start", r"(?im)^##+\s*.*(quick\s*start|getting started|installation|setup)"),
    ("configuration", r"(?im)^##+\s*.*(configuration|environment|env|config)"),
    ("deploy", r"(?im)^##+\s*.*(deploy|deployment|hosting)"),
    ("license", r"(?im)^##+\s*.*license"),
]
BOILERPLATE_MARKERS = [
    "This is a [Next.js](https://nextjs.org) project bootstrapped with",
    "This project uses [`next/font`]",
    "Learn Next.js",
]


def main() -> int:
    root_arg, json_mode, want_help = parse_cli(sys.argv[1:])
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        if json_mode:
            emit([f"[FAIL] {err}"], {"error": err, "checks": []}, True)
        else:
            print(f"[FAIL] {err}", file=sys.stderr)
        return 1
    readme = root / "README.md"
    if not readme.is_file():
        msg = f"README.md missing in {root}"
        if json_mode:
            emit([f"[FAIL] {msg}"], {"error": msg, "checks": []}, True)
        else:
            print(f"[FAIL] {msg}", file=sys.stderr)
        return 1

    text = readme.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    results = []

    for name, pat in REQUIRED_SECTIONS:
        results.append((bool(re.search(pat, text)), name, ""))

    # env table: a markdown table containing an env variable name or standard configuration header
    has_env_table = False
    sep_indices = [
        i for i, l in enumerate(lines)
        if re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", l)
    ]
    for s_idx in sep_indices:
        header = lines[s_idx - 1] if s_idx > 0 else ""
        if re.search(r"\|\s*`?(?:Variable|Env|Environment|Key|Name)`?\s*\|", header, re.I):
            has_env_table = True
            break
        for r_idx in range(s_idx + 1, min(s_idx + 25, len(lines))):
            row = lines[r_idx].strip()
            if not row.startswith("|") and not row.endswith("|"):
                break
            if re.search(r"\|\s*`?[A-Z][A-Z0-9_]{2,}`?\s*\|", row):
                has_env_table = True
                break
        if has_env_table:
            break
    results.append((has_env_table, "env var table", ""))

    # images: Markdown ![](), HTML <img src>, HTML <source srcset>
    imgs = readme_image_sources(text)
    results.append((len(imgs) >= 3, f"screenshots referenced (>=3, found {len(imgs)})", ""))

    # broken local image paths - resolved relative to the repository root
    broken = []
    for src in imgs:
        if is_remote_asset(src):
            continue
        if resolve_readme_asset(root, src) is None:
            broken.append(src)
    results.append((not broken, "all local image paths resolve", ", ".join(broken[:4])))

    # contact sheet
    shot_dirs = [d for d in ("docs/screenshots", "screenshots", "docs/images", "public/screenshots")
                 if (root / d).is_dir()]
    has_sheet = any((root / d / "contact-sheet.png").exists() for d in shot_dirs)
    results.append((has_sheet, "contact-sheet.png present", ", ".join(shot_dirs)))

    # boilerplate
    boiler = [m for m in BOILERPLATE_MARKERS if m.lower() in text.lower()]
    results.append((not boiler, "no create-next-app boilerplate", "; ".join(boiler)))

    # alt text
    no_alt = [s for s in re.findall(r"!\[\]\(([^)\s]+)\)", text)]
    results.append((not no_alt, "images have alt text", ", ".join(no_alt[:3])))

    # contributing + license files
    for fname, label in (("LICENSE", "LICENSE file"), ("CONTRIBUTING.md", "CONTRIBUTING.md")):
        results.append(((root / fname).exists(), label, ""))

    payload = {
        "root": str(root),
        "checks": [
            {"name": name, "ok": ok, "detail": detail} for ok, name, detail in results
        ],
    }
    fails = len([r for r in results if not r[0]])

    out = []
    out.append("=" * 62)
    out.append(f"README CHECK: {root.name}")
    out.append("=" * 62)
    for ok, name, detail in results:
        out.append(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  -> {detail}" if not ok and detail else ""))
    out.append("-" * 62)
    out.append(f"{len(results) - fails}/{len(results)} passed | {fails} failing")
    out.append("=" * 62)
    # In JSON mode the report goes to stderr so stdout stays pure JSON.
    emit(out, payload, json_mode)
    return 1 if fails else 0

if __name__ == "__main__":
    raise SystemExit(main())
