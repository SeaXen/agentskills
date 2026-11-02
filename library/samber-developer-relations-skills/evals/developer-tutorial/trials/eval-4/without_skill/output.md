# Plan: "Receive and Verify a Webhook" tutorial

**Quick date flag first:** my clock says today is 2026-09-19. You said launch is "the 19th, next Friday" — if that's actually today, the 6-hour budget below needs to run *now*, not this week. Confirm the real drop-dead date before you start the clock.

## Bottom line

One golden path, ship what a reader can run start-to-finish in 6 hours of writing time. Cut Docker Compose and the GitHub Actions workflow. Trim pytest to the tests that actually teach verification. Trim logging to one line. The "pipe in real production payloads from a sandbox" step can't ship as briefed — the sandbox doesn't exist. That's a blocker, not a scope note; get an answer on it before you write step 1.

## Why the scope gets cut this hard

Three constraints compound against each other:

| Constraint | Effect |
|---|---|
| One-off launch asset, not part of the docs set | No future editor will catch drift (dead Docker image tags, deprecated Actions syntax, broken CI badge). Anything that *can* rot, *will*, silently, forever. |
| Nobody owns the page after launch | Every extra moving part you ship is a moving part nobody will ever fix. Minimize moving parts, not maximize feature coverage. |
| 6 hours of writing time | Docker Compose + CI workflow + pytest/coverage + logging config + sandbox integration is a 2-3 day docs project, not a 6-hour one. Something gives regardless of what you decide. |

Given that, the deciding question for every eng-lead ask isn't "is this good practice" — it's "does this teach receive-and-verify, or does it teach something else wrapped around receive-and-verify." Cut the second category.

## The blocker: sandbox doesn't exist

Can't have a learner pipe in "their own production webhook payloads" from infrastructure that isn't built. Three options, pick one today:

- **A — Bundled fixture payloads (recommended).** Ship 3 static payloads in the tutorial repo: one validly signed, two tampered (bad signature, stale timestamp). Zero new infra, zero dependency on anyone else's unfinished work, fully within your 6 hours.
- **B — Generic public capture tool.** Point the learner at webhook.site or smee.io to receive a payload from their *own* test send (not production traffic — nothing routes real prod events there). Works, but puts a third-party tool's UI in your tutorial, and it's not "production payloads" — don't let the eng lead read it that way.
- **C — Wait for the real sandbox.** Incompatible with the deadline. Reject.

Recommend A. Send this upstream now, phrased as a decision request, not a status update: *"The sandbox isn't built, so 'pipe in your own production payloads' can't ship Friday. I'm using bundled sample payloads (valid + 2 tampered) instead — say now if that's wrong."*

## Scope decisions — send these to the eng lead today, as a single yes/no list

| Ask | Verdict | Why |
|---|---|---|
| Docker Compose | **Cut** | Reader already has a working local server from the quickstart. A compose file nobody maintains is a support ticket generator, not a teaching aid. If leadership insists on "prod-like," a one-line `next steps` pointer to a maintained infra doc is safer than an unowned compose file here. |
| GitHub Actions workflow | **Cut** | CI belongs to a repo you keep. A workflow YAML teaches repo hygiene, not signature verification — wrong lesson for the title. An unowned `.github/workflows/*.yml` copy-paste is also the single fastest thing in this list to go stale (action versions deprecate on their own schedule). |
| pytest + coverage | **Trim, keep the tests, drop the gate** | 4 focused tests (valid signature, tampered body, missing header, expired timestamp) directly reinforce "verify a webhook" — this is the one ask that's actually on-topic. Coverage threshold/badge is ceremony with nothing behind it once nobody owns the page; drop it. |
| Structured logging | **Trim to one line** | One structured log line at the accept/reject decision (`event="webhook_rejected" reason="bad_signature"`) is real, useful, and cheap. A logging config module is a second tutorial. |
| Sandbox payload piping | **Blocked — see above** | Can't teach a step against infrastructure that isn't built. |

## Time budget (6h)

| Block | Time | Output |
|---|---|---|
| Lock outline + get blocker answer | 0:00–0:30 | Confirmed scope, no more re-litigating mid-write |
| Step 1: receive raw body | 0:30–1:00 | Endpoint that captures raw bytes *before* any JSON parsing (call out explicitly — this is the #1 way people break verification) |
| Step 2: verify signature | 1:00–2:00 | Core section, gets the most time — SDK verify call, secret from env var |
| Checkpoint: send a signed fixture, see it verify | 2:00–2:30 | The "it works" moment |
| Step 3: reject invalid/tampered, log rejection | 2:30–3:15 | 400 response + the one structured log line |
| pytest section (4 cases) | 3:15–4:15 | Tests actually run, not just pasted |
| Troubleshooting | 4:15–4:45 | Mined from whatever broke while you wrote steps 1–3 (it always does — use it) |
| Title/meta/prereqs/"what you built"/complete code recap | 4:45–5:15 | Wraps the tutorial template |
| Self-edit pass, re-run every code block fresh | 5:15–5:45 | Nothing copy-pasted that doesn't actually run |
| Buffer | 5:45–6:00 | Slack for whatever step 2 or the pytest section overran |

First thing to cut if you're behind at hour 4: timestamp-tolerance/idempotency nuance in Step 3 — good practice, but outside "receive and verify" as scoped.

## Outline

```
# Receive and Verify a Webhook

| Time | Level | Prerequisites |
|---|---|---|
| 25–30 min | Intermediate | Completed the Brightwake quickstart |

## What You'll Build
An endpoint that receives a Brightwake webhook, verifies its signature,
and correctly accepts or rejects it.

## Prerequisites
- Brightwake SDK installed (from the quickstart)
- Your webhook signing secret (Dashboard → Webhooks)
- A way to receive local HTTP requests (reuse quickstart's server)

## Step 1: Receive the raw request body
  - Gotcha callout: don't let a JSON body-parser run before verification —
    signature check needs the exact raw bytes.

## Step 2: Verify the signature
  - SDK verify() call, secret from env var
  - Checkpoint: send the bundled valid fixture payload → see "verified"

## Step 3: Reject invalid payloads
  - Tampered/missing-header/expired cases → 400
  - One structured log line at the decision point

## Automated tests
  - pytest: valid signature / tampered body / missing header / expired timestamp
  - Run them, show real output

## Troubleshooting
  - Body parser consumed the raw body before verification
  - Wrong/missing secret env var
  - Clock skew on timestamp tolerance
  - Testing against the wrong (quickstart demo) endpoint

## What You Built / Complete Code

## Next Steps
- SDK reference docs
- (no "build on this" links — leadership called this a one-off)
```

## Open questions to close before hour 0:30

1. Sandbox blocker — option A/B/C above, need eng lead's pick.
2. Confirm Docker/CI cuts with eng lead, or get a scoped-down version they'll accept (e.g., a single `docker run` line instead of Compose, no CI at all).
3. Real deadline — today or actually next Friday (see date flag at top).

## Risk if shipped as originally briefed

Full eng-lead wishlist in 6 hours means every piece is under-tested — the likely failure mode isn't "doesn't ship," it's "ships with a Docker Compose file or CI workflow nobody verified end-to-end, on a page nobody will ever fix, that a backend dev copy-pastes on day one and hits a wall." For a one-off asset with no owner, a smaller tutorial that fully works beats a comprehensive one that half-works.