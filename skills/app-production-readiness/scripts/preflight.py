#!/usr/bin/env python3
"""Production-readiness preflight: checks the repo for the files/config a free-tier
production deploy needs. Non-destructive, read-only.

Usage:  python preflight.py [project_root]
Exit 0: all required checks pass | Exit 1: one or more required checks fail
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    emit,
    is_dotenv,
    is_env_template,
    parse_cli,
    resolve_root,
    root_error,
    root_files,
    walk_files,
)

SKIP = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "coverage",
        ".vercel", ".netlify", ".wrangler", ".svelte-kit", ".turbo", ".cache",
        ".pytest_cache", "__pycache__", ".venv", "venv", "target", ".gradle", "qa"}


def read(p: Path, limit: int = 200_000) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")[:limit]
    except OSError:
        return ""


def walk(root: Path):
    """Files under `root`, excluding nested projects (separate apps)."""
    return walk_files(root, skip_dirs=SKIP)


class Check:
    def __init__(self, name, ok, required, detail=""):
        self.name, self.ok, self.required, self.detail = name, ok, required, detail

    def as_dict(self):
        return {"name": self.name, "ok": self.ok, "required": self.required, "detail": self.detail}


# --- hardcoded-secret heuristic -------------------------------------------
# Module level on purpose: scripts/test_preflight.py imports these so the
# self-test exercises THIS implementation instead of a copy of it. A duplicated
# regex set keeps passing while the shipped scanner drifts - a test that
# cannot fail is worse than no test.
_ASSIGN = re.compile(
    r"""(?P<name>[A-Za-z_$][A-Za-z0-9_$]*(?:\.[A-Za-z0-9_$]+)*)"""
    r"""\s*[:=]\s*(?P<q>['"])(?P<val>[^'"\n]{8,})(?P=q)""",
)
# Unquoted assignment: the normal shape of a secret in a .env file
# ("STRIPE_SECRET_KEY=sk_live_...") or in YAML ("api_key: abc123").
# The value charset excludes the characters that appear in ordinary code
# (parens, braces, semicolons, spaces) so an expression such as
# `apiKey = response.json().apiKey` is never mistaken for a secret.
_ASSIGN_BARE = re.compile(
    r"""(?P<name>[A-Za-z_$][A-Za-z0-9_$]*(?:\.[A-Za-z0-9_$]+)*)"""
    r"""\s*[:=]\s*(?P<val>[A-Za-z0-9_\-./+~=]{12,})"""
    r"""\s*(?:[;,]\s*)?(?:#[^\n]*)?$""",
)
_SECRET_NAME = re.compile(
    r"(api[_-]?key|secret|token|password|passwd|pwd|credential|private[_-]?key|"
    r"signing[_-]?key|access[_-]?key)", re.I)
_BENIGN = re.compile(
    r"(example|placeholder|dummy|fake|mock|sample|fixture|stub|redacted|"
    r"changeme|your[_-]?key|your[_-]?secret|xxx|todo|lorem|\.\.\.|"
    r"^<[^>]+>$|\$\{|\{\{|process\.env|import\.meta\.env|os\.environ|"
    r"^demo|demo_|demo$|masked|redacted|hidden|scrubbed|"
    r"^[A-Za-z_]*_(ID|NAME|LABEL|TYPE|FIELD|KEY_NAME)$)", re.I)
# identifier names that mark a constant as NOT a secret.
# NOTE: "fallback"/"default" are deliberately NOT here - a hardcoded
# FALLBACK_SECRET / DEFAULT_API_KEY is a genuine finding.
_NON_SECRET_NAME = re.compile(
    r"(placeholder|example|dummy|sample|mock|fixture|"
    r"label|title|description|message|field|column|key_name|"
    r"_url$|_uri$|_endpoint$|_host$|_domain$|^url$|^uri$|"
    r"_cookie$|^cookie$|_name$|_header$|_field$|^demo$|_demo$)", re.I)
# values that are clearly not secrets
_BENIGN_VALUE = re.compile(
    r"^(https?|wss?|mailto):|^[/.]|^__Host-|^__Secure-|"
    r"^https?://|^/api/|^https://|^www\.", re.I)
# a salt is public by design (it is stored next to the ciphertext)
_SALT_NAME = re.compile(r"(^|[^a-z])(salt|pepper)([^a-z]|$)", re.I)
# A value that is the NAME of an env var (e.g. 'GOOGLE_CLIENT_SECRET')
# is a reference, not a secret. Detect ALL_CAPS_WITH_UNDERSCORES.
_ENV_NAME_VALUE = re.compile(r"^[A-Z][A-Z0-9_]{6,}$")


def flag_secret_line(line: str) -> bool:
    """True when a single source line looks like a hardcoded secret.

    Heuristic, not a replacement for a real secret scanner. It deliberately
    ignores env reads, obvious placeholders and public salts so that real
    findings stand out.
    """
    if "process.env" in line or "os.environ" in line or "import.meta.env" in line:
        return False
    m = _ASSIGN.search(line)
    if not m:
        # No quoted value: try the unquoted form (.env / YAML).
        m = _ASSIGN_BARE.search(line.strip())
        if not m:
            return False
    name, value = m.group("name"), m.group("val").strip()
    if not _SECRET_NAME.search(name):
        return False
    if not value or _BENIGN.search(value):
        return False
    if _BENIGN_VALUE.search(value):
        return False
    if _ENV_NAME_VALUE.match(value):
        return False
    if _NON_SECRET_NAME.search(name):
        return False
    if _SALT_NAME.search(name):
        return False
    # Real-world secrets are long and random-looking: they mix letters
    # with digits, or mix upper and lower case. A long all-lowercase
    # dashed/underscored phrase ("super-secret-binance-key") reads as a
    # human label or identifier, not an actual secret.
    if len(value) < 12 or not re.search(r"[A-Za-z]", value):
        return False
    has_digit = bool(re.search(r"[0-9]", value))
    has_upper = any(c.isupper() for c in value)
    return has_digit or has_upper


def _git_tracked(root: Path) -> set | None:
    """The repo-relative paths git tracks, or None when git cannot tell us.

    Knowing what git actually tracks is the only reliable way to tell a
    developer's own local ``.env`` (harmless, gitignored) from a ``.env``
    that is about to be published (a leak).
    """
    import subprocess
    try:
        proc = subprocess.run(["git", "ls-files", "-z"], cwd=str(root),
                              capture_output=True, text=True, timeout=20)
    except (OSError, ValueError):
        return None
    except Exception:  # subprocess.TimeoutExpired and friends
        return None
    if proc.returncode != 0:
        return None
    return {p for p in (proc.stdout or "").split("\0") if p}


def _gitignore_ignores(gitignore_text: str, name: str) -> bool:
    """True when .gitignore would ignore a file with this name."""
    import fnmatch
    for raw in (gitignore_text or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        pattern = line.rstrip("/")
        if not pattern:
            continue
        if fnmatch.fnmatch(name, pattern):
            return True
    return False


def detect_ecosystem(root: Path, files: dict | None = None) -> str:
    """Identify the project's ecosystem so checks match the stack.

    Returns one of: node, python, go, rust, worker, static, unknown.
    """
    if (root / "package.json").is_file():
        return "node"
    if any((root / n).is_file() for n in ("requirements.txt", "pyproject.toml", "Pipfile", "setup.py", "setup.cfg")):
        return "python"
    if (root / "go.mod").is_file():
        return "go"
    if (root / "Cargo.toml").is_file():
        return "rust"
    if any((root / n).is_file() for n in ("wrangler.toml", "wrangler.json", "wrangler.jsonc")):
        return "worker"
    if (root / "index.html").is_file():
        return "static"
    return "unknown"


def run(root: Path) -> list:
    checks = []
    # Manifest/config checks use files DIRECTLY in the project root: a nested
    # app (packages/web/package.json) is a separate project and must never be
    # mistaken for the root project's own manifest.
    files = root_files(root)
    # Recursive scans use every file of THIS project only.
    all_files = list(walk(root))
    all_names = {p.name for p in all_files}
    pkg_raw = read(root / "package.json")
    pkg = {}
    pkg_ok = False
    try:
        parsed = json.loads(pkg_raw)
        # A valid JSON document that is not an object (a list, a string) is
        # still not a usable manifest: reading .get() off it would crash.
        if isinstance(parsed, dict):
            pkg = parsed
            pkg_ok = True
    except json.JSONDecodeError:
        pass
    scripts = pkg.get("scripts", {}) or {}
    if not isinstance(scripts, dict):
        scripts = {}
    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
    if not isinstance(deps, dict):
        deps = {}

    # --- packaging & build ---
    # These checks must be ecosystem-aware: a Python/Go/Rust/Workers project
    # has no package.json, so a Node-only check would report false failures.
    ecosystem = detect_ecosystem(root, files)
    is_node = ecosystem == "node"
    is_python = ecosystem == "python"
    is_go = ecosystem == "go"
    is_rust = ecosystem == "rust"
    is_worker = ecosystem == "worker"
    is_static = ecosystem == "static"

    if is_node:
        checks.append(Check("package.json present", (root / "package.json").is_file(), True))
        checks.append(Check("package.json is valid JSON", pkg_ok, True,
                            "" if pkg_ok else "package.json does not parse as a JSON object"))
        checks.append(Check("build script defined", "build" in scripts, True, str(list(scripts))))
        checks.append(Check("start script defined", "start" in scripts, True, str(list(scripts))))
        checks.append(Check("lint script defined", "lint" in scripts, False))
        checks.append(Check("test script defined", "test" in scripts, False))
    else:
        # Non-Node ecosystems: verify the project declares its own runnable entry.
        if is_python:
            entry_names = ("main.py", "app.py", "server.py", "manage.py",
                           "wsgi.py", "asgi.py")
            # The entrypoint may live in a package (src/main.py) - the other
            # ecosystems already scan recursively, python must not be the
            # odd one out.
            entry_ok = (any(n in files for n in entry_names)
                        or any(p.name in entry_names for p in all_files))
            checks.append(Check("python entrypoint present", entry_ok, True,
                                "main.py/app.py/server.py anywhere in the project"))
            has_dep_manifest = any(n in files for n in ("requirements.txt", "pyproject.toml", "Pipfile"))
            checks.append(Check("python dependency manifest", has_dep_manifest, True))
        elif is_go:
            checks.append(Check("go.mod present", (root / "go.mod").is_file(), True))
            # The entrypoint is normally main.go at the root or cmd/<name>/main.go.
            go_files = [p for p in all_files if p.suffix == ".go"]
            checks.append(Check("go entrypoint present", bool(go_files), True,
                                "no .go source file found"))
        elif is_rust:
            checks.append(Check("Cargo.toml present", (root / "Cargo.toml").is_file(), True))
            # Rust sources live in src/ (src/main.rs, src/lib.rs).
            rust_files = [p for p in all_files if p.suffix == ".rs"]
            checks.append(Check("rust entrypoint present", bool(rust_files), True,
                                "no .rs source file found"))
        elif is_worker:
            wrangler_files = ("wrangler.toml", "wrangler.json", "wrangler.jsonc")
            checks.append(Check("wrangler config present",
                                any((root / n).is_file() for n in wrangler_files), True))
            worker_files = [p for p in all_files
                            if p.suffix in (".js", ".ts", ".mjs", ".cjs")]
            checks.append(Check("worker entrypoint present", bool(worker_files), True,
                                "no worker source file found"))
        elif is_static:
            checks.append(Check("static index.html present", (root / "index.html").is_file(), True))
        else:
            checks.append(Check("project manifest detected", False, True,
                                "no package.json/requirements.txt/go.mod/Cargo.toml/wrangler config"))

    # --- typescript strict ---
    ts = files.get("tsconfig.json")
    strict = False
    if ts:
        txt = read(ts)
        strict = bool(re.search(r'"strict"\s*:\s*true', txt))
    checks.append(Check("tsconfig strict mode", strict, bool(ts), "tsconfig.json" if ts else "no tsconfig"))

    # --- env hygiene ---
    # NOTE: the conventional filename is ".env.example" (leading dot). Also accept
    # "env.example" and ".env.sample" so real repos are not flagged by a naming nit.
    env_example = any(is_env_template(n) for n in files)
    # A static site with no server-side config has nothing to template.
    checks.append(Check(".env.example present", env_example, ecosystem != "static"))
    # Real env files (".env", ".env.local", ".env.production", ...) are local
    # secrets and must never be committed - templates are fine.
    env_real = sorted(n for n in all_names if is_dotenv(n))
    gitignore = read(root / ".gitignore")
    tracked = _git_tracked(root)

    def env_committed(name: str) -> bool:
        """True when git would publish this env file."""
        if tracked is not None:
            return any(t == name or t.endswith("/" + name) for t in tracked)
        # No git information: fall back to the ignore rules.  A file the
        # .gitignore covers is local; everything else would be published.
        return not _gitignore_ignores(gitignore, name)

    committed_env = [n for n in env_real if env_committed(n)]
    checks.append(Check(".env not committed", not committed_env, False,
                        (f"{', '.join(committed_env)} is committed - it holds your secrets"
                         if committed_env else
                         (f"{', '.join(env_real)} exists locally (keep it gitignored)"
                          if env_real else ""))))
    ignores_env = bool(re.search(r"^\.env", gitignore, re.MULTILINE))
    checks.append(Check(".gitignore ignores .env", ignores_env, bool(env_example), ""))

    # --- secrets not hardcoded ---
    # Uses the shared heuristic (flag_secret_line) so the self-test in
    # scripts/test_preflight.py covers exactly what ships.
    suspicious = []
    local_env = []
    test_re = re.compile(
        r"(^|[\\/])(tests?|__tests__|spec|e2e|__mocks__|fixtures?|__fixtures__)([\\/]|$)|"
        r"\.(test|spec)\.[cm]?[jt]sx?$", re.I)
    # scripts that only push/seed demo or test data
    seed_file = re.compile(
        r"(^|[\\/])(scripts?|tools?|seed)([\\/]|$)|[-_](test|seed|fixture)[-_.]", re.I)

    def is_test_path(p: Path) -> bool:
        rel = p.relative_to(root).as_posix()
        return bool(test_re.search(rel)) or bool(seed_file.search(rel))

    for p in walk(root):
        # Dotfiles like ".env.local" have no ".env" suffix, so env files are
        # matched by NAME as well as by extension.
        if p.suffix not in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
                            ".env", ".json", ".yml", ".yaml", ".toml"} \
                and not is_dotenv(p.name):
            continue
        if is_env_template(p.name):
            continue
        if is_test_path(p):
            continue
        for i, line in enumerate(read(p, 60_000).splitlines(), 1):
            if not flag_secret_line(line):
                continue
            hit = f"{p.relative_to(root)}:{i}"
            if is_dotenv(p.name) and not env_committed(p.name):
                # A developer's own, gitignored .env is not a leak: the tool
                # cannot see the developer's machine, and failing the build
                # over a local file contradicts the ".env not committed" hint.
                local_env.append(hit)
            else:
                suspicious.append(hit)
    checks.append(Check("no hardcoded secrets", not suspicious, True, ", ".join(suspicious[:3])))
    if local_env:
        checks.append(Check("local env file holds secrets", False, False,
                            f"{', '.join(local_env[:3])} - keep this file out of git"))

    # --- docker ---
    checks.append(Check("Dockerfile present", "Dockerfile" in files, False))
    checks.append(Check(".dockerignore present", ".dockerignore" in files, False))

    # --- CI ---
    gh = root / ".github" / "workflows"
    wf = list(gh.glob("*.yml")) + list(gh.glob("*.yaml")) if gh.is_dir() else []
    checks.append(Check("GitHub Actions workflow", bool(wf), False, ", ".join(w.name for w in wf)))

    # --- docs ---
    readme = (root / "README.md").is_file()
    checks.append(Check("README.md present", readme, True))
    rtxt = read(root / "README.md") if readme else ""
    for plat in ("Docker", "Vercel", "Netlify", "Railway", "Render", "Fly.io", "Cloudflare"):
        checks.append(Check(f"README documents {plat}", plat.lower() in rtxt.lower(), False))

    # --- health endpoint ---
    # A file named *health* is the easy case; the common case is a route
    # string declared in server.js / routes.ts / app.py.
    has_health = any("health" in p.name.lower() for p in walk(root))
    if not has_health:
        route_re = re.compile(r"""['"](/[\w\-/]*(?:healthz|health|alive)[\w\-/]*)['"]""")
        for p in walk(root):
            if p.suffix in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".py",
                            ".go", ".rs", ".rb"} and route_re.search(read(p, 80_000)):
                has_health = True
                break
    checks.append(Check("health endpoint source", has_health, False))

    # --- port handling (must not hardcode) ---
    hardcoded = []
    port_patterns = (
        r"listen\(\s*3000\s*\)",                # node / http server
        r"\brun\(\s*[^)]*\bport\s*=\s*3000\b",  # python app.run(port=3000)
        r"ListenAndServe\(\s*[\"']:3000",       # go
        r"\bPORT\s*=\s*3000\b",                 # const PORT = 3000
    )
    port_re = re.compile("|".join(port_patterns))
    for p in walk(root):
        if p.suffix in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
                        ".py", ".go", ".rb", ".rs"} and "node_modules" not in str(p):
            for i, line in enumerate(read(p, 60_000).splitlines(), 1):
                if port_re.search(line):
                    hardcoded.append(f"{p.relative_to(root)}:{i}")
    checks.append(Check("port from env (not hardcoded)", not hardcoded, False, ", ".join(hardcoded[:3])))

    # --- security headers / CSP ---
    has_csp = False
    for p in walk(root):
        if p.suffix in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
                        ".json", ".toml", ".yml", ".yaml"} and "node_modules" not in str(p):
            if re.search(r"Content-Security-Policy", read(p, 80_000), re.I):
                has_csp = True
                break
    checks.append(Check("CSP / security headers", has_csp, False))

    # --- reproducible installs: a lockfile must be committed ---
    lockfiles = ("package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb",
                 "bun.lock", "requirements.txt", "poetry.lock", "uv.lock",
                 "Pipfile.lock", "Cargo.lock", "go.sum")
    has_lock = any((root / f).is_file() for f in lockfiles)
    checks.append(Check("dependency lockfile committed", has_lock, is_node,
                        "" if has_lock else "no lockfile - installs are not reproducible"))

    # --- .env.example must cover the variables the code actually reads ---
    referenced = set()
    env_pat = re.compile(r"""process\.env\.([A-Z][A-Z0-9_]{2,})"""
                         r"""|os\.environ(?:\.get)?\[?['"]([A-Z][A-Z0-9_]{2,})['"]\]?"""
                         r"""|os\.getenv\(\s*['"]([A-Z][A-Z0-9_]{2,})['"]"""
                         r"""|import\.meta\.env\.([A-Z][A-Z0-9_]{2,})""")
    for p in walk(root):
        if p.suffix in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".py", ".go"}:
            for m in env_pat.finditer(read(p, 60_000)):
                referenced.add(next(g for g in m.groups() if g))
    template_keys = set()
    for name in files:
        if is_env_template(name):
            for line in read(files[name], 20_000).splitlines():
                m = re.match(r"^\s*([A-Z][A-Z0-9_]{2,})\s*=", line)
                if m:
                    template_keys.add(m.group(1))
    undocumented = sorted(referenced - template_keys)
    checks.append(Check(".env.example documents every used variable",
                        not undocumented, False,
                        ", ".join(undocumented[:6])))

    # --- CI must actually build and test, not just exist ---
    ci_text = ""
    for w in wf:
        ci_text += read(w, 80_000)
    checks.append(Check("CI runs build and test",
                        bool(ci_text) and bool(re.search(r"\btest\b", ci_text, re.I))
                        and bool(re.search(r"\bbuild\b", ci_text, re.I)),
                        False,
                        "the workflow should run both a build and the test suite"))

    # --- test hygiene: no focused/skipped suites left behind ---
    focused = []
    for p in walk(root):
        try:
            rel_parts = p.relative_to(root).parts
        except ValueError:
            rel_parts = p.parts
        if re.search(r"\.(test|spec)\.[cm]?[jt]sx?$", p.name) or "tests" in rel_parts:
            txt = read(p, 60_000)
            for pat, label in ((r"\bdescribe\.only\b|\bit\.only\b|\bfdescribe\b|\bfit\s*\(", "focused test"),
                               (r"\bdescribe\.skip\b|\bit\.skip\b|\bxtest\b", "skipped test"),
                               (r"@pytest\.mark\.skip|@unittest\.skip", "skipped test")):
                if re.search(pat, txt):
                    focused.append(f"{p.relative_to(root)} ({label})")
                    break
    checks.append(Check("no focused or skipped tests", not focused, False,
                        ", ".join(focused[:4])))

    # --- repository hygiene ---
    checks.append(Check("node_modules not committed",
                        not (root / "node_modules").is_dir(), False,
                        "node_modules must be gitignored"))
    checks.append(Check("LICENSE file present",
                        any(n.upper().startswith("LICENSE") for n in files), False,
                        "add a LICENSE file"))

    return checks



def main() -> int:
    root_arg, json_mode, want_help = parse_cli(sys.argv[1:])
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        if json_mode:
            payload = [{"name": "project root is a directory", "ok": False,
                        "required": True, "detail": err}]
            emit([f"[FAIL] {err}"], payload, True)
        else:
            print(f"[FAIL] {err}", file=sys.stderr)
        return 1

    checks = run(root)
    ecosystem = detect_ecosystem(root)
    required_fail = [c for c in checks if c.required and not c.ok]
    optional_fail = [c for c in checks if not c.required and not c.ok]

    payload = [c.as_dict() for c in checks]

    lines = []
    lines.append("=" * 62)
    lines.append(f"PRODUCTION READINESS PREFLIGHT  [{ecosystem}]")
    lines.append("=" * 62)
    for c in checks:
        icon = "PASS" if c.ok else ("FAIL" if c.required else "warn")
        line = f"[{icon}] {c.name}"
        if not c.ok and c.detail:
            line += f"  -> {c.detail}"
        lines.append(line)

    total = len(checks)
    passed = len([c for c in checks if c.ok])
    lines.append("-" * 62)
    lines.append(f"passed {passed}/{total} | required failures: {len(required_fail)} | warnings: {len(optional_fail)}")
    if optional_fail:
        lines.append("warnings (recommended, not blocking): " + ", ".join(c.name for c in optional_fail))
    lines.append("=" * 62)
    # In JSON mode the report is still produced, but it goes to stderr so
    # stdout carries nothing but the JSON payload.
    emit(lines, payload, json_mode)

    return 1 if required_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
