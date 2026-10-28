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
        (r"Access-Control-Allow-Origin['\"]?\s*[:,]\s*['\"]\*", "MEDIUM", "CORS wildcard origin"),
        (r"(?i)httpOnly\s*:\s*false", "MEDIUM", "cookie without httpOnly"),
        (r"(?i)secure\s*:\s*false", "LOW", "cookie without secure flag"),
    ]
    for p in walk(root):
        if p.suffix not in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".py", ".go"}:
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
    """npm audit summary (skip if no node project, no lockfile, or offline)."""
    if not (root / "package.json").is_file():
        return []
    # `npm audit` requires a lockfile. Without one it errors out *and* writes
    # noise to the console handle, which would corrupt machine-readable output.
    if not any((root / f).is_file() for f in ("package-lock.json", "npm-shrinkwrap.json")):
        return []
    env = dict(os.environ)
    env.update({
        "npm_config_loglevel": "silent",
        "npm_config_progress": "false",
        "npm_config_fund": "false",
        "npm_config_update_notifier": "false",
        "NO_UPDATE_NOTIFIER": "1",
    })
    try:
        proc = subprocess.run(
            ["npm", "audit", "--json", "--omit=dev"],
            cwd=root, capture_output=True, text=True, timeout=120,
            env=env,
        )
        if proc.returncode not in (0, 1):
            return []
        data = json.loads(proc.stdout or "{}")
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError):
        return []
    if data.get("error"):
        # e.g. ENOLOCK / offline / registry unreachable -> not a finding.
        return []
    vulns = data.get("metadata", {}).get("vulnerabilities", {})
    out = []
    for level in ("critical", "high"):
        if vulns.get(level):
            out.append({
                "severity": level.upper(), "type": f"{vulns[level]} vulnerable {level} dependencies",
                "file": "package.json", "line": 0,
            })
    return out


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

    findings = scan_secrets(root) + scan_patterns(root) + scan_audit(root)

    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    findings.sort(key=lambda f: (order.get(f["severity"], 3), f["file"], f["line"]))

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
