#!/usr/bin/env python3
"""Regression suite for the depth gates (N-U) and the absorbed skills.

Covers:

  qa_ext             shared check model, HTTP client, absorbed-script runner
  design_polish      Gate C rubric (7 dimensions)
  business_logic_check  Gate N (static smells + executed scenarios)
  load_check         Gate O (percentiles, live load)
  migration_check    Gate P (rollback, destructive DDL, idempotency)
  privacy_check      Gate Q (policy, consent, PII)
  i18n_check         Gate R (locales, missing keys, RTL)
  at_check           Gate S (screen-reader contract)
  payment_email_check   Gate T (payments, mail)
  code_quality       Gate U (complexity, duplication, dead code)
  mobile_check       mobile readiness
  flow_test          Playwright flow runner (no browser needed for the skip path)
  verify_claims      the new gate names and verifiers
  absorbed/          manifest integrity

Run:  python -m pytest scripts/test_gates_extended.py -q
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
FIXTURES = SCRIPTS / "fixtures"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(FIXTURES))

import make_sample_app    # noqa: E402
import qa_ext             # noqa: E402
import verify_claims      # noqa: E402


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

@pytest.fixture(scope="module")
def good_app(tmp_path_factory):
    out = tmp_path_factory.mktemp("good-app-ext")
    make_sample_app.build(out, variant="good")
    return out


@pytest.fixture(scope="module")
def broken_app(tmp_path_factory):
    out = tmp_path_factory.mktemp("broken-app-ext")
    make_sample_app.build(out, variant="broken")
    return out


LAST_STDERR = {"text": ""}


def run_gate(script, root, extra=(), timeout=300):
    """Run a gate script with --json and return (returncode, payload)."""
    cmd = [sys.executable, str(SCRIPTS / script), "--root", str(root), "--json", *extra]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    LAST_STDERR["text"] = proc.stderr
    try:
        payload = json.loads(proc.stdout)
    except ValueError:
        payload = None
    return proc.returncode, payload


def failed_checks(payload):
    return [c["name"] for c in (payload or {}).get("checks", []) if not c["ok"]]


# --------------------------------------------------------------------------
# qa_ext
# --------------------------------------------------------------------------

def test_gate_result_model_counts_only_required_failures():
    result = qa_ext.GateResult("X", "test")
    result.add("fine", True)
    result.add("also fine", True, False, "informational")
    assert result.blocking == []
    assert result.status == "ok"
    result.fail("broken", "because", "HIGH")
    assert result.status == "fail"
    assert len(result.blocking) == 1
    assert result.as_dict()["summary"]["failed"] == 1


def test_run_absorbed_reports_the_exit_code_of_the_script(tmp_path):
    result = qa_ext.run_absorbed("ux_audit.py", tmp_path, timeout=120)
    assert result["available"] is True
    assert "exit=" in result["detail"]


def test_run_absorbed_handles_a_missing_script(tmp_path):
    result = qa_ext.run_absorbed("does-not-exist.py", tmp_path)
    assert result["available"] is False
    assert result["ok"] is True


def test_http_request_reports_status_and_headers():
    from test_advanced import LocalServer  # reuse the local server helper
    with LocalServer() as srv:
        res = qa_ext.http_request(srv.url + "/healthz")
        assert res["status"] == 200
        assert "content-type" in res["headers"]
        assert isinstance(res["json"], dict)


def test_http_request_never_raises_on_a_dead_host():
    res = qa_ext.http_request("http://127.0.0.1:9/nope", timeout=2.0)
    assert res["status"] == 0
    assert res["error"]


# --------------------------------------------------------------------------
# Gate C - design polish
# --------------------------------------------------------------------------

def test_design_polish_rubric_passes_for_the_good_app(good_app):
    rc, payload = run_gate("design_polish.py", good_app)
    assert rc == 0, payload
    rubric = payload["rubric"]
    assert rubric["score"] >= 0.85
    assert len(rubric["dimensions"]) == 7
    assert payload["verdict"] == "rubric-met-needs-signoff"
    assert payload["human_signoff"] is None


def test_design_polish_rubric_fails_for_the_broken_app(broken_app):
    rc, payload = run_gate("design_polish.py", broken_app)
    assert rc == 1
    assert payload["rubric"]["score"] < 0.85
    assert failed_checks(payload)


# --------------------------------------------------------------------------
# Gate N - business logic
# --------------------------------------------------------------------------

def test_business_logic_is_clean_for_the_good_app(good_app):
    rc, payload = run_gate("business_logic_check.py", good_app)
    assert rc == 0, payload
    assert payload["status"] == "ok"


def test_business_logic_catches_an_empty_catch_block(broken_app):
    rc, payload = run_gate("business_logic_check.py", broken_app)
    assert rc == 1
    assert any("empty catch" in name for name in failed_checks(payload))


def test_business_logic_runs_the_declared_scenarios(good_app, tmp_path):
    import shutil
    from test_advanced import LocalServer
    app = tmp_path / "app"
    shutil.copytree(good_app, app)
    (app / "qa").mkdir(exist_ok=True)
    (app / "qa" / "scenarios.json").write_text(json.dumps({"scenarios": [
        {"name": "health answers", "method": "GET", "path": "/healthz",
         "expect_status": 200, "expect_body_contains": ["ok"]},
        {"name": "api answers", "method": "GET", "path": "/api/qa-cors-probe",
         "expect_status": 200},
        {"name": "unknown route is 404", "method": "GET", "path": "/api/nope",
         "expect_status": 404},
    ]}), encoding="utf-8")
    with LocalServer() as srv:
        rc, payload = run_gate("business_logic_check.py", app, ["--url", srv.url])
    assert rc == 0, (payload, LAST_STDERR["text"][:400])
    assert len(payload["scenarios"]) == 3
    assert all(s["ok"] for s in payload["scenarios"])


# --------------------------------------------------------------------------
# Gate O - load
# --------------------------------------------------------------------------

def test_load_check_percentiles():
    import load_check
    values = list(range(1, 101))
    assert load_check.percentile(values, 50) == pytest.approx(50.5, abs=1)
    assert load_check.percentile(values, 95) == pytest.approx(95.05, abs=1)
    assert load_check.percentile([], 95) == 0.0


def test_load_check_measures_a_live_app(good_app):
    from test_advanced import LocalServer
    with LocalServer() as srv:
        rc, payload = run_gate("load_check.py", good_app,
                               ["--url", srv.url, "--duration", "1", "--workers", "2"])
    assert rc == 0, (payload, LAST_STDERR["text"][:500])
    assert payload["phases"][0]["requests"] > 0
    assert payload["phases"][0]["error_rate_pct"] == 0.0


# --------------------------------------------------------------------------
# Gate P - migrations
# --------------------------------------------------------------------------

def test_migration_check_accepts_a_paired_rollback(good_app):
    rc, payload = run_gate("migration_check.py", good_app)
    assert rc == 0, payload
    assert not any("rollback" in name for name in failed_checks(payload))


def test_migration_check_catches_destructive_sql(broken_app):
    rc, payload = run_gate("migration_check.py", broken_app)
    assert rc == 1
    names = " ".join(failed_checks(payload))
    assert "rollback" in names
    assert "DROP TABLE" in names


def test_migration_check_is_skipped_without_migrations(tmp_path):
    (tmp_path / "app.js").write_text("console.log(1);")
    rc, payload = run_gate("migration_check.py", tmp_path)
    assert rc == 2
    assert payload["status"] == "skipped"


# --------------------------------------------------------------------------
# Gate Q - privacy
# --------------------------------------------------------------------------

def test_privacy_check_finds_the_policy(good_app):
    rc, payload = run_gate("privacy_check.py", good_app)
    assert rc == 0, payload
    assert any("privacy policy" in c["name"] for c in payload["checks"])


def test_privacy_check_catches_pii_in_logs(broken_app):
    rc, payload = run_gate("privacy_check.py", broken_app)
    assert rc == 1
    assert any("not written to logs" in name for name in failed_checks(payload))


def test_privacy_check_requires_a_policy(tmp_path):
    (tmp_path / "app.js").write_text("export const x = 1;\n")
    rc, payload = run_gate("privacy_check.py", tmp_path)
    assert rc == 1
    assert any("privacy policy" in name for name in failed_checks(payload))


# --------------------------------------------------------------------------
# Gate R - i18n
# --------------------------------------------------------------------------

def test_i18n_check_sees_two_languages(good_app):
    rc, payload = run_gate("i18n_check.py", good_app)
    assert rc == 0, payload
    assert set(payload["languages"]) == {"en", "fr"}


def test_i18n_check_catches_a_single_language(broken_app):
    rc, payload = run_gate("i18n_check.py", broken_app)
    assert rc == 1
    assert any("more than one language" in name for name in failed_checks(payload))


def test_i18n_check_reports_missing_keys(tmp_path):
    (tmp_path / "locales").mkdir()
    (tmp_path / "locales" / "en.json").write_text('{"a": "1", "b": "2"}')
    (tmp_path / "locales" / "de.json").write_text('{"a": "1"}')
    (tmp_path / "app.js").write_text('t("a");\n')
    rc, payload = run_gate("i18n_check.py", tmp_path)
    assert rc == 1
    assert any("every key" in name for name in failed_checks(payload))


# --------------------------------------------------------------------------
# Gate S - assistive technology
# --------------------------------------------------------------------------

def test_at_check_is_clean_for_the_good_app(good_app):
    rc, payload = run_gate("at_check.py", good_app)
    assert rc == 0, payload


def test_at_check_catches_unlabelled_controls(broken_app):
    rc, payload = run_gate("at_check.py", broken_app)
    assert rc == 1
    assert any("programmatic label" in name for name in failed_checks(payload))


def test_at_check_ignores_email_templates(tmp_path):
    (tmp_path / "welcome.html").write_text(
        "<html><body><h1>Hi</h1><img src='x.png' /></body></html>")
    (tmp_path / "mail-templates").mkdir()
    (tmp_path / "mail-templates" / "welcome.html").write_text("<p>no title</p>")
    rc, payload = run_gate("at_check.py", tmp_path)
    # the mail template is not a page, so only the real page is judged
    assert not any("mail-templates" in str(c.get("detail", "")) for c in payload["checks"])


# --------------------------------------------------------------------------
# Gate T - payment & email
# --------------------------------------------------------------------------

def test_payment_email_check_is_clean_for_the_good_app(good_app):
    rc, payload = run_gate("payment_email_check.py", good_app)
    assert rc == 0, payload


def test_payment_email_check_catches_a_hardcoded_key(broken_app):
    rc, payload = run_gate("payment_email_check.py", broken_app)
    assert rc == 1
    assert any("credential" in name for name in failed_checks(payload))


def test_payment_email_check_catches_an_unverified_webhook(tmp_path):
    (tmp_path / "pay.js").write_text(
        'import Stripe from "stripe";\n'
        'export function webhook(payload) { return JSON.parse(payload); }\n')
    rc, payload = run_gate("payment_email_check.py", tmp_path)
    assert rc == 1
    assert any("signature" in name for name in failed_checks(payload))


def test_payment_email_check_catches_card_data_in_a_form(tmp_path):
    (tmp_path / "checkout.html").write_text(
        '<form><input name="card_number" /><input name="cvv" /></form>')
    rc, payload = run_gate("payment_email_check.py", tmp_path)
    assert rc == 1
    assert any("card data" in name for name in failed_checks(payload))


# --------------------------------------------------------------------------
# Gate U - code quality
# --------------------------------------------------------------------------

def test_code_quality_is_clean_for_the_good_app(good_app):
    rc, payload = run_gate("code_quality.py", good_app)
    assert rc == 0, payload


def test_code_quality_catches_an_empty_catch(broken_app):
    rc, payload = run_gate("code_quality.py", broken_app)
    assert rc == 1
    assert any("empty catch" in name for name in failed_checks(payload))


def test_code_quality_catches_a_mutable_default(tmp_path):
    (tmp_path / "m.py").write_text("def f(items={}):\n    return items\n")
    rc, payload = run_gate("code_quality.py", tmp_path)
    assert rc == 1
    assert any("mutable default" in name for name in failed_checks(payload))


def test_code_quality_measures_nesting(tmp_path):
    (tmp_path / "deep.js").write_text(
        "function a(){\n" + "  if (x) {\n" * 6 + "  }\n" * 6 + "}\n")
    rc, payload = run_gate("code_quality.py", tmp_path)
    assert rc == 1
    assert any("nesting" in name for name in failed_checks(payload))


def test_a_missing_absorbed_tool_is_a_warning_not_a_failure(tmp_path, monkeypatch, capsys):
    """An environment gap must never fail gate U.

    The absorbed linters exit non-zero both when they find problems and when
    the tool they drive is not installed. Only the first is a defect in the app.
    """
    import code_quality

    (tmp_path / "index.js").write_text("export const answer = 42;\n")

    def fake_run_absorbed(name, root, timeout=120):
        return {"available": True, "ok": False, "rc": 127,
                "detail": f"{name} exited 127",
                "json": {"checks": [{"passed": False,
                                     "error": "eslint: command not found"}]}}

    monkeypatch.setattr(code_quality, "run_absorbed", fake_run_absorbed)
    monkeypatch.setattr(sys, "argv",
                        ["code_quality.py", "--root", str(tmp_path), "--json"])
    rc = code_quality.main()
    payload = json.loads(capsys.readouterr().out)
    assert rc == 0, payload
    assert any("could not run" in c["name"] for c in payload["checks"])
    assert not [c for c in payload["checks"] if c["required"] and not c["ok"]]


# --------------------------------------------------------------------------
# mobile
# --------------------------------------------------------------------------

def test_mobile_check_requires_a_viewport(tmp_path):
    (tmp_path / "index.html").write_text("<html><body><h1>x</h1></body></html>")
    (tmp_path / "a.css").write_text("body{margin:0}")
    rc, payload = run_gate("mobile_check.py", tmp_path)
    assert rc == 1
    assert any("viewport" in name for name in failed_checks(payload))


def test_mobile_check_passes_the_good_app(good_app):
    rc, payload = run_gate("mobile_check.py", good_app)
    assert rc == 0, payload


# --------------------------------------------------------------------------
# flow_test
# --------------------------------------------------------------------------

def test_flow_test_is_skipped_without_a_spec(tmp_path):
    cmd = [sys.executable, str(SCRIPTS / "flow_test.py"), "--root", str(tmp_path),
           "--url", "http://127.0.0.1:9", "--json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    assert proc.returncode == 2
    assert json.loads(proc.stdout)["status"] == "skipped"


# --------------------------------------------------------------------------
# verify_claims - the new gates
# --------------------------------------------------------------------------

def test_gate_names_cover_all_twenty_one_gates():
    assert set(verify_claims.GATE_NAMES) == set("ABCDEFGHIJKLMNOPQRSTU")
    assert len(verify_claims.GATE_NAMES) == 21


def test_every_gate_has_a_verifier():
    for gate in verify_claims.GATE_NAMES:
        assert gate in verify_claims.VERIFIERS, gate


def test_true_claims_file_covers_every_gate():
    gates, _src = verify_claims.parse_claims(FIXTURES / "claims_true.json")
    assert set(gates) == set(verify_claims.GATE_NAMES)
    assert all(v == "PASS" for v in gates.values())


def test_false_claims_file_covers_every_gate():
    gates, _src = verify_claims.parse_claims(FIXTURES / "claims_false.md")
    assert set(gates) == set(verify_claims.GATE_NAMES)


def test_the_new_verifiers_reject_a_broken_app(broken_app):
    claims = {"gates": {g: "PASS" for g in ("N", "P", "Q", "R", "S", "T", "U")}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "test_timeout": 60, "artifact_dirs": []}
    report = verify_claims.verify(broken_app, claims, ctx)
    by_gate = {r["gate"]: r["verdict"] for r in report["results"]}
    for gate in ("N", "P", "Q", "R", "S", "T", "U"):
        assert by_gate[gate] in ("CONTRADICTED", "UNSUPPORTED"), (gate, by_gate[gate])
    assert report["status"] == "fail"


def test_the_new_verifiers_accept_the_good_app(good_app):
    """The machine half of the depth gates accepts the good app.

    N and Q are special: they need a human sign-off on top of the machine
    half, so without one they are UNVERIFIABLE (Q) or UNSUPPORTED (N, when
    there is no URL to execute the scenarios against).  The signed-off path
    is covered in test_signoff.py.
    """
    claims = {"gates": {g: "PASS" for g in ("N", "P", "Q", "R", "S", "T", "U")}}
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "test_timeout": 60, "artifact_dirs": []}
    report = verify_claims.verify(good_app, claims, ctx)
    by_gate = {r["gate"]: r["verdict"] for r in report["results"]}
    for gate in ("P", "R", "S", "T", "U"):
        assert by_gate[gate] == "VERIFIED", (gate, by_gate[gate])
    # N: no live URL -> the executable contract cannot be exercised
    assert by_gate["N"] == "UNSUPPORTED"
    # Q: the machine posture passes, but nobody has signed off the policy
    assert by_gate["Q"] == "UNVERIFIABLE"
    # an unsupported claim is not a pass, so the run cannot be green
    assert report["status"] == "fail"


# --------------------------------------------------------------------------
# verify_claims - gate verdicts that must never contradict themselves
# --------------------------------------------------------------------------

def _ctx(**kw):
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "test_timeout": 60, "artifact_dirs": []}
    ctx.update(kw)
    return ctx


def test_gate_k_verdict_matches_the_signals_found_in_the_source(good_app, broken_app):
    """Gate K used to report VERIFIED while its own advisory said the very
    same signal was missing. The verdict and the rule set must agree."""
    import absorbed_rules
    for app in (good_app, broken_app):
        verdict, evidence = verify_claims.verify_K(app, _ctx())
        present = absorbed_rules.observability_signals(app)
        if verdict == verify_claims.VERIFIED:
            assert len(present) >= 3
            for signal in present:
                assert signal in evidence, (signal, evidence)
        else:
            assert verdict == verify_claims.CONTRADICTED, verdict
            assert len(present) < 3


def test_gate_k_contradicts_a_project_without_observability_signals(tmp_path):
    (tmp_path / "app.js").write_text("function add(a, b) { return a + b; }\n",
                                     encoding="utf-8")
    verdict, evidence = verify_claims.verify_K(tmp_path, _ctx())
    assert verdict == verify_claims.CONTRADICTED
    assert "missing" in evidence


def test_gate_h_contradicts_a_project_that_ships_no_tests(tmp_path):
    """A project with no test command at all must not read as 'skipped'."""
    (tmp_path / "package.json").write_text(
        json.dumps({"name": "no-tests", "scripts": {"start": "node index.js"}}),
        encoding="utf-8")
    verdict, evidence = verify_claims.verify_H(tmp_path, _ctx(skip_tests=False))
    assert verdict == verify_claims.CONTRADICTED
    assert "no test suite" in evidence


def test_gate_h_contradicts_a_suite_that_runs_zero_tests(tmp_path):
    """`npm test` exiting 0 without running a single test is a defect, not a
    measurement gap - the project has no effective test suite."""
    (tmp_path / "package.json").write_text(
        json.dumps({"name": "empty-suite", "scripts": {"test": "node --test"}}),
        encoding="utf-8")
    (tmp_path / "index.js").write_text("console.log('hi');\n", encoding="utf-8")
    verdict, evidence = verify_claims.verify_H(tmp_path, _ctx(skip_tests=False))
    assert verdict in (verify_claims.CONTRADICTED, verify_claims.UNSUPPORTED), verdict
    if verdict == verify_claims.CONTRADICTED:
        assert "0 tests" in evidence


def test_gate_g_never_passes_a_route_that_never_answered(tmp_path):
    """SEO of a route that did not answer was never measured - that is a
    measurement gap, not a pass."""
    (tmp_path / "index.html").write_text("<html><body>hi</body></html>",
                                         encoding="utf-8")
    # port 9 (discard) is closed: the route can never answer.
    verdict, evidence = verify_claims.verify_G(
        tmp_path, _ctx(url="http://127.0.0.1:9", routes=["/"]))
    assert verdict == verify_claims.UNSUPPORTED, (verdict, evidence)
    assert "never answered" in evidence


def test_an_unsupported_gate_is_never_counted_as_a_pass(tmp_path):
    """Exit-code contract: a skipped/unmeasured gate is never green."""
    (tmp_path / "index.html").write_text("<html><body>hi</body></html>",
                                         encoding="utf-8")
    claims = {"gates": {"A": "PASS"}}
    report = verify_claims.verify(tmp_path, claims, _ctx())
    assert report["summary"]["verified"] == 0
    assert report["summary"]["unsupported"] == 1
    assert report["status"] == "fail"


def test_gate_e_is_skipped_when_the_dependency_cve_scan_cannot_run(tmp_path, monkeypatch):
    """A gate that could not be measured is never a pass.

    Gate E claims "zero HIGH vulnerabilities".  When the dependency CVE scan
    cannot run, that claim was not re-derived, so the gate must be
    UNSUPPORTED (skipped) rather than VERIFIED with a footnote.
    """
    (tmp_path / "package.json").write_text('{"name": "x", "version": "1.0.0"}',
                                           encoding="utf-8")
    import dep_audit
    monkeypatch.setattr(dep_audit, "audit", lambda *a, **k: {
        "status": "skipped", "scan_state": "unavailable",
        "reason": "npm is not installed", "findings": [],
    })
    verdict, evidence = verify_claims.verify_E(tmp_path, _ctx())
    assert verdict == verify_claims.UNSUPPORTED, (verdict, evidence)
    assert "CVE" in evidence


def test_gate_e_verifies_when_there_is_nothing_to_audit(tmp_path, monkeypatch):
    """No dependency manifest = nothing to audit = the gate can still be green."""
    import dep_audit
    monkeypatch.setattr(dep_audit, "audit", lambda *a, **k: {
        "status": "skipped", "scan_state": "not_applicable",
        "reason": "no recognised dependency manifest", "findings": [],
    })
    verdict, evidence = verify_claims.verify_E(tmp_path, _ctx())
    assert verdict == verify_claims.VERIFIED, (verdict, evidence)
    assert "no dependency manifest" in evidence


def test_gate_l_contradicts_a_readme_without_free_tier_limits(tmp_path):
    """The README IS the evidence for Gate L. A README that exists but does
    not document the limits is a DEFECT, not an unavailable measurement."""
    (tmp_path / "README.md").write_text("# Demo\n\nInstall and run it.\n",
                                        encoding="utf-8")
    verdict, evidence = verify_claims.verify_L(tmp_path, _ctx())
    assert verdict == verify_claims.CONTRADICTED, (verdict, evidence)
    assert "free-tier" in evidence


def test_gate_l_is_only_skipped_when_the_readme_is_missing(tmp_path):
    """No README at all = the evidence is unavailable = SKIPPED."""
    verdict, evidence = verify_claims.verify_L(tmp_path, _ctx())
    assert verdict == verify_claims.UNSUPPORTED, (verdict, evidence)
    assert "README" in evidence


def test_gate_l_verifies_a_readme_with_limits_and_a_fallback(tmp_path):
    (tmp_path / "README.md").write_text(
        "# Demo\n\n## Free tier and limits\n\n"
        "| Service | Free limit | When it breaks | Fallback |\n"
        "|---|---|---|---|\n| Vercel | 100 GB | over quota | self-host |\n",
        encoding="utf-8")
    verdict, evidence = verify_claims.verify_L(tmp_path, _ctx())
    assert verdict == verify_claims.VERIFIED, (verdict, evidence)


# --------------------------------------------------------------------------
# absorbed scripts
# --------------------------------------------------------------------------

def test_the_absorbed_manifest_is_intact():
    sys.path.insert(0, str(SCRIPTS / "absorbed"))
    import verify_manifest
    report = verify_manifest.verify()
    assert report["status"] == "ok", report
    assert report["checked"] >= 12


def test_every_absorbed_script_is_documented():
    manifest = json.loads((SCRIPTS / "absorbed" / "MANIFEST.json").read_text(encoding="utf-8"))
    readme = (SCRIPTS / "absorbed" / "README.md").read_text(encoding="utf-8")
    files = manifest["files"]
    names = list(files) if isinstance(files, dict) else [e["file"] for e in files]
    for name in names:
        assert name in readme, name


# --------------------------------------------------------------------------
# fixture
# --------------------------------------------------------------------------

def test_the_good_fixture_carries_the_new_surfaces(good_app):
    for rel in ("locales/en.json", "locales/fr.json", "privacy.md",
                "db/migrate/001_init.sql", "db/migrate/001_init.down.sql",
                "db/schema.sql", "qa/scenarios.json", "src/i18n.js",
                "src/payments.js", "src/mailer.js", "src/index.html",
                "src/styles.css"):
        assert (good_app / rel).is_file(), rel


def test_the_broken_fixture_carries_the_new_defects(broken_app):
    assert (broken_app / "db" / "migrate" / "002_cleanup.sql").is_file()
    assert "DROP TABLE" in (broken_app / "db" / "migrate" / "002_cleanup.sql").read_text()
    legacy = (broken_app / "src" / "legacy.js").read_text(encoding="utf-8")
    assert "catch (err) {" in legacy
    assert "sk_live_" in legacy
