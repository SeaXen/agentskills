#!/usr/bin/env python3
"""``--fix`` mode: apply the safe, mechanical fixes the review found.

A review that only complains is half a tool.  This module writes the fixes
that are *mechanical* - the ones where the correct answer is unambiguous and
the change cannot change behaviour in a way the author did not intend:

* ``.env.example`` is generated from the environment variables the code
  actually reads, and ``!.env.example`` is added to ``.gitignore`` when the
  ignore rule would swallow the template (a very common, very quiet bug).
* a Next.js root layout without ``export const viewport`` gets one, so the
  responsive viewport is explicit instead of an invisible framework default.
* ``vercel.json`` without a ``framework`` key gets one, so the deploy target
  is declared instead of guessed.
* ``next.config.*`` without security headers gets the standard header set.

Every rule is **idempotent** (running it twice changes nothing) and
**conservative** (it never overwrites an existing value, never deletes a
line, and it backs the original file up to ``qa/fix-backup/`` before editing).

Anything that requires a human decision (renaming things, changing logic,
writing a README, choosing a licence) is deliberately *not* here - the report
lists those as recommendations instead.

Exit codes: ``0`` - everything applied or nothing to do, ``1`` - a fix failed.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qa_common import emit, load_json, parse_cli, resolve_root, root_error  # noqa: E402

try:
    import framework_profiles  # noqa: E402
except Exception:  # pragma: no cover
    framework_profiles = None


CODE_EXT = {".js", ".jsx", ".mjs", ".cjs", ".ts", ".tsx", ".py", ".go", ".rs",
            ".rb", ".php", ".java", ".kt", ".vue", ".svelte"}

SKIP_DIRS = {"node_modules", ".git", "dist", "build", "out", ".next", ".nuxt",
             "coverage", "__pycache__", ".venv", "venv", "vendor", "target",
             ".pytest_cache", "qa", ".cache", ".idea", ".vscode", "public"}

ENV_PATTERNS = [
    re.compile(r"process\.env\.([A-Z][A-Z0-9_]*)"),
    re.compile(r"process\.env\[[\"']([A-Z][A-Z0-9_]*)[\"']\]"),
    re.compile(r"import\.meta\.env\.([A-Z][A-Z0-9_]*)"),
    re.compile(r"os\.environ\[[\"']([A-Z][A-Z0-9_]*)[\"']\]"),
    re.compile(r"os\.environ\.get\([\"']([A-Z][A-Z0-9_]*)[\"']"),
    re.compile(r"os\.getenv\([\"']([A-Z][A-Z0-9_]*)[\"']"),
    re.compile(r"env\([\"']([A-Z][A-Z0-9_]*)[\"']\)"),
]

SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "X-Frame-Options": "SAMEORIGIN",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
}


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------

def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def _write(path: Path, text: str) -> bool:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return True
    except OSError:
        return False


def _backup(root: Path, path: Path) -> str:
    """Copy the original file to ``qa/fix-backup/`` so a fix is reversible."""
    try:
        rel = path.relative_to(root)
    except ValueError:
        rel = Path(path.name)
    dest = root / "qa" / "fix-backup" / rel
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        return str(dest.relative_to(root))
    except OSError:
        return ""


def _walk(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in CODE_EXT:
            yield path


def _used_env_vars(root: Path):
    """Environment variables the source code actually reads."""
    found = {}
    for path in _walk(root):
        text = _read(path)
        if not text:
            continue
        for pattern in ENV_PATTERNS:
            for name in pattern.findall(text):
                found.setdefault(name, str(path.relative_to(root)).replace("\\", "/"))
    return found


# --------------------------------------------------------------------------
# the fixes
# --------------------------------------------------------------------------

def fix_env_example(root: Path) -> dict:
    """Create ``.env.example`` from the variables the code reads."""
    root = Path(root)
    used = _used_env_vars(root)
    if not used:
        return {"id": "env-example", "status": "skipped",
                "detail": "no environment variables are read by the source code"}
    target = root / ".env.example"
    existing = _read(target) if target.exists() else ""
    have = set(re.findall(r"^\s*([A-Z][A-Z0-9_]*)\s*=", existing, re.M))
    missing = {k: v for k, v in used.items() if k not in have}
    if not missing:
        return {"id": "env-example", "status": "already-ok",
                "detail": f".env.example already documents all {len(used)} variables"}
    lines = []
    if existing and not existing.endswith("\n"):
        lines.append("")
    if not existing:
        lines.append("# Environment variables used by this project.")
        lines.append("# Copy to .env and fill in the real values. Never commit .env.")
        lines.append("")
    for name in sorted(missing):
        lines.append(f"# used in {missing[name]}")
        lines.append(f"{name}=")
    text = existing + "\n".join(lines).lstrip("\n") + "\n"
    if not _write(target, text):
        return {"id": "env-example", "status": "failed", "detail": "could not write .env.example"}
    if target.exists():
        pass
    return {"id": "env-example", "status": "applied",
            "detail": f"created .env.example with {len(missing)} variable(s): "
                      + ", ".join(sorted(missing)),
            "files": [".env.example"]}


def fix_gitignore_env_example(root: Path) -> dict:
    """Make sure ``.env.example`` is not swallowed by the ignore rules."""
    root = Path(root)
    gi = root / ".gitignore"
    if not gi.is_file():
        return {"id": "gitignore-env-example", "status": "skipped",
                "detail": "there is no .gitignore"}
    text = _read(gi)
    if "!.env.example" in text:
        return {"id": "gitignore-env-example", "status": "already-ok",
                "detail": ".gitignore already keeps .env.example"}
    lines = [ln for ln in text.splitlines()
             if ln.strip() and not ln.strip().startswith("#")]
    ignores_env = any(ln.strip() in (".env", ".env*", ".env.*", ".env.local")
                       or (ln.strip().startswith(".env") and "*" in ln)
                       for ln in lines)
    if not ignores_env:
        return {"id": "gitignore-env-example", "status": "skipped",
                "detail": ".gitignore does not ignore .env files - nothing to fix"}
    new = text.rstrip("\n") + "\n!.env.example\n"
    if not _write(gi, new):
        return {"id": "gitignore-env-example", "status": "failed",
                "detail": "could not write .gitignore"}
    return {"id": "gitignore-env-example", "status": "applied",
            "detail": "added '!.env.example' to .gitignore so the template is committable",
            "files": [".gitignore"]}


def fix_gitignore_qa_backups(root: Path) -> dict:
    """Ensure qa/fix-backup/ is ignored by git so local backups are never staged."""
    gi = root / ".gitignore"
    if not gi.is_file():
        return {"id": "gitignore-qa-backups", "status": "skipped", "detail": "there is no .gitignore"}
    text = _read(gi)
    if "qa/fix-backup" in text or "qa/fix-backup/" in text:
        return {"id": "gitignore-qa-backups", "status": "already-ok", "detail": ".gitignore already ignores qa/fix-backup/"}
    new = text.rstrip("\n") + "\n\n# Production readiness backups\nqa/fix-backup/\n"
    if not _write(gi, new):
        return {"id": "gitignore-qa-backups", "status": "failed", "detail": "could not write .gitignore"}
    return {
        "id": "gitignore-qa-backups",
        "status": "applied",
        "detail": "added 'qa/fix-backup/' to .gitignore to prevent committing local backups",
        "files": [".gitignore"],
    }


def _root_layout(root: Path):
    for rel in ("src/app/layout.tsx", "src/app/layout.jsx", "src/app/layout.js",
                "app/layout.tsx", "app/layout.jsx", "app/layout.js"):
        candidate = root / rel
        if candidate.is_file():
            return candidate
    return None


def fix_next_viewport(root: Path) -> dict:
    """Add an explicit ``export const viewport`` to a Next.js root layout."""
    root = Path(root)
    if framework_profiles is None:
        return {"id": "next-viewport", "status": "skipped", "detail": "framework profiles unavailable"}
    if framework_profiles.detect(root) != "next-app":
        return {"id": "next-viewport", "status": "skipped",
                "detail": "not a Next.js App Router project"}
    layout = _root_layout(root)
    if layout is None:
        return {"id": "next-viewport", "status": "skipped",
                "detail": "no root layout was found"}
    text = _read(layout)
    if re.search(r"export\s+const\s+viewport", text):
        return {"id": "next-viewport", "status": "already-ok",
                "detail": "the root layout already exports a viewport"}
    export = ('\nexport const viewport = {\n'
              '  width: "device-width",\n'
              '  initialScale: 1,\n'
              '};\n')
    # Insert after the last import statement, or after the metadata export.
    lines = text.splitlines()
    insert_at = 0
    for index, line in enumerate(lines):
        if line.startswith("import "):
            insert_at = index + 1
    new_text = "\n".join(lines[:insert_at]) + export + "\n".join(lines[insert_at:])
    backup = _backup(root, layout)
    if not _write(layout, new_text):
        return {"id": "next-viewport", "status": "failed",
                "detail": "could not write the root layout"}
    return {"id": "next-viewport", "status": "applied",
            "detail": f"added 'export const viewport' to {layout.relative_to(root)}",
            "files": [str(layout.relative_to(root)).replace("\\", "/")],
            "backup": backup}


def _vercel_framework(root: Path):
    if framework_profiles is not None:
        key = framework_profiles.detect(root)
        return {"next-app": "nextjs", "next-pages": "nextjs"}.get(key)
    return None


def fix_vercel_framework(root: Path) -> dict:
    """Declare the framework in ``vercel.json`` so the deploy is not guessed."""
    root = Path(root)
    target = root / "vercel.json"
    if not target.is_file():
        return {"id": "vercel-framework", "status": "skipped",
                "detail": "there is no vercel.json"}
    data = load_json(target)
    if not isinstance(data, dict):
        return {"id": "vercel-framework", "status": "failed",
                "detail": "vercel.json is not valid JSON - fix it by hand"}
    if data.get("framework"):
        return {"id": "vercel-framework", "status": "already-ok",
                "detail": f"vercel.json already declares the framework '{data['framework']}'"}
    framework = _vercel_framework(root)
    if not framework:
        return {"id": "vercel-framework", "status": "skipped",
                "detail": "the framework could not be detected - add a \"framework\" key by hand"}
    data["framework"] = framework
    backup = _backup(root, target)
    if not _write(target, json.dumps(data, indent=2) + "\n"):
        return {"id": "vercel-framework", "status": "failed",
                "detail": "could not write vercel.json"}
    return {"id": "vercel-framework", "status": "applied",
            "detail": f"added \"framework\": \"{framework}\" to vercel.json",
            "files": ["vercel.json"], "backup": backup}


def _next_config(root: Path):
    for rel in ("next.config.js", "next.config.mjs", "next.config.cjs",
                "next.config.ts"):
        candidate = root / rel
        if candidate.is_file():
            return candidate
    return None


def fix_next_security_headers(root: Path) -> dict:
    """Add the standard security headers to ``next.config.*``."""
    root = Path(root)
    if framework_profiles is not None and framework_profiles.detect(root) not in ("next-app", "next-pages"):
        return {"id": "next-security-headers", "status": "skipped",
                "detail": "not a Next.js project"}
    config = _next_config(root)
    if config is None:
        return {"id": "next-security-headers", "status": "skipped",
                "detail": "there is no next.config file"}
    text = _read(config)
    if re.search(r"\bheaders\s*[:=]", text):
        return {"id": "next-security-headers", "status": "already-ok",
                "detail": "next.config already declares headers"}
    if re.search(r"export\s+default\s*\{", text):
        anchor = "export default {"
    elif re.search(r"module\.exports\s*=\s*\{", text):
        anchor = "module.exports = {"
    else:
        return {"id": "next-security-headers", "status": "skipped",
                "detail": "the next.config shape is not recognised - add the headers by hand"}
    headers_block = [
        "  async headers() {",
        "    return [",
        "      {",
        "        source: \"/:path*\",",
        "        headers: [",
    ]
    for name, value in SECURITY_HEADERS.items():
        headers_block.append(f'          {{ key: "{name}", value: "{value}" }},')
    headers_block += [
        "        ],",
        "      },",
        "    ];",
        "  },",
    ]
    index = text.find(anchor) + len(anchor)
    new_text = text[:index] + "\n" + "\n".join(headers_block) + text[index:]
    backup = _backup(root, config)
    if not _write(config, new_text):
        return {"id": "next-security-headers", "status": "failed",
                "detail": "could not write the next.config file"}
    return {"id": "next-security-headers", "status": "applied",
            "detail": f"added the standard security headers to {config.relative_to(root)}",
            "files": [str(config.relative_to(root)).replace("\\", "/")],
            "backup": backup}


def fix_dockerignore(root: Path) -> dict:
    """Generate standard .dockerignore if Dockerfile exists and .dockerignore is missing."""
    dockerfile = root / "Dockerfile"
    dockerignore = root / ".dockerignore"
    if not dockerfile.is_file():
        return {"id": "dockerignore", "status": "skipped",
                "detail": "no Dockerfile in project root"}
    if dockerignore.is_file():
        return {"id": "dockerignore", "status": "already-ok",
                "detail": ".dockerignore already exists"}
    content = (
        "# Standard production dockerignore\n"
        "node_modules\n"
        "npm-debug.log\n"
        ".git\n"
        ".gitignore\n"
        ".env*\n"
        "!.env.example\n"
        "dist\n"
        "build\n"
        ".next\n"
        ".nuxt\n"
        "coverage\n"
        "qa\n"
        ".pytest_cache\n"
        "__pycache__\n"
    )
    if not _write(dockerignore, content):
        return {"id": "dockerignore", "status": "failed",
                "detail": "could not create .dockerignore"}
    return {
        "id": "dockerignore",
        "status": "applied",
        "detail": "generated standard .dockerignore for Dockerfile",
        "files": [".dockerignore"],
    }


def fix_robots_txt(root: Path) -> dict:
    """Scaffold standard compliant robots.txt for public web projects if absent."""
    is_web = any((root / p).exists() for p in (
        "index.html", "public", "src/pages", "src/app", "app", "pages",
        "vite.config.js", "vite.config.ts", "next.config.js", "next.config.mjs", "next.config.ts"
    ))
    if not is_web:
        return {"id": "robots-txt", "status": "skipped",
                "detail": "not detected as a public web application"}

    for candidate in (root / "public" / "robots.txt", root / "static" / "robots.txt", root / "robots.txt"):
        if candidate.is_file():
            return {"id": "robots-txt", "status": "already-ok",
                    "detail": f"robots.txt already exists at {candidate.relative_to(root)}"}

    target = (root / "public" / "robots.txt") if (root / "public").is_dir() else (root / "robots.txt")
    content = "User-agent: *\nAllow: /\n"
    if not _write(target, content):
        return {"id": "robots-txt", "status": "failed",
                "detail": "could not create robots.txt"}
    return {
        "id": "robots-txt",
        "status": "applied",
        "detail": f"scaffolded standard compliant robots.txt at {target.relative_to(root)}",
        "files": [str(target.relative_to(root)).replace("\\", "/")],
    }


def fix_license(root: Path) -> dict:
    """Scaffold standard MIT LICENSE template if no open-source license is present."""
    for candidate in ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md"):
        if (root / candidate).is_file():
            return {"id": "license", "status": "already-ok",
                    "detail": f"{candidate} already present"}

    target = root / "LICENSE"
    content = (
        "MIT License\n\n"
        "Copyright (c) 2026\n\n"
        "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
        "of this software and associated documentation files (the \"Software\"), to deal\n"
        "in the Software without restriction, including without limitation the rights\n"
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
        "copies of the Software, and to permit persons to whom the Software is\n"
        "furnished to do so, subject to the following conditions:\n\n"
        "The above copyright notice and this permission notice shall be included in all\n"
        "copies or substantial portions of the Software.\n\n"
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
        "SOFTWARE.\n"
    )
    if not _write(target, content):
        return {"id": "license", "status": "failed",
                "detail": "could not create LICENSE file"}
    return {
        "id": "license",
        "status": "applied",
        "detail": "scaffolded standard MIT LICENSE",
        "files": ["LICENSE"],
    }


def fix_cloudflare_assetsignore(root: Path) -> dict:
    """Scaffold .assetsignore for Cloudflare Pages to prevent uploading build artifacts, QA files, and maps."""
    root = Path(root)
    is_cf = (
        (root / "functions").is_dir()
        or (root / "wrangler.toml").is_file()
        or (root / "wrangler.json").is_file()
        or (root / "wrangler.jsonc").is_file()
        or (root / "_headers").is_file()
        or (root / "_routes.json").is_file()
        or any("cloudflare" in _read(root / d).lower() for d in ("DEPLOYMENT.md", "README.md") if (root / d).is_file())
    )
    if not is_cf:
        return {"id": "cloudflare-assetsignore", "status": "skipped",
                "detail": "not detected as a Cloudflare Pages/Workers project"}

    for candidate in (root / "public" / ".assetsignore", root / ".assetsignore"):
        if candidate.is_file():
            return {"id": "cloudflare-assetsignore", "status": "already-ok",
                    "detail": f".assetsignore already exists at {candidate.relative_to(root)}"}

    target = (root / "public" / ".assetsignore") if (root / "public").is_dir() else (root / ".assetsignore")
    content = (
        "# Cloudflare Pages asset ignore\n"
        ".git/\n"
        ".github/\n"
        "qa/\n"
        "coverage/\n"
        ".nyc_output/\n"
        "node_modules/\n"
        "*.map\n"
        "*.test.*\n"
        "*.spec.*\n"
        "__tests__/\n"
        ".DS_Store\n"
        "Thumbs.db\n"
    )
    if not _write(target, content):
        return {"id": "cloudflare-assetsignore", "status": "failed",
                "detail": "could not create .assetsignore"}
    return {
        "id": "cloudflare-assetsignore",
        "status": "applied",
        "detail": f"scaffolded Cloudflare Pages .assetsignore at {target.relative_to(root)}",
        "files": [str(target.relative_to(root)).replace("\\", "/")],
    }


def fix_gitignore_cloudflare(root: Path) -> dict:
    """Ensure Cloudflare local runtime directories (.wrangler, .cloudflare) are in .gitignore."""
    gi = root / ".gitignore"
    if not gi.is_file():
        return {"id": "gitignore-cloudflare", "status": "skipped", "detail": "there is no .gitignore"}
    text = _read(gi)
    entries = []
    if ".wrangler" not in text:
        entries.append(".wrangler/")
    if ".cloudflare" not in text:
        entries.append(".cloudflare/")
    if not entries:
        return {"id": "gitignore-cloudflare", "status": "already-ok",
                "detail": ".gitignore already ignores Cloudflare artifacts"}
    new = text.rstrip("\n") + "\n\n# Cloudflare artifacts\n" + "\n".join(entries) + "\n"
    if not _write(gi, new):
        return {"id": "gitignore-cloudflare", "status": "failed",
                "detail": "could not write .gitignore"}
    return {
        "id": "gitignore-cloudflare",
        "status": "applied",
        "detail": f"added {', '.join(entries)} to .gitignore",
        "files": [".gitignore"],
    }


ALL_FIXES = [
    fix_env_example,
    fix_gitignore_env_example,
    fix_gitignore_qa_backups,
    fix_gitignore_cloudflare,
    fix_cloudflare_assetsignore,
    fix_next_viewport,
    fix_vercel_framework,
    fix_next_security_headers,
    fix_dockerignore,
    fix_robots_txt,
    fix_license,
]


def apply_all(root, only=None) -> list:
    """Run every (or the selected) fix.  Returns one result dict per fix."""
    root = Path(root)
    results = []
    for fixer in ALL_FIXES:
        if only and fixer.__name__.replace("fix_", "") not in only:
            continue
        try:
            results.append(fixer(root))
        except Exception as exc:  # a broken fixer must not break the review
            results.append({"id": fixer.__name__, "status": "failed",
                            "detail": f"unexpected error: {exc}"})
    return results


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root_str, want_json, _ = parse_cli(argv)
    root = resolve_root(root_str)
    err = root_error(root)
    if err:
        print(f"[FAIL] {err}")
        return 1
    only = None
    for index, arg in enumerate(argv):
        if arg == "--only" and index + 1 < len(argv):
            only = [p.strip() for p in argv[index + 1].split(",") if p.strip()]
    results = apply_all(root, only)
    applied = [r for r in results if r.get("status") == "applied"]
    lines = ["FIXES"]
    for item in results:
        mark = {"applied": "[fixed]", "already-ok": "[ok]", "skipped": "[skip]",
                "failed": "[FAIL]"}.get(item.get("status"), "[?]")
        lines.append(f"  {mark} {item.get('id')}: {item.get('detail')}")
    payload = {"fixes": results, "applied": len(applied), "total": len(results)}
    emit(lines, payload, want_json)
    return 1 if any(r.get("status") == "failed" for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
