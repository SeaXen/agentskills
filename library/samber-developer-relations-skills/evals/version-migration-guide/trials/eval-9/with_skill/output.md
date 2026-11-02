# Ashgrove Log Pipeline: migrating from the legacy TCP ingest protocol to v8

**Status: draft for support and legal sign-off. It is not ready to publish.** Every `[CONFIRM: …]` marker is a fact I don't have, and I haven't invented any of them.

I read the skill and its references, but I did not run the interview or a cold upgrade. Section 5 lists what a publishable guide still needs.

---

## 1. Assumptions and open questions

**Assumptions**
- v8 is the first release without the legacy TCP ingest listener. It is a single hop from the last v7 minor.
- Contracts promise 90 days' notice of breaking changes, so the clock starts at formal notice under each contract, not at the v8 release date. Legal must confirm which event starts it (publication, email to the contract notice address, or both).
- Churn Rule: we operate or patch these deployments with our customers, so this is partly our work. The guide covers the customer-side steps, and Ashgrove offers vendor-run help for the rest (see [Support and escalation](#support-and-escalation)).

**Questions only you can answer**

| # | Question | Why it blocks |
|---|---|---|
| 1 | What is the exact last v7 version, and can one more v7 minor ship? | If it can, the staged path is the default. If not, this is a single hop. |
| 2 | When is v8 GA, and when does formal notice go out? | The removal date cannot be earlier than notice date + 90 days. |
| 3 | What is the longest patch cycle among the 9 air-gapped customers? | It sets the end date for their escape hatch (v7 support). |
| 4 | Which senders use the legacy protocol: Ashgrove forwarders, third-party shippers, or customer scripts? | It sets the blast-radius order. Without telemetry, ask each customer (see [Section 2](#2-inventory-and-blast-radius)). |
| 5 | Does v8 refuse to start if a legacy listener is configured, or ignore it? | It sets the literal error text. Recommend a hard failure at startup, not silent data loss. |
| 6 | What replaces the legacy protocol, and does it need TLS or auth setup the old one did not? | It drives the largest entry in the guide. |
| 7 | Who owns the migration tooling after v8 ships? | With no owner, we ship only search patterns and the warnings release, no codemod. |
| 8 | Does the contract require a specific channel for notice, or a migration-support commitment? | Legal decides what the guide may promise. |

**Telemetry:** there is none for the 9 air-gapped sites, and probably little for the other 25. This is a stated gap in the plan, not something to hide.

---

## 2. Inventory and blast radius

Ordered by how many deployments will hit each change. Every blast-radius cell is a hypothesis until each customer's sender inventory comes back. For the 34 contract customers, that is a census, so it should be complete, not a sample.

| # | Change | Type | Blast radius (hypothesis) | Evidence needed |
|---|---|---|---|---|
| 1 | Legacy TCP ingest listener removed | Removal | Every deployment with a sender on the old protocol | Sender census per customer |
| 2 | Legacy listener config now fails startup `[CONFIRM: fail vs ignore]` | Config change | Same set as #1 | Config diff of v7 vs v8 |
| 3 | Senders must use the new protocol, with its framing, ack and backpressure semantics | Wire change | Same set as #1, plus customers who relied on old ack behavior (Hyrum's Law) | Support tickets, protocol spec diff |
| 4 | Forwarder and agent version floors | Requirement floor | Customers running old forwarders | Version inventory |
| 5 | Dashboards and alerts keyed to the legacy port or its metrics | Removal | Customers with monitoring on the old listener | Metrics-name diff |
| 6 | Firewall and network rules for the old port | Housekeeping | Every affected customer, after migration | Not blocking |

Entries 1 to 3 are what customers must do before the removal date. The rest follow from them.

## 3. Recommended path shape

**Staged, with a single-hop fallback.** Ship one more v7 minor (`7.[LAST]`) whose only change is a runtime warning on each legacy connection. Each customer's logs then list their own legacy senders.

- **Air-gapped constraint:** warnings only help if the 9 air-gapped customers install `7.[LAST]` before v8. Ship it as an offline bundle with checksums. Budget their patch cycle (question 3) into the timeline.
- **Fallback:** if no v7 minor can ship, this guide is a single hop. The sender census then replaces the warning telemetry, and the timeline below stands unchanged.
- **Compat build:** none. A dual-protocol v8 would keep the removed listener alive. If a customer cannot migrate in time, the answer is the v7 escape hatch below, not a hidden flag.

---

## 4. The guide

*Draft text for publication. Replace each `[CONFIRM]` or `[DATE]` before release.*

---

# Upgrading from v7 to v8: legacy TCP ingest removed

**This guide covers** Ashgrove Log Pipeline `7.[LAST]` → `8.0` for on-premises and air-gapped deployments.
**Effort:** `[MEASURE: from the cold run; publish no figure until measured]`.
**Canonical URL:** `[URL]/migrate/v7-to-v8`. It will not move.

## Dates and notice

Read this first if you manage a contract or a change window.

| Event | Date |
|---|---|
| Notice published, and sent to contract notice addresses | `[NOTICE DATE]` |
| `7.[LAST]` available (online and offline bundle) | `[DATE]` |
| v8.0 generally available | `[DATE, no earlier than NOTICE DATE + 90 days]` |
| Legacy TCP ingest not supported in any v8 release | v8.0 GA |
| **v7 continues to receive security fixes until** | `[DATE]` (see [Managed and air-gapped deployments](#managed-and-air-gapped-deployments)) |

- You are never moved to v8 without your own change window. Ashgrove patches managed deployments only on the schedule you control `[CONFIRM against contract language]`.
- Upgrading to v8 does not depend on you finishing early. Staying on v7 until the date above is a supported choice.

### Support and escalation

- Support: `[CHANNEL / SLA]`.
- Escalation: `[NAMED ROLE, CONTACT]`.
- Ashgrove will `[CONFIRM WITH LEGAL: e.g. run the sender census with you, join a staging cutover]`.
- Do not wait for the deadline to ask. Open a ticket titled "v8 migration" and tell us your change-window dates.

## Before you start

1. Install `7.[LAST]` first. It behaves like `7.[PREVIOUS]` except that it logs a warning for every legacy connection. Your logs become your list of senders to migrate.
2. Run it for at least one full business cycle `[CONFIRM: recommend ≥ 1 month]`. Rare senders (monthly jobs, failover paths) only appear if they connect during that window.
3. Do not stop on `7.[KNOWN-BAD, if any]`. `[CONFIRM: delete this line if no release regresses.]`
4. Air-gapped sites: use the offline bundle `[PATH]`, and verify the checksum with the command below.

```sh
sha256sum -c ashgrove-7.[LAST]-offline.sha256
```

## Requirements

Machine-checkable floors. Fill these in once confirmed.

- Ashgrove forwarder `>= [X.Y]` (the version that speaks the new protocol)
- OS / kernel `>= [CONFIRM]`
- `[Any TLS, certificate or auth prerequisite the new protocol adds]` ← likely the largest hidden work item

## Breaking changes

### Removed: legacy TCP ingest listener {#removed-legacy-tcp-ingest}

**Affects you if** any sender writes to the legacy TCP ingest port (default `[PORT]`).
Find senders on a v7 host:

```sh
grep -E "legacy tcp ingest" /var/log/ashgrove/*.log   # [CONFIRM: exact path]
ss -tnp | grep ':[PORT]'
```

On `7.[LAST]` the warning is:

```
WARN  legacy_tcp_ingest deprecated: peer=<ip> removal=8.0   [CONFIRM: literal text]
```

On v8 a sender pointed at the old port gets `connection refused`.

The legacy protocol has no authentication and no framing guarantees, so a dropped connection can silently lose or split events. v8 removes it so that every accepted event has an acknowledgement. Senders must use `[NEW PROTOCOL]`.

```yaml
# Before (v7 forwarder config)
output:
  type: legacy_tcp
  host: ingest.example.internal
  port: [PORT]

# After (v8 forwarder config)
output:
  type: [NEW]
  host: ingest.example.internal
  port: [NEW PORT]
  [auth / TLS block]
```

**Fix** (manual; no codemod exists):
1. List every legacy sender from the warnings and the `ss` output.
2. Upgrade each to forwarder `>= [X.Y]`.
3. Change its output to the new type and port.
4. Confirm events arrive with `[VERIFICATION COMMAND, e.g. a count query]` before the next sender.
5. When the `legacy_tcp_ingest` warning stops appearing for a full cycle, the migration is complete.

**Escape hatch:** none in v8. Stay on v7 until the support-end date above (see below).

### Changed: v8 refuses to start with a legacy listener configured {#changed-legacy-listener-config}

`[CONFIRM behavior first.]` **Affects you if** your pipeline config contains `ingest.legacy_tcp`.
Search: `grep -rn "legacy_tcp" /etc/ashgrove/`.
v8 error: `[CONFIRM literal text]`.
We chose a hard stop at startup because silently ignoring the block would look like a running pipeline that drops data.

```yaml
# Before
ingest:
  legacy_tcp:
    enabled: true
    port: [PORT]
```

```yaml
# After: delete the legacy_tcp block entirely
ingest:
  [new listener block]
```

**Fix:** delete the `legacy_tcp` block and add the new listener block. **Escape hatch:** none.

### Changed: acknowledgement and backpressure behavior {#changed-ack-backpressure}

`[Fill from protocol spec diff.]` **Affects you if** a sender or script relied on the old protocol's behavior when the pipeline is busy or restarting (for example, blocking vs dropping vs buffering). Support has already seen `[CONFIRM: list known cases from tickets]`.
State here, for each behavior, what v7 did, what v8 does, and what the sender must now do. Include a before/after sender snippet per case.

### Changed: forwarder and agent version floor {#changed-forwarder-floor}

**Affects you if** any forwarder reports a version below `[X.Y]`: `ashgrove-forwarder --version`.
v8 rejects such senders at connect time with `[CONFIRM literal text]`.
**Fix:** upgrade forwarders to `>= [X.Y]` (offline package: `[PATH]`). **Escape hatch:** none.

### Removed: legacy-listener metrics and health checks {#removed-legacy-metrics}

**Affects you if** dashboards or alerts reference `[CONFIRM metric names, e.g. ingest_legacy_tcp_*]`.
Search your monitoring config for that prefix. After upgrade those series stop existing, and alerts that fire on absence will page.
**Fix:** point them at `[new metric names]`, and delete any health check on the old port.
**Escape hatch:** none.

## New deprecations

`[None, or list. Each row needs a replacement or "none".]`

## Deprecation timeline

| Deprecated | Replacement | Warning level in 7.[LAST] | Removed in |
|---|---|---|---|
| Legacy TCP ingest listener | `[NEW PROTOCOL]` | Runtime warning per connection | 8.0 |
| `ingest.legacy_tcp` config block | `ingest.[new]` | Runtime warning at startup | 8.0 |
| `ingest_legacy_tcp_*` metrics | `[new]` | Documentation only | 8.0 |

## Managed and air-gapped deployments

Your patch schedule is yours. The v7 line therefore has its own end date:

- **v7 security fixes until `[DATE]`.** `[CONFIRM: must be ≥ v8 GA + the longest air-gapped patch cycle, and no earlier than any contractual support term.]`
- **Delivery:** offline bundles for `7.[LAST]` and `8.x`, with checksums. Do not rely on online update checks.
- **Cutover:** Ashgrove staff do not change your running version without your scheduled window. Before your window you complete steps 1 to 5 in the removed-legacy-tcp-ingest entry. During it we `[CONFIRM: what Ashgrove does]`.
- **Rollback:** see below. Reinstall `7.[LAST]` from the offline bundle. Keep your v7 config backup until the new senders have run for a full cycle.

## Rollback

1. Before upgrading, back up `/etc/ashgrove/` and the data directory `[CONFIRM paths]`.
2. To roll back, stop v8, reinstall `7.[LAST]`, and restore the config. v7 listens on the legacy port again.
3. **Data caveat:** `[CONFIRM: whether v8 changes on-disk or queue formats. If so, state whether v7 can read data written by v8.]`
4. Rollback is possible until `[DATE]`, when v7 support ends.

## Housekeeping

After every sender is on the new protocol and v8 is running:
- Close firewall rules for the old port `[PORT]`.
- Remove legacy sender configs, including cron jobs and scripts that wrote to the old port.
- Delete dashboards and alerts on the `ingest_legacy_tcp_*` metrics.
- Remove any workaround scripts that re-sent events after a legacy connection dropped.

## Troubleshooting

| Text you see | Meaning | Go to |
|---|---|---|
| `connection refused` on the old port | Sender still on legacy protocol | [Removed: legacy TCP ingest listener](#removed-legacy-tcp-ingest) |
| `[v8 startup error text]` | Legacy listener block present | [Changed: listener config](#changed-legacy-listener-config) |
| `[v8 sender rejected text]` | Forwarder below floor | [Changed: forwarder floor](#changed-forwarder-floor) |
| Alert "no data on ingest_legacy_tcp_*" | Old metrics are gone | [Removed: legacy metrics](#removed-legacy-metrics) |

*(Add rows from support tickets and from the cold run.)*

## Full changelog

`[LINK]`. For traceability only; nothing in this guide depends on it.

---

## 5. Verification plan

No test project has been upgraded using this draft, so none of it is verified. Before publishing:

1. **Cold run.** Someone who didn't write the guide upgrades a real v7 deployment to v8 using only this page. Use a staging copy that has at least two legacy senders and one dashboard on the legacy metrics. Record elapsed time and publish that as the effort figure.
2. **Air-gapped run.** Do the same with the offline bundle on an isolated host. This path has the most unstated assumptions.
3. **Rollback run.** Execute the rollback on a copy. The rollback section is a promise, and legal will read it as one.
4. **Completeness.** Diff the v7 and v8 config schema, metric names and protocol spec against the entries above. Add anything support has already seen break.
5. **Sufficiency.** Any edit made during the cold run that the guide didn't describe is a defect in the guide.
6. **Review.** Support, then legal, then comms. Legal should confirm in particular: the notice start event, the "never moved without your window" sentence, the support-end date, and the vendor-assist wording. Say nothing in the guide that the contracts don't say.

## 6. KPIs

| Metric | Source | Note |
|---|---|---|
| **Senders still on legacy, per customer** | `7.[LAST]` warnings; for air-gapped sites, customer-reported counts at each check-in | The primary measure. 34 customers means a named list, not a percentage. |
| Customers fully migrated vs scheduled vs not scheduled | Account owners | Review weekly from notice date. |
| Tickets quoting an upgrade error, and which entry causes most | Support | Rewrite that entry first. |
| Guide search queries and exits to support | Docs analytics | Shows missing entries. |
| Stragglers after `[v7 end date]` | Same list as above | Worked directly by account owners. |

Start the per-customer list before notice goes out, because the first 90 days cannot be reconstructed afterward. Do not close the v7 escape hatch while any named customer is unmigrated and still within their contract.

---

**Next steps for you:**
1. Answer questions 1 to 8 in [Section 1](#1-assumptions-and-open-questions). Questions 1, 2, 3 and 6 unblock most of the `[CONFIRM]` markers.
2. Confirm the staged path in [Section 3](#3-recommended-path-shape), or tell me no v7 minor can ship.
3. I can then fill the placeholders and send the draft to legal.