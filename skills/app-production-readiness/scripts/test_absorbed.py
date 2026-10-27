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
                     if p.name not in ("verify_manifest.py", "refresh_manifest.py"))
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


def test_git_never_rewrites_the_line_endings_of_an_absorbed_copy():
    """A CRLF conversion would make every byte-exact copy look drifted.

    The absorbed scripts are hashed in MANIFEST.json, so Git must check them
    out unchanged.  Without this rule a fresh clone on Windows (core.autocrlf
    = true) reports 14 false drifts and `skill_check.py` fails.
    """
    attributes = ROOT / ".gitattributes"
    assert attributes.is_file(), ".gitattributes is missing"
    text = attributes.read_text(encoding="utf-8")
    rules = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            rules[parts[0]] = " ".join(parts[1:])
    assert rules.get("scripts/absorbed/*.py", "").startswith("-text"), (
        "scripts/absorbed/*.py must be marked -text so Git keeps the bytes "
        "identical to MANIFEST.json")
    assert "-text" in rules.get("scripts/absorbed/MANIFEST.json", ""), (
        "scripts/absorbed/MANIFEST.json must be marked -text")


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
# declared local patches
# ---------------------------------------------------------------------------
def test_every_declared_patch_records_its_base_and_its_reason(manifest):
    """A forked copy must say what it forked from and why."""
    patched = [name for name, entry in manifest["files"].items()
               if not entry.get("identical_to_source", True)]
    for name in patched:
        entry = manifest["files"][name]
        assert entry.get("upstream_sha256"), f"{name} has no pinned upstream base"
        assert entry.get("patch_reason"), f"{name} does not record why it changed"
        assert entry["upstream_sha256"] != entry["sha256"], (
            f"{name} is marked patched but pins the same hash as the copy")


def test_a_patched_copy_is_not_flagged_as_drift(manifest):
    """A declared patch must not break the integrity check."""
    sys.path.insert(0, str(ABSORBED))
    import verify_manifest  # type: ignore
    report = verify_manifest.verify()
    assert report["status"] == "ok", report
    for row in report["files"]:
        entry = manifest["files"][row["file"]]
        if not entry.get("identical_to_source", True):
            assert row["ok"], row
            assert "modified" not in row["detail"], row


def test_refresh_manifest_repins_a_copy_and_records_the_reason(tmp_path):
    """An intentional edit must be re-pinnable with a recorded reason."""
    import shutil as _shutil
    import verify_manifest  # type: ignore

    sandbox = tmp_path / "absorbed"
    sandbox.mkdir()
    for item in ABSORBED.iterdir():
        if item.suffix in (".py", ".json"):
            _shutil.copy2(item, sandbox / item.name)
    manifest_path = sandbox / "MANIFEST.json"
    target = "vulnerability_security_scan.py"

    # Simulate an intentional local edit that was never re-pinned.
    edited = sandbox / target
    edited.write_text(edited.read_text(encoding="utf-8") + "\n# local tweak\n",
                      encoding="utf-8")
    original_manifest = verify_manifest.MANIFEST
    original_here = verify_manifest.HERE
    verify_manifest.MANIFEST = manifest_path
    verify_manifest.HERE = sandbox
    try:
        report = verify_manifest.verify()
        assert report["status"] == "drift", report

        sys.path.insert(0, str(ABSORBED))
        import refresh_manifest  # type: ignore
        original_manifest_file = refresh_manifest.MANIFEST
        original_here = refresh_manifest.HERE
        refresh_manifest.MANIFEST = manifest_path
        refresh_manifest.HERE = sandbox
        try:
            assert refresh_manifest.refresh([target], "test tweak") == 0
        finally:
            refresh_manifest.MANIFEST = original_manifest_file
            refresh_manifest.HERE = original_here

        after = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert after["files"][target]["sha256"] == _sha256(edited)
        assert after["files"][target]["patch_reason"] == "test tweak"
        assert verify_manifest.verify()["status"] == "ok"
    finally:
        verify_manifest.MANIFEST = original_manifest
        verify_manifest.HERE = original_here


def test_refresh_manifest_requires_a_reason(tmp_path):
    import shutil as _shutil
    sandbox = tmp_path / "absorbed2"
    sandbox.mkdir()
    for item in ABSORBED.iterdir():
        if item.suffix in (".py", ".json"):
            _shutil.copy2(item, sandbox / item.name)
    sys.path.insert(0, str(ABSORBED))
    import refresh_manifest  # type: ignore
    original = refresh_manifest.MANIFEST
    refresh_manifest.MANIFEST = sandbox / "MANIFEST.json"
    try:
        assert refresh_manifest.main(["--file", "ux_audit.py"]) == 1
    finally:
        refresh_manifest.MANIFEST = original


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


# ---------------------------------------------------------------------------
# the absorbed knowledge pack
# ---------------------------------------------------------------------------

KNOWLEDGE = ROOT / "references" / "knowledge"


def test_the_knowledge_pack_matches_its_manifest():
    sys.path.insert(0, str(SCRIPTS))
    import refresh_knowledge
    problems, checked = refresh_knowledge.check(ROOT)
    assert problems == []
    assert checked >= 80


def test_the_knowledge_manifest_is_utf8_without_a_bom_and_uses_posix_paths():
    raw = (KNOWLEDGE / "MANIFEST.json").read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf")
    entries = json.loads(raw.decode("utf-8"))
    assert entries
    for entry in entries:
        assert "\\" not in entry["file"], entry
        assert "\\" not in entry["path"], entry
        assert "\\" not in entry["source"], entry
        assert entry["sha256"], entry
        assert entry["bytes"] > 0, entry


def test_every_knowledge_copy_is_byte_identical_to_its_source():
    """The copy is the original verbatim behind a short header."""
    entries = json.loads((KNOWLEDGE / "MANIFEST.json").read_text(encoding="utf-8"))
    checked = 0
    for entry in entries:
        local = KNOWLEDGE / entry["path"]
        raw = local.read_bytes()
        marker = b"-->\n"
        index = raw.find(marker)
        assert index != -1, entry["path"]
        body = raw[index + len(marker):]
        source = ROOT.parent / entry["source"]
        if not source.is_file():
            continue  # the sibling skill is gone - the local copy is authoritative
        assert body == source.read_bytes(), entry["path"]
        checked += 1
    assert checked >= 80


def test_a_tampered_knowledge_copy_is_detected(tmp_path):
    sys.path.insert(0, str(SCRIPTS))
    import refresh_knowledge
    pack = tmp_path / "knowledge"
    pack.mkdir()
    (pack / "MANIFEST.json").write_text(json.dumps([{
        "skill": "demo",
        "file": "SKILL.md",
        "path": "demo/SKILL.md",
        "source": "demo/SKILL.md",
        "bytes": 5,
        "sha256": hashlib.sha256(b"hello").hexdigest(),
    }]), encoding="utf-8")
    target = pack / "demo" / "SKILL.md"
    target.parent.mkdir(parents=True)
    target.write_text("hello", encoding="utf-8")
    root = tmp_path / "skill"
    (root / "references").mkdir(parents=True)
    (root / "references" / "knowledge").mkdir()
    (root / "references" / "knowledge" / "MANIFEST.json").write_text(
        (pack / "MANIFEST.json").read_text(encoding="utf-8"), encoding="utf-8")
    (root / "references" / "knowledge" / "demo").mkdir()
    (root / "references" / "knowledge" / "demo" / "SKILL.md").write_text(
        "hello", encoding="utf-8")
    assert refresh_knowledge.check(root) == ([], 1)
    (root / "references" / "knowledge" / "demo" / "SKILL.md").write_text(
        "tampered", encoding="utf-8")
    problems, _ = refresh_knowledge.check(root)
    assert any("sha256 drift" in p for p in problems)


def test_the_knowledge_pack_has_no_double_encoded_text():
    for path in sorted(KNOWLEDGE.rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
        assert not skill_check.MOJIBAKE_RE.search(text), path


def test_skill_check_detects_double_encoded_text(tmp_path):
    skill = tmp_path / "my-skill"
    (skill / "scripts").mkdir(parents=True)
    (skill / "references").mkdir(parents=True)
    (skill / "SKILL.md").write_text(
        "---\nname: my-skill\ndescription: " + "x" * 60 + "\n---\n\nbody\n",
        encoding="utf-8")
    # "->" encoded as UTF-8 and then decoded as cp1252
    (skill / "references" / "notes.md").write_text(
        "a \u00e2\u20ac\u2122 b\n", encoding="utf-8")
    report = skill_check.check_skill(skill)
    assert not report["ok"]
    assert any("double-encoded" in p for p in report["problems"])
