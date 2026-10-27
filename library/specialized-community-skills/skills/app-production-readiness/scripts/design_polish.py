#!/usr/bin/env python3
"""Gate C - design polish, measured instead of vibes.

The old skill graded "design polish 10/10" by reading the app and feeling
good about it.  That is exactly the kind of claim that inflates, so this
script turns polish into a rubric:

  1. Typography      - scale, minimum size, line height, family
  2. Colour          - tokens instead of hardcoded hex, readable body colours
  3. Spacing rhythm  - one spacing scale, mostly 4/8pt multiples
  4. Motion          - reduced-motion honoured, no runaway animations
  5. Consistency     - no inline styling, shared design tokens
  6. Content states  - loading / empty / error states, no filler copy
  7. Layout          - responsive, no fixed-width containers

Every dimension is scored 0..1; the gate needs a weighted score of >= 0.85
and no dimension below 0.50.  The absorbed ``ux_audit.py`` (frontend-design)
runs as an extra signal.  The rubric alone is not enough: a human has to sign
off on taste.  That decision is stored in ``qa/signoff/design.json`` and is
bound to the exact rubric measurement (a fingerprint), so a stale sign-off can
never be reused.  With a valid sign-off the gate becomes VERIFIED; without
one it stays UNVERIFIABLE in ``verify_claims.py``.

Usage:
  python scripts/design_polish.py --root <app_root> [--json]
  python scripts/design_polish.py --root <app_root> --json > qa/design-polish.json
  python scripts/design_polish.py --root <app_root> --record-signoff \
      --reviewer "Ada" --verdict approved --notes "hierarchy and rhythm are fine"

Exit 0 = rubric met, 1 = rubric not met, 2 = nothing to judge.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, load_json, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, print_report, read_files, run_absorbed  # noqa: E402

WEIGHTS = {
    "typography": 0.20,
    "colour": 0.15,
    "spacing": 0.15,
    "motion": 0.10,
    "consistency": 0.15,
    "content_states": 0.15,
    "layout": 0.10,
}
THRESHOLD = 0.85
MIN_DIMENSION = 0.50

STYLE_EXT = {".css", ".scss", ".sass", ".less"}
MARKUP_EXT = {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro"}
SCRIPT_EXT = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".vue", ".svelte"}

COLOR_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b|\brgba?\(|\bhsla?\(")
SIZE_RE = re.compile(r"font-size\s*:\s*([0-9.]+)(px|rem|em|%)", re.I)
SPACING_RE = re.compile(r"(?:padding|margin|gap|row-gap|column-gap)\s*:\s*"
                         r"([0-9.]+)(px|rem|em)", re.I)
INLINE_STYLE_RE = re.compile(r'style\s*=\s*["\'][^"\']*(?:color|background)', re.I)
FILLER_RE = re.compile(r"(?i)\b(lorem ipsum|dolor sit amet|placeholder text|"
                        r"tbd|todo text|xxx+)\b")
STATE_WORDS = ("loading", "empty", "error", "not found", "spinner", "skeleton")


def _collect(root: Path):
    styles, markups, scripts = [], [], []
    for path, text in read_files(root):
        ext = path.suffix.lower()
        if ext in STYLE_EXT:
            styles.append((path, text))
        elif ext in MARKUP_EXT:
            markups.append((path, text))
        if ext in SCRIPT_EXT:
            scripts.append((path, text))
    return styles, markups, scripts


def _dim_typography(styles, markups):
    checks = []
    sizes = []
    too_small = []
    family = False
    line_height = False
    for _path, text in styles:
        for m in SIZE_RE.finditer(text):
            value = float(m.group(1))
            unit = m.group(2).lower()
            sizes.append(value)
            px = value if unit == "px" else (value * 16 if unit == "rem" else None)
            if px is not None and px < 12:
                too_small.append(f"{m.group(0)}")
        if re.search(r"font-family\s*:", text, re.I):
            family = True
        if re.search(r"line-height\s*:", text, re.I):
            line_height = True
    scale = len({round(s) for s in sizes}) >= 3
    checks.append(("type scale has at least three distinct sizes", scale,
                   f"{len({round(s) for s in sizes})} distinct font sizes found"))
    checks.append(("no font-size below 12px", not too_small,
                   f"offenders: {too_small[:5]}" if too_small else ""))
    checks.append(("font-family declared", family, ""))
    checks.append(("line-height declared", line_height, ""))
    if not sizes:
        checks.append(("inline/markup typography present", bool(markups),
                       "no CSS typography found - styling may be inline"))
    return checks


def _dim_colour(styles, markups):
    checks = []
    token_count = 0
    hardcoded = 0
    body_colour = body_bg = False
    for _path, text in styles:
        token_count += len(re.findall(r"--[a-z0-9-]+\s*:", text, re.I))
        hardcoded += len(COLOR_RE.findall(text))
        if re.search(r"(?im)^\s*body\s*\{[^}]*color\s*:", text):
            body_colour = True
        if re.search(r"(?im)^\s*body\s*\{[^}]*background", text):
            body_bg = True
    checks.append(("design tokens used for colour (>= 3 custom properties)",
                   token_count >= 3, f"{token_count} custom properties"))
    checks.append(("body text colour declared", body_colour, ""))
    checks.append(("body background declared", body_bg, ""))
    checks.append(("hardcoded colours are the minority",
                   hardcoded == 0 or token_count >= hardcoded,
                   f"{hardcoded} hardcoded colour literals vs {token_count} tokens"))
    return checks


def _dim_spacing(styles):
    checks = []
    values = []
    token_values = []
    for _path, text in styles:
        for m in SPACING_RE.finditer(text):
            try:
                val = float(m.group(1))
            except ValueError:
                continue
            if m.group(2).lower() == "px":
                values.append(val)
        # a spacing scale expressed as design tokens counts too
        for m in re.finditer(r"--(?:space|gap|size)-\d+\s*:\s*([0-9.]+)px", text, re.I):
            try:
                token_values.append(float(m.group(1)))
            except ValueError:
                pass
    scale_values = values + token_values
    off_scale = [v for v in values if v % 4 != 0]
    checks.append(("a spacing scale exists (>= 5 spacing values)",
                   len(set(scale_values)) >= 5,
                   f"{len(set(scale_values))} distinct spacing values"))
    checks.append(("spacing values follow a 4/8pt scale", len(off_scale) <= max(1, len(values) * 0.15),
                   f"{len(off_scale)} off-scale value(s): {sorted(set(off_scale))[:6]}"))
    return checks


def _dim_motion(styles):
    checks = []
    reduced = False
    runaway = []
    slow = []
    for _path, text in styles:
        if "prefers-reduced-motion" in text:
            reduced = True
        for m in re.finditer(r"animation[^;{]*infinite", text, re.I):
            runaway.append(m.group(0)[:60])
        for m in re.finditer(r"transition[^;{]*?([0-9.]+)m?s", text, re.I):
            try:
                dur = float(m.group(1))
            except ValueError:
                continue
            if m.group(1).endswith("s") and dur > 0.5:
                slow.append(dur)
    checks.append(("prefers-reduced-motion honoured", reduced,
                   "add @media (prefers-reduced-motion: reduce)"))
    checks.append(("no infinite animation without a reduced-motion guard",
                   not runaway, f"{len(runaway)} infinite animation(s)"))
    checks.append(("transitions stay under 500ms", not slow, f"slow: {slow[:5]}"))
    return checks


def _dim_consistency(styles, markups):
    checks = []
    inline = 0
    for _path, text in markups:
        inline += len(INLINE_STYLE_RE.findall(text))
    token_files = [p.name for p, _t in styles
                   if re.search(r"--[a-z0-9-]+\s*:", p.read_text(encoding="utf-8",
                                                                 errors="ignore"), re.I)]
    checks.append(("no inline colour styling in markup", inline == 0,
                   f"{inline} inline style attribute(s)"))
    checks.append(("a shared token/variable stylesheet exists", bool(token_files),
                   ", ".join(token_files[:3])))
    return checks


def _dim_content_states(markups, scripts):
    checks = []
    blob = "\n".join(t for _p, t in markups + scripts).lower()
    present = [w for w in STATE_WORDS if w in blob]
    checks.append(("loading / empty / error states are handled",
                   len(present) >= 2, f"found: {present or 'none'}"))
    filler = []
    for path, text in markups:
        if FILLER_RE.search(text):
            filler.append(path.name)
    checks.append(("no filler or placeholder copy", not filler, ", ".join(filler[:3])))
    return checks


def _dim_layout(styles, markups):
    checks = []
    media = 0
    fixed = 0
    flex_grid = 0
    for _path, text in styles:
        media += len(re.findall(r"@media\s*\(", text, re.I))
        fixed += len(re.findall(r"(?<!max-)width\s*:\s*[0-9]{3,}px", text))
        flex_grid += len(re.findall(r"display\s*:\s*(flex|grid)", text, re.I))
    checks.append(("responsive breakpoints present", media >= 1,
                   f"{media} media query/queries"))
    checks.append(("layout uses flex/grid instead of fixed widths",
                   flex_grid >= 1 and fixed == 0,
                   f"{fixed} fixed-width declaration(s)"))
    overflow_hack = 0
    for _path, text in styles:
        overflow_hack += len(re.findall(r"overflow-x\s*:\s*hidden", text, re.I))
    checks.append(("no overflow-x:hidden masking", overflow_hack == 0,
                   f"{overflow_hack} occurrence(s)"))
    return checks


def score_dimensions(dimensions):
    score = 0.0
    details = {}
    for name, (checks, weight) in dimensions.items():
        if not checks:
            ratio = 0.0
        else:
            ratio = len([c for c in checks if c[1]]) / len(checks)
        details[name] = {"score": round(ratio, 3), "weight": weight,
                         "checks": [{"name": c[0], "ok": bool(c[1]), "detail": c[2]}
                                    for c in checks]}
        score += ratio * weight
    return round(score, 3), details


def analyse(root: Path):
    styles, markups, scripts = _collect(root)
    if not styles and not markups and not scripts:
        return None
    dimensions = {
        "typography": (_dim_typography(styles, markups), WEIGHTS["typography"]),
        "colour": (_dim_colour(styles, markups), WEIGHTS["colour"]),
        "spacing": (_dim_spacing(styles), WEIGHTS["spacing"]),
        "motion": (_dim_motion(styles), WEIGHTS["motion"]),
        "consistency": (_dim_consistency(styles, markups), WEIGHTS["consistency"]),
        "content_states": (_dim_content_states(markups, scripts), WEIGHTS["content_states"]),
        "layout": (_dim_layout(styles, markups), WEIGHTS["layout"]),
    }
    score, details = score_dimensions(dimensions)
    return {"score": score, "dimensions": details,
            "threshold": THRESHOLD, "min_dimension": MIN_DIMENSION}


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1

    result = GateResult("C", "DESIGN POLISH RUBRIC")
    report = analyse(root)
    if report is None:
        result.skipped = True
        result.reason = "no markup, styles or scripts found - nothing to judge"
        payload = print_report(result, json_mode)
        emit([], payload, json_mode)
        return 2

    for name, info in report["dimensions"].items():
        for check in info["checks"]:
            result.checks.append(_check(name, check))
    score = report["score"]
    worst = min(info["score"] for info in report["dimensions"].values())
    result.add(f"rubric score >= {THRESHOLD}", score >= THRESHOLD, True,
               f"score {score:.2f} (threshold {THRESHOLD})")
    result.add(f"no dimension below {MIN_DIMENSION}", worst >= MIN_DIMENSION, True,
               f"weakest dimension {worst:.2f}")

    ux = run_absorbed("ux_audit.py", root, timeout=180)
    if ux.get("available"):
        ux_score = None
        payload = ux.get("json") or {}
        if isinstance(payload, dict):
            ux_score = payload.get("score") or payload.get("overall_score")
        result.add("absorbed ux_audit.py reports compliance", bool(ux.get("ok")), False,
                   ux.get("detail", "") + (f" score={ux_score}" if ux_score else ""))
    else:
        result.warn("absorbed ux_audit.py available", ux.get("detail", ""))

    # ---- Web Interface Guidelines (absorbed from web-design-guidelines) ---
    guidelines_result: dict = {}
    try:
        import web_guidelines  # noqa: E402  (same directory)

        guidelines_result = web_guidelines.analyse(root)
        if guidelines_result.get("files_checked"):
            result.add(
                "no high-severity Web Interface Guidelines violations",
                guidelines_result["high"] == 0, True,
                f"{guidelines_result['high']} high, {guidelines_result['medium']} medium "
                f"finding(s) in {guidelines_result['files_checked']} file(s)",
            )
            if guidelines_result["medium"]:
                result.warn(
                    "Web Interface Guidelines: medium findings",
                    f"{guidelines_result['medium']} finding(s) - "
                    "run scripts/web_guidelines.py for the file:line list",
                )
        else:
            result.warn("Web Interface Guidelines applicable", "no UI files were found")
    except Exception as exc:  # the guidelines must never break the gate
        result.warn("Web Interface Guidelines available", f"could not run: {exc}")

    # ---- human sign-off -------------------------------------------------
    sign_opts = _signoff_args(args)
    sign_path = signoff_path(root, sign_opts["path"])

    if sign_opts["record"]:
        if not sign_opts["reviewer"].strip():
            print("ERROR: --record-signoff needs --reviewer '<name>'", file=sys.stderr)
            return 1
        record = build_signoff(sign_opts["reviewer"], sign_opts["verdict"],
                               sign_opts["notes"], report, sign_opts["scope"])
        if not write_signoff(sign_path, record):
            print(f"ERROR: could not write {sign_path}", file=sys.stderr)
            return 1
        print(f"[OK] design sign-off recorded in {sign_path}")
        print(f"     reviewer={record['reviewer']} verdict={record['verdict']} "
              f"score={record['rubric_score']} fingerprint={record['fingerprint']}")
        return 0

    signoff = read_signoff(sign_path)
    signed_off = False
    signoff_reasons: list = []
    if signoff is not None:
        signoff_reasons = validate_signoff(signoff, report)
        signed_off = not signoff_reasons
        if signed_off:
            result.add("a human reviewer signed the design off", True, True,
                       f"{signoff.get('reviewer')} on {signoff.get('date')} "
                       f"(score {signoff.get('rubric_score')})")
        else:
            result.warn("the recorded design sign-off is not valid",
                        "; ".join(signoff_reasons))
    else:
        result.notes.append("human sign-off still required: taste is not machine-checkable")
        result.notes.append("sign-off checklist: hierarchy, spacing consistency, "
                             "colour harmony, copy clarity, brand fit")
        result.notes.append("record the decision with: python scripts/design_polish.py "
                             f"--root <app> --record-signoff --reviewer '<name>' "
                             f"--verdict approved")

    if result.status == "fail":
        verdict = "rubric-failed"
    elif signed_off:
        verdict = "rubric-met-and-signed-off"
    else:
        verdict = "rubric-met-needs-signoff"

    payload = print_report(result, json_mode, extra={
        "rubric": report,
        "rubric_fingerprint": rubric_fingerprint(report),
        "human_signoff": signoff if signed_off else None,
        "signoff_reasons": signoff_reasons,
        "verdict": verdict,
        "web_guidelines": {
            "high": guidelines_result.get("high", 0),
            "medium": guidelines_result.get("medium", 0),
            "files_checked": guidelines_result.get("files_checked", 0),
            "findings": guidelines_result.get("findings", [])[:50],
        },
    })
    try:
        out_dir = root / "qa"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "design.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    except OSError:
        pass
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


def _check(dimension, check):
    from qa_ext import Check
    return Check(f"{dimension}: {check['name']}", check["ok"], True, check["detail"])


# --------------------------------------------------------------------------
# human sign-off record
#
# The rubric can only measure what a machine can see.  A human still has to
# sign the result off - and that decision is stored so it can be audited
# later instead of living in a chat transcript.  The record is bound to the
# exact rubric that was measured (a fingerprint), so a sign-off for an older
# or different score can never be reused.
# --------------------------------------------------------------------------

SIGNOFF_REL = ("qa", "signoff", "design.json")


def signoff_path(root: Path, override=None) -> Path:
    if override:
        return Path(override)
    return Path(root).joinpath(*SIGNOFF_REL)


def rubric_fingerprint(report) -> str:
    """A stable hash of the rubric measurement."""
    dims = report.get("dimensions") or {}
    parts = [f"score={round(float(report.get('score', 0)), 4)}",
             f"threshold={report.get('threshold')}"]
    for name in sorted(dims):
        info = dims[name] or {}
        parts.append(f"{name}={round(float(info.get('score', 0)), 4)}")
    blob = "|".join(parts)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:32]


def read_signoff(path: Path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def validate_signoff(signoff, report) -> list:
    """Return the list of reasons the sign-off is not valid (empty = valid)."""
    reasons = []
    if not isinstance(signoff, dict):
        return ["the sign-off file is not valid JSON"]
    reviewer = str(signoff.get("reviewer") or "").strip()
    if not reviewer:
        reasons.append("no reviewer is named")
    verdict = str(signoff.get("verdict") or "").strip().lower()
    if verdict != "approved":
        reasons.append(f"the verdict is '{verdict or 'missing'}', not 'approved'")
    raw_date = str(signoff.get("date") or "").strip()
    if not raw_date:
        reasons.append("no date is recorded")
    else:
        try:
            signed = datetime.date.fromisoformat(raw_date[:10])
            if signed > datetime.date.today():
                reasons.append("the sign-off date is in the future")
        except ValueError:
            reasons.append(f"the date '{raw_date}' is not an ISO date")
    score = signoff.get("rubric_score")
    if score is None:
        reasons.append("no rubric score was recorded")
    else:
        try:
            if abs(float(score) - float(report.get("score", 0))) > 0.02:
                reasons.append(f"the recorded score {score} does not match the "
                               f"current rubric score {round(float(report.get('score', 0)), 2)}")
        except (TypeError, ValueError):
            reasons.append("the recorded rubric score is not a number")
    fingerprint = str(signoff.get("fingerprint") or "")
    if fingerprint != rubric_fingerprint(report):
        reasons.append("the sign-off was recorded for a different rubric measurement")
    return reasons


def build_signoff(reviewer, verdict, notes, report, scope="") -> dict:
    return {
        "reviewer": reviewer,
        "date": datetime.date.today().isoformat(),
        "verdict": verdict,
        "notes": notes,
        "scope": scope,
        "rubric_score": round(float(report.get("score", 0)), 4),
        "rubric_threshold": report.get("threshold"),
        "fingerprint": rubric_fingerprint(report),
        "tool": "app-production-readiness design_polish.py",
    }


def write_signoff(path: Path, payload: dict) -> bool:
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return True
    except OSError:
        return False


def _signoff_args(argv):
    opts = {"path": None, "record": False, "reviewer": "", "verdict": "approved",
            "notes": "", "scope": ""}
    i = 0
    while i < len(argv):
        a = argv[i]
        nxt = argv[i + 1] if i + 1 < len(argv) else None
        if a == "--signoff" and nxt:
            opts["path"] = nxt
        elif a == "--record-signoff":
            opts["record"] = True
        elif a == "--reviewer" and nxt:
            opts["reviewer"] = nxt
        elif a == "--verdict" and nxt:
            opts["verdict"] = nxt
        elif a == "--notes" and nxt:
            opts["notes"] = nxt
        elif a == "--scope" and nxt:
            opts["scope"] = nxt
        i += 1
    return opts


if __name__ == "__main__":
    raise SystemExit(main())
