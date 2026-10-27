"""Self-test for the hardcoded-secret heuristic in preflight.py.

The cases below exercise the SHIPPED implementation
(`preflight.flag_secret_line`), not a copy of it. A duplicated regex set keeps
passing while the real scanner drifts, which is worse than having no test.

Run as pytest:  python -m pytest scripts/test_preflight.py -q
Run standalone: python scripts/test_preflight.py
Exit 0: all cases pass | Exit 1: a case regressed
"""
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import preflight  # noqa: E402
from preflight import flag_secret_line  # noqa: E402

# (line, expected_flagged, description)
CASES = [
    ('const PASSWORD = "brain#175hrS";', True, "real hardcoded password"),
    ('const FALLBACK_SECRET = "ruleforge-privacy-lock-salt-key-2026";', True, "hardcoded fallback secret"),
    ('const API_KEY = "sk_live_51H8xQ2eZvKYlo2Cabcdefghijk";', True, "real API key"),
    ('const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9";', True, "jwt token"),
    ('const SESSION_SECRET = "focus_hub_vault_salt_2026_x89q";', True, "session secret"),
    ('password: "hunter2hunter2hunter2"', True, "yaml style secret"),
    ('const apiKey = "super-secret-binance-key";', False, "human-readable label, not a secret"),
    ('const salt = "DGv6ra1nlYgDCS1FRnbzlw";', False, "salt is public by design"),
    ('const SALT_VALUE = "abcdef1234567890";', False, "salt name"),
    ('const apiKey = process.env.API_KEY;', False, "reads from env"),
    ('const apiKey = "your-api-key-here";', False, "placeholder"),
    ('const password = "placeholder-value";', False, "placeholder value"),
    ('const authToken = "<your-token>";', False, "angle placeholder"),
    ('const token = "${TOKEN}";', False, "template literal"),
    ('const PASSWORD_LABEL = "password_field";', False, "not a secret"),
    ('const token = "short1";', False, "too short"),
    ('const API_KEY = "aaaaaaaaaaaaaaaaaaaa";', False, "no digits, all letters"),
    ('const GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token";', False, "oauth url"),
    ("const TOKEN_URL = 'https://oauth2.googleapis.com/token';", False, "oauth url single quotes"),
    ('const SESSION_TOKEN_COOKIE = "__Host-grok-auth.session_token";', False, "cookie name"),
    ("cfg[exchangeKey].apiKeyMasked = 'DEMO_ACCOUNT';", False, "masked demo value"),
    ('const COOKIE_NAME = "focus_session";', False, "cookie name"),
    ('const authUrl = "https://accounts.google.com/o/oauth2/v2/auth";', False, "url property"),
    ("clientSecretEnv: 'GOOGLE_CLIENT_SECRET',", False, "env var name reference"),
    ("clientIdEnv: 'MICROSOFT_CLIENT_ID',", False, "env var name reference"),
    ('STRIPE_SECRET_KEY=sk_live_51H8xQ2eZvKYlo2Cabcdefghijk', True, "unquoted env secret"),
    ('export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYzq7S3cret', True, "unquoted exported secret"),
    ('api_key: f8Kd93jdksl2934jdksl', True, "unquoted yaml secret"),
    ('const apiKey = response.json().apiKey;', False, "expression, not a literal secret"),
    ('const maxRetries = 3000;', False, "number is not a secret"),
    ('PORT=3000', False, "port is not a secret"),
]


@pytest.mark.parametrize("line,expected,desc", CASES, ids=[c[2] for c in CASES])
def test_secret_heuristic(line, expected, desc):
    assert flag_secret_line(line) is expected, desc


def test_case_table_is_not_empty():
    """A silently emptied case table would make the suite pass vacuously."""
    assert len(CASES) >= 20
    assert any(expected for _, expected, _ in CASES), "no positive case - the detector would never fire"
    assert any(not expected for _, expected, _ in CASES), "no negative case - the detector would fire on everything"


# --------------------------------------------------------------------------
# A local .env is not a leak; a committed .env is
# --------------------------------------------------------------------------

LIVE_KEY = "STRIPE_SECRET_KEY=sk_live_51H8xQ2eZvKYlo2Cabcdefghijk\n"


def _project(tmp_path: Path, name: str) -> Path:
    app = tmp_path / name
    app.mkdir()
    (app / "package.json").write_text('{"name": "x", "version": "1.0.0"}', encoding="utf-8")
    (app / ".gitignore").write_text(".env\n", encoding="utf-8")
    (app / ".env").write_text(LIVE_KEY, encoding="utf-8")
    return app


def _checks(app: Path) -> dict:
    return {c.name: c for c in preflight.run(app)}


def test_a_local_gitignored_env_is_only_a_warning(tmp_path):
    """Failing a build over the developer's own gitignored .env is a false positive."""
    app = _project(tmp_path, "local-env")
    checks = _checks(app)
    assert checks["no hardcoded secrets"].ok is True
    assert checks["local env file holds secrets"].required is False
    assert checks[".env not committed"].ok is True


def test_a_committed_env_is_a_blocking_failure(tmp_path):
    """A .env that git actually tracks is a real leak and must block."""
    if not shutil.which("git"):
        pytest.skip("git is not installed")
    app = _project(tmp_path, "committed-env")
    subprocess.run(["git", "init", "-q"], cwd=str(app), check=True,
                   capture_output=True)
    subprocess.run(["git", "add", "-f", ".env"], cwd=str(app), check=True,
                   capture_output=True)
    checks = _checks(app)
    assert checks["no hardcoded secrets"].ok is False
    assert ".env" in checks["no hardcoded secrets"].detail
    assert checks[".env not committed"].ok is False


def main() -> int:
    fails = 0
    for line, expected, desc in CASES:
        got = flag_secret_line(line)
        ok = got == expected
        if not ok:
            fails += 1
        print(f"{'ok  ' if ok else 'FAIL'} expected={expected!s:<5} got={got!s:<5} {desc}")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
