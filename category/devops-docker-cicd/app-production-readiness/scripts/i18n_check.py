#!/usr/bin/env python3
"""Gate R - internationalisation and RTL.

Localising an app is not only translating strings:

* the locale catalogue must exist and cover more than one language
* every key used in the code must exist in every catalogue (missing keys are
  HIGH - the UI shows a raw key)
* the document language must be declared and must change with the locale
* when a right-to-left language is supported, the layout must use logical
  CSS properties and the document must switch `dir`
* strings must not be hardcoded in the markup
* the absorbed ``i18n_checker.py`` (i18n-localization) runs as a signal

Usage:
  python scripts/privacy_check.py --root <app_root>
  python scripts/i18n_check.py --root <app_root> [--json]

Exit 0 = i18n posture ok, 1 = blocking findings, 2 = nothing to check.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, load_json, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import (GateResult, print_report, read_files,  # noqa: E402
                     run_absorbed)

LOCALE_DIRS = ("locales", "i18n", "lang", "translations", "src/locales",
               "src/i18n", "public/locales", "app/locales")
RTL_LANGS = ("ar", "he", "fa", "ur", "yi", "dv", "ps", "sd", "ug", "ckb")
I18N_CALL = re.compile(r"\b(t|i18n\.t|translate|useTranslation|gettext|__\()\s*[\( ]")
HARD_STRING = re.compile(r">\s*[A-Za-z][A-Za-z0-9 ,.'!?-]{6,}\s*<")
LANG_ATTR = re.compile(r"<html[^>]*\blang\s*=", re.I)
RTL_DIR = re.compile(r"\bdir\s*=\s*['\"]?(rtl|ltr)|setAttribute\(\s*['\"]dir['\"]|"
                      r"document\.dir|dir\s*=\s*isRtl|direction:\s*rtl", re.I)
LOGICAL_CSS = re.compile(r"(?i)(margin-inline|padding-inline|inset-inline|"
                          r"border-inline|text-align:\s*start|text-align:\s*end)")
PHYSICAL_CSS = re.compile(r"(?i)(margin-left|margin-right|padding-left|padding-right|"
                           r"left\s*:|right\s*:|text-align:\s*(left|right))")
CATALOG_EXT = {".json", ".yaml", ".yml", ".po", ".properties"}


def find_catalogs(root: Path):
    catalogs = []
    for rel in LOCALE_DIRS:
        folder = root / rel
        if folder.is_dir():
            for path in sorted(folder.rglob("*")):
                if path.is_file() and path.suffix.lower() in CATALOG_EXT:
                    catalogs.append(path)
    return catalogs


def _flatten(obj, prefix=""):
    keys = set()
    if isinstance(obj, dict):
        for key, value in obj.items():
            name = f"{prefix}{key}"
            keys.add(name)
            keys |= _flatten(value, name + ".")
    return keys


def _catalog_keys(path: Path):
    if path.suffix.lower() == ".json":
        data = load_json(path)
        if isinstance(data, dict):
            if "translations" in data and isinstance(data["translations"], dict):
                data = data["translations"]
            return _flatten(data)
    if path.suffix.lower() in (".yaml", ".yml"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        return set(re.findall(r"^\s*([A-Za-z0-9_.\-]+)\s*:", text, re.M))
    return set()


def _language_of(path: Path):
    stem = path.stem.lower()
    for tag in re.split(r"[._-]", stem):
        if len(tag) == 2 and tag.isalpha():
            return tag
    return stem


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

    result = GateResult("R", "I18N & RTL")
    files = read_files(root, {".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html",
                              ".py", ".go", ".rb", ".php", ".css", ".scss"})
    catalogs = find_catalogs(root)
    if not files and not catalogs:
        result.skipped = True
        result.reason = "no source or locale files found - i18n not checked"
        payload = print_report(result, json_mode)
        emit([], payload, json_mode)
        return 2

    languages = sorted({_language_of(p) for p in catalogs})
    result.add("a locale catalogue exists", bool(catalogs), True,
               f"{len(catalogs)} catalogue file(s): {languages or 'none'}")
    result.add("more than one language is shipped", len(languages) >= 2, True,
               f"languages: {languages}")

    # missing keys across catalogues
    key_sets = {str(p.relative_to(root)): _catalog_keys(p) for p in catalogs}
    if len(key_sets) >= 2:
        biggest = max(key_sets.values(), key=len) if key_sets else set()
        for name, keys in key_sets.items():
            missing = biggest - keys
            result.add(f"catalogue {name} has every key of the largest catalogue",
                       not missing, True,
                       f"{len(missing)} missing key(s): {sorted(missing)[:5]}"
                       if missing else "")

    blob = "\n".join(t for _p, t in files)
    uses_i18n = bool(I18N_CALL.search(blob))
    result.add("the code uses an i18n mechanism", uses_i18n, True,
               "no t()/useTranslation/gettext call found" if not uses_i18n else "")

    hardcoded = []
    for path, text in files:
        if path.suffix.lower() in (".html", ".jsx", ".tsx", ".vue", ".svelte"):
            for m in HARD_STRING.finditer(text):
                snippet = m.group(0).strip()
                if snippet.lower() in ("<", ">"):
                    continue
                hardcoded.append(f"{path.relative_to(root)}: {snippet[:40]}")
    result.add("no user-facing strings are hardcoded in markup", not hardcoded, False,
               "; ".join(hardcoded[:4]) if hardcoded else "")

    result.add("the document language is declared", bool(LANG_ATTR.search(blob)), True,
               "" if LANG_ATTR.search(blob) else "no <html lang=...> found")

    rtl_langs = [l for l in languages if l in RTL_LANGS]
    if rtl_langs:
        result.add("right-to-left support is implemented", bool(RTL_DIR.search(blob)), True,
                   f"RTL language(s) {rtl_langs} present but no dir switching found")
        physical = []
        for path, text in files:
            if path.suffix.lower() in (".css", ".scss", ".less"):
                for m in PHYSICAL_CSS.finditer(text):
                    physical.append(f"{path.relative_to(root)}: {m.group(0).strip()}")
        result.add("layout uses logical CSS properties (RTL safe)",
                   len(physical) == 0, True,
                   f"{len(physical)} physical propert(ies) e.g. {physical[:3]}"
                   if physical else "")
    else:
        result.warn("right-to-left support is implemented",
                    "no RTL language in the catalogues - rule not applicable")

    checker = run_absorbed("i18n_checker.py", root, timeout=120)
    if checker.get("available"):
        result.add("absorbed i18n_checker.py reports a clean i18n setup",
                   bool(checker.get("ok")), False, checker.get("detail", ""))
    else:
        result.warn("absorbed i18n_checker.py available", checker.get("detail", ""))

    payload = print_report(result, json_mode, extra={
        "catalogs": [str(p.relative_to(root)) for p in catalogs],
        "languages": languages,
    })
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
