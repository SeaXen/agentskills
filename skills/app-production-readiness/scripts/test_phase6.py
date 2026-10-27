#!/usr/bin/env python3
"""Tests for the deep modes that close the last review gaps.

Covered here:

* ``deploy_smoke.py``      - the app really boots and answers
* ``migration_apply.py``   - migrations really apply, roll back and re-apply
* ``payment_email_live.py``- live test-mode payment / email round-trip
* ``load_check.py``        - the soak is a real time series
* ``design_polish.py``     - the human sign-off record and its validation
* ``verify_claims.py``     - the new evidence is what the verifier accepts
"""
from __future__ import annotations

import json
import shutil
import socket
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SCRIPTS / "fixtures"))

import design_polish  # noqa: E402
import deploy_smoke  # noqa: E402
import load_check  # noqa: E402
import migration_apply  # noqa: E402
import payment_email_live  # noqa: E402
import verify_claims  # noqa: E402
from make_sample_app import build as build_sample_app  # noqa: E402  (module import!)

FIXTURES = SCRIPTS / "fixtures"


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

START_SERVER = '''\
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("PORT", "3000"))

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            body = b'{"status":"ok"}'
            ctype = "application/json"
        else:
            body = b"<html><head><title>t</title></head><body>ok</body></html>"
            ctype = "text/html"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass

ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
'''


class LocalServer:
    """A tiny HTTP server for the load and runtime tests."""

    def __init__(self, health=True):
        self.health = health
        self.server = None
        self.thread = None
        self.port = None

    def __enter__(self):
        health = self.health

        class H(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/healthz":
                    if not health:
                        self.send_error(404)
                        return
                    body = b'{"status":"ok"}'
                    ctype = "application/json"
                else:
                    body = b"<html><body>ok</body></html>"
                    ctype = "text/html"
                self.send_response(200)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                pass

        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            self.port = probe.getsockname()[1]
        self.server = ThreadingHTTPServer(("127.0.0.1", self.port), H)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        return self

    def __exit__(self, *exc):
        self.server.shutdown()
        self.server.server_close()
        return False

    @property
    def url(self):
        return f"http://127.0.0.1:{self.port}"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_runnable_app(tmp_path: Path) -> Path:
    """A tiny app whose ``start`` script serves /healthz on $PORT."""
    app = tmp_path / "runnable"
    app.mkdir(parents=True, exist_ok=True)
    _write(app / "start.py", START_SERVER)
    _write(app / "package.json", json.dumps({
        "name": "runnable-app", "version": "1.0.0", "private": True,
        "scripts": {"start": "python start.py"},
    }, indent=2))
    return app


def make_migration_app(tmp_path: Path, with_rollback=True, broken=False) -> Path:
    app = tmp_path / ("mig-broken" if broken else "mig-ok")
    app.mkdir(parents=True, exist_ok=True)
    forward = ("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT);")
    if broken:
        forward = "DROP TABLE does_not_exist;"
    _write(app / "db" / "migrate" / "001_init.sql", forward)
    if with_rollback:
        _write(app / "db" / "migrate" / "001_init.down.sql",
               "DROP TABLE IF EXISTS items;")
    return app


# --------------------------------------------------------------------------
# deploy_smoke
# --------------------------------------------------------------------------

def test_deploy_smoke_detects_a_runtime_plan(tmp_path):
    app = make_runnable_app(tmp_path)
    plan = deploy_smoke.detect_plan(app)
    assert plan["mode"] == "runtime"
    assert "start.py" in plan["start"]


def test_deploy_smoke_boots_the_app_and_probes_it(tmp_path):
    app = make_runnable_app(tmp_path)
    result = deploy_smoke.run_smoke(app, {
        "healthz": "/healthz", "routes": ["/"], "port": None,
        "boot_timeout": 30.0, "remote": False, "remote_url": None, "build": None,
    })
    assert result["status"] == "ok"
    assert result["health_ok"] is True
    assert result["routes_ok"] is True
    assert result["probes"][0]["status"] == 200


def test_deploy_smoke_reports_a_failing_health_endpoint(tmp_path):
    app = make_runnable_app(tmp_path)
    # /healthz answers 404 in this variant -> the probe must fail
    _write(app / "start.py", START_SERVER.replace(
        "self.send_response(200)",
        "self.send_response(404 if self.path == '/healthz' else 200)"))
    result = deploy_smoke.run_smoke(app, {
        "healthz": "/healthz", "routes": ["/"], "port": None,
        "boot_timeout": 30.0, "remote": False, "remote_url": None, "build": None,
    })
    assert result["status"] == "fail"
    assert result["health_ok"] is False


def test_deploy_smoke_skips_when_there_is_nothing_to_boot(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    result = deploy_smoke.run_smoke(empty, {
        "healthz": "/healthz", "routes": ["/"], "port": None,
        "boot_timeout": 5.0, "remote": False, "remote_url": None, "build": None,
    })
    assert result["status"] == "skipped"


def test_deploy_smoke_cli_exits_2_when_nothing_can_be_booted(tmp_path, capsys):
    empty = tmp_path / "empty"
    empty.mkdir()
    rc = deploy_smoke.main(["--root", str(empty)])
    assert rc == 2
    assert "SKIP" in capsys.readouterr().out


def test_deploy_smoke_cli_rejects_a_bad_root(capsys):
    rc = deploy_smoke.main(["--root", str(ROOT / "does-not-exist")])
    assert rc == 1


# --------------------------------------------------------------------------
# migration_apply
# --------------------------------------------------------------------------

def test_migration_discovery_pairs_forward_and_rollback(tmp_path):
    app = make_migration_app(tmp_path)
    found = migration_apply.discover(app / "db" / "migrate")
    assert len(found) == 1
    assert found[0]["rollback"] is not None
    assert found[0]["version"] == "001"


def test_migration_apply_runs_a_full_round_trip(tmp_path):
    app = make_migration_app(tmp_path)
    engine = migration_apply.SqliteEngine(app)
    try:
        roundtrip = migration_apply.run_roundtrip(app, engine,
                                                  migration_apply.discover(app / "db" / "migrate"))
    finally:
        engine.cleanup()
    assert all(s["status"] == "ok" for s in roundtrip["apply"])
    assert all(s["status"] == "ok" for s in roundtrip["rollback"])
    assert "items" in roundtrip["tables_after_apply"]
    assert "items" not in roundtrip["tables_after_rollback"]


def test_migration_apply_fails_on_broken_sql(tmp_path):
    app = make_migration_app(tmp_path, broken=True)
    engine = migration_apply.SqliteEngine(app)
    try:
        roundtrip = migration_apply.run_roundtrip(app, engine,
                                                  migration_apply.discover(app / "db" / "migrate"))
    finally:
        engine.cleanup()
    assert any(s["status"] == "fail" for s in roundtrip["apply"])


def test_migration_apply_cli_fails_without_a_rollback(tmp_path):
    app = make_migration_app(tmp_path, with_rollback=False)
    rc = migration_apply.main(["--root", str(app)])
    assert rc == 1


def test_migration_apply_cli_skips_when_there_are_no_migrations(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    rc = migration_apply.main(["--root", str(empty)])
    assert rc == 2


# --------------------------------------------------------------------------
# payment_email_live
# --------------------------------------------------------------------------

def test_payment_email_live_skips_without_credentials(tmp_path, monkeypatch):
    monkeypatch.delenv("STRIPE_SECRET_KEY", raising=False)
    monkeypatch.delenv("RESEND_API_KEY", raising=False)
    monkeypatch.delenv("MAIL_API_KEY", raising=False)
    app = tmp_path / "app"
    app.mkdir()
    rc = payment_email_live.main(["--root", str(app)])
    assert rc == 2


def test_payment_email_live_refuses_a_live_stripe_key(tmp_path, monkeypatch):
    monkeypatch.setenv("STRIPE_SECRET_KEY", "sk_live_51H8xYz2eZvKYlo2C0abcdef")
    monkeypatch.delenv("RESEND_API_KEY", raising=False)
    app = tmp_path / "app"
    app.mkdir()
    rc = payment_email_live.main(["--root", str(app)])
    assert rc == 1


def test_payment_email_live_builds_a_stripe_request(tmp_path, monkeypatch):
    captured = {}

    def fake_request(url, method="GET", headers=None, body=None, timeout=15.0,
                     allow_redirects=True):
        captured["url"] = url
        captured["body"] = body.decode() if body else ""
        captured["auth"] = (headers or {}).get("Authorization")
        return {"ok": True, "status": 200, "headers": {}, "body": '{"id":"pi_123"}',
                "bytes": 13, "json": {"id": "pi_123", "amount": 100,
                                       "currency": "usd", "status": "requires_payment_method"},
                "elapsed_ms": 5.0, "error": ""}

    monkeypatch.setattr(payment_email_live, "http_request", fake_request)
    result = payment_email_live.stripe_intent("sk_test_123", 100, "usd")
    assert result["ok"] is True
    assert result["id"] == "pi_123"
    assert "amount=100" in captured["body"]
    assert captured["auth"] == "Bearer sk_test_123"


# --------------------------------------------------------------------------
# load_check soak
# --------------------------------------------------------------------------

def test_load_check_soak_produces_a_time_series():
    with LocalServer() as server:
        import subprocess
        cmd = [sys.executable, str(SCRIPTS / "load_check.py"), "--url", server.url,
               "--routes", "/", "--duration", "1", "--soak", "4",
               "--soak-interval", "2", "--workers", "2", "--json"]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    data = json.loads(proc.stdout)
    soak = data["soak"]
    assert soak, "the soak produced no data"
    entry = soak[0]
    assert entry["windows"] >= 2
    assert len(entry["series"]) == entry["windows"]
    assert "drift_pct" in entry
    assert entry["first_error_rate_pct"] >= 0


def test_load_check_percentile():
    values = list(range(1, 101))
    assert 94 <= load_check.percentile(values, 95) <= 96
    assert load_check.percentile([], 95) == 0


# --------------------------------------------------------------------------
# design_polish sign-off
# --------------------------------------------------------------------------

@pytest.fixture(scope="module")
def good_app(tmp_path_factory):
    out = tmp_path_factory.mktemp("good-app")
    build_sample_app(out, variant="good")
    return out


def test_rubric_fingerprint_changes_with_the_score():
    report = {"score": 0.9, "threshold": 0.85,
              "dimensions": {"typography": {"score": 0.9}}}
    other = {"score": 0.8, "threshold": 0.85,
             "dimensions": {"typography": {"score": 0.8}}}
    assert design_polish.rubric_fingerprint(report) != design_polish.rubric_fingerprint(other)


def test_signoff_validation_accepts_a_fresh_approval(good_app):
    report = design_polish.analyse(good_app)
    record = design_polish.build_signoff("Ada", "approved", "fine", report)
    assert design_polish.validate_signoff(record, report) == []


def test_signoff_validation_rejects_a_stale_fingerprint(good_app):
    report = design_polish.analyse(good_app)
    record = design_polish.build_signoff("Ada", "approved", "fine", report)
    record["fingerprint"] = "0" * 32
    reasons = design_polish.validate_signoff(record, report)
    assert any("different rubric measurement" in r for r in reasons)


def test_signoff_validation_rejects_a_wrong_score(good_app):
    report = design_polish.analyse(good_app)
    record = design_polish.build_signoff("Ada", "approved", "fine", report)
    record["rubric_score"] = 0.11
    reasons = design_polish.validate_signoff(record, report)
    assert any("does not match" in r for r in reasons)


def test_signoff_validation_rejects_a_rejected_verdict(good_app):
    report = design_polish.analyse(good_app)
    record = design_polish.build_signoff("Ada", "rejected", "no", report)
    reasons = design_polish.validate_signoff(record, report)
    assert any("not 'approved'" in r for r in reasons)


def test_signoff_validation_rejects_a_future_date(good_app):
    report = design_polish.analyse(good_app)
    record = design_polish.build_signoff("Ada", "approved", "fine", report)
    record["date"] = "2999-01-01"
    reasons = design_polish.validate_signoff(record, report)
    assert any("future" in r for r in reasons)


def test_signoff_validation_requires_a_reviewer(good_app):
    report = design_polish.analyse(good_app)
    record = design_polish.build_signoff("", "approved", "fine", report)
    reasons = design_polish.validate_signoff(record, report)
    assert any("reviewer" in r for r in reasons)


def test_design_polish_reports_signed_off(good_app, tmp_path):
    report = design_polish.analyse(good_app)
    sign = tmp_path / "signoff.json"
    design_polish.write_signoff(sign, design_polish.build_signoff(
        "Ada", "approved", "looks good", report))
    import subprocess
    cmd = [sys.executable, str(SCRIPTS / "design_polish.py"), "--root", str(good_app),
           "--signoff", str(sign), "--json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    data = json.loads(proc.stdout)
    assert data["verdict"] == "rubric-met-and-signed-off"
    assert data["human_signoff"]["reviewer"] == "Ada"


def test_design_polish_without_a_signoff_stays_unsigned(good_app):
    import subprocess
    cmd = [sys.executable, str(SCRIPTS / "design_polish.py"), "--root", str(good_app),
           "--json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    data = json.loads(proc.stdout)
    assert data["verdict"] == "rubric-met-needs-signoff"
    assert data["human_signoff"] is None


# --------------------------------------------------------------------------
# verify_claims with the new evidence
# --------------------------------------------------------------------------

def test_verify_c_is_verified_with_a_valid_signoff(good_app, tmp_path):
    report = design_polish.analyse(good_app)
    sign = tmp_path / "signoff.json"
    design_polish.write_signoff(sign, design_polish.build_signoff(
        "Ada", "approved", "looks good", report))
    ctx = {"artifact_dirs": (str(sign.parent),)}
    # the verifier re-runs design_polish, so the sign-off has to live in the
    # default location for this check
    default = design_polish.signoff_path(good_app)
    design_polish.write_signoff(default, design_polish.build_signoff(
        "Ada", "approved", "looks good", report))
    verdict, evidence = verify_claims.verify_C(good_app, ctx)
    assert verdict == verify_claims.VERIFIED
    assert "Ada" in evidence


def test_verify_c_stays_unverifiable_without_a_signoff(good_app):
    sign = design_polish.signoff_path(good_app)
    if sign.exists():
        sign.unlink()
    verdict, evidence = verify_claims.verify_C(good_app, {})
    assert verdict == verify_claims.UNVERIFIABLE
    assert "sign-off" in evidence


def test_verify_i_accepts_a_deploy_smoke_report(good_app):
    payload = {"smoke": {"status": "ok", "mode": "runtime",
                         "health_ok": True, "routes_ok": True}}
    (good_app / "qa").mkdir(parents=True, exist_ok=True)
    (good_app / "qa" / "deploy-smoke.json").write_text(json.dumps(payload))
    verdict, evidence = verify_claims.verify_I(good_app, {"healthz": "/healthz"})
    assert verdict == verify_claims.VERIFIED
    assert "boots" in evidence


def test_verify_i_contradicts_a_failed_deploy_smoke(good_app):
    payload = {"smoke": {"status": "fail", "error": "the app did not open port 8080"}}
    (good_app / "qa").mkdir(parents=True, exist_ok=True)
    (good_app / "qa" / "deploy-smoke.json").write_text(json.dumps(payload))
    verdict, evidence = verify_claims.verify_I(good_app, {"healthz": "/healthz"})
    assert verdict == verify_claims.CONTRADICTED


def test_verify_p_accepts_a_migration_round_trip(good_app):
    payload = {"status": "ok",
               "roundtrip": {"engine": "sqlite", "apply": [{"migration": "001"}]}}
    (good_app / "qa").mkdir(parents=True, exist_ok=True)
    (good_app / "qa" / "migrations.json").write_text(json.dumps(payload))
    verdict, evidence = verify_claims.verify_P(good_app, {})
    assert verdict == verify_claims.VERIFIED
    assert "sqlite" in evidence


def test_verify_p_contradicts_a_failed_migration(good_app):
    payload = {"status": "fail", "blocking": ["every migration applies cleanly: boom"]}
    (good_app / "qa").mkdir(parents=True, exist_ok=True)
    (good_app / "qa" / "migrations.json").write_text(json.dumps(payload))
    verdict, evidence = verify_claims.verify_P(good_app, {})
    assert verdict == verify_claims.CONTRADICTED


def test_verify_t_accepts_a_live_round_trip(good_app):
    payload = {"status": "ok", "channels": [{"channel": "stripe"}, {"channel": "email"}]}
    (good_app / "qa").mkdir(parents=True, exist_ok=True)
    (good_app / "qa" / "payment-email-live.json").write_text(json.dumps(payload))
    verdict, evidence = verify_claims.verify_T(good_app, {})
    assert verdict == verify_claims.VERIFIED
    assert "stripe" in evidence


def test_verify_t_contradicts_a_failed_live_round_trip(good_app):
    payload = {"status": "fail", "blocking": ["a test PaymentIntent is created: HTTP 401"]}
    (good_app / "qa").mkdir(parents=True, exist_ok=True)
    (good_app / "qa" / "payment-email-live.json").write_text(json.dumps(payload))
    verdict, evidence = verify_claims.verify_T(good_app, {})
    assert verdict == verify_claims.CONTRADICTED


# --------------------------------------------------------------------------
# housekeeping
# --------------------------------------------------------------------------

def test_the_new_scripts_are_listed_in_the_skill_docs():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for name in ("deploy_smoke.py", "migration_apply.py", "payment_email_live.py"):
        assert name in skill, f"{name} is not documented in SKILL.md"


def test_shutil_is_available_for_cleanup():
    assert shutil.which("python") or shutil.which("python3")
