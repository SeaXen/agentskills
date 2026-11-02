Using the developer-troubleshooting-docs skill (methods: KCS capture/evolve loop, OASIS DITA `<troubleshooting>` topic type, Nielsen heuristic 9, Google SRE postmortem practice) to turn your five clusters into pages — with the document-vs-fix gate applied per cluster, since two of these clusters shouldn't ship as public pages at all.

**Assumptions taken instead of blocking on the interview** (state these back to me if wrong): docs site format unspecified → plain Markdown; no version/field names given → `<PLACEHOLDER>`; no ticket exports available → nothing below was reproduced against a live agent, so every entry ships with an explicit unverified note per Step 7; coverage target = 100% of this batch (all 5 survived mining, none dropped at the self-serviceability gate outright, though C changes shape); owners unnamed → `TBD`, yours to assign.

---

## 1. Ranked cluster queue

| # | Cluster | Count | Shape | Gate | Why this order |
|---|---|---|---|---|---|
| 1 | D — `E_SHARD_UNAVAILABLE` | 28 | Known-issues entry | **Above the line** — regression, file it | Zero occurrences before 5.2, 28 in 11 days = growing ~2.5/day. Cheapest page to write (one cause, "under investigation"), highest urgency. |
| 2 | B — silent span drop behind TLS proxy | 19 | Troubleshooting how-to | Above the line (DX fix owed) + interim page now | Wrong-order fix corrupts the queue — blast radius is severe even though count is mid-pack. Ships as a page today; escalate for a single fixing command. |
| 3 | C — `403 ingest rejected: account not provisioned` | 33 | **Not a public page** | Routed away from docs | Matches the routing table row verbatim: "cause is account state → product surface or support macro, not a public page." Second-highest count but near-zero doc effort — the fix is a string change, not a page. |
| 4 | A — `agent: operation failed (code 7)` | 41 | Error reference entry (draft, blocked) | Above the line — message doesn't name what to do | Highest count, but the six real causes aren't in evidence I have. Ships as a self-serve triage entry now; full six-branch version is blocked on support/eng input. |
| 5 | E — memory ballooning, high cardinality | 12 | Troubleshooting how-to | Above the line — named in 4/7 postmortems, promoted by hand despite low count | Explicitly the "rare and expensive, promote from incident review" case in Step 2. Page ships as an admitted stopgap, not a substitute for the fix. |

Two of these are not simple "write the page" cases — C is redirected entirely, D and A ship as intentionally partial/short-lived artifacts. That's the gate working, not scope creep.

---

## 2. The five deliverables

### D — `E_SHARD_UNAVAILABLE` (Known-issues entry)

```markdown
### Shard temporarily unavailable during ingest (`E_SHARD_UNAVAILABLE`) — affects 5.2.x, reported 2026-09-19

**Symptom**: Agent or collector logs `E_SHARD_UNAVAILABLE` and the affected batch is not ingested.

```text
E_SHARD_UNAVAILABLE
```

**Applies to**: 5.2.0 and later. Zero reports before 5.2 shipped (11 days ago); 28 reports since, and growing daily — this is a regression, not a pre-existing edge case.

**Cause**: Under investigation. Correlates exactly with the 5.2 release; not yet isolated to a specific 5.2 change. Do not publish a speculative cause — say "under investigation" until engineering confirms it, per the skill's rule that an unverified cause stated confidently costs more trust than an admitted gap.

**Workaround**: None confirmed yet from the evidence I have. Two candidates for engineering to validate before I publish them as steps: (a) retry-with-backoff on the client side, if the unavailability is transient per-shard; (b) pin affected accounts to pre-5.2 shard-routing behavior, if a feature flag exists for it. Do not ship either as a documented workaround until reproduced.

**Tracking**: `<file the regression now — link here>` **Fixed in**: unreleased
```

**Action, not just a page**: file this as a regression against 5.2 today — Google SRE's rule applies directly: a workaround page "can speed up incident response" but the postmortem/regression fix is what actually stops the recurrence, and growth rate says this isn't stabilizing on its own.

**Retire this entry** the moment a 5.2.x patch ships: move the one line into the changelog, delete the entry. A known-issues list that only grows becomes a graveyard nobody reads.

---

### B — Silent span drop behind a TLS-terminating proxy (Troubleshooting how-to)

```markdown
# Spans silently dropped when the agent sits behind a TLS-terminating proxy

## Symptoms

- No spans arrive from a host running behind a TLS-terminating (MITM-style) proxy.
- No error is logged by the agent or the collector — the drop is silent.
- Works when the same agent runs without the proxy in the path.

## Before you start

You need: edit access to `agent.yaml` and `collector.toml` on the affected host, permission to regenerate the local cert bundle, and permission to restart the collector. Confirm a maintenance window — this fix restarts the collector's ingest queue.

## Check 1 — confirm the proxy is TLS-terminating

<PLACEHOLDER: command to confirm, e.g. compare the leaf cert served on the agent→collector connection against the collector's own cert>. If the served cert's issuer is the proxy rather than your own CA, this is the cause.

## Fix — exact order matters, do not skip or reorder

Running these out of order corrupts the local ingest queue and requires a full queue rebuild to recover. Do all four steps in one pass, don't pause between step 2 and step 3.

1. Edit `agent.yaml`: point the agent's trust store at the proxy's intercepting CA certificate (`<TLS_TRUST_STORE_PATH>`). Do not restart yet.
2. Regenerate the cert bundle: `<PLACEHOLDER command>`. This must run after step 1 — regenerating against the old trust store is what corrupts the queue.
3. Edit `collector.toml`: set `<COLLECTOR_TLS_CONFIG_KEY>` to the same CA reference used in step 1.
4. Restart the collector: `<PLACEHOLDER restart command>`.
   - Expected: collector comes up clean, no `queue corrupt` line in its startup log.
   - If you see a queue-corruption error here: you restarted before step 2 finished, or edited the files out of order. Do not attempt to repair the queue by hand — wipe the local queue directory and restart again from a clean state; you will lose any spans buffered since the last successful flush.

## Confirm it worked

Spans from the affected host appear in the backend within one flush interval, and `collector.toml`'s startup log shows no TLS handshake warnings.

## Still stuck

Attach: `agent.yaml` and `collector.toml` (redact the trust-store path if it contains an internal hostname), the collector startup log, and whether step 4's queue-corruption message appeared.

---
Last verified: not reproduced — draft written from the reported symptom and fix sequence, not executed against a live agent/proxy pair. Ship with the "reported, not reproduced" note until run once end-to-end. Owner: TBD.
```

**Escalate alongside the page**: this is the routing table's "fix is edit three config files in order" row — the permanent answer is a single idempotent command (`agent doctor --fix-tls-proxy` or equivalent) that does all four steps atomically, not four manual edits a reader can get wrong. Say this to engineering explicitly; the page is the stopgap, not the fix.

---

### C — `403 ingest rejected: account not provisioned` (routed away from docs — not a page)

This cluster fails the "write a page" test on purpose. All 33 records reduce to one deterministic cause — expired trial or plan downgrade — which is exactly the routing table's row: *"Cause is account state (quota, plan, suspension) → Product surface or a support macro, not a public page."* A public troubleshooting page for this would out-compete a fix that's strictly better: tell the reader the real reason at the moment of failure.

**What I'm delivering instead of a page:**

1. **Product string change** (send to the owning team, not docs):
   ```
   403 ingest rejected: account not provisioned — your trial has expired or your
   plan no longer includes ingest. Renew or upgrade at <BILLING_URL>.
   ```
   This alone should collapse most of the 33/cycle to zero support contact, because the fix is now in the one place every one of those readers already is — the response they got.

2. **Support macro** (KCS-style, for the tickets that still arrive before the string ships):
   ```
   Subject: 403 ingest rejected: account not provisioned
   This means your trial has expired or your plan was downgraded below the ingest
   tier. Check your plan status at <BILLING_URL>. Renewing/upgrading restores
   ingest immediately — no agent-side change needed.
   ```

If you still want a public-facing landing point for the exact string (some readers will paste it into search before opening a ticket), the only version that earns its place is one line pointing at the billing page — not a six-part troubleshooting entry for a billing state.

---

### A — `agent: operation failed (code 7)` (Error reference entry — draft, partially blocked)

```markdown
# `agent: operation failed (code 7)`

The agent emitted a generic failure code without saying which of several internal errors occurred.

## Message

```text
agent: operation failed (code 7)
```

## Applies to

<PLACEHOLDER: versions — not in the evidence I have>. 41 reports so far; this code has been confirmed to map to at least six distinct underlying failures, most of which are only resolved today by support requesting logs.

## Cause

`code 7` is a catch-all exit code that does not distinguish between its underlying causes. The reader cannot self-diagnose from the message alone — that's the defect, not a support gap.

## Fix

### Self-serve first: find the real reason before filing a ticket

1. Locate the agent's local debug/error log (the one support currently asks for): `<PLACEHOLDER log path>`.
2. Find the line immediately preceding `operation failed (code 7)` — it carries the actual subsystem and reason string support uses to triage today.
3. Match that reason against the table below.

| Confirmed underlying cause | Fix | Status |
|---|---|---|
| `<TBD — pull from the last 41 ticket resolution notes>` | `<TBD>` | Unconfirmed |
| `<TBD>` | `<TBD>` | Unconfirmed |
| `<TBD>` | `<TBD>` | Unconfirmed |
| `<TBD>` | `<TBD>` | Unconfirmed |
| `<TBD>` | `<TBD>` | Unconfirmed |
| `<TBD>` | `<TBD>` | Unconfirmed |

I don't have the six real causes — nobody handed me the ticket exports or resolution notes this pass. Filling this table is the highest-leverage single task left on this cluster; it converts every future "ask for logs" into a table lookup.

## Confirm it worked

The subsystem named in step 2's reason string no longer appears, and the operation that failed now completes.

## Still stuck

Attach the full debug log line from step 2, the agent version, and the operation being attempted when it failed.

---
Last verified: not reproduced. Steps 1–2 (self-serve log lookup) are safe to publish now. The six-row table is a **draft skeleton, not fact** — do not publish it until support/eng confirms the real causes. Owner: TBD.
```

**Escalate alongside the page**: split `code 7` into distinct codes, or at minimum emit the reason string already used for support triage directly in the top-level message (`agent: operation failed (code 7: <reason>)`). That's the routing table's "error text does not name what to do" row — a doc page is a workaround for a message defect, not a fix for it.

---

### E — Memory ballooning under high cardinality (Troubleshooting how-to — stated admission)

Saying this out loud per Step 3: publishing this page is an admission that a defect named in 4 of the last 7 incident reviews is being tolerated, not fixed. It ships anyway because readers are hitting it now and a scheduled fix takes longer than this cycle. Owner for the scheduled fix: **TBD — name someone before this ships**, not "the team."

```markdown
# Agent memory grows unbounded under high-cardinality workloads

## Symptoms

- Agent RSS climbs steadily over hours/days rather than plateauing.
- Eventually OOM-killed or restarted by the host's supervisor.
- Correlates with label/tag sets that include high-cardinality values (user IDs, request IDs, raw timestamps used as label values).

## Before you start

You need: access to the agent's own memory metric or host-level RSS for the process, and the ability to inspect which labels/tags are attached to the spans or metrics it's processing.

## Check 1 — confirm high cardinality is the driver (cheap, do first)

<PLACEHOLDER: command to list active series / distinct label-value count>. A count in the tens or hundreds of thousands for a single label is the signature of this failure; a flat, bounded count means this isn't your cause — stop here and file a fresh ticket instead of following the rest of this page.

## Check 2 — identify the offending label(s)

Look for labels whose values are effectively unique per event (user ID, session ID, raw request ID, unrounded timestamp). Each distinct value the agent has ever seen typically stays resident until restart — that's the mechanism, not a guess: confirm by watching RSS after removing one candidate label from the pipeline and observing whether growth stops.

## Mitigate now (does not fix the underlying defect)

1. Drop or hash high-cardinality labels at the source before they reach the agent, if your pipeline supports a label-filtering step: `<PLACEHOLDER config key>`.
2. If no filtering step exists yet, schedule a periodic agent restart as a stopgap to bound memory — this is a mitigation, not a resolution, and it should be removed the moment the underlying fix ships.

## Confirm it worked

RSS plateaus within one observation window after removing or bounding the high-cardinality label, instead of continuing to climb.

## Still stuck

Attach the RSS graph over the growth period, the label(s) you identified in Check 2, and the approximate distinct-value count from Check 1.

---
Last verified: not reproduced against a live high-cardinality workload — written from the incident-review pattern, not an executed repro. Owner: TBD. This page is a stopgap; the scheduled fix (a cardinality guard or bounded eviction on the agent's label store) belongs to engineering, tracked at `<link the postmortem action items here>`.
```

---

## 3. Verification log

| Cluster | Reproduced? | What's confirmed | What's blocking full verification |
|---|---|---|---|
| D | No | Regression window and count | Root cause; no workaround to test yet |
| B | No | Fix sequence as reported | Exact config keys/commands; needs one real end-to-end run |
| C | N/A | Cause is deterministic (billing state) | No page shipped, so no fix to verify — only the string change needs sign-off from the owning team |
| A | Partially | Self-serve log-lookup steps are safe as written | The six underlying causes — need the actual ticket resolution notes |
| E | No | Correlation with high-cardinality labels, matches 4/7 postmortems | Exact mitigation config key; needs one real repro on a ballooning host |

Per Step 7, none of these ship as confidently-verified pages today — they ship with the explicit "reported, not reproduced" note attached above. Have someone run each cold before it goes live; that's usually where the placeholder commands turn out wrong.

---

## 4. Wiring and measurement plan

- **D, B, A, E**: link from wherever the string is emitted — the agent's own error output should point at the entry (a `doc_url`-style field in the payload, Stripe's pattern, is the cheapest version of this if the payload is structured).
- **C**: no doc link needed once the product string carries the answer itself — that's the point of routing it away from docs.
- **B's escalation** and **E's escalation**: track as engineering tickets, not docs tickets — a docs-owned ask to change agent internals goes nowhere.
- Metrics to watch per entry once live: ticket volume per error on a fixed window (before/after), zero-result docs-search queries for each exact string, and — for A specifically — the size of the six-cause table filling in over time as a coverage proxy.
- Refuse to promise a deflection percentage; Gartner's 5,728-customer survey puts full self-service resolution at 14% even for best-in-class docs. Track resolution rate and cost per resolution instead.

## 5. Maintenance triggers

- **D**: delete on the 5.2.x patch that fixes it; move the one line to the changelog.
- **A**: re-run the mining pass after the six-cause table is filled — if new records still show up with no matching row, the table is incomplete, not the page.
- **B, E**: re-verify on the next release that touches the collector/agent memory path respectively.
- **C**: no maintenance — it's not a page.
- Stamp last-verified dates once each entry is actually run end-to-end; today's drafts are explicitly not stamped as verified.