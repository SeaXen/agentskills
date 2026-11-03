---
name: hermes-network-health-check
category: devops
description: Quick non-blocking network checks for Hermes Agent.
---

# Hermes Network Health Check — Quick & Non-Blocking

**Purpose**: Verify network connectivity for Hermes Agent **without** triggering long-running tests that make Discord appear offline.

---

## When to Use

- User reports Hermes Discord appears offline
- Need to verify basic connectivity before diagnosing deeper issues
- Quick pre-flight before network-dependent operations

---

## The Rule (User Preference)

> **"stop doing this every time you do this hermes discord get offline"**

Long-running network tests (WARP connect/disconnect cycles, multi-minute speedtests) **make Hermes Discord appear offline** on this host. **Avoid these tests unless explicitly asked and warned first.**

---

## Safe Checks (Use These)

| Check | Command | Duration | Notes |
|---|---|---|---|
| WARP status | `warp-cli status` | <1s | Shows connection state |
| Public IP | `curl -s ifconfig.me` | <1s | Verify outbound connectivity |
| Cloudflare trace | `curl -s https://1.1.1.1/cdn-cgi/trace` | <1s | CDN connectivity |
| DNS resolution | `dig +short google.com` | <1s | DNS working |
| Gateway status | `hermes gateway status` | <1s | Hermes gateway |

---

## Dangerous Checks (AVOID)

| Check | Why | Alternative |
|---|---|---|
| `warp-cli connect/disconnect` | Multi-second, triggers offline | `warp-cli status` |
| `speedtest-cli` | 30-60s blocks | `curl ifconfig.me` |
| `ping -c 100` | 100+ seconds | `ping -c 1` |
| `mtr` | Continuous | Single `dig`/`curl` |
| `traceroute` | 10-30s | Cloudflare trace |
| Puppeteer network tests | Heavy | browser-tool only |

---

## Diagnostic Flow

```
1. hermes gateway status
2. warp-cli status
3. curl -s ifconfig.me
4. curl -s https://1.1.1.1/cdn-cgi/trace
```

If all pass: NOT a network issue.

---

## Deep Tests Require Warning

If user asks for full diagnostic:
1. Warn: "2-3 min, may make Discord offline. Continue?"
2. Only proceed if confirmed
3. Run in background with `notify_on_complete=true`

---

## Cross-References

| Related | Relationship |
|---|---|
| `hermes-gateway-safe-restart` | Gateway restart |
| `sagar-hermes-ops` | User-specific ops |

---

## Pitfalls

- Deep tests without warning → Discord offline
- Assume network when gateway down → check gateway first
- Puppeteer for network → use browser-tool
- Multi-minute foreground tests → background + notify
