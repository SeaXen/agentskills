#!/usr/bin/env python3
"""Tests for the fingerprint-bound human sign-off mechanism.

The sign-off is the last mile of the review: a script can prove the code
does what the rules say, only a human can say the rules are the intended
ones.  The property that matters is **binding**: the approval covers the
exact content that was reviewed, so changing the rules (or the privacy
policy) invalidates it and the gate falls back to UNVERIFIABLE instead of
staying green.

Run:
  python -m pytest scripts/test_signoff.py -q
"""
from __future__ import annotations

import json
import shutil
import socket
import sys
import threading
from datetime import date, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SCRIPTS / "fixtures"))

import signoff as signoff_mod  # noqa: E402
import verify_claims  # noqa: E402
import make_sample_app  # noqa: E402


# --------------------------------------------------------------------------
# a tiny app server so the executable contract can really run
# --------------------------------------------------------------------------
class _Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):  # silence the test output
        pass

    def _send(self, status, body, ctype="application/json"):
        raw = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if self.path == "/healthz":
            self._send(200, json.dumps({"ok": True}))
        elif self.path == "/api/items":
            self._send(200, json.dumps([{"name": "widget"}]))
        elif self.path == "/privacy":
            self._send(200, "# Privacy Policy\n", "text/plain")
        else:
            self._send(404, json.dumps({"error": "not found"}))


class LocalServer:
    """Context manager that serves the fixture's routes on a free port."""

    def __init__(self):
        self.httpd = None
        self.url = ""

    def __enter__(self):
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
        self.url = f"http://127.0.0.1:{self.httpd.server_address[1]}"
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        return self

    def __exit__(self, *exc):
        self.httpd.shutdown()
        self.httpd.server_close()
        return False


@pytest.fixture(scope="module")
def good_app(tmp_path_factory):
    out = tmp_path_factory.mktemp("signoff-good")
    make_sample_app.build(out, variant="good")
    return out


@pytest.fixture
def app(good_app, tmp_path):
    dest = tmp_path / "app"
    shutil.copytree(good_app, dest)
    return dest


# --------------------------------------------------------------------------
# the signoff module itself
# --------------------------------------------------------------------------
def test_signoff_path_default_and_override(tmp_path):
    default = signoff_mod.signoff_path(tmp_path, "business-rules.json")
    assert default == tmp_path / "qa" / "signoff" / "business-rules.json"
    override = signoff_mod.signoff_path(tmp_path, "business-rules.json", "custom.json")
    assert override == tmp_path / "custom.json"
    absolute = signoff_mod.signoff_path(tmp_path, "x.json", str(tmp_path / "abs.json"))
    assert absolute == tmp_path / "abs.json"


def test_fingerprint_is_stable_and_content_bound(tmp_path):
    a = tmp_path / "rules.md"
    a.write_text("rule one", encoding="utf-8")
    first = signoff_mod.fingerprint([a], root=tmp_path)
    second = signoff_mod.fingerprint([a], root=tmp_path)
    assert first == second
    assert len(first) == 32
    a.write_text("rule one changed", encoding="utf-8")
    assert signoff_mod.fingerprint([a], root=tmp_path) != first


def test_fingerprint_notices_a_deleted_file(tmp_path):
    a = tmp_path / "rules.md"
    a.write_text("rule", encoding="utf-8")
    before = signoff_mod.fingerprint([a], root=tmp_path)
    a.unlink()
    assert signoff_mod.fingerprint([a], root=tmp_path) != before


def test_fingerprint_extra_marker_changes_the_value(tmp_path):
    a = tmp_path / "policy.md"
    a.write_text("policy", encoding="utf-8")
    assert signoff_mod.fingerprint([a], root=tmp_path) != \
        signoff_mod.fingerprint([a], extra="/privacy", root=tmp_path)


def test_validate_signoff_accepts_a_good_record():
    record = {"reviewer": "Jane", "date": date.today().isoformat(),
              "verdict": "approved", "fingerprint": "abc"}
    assert signoff_mod.validate_signoff(record, "abc") == []


def test_validate_signoff_rejects_every_weakness():
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    cases = [
        (None, "not a JSON object"),
        ({"verdict": "approved", "date": "2026-01-01", "fingerprint": "a"}, "reviewer"),
        ({"reviewer": "J", "date": "2026-01-01", "verdict": "maybe",
          "fingerprint": "a"}, "verdict"),
        ({"reviewer": "J", "verdict": "approved", "fingerprint": "a"}, "date"),
        ({"reviewer": "J", "date": "nope", "verdict": "approved",
          "fingerprint": "a"}, "ISO-8601"),
        ({"reviewer": "J", "date": tomorrow, "verdict": "approved",
          "fingerprint": "a"}, "future"),
        ({"reviewer": "J", "date": "2026-01-01", "verdict": "approved",
          "fingerprint": "b"}, "fingerprint"),
    ]
    for record, needle in cases:
        reasons = signoff_mod.validate_signoff(record, "a")
        assert reasons, record
        assert any(needle in r for r in reasons), (record, reasons)


def test_build_and_write_and_read_round_trip(tmp_path):
    record = signoff_mod.build_signoff("Jane", "approved", "looks right", "fp123",
                                       scope="checkout")
    assert record["reviewer"] == "Jane"
    assert record["verdict"] == "approved"
    assert record["fingerprint"] == "fp123"
    assert record["date"] == date.today().isoformat()
    path = tmp_path / "qa" / "signoff" / "business-rules.json"
    assert signoff_mod.write_signoff(path, record)
    assert signoff_mod.read_signoff(path) == record


def test_read_signoff_returns_none_for_broken_json(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("{not json", encoding="utf-8")
    assert signoff_mod.read_signoff(bad) is None
    assert signoff_mod.read_signoff(tmp_path / "missing.json") is None


def test_signoff_args_parses_every_flag():
    opts = signoff_mod.signoff_args([
        "--signoff", "qa/x.json", "--record-signoff", "--reviewer", "Jane",
        "--verdict", "approved", "--notes", "n", "--scope", "s",
        "--rules-ref", "SPEC-1"], prefix="rules")
    assert opts["path"] == "qa/x.json"
    assert opts["record"] is True
    assert opts["reviewer"] == "Jane"
    assert opts["verdict"] == "approved"
    assert opts["notes"] == "n"
    assert opts["scope"] == "s"
    assert opts["ref"] == "SPEC-1"


def test_signoff_args_accepts_a_basis_alias():
    opts = signoff_mod.signoff_args(["--legal-basis", "GDPR Art.13"], prefix="legal")
    assert opts["ref"] == "GDPR Art.13"


def test_resolve_signoff_reports_a_missing_record(tmp_path):
    res = signoff_mod.resolve_signoff(tmp_path, "business-rules.json", {}, "fp")
    assert res["record"] is None
    assert any("no sign-off record" in r for r in res["reasons"])


def test_resolve_signoff_records_and_validates(tmp_path):
    opts = {"record": True, "reviewer": "Jane", "verdict": "approved",
            "notes": "", "scope": "", "path": None, "ref": ""}
    res = signoff_mod.resolve_signoff(tmp_path, "business-rules.json", opts, "fp")
    assert res["reasons"] == []
    assert res["record"]["reviewer"] == "Jane"
    assert (tmp_path / "qa" / "signoff" / "business-rules.json").is_file()


def test_resolve_signoff_rejects_a_stale_fingerprint(tmp_path):
    opts = {"record": True, "reviewer": "Jane", "verdict": "approved",
            "notes": "", "scope": "", "path": None, "ref": ""}
    signoff_mod.resolve_signoff(tmp_path, "business-rules.json", opts, "fp")
    res = signoff_mod.resolve_signoff(tmp_path, "business-rules.json", {}, "other-fp")
    assert any("fingerprint does not match" in r for r in res["reasons"])


# --------------------------------------------------------------------------
# Gate N - business rules
# --------------------------------------------------------------------------
def _run_business(root, url, extra=()):
    import subprocess
    cmd = [sys.executable, str(SCRIPTS / "business_logic_check.py"),
           "--root", str(root), "--json"]
    if url:
        cmd += ["--url", url]
    cmd += list(extra)
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(root))
    return proc.returncode, json.loads(proc.stdout)


def test_gate_n_needs_a_sign_off_first(app):
    with LocalServer() as srv:
        rc, data = _run_business(app, srv.url)
    assert rc == 0
    assert data["verdict"] == "executable-contract-met-needs-signoff"
    assert data["human_signoff"] is None
    assert any("no sign-off record" in r for r in data["signoff_reasons"])


def test_gate_n_becomes_signed_off(app):
    with LocalServer() as srv:
        rc, data = _run_business(app, srv.url, [
            "--record-signoff", "--reviewer", "Jane Doe", "--verdict", "approved",
            "--notes", "rules match spec v3", "--rules-ref", "SPEC-42"])
        assert rc == 0
        assert data["verdict"] == "executable-contract-met-and-signed-off"
        assert data["human_signoff"]["reviewer"] == "Jane Doe"
        assert data["human_signoff"]["rules_ref"] == "SPEC-42"
        # the rule document is part of what was signed off
        assert "docs/rules.md" in data["signoff_subject"]
        assert "qa/scenarios.json" in data["signoff_subject"]


def test_gate_n_sign_off_does_not_survive_a_rules_change(app):
    with LocalServer() as srv:
        _run_business(app, srv.url, ["--record-signoff", "--reviewer", "Jane"])
        rules = app / "docs" / "rules.md"
        rules.write_text(rules.read_text(encoding="utf-8") + "\nR5 - new rule\n",
                         encoding="utf-8")
        rc, data = _run_business(app, srv.url)
    assert rc == 0
    assert data["verdict"] == "executable-contract-met-needs-signoff"
    assert any("fingerprint does not match" in r for r in data["signoff_reasons"])


def test_gate_n_sign_off_does_not_survive_a_scenario_change(app):
    with LocalServer() as srv:
        _run_business(app, srv.url, ["--record-signoff", "--reviewer", "Jane"])
        spec = app / "qa" / "scenarios.json"
        payload = json.loads(spec.read_text(encoding="utf-8"))
        payload["scenarios"].append({"name": "extra", "method": "GET",
                                     "path": "/healthz", "expect_status": 200})
        spec.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        rc, data = _run_business(app, srv.url)
    assert rc == 0
    assert data["verdict"] == "executable-contract-met-needs-signoff"


def test_gate_n_without_a_scenario_spec_is_unavailable(app):
    (app / "qa" / "scenarios.json").unlink()
    with LocalServer() as srv:
        rc, data = _run_business(app, srv.url)
    assert rc == 0
    assert data["verdict"] == "executable-contract-unavailable"


def test_gate_n_fails_when_a_scenario_fails(app):
    spec = app / "qa" / "scenarios.json"
    payload = json.loads(spec.read_text(encoding="utf-8"))
    payload["scenarios"].append({"name": "wrong", "method": "GET",
                                 "path": "/healthz", "expect_status": 418})
    spec.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    with LocalServer() as srv:
        rc, data = _run_business(app, srv.url)
    assert rc == 1
    assert data["verdict"] == "executable-contract-failed"


# --------------------------------------------------------------------------
# Gate Q - privacy / legal sign-off
# --------------------------------------------------------------------------
def _run_privacy(root, url, extra=()):
    import subprocess
    cmd = [sys.executable, str(SCRIPTS / "privacy_check.py"),
           "--root", str(root), "--json"]
    if url:
        cmd += ["--url", url]
    cmd += list(extra)
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(root))
    return proc.returncode, json.loads(proc.stdout)


def test_gate_q_needs_a_legal_sign_off(app):
    with LocalServer() as srv:
        rc, data = _run_privacy(app, srv.url)
    assert rc == 0
    assert data["verdict"] == "policy-met-needs-signoff"


def test_gate_q_becomes_signed_off(app):
    with LocalServer() as srv:
        rc, data = _run_privacy(app, srv.url, [
            "--record-signoff", "--reviewer", "Jane Doe", "--verdict", "approved",
            "--notes", "Art.13/17 covered", "--legal-basis", "GDPR Art.13"])
        assert rc == 0
        assert data["verdict"] == "policy-met-and-legal-signed-off"
        assert data["human_signoff"]["legal_basis"] == "GDPR Art.13"
        assert "privacy.md" in data["signoff_subject"]


def test_gate_q_sign_off_does_not_survive_a_policy_change(app):
    with LocalServer() as srv:
        _run_privacy(app, srv.url, ["--record-signoff", "--reviewer", "Jane"])
        policy = app / "privacy.md"
        policy.write_text(policy.read_text(encoding="utf-8") + "\nWe sold your data.\n",
                          encoding="utf-8")
        rc, data = _run_privacy(app, srv.url)
    assert rc == 0
    assert data["verdict"] == "policy-met-needs-signoff"
    assert any("fingerprint does not match" in r for r in data["signoff_reasons"])


def test_gate_q_still_fails_on_a_hard_violation(app):
    (app / "src" / "legacy.js").write_text(
        "export function log(u){ console.log('user', u.email); }\n", encoding="utf-8")
    with LocalServer() as srv:
        rc, data = _run_privacy(app, srv.url)
    assert rc == 1
    assert data["verdict"] == "policy-failed"


# --------------------------------------------------------------------------
# the verifier
# --------------------------------------------------------------------------
def _verify(root, url=None):
    claims = {"gates": {"N": "PASS", "Q": "PASS"}}
    ctx = {"url": url, "routes": ["/"], "healthz": "/healthz", "skip_tests": True,
           "artifact_dirs": (), "use_scope": True, "gate_timeout": 120}
    return verify_claims.verify(root, claims, ctx)


def test_verifier_marks_n_and_q_unverifiable_without_sign_offs(app):
    with LocalServer() as srv:
        report = _verify(app, srv.url)
    verdicts = {r["gate"]: r["verdict"] for r in report["results"]}
    assert verdicts["N"] == "UNVERIFIABLE"
    assert verdicts["Q"] == "UNVERIFIABLE"


def test_verifier_marks_n_and_q_verified_with_sign_offs(app):
    with LocalServer() as srv:
        _run_business(app, srv.url, ["--record-signoff", "--reviewer", "Jane"])
        _run_privacy(app, srv.url, ["--record-signoff", "--reviewer", "Jane"])
        report = _verify(app, srv.url)
    verdicts = {r["gate"]: r["verdict"] for r in report["results"]}
    assert verdicts["N"] == "VERIFIED"
    assert verdicts["Q"] == "VERIFIED"
    assert report["summary"]["unverifiable"] == 0


def test_verifier_drops_back_to_unverifiable_when_the_rules_change(app):
    with LocalServer() as srv:
        _run_business(app, srv.url, ["--record-signoff", "--reviewer", "Jane"])
        rules = app / "docs" / "rules.md"
        rules.write_text(rules.read_text(encoding="utf-8") + "\nR5 - new rule\n",
                         encoding="utf-8")
        report = _verify(app, srv.url)
    verdicts = {r["gate"]: r["verdict"] for r in report["results"]}
    assert verdicts["N"] == "UNVERIFIABLE"


def test_gate_names_mention_the_sign_off():
    assert "sign-off" in verify_claims.GATE_NAMES["N"]
    assert "sign-off" in verify_claims.GATE_NAMES["Q"]
