#!/usr/bin/env python3
"""Mobile readiness - the absorbed mobile-design skill plus web mobile rules.

``mobile_audit.py`` (mobile-design) is run as a subprocess for native
projects (React Native / Flutter).  On top of that this script checks the
web rules that matter on a phone:

* a responsive viewport meta
* touch targets of at least 44x44 CSS px (nav links, buttons, form controls)
* no hover-only interactions (the content must be reachable without a mouse)
* a usable font size on small screens
* no fixed-width layout that forces horizontal scrolling
* orientation / safe-area handling for full-bleed layouts

Usage:
  python scripts/mobile_check.py --root <app_root> [--json]

Exit 0 = mobile ready, 1 = findings, 2 = nothing to check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, print_report, read_files, run_absorbed  # noqa: E402

STYLE_EXT = {".css", ".scss", ".less"}
MARKUP_EXT = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"}

VIEWPORT = re.compile(r"<meta[^>]+name\s*=\s*['\"]viewport['\"][^>]*", re.I)
VIEWPORT_OK = re.compile(r"<meta[^>]+content\s*=\s*['\"][^'\"]*width\s*=\s*device-width", re.I)
TAP_RULES = re.compile(r"(?is)([^{}]*)\{([^{}]*)\}")
SMALL_TEXT = re.compile(r"font-size\s*:\s*(\d+)px", re.I)
FIXED_WIDTH = re.compile(r"(?<!max-)width\s*:\s*(\d{3,})px", re.I)
HOVER_ONLY = re.compile(r"(?i):hover\s*\{[^}]*opacity\s*:\s*0")
SAFE_AREA = re.compile(r"(?i)env\(\s*safe-area-inset|viewport-fit\s*=\s*cover")
TOUCH_SELECTORS = ("a", "button", "input", "select", "textarea", "[role=button]")


def _framework_default_viewport(root):
    """Frameworks that inject a responsive viewport meta at runtime.

    A missing ``<meta name="viewport">`` in the source of such a project is not
    a defect, so the gate must not report it as one.  The knowledge lives in
    ``framework_profiles`` so every gate asks the same question the same way.
    """
    try:
        import framework_profiles
    except Exception:  # pragma: no cover
        return ""
    if not framework_profiles.injects_viewport(root):
        return ""
    return framework_profiles.profile(root).get("label", "")


def _touch_targets(styles):
    """Return the declared min sizes found in the CSS."""
    small = []
    found = 0
    for _path, text in styles:
        for selector, body in TAP_RULES.findall(text):
            selector = selector.strip()
            if not any(sel in selector for sel in TOUCH_SELECTORS):
                continue
            found += 1
            size = re.search(r"(?i)(?:min-)?(?:width|height)\s*:\s*(\d+)px", body)
            padding = re.search(r"(?i)padding\s*:\s*(\d+)px\s+(\d+)px", body)
            if size and int(size.group(1)) < 44:
                small.append(f"{selector} -> {size.group(1)}px")
            elif padding and int(padding.group(2)) < 16:
                small.append(f"{selector} -> padding {padding.group(2)}px")
    return found, small


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    root_arg = "."
    i = 0
    while i < len(args):
        if args[i] == "--root" and i + 1 < len(args):
            root_arg = args[i + 1]
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

    result = GateResult("A+", "MOBILE READINESS")
    styles = [(p, t) for p, t in read_files(root, STYLE_EXT)]
    markups = [(p, t) for p, t in read_files(root, MARKUP_EXT)]
    if not styles and not markups:
        result.skipped = True
        result.reason = "no markup or styles found - mobile readiness not checked"
        payload = print_report(result, json_mode)
        emit([], payload, json_mode)
        return 2

    markup_blob = "\n".join(t for _p, t in markups)
    style_blob = "\n".join(t for _p, t in styles)

    has_viewport = bool(VIEWPORT.search(markup_blob) and VIEWPORT_OK.search(markup_blob))
    framework_viewport = _framework_default_viewport(root)
    if has_viewport:
        result.add("a responsive viewport meta is present", True, True,
                   "declared in source")
    elif framework_viewport:
        # Next.js (App Router) and Nuxt inject ``width=device-width, initial-scale=1``
        # at runtime, so a missing declaration in source is NOT a defect - but a
        # custom viewport (user-scalable, viewport-fit) still has to be set
        # explicitly in the framework's own metadata export.
        result.add("a responsive viewport meta is present", True, True,
                   f"not declared in source, but {framework_viewport} injects the default "
                   "responsive viewport at runtime (set an explicit viewport export to "
                   "control user-scalable / viewport-fit)")
    else:
        result.add("a responsive viewport meta is present", False, True,
                   "add <meta name=viewport content='width=device-width, initial-scale=1'>")

    found, small = _touch_targets(styles)
    if found:
        result.add("touch targets are at least 44x44 CSS px", not small, True,
                   "; ".join(small[:4]) if small else f"{found} interactive rule(s) checked")
    else:
        result.warn("touch targets are at least 44x44 CSS px",
                    "no explicit sizing found for interactive elements")

    result.add("no hover-only interactions", not HOVER_ONLY.search(style_blob), True,
               "content that only appears on :hover is unreachable on touch")

    small_fonts = [s for s in SMALL_TEXT.findall(style_blob) if int(s) < 14]
    result.add("body text is at least 14px on small screens", not small_fonts, False,
               f"{len(small_fonts)} declaration(s) below 14px" if small_fonts else "")

    fixed = [w for w in FIXED_WIDTH.findall(style_blob) if int(w) > 480]
    result.add("no fixed width forces horizontal scrolling", not fixed, False,
               f"{len(fixed)} fixed width(s) above 480px" if fixed else "")

    result.warn("safe-area insets are handled",
                "not needed for every layout, but required for full-bleed mobile UI")

    native = run_absorbed("mobile_audit.py", root, timeout=240)
    if native.get("available"):
        result.add("absorbed mobile_audit.py reports compliance", bool(native.get("ok")),
                   False, native.get("detail", ""))
    else:
        result.warn("absorbed mobile_audit.py available", native.get("detail", ""))

    payload = print_report(result, json_mode)
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
