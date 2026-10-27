#!/usr/bin/env python3
"""WCAG 2.1 AA audit with axe-core plus a keyboard-traversal pass.

Gate F used to be "run axe via Lighthouse and a Playwright keyboard
script" - neither existed. This script does both, in one run, across every
browser engine that is installed.

Usage:
  python a11y_audit.py --url http://localhost:3000 --routes /,/pricing \\
      --browsers chromium,firefox,webkit --out qa/a11y [--json]

Exit 0: no critical/serious violations and keyboard pass is clean
Exit 1: violations or keyboard failures
Exit 2: Playwright/axe unavailable (reported as SKIPPED, never a pass)
"""
from __future__ import annotations

import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    emit,
    parse_cli,
    resolve_out_dir,
    resolve_root,
    root_error,
    write_json,
)

HERE = Path(__file__).resolve().parent
CACHE_DIR = HERE / ".cache"
AXE_FILENAME = "axe.min.js"
AXE_URLS = (
    "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js",
    "https://unpkg.com/axe-core@4.10.2/axe.min.js",
)
AXE_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"]
BROWSERS = ("chromium", "firefox", "webkit")


def find_axe(root: Path):
    """Locate axe-core locally, in the cache, or download it once."""
    candidates = [
        root / "node_modules" / "axe-core" / "axe.min.js",
        HERE / "node_modules" / "axe-core" / "axe.min.js",
        CACHE_DIR / AXE_FILENAME,
    ]
    for c in candidates:
        if c.is_file() and c.stat().st_size > 1000:
            return c.read_text(encoding="utf-8", errors="ignore"), str(c)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    target = CACHE_DIR / AXE_FILENAME
    for url in AXE_URLS:
        try:
            with urllib.request.urlopen(url, timeout=45) as resp:
                data = resp.read()
            if len(data) > 1000:
                target.write_bytes(data)
                return data.decode("utf-8", errors="ignore"), f"{target} (downloaded from {url})"
        except Exception:
            continue
    return None, None


def axe_run(page, source: str):
    """Inject axe-core and run it against the current page."""
    page.add_script_tag(content=source)
    result = page.evaluate(
        """async () => {
            const r = await axe.run(document, {
                runOnly: { type: 'tag', values: %s },
                resultTypes: ['violations']
            });
            return r.violations.map(v => ({
                id: v.id,
                impact: v.impact,
                help: v.help,
                helpUrl: v.helpUrl,
                nodes: v.nodes.slice(0, 5).map(n => ({
                    target: n.target,
                    failureSummary: (n.failureSummary || '').slice(0, 400)
                }))
            }));
        }""" % ("[" + ",".join('"%s"' % t for t in AXE_TAGS) + "]")
    )
    return result or []


KEYBOARD_JS = r"""
() => {
  const style = (el) => window.getComputedStyle(el);
  const visibleFocus = (el) => {
    const s = style(el);
    const outline = s.outlineStyle !== 'none' && parseFloat(s.outlineWidth || '0') > 0;
    const shadow = s.boxShadow && s.boxShadow !== 'none';
    const border = parseFloat(s.borderTopWidth || '0') > 0 && s.borderTopStyle !== 'none';
    return outline || shadow || border;
  };
  const focusables = document.querySelectorAll(
    'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), ' +
    'textarea:not([disabled]), [tabindex]:not([tabindex="-1"])');
  const headings = Array.from(document.querySelectorAll('h1,h2,h3,h4,h5,h6'));
  let skipped = null;
  let prev = 0;
  for (const h of headings) {
    const lvl = Number(h.tagName.slice(1));
    if (prev && lvl > prev + 1) { skipped = `h${prev} -> h${lvl}`; break; }
    prev = lvl;
  }
  const landmarks = {
    header: !!document.querySelector('header,[role=banner]'),
    nav: !!document.querySelector('nav,[role=navigation]'),
    main: !!document.querySelector('main,[role=main]'),
    footer: !!document.querySelector('footer,[role=contentinfo]')
  };
  const skipLink = !!document.querySelector('a[href^="#"][class*="skip" i], a[href^="#main"], .skip-link');
  // Accessible name: the same fallbacks a screen reader uses. A form control
  // labelled with <label for="..."> IS named - flagging it would be a false
  // positive that trains people to ignore the audit.
  const accName = (el) => {
    const aria = el.getAttribute('aria-label');
    if (aria && aria.trim()) return aria.trim();
    const labelledby = el.getAttribute('aria-labelledby');
    if (labelledby) {
      const t = labelledby.split(/[\s]+/).map((id) => {
        const n = document.getElementById(id);
        return n ? (n.textContent || '').trim() : '';
      }).join(' ').trim();
      if (t) return t;
    }
    const id = el.id;
    if (id) {
      const labels = document.querySelectorAll('label');
      for (const lab of labels) {
        if (lab.getAttribute('for') === id && (lab.textContent || '').trim()) {
          return lab.textContent.trim();
        }
      }
    }
    const wrap = el.closest ? el.closest('label') : null;
    if (wrap && (wrap.textContent || '').trim()) return wrap.textContent.trim();
    const txt = (el.textContent || '').trim();
    if (txt) return txt;
    for (const attr of ['title', 'alt', 'placeholder', 'value']) {
      const v = el.getAttribute(attr);
      if (v && v.trim()) return v.trim();
    }
    return '';
  };
  return {
    focusableCount: focusables.length,
    focusablesWithoutName: Array.from(focusables)
      .filter(el => !accName(el))
      .map(el => el.tagName + (el.id ? '#' + el.id : '')).slice(0, 10),
    headingCount: headings.length,
    headingSkip: skipped,
    h1Count: document.querySelectorAll('h1').length,
    landmarks: landmarks,
    skipLink: skipLink
  };
}
"""


FOCUS_FALLBACK_JS = """
() => {
  const focusables = Array.from(document.querySelectorAll(
    'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), ' +
    'textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'));
  const invisible = [];
  for (const el of focusables.slice(0, 40)) {
    el.focus();
    const s = window.getComputedStyle(el);
    const outline = s.outlineStyle !== 'none' && parseFloat(s.outlineWidth || '0') > 0;
    const shadow = s.boxShadow && s.boxShadow !== 'none';
    const border = parseFloat(s.borderTopWidth || '0') > 0 && s.borderTopStyle !== 'none';
    const visible = outline || shadow || border;
    if (!visible) {
      invisible.push(el.tagName + (el.id ? '#' + el.id : ''));
    }
  }
  return { checked: focusables.length, invisible: invisible, mode: 'programmatic-focus' };
}
"""


def keyboard_pass(page):
    """Tab through the page and check that focus is always visible.

    Some engines (WebKit) do not move focus for synthetic Tab presses, so
    when no tab stop is observed we fall back to focusing every focusable
    element programmatically and inspecting the resulting focus style.
    """
    page.evaluate("() => { window.scrollTo(0,0); }")
    invisible = []
    seen = 0
    for _ in range(40):
        page.keyboard.press("Tab")
        info = page.evaluate(
            """() => {
                const el = document.activeElement;
                if (!el || el === document.body) return null;
                const s = window.getComputedStyle(el);
                const outline = s.outlineStyle !== 'none' && parseFloat(s.outlineWidth || '0') > 0;
                const shadow = s.boxShadow && s.boxShadow !== 'none';
                const border = parseFloat(s.borderTopWidth || '0') > 0 && s.borderTopStyle !== 'none';
                return {
                    tag: el.tagName,
                    id: el.id || '',
                    visible: outline || shadow || border
                };
            }"""
        )
        if not info:
            continue
        seen += 1
        if not info["visible"]:
            invisible.append(f"{info['tag']}{('#' + info['id']) if info['id'] else ''}")
        if seen >= 25:
            break
    mode = "tab"
    if seen == 0:
        try:
            fb = page.evaluate(FOCUS_FALLBACK_JS) or {}
        except Exception:
            fb = {}
        mode = fb.get("mode", "unavailable")
        invisible = list(fb.get("invisible") or [])
        seen = int(fb.get("checked") or 0)
    return {"tabbedElements": seen, "invisibleFocus": invisible, "mode": mode}


def audit(url: str, routes: list, browsers: list, source: str, timeout_ms: int):
    from playwright.sync_api import sync_playwright

    report = {"url": url, "routes": routes, "browsers": {}, "status": "ok"}
    failures = []
    with sync_playwright() as p:
        for bname in browsers:
            engine = getattr(p, bname, None)
            if engine is None:
                report["browsers"][bname] = {"status": "skipped",
                                             "reason": "unknown browser engine"}
                failures.append(f"{bname}: unknown engine")
                continue
            try:
                browser = engine.launch()
            except Exception as exc:
                report["browsers"][bname] = {
                    "status": "skipped",
                    "reason": f"browser not installed: {str(exc).splitlines()[0][:120]}"}
                failures.append(f"{bname}: not installed")
                continue
            # bypass_csp: a strict CSP blocks the injected axe script, which
            # would otherwise make the audit silently report "0 violations".
            ctx = browser.new_context(bypass_csp=True)
            page = ctx.new_page()
            page.set_default_timeout(timeout_ms)
            breport = {"status": "ok", "routes": {}}
            for route in routes:
                target = url.rstrip("/") + "/" + route.lstrip("/") if route != "/" else url.rstrip("/") + "/"
                entry = {"url": target}
                try:
                    resp = page.goto(target, wait_until="domcontentloaded", timeout=timeout_ms)
                    entry["status"] = resp.status if resp else 0
                    page.wait_for_timeout(400)
                except Exception as exc:
                    entry["error"] = f"navigation failed: {str(exc)[:200]}"
                    entry["violations"] = []
                    entry["structure"] = {}
                    entry["keyboard"] = {}
                    entry["axe_ran"] = False
                    breport["routes"][route] = entry
                    failures.append(f"{bname}{route}: navigation failed")
                    continue

                try:
                    entry["violations"] = axe_run(page, source)
                    entry["axe_ran"] = True
                except Exception as exc:
                    entry["violations"] = []
                    entry["axe_ran"] = False
                    entry["axe_error"] = str(exc)[:300]
                try:
                    entry["structure"] = page.evaluate(KEYBOARD_JS)
                except Exception as exc:
                    entry["structure"] = {}
                    entry["structure_error"] = str(exc)[:200]
                try:
                    entry["keyboard"] = keyboard_pass(page)
                except Exception as exc:
                    entry["keyboard"] = {}
                    entry["keyboard_error"] = str(exc)[:200]
                breport["routes"][route] = entry

                if not entry.get("axe_ran"):
                    failures.append(f"{bname}{route}: axe could not run (CSP or injection error)")
                for v in entry.get("violations", []):
                    if v.get("impact") in ("critical", "serious"):
                        failures.append(f"{bname}{route}: axe {v.get('id')} ({v.get('impact')})")
                kb = entry.get("keyboard") or {}
                if kb.get("invisibleFocus"):
                    failures.append(f"{bname}{route}: invisible focus on {kb['invisibleFocus'][:3]}")
                struct = entry.get("structure") or {}
                if struct.get("headingSkip"):
                    failures.append(f"{bname}{route}: heading level skip {struct['headingSkip']}")
                if struct.get("h1Count", 0) != 1:
                    failures.append(f"{bname}{route}: {struct.get('h1Count')} h1 elements")
                if not (struct.get("landmarks") or {}).get("main"):
                    failures.append(f"{bname}{route}: no main landmark")
                if struct.get("focusablesWithoutName"):
                    failures.append(f"{bname}{route}: unnamed focusable elements")
            browser.close()
            report["browsers"][bname] = breport
    report["failures"] = failures
    report["status"] = "fail" if failures else "ok"
    return report


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    url = os.environ.get("APP_URL")
    routes_arg = os.environ.get("ROUTES")
    browsers_arg = os.environ.get("BROWSERS")
    out_arg = "qa/a11y"
    root_arg = "."
    timeout_ms = 30000
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
        elif a == "--browsers" and i + 1 < len(args):
            browsers_arg = args[i + 1]
            i += 1
        elif a == "--out" and i + 1 < len(args):
            out_arg = args[i + 1]
            i += 1
        elif a == "--timeout" and i + 1 < len(args):
            try:
                timeout_ms = int(args[i + 1])
            except ValueError:
                pass
            i += 1
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

    routes = [r.strip() for r in (routes_arg or "/").split(",") if r.strip()] or ["/"]
    browsers = [b.strip().lower() for b in (browsers_arg or "chromium").split(",") if b.strip()]
    browsers = [b for b in browsers if b in BROWSERS] or ["chromium"]

    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        payload = {"status": "skipped",
                   "reason": "playwright is not installed (pip install playwright && playwright install)",
                   "failures": []}
        emit(["[SKIP] playwright not installed - WCAG audit NOT performed"], payload, json_mode)
        return 2

    source, axe_origin = find_axe(root)
    if not source:
        payload = {"status": "skipped",
                   "reason": "axe-core could not be located or downloaded",
                   "failures": []}
        emit(["[SKIP] axe-core unavailable - WCAG audit NOT performed"], payload, json_mode)
        return 2

    report = audit(url, routes, browsers, source, timeout_ms)
    report["axe_origin"] = axe_origin
    write_json(out_dir / "a11y-report.json", report)

    lines = ["=" * 62, f"ACCESSIBILITY AUDIT  [{url}]", "=" * 62]
    for bname, breport in report["browsers"].items():
        if breport.get("status") == "skipped":
            lines.append(f"[SKIP] {bname}: {breport.get('reason')}")
            continue
        for route, entry in breport["routes"].items():
            v = entry.get("violations") or []
            crit = [x for x in v if x.get("impact") in ("critical", "serious")]
            kb = entry.get("keyboard") or {}
            if not entry.get("axe_ran"):
                lines.append(f"[{bname}] {route}: AXE DID NOT RUN - {entry.get('axe_error', '')[:120]}")
                continue
            lines.append(f"[{bname}] {route}: {len(v)} axe violation(s), "
                         f"{len(crit)} critical/serious, {kb.get('tabbedElements', 0)} focus stops "
                         f"({kb.get('mode', 'tab')})")
            for x in v[:5]:
                lines.append(f"    - {x.get('impact')}: {x.get('id')} - {x.get('help','')[:60]}")
    lines.append("-" * 62)
    lines.append(f"blocking failures: {len(report['failures'])}")
    lines.append(f"report: {out_dir / 'a11y-report.json'}")
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
