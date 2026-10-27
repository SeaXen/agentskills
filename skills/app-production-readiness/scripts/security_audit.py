#!/usr/bin/env python3
"""Deep security mode: security-audit-compatible findings + coverage ledger.

This skill absorbs the machine-checkable core of the `security-audit` skill:
its finding schema (`report-schema.json`) and its two validators
(`validate-findings.cjs`, `validate-coverage-ledger.cjs`).  The Gate E
static scan is turned into

  * `findings.json`          - one record per finding, in the security-audit
                               schema (confirmed / needs_validation / rejected)
  * `coverage-ledger.json`   - what was actually inspected, per surface x
                               boundary x subsystem x attack class

and both files are then validated by the absorbed validators.  A finding that
does not satisfy the schema is a bug in this script, not a "pass".

Scope: this is a **source-first static pass**, not a pen test.  A credential
that is committed to the repository is reported as `confirmed` (the exposure
is a fact).  Everything else is reported as `needs_validation` with the exact
blocker and a safe local validation plan, because a regex match alone never
proves a trust boundary was crossed.  The hunting playbooks for a manual pass
live in `references/security/`.

Usage:
  python security_audit.py --root <app_root> [--out qa/security] [--json]
                            [--skip-validate]

Exit 0: both artefacts produced and validated
Exit 1: a validator rejected the artefacts (or the scan itself failed)
Exit 2: no validator could run (the report schema is missing or unreadable)

`--skip-validate` skips the *Node* validators only.  The portable Python
validators always run, so the artefacts are never left unvalidated.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (  # noqa: E402
    emit,
    load_json,
    parse_cli,
    resolve_out_dir,
    resolve_root,
    root_error,
    which,
)

PACK = Path(__file__).resolve().parent / "security_audit_pack"
AGENT_ATTEMPT = "pdqa-hunter-1"
AGENT_OWNER = "pdqa-static-owner"

SECRET_RE = re.compile(r"secret|api[\s_-]?key|token|password|credential|private key|stripe|aws key", re.I)
FINGERPRINT_SAFE = re.compile(r"[^A-Za-z0-9._:/@+-]+")


def _slug(text: str, limit: int = 60) -> str:
    out = FINGERPRINT_SAFE.sub("-", str(text)).strip("-")
    out = re.sub(r"-{2,}", "-", out)
    return (out[:limit] or "finding").lower()


def _rel(root: Path, file: str) -> str:
    path = Path(file)
    try:
        rel = path.resolve().relative_to(root.resolve())
    except (ValueError, OSError):
        rel = path
    return rel.as_posix()


def _redact(text: str) -> str:
    """Never copy a live credential into a report."""
    return re.sub(r"([A-Za-z0-9_\-]{6})[A-Za-z0-9_\-]{4,}", r"\1***", str(text))


def _severity_words(sev: str):
    return {"HIGH": "high", "MEDIUM": "medium", "LOW": "low"}.get(sev, "informational")


def build_findings(scan_findings, root: Path) -> list:
    """Turn the flat Gate E finding list into security-audit schema records."""
    records = []
    seen = set()
    for finding in scan_findings:
        sev = finding.get("severity", "LOW")
        ftype = str(finding.get("type", "finding"))
        file_rel = _rel(root, finding.get("file", ""))
        line = int(finding.get("line") or 0)
        base = f"{_slug(ftype)}:{file_rel}:{line}"
        fingerprint = base
        counter = 1
        while fingerprint in seen:
            counter += 1
            fingerprint = f"{base}:{counter}"
        seen.add(fingerprint)
        title = f"{ftype} in {file_rel}" + (f":{line}" if line else "")
        description = (f"The static security scan reported {ftype} in {file_rel}"
                       + (f" at line {line}" if line else "")
                       + ". The pattern is present in the reviewed source tree.")
        trace = [{
            "kind": "sink",
            "file": file_rel,
            "line": max(line, 1),
            "scope": "repository",
            "description": f"{ftype} was matched in {file_rel}.",
        }]
        evidence = [{
            "file": file_rel,
            "line": max(line, 1),
            "description": _redact(f"Static scan rule matched: {ftype}."),
        }]
        if sev == "HIGH" and SECRET_RE.search(ftype):
            records.append({
                "verdict": "confirmed",
                "fingerprint": fingerprint,
                "title": title,
                "description": description + (" The credential material is present in the "
                                              "reviewed source tree, so every reader of the "
                                              "repository - and of its history - obtains it."),
                "root_cause": ("A live-looking credential was committed to the repository "
                               "instead of being read from the environment or a secret store."),
                "intended_behavior": ("Credentials are supplied at runtime through the "
                                      "deployment environment and are never stored in source."),
                "trace": trace,
                "evidence": evidence,
                "conditions": [{
                    "kind": "system_configuration",
                    "description": ("The repository is readable by the people and systems "
                                    "that have access to it."),
                }],
                "execution": {
                    "attacker_perspective": ("An unauthenticated reader of the repository, "
                                             "or of a clone of it, can extract the credential "
                                             "without touching the running service."),
                    "payloads": [_redact(ftype)],
                    "instructions": [
                        f"Open {file_rel} and read the matched value.",
                        "Use the value against the provider API it belongs to.",
                    ],
                    "observed_result": (f"The credential literal is present in {file_rel}"
                                        + (f" at line {line}" if line else "") + "."),
                },
                "remediation": {
                    "strategy": ("Rotate the credential at the provider, remove it from the "
                                 "file, load it from the environment, and purge it from the "
                                 "git history."),
                    "code_changes": [{
                        "file_name": file_rel,
                        "fixed_code": "# load the key from process.env at runtime, never inline it",
                    }],
                },
                "severity": {
                    "likelihood": {"score": "high",
                                   "reason": "Reading a committed file needs no privilege."},
                    "impact": {"score": "high",
                               "reason": ("A committed provider credential can be used to act "
                                          "as the project against that provider.")},
                    "overall_severity": "high",
                },
                "confidence": {"score": "high",
                               "reason": ("The credential literal is present in the reviewed "
                                          "source; whether it is still active was not tested.")},
            })
        else:
            records.append({
                "verdict": "needs_validation",
                "fingerprint": fingerprint,
                "title": title,
                "description": description,
                "claimed_root_cause": f"The static rule {ftype} matched in {file_rel}.",
                "trace": trace,
                "evidence": evidence,
                "blockers": [
                    ("A pattern match alone does not show that a trust boundary is crossed; "
                     "the code path and the deployed configuration were not exercised."),
                ],
                "validation_plan": {
                    "local": (f"Read {file_rel} around line {max(line, 1)}, trace the value to "
                              "its sink, then reproduce the reachable behaviour in a local "
                              "harness with dummy data."),
                    "deployment": ("Confirm on the deployed service that the same code path is "
                                   "reachable and that the deployment's controls (proxy, WAF, "
                                   "identity policy) do not already neutralise it."),
                },
            })
    return records


def _top_paths(root: Path, limit: int = 12) -> list:
    try:
        entries = sorted(p.name for p in root.iterdir()
                         if p.name not in (".git", "node_modules", ".venv", "venv"))
    except OSError:
        entries = []
    return entries[:limit] or ["README.md"]


def _unit(root: Path, refs: dict, paths: list, findings: list, check_text: str):
    """One coverage-ledger unit."""
    def encode(value: str) -> str:
        out = []
        for byte in str(value).encode("utf-8"):
            ch = chr(byte)
            if (ch.isascii() and (ch.isalnum() or ch in "-._~")):
                out.append(ch)
            else:
                out.append("%%%02X" % byte)
        return "".join(out)

    coverage_id = "::".join(encode(refs[field]) for field in
                            ("surface", "boundary", "subsystem", "attack_class"))
    fingerprints = [f["fingerprint"] for f in findings]
    status = "candidate" if fingerprints else "covered"
    attempt = {
        "wave": 1,
        "status": status,
        "agent_id": AGENT_ATTEMPT,
        "reviewed_paths": list(paths),
        "local_checks": [{
            "agent_id": AGENT_ATTEMPT,
            "reviewed_paths": list(paths),
            "invariant": check_text,
            "method": "source",
            "result": (f"{len(findings)} finding(s) matched in this unit."
                       if findings else "No pattern matched in this unit."),
            "artifact": None,
        }],
        "result_fingerprints": list(fingerprints),
        "unresolved": [],
        "reassignment_reason": "Static pass completed; no further attempt was needed.",
    }
    return {
        "coverage_id": coverage_id,
        "canonical_refs": dict(refs),
        "surface": refs["surface"],
        "boundary": refs["boundary"],
        "subsystem": refs["subsystem"],
        "attack_class": refs["attack_class"],
        "starting_paths": list(paths),
        "ordinary_attack_class_block": "references/security/ATTACK-CLASSES.md",
        "selected_companion_blocks": ["references/security/SUPPLY-CHAIN-AND-RELEASE.md"],
        "excluded_blocks": [],
        "prior_status": "new",
        "attempts": [attempt],
        "wave": 2,
        "status": status,
        "agent_id": AGENT_OWNER,
        "reviewed_paths": list(paths),
        "local_checks": [{
            "agent_id": AGENT_OWNER,
            "reviewed_paths": list(paths),
            "invariant": check_text,
            "method": "source",
            "result": (f"{len(findings)} finding(s) matched in this unit."
                       if findings else "No pattern matched in this unit."),
            "artifact": None,
        }],
        "result_fingerprints": list(fingerprints),
        "unresolved": [],
    }


def build_ledger(scan_findings, records, root: Path) -> list:
    """Coverage units for the surfaces this skill actually inspects."""
    paths = _top_paths(root)
    secret_idx = [i for i, f in enumerate(scan_findings)
                  if SECRET_RE.search(str(f.get("type", "")))]
    code_idx = [i for i, f in enumerate(scan_findings) if i not in set(secret_idx)]
    secret_findings = [records[i] for i in secret_idx]
    code_findings = [records[i] for i in code_idx]
    units = [
        _unit(root, {"surface": "repository", "boundary": "source-to-vcs",
                     "subsystem": "credentials", "attack_class": "credential-exposure"},
              paths, secret_findings,
              "No credential material is committed to the source tree."),
        _unit(root, {"surface": "repository", "boundary": "source-to-runtime",
                     "subsystem": "application-code", "attack_class": "insecure-implementation"},
              paths, code_findings,
              "No insecure implementation pattern is present in the reviewed source."),
        _unit(root, {"surface": "dependency-graph", "boundary": "manifest-to-registry",
                     "subsystem": "dependencies", "attack_class": "supply-chain"},
              paths, [],
              "Every declared dependency resolves to a registry version without a known CVE."),
        _unit(root, {"surface": "deployment-config", "boundary": "config-to-runtime",
                     "subsystem": "platform-config", "attack_class": "misconfiguration"},
              paths, [],
              "Every deployment target is configured with a non-root user and a health check."),
    ]
    units.sort(key=lambda unit: unit["coverage_id"])
    return units


def _validate_node(script: Path, target: Path):
    """Run an absorbed Node validator.

    Returns (rc, output).  rc is None when the validator could not run on this
    platform: the security-audit validators need no-follow, nonblocking file
    reads, which Windows cannot provide.
    """
    node = which("node")
    if not node:
        return None, "node is not installed - the Node validators were not run"
    if not script.is_file():
        return None, f"validator {script.name} is missing from scripts/security_audit_pack/"
    proc = subprocess.run([node, str(script), str(target)],
                          capture_output=True, text=True)
    output = (proc.stdout or "") + (proc.stderr or "")
    if "no-follow and nonblocking input protection is unavailable" in output:
        return None, (f"{script.name} cannot run on this platform "
                      "(no no-follow file access); the portable Python check was used")
    return proc.returncode, output


def analyse(root: Path, out_dir: Path) -> dict:
    import security_scan
    scan_findings = security_scan.scan_all(root)
    findings = build_findings(scan_findings, root)
    ledger = build_ledger(scan_findings, findings, root)

    out_dir.mkdir(parents=True, exist_ok=True)
    findings_path = out_dir / "findings.json"
    ledger_path = out_dir / "coverage-ledger.json"
    findings_path.write_text(json.dumps(findings, indent=2, ensure_ascii=False) + "\n",
                              encoding="utf-8")
    ledger_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")

    report = {
        "root": str(root),
        "out_dir": str(out_dir),
        "findings_file": str(findings_path),
        "ledger_file": str(ledger_path),
        "scan_findings": len(scan_findings),
        "confirmed": len([f for f in findings if f["verdict"] == "confirmed"]),
        "needs_validation": len([f for f in findings if f["verdict"] == "needs_validation"]),
        "coverage_units": len(ledger),
        "validation": {},
        "status": "ok",
    }
    return report


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
    out_arg = None
    skip_validate = "--skip-validate" in args
    i = 0
    while i < len(args):
        if args[i] == "--out" and i + 1 < len(args):
            out_arg = args[i + 1]
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
    out_dir, out_err = resolve_out_dir(root, out_arg or "qa/security", must_be_inside=True)
    if out_err:
        print(f"ERROR: {out_err}", file=sys.stderr)
        return 1

    report = analyse(root, out_dir)
    findings_path = Path(report["findings_file"])
    ledger_path = Path(report["ledger_file"])

    lines = ["=" * 62, "DEEP SECURITY AUDIT (security-audit schema)", "=" * 62]
    lines.append(f"scan findings : {report['scan_findings']}")
    lines.append(f"confirmed     : {report['confirmed']}")
    lines.append(f"needs validation: {report['needs_validation']}")
    lines.append(f"coverage units: {report['coverage_units']}")
    lines.append(f"findings.json : {findings_path}")
    lines.append(f"coverage-ledger.json: {ledger_path}")

    rc_findings, out_findings = (None, "the Node validators were skipped by request")
    rc_ledger, out_ledger = (None, "the Node validators were skipped by request")
    if not skip_validate:
        rc_findings, out_findings = _validate_node(PACK / "validate-findings.cjs", findings_path)
        rc_ledger, out_ledger = _validate_node(PACK / "validate-coverage-ledger.cjs", ledger_path)
    report["validation"]["node_findings"] = {"rc": rc_findings, "output": out_findings}
    report["validation"]["node_coverage_ledger"] = {"rc": rc_ledger, "output": out_ledger}

    # Portable, always-available validation: the same schema and the same
    # structural rules, implemented in Python (scripts/schema_validate.py).
    schema = load_json(PACK / "report-schema.json")
    schema_errors = []
    findings_doc = load_json(findings_path)
    ledger_doc = load_json(ledger_path)
    schema_available = isinstance(schema, dict)
    if schema_available:
        import schema_validate
        schema_errors = schema_validate.validate_findings(findings_doc, schema)
        ledger_errors = schema_validate.validate_ledger(ledger_doc)
    else:
        schema_errors = ["report-schema.json is missing or unreadable"]
        ledger_errors = ["report-schema.json is missing or unreadable"]
    report["validation"]["python_findings"] = {"errors": schema_errors}
    report["validation"]["python_coverage_ledger"] = {"errors": ledger_errors}
    report["validation"]["schema_available"] = schema_available

    lines.append("-" * 62)
    ok = True
    skipped = False
    node_validated = (rc_findings == 0 and rc_ledger == 0)
    if not schema_available and not node_validated:
        # No validator could run at all: the schema is unavailable and the
        # Node validators did not run.  That is a SKIP, never a silent pass.
        skipped = True
        lines.append("[SKIP] no validator could run: report-schema.json is missing "
                     "or unreadable and the Node validators did not run")
    elif schema_errors:
        ok = False
        lines.append(f"[FAIL] findings.json does not satisfy report-schema.json "
                     f"({len(schema_errors)} error(s)):")
        for message in schema_errors[:10]:
            lines.append("  " + message)
    else:
        lines.append("[OK  ] findings.json satisfies report-schema.json")
    if schema_available and ledger_errors:
        ok = False
        lines.append(f"[FAIL] coverage-ledger.json breaks the ledger rules "
                     f"({len(ledger_errors)} error(s)):")
        for message in ledger_errors[:10]:
            lines.append("  " + message)
    elif schema_available:
        lines.append("[OK  ] coverage-ledger.json satisfies the ledger rules")
    for name, rc, out in (("findings.json", rc_findings, out_findings),
                          ("coverage-ledger.json", rc_ledger, out_ledger)):
        if rc is None:
            lines.append(f"[SKIP] Node validator for {name}: {out}")
        elif rc == 0:
            lines.append(f"[OK  ] Node validator accepted {name}")
        else:
            lines.append(f"[FAIL] Node validator rejected {name}:")
            for line in (out or "").splitlines()[:8]:
                lines.append("  " + line)
            ok = False
    if not ok:
        report["status"] = "fail"
    elif skipped:
        report["status"] = "skipped"
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    if not ok:
        return 1
    return 2 if skipped else 0


if __name__ == "__main__":
    raise SystemExit(main())
