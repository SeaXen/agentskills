#!/usr/bin/env python3
"""Health check for this skill package (and any other skill folder).

A skill that reviews apps is worthless if its own packaging is broken: a
missing frontmatter key, a script that does not compile, a reference file that
is linked but absent, or an absorbed script that drifted from its source.

Usage:
    python scripts/skill_check.py [--root .] [--json] [--package OUT_DIR]

Checks
  1. SKILL.md exists, has YAML frontmatter with name + description
  2. no unexpected frontmatter keys (name/description/license/allowed-tools/
     metadata/compatibility)
  3. the declared name matches the folder name
  4. every python script under scripts/ compiles
  5. every reference/script file mentioned in SKILL.md exists
  6. every file under references/ is linked from SKILL.md
  7. the absorbed scripts match their manifest (scripts/absorbed/verify_manifest.py)

Exit 0: everything passes | Exit 1: at least one problem | Exit 2: cannot run
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import emit  # noqa: E402

ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata",
                "compatibility"}
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SKIP_DIRS = {"__pycache__", ".git", ".pytest_cache", "qa", "node_modules"}


# ---------------------------------------------------------------------------
# frontmatter
# ---------------------------------------------------------------------------
def parse_frontmatter(text: str):
    """Return (frontmatter_dict, error_string)."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, "SKILL.md has no YAML frontmatter block"
    raw = match.group(1)
    try:
        import yaml  # optional dependency
    except ImportError:
        yaml = None
    if yaml is not None:
        try:
            data = yaml.safe_load(raw)
        except Exception as exc:
            return None, f"invalid YAML frontmatter: {exc}"
    else:
        data = {}
        for line in raw.splitlines():
            if ":" not in line or line.strip().startswith("#"):
                continue
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip().strip('"')
    if not isinstance(data, dict):
        return None, "frontmatter must be a mapping"
    return data, ""


def check_skill(root: Path) -> dict:
    problems = []
    notes = []
    skill_md = root / "SKILL.md"
    if not skill_md.is_file():
        return {"ok": False, "problems": ["SKILL.md is missing"], "notes": [],
                "checks": {}}
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    front, error = parse_frontmatter(text)
    if error:
        problems.append(error)
        front = {}
    else:
        if not front.get("name"):
            problems.append("frontmatter has no 'name'")
        if not front.get("description"):
            problems.append("frontmatter has no 'description'")
        extra = sorted(set(front) - ALLOWED_KEYS)
        if extra:
            problems.append(f"unexpected frontmatter key(s): {', '.join(extra)}")
        desc = str(front.get("description") or "")
        if desc and len(desc) < 40:
            problems.append("frontmatter description is too short to route on")
        folder = root.resolve().name
        if front.get("name") and front["name"] != folder:
            problems.append(
                f"frontmatter name '{front['name']}' != folder name '{folder}'")

    # 4. every script compiles
    scripts_dir = root / "scripts"
    script_files = []
    if scripts_dir.is_dir():
        for path in sorted(scripts_dir.rglob("*.py")):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            script_files.append(path)
    bad = []
    for path in script_files:
        try:
            source = path.read_text(encoding="utf-8", errors="ignore")
            compile(source, str(path), "exec")
        except SyntaxError as exc:
            bad.append(f"{path.relative_to(root)}:{exc.lineno}: {exc.msg}")
        except Exception as exc:  # pragma: no cover - defensive
            bad.append(f"{path.relative_to(root)}: {exc}")
    if bad:
        problems.append(f"{len(bad)} script(s) do not compile: " + "; ".join(bad[:5]))

    # 5/6. references referenced from SKILL.md
    referenced = set(re.findall(r"(?:references|scripts)/[A-Za-z0-9_\-./]+\.md",
                                text))
    referenced |= set(re.findall(r"(?:references|scripts)/[A-Za-z0-9_\-./]+\.py", text))
    missing = sorted(ref for ref in referenced if not (root / ref).exists())
    if missing:
        problems.append(f"SKILL.md references missing file(s): {', '.join(missing)}")
    refs_dir = root / "references"
    linked_dirs = {str(Path(ref).parent).replace("\\", "/")
                   for ref in referenced if "/" in ref}
    # A directory that SKILL.md names (e.g. "references/knowledge/") counts as
    # linked for every file below it.
    for mention in re.findall(r"(?:references|scripts)/[A-Za-z0-9_\-./]*", text):
        mention = mention.rstrip(".")
        if mention.endswith("/"):
            linked_dirs.add(mention.rstrip("/"))
    linked = []
    for path in sorted(refs_dir.rglob("*.md")) if refs_dir.is_dir() else []:
        rel = path.relative_to(root).as_posix()
        if rel in referenced:
            continue
        ancestors = {str(Path(rel).parent).replace("\\", "/")}
        ancestors |= {str(p).replace("\\", "/") for p in Path(rel).parents}
        if ancestors & linked_dirs:
            continue  # the directory itself is linked from SKILL.md
        linked.append(rel)
    if linked:
        notes.append("not linked from SKILL.md: " + ", ".join(linked))

    # 7. absorbed manifest
    manifest_check = {"status": "skipped"}
    verifier = scripts_dir / "absorbed" / "verify_manifest.py"
    if verifier.is_file():
        try:
            sys.path.insert(0, str(verifier.parent))
            import verify_manifest  # type: ignore
            manifest_check = verify_manifest.verify()
        except Exception as exc:
            manifest_check = {"status": "error", "reason": str(exc)}
        else:
            if manifest_check.get("status") == "drift":
                problems.append(
                    f"absorbed scripts drifted from their sources "
                    f"({manifest_check.get('mismatches')} mismatch(es))")
            elif manifest_check.get("status") == "ok":
                notes.append(f"absorbed scripts verified: "
                             f"{manifest_check.get('checked')} file(s)")

    return {
        "ok": not problems,
        "problems": problems,
        "notes": notes,
        "checks": {
            "scripts_compiled": len(script_files),
            "references_checked": len(list(refs_dir.rglob("*.md"))) if refs_dir.is_dir() else 0,
            "absorbed": manifest_check,
        },
    }


# ---------------------------------------------------------------------------
# packaging
# ---------------------------------------------------------------------------
def package_skill(root: Path, out_dir: Path) -> Path:
    """Write <out_dir>/<skill-name>.skill (a zip of the skill folder)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{root.resolve().name}.skill"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(root.rglob("*")):
            rel = path.relative_to(root)
            if any(part in SKIP_DIRS for part in rel.parts):
                continue
            if path.suffix in {".pyc"} or path.name.endswith(".pyc-check"):
                continue
            if path.is_file():
                zf.write(path, (Path(root.resolve().name) / rel).as_posix())
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--package", metavar="OUT_DIR",
                        help="also write a distributable .skill zip")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"ERROR: {root} is not a directory", file=sys.stderr)
        return 2
    if not (root / "SKILL.md").is_file():
        print(f"ERROR: no SKILL.md in {root}", file=sys.stderr)
        return 2

    report = check_skill(root)
    report["root"] = str(root)
    if args.package:
        out = package_skill(root, Path(args.package).resolve())
        report["package"] = str(out)

    lines = ["=" * 62, "SKILL PACKAGE CHECK", "=" * 62]
    lines.append(f"root: {root}")
    for note in report["notes"]:
        lines.append(f"[NOTE] {note}")
    if report["ok"]:
        lines.append("[OK] skill package is healthy")
    else:
        for problem in report["problems"]:
            lines.append(f"[FAIL] {problem}")
    lines.append("=" * 62)
    emit(lines, report, args.json)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
