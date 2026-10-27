#!/usr/bin/env python3
"""Dependency vulnerability audit for every ecosystem the skill supports.

Replaces the npm-only audit that used to hide pnpm/yarn/bun and
non-Node projects. Each ecosystem is audited with its own native tool;
when that tool is not installed the audit is reported as SKIPPED with a
reason, never as a silent pass.

Usage:
  python dep_audit.py [project_root] [--json] [--fail-on high]

Exit 0: no findings at or above --fail-on severity
Exit 1: findings at or above the threshold, or the audit could not run
Exit 2: the audit tool itself is unavailable (report says SKIPPED)

Severity order: critical > high > moderate > low
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    emit,
    parse_cli,
    resolve_root,
    root_error,
    run_cmd,
    which,
)

SEVERITY_ORDER = ["critical", "high", "moderate", "medium", "low"]
THRESHOLD_ALIASES = {"moderate": "moderate", "medium": "moderate"}


def _rank(sev: str) -> int:
    """Numeric rank of a severity string (higher = more severe)."""
    s = str(sev or "").strip().lower()
    s = THRESHOLD_ALIASES.get(s, s)
    if s in ("critical",):
        return 4
    if s in ("high",):
        return 3
    if s in ("moderate", "medium"):
        return 2
    if s in ("low",):
        return 1
    return 0


def _at_or_above(sev: str, threshold: str) -> bool:
    return _rank(sev) >= _rank(threshold)


def detect_ecosystem(root: Path):
    """(ecosystem, lockfile name) for the project."""
    for name, eco in (
        ("pnpm-lock.yaml", "node-pnpm"),
        ("bun.lockb", "node-bun"),
        ("bun.lock", "node-bun"),
        ("yarn.lock", "node-yarn"),
        ("package-lock.json", "node-npm"),
    ):
        if (root / name).is_file():
            return eco, name
    if (root / "package.json").is_file():
        return "node-npm", ""
    for name, eco in (
        ("requirements.txt", "python"),
        ("uv.lock", "python"),
        ("poetry.lock", "python"),
        ("Pipfile.lock", "python"),
        ("pyproject.toml", "python"),
    ):
        if (root / name).is_file():
            return eco, name
    if (root / "Cargo.lock").is_file() or (root / "Cargo.toml").is_file():
        return "rust", "Cargo.lock"
    if (root / "go.sum").is_file() or (root / "go.mod").is_file():
        return "go", "go.sum"
    return "unknown", ""


def _npm_findings(data) -> list:
    """npm audit v2/v1 JSON -> flat findings list."""
    out = []
    vulns = (data or {}).get("vulnerabilities")
    if isinstance(vulns, dict):
        for name, v in vulns.items():
            sev = str(v.get("severity", "")).lower()
            via = v.get("via") or []
            title, url = "", ""
            for item in via:
                if isinstance(item, dict):
                    title = item.get("title", title)
                    url = item.get("url", url)
                    if item.get("severity"):
                        sev = str(item["severity"]).lower()
                    break
            out.append({
                "package": name,
                "severity": sev or "unknown",
                "title": title or v.get("name", "") or name,
                "url": url,
                "fixed_in": (v.get("fixAvailable") or {}).get("version")
                if isinstance(v.get("fixAvailable"), dict) else None,
            })
        return out
    for key in ("advisories", "vulnerabilities"):
        items = (data or {}).get(key)
        if isinstance(items, dict):
            for _id, v in items.items():
                out.append({
                    "package": (v or {}).get("module_name", (v or {}).get("package_name", "")),
                    "severity": str((v or {}).get("severity", "unknown")).lower(),
                    "title": (v or {}).get("title", ""),
                    "url": (v or {}).get("url", ""),
                    "fixed_in": (v or {}).get("patched_versions"),
                })
    return out


def _generic_findings(data) -> list:
    """Best-effort mapping for pip-audit / cargo-audit / govulncheck JSON."""
    out = []
    if not isinstance(data, dict):
        return out
    # pip-audit
    deps = data.get("dependencies")
    if isinstance(deps, list):
        for d in deps:
            for v in d.get("vulns") or []:
                out.append({
                    "package": d.get("name", ""),
                    "severity": _pip_severity(v),
                    "title": v.get("description", "")[:200],
                    "url": v.get("id", ""),
                    "fixed_in": "; ".join(v.get("fix_versions") or []) or None,
                })
        return out
    # cargo-audit
    vulns = data.get("vulnerabilities")
    if isinstance(vulns, dict):
        for v in vulns.values():
            info = (v.get("advisory") or {})
            out.append({
                "package": (v.get("package") or {}).get("name", ""),
                "severity": "high",
                "title": info.get("title", ""),
                "url": info.get("url", ""),
                "fixed_in": (v.get("versions") or {}).get("patched"),
            })
        return out
    # govulncheck
    if "osv" in data or "vulns" in data:
        for v in (data.get("osv") or []):
            out.append({
                "package": ",".join(v.get("affected") or [])[:120],
                "severity": "high",
                "title": (v.get("summary") or "")[:200],
                "url": v.get("id", ""),
                "fixed_in": None,
            })
    return out


def _pip_severity(v) -> str:
    """pip-audit has no severity field; map CVSS-ish aliases."""
    aliases = (v.get("aliases") or [])
    for a in aliases:
        if "critical" in str(a).lower():
            return "critical"
    return "moderate"


def audit_node(root: Path, eco: str, lock: str):
    """Audit a Node project with its own package manager."""
    if eco == "node-npm":
        if not lock:
            return {"status": "skipped", "state": "not_applicable",
                    "reason": "no package-lock.json (npm audit needs a lockfile)"}
        if not which("npm"):
            return {"status": "skipped", "state": "unavailable", "reason": "npm is not installed"}
        rc, out, err = run_cmd(
            ["npm", "audit", "--json", "--omit=dev"], cwd=root, timeout=180)
        data = load_json_str(out)
        if data is None:
            return {"status": "skipped", "state": "unavailable",
                    "reason": f"npm audit produced no JSON (rc={rc}): {err.strip()[:200]}"}
        return {"status": "ok", "tool": "npm audit", "findings": _npm_findings(data)}
    if eco == "node-pnpm":
        if not which("pnpm"):
            return {"status": "skipped", "state": "unavailable",
                    "reason": "pnpm is not installed (pnpm-lock.yaml present)"}
        rc, out, err = run_cmd(["pnpm", "audit", "--json"], cwd=root, timeout=180)
        data = load_json_str(out)
        if data is None:
            return {"status": "skipped", "state": "unavailable",
                    "reason": f"pnpm audit produced no JSON: {err.strip()[:200]}"}
        return {"status": "ok", "tool": "pnpm audit", "findings": _generic_findings(data)}
    if eco == "node-yarn":
        if not which("yarn"):
            return {"status": "skipped", "state": "unavailable",
                    "reason": "yarn is not installed (yarn.lock present)"}
        rc, out, err = run_cmd(["yarn", "npm", "audit", "--json"], cwd=root, timeout=180)
        data = load_json_str(out)
        if data is None:
            rc, out, err = run_cmd(["yarn", "audit", "--json"], cwd=root, timeout=180)
            data = load_json_str(out)
        if data is None:
            return {"status": "skipped", "state": "unavailable",
                    "reason": f"yarn audit produced no JSON: {err.strip()[:200]}"}
        return {"status": "ok", "tool": "yarn npm audit", "findings": _generic_findings(data)}
    if eco == "node-bun":
        if not which("bun"):
            return {"status": "skipped", "state": "unavailable",
                    "reason": "bun is not installed (bun.lock present)"}
        rc, out, err = run_cmd(["bun", "audit", "--json"], cwd=root, timeout=180)
        data = load_json_str(out)
        if data is None:
            return {"status": "skipped", "state": "unavailable",
                    "reason": f"bun audit produced no JSON: {err.strip()[:200]}"}
        return {"status": "ok", "tool": "bun audit", "findings": _generic_findings(data)}
    return {"status": "skipped", "state": "not_applicable",
                    "reason": f"unsupported node ecosystem {eco}"}


def audit_python(root: Path, eco: str, lock: str):
    if which("pip-audit"):
        rc, out, err = run_cmd(["pip-audit", "--format", "json", "--progress-spinner", "off"],
                               cwd=root, timeout=300)
        data = load_json_str(out)
        if data is None:
            return {"status": "skipped", "state": "unavailable",
                    "reason": f"pip-audit produced no JSON: {err.strip()[:200]}"}
        return {"status": "ok", "tool": "pip-audit", "findings": _generic_findings(data)}
    if which("uv") and (root / "uv.lock").is_file():
        rc, out, err = run_cmd(["uv", "pip", "audit", "--format", "json"], cwd=root, timeout=300)
        data = load_json_str(out)
        if data is not None:
            return {"status": "ok", "tool": "uv pip audit", "findings": _generic_findings(data)}
    return {"status": "skipped", "state": "unavailable",
            "reason": "pip-audit is not installed (pip install pip-audit) - no Python CVE scan performed"}


def audit_rust(root: Path, eco: str, lock: str):
    if which("cargo-audit") or which("cargo-audit.exe"):
        rc, out, err = run_cmd(["cargo-audit", "--json"], cwd=root, timeout=300)
        data = load_json_str(out)
        if data is None:
            return {"status": "skipped", "state": "unavailable",
                    "reason": f"cargo-audit produced no JSON: {err.strip()[:200]}"}
        return {"status": "ok", "tool": "cargo-audit", "findings": _generic_findings(data)}
    return {"status": "skipped", "state": "unavailable",
            "reason": "cargo-audit is not installed (cargo install cargo-audit) - no Rust CVE scan performed"}


def audit_go(root: Path, eco: str, lock: str):
    if which("govulncheck"):
        rc, out, err = run_cmd(["govulncheck", "-json", "./..."], cwd=root, timeout=300)
        data = load_json_str(out)
        if data is None:
            return {"status": "skipped", "state": "unavailable",
                    "reason": f"govulncheck produced no JSON: {err.strip()[:200]}"}
        findings = _generic_findings(data)
        if not findings:
            # govulncheck streams one JSON object per line.
            for line in out.splitlines():
                chunk = load_json_str(line)
                if chunk:
                    findings.extend(_generic_findings(chunk))
        return {"status": "ok", "tool": "govulncheck", "findings": findings}
    return {"status": "skipped", "state": "unavailable",
            "reason": "govulncheck is not installed - no Go CVE scan performed"}


def load_json_str(text: str):
    """Parse JSON from a subprocess stdout blob (tolerates leading noise)."""
    import json as _json
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    try:
        return _json.loads(text)
    except ValueError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end > start:
        try:
            return _json.loads(text[start:end + 1])
        except ValueError:
            return None
    return None


def audit(root: Path, fail_on: str = "high") -> dict:
    eco, lock = detect_ecosystem(root)
    if eco.startswith("node"):
        result = audit_node(root, eco, lock)
    elif eco == "python":
        result = audit_python(root, eco, lock)
    elif eco == "rust":
        result = audit_rust(root, eco, lock)
    elif eco == "go":
        result = audit_go(root, eco, lock)
    else:
        result = {"status": "skipped", "state": "not_applicable",
                  "reason": "no recognised dependency manifest"}

    findings = result.get("findings", []) or []
    blocking = [f for f in findings if _at_or_above(f.get("severity", ""), fail_on)]
    counts = {}
    for f in findings:
        sev = str(f.get("severity", "unknown")).lower()
        counts[sev] = counts.get(sev, 0) + 1

    return {
        "root": str(root),
        "ecosystem": eco,
        "lockfile": lock,
        "status": result.get("status", "skipped"),
        "scan_state": result.get("state") or ("ok" if result.get("status") == "ok" else "unavailable"),
        "tool": result.get("tool"),
        "reason": result.get("reason"),
        "fail_on": fail_on,
        "counts": counts,
        "findings": findings,
        "blocking_count": len(blocking),
    }


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
    fail_on = "high"
    for i, a in enumerate(args):
        if a == "--fail-on" and i + 1 < len(args):
            fail_on = args[i + 1].lower()
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        payload = {"error": err, "status": "failed", "findings": []}
        emit([f"[FAIL] {err}"], payload, True) if json_mode else print(f"[FAIL] {err}", file=sys.stderr)
        return 1

    report = audit(root, fail_on)
    lines = ["=" * 62, f"DEPENDENCY AUDIT  [{report['ecosystem']}]", "=" * 62]
    if report["status"] != "ok":
        lines.append(f"[SKIP] {report.get('reason')}")
        lines.append("-" * 62)
        lines.append("audit could not run - dependency CVEs are UNVERIFIED")
        lines.append("=" * 62)
        emit(lines, report, json_mode)
        # A skipped audit is not a pass: it must never look clean.
        return 2
    lines.append(f"tool: {report['tool']} | lockfile: {report['lockfile'] or 'n/a'}")
    for f in report["findings"]:
        lines.append(f"[{str(f.get('severity','?')).upper()}] {f.get('package')} - {f.get('title','')[:80]}")
    lines.append("-" * 62)
    lines.append(f"findings: {len(report['findings'])} | at/above {fail_on}: {report['blocking_count']}")
    if report["counts"]:
        lines.append("by severity: " + ", ".join(f"{k}={v}" for k, v in sorted(report["counts"].items())))
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    return 1 if report["blocking_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
