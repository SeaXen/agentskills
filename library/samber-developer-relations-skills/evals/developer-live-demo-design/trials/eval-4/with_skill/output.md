# Kelvinsort demo runbook — partner summit (10M-record dedup claim)

## First — the two asks I'm not building, and why

Both are named explicitly, almost word-for-word, in this skill's own risk register as the line between hardening and faking:

| What you asked for | What the skill calls it |
|---|---|
| Timer-driven progress bar that always lands at 28s | *"A 'rows migrated' counter that increments on a timer"* — listed under **Faked; never ship** |
| Filter the weird record class out of the verification count | *"A verification query with the failure case filtered out of the WHERE clause"* — listed under **Faked; never ship** |

The test the skill gives: *if a buyer asked "is that real?", could you say yes and prove it on the spot?* Neither survives that. And this is a room of 60 **buyers** for a **data-quality product** — the exact audience most likely to ask a follow-up like "can I feed it our export" or "what happens with malformed rows," during the demo or in the POC that follows it. A stubbed counter fails the moment anyone times it against a phone. A filtered verification query fails the moment anyone asks for the raw count or runs it on their own sample during the trial you're trying to close. For a dedup tool specifically, getting caught hiding a class of records that doesn't dedupe correctly isn't a demo foul — it's evidence the product doesn't do the one thing it's sold to do, which is worse than a slow demo.

Per the skill: *"When a demo can only clear its claim by faking, the claim is wrong — narrow it."* You don't need to narrow it, though — you need to move the speed proof off your laptop and stop treating the correctness gap as a UI problem. Below is the real version.

## What's actually going on (two different problems, don't merge them)

1. **Speed**: your laptop is slow, not the product. A recorded run on real, representative hardware settles this without lying to anyone.
2. **Correctness**: some record class doesn't verify cleanly. That's a product bug, not a demo problem, and hiding it from the count doesn't fix it — it just moves the discovery to a worse moment (a buyer's POC, after the deal is supposedly progressing).

The 80%-stall bug sits between the two: until you know its cause, you don't actually know it's *only* cosmetic. Treat it as a real defect until proven otherwise.

---

## Header

```
Demo:          Kelvinsort 10M-record dedupe
Claim:         "Kelvinsort dedupes a real 10M-record contact list to
               production-quality accuracy in under 30 seconds."
Venue/format:  Partner summit stage, ~60 buyers, mixed technical depth
Budget:        ASSUMED 3-5 min inside a longer pitch — confirm your slot
Tier:          3 (recorded screencast, narrated live)  Fallback tier: 4
Network:       Offline — nothing in this demo needs the venue network
Data:          Synthetic 10M-row contact fixture, realistic shape/volume,
               zero real PII. Never run this on an actual customer export
               on that stage.
Buddy:         ASSUMED available — confirm; hold a clone of the recording,
               deck, and a laptop with the live-subset fallback (segment 4)
Owner:         ASSUMED presenter — confirm who maintains this after the event
Last verified: NOT YET — no clean run exists until the two defects below
               are closed and a real recording is made
Re-verify:     Before the event, and again if the dedup engine changes
```

**Why tier 3, not tier 2 or 1.** You're inside two weeks — this skill's own rule is that a date that close "rules out building a local stack from scratch and promotes the recorded tier." Your claim is a scale-and-speed claim ("this takes 30 seconds"), which the ladder says is fully proved at tier 3 — you don't need live re-execution to prove a number, you need an honest recording of a real run. Tier 2 (live, fully local, on hardware fast enough to hit 30s) is the upgrade path *if* you can get qualifying hardware into rehearsal this week — see segment 4 below for a cheap way to get tier-1/2 credibility without betting the whole claim on live execution.

**Open question that changes everything downstream: has Kelvinsort ever actually hit <30s on real hardware, on the full 10M rows, with the record-class bug fixed?** If yes, you're hardening a true claim. If no — if 30s is a target nobody has actually measured — then the claim itself is the thing that's wrong, and the fix is renaming it ("under 30 seconds on a 32-core instance," or "under 5 minutes on commodity hardware"), not a faster-looking demo. Confirm this before doing anything else below.

---

## Segments

| # | Proves | Enter from | Runs | Budget | Droppable | Fallback |
|---|---|---|---|---|---|---|
| 1 | This is a real 10M-row messy list, not a toy | fixture file, row-count command | live, `wc -l` / row-count on the fixture | 15s | no | screenshot of the count |
| 2 | It dedupes 10M records in under 30s | recording `01-fullrun.mp4` | plays the recording, real elapsed-time overlay from the actual run | 35s | no | same recording, always — this segment is *never* live given the 1-in-5 stall |
| 3 | The result is actually correct, including edge cases | live verification query against the completed run's output | live query, full count, no filter | 30s | **no** — see below | screenshot of the same query's output, timestamped |
| 4 (optional, upgrade) | It's not a trick — here's it running again, live, at smaller scale | seeded 500k-row tenant | live execution | 45s | yes | skip straight to Q&A |

Segment 3 is marked **not droppable** deliberately, against the instinct to cut the awkward one when the clock slips. For a data-quality product, "does it actually work" is closer to the claim than "is it fast." Dropping the speed segment under time pressure costs you a number; dropping the correctness segment costs you the argument for buying the product at all.

**Segment 4 is the highest-leverage two weeks of engineering you can spend here.** It doesn't need to hit 30 seconds — it needs to be small enough to run live and fast enough not to be boring, so that when someone asks "is that real," you switch from the recording to a live terminal and just run it again in front of them. That's the difference between "trust me" and "watch me." It's the honest version of what a timer-driven bar was trying to fake.

---

## The two engineering blockers — put these on the runbook, with owners and dates

This section exists because the runbook template says an empty field is an untested assumption, and right now these are the two biggest untested assumptions in the whole demo.

**Blocker A — the 80%-stall bug (~1 in 5 runs).** Don't design the demo around hiding it; root-cause it before the event, because it's the kind of thing that also hits actual customers.
- Cheapest checks first: is it GC-pause shaped (spikes in a specific generation), I/O-wait shaped (disk or a lock on the fixture file), thread-pool exhaustion at a specific stage boundary (80% is suspiciously specific — check what phase the pipeline enters right around there, e.g., a shuffle/merge/final-hash-resolution step), or a blocking call to something off-box (license check, telemetry, an update check)?
- Instrument it with real timestamps per pipeline stage across ~20 runs; a stall that always lands near the same *stage* rather than the same *wall-clock time* tells you it's structural, not random.
- Until it's fixed: never run the full 10M job live. Record several takes, keep the two cleanest as `01-fullrun.mp4` and `01-fullrun-backup.mp4`, and track this as an open defect with a real target date — not a demo workaround.

**Blocker B — the excluded record class.** Find out which of these it is before deciding anything about the demo:
- **It's a real correctness bug** (that class of record isn't deduped right) → fix it, or if two weeks isn't enough, say so on stage: *"today Kelvinsort handles exact and fuzzy matches across N record types; [class] is on the roadmap for [date]"* — a scoped, honest claim beats a clean number that doesn't survive inspection.
- **It's a legitimate exclusion** (e.g., that class is intentionally treated as non-duplicate) → then it belongs *in* the verification output, not filtered from it: *"9,998,200 duplicates removed; 1,800 records flagged ambiguous, held for review"* is a more credible number to a data buyer than a suspiciously round one, because it shows the tool knows what it doesn't know.

Either branch is compatible with hitting the stage on time. Silently filtering it is the only branch that isn't, because it's the only one that doesn't survive a follow-up question.

---

## Fallback assets

```
01-fullrun.mp4          full 10M-row run, recorded on [hardware TBD],
                        real elapsed-time overlay, embedded in the deck
01-fullrun-backup.mp4   second clean take, same hardware, same day
02-verification.png     screenshot of the unfiltered verification query,
                        timestamped, matching the recorded run
deck.pdf                includes all key frames, on a USB key + buddy's laptop
```

Record both `.mp4`s from the *same* qualifying hardware, same fixture, same day as the verification screenshot — a recording and a verification output from two different runs is its own small credibility gap if anyone lines up the numbers.

## Reset and pre-provisioning

```
Reset (one command):   ./demo reset      — ASSUMED name, confirm actual command
Verified cold:         NOT YET — pending Blocker A fix
Pre-provisioned:       fixture loaded, recordings embedded in deck, verification
                       query pre-typed in a script file (paste, don't retype)
Never on stage:        the full 10M run, until 3 consecutive clean cold runs
                       exist without the stall
```

## Recovery lines

- Segment 2 is a recording by design, so there's nothing to "recover" from — the line to have ready is the honest framing, said once, up front: *"This next part is a recording — ten million rows takes long enough that watching it live would cost us the room. Run this morning on [hardware], nothing sped up."*
- If segment 3's live query hangs or errors: *"That's a new one, and I'm not going to debug it at you — here's the same query's output from this morning,"* then show `02-verification.png`.
- If segment 4 (live subset) fails: *"I'll skip the live re-run — happy to do it one-on-one after this if you want to watch it yourself."* Then continue; segment 4 is droppable, segments 1-3 are not.

## Pre-flight checklist

```
[ ] Machine plugged in, sleep and screensaver off
[ ] Do Not Disturb on; chat, mail, calendar quit
[ ] Fresh demo profile — no daily-driver accounts, no real contact data anywhere
    on this machine (this is a contact-list product; treat PII rules as live here)
[ ] Terminal 24pt+, high-contrast theme, block cursor
[ ] Recording plays full-screen inside the deck, tested at venue resolution
[ ] Segment 4 fixture (500k rows) pre-seeded, reset command run once, cold-tested
[ ] Verification query script ready to paste, not retype
[ ] deck.pdf + both .mp4s on a USB key and with the buddy
[ ] No customer name, real contact data, or production credential on this machine
[ ] Recovery lines rehearsed out loud, including the "this is a recording" line
```

## Rehearsal log — target for the next two weeks

| Date | Run type | Result | Change made |
|---|---|---|---|
| Week 1 | Instrument + reproduce Blocker A across 20 runs | — | identify stage where stall occurs |
| Week 1 | Classify Blocker B (bug vs. legitimate exclusion) | — | decide claim wording or fix |
| Week 1-2 | Fix or scope both blockers | — | — |
| Week 2 | Record `01-fullrun.mp4` + `02-verification.png`, same session | — | confirm they match |
| Week 2 | 3 consecutive clean cold runs of segment 4 (live subset) | — | — |
| Week 2 | Full dry run at venue-equivalent resolution, timed | — | — |

Pass threshold before this is stage-ready: the recording and the verification screenshot come from the same real run on disclosed hardware, segment 4 has three clean cold runs behind it, and Blocker B is either fixed or explicitly scoped in the claim — not filtered out of it.

---

**What I need from you to close the remaining gaps**: the actual slot length, whether a buddy is realistic, whether you have (or can rent) hardware that's actually hit <30s, and which of the two Blocker-B branches is true. The rest of this runbook holds regardless of those answers — those four just tune the numbers.