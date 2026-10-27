"""Regression tests for the app-production-readiness CLI scripts.

Run:  python -m pytest scripts/test_qa_scripts.py -q
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import qa_common  # noqa: E402


def run_script(name: str, *args: str):
    """Run a CLI script and return the completed process."""
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *args],
        capture_output=True,
        text=True,
        cwd=str(SCRIPTS),
    )


# --- fixtures ----------------------------------------------------------------

@pytest.fixture()
def node_project(tmp_path: Path) -> Path:
    """A minimal but valid Node project."""
    root = tmp_path / "app"
    (root / "src").mkdir(parents=True)
    (root / "package.json").write_text(json.dumps({
        "name": "demo",
        "scripts": {"build": "next build", "start": "next start", "lint": "eslint ."},
    }), encoding="utf-8")
    (root / ".env.example").write_text("PORT=3000\nAPI_KEY=\n", encoding="utf-8")
    (root / ".gitignore").write_text("node_modules\n.env\n", encoding="utf-8")
    (root / "README.md").write_text("# Demo\n", encoding="utf-8")
    (root / "src" / "index.ts").write_text("export const x = 1;\n", encoding="utf-8")
    return root


@pytest.fixture()
def nested_project(tmp_path: Path) -> Path:
    """A project with a nested app inside packages/web."""
    root = tmp_path / "parent"
    nested = root / "packages" / "web"
    nested.mkdir(parents=True)
    (root / "package.json").write_text(json.dumps({
        "name": "parent",
        "scripts": {"build": "tsc", "start": "node dist/index.js"},
    }), encoding="utf-8")
    (root / "README.md").write_text("# Parent\n", encoding="utf-8")
    (root / ".env.example").write_text("PORT=3000\n", encoding="utf-8")
    (nested / "package.json").write_text(json.dumps({
        "name": "web",
        "scripts": {"build": "vite build", "start": "vite preview"},
    }), encoding="utf-8")
    (nested / "src.ts").write_text("const secret = 'x';\n", encoding="utf-8")
    return root


# --- root validation ---------------------------------------------------------

def test_missing_root_exits_nonzero(tmp_path: Path):
    missing = tmp_path / "nope"
    for args in ([str(missing)], [str(missing), "--json"], ["--json", str(missing)]):
        proc = run_script("preflight.py", *args)
        assert proc.returncode != 0, f"expected failure for {args}"
        assert "does not exist" in proc.stderr


def test_file_as_root_exits_nonzero(tmp_path: Path):
    f = tmp_path / "a-file.txt"
    f.write_text("x", encoding="utf-8")
    proc = run_script("preflight.py", str(f))
    assert proc.returncode != 0
    assert "not a directory" in proc.stderr


def test_invalid_root_json_stdout_is_pure_json(tmp_path: Path):
    missing = tmp_path / "nope"
    proc = run_script("preflight.py", "--json", str(missing))
    assert proc.returncode != 0
    # stdout must contain nothing but JSON
    data = json.loads(proc.stdout)
    assert isinstance(data, list) and data
    assert data[0]["ok"] is False




# --- argument order ----------------------------------------------------------

@pytest.mark.parametrize("script", [
    "preflight.py", "security_scan.py", "check_readme.py",
])
def test_root_and_json_in_either_order(script: str, node_project: Path):
    a = run_script(script, "--json", str(node_project))
    b = run_script(script, str(node_project), "--json")
    assert a.returncode == b.returncode
    # both stdout payloads must parse as JSON
    json.loads(a.stdout)
    json.loads(b.stdout)


def test_unknown_flag_is_not_treated_as_a_path(node_project: Path):
    proc = run_script("preflight.py", "--json", "--verbose", str(node_project))
    assert proc.returncode in (0, 1)
    json.loads(proc.stdout)


# --- JSON output -------------------------------------------------------------

def test_json_mode_keeps_stdout_pure(node_project: Path):
    proc = run_script("preflight.py", "--json", str(node_project))
    data = json.loads(proc.stdout)  # raises if anything else leaked into stdout
    assert isinstance(data, list)
    for item in data:
        assert set(item) == {"name", "ok", "required", "detail"}


def test_json_mode_writes_human_report_to_stderr(node_project: Path):
    proc = run_script("preflight.py", "--json", str(node_project))
    # the human report (if any) belongs on stderr, never on stdout
    assert "PRODUCTION READINESS PREFLIGHT" not in proc.stdout
    assert "PRODUCTION READINESS PREFLIGHT" in proc.stderr


def test_human_mode_writes_report_to_stdout(node_project: Path):
    proc = run_script("preflight.py", str(node_project))
    assert "PRODUCTION READINESS PREFLIGHT" in proc.stdout
    with pytest.raises(json.JSONDecodeError):
        json.loads(proc.stdout)


# --- project detection -------------------------------------------------------

def test_nested_project_does_not_leak_into_parent(nested_project: Path):
    proc = run_script("preflight.py", "--json", str(nested_project))
    data = json.loads(proc.stdout)
    names = {c["name"]: c for c in data}
    # the parent's own package.json is the one that matters
    assert names["package.json present"]["ok"] is True
    # the nested app's scripts must not be adopted by the parent
    build = names["build script defined"]
    assert "vite" not in (build.get("detail") or "")


def test_nested_project_files_are_excluded_from_scan(nested_project: Path):
    found = {p.name for p in qa_common.walk_files(nested_project)}
    assert "src.ts" not in found
    assert "package.json" in found  # the parent's own manifest


def test_root_files_only_contains_top_level(nested_project: Path):
    files = qa_common.root_files(nested_project)
    assert "package.json" in files
    assert "README.md" in files
    assert not any("web" in name for name in files)

@pytest.mark.parametrize("script", [
    "preflight.py", "detect_env.py", "security_scan.py",
    "scan_workspace.py", "check_readme.py",
])
def test_all_scripts_reject_bad_root(script: str, tmp_path: Path):
    proc = run_script(script, str(tmp_path / "missing"))
    assert proc.returncode != 0, f"{script} accepted a non-existent root"


@pytest.mark.parametrize("script", [
    "preflight.py", "detect_env.py", "security_scan.py",
    "scan_workspace.py", "check_readme.py",
])
def test_all_scripts_keep_stdout_parseable_on_bad_root(script: str, tmp_path: Path):
    """Even on failure, stdout must be valid JSON so callers can parse it."""
    proc = run_script(script, str(tmp_path / "missing"), "--json")
    assert proc.returncode != 0
    data = json.loads(proc.stdout)
    assert data is not None
    # the human-readable reason belongs on stderr
    assert "does not exist" in proc.stderr


# --- env template vs real env file ------------------------------------------

@pytest.mark.parametrize("name", [
    ".env", ".env.local", ".env.production", "env", "env.local",
])
def test_real_env_files_are_dotenvs(name: str):
    assert qa_common.is_dotenv(name) is True
    assert qa_common.is_env_template(name) is False


@pytest.mark.parametrize("name", [
    ".env.example", "env.example", ".env.sample", ".env.template",
    ".env.dist", "env.sample",
])
def test_env_templates_are_templates(name: str):
    assert qa_common.is_env_template(name) is True
    assert qa_common.is_dotenv(name) is False


def test_security_scan_flags_secret_in_dotenv(node_project: Path):
    (node_project / ".env.local").write_text(
        "API_KEY=sk_live_51H8xQ2eZvKYlo2Cabcdefghijk\n", encoding="utf-8")
    proc = run_script("security_scan.py", "--json", str(node_project))
    data = json.loads(proc.stdout)
    assert any(f["file"].replace("\\", "/") == ".env.local" for f in data), data


def test_security_scan_ignores_env_template(node_project: Path):
    (node_project / ".env.example").write_text(
        "API_KEY=sk_live_51H8xQ2eZvKYlo2Cabcdefghijk\n", encoding="utf-8")
    proc = run_script("security_scan.py", "--json", str(node_project))
    data = json.loads(proc.stdout)
    assert not any(".env.example" in f["file"] for f in data), data


def test_preflight_reports_real_env_file(node_project: Path):
    (node_project / ".env.local").write_text("API_KEY=abc123\n", encoding="utf-8")
    proc = run_script("preflight.py", "--json", str(node_project))
    data = json.loads(proc.stdout)
    env_check = [c for c in data if c["name"] == ".env not committed"][0]
    assert env_check["ok"] is False
    assert ".env.local" in env_check["detail"]


def test_preflight_env_template_is_not_a_violation(node_project: Path):
    proc = run_script("preflight.py", "--json", str(node_project))
    data = json.loads(proc.stdout)
    env_check = [c for c in data if c["name"] == ".env not committed"][0]
    assert env_check["ok"] is True



# --- README checks -----------------------------------------------------------

def test_readme_image_sources_markdown_and_html():
    text = (
        "![one](docs/one.png)\n"
        '<img src="docs/two.png" alt="two">\n'
        '<source srcset="docs/three.png">\n'
    )
    srcs = qa_common.readme_image_sources(text)
    assert "docs/one.png" in srcs
    assert "docs/two.png" in srcs
    assert "docs/three.png" in srcs


def test_readme_asset_resolves_from_repo_root(tmp_path: Path):
    root = tmp_path / "repo"
    (root / "docs").mkdir(parents=True)
    (root / "docs" / "shot.png").write_bytes(b"x")
    resolved = qa_common.resolve_readme_asset(root, "docs/shot.png")
    assert resolved is not None
    assert resolved == (root / "docs" / "shot.png").resolve()


def test_readme_remote_asset_is_ignored(tmp_path: Path):
    assert qa_common.resolve_readme_asset(tmp_path, "https://x.dev/a.png") is None
    assert qa_common.resolve_readme_asset(tmp_path, "data:image/png;base64,AAA") is None


def test_check_readme_detects_missing_local_image(tmp_path: Path):
    root = tmp_path / "repo"
    root.mkdir()
    (root / "README.md").write_text(
        "# T\n\n![a](docs/missing.png)\n", encoding="utf-8")
    proc = run_script("check_readme.py", "--json", str(root))
    data = json.loads(proc.stdout)
    broken = [c for c in data["checks"] if c["name"] == "all local image paths resolve"][0]
    assert broken["ok"] is False
    assert "docs/missing.png" in broken["detail"]


def test_check_readme_accepts_existing_local_image(tmp_path: Path):
    root = tmp_path / "repo"
    (root / "docs").mkdir(parents=True)
    (root / "docs" / "shot.png").write_bytes(b"x")
    (root / "README.md").write_text(
        "# T\n\n![a](docs/shot.png)\n", encoding="utf-8")
    proc = run_script("check_readme.py", "--json", str(root))
    data = json.loads(proc.stdout)
    broken = [c for c in data["checks"] if c["name"] == "all local image paths resolve"][0]
    assert broken["ok"] is True


def test_check_readme_counts_html_images(tmp_path: Path):
    root = tmp_path / "repo"
    root.mkdir()
    (root / "README.md").write_text(
        "# T\n\n"
        '<img src="a.png" alt="a">\n'
        '<img src="b.png" alt="b">\n'
        '<source srcset="c.png">\n',
        encoding="utf-8",
    )
    proc = run_script("check_readme.py", "--json", str(root))
    data = json.loads(proc.stdout)
    count = [c for c in data["checks"] if c["name"].startswith("screenshots referenced")][0]
    assert "found 3" in count["name"]


# --- screenshot output containment -------------------------------------------

def test_out_dir_inside_root_is_allowed(tmp_path: Path):
    root = tmp_path / "app"
    root.mkdir()
    out, err = qa_common.resolve_out_dir(root, "docs/screenshots")
    assert err is None
    assert out == (root / "docs" / "screenshots").resolve()


def test_out_dir_escaping_root_is_rejected(tmp_path: Path):
    root = tmp_path / "app"
    root.mkdir()
    out, err = qa_common.resolve_out_dir(root, "../evil")
    assert err is not None
    assert "escapes the project root" in err


def test_out_dir_absolute_outside_root_is_rejected(tmp_path: Path):
    root = tmp_path / "app"
    root.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    out, err = qa_common.resolve_out_dir(root, str(outside))
    assert err is not None
    assert "escapes the project root" in err


def test_capture_screenshots_rejects_escaping_out(tmp_path: Path):
    root = tmp_path / "app"
    root.mkdir()
    proc = run_script(
        "capture_screenshots.py",
        "--root", str(root),
        "--url", "http://localhost:3000",
        "--out", "../evil",
    )
    assert proc.returncode != 0
    assert "escapes the project root" in proc.stderr


def test_capture_screenshots_rejects_missing_root(tmp_path: Path):
    proc = run_script(
        "capture_screenshots.py",
        "--root", str(tmp_path / "missing"),
        "--url", "http://localhost:3000",
    )
    assert proc.returncode != 0
    assert "does not exist" in proc.stderr


def test_the_fixture_generator_refuses_an_unknown_variant(tmp_path: Path):
    """An unknown variant must fail loudly.

    Falling through to the "good" fixture would make a broken-fixture test
    pass for the wrong reason - the worst possible failure mode for a test
    corpus.
    """
    sys.path.insert(0, str(SCRIPTS / "fixtures"))
    import make_sample_app  # noqa: E402

    with pytest.raises(ValueError) as excinfo:
        make_sample_app.build(tmp_path / "nope", variant="nope")
    assert "unknown fixture variant" in str(excinfo.value)


def test_the_empty_fixture_ships_no_app_surface(tmp_path: Path):
    """The "empty" variant must stay empty - it is the skip-behaviour probe."""
    sys.path.insert(0, str(SCRIPTS / "fixtures"))
    import make_sample_app  # noqa: E402

    out = make_sample_app.build(tmp_path / "empty", variant="empty")
    entries = sorted(p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file())
    assert entries == ["package.json"]

