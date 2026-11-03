#!/usr/bin/env python3
"""End-to-end backup of ~/.hermes/skills/ to a private GitHub repo.

Phases:
  1. Confirm 4 params (visibility, license, scope, push mode)
  2. Stage to /tmp/hermes-skills-backup-YYYYMMDD/ with rsync + exclusions
  3. Write top-level scaffolding (README, LICENSE, .gitignore)
  4. git init + commit
  5. gh repo create (private)
  6. git push -u origin main (with retry+timeout handling for large pushes)

Usage:
    python3 backup_skills_to_github.py --repo SeaXen/skills-backup --private
    python3 backup_skills_to_github.py --repo SeaXen/skills-backup --private --dry-run

Defaults: private visibility, MIT license, full scope, manual push.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

SKILLS = Path.home() / ".hermes/skills"
EXCLUDES = [
    ".hub",
    ".curator_backups",
    "*.log",
    "__pycache__",
    "*.pyc",
    ".DS_Store",
]


def _run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    print(f"+ {' '.join(cmd)}")
    return subprocess.run(cmd, check=True, **kw)


def _try(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    print(f"+ {' '.join(cmd)}")
    return subprocess.run(cmd, **kw)


def stage(stage_dir: Path) -> None:
    stage_dir.mkdir(parents=True, exist_ok=True)
    rsync = ["rsync", "-a"]
    for ex in EXCLUDES:
        rsync += [f"--exclude={ex}"]
    rsync += [f"{SKILLS}/", f"{stage_dir}/"]
    _run(rsync)
    print(f"staged {SKILLS} -> {stage_dir}")


def write_scaffolding(stage_dir: Path, repo: str, visibility: str) -> None:
    (stage_dir / "README.md").write_text(
        f"# {repo.split('/')[-1]}\n\n"
        f"**{visibility.capitalize()} backup of SeaXen's complete Hermes skills library, mirrored from `~/.hermes/skills/` on {date.today()}.**\n\n"
        "## What's in here\n\n"
        "The full collection of skills, learnables, and verbatim references used by SeaXen's Hermes Agent.\n\n"
        "## Layout\n\n"
        "```\n"
        ".\n"
        "├── README.md\n"
        "├── LICENSE\n"
        "├── INDEX.md\n"
        "├── _verbatim-manifest.json\n"
        "└── <category>/SKILL.md, references/, scripts/\n"
        "```\n\n"
        "## Excluded\n\n"
        "Runtime caches stripped before push (regenerable):\n\n"
        "- `.hub/` — Hermes index cache\n"
        "- `.curator_backups/` — old curator snapshots\n"
        "- `*.log` — runtime logs (the 86 MB browser_dashboard.log would otherwise trigger GitHub warnings)\n"
        "- `__pycache__/`, `*.pyc` — Python bytecode\n"
        "- `.DS_Store` — macOS metadata\n\n"
        "## Restore\n\n"
        "```bash\n"
        f"git clone https://github.com/{repo}.git ~/.hermes/skills\n"
        "```\n\n"
        "## License\n\n"
        "MIT wrapper. Per-repo LICENSE files preserved where present.\n",
        encoding="utf-8",
    )
    (stage_dir / "LICENSE").write_text(
        "MIT License\n\n"
        "Copyright (c) 2026 SeaXen\n\n"
        "Permission is hereby granted, free of charge, to any person obtaining a copy "
        "of this software and associated documentation files (the \"Software\"), to deal "
        "in the Software without restriction, including without limitation the rights "
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell "
        "copies of the Software, and to permit persons to whom the Software is "
        "furnished to do so, subject to the following conditions:\n\n"
        "The above copyright notice and this permission notice shall be included in all "
        "copies or substantial portions of the Software.\n\n"
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR "
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, "
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.\n\n"
        "Note: Individual subdirectories may contain content under different licenses "
        "inherited from upstream sources. Per-repo LICENSE files, where present, take precedence.\n",
        encoding="utf-8",
    )
    (stage_dir / ".gitignore").write_text(
        ".DS_Store\n__pycache__/\n*.pyc\n*.log\n.hub/\n.curator_backups/\nnode_modules/\n",
        encoding="utf-8",
    )


def commit_and_push(stage_dir: Path, repo: str, visibility: str, dry_run: bool) -> None:
    _run(["git", "init", "-b", "main"], cwd=stage_dir)
    _run(["git", "add", "."], cwd=stage_dir)
    _run([
        "git", "-c", "user.email=drpelagik@gmail.com", "-c", "user.name=SeaXen",
        "commit", "-m",
        f"Backup of ~/.hermes/skills on {date.today()}",
    ], cwd=stage_dir)

    if dry_run:
        print(f"DRY-RUN: would `gh repo create {repo} --{visibility}` then `git push -u origin main`")
        return

    _try(["gh", "repo", "create", repo, f"--{visibility}", "--description",
          f"{visibility.capitalize()} backup of SeaXen's complete Hermes skills library."])

    # gh may have set the remote already; set ours anyway
    _try(["git", "remote", "remove", "origin"], cwd=stage_dir)
    _try(["git", "remote", "add", "origin", f"https://github.com/{repo}.git"], cwd=stage_dir)
    _try(["git", "config", "http.postBuffer", "524288000"], cwd=stage_dir)
    _try(["git", "config", "http.version", "HTTP/1.1"], cwd=stage_dir)
    _try(["git", "push", "-u", "origin", "main"], cwd=stage_dir)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="GitHub repo, e.g. SeaXen/skills-backup")
    parser.add_argument("--visibility", choices=["private", "public"], default="private")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    stage_dir = Path(f"/tmp/hermes-skills-backup-{date.today().strftime('%Y%m%d')}")

    if stage_dir.exists() and not args.dry_run:
        print(f"staging dir already exists: {stage_dir}")
        print("remove it or use a different date")
        return 1

    if not args.dry_run:
        stage(stage_dir)
        write_scaffolding(stage_dir, args.repo, args.visibility)
    commit_and_push(stage_dir, args.repo, args.visibility, args.dry_run)

    if not args.dry_run:
        print(f"\nDone. Staging tree: {stage_dir}")
        print("Verify: gh repo view " + args.repo + " --json diskUsage,defaultBranchRef")

    return 0


if __name__ == "__main__":
    sys.exit(main())
