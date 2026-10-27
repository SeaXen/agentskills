#!/usr/bin/env python3
"""Shared helpers for the app-production-readiness scripts (stdlib only).

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

  which(cmd) / run_cmd(cmd, cwd, timeout)
      External-tool discovery and safe subprocess execution: a missing tool
      is reported, never crashed on, and a hanging tool is killed.

  gzip_size(path) / file_size(path)
      Byte sizes, optionally gzip-compressed, used by the budget checks.

  find_dist(root) / load_json(path) / write_json(path, data)
      Build-output discovery and JSON helpers shared by the report scripts.
"""
from __future__ import annotations

import gzip
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Directories that never hold project source.
SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "coverage",
    ".vercel", ".netlify", ".wrangler", ".svelte-kit", ".turbo", ".cache",
    ".pytest_cache", "__pycache__", ".venv", "venv", "target", ".gradle",
    ".agent", ".agents", ".claude", ".cursor", ".vscode", "vendor",
    "fixtures", "__fixtures__",
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


# --- external tools ------------------------------------------------------------

def which(cmd: str):
    """Absolute path of an executable, or None when it is not installed."""
    return shutil.which(cmd)


def run_cmd(cmd, cwd=None, timeout=120, env=None):
    """Run a command without a shell.

    Returns (returncode, stdout, stderr). A missing executable or a
    timeout is reported as a non-zero return code instead of raising:
    an absent tool must never look like a successful check.
    """
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
            shell=False,
        )
    except FileNotFoundError:
        return 127, "", f"executable not found: {cmd[0]}"
    except subprocess.TimeoutExpired:
        return 124, "", f"command timed out after {timeout}s: {' '.join(map(str, cmd))}"
    except OSError as exc:
        return 126, "", f"could not run {cmd[0]}: {exc}"
    return proc.returncode, proc.stdout or "", proc.stderr or ""


# --- sizes and files -----------------------------------------------------------

def file_size(path) -> int:
    try:
        return Path(path).stat().st_size
    except OSError:
        return 0


def gzip_size(path) -> int:
    """Size of the file after gzip compression (what a server actually sends)."""
    try:
        raw = Path(path).read_bytes()
    except OSError:
        return 0
    return len(gzip.compress(raw, 9))


def find_dist(root: Path):
    """Locate the build output directory of a project.

    Returns (path, kind) or (None, None) when nothing is built yet.

    ``public/`` is only a build output for static-site generators, and only when
    it actually looks like one (it contains an index.html). For a Next.js app
    the build output is ``.next/``; if ``.next`` is missing the project is NOT
    built, even when a ``public/`` folder with static assets exists - otherwise
    a failed build would be reported as a healthy 1 kB bundle.
    """
    root = Path(root)
    next_config = any(
        (root / n).exists()
        for n in ("next.config.js", "next.config.mjs", "next.config.ts", "next.config.cjs")
    )
    for name in (".next", "dist", "build", "out", "_site"):
        d = root / name
        if d.is_dir():
            if name == ".next":
                static = d / "static"
                if static.is_dir():
                    return static, "next"
                return d, "next"
            return d, name
    if not next_config:
        d = root / "public"
        if d.is_dir() and (d / "index.html").is_file():
            return d, "public"
    return None, None


def load_json(path):
    """Parse a JSON file, returning None instead of raising."""
    try:
        return json.loads(Path(path).read_text(encoding="utf-8", errors="ignore"))
    except (OSError, ValueError):
        return None


def write_json(path, data) -> bool:
    """Write JSON to a path, creating parents. Returns success."""
    try:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
        return True
    except OSError:
        return False


def slugify(text: str, fallback: str = "item") -> str:
    """Lowercase, hyphenated, filesystem-safe name."""
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    return s or fallback


