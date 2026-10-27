#!/usr/bin/env python3
"""Direct unit tests for the checkers whose rules are otherwise only reached
through a subprocess.

``verify_claims._rerun_gate()`` runs the gate checkers as child processes, so
``coverage.py`` never sees inside them: six checkers reported 0% coverage even
though the suites exercise them.  These tests call the rule functions
themselves, which pins the behaviour that actually matters - which finding is
raised, and which positive property is confirmed - instead of only the exit
code of the CLI.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import i18n_check  # noqa: E402
import migration_check  # noqa: E402
import mobile_check  # noqa: E402
import payment_email_check  # noqa: E402
import privacy_check  # noqa: E402
import scan_workspace  # noqa: E402


# ---------------------------------------------------------------------------
# i18n_check
# ---------------------------------------------------------------------------

def test_flatten_adds_the_parent_and_the_dotted_child():
    keys = i18n_check._flatten({"a": {"b": 1}, "c": 2})
    assert keys == {"a", "a.b", "c"}


def test_catalog_keys_unwraps_a_translations_dictionary(tmp_path):
    path = tmp_path / "en.json"
    path.write_text(json.dumps({"translations": {"hello": "Hi", "bye": "Bye"}}),
                    encoding="utf-8")
    assert i18n_check._catalog_keys(path) == {"hello", "bye"}


def test_catalog_keys_reads_yaml_catalogue_keys(tmp_path):
    path = tmp_path / "fr.yaml"
    path.write_text("hello: Bonjour\nbye: Au revoir\n", encoding="utf-8")
    assert i18n_check._catalog_keys(path) == {"hello", "bye"}


def test_language_of_uses_the_first_two_letter_tag(tmp_path):
    assert i18n_check._language_of(tmp_path / "en.json") == "en"
    assert i18n_check._language_of(tmp_path / "fr-CA.json") == "fr"


def test_find_catalogs_finds_every_locale_folder(tmp_path):
    (tmp_path / "locales").mkdir()
    (tmp_path / "locales" / "en.json").write_text("{}", encoding="utf-8")
    (tmp_path / "i18n").mkdir()
    (tmp_path / "i18n" / "de.yaml").write_text("a: 1", encoding="utf-8")
    found = {p.name for p in i18n_check.find_catalogs(tmp_path)}
    assert found == {"en.json", "de.yaml"}


def test_a_catalogue_missing_a_key_is_reported(tmp_path):
    import io
    import contextlib
    loc = tmp_path / "locales"
    loc.mkdir()
    (loc / "en.json").write_text(json.dumps({"a": 1, "b": 2}), encoding="utf-8")
    (loc / "fr.json").write_text(json.dumps({"a": 1}), encoding="utf-8")
    argv = sys.argv
    sys.argv = ["i18n_check.py", "--root", str(tmp_path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            rc = i18n_check.main()
    finally:
        sys.argv = argv
    assert rc == 1, "a catalogue that lost a key must fail the gate"


# ---------------------------------------------------------------------------
# migration_check
# ---------------------------------------------------------------------------

def _migration(tmp_path, name, body):
    d = tmp_path / "db" / "migrate"
    d.mkdir(parents=True, exist_ok=True)
    (d / name).write_text(body, encoding="utf-8")
    return d / name


def test_find_migrations_finds_the_sql_files(tmp_path):
    _migration(tmp_path, "001_init.sql", "CREATE TABLE t (id INT);")
    assert [p.name for p in migration_check.find_migrations(tmp_path)] == ["001_init.sql"]


def test_a_migration_without_a_rollback_is_high(tmp_path):
    _migration(tmp_path, "001_init.sql", "CREATE TABLE t (id INT);")
    _migrations, findings, _schema = migration_check.analyse(tmp_path)
    assert any(f["severity"] == "HIGH" and "no rollback" in f["check"] for f in findings)


def test_a_down_migration_satisfies_the_rollback_rule(tmp_path):
    _migration(tmp_path, "001_init.sql", "CREATE TABLE IF NOT EXISTS t (id INT);")
    _migration(tmp_path, "001_init_down.sql", "DROP TABLE IF EXISTS t;")
    _migrations, findings, _schema = migration_check.analyse(tmp_path)
    assert not any("no rollback" in f["check"] for f in findings)


def test_a_destructive_statement_is_reported(tmp_path):
    _migration(tmp_path, "001_init.sql", "CREATE TABLE IF NOT EXISTS t (id INT);")
    _migration(tmp_path, "002_drop.sql", "DROP TABLE t;")
    _migrations, findings, _schema = migration_check.analyse(tmp_path)
    assert any(f["severity"] in ("HIGH", "MEDIUM") and "unguarded" in f["check"]
               for f in findings)


def test_a_non_idempotent_create_is_reported(tmp_path):
    _migration(tmp_path, "001_init.sql", "CREATE TABLE t (id INT);")
    _migrations, findings, _schema = migration_check.analyse(tmp_path)
    assert any("non-idempotent" in f["check"] for f in findings)


def test_analyse_reports_the_schema_file(tmp_path):
    _migration(tmp_path, "001_init.sql", "CREATE TABLE IF NOT EXISTS t (id INT);")
    (tmp_path / "db").mkdir(exist_ok=True)
    (tmp_path / "db" / "schema.sql").write_text("CREATE TABLE t (id INT);", encoding="utf-8")
    _migrations, _findings, schema_files = migration_check.analyse(tmp_path)
    assert "db/schema.sql" in schema_files


# ---------------------------------------------------------------------------
# mobile_check
# ---------------------------------------------------------------------------

def test_a_small_button_is_reported():
    found, small = mobile_check._touch_targets([(Path("a.css"), "button { width: 32px; }")])
    assert found == 1
    assert small and "32px" in small[0]


def test_a_comfortable_button_is_not_reported():
    found, small = mobile_check._touch_targets(
        [(Path("a.css"), "button { min-height: 44px; }")])
    assert found == 1
    assert small == []


def test_a_non_interactive_selector_is_ignored():
    # ".card" contains the letter "a" but it is not an interactive control.
    found, small = mobile_check._touch_targets([(Path("a.css"), ".card { width: 10px; }")])
    assert found == 0
    assert small == []


def test_a_role_button_is_an_interactive_target():
    found, _small = mobile_check._touch_targets(
        [(Path("a.css"), '[role="button"] { width: 10px; }')])
    assert found == 1


def test_a_thin_vertical_padding_is_reported():
    found, small = mobile_check._touch_targets(
        [(Path("a.css"), "a.btn { padding: 2px 4px; }")])
    assert found == 1
    assert small and "padding" in small[0]


# ---------------------------------------------------------------------------
# privacy_check
# ---------------------------------------------------------------------------

def test_a_logged_email_is_flagged(tmp_path):
    (tmp_path / "app.js").write_text("console.log('user', user.email);\n", encoding="utf-8")
    hits = privacy_check._logged_pii(tmp_path)
    assert hits and "email" in hits[0]


def test_a_stored_card_number_is_flagged(tmp_path):
    (tmp_path / "app.js").write_text(
        "localStorage.setItem('card_number', value);\n", encoding="utf-8")
    assert privacy_check._storage_pii(tmp_path)


def test_a_clean_file_is_not_flagged(tmp_path):
    (tmp_path / "app.js").write_text("console.log('server started');\n", encoding="utf-8")
    assert privacy_check._logged_pii(tmp_path) == []
    assert privacy_check._storage_pii(tmp_path) == []


# ---------------------------------------------------------------------------
# scan_workspace
# ---------------------------------------------------------------------------

def test_is_app_detects_a_node_project(tmp_path):
    (tmp_path / "package.json").write_text("{}", encoding="utf-8")
    assert scan_workspace.is_app(tmp_path) is True


def test_is_app_ignores_an_empty_directory(tmp_path):
    assert scan_workspace.is_app(tmp_path) is False


def test_the_workspace_scan_lists_the_apps(tmp_path, capsys):
    app = tmp_path / "my-app"
    app.mkdir()
    (app / "package.json").write_text("{}", encoding="utf-8")
    (app / "README.md").write_text("# hi", encoding="utf-8")
    argv = sys.argv
    sys.argv = ["scan_workspace.py", str(tmp_path)]
    try:
        rc = scan_workspace.main()
    finally:
        sys.argv = argv
    payload = json.loads(capsys.readouterr().out)
    assert rc == 0
    assert payload["count"] == 1
    assert payload["apps"][0]["name"] == "my-app"
    assert payload["apps"][0]["has_readme"] is True


# ---------------------------------------------------------------------------
# payment_email_check
# ---------------------------------------------------------------------------

STRIPE_SOURCE = (
    "const stripe = require('stripe');\n"
    "app.post('/webhook', (req, res) => {\n"
    "  const event = stripe.webhooks.constructEvent(req.body, sig, secret);\n"
    "  stripe.payments.create({ unit_amount: 1000, currency: 'usd' },\n"
    "    { idempotencyKey: 'k' });\n"
    "});\n"
)


def _source(tmp_path, name, text):
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return [(path, text)]


def test_a_card_number_literal_is_high(tmp_path):
    files = _source(tmp_path, "pay.js", "const card_number = '4242424242424242';\n")
    blob = files[0][1]
    findings = payment_email_check.analyse_payments(tmp_path, blob, files)
    assert any(sev == "HIGH" and "card number literal" in check
               for sev, check, _detail in findings)


def test_a_verified_stripe_webhook_confirms_the_positive_properties(tmp_path):
    files = _source(tmp_path, "pay.js", STRIPE_SOURCE)
    blob = files[0][1]
    props = dict(payment_email_check.payment_positives(tmp_path, blob, files))
    assert "a payment provider is used" in props
    assert "the webhook signature is verified" in props
    assert "the payment carries an explicit currency" in props
    assert "amounts use integer minor units" in props
    assert "the payment call carries an idempotency key" in props


def test_an_unverified_webhook_is_high(tmp_path):
    files = _source(tmp_path, "pay.js",
                    "const stripe = require('stripe');\n"
                    "app.post('/webhook', (req, res) => { res.json({ ok: true }); });\n")
    blob = files[0][1]
    findings = payment_email_check.analyse_payments(tmp_path, blob, files)
    assert any(sev == "HIGH" and "does not verify its signature" in check
               for sev, check, _detail in findings)


def test_a_project_without_payments_says_so(tmp_path):
    files = _source(tmp_path, "app.js", "console.log('hello');\n")
    blob = files[0][1]
    findings = payment_email_check.analyse_payments(tmp_path, blob, files)
    assert any(sev == "INFO" and "no payment provider detected" in check
               for sev, check, _detail in findings)


def test_a_project_without_mail_says_so(tmp_path):
    files = _source(tmp_path, "app.js", "console.log('hello');\n")
    blob = files[0][1]
    findings = payment_email_check.analyse_email(tmp_path, blob, files)
    assert any(sev == "INFO" and "no transactional email provider detected" in check
               for sev, check, _detail in findings)


def test_a_hardcoded_provider_key_is_high(tmp_path):
    files = _source(tmp_path, "pay.js",
                    "const key = 'sk_live_51H8xQ2eZvKYlo2Cabcdefghij';\n")
    blob = files[0][1]
    findings = payment_email_check.analyse_payments(tmp_path, blob, files)
    assert any(sev == "HIGH" and "hardcoded payment/email credential" in check
               for sev, check, _detail in findings)
