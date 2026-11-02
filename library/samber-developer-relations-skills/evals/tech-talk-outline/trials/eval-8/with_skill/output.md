Using **tech-talk-outline** (plus its four reference files: narrative arcs, the worked example, sources/defaults, and slide/demo craft) to turn this into a rehearsable structure.

I'm missing several interview answers (no abstract text, no demo requirement, no rehearsal ceiling, one-off vs. re-give unknown, no confirmed incident/migration story). Per the skill, I'm not blocking on those — I built the outline on what's confirmed and flagged every assumption inline so you can correct them fast.

**Assumptions made to build this (confirm or overrule):**
- No accepted abstract exists yet — treat this outline's arrow as the abstract's promise; write the CFP text from the arrow, not the other way around.
- Demo: assumed required, anchored under Pillar 3. Fidelity tier and rehearsal ceiling unconfirmed — see Rehearsal plan.
- Desired audience action: assumed "start treating sampling/budget as a per-service decision, try trace-diffing as a triage habit." Correct me if marketing wants something narrower (e.g., "book a demo").
- Raw material: assumed you have a real number for the "one noisy service starves the budget" story (customer or internal). If that number doesn't exist, Pillar 1's evidence needs a substitute before this is rehearsable.
- Recording status and re-give plan unknown — both would re-rank effort here (see references/sources-and-defaults.md's own caveat on this).

---

## The seven-features problem, dealt with first

Marketing's ask — all seven in the talk — is this skill's named anti-pattern: a feature tour has no tension and nothing to remember, and an SRE-heavy room clocks it as a pitch inside the first five minutes. The fix isn't to cut features, it's to stop treating them as the *structure* and use them as *evidence*:

- **Adaptive sampling + per-service budgets** → evidence under Pillar 1 (same problem, two knobs)
- **OTel-native ingest + query language** → evidence under Pillar 2 (same problem, two knobs)
- **Trace-diff view + anomaly alerts** → evidence under Pillar 3 (same problem, two knobs)
- **Terraform provider** → cut from the body. It doesn't sit under an SRE pain point — it's a provisioning concern, not a cost or triage concern, and forcing it in would need a fourth pillar, which the house default says reliably steals the buffer. Give it one line on the closing link slide and route the rest to a blog post or the booth. That's how marketing gets all seven mentioned without the talk becoming a catalog.

---

## Deliverable

```
Arrow            "Observability doesn't get expensive because you collect too
                 much — it gets expensive because you collect the same amount
                 from every service."

Arc              Problem → dead ends → insight → proof (arc 1).

                 Why this over the alternatives: Incident and Migration rank
                 higher on value when the speaker has a specific, cleared
                 story to tell — but you're DevRel, not the engineer who lived
                 an outage, and no migration story was confirmed. Arc 1 is the
                 one deliverable without further raw-material confirmation.
                 It also fits the room: ObservabilityDays SREs already believe
                 "observability is expensive and slow to debug" in general,
                 but not yet the specific claim that uniform config is the
                 root cause — so the dead ends still have work to do, which
                 rules out skipping straight to the insight (arcs 3/4).
                 Contrarian was rejected (no belief strong enough to attack
                 fairly in 30 min); progressive construction was rejected
                 (unconfirmed rehearsal ceiling, and it would eat the slide
                 budget three features need).

                 Ask your speaker gut-check: if a specific, customer-cleared
                 incident exists, Incident would outrank this — revisit if so.

Pillars          1. "Uniform collection is a tax you can't turn off"
                    Evidence: the per-service trace-volume graph (the noisy
                    service vs. the starved one) + adaptive sampling +
                    per-service budgets as the fix. Speaks to EMs (spend),
                    SREs (the data you need is the data that got dropped),
                    staff engineers (what breaks at scale: a flat sampling
                    rate on a cardinality-heavy service).
                    Term to define out loud: tail-based sampling.

                 2. "An incident isn't a data problem, it's a translation
                    problem"
                    Evidence: OTel-native ingest (nothing lossy at the
                    format seam) + the query language (one syntax across
                    traces/metrics/logs, shown as a before/after query).
                    Speaks to staff engineers (fewer adapters = fewer
                    silent failure modes) and SREs (one place to look, not
                    three tools mid-page).
                    Term to define out loud: semantic conventions.

                 3. "You don't read your way to root cause, you diff your
                    way there"
                    Evidence: trace-diff view (known-good trace vs. the
                    incident trace) + anomaly alerts (the system found the
                    deviation before a human went looking). This is where
                    the demo lives.
                    Speaks directly to the 60% SRE majority — this is their
                    3am pillar.
                    Term to define out loud: trace diffing (assume it's
                    unfamiliar even to this room).

Realization      End of Pillar 1, ~minute 9. The graph showing one noisy
                 service eating the shared trace budget while the service
                 actually paging that night got sampled into invisibility.
                 Hold the slide, say nothing for a beat. "We used to think a
                 sampling rate was a neutral cost control. Then we watched
                 the wrong service pay for it. Now we treat sampling as a
                 per-service spend decision." [Matthew Dicks' 5-Second
                 Moment — named method, not a measured effect.]

Time budget      Q&A is after the slot, so all 30 minutes are content —
                 no need to carve out room for questions inside it. Buffer
                 target is 10-15% of the slot (house default, not measured):
                 4 minutes here, absorbed inside the pillar estimates below
                 rather than shown as a dead block.

                 0:00-0:02  hook + stakes (the arrow, unexplained + the number)
                 0:02-0:04  promise + scope + affiliation disclosure
                 0:04-0:11  Pillar 1 (7m) — realization lands ~0:09
                 0:11-0:17  Pillar 2 (6m)
                 0:17-0:24  Pillar 3 + demo (7m)
                 0:24-0:26  arrow restated, same words as the hook
                 0:26-0:30  buffer slack / closing link slide stays up
                 [Q&A starts here, outside the 30]

                 Get the speaker's real words-per-minute before trusting
                 these minute counts: 200 words read aloud, timed, divided.
                 Table values are not a substitute.

Slide skeleton
  #   Slide must accomplish                              Notes
  --  --------------------------------------------------  --------------------------------
  1   Title + handle, small "DevRel, Corvid" credit
  2   The arrow, stated, unexplained                      The hook [NEVER CUT]
  3   The one number: noisy-service trace volume vs.
      the incident it starved
  4   What you'll leave able to decide                    The promise
  5   Scope + disclosure                                  "I work at Corvid — here's
                                                            where we're the wrong choice:
                                                            [fill in honestly]." Not for
                                                            teams under N services / not
                                                            yet on OTel. Repo link starts
                                                            here (repeats at #24).
  6   Section marker: collection is a tax
  7   Dead end — flat-rate sampling, the naive config
  8   Dead end — "just buy more retention," cost curve
      doesn't bend
  9   The graph: trace volume by service, budget line
      overlaid
  10  REALIZATION — hold it, silent beat                  [NEVER CUT]
  11  "Uniform collection is a tax you can't turn off"     Names adaptive sampling +
                                                            per-service budgets
  12  Section marker: an incident is a translation
      problem
  13  Dead end — one tool per signal (traces here,
      metrics there, logs elsewhere)
  14  OTel-native ingest — nothing lossy at the seam
  15  Query language — one syntax, before/after query     Highlight the diff, not two
                                                            dense slides
  16  "An incident isn't a data problem, it's a
      translation problem"
  17  Section marker: diffing beats reading
  18  The old way — reading a trace top-to-bottom
      under a page
  19  What the diff view does, in three lines             State what to watch before
                                                            starting the demo
  20  DEMO — known-good trace vs. incident trace,
      anomaly alert already flagged it                    Checkpoint: past 0:21, skip it
  21  Before/after screenshot                              Insurance if the demo dies
                                                            [NEVER CUT]
  22  "You don't read your way to root cause, you diff
      your way there"
  23  Arrow restated, verbatim from slide 2                [NEVER CUT]
  24  Repo + docs + handle + one line on the Terraform
      provider                                             Repeats slide 5's link, stays
                                                            up through Q&A

Cut checkpoints  Past 0:08 at slide 8 → drop the retention dead end, jump
                 straight to the graph (9).
                 Past 0:14 at slide 13 → drop the tool-per-signal dead end,
                 jump straight to OTel ingest (14).
                 Past 0:21 at slide 20 → skip the live demo, narrate slide
                 21 instead, keep the arrow.
                 Badly behind past 0:15 remaining → cut all of Pillar 2
                 (slides 12-16) whole, jump to the Pillar 3 marker (17).
                 Thin one pillar to nothing before you thin all three.
                 Never cut: 2 (hook), 10 (realization), 21 (demo
                 insurance), 23 (arrow).

Rehearsal plan   Accordion: speak it to 3 min, then 2, then 1, then 30
                 seconds, staying in character, ending strong each time.
                 Then expand back up through 1, 2, 3. What survives the
                 30-second rep is Pillar 1 + the arrow — everything that
                 only reappears on the way back up is the real cut list,
                 in cut order, and it overrules the checkpoints above once
                 you have a timed run.

                 Two open items before this is rehearsable:
                 - Demo fidelity tier unconfirmed. Given a 30-min technical
                   session and no rehearsal-hours number from you, default
                   recommendation is a scripted live demo against a seeded
                   environment (middle of the efficiency/value trade-off) —
                   budget it at 2x its rehearsed length, narrate the wait.
                   Confirm your rehearsal hours and I'll re-rank this
                   against a narrated screencast.
                 - Get a colleague to read only this outline and say the
                   arrow back in one sentence, unprompted, before you
                   finish the deck.

                 Quality gate (this skill's own bar, not a standard):
                 - Two consecutive timed runs land inside 26 min (30 minus
                   the 4-min buffer).
                 - Every slide passes one-idea + title-as-takeaway.
                 - Every pillar's evidence has a number or a screenshot,
                   not just an assertion.
                 - Demo ends by 0:24, at least 2 min of talking left after it.
                 - A colleague restates the arrow unprompted.

                 Do not finish the deck before the first timed run — it
                 tells you how much deck you actually need.
```

**One more disclosure note:** because you're DevRel at Corvid, name a real competing approach fairly on slide 5 and state honestly where Corvid is the wrong tool. An SRE-heavy room will clock the affiliation regardless — naming it in minute two is the only version that doesn't retroactively turn the whole talk into an ad.