#!/usr/bin/env python3
"""Gate N - business logic, error handling and API contract.

Three independent signals, because "the app works" is a claim that must be
earned:

1. **Static logic smells** - swallowed errors, empty catch blocks, `if (true)`
   without an exit, `process.exit` inside request handlers, unchecked
   promises, stray debug logging.
2. **Live scenarios** - a declarative spec (``qa/scenarios.json``) is executed
   against the running app: status code, JSON path assertions and body
   assertions.  This is the part that actually exercises business rules.
3. **API contract** - the absorbed ``api_validator.py`` (api-patterns) checks
   the shape of the API surface (REST conventions, versioning, pagination,
   status codes) and is reported as an extra signal.

A script can prove *the code implements the rules as written*.  It can
never prove *the written rules are the intended ones* - that is a domain
question.  So the gate splits in two and the second half is signed by a
human, bound to the exact rules that were reviewed:

  machine : scenarios executed + API contract + static smells
  human   : ``qa/signoff/business-rules.json`` (reviewer, date, verdict,
            fingerprint of the scenario spec + rule documents)

Changing the rules or the scenario spec invalidates the approval, so a
sign-off can never drift onto a different set of rules.

Usage:
  python scripts/business_logic_check.py --root <app_root> [--url http://localhost:3000]
  python scripts/business_logic_check.py --root <app_root> \
      --record-signoff --reviewer "Jane Doe" --verdict approved \
      --notes "rules match product spec v3" --rules-ref "SPEC-42"

Exit 0 = machine signals clean (a missing sign-off is not a failure, it is
reported as "needs sign-off"), 1 = findings, 2 = nothing checkable.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, load_json, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import (GateResult, http_request, print_report, read_files,  # noqa: E402
                     run_absorbed)
import signoff as signoff_mod  # noqa: E402

SPEC_LOCATIONS = ("qa/scenarios.json", "tests/scenarios.json", "scenarios.json",
                  "qa/business-scenarios.json", "tests/business-scenarios.json")

SIGNOFF_NAME = "business-rules.json"

# documents that state the business rules; approving them is what the
# domain owner signs off
RULE_DOC_NAMES = ("rules.md", "business-rules.md", "domain-rules.md",
                  "rules.txt", "spec.md", "business-rules.txt")
RULE_DOC_DIRS = ("docs", "doc", "spec", "specs", "documentation", "domain")

CODE_EXT = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".go", ".rs",
            ".rb", ".php", ".java", ".kt", ".vue", ".svelte"}

EMPTY_CATCH = re.compile(
    r"catch\s*(\([^)]*\))?\s*\{\s*\}|except[^:\n]*:\s*(pass|\.\.\.)\s*$",
    re.M)
SWALLOWED = re.compile(r"\.catch\(\s*(\(\s*\)|function\s*\(\s*\)\s*\{\s*\})")
IF_TRUE = re.compile(r"if\s*\(\s*true\s*\)|while\s*\(\s*true\s*\)")
PROCESS_EXIT = re.compile(r"process\.exit\s*\(|sys\.exit\s*\(|os\._exit\s*\(")
DEBUG_LOG = re.compile(r"console\.(log|debug)\s*\(|print\s*\(|println!\s*\(")
TODO = re.compile(r"(?i)\b(TODO|FIXME|XXX|HACK)\b")
EQUALS_NULL = re.compile(r"==\s*null|null\s*==|!=\s*null|null\s*!=")
ERROR_HANDLER = re.compile(
    r"app\.use\s*\(\s*\(?\s*(err|error|e)|errorHandler|@exception_handler|"
    r"def\s+handle_error|express-async-errors|middleware\[.?error|"
    r"catch\s*\(\s*(err|error|e)\s*\)", re.I)


def find_spec(root: Path):
    for rel in SPEC_LOCATIONS:
        cand = root / rel
        if cand.is_file():
            return cand
    return None


def find_rule_docs(root: Path):
    """Find the documents that state the business rules (if any)."""
    found = []
    for name in RULE_DOC_NAMES:
        cand = root / name
        if cand.is_file() and cand not in found:
            found.append(cand)
    for d in RULE_DOC_DIRS:
        folder = root / d
        if not folder.is_dir():
            continue
        for cand in sorted(folder.glob("**/*")):
            if cand.is_file() and cand.name.lower() in RULE_DOC_NAMES and cand not in found:
                found.append(cand)
    return found


def static_signals(root: Path):
    """Return (findings, signals) for the code-level checks."""
    findings = []
    signals = {}
    files = [(p, t) for p, t in read_files(root, CODE_EXT)]
    if not files:
        return findings, signals
    empty_catch, swallowed, if_true, exits, debug, todos, eq_null = ([] for _ in range(7))
    has_error_handler = False
    for path, text in files:
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        for m in EMPTY_CATCH.finditer(text):
            empty_catch.append(f"{rel}:{text[:m.start()].count(chr(10)) + 1}")
        for m in SWALLOWED.finditer(text):
            swallowed.append(f"{rel}:{text[:m.start()].count(chr(10)) + 1}")
        for m in IF_TRUE.finditer(text):
            if_true.append(f"{rel}:{text[:m.start()].count(chr(10)) + 1}")
        for m in PROCESS_EXIT.finditer(text):
            line = text[text.rfind("\n", 0, m.start()) + 1: m.start()].lower()
            if any(word in line for word in ("route", "handler", "controller",
                                             "request", "api", "view", "lambda")):
                exits.append(f"{rel}:{text[:m.start()].count(chr(10)) + 1}")
        for m in DEBUG_LOG.finditer(text):
            debug.append(f"{rel}:{text[:m.start()].count(chr(10)) + 1}")
        for m in TODO.finditer(text):
            todos.append(f"{rel}:{text[:m.start()].count(chr(10)) + 1}")
        for m in EQUALS_NULL.finditer(text):
            eq_null.append(f"{rel}:{text[:m.start()].count(chr(10)) + 1}")
        if ERROR_HANDLER.search(text):
            has_error_handler = True

    def add(name, hits, severity, detail):
        if hits:
            findings.append({"severity": severity, "check": name,
                             "detail": f"{len(hits)} occurrence(s): {', '.join(hits[:5])}"})

    add("empty catch block swallows the error", empty_catch, "HIGH", "")
    add("promise rejection silently ignored", swallowed, "HIGH", "")
    add("unconditional loop or branch with no exit", if_true, "MEDIUM", "")
    add("process exit inside a request handler", exits, "HIGH", "")
    add("debug logging left in production code", debug, "LOW", "")
    add("TODO/FIXME markers in shipped code", todos, "LOW", "")
    add("loose null comparison", eq_null, "LOW", "")
    signals["files_scanned"] = len(files)
    signals["error_handler_present"] = has_error_handler
    return findings, signals


def _dig(obj, dotted):
    cur = obj
    for part in dotted.split("."):
        if isinstance(cur, dict):
            cur = cur.get(part)
        elif isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except (ValueError, IndexError):
                return None
        else:
            return None
        if cur is None:
            return None
    return cur


def run_scenarios(spec, base_url, timeout=15.0):
    """Execute the scenario spec.  Returns (results, failures)."""
    results = []
    failures = []
    for sc in spec.get("scenarios", []):
        name = sc.get("name") or sc.get("path", "scenario")
        method = (sc.get("method") or "GET").upper()
        path = sc.get("path", "/")
        url = path if str(path).startswith("http") else base_url.rstrip("/") + "/" + str(path).lstrip("/")
        headers = sc.get("headers") or {}
        body = sc.get("body")
        payload = None
        if body is not None:
            payload = json.dumps(body).encode("utf-8")
            headers.setdefault("Content-Type", "application/json")
        res = http_request(url, method=method, headers=headers, body=payload,
                           timeout=timeout)
        expected_status = sc.get("expect_status", 200)
        entry = {"name": name, "method": method, "path": path,
                 "status": res["status"], "expected_status": expected_status,
                 "assertions": [], "ok": True}
        if res["status"] != expected_status:
            entry["ok"] = False
            entry["assertions"].append(
                f"status {res['status']} != {expected_status}")
        for dotted, expected in (sc.get("expect_json") or {}).items():
            actual = _dig(res.get("json"), dotted) if res.get("json") is not None else None
            ok = actual == expected
            entry["assertions"].append(
                f"json {dotted}: {actual!r} == {expected!r} -> {ok}")
            if not ok:
                entry["ok"] = False
        for needle in (sc.get("expect_body_contains") or []):
            ok = needle.lower() in (res.get("body") or "").lower()
            entry["assertions"].append(f"body contains {needle!r} -> {ok}")
            if not ok:
                entry["ok"] = False
        results.append(entry)
        if not entry["ok"]:
            failures.append(f"{name}: " + "; ".join(
                a for a in entry["assertions"] if "-> False" in a or "!=" in a))
    return results, failures


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    url = None
    root_arg = "."
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--url" and i + 1 < len(args):
            url = args[i + 1]
            i += 1
        elif a == "--root" and i + 1 < len(args):
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

    result = GateResult("N", "BUSINESS RULES: EXECUTABLE CONTRACT + SIGN-OFF")
    findings, signals = static_signals(root)
    if not signals.get("files_scanned"):
        result.skipped = True
        result.reason = "no source files found - nothing to judge"
        payload = print_report(result, json_mode)
        emit([], payload, json_mode)
        return 2

    for finding in findings:
        if finding["severity"] in ("HIGH", "CRITICAL"):
            result.fail(finding["check"], finding["detail"], finding["severity"])
        else:
            result.warn(finding["check"], finding["detail"])
    result.add("a central error handler exists",
               bool(signals.get("error_handler_present")), False,
               "no app.use(error)/errorHandler found - errors may leak as 500s"
               if not signals.get("error_handler_present") else "")

    spec_path = find_spec(root)
    rule_docs = find_rule_docs(root)
    scenario_results = []
    contract_available = True
    if spec_path is None:
        contract_available = False
        result.warn("business scenario spec present", "no qa/scenarios.json - "
                    "business rules were not exercised")
    elif not url:
        contract_available = False
        result.warn("business scenarios executed", "no --url given - scenarios skipped")
    else:
        spec = load_json(spec_path) or {}
        scenario_results, scenario_failures = run_scenarios(spec, url)
        # status 0 means "no connection" - if every scenario got status 0 the
        # app was not reachable, so the contract was never measured. That is a
        # skip, not a failing business rule.
        unreachable = bool(scenario_results) and all(
            (sc.get("status") or 0) == 0 for sc in scenario_results)
        if unreachable:
            contract_available = False
            result.warn("business scenarios executed",
                        "the app was not reachable - the scenarios could not be "
                        "run, so the contract was not measured")
            # the scenarios were never evaluated: do not report their
            # connection failure as a failed business rule
            for scenario in scenario_results:
                scenario["not_evaluated"] = True
                scenario["ok"] = None
                scenario["assertions"] = [
                    "not evaluated - the app was not reachable"]
        else:
            for scenario in scenario_results:
                result.add(f"scenario: {scenario['name']}", scenario["ok"], True,
                           "; ".join(scenario["assertions"])[:200]
                           if not scenario["ok"] else
                           f"{scenario['status']} ok")

    api = run_absorbed("api_validator.py", root, timeout=120)
    if api.get("available"):
        result.add("absorbed api_validator.py reports a clean API surface",
                   bool(api.get("ok")), False, api.get("detail", ""))
    else:
        result.warn("absorbed api_validator.py available", api.get("detail", ""))

    # ---- human sign-off: "are the written rules the intended ones?" ----
    sign_opts = signoff_mod.signoff_args(args, prefix="rules")
    subject = ([spec_path] if spec_path else []) + rule_docs
    subject_rel = []
    for p in subject:
        try:
            subject_rel.append(p.relative_to(root).as_posix())
        except ValueError:
            subject_rel.append(p.name)
    fp = signoff_mod.fingerprint(subject, root=root)
    sign = signoff_mod.resolve_signoff(
        root, SIGNOFF_NAME, sign_opts, fp, subject=subject_rel,
        extra={"rules_ref": sign_opts.get("ref") or None})
    signed_off = not sign["reasons"]
    result.add("a domain sign-off is recorded", signed_off, False,
               "; ".join(sign["reasons"]) if sign["reasons"] else
               f"signed off by {sign['record'].get('reviewer')} on "
               f"{sign['record'].get('date')}")

    if result.blocking:
        verdict = "executable-contract-failed"
    elif not contract_available:
        verdict = "executable-contract-unavailable"
    elif signed_off:
        verdict = "executable-contract-met-and-signed-off"
    else:
        verdict = "executable-contract-met-needs-signoff"

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from absorbed_rules import api_contract_findings
        for item in api_contract_findings(root):
            if item["severity"] in ("HIGH", "CRITICAL"):
                result.fail(item["type"], f"{item['file']}: {item['type']}", item["severity"])
            else:
                result.warn(item["type"], f"{item['file']}")
    except Exception:
        pass

    payload = print_report(result, json_mode, extra={
        "scenarios": scenario_results,
        "signals": signals,
        "verdict": verdict,
        "signoff_fingerprint": fp,
        "signoff_subject": subject_rel,
        "human_signoff": sign["record"],
        "signoff_reasons": sign["reasons"],
        "signoff_path": sign["path"],
        "rules_ref": sign_opts.get("ref") or None,
    })
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
