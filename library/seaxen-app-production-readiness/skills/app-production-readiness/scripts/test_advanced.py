#!/usr/bin/env python3
"""Regression suite for the extended app-production-readiness tooling.

Covers the scripts that back gates A, B, D, E, F, G, H, I, L, M:

  dep_audit      multi-ecosystem CVE audit
  bundle_report  bundle / route-JS budgets
  deploy_verify  real deploy-config validation
  runtime_check  live HTTP, headers, SEO, health, 404
  a11y_audit     axe-core + keyboard pass (needs Playwright)
  lighthouse_run lighthouse report parsing (no browser needed)
  verify_claims  adversarial re-derivation of claimed gate results
  security_scan  the added insecure-code patterns
  qa_common      shared helpers

Everything runs offline against generated fixtures and a local HTTP server.
Run:  python -m pytest scripts/test_advanced.py -q
"""
from __future__ import annotations

import gzip
import json
import shutil
import socket
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
SKILL = SCRIPTS.parent
FIXTURES = SCRIPTS / "fixtures"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(FIXTURES))

import qa_common          # noqa: E402
import dep_audit          # noqa: E402
import bundle_report      # noqa: E402
import deploy_verify      # noqa: E402
import runtime_check      # noqa: E402
import verify_claims      # noqa: E402
import security_scan      # noqa: E402
import make_sample_app    # noqa: E402


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

@pytest.fixture(scope="session")
def good_app(tmp_path_factory):
    """The 'good' sample app (production-ready by construction)."""
    out = tmp_path_factory.mktemp("good-app")
    make_sample_app.build(out, variant="good")
    return out


@pytest.fixture(scope="session")
def broken_app(tmp_path_factory):
    """The 'broken' sample app (secrets, eval(), oversized bundle, bad README)."""
    out = tmp_path_factory.mktemp("broken-app")
    make_sample_app.build(out, variant="broken")
    return out


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


GOOD_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Sample App - production dashboard</title>
<meta name="description" content="Sample App is a small production-ready dashboard used for testing.">
<meta property="og:title" content="Sample App">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="canonical" href="http://127.0.0.1/">
<link rel="stylesheet" href="/assets/app.css">
</head>
<body>
<a href="#main" class="skip-link">Skip to content</a>
<header><nav><a href="/">Home</a></nav></header>
<main id="main">
  <h1>Sample App</h1>
  <img src="/assets/og.png" alt="Sample App dashboard preview">
  <form><label for="q">Search</label><input id="q" name="q"></form>
</main>
<footer><p>2026</p></footer>
</body>
</html>
"""

BAD_HTML = """<!doctype html>
<html>
<head><title>x</title></head>
<body><h1>One</h1><h1>Two</h1><img src="/a.png"></body>
</html>
"""


class LocalServer:
    """A tiny configurable HTTP server used as the 'live app'."""

    def __init__(self, html=GOOD_HTML, secure_headers=True, healthz="/healthz"):
        self.html = html
        self.secure_headers = secure_headers
        self.healthz = healthz
        self.port = _free_port()
        self.httpd = None
        self.thread = None

    # -- routing ---------------------------------------------------------
    def _handler(self):
        server = self

        class Handler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def log_message(self, *args):        # silence the test output
                pass

            def _send(self, status, body: bytes, ctype="text/html; charset=utf-8",
                      extra=None, gzip_it=False):
                if gzip_it:
                    body = gzip.compress(body)
                    self.send_response(status)
                    self.send_header("Content-Type", ctype)
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Content-Encoding", "gzip")
                else:
                    self.send_response(status)
                    self.send_header("Content-Type", ctype)
                    self.send_header("Content-Length", str(len(body)))
                if server.secure_headers:
                    self.send_header("X-Content-Type-Options", "nosniff")
                    self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
                    self.send_header("Content-Security-Policy", "default-src 'self'")
                    self.send_header("X-Frame-Options", "DENY")
                self.send_header("Cache-Control", "public, max-age=60")
                for k, v in (extra or {}).items():
                    self.send_header(k, v)
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                path = self.path.split("?")[0]
                if path == server.healthz:
                    self._send(200, b'{"status":"ok"}', "application/json")
                elif path == "/robots.txt":
                    self._send(200, b"User-agent: *\n", "text/plain")
                elif path == "/sitemap.xml":
                    self._send(200, b"<urlset></urlset>", "application/xml")
                elif path == "/api/qa-cors-probe":
                    self._send(200, b"{}", "application/json")
                elif path in ("/", "/index.html", "/pricing"):
                    body = server.html.encode()
                    want_gzip = "gzip" in (self.headers.get("Accept-Encoding") or "")
                    self._send(200, body, gzip_it=want_gzip)
                else:
                    self._send(404, b"<h1>404</h1>", "text/html; charset=utf-8")

        return Handler

    def __enter__(self):
        self.httpd = ThreadingHTTPServer(("127.0.0.1", self.port), self._handler())
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        return self

    def __exit__(self, *exc):
        self.httpd.shutdown()
        self.httpd.server_close()
        self.thread.join(timeout=5)
        return False

    @property
    def url(self):
        return f"http://127.0.0.1:{self.port}"


# --------------------------------------------------------------------------
# qa_common
# --------------------------------------------------------------------------

def test_run_cmd_reports_missing_executable():
    rc, out, err = qa_common.run_cmd(["definitely-not-a-real-binary-xyz"])
    assert rc == 127
    assert "not" in (out + err).lower() or "no such" in (out + err).lower()


def test_run_cmd_timeout_is_not_an_exception():
    rc, out, err = qa_common.run_cmd(
        [sys.executable, "-c", "import time; time.sleep(5)"], timeout=1)
    assert rc == 124


def test_run_cmd_captures_stdout():
    rc, out, err = qa_common.run_cmd(
        [sys.executable, "-c", "print('hello-qa')"])
    assert rc == 0
    assert "hello-qa" in out


def test_gzip_size_is_smaller_for_compressible_content(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("x" * 5000)
    assert qa_common.gzip_size(p) < qa_common.file_size(p)


def test_find_dist_prefers_dist_then_build(tmp_path):
    assert qa_common.find_dist(tmp_path)[0] is None
    (tmp_path / "build").mkdir()
    assert qa_common.find_dist(tmp_path)[0].name == "build"
    (tmp_path / "dist").mkdir()
    assert qa_common.find_dist(tmp_path)[0].name == "dist"


def test_json_roundtrip(tmp_path):
    p = tmp_path / "x.json"
    assert qa_common.write_json(p, {"a": 1}) is True
    assert qa_common.load_json(p) == {"a": 1}
    assert qa_common.load_json(tmp_path / "missing.json") is None


def test_slugify_is_filesystem_safe():
    assert qa_common.slugify("Pricing / Plans!") == "pricing-plans"
    assert qa_common.slugify("///") == "item"


def test_which_finds_the_running_interpreter():
    assert qa_common.which("python") or qa_common.which("py")


# --------------------------------------------------------------------------
# dep_audit
# --------------------------------------------------------------------------

@pytest.mark.parametrize("lock,name", [
    ("package-lock.json", "node-npm"),
    ("pnpm-lock.yaml", "node-pnpm"),
    ("yarn.lock", "node-yarn"),
    ("bun.lockb", "node-bun"),
])
def test_detect_ecosystem_for_node_package_managers(tmp_path, lock, name):
    (tmp_path / "package.json").write_text('{"name":"x"}')
    (tmp_path / lock).write_text("")
    eco, found = dep_audit.detect_ecosystem(tmp_path)
    assert eco == name
    assert found == lock


def test_detect_ecosystem_for_other_ecosystems(tmp_path):
    (tmp_path / "requirements.txt").write_text("flask")
    assert dep_audit.detect_ecosystem(tmp_path)[0] == "python"
    (tmp_path / "requirements.txt").unlink()
    (tmp_path / "Cargo.toml").write_text("[package]\nname='x'\n")
    assert dep_audit.detect_ecosystem(tmp_path)[0] == "rust"
    (tmp_path / "Cargo.toml").unlink()
    (tmp_path / "go.mod").write_text("module x\n")
    assert dep_audit.detect_ecosystem(tmp_path)[0] == "go"


def test_audit_without_manifest_is_skipped_not_passed(tmp_path):
    report = dep_audit.audit(tmp_path)
    assert report["status"] == "skipped"
    assert report["findings"] == []
    assert "manifest" in (report.get("reason") or "").lower()


def test_severity_threshold_ranking():
    assert dep_audit._at_or_above("critical", "high")
    assert dep_audit._at_or_above("high", "high")
    assert not dep_audit._at_or_above("medium", "high")
    assert dep_audit._at_or_above("moderate", "low")


def test_npm_audit_v2_findings_are_flattened():
    data = {"auditReportVersion": 2,
            "vulnerabilities": {
                "lodash": {"name": "lodash", "severity": "high",
                           "via": [{"title": "Prototype pollution", "severity": "high"}]}}}
    findings = dep_audit._npm_findings(data)
    assert len(findings) == 1
    assert findings[0]["severity"] == "high"
    assert findings[0]["package"] == "lodash"


def test_npm_audit_v1_findings_are_flattened():
    data = {"advisories": {"1234": {"module_name": "minimist",
                                    "severity": "moderate", "title": "ReDoS",
                                    "findings": ["https://example.test/a"]}}}
    findings = dep_audit._npm_findings(data)
    assert len(findings) == 1
    assert findings[0]["package"] == "minimist"


def test_load_json_str_tolerates_noise_around_json():
    assert dep_audit.load_json_str('noise {"a": 1} tail') == {"a": 1}
    assert dep_audit.load_json_str("not json at all") is None


def test_audit_reports_the_detected_ecosystem(good_app):
    report = dep_audit.audit(good_app)
    assert report["ecosystem"].startswith("node")
    assert report["status"] in ("ok", "skipped")


# --------------------------------------------------------------------------
# bundle_report
# --------------------------------------------------------------------------

def test_bundle_report_without_build_is_no_build(tmp_path):
    report = bundle_report.analyse(tmp_path)
    assert report["status"] == "no-build"
    assert any(not c["ok"] for c in report["checks"])


def test_bundle_report_good_app_meets_budgets(good_app):
    report = bundle_report.analyse(good_app)
    assert report["status"] == "ok"
    assert report["route_budget_kb"] <= 200
    assert not [c for c in report["checks"] if c["required"] and not c["ok"]]


def test_bundle_report_flags_oversized_asset(broken_app):
    report = bundle_report.analyse(broken_app)
    assert report["status"] == "fail"
    failed = [c["name"] for c in report["checks"] if c["required"] and not c["ok"]]
    assert failed


def test_bundle_report_ignores_dev_dependencies(good_app):
    report = bundle_report.analyse(good_app)
    assert "vite" not in (report.get("unused_dependencies") or [])


# --------------------------------------------------------------------------
# deploy_verify
# --------------------------------------------------------------------------

def _failed_checks(report):
    return [f"{c['platform']}: {c['name']} ({c['detail']})"
            for c in report["checks"] if c["required"] and not c["ok"]]


def test_deploy_verify_accepts_valid_configs(good_app):
    report = deploy_verify.verify(good_app)
    assert report["status"] == "ok", _failed_checks(report)
    assert not _failed_checks(report)
    assert report["platforms"], report["checks"]


def test_deploy_verify_flags_missing_start_command(tmp_path):
    (tmp_path / "vercel.json").write_text(json.dumps({"version": 2}))
    report = deploy_verify.verify(tmp_path)
    assert report["status"] == "fail"
    assert _failed_checks(report)


def test_deploy_verify_flags_a_dockerfile_without_expose(tmp_path):
    (tmp_path / "Dockerfile").write_text("FROM node:20\nCMD [\"node\", \"server.js\"]\n")
    report = deploy_verify.verify(tmp_path)
    failures = " ".join(_failed_checks(report)).lower()
    assert "expose" in failures
    non_root = [c for c in report["checks"] if c["name"] == "runs as non-root USER"]
    assert non_root and non_root[0]["ok"] is False


def test_fly_internal_port_is_accepted_inside_http_service(tmp_path):
    (tmp_path / "fly.toml").write_text(
        'app = "x"\n\n[http_service]\n  internal_port = 8080\n  auto_stop_machines = "stop"\n')
    report = deploy_verify.verify(tmp_path)
    fly = [f for f in _failed_checks(report) if f.startswith("fly")]
    assert not fly


# --------------------------------------------------------------------------
# runtime_check
# --------------------------------------------------------------------------

def test_runtime_check_passes_a_healthy_app():
    with LocalServer() as srv:
        report = runtime_check.run(srv.url, ["/", "/pricing"], "/healthz", 10)
    assert report["status"] == "ok", report["failures"]
    assert not report["failures"]


def test_runtime_check_flags_missing_seo_and_headers():
    with LocalServer(html=BAD_HTML, secure_headers=False) as srv:
        report = runtime_check.run(srv.url, ["/"], "/healthz", 10)
    assert report["status"] == "fail"
    joined = " ".join(report["failures"]).lower()
    assert "seo:" in joined
    assert "security:" in joined


def test_runtime_check_detects_a_missing_health_endpoint():
    with LocalServer() as srv:
        report = runtime_check.run(srv.url, ["/"], "/no-such-health", 10)
    assert report["status"] == "fail"
    assert any("health endpoint" in f for f in report["failures"])


def test_runtime_check_reports_unreachable_host():
    report = runtime_check.run("http://127.0.0.1:9", ["/"], "/healthz", 2)
    assert report["status"] == "fail"


def test_meta_checks_detect_two_h1s_and_missing_alt():
    checks = dict((name, ok) for name, ok, _ in runtime_check.meta_checks(BAD_HTML, {}))
    assert checks["exactly one h1"] is False
    assert checks["all images have alt text"] is False
    assert checks["meta description present"] is False


def test_hsts_is_only_required_over_https():
    res = {"headers": {"strict-transport-security": "max-age=1"}}
    insecure = dict((n, (ok, req)) for n, ok, _, req in
                    runtime_check.header_checks(res, secure=False))
    secure = dict((n, (ok, req)) for n, ok, _, req in
                  runtime_check.header_checks(res, secure=True))
    assert insecure["header strict-transport-security (HTTPS only)"][1] is False
    assert secure["header strict-transport-security"][1] is True


# --------------------------------------------------------------------------
# lighthouse_run
# --------------------------------------------------------------------------

def test_parse_report_extracts_scores_and_metrics():
    data = {
        "categories": {
            "performance": {"score": 0.96},
            "accessibility": {"score": 0.97},
            "best-practices": {"score": 0.95},
            "seo": {"score": 0.93},
        },
        "audits": {
            "largest-contentful-paint": {"numericValue": 1234},
            "cumulative-layout-shift": {"numericValue": 0.02},
            "total-blocking-time": {"numericValue": 120},
            "first-contentful-paint": {"numericValue": 800},
            "speed-index": {"numericValue": 1100},
        },
    }
    parsed = lighthouse_run_parse(data)
    assert parsed["scores"]["performance"] == 96
    assert parsed["scores"]["accessibility"] == 97
    assert parsed["scores"]["best-practices"] == 95
    assert parsed["metrics"]["LCP"] == 1234
    assert parsed["metrics"]["CLS"] == 0.02
    assert parsed["metrics"]["TBT"] == 120


def lighthouse_run_parse(data):
    import lighthouse_run
    return lighthouse_run.parse_report(data)


def test_lighthouse_command_prefers_local_binary(tmp_path):
    import lighthouse_run
    node_modules = tmp_path / "node_modules" / ".bin"
    node_modules.mkdir(parents=True)
    lh = node_modules / "lighthouse"
    lh.write_text("#!/bin/sh\n")
    cmd, source = lighthouse_run.lighthouse_cmd(tmp_path)
    assert cmd[0].endswith("lighthouse")
    assert "local" in source


# --------------------------------------------------------------------------
# security_scan additions
# --------------------------------------------------------------------------

@pytest.mark.parametrize("code,needle", [
    ("import pickle; pickle.loads(data)", "pickle"),
    ("import yaml; yaml.load(f)", "yaml"),
    ("subprocess.run(cmd, shell=True)", "shell"),
    ("exec(\"print(user_input)\")", "exec"),
    ("hashlib.md5(b'x')", "md5"),
    ("jwt.decode(t, key, options={'verify_signature': False})", "jwt"),
    ("el.innerHTML = data", "innerhtml"),
    ("fetch('http://api.example.com/x')", "http"),
    ("db.query(\"SELECT * FROM t WHERE id = \" + id)", "sql"),
    ("document.write(html)", "document.write"),
])
def test_security_scan_flags_insecure_patterns(tmp_path, code, needle):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "app.py").write_text(code)
    findings = security_scan.scan_all(tmp_path)
    blob = json.dumps(findings).lower()
    assert needle in blob, findings


def test_security_scan_flags_broken_fixture_secrets(broken_app):
    findings = security_scan.scan_all(broken_app)
    high = [f for f in findings if f["severity"] == "HIGH"]
    assert high, findings


def test_security_scan_is_clean_for_the_good_app(good_app):
    findings = security_scan.scan_all(good_app)
    assert not [f for f in findings if f["severity"] == "HIGH"], findings


def test_security_scan_flags_disabled_jwt_verification(tmp_path):
    (tmp_path / "auth.js").write_text(
        "const t = jwt.decode(token, key, { algorithms: ['none'], verify: false });")
    findings = security_scan.scan_all(tmp_path)
    assert findings


# --------------------------------------------------------------------------
# verify_claims
# --------------------------------------------------------------------------

@pytest.fixture
def app_copy(tmp_path, good_app):
    """A private, mutable copy of the good app (session fixture is read-only)."""
    dst = tmp_path / "app"
    shutil.copytree(good_app, dst)
    return dst


def _write_evidence(app: Path, *, lighthouse_ok=True, manifest_browsers=("chromium", "firefox")):
    """Create the artefacts a completed review would have left behind."""
    shots = app / "docs" / "screenshots"
    shots.mkdir(parents=True, exist_ok=True)
    for name in ("home.png", "pricing.png", "mobile.png"):
        (shots / name).write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 64)
    (shots / "contact-sheet.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 64)
    (shots / "manifest.json").write_text(json.dumps({
        "captures": [{"browser": b, "route": "/"} for b in manifest_browsers]}))
    lh = app / "qa" / "lighthouse"
    lh.mkdir(parents=True, exist_ok=True)
    (lh / "lighthouse-summary.json").write_text(json.dumps({
        "status": "ok",
        "thresholds": {"performance": 90, "accessibility": 95,
                       "best-practices": 95, "seo": 90},
        "results": {"/": {"scores": {"performance": 100, "accessibility": 100,
                                     "best-practices": 100, "seo": 100}}},
    } if lighthouse_ok else {
        "status": "ok",
        "thresholds": {"performance": 90},
        "results": {"/": {"scores": {"performance": 42}}},
    }))
    a11y = app / "qa" / "a11y"
    a11y.mkdir(parents=True, exist_ok=True)
    (a11y / "a11y-report.json").write_text(json.dumps({
        "status": "ok", "failures": [], "browsers": {"chromium": {}}}))


def test_parse_claims_reads_json():
    p = SKILL / "scripts" / "fixtures" / "claims_true.json"
    gates, source = verify_claims.parse_claims(p)
    assert gates["A"] == "PASS"
    assert "M" in gates
    assert source.endswith("claims_true.json")


def test_parse_claims_reads_the_markdown_report():
    p = SKILL / "scripts" / "fixtures" / "claims_false.md"
    gates, source = verify_claims.parse_claims(p)
    assert gates["A"] == "PASS"
    assert len(gates) >= 10


def test_parse_claims_ignores_unknown_gate_keys(tmp_path):
    p = tmp_path / "c.json"
    p.write_text(json.dumps({"gates": {"A": "PASS", "Z": "PASS"}}))
    gates, _ = verify_claims.parse_claims(p)
    assert "A" in gates and "Z" not in gates


def test_verify_claims_accepts_a_truthful_report(app_copy):
    _write_evidence(app_copy)
    claims = {"gates": {k: "PASS" for k in "ABCDEFGHIJKLM"}}
    with LocalServer() as srv:
        ctx = {"url": srv.url, "routes": ["/"], "healthz": "/healthz",
               "skip_tests": False, "test_timeout": 300}
        report = verify_claims.verify(app_copy, claims, ctx)
    by_gate = {r["gate"]: r["verdict"] for r in report["results"]}
    assert by_gate["A"] == "VERIFIED"
    assert by_gate["B"] == "VERIFIED"
    assert by_gate["D"] == "VERIFIED"
    assert by_gate["J"] == "VERIFIED"
    assert by_gate["M"] == "VERIFIED"
    assert by_gate["C"] == "UNVERIFIABLE"
    assert report["status"] != "fail", report["blocking"]


def test_verify_claims_catches_a_false_pass_on_lighthouse(app_copy):
    _write_evidence(app_copy, lighthouse_ok=False)
    claims = {"gates": {"D": "PASS"}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "test_timeout": 60}
    report = verify_claims.verify(app_copy, claims, ctx)
    assert report["status"] == "fail"
    assert report["results"][0]["verdict"] == "CONTRADICTED"


def test_verify_claims_catches_a_false_pass_on_browser_coverage(app_copy):
    _write_evidence(app_copy, manifest_browsers=("chromium",))
    claims = {"gates": {"A": "PASS"}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "test_timeout": 60}
    report = verify_claims.verify(app_copy, claims, ctx)
    assert report["status"] == "fail"
    assert "CONTRADICTED" in report["results"][0]["verdict"]


@pytest.mark.skipif(not qa_common.which("npm"), reason="npm not installed")
def test_verify_claims_catches_a_false_pass_on_tests(app_copy):
    _write_evidence(app_copy)
    # break the test suite
    (app_copy / "tests").mkdir(exist_ok=True)
    (app_copy / "tests" / "app.test.js").write_text("throw new Error('boom');")
    claims = {"gates": {"H": "PASS"}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": False, "test_timeout": 120}
    report = verify_claims.verify(app_copy, claims, ctx)
    assert report["status"] == "fail"
    assert report["results"][0]["verdict"] == "CONTRADICTED"


def test_verify_claims_detects_a_mismatched_live_url(app_copy):
    _write_evidence(app_copy)
    claims = {"gates": {"G": "PASS", "I": "PASS"}}
    with LocalServer(html="<html><body><h1>Some other product</h1></body></html>") as srv:
        ctx = {"url": srv.url, "routes": ["/"], "healthz": "/healthz",
               "skip_tests": True, "test_timeout": 60}
        report = verify_claims.verify(app_copy, claims, ctx)
    assert report["identity"]["ok"] is False
    assert report["status"] == "fail"


def test_verify_claims_marks_non_passed_gates_as_not_claimed(app_copy):
    claims = {"gates": {"A": "FAIL"}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "test_timeout": 60}
    report = verify_claims.verify(app_copy, claims, ctx)
    assert report["results"][0]["verdict"] == "NOT_CLAIMED_PASS"
    assert report["status"] != "fail"


# --------------------------------------------------------------------------
# verify_claims: artefact lookup + test counting
# --------------------------------------------------------------------------

@pytest.mark.parametrize("output,expected", [
    ("# tests 1\n# pass 1\n# fail 0", 1),
    ("â„¹ tests 3\nâ„¹ pass 3", 3),
    ("1 passed in 0.12s", 1),
    ("Tests:       2 passed, 2 total", 2),
    ("test result: ok. 4 passed; 0 failed", 4),
    ("ok  \tgithub.com/x/y\t0.01s", 1),
    ("â„¹ tests 0\nâ„¹ pass 0", 0),
    ("everything is fine", None),
    ("", None),
])
def test_count_tests_understands_the_common_runners(output, expected):
    assert verify_claims.count_tests(output) == expected


def test_verify_claims_ignores_artefacts_outside_the_app_root(app_copy, tmp_path, monkeypatch):
    """A stale report in the working directory must not verify a gate."""
    other = tmp_path / "other-project"
    (other / "qa" / "lighthouse").mkdir(parents=True)
    (other / "qa" / "lighthouse" / "lighthouse-summary.json").write_text(json.dumps({
        "status": "ok",
        "thresholds": {"performance": 90},
        "results": {"/": {"scores": {"performance": 100}}},
    }))
    monkeypatch.chdir(other)
    claims = {"gates": {"D": "PASS"}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "test_timeout": 60, "artifact_dirs": []}
    report = verify_claims.verify(app_copy, claims, ctx)
    assert report["results"][0]["verdict"] == "UNSUPPORTED"
    assert report["status"] == "fail"


def test_verify_claims_accepts_an_explicit_artifact_dir(app_copy, tmp_path):
    """--artifact-dir lets a review workspace hold the evidence."""
    workspace = tmp_path / "review"
    (workspace / "qa" / "lighthouse").mkdir(parents=True)
    (workspace / "qa" / "lighthouse" / "lighthouse-summary.json").write_text(json.dumps({
        "status": "ok",
        "thresholds": {"performance": 90},
        "results": {"/": {"scores": {"performance": 100}}},
    }))
    claims = {"gates": {"D": "PASS"}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "test_timeout": 60, "artifact_dirs": [str(workspace)]}
    report = verify_claims.verify(app_copy, claims, ctx)
    assert report["results"][0]["verdict"] == "VERIFIED"
    assert report["status"] != "fail"


@pytest.mark.skipif(not qa_common.which("npm"), reason="npm not installed")
def test_verify_claims_flags_a_test_command_that_ran_nothing(app_copy):
    """A green test command that executed zero tests is not evidence."""
    pkg = json.loads((app_copy / "package.json").read_text())
    pkg["scripts"]["test"] = "echo no tests here"
    (app_copy / "package.json").write_text(json.dumps(pkg))
    claims = {"gates": {"H": "PASS"}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": False, "test_timeout": 60, "artifact_dirs": []}
    report = verify_claims.verify(app_copy, claims, ctx)
    assert report["results"][0]["verdict"] == "UNSUPPORTED"
    assert report["status"] == "fail"


# --------------------------------------------------------------------------
# fixture generator
# --------------------------------------------------------------------------

def test_fixture_good_variant_is_complete(good_app):
    for rel in ("package.json", "server.js", "README.md", "Dockerfile",
                "vercel.json", "netlify.toml", "fly.toml", "render.yaml",
                "wrangler.toml", "LICENSE", ".env.example",
                ".github/workflows/ci.yml"):
        assert (good_app / rel).is_file(), rel
    assert (good_app / "dist" / "index.html").is_file()
    assert (good_app / "docs" / "screenshots").is_dir()


def test_fixture_broken_variant_carries_the_defects(broken_app):
    assert (broken_app / ".env").is_file()
    assert (broken_app / "src" / "broken.js").is_file()
    huge = broken_app / "dist" / "assets" / "huge.js"
    assert huge.is_file()
    assert huge.stat().st_size > 200 * 1024


def test_fixture_generator_is_deterministic(tmp_path):
    a = tmp_path / "a"
    b = tmp_path / "b"
    make_sample_app.build(a, variant="good")
    make_sample_app.build(b, variant="good")
    assert (a / "package.json").read_text() == (b / "package.json").read_text()


# --------------------------------------------------------------------------
# a11y_audit (Playwright optional)
# --------------------------------------------------------------------------

def _playwright_available():
    try:
        import playwright  # noqa: F401
        return True
    except Exception:
        return False


@pytest.mark.skipif(not _playwright_available(), reason="playwright not installed")
def test_a11y_audit_finds_a_missing_alt_text():
    import a11y_audit
    source, _origin = a11y_audit.find_axe(SKILL)
    if not source:
        pytest.skip("axe-core not available offline")
    with LocalServer(html=BAD_HTML) as srv:
        report = a11y_audit.audit(srv.url, ["/"], ["chromium"], source, 15000)
    assert report["status"] != "skipped"
    failures = report.get("failures") or []
    assert failures, report


@pytest.mark.skipif(not _playwright_available(), reason="playwright not installed")
def test_a11y_audit_reports_axe_ran():
    import a11y_audit
    source, _origin = a11y_audit.find_axe(SKILL)
    if not source:
        pytest.skip("axe-core not available offline")
    with LocalServer() as srv:
        report = a11y_audit.audit(srv.url, ["/"], ["chromium"], source, 15000)
    route = report["browsers"]["chromium"]["routes"]["/"]
    assert route.get("axe_ran") is True
    assert report["status"] == "ok", report.get("failures")


# --------------------------------------------------------------------------
# end-to-end CLI smoke tests
# --------------------------------------------------------------------------

def _cli(script, *args):
    return subprocess.run([sys.executable, str(SCRIPTS / script), *args],
                          capture_output=True, text=True)


def test_cli_scripts_reject_a_bad_root():
    for script in ("dep_audit.py", "bundle_report.py", "deploy_verify.py",
                   "runtime_check.py", "verify_claims.py", "a11y_audit.py",
                   "lighthouse_run.py"):
        proc = _cli(script, "--root", str(SCRIPTS / "does-not-exist"))
        assert proc.returncode != 0, script


def test_cli_json_mode_emits_pure_json(good_app):
    proc = _cli("bundle_report.py", "--root", str(good_app), "--json")
    assert proc.returncode == 0
    payload = json.loads(proc.stdout)
    assert payload["status"] == "ok"
