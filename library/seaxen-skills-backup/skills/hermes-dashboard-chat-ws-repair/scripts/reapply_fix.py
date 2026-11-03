#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

WEB_SERVER = Path('/usr/local/lib/hermes-agent/hermes_cli/web_server.py')
TEST_FILE = Path('/usr/local/lib/hermes-agent/tests/hermes_cli/test_dashboard_auth_ws_auth.py')
PYTEST = Path('/usr/local/lib/hermes-agent/venv/bin/python')

ANCHORS = [
    (
        '    if getattr(app.state, "auth_required", False):\n        return True\n    client_host = ws.client.host if ws.client else ""\n',
        '    if getattr(app.state, "auth_required", False):\n        return True\n    bound_host = getattr(app.state, "bound_host", "")\n    if bound_host in {"0.0.0.0", "::"}:\n        return True\n    client_host = ws.client.host if ws.client else ""\n',
    ),
    (
        '    if app.state.auth_required:\n        return True\n\n    return client_host in _LOOPBACK_HOSTS\n',
        '    if app.state.auth_required:\n        return True\n\n    bound_host = getattr(app.state, "bound_host", "")\n    if bound_host in {"0.0.0.0", "::"}:\n        return True\n\n    return client_host in _LOOPBACK_HOSTS\n',
    ),
]

if not WEB_SERVER.exists():
    print(f'missing: {WEB_SERVER}', file=sys.stderr)
    sys.exit(1)

text = WEB_SERVER.read_text()
if 'bound_host in {"0.0.0.0", "::"}' in text:
    print('fix already present in web_server.py')
else:
    patched = False
    for needle, replacement in ANCHORS:
        if needle in text:
            WEB_SERVER.write_text(text.replace(needle, replacement, 1))
            print('patched web_server.py')
            patched = True
            break
    if not patched:
        print('expected patch anchor not found; inspect file manually', file=sys.stderr)
        sys.exit(2)

if PYTEST.exists() and TEST_FILE.exists():
    cmd = [str(PYTEST), '-m', 'pytest', str(TEST_FILE), '-q']
    print('$', ' '.join(cmd))
    raise SystemExit(subprocess.call(cmd))
else:
    print('pytest path or test file missing; patch applied but tests skipped')
