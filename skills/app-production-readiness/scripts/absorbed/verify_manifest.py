#!/usr/bin/env python3
"""Verify that the absorbed scripts are byte-identical to their sources.

``scripts/absorbed/MANIFEST.json`` records, for every absorbed script, the
skill it came from, its original path and its sha256.  This checker recomputes
the hashes so a drift (or an accidental edit) is caught instead of silently
changing what the skill runs.

Usage:
  python scripts/absorbed/verify_manifest.py [--source-root D:/Repo/.agents/skills]
  python scripts/absorbed/verify_manifest.py --json

Exit 0 = every file matches, 1 = mismatch/missing, 2 = manifest missing.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "MANIFEST.json"
DEFAULT_SOURCE_ROOT = Path(r"D:\Repo\.agents\skills")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _original_candidates(entry, source_root):
    """Return the possible locations of the original script.

    The recorded absolute ``source_path`` is used first.  When an explicit
    ``source_root`` is given the path is rebuilt relative to that root, so the
    check still works when the sibling skills live somewhere else (or when the
    absorbed copy was renamed).
    """
    candidates = []
    recorded = entry.get("source_path")
    if recorded:
        candidates.append(Path(recorded))
    skill = entry.get("source_skill")
    if source_root and skill and recorded:
        parts = Path(recorded).parts
        if skill in parts:
            tail = parts[parts.index(skill) + 1:]
            candidates.append(Path(source_root) / skill / Path(*tail))
    seen, unique = set(), []
    for path in candidates:
        key = str(path).lower()
        if key not in seen:
            seen.add(key)
            unique.append(path)
    return unique


def verify(source_root: Path = DEFAULT_SOURCE_ROOT):
    if not MANIFEST.is_file():
        return {"status": "error", "reason": f"manifest missing: {MANIFEST}",
                "files": []}
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    results = []
    mismatches = 0
    warnings = 0
    files = data.get("files") or {}
    entries = files.items() if isinstance(files, dict) else (
        (entry.get("file"), entry) for entry in files)
    for name, entry in entries:
        local = HERE / name
        patched = not entry.get("identical_to_source", True)
        row = {"file": name, "source_skill": entry.get("source_skill"),
               "ok": True, "detail": "", "patched": patched}
        if not local.is_file():
            row["ok"] = False
            row["detail"] = "absorbed copy is missing"
        else:
            local_hash = sha256(local)
            row["local_sha256"] = local_hash
            if local_hash != entry["sha256"]:
                row["ok"] = False
                row["detail"] = "absorbed copy was modified"
            else:
                original = None
                for candidate in _original_candidates(entry, source_root):
                    if candidate.is_file():
                        original = candidate
                        break
                if original is not None:
                    original_hash = sha256(original)
                    if patched:
                        # The copy is intentionally forked: the pinned base
                        # revision must still match, otherwise the patch has to
                        # be rebased. This is a warning, not drift.
                        pinned = entry.get("upstream_sha256")
                        if pinned and original_hash != pinned:
                            row["detail"] = ("upstream changed since the patch was "
                                             "applied (rebase the patch)")
                            row["warning"] = True
                    elif original_hash != entry["sha256"]:
                        row["ok"] = False
                        row["detail"] = f"the original {original} changed on disk"
                else:
                    row["detail"] = "original not found (kept the absorbed copy)"
        if not row["ok"]:
            mismatches += 1
        elif row.get("warning"):
            warnings += 1
        results.append(row)
    return {
        "status": "ok" if mismatches == 0 else "drift",
        "files": results,
        "checked": len(results),
        "mismatches": mismatches,
        "warnings": warnings,
    }


def main() -> int:
    args = sys.argv[1:]
    json_mode = "--json" in args
    source_root = DEFAULT_SOURCE_ROOT
    if "--source-root" in args:
        idx = args.index("--source-root")
        if idx + 1 < len(args):
            source_root = Path(args[idx + 1])
    report = verify(source_root)
    if json_mode:
        print(json.dumps(report, indent=2))
    else:
        print("=" * 62)
        print("ABSORBED SCRIPTS - INTEGRITY CHECK")
        print("=" * 62)
        for row in report["files"]:
            icon = "OK  " if row["ok"] else "DRIFT"
            if row["ok"] and row.get("warning"):
                icon = "WARN "
            label = row["file"] + ("  (patched)" if row.get("patched") else "")
            print(f"[{icon}] {label}  <- {row['source_skill']}"
                  + (f"  ({row['detail']})" if row["detail"] else ""))
        print("-" * 62)
        print(f"checked {report.get('checked', 0)} file(s), "
              f"{report.get('mismatches', 0)} mismatch(es), "
              f"{report.get('warnings', 0)} warning(s)")
        print("=" * 62)
    if report["status"] == "error":
        return 2
    return 1 if report["status"] == "drift" else 0


if __name__ == "__main__":
    raise SystemExit(main())
