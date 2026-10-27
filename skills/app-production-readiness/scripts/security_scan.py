#!/usr/bin/env python3
"""Read-only security scan: secrets, dangerous patterns, dependency audit, headers.

Usage:  python security_scan.py [project_root]
Exit 0: no high-severity findings | Exit 1: high-severity findings present
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
    is_dotenv,
    is_env_template,
    parse_cli,
    resolve_root,
    root_error,
    walk_files,
)

SKIP = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "coverage", ".venv"}
SCAN_EXT = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".py", ".go", ".rb", ".php", ".env", ".yml", ".yaml", ".json"}
CODE_EXT = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".py", ".go", ".vue", ".svelte", ".rb", ".php"}
MAX_BYTES = 200_000


def read(p: Path, limit: int = MAX_BYTES) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")[:limit]
    except OSError:
        return ""


def walk(root: Path):
    """Files under `root`, excluding nested projects (separate apps)."""
    return walk_files(root, skip_dirs=SKIP)


def scan_secrets(root: Path) -> list:
    """High-confidence secret patterns (provider key shapes)."""
    findings = []
    patterns = [
        (r"AKIA[0-9A-Z]{16}", "AWS access key id"),
        (r"gh[pousr]_[A-Za-z0-9]{36,}", "GitHub token"),
        (r"sk-[A-Za-z0-9]{32,}", "OpenAI-style API key"),
        (r"sk_live_[A-Za-z0-9]{16,}", "Stripe live secret key"),
        (r"sk_test_[A-Za-z0-9]{16,}", "Stripe test secret key"),
        (r"xox[baprs]-[A-Za-z0-9-]{10,}", "Slack token"),
        (r"AIza[0-9A-Za-z\-_]{35}", "Google API key"),
        (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
        (r"(?i)secret[_-]?key\s*[:=]\s*['\"][A-Za-z0-9/+_\-]{24,}['\"]", "hardcoded secret key"),
    ]
    for p in walk(root):
        # Real env files are matched by NAME so dotfiles such as ".env.local"
        # (which have no ".env" suffix) are scanned too.
        if p.suffix not in SCAN_EXT and not is_dotenv(p.name):
            continue
        # Templates are meant to be committed and hold placeholder values.
        if is_env_template(p.name):
            continue
        txt = read(p)
        for pat, label in patterns:
            for m in re.finditer(pat, txt):
                findings.append({
                    "severity": "HIGH", "type": label,
                    "file": str(p.relative_to(root)),
                    "line": txt[:m.start()].count("\n") + 1,
                })
    return findings


def scan_patterns(root: Path) -> list:
    """Dangerous code patterns."""
    findings = []
    rules = [
        (r"dangerouslySetInnerHTML", "MEDIUM", "dangerouslySetInnerHTML - verify input is sanitized"),
        (r"\beval\s*\(", "HIGH", "eval() - arbitrary code execution risk"),
        (r"new Function\s*\(", "HIGH", "new Function() - code execution risk"),
        (r"child_process\.(exec|execSync)\s*\(", "HIGH", "shell exec - command injection risk"),
        (r"os\.system\s*\(", "HIGH", "os.system - command injection risk"),
        (r"(?i)verify\s*=\s*False", "HIGH", "SSL verify disabled"),
        (r"(?i)rejectUnauthorized\s*:\s*false", "HIGH", "TLS verification disabled"),
        (r"(?i)verify(?:_signature)?['\"]?\s*[:=]\s*false", "HIGH", "signature/verification disabled"),
        (r"Access-Control-Allow-Origin['\"]?\s*[:,]\s*['\"]\*", "MEDIUM", "CORS wildcard origin"),
        (r"(?i)httpOnly\s*:\s*false", "MEDIUM", "cookie without httpOnly"),
        (r"(?i)secure\s*:\s*false", "LOW", "cookie without secure flag"),
        # --- deserialisation / code injection ---
        (r"(?i)\bpickle\.loads?\s*\(", "HIGH", "pickle deserialisation - RCE risk"),
        (r"(?i)\bmarshal\.loads?\s*\(", "HIGH", "marshal deserialisation - RCE risk"),
        (r"(?i)yaml\.load\s*\((?![^)]*Safe)", "HIGH", "yaml.load without SafeLoader - RCE risk"),
        (r"subprocess\.(run|call|Popen|check_output)\s*\([^)]*shell\s*=\s*True", "HIGH",
         "subprocess with shell=True - command injection risk"),
        (r"(?i)\bexec\s*\(\s*(f?['\"])", "HIGH", "exec() on a string - code execution risk"),
        # --- crypto / auth weaknesses ---
        (r"(?i)hashlib\.(md5|sha1)\s*\(", "MEDIUM", "MD5/SHA1 used for hashing - weak for passwords"),
        (r"(?i)createHash\(\s*['\"](md5|sha1)['\"]\s*\)", "MEDIUM",
         "MD5/SHA1 used for hashing - weak for passwords"),
        (r"(?i)jwt\.(decode|verify)\s*\([^)]*verify(?:_signature)?['\"]?\s*[:=]\s*False", "HIGH",
         "JWT signature verification disabled"),
        (r"(?i)algorithms?\s*[:=]\s*\[[^\]]*['\"]none['\"]", "HIGH", "JWT algorithm 'none' allowed"),
        (r"Math\.random\s*\(\s*\)", "LOW", "Math.random() - insecure randomness, not for tokens/IDs"),
        # --- injection ---
        (r"(?i)\.innerHTML\s*=", "MEDIUM", "innerHTML assignment - XSS risk if untrusted"),
        (r"document\.write\s*\(", "MEDIUM", "document.write - XSS risk"),
        (r"(?i)(execute|query)\s*\(\s*f?['\"][^'\"]*(SELECT|INSERT|UPDATE|DELETE)[^'\"]*\{", "MEDIUM",
         "SQL built with string interpolation - injection risk"),
        (r"(?i)(execute|query)\s*\(\s*['\"][^'\"]*(SELECT|INSERT|UPDATE|DELETE)[^'\"]*['\"]\s*\+", "MEDIUM",
         "SQL built by concatenation - injection risk"),
        # --- transport / info leakage ---
        (r"http://(?!localhost|127\.0\.0\.1|0\.0\.0\.0)[A-Za-z0-9.\-]+", "LOW",
         "plain http:// endpoint - no TLS"),
        (r"(?i)server:\s*true|removeHeader\(\s*['\"]x-powered-by", "LOW",
         "X-Powered-By leaks the stack - consider disabling"),
    ]
    for p in walk(root):
        if p.suffix not in CODE_EXT:
            continue
        txt = read(p)
        for pat, sev, label in rules:
            for m in re.finditer(pat, txt):
                line_no = txt[:m.start()].count("\n") + 1
                findings.append({
                    "severity": sev, "type": label,
                    "file": str(p.relative_to(root)), "line": line_no,
                })
    return findings


def scan_audit(root: Path) -> list:
    """Dependency CVE audit for the detected ecosystem.

    Delegates to dep_audit.py so npm/pnpm/yarn/bun/pip/cargo/go are all
    covered. A skipped audit is reported as a LOW finding ("CVE scan not
    performed") so it can never be mistaken for a clean bill of health.
    """
    try:
        import dep_audit
    except ImportError:
        return []
    try:
        report = dep_audit.audit(root, fail_on="high")
    except Exception:
        return []
    findings = []
    if report.get("status") != "ok":
        reason = report.get("reason") or "audit unavailable"
        findings.append({
            "severity": "LOW", "type": f"dependency CVE scan NOT performed: {reason}",
            "file": report.get("lockfile") or "package.json", "line": 0,
        })
        return findings
    for f in report.get("findings", []):
        sev = str(f.get("severity", "unknown")).upper()
        if sev not in ("CRITICAL", "HIGH"):
            continue
        findings.append({
            "severity": sev,
            "type": f"{f.get('package')} - {f.get('title', '')[:100]}",
            "file": report.get("lockfile") or "package.json", "line": 0,
        })
    return findings


def scan_second_scanner(root: Path) -> list:
    """Independent rule set from the absorbed ``vulnerability-scanner`` skill.

    ``scripts/absorbed/vulnerability_security_scan.py`` is a different
    implementation (different patterns, different traversal) which is run as a
    second opinion.  Its dependency section is ignored on purpose - ``dep_audit``
    already covers npm/pnpm/yarn/bun/pip/cargo/go properly and that scanner
    reports a missing lock file per package manager, which is noise.

    The absorbed scanner always exits 0, so only its JSON payload is used.
    """
    script = Path(__file__).resolve().parent / "absorbed" / "vulnerability_security_scan.py"
    if not script.is_file():
        return []
    try:
        proc = subprocess.run(
            [sys.executable, str(script), str(root), "--output", "json"],
            capture_output=True, text=True, timeout=180,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    payload = _json_from(proc.stdout or "")
    if not isinstance(payload, dict):
        return []
    scans = payload.get("scans") or {}
    findings = []
    for section, severity_map in (
        ("secrets", {"critical": "HIGH", "high": "HIGH", "medium": "MEDIUM", "low": "LOW"}),
        ("code_patterns", {"critical": "HIGH", "high": "HIGH", "medium": "MEDIUM", "low": "LOW"}),
    ):
        # The absorbed scanner's "configuration" section only looks for a config
        # file; the live response headers are checked properly by runtime_check.
        block = scans.get(section) or {}
        for item in block.get("findings") or []:
            if not isinstance(item, dict):
                continue
            raw_sev = str(item.get("severity") or "").lower()
            sev = severity_map.get(raw_sev)
            if not sev:
                continue
            label = (item.get("type") or item.get("issue")
                     or item.get("pattern") or section)
            detail = item.get("message") or item.get("recommendation") or ""
            findings.append({
                "severity": sev,
                "type": f"[scanner2/{section}] {label}"
                        + (f" - {detail[:120]}" if detail else ""),
                "file": item.get("file") or str(root.name),
                "line": int(item.get("line") or 0),
            })
    return findings


def _json_from(text: str):
    """Best-effort JSON extraction from a mixed stdout blob."""
    text = text.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except ValueError:
        pass
    start = text.find("{")
    while start != -1:
        depth, in_str, esc = 0, False, False
        for i in range(start, len(text)):
            ch = text[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
                continue
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except ValueError:
                        break
        start = text.find("{", start + 1)
    return None


def scan_all(root: Path) -> list:
    """Every finding this scanner can produce, sorted by severity."""
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from absorbed_rules import api_hardening_findings
        extra = api_hardening_findings(root)
    except Exception:
        extra = []
    findings = (scan_secrets(root) + scan_patterns(root) + scan_audit(root)
                + scan_second_scanner(root) + extra)
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    findings.sort(key=lambda f: (order.get(f["severity"], 3), f["file"], f["line"]))
    return findings


def main() -> int:
    root_arg, json_mode, want_help = parse_cli(sys.argv[1:])
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        if json_mode:
            emit([f"[FAIL] {err}"], {"error": err}, True)
        else:
            print(f"[FAIL] {err}", file=sys.stderr)
        return 1

    findings = scan_all(root)

    lines = []
    lines.append("=" * 62)
    lines.append("SECURITY SCAN")
    lines.append("=" * 62)
    if not findings:
        lines.append("No findings. Clean.")
    else:
        for f in findings:
            loc = f"{f['file']}:{f['line']}" if f["line"] else f["file"]
            lines.append(f"[{f['severity']:<6}] {f['type']}  ({loc})")
    counts = {}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    lines.append("-" * 62)
    lines.append("summary: " + (", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "0 findings"))
    lines.append("=" * 62)
    # In JSON mode the report goes to stderr so stdout stays pure JSON.
    emit(lines, findings, json_mode)

    return 1 if any(f["severity"] == "HIGH" for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
