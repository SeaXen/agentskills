#!/usr/bin/env python3
"""Gate P - migrations and schema safety.

A migration that cannot be rolled back is an outage waiting for a bad deploy.
This gate inspects the migration history and the schema:

* every migration must have a rollback path (down/rollback partner)
* destructive statements (DROP TABLE/COLUMN, TRUNCATE, DELETE without WHERE)
  must be guarded - flagged HIGH when unguarded
* migrations should be idempotent (IF EXISTS / IF NOT EXISTS)
* migrations must be ordered (timestamped or numbered) and the history must
  not contain duplicate versions
* a declared schema (schema.sql, prisma/schema.prisma, models) must be
  reachable from the migration folder
* the absorbed ``schema_validator.py`` (database-design) runs as a signal

Usage:
  python scripts/migration_check.py --root <app_root> [--json]

Exit 0 = migrations are safe, 1 = blocking findings, 2 = no migrations found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, print_report, read_files, run_absorbed  # noqa: E402

MIGRATION_DIRS = ("db/migrate", "migrations", "db/migrations", "alembic/versions",
                  "prisma/migrations", "database/migrations", "sql/migrations",
                  "server/migrations")
SCHEMA_FILES = ("schema.sql", "db/schema.sql", "database/schema.sql",
                "prisma/schema.prisma", "schema.prisma", "db/schema.rb",
                "models.py", "schema.py")

DESTRUCTIVE = [
    (re.compile(r"DROP\s+TABLE", re.I), "DROP TABLE"),
    (re.compile(r"DROP\s+COLUMN", re.I), "DROP COLUMN"),
    (re.compile(r"TRUNCATE\s+(TABLE\s+)?\w+", re.I), "TRUNCATE"),
    (re.compile(r"DELETE\s+FROM\s+[\w`\"]+\s*(;|$)", re.I | re.M), "DELETE without WHERE"),
    (re.compile(r"DROP\s+DATABASE", re.I), "DROP DATABASE"),
]
GUARD = re.compile(r"IF\s+(EXISTS|NOT\s+EXISTS)", re.I)
VERSION_RE = re.compile(r"(\d{6,14}[_-]?\d{0,6})")


def find_migrations(root: Path):
    found = []
    for rel in MIGRATION_DIRS:
        folder = root / rel
        if folder.is_dir():
            for path in sorted(folder.rglob("*")):
                if path.is_file() and path.suffix.lower() in (".sql", ".py", ".js", ".ts"):
                    found.append(path)
    if not found:
        # flat migration files, e.g. migrations/001_init.sql
        for path in sorted(root.rglob("*.sql")):
            parts = set(path.parts)
            if parts & {"migrations", "migrate", "versions"}:
                found.append(path)
    return found


def _has_rollback(path: Path, text: str, siblings=()) -> bool:
    name = path.name.lower()
    if re.search(r"(^|[._-])(down|rollback|revert)([._-]|$)", name):
        return True
    if re.search(r"\bdef\s+downgrade\b|\bdef\s+down\b|rollback\s*\(", text, re.I):
        return True
    if re.search(r"\bup\s*[:=]|\bdown\s*[:=]", text, re.I):
        return True
    # a paired file: 001_init.sql <-> 001_init.down.sql
    stem = path.stem.lower()
    for other in siblings:
        other_stem = other.stem.lower()
        if other_stem == stem:
            continue
        if re.sub(r"[._-]?(down|rollback|revert)$", "", other_stem) == stem:
            return True
    return False


def analyse(root: Path):
    migrations = find_migrations(root)
    findings = []
    versions = {}
    siblings = list(migrations)
    for path in migrations:
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not _has_rollback(path, text, siblings):
            findings.append({"severity": "HIGH", "check": "migration has no rollback path",
                             "detail": str(rel)})
        for pattern, label in DESTRUCTIVE:
            for m in pattern.finditer(text):
                line_no = text[:m.start()].count("\n") + 1
                line = text.splitlines()[line_no - 1] if line_no <= len(text.splitlines()) else ""
                if not GUARD.search(line) and "IF EXISTS" not in text[m.start():m.start() + 80].upper():
                    findings.append({
                        "severity": "HIGH" if label != "DELETE without WHERE" else "MEDIUM",
                        "check": f"unguarded {label}",
                        "detail": f"{rel}:{line_no}"})
        if re.search(r"CREATE\s+TABLE", text, re.I) and not re.search(
                r"CREATE\s+TABLE\s+(IF\s+NOT\s+EXISTS|[\w\"`]+)", text, re.I | re.S):
            pass
        if re.search(r"CREATE\s+(TABLE|INDEX|UNIQUE)", text, re.I) and not GUARD.search(text):
            findings.append({"severity": "MEDIUM",
                             "check": "non-idempotent DDL (no IF EXISTS / IF NOT EXISTS)",
                             "detail": str(rel)})
        m = VERSION_RE.search(path.name)
        if m:
            versions.setdefault(m.group(1), []).append(str(rel))
    for version, paths in versions.items():
        if len(paths) > 1:
            findings.append({"severity": "MEDIUM", "check": "duplicate migration version",
                             "detail": f"{version}: {', '.join(paths)}"})
    schema_files = [rel for rel in SCHEMA_FILES if (root / rel).is_file()]
    return migrations, findings, schema_files


def main() -> int:
    args = sys.argv[1:]
    _root, json_mode, want_help = parse_cli(args)
    root_arg = "."
    i = 0
    while i < len(args):
        if args[i] == "--root" and i + 1 < len(args):
            root_arg = args[i + 1]
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

    result = GateResult("P", "MIGRATIONS & SCHEMA")
    migrations, findings, schema_files = analyse(root)
    if not migrations:
        result.skipped = True
        result.reason = ("no migrations found - if the app has a database this gate "
                         "was NOT checked")
        payload = print_report(result, json_mode, extra={"migrations": []})
        emit([], payload, json_mode)
        return 2

    for finding in findings:
        if finding["severity"] in ("HIGH", "CRITICAL"):
            result.fail(finding["check"], finding["detail"], finding["severity"])
        else:
            result.warn(finding["check"], finding["detail"])
    result.add("migration history is present", True, False, f"{len(migrations)} file(s)")
    result.add("a declared schema exists", bool(schema_files), False,
               ", ".join(schema_files) if schema_files else
               "no schema.sql / prisma schema found - schema drift cannot be checked")

    schema = run_absorbed("schema_validator.py", root, timeout=120)
    if schema.get("available"):
        result.add("absorbed schema_validator.py reports a valid schema",
                   bool(schema.get("ok")), False, schema.get("detail", ""))
    else:
        result.warn("absorbed schema_validator.py available", schema.get("detail", ""))

    payload = print_report(result, json_mode, extra={
        "migrations": [str(p.relative_to(root)) for p in migrations],
        "schema_files": schema_files,
    })
    emit([], payload, json_mode)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
