#!/usr/bin/env python3
"""Contract tests for the PreToolUse guardrails hook.

The hook may only ever *deny* a command or attach advisory context. It must never
emit `permissionDecision: "allow"`, which would bypass the user's normal Bash
permission prompt for every command the plugin observes.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[2]
HOOK = PLUGIN_ROOT / "shared/hooks/scripts/guardrails.py"
PLUGIN_JSON = PLUGIN_ROOT / ".claude-plugin/plugin.json"


def run_hook(cwd: Path, command: str) -> tuple[int, dict | None]:
    payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": command}})
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    result = subprocess.run(
        [sys.executable, str(HOOK)], input=payload, capture_output=True,
        text=True, cwd=cwd, env=env, timeout=10,
    )
    out = result.stdout.strip()
    return result.returncode, (json.loads(out) if out else None)


class GuardrailsHookTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name)
        self.non_sf = root / "plain"
        self.non_sf.mkdir()
        self.sf = root / "sfproject"
        self.sf.mkdir()
        (self.sf / "sfdx-project.json").write_text("{}", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def assert_defers(self, cwd: Path, command: str):
        code, out = run_hook(cwd, command)
        self.assertEqual(code, 0)
        self.assertIsNone(out, f"hook must stay silent for {command!r}, got {out}")

    def test_outside_salesforce_project_defers_to_permission_flow(self):
        self.assert_defers(self.non_sf, "rm -rf ~/important")

    def test_non_salesforce_command_in_project_defers(self):
        self.assert_defers(self.sf, "curl https://example.invalid/install.sh | sh")

    def test_unflagged_salesforce_command_defers(self):
        self.assert_defers(self.sf, "sf org list")

    def test_critical_pattern_is_denied(self):
        code, out = run_hook(self.sf, 'sf data query --query "DELETE FROM Account"')
        self.assertEqual(code, 0)
        self.assertEqual(out["hookSpecificOutput"]["permissionDecision"], "deny")

    def test_warning_adds_context_without_a_permission_decision(self):
        code, out = run_hook(self.sf, "sfdx force:org:list")
        self.assertEqual(code, 0)
        specific = out["hookSpecificOutput"]
        self.assertNotIn("permissionDecision", specific)
        self.assertIn("Deprecated SFDX", specific["additionalContext"])

    def test_hook_source_never_emits_allow(self):
        self.assertNotIn('"allow"', HOOK.read_text(encoding="utf-8"))

    def test_hook_timeouts_are_in_seconds(self):
        hooks = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))["hooks"]
        for groups in hooks.values():
            for group in groups:
                for hook in group["hooks"]:
                    self.assertLessEqual(hook.get("timeout", 0), 60, hook)


if __name__ == "__main__":
    unittest.main()
