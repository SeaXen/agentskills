#!/usr/bin/env python3
"""Autonomous Remediation Engine for app-production-readiness.

Parses audit findings (from `qa/report.md` or live gate runs), applies safe deterministic
codemods with atomic rollback safeguards, and emits structured recipes for complex refactorings.

Usage:
    python scripts/remediate.py --root <app_root> [--dry-run] [--rollback] [--recipe-only] [--json]

Exit codes:
    0 - All detected remediations succeeded (or nothing to do)
    1 - At least one remediation failed, or a requested rollback restored nothing
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, resolve_root, root_error
import fixes as fixes_mod
import remediation_handlers as rh

BACKUP_DIR = Path("qa") / "fix-backup"


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
    backup_dir = Path(root) / BACKUP_DIR / session_id
    if not backup_dir.is_dir():
        print(f"[WARN] No backup found for session '{session_id}'")
        return 0
    restored = 0
    for path in sorted(backup_dir.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(backup_dir)
        target = Path(root) / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        restored += 1
    print(f"[OK] Restored {restored} file(s) from {backup_dir.relative_to(Path(root))}")
    return restored


def clean_backups(root: Path) -> int:
    """Remove qa/fix-backup directory once verification is complete and confirmed."""
    backup_dir = Path(root) / BACKUP_DIR
    if backup_dir.is_dir():
        shutil.rmtree(backup_dir)
        print(f"[OK] Cleaned backup directory: {backup_dir.relative_to(Path(root))}")
        return 0
    print("[INFO] No backup directory to clean")
    return 0


def _record(actions: list[dict], category: str, target: str, status: str, detail: str,
            **extra) -> None:
    entry = {"category": category, "target": target, "status": status, "detail": detail}
    entry.update(extra)
    actions.append(entry)


def remediate_app(root: Path, dry_run: bool = False, recipe_only: bool = False) -> dict:
    """Run the remediation loop across detected findings and mechanical fixes."""
    root = Path(root)
    actions: list[dict] = []
    recipes: list[str] = []
    failures: list[str] = []

    recipe_status = "recipe_planned" if dry_run else "recipe_created"

    def _record_recipe(target: str, recipe_rel: str, label: str) -> None:
        recipes.append(recipe_rel)
        verb = "Would generate" if dry_run else "Generated"
        _record(actions, "recipe", target, recipe_status, f"{verb} {label}: {recipe_rel}")

    def _track(res: dict, category: str, target: str) -> None:
        status = res.get("status", "skipped")
        detail = res.get("detail", "")
        _record(actions, category, target, status, detail)
        if status == "failed":
            failures.append(f"{category}/{target}: {detail}")
        recipe = res.get("recipe")
        if recipe:
            _record_recipe(target, recipe, "recipe")

    # 1. Run basic mechanical fixes first (dotenv, dockerignore, robots, license)
    if not recipe_only:
        mechanical = fixes_mod.apply_all(root, dry_run=dry_run)
        for fix in mechanical:
            status = fix.get("status")
            if status in ("applied", "planned"):
                _record(actions, "mechanical", fix.get("id"), status, fix.get("detail", ""))
            elif status == "failed":
                failures.append(f"mechanical/{fix.get('id')}: {fix.get('detail', '')}")
                _record(actions, "mechanical", fix.get("id"), "failed", fix.get("detail", ""))

    # 2. Ingest findings from qa/report.md
    report_file = root / "qa" / "report.md"
    findings = parse_findings_from_report(report_file)

    # 3. Always apply base UI / Accessibility additive styles if CSS files exist
    if not recipe_only:
        _track(rh.remediate_touch_targets(root, dry_run=dry_run), "ui_design", "touch_targets")
        _track(rh.remediate_focus_visible(root, dry_run=dry_run), "accessibility", "focus_visible")
        _track(rh.remediate_reduced_motion(root, dry_run=dry_run), "accessibility", "reduced_motion")

    # 4. Process each specific blocker finding
    for f in findings:
        gate = f["gate"]
        file_rel = f["file"]
        line_no = f["line"]
        detail = f["detail"]

        # Code quality & function length -> Agent Recipe
        if "function is too long" in detail or "is too long" in detail:
            recipe_rel = rh.generate_agent_recipe(root, gate, file_rel, line_no, rule="function_complexity",
                                                  detail=detail, dry_run=dry_run)
            _record_recipe(file_rel, recipe_rel, "recipe")
            continue

        # Empty catch blocks
        if "empty catch" in detail.lower() and file_rel:
            _track(rh.remediate_empty_catch(root, file_rel, dry_run=dry_run), "code_quality", file_rel)
            continue

        # innerHTML XSS risk
        if "innerhtml" in detail.lower() and file_rel:
            _track(rh.remediate_xss_innerhtml(root, file_rel, line_no, dry_run=dry_run), "security", file_rel)
            continue

        # CORS wildcard
        if "cors" in detail.lower() and file_rel:
            _track(rh.remediate_cors_wildcard(root, file_rel, line_no, dry_run=dry_run), "security", file_rel)
            continue

        # Missing accessible names
        if ("aria-label" in detail.lower() or "accessible name" in detail.lower()) and file_rel:
            _track(rh.remediate_aria_label(root, file_rel, dry_run=dry_run), "accessibility", file_rel)
            continue

        # Missing SEO metadata
        seo_words = ("meta description", "open graph", "og:", "twitter card", "canonical")
        if any(word in detail.lower() for word in seo_words) and file_rel:
            _track(rh.remediate_seo_meta_tags(root, file_rel, dry_run=dry_run), "seo", file_rel)
            continue

        # Missing migrations or complex database rules
        if gate == "P" or "migration" in detail.lower():
            recipe_rel = rh.generate_agent_recipe(root, "P", "schema", 0, "migrations_required",
                                                  detail, dry_run=dry_run)
            _record_recipe("migrations", recipe_rel, "migration recipe")

    # Write summary log to qa/remediation-log.md (never during a dry run)
    log_file = root / "qa" / "remediation-log.md"
    lines = [
        "# Remediation Execution Log",
        f"- Root: `{root}`",
        f"- Dry run: {'yes' if dry_run else 'no'}",
        f"- Actions applied: {len([a for a in actions if a['status'] == 'applied'])}",
        f"- Actions planned: {len([a for a in actions if a['status'] == 'planned'])}",
        f"- Actions failed: {len(failures)}",
        f"- Recipes generated: {len(recipes)}",
        "\n## Actions\n",
    ]
    for act in actions:
        lines.append(f"- **[{act['status'].upper()}]** ({act['category']}) {act['target']}: {act['detail']}")
    if recipes:
        lines.append("\n## Recipes for Intelligent Agent Execution\n")
        for rec in recipes:
            lines.append(f"- `{rec}`")
    if failures:
        lines.append("\n## Failures\n")
        for failure in failures:
            lines.append(f"- {failure}")
    if not dry_run:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        log_file.write_text("\n".join(lines), encoding="utf-8")

    return {
        "ok": not failures,
        "dry_run": dry_run,
        "actions": actions,
        "recipes": recipes,
        "failures": failures,
        "applied_count": len([a for a in actions if a["status"] == "applied"]),
        "planned_count": len([a for a in actions if a["status"] == "planned"]),
        "failed_count": len(failures),
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
        restored = rollback_session(root)
        return 0 if restored else 1

    res = remediate_app(root, dry_run=args.dry_run, recipe_only=args.recipe_only)

    human_lines = [
        "=" * 60,
        "AUTONOMOUS REMEDIATION ENGINE",
        "=" * 60,
        f"root: {root}",
    ]
    if res["dry_run"]:
        human_lines.append("DRY RUN - no file was modified")
    human_lines += [
        f"actions executed: {len(res['actions'])} (applied: {res['applied_count']}, "
        f"planned: {res['planned_count']}, failed: {res['failed_count']})",
        ("recipes planned: " if res["dry_run"] else "recipes generated: ") + str(len(res["recipes"])),
        "-" * 60,
    ]
    for act in res["actions"]:
        icon = {"applied": "[FIXED]", "planned": "[PLAN]", "failed": "[FAIL]"}.get(act["status"], f"[{act['status'].upper()}]")
        human_lines.append(f"{icon} {act['category']:14}: {act['detail']}")

    if res["recipes"]:
        human_lines.append("-" * 60)
        if res["dry_run"]:
            human_lines.append("Agent refactoring recipes that WOULD be written to qa/recipes/:")
        else:
            human_lines.append("Agent refactoring recipes ready in qa/recipes/:")
        for r in res["recipes"]:
            human_lines.append(f"  -> {r}")

    if res["failures"]:
        human_lines.append("-" * 60)
        human_lines.append(f"{len(res['failures'])} remediation(s) failed - see qa/remediation-log.md")

    human_lines.append("=" * 60)
    emit(human_lines, res, args.json)
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
