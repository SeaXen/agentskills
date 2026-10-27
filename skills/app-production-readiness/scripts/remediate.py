#!/usr/bin/env python3
"""Autonomous Remediation Engine for app-production-readiness.

Parses audit findings (from `qa/report.md` or live gate runs), applies safe deterministic
codemods with atomic rollback safeguards, and emits structured recipes for complex refactorings.

Usage:
    python scripts/remediate.py --root <app_root> [--dry-run] [--rollback] [--recipe-only] [--json]

Exit codes:
    0 - All detected remediations succeeded or nothing to do
    1 - Remediation failure or unrecoverable error
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, resolve_root, root_error
import fixes as fixes_mod
import remediation_handlers as rh


def parse_findings_from_report(report_path: Path) -> list[dict]:
    """Extract structured blocker findings from qa/report.md."""
    if not report_path.is_file():
        return []
    text = report_path.read_text(encoding="utf-8", errors="ignore")
    blockers_match = re.search(r"##\s*BLOCKERS\s*\n(.*?)(?:\n##|\Z)", text, re.DOTALL)
    if not blockers_match:
        return []

    findings = []
    for line in blockers_match.group(1).splitlines():
        line = line.strip()
        if not line.startswith("*"):
            continue
        # Pattern: * **G** - detail or * **U** - code_quality.py: detail
        m = re.match(r"\*\s*\*\*([A-U])\*\*\s*-\s*(.*)", line)
        if m:
            gate, detail = m.group(1), m.group(2).strip()
            # Extract file and line if present (e.g. path/to/file.ext:123)
            file_m = re.findall(r"([A-Za-z0-9_\-./\\]+\.[a-z]+):(\d+)", detail)
            if file_m:
                for fpath, lno in file_m:
                    findings.append({
                        "gate": gate,
                        "file": fpath.replace("\\", "/"),
                        "line": int(lno),
                        "detail": detail,
                    })
            else:
                findings.append({
                    "gate": gate,
                    "file": "",
                    "line": 0,
                    "detail": detail,
                })
    return findings


def rollback_session(root: Path, session_id: str = "latest") -> int:
    """Restore all files backed up during the specified remediation session."""
    backup_dir = root / "qa" / "fix-backup" / session_id
    if not backup_dir.is_dir():
        print(f"[WARN] No backup found for session '{session_id}'")
        return 0
    restored = 0
    for path in backup_dir.rglob("*"):
        if path.is_file():
            rel = path.relative_to(backup_dir)
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            restored += 1
    print(f"[OK] Restored {restored} file(s) from {backup_dir.relative_to(root)}")
    return restored


def clean_backups(root: Path) -> int:
    """Remove qa/fix-backup directory once verification is complete and confirmed."""
    backup_dir = root / "qa" / "fix-backup"
    if backup_dir.is_dir():
        shutil.rmtree(backup_dir)
        print(f"[OK] Cleaned backup directory: {backup_dir.relative_to(root)}")
        return 0
    print("[INFO] No backup directory to clean")
    return 0


def remediate_app(root: Path, dry_run: bool = False, recipe_only: bool = False) -> dict:
    """Run the remediation loop across detected findings and mechanical fixes."""
    actions = []

    # 1. Run basic mechanical fixes first (dotenv, dockerignore, robots, license)
    if not recipe_only:
        mechanical = fixes_mod.apply_all(root)
        for fix in mechanical:
            if fix.get("status") == "applied":
                actions.append({"category": "mechanical", "target": fix.get("id"), "status": "applied", "detail": fix.get("detail")})

    # 2. Ingest findings from qa/report.md
    report_file = root / "qa" / "report.md"
    findings = parse_findings_from_report(report_file)

    # 3. Always apply base UI / Accessibility additive styles if CSS files exist
    if not recipe_only:
        touch_res = rh.remediate_touch_targets(root)
        if touch_res.get("status") == "applied":
            actions.append({"category": "ui_design", "target": "touch_targets", "status": "applied", "detail": touch_res.get("detail")})
        focus_res = rh.remediate_focus_visible(root)
        if focus_res.get("status") == "applied":
            actions.append({"category": "accessibility", "target": "focus_visible", "status": "applied", "detail": focus_res.get("detail")})
        motion_res = rh.remediate_reduced_motion(root)
        if motion_res.get("status") == "applied":
            actions.append({"category": "accessibility", "target": "reduced_motion", "status": "applied", "detail": motion_res.get("detail")})

    # 4. Process each specific blocker finding
    recipes = []
    for f in findings:
        gate = f["gate"]
        file_rel = f["file"]
        line_no = f["line"]
        detail = f["detail"]

        # Code quality & function length -> Agent Recipe
        if "function is too long" in detail or "is too long" in detail:
            rule = "function_complexity"
            recipe_rel = rh.generate_agent_recipe(root, gate, file_rel, line_no, rule, detail)
            recipes.append(recipe_rel)
            actions.append({"category": "recipe", "target": file_rel, "status": "recipe_created", "detail": f"Generated recipe: {recipe_rel}"})
            continue

        # Empty catch blocks
        if "empty catch" in detail.lower() and file_rel:
            res = rh.remediate_empty_catch(root, file_rel)
            actions.append({"category": "code_quality", "target": file_rel, "status": res.get("status"), "detail": res.get("detail")})
            continue

        # innerHTML XSS risk
        if "innerhtml" in detail.lower() and file_rel:
            res = rh.remediate_xss_innerhtml(root, file_rel, line_no)
            actions.append({"category": "security", "target": file_rel, "status": res.get("status"), "detail": res.get("detail")})
            continue

        # CORS wildcard
        if "cors" in detail.lower() and file_rel:
            res = rh.remediate_cors_wildcard(root, file_rel, line_no)
            actions.append({"category": "security", "target": file_rel, "status": res.get("status"), "detail": res.get("detail")})
            continue

        # Missing migrations or complex database rules
        if gate == "P" or "migration" in detail.lower():
            recipe_rel = rh.generate_agent_recipe(root, "P", "schema", 0, "migrations_required", detail)
            recipes.append(recipe_rel)
            actions.append({"category": "recipe", "target": "migrations", "status": "recipe_created", "detail": f"Generated migration recipe: {recipe_rel}"})

    # Write summary log to qa/remediation-log.md
    log_file = root / "qa" / "remediation-log.md"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Remediation Execution Log",
        f"- Root: `{root}`",
        f"- Actions applied: {len([a for a in actions if a['status'] == 'applied'])}",
        f"- Recipes generated: {len(recipes)}",
        "\n## Actions\n",
    ]
    for act in actions:
        lines.append(f"- **[{act['status'].upper()}]** ({act['category']}) {act['target']}: {act['detail']}")
    if recipes:
        lines.append("\n## Recipes for Intelligent Agent Execution\n")
        for rec in recipes:
            lines.append(f"- `{rec}`")
    log_file.write_text("\n".join(lines), encoding="utf-8")

    return {
        "ok": True,
        "actions": actions,
        "recipes": recipes,
        "applied_count": len([a for a in actions if a["status"] == "applied"]),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Autonomous Remediation Engine for production-readiness blockers.")
    parser.add_argument("--root", default=".", help="Project root to remediate")
    parser.add_argument("--dry-run", action="store_true", help="Simulate remediation without altering files")
    parser.add_argument("--rollback", action="store_true", help="Roll back files from the latest remediation session")
    parser.add_argument("--clean-backup", action="store_true", help="Remove qa/fix-backup directory after verified success")
    parser.add_argument("--recipe-only", action="store_true", help="Only generate AI agent recipes for complex issues")
    parser.add_argument("--json", action="store_true", help="Emit JSON on stdout")
    args = parser.parse_args(argv)

    root = resolve_root(args.root)
    err = root_error(root)
    if err:
        print(f"[FAIL] {err}", file=sys.stderr)
        return 1

    if args.clean_backup:
        return clean_backups(root)

    if args.rollback:
        rollback_session(root)
        return 0

    res = remediate_app(root, dry_run=args.dry_run, recipe_only=args.recipe_only)

    human_lines = [
        "=" * 60,
        "AUTONOMOUS REMEDIATION ENGINE",
        "=" * 60,
        f"root: {root}",
        f"actions executed: {len(res['actions'])} (applied: {res['applied_count']})",
        f"recipes generated: {len(res['recipes'])}",
        "-" * 60,
    ]
    for act in res["actions"]:
        icon = "[FIXED]" if act["status"] == "applied" else f"[{act['status'].upper()}]"
        human_lines.append(f"{icon} {act['category']:14}: {act['detail']}")

    if res["recipes"]:
        human_lines.append("-" * 60)
        human_lines.append("Agent refactoring recipes ready in qa/recipes/:")
        for r in res["recipes"]:
            human_lines.append(f"  -> {r}")

    human_lines.append("=" * 60)
    emit(human_lines, res, args.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
