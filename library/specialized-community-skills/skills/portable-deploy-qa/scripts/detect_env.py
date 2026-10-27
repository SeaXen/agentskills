#!/usr/bin/env python3
"""Detect app runtime facts so QA gates target the right port/URL/routes.

Usage:  python detect_env.py [project_root]
Output: JSON { app_url, port, pkg, framework, routes, healthz, dist_dir }
Exit 0 detected | Exit 1 nothing found (caller should ask the user)
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    parse_cli,
    resolve_root,
    root_error,
    walk_files,
)

SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "coverage", ".turbo"}


def read(p: Path, limit: int = 200_000) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")[:limit]
    except OSError:
        return ""


def find_port(root: Path):
    """env file > package.json scripts > framework config > Dockerfile EXPOSE > fly.toml."""
    for name in (".env.local", ".env", ".env.example"):
        f = root / name
        if not f.is_file():
            continue
        m = re.search(r"^\s*PORT\s*=\s*(\d{2,5})\s*$", read(f), re.MULTILINE)
        if m:
            return int(m.group(1))

    pkg = root / "package.json"
    if pkg.is_file():
        try:
            data = json.loads(read(pkg))
        except json.JSONDecodeError:
            data = {}
        for script in (data.get("scripts", {}) or {}).values():
            m = re.search(r"(?:--port[= ]|-p\s*|PORT=)(\d{2,5})", str(script))
            if m:
                return int(m.group(1))

    for cfg, pat in (
        ("vite.config.ts", r"port\s*:\s*(\d{2,5})"),
        ("vite.config.js", r"port\s*:\s*(\d{2,5})"),
        ("next.config.js", r"port\s*:\s*(\d{2,5})"),
        ("angular.json", r"\"port\"\s*:\s*(\d{2,5})"),
        ("wrangler.toml", r"port\s*=\s*(\d{2,5})"),
        ("fly.toml", r"internal_port\s*=\s*(\d{2,5})"),
    ):
        f = root / cfg
        if f.is_file():
            m = re.search(pat, read(f))
            if m:
                return int(m.group(1))

    df = root / "Dockerfile"
    if df.is_file():
        m = re.search(r"EXPOSE\s+(\d{2,5})", read(df))
        if m:
            return int(m.group(1))
    return None



def find_framework(root: Path):
    """Detect the app's framework/stack. Checks deps AND devDeps, then files."""
    deps = {}
    pkg = root / "package.json"
    if pkg.is_file():
        try:
            data = json.loads(read(pkg))
            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        except json.JSONDecodeError:
            deps = {}
    for marker, name in (
        ("next", "Next.js"), ("vite", "Vite"), ("@angular/core", "Angular"),
        ("nuxt", "Nuxt"), ("astro", "Astro"), ("svelte", "Svelte"),
        ("@remix-run", "Remix"), ("express", "Express"), ("hono", "Hono"),
        ("fastify", "Fastify"), ("gatsby", "Gatsby"), ("@nestjs/core", "NestJS"),
        ("@sveltejs/kit", "SvelteKit"), ("react", "React"), ("vue", "Vue"),
    ):
        if marker in deps:
            return name
    for f, name in (("server.py", "Python"), ("main.py", "Python"), ("app.py", "Python"),
                    ("main.go", "Go"), ("Cargo.toml", "Rust"), ("requirements.txt", "Python"),
                    ("pyproject.toml", "Python"), ("go.mod", "Go")):
        if (root / f).is_file():
            return name
    # static site: no framework deps but plain HTML entrypoint
    if not deps and (root / "index.html").is_file():
        return "Static"
    return None


def find_pkg(root: Path) -> str | None:
    """Detect the package manager / ecosystem for the app."""
    for lock, mgr in (("pnpm-lock.yaml", "pnpm"), ("bun.lockb", "bun"),
                      ("bun.lock", "bun"), ("yarn.lock", "yarn"),
                      ("package-lock.json", "npm")):
        if (root / lock).is_file():
            return mgr
    if (root / "package.json").is_file():
        return "npm"
    if (root / "uv.lock").is_file():
        return "uv"
    if (root / "poetry.lock").is_file():
        return "poetry"
    if (root / "pdm.lock").is_file():
        return "pdm"
    if (root / "Pipfile.lock").is_file() or (root / "Pipfile").is_file():
        return "pipenv"
    py = root / "pyproject.toml"
    if py.is_file():
        try:
            content = read(py).lower()
            if "poetry" in content:
                return "poetry"
            if "uv" in content:
                return "uv"
            if "[tool.pdm]" in content:
                return "pdm"
        except OSError:
            pass
        return "pip"
    if (root / "requirements.txt").is_file():
        return "pip"
    for f in ("server.py", "main.py", "app.py", "manage.py"):
        if (root / f).is_file():
            return "pip"
    if (root / "go.mod").is_file():
        return "go"
    if (root / "Cargo.toml").is_file():
        return "cargo"
    return None


def find_healthz(root: Path):
    for p in walk_files(root, skip_dirs=SKIP_DIRS):
        if "health" in p.name.lower():
            txt = read(p)
            m = re.search(r"['\"](/[\w\-/]*(?:healthz|health)[\w\-/]*)['\"]", txt)
            if m:
                return m.group(1)
    return None


def find_routes(root: Path) -> list:
    """Routes from framework dirs, else from anchor hrefs in source."""
    routes = []
    for base in ("app", "pages", "src/app", "src/pages", "src/routes"):
        d = root / base
        if not d.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(d):
            dirnames[:] = [x for x in dirnames if x not in SKIP_DIRS and not x.startswith("(")]
            for fn in filenames:
                if fn in ("page.tsx", "page.ts", "page.jsx", "page.js", "route.ts",
                          "route.tsx", "route.js", "index.tsx", "index.ts",
                          "index.jsx", "index.js"):
                    rel = os.path.relpath(os.path.join(dirpath, fn), d)
                    slug = os.path.dirname(rel).replace(os.sep, "/")
                    if slug not in (".", ""):
                        routes.append("/" + slug)
        if routes:
            break

    if not routes:
        for p in walk_files(root, skip_dirs=SKIP_DIRS):
            if p.suffix in (".tsx", ".jsx", ".ts", ".js", ".html", ".vue", ".svelte"):
                txt = read(p, 80_000)
                for m in re.finditer(r"""href\s*=\s*["'](/[^"'#?]{0,60})["']""", txt):
                    r = m.group(1)
                    if not r.startswith("//") and not r.startswith(("/_", "/api/")):
                        routes.append(r)
            if len(set(routes)) > 40:
                break

    cleaned = sorted({r.rstrip("/") or "/" for r in routes if r.startswith("/")})
    return cleaned[:40]


def main() -> int:
    root_arg, _json_mode, want_help = parse_cli(sys.argv[1:])
    if want_help:
        print(__doc__)
        print("\nEnv overrides: APP_URL, PORT, ROUTES, HEALTHZ")
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        # This script's contract is JSON output, so stdout must stay parseable
        # even on failure. The human message goes to stderr.
        print(json.dumps({"error": err}, indent=2))
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    port = find_port(root)
    url_env = os.environ.get("APP_URL")
    app_url = url_env or (f"http://localhost:{port}" if port else "http://localhost:3000")
    result = {
        "app_url": app_url,
        "port": port,
        "pkg": find_pkg(root),
        "framework": find_framework(root),
        "routes": find_routes(root),
        "healthz": find_healthz(root) or "/",
        "dist_dir": next((d for d in ("dist", "build", "out", ".next", "public")
                          if (root / d).is_dir()), None),
    }
    print(json.dumps(result, indent=2))
    if port is None and not url_env:
        print("WARN: port not detected - ask user for APP_URL", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

