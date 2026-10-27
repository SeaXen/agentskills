#!/usr/bin/env python
"""Web Interface Guidelines checker (absorbed from the ``web-design-guidelines`` skill).

The upstream skill fetches the Vercel "Web Interface Guidelines" and asks an agent to
review the files by hand. This module turns the machine-checkable subset of those
rules into deterministic checks that report findings in the same terse format:

    src/app/page.tsx:42 - form control has no label

Every rule carries a severity:

* ``high``   - an accessibility / correctness problem (icons without a name, inputs
                without a label, blocked zoom, removed focus outlines, ...).
* ``medium`` - a quality problem (missing image dimensions, ``transition: all``,
                layout reads during render, ...).

Only ``high`` findings fail the gate; ``medium`` findings are reported as warnings.
That keeps the gate strict about correctness without failing a build over taste.

Rules that cannot be expressed as a pattern are listed in ``MANUAL_CHECKS`` and are
printed with the report so a human can still work through them.

Exit codes
----------
0   no high-severity finding (medium findings are printed as warnings)
1   at least one high-severity finding
2   the rules could not be loaded (no upstream file and no bundled snapshot)

Usage
-----
    python scripts/web_guidelines.py --root <app> [--json] [--refresh]
"""

from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CACHE_FILE = SCRIPT_DIR / ".cache" / "web-interface-guidelines.md"
SNAPSHOT_FILE = SCRIPT_DIR.parent / "references" / "web-interface-guidelines.md"
UPSTREAM_URL = "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md"

UI_EXT = {".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".html", ".htm", ".astro", ".mdx"}
STYLE_EXT = {".css", ".scss", ".sass", ".less"}
SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", "out", ".next", ".nuxt", ".svelte-kit",
    "coverage", ".vercel", ".netlify", ".wrangler", ".turbo", ".cache", ".pytest_cache",
    "__pycache__", ".venv", "venv", "target", "qa", "docs",
}

# (id, section, severity, extensions-or-None(for all), compiled regex, message)
RULES: list[tuple[str, str, str, set[str] | None, str, str]] = [
    # --- accessibility -----------------------------------------------------
    ("a11y-img-alt", "Accessibility", "high", UI_EXT,
     r"<img\b(?![^>]*\balt\s*=)[^>]*>", "image has no alt attribute"),
    ("a11y-input-label", "Accessibility", "high", UI_EXT,
     r"<(input|select|textarea)\b(?![^>]*\b(aria-label|aria-labelledby|id)\s*=)[^>]*>",
     "form control has no label, aria-label or id"),
    ("a11y-icon-button", "Accessibility", "high", UI_EXT,
     r"<button\b(?![^>]*aria-label)[^>]*>\s*<(svg|img|i|span)\b",
     "icon-only button has no accessible name"),
    ("a11y-div-click", "Accessibility", "high", UI_EXT,
     r"<(div|span)\b[^>]*\bon(Click|KeyDown)\s*=",
     "clickable div/span should be a <button> with keyboard support"),
    ("a11y-anchor-click", "Accessibility", "medium", UI_EXT,
     r"<a\b[^>]*\bonClick\s*=",
     "navigation should use a link, not an onClick handler"),
    ("a11y-html-lang", "Accessibility", "high", {".html", ".htm"},
     r"<html\b(?![^>]*\blang\s*=)[^>]*>", "html element has no lang attribute"),
    ("a11y-aria-no-role", "Accessibility", "medium", UI_EXT,
     r"<(div|span)\b[^>]*aria-label(?![^>]*\brole\s*=)[^>]*>",
     "aria-label on a non-interactive element without a role"),
    ("a11y-live-region", "Accessibility", "medium", UI_EXT,
     r"aria-live\s*=\s*[\"']assertive[\"']",
     "assertive live region interrupts the screen reader; use polite"),
    ("a11y-autofocus", "Accessibility", "medium", UI_EXT,
     r"\bautoFocus\b", "autoFocus should be used sparingly"),
    ("a11y-img-dimensions", "Images", "medium", UI_EXT,
     r"<img\b(?![^>]*\bwidth\s*=)(?![^>]*\bheight\s*=)[^>]*>",
     "image has no explicit width/height (causes layout shift)"),

    # --- focus -------------------------------------------------------------
    ("focus-outline-none", "Focus states", "high", {".css", ".scss", ".sass", ".less", ".jsx", ".tsx", ".vue", ".svelte"},
     r"outline\s*:\s*(none|0)\b", "outline removed without a replacement focus style"),
    ("focus-outline-none-util", "Focus states", "high", UI_EXT,
     r"\boutline-none\b", "outline-none used without a :focus-visible replacement"),
    ("focus-visible-missing", "Focus states", "medium", STYLE_EXT,
     r":focus-visible\b", "focus-visible used but :focus may be the only fallback"),

    # --- forms -------------------------------------------------------------
    ("form-no-autocomplete", "Forms", "medium", UI_EXT,
     r"<input\b(?![^>]*\bautoComplete\s*=)[^>]*>",
     "input has no autoComplete attribute"),
    ("form-no-type", "Forms", "medium", UI_EXT,
     r"<input\b(?![^>]*\btype\s*=)[^>]*>", "input has no type attribute"),
    ("form-block-paste", "Forms", "high", UI_EXT,
     r"onPaste\s*=\s*\{[^}]*preventDefault", "paste is blocked on this field"),

    # --- interaction / zoom ------------------------------------------------
    ("zoom-blocked", "Anti-patterns", "high", {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"},
     r"user-scalable\s*=\s*[\"']?no|maximum-scale\s*=\s*1(?!\.0)",
     "viewport blocks zooming (user-scalable=no / maximum-scale=1)"),

    # --- animation ---------------------------------------------------------
    ("anim-transition-all", "Animation", "medium", STYLE_EXT,
     r"transition\s*:\s*all\b", "transition: all animates every property"),
    ("anim-infinite", "Animation", "medium", STYLE_EXT,
     r"animation(?:-duration)?\s*:[^;]*\binfinite\b",
     "infinite animation needs a prefers-reduced-motion fallback"),

    # --- performance / hydration ------------------------------------------
    ("perf-layout-read", "Performance", "medium", {".jsx", ".tsx"},
     r"\b(getBoundingClientRect|offsetHeight|offsetWidth|scrollTop|clientHeight|clientWidth)\b",
     "layout read during render (batch reads/writes, or use a ref in an effect)"),
    ("perf-random-render", "Performance", "medium", {".jsx", ".tsx"},
     r"\bMath\.random\s*\(\s*\)", "random value during render (hydration mismatch risk)"),
    ("perf-date-render", "Performance", "medium", {".jsx", ".tsx"},
     r"\bnew Date\s*\(\s*\)", "current date during render (hydration mismatch risk)"),

    # --- security ----------------------------------------------------------
    ("sec-target-blank", "Security", "high", UI_EXT,
     r"target\s*=\s*[\"']_blank[\"'](?![^>]*rel\s*=\s*[\"'][^\"']*noopener)",
     "target=_blank without rel=noopener"),
    ("sec-dangerous-html", "Security", "high", UI_EXT,
     r"\bdangerouslySetInnerHTML\b", "raw HTML injection - sanitize the value"),
    ("sec-innerhtml", "Security", "high", {".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"},
     r"\.innerHTML\s*=", "innerHTML assignment can introduce an XSS sink"),
    ("sec-eval", "Security", "high", {".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"},
     r"\beval\s*\(", "eval() executes arbitrary code"),

    # --- copy / i18n -------------------------------------------------------
    ("copy-three-dots", "Typography", "medium", UI_EXT,
     r">\s*\.\.\.\s*<|\"\\.\\.\\.\"|'\\.\\.\\.'",
     "use the ellipsis character … instead of three dots"),
    ("i18n-locale-date", "Locale & i18n", "medium", {".jsx", ".tsx", ".js", ".ts"},
     r"toLocale(Date|Time)String\s*\(\s*\)", "locale-dependent formatting without an explicit locale"),

    # --- navigation --------------------------------------------------------
    ("nav-placeholder-href", "Navigation & state", "medium", UI_EXT,
     r"<a\b[^>]*href\s*=\s*[\"']#[\"']", "placeholder link - give it a real destination"),
]

COMPILED = [
    (rid, section, sev, exts, re.compile(pattern, re.IGNORECASE), message)
    for rid, section, sev, exts, pattern, message in RULES
]

MANUAL_CHECKS = [
    "the heading hierarchy is correct (no skipped levels) and every page has one h1",
    "async updates announce themselves (aria-live=polite) and never move focus unexpectedly",
    "loading states are announced and end with an ellipsis (…); skeletons do not trap focus",
    "the destructive action is confirmed or undoable, and the URL reflects the current state",
    "interactive targets are at least 44x44 px and every gesture has a button alternative",
    "form errors are inline, mention the fix and move focus to the first invalid field",
    "the user is warned before leaving a form with unsaved changes",
    "date, number and currency are formatted with Intl for the active locale",
    "dark mode sets color-scheme and the native select keeps a readable background",
    "reduced motion is honoured for every animation, including looping and autoplaying media",
    "long user content is truncated or wrapped without breaking the layout (min-w-0, line-clamp)",
    "the media has captions, controls are keyboard reachable and the fallback is readable",
]

SKIP_MARKERS = ("node_modules", "/.git/", "/dist/", "/build/", "/.next/", "/qa/", "/docs/")


# --------------------------------------------------------------------------- #
# rules file
# --------------------------------------------------------------------------- #
def load_rules_text(refresh: bool = False) -> tuple[str | None, str]:
    """Return (text, source). Text is None when no rules file could be found."""
    if refresh:
        try:
            CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(UPSTREAM_URL, timeout=20) as resp:
                data = resp.read().decode("utf-8", "replace")
            CACHE_FILE.write_text(data, encoding="utf-8")
            return data, "upstream (refreshed)"
        except (urllib.error.URLError, OSError, TimeoutError):
            pass
    if CACHE_FILE.exists():
        try:
            return CACHE_FILE.read_text(encoding="utf-8", errors="replace"), "cache"
        except OSError:
            pass
    if SNAPSHOT_FILE.exists():
        try:
            return SNAPSHOT_FILE.read_text(encoding="utf-8", errors="replace"), "bundled snapshot"
        except OSError:
            pass
    return None, "unavailable"


# --------------------------------------------------------------------------- #
# scanning
# --------------------------------------------------------------------------- #
def iter_ui_files(root: Path):
    """Yield the UI/style files of the project.

    The skip check runs on the path *relative to the project* so that a
    directory which merely contains a marker somewhere in the absolute path
    cannot hide the whole app.
    """
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        try:
            rel = path.relative_to(root).as_posix().lower()
        except ValueError:
            rel = path.as_posix().lower()
        if any(marker in rel for marker in SKIP_MARKERS):
            continue
        if path.suffix.lower() in UI_EXT | STYLE_EXT:
            yield path


def scan_text(text: str, ext: str, path_label: str) -> list[dict]:
    findings: list[dict] = []
    lines = text.splitlines()
    for rid, section, severity, exts, pattern, message in COMPILED:
        if exts and ext not in exts:
            continue
        for number, line in enumerate(lines, 1):
            if len(line) > 4000:
                line = line[:4000]
            if pattern.search(line):
                findings.append({
                    "rule": rid,
                    "section": section,
                    "severity": severity,
                    "file": path_label,
                    "line": number,
                    "message": message,
                    "excerpt": line.strip()[:160],
                })
                break  # one finding per rule per file keeps the output readable
    return findings


def analyse(root: Path) -> dict:
    findings: list[dict] = []
    files_checked = 0
    for path in iter_ui_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        files_checked += 1
        label = path.relative_to(root).as_posix()
        findings.extend(scan_text(text, path.suffix.lower(), label))
    high = [f for f in findings if f["severity"] == "high"]
    medium = [f for f in findings if f["severity"] == "medium"]
    return {
        "root": str(root),
        "status": "ok",
        "files_checked": files_checked,
        "rules": len(RULES),
        "findings": findings,
        "high": len(high),
        "medium": len(medium),
        "manual_checks": MANUAL_CHECKS,
    }


def format_report(result: dict) -> list[str]:
    lines: list[str] = ["WEB INTERFACE GUIDELINES"]
    if not result["files_checked"]:
        lines.append("[SKIP] no UI files were found to review")
        return lines
    lines.append(
        f"{result['files_checked']} file(s) checked against {result['rules']} rules "
        f"-> {result['high']} high, {result['medium']} medium finding(s)"
    )
    by_file: dict[str, list[dict]] = {}
    for finding in result["findings"]:
        by_file.setdefault(finding["file"], []).append(finding)
    for name in sorted(by_file):
        lines.append("")
        lines.append(name)
        for finding in sorted(by_file[name], key=lambda f: f["line"]):
            mark = "FAIL" if finding["severity"] == "high" else "warn"
            lines.append(
                f"  {name}:{finding['line']} - [{finding['section']}] {finding['message']} ({mark})"
            )
    lines.append("")
    lines.append("Manual checks (a human still has to confirm these):")
    for item in result["manual_checks"]:
        lines.append(f"  - {item}")
    return lines


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def parse_args(argv: list[str]) -> dict:
    opts = {"root": ".", "json": False, "refresh": False}
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg == "--root" and index + 1 < len(argv):
            opts["root"] = argv[index + 1]
            index += 2
            continue
        if arg == "--json":
            opts["json"] = True
        elif arg == "--refresh":
            opts["refresh"] = True
        elif arg in ("-h", "--help"):
            print(__doc__)
            raise SystemExit(0)
        index += 1
    return opts


def main(argv: list[str] | None = None) -> int:
    opts = parse_args(list(sys.argv[1:] if argv is None else argv))
    root = Path(opts["root"]).expanduser().resolve()
    if not root.is_dir():
        message = f"[FAIL] not a directory: {root}"
        if opts["json"]:
            print(json.dumps({"status": "fail", "error": message}, indent=2))
        else:
            print(message)
        return 1

    text, source = load_rules_text(refresh=opts["refresh"])
    if text is None:
        message = (
            "[SKIP] the Web Interface Guidelines could not be loaded "
            f"(no upstream file at {UPSTREAM_URL} and no bundled snapshot) - "
            "this gate was NOT measured"
        )
        if opts["json"]:
            print(json.dumps({"status": "skipped", "reason": message}, indent=2))
        else:
            print(message)
        return 2

    result = analyse(root)
    result["rules_source"] = source
    result["rules_url"] = UPSTREAM_URL
    if opts["json"]:
        print(json.dumps(result, indent=2))
    else:
        for line in format_report(result):
            print(line)
    return 1 if result["high"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

