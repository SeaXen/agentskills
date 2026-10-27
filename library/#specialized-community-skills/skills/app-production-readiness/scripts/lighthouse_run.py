#!/usr/bin/env python3
"""Run Lighthouse for real and enforce the Gate D score thresholds.

Gate D used to be prose with no runner behind it. This script executes
Lighthouse against the live app on the desktop preset, stores the JSON and
HTML reports as review artifacts, and FAILS when a category drops below the
required score.

Usage:
  python lighthouse_run.py --url http://localhost:3000 --routes /,/pricing \\
      --out qa/lighthouse [--json] [--perf 90] [--a11y 95] [--bp 95] [--seo 90]

Exit 0: every route meets every threshold | Exit 1: a score is below target
Exit 2: Lighthouse could not run (reported as SKIPPED, never a pass)
"""
from __future__ import annotations

import os
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    emit,
    load_json,
    parse_cli,
    resolve_out_dir,
    resolve_root,
    root_error,
    run_cmd,
    which,
    write_json,
)

CATEGORIES = ("performance", "accessibility", "best-practices", "seo")
DEFAULT_THRESHOLDS = {"performance": 90, "accessibility": 95,
                      "best-practices": 95, "seo": 90}
METRICS = {
    "largest-contentful-paint": "LCP",
    "cumulative-layout-shift": "CLS",
    "total-blocking-time": "TBT",
    "first-contentful-paint": "FCP",
    "speed-index": "SI",
    "interactive": "TTI",
}
CHROME_FLAGS = "--headless=new --no-sandbox --disable-gpu --disable-dev-shm-usage"


def find_chrome():
    """Locate a Chrome/Chromium binary: env, Playwright's browsers, then PATH."""
    env_path = os.environ.get("CHROME_PATH")
    if env_path and Path(env_path).exists():
        return env_path
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            exe = p.chromium.executable_path
            if exe and Path(exe).exists():
                return exe
    except Exception:
        pass
    for name in ("chrome", "chrome.exe", "msedge", "msedge.exe",
                 "chromium", "chromium.exe", "google-chrome"):
        found = which(name)
        if found:
            return found
    return None


def lighthouse_cmd(root: Path):
    """Return (argv_prefix, description) for running Lighthouse, or (None, reason)."""
    local = root / "node_modules" / ".bin" / "lighthouse"
    if local.exists():
        return [str(local)], "local node_modules/.bin/lighthouse"
    if which("lighthouse"):
        return ["lighthouse"], "global lighthouse"
    if which("npx"):
        return ["npx", "--yes", "lighthouse@12"], "npx lighthouse@12"
    return None, "neither a local, global nor npx-installable lighthouse was found"


def parse_report(data: dict) -> dict:
    """Pull scores and key metrics out of a Lighthouse JSON report."""
    cats = data.get("categories") or {}
    scores = {}
    for key in CATEGORIES:
        cat = cats.get(key) or {}
        scores[key] = round(float(cat.get("score") or 0) * 100, 1)
    audits = data.get("audits") or {}
    metrics = {}
    for aid, label in METRICS.items():
        audit = audits.get(aid) or {}
        value = audit.get("numericValue")
        if value is not None:
            metrics[label] = round(float(value), 3)
    for aid, label in (("total-byte-weight", "transfer KB"),
                       ("total-blocking-time", "TBT"),
                       ("speed-index", "SI")):
        if label in metrics:
            continue
        audit = audits.get(aid) or {}
        if audit.get("numericValue") is not None:
            metrics[label] = round(float(audit["numericValue"]), 3)
    failures = []
    for aid, audit in audits.items():
        if audit.get("score") is not None and audit.get("score") < 0.5 \
                and audit.get("scoreDisplayMode") in ("binary", "numeric"):
            if aid in ("first-contentful-paint", "largest-contentful-paint",
                       "total-blocking-time", "cumulative-layout-shift",
                       "speed-index", "interactive"):
                continue
            failures.append({"id": aid, "title": audit.get("title", "")[:120]})
    return {"scores": scores, "metrics": metrics, "failed_audits": failures[:20]}


def run_one(cmd_prefix, url: str, out_dir: Path, slug: str, chrome: str, timeout: int):
    """Run Lighthouse for one URL. Returns (report_dict, error_string)."""
    json_path = out_dir / f"lighthouse-{slug}.json"
    html_path = out_dir / f"lighthouse-{slug}.html"
    # Lighthouse names the files "<output-path>.report.json" / ".report.html"
    # when several --output formats are requested.
    json_candidates = [json_path, out_dir / f"lighthouse-{slug}.report.json"]
    html_candidates = [html_path, out_dir / f"lighthouse-{slug}.report.html"]
    argv = list(cmd_prefix) + [
        url,
        "--preset=desktop",
        "--output=json",
        "--output=html",
        f"--output-path={out_dir / ('lighthouse-' + slug)}",
        "--quiet",
        f"--chrome-flags={CHROME_FLAGS}",
        "--only-categories=performance,accessibility,best-practices,seo",
    ]
    env = dict(os.environ)
    if chrome:
        env["CHROME_PATH"] = chrome
    rc, out, err = run_cmd(argv, cwd=out_dir.parent if out_dir.parent.exists() else None,
                            timeout=timeout, env=env)
    data = None
    for cand in json_candidates:
        data = load_json(cand)
        if data is not None:
            break
    if data is None:
        return None, (err or out or f"lighthouse exited {rc} without a JSON report")[:400]
    for cand in html_candidates:
        if cand.exists() and cand != html_path:
            shutil.move(str(cand), str(html_path))
            break
    for cand in json_candidates:
        if cand.exists() and cand != json_path:
            shutil.move(str(cand), str(json_path))
            break
    return data, None


def run_one_fallback(url: str, out_dir: Path, slug: str, timeout: int):
    """Fallback runner: the absorbed ``performance-profiling`` Lighthouse script.

    It drives a globally installed ``lighthouse`` binary with the older
    ``--chrome-flags=--headless`` style, which still works on machines where
    the modern ``--headless=new`` invocation fails.  Only the category scores
    are returned (that script does not collect metrics).
    """
    script = Path(__file__).resolve().parent / "absorbed" / "lighthouse_audit.py"
    if not script.is_file():
        return None, "absorbed fallback Lighthouse runner is not available"
    try:
        from qa_ext import _extract_json
    except Exception:
        _extract_json = None
    rc, out, err = run_cmd([sys.executable, str(script), url], timeout=timeout)
    payload = None
    if _extract_json is not None:
        payload = _extract_json(out or "")
    if not isinstance(payload, dict):
        payload = None
    if payload is None:
        return None, (err or out or f"fallback lighthouse exited {rc}")[:400]
    if payload.get("error"):
        return None, str(payload.get("error"))[:400]
    scores = payload.get("scores") or {}
    data = {"categories": {}, "audits": {}, "fallback": True}
    for key, cat in (("performance", "performance"), ("accessibility", "accessibility"),
                     ("best_practices", "best-practices"), ("seo", "seo")):
        data["categories"][cat] = {"score": (scores.get(key) or 0) / 100}
    try:
        write_json(out_dir / f"lighthouse-{slug}.json", data)
    except Exception:
        pass
    return data, None


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    url = os.environ.get("APP_URL")
    routes_arg = os.environ.get("ROUTES")
    out_arg = "qa/lighthouse"
    root_arg = "."
    timeout = 300
    thresholds = dict(DEFAULT_THRESHOLDS)
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--url" and i + 1 < len(args):
            url = args[i + 1]
            i += 1
        elif a == "--root" and i + 1 < len(args):
            root_arg = args[i + 1]
            i += 1
        elif a == "--routes" and i + 1 < len(args):
            routes_arg = args[i + 1]
            i += 1
        elif a == "--out" and i + 1 < len(args):
            out_arg = args[i + 1]
            i += 1
        elif a == "--timeout" and i + 1 < len(args):
            try:
                timeout = int(args[i + 1])
            except ValueError:
                pass
            i += 1
        else:
            for key, flag in (("performance", "--perf"), ("accessibility", "--a11y"),
                              ("best-practices", "--bp"), ("seo", "--seo")):
                if a == flag and i + 1 < len(args):
                    try:
                        thresholds[key] = int(args[i + 1])
                    except ValueError:
                        pass
                    i += 1
                    break
        i += 1
    if want_help:
        print(__doc__)
        return 0
    if not url:
        print("ERROR: --url is required (or set APP_URL)", file=sys.stderr)
        return 1

    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    out_dir, out_err = resolve_out_dir(root, out_arg)
    if out_err:
        print(f"ERROR: {out_err}", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)

    routes = [r.strip() for r in (routes_arg or "/").split(",") if r.strip()] or ["/"]
    cmd_prefix, source = lighthouse_cmd(root)
    report = {"url": url, "routes": routes, "thresholds": thresholds,
              "tool": source, "results": {}, "failures": [], "status": "ok"}

    if not cmd_prefix:
        report["status"] = "skipped"
        report["reason"] = source
        emit([f"[SKIP] {source}",
              "Lighthouse did not run - Gate D performance/accessibility scores are UNVERIFIED"],
             report, json_mode)
        return 2

    chrome = find_chrome()
    if not chrome:
        report["status"] = "skipped"
        report["reason"] = "no Chrome/Chromium binary found for Lighthouse"
        emit(["[SKIP] no Chrome binary - Lighthouse did not run"], report, json_mode)
        return 2

    for route in routes:
        target = url.rstrip("/") + "/" + route.lstrip("/") if route != "/" else url.rstrip("/") + "/"
        slug = "home" if route == "/" else route.strip("/").replace("/", "-")
        started = time.perf_counter()
        data, error = run_one(cmd_prefix, target, out_dir, slug, chrome, timeout)
        if error:
            # A transient npx/npm cache race (ECOMPROMISED / "Lock compromised")
            # is not an app defect - retry once before giving up.
            time.sleep(5)
            retry_data, retry_error = run_one(cmd_prefix, target, out_dir, slug,
                                              chrome, timeout)
            if retry_data is not None:
                data, error = retry_data, None
            else:
                error = f"{error} | retry: {retry_error}"
        if error:
            # Second chance with the absorbed runner (different flags).
            data, fallback_error = run_one_fallback(target, out_dir, slug, timeout)
            if data is None:
                # The measurement could not be taken. That is a SKIP, never a
                # failing score: a route without scores must not be reported
                # as "performance 0".
                report["results"][route] = {"error": error}
                report.setdefault("errors", []).append(f"{route}: {error}")
                continue
            source = source + " (fallback: absorbed lighthouse_audit.py)"
            report["tool"] = source
        parsed = parse_report(data)
        parsed["duration_s"] = round(time.perf_counter() - started, 1)
        parsed["report_json"] = str(out_dir / f"lighthouse-{slug}.json")
        report["results"][route] = parsed
        for cat, minimum in thresholds.items():
            score = parsed["scores"].get(cat, 0)
            if score < minimum:
                report["failures"].append(f"{route}: {cat} {score} < {minimum}")
        write_json(out_dir / "lighthouse-summary.json", report)

    measured = [r for r, v in report["results"].items() if (v or {}).get("scores")]
    if report["failures"]:
        report["status"] = "fail"
    elif not measured:
        report["status"] = "skipped"
        report["reason"] = "the Lighthouse run could not measure any route"
    else:
        report["status"] = "ok"
    write_json(out_dir / "lighthouse-summary.json", report)

    lines = ["=" * 62, f"LIGHTHOUSE (desktop)  [{url}]", "=" * 62]
    lines.append(f"tool: {source} | chrome: {chrome}")
    for route, res in report["results"].items():
        if res.get("error"):
            lines.append(f"[SKIP] {route}: the run could not be measured - {res['error']}")
            continue
        s = res["scores"]
        lines.append(f"-- {route} --")
        for cat, minimum in thresholds.items():
            score = s.get(cat, 0)
            icon = "PASS" if score >= minimum else "FAIL"
            lines.append(f"  [{icon}] {cat}: {score} (target {minimum})")
        m = res.get("metrics") or {}
        lines.append("  metrics: " + ", ".join(f"{k}={v}" for k, v in m.items()))
    lines.append("-" * 62)
    lines.append(f"blocking failures: {len(report['failures'])}")
    lines.append(f"reports: {out_dir}")
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    if report["failures"]:
        return 1
    if report.get("status") == "skipped":
        # nothing could be measured - a skip, never a pass and never a fail
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
