# Nginx Reverse Proxy + Hermes Dashboard Auth Interaction

## Problem
When nginx proxies to hermes dashboard, both can enforce auth independently:
- nginx: `auth_basic` directive
- hermes: `basic_auth` in config.yaml

Result: **double auth prompt**.

## Solutions

### Option A: Hermes auth only (recommended)
Remove nginx auth_basic. Users hit hermes login at 9119.

### Option B: nginx auth only (hermes on localhost)
Bind hermes to 127.0.0.1 only, nginx adds auth externally.

## Port Convention (Dr. Sagar)
- 9119 = nginx reverse proxy
- 9120 = hermes dashboard direct (always auth, --insecure deprecated June 2026)

## Password Hash Generator
PYTHONPATH=/usr/local/lib/hermes-agent python3 -c \
  "from plugins.dashboard_auth.basic import hash_password; print(hash_password('your-password'))"

## Traps
- systemctl restart from inside gateway is blocked
- --insecure no longer disables auth
- Both nginx + hermes auth = double prompt (remove one)
