#!/usr/bin/env python3
"""Shared helpers for the extended gates (N-U) and the absorbed-skill runners.

Everything here is stdlib-only so the skill keeps working with nothing but a
Python interpreter.  The module provides:

* a tiny check/severity model shared by every new gate script
* an HTTP client built on urllib (no third-party dependency)
* a runner for the scripts absorbed from sibling skills in
  ``scripts/absorbed`` (see ``scripts/absorbed/MANIFEST.json``)
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ABSORBED_DIR = SCRIPT_DIR / "absorbed"

SEVERITY_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}


class Check:
    """One named check inside a gate."""

    def __init__(self, name, ok, required=True, detail=""):
        self.name = name
        self.ok = bool(ok)
        self.required = bool(required)
        self.detail = detail

    def as_dict(self):
        return {"name": self.name, "ok": self.ok, "required": self.required,
                "detail": self.detail}

    def __repr__(self):  # pragma: no cover - debugging aid
        return f"Check({self.name!r}, ok={self.ok}, required={self.required})"


class GateResult:
    """The result of a gate: a list of checks plus optional findings."""

    def __init__(self, gate, title, checks=None, findings=None, notes=None,
                 skipped=False, reason=""):
        self.gate = gate
        self.title = title
        self.checks = list(checks or [])
        self.findings = list(findings or [])
        self.notes = list(notes or [])
        self.skipped = skipped
        self.reason = reason

    def add(self, name, ok, required=True, detail=""):
        self.checks.append(Check(name, ok, required, detail))
        return self

    def fail(self, name, detail, severity="MEDIUM"):
        self.checks.append(Check(name, False, True, detail))
        self.findings.append({"severity": severity, "check": name, "detail": detail})
        return self

    def warn(self, name, detail):
        # a warning is NOT a pass: it must never be counted as one, it must
        # only stay out of the blocking list
        self.checks.append(Check(name, False, False, detail))
        self.findings.append({"severity": "LOW", "check": name, "detail": detail})
        return self

    @property
    def blocking(self):
        return [c for c in self.checks if c.required and not c.ok]

    @property
    def status(self):
        if self.skipped:
            return "skipped"
        return "fail" if self.blocking else "ok"

    def as_dict(self):
        return {
            "gate": self.gate,
            "title": self.title,
            "status": self.status,
            "skipped": self.skipped,
            "reason": self.reason,
            "checks": [c.as_dict() for c in self.checks],
            "findings": self.findings,
            "notes": self.notes,
            "blocking": [f"{c.name}: {c.detail}" for c in self.blocking],
            "summary": {
                "checks": len(self.checks),
                "passed": len([c for c in self.checks if c.ok]),
                "failed": len(self.blocking),
                "warnings": len([c for c in self.checks
                                 if not c.required and not c.ok]),
            },
        }


# --------------------------------------------------------------------------
# text helpers
# --------------------------------------------------------------------------

CODE_EXT = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".go", ".rs",
            ".rb", ".php", ".java", ".kt", ".swift", ".vue", ".svelte", ".html",
            ".css", ".scss", ".sql", ".yaml", ".yml", ".json", ".toml", ".sh",
            ".tf", ".graphql", ".prisma"}

SKIP_DIRS = {"node_modules", ".git", "dist", "build", "out", ".next", ".nuxt",
             "coverage", "__pycache__", ".venv", "venv", "vendor", "target",
             ".pytest_cache", "qa", ".cache", ".idea", ".vscode"}


def walk_files(root: Path, exts=None, skip_dirs=None):
    """Yield files under root, skipping vendor/build directories."""
    skip = set(skip_dirs or SKIP_DIRS)
    exts = {e.lower() for e in exts} if exts else None
    root = Path(root)
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in skip for part in path.parts):
            continue
        if exts and path.suffix.lower() not in exts:
            continue
        yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def read_files(root: Path, exts=None, skip_dirs=None):
    """Return a list of (path, text) pairs."""
    return [(p, read_text(p)) for p in walk_files(root, exts, skip_dirs)]


def grep(root: Path, pattern, exts=None, skip_dirs=None, flags=re.I):
    """Find regex matches in the project.  Returns [(path, line_no, line)]."""
    rx = re.compile(pattern, flags)
    hits = []
    for path, text in read_files(root, exts, skip_dirs):
        for n, line in enumerate(text.splitlines(), 1):
            if rx.search(line):
                hits.append((path, n, line.strip()[:200]))
    return hits


# --------------------------------------------------------------------------
# HTTP (stdlib only)
# --------------------------------------------------------------------------

def _parse_json(text):
    text = (text or "").strip()
    if text.startswith("{") or text.startswith("["):
        try:
            return json.loads(text)
        except ValueError:
            return None
    return None


def http_request(url, method="GET", headers=None, body=None, timeout=15.0,
                 allow_redirects=True):
    """Perform an HTTP request.  Returns a dict; never raises for HTTP errors."""
    req = urllib.request.Request(url, data=body, method=method)
    for key, value in (headers or {}).items():
        req.add_header(key, value)
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            text = raw.decode("utf-8", errors="ignore")
            return {
                "ok": True,
                "status": resp.status,
                "headers": {k.lower(): v for k, v in resp.headers.items()},
                "body": text,
                "bytes": len(raw),
                "json": _parse_json(text),
                "elapsed_ms": round((time.perf_counter() - started) * 1000, 1),
                "error": "",
            }
    except urllib.error.HTTPError as exc:
        raw = b""
        try:
            raw = exc.read()
        except Exception:
            pass
        text = raw.decode("utf-8", errors="ignore")
        return {
            "ok": False,
            "status": exc.code,
            "headers": {k.lower(): v for k, v in (exc.headers or {}).items()},
            "body": text,
            "bytes": len(raw),
            "json": _parse_json(text),
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 1),
            "error": f"HTTP {exc.code}",
        }
    except Exception as exc:
        return {
            "ok": False,
            "status": 0,
            "headers": {},
            "body": "",
            "bytes": 0,
            "json": None,
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 1),
            "error": str(exc),
        }


def http_json(url, method="GET", payload=None, headers=None, timeout=15.0):
    hdrs = {"Accept": "application/json"}
    hdrs.update(headers or {})
    body = None
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        hdrs.setdefault("Content-Type", "application/json")
    res = http_request(url, method=method, headers=hdrs, body=body, timeout=timeout)
    res["json"] = None
    text = (res.get("body") or "").strip()
    if text.startswith("{") or text.startswith("["):
        try:
            res["json"] = json.loads(text)
        except ValueError:
            res["json"] = None
    return res


# --------------------------------------------------------------------------
# absorbed sibling-skill scripts
# --------------------------------------------------------------------------

def _extract_json(text):
    """Pull a JSON document out of mixed stdout (most absorbed scripts print
    a human report around the JSON).  Returns None when nothing parses."""
    if not text:
        return None
    start = text.find("{")
    if start == -1:
        start = text.find("[")
    if start == -1:
        return None
    for end in range(len(text), start, -1):
        chunk = text[start:end].rstrip()
        if not chunk:
            continue
        try:
            return json.loads(chunk)
        except ValueError:
            continue
    return None


def run_absorbed(name, target, timeout=180, extra_args=()):
    """Run one of the scripts absorbed from sibling skills.

    Returns a dict with the exit code, captured output and (when the script
    emitted one) the parsed JSON payload.  ``ok`` mirrors the absorbed
    script's own exit code: 0 = clean, 1 = findings.
    """
    script = ABSORBED_DIR / name
    if not script.is_file():
        return {"available": False, "ok": True, "rc": 0, "stdout": "",
                "stderr": "", "json": None,
                "detail": f"{name} is not present in scripts/absorbed/"}
    cmd = [sys.executable, str(script), str(target), *extra_args]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              timeout=timeout, cwd=str(target) if Path(target).is_dir() else None)
    except subprocess.TimeoutExpired:
        return {"available": True, "ok": False, "rc": 124, "stdout": "",
                "stderr": f"timeout after {timeout}s", "json": None,
                "detail": f"{name} timed out"}
    except OSError as exc:
        return {"available": True, "ok": False, "rc": 127, "stdout": "",
                "stderr": str(exc), "json": None, "detail": f"{name} could not run"}
    out = proc.stdout or ""
    return {
        "available": True,
        "ok": proc.returncode == 0,
        "rc": proc.returncode,
        "stdout": out,
        "stderr": proc.stderr or "",
        "json": _extract_json(out),
        "detail": f"{name} exit={proc.returncode}",
    }


# --------------------------------------------------------------------------
# report printing
# --------------------------------------------------------------------------

def print_report(result: GateResult, json_mode=False, extra=None):
    """Print a gate result the same way every script in this skill does.

    In JSON mode nothing is printed here - the caller hands the payload to
    ``qa_common.emit`` so stdout carries exactly one JSON document.
    """
    payload = result.as_dict()
    if extra:
        payload.update(extra)
    if json_mode:
        return payload
    bar = "=" * 62
    print(bar)
    print(f"{result.gate}  {result.title}")
    print(bar)
    if result.skipped:
        print(f"[SKIP] {result.reason}")
    for check in result.checks:
        if check.required:
            icon = "PASS" if check.ok else "FAIL"
        else:
            icon = "warn" if not check.ok else "PASS"
        detail = f"  -> {check.detail}" if check.detail else ""
        print(f"[{icon}] {check.name}{detail}")
    for note in result.notes:
        print(f"  note: {note}")
    print("-" * 62)
    print(f"blocking failures: {len(result.blocking)}")
    print(bar)
    return payload


def parse_common_args(argv=None):
    """Parse the flags every gate script understands.

    Returns (root, options dict).  Unknown flags are ignored on purpose so a
    script never mistakes a flag for a path.
    """
    argv = list(sys.argv[1:] if argv is None else argv)
    root = "."
    opts = {
        "url": None,
        "routes": [],
        "healthz": "/healthz",
        "json": False,
        "timeout": 30.0,
        "budget": 0,
        "strict": False,
        "extra": [],
    }
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--root" and i + 1 < len(argv):
            root = argv[i + 1]
            i += 1
        elif a == "--url" and i + 1 < len(argv):
            opts["url"] = argv[i + 1]
            i += 1
        elif a == "--routes" and i + 1 < len(argv):
            opts["routes"] = [r.strip() for r in argv[i + 1].split(",") if r.strip()]
            i += 1
        elif a == "--healthz" and i + 1 < len(argv):
            opts["healthz"] = argv[i + 1]
            i += 1
        elif a == "--timeout" and i + 1 < len(argv):
            try:
                opts["timeout"] = float(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--budget" and i + 1 < len(argv):
            try:
                opts["budget"] = int(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--json":
            opts["json"] = True
        elif a == "--strict":
            opts["strict"] = True
        elif a.startswith("-"):
            opts["extra"].append(a)
        i += 1
    return root, opts
