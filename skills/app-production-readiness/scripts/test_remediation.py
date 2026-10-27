#!/usr/bin/env python3
"""Unit and regression tests for the Autonomous Remediation Engine."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remediate
import remediation_handlers as rh


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


def test_full_remediate_cli(test_app):
    res = remediate.remediate_app(test_app)
    assert res["ok"] is True
    assert res["applied_count"] >= 1
    assert len(res["recipes"]) >= 1
    assert (test_app / "qa" / "remediation-log.md").is_file()
