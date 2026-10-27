#!/usr/bin/env python3
"""Environment bootstrapper and dependency checker for app-production-readiness.

Checks whether the host machine has the required tooling installed for full-fidelity
audits (Playwright, browser engines, Lighthouse, Node.js, Python), and optionally installs
missing dependencies when invoked with `--install`.

Usage:
    python scripts/bootstrap_env.py [--json] [--install] [--browsers chromium,firefox,webkit]

Exit codes:
    0 - All required and recommended tools are available
    1 - Missing critical tools or installation failure
    2 - Operational in degraded mode (some optional deep gates will be skipped)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, run_cmd, which


def check_python() -> dict:
    major, minor = sys.version_info[:2]
    ok = (major, minor) >= (3, 8)
    return {
        "name": "python",
        "version": f"{major}.{minor}.{sys.version_info[2]}",
        "available": True,
        "required": True,
        "ok": ok,
        "detail": "Python 3.8+ is active" if ok else "Python 3.8+ required",
    }


def check_node() -> dict:
    node_path = which("node")
    if not node_path:
        return {
            "name": "node",
            "version": None,
            "available": False,
            "required": False,
            "ok": False,
            "detail": "node not found in PATH (needed for Lighthouse)",
        }
    code, stdout, _ = run_cmd(["node", "--version"], timeout=5)
    version = stdout.strip() if code == 0 else "unknown"
    return {
        "name": "node",
        "version": version,
        "available": True,
        "required": False,
        "ok": True,
        "detail": f"Node.js found ({version})",
    }


def check_playwright() -> dict:
    try:
        import playwright  # noqa: F401
        has_module = True
    except ImportError:
        has_module = False

    if not has_module:
        return {
            "name": "playwright",
            "module_installed": False,
            "browsers": {},
            "available": False,
            "required": False,
            "ok": False,
            "detail": "Python playwright package not installed (pip install playwright)",
        }

    # Check browser engine availability via playwright cli
    browsers = {}
    for engine in ("chromium", "firefox", "webkit"):
        try:
            # Quick check if engine can launch headlessly
            code, out, _ = run_cmd(
                [sys.executable, "-c",
                 f"from playwright.sync_api import sync_playwright; p=sync_playwright().start(); b=p.{engine}.launch(); b.close(); p.stop()"],
                timeout=10,
            )
            browsers[engine] = (code == 0)
        except Exception:
            browsers[engine] = False

    all_browsers = all(browsers.values())
    any_browsers = any(browsers.values())
    return {
        "name": "playwright",
        "module_installed": True,
        "browsers": browsers,
        "available": any_browsers,
        "required": False,
        "ok": all_browsers,
        "detail": (
            "All browser engines ready" if all_browsers else
            ("Partial browser engines ready" if any_browsers else "Browser binaries missing (run: playwright install)")
        ),
    }


def check_lighthouse() -> dict:
    lh_path = which("lighthouse")
    if lh_path:
        code, out, _ = run_cmd(["lighthouse", "--version"], timeout=5)
        return {
            "name": "lighthouse",
            "version": out.strip() if code == 0 else "installed",
            "available": True,
            "required": False,
            "ok": True,
            "detail": f"Lighthouse CLI installed globally ({out.strip()})",
        }

    npx_path = which("npx")
    if npx_path:
        return {
            "name": "lighthouse",
            "version": "via npx",
            "available": True,
            "required": False,
            "ok": True,
            "detail": "Lighthouse available on-demand via npx",
        }

    return {
        "name": "lighthouse",
        "version": None,
        "available": False,
        "required": False,
        "ok": False,
        "detail": "Neither lighthouse nor npx found (Gate D will be skipped)",
    }


def install_dependencies(browsers_to_install: list[str] | None = None):
    """Install the missing tooling. Returns (log lines, succeeded)."""
    logs = []
    ok = True
    # 1. install python packages
    logs.append("[INSTALL] Installing python dependencies (playwright, pytest)...")
    code, out, err = run_cmd([sys.executable, "-m", "pip", "install", "playwright", "pytest"], timeout=180)
    if code != 0:
        logs.append(f"[FAIL] pip install failed: {err}")
        ok = False
    else:
        logs.append("[OK] Python packages installed successfully.")

    # 2. install browser engines
    engines = browsers_to_install or ["chromium", "firefox", "webkit"]
    logs.append(f"[INSTALL] Installing Playwright browsers: {', '.join(engines)}...")
    code, out, err = run_cmd([sys.executable, "-m", "playwright", "install"] + engines, timeout=300)
    if code != 0:
        logs.append(f"[FAIL] playwright install failed: {err}")
        ok = False
    else:
        logs.append("[OK] Playwright browser binaries installed.")

    return logs, ok


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Audit and prepare environment for production readiness reviews.")
    parser.add_argument("--json", action="store_true", help="Output JSON on stdout")
    parser.add_argument("--install", action="store_true", help="Automatically install missing dependencies")
    parser.add_argument("--browsers", default="chromium,firefox,webkit", help="Comma-separated browser engines to install")
    args = parser.parse_args(argv)

    install_logs = []
    install_ok = True
    if args.install:
        engines = [b.strip() for b in args.browsers.split(",") if b.strip()]
        install_logs, install_ok = install_dependencies(engines)

    py_stat = check_python()
    node_stat = check_node()
    pw_stat = check_playwright()
    lh_stat = check_lighthouse()

    checks = [py_stat, node_stat, pw_stat, lh_stat]
    all_ok = all(c["ok"] for c in checks)
    # Every optional tool that is missing puts the environment in DEGRADED mode:
    # the deep gates that need it will be SKIPPED, never silently passed.
    degraded = not node_stat["ok"] or not pw_stat["ok"] or not lh_stat["ok"]
    failed = not py_stat["ok"] or not install_ok

    human_lines = ["ENVIRONMENT BOOTSTRAP CHECK", "=" * 40]
    for c in checks:
        icon = "[OK]" if c["ok"] else ("[WARN]" if not c["required"] else "[FAIL]")
        human_lines.append(f"{icon} {c['name']:12}: {c['detail']}")

    if install_logs:
        human_lines.append("-" * 40)
        human_lines.extend(install_logs)

    human_lines.append("=" * 40)
    if failed:
        human_lines.append("Environment is NOT ready - a required tool is missing or an install failed.")
        if not install_ok:
            human_lines.append("[FAIL] installation failed - see the log above.")
    elif all_ok:
        human_lines.append("Environment is 10/10 ready for all 21 quality gates.")
    else:
        human_lines.append("Environment is operational, but optional deep gates (Lighthouse / multi-browser) may be SKIPPED.")
        human_lines.append("Tip: Run `python scripts/bootstrap_env.py --install` to install missing tools.")

    payload = {
        "status": "ready" if all_ok else ("failed" if failed else "degraded"),
        "all_ok": all_ok,
        "degraded": degraded,
        "install_ok": install_ok,
        "checks": checks,
        "install_logs": install_logs,
    }

    emit(human_lines, payload, args.json)

    if failed:
        return 1
    if degraded:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
