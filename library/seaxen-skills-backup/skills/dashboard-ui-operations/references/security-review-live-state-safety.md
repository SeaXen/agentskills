# Live-safe security review for self-hosted dashboards

Use this when auditing authentication boundaries, forwarded headers, privileged APIs, backups, and mutable dashboard state.

## 1. Snapshot before probing

- Record non-secret state invariants before any live test: app count, section count, config checksum/size, permissions, and service state.
- Confirm a known-good backup exists and validate its expected member names before testing.
- Never print secrets while establishing the baseline.

## 2. Keep review probes read-only by construction

A payload that looks harmless, such as `{}` sent to a config endpoint, can still replace a complete configuration with defaults. Reviewer intent does not make a POST non-destructive.

Preferred order:

1. Test handlers in an isolated temporary server with a temporary config path.
2. Use unit tests with persistence functions mocked.
3. For live origin/auth probes, target a route/action guaranteed to fail before dispatch, and verify state invariants immediately afterward.
4. Do not send valid POST/PUT/DELETE requests to live config, restore, action, or Docker endpoints during an independent review.

If live state changes unexpectedly, stop testing, compare only non-secret invariants, restore the last known-good validated backup, verify restrictive permissions, and report the incident explicitly.

## 3. Audit forwarded headers at every use site

Fixing public/private classification alone is insufficient. Search every use of:

- `Host`
- `X-Forwarded-Host`
- `X-Forwarded-For`
- `X-Forwarded-Proto`
- vendor client-IP headers such as `CF-Connecting-IP`

Only consume forwarded values when the direct socket peer matches an explicit trusted-proxy IP/CIDR allowlist. Apply the same gate to:

- auth/public classification
- origin and CSRF comparison
- login rate-limit identity
- Secure-cookie decisions
- HSTS decisions
- redirects and absolute URL generation

Regression probes should prove an untrusted peer cannot alter each behavior. Also classify non-private direct peers as public regardless of a spoofed private `Host`.

## 4. Prefer explicit deployment policy

Provide explicit controls rather than inferring the entire security boundary from headers:

- configurable bind address, defaulting to loopback for development
- explicit trusted-proxy CIDRs, empty by default
- universal-auth mode for operators who want LAN authentication
- bounded request concurrency before expensive password hashing

## 5. Bound recovery artifacts persistently

Process-local deduplication resets on restart. Corrupt-config recovery copies and similar artifacts need a persistent count/age retention cap, or content-addressed deduplication that survives process restarts. Test this by simulating repeated restarts against unchanged corrupt input.

## 6. Final verification

Before commit and push:

- run spoof tests for Host and every forwarded header
- reject ambiguous framing: Transfer-Encoding, missing Content-Length, and duplicate Content-Length
- verify live state invariants are unchanged
- verify backup restore targets the configured runtime path, not the repository
- confirm dedicated service identity and capability restrictions
- run the complete test suite, live health check, secret scan, clean-tree check, and local/remote commit equality
