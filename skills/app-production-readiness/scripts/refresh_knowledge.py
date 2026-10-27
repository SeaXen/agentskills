#!/usr/bin/env python3
"""Integrity tooling for the absorbed knowledge pack in ``references/knowledge``.

The pack holds verbatim copies of the documentation of sibling skills
(``api-contract-testing``, ``security-hardened-api``, ``observability-and-instrumentation``,
...) so that this review skill stays self-contained.  Every copy carries a short
header and is recorded in ``references/knowledge/MANIFEST.json`` with the sha256
of the copy and of the original it came from.

Two operations:

``--check``   verify every copy against the manifest (default).
``--rebuild`` re-copy the originals from the sibling skills and rewrite the
              manifest.  A sibling that is missing is reported, never fatal:
              the local copy stays authoritative.

The sibling skills live next to this skill, in the parent directory of the
skill root.  Their paths are recorded **relative to that directory** so the
manifest survives being moved to another machine.

Exit codes:
    0 - every copy matches the manifest (or was rebuilt successfully).
    1 - drift was found (or a rebuild failed).
    2 - the knowledge pack or its manifest is missing.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

HEADER = ("<!-- Absorbed from the sibling skill '{skill}' (source: {source}).\n"
          "     Kept verbatim so this review skill stays self-contained.\n"
          "     The sibling skill itself was NOT deleted. -->\n")

EXCLUDED_NAMES = ("README.md", "MANIFEST.json")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def knowledge_dir(root: Path) -> Path:
    return root / "references" / "knowledge"


def manifest_path(root: Path) -> Path:
    return knowledge_dir(root) / "MANIFEST.json"


def load_manifest(root: Path) -> list[dict]:
    """Read the manifest, tolerating a byte-order mark."""
    raw = manifest_path(root).read_bytes()
    data = json.loads(raw.decode("utf-8-sig"))
    if not isinstance(data, list):
        raise ValueError("the knowledge manifest must be a list of entries")
    return data


def dump_manifest(root: Path, entries: list[dict]) -> None:
    """Write the manifest as UTF-8 without a BOM, with POSIX separators."""
    text = json.dumps(entries, indent=2, ensure_ascii=False) + "\n"
    manifest_path(root).write_text(text, encoding="utf-8")


def entry_path(root: Path, entry: dict) -> Path:
    """Absolute path of a knowledge copy described by a manifest entry."""
    rel = entry.get("path") or f"{entry['skill']}/{entry['file']}"
    return knowledge_dir(root) / Path(rel.replace("\\", "/"))


def source_path(root: Path, entry: dict) -> Path:
    """Absolute path of the original the copy came from."""
    source = entry.get("source") or f"{entry['skill']}/{entry['file']}"
    if Path(source).is_absolute():
        return Path(source)
    return root.parent / Path(source.replace("\\", "/"))


def iter_copies(root: Path):
    """Every file of the knowledge pack except the index and the manifest."""
    kdir = knowledge_dir(root)
    if not kdir.is_dir():
        return
    for path in sorted(kdir.rglob("*")):
        if not path.is_file():
            continue
        if path.name in EXCLUDED_NAMES:
            continue
        yield path


def check(root: Path) -> tuple[list[str], int]:
    """Return (problems, checked)."""
    problems: list[str] = []
    try:
        entries = load_manifest(root)
    except FileNotFoundError:
        return ["the knowledge manifest is missing"], 0
    except (ValueError, json.JSONDecodeError) as exc:
        return [f"the knowledge manifest is not readable JSON: {exc}"], 0

    checked = 0
    listed: set[str] = set()
    for entry in entries:
        rel = (entry.get("path") or f"{entry['skill']}/{entry['file']}").replace("\\", "/")
        listed.add(rel)
        target = knowledge_dir(root) / Path(rel)
        if not target.is_file():
            problems.append(f"{rel}: listed in the manifest but missing on disk")
            continue
        data = target.read_bytes()
        checked += 1
        expected = entry.get("sha256")
        if expected:
            actual = sha256_bytes(data)
            if actual != expected:
                problems.append(f"{rel}: sha256 drift (manifest {expected[:12]}…, file {actual[:12]}…)")
        if entry.get("bytes") is not None and int(entry["bytes"]) != len(data):
            problems.append(f"{rel}: size {len(data)} does not match the manifest ({entry['bytes']})")

    for path in iter_copies(root):
        rel = path.relative_to(knowledge_dir(root)).as_posix()
        if rel not in listed:
            problems.append(f"{rel}: present in the pack but missing from the manifest")
    return problems, checked


def rebuild(root: Path) -> tuple[list[str], int]:
    """Re-copy the originals and rewrite the manifest."""
    problems: list[str] = []
    try:
        entries = load_manifest(root)
    except FileNotFoundError:
        return ["the knowledge manifest is missing"], 0
    except (ValueError, json.JSONDecodeError) as exc:
        return [f"the knowledge manifest is not readable JSON: {exc}"], 0

    new_entries: list[dict] = []
    rebuilt = 0
    for entry in entries:
        skill = entry["skill"]
        file = entry["file"].replace("\\", "/")
        rel = f"{skill}/{file}"
        target = knowledge_dir(root) / Path(rel)
        src = source_path(root, entry)
        source_rel = entry.get("source") or rel
        if src.is_absolute():
            try:
                source_rel = src.relative_to(root.parent).as_posix()
            except ValueError:
                source_rel = src.as_posix()
        source_hash = None
        if src.is_file():
            data = src.read_bytes()
            header = HEADER.format(skill=skill, source=source_rel).encode("utf-8")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(header + data)
            source_hash = sha256_bytes(data)
            rebuilt += 1
        else:
            problems.append(f"{rel}: the original {src} is missing - the local copy was kept as is")
            data = target.read_bytes() if target.is_file() else b""
            if not data:
                problems.append(f"{rel}: neither the original nor a local copy exists")
        new_entries.append({
            "skill": skill,
            "file": file,
            "path": rel,
            "source": source_rel.replace("\\", "/"),
            "bytes": len(target.read_bytes()) if target.is_file() else 0,
            "sha256": sha256_bytes(target.read_bytes()) if target.is_file() else "",
            "source_bytes": entry.get("source_bytes", len(data)),
            "source_sha256": source_hash or entry.get("source_sha256", ""),
        })
    dump_manifest(root, new_entries)
    return problems, rebuilt


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--root", default=".", help="Skill root (the directory holding references/)")
    parser.add_argument("--check", action="store_true", help="Verify the pack against the manifest (default)")
    parser.add_argument("--rebuild", action="store_true", help="Re-copy the originals and rewrite the manifest")
    parser.add_argument("--json", action="store_true", help="Emit JSON on stdout")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not (root / "references" / "knowledge").is_dir():
        print(f"[FAIL] no knowledge pack under {root}", file=sys.stderr)
        return 2

    if args.rebuild:
        problems, count = rebuild(root)
        action = "rebuilt"
    else:
        problems, count = check(root)
        action = "checked"

    payload = {
        "root": str(root),
        "action": action,
        "files": count,
        "problems": problems,
        "ok": not problems,
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"knowledge pack {action}: {count} file(s)")
        for problem in problems:
            print(f"[FAIL] {problem}")
        print("[OK] the knowledge pack is intact" if not problems else f"[FAIL] {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
