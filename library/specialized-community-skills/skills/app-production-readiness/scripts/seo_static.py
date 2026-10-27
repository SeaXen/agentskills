#!/usr/bin/env python3
"""Static SEO + AI-citability (GEO) audit of the pages in a project.

Gate G is proven against the *running* app (`runtime_check.py`): that is the
only way to see the real `<title>`, the real canonical URL and the real
404 behaviour.  This script covers what a live request cannot see:

* pages that exist in the repository but are not on the route list
* source-level metadata gaps (missing description / Open Graph / alt text)
* how quotable the content is for AI answer engines (GEO readiness)

It runs the absorbed `seo-fundamentals` and `geo-fundamentals` engines.
SEO findings are real metadata gaps and are reported as blocking when
`--strict` is given.  GEO findings are advisory only: AI-citability score
is a moving target and must never fail a production gate on its own.

Usage:
  python seo_static.py --root <app_root> [--json] [--strict]

Exit 0: no SEO gap found (GEO advice may still be listed)
Exit 1: SEO gaps found (or --strict and only advice exists)
Exit 2: there is nothing to audit (no page files)
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402

ABSORBED = Path(__file__).resolve().parent / "absorbed"

# Generated output is not part of the product: Lighthouse HTML reports, coverage
# pages and Playwright traces would otherwise be audited as if they were pages.
EXCLUDE_DIRS = {"qa", "coverage", "test-results", "playwright-report", ".git",
                "node_modules", "__pycache__", "fixtures", "__fixtures__"}


def _is_generated(path: Path, root: Path) -> bool:
    try:
        rel = path.resolve().relative_to(root.resolve())
    except (ValueError, OSError):
        return False
    parts = {part.lower() for part in rel.parts[:-1]}
    if parts & EXCLUDE_DIRS:
        return True
    return bool(parts & {"lighthouse", "report", "reports"})


def _load(name: str):
    """Import an absorbed script as a module (their CLI is guarded)."""
    path = ABSORBED / name
    if not path.is_file():
        return None
    try:
        spec = importlib.util.spec_from_file_location(f"absorbed_{path.stem}", path)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception:
        return None


def _pages(module, root: Path):
    for finder in ("find_pages", "find_web_pages"):
        fn = getattr(module, finder, None)
        if fn is None:
            continue
        try:
            found = fn(root)
        except Exception:
            continue
        if found:
            return [p for p in found if not _is_generated(p, root)]
    return []


def _issues(result) -> list:
    if isinstance(result, dict):
        raw = result.get("issues") or result.get("problems") or []
        if isinstance(raw, str):
            return [raw]
        out = []
        for item in raw:
            out.append(item if isinstance(item, str) else str(item))
        return out
    if isinstance(result, (list, tuple)):
        return [str(i) for i in result]
    return []


def analyse(root: Path) -> dict:
    seo = _load("seo_checker.py")
    geo = _load("geo_checker.py")
    seo_findings = []
    pages = []
    if seo is not None:
        pages = _pages(seo, root)
        for page in pages:
            try:
                result = seo.check_page(page)
            except Exception as exc:
                seo_findings.append({"file": getattr(page, "name", str(page)),
                                     "issue": f"seo check failed: {exc}"})
                continue
            for issue in _issues(result):
                seo_findings.append({"file": str(result.get("file", getattr(page, "name", "?"))),
                                     "issue": issue})
    geo_findings = []
    geo_score = None
    if geo is not None:
        geo_pages = _pages(geo, root) or pages
        scores = []
        for page in geo_pages:
            try:
                result = geo.check_page(page)
            except Exception:
                continue
            if isinstance(result, dict):
                if isinstance(result.get("score"), (int, float)):
                    scores.append(result["score"])
                for issue in _issues(result):
                    geo_findings.append({"file": str(result.get("file", getattr(page, "name", "?"))),
                                         "advice": issue})
        if scores:
            geo_score = round(sum(scores) / len(scores), 1)

    return {
        "status": "issues" if seo_findings else "ok",
        "pages_checked": len(pages),
        "seo_findings": seo_findings,
        "geo_score": geo_score,
        "geo_advice": geo_findings,
        "engines": {
            "seo": bool(seo),
            "geo": bool(geo),
        },
    }


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
    strict = "--strict" in args
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    report = analyse(root)
    if not report["pages_checked"]:
        report["status"] = "skipped"
        report["reason"] = "no page files to audit"
        lines = ["[SKIP] static SEO audit - no page files found"]
        emit(lines, report, json_mode)
        return 2
    lines = ["=" * 62, "STATIC SEO / GEO AUDIT", "=" * 62]
    lines.append(f"pages checked: {report['pages_checked']}")
    if report["seo_findings"]:
        lines.append(f"[FAIL] {len(report['seo_findings'])} metadata gap(s):")
        for finding in report["seo_findings"][:20]:
            lines.append(f"  - {finding['file']}: {finding['issue']}")
    else:
        lines.append("[OK] no metadata gaps found")
    if report["geo_score"] is not None:
        lines.append(f"[note] AI-citability score: {report['geo_score']}% (advisory only)")
        for advice in report["geo_advice"][:5]:
            lines.append(f"  - {advice['file']}: {advice['advice']}")
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    if report["seo_findings"]:
        return 1 if strict else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
