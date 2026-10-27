#!/usr/bin/env python3
"""The review orchestrator: scope -> measure -> judge -> report.

Until now the skill was a set of gate scripts you had to remember to run in
the right order, with the app already running.  This script does the whole
thing in one command:

1. **Scope** - ``gate_scope`` decides which of the 21 gates apply to this app.
2. **Fix** (optional, ``--fix``) - apply the safe, mechanical fixes.
3. **Measure** - run the gate scripts, writing their evidence into the app.
   With ``--serve`` the app is started by the skill itself, so the live gates
   work even when nobody started the server.  The start mode is recorded:
   a dev server means every measurement is a DEV measurement.
4. **Judge** - every gate is judged by the *verifiers* in ``verify_claims``,
   the same adversarial engine that re-derives a claimed PASS.  The report can
   therefore never contain a PASS the tooling did not prove.
5. **Report** - ``qa/report.md`` + ``qa/summary.json``.

Usage::

    python scripts/review.py --root <app> --serve
    python scripts/review.py --root <app> --url http://127.0.0.1:3000 --fix
    python scripts/review.py --root <app> --gates A,B,E --json

Exit codes: ``0`` - no gate was contradicted, ``1`` - at least one gate was
contradicted (or, with ``--strict``, at least one gate could not be verified).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qa_common import emit, run_cmd  # noqa: E402

import verify_claims  # noqa: E402

try:
    import gate_scope  # noqa: E402
except Exception:  # pragma: no cover
    gate_scope = None

try:
    import framework_profiles  # noqa: E402
except Exception:  # pragma: no cover
    framework_profiles = None

try:
    import serve as serve_mod  # noqa: E402
except Exception:  # pragma: no cover
    serve_mod = None

try:
    import fixes as fixes_mod  # noqa: E402
except Exception:  # pragma: no cover
    fixes_mod = None

SCRIPT_DIR = Path(__file__).resolve().parent
PY = sys.executable

GATE_ORDER = list("ABCDEFGHIJKLMNOPQRSTU")


# --------------------------------------------------------------------------
# measurement
# --------------------------------------------------------------------------

def _run(cmd, cwd, timeout=600):
    rc, out, err = run_cmd(cmd, cwd=cwd, timeout=timeout)
    return {"cmd": " ".join(str(c) for c in cmd), "rc": rc,
            "out": (out or "")[-4000:], "err": (err or "")[-2000:]}


def measure(root: Path, url, routes, healthz, opts) -> dict:
    """Run the gate scripts that produce evidence.  Returns a step log."""
    steps = []
    browsers = opts.get("browsers", "chromium,firefox,webkit")
    route_arg = ",".join(routes) if routes else "/"
    out_dir = opts.get("out_dir") or "qa"

    wanted = set(opts.get("gates") or [])

    def need(*gates):
        """Only run a measurement step when a gate that needs it is requested."""
        return (not wanted) or any(g in wanted for g in gates)

    def add(name, cmd, timeout=600, gates=()):
        if gates and not need(*gates):
            return None
        res = _run(cmd, root, timeout)
        res["step"] = name
        steps.append(res)
        return res

    # A - screenshots (also produces the evidence for gate M)
    add("A capture_screenshots", [
        PY, str(SCRIPT_DIR / "capture_screenshots.py"), "--root", str(root),
        "--url", url, "--routes", route_arg, "--out", "docs/screenshots",
        "--browsers", browsers], gates=("A", "M"))

    # D - lighthouse
    add("D lighthouse", [
        PY, str(SCRIPT_DIR / "lighthouse_run.py"), "--root", str(root),
        "--url", url, "--routes", route_arg, "--out", f"{out_dir}/lighthouse",
        "--timeout", str(opts.get("lighthouse_timeout", 180))], timeout=1800,
        gates=("D",))

    # F - accessibility (axe + keyboard)
    add("F a11y_audit", [
        PY, str(SCRIPT_DIR / "a11y_audit.py"), "--root", str(root),
        "--url", url, "--routes", route_arg, "--browsers", browsers],
        timeout=1200, gates=("F",))

    # O - load + soak
    soak = int(opts.get("soak", 0))
    load_cmd = [PY, str(SCRIPT_DIR / "load_check.py"), "--url", url,
                "--duration", str(opts.get("duration", 10))]
    if soak:
        load_cmd += ["--soak", str(soak),
                     "--soak-interval", str(max(1, soak // 6))]
    add("O load_check", load_cmd, timeout=900, gates=("O",))

    # I deep mode - the platform start command really boots the app
    add("I deploy_smoke", [
        PY, str(SCRIPT_DIR / "deploy_smoke.py"), str(root),
        "--healthz", healthz, "--routes", route_arg,
        "--boot-timeout", str(opts.get("boot_timeout", 60))], timeout=600,
        gates=("I",))

    # E deep mode - the security-audit schema + coverage ledger
    add("E security_audit", [
        PY, str(SCRIPT_DIR / "security_audit.py"), str(root)], timeout=600,
        gates=("E",))

    # P deep mode - migrations really apply, roll back and re-apply
    add("P migration_apply", [
        PY, str(SCRIPT_DIR / "migration_apply.py"), str(root)], timeout=900,
        gates=("P",))

    # T deep mode - a real payment + email round trip (skipped without keys)
    add("T payment_email_live", [
        PY, str(SCRIPT_DIR / "payment_email_live.py"), str(root)], timeout=300,
        gates=("T",))

    return {"steps": steps}


# --------------------------------------------------------------------------
# judging
# --------------------------------------------------------------------------

ADVISORY_FAMILIES = {
    "K": "observability_findings",
    "I": "resilience_findings",
    "H": "test_quality_findings",
}


def _advisory_notes(root: Path, gate: str) -> str:
    """Extra signal absorbed from the documentation-only sibling skills.

    These families are advisory: they never change a verdict, they only add the
    observations the reviewer should look at (missing observability signals,
    missing resilience mechanisms, missing property/mutation testing).
    """
    name = ADVISORY_FAMILIES.get(gate)
    if not name:
        return ""
    try:
        import absorbed_rules
    except Exception:
        return ""
    try:
        items = getattr(absorbed_rules, name)(root)
    except Exception:
        return ""
    if not items:
        return ""
    details = "; ".join(sorted({str(item.get("type", "")).split("] ", 1)[-1] for item in items}))
    return f"advisory: {len(items)} observation(s) - {details}"


def judge(root: Path, ctx, gates=None) -> list:
    """Judge every gate with the adversarial verifiers."""
    results = []
    scope = None
    if gate_scope is not None:
        try:
            scope = gate_scope.analyse(root)
        except Exception:
            scope = None
    for gate in GATE_ORDER:
        if gates and gate not in gates:
            continue
        name = verify_claims.GATE_NAMES.get(gate, gate)
        if scope is not None:
            status, reason = gate_scope.scope_for_gate(scope, gate)
            if status == gate_scope.NOT_APPLICABLE:
                results.append({"gate": gate, "name": name, "verdict": "NOT_APPLICABLE",
                                "evidence": f"not applicable to this app: {reason}"})
                continue
        verifier = verify_claims.VERIFIERS.get(gate)
        if verifier is None:
            results.append({"gate": gate, "name": name, "verdict": "UNVERIFIABLE",
                            "evidence": "no verifier for this gate"})
            continue
        try:
            verdict, evidence = verifier(root, ctx)
        except Exception as exc:
            verdict, evidence = "UNSUPPORTED", f"the verifier failed: {exc}"
        advisory = _advisory_notes(root, gate)
        if advisory:
            evidence = f"{evidence} | {advisory}"
        results.append({"gate": gate, "name": name, "verdict": verdict,
                        "evidence": str(evidence)[:600]})
    return results


# --------------------------------------------------------------------------
# report
# --------------------------------------------------------------------------

VERDICT_MARK = {
    "VERIFIED": "PASS",
    "CONTRADICTED": "FAIL",
    "UNSUPPORTED": "SKIP",
    "UNVERIFIABLE": "NEEDS-HUMAN",
    "NOT_APPLICABLE": "N/A",
}


def write_report(root: Path, payload: dict) -> str:
    """Write ``qa/report.md``."""
    qa = root / "qa"
    try:
        qa.mkdir(parents=True, exist_ok=True)
    except OSError:
        pass
    lines = []
    lines.append(f"# Production-readiness review - {payload['app']['name']}")
    lines.append("")
    lines.append(f"* generated: {payload['generated']}")
    lines.append(f"* app root: `{payload['app']['root']}`")
    lines.append(f"* framework: {payload['app']['framework']}")
    lines.append(f"* live URL: {payload['app']['url'] or 'not started'}"
                 + ("  (DEV SERVER - every live number below is a dev measurement)"
                    if payload["app"].get("dev_mode") else ""))
    lines.append("")
    lines.append("## SCOPE")
    scope = payload.get("scope") or {}
    lines.append(f"gates that apply: {scope.get('run', '?')} | "
                 f"conditional: {scope.get('maybe', '?')} | "
                 f"not applicable: {scope.get('skip', '?')}")
    lines.append("")
    if payload.get("fixes"):
        lines.append("## FIXES APPLIED")
        for item in payload["fixes"]:
            lines.append(f"* **{item.get('status')}** `{item.get('id')}` - {item.get('detail')}")
        lines.append("")
    lines.append("## GATES")
    lines.append("| gate | result | evidence |")
    lines.append("| --- | --- | --- |")
    for item in payload["gates"]:
        mark = VERDICT_MARK.get(item["verdict"], item["verdict"])
        evidence = (item.get("evidence") or "").replace("|", "/").replace("\n", " ")
        lines.append(f"| {item['gate']} {item['name']} | **{mark}** | {evidence[:220]} |")
    lines.append("")
    lines.append("## SUMMARY")
    summary = payload["summary"]
    lines.append(f"* verified: {summary.get('verified', 0)} | "
                 f"contradicted: {summary.get('contradicted', 0)} | "
                 f"unsupported: {summary.get('unsupported', 0)} | "
                 f"needs a human: {summary.get('unverifiable', 0)} | "
                 f"not applicable: {summary.get('not_applicable', 0)}")
    lines.append("")
    if payload.get("blocking"):
        lines.append("## BLOCKERS")
        for item in payload["blocking"]:
            lines.append(f"* **{item['gate']}** - {item['evidence']}")
        lines.append("")
    lines.append("## ARTEFACTS")
    for path in payload.get("artefacts", []):
        lines.append(f"* `{path}`")
    lines.append("")
    text = "\n".join(lines) + "\n"
    try:
        (qa / "report.md").write_text(text, encoding="utf-8")
        (qa / "summary.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    except OSError:
        pass
    return str(qa / "report.md")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root = Path(".").resolve()
    want_json = "--json" in argv
    opts = {
        "url": None, "routes": [], "healthz": "/healthz", "serve": False,
        "fix": False, "strict": False, "gates": None, "browsers": "chromium,firefox,webkit",
        "duration": 10, "soak": 0, "out_dir": "qa", "lighthouse_timeout": 180,
        "boot_timeout": 60, "skip_tests": False, "test_timeout": 600,
    }
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--root" and i + 1 < len(argv):
            root = Path(argv[i + 1]).expanduser().resolve()
            i += 1
        elif a == "--url" and i + 1 < len(argv):
            opts["url"] = argv[i + 1].rstrip("/")
            i += 1
        elif a == "--routes" and i + 1 < len(argv):
            opts["routes"] = [r.strip() for r in argv[i + 1].split(",") if r.strip()]
            i += 1
        elif a == "--healthz" and i + 1 < len(argv):
            opts["healthz"] = argv[i + 1]
            i += 1
        elif a == "--gates" and i + 1 < len(argv):
            opts["gates"] = [g.strip().upper() for g in argv[i + 1].split(",") if g.strip()]
            i += 1
        elif a == "--browsers" and i + 1 < len(argv):
            opts["browsers"] = argv[i + 1]
            i += 1
        elif a == "--duration" and i + 1 < len(argv):
            try:
                opts["duration"] = int(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--soak" and i + 1 < len(argv):
            try:
                opts["soak"] = int(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--boot-timeout" and i + 1 < len(argv):
            try:
                opts["boot_timeout"] = int(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--serve":
            opts["serve"] = True
        elif a == "--fix":
            opts["fix"] = True
        elif a == "--strict":
            opts["strict"] = True
        elif a == "--skip-tests":
            opts["skip_tests"] = True
        i += 1

    if not root.is_dir():
        print(f"[FAIL] project root does not exist: {root}")
        return 1

    started = time.time()
    app = {"name": root.name, "root": str(root), "url": opts.get("url"),
           "dev_mode": False, "mode": None, "serve_error": ""}
    if framework_profiles is not None:
        try:
            app["framework"] = framework_profiles.describe(root)["label"]
        except Exception:
            app["framework"] = "unknown"
    else:
        app["framework"] = "unknown"

    fixes = []
    if opts["fix"] and fixes_mod is not None:
        fixes = fixes_mod.apply_all(root)

    # --- start the app ourselves when asked ---------------------------
    handle = None
    if opts["serve"] and serve_mod is not None and not opts.get("url"):
        result = serve_mod.start_server(root, {"port": None, "timeout": 180.0})
        if result.get("ok"):
            handle = result["handle"]
            app["url"] = handle.url
            app["dev_mode"] = handle.dev_mode
            app["mode"] = handle.mode
            app["serve_notes"] = result.get("notes", [])
        else:
            app["serve_error"] = result.get("error", "the app could not be started")
            app["url"] = None
    elif opts.get("url"):
        app["url"] = opts["url"]

    # The server must stay up for the whole measurement AND the judging:
    # the business-rule scenarios are executed during judge(), so stopping it
    # after measure() made gate N fail with "status 0 != 200".
    steps = []
    if app.get("url"):
        steps = measure(root, app["url"], opts["routes"] or ["/"],
                        opts["healthz"], opts)["steps"]
    else:
        app["serve_error"] = app.get("serve_error") or (
            "no live URL: pass --url or --serve so the live gates can run")

    try:
        ctx = {
            "url": app.get("url"),
            "routes": opts["routes"] or ["/"],
            "healthz": opts["healthz"],
            "skip_tests": opts["skip_tests"],
            "test_timeout": opts["test_timeout"],
            "artifact_dirs": (),
            "use_scope": True,
        }
        gates = judge(root, ctx, opts["gates"])

        summary = {"verified": 0, "contradicted": 0, "unsupported": 0,
                   "unverifiable": 0, "not_applicable": 0}
        for item in gates:
            key = {"VERIFIED": "verified", "CONTRADICTED": "contradicted",
                   "UNSUPPORTED": "unsupported", "UNVERIFIABLE": "unverifiable",
                   "NOT_APPLICABLE": "not_applicable"}.get(item["verdict"])
            if key:
                summary[key] += 1
        blocking = [g for g in gates if g["verdict"] in ("CONTRADICTED", "UNSUPPORTED")]

        scope_summary = {}
        if gate_scope is not None:
            try:
                report = gate_scope.analyse(root)
                scope_summary = {"run": len(report.get("required", [])),
                                 "maybe": len(report.get("recommended", [])),
                                 "skip": len(report.get("skipped", []))}
            except Exception:
                scope_summary = {}

        artefacts = []
        for rel in ("qa/report.md", "qa/summary.json", "qa/deploy-smoke.json",
                    "qa/load.json", "qa/migrations.json", "qa/security/findings.json",
                    "qa/security/coverage-ledger.json", "qa/lighthouse/lighthouse-summary.json",
                    "qa/a11y/a11y-report.json", "docs/screenshots/manifest.json"):
            if (root / rel).exists():
                artefacts.append(rel)

        payload = {
            "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
            "app": app,
            "scope": scope_summary,
            "fixes": fixes,
            "steps": [{"step": s["step"], "rc": s["rc"]} for s in steps],
            "gates": gates,
            "summary": summary,
            "blocking": blocking,
            "artefacts": artefacts,
            "seconds": round(time.time() - started, 1),
        }
        report_path = write_report(root, payload)
    except BaseException:
        if handle is not None:
            handle.stop()
        raise
    finally:
        if handle is not None:
            handle.stop()

    lines = [f"REVIEW {root.name} -> {report_path}"]
    for item in gates:
        lines.append(f"  [{VERDICT_MARK.get(item['verdict'], item['verdict'])}] "
                     f"{item['gate']} {item['name']}: {item['evidence'][:150]}")
    lines.append(f"  summary: {summary}")
    emit(lines, payload, want_json)

    if summary["contradicted"]:
        return 1
    if opts["strict"] and (summary["unsupported"] or summary["unverifiable"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
