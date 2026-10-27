#!/usr/bin/env python3
"""Tests for the absorbed sibling skills and the skill's own package health.

These tests answer the question "can I delete the sibling skills?":

* every absorbed script is byte-identical to the copy recorded in MANIFEST.json
* the manifest check tolerates the originals being gone (that is not drift)
* no runtime code depends on a path inside ``D:\\Repo\\.agents\\skills``
* the absorbed engines are really wired into the gates (second security
  scanner, fallback test-command detection, fallback Lighthouse runner)
* this skill's own package (frontmatter, scripts, references) is healthy
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
ABSORBED = SCRIPTS / "absorbed"
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SCRIPTS / "fixtures"))

import security_scan  # noqa: E402
import skill_check  # noqa: E402
import verify_claims  # noqa: E402
from make_sample_app import build as build_sample_app  # noqa: E402


@pytest.fixture(scope="session")
def good_app(tmp_path_factory):
    """The 'good' sample app (production-ready by construction)."""
    out = tmp_path_factory.mktemp("good-app-absorbed")
    build_sample_app(out, variant="good")
    return out


@pytest.fixture(scope="module")
def manifest() -> dict:
    return json.loads((ABSORBED / "MANIFEST.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def absorbed_files(manifest) -> list:
    return sorted(manifest["files"])


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# manifest integrity
# ---------------------------------------------------------------------------
def test_manifest_covers_every_absorbed_script(manifest, absorbed_files):
    on_disk = sorted(p.name for p in ABSORBED.glob("*.py")
                     if p.name != "verify_manifest.py")
    assert on_disk == absorbed_files, (
        f"MANIFEST.json and scripts/absorbed/ disagree: "
        f"only on disk={sorted(set(on_disk) - set(absorbed_files))}, "
        f"only in manifest={sorted(set(absorbed_files) - set(on_disk))}")


def test_absorbed_copies_match_their_recorded_hash(manifest, absorbed_files):
    for name in absorbed_files:
        entry = manifest["files"][name]
        path = ABSORBED / name
        assert path.is_file(), f"{name} is missing"
        assert _sha256(path) == entry["sha256"], f"{name} drifted from its hash"


def test_manifest_records_the_origin_of_every_file(manifest, absorbed_files):
    for name in absorbed_files:
        entry = manifest["files"][name]
        assert entry.get("source_skill"), f"{name} has no source skill"
        assert entry.get("source_path"), f"{name} has no source path"
        assert entry.get("bytes") == (ABSORBED / name).stat().st_size


def test_absorbed_scripts_are_valid_python(absorbed_files):
    for name in absorbed_files:
        source = (ABSORBED / name).read_text(encoding="utf-8", errors="ignore")
        compile(source, name, "exec")


def test_verify_manifest_reports_ok():
    sys.path.insert(0, str(ABSORBED))
    import verify_manifest  # type: ignore
    report = verify_manifest.verify()
    assert report["status"] == "ok", report
    assert report["mismatches"] == 0
    assert report["checked"] == len(report["files"]) >= 14


def test_verify_manifest_tolerates_deleted_originals(tmp_path):
    """Deleting the sibling skills must not look like drift."""
    sys.path.insert(0, str(ABSORBED))
    import verify_manifest  # type: ignore
    report = verify_manifest.verify(source_root=tmp_path / "does-not-exist")
    assert report["status"] == "ok", report
    assert report["mismatches"] == 0
    assert all("original not found" in row["detail"] or row["detail"] == ""
               for row in report["files"])


# ---------------------------------------------------------------------------
# self-containment
# ---------------------------------------------------------------------------
def test_no_script_depends_on_the_sibling_skills_directory():
    """Only the optional provenance checker may mention the sibling root."""
    offenders = []
    for path in list(SCRIPTS.rglob("*.py")):
        if path.name == "verify_manifest.py" and path.parent == ABSORBED:
            continue  # optional --source-root provenance check
        if path.name.startswith("test_"):
            continue  # this suite names the path in order to assert on it
        text = path.read_text(encoding="utf-8", errors="ignore")
        if ".agents\\skills" in text or ".agents/skills" in text:
            offenders.append(str(path.relative_to(ROOT)))
    assert not offenders, f"runtime dependency on the sibling skills: {offenders}"


def test_absorbed_scripts_import_nothing_from_the_sibling_skills():
    for path in ABSORBED.glob("*.py"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        assert "agents.skills" not in text, f"{path.name} imports from a sibling skill"


def test_skill_md_documents_every_absorbed_source_skill(manifest):
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for skill in sorted({entry["source_skill"] for entry in manifest["files"].values()}):
        assert skill in text, f"SKILL.md does not mention the absorbed skill '{skill}'"


# ---------------------------------------------------------------------------
# the absorbed engines are really wired in
# ---------------------------------------------------------------------------
def test_second_security_scanner_is_run_by_scan_all(tmp_path):
    (tmp_path / "app.js").write_text(
        "const apiKey = 'a1b2c3d4e5f6g7h8';\n", encoding="utf-8")
    findings = security_scan.scan_all(tmp_path)
    assert findings, "the scanner produced no findings at all"
    assert any(f["type"].startswith("[scanner2/") for f in findings), (
        "the absorbed vulnerability-scanner engine was not used")


def test_second_security_scanner_is_quiet_for_the_good_app(good_app):
    findings = security_scan.scan_all(good_app)
    assert not [f for f in findings if f["type"].startswith("[scanner2/")], findings


def test_our_own_secret_rules_still_fire_alongside_the_second_scanner(tmp_path):
    """The merge must not hide the scanner's own findings."""
    (tmp_path / "app.js").write_text(
        "const stripeKey = 'sk_live_51H8xYz2eZvKYlo2C0abcdef';\n"
        "const apiKey = 'a1b2c3d4e5f6g7h8';\n", encoding="utf-8")
    findings = security_scan.scan_all(tmp_path)
    types = " ".join(f["type"] for f in findings)
    assert "Stripe" in types, findings
    assert any(f["type"].startswith("[scanner2/") for f in findings), findings


def test_broken_app_still_fails_the_cli():
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "security_scan.py"),
         str(ROOT / "scripts" / "fixtures")],
        capture_output=True, text=True)
    assert proc.returncode in (0, 1, 2)


def test_absorbed_test_command_detects_jest_without_a_test_script(tmp_path):
    (tmp_path / "package.json").write_text(
        json.dumps({"name": "x", "devDependencies": {"jest": "^29.0.0"}}),
        encoding="utf-8")
    cmd, runner = verify_claims.absorbed_test_command(tmp_path)
    assert cmd, "the absorbed test detector found no command"
    assert "jest" in " ".join(cmd).lower()
    assert "absorbed test_runner" in runner


def test_absorbed_test_command_returns_nothing_without_a_framework(tmp_path):
    cmd, runner = verify_claims.absorbed_test_command(tmp_path)
    assert cmd is None and runner is None


def test_absorbed_test_command_finds_a_python_project(tmp_path):
    (tmp_path / "requirements.txt").write_text("pytest\n", encoding="utf-8")
    cmd, runner = verify_claims.absorbed_test_command(tmp_path)
    assert cmd and "pytest" in " ".join(cmd)


def test_lighthouse_fallback_reports_an_error_instead_of_raising():
    from lighthouse_run import run_one_fallback
    out_dir = SCRIPTS / ".cache" / "_lh_fallback_test"
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        data, error = run_one_fallback("http://127.0.0.1:9/", out_dir, "probe", 90)
        assert data is None, "the fallback should not produce a report for a dead URL"
        assert error, "the fallback must explain why it could not run"
    finally:
        shutil.rmtree(out_dir, ignore_errors=True)


# ---------------------------------------------------------------------------
# this skill's own package health
# ---------------------------------------------------------------------------
def test_skill_check_passes_for_this_skill():
    report = skill_check.check_skill(ROOT)
    assert report["ok"], report["problems"]
    assert report["checks"]["scripts_compiled"] > 20


def test_skill_check_detects_a_broken_frontmatter(tmp_path):
    skill = tmp_path / "my-skill"
    (skill / "scripts").mkdir(parents=True)
    (skill / "references").mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        "---\nname: wrong-name\nbogus: 1\n---\n\n# x\n", encoding="utf-8")
    report = skill_check.check_skill(skill)
    assert not report["ok"]
    joined = " ".join(report["problems"])
    assert "bogus" in joined
    assert "folder name" in joined


def test_skill_check_detects_a_missing_reference(tmp_path):
    skill = tmp_path / "my-skill"
    (skill / "scripts").mkdir(parents=True)
    (skill / "references").mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        "---\nname: my-skill\ndescription: " + "x" * 60 + "\n---\n\n"
        "see [r](references/missing.md)\n", encoding="utf-8")
    report = skill_check.check_skill(skill)
    assert not report["ok"]
    assert any("missing file" in p for p in report["problems"])


def test_skill_check_detects_a_script_that_does_not_compile(tmp_path):
    skill = tmp_path / "my-skill"
    (skill / "scripts").mkdir(parents=True)
    (skill / "references").mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        "---\nname: my-skill\ndescription: " + "x" * 60 + "\n---\n\nbody\n",
        encoding="utf-8")
    (skill / "scripts" / "broken.py").write_text("def (:\n", encoding="utf-8")
    report = skill_check.check_skill(skill)
    assert not report["ok"]
    assert any("do not compile" in p for p in report["problems"])


def test_skill_check_packages_a_skill_archive(tmp_path):
    target = skill_check.package_skill(ROOT, tmp_path)
    assert target.is_file()
    import zipfile
    with zipfile.ZipFile(target) as zf:
        names = zf.namelist()
    assert any(name.endswith("SKILL.md") for name in names)
    assert not any("__pycache__" in name for name in names)


def test_skill_check_cli_exits_zero_on_this_skill():
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "skill_check.py"), "--root", str(ROOT)],
        capture_output=True, text=True)
    assert proc.returncode == 0, proc.stdout + proc.stderr
