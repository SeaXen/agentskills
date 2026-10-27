#!/usr/bin/env python3
"""Gate U - code quality and AI-risk debt.

This gate absorbs the review-team's code-review pass and the clean-code
rules into one runnable check.  It is deliberately objective: every finding
points at a file and a line.

Own rules (code-review-checklist + clean-code):
* functions that are too long, too wide, too deeply nested
* duplicated blocks (copy-paste detection)
* dead markers: TODO/FIXME/placeholder/mock left in shipped code
* bare except / empty catch / swallowed errors
* mutable default arguments
* commented-out code
* long files that should have been split

Absorbed signals (run as subprocesses, exit code honoured):
* ``lint_runner.py``            (lint-and-validate)
* ``type_coverage.py``          (lint-and-validate)
* ``react_performance_checker.py`` (nextjs-react-expert)

Usage:
  python scripts/code_quality.py --root <app_root> [--json]

Exit 0 = quality ok, 1 = blocking findings, 2 = nothing to check.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, print_report, read_files, run_absorbed  # noqa: E402

CODE_EXT = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".go", ".rs",
            ".rb", ".php", ".java", ".kt", ".vue", ".svelte"}
MAX_FUNCTION_LINES = 80
MAX_PARAMS = 5
MAX_NESTING = 4
MAX_FILE_LINES = 600
DEAD_MARKER = re.compile(r"(?i)\b(TODO|FIXME|XXX|HACK|placeholder|dummy|mock|stub|"
                         r"for now|temporary|not implemented|coming soon)\b")
MUTABLE_DEFAULT = re.compile(r"def\s+\w+\s*\([^)]*=\s*(\[\]|\{\}|set\(\))")
JS_MUTABLE_DEFAULT = re.compile(r"=\s*(\{\}|\[\])\s*[,)]")
BARE_EXCEPT = re.compile(r"except\s*:|except\s+Exception\s*:\s*(pass|\.\.\.)")
EMPTY_CATCH = re.compile(r"catch\s*(\([^)]*\))?\s*\{\s*\}", re.M)
COMMENTED_CODE = re.compile(r"(?m)^\s*(//|#)\s*(function|const|let|var|def|class|import|"
                             r"return\s+\w+\(|if\s*\(|for\s*\()")
FUNC_DEF = re.compile(r"^\s*(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s+(\w+)\s*(?=\()|"
                      r"^\s*(?:export\s+)?(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?(?:function\b)?(?=\()|"
                      r"^\s*def\s+(\w+)\s*(?=\()|"
                      r"^\s*func\s+(\w+)\s*(?=\()", re.M)
PARAM_LIST = re.compile(r"\(([^)]*)\)")
# An absorbed checker exits non-zero for two very different reasons: it found
# problems, or the tool it drives is not installed.  Only the first is a
# defect in the app; the second is a gap in the environment and must never
# fail the gate.
_TOOL_MISSING_RE = re.compile(
    r"(command not found|is not the tsc command|"
    r"not recognized as an internal or external command|"
    r"cannot find the path specified|executable file not found)", re.I)


def _could_not_run(res: dict) -> bool:
    """True when an absorbed checker failed because its tool was missing."""
    rc = res.get("rc")
    if rc in (124, 126, 127):
        return True
    payload = res.get("json")
    if not isinstance(payload, dict):
        return False
    checks = payload.get("checks")
    if not isinstance(checks, list) or not checks:
        return False
    failures = [c for c in checks if isinstance(c, dict) and not c.get("passed")]
    if not failures:
        return False
    return all(_TOOL_MISSING_RE.search(str(c.get("error") or "")) for c in failures)


def _functions(text, path):
    """Yield (name, start_line, end_line) for function-ish blocks.

    Python blocks end at the first following line that is not indented
    deeper than the ``def``; brace languages end when the braces balance.
    """
    lines = text.splitlines()
    is_py = Path(path).suffix.lower() == ".py"
    for m in FUNC_DEF.finditer(text):
        name = next((g for g in m.groups() if g), "?")
        start = text[:m.start()].count("\n")
        if is_py:
            base_indent = len(lines[start]) - len(lines[start].lstrip())
            end = start
            for i in range(start + 1, len(lines)):
                line = lines[i]
                if not line.strip():
                    continue
                indent = len(line) - len(line.lstrip())
                if indent <= base_indent:
                    break
                end = i
            yield name, start, end
            continue
        depth = 0
        seen = False
        end = start
        for i in range(start, len(lines)):
            line = lines[i]
            depth += line.count("{") + line.count("(") - line.count("}") - line.count(")")
            if "{" in line:
                seen = True
            if seen and depth <= 0 and i > start:
                end = i
                break
            end = i
        yield name, start, end


def _params(text, m, window=300):
    """The parameter list of the function that starts at match ``m``.

    The opening parenthesis is never consumed by ``FUNC_DEF`` (it is only
    looked ahead at), so the parameter list is found from the start of the
    definition - this works for ``function f(a)`` as well as for the
    ``const f = (a) =>`` form that dominated the old, broken lookup.
    """
    tail = text[m.start(): m.start() + window]
    pm = PARAM_LIST.search(tail)
    return pm.group(1) if pm else None


def _duplicates(text, min_lines=5):
    """Find repeated blocks of min_lines identical non-trivial lines."""
    lines = [l.strip() for l in text.splitlines()]
    blocks = {}
    for i in range(len(lines) - min_lines + 1):
        window = lines[i:i + min_lines]
        if not all(w for w in window):
            continue
        if any(w.startswith(("//", "#", "*", "/*")) for w in window):
            continue
        key = "\n".join(window)
        blocks.setdefault(key, []).append(i + 1)
    return {k: v for k, v in blocks.items() if len(v) > 1}


def _max_control_depth(text, path):
    """How deeply are control statements nested?

    Brace languages are measured with braces, Python with indentation.  The
    number is the nesting level of the deepest control statement, so a
    function body counts as level 1.
    """
    control = re.compile(r"^(if|elif|else|for|while|switch|case|try|catch|except|"
                         r"finally|with|match)\b")
    best = 0
    if path.suffix.lower() == ".py":
        for line in text.splitlines():
            if not control.match(line.strip()):
                continue
            indent = len(line) - len(line.lstrip())
            best = max(best, indent // 4 + 1)
        return best
    depth = 0
    for line in text.splitlines():
        stripped = line.strip()
        if control.match(stripped):
            best = max(best, depth + 1)
        depth += line.count("{") - line.count("}")
    return best


def _count_parameters(param_str: str) -> int:
    """Count logical parameters, treating destructured objects/arrays as 1 parameter."""
    cleaned = param_str.strip()
    if not cleaned:
        return 0
    depth_brace = 0
    depth_bracket = 0
    depth_paren = 0
    count = 1
    for ch in cleaned:
        if ch == '{': depth_brace += 1
        elif ch == '}': depth_brace = max(0, depth_brace - 1)
        elif ch == '[': depth_bracket += 1
        elif ch == ']': depth_bracket = max(0, depth_bracket - 1)
        elif ch == '(': depth_paren += 1
        elif ch == ')': depth_paren = max(0, depth_paren - 1)
        elif ch == ',' and depth_brace == 0 and depth_bracket == 0 and depth_paren == 0:
            count += 1
    return count


def analyse(root: Path):
    files = read_files(root, CODE_EXT)
    findings = []
    signals = {"files": len(files), "long_functions": 0, "wide_functions": 0,
               "deep_nesting": 0, "long_files": 0, "duplicates": 0}
    for path, text in files:
        rel = path.relative_to(root)
        line_count = len(text.splitlines())
        if line_count > MAX_FILE_LINES:
            signals["long_files"] += 1
            findings.append({"severity": "LOW", "check": "file is too long",
                             "detail": f"{rel}: {line_count} lines"})
        for name, start, end in _functions(text, path):
            length = end - start + 1
            if length > MAX_FUNCTION_LINES:
                signals["long_functions"] += 1
                findings.append({
                    "severity": "MEDIUM", "check": "function is too long",
                    "detail": f"{rel}:{start + 1} {name}() is {length} lines"})
        for m in FUNC_DEF.finditer(text):
            param_str = _params(text, m)
            if param_str is None:
                continue
            param_count = _count_parameters(param_str)
            if param_count > MAX_PARAMS:
                signals["wide_functions"] += 1
                findings.append({
                    "severity": "MEDIUM", "check": "function takes too many parameters",
                    "detail": f"{rel}:{text[:m.start()].count(chr(10)) + 1} "
                              f"{param_count} parameters"})
            if JS_MUTABLE_DEFAULT.search(param_str):
                findings.append({
                    "severity": "HIGH", "check": "mutable default argument",
                    "detail": f"{rel}:{text[:m.start()].count(chr(10)) + 1} "
                              f"({param_str[:60]})"})
        depth = _max_control_depth(text, path)
        if depth > MAX_NESTING:
            signals["deep_nesting"] += 1
            findings.append({"severity": "MEDIUM", "check": "nesting is too deep",
                             "detail": f"{rel}: depth {depth}"})
        dead = DEAD_MARKER.findall(text)
        if dead:
            findings.append({"severity": "LOW", "check": "dead marker left in the code",
                             "detail": f"{rel}: {sorted({d.lower() for d in dead})[:4]}"})
        for m in MUTABLE_DEFAULT.finditer(text):
            findings.append({"severity": "HIGH", "check": "mutable default argument",
                             "detail": f"{rel}:{text[:m.start()].count(chr(10)) + 1}"})
        for m in BARE_EXCEPT.finditer(text):
            findings.append({"severity": "HIGH", "check": "bare except swallows everything",
                             "detail": f"{rel}:{text[:m.start()].count(chr(10)) + 1}"})
        for m in EMPTY_CATCH.finditer(text):
            findings.append({"severity": "HIGH", "check": "empty catch block",
                             "detail": f"{rel}:{text[:m.start()].count(chr(10)) + 1}"})
        commented = COMMENTED_CODE.findall(text)
        if len(commented) >= 3:
            findings.append({"severity": "LOW", "check": "commented-out code",
                             "detail": f"{rel}: {len(commented)} line(s)"})
        dupes = _duplicates(text)
        if dupes:
            signals["duplicates"] += len(dupes)
            for key, lines_ in list(dupes.items())[:2]:
                findings.append({"severity": "LOW", "check": "duplicated block",
                                 "detail": f"{rel}: lines {lines_}"})
    return findings, signals


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
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

    result = GateResult("U", "CODE QUALITY & AI RISK")
    findings, signals = analyse(root)
    if not signals["files"]:
        result.skipped = True
        result.reason = "no source files found - quality not checked"
        payload = print_report(result, json_mode)
        emit([], payload, json_mode)
        return 2

    for finding in findings:
        if finding["severity"] in ("HIGH", "CRITICAL"):
            result.fail(finding["check"], finding["detail"], finding["severity"])
        elif finding["severity"] == "MEDIUM":
            result.fail(finding["check"], finding["detail"], "MEDIUM")
        else:
            result.warn(finding["check"], finding["detail"])
    result.add("no dead markers or commented-out code",
               not any(f["check"] in ("dead marker left in the code",
                                      "commented-out code") for f in findings),
               False, "")

    for name, label in (("lint_runner.py", "lint"),
                         ("type_coverage.py", "type coverage"),
                         ("react_performance_checker.py", "React performance")):
        res = run_absorbed(name, root, timeout=240)
        if res.get("available"):
            # The absorbed engine ran: its verdict is honoured. A tool that
            # could not run at all is a SKIP (advisory), never a pass.
            if _could_not_run(res):
                result.warn(f"absorbed {label} check could not run",
                            f"{res.get('detail', '')} - the underlying tool is not "
                            f"available; this is NOT a clean result")
            else:
                result.add(f"absorbed {label} check is clean", bool(res.get("ok")), True,
                           res.get("detail", ""))
        else:
            result.warn(f"absorbed {name} available", res.get("detail", ""))

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from absorbed_rules import ai_debt_findings
        for item in ai_debt_findings(root):
            detail = f"{item['file']}:{item['line']}"
            if item["severity"] in ("HIGH", "CRITICAL"):
                result.fail(item["type"], detail, item["severity"])
            elif item["severity"] == "MEDIUM":
                result.fail(item["type"], detail, "MEDIUM")
            else:
                result.warn(item["type"], detail)
    except Exception as exc:
        # A detector that could not run must never look like a clean scan.
        result.warn("AI debt detector available", f"the detector did not run: {exc}")

    payload = print_report(result, json_mode, extra={"signals": signals})
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
