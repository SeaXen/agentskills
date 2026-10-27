#!/usr/bin/env python3
"""Gate S - assistive technology contract (screen readers).

axe-core proves that an element is *technically* accessible.  A screen
reader user needs more: the same information, the same order and the same
announcements.  Those rules cannot be automated away, but the most common
breakages can be detected statically:

* every form control needs a programmatic label (<label for>, aria-label,
  aria-labelledby, wrapping label)
* errors must be wired to their field (aria-describedby / aria-errormessage)
* asynchronous updates need a live region (role=status / aria-live)
* focus must follow the DOM (no positive tabindex) and must not be hidden
  (no aria-hidden on a focusable element)
* a skip link and a <main> landmark must exist
* every page needs its own <title>
* dialogs need role="dialog" + aria-modal
* tables need header scopes

The absorbed ``accessibility_checker.py`` (frontend-design) runs as a signal.

Usage:
  python scripts/at_check.py --root <app_root> [--json]

Exit 0 = AT contract ok, 1 = blocking findings, 2 = nothing to check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, print_report, read_files, run_absorbed  # noqa: E402

MARKUP_EXT = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}
CONTROL = re.compile(r"<(input|select|textarea)\b[^>]*>", re.I)
CONTROL_ID = re.compile(r"\bid\s*=\s*['\"]([^'\"]+)['\"]", re.I)
LABEL_FOR = re.compile(r"<label\b[^>]*\bfor\s*=\s*['\"]([^'\"]+)['\"]", re.I)
ARIA_LABEL = re.compile(r"\baria-label(?:ledby)?\s*=", re.I)
TITLE_ATTR = re.compile(r"\btitle\s*=\s*['\"][^'\"]+['\"]", re.I)
LIVE_REGION = re.compile(r"role\s*=\s*['\"](status|alert)['\"]|aria-live\s*=", re.I)
ASYNC = re.compile(r"fetch\(|axios|XMLHttpRequest|await\s+\w+\(|\.then\(", re.I)
DESCRIBEDBY = re.compile(r"aria-describedby|aria-errormessage", re.I)
POSITIVE_TABINDEX = re.compile(r"tabindex\s*=\s*['\"]?([1-9]\d*)", re.I)
ARIA_HIDDEN = re.compile(r"<[^>]*aria-hidden\s*=\s*['\"]true['\"][^>]*>", re.I)
FOCUSABLE_HIDDEN = re.compile(r"<[^>]*aria-hidden\s*=\s*['\"]true['\"][^>]*"
                              r"(tabindex|<a\b|<button\b|<input\b)", re.I)
SKIP_LINK = re.compile(r"href\s*=\s*['\"]#(main|content|main-content|skip)", re.I)
MAIN_LANDMARK = re.compile(r"<main\b|role\s*=\s*['\"]main['\"]", re.I)
TITLE_TAG = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
DIALOG = re.compile(r"role\s*=\s*['\"]dialog['\"]|aria-modal", re.I)
TABLE = re.compile(r"<table\b", re.I)
TH = re.compile(r"<th\b[^>]*>", re.I)
BUTTON = re.compile(r"<button\b([^>]*)>(.*?)</button>", re.I | re.S)
LINK = re.compile(r"<a\b([^>]*)>(.*?)</a>", re.I | re.S)
IMG = re.compile(r"<img\b[^>]*>", re.I)
ALT = re.compile(r"\balt\s*=", re.I)
VOID_TEXT = re.compile(r"^\s*(&nbsp;|\s|<!--.*-->)*$", re.S)


def _label_ids(markup):
    return {m.group(1) for m in LABEL_FOR.finditer(markup)}


def _controls(markup):
    return CONTROL.findall(markup)


LAYOUT_TITLE = re.compile(r"\btitle\s*:\s*['\"`]([^'\"`]+)['\"`]", re.I)


def _root_layout(root: Path):
    """Return (path, text) of the framework root layout, if the app has one.

    Next.js / Nuxt / SvelteKit put the document shell (and usually the only
    <title>) in a root layout.  A page file that does not declare its own
    metadata therefore *inherits* that title - it is not a missing title.
    """
    candidates = [
        ("src/app/layout.tsx", "src/app/layout.jsx", "src/app/layout.js"),
        ("app/layout.tsx", "app/layout.jsx", "app/layout.js"),
        ("src/routes/+layout.svelte",),
        ("layouts/default.vue", "layouts/default.ts"),
    ]
    for group in candidates:
        for rel in group:
            path = root / rel
            if path.is_file():
                try:
                    return path, path.read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    return path, ""
    return None, ""


def _inherited_title(root: Path):
    """The title a page inherits from the root layout, or None.

    Only frameworks that really do inherit the document title count.  The
    knowledge lives in ``framework_profiles`` so the answer cannot drift
    between gates.
    """
    try:
        import framework_profiles
        if not framework_profiles.inherits_layout_title(root):
            return None
    except Exception:  # pragma: no cover
        pass
    path, text = _root_layout(root)
    if not path or not text:
        return None
    if not re.search(r"\bmetadata\b\s*[=:]", text) and not re.search(r"\buseHead\b", text):
        return None
    m = LAYOUT_TITLE.search(text)
    return m.group(1).strip()[:60] if m else None


def analyse(root: Path):
    files = [(p, t) for p, t in read_files(root, MARKUP_EXT)]
    # e-mail templates are documents, not application pages
    files = [(p, t) for p, t in files
             if not re.search(r"mail[-_]?templates?|emails?[/\\]|newsletter", str(p), re.I)]
    findings = []
    labelled = unlabelled = 0
    titles = []
    layout_path, _layout_text = _root_layout(root)
    inherited = _inherited_title(root)
    inherited_pages = []
    for path, text in files:
        rel = path.relative_to(root)
        labels = _label_ids(text)
        for control in _controls(text):
            if re.search(r"type\s*=\s*['\"]hidden['\"]", control, re.I):
                continue
            if re.search(r"type\s*=\s*['\"](submit|button|image|reset)['\"]", control, re.I):
                continue
            control_id = CONTROL_ID.search(control)
            has_label = (
                (control_id and control_id.group(1) in labels)
                or ARIA_LABEL.search(control)
                or TITLE_ATTR.search(control)
                or re.search(r"aria-labelledby", control, re.I)
            )
            if has_label:
                labelled += 1
            else:
                unlabelled += 1
                findings.append({"severity": "HIGH",
                                 "check": "form control without a programmatic label",
                                 "detail": f"{rel}: {control[:90]}"})
        m = TITLE_TAG.search(text)
        titles.append((str(rel), (m.group(1).strip()[:60] if m else "")))
        if not m or not m.group(1).strip():
            if layout_path is not None and path == layout_path:
                pass  # the layout is the source of the inherited title, not a page
            elif inherited:
                inherited_pages.append(str(rel))
                findings.append({"severity": "MEDIUM",
                                 "check": "page inherits the root layout title",
                                 "detail": f"{rel}: inherits {inherited!r} - every page then "
                                           "ships the same title (add per-page metadata)"})
            else:
                findings.append({"severity": "HIGH", "check": "page without a <title>",
                                 "detail": str(rel)})
        if not MAIN_LANDMARK.search(text):
            findings.append({"severity": "MEDIUM", "check": "no <main> landmark",
                             "detail": str(rel)})
        if not SKIP_LINK.search(text):
            findings.append({"severity": "LOW", "check": "no skip link",
                             "detail": str(rel)})
        if POSITIVE_TABINDEX.search(text):
            findings.append({"severity": "HIGH",
                             "check": "positive tabindex breaks focus order",
                             "detail": str(rel)})
        if FOCUSABLE_HIDDEN.search(text):
            findings.append({"severity": "HIGH",
                             "check": "focusable element hidden with aria-hidden",
                             "detail": str(rel)})
        if ASYNC.search(text) and not LIVE_REGION.search(text):
            findings.append({"severity": "MEDIUM",
                             "check": "async updates without a live region",
                             "detail": str(rel)})
        if re.search(r"error|invalid", text, re.I) and not DESCRIBEDBY.search(text):
            findings.append({"severity": "LOW",
                             "check": "form errors are not associated with their field",
                             "detail": str(rel)})
        for tag, name in ((BUTTON, "button"), (LINK, "link")):
            for m in tag.finditer(text):
                attrs, inner = m.group(1), m.group(2)
                if not inner.strip() and not ARIA_LABEL.search(attrs) and not TITLE_ATTR.search(attrs):
                    findings.append({"severity": "HIGH",
                                     "check": f"{name} without an accessible name",
                                     "detail": f"{rel}: <{name} {attrs[:60]}>"})
        for img in IMG.findall(text):
            if not ALT.search(img):
                findings.append({"severity": "HIGH", "check": "image without alt",
                                 "detail": f"{rel}: {img[:90]}"})
        if TABLE.search(text):
            for th in TH.findall(text):
                if not re.search(r"\bscope\s*=", th, re.I):
                    findings.append({"severity": "LOW",
                                     "check": "table header without scope",
                                     "detail": f"{rel}: {th[:60]}"})
                    break
    dupes = {}
    for name, title in titles:
        if title:
            dupes.setdefault(title, []).append(name)
    for title, names in dupes.items():
        if len(names) > 1:
            findings.append({"severity": "MEDIUM",
                             "check": "pages share the same <title>",
                             "detail": f"{title!r} in {', '.join(names[:4])}"})
    if inherited and len(inherited_pages) > 1:
        findings.append({"severity": "MEDIUM",
                         "check": "pages share the same <title>",
                         "detail": f"{inherited!r} in {', '.join(inherited_pages[:4])}"})
    return findings, {"labelled_controls": labelled, "unlabelled_controls": unlabelled,
                      "pages": len(files), "titles": titles,
                      "inherited_title": inherited, "inherited_pages": inherited_pages}


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

    result = GateResult("S", "ASSISTIVE TECHNOLOGY CONTRACT")
    findings, signals = analyse(root)
    if not signals["pages"]:
        result.skipped = True
        result.reason = "no markup found - the AT contract was NOT checked"
        payload = print_report(result, json_mode)
        emit([], payload, json_mode)
        return 2

    for finding in findings:
        if finding["severity"] in ("HIGH", "CRITICAL"):
            result.fail(finding["check"], finding["detail"], finding["severity"])
        else:
            result.warn(finding["check"], finding["detail"])
    result.add("every form control has a programmatic label",
               signals["unlabelled_controls"] == 0, True,
               f"{signals['labelled_controls']} labelled, "
               f"{signals['unlabelled_controls']} unlabelled")

    checker = run_absorbed("accessibility_checker.py", root, timeout=120)
    if checker.get("available"):
        result.add("absorbed accessibility_checker.py reports no issues",
                   bool(checker.get("ok")), False, checker.get("detail", ""))
    else:
        result.warn("absorbed accessibility_checker.py available", checker.get("detail", ""))

    payload = print_report(result, json_mode, extra={"signals": signals})
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
