Here are the five pages, ready to drop into the KB.

---

# KB-041 — `agent: operation failed (code 7)`

**Volume:** 41 records (highest single-string cluster) | **Status:** Open — triage workaround in place | **Owner:** Agent Core

## Symptom

The agent logs and surfaces exactly one string, `agent: operation failed (code 7)`, for at least six distinct underlying failures. The message carries no discriminating detail — no subcode, no field name, no upstream error. Support cannot resolve a single one of these tickets from the message alone; every case requires a debug-log pull before triage can even start.

## Why this is worse than a normal bug

A single string mapped to six causes means support's first reply is always "send logs," which adds a full round trip to every one of the 41 cases before real diagnosis begins. The cost here is triage latency, not the underlying failures themselves — some of which may be trivial once visible.

## Immediate workaround (support-facing)

1. Do not attempt to guess the cause from the ticket text. Request the debug bundle (`agent diagnose --bundle`) on first response — don't wait for a second exchange.
2. Grep the bundle for the log line immediately preceding `operation failed (code 7)`. That preceding line currently carries the real signal; code 7 is logged by a shared error-handling path that discards it.
3. File the underlying cause against this KB entry's tracking issue with the preceding-line text attached, so the six causes can be catalogued from real data rather than guessed.

## Root cause

Code 7 is a catch-all returned by a shared error-wrapping function; whatever specific error each of the six call sites produced gets normalized away before it reaches the log line the customer sees. This is an error-handling defect, not six separate bugs — fixing the wrapper fixes all six at once.

## Real fix (tracked, not yet shipped)

Replace the shared wrapper's single exit code with the six original error identities, surfaced as either distinct codes (`code 7a`–`7f`) or a structured field (`cause=`) on the same log line. Until that ships, this cluster cannot shrink — it can only be triaged faster.

## Prevention

Add a lint rule (or code-review checklist item) that rejects new call sites feeding into a shared catch-all error path without a preserved cause field. This defect class will recur elsewhere in the codebase if the pattern itself isn't flagged.

---

# KB-019 — Collector drops spans silently behind a TLS-terminating proxy

**Volume:** 19 records | **Status:** Fix known and documented | **Owner:** Collector / Platform

## Symptom

Customers running the collector behind a TLS-terminating proxy see spans vanish with no error, no warning, and no rejected-request log anywhere in the pipeline. Data loss is silent, which is why these tickets arrive as "our dashboards look wrong" rather than "we got an error."

## Root cause

The collector validates the upstream TLS chain against the certificate bundle baked into `agent.yaml` at startup. When a TLS-terminating proxy sits in front of the customer's endpoint, the proxy presents its own certificate, which the collector's stale bundle doesn't trust. Rather than surfacing a TLS handshake error, the current failure path drops the span and moves on — this silent-drop behavior, not the mismatch itself, is the second half of the defect and should be tracked separately.

## Fix procedure — order matters

Performing these steps out of order corrupts the queue. Follow this exact sequence:

1. **Edit `agent.yaml`** — point the trust bundle path at the proxy's CA certificate, not the origin server's.
2. **Regenerate the cert bundle** — run the bundle-regeneration step so the new trust root is actually compiled into the artifact the collector loads. Editing the YAML alone does not do this.
3. **Edit `collector.toml`** — update the matching TLS section to reference the regenerated bundle's new path/hash.
4. **Restart the collector.**

Reversing steps 1 and 3, or restarting before step 2 completes, leaves the collector holding a queue reference to a bundle that no longer matches what's on disk — this is the corruption support has seen when customers self-serve this fix from partial documentation.

## Support script

Ask first: "Is there a TLS-terminating proxy, load balancer, or service mesh sidecar in front of the agent?" This single question identifies the cluster before any log review is needed.

## Prevention

File against Collector: make step ordering unnecessary by having the collector detect a bundle/config mismatch and refuse to start (loud failure) rather than silently dropping spans against a stale trust root. That also converts the *next* occurrence of this misconfiguration from a silent data-loss ticket into a startup error — a strictly better failure mode even before the underlying TLS handling is redesigned.

---

# KB-033 — `403 ingest rejected: account not provisioned`

**Volume:** 33 records | **Status:** Not a bug — support/billing macro | **Owner:** Support, with Billing as escalation path

## Symptom

Ingest requests return `403 ingest rejected: account not provisioned`. Every one of the 33 records traces back to one of two account states: an expired trial, or a plan downgrade that dropped ingest entitlement.

## Root cause

None — this is the provisioning check working as designed. The cluster exists because the error message doesn't tell the customer *which* of the two states they're in, or what to do about it, so every case becomes a ticket instead of a self-service fix.

## Resolution

- **Expired trial:** direct to plan upgrade/renewal flow. No engineering involvement needed.
- **Plan downgrade:** confirm the downgrade in the billing console, then either restore ingest entitlement on the current plan or point the customer at the plan tier that includes it.

Support should be able to close these without pulling logs — checking account/plan status in the billing console is sufficient and faster than a diagnostic round trip.

## Recommended fix (product, not urgent)

Split the single 403 message into two: `account_trial_expired` and `account_plan_downgraded`, each with a link to the relevant self-service action (renew / upgrade). This is a low-effort change that could convert most of this cluster into zero-ticket self-service, since the underlying cause is already fully known — support only lacks the ability to *show* customers the distinction the account record already contains.

## Prevention

None needed on the engineering side; this is working as intended. The only preventable cost is the support round trip, addressed above.

---

# KB-028 — `E_SHARD_UNAVAILABLE`

**Volume:** 28 records, 100% within the 11 days since release 5.2 | **Status:** Suspected regression — active investigation | **Owner:** Storage/Sharding, escalated to on-call

## Symptom

Ingest or query requests fail with `E_SHARD_UNAVAILABLE`. Zero occurrences exist in the record history before 5.2's release date; all 28 fall inside the 11 days since.

## Why this gets priority over its raw count

A brand-new error with zero prior baseline and a clean correlation to a specific release is the strongest signal in this batch that something 5.2 changed broke shard availability — not customer environment, not load, not chance. Treat the release correlation as the primary lead, not one hypothesis among several.

## Immediate action

1. Pull the 5.2 diff for any change touching shard discovery, shard-to-node assignment, or the shard health check — that's where a change would produce this exact symptom with no ramp-up period.
2. Check whether the 28 records cluster on a specific shard count, region, or upgrade path (in-place upgrade vs. fresh 5.2 install) — that split will confirm or rule out a migration-time bug versus a steady-state bug in 5.2's sharding logic.
3. Confirm whether affected customers can work around it by pinning to 5.1 while the regression is isolated — if yes, offer that as an interim mitigation on open tickets.

## Root cause

Not yet identified. This page will be updated once the offending change is found; until then, treat "shipped in 5.2" as confirmed and "which specific change" as the open question.

## Prevention

Once found, add a regression test covering the specific shard-availability path that broke, and check whether the release process needs a shard-health smoke test before 5.2-class releases ship — a clean zero-to-28 jump on day one suggests this would have been caught by a basic post-release smoke check rather than requiring customer reports.

---

# KB-012 — Memory ballooning under high cardinality

**Volume:** 12 records | **Root cause in 4 of the last 7 incident reviews** | **Status:** Chronic, under-tracked relative to its actual cost | **Owner:** Agent Core / Performance

## Why this page exists despite the low ticket count

Twelve support records understate this cluster's real cost. It's the named root cause in more than half of the team's last seven incident reviews — meaning its actual impact shows up as outages and escalations, not tickets, because customers experiencing it often can't file a clean ticket before the agent is already unresponsive. Rank this by incident weight, not record count, when prioritizing against the other four clusters.

## Symptom

Agent memory grows unbounded when the customer's workload has high-cardinality labels/tags (for example, per-request or per-user dimensions with unbounded value sets). Left unaddressed, it ends in an OOM kill, taking the agent — and the customer's observability into whatever it was watching — down with it.

## Root cause

The agent's in-memory aggregation structures index by label combination, and nothing currently bounds the number of distinct combinations tracked. A workload with an unbounded-cardinality label turns that index into unbounded memory growth.

## Immediate mitigation (support-facing)

1. Identify the offending label(s) — look for tags whose value set correlates with request count or user count rather than a fixed small set of categories.
2. Recommend a cardinality limit or label drop/rewrite rule on the offending tag as an interim customer-side mitigation.
3. If the agent is already in a degraded state, a restart temporarily clears the index — flag this as a stopgap, not a fix, since it will recur under the same workload.

## Real fix (needs prioritization commensurate with its incident weight, not its ticket count)

Add a configurable cap on tracked label-combination cardinality, with a documented, predictable behavior when the cap is hit (drop new combinations, aggregate overflow into an "other" bucket, or emit a warning) instead of growing without bound. This is a design change to the aggregation path, not a patch — size the effort accordingly.

## Prevention

Add a memory-growth alert tied to label cardinality growth rate, not just absolute memory, so this surfaces as a monitored signal before the next incident review rather than after it.