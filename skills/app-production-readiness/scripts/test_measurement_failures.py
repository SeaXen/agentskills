"""A failed measurement must never be reported as an app defect.

The rule this file locks down:

    If a gate could not MEASURE something, the verdict is UNSUPPORTED
    (or SKIPPED). It is never CONTRADICTED.

A Lighthouse run that crashed because npm held a lock is not a slow app.
A load test where every request failed because the server was gone is not
a 100 % error rate. A business-rule scenario that could not connect is
not a broken business rule.

These tests cover the four places where that rule was broken, plus the
orchestrator bug where the server was stopped before the gates were judged.
"""

import json
import os
import socket
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import verify_claims  # noqa: E402


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _closed_port() -> int:
    """A port that nothing is listening on (bind then release)."""
    port = _free_port()
    return port


def _run(script: str, args, cwd: Path):
    cmd = [sys.executable, str(SCRIPTS / script)] + [str(a) for a in args]
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True,
                          timeout=600)
    return proc


def _write_lighthouse_summary(root: Path, results: dict, thresholds=None,
                              status="ok") -> Path:
    out = root / "qa" / "lighthouse"
    out.mkdir(parents=True, exist_ok=True)
    payload = {
        "tool": "lighthouse",
        "status": status,
        "results": results,
        "failures": [],
        "errors": [],
        "thresholds": thresholds or {"performance": 90, "accessibility": 95,
                                     "best-practices": 95, "seo": 90},
    }
    p = out / "lighthouse-summary.json"
    p.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return p


# --------------------------------------------------------------------------
# Gate D - a Lighthouse run that errored is not a score of 0
# --------------------------------------------------------------------------

def test_verify_d_treats_an_errored_route_as_unsupported(tmp_path):
    _write_lighthouse_summary(tmp_path, {
        "/": {"error": "npm error code ECOMPROMISED / npm error Lock compromised"},
    })
    verdict, evidence = verify_claims.verify_D(tmp_path, {})
    assert verdict == verify_claims.UNSUPPORTED
    assert "could not be measured" in evidence
    assert "ECOMPROMISED" in evidence


def test_verify_d_treats_a_route_without_scores_as_unsupported(tmp_path):
    _write_lighthouse_summary(tmp_path, {"/": {}})
    verdict, evidence = verify_claims.verify_D(tmp_path, {})
    assert verdict == verify_claims.UNSUPPORTED
    assert "no scores were recorded" in evidence


def test_verify_d_contradicts_a_real_low_score(tmp_path):
    _write_lighthouse_summary(tmp_path, {
        "/": {"scores": {"performance": 50, "accessibility": 96,
                         "best-practices": 96, "seo": 100}},
    })
    verdict, evidence = verify_claims.verify_D(tmp_path, {})
    assert verdict == verify_claims.CONTRADICTED
    assert "performance 50 < 90" in evidence


def test_verify_d_verifies_when_every_route_meets_the_thresholds(tmp_path):
    _write_lighthouse_summary(tmp_path, {
        "/": {"scores": {"performance": 100, "accessibility": 100,
                         "best-practices": 100, "seo": 100}},
        "/pricing": {"scores": {"performance": 99, "accessibility": 100,
                                "best-practices": 100, "seo": 100}},
    })
    verdict, evidence = verify_claims.verify_D(tmp_path, {})
    assert verdict == verify_claims.VERIFIED
    assert "2 route(s)" in evidence


def test_verify_d_is_unsupported_when_lighthouse_never_ran(tmp_path):
    _write_lighthouse_summary(tmp_path, {}, status="skipped")
    verdict, evidence = verify_claims.verify_D(tmp_path, {})
    assert verdict == verify_claims.UNSUPPORTED
    assert "did not run" in evidence


# --------------------------------------------------------------------------
# Gate O - an unreachable app means "not measured", not "100 % errors"
# --------------------------------------------------------------------------

def test_load_check_skips_when_the_app_is_unreachable(tmp_path):
    (tmp_path / "package.json").write_text(
        json.dumps({"name": "unreachable-app", "version": "1.0.0"}), encoding="utf-8")
    port = _closed_port()
    proc = _run("load_check.py", [
        "--root", tmp_path,
        "--url", f"http://127.0.0.1:{port}",
        "--routes", "/",
        "--duration", "2",
        "--workers", "2",
    ], tmp_path)
    assert proc.returncode == 2, proc.stdout + proc.stderr
    data = json.loads((tmp_path / "qa" / "load.json").read_text(encoding="utf-8"))
    assert data.get("unreachable") is True
    # the p95 / error-rate checks must not have been produced at all
    names = " ".join(c.get("name", "") for c in data.get("checks", []))
    assert "p95" not in names
    assert "error rate" not in names


def test_load_check_does_not_skip_a_reachable_but_slow_app(tmp_path):
    """A reachable app that is slow is a real finding, not a skip."""
    import threading
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    class H(BaseHTTPRequestHandler):
        def do_GET(self):
            import time
            time.sleep(0.4)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")

        def log_message(self, *a):
            pass

    port = _free_port()
    srv = ThreadingHTTPServer(("127.0.0.1", port), H)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    try:
        (tmp_path / "package.json").write_text(
            json.dumps({"name": "slow-app", "version": "1.0.0"}), encoding="utf-8")
        proc = _run("load_check.py", [
            "--root", tmp_path,
            "--url", f"http://127.0.0.1:{port}",
            "--routes", "/",
            "--duration", "2",
            "--workers", "2",
            "--p95", "100",
        ], tmp_path)
        data = json.loads((tmp_path / "qa" / "load.json").read_text(encoding="utf-8"))
        assert data.get("unreachable") is False
        assert proc.returncode == 1, proc.stdout + proc.stderr
    finally:
        srv.shutdown()


# --------------------------------------------------------------------------
# Gate N - an unreachable app means "no executable contract to verify"
# --------------------------------------------------------------------------

def test_business_logic_check_reports_the_contract_as_unavailable(tmp_path):
    (tmp_path / "package.json").write_text(
        json.dumps({"name": "unreachable-app", "version": "1.0.0"}), encoding="utf-8")
    (tmp_path / "server.js").write_text("console.log('x');\n", encoding="utf-8")
    (tmp_path / "qa").mkdir(exist_ok=True)
    (tmp_path / "qa" / "scenarios.json").write_text(json.dumps({
        "scenarios": [{"name": "home", "method": "GET", "path": "/",
                       "expect_status": 200}],
    }), encoding="utf-8")
    port = _closed_port()
    proc = _run("business_logic_check.py", [
        "--root", tmp_path,
        "--url", f"http://127.0.0.1:{port}",
        "--json",
    ], tmp_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    data = json.loads(proc.stdout)
    assert data.get("verdict") == "executable-contract-unavailable"
    # no scenario may be reported as a failed assertion
    for sc in data.get("scenarios", []):
        assert sc.get("status") != 0 or sc.get("ok") is not False, sc


def test_verify_n_reports_an_unavailable_contract_as_unsupported(tmp_path):
    (tmp_path / "package.json").write_text(
        json.dumps({"name": "unreachable-app", "version": "1.0.0"}), encoding="utf-8")
    (tmp_path / "server.js").write_text("console.log('x');\n", encoding="utf-8")
    (tmp_path / "qa").mkdir(exist_ok=True)
    (tmp_path / "qa" / "scenarios.json").write_text(json.dumps({
        "scenarios": [{"name": "home", "method": "GET", "path": "/",
                       "expect_status": 200}],
    }), encoding="utf-8")
    port = _closed_port()
    ctx = {"url": f"http://127.0.0.1:{port}", "routes": ["/"],
           "use_scope": False, "skip_tests": True, "test_timeout": 60}
    verdict, evidence = verify_claims.verify_N(tmp_path, ctx)
    assert verdict == verify_claims.UNSUPPORTED
    assert "status 0" not in evidence


# --------------------------------------------------------------------------
# the orchestrator must keep the server up while it judges
# --------------------------------------------------------------------------

def test_the_orchestrator_keeps_the_server_up_while_judging(tmp_path):
    """The business-rule scenarios must run against a LIVE server.

    Regression: review.py used to stop the --serve handle at the end of
    measure(), so the scenarios in judge() all got "status 0" and the gate
    was reported as CONTRADICTED.
    """
    app = tmp_path / "app"
    app.mkdir()
    (app / "package.json").write_text(json.dumps({
        "name": "tiny-app",
        "version": "1.0.0",
        "scripts": {"start": "node server.js"},
    }), encoding="utf-8")
    (app / "server.js").write_text(
        "const http=require('http');\n"
        "const port=process.env.PORT||3000;\n"
        "http.createServer((req,res)=>{"
        "res.writeHead(200,{'Content-Type':'application/json'});"
        "res.end(JSON.stringify({ok:true,path:req.url}));"
        "}).listen(port,'127.0.0.1');\n",
        encoding="utf-8")
    (app / "qa").mkdir()
    (app / "qa" / "scenarios.json").write_text(json.dumps({
        "scenarios": [{"name": "home", "method": "GET", "path": "/",
                       "expect_status": 200, "expect_json": {"ok": True}}],
    }), encoding="utf-8")
    (app / "README.md").write_text("# tiny-app\n\nA tiny app.\n", encoding="utf-8")

    proc = _run("review.py", [
        "--root", app,
        "--serve",
        "--gates", "N",
        "--skip-tests",
    ], app)
    assert proc.returncode in (0, 1), proc.stdout + proc.stderr
    summary = json.loads((app / "qa" / "summary.json").read_text(encoding="utf-8"))
    gates = {g["gate"]: g for g in summary.get("gates", [])}
    assert "N" in gates, summary
    n = gates["N"]
    assert n["verdict"] != verify_claims.CONTRADICTED, n
    assert "status 0" not in json.dumps(n)
    # the machine half must actually have been measured against the live server
    assert n["verdict"] in (verify_claims.VERIFIED, verify_claims.UNVERIFIABLE), n


def test_the_orchestrator_never_reports_a_measurement_failure_as_a_defect(tmp_path):
    """No gate may be CONTRADICTED because a measurement could not be taken."""
    app = tmp_path / "app"
    app.mkdir()
    (app / "package.json").write_text(json.dumps({
        "name": "tiny-app", "version": "1.0.0",
        "scripts": {"start": "node server.js"},
    }), encoding="utf-8")
    (app / "server.js").write_text(
        "const http=require('http');\n"
        "const port=process.env.PORT||3000;\n"
        "http.createServer((req,res)=>{"
        "res.writeHead(200,{'Content-Type':'text/html'});"
        "res.end('<html lang=\"en\"><head><title>t</title></head>"
        "<body><h1>t</h1></body></html>');"
        "}).listen(port,'127.0.0.1');\n",
        encoding="utf-8")
    (app / "README.md").write_text("# tiny-app\n\nA tiny app.\n", encoding="utf-8")
    proc = _run("review.py", [
        "--root", app, "--serve", "--gates", "N,D,O", "--skip-tests",
        "--duration", "2",
    ], app)
    summary = json.loads((app / "qa" / "summary.json").read_text(encoding="utf-8"))
    for item in summary.get("gates", []):
        if item["verdict"] == verify_claims.CONTRADICTED:
            ev = (item.get("evidence") or "").lower()
            assert "could not be measured" not in ev, item
            assert "not reachable" not in ev, item
            assert "status 0" not in ev, item
            assert "no scores" not in ev, item
