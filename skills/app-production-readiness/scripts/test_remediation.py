#!/usr/bin/env python3
"""Unit and regression tests for the Autonomous Remediation Engine."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remediate
import remediation_handlers as rh
import fixes


@pytest.fixture
def test_app(tmp_path):
    """Create a minimal project fixture with intentional issues."""
    app_dir = tmp_path / "mock_app"
    app_dir.mkdir()

    # CSS with missing focus / touch targets
    css_dir = app_dir / "src" / "styles"
    css_dir.mkdir(parents=True)
    (css_dir / "components.css").write_text(".btn { color: red; }\n", encoding="utf-8")

    # JS with empty catch & innerHTML
    js_dir = app_dir / "src" / "components"
    js_dir.mkdir(parents=True)
    sample_js = (
        "function test() {\n"
        "  try {\n"
        "    const x = 1;\n"
        "  } catch (err) {}\n"
        "  const elem = document.getElementById('msg');\n"
        "  elem.innerHTML = 'Hello World';\n"
        "}\n"
    )
    (js_dir / "sample.js").write_text(sample_js, encoding="utf-8")

    # HTML with icon button missing aria-label
    html_content = '<button id="btn-menu"><svg></svg></button>'
    (app_dir / "index.html").write_text(html_content, encoding="utf-8")

    # Mock qa/report.md
    qa_dir = app_dir / "qa"
    qa_dir.mkdir()
    report = (
        "# Production-readiness review\n\n"
        "## BLOCKERS\n"
        "* **U** - code_quality.py: function is too long: src/components/sample.js:1 test() is 120 lines\n"
        "* **E** - security_scan.py: innerHTML assignment (src/components/sample.js:6)\n"
    )
    (qa_dir / "report.md").write_text(report, encoding="utf-8")

    return app_dir


def test_remediate_touch_targets(test_app):
    res = rh.remediate_touch_targets(test_app)
    assert res["status"] == "applied"
    css_content = (test_app / "src" / "styles" / "components.css").read_text(encoding="utf-8")
    assert "min-height: 44px" in css_content


def test_remediate_focus_visible(test_app):
    res = rh.remediate_focus_visible(test_app)
    assert res["status"] == "applied"
    css_content = (test_app / "src" / "styles" / "components.css").read_text(encoding="utf-8")
    assert ":focus-visible" in css_content


def test_remediate_empty_catch(test_app):
    res = rh.remediate_empty_catch(test_app, "src/components/sample.js")
    assert res["status"] == "applied"
    js_content = (test_app / "src" / "components" / "sample.js").read_text(encoding="utf-8")
    assert 'console.error("Unhandled error caught:", err)' in js_content


def test_remediate_xss_innerhtml(test_app):
    res = rh.remediate_xss_innerhtml(test_app, "src/components/sample.js", line_no=6)
    assert res["status"] == "applied"
    js_content = (test_app / "src" / "components" / "sample.js").read_text(encoding="utf-8")
    assert "elem.textContent = 'Hello World'" in js_content


def test_remediate_aria_label(test_app):
    res = rh.remediate_aria_label(test_app, "index.html")
    assert res["status"] == "applied"
    html_content = (test_app / "index.html").read_text(encoding="utf-8")
    assert 'aria-label="Menu"' in html_content


def test_generate_agent_recipe(test_app):
    recipe_rel = rh.generate_agent_recipe(
        test_app, "U", "src/components/sample.js", 1, "function_too_long", "test() is 120 lines"
    )
    recipe_path = test_app / recipe_rel
    assert recipe_path.is_file()
    content = recipe_path.read_text(encoding="utf-8")
    assert "test() is 120 lines" in content
    assert "Recommended Refactoring Instructions" in content


def test_rollback_session(test_app):
    target = test_app / "src" / "components" / "sample.js"
    orig_content = target.read_text(encoding="utf-8")
    rh.backup_file(test_app, target, session_id="latest")
    target.write_text("corrupted content", encoding="utf-8")

    restored = remediate.rollback_session(test_app, session_id="latest")
    assert restored == 1
    assert target.read_text(encoding="utf-8") == orig_content


def test_a_dry_run_never_claims_a_recipe_was_created(test_app):
    res = remediate.remediate_app(test_app, dry_run=True)
    assert res["dry_run"] is True
    assert res["recipes"], "the fixture report should produce at least one recipe"
    recipe_actions = [a for a in res["actions"] if a["category"] == "recipe"]
    assert recipe_actions
    assert all(a["status"] == "recipe_planned" for a in recipe_actions)
    assert all("Would generate" in a["detail"] for a in recipe_actions)
    assert not (test_app / "qa" / "recipes").exists()
    assert not (test_app / "qa" / "remediation-log.md").exists()


def test_full_remediate_cli(test_app):
    res = remediate.remediate_app(test_app)
    assert res["ok"] is True
    assert res["applied_count"] >= 1
    assert len(res["recipes"]) >= 1
    assert (test_app / "qa" / "remediation-log.md").is_file()


# ---------------------------------------------------------------------------
# safety regressions - every one of these used to be a real defect
# ---------------------------------------------------------------------------

def _snapshot(root: Path) -> dict:
    return {str(p): p.read_bytes() for p in sorted(root.rglob("*")) if p.is_file()}


def test_dry_run_never_touches_the_project(test_app):
    """--dry-run must not modify a single byte."""
    before = _snapshot(test_app)
    res = remediate.remediate_app(test_app, dry_run=True)
    assert res["dry_run"] is True
    assert res["applied_count"] == 0
    assert res["planned_count"] >= 1
    assert _snapshot(test_app) == before, "dry run modified the project"


def test_mechanical_fixes_support_dry_run(test_app):
    before = _snapshot(test_app)
    results = fixes.apply_all(test_app, dry_run=True)
    assert _snapshot(test_app) == before
    assert not any(r.get("status") == "applied" for r in results)
    assert any(r.get("status") == "planned" for r in results)


def test_a_failing_remediation_is_reported_and_fails_the_run(test_app, monkeypatch):
    monkeypatch.setattr(rh, "remediate_xss_innerhtml",
                        lambda *a, **k: {"id": "sec_xss_innerhtml", "status": "failed",
                                         "detail": "boom"})
    res = remediate.remediate_app(test_app)
    assert res["ok"] is False
    assert res["failed_count"] >= 1
    assert remediate.main(["--root", str(test_app)]) == 1


def test_a_path_outside_the_project_is_refused(test_app):
    outside = test_app.parent / "outside.js"
    outside.write_text("const secret = 1;\n", encoding="utf-8")
    res = rh.remediate_xss_innerhtml(test_app, "../outside.js")
    assert res["status"] == "skipped"
    assert "outside the project root" in res["detail"]
    assert outside.read_text(encoding="utf-8") == "const secret = 1;\n"


def test_cors_codemod_never_rewrites_a_json_file(test_app):
    """A JSON config must not receive JavaScript."""
    config = test_app / "src" / "config.json"
    config.write_text('{"Access-Control-Allow-Origin": "*"}', encoding="utf-8")
    res = rh.remediate_cors_wildcard(test_app, "src/config.json")
    assert res["status"] == "manual"
    assert config.read_text(encoding="utf-8") == '{"Access-Control-Allow-Origin": "*"}'


def test_cors_codemod_uses_the_allowlist_when_one_exists(test_app):
    source = test_app / "src" / "server.js"
    source.write_text(
        "const ALLOWED_ORIGINS = ['https://a.example'];\n"
        "app.use((req, res, next) => {\n"
        "  res.setHeader('Access-Control-Allow-Origin', '*');\n"
        "  res.setHeader('X-Other', '*');\n"
        "  next();\n"
        "});\n", encoding="utf-8")
    res = rh.remediate_cors_wildcard(test_app, "src/server.js")
    assert res["status"] == "applied"
    text = source.read_text(encoding="utf-8")
    assert "ALLOWED_ORIGINS.includes(req.headers.origin)" in text
    assert "'X-Other', '*'" in text, "an unrelated header must not be touched"


def test_cors_codemod_defers_when_the_allowlist_is_unknown(test_app):
    source = test_app / "src" / "server.js"
    source.write_text("res.setHeader('Access-Control-Allow-Origin', '*');\n", encoding="utf-8")
    res = rh.remediate_cors_wildcard(test_app, "src/server.js")
    assert res["status"] == "manual"
    assert res.get("recipe")
    assert source.read_text(encoding="utf-8") == "res.setHeader('Access-Control-Allow-Origin', '*');\n"


def test_typescript_empty_catch_stays_valid(test_app):
    source = test_app / "src" / "app.ts"
    source.write_text("try { work(); } catch (e: unknown) {}\n", encoding="utf-8")
    res = rh.remediate_empty_catch(test_app, "src/app.ts")
    assert res["status"] == "applied"
    text = source.read_text(encoding="utf-8")
    assert 'catch (e) { console.error("Unhandled error caught:", e); }' in text
    assert "e: unknown" not in text
    assert rh.validate_syntax(source, text)


def test_only_the_matched_innerhtml_assignment_is_rewritten(test_app):
    source = test_app / "src" / "app.js"
    source.write_text(
        "a.innerHTML = 'plain'; b.innerHTML = '<b>html</b>';\n"
        "const s = \"el.innerHTML = 'in a string'\";\n", encoding="utf-8")
    res = rh.remediate_xss_innerhtml(test_app, "src/app.js")
    assert res["status"] == "applied"
    text = source.read_text(encoding="utf-8")
    assert "a.textContent = 'plain';" in text
    assert "b.innerHTML = '<b>html</b>';" in text
    assert "el.innerHTML = 'in a string'" in text, "a string literal must not be rewritten"


def test_the_pristine_backup_is_kept(test_app):
    target = test_app / "src" / "components" / "sample.js"
    original = target.read_text(encoding="utf-8")
    rh.remediate_xss_innerhtml(test_app, "src/components/sample.js", line_no=6)
    rh.remediate_xss_innerhtml(test_app, "src/components/sample.js", line_no=6)
    remediate.rollback_session(test_app, session_id="latest")
    assert target.read_text(encoding="utf-8") == original


def test_line_endings_survive_a_remediation(test_app):
    source = test_app / "src" / "crlf.js"
    source.write_bytes(b"const a = 1;\r\nel.innerHTML = 'x';\r\n")
    rh.remediate_xss_innerhtml(test_app, "src/crlf.js")
    raw = source.read_bytes()
    assert b"\r\n" in raw
    assert b"\n\n" not in raw.replace(b"\r\n", b"")
    assert b"el.textContent = 'x';" in raw


def test_rollback_without_a_session_is_an_error(test_app):
    assert remediate.main(["--root", str(test_app), "--rollback"]) == 1


def test_an_unlabelled_button_gets_an_aria_label(test_app):
    html = test_app / "page.html"
    html.write_text('<button id="btn-menu" data-x="a>b"><svg></svg></button>', encoding="utf-8")
    res = rh.remediate_aria_label(test_app, "page.html")
    assert res["status"] == "applied"
    text = html.read_text(encoding="utf-8")
    assert 'aria-label="Menu"' in text
    assert 'data-x="a>b"' in text, "an attribute containing > must survive"


def test_the_security_scan_ignores_the_remediation_backups(test_app):
    """The engine's own backups must never be reported as live findings."""
    import security_scan

    target = test_app / "src" / "components" / "sample.js"
    target.write_text("const key = 'sk_live_51Hxxxxxxxxxxxxxxxxxxxxxx';\n", encoding="utf-8")
    rh.backup_file(test_app, target)
    findings = security_scan.scan_all(test_app)
    assert findings, "the secret in the source file must still be found"
    assert not any("fix-backup" in f["file"] for f in findings), findings


def test_missing_seo_metadata_is_scaffolded(test_app):
    page = test_app / "index.html"
    page.write_text(
        "<!doctype html><html><head><title>Widget store</title></head>"
        "<body><h1>Widgets</h1><p>Buy the best widgets online.</p></body></html>",
        encoding="utf-8")
    res = rh.remediate_seo_meta_tags(test_app, "index.html")
    assert res["status"] == "applied"
    text = page.read_text(encoding="utf-8")
    assert '<meta name="description" content="Buy the best widgets online.">' in text
    assert '<meta property="og:title" content="Widget store">' in text
    assert "twitter:card" in text
    assert "<title>Widget store</title>" in text, "the title must survive"
    # a second pass is a no-op
    assert rh.remediate_seo_meta_tags(test_app, "index.html")["status"] == "already-ok"

