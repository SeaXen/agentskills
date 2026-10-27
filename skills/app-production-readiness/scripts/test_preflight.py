"""Self-test for the hardcoded-secret heuristic in preflight.py.

Run:  python scripts/test_preflight.py
Exit 0: all cases pass | Exit 1: a case regressed
"""
import re
import sys

assign = re.compile(
    r"""(?P<name>[A-Za-z_$][A-Za-z0-9_$]*(?:\.[A-Za-z0-9_$]+)*)"""
    r"""\s*[:=]\s*(?P<q>['"])(?P<val>[^'"\n]{8,})(?P=q)""",
)
SECRET_NAME = re.compile(
    r"(api[_-]?key|secret|token|password|passwd|pwd|credential|private[_-]?key|"
    r"signing[_-]?key|access[_-]?key)", re.I)
benign = re.compile(
    r"(example|placeholder|dummy|fake|mock|sample|fixture|stub|redacted|"
    r"changeme|your[_-]?key|your[_-]?secret|xxx|todo|lorem|\.\.\.|"
    r"^<[^>]+>$|\$\{|\{\{|process\.env|import\.meta\.env|os\.environ|"
    r"^demo|demo_|demo$|masked|redacted|hidden|scrubbed|"
    r"^[A-Za-z_]*_(ID|NAME|LABEL|TYPE|FIELD|KEY_NAME)$)", re.I)
non_secret_name = re.compile(
    r"(placeholder|example|dummy|sample|mock|fixture|"
    r"label|title|description|message|field|column|key_name|"
    r"_url$|_uri$|_endpoint$|_host$|_domain$|^url$|^uri$|"
    r"_cookie$|^cookie$|_name$|_header$|_field$|^demo$|_demo$)", re.I)
benign_value = re.compile(
    r"^(https?|wss?|mailto):|^[/.]|^__Host-|^__Secure-|"
    r"^https?://|^/api/|^https://|^www\.", re.I)
salt_name = re.compile(r"(^|[^a-z])(salt|pepper)([^a-z]|$)", re.I)
env_name_value = re.compile(r"^[A-Z][A-Z0-9_]{6,}$")


def flag(line):
    if "process.env" in line or "os.environ" in line or "import.meta.env" in line:
        return False
    m = assign.search(line)
    if not m:
        return False
    name, value = m.group("name"), m.group("val").strip()
    if not SECRET_NAME.search(name):
        return False
    if not value or benign.search(value):
        return False
    if benign_value.search(value):
        return False
    if env_name_value.match(value):
        return False
    if non_secret_name.search(name):
        return False
    if salt_name.search(name):
        return False
    if len(value) < 12 or not re.search(r"[A-Za-z]", value):
        return False
    has_digit = bool(re.search(r"[0-9]", value))
    has_upper = any(c.isupper() for c in value)
    return has_digit or has_upper


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
]


def main():
    fails = 0
    for line, expected, desc in CASES:
        got = flag(line)
        ok = got == expected
        if not ok:
            fails += 1
        print(f"{'ok  ' if ok else 'FAIL'} expected={expected!s:<5} got={got!s:<5} {desc}")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
