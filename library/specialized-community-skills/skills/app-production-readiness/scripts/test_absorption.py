"""Tests for the newly absorbed sibling-skill knowledge (Phase 9).

Covers:
  * ``web_guidelines.py``  - the machine-checkable subset of the Vercel Web
    Interface Guidelines (absorbed from the ``web-design-guidelines`` skill).
  * ``absorbed_rules.py``  - the checkable rules of the doc-only sibling skills
    (api-contract-testing, security-hardened-api, observability-and-instrumentation,
    microservices-resilience, ai-debt-detector, property-based-testing,
    mutation-testing).

Exit-code contract under test: 1 = a real high-severity finding, 0 = only
medium findings, 2 = the rules could not be loaded (never a pass).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import absorbed_rules  # noqa: E402
import web_guidelines  # noqa: E402


# --------------------------------------------------------------------------- helpers
def _write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _rules_for(findings: list[dict], file_label: str) -> list[str]:
    return [f["rule"] for f in findings if f.get("file") == file_label]


def _types(findings: list[dict]) -> str:
    return " ".join(str(f.get("type", "")).lower() for f in findings)


# --------------------------------------------------------------------------- web guidelines
def test_a_missing_image_alt_is_a_high_finding(tmp_path: Path):
    _write(tmp_path / "src" / "page.tsx", 'export const A = () => <img src="/logo.png" />;\n')
    result = web_guidelines.analyse(tmp_path)
    assert result["high"] >= 1, result
    rules = _rules_for(result["findings"], "src/page.tsx")
    assert any("img" in r or "alt" in r for r in rules), rules


def test_an_unlabelled_input_is_a_high_finding(tmp_path: Path):
    _write(tmp_path / "src" / "form.tsx", 'export const F = () => <input type="text" />;\n')
    result = web_guidelines.analyse(tmp_path)
    high = [f for f in result["findings"] if f.get("file") == "src/form.tsx" and f["severity"] == "high"]
    assert high, result
    rules = _rules_for(result["findings"], "src/form.tsx")
    assert any("input" in r or "label" in r for r in rules), rules


def test_eval_is_a_high_finding(tmp_path: Path):
    _write(tmp_path / "src" / "run.js", "export const run = (x) => eval(x);\n")
    result = web_guidelines.analyse(tmp_path)
    rules = _rules_for(result["findings"], "src/run.js")
    assert any("eval" in r for r in rules), rules


def test_a_clean_file_produces_no_high_finding(tmp_path: Path):
    _write(tmp_path / "src" / "ok.ts", "export function add(a: number, b: number) {\n  return a + b;\n}\n")
    result = web_guidelines.analyse(tmp_path)
    assert result["high"] == 0, result
    assert result["files_checked"] == 1


def test_only_medium_findings_still_exit_zero(tmp_path: Path):
    # an image with an alt but without width/height is a medium (layout shift) finding
    _write(tmp_path / "src" / "pic.tsx", 'export const A = () => <img src="/x.png" alt="Logo" />;\n')
    result = web_guidelines.analyse(tmp_path)
    assert result["high"] == 0, result
    assert result["medium"] >= 1, result
    assert web_guidelines.main(["--root", str(tmp_path)]) == 0


def test_a_high_finding_exits_one(tmp_path: Path):
    _write(tmp_path / "src" / "bad.tsx", 'export const A = () => <img src="/x.png" />;\n')
    assert web_guidelines.main(["--root", str(tmp_path)]) == 1


def test_missing_rules_exit_two_instead_of_a_pass(tmp_path: Path, monkeypatch):
    monkeypatch.setattr(web_guidelines, "load_rules_text", lambda refresh=False: (None, ""))
    _write(tmp_path / "src" / "x.tsx", 'export const A = () => <img src="/x.png" />;\n')
    assert web_guidelines.main(["--root", str(tmp_path)]) == 2


def test_the_manual_checklist_is_part_of_the_result(tmp_path: Path):
    result = web_guidelines.analyse(tmp_path)
    assert result["manual_checks"], "the human-only checklist must never be lost"


# --------------------------------------------------------------------------- absorbed rules
def test_api_contract_findings_flag_api_routes_without_a_contract(tmp_path: Path):
    _write(tmp_path / "package.json", json.dumps({"name": "x", "dependencies": {"express": "^4"}}))
    _write(tmp_path / "src" / "app" / "api" / "items" / "route.ts", 'export const route = "/api/items";\n')
    findings = absorbed_rules.api_contract_findings(tmp_path)
    assert any("contract" in f["type"].lower() for f in findings), findings


def test_api_hardening_findings_flag_a_missing_rate_limit(tmp_path: Path):
    _write(tmp_path / "package.json", json.dumps({"name": "x", "dependencies": {"express": "^4"}}))
    _write(tmp_path / "src" / "server.js", "const express = require('express');\napp.listen(3000);\n")
    findings = absorbed_rules.api_hardening_findings(tmp_path)
    assert any("rate limit" in f["type"].lower() for f in findings), findings


def test_api_hardening_findings_flag_wildcard_cors_with_credentials(tmp_path: Path):
    _write(tmp_path / "package.json", json.dumps({"name": "x", "dependencies": {"express": "^4"}}))
    _write(
        tmp_path / "src" / "server.js",
        "app.listen(3000);\n"
        'res.setHeader("access-control-allow-origin", "*");\n'
        'res.setHeader("access-control-allow-credentials", "true");\n',
    )
    findings = absorbed_rules.api_hardening_findings(tmp_path)
    assert any(f["severity"] == "HIGH" for f in findings), findings


def test_ai_debt_findings_catch_todos_and_commented_out_code(tmp_path: Path):
    _write(tmp_path / "src" / "a.js", "// TODO: remove this\n// const x = 1;\n")
    findings = absorbed_rules.ai_debt_findings(tmp_path)
    assert len(findings) >= 2, findings
    assert "commented-out" in _types(findings), findings
    assert all(f["severity"] == "LOW" for f in findings), findings


def test_test_quality_findings_ask_for_property_based_tests(tmp_path: Path):
    _write(tmp_path / "package.json", json.dumps({"name": "x", "scripts": {"test": "jest"}}))
    _write(tmp_path / "tests" / "a.test.ts", "test('a', () => {});\n")
    findings = absorbed_rules.test_quality_findings(tmp_path)
    assert any(f["severity"] == "LOW" for f in findings), findings


def test_observability_and_resilience_report_the_missing_signals(tmp_path: Path):
    _write(tmp_path / "package.json", json.dumps({"name": "x", "dependencies": {"express": "^4"}}))
    _write(tmp_path / "src" / "server.js", "app.listen(3000);\n")
    obs = absorbed_rules.observability_findings(tmp_path)
    res = absorbed_rules.resilience_findings(tmp_path)
    assert obs and res, (obs, res)
    assert all(f["severity"] == "LOW" for f in obs + res), (obs, res)


# --------------------------------------------------------------------------- regressions
def test_files_whose_name_contains_out_are_not_skipped(tmp_path: Path):
    """Regression: a substring skip-check silently dropped route.ts / about.ts.

    ``route`` contains "out", and "out" is a skip marker - so every API route
    file was invisible to the absorbed rule families.
    """
    _write(tmp_path / "package.json", json.dumps({"name": "x", "dependencies": {"express": "^4"}}))
    _write(tmp_path / "src" / "app" / "api" / "items" / "route.ts", 'export const route = "/api/items";\n')
    _write(tmp_path / "src" / "about.ts", "export const about = 1;\n")
    found = [p.name for p in absorbed_rules._files(tmp_path, absorbed_rules.CODE_EXT)]
    assert "route.ts" in found, found
    assert "about.ts" in found, found


def test_ui_files_whose_name_contains_out_are_not_skipped(tmp_path: Path):
    _write(tmp_path / "src" / "layout.tsx", "export const L = () => null;\n")
    _write(tmp_path / "src" / "checkout.tsx", "export const C = () => null;\n")
    found = [p.name for p in web_guidelines.iter_ui_files(tmp_path)]
    assert "layout.tsx" in found, found
    assert "checkout.tsx" in found, found

