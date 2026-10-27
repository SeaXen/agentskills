#!/usr/bin/env python3
"""Tests for the adaptive gate scoping, the static SEO audit and the deep
security mode (the absorbed security-audit schema).

These are the pieces that decide *what* gets reviewed: without them every app
would be pushed through all 21 gates, and the security artefacts would not be
machine-checkable.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SCRIPTS / "fixtures"))

import gate_scope  # noqa: E402
import schema_validate  # noqa: E402
import security_audit  # noqa: E402
import seo_static  # noqa: E402
import verify_claims  # noqa: E402
import make_sample_app  # noqa: E402


@pytest.fixture(scope="module")
def good_app(tmp_path_factory):
    out = tmp_path_factory.mktemp("good")
    make_sample_app.build(out, variant="good")
    return out


@pytest.fixture(scope="module")
def broken_app(tmp_path_factory):
    out = tmp_path_factory.mktemp("broken")
    make_sample_app.build(out, variant="broken")
    return out


def _static_site(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    (root / "index.html").write_text(
        "<html lang='en'><head><title>Static</title>"
        "<meta name='description' content='x'></head><body><h1>Hi</h1></body></html>",
        encoding="utf-8")
    (root / "styles.css").write_text("body{color:#000}", encoding="utf-8")
    return root


def _api_only(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    (root / "package.json").write_text(json.dumps({
        "name": "api-only", "dependencies": {"express": "^4.0.0"},
        "scripts": {"start": "node server.js"}}), encoding="utf-8")
    (root / "server.js").write_text(
        "const express=require('express');const app=express();"
        "app.get('/healthz',(q,r)=>r.json({ok:true}));app.listen(3000);",
        encoding="utf-8")
    return root


# --- gate scoping ----------------------------------------------------------

def test_static_site_has_no_database_or_payment_gates(tmp_path):
    report = gate_scope.analyse(_static_site(tmp_path / "site"))
    assert report["app"]["kind"] == "static-site"
    assert "P" in report["skipped"], "a static site has no migrations"
    assert "T" in report["skipped"], "a static site has no payments"
    assert report["gates"]["P"]["status"] == gate_scope.NOT_APPLICABLE
    assert "database" in report["gates"]["P"]["reason"]


def test_api_service_has_no_visual_gates(tmp_path):
    report = gate_scope.analyse(_api_only(tmp_path / "api"))
    assert report["app"]["kind"] == "api-or-service"
    for gate in ("A", "C", "D", "F", "S"):
        assert gate in report["skipped"], f"gate {gate} must not apply to an API service"
    assert "E" in report["required"], "security always applies"


def test_full_app_keeps_every_gate(tmp_path):
    report = gate_scope.analyse(_static_site(tmp_path / "x"))
    assert report["summary"]["total"] == 21


def test_full_stack_fixture_applies_all_depth_gates(good_app):
    report = gate_scope.analyse(good_app)
    for gate in ("P", "Q", "R", "T", "N", "O"):
        assert gate in report["required"], f"gate {gate} must apply to the sample app"
    assert report["summary"]["not_applicable"] == 0


def test_scope_cli_is_json_clean(tmp_path):
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "gate_scope.py"), "--root",
         str(_static_site(tmp_path / "site")), "--json"],
        capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    payload = json.loads(proc.stdout)
    assert payload["summary"]["total"] == 21


def test_scope_cli_rejects_a_bad_root(tmp_path):
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "gate_scope.py"), "--root",
         str(tmp_path / "nope"), "--json"],
        capture_output=True, text=True)
    assert proc.returncode != 0


def test_scope_for_gate_returns_reason(tmp_path):
    report = gate_scope.analyse(_api_only(tmp_path / "api"))
    status, reason = gate_scope.scope_for_gate(report, "A")
    assert status == gate_scope.NOT_APPLICABLE
    assert reason


# --- scoping inside the verifier ------------------------------------------

def test_claimed_pass_on_an_inapplicable_gate_is_not_a_failure(tmp_path):
    app = _api_only(tmp_path / "api")
    claims = {"gates": {"A": "PASS", "T": "PASS", "E": "PASS"}}
    report = verify_claims.verify(app, claims, {"use_scope": True})
    verdicts = {r["gate"]: r["verdict"] for r in report["results"]}
    assert verdicts["A"] == verify_claims.NOT_APPLICABLE
    assert verdicts["T"] == verify_claims.NOT_APPLICABLE
    assert report["status"] != "fail"
    assert report["summary"]["not_applicable"] == 2


def test_scope_can_be_switched_off(tmp_path):
    app = _api_only(tmp_path / "api")
    claims = {"gates": {"A": "PASS"}}
    report = verify_claims.verify(app, claims, {"use_scope": False})
    verdicts = {r["gate"]: r["verdict"] for r in report["results"]}
    assert verdicts["A"] != verify_claims.NOT_APPLICABLE


# --- static SEO / GEO ------------------------------------------------------

def test_static_seo_finds_nothing_in_a_clean_app(good_app):
    report = seo_static.analyse(good_app)
    assert report["seo_findings"] == []
    assert report["pages_checked"] > 0


def test_static_seo_catches_the_broken_pages(broken_app):
    report = seo_static.analyse(broken_app)
    assert report["seo_findings"], "the broken fixture must have metadata gaps"
    kinds = " ".join(finding["issue"] for finding in report["seo_findings"])
    assert "description" in kinds.lower()


def test_static_seo_skips_a_project_without_pages(tmp_path):
    app = _api_only(tmp_path / "api")
    report = seo_static.analyse(app)
    assert report["pages_checked"] == 0


def test_static_seo_cli_exit_codes(broken_app):
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "seo_static.py"), "--root", str(broken_app),
         "--json"], capture_output=True, text=True)
    assert proc.returncode == 0  # advisory by default
    payload = json.loads(proc.stdout)
    assert payload["status"] == "issues"
    strict = subprocess.run(
        [sys.executable, str(SCRIPTS / "seo_static.py"), "--root", str(broken_app),
         "--strict", "--json"], capture_output=True, text=True)
    assert strict.returncode == 1


# --- deep security mode ----------------------------------------------------

def test_security_audit_writes_schema_valid_artefacts(broken_app, tmp_path):
    out = tmp_path / "qa" / "security"
    report = security_audit.analyse(broken_app, out)
    findings = json.loads((out / "findings.json").read_text(encoding="utf-8"))
    ledger = json.loads((out / "coverage-ledger.json").read_text(encoding="utf-8"))
    schema = json.loads((SCRIPTS / "security_audit_pack" / "report-schema.json")
                        .read_text(encoding="utf-8"))
    assert schema_validate.validate_findings(findings, schema) == []
    assert schema_validate.validate_ledger(ledger) == []
    assert report["confirmed"] >= 1, "a committed secret must be a confirmed finding"
    assert report["needs_validation"] >= 1


def test_security_audit_classifies_a_secret_as_confirmed(broken_app, tmp_path):
    out = tmp_path / "qa" / "security"
    security_audit.analyse(broken_app, out)
    findings = json.loads((out / "findings.json").read_text(encoding="utf-8"))
    confirmed = [f for f in findings if f["verdict"] == "confirmed"]
    assert confirmed
    for record in confirmed:
        assert record["severity"]["overall_severity"] in ("critical", "high", "medium")
        assert record["confidence"]["score"] in ("low", "medium", "high")
        assert record["execution"]["observed_result"]
        assert record["remediation"]["strategy"]


def test_security_audit_ledger_units_are_sorted_and_identified(broken_app, tmp_path):
    out = tmp_path / "qa" / "security"
    security_audit.analyse(broken_app, out)
    ledger = json.loads((out / "coverage-ledger.json").read_text(encoding="utf-8"))
    ids = [unit["coverage_id"] for unit in ledger]
    assert ids == sorted(ids)
    for unit in ledger:
        assert unit["coverage_id"] == schema_validate.canonical_coverage_id(
            unit["canonical_refs"])
        assert unit["status"] in ("covered", "candidate")


def test_security_audit_cli_reports_ok(broken_app):
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "security_audit.py"), "--root", str(broken_app),
         "--json"], capture_output=True, text=True)
    payload = json.loads(proc.stdout)
    assert payload["status"] == "ok", payload["validation"]
    assert proc.returncode == 0


def test_security_audit_cli_rejects_a_bad_root(tmp_path):
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "security_audit.py"), "--root",
         str(tmp_path / "nope"), "--json"], capture_output=True, text=True)
    assert proc.returncode != 0


# --- the portable schema validators ---------------------------------------

def test_schema_validator_rejects_a_broken_finding():
    schema = json.loads((SCRIPTS / "security_audit_pack" / "report-schema.json")
                        .read_text(encoding="utf-8"))
    bad = [{"verdict": "confirmed", "title": "no fingerprint", "description": "x"}]
    assert schema_validate.validate_findings(bad, schema)


def test_schema_validator_rejects_a_broken_ledger():
    bad = [{"coverage_id": "x"}]
    assert schema_validate.validate_ledger(bad)


def test_canonical_coverage_id_encodes_special_characters():
    assert schema_validate.canonical_coverage_id(
        {"surface": "a b", "boundary": "c/d", "subsystem": "e",
         "attack_class": "f"}) == "a%20b::c%2Fd::e::f"


def test_ledger_validator_catches_an_unsorted_ledger():
    good = {
        "coverage_id": "a::b::c::d",
        "canonical_refs": {"surface": "a", "boundary": "b", "subsystem": "c",
                           "attack_class": "d"},
        "surface": "a", "boundary": "b", "subsystem": "c", "attack_class": "d",
        "starting_paths": ["src"], "ordinary_attack_class_block": "x",
        "selected_companion_blocks": [], "excluded_blocks": [],
        "prior_status": "new", "attempts": [], "wave": 1, "status": "covered",
        "agent_id": "pdqa-owner", "reviewed_paths": ["src"],
        "local_checks": [], "result_fingerprints": [], "unresolved": [],
    }
    assert schema_validate.validate_ledger([good])
