#!/usr/bin/env python3
"""Re-pin the absorbed manifest after an intentional change to a copy.

Editing an absorbed script without telling the manifest makes
``verify_manifest.py`` report drift, which in turn fails ``skill_check.py``
and the whole test suite.  This tool makes the intent explicit instead of
hand-editing JSON:

    python scripts/absorbed/refresh_manifest.py --file vulnerability_security_scan.py \\
        --reason "tightened GCP credential regex"

    python scripts/absorbed/refresh_manifest.py --all --reason "re-absorbed upstream"

Options
-------
--file NAME    Re-pin a single absorbed copy (repeatable).
--all          Re-pin every absorbed copy.
--reason TEXT  Why the copy changed.  Required: without a reason a forked
               copy is indistinguishable from an accidental edit.
--drop-patch   Mark the copy as identical to its upstream source again
               (use after copying the original file back verbatim).

The upstream base revision is preserved in ``upstream_sha256`` so the
verifier can still tell you when the sibling skill has moved on and the
patch needs to be rebased.

Exit 0 = manifest updated, 1 = bad arguments, 2 = manifest missing.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "MANIFEST.json"


def sha256(path: Path) -> str:
    import hashlib
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _original_path(entry: dict) -> Path | None:
    recorded = entry.get("source_path")
    return Path(recorded) if recorded else None


def refresh(names: list[str], reason: str, drop_patch: bool = False) -> int:
    if not MANIFEST.is_file():
        print(f"manifest missing: {MANIFEST}", file=sys.stderr)
        return 2
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    files = data.setdefault("files", {})
    unknown = [name for name in names if name not in files]
    if unknown:
        print(f"not in the manifest: {', '.join(unknown)}", file=sys.stderr)
        return 1

    changed = []
    for name in names:
        entry = files[name]
        local = HERE / name
        if not local.is_file():
            print(f"absorbed copy is missing: {local}", file=sys.stderr)
            return 1
        local_hash = sha256(local)
        previous = entry.get("sha256")
        upstream = entry.get("upstream_sha256")
        original = _original_path(entry)
        original_hash = sha256(original) if original and original.is_file() else None

        entry["sha256"] = local_hash
        entry["bytes"] = local.stat().st_size

        if drop_patch:
            entry["identical_to_source"] = True
            entry.pop("upstream_sha256", None)
            entry.pop("patch_reason", None)
        elif original_hash and original_hash == local_hash:
            # The copy is back in sync with its source.
            entry["identical_to_source"] = True
            entry.pop("upstream_sha256", None)
            entry.pop("patch_reason", None)
        else:
            entry["identical_to_source"] = False
            entry["upstream_sha256"] = upstream or original_hash or previous
            entry["patch_reason"] = reason

        changed.append((name, previous, local_hash))

    data["generated"] = date.today().isoformat()
    MANIFEST.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for name, previous, current in changed:
        state = "unchanged" if previous == current else "re-pinned"
        print(f"[{state}] {name}  {current}")
    print(f"manifest updated: {MANIFEST}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--file", action="append", default=[],
                        help="absorbed file to re-pin (repeatable)")
    parser.add_argument("--all", action="store_true",
                        help="re-pin every absorbed copy")
    parser.add_argument("--reason", default="",
                        help="why the copy changed (required for a fork)")
    parser.add_argument("--drop-patch", action="store_true",
                        help="mark the copy as identical to its source again")
    args = parser.parse_args(argv)

    names = list(args.file)
    if args.all:
        if names:
            print("--all and --file are mutually exclusive", file=sys.stderr)
            return 1
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        names = list(data.get("files", {}))
    if not names:
        parser.print_help()
        return 1
    if not args.reason and not args.drop_patch:
        print("--reason is required: a changed copy must record why it changed",
              file=sys.stderr)
        return 1
    return refresh(names, args.reason, args.drop_patch)


if __name__ == "__main__":
    raise SystemExit(main())
