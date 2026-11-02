Applying the `developer-quickstart-guide` skill to Ferrous. This is a rewrite request ("nobody finishes it" pattern), so defects lead, then the rewritten page — per the skill, I never rewrite from description alone, so section 5 below is the real cold-run plan someone on your team needs to execute; everything else here is built from the two hard facts you gave me (4 min on your laptop, 2–4 weeks in the field, "stuck at step 1" is the #1 ticket).

---

## 1. Success moment + time budget

**Success moment:** a `POST` to Ferrous's mask endpoint, against a container the reader just started, returns the sample record with its sensitive fields masked. (Not the health check — that only proves the process is alive, not that the product works.)

**Time budget — two separate commitments, not one:**
- **Hands-on-keyboard path:** 5 minutes, measured from the moment the reader already has a pulled image and a valid license key. This matches your own 4-minute run with a small margin for someone who isn't you.
- **Access path:** tracked separately, not folded into the page's time claim. Target: cut the typical 2–4 weeks to ≤3 business days. This number belongs to Product/Sales/Security, not to the docs page — a page cannot promise an access grant it doesn't control.

The gap between "4 minutes" and "2–4 weeks" is a 1000x difference. No amount of copy-editing produces that. That ratio is the tell that the page's actual defect is upstream of step 1, not inside it.

## 2. Defect table (ranked by time lost)

| # | Step | What the page currently assumes | What it costs a bank/insurer reader |
|---|---|---|---|
| 1 | Before step 1 (missing entirely) | Reader already has registry credentials, an active license key, and network egress to pull the image — because that's true on your laptop | This is where almost all 2–4 weeks goes. Nothing on the page tells the reader what to request, from whom, or that they should start the request *before* trying step 1. They discover the requirement by failing, then file a ticket, which gets routed serially through security → network → licensing instead of started in parallel on day one. |
| 2 | Step 1: `docker pull` | A generic `docker pull` will just work | This is your literal "stuck at step 1" ticket. It fails for at least three distinct reasons — no registry auth, no egress, TLS-intercepting proxy — and the page can't tell the reader which one they hit, so every one of them becomes the same undifferentiated support ticket instead of a self-fixable error. |
| 3 | Step 1, no offline variant | The reader's network has (or can get) internet egress to a public/vendor registry | Many bank and insurer networks have zero external registry egress by policy, permanently, not as a bug to route around. "Just open a firewall rule" is a request nobody on their side can grant. Every reader in this situation burns a full ticket round-trip discovering that the online path is a dead end for them specifically. |
| 4 | Prereqs (missing) | Docker is the approved container runtime, and current CPU/RAM/license-file placement are self-evident | Some shops mandate Podman or an internally scanned registry only. Discovered after the image has already cleared their security scan — another redo cycle. |
| 5 | Steps 2–4 (run, health curl, mask sample) | — | Unconfirmed but *not* implicated by your evidence — this is the half of the page that already reproduces your 4-minute run. Don't touch it blind; confirm with a real cold run (§5) before spending effort here. |

Defect #1 is the one to fix first. It's worth more than the rest combined.

## 3. The rewritten page

```markdown
# Mask your first record with Ferrous in 5 minutes

You'll start a Ferrous container locally and send it one record — a
name, an SSN, an email — and see it come back masked.

This page assumes you already have a Ferrous image and a license key
in hand. If you don't yet, start with the box below **today**, in
parallel with everything else your rollout needs — it typically takes
the longest step in the whole process.

## Get access first (do this before anything else)

Ferrous ships as a container image behind a license key. Getting both
is a request to your Ferrous account team, not something this page can
hand you directly. Send this, verbatim, as early as possible:

> Requesting a Ferrous evaluation: registry pull credentials (or an
> offline image bundle, if our network has no external registry
> egress — see below), plus a trial license key.
> Account/organization: <YOUR_ORG_NAME>
> Contact: <YOUR_EMAIL>

- **Registry egress:** if your network allows outbound HTTPS to
  `registry.ferrous.example` (confirm with your network team — most
  bank/insurer networks do not, by policy, and that's expected, not a
  problem), use the online path in step 1.
- **No registry egress:** ask your Ferrous contact for the **offline
  bundle** instead — a signed `.tar.gz` you transfer over your
  organization's normal approved file-transfer channel. Use step 1b.
- **License key:** arrives by email once the trial is approved. It's a
  single string starting with `flk_`.

Not sure which applies to you? Run this before requesting anything —
it tells you in five seconds which path to ask for:

    curl -sI --max-time 5 https://registry.ferrous.example/v2/

Reply, no error → ask for registry credentials.
Timeout or connection error → ask for the offline bundle instead; this
is normal on a locked-down network, not something to troubleshoot.

## Before you start

- Docker 24 or later (or Podman 4+, substitute `podman` for `docker`
  below): check with `docker --version`
- 2 CPUs, 4 GB RAM free
- A Ferrous license key (`flk_...`) from the step above
- Either registry credentials or the offline bundle from the step above

## 1. Get the image

**If you have registry access:**

    docker pull ferrous/engine:2.4

**1b. If you received the offline bundle instead:**

    docker load -i ferrous-engine-2.4.tar.gz

You should see:

    Loaded image: ferrous/engine:2.4

`unauthorized: authentication required`? Your registry credentials
haven't activated yet — reply to your access request with the error
text; don't retry blindly.

`dial tcp ... i/o timeout` or `connection refused`? Your network has
no egress to the registry, which is common and not a bug. Switch to
1b and request the offline bundle if you haven't already.

`x509: certificate signed by unknown authority`? Your network's proxy
is inspecting TLS. Use the offline bundle (1b) instead of trying to
work around the proxy.

## 2. Run Ferrous

    docker run -d --name ferrous -p 8443:8443 \
      -e FERROUS_LICENSE_KEY=<YOUR_LICENSE_KEY> \
      ferrous/engine:2.4

You should see a container ID printed, then:

    docker ps --filter name=ferrous

    CONTAINER ID   IMAGE                 STATUS
    a1b2c3d4e5f6   ferrous/engine:2.4    Up 5 seconds

Exits immediately instead? Run `docker logs ferrous` — the most common
cause at this step is a license key that was copied with a trailing
space or newline.

## 3. Confirm it's healthy

    curl -sk https://localhost:8443/healthz

You should see:

    {"status":"ok"}

Connection refused? Give it 10 more seconds — first boot loads the
masking ruleset — then retry.

## 4. Mask a sample record

    curl -sk -X POST https://localhost:8443/v1/mask \
      -H "Content-Type: application/json" \
      -d '{"fields":{"ssn":"123-45-6789","email":"jane.doe@example.com"}}'

You should see:

    {"fields":{"ssn":"***-**-6789","email":"j***@example.com"}}

## What just happened

Ferrous applied its default masking ruleset to the record you sent,
in place, with no data leaving your machine. Everything after this is
configuring which fields get masked and how.

## Next steps

- [Configure masking rules for your own schema](…)
- [API reference](…)
- [Talk to your account team about production deployment](…)
```

## 4. Cut list

- Masking-algorithm/architecture explanation → moved to concept docs; the reader sees the product work before reading why.
- Full field-type/rule config matrix → moved to reference docs, linked from Next steps.
- Production hardening (TLS certs, HA, log retention, audit settings) → moved to a separate "Deploying Ferrous to production" guide, explicitly out of scope here. A quickstart proves the product works, not that it's production-ready.
- License-tier/contract detail → moved to a short "Getting your license" page the access box links to, not inlined.

## 5. Verification plan (someone on your team runs this — I can't)

1. Clean-environment cold run on a normal unrestricted VM, timing from page load, both reader profiles (someone who knows Docker, someone who doesn't).
2. A second cold run on a network shaped like your actual customers': proxy with TLS interception, no registry egress, no pre-cached image. This is the run that actually tests the fix — the first one just re-confirms what you already know works.
3. Log every defect and every hesitation (friction log, green/yellow/red) in both runs.
4. Ship only when: every command in the restricted-network run succeeds via the offline path with no undocumented workaround, output matches, and the hands-on-keyboard portion lands at 5 minutes.
5. Owner: whoever on the Ferrous team already owns the container image and health/mask endpoints — they're the only one who can state real error text and confirm the offline-bundle process actually exists end to end today (this page currently assumes it does; verify before publishing).

## 6. Instrumentation

- **Step-level drop-off on the docs page**: page load, copy-click per step, success-event proxy (can't observe the customer's own container directly).
- **Support tickets tagged by step number** — you already know #1 dominates; keep tracking it post-fix to confirm the box in §3 actually kills it.
- **Access-request-to-grant cycle time**, tracked by whoever owns that process (Sales/Security), as its own funnel — this is the metric that actually explains the 2–4 weeks, and no docs change moves it without their process changing too.
- **Median time from "access granted" to first successful `/v1/mask` call** — this is the real, at-scale version of your 4-minute number, replacing anecdote with data.
- Skip day-7 return as written; for a sales-gated on-prem product the compounding-value equivalent is trial-to-paid conversion within the eval window, owned by CS, not docs.
- **Do not instrument the Ferrous binary or image itself** to phone home usage data. Your customers are banks and insurers evaluating a data-masking product specifically for compliance reasons; any telemetry from their running instance needs to be an explicit, contractually-disclosed opt-in, decided with Legal/Product — not something wired into a quickstart fix.

**The one thing worth escalating past docs:** the biggest lever isn't wording, it's the access mechanism itself. Right now Ferrous sits at "sales-gated sandbox" — the slowest rung on the access ladder. Moving eval requests to an immediate, self-serve trial key (even if the broader commercial deal stays sales-led) is the change most likely to turn "2-4 weeks" into "3 days," because most of that time is procurement/security routing, not anything a reader can fix by reading more carefully.