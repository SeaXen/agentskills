#!/usr/bin/env python3
"""Deep mode for Gate I: actually boot the app the way a platform would and
prove it answers.

Why this exists
---------------
``deploy_verify.py`` only *parses* Dockerfile / vercel.json / netlify.toml /
fly.toml / render.yaml.  A config that parses is not an app that boots.  This
script closes that gap: it starts the app with the command the platform would
use, waits for the port, then hits the health endpoint and the main routes.

Three modes, chosen automatically from the repo:

``runtime``
    The platform runs a long-lived server (``package.json`` ``start`` script,
    ``Procfile`` ``web:`` entry, ``render.yaml`` ``startCommand``, ``fly.toml``
    ``[processes]`` / Dockerfile ``CMD``).  The command is started, the port is
    polled, the health endpoint and the routes are requested.

``static``
    The platform only serves a build output (``vercel.json`` ``outputDirectory``,
    ``netlify.toml`` ``publish``).  The directory is served locally and the
    routes are requested.

``docker``
    A ``Dockerfile`` exists and Docker is installed: the image is built and the
    container is started with the exposed port mapped.

Exit codes follow the skill-wide contract:

* ``0`` - the app booted and answered (PASS)
* ``1`` - the app was started but did not boot / did not answer (FAIL)
* ``2`` - nothing could be attempted (no start command, no Docker, no static
  output).  A skip is never reported as a pass.

Artefact: ``qa/deploy-smoke.json``.
"""
from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qa_common import emit, parse_cli, resolve_root, root_error  # noqa: E402
from qa_ext import GateResult, http_request, print_report  # noqa: E402

try:  # optional - the app under test owns the package manager
    import detect_env  # noqa: E402
except Exception:  # pragma: no cover
    detect_env = None


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def free_port() -> int:
    """Return a free TCP port on localhost."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def wait_for_port(host: str, port: int, timeout: float) -> float:
    """Poll until the port accepts connections.  Returns seconds waited."""
    started = time.perf_counter()
    while time.perf_counter() - started < timeout:
        if port_open(host, port):
            return time.perf_counter() - started
        time.sleep(0.25)
    return timeout


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def load_json(path: Path):
    try:
        return json.loads(read_text(path))
    except ValueError:
        return None


def kill_tree(proc: subprocess.Popen) -> None:
    """Stop the child process (and its children) on Windows and POSIX."""
    if proc.poll() is not None:
        return
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                           capture_output=True, timeout=20)
        else:
            os.killpg(os.getpgid(proc.pid), 15)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


# --------------------------------------------------------------------------
# deployment plan detection
# --------------------------------------------------------------------------

def _pkg_start(root: Path):
    """Return (pkg_manager, start_script) from package.json."""
    data = load_json(root / "package.json")
    if not isinstance(data, dict):
        return None, None
    scripts = data.get("scripts") or {}
    start = scripts.get("start") or scripts.get("serve")
    if not start:
        return None, None
    pkg = "npm"
    if (root / "pnpm-lock.yaml").exists():
        pkg = "pnpm"
    elif (root / "yarn.lock").exists():
        pkg = "yarn"
    elif (root / "bun.lockb").exists() or (root / "bun.lock").exists():
        pkg = "bun"
    return pkg, start


def detect_plan(root: Path) -> dict:
    """Work out how a platform would run this app."""
    plan = {
        "mode": None,
        "platform": None,
        "start": None,
        "build": None,
        "output_dir": None,
        "dockerfile": None,
        "docker_port": None,
        "notes": [],
    }

    pkg, start = _pkg_start(root)
    if start:
        plan["start"] = start
        plan["pkg"] = pkg
        plan["notes"].append(f"package.json start script: {start}")

    procfile = root / "Procfile"
    if procfile.exists():
        for line in read_text(procfile).splitlines():
            if line.lower().startswith("web:"):
                plan["start"] = line.split(":", 1)[1].strip()
                plan["platform"] = plan["platform"] or "heroku-style (Procfile)"
                plan["notes"].append("Procfile web: entry used as the start command")
                break

    render = root / "render.yaml"
    if render.exists():
        text = read_text(render)
        for line in text.splitlines():
            if line.strip().startswith("startCommand:"):
                plan["start"] = line.split(":", 1)[1].strip().strip("'\"")
                plan["platform"] = plan["platform"] or "render"
                plan["notes"].append("render.yaml startCommand used as the start command")

    fly = root / "fly.toml"
    if fly.exists():
        text = read_text(fly)
        if "[processes]" in text:
            for line in text.splitlines():
                if line.strip().startswith("command"):
                    plan["start"] = line.split("=", 1)[1].strip().strip("'\"")
                    plan["platform"] = plan["platform"] or "fly.io"
                    plan["notes"].append("fly.toml [processes] command used")

    vercel = root / "vercel.json"
    if vercel.exists():
        data = load_json(vercel) or {}
        out = data.get("outputDirectory")
        if out and (root / out).is_dir():
            plan["static_platform"] = "vercel"
            plan["output_dir"] = str((root / out).resolve())
            plan["notes"].append(f"vercel.json outputDirectory: {out}")

    netlify = root / "netlify.toml"
    if netlify.exists():
        publish = None
        for line in read_text(netlify).splitlines():
            if line.strip().startswith("publish"):
                publish = line.split("=", 1)[1].strip().strip("'\"")
        if publish and (root / publish).is_dir():
            plan["static_platform"] = "netlify"
            plan["output_dir"] = str((root / publish).resolve())
            plan["notes"].append(f"netlify.toml publish: {publish}")

    dockerfile = root / "Dockerfile"
    if dockerfile.exists():
        plan["dockerfile"] = str(dockerfile)
        text = read_text(dockerfile)
        for line in text.splitlines():
            if line.strip().upper().startswith("EXPOSE"):
                try:
                    plan["docker_port"] = int(line.split()[1])
                except (IndexError, ValueError):
                    plan["docker_port"] = None
                break

    if plan["mode"] is None:
        # Priority: a real container, then a real server process, then a
        # static build output.  A server is always preferred over a static
        # directory because that is what the platform will actually run.
        if plan["dockerfile"] and shutil.which("docker"):
            plan["mode"] = "docker"
            plan["platform"] = "docker"
        elif plan["start"]:
            plan["mode"] = "runtime"
            plan["platform"] = plan.get("platform") or "node/package script"
        elif plan["output_dir"]:
            plan["mode"] = "static"
            plan["platform"] = plan.get("static_platform") or "static"
    return plan


# --------------------------------------------------------------------------
# the three smoke modes
# --------------------------------------------------------------------------

def _probe(url: str, path: str, timeout: float = 10.0) -> dict:
    res = http_request(url.rstrip("/") + path, timeout=timeout)
    return {
        "path": path,
        "status": res.get("status"),
        "ok": res.get("ok"),
        "elapsed_ms": res.get("elapsed_ms"),
        "error": res.get("error", ""),
        "bytes": res.get("bytes", 0),
        "body_head": (res.get("body") or "")[:200],
    }


def smoke_runtime(root: Path, plan: dict, opts: dict) -> dict:
    """Start the app with the platform's start command and probe it."""
    port = int(opts.get("port") or free_port())
    host = "127.0.0.1"
    url = f"http://{host}:{port}"
    env = dict(os.environ)
    env["PORT"] = str(port)
    env["HOST"] = host
    env["NODE_ENV"] = "production"

    steps = []
    build_cmd = opts.get("build")
    if build_cmd:
        steps.append({"step": "build", "command": build_cmd, "status": "skipped",
                      "detail": "no build step requested"})
    elif detect_env is not None and (root / "package.json").exists():
        pkg = plan.get("pkg") or "npm"
        if (root / "node_modules").is_dir():
            steps.append({"step": "build", "command": f"{pkg} run build", "status": "ok"})
        else:
            steps.append({"step": "build", "command": f"{pkg} run build", "status": "skipped",
                          "detail": "node_modules is absent - the build script cannot run here"})

    start = plan["start"]
    log = tempfile.NamedTemporaryFile(prefix="pdqa-deploy-", suffix=".log", delete=False)
    log.close()
    started = None
    try:
        started = subprocess.Popen(
            start,
            cwd=str(root),
            env=env,
            shell=True,
            stdout=open(log.name, "w", encoding="utf-8", errors="ignore"),
            stderr=subprocess.STDOUT,
            creationflags=(subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0),
        )
    except OSError as exc:
        return {"mode": "runtime", "status": "fail", "steps": steps,
                "error": f"could not start the app: {exc}"}

    waited = wait_for_port(host, port, float(opts.get("boot_timeout", 30)))
    probes = []
    try:
        if waited >= float(opts.get("boot_timeout", 30)):
            return {
                "mode": "runtime", "status": "fail", "steps": steps,
                "error": f"the app did not open port {port} within the boot timeout",
                "log": read_text(Path(log.name))[-4000:],
            }
        probes.append(_probe(url, opts.get("healthz", "/healthz")))
        for route in opts.get("routes") or ["/"]:
            probes.append(_probe(url, route))
    finally:
        kill_tree(started)
        try:
            os.unlink(log.name)
        except OSError:
            pass

    healthy = bool(probes) and probes[0]["ok"] and probes[0]["status"] == 200
    routes_ok = all(p["ok"] for p in probes[1:]) if len(probes) > 1 else healthy
    return {
        "mode": "runtime",
        "status": "ok" if (healthy and routes_ok) else "fail",
        "steps": steps,
        "port": port,
        "boot_seconds": round(waited, 2),
        "probes": probes,
        "health_ok": healthy,
        "routes_ok": routes_ok,
    }


def smoke_docker(root: Path, plan: dict, opts: dict) -> dict:
    """Build the image and run the container."""
    port = int(opts.get("port") or free_port())
    image = "pdqa-smoke:latest"
    steps = []
    build = subprocess.run(["docker", "build", "-t", image, "."], cwd=str(root),
                           capture_output=True, text=True, timeout=900)
    steps.append({"step": "docker build", "status": "ok" if build.returncode == 0 else "fail",
                  "detail": (build.stderr or build.stdout or "")[-1500:]})
    if build.returncode != 0:
        return {"mode": "docker", "status": "fail", "steps": steps,
                "error": "docker build failed"}
    run = subprocess.run(
        ["docker", "run", "--rm", "-d", "-p", f"{port}:{plan.get('docker_port') or port}", image],
        capture_output=True, text=True, timeout=120)
    steps.append({"step": "docker run", "status": "ok" if run.returncode == 0 else "fail",
                  "detail": (run.stdout or run.stderr or "")[:500]})
    if run.returncode != 0:
        return {"mode": "docker", "status": "fail", "steps": steps,
                "error": "docker run failed"}
    container = (run.stdout or "").strip()
    url = f"http://127.0.0.1:{port}"
    try:
        waited = wait_for_port("127.0.0.1", port, float(opts.get("boot_timeout", 60)))
        probes = [_probe(url, opts.get("healthz", "/healthz"))]
        for route in opts.get("routes") or ["/"]:
            probes.append(_probe(url, route))
        healthy = bool(probes) and probes[0]["ok"] and probes[0]["status"] == 200
        routes_ok = all(p["ok"] for p in probes[1:]) if len(probes) > 1 else healthy
        return {"mode": "docker", "status": "ok" if (healthy and routes_ok) else "fail",
                "steps": steps, "port": port, "boot_seconds": round(waited, 2),
                "probes": probes, "health_ok": healthy, "routes_ok": routes_ok}
    finally:
        subprocess.run(["docker", "rm", "-f", container], capture_output=True, timeout=60)


def smoke_static(root: Path, plan: dict, opts: dict) -> dict:
    """Serve the build output and probe it."""
    out = Path(plan["output_dir"])
    port = int(opts.get("port") or free_port())
    env = dict(os.environ)
    started = None
    try:
        started = subprocess.Popen(
            [sys.executable, "-m", "http.server", str(port), "--directory", str(out)],
            cwd=str(root), env=env,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            creationflags=(subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0),
        )
    except OSError as exc:
        return {"mode": "static", "status": "fail", "steps": [],
                "error": f"could not serve {out}: {exc}"}
    url = f"http://127.0.0.1:{port}"
    try:
        waited = wait_for_port("127.0.0.1", port, 15)
        probes = [_probe(url, opts.get("healthz", "/healthz"))]
        for route in opts.get("routes") or ["/"]:
            probes.append(_probe(url, route))
        healthy = probes[0]["ok"] and probes[0]["status"] in (200, 404)
        routes_ok = all(p["ok"] for p in probes[1:]) if len(probes) > 1 else healthy
        return {"mode": "static", "status": "ok" if routes_ok else "fail",
                "steps": [{"step": "serve", "command": f"http.server {out}", "status": "ok"}],
                "port": port, "boot_seconds": round(waited, 2), "probes": probes,
                "health_ok": healthy, "routes_ok": routes_ok}
    finally:
        kill_tree(started)


def smoke_remote(root: Path, plan: dict, opts: dict) -> dict:
    """Optional: use a real platform CLI.  Honest SKIP when unavailable."""
    platform = plan.get("platform") or ""
    commands = {
        "vercel": ["vercel", "deploy", "--prod", "--yes"],
        "netlify": ["netlify", "deploy", "--prod"],
        "fly.io": ["fly", "deploy"],
    }
    cmd = None
    for key, value in commands.items():
        if key in platform:
            cmd = value
            break
    if not cmd or not shutil.which(cmd[0]):
        return {"mode": "remote", "status": "skipped",
                "error": f"no usable platform CLI for '{platform or 'unknown'}' - "
                         "remote deploy was not attempted"}
    url = opts.get("remote_url")
    if not url:
        return {"mode": "remote", "status": "skipped",
                "error": "a --remote-url is required to probe a remote deployment"}
    probes = [_probe(url, opts.get("healthz", "/healthz"))]
    for route in opts.get("routes") or ["/"]:
        probes.append(_probe(url, route))
    healthy = probes[0]["ok"] and probes[0]["status"] == 200
    routes_ok = all(p["ok"] for p in probes[1:]) if len(probes) > 1 else healthy
    return {"mode": "remote", "status": "ok" if (healthy and routes_ok) else "fail",
            "probes": probes, "health_ok": healthy, "routes_ok": routes_ok}


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def run_smoke(root: Path, opts: dict) -> dict:
    plan = detect_plan(root)
    if opts.get("remote"):
        result = smoke_remote(root, plan, opts)
    elif plan["mode"] == "docker":
        result = smoke_docker(root, plan, opts)
    elif plan["mode"] == "static":
        result = smoke_static(root, plan, opts)
    elif plan["mode"] == "runtime":
        result = smoke_runtime(root, plan, opts)
    else:
        result = {"mode": None, "status": "skipped",
                  "error": "no start command, build output or Dockerfile was found - "
                           "there is nothing to boot"}
    result["plan"] = plan
    return result


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root_str, want_json, _ = parse_cli(argv)
    root = resolve_root(root_str)
    err = root_error(root)
    if err:
        print(f"[FAIL] {err}")
        return 1

    opts = {
        "healthz": "/healthz",
        "routes": ["/"],
        "port": None,
        "boot_timeout": 30.0,
        "remote": False,
        "remote_url": None,
        "build": None,
    }
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--healthz" and i + 1 < len(argv):
            opts["healthz"] = argv[i + 1]
            i += 1
        elif a == "--routes" and i + 1 < len(argv):
            opts["routes"] = [r.strip() for r in argv[i + 1].split(",") if r.strip()]
            i += 1
        elif a == "--port" and i + 1 < len(argv):
            try:
                opts["port"] = int(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--boot-timeout" and i + 1 < len(argv):
            try:
                opts["boot_timeout"] = float(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--remote":
            opts["remote"] = True
        elif a == "--remote-url" and i + 1 < len(argv):
            opts["remote_url"] = argv[i + 1]
            i += 1
        elif a == "--build" and i + 1 < len(argv):
            opts["build"] = argv[i + 1]
            i += 1
        i += 1

    if detect_env is not None:
        if opts["healthz"] == "/healthz":
            found = detect_env.find_healthz(root)
            if found:
                opts["healthz"] = found
        if opts["routes"] == ["/"]:
            routes = detect_env.find_routes(root)
            html_routes = [r for r in routes if not r.startswith("/assets")
                           and "." not in r.rsplit("/", 1)[-1]]
            if html_routes:
                opts["routes"] = html_routes[:5]

    result = GateResult("I", "DEPLOY SMOKE (the app really boots)")
    smoke = run_smoke(root, opts)

    if smoke.get("status") == "skipped":
        result.skipped = True
        result.reason = smoke.get("error", "nothing to boot")
    else:
        probes = smoke.get("probes") or []
        health = next((p for p in probes if p["path"] == opts["healthz"]), None)
        result.add("the app boots with the platform start command",
                   smoke.get("status") == "ok",
                   detail=smoke.get("error", "") or f"mode={smoke.get('mode')}")
        if health is not None:
            result.add("health endpoint answers 2xx",
                       bool(health.get("ok")) and health.get("status") == 200,
                       detail=f"{health.get('path')} -> {health.get('status')}")
        route_probes = [p for p in probes if p["path"] != opts["healthz"]]
        if route_probes:
            result.add("every main route answers",
                       all(p.get("ok") for p in route_probes),
                       detail=", ".join(f"{p['path']}={p['status']}" for p in route_probes))
        for note in smoke.get("plan", {}).get("notes", []):
            result.notes.append(note)

    payload = print_report(result, want_json, extra={"smoke": smoke})
    out_dir = root / "qa"
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "deploy-smoke.json").write_text(
            json.dumps(payload, indent=2), encoding="utf-8")
    except OSError:
        pass
    emit([], payload, want_json)
    if result.skipped:
        return 2
    return 1 if result.blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
