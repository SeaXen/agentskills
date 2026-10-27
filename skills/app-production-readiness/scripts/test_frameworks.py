#!/usr/bin/env python3
"""Tests for the framework profiles, the serve mode, the --fix mode and the
review orchestrator (the three features added after the tradex review)."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SCRIPTS / "fixtures"))

import framework_profiles  # noqa: E402
import fixes  # noqa: E402
import review  # noqa: E402
import serve  # noqa: E402
import make_sample_app  # noqa: E402


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def make_next_app(root: Path, app_dir: str = "src/app") -> Path:
    """A minimal Next.js App Router project."""
    (root / app_dir).mkdir(parents=True, exist_ok=True)
    (root / "next.config.ts").write_text("export default { output: 'standalone' }",
                                         encoding="utf-8")
    (root / app_dir / "layout.tsx").write_text(
        "import type { Metadata } from 'next'\n"
        "export const metadata: Metadata = { title: 'Demo' }\n"
        "export default function RootLayout({ children }) { return <html><body>{children}</body></html> }\n",
        encoding="utf-8")
    (root / app_dir / "page.tsx").write_text("export default function Page() { return <h1>Hi</h1> }\n",
                                             encoding="utf-8")
    return root


@pytest.fixture()
def next_app(tmp_path):
    return make_next_app(tmp_path / "nextapp") or tmp_path / "nextapp"


@pytest.fixture(scope="module")
def good_app(tmp_path_factory):
    out = tmp_path_factory.mktemp("good")
    make_sample_app.build(out, variant="good")
    return out


# --------------------------------------------------------------------------
# framework profiles
# --------------------------------------------------------------------------

def test_detects_next_app_router(next_app):
    assert framework_profiles.detect(next_app) == "next-app"


def test_detects_vite(tmp_path):
    (tmp_path / "vite.config.ts").write_text("export default {}", encoding="utf-8")
    assert framework_profiles.detect(tmp_path) == "vite"


def test_unknown_project_is_static(tmp_path):
    assert framework_profiles.detect(tmp_path) == "static"


def test_next_injects_the_viewport(next_app):
    assert framework_profiles.injects_viewport(next_app) is True


def test_a_plain_project_does_not_inject_the_viewport(tmp_path):
    (tmp_path / "index.html").write_text("<html></html>", encoding="utf-8")
    assert framework_profiles.injects_viewport(tmp_path) is False


def test_next_config_without_an_app_folder_does_not_inject_the_viewport(tmp_path):
    (tmp_path / "next.config.ts").write_text("export default {}", encoding="utf-8")
    assert framework_profiles.injects_viewport(tmp_path) is False


def test_next_inherits_the_layout_title(next_app):
    assert framework_profiles.inherits_layout_title(next_app) is True


def test_vite_does_not_inherit_a_layout_title(tmp_path):
    (tmp_path / "vite.config.ts").write_text("export default {}", encoding="utf-8")
    assert framework_profiles.inherits_layout_title(tmp_path) is False


def test_hmr_console_noise_is_recognised(next_app):
    assert framework_profiles.is_dev_console_noise(
        "WebSocket connection to 'ws://127.0.0.1:3000/_next/webpack-hmr' failed",
        next_app) is True


def test_a_real_console_error_is_not_noise(next_app):
    assert framework_profiles.is_dev_console_noise(
        "TypeError: cannot read properties of undefined (reading 'map')",
        next_app) is False


def test_a_failed_build_is_not_a_real_build(next_app):
    (next_app / ".next" / "static").mkdir(parents=True, exist_ok=True)
    (next_app / ".next" / "static" / "app.js").write_text("x", encoding="utf-8")
    assert framework_profiles.build_is_real(next_app) is False


def test_a_completed_build_is_a_real_build(next_app):
    (next_app / ".next").mkdir(parents=True, exist_ok=True)
    (next_app / ".next" / "BUILD_ID").write_text("abc", encoding="utf-8")
    assert framework_profiles.build_is_real(next_app) is True


def test_describe_reports_the_profile(next_app):
    described = framework_profiles.describe(next_app)
    assert described["framework"] == "next-app"
    assert described["injects_viewport"] is True
    assert "Next.js" in described["label"]


# --------------------------------------------------------------------------
# serve mode
# --------------------------------------------------------------------------

def test_detect_commands_finds_the_start_script(tmp_path):
    (tmp_path / "package.json").write_text(
        json.dumps({"scripts": {"start": "node server.js", "dev": "next dev"}}),
        encoding="utf-8")
    commands = serve.detect_commands(tmp_path)
    assert "start" in commands["prod"]
    assert "dev" in commands["dev"]


def test_detect_commands_falls_back_to_a_python_entry_point(tmp_path):
    (tmp_path / "main.py").write_text("print('hi')\n", encoding="utf-8")
    commands = serve.detect_commands(tmp_path)
    assert commands["kind"] == "python"
    assert commands["prod"].endswith("main.py")


def test_start_server_without_a_start_command_is_skipped(tmp_path):
    result = serve.start_server(tmp_path, {})
    assert result["ok"] is False
    assert result["status"] == "skipped"


def test_start_server_boots_a_python_app(tmp_path):
    (tmp_path / "main.py").write_text(
        "import os\n"
        "from http.server import BaseHTTPRequestHandler, HTTPServer\n"
        "port = int(os.environ.get('PORT', '0'))\n"
        "class H(BaseHTTPRequestHandler):\n"
        "    def do_GET(self):\n"
        "        self.send_response(200); self.end_headers(); self.wfile.write(b'ok')\n"
        "    def log_message(self, *a): pass\n"
        "HTTPServer(('127.0.0.1', port), H).serve_forever()\n",
        encoding="utf-8")
    result = serve.start_server(tmp_path, {"timeout": 30})
    try:
        assert result["ok"] is True, result.get("error")
        assert result["handle"].url.startswith("http://127.0.0.1:")
    finally:
        if result.get("handle"):
            result["handle"].stop()


# --------------------------------------------------------------------------
# --fix mode
# --------------------------------------------------------------------------

def test_env_example_is_created_from_the_used_variables(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "app.js").write_text(
        "const key = process.env.OPENAI_API_KEY;\nconst other = process.env.SECOND;\n",
        encoding="utf-8")
    result = fixes.fix_env_example(tmp_path)
    assert result["status"] == "applied"
    text = (tmp_path / ".env.example").read_text(encoding="utf-8")
    assert "OPENAI_API_KEY=" in text
    assert "SECOND=" in text


def test_env_example_does_not_overwrite_existing_values(tmp_path):
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "app.js").write_text("process.env.KEEP_ME;", encoding="utf-8")
    (tmp_path / ".env.example").write_text("KEEP_ME=real-value\n", encoding="utf-8")
    result = fixes.fix_env_example(tmp_path)
    assert result["status"] == "already-ok"
    assert "real-value" in (tmp_path / ".env.example").read_text(encoding="utf-8")


def test_gitignore_is_taught_to_keep_the_env_example(tmp_path):
    (tmp_path / ".gitignore").write_text(".env*\nnode_modules\n", encoding="utf-8")
    result = fixes.fix_gitignore_env_example(tmp_path)
    assert result["status"] == "applied"
    assert "!.env.example" in (tmp_path / ".gitignore").read_text(encoding="utf-8")


def test_gitignore_fix_is_idempotent(tmp_path):
    (tmp_path / ".gitignore").write_text(".env*\n", encoding="utf-8")
    fixes.fix_gitignore_env_example(tmp_path)
    again = fixes.fix_gitignore_env_example(tmp_path)
    assert again["status"] == "already-ok"


def test_next_viewport_export_is_added(next_app):
    result = fixes.fix_next_viewport(next_app)
    assert result["status"] == "applied"
    text = (next_app / "src" / "app" / "layout.tsx").read_text(encoding="utf-8")
    assert "export const viewport" in text
    assert "device-width" in text


def test_next_viewport_fix_is_idempotent(next_app):
    fixes.fix_next_viewport(next_app)
    again = fixes.fix_next_viewport(next_app)
    assert again["status"] == "already-ok"


def test_next_viewport_fix_is_skipped_for_other_frameworks(tmp_path):
    (tmp_path / "vite.config.ts").write_text("export default {}", encoding="utf-8")
    assert fixes.fix_next_viewport(tmp_path)["status"] == "skipped"


def test_vercel_framework_key_is_added(next_app):
    (next_app / "vercel.json").write_text(json.dumps({"headers": []}), encoding="utf-8")
    result = fixes.fix_vercel_framework(next_app)
    assert result["status"] == "applied"
    data = json.loads((next_app / "vercel.json").read_text(encoding="utf-8"))
    assert data["framework"] == "nextjs"
    assert data["headers"] == []


def test_vercel_fix_keeps_existing_keys(next_app):
    (next_app / "vercel.json").write_text(json.dumps({"framework": "nextjs"}), encoding="utf-8")
    result = fixes.fix_vercel_framework(next_app)
    assert result["status"] == "already-ok"


def test_next_security_headers_are_added(next_app):
    result = fixes.fix_next_security_headers(next_app)
    assert result["status"] == "applied"
    text = (next_app / "next.config.ts").read_text(encoding="utf-8")
    assert "X-Content-Type-Options" in text
    assert "headers" in text


def test_a_changed_file_is_backed_up_before_it_is_edited(next_app):
    fixes.fix_next_security_headers(next_app)
    backups = list((next_app / "qa" / "fix-backup").rglob("next.config.ts"))
    assert backups, "the original next.config.ts must be recoverable"


def test_apply_all_reports_every_fix(good_app):
    copy = good_app.parent / (good_app.name + "-fixcopy")
    shutil.copytree(good_app, copy)
    results = fixes.apply_all(copy)
    ids = {r["id"] for r in results}
    assert "env-example" in ids
    assert all(r["status"] != "failed" for r in results)


# --------------------------------------------------------------------------
# the orchestrator
# --------------------------------------------------------------------------

def test_judge_returns_a_verdict_for_every_gate(good_app):
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "use_scope": True}
    results = review.judge(good_app, ctx)
    assert len(results) == 21
    for item in results:
        assert item["verdict"] in ("VERIFIED", "CONTRADICTED", "UNSUPPORTED",
                                   "UNVERIFIABLE", "NOT_APPLICABLE")


def test_judge_can_be_restricted_to_some_gates(good_app):
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "use_scope": True}
    results = review.judge(good_app, ctx, ["B", "E", "J"])
    assert [r["gate"] for r in results] == ["B", "E", "J"]


def test_the_report_is_written(good_app):
    copy = good_app.parent / (good_app.name + "-reportcopy")
    shutil.copytree(good_app, copy)
    ctx = {"url": None, "routes": ["/"], "healthz": "/healthz",
           "skip_tests": True, "use_scope": True}
    payload = {"generated": "now", "app": {"name": copy.name, "root": str(copy),
                                           "url": None, "framework": "test"},
               "scope": {"run": 21}, "fixes": [], "gates": review.judge(copy, ctx),
               "summary": {}, "blocking": [], "artefacts": []}
    path = review.write_report(copy, payload)
    assert Path(path).exists()
    text = Path(path).read_text(encoding="utf-8")
    assert "## GATES" in text
    assert "## SUMMARY" in text


def test_the_cli_runs_without_a_server_and_still_reports(good_app):
    copy = good_app.parent / (good_app.name + "-clicopy")
    shutil.copytree(good_app, copy)
    rc = review.main(["--root", str(copy), "--gates", "B,J", "--json"])
    assert rc in (0, 1)
    assert (copy / "qa" / "report.md").exists()
    data = json.loads((copy / "qa" / "summary.json").read_text(encoding="utf-8"))
    assert "gates" in data and data["gates"]
