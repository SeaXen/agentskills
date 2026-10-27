#!/usr/bin/env python3
"""Playwright flow runner - the E2E half of the extended gates.

Business logic, payment and email flows cannot be proven by reading code.
This runner executes a declarative flow spec against a live app and reports
exactly which step failed, plus the console errors the page produced.

Spec file (looked up in this order):
    qa/flows.json, tests/flows.json, flows.json, e2e/flows.json

Format:
    {
      "flows": [
        {
          "name": "signup",
          "steps": [
            {"action": "goto",    "value": "/signup"},
            {"action": "fill",    "value": "#email", "text": "qa@example.com"},
            {"action": "click",   "value": "button[type=submit]"},
            {"action": "assert_text", "value": "h1", "text": "Welcome"}
          ]
        }
      ]
    }

Supported actions: goto, click, fill, press, wait_for, wait_ms, assert_text,
assert_visible, assert_hidden, assert_url, assert_count, screenshot.

Usage:
  python scripts/flow_test.py --root <app_root> --url http://localhost:3000
  python scripts/flow_test.py --root <app_root> --url ... --json

Exit 0 = every flow passed, 1 = a flow failed, 2 = Playwright/spec missing.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, load_json, parse_cli, resolve_root, root_error  # noqa: E402

SPEC_LOCATIONS = ("qa/flows.json", "tests/flows.json", "flows.json",
                  "e2e/flows.json", "qa/e2e/flows.json")
REPORT_DIR = "qa/flows"


def find_spec(root: Path):
    for rel in SPEC_LOCATIONS:
        cand = root / rel
        if cand.is_file():
            return cand
    return None


def _require_playwright():
    try:
        import playwright.sync_api  # noqa: F401
        return True, ""
    except Exception as exc:
        return False, f"playwright is not installed ({exc})"


def run_flows(spec, base_url, out_dir: Path, browsers=("chromium",), timeout_ms=15000):
    """Execute every flow.  Returns (report, failures)."""
    from playwright.sync_api import sync_playwright

    out_dir.mkdir(parents=True, exist_ok=True)
    report = {"base_url": base_url, "flows": [], "failures": [],
              "browsers": list(browsers), "generated": time.strftime("%Y-%m-%dT%H:%M:%S")}
    with sync_playwright() as pw:
        for bname in browsers:
            try:
                browser = getattr(pw, bname).launch()
            except Exception as exc:
                report["failures"].append(f"{bname}: browser not available ({exc})")
                continue
            for flow in spec.get("flows", []):
                entry = {"name": flow.get("name", "unnamed"), "browser": bname,
                         "steps": [], "status": "ok", "console_errors": []}
                context = browser.new_context()
                page = context.new_page()
                page.set_default_timeout(timeout_ms)
                page.on("console", lambda msg, e=entry: (
                    e["console_errors"].append(msg.text)
                    if msg.type == "error" and len(e["console_errors"]) < 20 else None))
                page.on("pageerror", lambda exc, e=entry: (
                    e["console_errors"].append(f"pageerror: {exc}")
                    if len(e["console_errors"]) < 20 else None))
                try:
                    for step in flow.get("steps", []):
                        entry["steps"].append(_run_step(page, base_url, step))
                        if entry["steps"][-1]["ok"] is False:
                            entry["status"] = "fail"
                            break
                except Exception as exc:
                    entry["status"] = "fail"
                    entry["steps"].append({"action": "exception", "ok": False,
                                           "detail": str(exc)[:300]})
                if entry["status"] == "fail":
                    shot = out_dir / f"{bname}-{_slug(flow.get('name', 'flow'))}.png"
                    try:
                        page.screenshot(path=str(shot), full_page=True)
                        entry["screenshot"] = str(shot)
                    except Exception:
                        pass
                context.close()
                report["flows"].append(entry)
                if entry["status"] == "fail":
                    report["failures"].append(
                        f"{entry['browser']}:{entry['name']}: "
                        f"{_failed_step(entry)}")
            browser.close()
    return report, report["failures"]


def _failed_step(entry):
    for step in entry["steps"]:
        if step.get("ok") is False:
            return f"step {step.get('action')} {step.get('value', '')} - {step.get('detail', '')}"
    return "unknown failure"


def _slug(text):
    import re
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-") or "flow"


def _run_step(page, base_url, step):
    action = (step.get("action") or "").lower()
    value = step.get("value")
    text = step.get("text")
    detail = ""
    ok = True
    try:
        if action == "goto":
            target = value if str(value).startswith("http") else base_url.rstrip("/") + "/" + str(value).lstrip("/")
            resp = page.goto(target, wait_until="domcontentloaded")
            status = resp.status if resp else 0
            ok = bool(status and status < 400)
            detail = f"status {status}"
        elif action == "click":
            page.click(value)
            detail = f"clicked {value}"
        elif action == "fill":
            page.fill(value, text or "")
            detail = f"filled {value}"
        elif action == "press":
            page.press(value, text or "Enter")
            detail = f"pressed {value}"
        elif action == "wait_for":
            page.wait_for_selector(value, state="visible")
            detail = f"waited for {value}"
        elif action == "wait_ms":
            page.wait_for_timeout(int(text or 100))
            detail = f"waited {text}ms"
        elif action == "assert_text":
            content = page.text_content(value) or ""
            ok = (text or "").lower() in content.lower()
            detail = f"{value} contains {text!r} (got {content[:60]!r})"
        elif action == "assert_visible":
            ok = page.is_visible(value)
            detail = f"{value} visible={ok}"
        elif action == "assert_hidden":
            ok = not page.is_visible(value)
            detail = f"{value} hidden={ok}"
        elif action == "assert_url":
            ok = (text or "") in page.url
            detail = f"url {page.url} contains {text!r}"
        elif action == "assert_count":
            expected = int(text or 1)
            actual = page.locator(value).count()
            ok = actual == expected
            detail = f"{value} count {actual} (expected {expected})"
        elif action == "screenshot":
            path = step.get("path") or "flow.png"
            page.screenshot(path=path, full_page=True)
            detail = f"saved {path}"
        else:
            ok = False
            detail = f"unknown action {action!r}"
    except Exception as exc:
        ok = False
        detail = str(exc)[:200]
    return {"action": action, "value": value, "text": text, "ok": ok, "detail": detail}


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    url = None
    root_arg = "."
    browsers = ("chromium",)
    out_dir = None
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--url" and i + 1 < len(args):
            url = args[i + 1]
            i += 1
        elif a == "--root" and i + 1 < len(args):
            root_arg = args[i + 1]
            i += 1
        elif a == "--browsers" and i + 1 < len(args):
            browsers = tuple(b.strip() for b in args[i + 1].split(",") if b.strip())
            i += 1
        elif a == "--out" and i + 1 < len(args):
            out_dir = args[i + 1]
            i += 1
        i += 1
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    if not url:
        print("ERROR: --url is required", file=sys.stderr)
        return 1

    spec_path = find_spec(root)
    if spec_path is None:
        lines = ["=" * 62, "FLOW TESTS  [skipped: no flow spec found]", "=" * 62,
                 f"looked for: {', '.join(SPEC_LOCATIONS)}"]
        emit(lines, {"status": "skipped",
                     "reason": "no flow spec found",
                     "looked_for": list(SPEC_LOCATIONS)}, json_mode)
        return 2
    ok, why = _require_playwright()
    if not ok:
        lines = ["=" * 62, f"FLOW TESTS  [skipped: {why}]", "=" * 62]
        emit(lines, {"status": "skipped", "reason": why}, json_mode)
        return 2

    spec = load_json(spec_path) or {}
    target_out = Path(out_dir) if out_dir else (root / REPORT_DIR)
    report, failures = run_flows(spec, url, target_out, browsers=browsers)

    lines = ["=" * 62, f"FLOW TESTS  [{url}]", "=" * 62]
    for flow in report["flows"]:
        icon = "PASS" if flow["status"] == "ok" else "FAIL"
        lines.append(f"[{icon}] {flow['browser']}:{flow['name']} "
                     f"({len(flow['steps'])} step(s))")
        if flow["status"] == "fail":
            lines.append(f"       {_failed_step(flow)}")
        for err_msg in flow["console_errors"][:3]:
            lines.append(f"       console: {err_msg[:120]}")
    lines.append("-" * 62)
    lines.append(f"blocking failures: {len(failures)}")
    lines.append("=" * 62)
    try:
        (target_out / "flow-report.json").write_text(
            json.dumps(report, indent=2), encoding="utf-8")
        lines.append(f"report: {target_out / 'flow-report.json'}")
    except OSError:
        pass
    emit(lines, report, json_mode)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
