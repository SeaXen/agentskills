# Grebe Launch Demo — Live Migration-Agent Playbook

*(Repo has no product context for "Grebe" — this is a from-scratch plan built on the brief: live, unscripted, audience-supplied schema, 20 min, 4 weeks out, full eng team.)*

## The core design call

"Not cherry-picked" and "safe to run on stage" are not in tension — the tension only appears if you treat "safe" as "limit which schemas we accept." Don't. Accept *anything*. Instead, isolate the blast radius so it doesn't matter what arrives. That's the one judgment call this plan is built around, stated up front because it changes the architecture:

**Never let Grebe open a live connection to a stranger's real running database, on stage, in front of a camera.** Not because Grebe might fail — because *credential handling for an unknown third-party production system, live, with no time to verify anything,* is a bad idea independent of how good the product is. One leaked connection string, one audience member handing over a database that turns out to still have customer PII, one accidental write to something that wasn't actually a throwaway copy — any of those is a worse story than "the demo had a hiccup." The fix costs you nothing in authenticity:

**Grebe always operates against a fresh, isolated, ephemeral instance loaded from whatever the audience hands over — a schema dump / DDL export, not a live connection.** The audience still fully controls what it contains. Grebe still sees it for the first time, live, unrehearsed. You lose nothing on the "not cherry-picked" claim and remove the one failure mode that isn't a demo failure but an incident.

State this rule on stage, explicitly, before you start: *"We're not going to ask anyone to paste production credentials into a laptop on a stage — that'd be reckless regardless of what Grebe can do. Hand us a schema dump, we spin up a throwaway copy of it right here, Grebe never sees anything else."* That line does double duty: it's the safety boundary, and it's also a credibility signal that plays *in your favor* against the cherry-picked accusation — it says "we thought about how someone could fake this, and closed that door too."

## Intake protocol — "whatever schema someone in the room hands it"

- **Pre-event kiosk, open during the mixer before the talk:** attendees upload a schema dump (`pg_dump --schema-only`, Rails `schema.rb`, Django migrations state, whatever) via a QR-linked form. This doesn't break liveness — the *selection* still happens on stage.
- **On stage:** pull one submission at random (or literally invite the submitter up), display the raw file on the big screen unedited, timestamp visible, so the room sees it wasn't touched beforehand.
- **Backstage, invisible to the audience:** an automated pipeline validates the upload before it reaches Grebe — reject non-SQL binaries, cap file size, strip anything that looks like a zip bomb or embedded payload, reject in <2s with a friendly on-screen message rather than hanging. This is intake hardening, not schema curation — it never touches *which* schemas are eligible, only guards against a malformed file breaking the pipeline in a way that has nothing to do with Grebe's actual capability.
- **Fallback intake, purist version, higher risk:** literal live USB upload on stage instead of a pre-event kiosk. Recommend against it *only* for the last-mile plumbing (file I/O flakiness live is a dumb way to lose your slot) — Grebe's first look at the content is identical either way.

## What Grebe runs inside

- **One ephemeral, network-isolated sandbox per run** (microVM or throwaway container), provisioned in seconds, torn down automatically on a hard timer regardless of outcome.
- **No egress.** Grebe cannot reach anything outside its sandbox — removes an entire class of "what if the audience schema contains something adversarial aimed at the agent" risk.
- **Resource caps** (CPU, memory, execution time) enforced at the container level, not the application level — an infinite loop in a generated migration should get killed by the platform, not trusted to self-terminate.
- **Two-step execution, always, shown on screen:** Grebe writes the migration → displays the diff/plan → then applies it. Don't collapse this into one invisible step even though you could — watching it "write" and then "run" as two distinct, readable moments is *more* convincing than a black box, and it gives you a natural pause point if something looks wrong before it's too late to stop.
- **Visible kill switch**, held by an engineer standing just off stage, cuts execution immediately. Rehearse using it. If it's only ever a hidden safety net, the first time it fires live will look like a disaster; if you've shown it once in rehearsal-footage-style prep material or even acknowledge its existence on stage, invoking it reads as "the safety systems worked," not "it broke."

## 20-minute stage runsheet (draft)

| Min | Beat |
|---|---|
| 0–2 | Frame the ask: "people said our demos were cherry-picked — so tonight we're not choosing the schema, you are." State the safety rule (dump, not live creds) as a deliberate choice, not an apology. |
| 2–4 | Pull a submission (or bring up a volunteer), show the raw file unedited. |
| 4–5 | Sandbox spins up on screen (real provisioning log, not a spinner) — this is dead time, fill it talking about what's happening, not stalling. |
| 5–10 | Grebe analyzes schema, writes migration, diff appears on screen. Narrate what it's doing, don't just watch silently. |
| 10–11 | Pause beat: "here's the plan it wrote — let's run it." Deliberate, not rushed — this is your last human checkpoint before commit. |
| 11–14 | Execute. Show real output, not a mocked progress bar. |
| 14–17 | Verify: query the migrated schema live, show the result matches intent. This is the moment that actually kills the cherry-picked accusation — verification, not just "it ran." |
| 17–20 | Second one if time allows (harder/weirder submission), or Q&A / close. |

Build in a **decision point at minute 10** — if the plan Grebe produced looks wrong, that's a legitimate on-stage moment ("it flagged this itself, here's why"), not a failure to hide. Rehearse narrating a bad plan as convincingly as a good one.

## Failure modes — pre-built responses, not improvisation

| Failure | Response |
|---|---|
| Grebe can't safely handle a construct (exotic partitioning, vendor-specific extension) | Rehearsed: Grebe says so explicitly and declines rather than guessing — narrate this as *correct* behavior, not a limitation. Have one such schema in your rehearsal corpus so this isn't the first time you're narrating it. |
| Execution times out | Kill switch fires, sandbox log shown, move to second pre-staged submission. |
| Sandbox provisioning fails (infra hiccup, not Grebe) | Have a second sandbox pool warmed and ready; failover is invisible if pre-built. |
| Verification shows a wrong result | Say so on stage. This is the single highest-credibility recovery available to you — "it got this one wrong, here's what happened" is a stronger four-week-later story than a suspiciously perfect run. Don't script around this; build the narration for it. |
| Wifi/AV dies | Local-only fallback path: everything (sandbox, Grebe, DB) runs on hardware physically in the room, zero dependency on venue network. Non-negotiable — decide this in week 1, not week 4. |

## 4-week plan, full team, parallel workstreams

- **Week 1** — Harden sandbox isolation (no-egress, resource caps, warm pool, local-hardware fallback). Build the kill switch. Start assembling an adversarial schema corpus: real dumps from Rails/Django/Laravel/WordPress/Salesforce exports, plus hand-built pathological ones (circular FKs, huge enum sets, custom extensions, multi-schema, mixed casing/encoding).
- **Week 2** — Batch-run Grebe against the full corpus (hundreds of runs, unattended). Build a failure taxonomy from the results. Fix the top failure classes. Explicitly build and test the "I can't safely do this" decline path — this needs to be a first-class behavior, not an unhandled exception with a stack trace on screen.
- **Week 3** — Full dress rehearsals on the actual stage hardware, actual network conditions, actual room noise. Recruit 3–5 people *outside* the eng team to submit schemas blind — nobody who built Grebe should know what's coming in the final rehearsals, or you've quietly recreated the cherry-picking problem internally. Rehearse the kill-switch and the "verification shows a wrong result" narration explicitly, at least once each, on purpose.
- **Week 4** — Feature freeze except fixes to bugs found in week-3 rehearsals. Final dress rehearsals. Prepare a recorded fallback segment as an *explicit, named last resort* (venue-wide power/network failure class of event only) — brief the speaker on the exact criteria for invoking it so it's a decision, not a panic call mid-talk.

## Go/no-go, morning of

- Local-hardware fallback path tested end-to-end in the actual venue, not just at the office.
- Kill switch tested in the actual venue.
- Corpus pass rate and decline-rate reviewed one last time — a rising decline rate late in week 4 is a signal to simplify the ask (e.g. cap schema size) before stage, not to push through.
- Speaker has personally run the demo, live, at least 10 times against schemas they haven't seen before.

## After the talk

The live moment convinces the room. It doesn't convince the internet, which is the actual audience for "not cherry-picked" a year from now. **Publish the full unedited recording, the sandbox execution logs, and stand up a public sandbox link letting anyone replay Grebe against the same schema afterward.** That's what actually closes the credibility gap the last round of demos opened — the stage moment is the trailer, the reproducible public artifact is the receipt.