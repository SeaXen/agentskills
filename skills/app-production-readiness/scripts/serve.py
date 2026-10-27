#!/usr/bin/env python3
"""Start the app under review so the live gates can run on their own.

Why this exists
---------------
Half of the gates (``runtime_check``, ``a11y_audit``, ``lighthouse_run``,
``capture_screenshots``, ``load_check``) need a *running* app.  Until now the
operator had to start it by hand, which meant the review silently could not
complete when the app was already broken - exactly the case where you most
want evidence.

This module boots the app the way the platform would (``package.json``
``start``), falls back to the dev server when there is no production build,
and reports honestly which mode it used:

* ``dev_mode=True``  - the production build is missing or broken, so the dev
  server was used.  Every measurement taken against it is a *dev* measurement
  and is labelled as such.
* ``dev_mode=False`` - the production start command was used.

The server is stopped again when the caller leaves the context manager, so a
review never leaves stray processes behind.

Exit codes (CLI):

* ``0`` - the app answered on the URL that was printed
* ``1`` - the app did not start or did not answer
* ``2`` - nothing could be started (no start command at all)
"""
from __future__ import annotations

import os
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from qa_common import emit, load_json, parse_cli, resolve_root, root_error  # noqa: E402

try:  # optional
    import framework_profiles  # noqa: E402
except Exception:  # pragma: no cover
    framework_profiles = None


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def free_port() -> int:
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
    started = time.perf_counter()
    while time.perf_counter() - started < timeout:
        if port_open(host, port, 0.5):
            return time.perf_counter() - started
        time.sleep(0.25)
    return timeout


def kill_tree(proc: subprocess.Popen) -> None:
    if proc is None or proc.poll() is not None:
        return
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                           capture_output=True, timeout=20)
        else:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    except Exception:
        try:
            proc.terminate()
        except Exception:
            pass


# --------------------------------------------------------------------------
# how to start the app
# --------------------------------------------------------------------------

def _pkg_manager(root: Path) -> str:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    if (root / "bun.lockb").exists() or (root / "bun.lock").exists():
        return "bun"
    return "npm"


def detect_commands(root: Path) -> dict:
    """Find the production start command and the dev command."""
    root = Path(root)
    data = load_json(root / "package.json")
    scripts = {}
    if isinstance(data, dict):
        scripts = data.get("scripts") or {}
    pkg = _pkg_manager(root)
    out = {"pkg": pkg, "prod": None, "dev": None, "kind": None, "notes": []}

    if scripts.get("start"):
        out["prod"] = f"{pkg} start"
        out["kind"] = "node"
    elif scripts.get("serve"):
        out["prod"] = f"{pkg} run serve"
        out["kind"] = "node"
    if scripts.get("dev"):
        out["dev"] = f"{pkg} run dev"

    procfile = root / "Procfile"
    if procfile.exists() and out["prod"] is None:
        try:
            for line in procfile.read_text(encoding="utf-8", errors="ignore").splitlines():
                if line.lower().startswith("web:"):
                    out["prod"] = line.split(":", 1)[1].strip()
                    out["kind"] = "procfile"
                    break
        except OSError:
            pass

    if out["prod"] is None:
        # python apps
        for name in ("main.py", "app.py", "server.py", "manage.py"):
            if (root / name).exists():
                out["prod"] = f"{sys.executable} {name}"
                out["kind"] = "python"
                break
        for name in ("main.ts", "server.ts", "index.ts", "main.js", "server.js", "index.js"):
            if out["prod"] is None and (root / name).exists():
                out["prod"] = f"npx tsx {name}" if name.endswith(".ts") else f"node {name}"
                out["kind"] = "node-file"
                break
    return out


def _with_port(command: str, port: int, kind: str) -> str:
    """Teach a command which port to listen on."""
    if kind in ("node", "procfile", "node-file"):
        # next start / next dev understand -p; append it to the npm call.
        if "next" in command or "dev" in command or "start" in command:
            return f"{command} -- -p {port}"
        return f"{command} --port {port}"
    if kind == "python":
        return f"{command} --port {port}"
    return command


# --------------------------------------------------------------------------
# the server handle
# --------------------------------------------------------------------------

class ServerHandle:
    """A running app.  Use it as a context manager."""

    def __init__(self, proc, url, port, mode, dev_mode, log_path, notes=None):
        self.proc = proc
        self.url = url
        self.port = port
        self.mode = mode
        self.dev_mode = dev_mode
        self.log_path = log_path
        self.notes = list(notes or [])
        self.stopped = False

    def stop(self) -> None:
        if self.stopped:
            return
        self.stopped = True
        kill_tree(self.proc)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.stop()
        return False

    def as_dict(self) -> dict:
        return {
            "url": self.url,
            "port": self.port,
            "mode": self.mode,
            "dev_mode": self.dev_mode,
            "log": self.log_path,
            "notes": self.notes,
        }


def start_server(root, opts=None) -> dict:
    """Start the app.  Returns a dict with a ``handle`` key on success."""
    root = Path(root)
    opts = dict(opts or {})
    commands = detect_commands(root)
    notes = list(commands.get("notes") or [])

    prefer_dev = bool(opts.get("dev"))
    prod_command = commands.get("prod")
    dev_command = commands.get("dev")

    has_build = True
    if framework_profiles is not None:
        has_build = framework_profiles.build_is_real(root)
    elif (root / ".next").exists():
        has_build = (root / ".next" / "BUILD_ID").exists()

    mode = None
    command = None
    dev_mode = False

    if not prefer_dev and prod_command:
        # A production start command only makes sense when a build exists.
        if has_build or not dev_command:
            command = prod_command
            mode = "production"
        else:
            command = dev_command
            mode = "development"
            dev_mode = True
            notes.append("no production build was found - the dev server was used, "
                         "so every measurement is a DEV measurement")
    elif dev_command:
        command = dev_command
        mode = "development"
        dev_mode = True
        notes.append("the dev server was used, so every measurement is a DEV measurement")
    elif prod_command:
        command = prod_command
        mode = "production"

    if not command:
        return {"ok": False, "status": "skipped",
                "error": "no start command was found (no package.json start script, "
                         "no Procfile web: entry, no python entry point)"}

    port = int(opts.get("port") or free_port())
    host = "127.0.0.1"
    url = f"http://{host}:{port}"
    env = dict(os.environ)
    env["PORT"] = str(port)
    env["HOST"] = host
    env.setdefault("BROWSER", "none")
    env["CI"] = "1"

    full = _with_port(command, port, commands.get("kind"))
    log_dir = root / "qa"
    try:
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / "serve.log"
    except OSError:
        log_path = Path("serve.log")

    try:
        handle_f = open(log_path, "w", encoding="utf-8", errors="ignore")
    except OSError:
        handle_f = subprocess.DEVNULL
        log_path = None

    try:
        proc = subprocess.Popen(
            full, cwd=str(root), env=env, shell=True,
            stdout=handle_f, stderr=subprocess.STDOUT,
            creationflags=(subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0),
        )
    except OSError as exc:
        return {"ok": False, "status": "fail", "error": f"could not start the app: {exc}"}

    timeout = float(opts.get("timeout", 120))
    waited = wait_for_port(host, port, timeout)
    if waited >= timeout:
        kill_tree(proc)
        tail = ""
        if log_path:
            try:
                tail = log_path.read_text(encoding="utf-8", errors="ignore")[-3000:]
            except OSError:
                tail = ""
        return {"ok": False, "status": "fail",
                "error": f"the app did not open port {port} within {timeout:.0f}s",
                "command": full, "log": str(log_path) if log_path else "", "log_tail": tail,
                "notes": notes}

    handle = ServerHandle(proc, url, port, mode, dev_mode,
                          str(log_path) if log_path else "", notes)
    return {"ok": True, "status": "ok", "handle": handle,
            "command": full, "boot_seconds": round(waited, 2), "notes": notes}


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root_str, want_json, _ = parse_cli(argv)
    root = resolve_root(root_str)
    err = root_error(root)
    if err:
        print(f"[FAIL] {err}")
        return 1

    opts = {"port": None, "dev": False, "timeout": 120.0, "wait": False}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--port" and i + 1 < len(argv):
            try:
                opts["port"] = int(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--dev":
            opts["dev"] = True
        elif a == "--timeout" and i + 1 < len(argv):
            try:
                opts["timeout"] = float(argv[i + 1])
            except ValueError:
                pass
            i += 1
        elif a == "--wait":
            opts["wait"] = True
        i += 1

    result = start_server(root, opts)
    handle = result.get("handle")
    payload = {
        "status": result.get("status"),
        "url": result.get("url") or (handle.url if handle else None),
        "dev_mode": bool(handle.dev_mode) if handle else None,
        "mode": handle.mode if handle else None,
        "command": result.get("command"),
        "boot_seconds": result.get("boot_seconds"),
        "notes": result.get("notes", []),
        "error": result.get("error", ""),
        "log_tail": result.get("log_tail", ""),
    }
    emit([], payload, want_json)
    if not result.get("ok"):
        return 2 if result.get("status") == "skipped" else 1
    if opts["wait"]:
        print(f"app is running at {handle.url} - press Ctrl+C to stop", file=sys.stderr)
        try:
            while handle.proc.poll() is None:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            handle.stop()
    else:
        handle.stop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
