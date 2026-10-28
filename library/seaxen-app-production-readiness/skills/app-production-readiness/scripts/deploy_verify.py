#!/usr/bin/env python3
"""Verify that the deployment targets this app claims are actually wired up.

The "portable to Vercel/Netlify/Railway/Render/Fly/Cloudflare" claim used
to be checked by the mere PRESENCE of a config file. This script parses
those configs and verifies the fields that decide whether a deploy works:
build command, output directory, start command, PORT handling, health
check path, non-root container user.

Usage:
  python deploy_verify.py [project_root] [--json] [--build]

  --build   additionally run `docker build` when Docker is available
            (otherwise the build step is reported as SKIPPED, not PASS)

Exit 0: every present platform config is valid | Exit 1: a config is invalid
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_common import (
    emit,
    load_json,
    parse_cli,
    resolve_root,
    root_error,
    run_cmd,
    which,
)

SKIP = {"node_modules", ".git", "dist", "build", "out", "coverage", ".next",
        ".venv", "venv", "target", "__pycache__"}


def _read(path: Path, limit=200_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except OSError:
        return ""


class Result:
    def __init__(self):
        self.checks = []

    def add(self, platform, name, ok, detail="", required=True):
        self.checks.append({"platform": platform, "name": name, "ok": bool(ok),
                            "required": required, "detail": detail})

    @property
    def failures(self):
        return [c for c in self.checks if c["required"] and not c["ok"]]


def check_docker(root: Path, res: Result):
    df = root / "Dockerfile"
    if not df.is_file():
        res.add("docker", "Dockerfile present", False, "no Dockerfile", required=False)
        return
    res.add("docker", "Dockerfile present", True)
    txt = _read(df)

    has_cmd = bool(re.search(r"^\s*(CMD|ENTRYPOINT)\s+", txt, re.M | re.I))
    res.add("docker", "container has CMD/ENTRYPOINT", has_cmd,
            "" if has_cmd else "image would have no runnable process")

    expose = re.search(r"^\s*EXPOSE\s+(\d{2,5})", txt, re.M | re.I)
    res.add("docker", "EXPOSE declared", bool(expose),
            expose.group(1) if expose else "no EXPOSE - platform cannot route traffic")

    users = re.findall(r"^\s*USER\s+(\S+)", txt, re.M | re.I)
    last_user = users[-1] if users else ""
    non_root = bool(last_user) and last_user.lower() not in ("root", "0", "")
    res.add("docker", "runs as non-root USER", non_root,
            f"USER {last_user}" if last_user else "no USER instruction - container runs as root",
            required=False)

    health = bool(re.search(r"^\s*HEALTHCHECK\s+", txt, re.M | re.I))
    res.add("docker", "HEALTHCHECK declared", health,
            "no HEALTHCHECK - orchestrators cannot detect a broken container", required=False)

    stages = len(re.findall(r"^\s*FROM\s+", txt, re.M | re.I))
    res.add("docker", "multi-stage build", stages >= 2,
            f"{stages} stage(s) - multi-stage keeps the final image small", required=False)

    port_env = bool(re.search(r"\$\{?PORT\}?", txt)) or bool(re.search(r"process\.env\.PORT", txt))
    res.add("docker", "honours $PORT", port_env,
            "container must bind $PORT, not a hardcoded port", required=False)

    res.add("docker", ".dockerignore present", (root / ".dockerignore").is_file(),
            ".dockerignore keeps the build context small", required=False)


def check_vercel(root: Path, res: Result):
    f = root / "vercel.json"
    if not f.is_file():
        res.add("vercel", "vercel.json present", False, "not configured", required=False)
        return
    res.add("vercel", "vercel.json present", True)
    data = load_json(f)
    if data is None:
        res.add("vercel", "vercel.json is valid JSON", False, "parse error")
        return
    res.add("vercel", "vercel.json is valid JSON", True)
    has_build = any(k in data for k in ("builds", "buildCommand", "outputDirectory",
                                        "functions", "framework", "rewrites"))
    res.add("vercel", "declares build/output/framework", has_build,
            "vercel.json needs at least one of builds/buildCommand/outputDirectory/framework")
    if "outputDirectory" in data:
        out = str(data["outputDirectory"])
        res.add("vercel", "outputDirectory exists", (root / out).is_dir(),
                f"{out} not found in the repo", required=False)


def check_netlify(root: Path, res: Result):
    f = root / "netlify.toml"
    if not f.is_file():
        res.add("netlify", "netlify.toml present", False, "not configured", required=False)
        return
    res.add("netlify", "netlify.toml present", True)
    txt = _read(f)
    try:
        import tomllib
        data = tomllib.loads(txt)
    except Exception as exc:
        res.add("netlify", "netlify.toml is valid TOML", False, str(exc)[:120])
        return
    res.add("netlify", "netlify.toml is valid TOML", True)
    build = (data.get("build") or {}) if isinstance(data.get("build"), dict) else {}
    cmd = build.get("command")
    publish = build.get("publish")
    res.add("netlify", "build command declared", bool(cmd),
            "netlify.toml [build] command is required")
    if publish:
        res.add("netlify", "publish directory exists", (root / str(publish)).is_dir(),
                f"{publish} not found", required=False)


def check_fly(root: Path, res: Result):
    f = root / "fly.toml"
    if not f.is_file():
        res.add("fly", "fly.toml present", False, "not configured", required=False)
        return
    res.add("fly", "fly.toml present", True)
    txt = _read(f)
    try:
        import tomllib
        data = tomllib.loads(txt)
    except Exception as exc:
        res.add("fly", "fly.toml is valid TOML", False, str(exc)[:120])
        return
    res.add("fly", "fly.toml is valid TOML", True)
    res.add("fly", "app name declared", bool(data.get("app")),
            "fly.toml needs [app] name to deploy")
    http = data.get("http_service") or {}
    res.add("fly", "http_service section present", bool(http),
            "fly.toml needs [http_service] to expose the port")
    # internal_port may live at the top level or inside [http_service]
    internal_port = data.get("internal_port") or http.get("internal_port")
    res.add("fly", "internal_port declared", bool(internal_port),
            "fly.toml needs internal_port so the platform can route")
    if http:
        checks = http.get("http_checks") or []
        res.add("fly", "health check configured", bool(checks),
                "no [http_service.http_checks] - deploys roll out without verification", required=False)


def check_render(root: Path, res: Result):
    f = root / "render.yaml"
    if not f.is_file():
        res.add("render", "render.yaml present", False, "not configured", required=False)
        return
    res.add("render", "render.yaml present", True)
    try:
        import yaml  # optional dependency
        data = yaml.safe_load(_read(f))
    except ImportError:
        res.add("render", "render.yaml parseable", False,
                "PyYAML not installed - install pyyaml to validate render.yaml", required=False)
        return
    except Exception as exc:
        res.add("render", "render.yaml parseable", False, str(exc)[:120])
        return
    res.add("render", "render.yaml parseable", True)
    services = (data or {}).get("services") or []
    res.add("render", "service defined", bool(services), "render.yaml needs services:[]")
    for svc in services:
        name = svc.get("name", "service")
        res.add("render", f"{name}: build/start command",
                bool(svc.get("buildCommand") or svc.get("runtime")),
                "a service needs buildCommand+startCommand or a runtime")
        res.add("render", f"{name}: health check path",
                bool(svc.get("healthCheckPath")), "no healthCheckPath", required=False)


def check_cloudflare(root: Path, res: Result):
    f = None
    for name in ("wrangler.toml", "wrangler.json", "wrangler.jsonc"):
        if (root / name).is_file():
            f = root / name
            break
    if f is None:
        res.add("cloudflare", "wrangler config present", False, "not configured", required=False)
        return
    res.add("cloudflare", "wrangler config present", True, f.name)
    txt = _read(f)
    if f.suffix == ".json":
        data = load_json(f)
        if data is None:
            res.add("cloudflare", "wrangler config is valid JSON", False, "parse error")
            return
        res.add("cloudflare", "wrangler config is valid JSON", True)
        res.add("cloudflare", "name declared", bool(data.get("name")), "wrangler needs a name")
        res.add("cloudflare", "entrypoint declared",
                bool(data.get("main") or data.get("main_module") or data.get("assets")),
                "wrangler needs main/assets")
        res.add("cloudflare", "compatibility_date set", bool(data.get("compatibility_date")),
                "compatibility_date pins the runtime version", required=False)
        return
    try:
        import tomllib
        data = tomllib.loads(txt)
    except Exception as exc:
        res.add("cloudflare", "wrangler.toml is valid TOML", False, str(exc)[:120])
        return
    res.add("cloudflare", "wrangler.toml is valid TOML", True)
    res.add("cloudflare", "name declared", bool(data.get("name")), "wrangler.toml needs name")
    res.add("cloudflare", "entrypoint declared",
            bool(data.get("main") or data.get("main_module") or data.get("site")),
            "wrangler.toml needs main (Workers) or site (Pages)")
    res.add("cloudflare", "compatibility_date set", bool(data.get("compatibility_date")),
            "compatibility_date pins the runtime version", required=False)
    if data.get("pages_build_output_dir"):
        res.add("cloudflare", "pages build output exists",
                (root / str(data["pages_build_output_dir"])).is_dir(),
                data["pages_build_output_dir"], required=False)


def check_railway_procfile(root: Path, res: Result):
    proc = root / "Procfile"
    if proc.is_file():
        res.add("railway", "Procfile present", True)
        txt = _read(proc)
        res.add("railway", "Procfile declares a web process",
                bool(re.search(r"^web:", txt, re.M)), "no 'web:' line - the platform will not route")
    else:
        res.add("railway", "Procfile present", False, "not configured", required=False)
    for name in ("railway.json", "railway.toml"):
        f = root / name
        if f.is_file():
            res.add("railway", f"{name} present", True)
            if name.endswith(".json") and load_json(f) is None:
                res.add("railway", f"{name} is valid JSON", False, "parse error")


def check_port_honouring(root: Path, res: Result):
    """The start script must not hardcode a port."""
    pkg = load_json(root / "package.json")
    if not isinstance(pkg, dict):
        return
    scripts = pkg.get("scripts") or {}
    bad = []
    for name, cmd in scripts.items():
        cmd = str(cmd)
        if name != "start" and "start" not in name:
            continue
        for m in re.finditer(r"(?:--port[= ]|-p\s*|PORT=)(\d{2,5})", cmd):
            bad.append(f"{name}: {m.group(0)}")
    res.add("runtime", "start script does not hardcode a port", not bad,
            ", ".join(bad) if bad else "")


def docker_build(root: Path, res: Result):
    """Optional real container build."""
    if not which("docker"):
        res.add("docker", "docker build", False,
                "SKIPPED - docker is not installed; container build unverified", required=False)
        return
    rc, out, err = run_cmd(["docker", "build", "-t", "app-production-readiness:verify", "."],
                            cwd=root, timeout=900)
    res.add("docker", "docker build", rc == 0,
            (err or out).strip().splitlines()[-1][:200] if rc != 0 else "image built",
            required=False)


def verify(root: Path, do_build: bool = False) -> dict:
    res = Result()
    check_docker(root, res)
    check_vercel(root, res)
    check_netlify(root, res)
    check_fly(root, res)
    check_render(root, res)
    check_cloudflare(root, res)
    check_railway_procfile(root, res)
    check_port_honouring(root, res)
    if do_build:
        docker_build(root, res)
    return {
        "root": str(root),
        "checks": res.checks,
        "platforms": sorted({c["platform"] for c in res.checks}),
        "status": "fail" if res.failures else "ok",
        "blocking": len(res.failures),
    }


def main() -> int:
    args = sys.argv[1:]
    root_arg, json_mode, want_help = parse_cli(args)
    do_build = "--build" in args
    if want_help:
        print(__doc__)
        return 0
    root = resolve_root(root_arg)
    err = root_error(root)
    if err:
        payload = {"error": err, "status": "failed", "checks": []}
        if json_mode:
            emit([f"[FAIL] {err}"], payload, True)
        else:
            print(f"[FAIL] {err}", file=sys.stderr)
        return 1

    report = verify(root, do_build)
    lines = ["=" * 62, "DEPLOY TARGET VERIFICATION", "=" * 62]
    current = None
    for c in report["checks"]:
        if c["platform"] != current:
            current = c["platform"]
            lines.append(f"-- {current} --")
        icon = "PASS" if c["ok"] else ("FAIL" if c["required"] else "warn")
        lines.append(f"[{icon}] {c['name']}" + (f"  -> {c['detail']}" if not c["ok"] and c["detail"] else ""))
    lines.append("-" * 62)
    lines.append(f"blocking failures: {report['blocking']} | platforms seen: {len(report['platforms'])}")
    lines.append("=" * 62)
    emit(lines, report, json_mode)
    return 1 if report["blocking"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
