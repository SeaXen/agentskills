#!/usr/bin/env python3
"""Documentation-consistency tests.

The skill's value depends on its docs matching what the scripts actually do.
These tests fail when a script is added without being documented, when a
reference file is orphaned, when a documented number drifts, or when the
report format in SKILL.md stops being machine-readable by verify_claims.py.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = ROOT / "SKILL.md"
REFERENCES = ROOT / "references"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_claims import GATE_NAMES, parse_claims  # noqa: E402


@pytest.fixture(scope="module")
def skill_text() -> str:
    return SKILL_MD.read_text(encoding="utf-8")


def _pytest_count(path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", str(path), "--collect-only", "-q"],
        cwd=str(ROOT), capture_output=True, text=True,
    )
    m = re.search(r"(\d+)\s+tests?\s+collected", proc.stdout)
    assert m, f"could not count tests in {path.name}: {proc.stdout[-500:]}"
    return int(m.group(1))


def test_every_script_is_documented(skill_text):
    scripts = sorted(
        p.name for p in (ROOT / "scripts").glob("*.py")
        if not p.name.startswith("test_")
    )
    assert scripts, "no scripts found"
    missing = [name for name in scripts if name not in skill_text]
    assert not missing, f"scripts not mentioned in SKILL.md: {missing}"


def test_every_reference_is_linked(skill_text):
    refs = sorted(p.name for p in REFERENCES.glob("*.md"))
    assert refs, "no reference docs found"
    missing = [name for name in refs if name not in skill_text]
    assert not missing, f"reference docs not linked from SKILL.md: {missing}"


def test_no_stale_check_count(skill_text):
    """The preflight check count must be stated and consistent across the docs."""
    assert "24 checks" not in skill_text, "SKILL.md still claims the old 24-check preflight"
    assert "30 checks" not in skill_text, "SKILL.md still claims the old 30-check preflight"
    m = re.search(r"Production-readiness checks \(\*\*(\d+) checks\*\*", skill_text)
    assert m, "SKILL.md does not state the preflight check count"
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    r = re.search(r"File/config preflight \(up to (\d+) checks\)", readme)
    assert r, "README.md does not state the preflight check count"
    assert m.group(1) == r.group(1), (
        f"SKILL.md says {m.group(1)} preflight checks, README.md says {r.group(1)}")


def test_the_documented_preflight_count_matches_the_script(tmp_path):
    """The number in the docs must be the number the script really reports."""
    sys.path.insert(0, str(ROOT / "scripts"))
    sys.path.insert(0, str(ROOT / "scripts" / "fixtures"))
    import preflight
    from make_sample_app import build as build_sample_app

    app = tmp_path / "good"
    build_sample_app(app, variant="good")
    actual = len(preflight.run(app))
    documented = int(re.search(
        r"Production-readiness checks \(\*\*(\d+) checks\*\*",
        SKILL_MD.read_text(encoding="utf-8")).group(1))
    assert actual == documented, (
        f"preflight reports {actual} checks, the docs claim {documented}")


def test_documented_test_counts_match(skill_text):
    """The numbers in the self-test block must match what pytest collects.

    Every suite in ``scripts/`` is checked - a new suite that nobody
    documented (or a count that drifted) fails here.
    """
    suites = sorted(p.name for p in (ROOT / "scripts").glob("test_*.py"))
    assert suites, "no test suites found"
    for suite in suites:
        m = re.search(rf"scripts/{re.escape(suite)}[^\n]*#\s*(\d+)\s*tests", skill_text)
        assert m, f"SKILL.md does not document the test count for {suite}"
        documented = int(m.group(1))
        actual = _pytest_count(ROOT / "scripts" / suite)
        assert documented == actual, (
            f"{suite}: SKILL.md says {documented} tests, pytest collects {actual}"
        )


def test_documented_total_matches_the_sum_of_the_suites(skill_text):
    """The headline number must be the sum of the per-suite numbers."""
    total = re.search(r"Total:\s*\*?\*?(\d+)\s+tests", skill_text)
    assert total, "SKILL.md does not state a test total"
    documented = int(total.group(1))
    suites = sorted(p.name for p in (ROOT / "scripts").glob("test_*.py"))
    actual = sum(_pytest_count(ROOT / "scripts" / suite) for suite in suites)
    assert documented == actual, (
        f"SKILL.md claims {documented} tests in total, the suites collect {actual}"
    )


def test_report_format_is_machine_readable(skill_text):
    """The GATES line in the report format must be parsable by verify_claims."""
    block = re.search(
        r"##\s*7\.\s*Final Report Format.*?```(.*?)```", skill_text, re.S
    )
    assert block, "could not find the final report format block in SKILL.md"
    report = block.group(1)
    tmp = ROOT / "scripts" / ".cache" / "_report_format_check.txt"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(report, encoding="utf-8")
    try:
        gates, _src = parse_claims(tmp)
    finally:
        tmp.unlink(missing_ok=True)
    assert set(gates) == set(GATE_NAMES), (
        f"report format does not cover every gate: missing {sorted(set(GATE_NAMES) - set(gates))}"
    )
    assert all(v == "PASS" for v in gates.values()), "report format must show PASS statuses"


def test_exit_code_contract_is_documented(skill_text):
    assert "Exit-code contract" in skill_text
    assert "SKIPPED" in skill_text
    assert "never a pass" in skill_text.lower() or "never a PASS" in skill_text


def test_every_gate_documents_its_evidence(skill_text):
    """Each gate section must name the script/artifact that proves it."""
    sections = re.split(r"\n###\s*Gate\s+([A-U])\b", skill_text)
    # sections[0] is the preamble; then pairs of (gate, body)
    pairs = list(zip(sections[1::2], sections[2::2]))
    assert len(pairs) == 21, f"expected 21 gate sections, found {len(pairs)}"
    for gate, body in pairs:
        assert "Proof" in body or "Proof" in body, f"gate {gate} has no evidence line"


def test_skill_mentions_the_verifier(skill_text):
    assert "verify_claims.py" in skill_text
    assert "UNVERIFIABLE" in skill_text or "unverifiable" in skill_text.lower()


def test_artifact_lookup_rules_are_documented(skill_text):
    """The artefact-location rules must be in SKILL.md and in the reference."""
    assert "--artifact-dir" in skill_text
    ref = (REFERENCES / "verification.md").read_text(encoding="utf-8")
    assert "--artifact-dir" in ref
    assert "0 tests" in ref or "0 tests executed" in ref
    assert "UNSUPPORTED" in ref
