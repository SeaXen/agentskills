#!/usr/bin/env python3
"""Bundle-size and performance-budget report for a built app.

Turns Gate B ("route JS <= 200 kB gzipped", "no dependency > 50 kB
gzipped without justification") into an enforced, measurable check instead
of an opinion.

Usage:
  python bundle_report.py [project_root] [--json] [--budget 200] [--dep-budget 50]

Exit 0: every budget met | Exit 1: a budget was exceeded | Exit 2: nothing built
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    emit,
    find_dist,
    gzip_size,
    load_json,
    parse_cli,
    resolve_root,
    root_error,
    walk_files,
)

ASSET_EXT = {".js", ".mjs", ".cjs", ".css", ".html", ".json", ".svg", ".png",
              ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico", ".woff", ".woff2",
              ".ttf", ".otf", ".map"}
CODE_EXT = {".js", ".mjs", ".cjs", ".css"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", "out", "coverage", ".next",
             ".nuxt", ".svelte-kit", ".turbo", ".cache", "target", "vendor",
             ".venv", "venv", "__pycache__", ".pytest_cache", "qa"}


def collect_assets(dist: Path):
    """Every shipped asset with its raw and gzipped size."""
    out = []
    for p in sorted(dist.rglob("*")):
        if not p.is_file():
            continue
        if p.suffix.lower() not in ASSET_EXT:
            continue
        raw = p.stat().st_size
        gz = gzip_size(p) if p.suffix.lower() in CODE_EXT or p.suffix.lower() in {".html", ".json", ".svg"} else raw
        out.append({
            "path": str(p.relative_to(dist)).replace("\\", "/"),
            "ext": p.suffix.lower(),
            "bytes": raw,
            "gzip_bytes": gz,
            "gzip_kb": round(gz / 1024, 1),
        })
    return out


def vite_manifest_entries(root: Path, dist: Path):
    """Entry chunks from a Vite manifest, when present."""
    for cand in (dist / ".vite" / "manifest.json", dist / "manifest.json",
                 root / ".vite" / "manifest.json"):
        if cand.is_file():
            data = load_json(cand)
            if isinstance(data, dict):
                return {k: v for k, v in data.items()
                        if isinstance(v, dict) and v.get("isEntry")}, cand
    return {}, None


def next_route_chunks(root: Path):
    """Per-route JS chunks from a Next.js build manifest."""
    manifest = root / ".next" / "build-manifest.json"
    if not manifest.is_file():
        return {}, None
    data = load_json(manifest)
    if not isinstance(data, dict):
        return {}, None
    pages = data.get("pages") or {}
    if not isinstance(pages, dict):
        return {}, None
    return {k: v for k, v in pages.items() if isinstance(v, list)}, manifest


def estimate_route_js(assets):
    """Fallback: largest JS asset group per route-less estimate."""
    js = [a for a in assets if a["ext"] in {".js", ".mjs", ".cjs"}]
    total = sum(a["gzip_bytes"] for a in js)
    return total, js


def unused_dependencies(root: Path):
    """Runtime dependencies that never appear in the source tree.

    Only `dependencies` are checked: build tooling (vite, eslint, typescript)
    is invoked from scripts and never imported, so flagging it would be a
    false positive.
    """
    pkg = load_json(root / "package.json")
    if not isinstance(pkg, dict):
        return []
    deps = dict(pkg.get("dependencies") or {})
    if not deps:
        return []
    sources = []
    for p in walk_files(root, skip_dirs=SKIP_DIRS):
        if p.suffix in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".vue", ".svelte", ".html"}:
            try:
                sources.append(p.read_text(encoding="utf-8", errors="ignore")[:120_000])
            except OSError:
                continue
    blob = "\n".join(sources)
    unused = []
    for name in deps:
        # Look for an import/require of the package name (scoped names included).
        pattern = re.compile(r"""(?:from|import|require\s*\()\s*['"]""" + re.escape(name) + r"""['"]""")
        if not pattern.search(blob):
            unused.append(name)
    return sorted(unused)


def analyse(root: Path, route_budget_kb: int = 200, dep_budget_kb: int = 50) -> dict:
    dist, kind = find_dist(root)
    report = {
        "root": str(root),
        "dist": str(dist) if dist else None,
        "dist_kind": kind,
        "budget_route_kb": route_budget_kb,
        "budget_dep_kb": dep_budget_kb,
        "checks": [],
        "assets": [],
        "routes": {},
        "warnings": [],
    }

    def check(name, ok, detail="", required=True):
        report["checks"].append({"name": name, "ok": bool(ok),
                                 "required": required, "detail": detail})
        return ok

    if not dist:
        check("build output present", False,
              "no dist/build/out/.next directory - run the project's build first")
        report["status"] = "no-build"
        return report

    # A framework dev server writes the same directory a production build
    # writes (``.next/static`` exists after a *failed* build too).  The
    # framework profile knows the marker files only a completed build leaves
    # behind, so a half-finished build is never reported as a healthy bundle.
    try:
        import framework_profiles
        markers = framework_profiles.build_markers(root)
        if markers and not framework_profiles.build_is_real(root):
            check("build output present", False,
                  f"{dist.name} exists but the production build did not complete "
                  f"(no {', '.join(markers)}) - the assets below are "
                  "development output, not a shippable bundle")
            report["status"] = "no-build"
            report["dev_only"] = True
            return report
    except Exception:  # pragma: no cover
        pass

    assets = collect_assets(dist)
    report["assets"] = assets
    check("build output present", True, str(dist))

    # --- per-route JS budget ---
    entries, manifest_path = vite_manifest_entries(root, dist)
    if entries:
        total = 0
        for key, meta in entries.items():
            size = 0
            for f in meta.get("file", "") and [meta["file"]] or []:
                p = dist / f
                if p.is_file():
                    size += gzip_size(p)
            for imp in meta.get("imports") or []:
                m = entries.get(imp) or {}
                f = m.get("file")
                if f and (dist / f).is_file():
                    size += gzip_size(dist / f)
            total += size
            report["routes"][key] = {"gzip_kb": round(size / 1024, 1)}
        report["route_budget_kb"] = round(total / 1024, 1)
        check(f"route JS budget <= {route_budget_kb} kB gzipped",
              total <= route_budget_kb * 1024,
              f"{round(total / 1024, 1)} kB across {len(entries)} entries"
              + (f" (manifest: {manifest_path.name})" if manifest_path else ""))
    else:
        pages, mpath = next_route_chunks(root)
        if pages:
            for route, files in pages.items():
                size = sum(gzip_size(root / ".next" / f) for f in files
                           if (root / ".next" / f).is_file())
                report["routes"][route] = {"gzip_kb": round(size / 1024, 1)}
            worst = max((v["gzip_kb"] for v in report["routes"].values()), default=0)
            report["route_budget_kb"] = worst
            check(f"route JS budget <= {route_budget_kb} kB gzipped",
                  worst <= route_budget_kb,
                  f"worst route {worst} kB ({mpath.name if mpath else 'next manifest'})")
        else:
            total, js = estimate_route_js(assets)
            report["route_budget_kb"] = round(total / 1024, 1)
            check(f"route JS budget <= {route_budget_kb} kB gzipped",
                  total <= route_budget_kb * 1024,
                  f"{round(total / 1024, 1)} kB total JS (no manifest - total used as estimate)")

    # --- per-asset budget ---
    big = [a for a in assets if a["ext"] in CODE_EXT and a["gzip_kb"] > dep_budget_kb]
    check(f"no JS/CSS asset > {dep_budget_kb} kB gzipped", not big,
          ", ".join(f"{a['path']} {a['gzip_kb']}kB" for a in big[:5]))

    # --- source maps must not ship to production ---
    maps = [a for a in assets if a["ext"] == ".map"]
    check("no source maps in build output", not maps,
          ", ".join(a["path"] for a in maps[:5]), required=False)

    # --- image weight / modern formats ---
    heavy = [a for a in assets if a["ext"] in IMAGE_EXT and a["bytes"] > 200 * 1024]
    check("no image > 200 kB", not heavy,
          ", ".join(f"{a['path']} {round(a['bytes']/1024)}kB" for a in heavy[:5]), required=False)
    legacy = [a for a in assets if a["ext"] in {".png", ".jpg", ".jpeg"} and a["bytes"] > 50 * 1024]
    if legacy:
        report["warnings"].append(
            "modern image format recommended for: " + ", ".join(a["path"] for a in legacy[:5]))

    # --- unused dependencies ---
    unused = unused_dependencies(root)
    report["unused_dependencies"] = unused
    check("no unused dependencies", not unused, ", ".join(unused[:8]), required=False)

    report["total_kb"] = round(sum(a["gzip_bytes"] for a in assets) / 1024, 1)
    required_fail = [c for c in report["checks"] if c["required"] and not c["ok"]]
    report["status"] = "fail" if required_fail else "ok"
    return report


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
    route_budget = 200
    dep_budget = 50
    for i, a in enumerate(args):
        if a == "--budget" and i + 1 < len(args):
            try:
                route_budget = int(args[i + 1])
            except ValueError:
                pass
        if a == "--dep-budget" and i + 1 < len(args):
            try:
                dep_budget = int(args[i + 1])
            except ValueError:
                pass
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        payload = {"error": err, "status": "failed", "checks": []}
        if json_mode:
            emit([f"[FAIL] {err}"], payload, True)
        else:
            print(f"[FAIL] {err}", file=sys.stderr)
        return 1

    report = analyse(root, route_budget, dep_budget)
    lines = ["=" * 62, f"BUNDLE REPORT  [{report.get('dist_kind') or 'no build'}]", "=" * 62]
    if report.get("status") == "no-build":
        lines.append("[FAIL] build output present  -> no dist/build/out/.next found")
        lines.append("=" * 62)
        emit(lines, report, json_mode)
        return 2
    for c in report["checks"]:
        icon = "PASS" if c["ok"] else ("FAIL" if c["required"] else "warn")
        lines.append(f"[{icon}] {c['name']}" + (f"  -> {c['detail']}" if not c["ok"] and c["detail"] else ""))
    for w in report.get("warnings", []):
        lines.append(f"[warn] {w}")
    lines.append("-" * 62)
    lines.append(f"total shipped (gzipped est): {report.get('total_kb', 0)} kB")
    if report.get("route_budget_kb") is not None:
        lines.append(f"route JS budget usage: {report['route_budget_kb']} kB / {route_budget} kB")
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    return 1 if report["status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
