## Corvid Cache doc-gap analysis — Sept 3 (4.2 release) support review

### Signal read

- **connection-refused**: 31 tickets, evenly split before/after Sept 3, 812 telemetry events (~26 events/ticket). Flat rate across the release boundary → chronic environmental issue, not caused by 4.2.
- **token-expired**: 24 tickets, **100% after Sept 3** (zero before), 1,140 telemetry events (~48 events/ticket). Zero-before/all-after is a regression signature, not "users didn't read the changelog."
- 1,952 telemetry events vs. 55 tickets total → ~97% of failures never reach support. Docs need to catch the silent-retry majority, not just the ticket-filers.

### Priority

**P0 — token-expired** (release-tied, full auth lockout, newest, highest event/ticket ratio)
**P1 — connection-refused** (chronic, higher raw ticket count, but not a regression)

---

### Doc target 1 (P0): "Token expired after upgrading to 4.2"

- Slug: `/docs/troubleshooting/token-expired-after-4-2`
- Audience: Java + Go clients upgrading from pre-4.2
- Embed verbatim (for search/Ctrl-F match):
  - `CorvidAuthException: credential rejected, token expired`
  - `auth failed: token expired for node <node>`
- Outline:
  1. What changed in 4.2 auth — state plainly whether token TTL, refresh flow, or clock-skew validation changed. **Confirm with engineering before publishing** — 0-before/24-after is more consistent with an unintended regression than an undocumented-but-intended change.
  2. Symptom match: exact error strings above + "started right after upgrading to 4.2."
  3. Fix/workaround: Java token-refresh snippet + `CorvidAuthException` catch pattern; Go client equivalent.
  4. Credential rotation steps if that's the actual fix (exact CLI/API call).
  5. Escalation line: mid-session (not just at-upgrade) expiry → file a ticket, likely a bug not a config gap.
- Parallel action: open/confirm an engineering ticket regardless of doc publication. A doc page documents a regression — it doesn't fix one.

### Doc target 2 (P1): "Connection refused" / cluster connectivity

- Slug: `/docs/troubleshooting/connection-refused`
- Audience: infra/ops standing up cache-prod/staging clusters, both client languages
- Embed verbatim:
  - `connection to corvid://<node>:7946 refused after 20s`
  - `dial tcp <ip>:7946: connect: connection refused`
  - `CorvidConnectionException: caused by java.net.ConnectException: Connection refused`
- Outline:
  1. Port 7946 requirement (gossip/membership) — must be open both directions, client subnet included.
  2. Pre-flight checklist: DNS resolves node hostname? firewall/security group/k8s NetworkPolicy allows 7946? node health check passing?
  3. Why 20s specifically — document the connect timeout, whether it's configurable, retry behavior after.
  4. Staging-specific gotchas — one ticket names staging explicitly, suggests env-specific DNS/config drift worth calling out separately from prod.
  5. Client-specific snippets (Java/Go) + how to raise log verbosity to diagnose faster.
- Because this is chronic, pair it with a **reference page** (ports/firewall requirements table), not just a reactive troubleshooting page — prevents the next 31 tickets instead of just answering them faster.

### Cross-cutting

- **Troubleshooting index**: surface both pages by exact error string at the top, since these are this cycle's top two categories. Create one if none exists.
- **4.2 release notes**: add a visible callout linking straight to the token-expired page — upgrading users read the changelog before they ever hit the error.

### Success metric

- 2-week post-publish watch: connection-refused ticket rate flat-to-down (environmental — docs reduce confusion, won't zero it out); token-expired trending to zero once the doc and/or the eng fix ships.
- Watch event-to-ticket ratio, not just ticket count — events staying high while tickets drop means users are self-serving via the new docs, which is the real target, not ticket suppression.