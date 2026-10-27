#!/usr/bin/env python3
"""Shared helpers for the portable-deploy-qa scripts (stdlib only).

Every script in this folder uses these helpers so they agree on
argument parsing, project-root validation, file scoping and
machine-readable output:

  parse_cli(argv, json_default=False) -> (root_str, want_json, want_help)
      Accepts the project root and flags in ANY order, e.g.
      `script.py --json <root>` and `script.py <root> --json` behave
      identically. Unknown flags are ignored instead of being mistaken
      for a filesystem path.

  resolve_root(root_str) -> Path
      Absolute, expanded project root.

  root_error(root) -> str | None
      Human-readable reason why the root is unusable, or None if it is
      a usable directory. Callers MUST exit non-zero when this is set,
      so a bad path can never look like a clean run.

  emit(human_lines, payload, want_json) -> None
      In JSON mode the JSON payload is the ONLY thing written to stdout
      (the human report moves to stderr), so stdout always parses.

  walk_files(root) / root_files(root)
      File discovery scoped to the selected project root. Nested projects
      (a second `package.json` deeper in the tree) never leak into the
      parent project's results.

  is_dotenv(name) / is_env_template(name)
      One definition of "this is a real .env file" and "this is a safe
      template", shared by every scanner.

  readme_image_sources(text) / resolve_readme_asset(root, src)
      README image references, in Markdown and HTML form, resolved
      relative to the repository root.

  resolve_out_dir(root, out_arg)
      Resolves a write target and guarantees it stays inside the root.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

# Directories that never hold project source.
SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "coverage",
    ".vercel", ".netlify", ".wrangler", ".svelte-kit", ".turbo", ".cache",
    ".pytest_cache", "__pycache__", ".venv", "venv", "target", ".gradle",
    ".agent", ".agents", ".claude", ".cursor", ".vscode", "vendor",
}

# A directory holding one of these is a project of its own.
APP_MARKERS = (
    "package.json", "pyproject.toml", "requirements.txt", "go.mod", "Cargo.toml",
    "Dockerfile", "wrangler.toml", "fly.toml", "vercel.json", "netlify.toml",
)

# Env files that are safe to publish (templates).
ENV_TEMPLATE_NAMES = {
    ".env.example", "env.example", ".env.sample", ".env.template",
    ".env.dist", "env.template", "env.sample", ".env.template.example",
}


def parse_cli(argv, json_default=False):
    """Split argv into (root, want_json, want_help); order-independent."""
    root = None
    want_json = bool(json_default)
    want_help = False
    for arg in argv:
        if arg in ("-h", "--help"):
            want_help = True
        elif arg == "--json":
            want_json = True
        elif arg.startswith("-"):
            continue  # unknown flag: ignore, never treat as a path
        elif root is None:
            root = arg
    return (root or "."), want_json, want_help


def resolve_root(root_str):
    """Absolute, expanded project root."""
    return Path(root_str).expanduser().resolve()


def root_error(root):
    """Return why `root` is unusable, or None when it is a valid dir."""
    root = Path(root)
    if not root.exists():
        return f"project root does not exist: {root}"
    if not root.is_dir():
        return f"project root is not a directory: {root}"
    return None


def emit(human_lines, payload, want_json):
    """Write the human report and the machine payload.

    With --json, stdout carries only the JSON payload so it always
    parses regardless of argument order; the human report goes to
    stderr. Without --json the human report stays on stdout.
    """
    if want_json:
        for line in human_lines:
            print(line, file=sys.stderr)
        print(json.dumps(payload, indent=2))
    else:
        for line in human_lines:
            print(line)


def is_env_template(name: str) -> bool:
    """True for safe-to-publish env templates (.env.example, env.sample, ...)."""
    n = str(name).lower()
    if n in ENV_TEMPLATE_NAMES:
        return True
    return bool(re.match(r"^\.?env[.-](example|sample|template|dist)\b", n))


def is_dotenv(name: str) -> bool:
    """True for REAL env files (.env, .env.local, .env.production, ...).

    Templates are excluded: they are meant to be committed.
    """
    n = str(name).lower()
    if is_env_template(n):
        return False
    if n in {".env", "env"}:
        return True
    return n.startswith(".env.") or n.startswith("env.")


def is_nested_project(path: Path) -> bool:
    """True when `path` is a project root of its own (nested app)."""
    path = Path(path)
    if path.is_file():
        path = path.parent
    return any((path / m).is_file() for m in APP_MARKERS)


def walk_files(root: Path, skip_dirs=None, exclude_nested=True):
    """Yield every file under `root`, skipping build dirs and nested apps.

    A nested app (a second `package.json` deeper in the tree) is a
    separate project and must never leak into the parent's results.
    """
    root = Path(root)
    skip = SKIP_DIRS if skip_dirs is None else skip_dirs
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in skip)
        current = Path(dirpath)
        if exclude_nested and current != root and is_nested_project(current):
            dirnames[:] = []
            continue
        for fn in sorted(filenames):
            yield current / fn


def root_files(root: Path) -> dict:
    """Map of file name -> path for files living directly in `root`."""
    out = {}
    try:
        for child in sorted(Path(root).iterdir()):
            if child.is_file():
                out[child.name] = child
    except OSError:
        pass
    return out


# --- README images -----------------------------------------------------------

MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(\s*<?([^)>\s]+)>?(?:\s+[\"'][^\"']*[\"'])?\s*\)")
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*?\bsrc\s*=\s*[\"']([^\"']+)[\"']", re.I)
HTML_SOURCE_RE = re.compile(r"<source\b[^>]*?\bsrc(?:set)?\s*=\s*[\"']([^\"']+)[\"']", re.I)


def readme_image_sources(text: str) -> list:
    """Image references in a README: Markdown, HTML <img> and <source>.

    Order is preserved and duplicates are removed.
    """
    found = []
    for rx in (MD_IMAGE_RE, HTML_IMAGE_RE, HTML_SOURCE_RE):
        for m in rx.finditer(text or ""):
            src = m.group(1).strip()
            # a srcset may list several candidates: use the first one
            if rx is HTML_SOURCE_RE and "," in src:
                src = src.split(",")[0].strip().split()[0] if src.split(",")[0].strip() else ""
            if src and src not in found:
                found.append(src)
    return found


def is_remote_asset(src: str) -> bool:
    """True for URLs and inline data: they are not local files."""
    s = str(src).strip().lower()
    return s.startswith(("http://", "https://", "//", "data:", "mailto:", "#"))


def resolve_readme_asset(root: Path, src: str):
    """Resolve a README image reference to a file under `root`.

    README images are relative to the REPOSITORY ROOT (not to the
    README's own folder), matching how GitHub renders them. Returns the
    resolved Path, or None when the asset is remote or missing.
    """
    src = str(src).strip()
    if not src or is_remote_asset(src):
        return None
    # strip any query/hash fragment
    src = src.split("#", 1)[0].split("?", 1)[0]
    if not src:
        return None
    src = src.replace("\\", "/")
    root = Path(root)
    candidate = root / src.lstrip("/")
    try:
        resolved = candidate.resolve()
    except OSError:
        return None
    if not resolved.exists():
        return None
    return resolved


def resolve_out_dir(root: Path, out_arg, must_be_inside=True):
    """Resolve an output directory, guaranteeing it stays inside `root`.

    Returns (path, error_message). `error_message` is None on success.
    Absolute paths outside the project root are rejected so a stray
    `--out ../../etc` can never write outside the intended directory.
    """
    root = Path(root).resolve()
    raw = Path(str(out_arg))
    out = raw if raw.is_absolute() else (root / str(out_arg).lstrip("/\\"))
    try:
        resolved = out.resolve()
    except OSError:
        resolved = out.absolute()
    if must_be_inside:
        try:
            resolved.relative_to(root)
        except ValueError:
            return resolved, f"output directory escapes the project root: {resolved}"
    return resolved, None

