#!/usr/bin/env python3
"""Adversarially verify a review's claimed gate results.

A review that says "D lighthouse PASS (Perf 96)" used to be unverifiable:
nothing re-checked the claim, so a gate could be marked PASS with no
evidence at all. This script ignores the prose and re-derives each gate
from artifacts on disk and from a fresh run of the relevant checks.

Usage:
  python verify_claims.py --root <app_root> --claims qa/claims.json \\
      [--url http://localhost:3000] [--artifact-dir <dir>] [--json] [--skip-tests]

Artifacts (screenshots manifest, lighthouse summary, a11y report) are read
from the reviewed app root.  If they live in a separate review workspace,
point at it explicitly with --artifact-dir (repeatable) or the
QA_ARTIFACT_DIRS environment variable.  Nothing is picked up implicitly
from the current directory: stale evidence from another project must never
be able to verify a gate.

Claims file formats (both accepted):
  {"gates": {"A": "PASS", "B": "PASS"}}          # JSON
  GATES      : A visual PASS | B perf PASS | ...  # the markdown report

Gate scoping: before a claimed PASS is checked, the app is classified by
`gate_scope.py`.  A gate that cannot apply to this kind of app (migrations
for a static site, payments for an API service) is reported as
NOT_APPLICABLE instead of being failed.  Use --no-scope to disable this.

Exit 0: every claimed PASS is supported by evidence
Exit 1: a claimed PASS is unsupported or contradicted by the evidence
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    emit,
    load_json,
    parse_cli,
    resolve_root,
    root_error,
    run_cmd,
    which,
)

GATE_NAMES = {
    "A": "cross-browser visual QA",
    "B": "performance / bundle budget",
    "C": "design polish (rubric + human sign-off)",
    "D": "desktop Lighthouse",
    "E": "security",
    "F": "accessibility (WCAG 2.1 AA)",
    "G": "SEO & metadata",
    "H": "tests & correctness",
    "I": "reliability & error handling",
    "J": "docs & DX",
    "K": "observability",
    "L": "free-tier cost check",
    "M": "README & screenshots",
    "N": "business rules (executable contract + domain sign-off)",
    "O": "load & soak",
    "P": "migrations & schema",
    "Q": "privacy & GDPR (policy + legal sign-off)",
    "R": "i18n & RTL",
    "S": "assistive technology contract",
    "T": "payment & email flows",
    "U": "code quality & AI risk",
}
VERIFIED = "VERIFIED"
CONTRADICTED = "CONTRADICTED"
UNSUPPORTED = "UNSUPPORTED"
UNVERIFIABLE = "UNVERIFIABLE"
NOT_APPLICABLE = "NOT_APPLICABLE"


def parse_claims(path: Path):
    """Read a claims file. Returns (dict gate->status, source description)."""
    if not path.is_file():
        return {}, f"claims file not found: {path}"
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix.lower() == ".json" or text.lstrip().startswith("{"):
        data = load_json(path)
        if isinstance(data, dict):
            gates = data.get("gates") if isinstance(data.get("gates"), dict) else data
            out = {}
            for key, value in gates.items():
                k = str(key).strip().upper()
                if k in GATE_NAMES:
                    out[k] = str(value).strip().upper()
            if out:
                return out, str(path)
    # markdown / text report
    out = {}
    for m in re.finditer(r"\b([A-U])\b[^|\n]{0,40}?\b(PASS|FAIL|WARN)\b", text):
        gate, status = m.group(1), m.group(2).upper()
        out.setdefault(gate, status)
    return out, str(path)


def find_claims_file(root: Path, explicit):
    if explicit:
        return Path(explicit)
    for name in ("qa/claims.json", "qa/report.json", "PRODUCTION_REVIEW.md",
                 "qa/REVIEW.md", "REVIEW.md"):
        cand = root / name
        if cand.is_file():
            return cand
    return None


def find_artifact(root: Path, rels, extra_dirs=()):
    """Find a review artifact.

    Only the reviewed app root is searched by default (plus any directory the
    caller passes explicitly through --artifact-dir).  The current working
    directory is deliberately NOT used as an implicit fallback: a stale
    report left in some other project would otherwise be mistaken for
    evidence about this app.
    Returns the path or None.
    """
    bases = [root]
    for extra in extra_dirs or ():
        try:
            p = Path(extra)
        except TypeError:
            continue
        if p.is_dir() and p.resolve() != root.resolve():
            bases.append(p)
    for base in bases:
        for rel in rels:
            p = base / rel
            if p.is_file():
                return p
    return None


# --- individual gate verifiers ------------------------------------------------

def verify_A(root: Path, ctx):
    """Cross-browser visual evidence."""
    p = find_artifact(root, ("docs/screenshots/manifest.json", "qa/screenshots/manifest.json",
                             "screenshots/manifest.json"), ctx.get("artifact_dirs"))
    if p is not None:
        rel = p.name
        data = load_json(p)
        if not isinstance(data, dict):
            return UNSUPPORTED, f"{rel} is not readable JSON"
        browsers = sorted({c.get("browser") for c in data.get("captures", [])
                           if isinstance(c, dict) and c.get("browser")})
        routes = sorted({c.get("route") for c in data.get("captures", [])
                         if isinstance(c, dict) and c.get("route")})
        if len(browsers) >= 2:
            return VERIFIED, f"captured {len(browsers)} engines {browsers} over {len(routes)} routes"
        return CONTRADICTED, f"only one browser engine captured ({browsers or 'none'}) - not cross-browser"
    return UNSUPPORTED, "no screenshot manifest found (docs/screenshots/manifest.json)"


def verify_B(root: Path, ctx):
    """Bundle / performance budget, recomputed now."""
    try:
        import bundle_report
        report = bundle_report.analyse(root)
    except Exception as exc:
        return UNSUPPORTED, f"bundle_report could not run: {exc}"
    if report.get("status") == "no-build":
        return UNSUPPORTED, "no build output to measure"
    failures = [c for c in report["checks"] if c["required"] and not c["ok"]]
    if failures:
        return CONTRADICTED, "; ".join(f"{c['name']} ({c['detail']})" for c in failures)
    return VERIFIED, f"all bundle budgets met (route JS {report.get('route_budget_kb')} kB)"


def verify_C(root: Path, ctx):
    """Design polish: objective rubric + human sign-off.

    The rubric is machine-checkable, taste is not.  A failing rubric
    CONTRADICTS the claim; a passing rubric still needs a human, so the
    verdict stays UNVERIFIABLE.
    """
    script = Path(__file__).parent / "design_polish.py"
    cmd = [sys.executable, str(script), "--root", str(root), "--json"]
    rc, out, err = run_cmd(cmd, cwd=root, timeout=ctx.get("gate_timeout", 300))
    try:
        data = json.loads(out)
    except ValueError:
        return UNVERIFIABLE, "design polish could not be measured (no report produced)"
    if data.get("status") == "skipped":
        return UNVERIFIABLE, f"nothing to judge: {data.get('reason', '')}"
    rubric = data.get("rubric") or {}
    score = rubric.get("score")
    if rc == 1:
        blocking = data.get("blocking") or []
        return CONTRADICTED, f"design rubric failed (score {score}): " + \
            "; ".join(blocking[:3])
    if data.get("verdict") == "rubric-met-and-signed-off":
        signoff = data.get("human_signoff") or {}
        return VERIFIED, (f"design rubric passed (score {score}) and was signed off by "
                          f"{signoff.get('reviewer', 'unknown')} on {signoff.get('date', '?')}")
    if data.get("signoff_reasons"):
        return UNVERIFIABLE, (f"design rubric passed (score {score}) but the recorded "
                              f"sign-off is not valid: "
                              + "; ".join(data["signoff_reasons"][:3]))
    return (UNVERIFIABLE,
            f"design rubric passed (score {score}) - human sign-off still required")


def verify_D(root: Path, ctx):
    """Lighthouse thresholds, recomputed from the stored report."""
    p = find_artifact(root, ("qa/lighthouse/lighthouse-summary.json",
                             "lighthouse/lighthouse-summary.json"),
                      ctx.get("artifact_dirs"))
    if p is None:
        return UNSUPPORTED, "no qa/lighthouse/lighthouse-summary.json"
    data = load_json(p)
    if not isinstance(data, dict):
        return UNSUPPORTED, "lighthouse-summary.json is not readable JSON"
    if data.get("status") == "skipped":
        return UNSUPPORTED, f"lighthouse did not run: {data.get('reason')}"
    thresholds = data.get("thresholds") or {}
    failures = []
    errors = []
    measured = 0
    for route, res in (data.get("results") or {}).items():
        res = res or {}
        scores = res.get("scores") or {}
        if not scores:
            # A run that errored (npx lock race, no Chrome, timeout) is NOT a
            # score of 0 and NOT an app defect - the measurement never happened.
            errors.append(f"{route}: {res.get('error') or 'no scores were recorded'}")
            continue
        measured += 1
        for cat, minimum in thresholds.items():
            score = scores.get(cat, 0)
            if score < minimum:
                failures.append(f"{route}: {cat} {score} < {minimum}")
    if failures:
        return CONTRADICTED, "; ".join(failures[:4])
    if errors:
        return UNSUPPORTED, ("the Lighthouse run could not be measured - "
                             + "; ".join(errors[:3]))
    return VERIFIED, f"{measured} route(s) meet every threshold"


def verify_E(root: Path, ctx):
    """Security scan, re-run now."""
    try:
        import security_scan
        findings = security_scan.scan_all(root)
    except Exception as exc:
        return UNSUPPORTED, f"security_scan could not run: {exc}"
    high = [f for f in findings if f["severity"] == "HIGH"]
    if high:
        return CONTRADICTED, "; ".join(f"{f['type']} ({f['file']}:{f['line']})" for f in high[:4])
    med = len([f for f in findings if f["severity"] == "MEDIUM"])
    note = f"{med} medium finding(s) outstanding" if med else "no findings"
    unverified_cve = [f for f in findings if "CVE scan NOT performed" in f["type"]]
    if unverified_cve:
        note += "; dependency CVE scan was skipped"
    return VERIFIED, note


def verify_F(root: Path, ctx):
    """axe-core + keyboard audit report."""
    p = find_artifact(root, ("qa/a11y/a11y-report.json", "a11y/a11y-report.json"),
                      ctx.get("artifact_dirs"))
    if p is None:
        return UNSUPPORTED, "no qa/a11y/a11y-report.json"
    data = load_json(p)
    if not isinstance(data, dict):
        return UNSUPPORTED, "a11y-report.json is not readable JSON"
    if data.get("status") == "skipped":
        return UNSUPPORTED, f"a11y audit did not run: {data.get('reason')}"
    failures = data.get("failures") or []
    if failures:
        return CONTRADICTED, "; ".join(str(f) for f in failures[:4])
    engines = sorted((data.get("browsers") or {}).keys())
    return VERIFIED, f"no critical/serious violations across {', '.join(engines) or 'n/a'}"


def verify_G(root: Path, ctx):
    """SEO/metadata, checked against the live app when a URL is known."""
    static_gaps = []
    try:
        import seo_static
        static = seo_static.analyse(root)
        static_gaps = static.get("seo_findings") or []
    except Exception:
        static_gaps = []
    if not ctx.get("url"):
        if static_gaps:
            return CONTRADICTED, "; ".join(
                f"{g.get('file')}: {g.get('issue')}" for g in static_gaps[:4])
        return UNSUPPORTED, "no live URL given - SEO metadata cannot be verified"
    try:
        import runtime_check
        report = runtime_check.run(ctx["url"], ctx.get("routes") or ["/"],
                                   ctx.get("healthz") or "/healthz", 15.0)
    except Exception as exc:
        return UNSUPPORTED, f"runtime_check could not run: {exc}"
    seo_failures = [f for f in report.get("failures", [])
                    if "seo:" in f or "global: unknown route" in f]
    if report.get("status") == "fail" and seo_failures:
        return CONTRADICTED, "; ".join(seo_failures[:4])
    if static_gaps:
        return CONTRADICTED, "static pages: " + "; ".join(
            f"{g.get('file')}: {g.get('issue')}" for g in static_gaps[:4])
    if report.get("status") == "fail":
        return VERIFIED, "SEO metadata present (other runtime checks failed)"
    return VERIFIED, "SEO metadata present on every checked route"


def count_tests(text):
    """How many tests did the runner report? None when the output is opaque."""
    if not text:
        return None
    counts = []
    patterns = [
        r"tests?\s+(\d+)",                          # node --test: "tests 1"
        r"tests?:\s*(\d+)",                         # jest: "Tests: 1 passed"
        r"(\d+)\s+(?:passed|passing|examples?)\b",  # pytest / jest / rspec
        r"pass\s+(\d+)",                            # node --test: "pass 1"
        r"test result:\s*ok\.\s*(\d+)\s+passed",   # cargo test
    ]
    for pat in patterns:
        for m in re.finditer(pat, text, re.I):
            try:
                counts.append(int(m.group(1)))
            except ValueError:
                pass
    go_ok = len(re.findall(r"^ok\s+\S+", text, re.M))
    if go_ok:
        counts.append(go_ok)
    if not counts:
        return None
    return max(counts)


def verify_H(root: Path, ctx):
    """The project's own test suite, executed now."""
    if ctx.get("skip_tests"):
        return UNSUPPORTED, "tests skipped by request"
    cmd, runner = detect_test_command(root)
    if not cmd:
        return UNSUPPORTED, "no detectable test command"
    rc, out, err = run_cmd(cmd, cwd=root, timeout=ctx.get("test_timeout", 600))
    output = (out or "") + "\n" + (err or "")
    if rc == 0:
        ran = count_tests(output)
        if ran is None:
            return (UNSUPPORTED,
                    f"{runner} exited 0 but no test count could be parsed - "
                    "cannot confirm that any test ran")
        if ran <= 0:
            return UNSUPPORTED, f"{runner} exited 0 but ran 0 tests"
        return VERIFIED, f"{runner} exited 0, {ran} test(s) passed"
    tail = (out or err).strip().splitlines()[-1][:160] if (out or err).strip() else f"rc={rc}"
    return CONTRADICTED, f"{runner} failed: {tail}"


def detect_test_command(root: Path):
    """The test command for the detected ecosystem."""
    pkg = load_json(root / "package.json")
    if isinstance(pkg, dict):
        scripts = pkg.get("scripts") or {}
        if "test" in scripts:
            mgr = "npm"
            for lock, name in (("pnpm-lock.yaml", "pnpm"), ("yarn.lock", "yarn"),
                               ("bun.lockb", "bun"), ("bun.lock", "bun")):
                if (root / lock).is_file():
                    mgr = name
                    break
            return [mgr, "test"], f"{mgr} test"
    if (root / "pyproject.toml").is_file() or (root / "pytest.ini").is_file() \
            or (root / "tests").is_dir():
        if which("pytest"):
            return [sys.executable, "-m", "pytest", "-q"], "pytest"
    if (root / "go.mod").is_file() and which("go"):
        return ["go", "test", "./..."], "go test"
    if (root / "Cargo.toml").is_file() and which("cargo"):
        return ["cargo", "test"], "cargo test"
    cmd, runner = absorbed_test_command(root)
    if cmd:
        return cmd, runner
    return None, None


def absorbed_test_command(root: Path):
    """Ask the absorbed ``testing-patterns`` runner for a test command.

    It also knows jest / vitest / unittest projects that have no ``test``
    script in package.json - a case our own detection cannot cover.  The
    absorbed script is imported as a module (its CLI is guarded), so nothing
    is executed here.
    """
    module_path = Path(__file__).resolve().parent / "absorbed" / "test_runner.py"
    if not module_path.is_file():
        return None, None
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "absorbed_test_runner", module_path)
        if spec is None or spec.loader is None:
            return None, None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        info = module.detect_test_framework(root)
    except Exception:
        return None, None
    cmd = info.get("cmd")
    if not cmd:
        return None, None
    framework = info.get("framework") or info.get("type") or "auto"
    return list(cmd), f"absorbed test_runner ({framework})"


def verify_I(root: Path, ctx):
    """Reliability: the app must boot and the health endpoint must answer.

    When a deploy smoke report exists it is the stronger evidence: the app
    was started the way the platform starts it and then probed.  Otherwise
    the live health endpoint is checked.
    """
    healthz = ctx.get("healthz") or "/healthz"
    smoke_path = find_artifact(root, ("qa/deploy-smoke.json", "deploy-smoke.json"),
                               ctx.get("artifact_dirs"))
    if smoke_path is not None:
        data = load_json(smoke_path)
        smoke = (data or {}).get("smoke") or {}
        status = smoke.get("status")
        if status == "ok":
            if smoke.get("health_ok", True) and smoke.get("routes_ok", True):
                return VERIFIED, (f"the app boots with the platform start command and "
                                  f"{healthz} answers 2xx (mode={smoke.get('mode')})")
            return CONTRADICTED, ("the app booted but the health endpoint or a route "
                                  "did not answer")
        if status in ("fail", "failed"):
            return CONTRADICTED, smoke.get("error") or "the deploy smoke test failed"
    if not ctx.get("url"):
        return UNSUPPORTED, "no live URL given - reliability cannot be verified"
    try:
        import runtime_check
        report = runtime_check.run(ctx["url"], [healthz], healthz, 15.0)
    except Exception as exc:
        return UNSUPPORTED, f"runtime_check could not run: {exc}"
    health = [c for c in report["global"]["checks"] if "health endpoint" in c["name"]]
    if health and health[0]["ok"]:
        return VERIFIED, f"health endpoint {healthz} responds 2xx"
    return CONTRADICTED, (health[0]["detail"] if health else "health endpoint not reachable")


def verify_J(root: Path, ctx):
    """README standard, re-validated now."""
    rc, out, err = run_cmd([sys.executable, str(Path(__file__).parent / "check_readme.py"),
                             str(root)], timeout=120)
    if rc == 0:
        return VERIFIED, "README passes the production standard"
    fails = [ln.strip() for ln in out.splitlines() if ln.startswith("[FAIL]")]
    return CONTRADICTED, "; ".join(fails[:4]) or "README check failed"


def verify_K(root: Path, ctx):
    """Observability evidence in the source."""
    evidence = {
        "structured logging": r"JSON\.stringify\(\s*\{|logging\.getLogger|logger\.(info|error|warn)",
        "request id": r"x-request-id|requestId|request_id",
        "error tracking": r"sentry|Sentry|captureException|rollbar|bugsnag",
        "health endpoint": r"healthz|/health",
    }
    found = set()
    try:
        import security_scan as ss
        for p in ss.walk(root):
            if p.suffix not in ss.CODE_EXT:
                continue
            txt = ss.read(p)
            for label, pattern in evidence.items():
                if label in found:
                    continue
                if re.search(pattern, txt, re.I):
                    found.add(label)
    except Exception as exc:
        return UNSUPPORTED, f"could not scan the source: {exc}"
    if len(found) >= 3:
        return VERIFIED, "evidence: " + ", ".join(sorted(found))
    return UNSUPPORTED, "only found: " + (", ".join(sorted(found)) or "nothing")


def verify_L(root: Path, ctx):
    """Free-tier documentation."""
    readme = root / "README.md"
    if not readme.is_file():
        return UNSUPPORTED, "no README.md"
    text = readme.read_text(encoding="utf-8", errors="ignore")
    has_limits = bool(re.search(r"(?i)free\s*(tier|plan)|limits?\b", text))
    has_fallback = bool(re.search(r"(?i)fallback|what breaks|when the limit|exceeded", text))
    if has_limits and has_fallback:
        return VERIFIED, "README documents free-tier limits and the fallback"
    if has_limits:
        return CONTRADICTED, "README mentions free-tier limits but not the fallback behaviour"
    return UNSUPPORTED, "README documents no free-tier limits"


def verify_M(root: Path, ctx):
    """Screenshots + contact sheet."""
    shots = []
    for d in ("docs/screenshots", "screenshots", "docs/images", "public/screenshots"):
        p = root / d
        if p.is_dir():
            shots.extend([f for f in p.rglob("*.png") if f.name != "contact-sheet.png"])
    sheet = any((root / d / "contact-sheet.png").exists()
                for d in ("docs/screenshots", "screenshots", "docs/images", "public/screenshots"))
    if len(shots) >= 3 and sheet:
        return VERIFIED, f"{len(shots)} screenshot(s) + contact sheet present"
    if not sheet:
        return CONTRADICTED, f"contact-sheet.png missing ({len(shots)} screenshots)"
    return CONTRADICTED, f"only {len(shots)} screenshot(s), 3 required"


def _rerun_gate(script_name, root, ctx, extra=()):
    """Re-run one of the extended gate scripts and turn its result into a verdict."""
    script = Path(__file__).parent / script_name
    if not script.is_file():
        return UNSUPPORTED, f"{script_name} is missing from the skill"
    cmd = [sys.executable, str(script), "--root", str(root), "--json", *extra]
    rc, out, err = run_cmd(cmd, cwd=root, timeout=ctx.get("gate_timeout", 600))
    try:
        data = json.loads(out)
    except ValueError:
        tail = (out or err or "").strip().splitlines()[-1][:160] if (out or err or "").strip() else ""
        return UNSUPPORTED, f"{script_name} produced no parsable report (rc={rc}) {tail}"
    if rc == 2 or data.get("status") == "skipped":
        return UNSUPPORTED, data.get("reason") or f"{script_name} was skipped"
    summary = data.get("summary") or {}
    if rc == 0:
        return (VERIFIED,
                f"{script_name}: no blocking failures "
                f"({summary.get('passed', 0)}/{summary.get('checks', 0)} checks passed, "
                f"{summary.get('warnings', 0)} warnings)")
    blocking = data.get("blocking") or []
    return CONTRADICTED, f"{script_name}: " + "; ".join(str(b)[:120] for b in blocking[:3])


def _url_args(ctx):
    args = []
    if ctx.get("url"):
        args += ["--url", ctx["url"]]
    if ctx.get("routes"):
        args += ["--routes", ",".join(ctx["routes"])]
    return args


def verify_N(root: Path, ctx):
    """Business rules: executed contract (machine) + domain sign-off (human).

    The machine half proves the code implements the written rules.  The
    human half - a fingerprint-bound sign-off - proves the written rules
    are the intended ones.  Both are required for a PASS.
    """
    script = Path(__file__).parent / "business_logic_check.py"
    cmd = [sys.executable, str(script), "--root", str(root), "--json"]
    if ctx.get("url"):
        cmd += ["--url", ctx["url"]]
    rc, out, err = run_cmd(cmd, cwd=root, timeout=ctx.get("gate_timeout", 300))
    try:
        data = json.loads(out)
    except ValueError:
        return UNSUPPORTED, "business logic could not be measured (no report produced)"
    if data.get("status") == "skipped":
        return UNSUPPORTED, f"nothing to judge: {data.get('reason', '')}"
    verdict = data.get("verdict")
    if verdict == "executable-contract-failed" or rc == 1:
        blocking = data.get("blocking") or []
        return CONTRADICTED, ("the executable business contract failed: "
                              + ("; ".join(str(b)[:120] for b in blocking[:3])
                                 if blocking else "scenarios or static smells failed"))
    if verdict == "executable-contract-unavailable":
        return UNSUPPORTED, ("no executable contract to verify - add qa/scenarios.json "
                             "and run with --url")
    if verdict == "executable-contract-met-and-signed-off":
        signoff = data.get("human_signoff") or {}
        scenarios = len(data.get("scenarios") or [])
        return VERIFIED, (f"{scenarios} business scenarios executed and the rules were "
                          f"signed off by {signoff.get('reviewer', 'unknown')} on "
                          f"{signoff.get('date', '?')}")
    if data.get("signoff_reasons"):
        return UNVERIFIABLE, ("the executable contract passed, but the domain sign-off "
                              "is not valid: " + "; ".join(data["signoff_reasons"][:3]))
    return UNVERIFIABLE, ("the executable contract passed - a domain sign-off is still "
                          "required to confirm the rules are the intended ones")


def verify_O(root: Path, ctx):
    """Load and soak: a short live load run against the app."""
    if not ctx.get("url"):
        return UNSUPPORTED, "no live URL given - load was not measured"
    duration = str(ctx.get("load_duration", 5))
    verdict, evidence = _rerun_gate("load_check.py", root, ctx,
                                    ["--url", ctx["url"], "--duration", duration])
    soak_path = find_artifact(root, ("qa/load.json", "load.json"),
                              ctx.get("artifact_dirs"))
    if soak_path is not None:
        data = load_json(soak_path) or {}
        soak = data.get("soak") or []
        if soak:
            drift = max(float(s.get("drift_pct", 0)) for s in soak)
            windows = soak[0].get("windows", 0)
            evidence += (f"; soak series: {windows} windows, worst drift {drift} %")
    return verdict, evidence


def verify_P(root: Path, ctx):
    """Migrations and schema safety - static rules plus a real apply/rollback."""
    mig_path = find_artifact(root, ("qa/migrations.json", "migrations.json"),
                             ctx.get("artifact_dirs"))
    if mig_path is not None:
        data = load_json(mig_path) or {}
        if data.get("status") == "ok":
            roundtrip = data.get("roundtrip") or {}
            applied = len(roundtrip.get("apply") or [])
            return VERIFIED, (f"{applied} migrations apply, roll back and re-apply "
                              f"cleanly on {roundtrip.get('engine', '?')}")
        blocking = data.get("blocking") or []
        if blocking:
            return CONTRADICTED, "; ".join(str(b)[:120] for b in blocking[:3])
    return _rerun_gate("migration_check.py", root, ctx)


def verify_Q(root: Path, ctx):
    """Privacy and GDPR: machine posture + legal sign-off of the policy."""
    script = Path(__file__).parent / "privacy_check.py"
    cmd = [sys.executable, str(script), "--root", str(root), "--json"]
    if ctx.get("url"):
        cmd += ["--url", ctx["url"]]
    rc, out, err = run_cmd(cmd, cwd=root, timeout=ctx.get("gate_timeout", 300))
    try:
        data = json.loads(out)
    except ValueError:
        return UNSUPPORTED, "privacy could not be measured (no report produced)"
    if data.get("status") == "skipped":
        return UNSUPPORTED, f"nothing to judge: {data.get('reason', '')}"
    verdict = data.get("verdict")
    if verdict == "policy-failed" or rc == 1:
        blocking = data.get("blocking") or []
        return CONTRADICTED, ("the privacy posture failed: "
                              + ("; ".join(str(b)[:120] for b in blocking[:3])
                                 if blocking else "consent/PII/policy rules failed"))
    if verdict == "policy-met-and-legal-signed-off":
        signoff = data.get("human_signoff") or {}
        basis = signoff.get("legal_basis") or data.get("legal_basis") or "n/a"
        return VERIFIED, (f"privacy posture ok and the policy was signed off by "
                          f"{signoff.get('reviewer', 'unknown')} on "
                          f"{signoff.get('date', '?')} (basis: {basis})")
    if data.get("signoff_reasons"):
        return UNVERIFIABLE, ("the privacy posture passed, but the legal sign-off "
                              "is not valid: " + "; ".join(data["signoff_reasons"][:3]))
    return UNVERIFIABLE, ("the privacy posture passed - a legal sign-off of the policy "
                          "is still required")


def verify_R(root: Path, ctx):
    """Internationalisation and RTL."""
    return _rerun_gate("i18n_check.py", root, ctx)


def verify_S(root: Path, ctx):
    """Screen-reader contract."""
    return _rerun_gate("at_check.py", root, ctx)


def verify_T(root: Path, ctx):
    """Payment and email flows - static rules plus a live test round-trip."""
    live_path = find_artifact(root, ("qa/payment-email-live.json",
                                     "payment-email-live.json"),
                              ctx.get("artifact_dirs"))
    if live_path is not None:
        data = load_json(live_path) or {}
        if data.get("status") == "ok":
            channels = data.get("channels") or []
            return VERIFIED, ("a live test round-trip succeeded for: "
                              + ", ".join(str(c.get("channel", "?")) for c in channels))
        blocking = data.get("blocking") or []
        if blocking:
            return CONTRADICTED, "; ".join(str(b)[:120] for b in blocking[:3])
    return _rerun_gate("payment_email_check.py", root, ctx)


def verify_U(root: Path, ctx):
    """Code quality and AI-risk debt."""
    return _rerun_gate("code_quality.py", root, ctx)


VERIFIERS = {
    "A": verify_A, "B": verify_B, "C": verify_C, "D": verify_D, "E": verify_E,
    "F": verify_F, "G": verify_G, "H": verify_H, "I": verify_I, "J": verify_J,
    "K": verify_K, "L": verify_L, "M": verify_M,
    "N": verify_N, "O": verify_O, "P": verify_P, "Q": verify_Q, "R": verify_R,
    "S": verify_S, "T": verify_T, "U": verify_U,
}


def check_identity(root: Path, ctx):
    """Is the live URL actually the project under review?

    Without this, a reviewer could point --url at any healthy site and have
    the live gates (SEO, health) "verify" against an app that was never
    reviewed.
    """
    url = ctx.get("url")
    if not url:
        return True, "no live URL given - live gates cannot be cross-checked"
    pkg = load_json(root / "package.json")
    name = pkg.get("name") if isinstance(pkg, dict) else None
    if not name:
        return True, "project has no name to compare against"
    try:
        import runtime_check
        res = runtime_check.fetch(url.rstrip("/") + "/", 10.0)
    except Exception as exc:
        return True, f"could not fetch the live URL ({exc})"
    body = res.get("body", b"") or b""
    text = body.decode("utf-8", errors="ignore").lower()
    flat = re.sub(r"[^a-z0-9]", "", text)
    needle = re.sub(r"[^a-z0-9]", "", str(name).lower())
    if needle and needle in flat:
        return True, f"live URL serves project '{name}'"
    return False, (f"live URL does not mention project '{name}' - "
                   f"it is probably not the app under review")


def verify(root: Path, claims: dict, ctx) -> dict:
    # accept both {"gates": {...}} and a flat {gate: status} mapping
    if isinstance(claims.get("gates"), dict):
        claims = claims["gates"]
    results = []
    identity_ok, identity_note = check_identity(root, ctx)
    scope = None
    if ctx.get("use_scope", True):
        try:
            import gate_scope
            scope = gate_scope.analyse(root)
        except Exception:
            scope = None
    for gate in sorted(claims):
        status = claims[gate]
        name = GATE_NAMES.get(gate, gate)
        if status != "PASS":
            results.append({"gate": gate, "name": name, "claimed": status,
                            "verdict": "NOT_CLAIMED_PASS", "evidence": "gate not claimed PASS"})
            continue
        if scope is not None:
            gstatus, reason = gate_scope.scope_for_gate(scope, gate)
            if gstatus == gate_scope.NOT_APPLICABLE:
                results.append({"gate": gate, "name": name, "claimed": status,
                                "verdict": NOT_APPLICABLE,
                                "evidence": f"not applicable to this app: {reason}"})
                continue
        verifier = VERIFIERS.get(gate)
        if verifier is None:
            results.append({"gate": gate, "name": name, "claimed": status,
                            "verdict": UNVERIFIABLE, "evidence": "no verifier exists for this gate"})
            continue
        try:
            verdict, evidence = verifier(root, ctx)
        except Exception as exc:
            verdict, evidence = UNSUPPORTED, f"verifier raised: {exc}"
        if not identity_ok and gate in ("G", "I"):
            verdict, evidence = CONTRADICTED, identity_note
        results.append({"gate": gate, "name": name, "claimed": status,
                        "verdict": verdict, "evidence": evidence})
    bad = [r for r in results if r["verdict"] in (CONTRADICTED, UNSUPPORTED)]
    unver = [r for r in results if r["verdict"] == UNVERIFIABLE]
    return {
        "root": str(root),
        "results": results,
        "identity": {"ok": identity_ok, "note": identity_note},
        "scope": {
            "applied": scope is not None,
            "skipped": sorted(scope.get("skipped") or []) if scope else [],
            "conditional": sorted(scope.get("recommended") or []) if scope else [],
            "app": (scope.get("app") if scope else None),
        },
        "summary": {
            "claimed": len(results),
            "verified": len([r for r in results if r["verdict"] == VERIFIED]),
            "contradicted": len([r for r in results if r["verdict"] == CONTRADICTED]),
            "unsupported": len([r for r in results if r["verdict"] == UNSUPPORTED]),
            "unverifiable": len(unver),
            "not_applicable": len([r for r in results if r["verdict"] == NOT_APPLICABLE]),
        },
        "status": "fail" if bad else ("warn" if unver else "ok"),
        "blocking": [f"{r['gate']} {r['name']}: {r['verdict']} - {r['evidence']}" for r in bad],
    }


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
    claims_arg = None
    url = None
    routes = None
    healthz = None
    skip_tests = "--skip-tests" in args
    use_scope = "--no-scope" not in args
    test_timeout = 600
    artifact_dirs = [d for d in (os.environ.get("QA_ARTIFACT_DIRS") or "").split(os.pathsep) if d]
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--root" and i + 1 < len(args):
            root_arg = args[i + 1]
            i += 1
        elif a == "--claims" and i + 1 < len(args):
            claims_arg = args[i + 1]
            i += 1
        elif a == "--artifact-dir" and i + 1 < len(args):
            artifact_dirs.append(args[i + 1])
            i += 1
        elif a == "--url" and i + 1 < len(args):
            url = args[i + 1]
            i += 1
        elif a == "--routes" and i + 1 < len(args):
            routes = args[i + 1]
            i += 1
        elif a == "--healthz" and i + 1 < len(args):
            healthz = args[i + 1]
            i += 1
        elif a == "--test-timeout" and i + 1 < len(args):
            try:
                test_timeout = int(args[i + 1])
            except ValueError:
                pass
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

    claims_path = find_claims_file(root, claims_arg)
    if claims_path is None:
        print("ERROR: no claims file found (use --claims or create qa/claims.json)",
              file=sys.stderr)
        return 1
    claims, source = parse_claims(claims_path)
    if not claims:
        print(f"ERROR: no gate results parsed from {source}", file=sys.stderr)
        return 1

    ctx = {"url": url, "routes": [r.strip() for r in (routes or "/").split(",") if r.strip()],
           "healthz": healthz, "skip_tests": skip_tests, "test_timeout": test_timeout,
           "artifact_dirs": artifact_dirs, "use_scope": use_scope}
    report = verify(root, claims, ctx)
    report["claims_source"] = source

    lines = ["=" * 62, "CLAIM VERIFICATION (adversarial)", "=" * 62]
    ident = report.get("identity") or {}
    lines.append(f"identity: {'OK' if ident.get('ok') else 'MISMATCH'} - {ident.get('note', '')}")
    scope_info = report.get("scope") or {}
    if scope_info.get("applied"):
        skipped = scope_info.get("skipped") or []
        lines.append("scope: gates that do not apply to this app: "
                     + (", ".join(skipped) if skipped else "none"))
    else:
        lines.append("scope: disabled (--no-scope)")
    for r in report["results"]:
        icon = {"VERIFIED": "PASS", "CONTRADICTED": "FAIL", "UNSUPPORTED": "FAIL",
                "UNVERIFIABLE": "warn", "NOT_CLAIMED_PASS": "skip",
                "NOT_APPLICABLE": "skip"}.get(r["verdict"], "?")
        lines.append(f"[{icon}] {r['gate']} {r['name']}: claimed {r['claimed']} -> {r['verdict']}")
        lines.append(f"       {r['evidence']}")
    s = report["summary"]
    lines.append("-" * 62)
    lines.append(f"claimed {s['claimed']} | verified {s['verified']} | contradicted {s['contradicted']} "
                 f"| unsupported {s['unsupported']} | unverifiable {s['unverifiable']} "
                 f"| not-applicable {s['not_applicable']}")
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    return 1 if report["status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
