I know nothing about Quarrow's real commands, config keys, defaults, error semantics or alert names, and I was told not to read `skill-wip/`. So these are nine drafts with the structure, ordering and reasoning filled in. Every product fact is a `{{CONFIRM: …}}` slot instead of an invented value. A fabricated default or flag in docs is worse than a gap, because people paste it.

**On "same template for each":** one literal template would break four of them. I used one shared skeleton, with sections dropped where they don't apply:

> **Title** → **Who this is for / outcome** → **Before you start** → **Steps** → **Verify** → **If it fails** → **Next**

| Guide | Real type | Deviation from the skeleton |
|---|---|---|
| a, c | Tutorial | None; they fit it best |
| b, i | Task how-to | None |
| d | Runbook | Adds Triage first, Escalate last |
| e | Reference | No Steps; a table instead |
| f | Troubleshooting | Cause-first, ordered by likelihood |
| g | Migration | Adds Breaking changes and Rollback |
| h | Decision | Not a how-to; a recommendation with a method |

---

## a) Get started with Quarrow

**Outcome:** about 10 minutes from zero to your first log line in the Quarrow UI. {{CONFIRM: real time}}

**Before you start**
- A machine with a log file to ship. {{CONFIRM: supported OS and arch}}
- Admin rights on that machine.
- An email address for sign-up. {{CONFIRM: SSO or other sign-up methods}}

**Steps**
1. **Create an account.** Go to {{signup URL}}, verify your email, and create your first workspace. {{CONFIRM: org/workspace naming}}
2. **Create an ingest token.** Go to {{UI path}} and copy the token. It is shown once. Store it as an environment variable, never in a repo.
3. **Install the agent.** Run {{install command per OS}}.
4. **Point it at a log file.** Add a minimal config with your token and one source path. {{CONFIRM: minimal config file and location}}
5. **Start the agent.** Run {{start/service command}}.
6. **Write a test line.** Run `echo "hello quarrow" >> {{path}}`.

**Verify:** Open {{UI path to live view}}. `hello quarrow` appears within {{CONFIRM: expected latency}} seconds. If it doesn't, run {{agent status/doctor command}}.

**If it fails**

| Symptom | Likely cause | Fix |
|---|---|---|
| Agent starts, nothing in UI | Wrong token or region | {{CONFIRM}} |
| Permission error on the file | Agent user can't read it | {{CONFIRM}} |
| Connection errors | Proxy or firewall | See guide (b) |

**Next:** Understand the ingestion pipeline (c). Forward to a SIEM (i).

---

## b) Install the Quarrow agent behind a corporate proxy

**Outcome:** The agent installs and ships logs through an HTTP(S) proxy.

**Before you start**
- Proxy host, port and auth type (none, basic, NTLM). {{CONFIRM: which the agent supports}}
- The Quarrow endpoints to allowlist: {{CONFIRM: hostnames, ports}}.
- Your proxy's CA certificate, if it does TLS inspection.

**Steps**
1. **Allowlist endpoints** on the proxy: {{list}}. Both the installer download host and the ingest host need access.
2. **Download the installer through the proxy.** Set {{proxy env vars}}, or download on another machine and copy it over.
3. **Configure the agent's proxy.** Set {{CONFIRM: config keys or env vars}}. Keep credentials out of the file, using {{secret mechanism}}.
4. **Trust the proxy CA** if it intercepts TLS: {{CONFIRM: CA bundle key}}. Never disable verification.
5. **Restart the agent.**

**Verify:** {{status command}} reports connected through the proxy, and a test line arrives (see (a)).

**If it fails**
- 407: proxy credentials are wrong or missing.
- Certificate errors: step 4 is missing or incomplete.
- Works from curl but not the agent: the service doesn't inherit your shell's env vars. Set them in the service definition.
- Timeouts: allowlist missing {{port}}.

---

## c) Understand the ingestion pipeline

**Outcome:** You build a three-stage pipeline and watch one raw line become a structured event. You learn that stages run in order, and that each stage sees the previous stage's output.

**Before you start:** Complete (a). {{CONFIRM: whether pipelines are edited in the UI, YAML, or API}}

**The sample line**
```
2026-10-30T09:14:02Z ERROR payment-api user=42 msg="card declined"
```

**Steps**
1. **Create an empty pipeline** named `tutorial` and attach it to your source.
2. **Add stage 1, parse.** {{CONFIRM: grok/regex/JSON stage}} extracts `timestamp`, `level`, `service`, and the rest as `message`. Send the line and inspect: four fields exist.
3. **Add stage 2, key-value.** Parse `user=42` out of `message`. Send the line again. Now `user` exists. This works only because stage 1 ran first.
4. **Add stage 3, filter or route.** Drop `level=DEBUG`. Send a DEBUG line and confirm it never arrives.
5. **Reorder.** Move stage 3 above stage 1 and resend. The filter finds no `level` field, so DEBUG lines get through. This is the lesson: order is semantics.

**Verify:** Use {{preview/test tool}} to see the event after each stage.

**Next:** Fix failed parses (see {{CONFIRM: dead-letter/parse-failure behaviour}}). Reference: all config keys (e).

---

## d) What to do when ingest pages at 3am (internal)

**For:** On-call SREs. **Goal:** Stop data loss first, find the cause second.

**Triage (5 minutes)**
1. Open {{dashboard link}}. Is it ingest lag, error rate, or a rejection spike?
2. Check {{status page / deploy log}}: did anything ship or fail in the last hour?
3. Classify by blast radius: all tenants, one region, or one tenant.

**Decision table**

| Signal | Likely cause | Action |
|---|---|---|
| Lag rising, queue depth rising, consumers healthy | Traffic surge | {{CONFIRM: scale step}} |
| Lag rising, consumers unhealthy | Consumer crash or bad deploy | {{rollback step}} |
| One tenant at 429/quota errors | Quota hit | Check (f); not an incident for us |
| Storage write errors | Backend degraded | {{CONFIRM: failover}} |
| Agents reconnecting in waves | LB or cert issue | {{CONFIRM}} |

**Rules**
- Mitigate before diagnosing. Roll back before debugging.
- Don't purge queues without {{CONFIRM: approval owner}}. Dropped data can't be recovered.
- Post in {{channel}} within 10 minutes, even if you know nothing.

**Escalate** to {{secondary}} if there's no improvement in 20 minutes or if more than one region is affected.

**After:** Open an incident doc, record timeline and the alert's usefulness, and tune the alert if it was noisy.

---

## e) Every agent config key

I can't write this one. A reference page is only worth anything if it's exact. Generate it from the agent's config schema or source, so it can't drift. Use this layout:

| Key | Type | Default | Required | Since | Description |
|---|---|---|---|---|---|
| {{key}} | {{type}} | {{default}} | {{y/n}} | {{version}} | {{one sentence}} |

Group by section (auth, sources, proxy, TLS, buffering, logging). Mark deprecated keys with their replacement. Show one full example file at the end. **Send me the schema or `--help` output and I'll fill this in.**

---

## f) Fix E_QUOTA_EXCEEDED

**You're here because** ingest rejected data with `E_QUOTA_EXCEEDED`.

**What it means:** {{CONFIRM: which quota: daily volume, rate limit, or retention}}. Data sent after the limit is {{CONFIRM: dropped, buffered, or rejected}}.

**Fix, in order of likelihood**
1. **Check usage.** {{UI path}} shows which quota and which source.
2. **Find the noisy source.** Look for a sudden volume jump: debug logging left on, or a log loop.
3. **Cut volume at the agent.** Add a drop/sample stage (see (c)).
4. **Raise the limit.** {{CONFIRM: plan, self-serve or sales}}.
5. **Wait for reset.** The quota resets at {{CONFIRM}}.

**Check your data:** {{CONFIRM: does the agent retry or buffer? For how long?}} State this plainly, because it's the first thing readers worry about.

**Still failing after raising it?** {{CONFIRM: propagation delay}}. Contact support with the workspace ID and the full error body.

---

## g) Upgrade from agent 2.x to 3.0

**Outcome:** Agent 3.0 running with a converted config and no log gap.

**Before you start**
- Back up the current config and note the 2.x version.
- Read the breaking changes below.
- Pick a canary host.

**Breaking changes** (largest blast radius first)
{{CONFIRM: list each as: what changed → how to detect it → before/after}}

```
# 2.x
{{old config}}
# 3.0
{{new config}}
```

**Steps**
1. **Convert the config.** {{CONFIRM: converter command, and whether it covers all keys}}. Review anything it flags manually.
2. **Dry-run.** {{validate command}}.
3. **Upgrade the canary.** {{command}}. Watch it for {{duration}}.
4. **Verify no gap or duplicates.** Compare line counts before and after in the UI. {{CONFIRM: does 3.0 resume from 2.x file offsets?}}
5. **Roll out** in batches.

**Rollback:** Reinstall 2.x and restore the backed-up config. {{CONFIRM: is the 3.0 state or offset format readable by 2.x?}}

---

## h) Should token rotation have an overlap window, and how long?

**Recommendation: yes.** Without overlap, rotation means every agent must switch at the same instant. That's impossible across a fleet, and the agents that miss it start losing data. Overlap makes rotation a rollout instead of an outage.

**Sizing the window**

`window ≥ slowest time for any agent to receive and apply the new token + safety margin`

Inputs:
- **Distribution time:** how long your config management takes to reach every host. {{CONFIRM: fleet data}}
- **Reload behaviour:** whether the agent hot-reloads the token or needs a restart. {{CONFIRM}}
- **Offline agents:** laptops, edge devices, or hosts down for maintenance. Decide whether to support them or require re-enrollment.
- **Margin:** at least 2× the observed worst case.

**Starting point:** 24 hours for server fleets, and 7 days if offline hosts count. Treat both as defaults to test, not findings. Measure your real rollout time first.

**Tradeoffs**
- A longer window leaves the old token live longer if it was leaked. For a compromise, rotate immediately with zero overlap and accept the gap.
- Cap the window, and revoke on expiry automatically. A manual revoke gets forgotten.
- Emit a metric for "requests still using the old token". Revoke when it hits zero, or at the cap.

**Needed from the platform team:** whether both tokens are valid server-side, the max token lifetime, and the number of offline agents.

---

## i) Forward logs to a SIEM over TLS

**Outcome:** Events flow from Quarrow to your SIEM over an encrypted, verified connection.

**Before you start**
- SIEM receiver host, port and protocol. {{CONFIRM: syslog-TLS, HTTPS/HEC, Kafka}}
- Server CA certificate. For mutual TLS, a client certificate and key as well.
- Network path from Quarrow (or the agent) to the SIEM. {{CONFIRM: which component forwards}}

**Steps**
1. **Create the destination.** {{UI path or config}}: host, port, protocol.
2. **Add certificates.** Upload the CA, and the client cert and key for mTLS. Set the minimum TLS version to {{CONFIRM: 1.2}}.
3. **Choose the format.** {{CONFIRM: JSON, CEF, syslog}}. Match what your SIEM parser expects.
4. **Select what to forward.** Use a route or filter, not "everything". It's cheaper and keeps noise out of the SIEM.
5. **Send a test event.** {{test button/command}}.

**Verify:** The event appears in the SIEM with the right timestamp, host and fields.

**If it fails**
- Handshake failure: CA missing, hostname mismatch, or expired cert.
- Connected but no data: format or index rejected by the SIEM.
- Intermittent drops: {{CONFIRM: buffering and retry behaviour}}.
- Never fix any of these by turning off verification.

---

## What I need to finish these

1. Config schema or `--help` output, which unlocks (e) completely.
2. Install, start and status commands, and the proxy and TLS keys, for (a), (b), (i).
3. What `E_QUOTA_EXCEEDED` actually gates, and the 2.x and 3.0 config samples, for (f) and (g).
4. Your alert names, dashboards and runbook channels, for (d).
5. Your fleet's rollout time and offline-agent count, for (h).

I can replace every `{{CONFIRM}}` once you give me those.