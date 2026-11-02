# Ashgrove Systems v7 to v8 migration guide: legacy TCP ingest removal

I drafted this without access to your code, contracts or release plan. Everything in `[BRACKETS]` is a fact only you can supply. I did not invent protocol names, flags, ports, versions or dates. Section 0 is for you and Legal and should not be published. Sections 1 to 10 are the guide.

---

## 0. Internal notes (do not publish)

**Decisions needed before publishing**

| # | Decision | Why it blocks |
|---|---|---|
| 1 | The notice clock. The contracts say 90 days' notice, but when does it start: on dispatch, on receipt, or on the date of a named notice channel? Legal must confirm the trigger and whether publishing this guide counts as notice. | Every date below derives from it. |
| 2 | The v7 support commitment. Will v7 keep receiving security fixes after v8 ships? Until when? | The "stay on v7" path depends on it. If the answer is "no end date", say that. If it is "none", the 90-day promise needs a second look for air-gapped customers. |
| 3 | Whether a v7 release exists that logs a deprecation warning for legacy TCP use. This is the staged path, and it is the best option if v7 can still ship. | It turns each customer's logs into their own inventory. Air-gapped customers cannot discover this any other way. |
| 4 | Whether v8 can run during the transition with legacy TCP disabled but detectable, so a connection attempt gets a clear refusal message. | Without it, a missed sender fails silently as dropped logs. |
| 5 | Who answers support and escalation questions during the window, and the contractual response times. | Contractual readers need a named owner. |

**Date arithmetic.** Today is 2026-10-03. If notice is deemed given on 2026-10-05, 90 days later is 2027-01-03. Treat that as the earliest v8 date that can break legacy TCP for anyone. Legal may require more, such as business days, receipt delay or a longer window in specific contracts. Check all 34 contracts for stricter notice clauses before fixing the date.

**The 9 air-gapped customers.** The guide must work with no internet, no phone-home and no vendor access, and on a schedule they control. I wrote it that way. Two consequences:

- You cannot measure their adoption by telemetry. Track them by named account and by a direct contact checklist.
- "We ship v8 on date X" cannot mean "they are on v8 on date X". The guide therefore separates when v8 is available from when each customer chooses to move. Do not promise otherwise in print.

**Legal should check:**

- No sentence promises a date or support level that is not in section 0 decision 1 or 2.
- "Breaking change" is used consistently with the contract definition.
- The guide does not offer remedies, credits or SLAs.
- Nothing names customers. I wrote none.

---

## 1. Summary

Ashgrove v8 removes the legacy TCP ingest protocol. After upgrading to v8, any sender that still uses it can no longer deliver logs to your pipeline.

- **Who is affected:** deployments with any agent, forwarder, appliance or script that sends logs over the legacy TCP ingest protocol.
- **Who is not affected:** deployments where every sender already uses `[REPLACEMENT PROTOCOL NAME]`.
- **What you must do:** move every legacy TCP sender to `[REPLACEMENT PROTOCOL NAME]` before upgrading the receiving side to v8.
- **Notice:** this guide is part of our notice that v8 removes legacy TCP ingest. v8 is available from `[DATE: notice date + at least 90 days]`. You choose when to upgrade. v7 remains `[SUPPORT STATEMENT FROM DECISION 2]`.
- **Contact:** `[SUPPORT CHANNEL, NAMED OWNER, RESPONSE TIMES]`.

## 2. Timeline

| Date | Event |
|---|---|
| `[NOTICE DATE]` | This guide is published and notice is given. |
| `[DATE]` | v7.`[X]` released. It logs a warning when legacy TCP ingest is used (see decision 3). |
| `[NOTICE DATE + 90 days or more]` | v8 generally available. Legacy TCP ingest is removed. |
| `[DATE]` | End of v7 security fixes (see decision 2). |

You control when you move to v8. Upgrading to v8 is the point at which legacy TCP stops working, not before.

## 3. Choose your path

Follow the staged path unless you cannot install v7.`[X]`.

1. **Staged (recommended).**
   1. Upgrade to v7.`[X]`. It changes nothing except the warning.
   2. Find every sender the warning names and migrate it.
   3. When the warning has been silent for `[N]` days of full traffic, upgrade to v8.
2. **Single hop.** Inventory senders manually (section 5), migrate them, then upgrade to v8. Choose this if you want one change window and your sender list is short and known.

If you stay on v7, see section 2 for what is supported and until when.

## 4. Requirements before you start

Check these first; they cannot be fixed mid-upgrade.

- Running v7 version: `>= [MINIMUM v7 VERSION]`. Older versions go to `[MINIMUM]` first. Do not skip intermediate versions: `[KNOWN-BAD VERSION, IF ANY: "skip X, go directly to Y, because ..."]`.
- Every sender can run a version that supports `[REPLACEMENT PROTOCOL NAME]`: `>= [MINIMUM AGENT/FORWARDER VERSION]`.
- `[REPLACEMENT PORT/TLS/AUTH REQUIREMENTS, e.g. new port, certificates]` are available on the receiver.
- Firewall rules allow the replacement protocol between every sender and the receiver.

**Air-gapped installations.** Everything needed is in the offline bundle: `[BUNDLE NAME, CHECKSUM/SIGNATURE VERIFICATION COMMAND]`. It includes v7.`[X]`, v8, sender packages and this guide in `[FORMAT]`. No step in this guide requires internet access or contact with Ashgrove.

## 5. Find every legacy TCP sender

This is the step most likely to go wrong. The senders you forgot are the ones that break.

**5.1 From v7.`[X]` warnings.** The receiver logs:

```
[EXACT WARNING TEXT]
```

Search for it:

```
[SEARCH COMMAND, e.g. grep against the receiver log path]
```

**5.2 From the receiver, without v7.`[X]`.** List current connections on the legacy listener and record source addresses over at least one full business cycle (include month-end and any batch jobs):

```
[COMMAND TO LIST LEGACY LISTENER CONNECTIONS / METRIC NAME]
```

**5.3 From configuration.** Search your sender configs and deployment automation for the legacy TCP target:

```
[SEARCH PATTERN: setting name, port number]
```

**5.4 Sources people forget:**

- appliances and network devices with a hard-coded log destination
- scripts and cron jobs that send over a raw socket
- test and staging systems
- senders that only run quarterly or at year end
- third-party software configured by a vendor

Write down each source, its owner and its migration status before moving on.

## 6. Migrate each sender

### Changed: sender protocol moves from legacy TCP to `[REPLACEMENT PROTOCOL NAME]` {#sender-protocol}

**Affected if:** the sender config contains `[SEARCH PATTERN]`, or v7.`[X]` logs `[EXACT WARNING TEXT]`. After upgrading to v8 it appears as `[EXACT ERROR TEXT SENDER SEES]` on the sender and `[EXACT RECEIVER LOG TEXT]` on the receiver.

**What changed and why.** v8 no longer accepts legacy TCP ingest. `[ONE-SENTENCE REASON]`. Logs sent this way are not accepted and not queued by the receiver.

```yaml
# Before
[LEGACY SENDER CONFIG]
```

```yaml
# After
[REPLACEMENT SENDER CONFIG, complete and pasteable]
```

**Fix.**

1. `[STEP]`
2. `[STEP]`
3. Restart the sender and confirm in the receiver: `[VERIFICATION COMMAND AND EXPECTED OUTPUT]`.

**Escape hatch.** There is none in v8. The legacy listener cannot be re-enabled. Staying on v7 is the only way to keep using it (section 2).

### Changed: `[RECEIVER CONFIG ITEM, IF ANY]` {#receiver-config}

`[Same six-part entry. Add one per additional breaking change: removed legacy listener config, ports, metrics names, health-check endpoints, dashboards or alerts that reference the legacy listener. If legacy TCP is the only break, delete this entry.]`

## 7. Upgrade the receiver to v8

Do this only when section 5 shows no remaining legacy senders.

1. Back up `[CONFIG AND DATA PATHS]`.
2. Install v8 from the offline bundle: `[COMMAND]`.
3. Remove legacy listener settings: `[SEARCH PATTERN AND ACTION]`.
4. Start v8 and confirm: `[VERIFICATION COMMAND AND EXPECTED OUTPUT]`.
5. Confirm every sender in your section 5 list is delivering. Compare event counts per sender for `[N]` hours against the same period before.

## 8. Roll back

If any sender is not delivering after the upgrade:

1. Stop v8: `[COMMAND]`.
2. Reinstall v7.`[X]` from the offline bundle: `[COMMAND]`.
3. Restore the section 7 backup: `[COMMAND]`.
4. Legacy senders resume. Logs sent while v8 was running are `[DESCRIBE EXACTLY WHAT IS LOST OR BUFFERED, VERIFIED BY TEST]`.

State here whether rollback is supported after v8 has migrated any on-disk data: `[YES/NO, with the data-format note]`. Verify this on a cold run before publishing.

## 9. Clean up afterwards

Delete these once v8 is stable:

- legacy listener port rules in firewalls
- the old sender config and any wrapper scripts
- dashboards and alerts that referenced the legacy listener
- `[ANY OTHER ARTEFACT]`

## 10. Troubleshooting by error text

| You see | Cause | Do |
|---|---|---|
| `[SENDER ERROR TEXT]` | Sender still uses legacy TCP against a v8 receiver | Section 6 |
| `[RECEIVER ERROR TEXT]` | Same | Section 6 |
| Sender is quiet, no error | Sender is buffering or dropping silently | `[HOW TO CHECK]`, then section 6 |
| `[OTHER]` | | |

**Support:** `[CHANNEL, NAMED OWNER, HOURS, RESPONSE TARGETS PER CONTRACT]`. Include your contract or account identifier and the output of `[DIAGNOSTIC COMMAND]`. This works offline: `[HOW TO PRODUCE AND TRANSFER A SUPPORT BUNDLE FROM AN AIR-GAPPED SITE]`.

---

## Before you publish: cold-run check

- Run the guide end to end on a real v7 deployment with someone who did not write it. Include one air-gapped-style install with no network.
- Fill in every bracket from that run, not from memory.
- Confirm that every entry has a search pattern and the literal error text.
- Measure the elapsed time and publish it, or publish none.
- Send the finished text to Legal with the section 0 questions answered.

I can tighten this once you supply the protocol names, the v7 plan and Legal's answers on the notice trigger.