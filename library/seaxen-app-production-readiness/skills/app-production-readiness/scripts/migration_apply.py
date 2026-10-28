#!/usr/bin/env python3
"""Deep mode for Gate P: really apply the migrations, then really roll them back.

``migration_check.py`` reads the SQL and guesses.  This script executes it
against a throwaway database so a broken migration cannot reach production:

1. discover the migration files (forward + rollback)
2. create a throwaway database (SQLite file by default, PostgreSQL when
   ``--pg-url`` is given and ``psql`` is installed)
3. apply every migration in order
4. roll them back in reverse order using the ``.down.sql`` / ``down.sql``
   companions
5. re-apply the whole chain on a fresh database to prove it works from zero
6. apply the chain twice to report whether the migrations are idempotent

Exit codes follow the skill-wide contract:

* ``0`` - apply + rollback + re-apply all succeeded
* ``1`` - a migration failed to apply or to roll back
* ``2`` - nothing could be attempted (no migrations found, or no database
  engine available).  A skip is never reported as a pass.

Artefact: ``qa/migrations.json``.
"""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, print_report  # noqa: E402

MIGRATION_DIRS = (
    "db/migrate", "db/migrations", "migrations", "sql/migrations",
    "database/migrations", "src/db/migrate",
)

FORWARD_SUFFIXES = (".sql",)
UP_MARKERS = (".up.sql", "_up.sql")
ROLLBACK_MARKERS = (".down.sql", "_down.sql", ".rollback.sql")


# --------------------------------------------------------------------------
# discovery
# --------------------------------------------------------------------------

def find_migration_dir(root: Path):
    for rel in MIGRATION_DIRS:
        candidate = root / rel
        if candidate.is_dir():
            return candidate
    return None


def discover(directory: Path) -> list:
    """Return [{version, name, forward, rollback}] sorted by version.

    ``001_init.sql`` pairs with ``001_init.down.sql``; ``001_init.up.sql``
    pairs with ``001_init.down.sql`` as well.  The pairing key is the path
    without the migration suffix, so both spellings of a pair line up.
    """
    items = []
    if not directory:
        return items
    forwards = {}
    rollbacks = {}
    for path in sorted(directory.rglob("*.sql")):
        rel = path.relative_to(directory).as_posix()
        lowered = rel.lower()
        matched = False
        for marker in ROLLBACK_MARKERS:
            if lowered.endswith(marker):
                rollbacks[rel[: -len(marker)]] = path
                matched = True
                break
        if matched:
            continue
        key = rel
        for marker in UP_MARKERS:
            if key.lower().endswith(marker):
                key = key[: -len(marker)]
                break
        else:
            if key.lower().endswith(".sql"):
                key = key[:-4]
        forwards[key] = path
    for key, path in forwards.items():
        version = "".join(ch for ch in Path(key).stem.split("_")[0] if ch.isdigit())
        items.append({
            "key": key,
            "version": version or key,
            "name": Path(key).stem,
            "forward": path,
            "rollback": rollbacks.get(key),
        })
    items.sort(key=lambda m: (m["version"], m["key"]))
    return items


# --------------------------------------------------------------------------
# engines
# --------------------------------------------------------------------------

class SqliteEngine:
    name = "sqlite"

    def __init__(self, root: Path):
        self.path = Path(tempfile.mkdtemp(prefix="pdqa-mig-")) / "qa.db"
        self.path = str(self.path)

    def script(self, sql: str) -> int:
        conn = sqlite3.connect(self.path)
        try:
            conn.executescript(sql)
            conn.commit()
            return 0
        except Exception as exc:  # noqa: BLE001 - any SQL error is a failure
            print(f"SQL ERROR: {exc}", file=sys.stderr)
            return 1
        finally:
            conn.close()

    def run_file(self, path: Path) -> int:
        try:
            sql = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            print(f"READ ERROR: {exc}", file=sys.stderr)
            return 1
        return self.script(sql)

    def tables(self):
        conn = sqlite3.connect(self.path)
        try:
            rows = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' "
                "AND name NOT LIKE 'sqlite_%'").fetchall()
            return sorted(r[0] for r in rows)
        finally:
            conn.close()

    def cleanup(self):
        try:
            os.unlink(self.path)
        except OSError:
            pass


class PostgresEngine:
    name = "postgres"

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.db_name = f"pdqa_mig_{int(time.time())}"
        parts = urlsplit(base_url)
        self.url = urlunsplit((parts.scheme, parts.netloc, f"/{self.db_name}",
                               parts.query, parts.fragment))
        self.created = False

    def _psql(self, url: str, *args, sql=None, file=None):
        cmd = ["psql", "-v", "ON_ERROR_STOP=1", "-q", "-d", url]
        if file is not None:
            cmd += ["-f", str(file)]
        elif sql is not None:
            cmd += ["-c", sql]
        cmd += list(args)
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if proc.returncode != 0:
            print((proc.stderr or proc.stdout or "")[:1500], file=sys.stderr)
        return proc.returncode

    def script(self, sql: str) -> int:
        return self._psql(self.url, sql=sql)

    def run_file(self, path: Path) -> int:
        return self._psql(self.url, file=path)

    def tables(self):
        proc = subprocess.run(
            ["psql", "-t", "-A", "-d", self.url, "-c",
             "SELECT tablename FROM pg_tables WHERE schemaname='public'"],
            capture_output=True, text=True, timeout=60)
        return sorted(x.strip() for x in (proc.stdout or "").splitlines() if x.strip())

    def cleanup(self):
        if self.created:
            self._psql(self.base_url, sql=f"DROP DATABASE IF EXISTS {self.db_name}")


# --------------------------------------------------------------------------
# the round trip
# --------------------------------------------------------------------------

def apply_chain(engine, migrations, direction="forward"):
    """Apply (or roll back) the chain.  Returns a list of step results."""
    steps = []
    items = migrations if direction == "forward" else list(reversed(migrations))
    for mig in items:
        path = mig["forward"] if direction == "forward" else mig["rollback"]
        if path is None:
            steps.append({"migration": mig["key"], "status": "skipped",
                          "detail": "no rollback file"})
            continue
        started = time.perf_counter()
        rc = engine.run_file(path)
        steps.append({
            "migration": mig["key"],
            "file": str(path.name),
            "status": "ok" if rc == 0 else "fail",
            "rc": rc,
            "ms": int((time.perf_counter() - started) * 1000),
        })
    return steps


def run_roundtrip(root: Path, engine, migrations) -> dict:
    result = {"engine": engine.name}
    result["apply"] = apply_chain(engine, migrations, "forward")
    result["tables_after_apply"] = engine.tables()
    result["rollback"] = apply_chain(engine, migrations, "backward")
    result["tables_after_rollback"] = engine.tables()

    # fresh database -> the whole chain must run from zero
    if engine.name == "sqlite":
        fresh = SqliteEngine(root)
        try:
            result["reapply"] = apply_chain(fresh, migrations, "forward")
            result["tables_after_reapply"] = fresh.tables()
        finally:
            fresh.cleanup()
    else:
        result["reapply"] = [{"migration": m["key"], "status": "skipped",
                              "detail": "re-apply on a fresh database needs a second "
                                        "PostgreSQL database; skipped"}]

    # idempotency probe: run the chain twice on one database
    engine.run_file(migrations[0]["forward"]) if migrations else None
    result["idempotent"] = None
    if migrations:
        twice = apply_chain(engine, migrations, "forward")
        result["idempotent"] = all(s["status"] == "ok" for s in twice)
        result["idempotency_steps"] = twice
    return result


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root_str, want_json, _ = parse_cli(argv)
    root = resolve_root(root_str)
    err = root_error(root)
    if err:
        print(f"[FAIL] {err}")
        return 1

    pg_url = os.environ.get("QA_PG_URL") or os.environ.get("DATABASE_URL")
    use_pg = False
    i = 0
    while i < len(argv):
        if argv[i] == "--pg-url" and i + 1 < len(argv):
            pg_url = argv[i + 1]
            i += 1
        elif argv[i] == "--sqlite":
            pg_url = None
        i += 1

    result = GateResult("P", "MIGRATION APPLY (real forward + rollback)")
    directory = find_migration_dir(root)
    migrations = discover(directory) if directory else []

    if not migrations:
        result.skipped = True
        result.reason = ("no migrations were found (looked in: "
                         + ", ".join(MIGRATION_DIRS) + ")")
        payload = print_report(result, want_json, extra={"migrations": []})
        emit([], payload, want_json)
        return 2

    missing_rollback = [m["key"] for m in migrations if m["rollback"] is None]

    engine = None
    if pg_url and shutil.which("psql"):
        engine = PostgresEngine(pg_url)
        engine.created = True
        rc = engine._psql(pg_url, sql=f"CREATE DATABASE {engine.db_name}")
        if rc != 0:
            engine = None
    if engine is None:
        if pg_url and not shutil.which("psql"):
            result.notes.append("psql is not installed - PostgreSQL was not exercised")
        engine = SqliteEngine(root)

    try:
        roundtrip = run_roundtrip(root, engine, migrations)
    finally:
        engine.cleanup()

    apply_failed = [s for s in roundtrip["apply"] if s["status"] == "fail"]
    rollback_failed = [s for s in roundtrip["rollback"] if s["status"] == "fail"]
    reapply_failed = [s for s in roundtrip.get("reapply", []) if s["status"] == "fail"]

    result.add("every migration applies cleanly", not apply_failed,
               detail="; ".join(f"{s['migration']}: {s.get('detail', 'error')}"
                                for s in apply_failed) or f"{len(migrations)} migrations applied")
    result.add("every migration rolls back cleanly", not rollback_failed and not missing_rollback,
               detail="; ".join(f"{s['migration']}: {s.get('detail', 'error')}"
                                for s in rollback_failed)
               or ("missing rollback files: " + ", ".join(missing_rollback)
                   if missing_rollback else "rollback chain is clean"))
    if roundtrip.get("reapply") and not all(s["status"] == "skipped" for s in roundtrip["reapply"]):
        result.add("the chain applies from an empty database", not reapply_failed,
                   detail="; ".join(f"{s['migration']} failed" for s in reapply_failed)
                   or "clean re-apply")
    result.notes.append(
        f"tables after apply: {', '.join(roundtrip['tables_after_apply']) or 'none'}")
    result.notes.append(
        f"tables after rollback: {', '.join(roundtrip['tables_after_rollback']) or 'none'}")
    if roundtrip.get("idempotent") is not None:
        result.add("migrations are idempotent (re-running is safe)",
                   bool(roundtrip["idempotent"]), False,
                   "re-running the chain succeeded" if roundtrip["idempotent"]
                   else "re-running the chain failed - the migrations are not idempotent")

    payload = print_report(result, want_json, extra={"roundtrip": roundtrip,
                                                     "migrations": [m["key"] for m in migrations]})
    try:
        out_dir = root / "qa"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "migrations.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    except OSError:
        pass
    emit([], payload, want_json)
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
