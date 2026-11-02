Using the **tech-talk-outline** skill for this. Two things in your ask conflict with it directly, so I'm flagging both before the deliverable rather than silently overriding you:

**"22 slides, one per minute" — not applying this.** The skill's own craft rules are explicit: *"There is no slides-per-minute rule, and skills that invent one optimize the wrong variable... let the count fall out of [what each slide has to accomplish]."* A hook slide might need 10 seconds; a benchmark chart might need to sit on screen for two minutes while you talk over it. Forcing 1:1 gives you slides with nothing to say and sections with no room to breathe. What to tell comms instead: the slide count that survives your first timed rehearsal is the real number — I'd bet it lands around 14-16 for a 22-minute technical session, not 22.

**"Export straight into Google Slides" — not building the deck.** The skill refuses this outright: *"Refuse to output slide files... whatever the speaker asks — both defeat the artifact's purpose."* Building the deck before you've timed the talk means polishing slides the accordion rehearsal is about to delete. What you get below is the skeleton — title + bullets per slide, in order — which you paste into Slides yourself once it's survived a timed run, not before.

**Assumptions I made, since you gave me title + slot + audience but not a full interview** (correct any of these and I'll re-cut the outline):
- You work on the platform (implied by "our serverless platform") — built the disclosure into the outline.
- No live demo — this reads as a data/benchmark talk, not a hands-on-keyboard one. Say the word and I'll place one per the demo rules (after the problem lands, narrated, budgeted at 2x rehearsed length, never last).
- Q&A sits outside the 22 minutes, not inside it.
- One-off talk, not a re-give — if you're taking this to more events, say so, it changes what's worth over-investing in.
- I don't have your actual technical levers, so pillars 1-2 use placeholder mechanisms in `[brackets]` — swap in your real numbers/incidents before you rehearse; nothing in Q&A survives an invented statistic.

---

```
Arrow          "Cold starts weren't a scheduling problem — they were an
               initialization problem. We stopped re-doing the init work
               and started restoring a runtime that was already warm."
```
`[Swap for your real mechanism if it's not checkpoint/restore-shaped — e.g. predictive pre-warming, a runtime swap, a language change. The arrow must survive the 30-second accordion rep unchanged, so get the real one in before you rehearse.]`

```
Arc            Problem → dead ends → insight → proof (the default arc for
               a technical argument)
```
Why this over the alternatives: no outage to source, so the incident arc is out. Migration (before/after) is the closest runner-up — pick it instead if your real story is "we replaced architecture X with Y," not "we tried three things and one worked." Progressive construction and sparkline are both too expensive for a single 22-minute slot with no confirmed rehearsal ceiling. Contrarian doesn't apply — a Velocity Berlin audience already agrees cold starts are painful, they just don't yet believe an 80% cut is possible without a rewrite, which is exactly what arc 1 is built to earn.

```
Pillars        1. The obvious fixes don't fully work
                  Evidence: [your number] — e.g. "provisioned concurrency
                  cut p99 by ~30% but cost 4x at peak and still spiked
                  during traffic bursts."
               2. The real bottleneck was runtime init, not scheduling
                  Evidence: [your number] — e.g. "profiling showed 860ms
                  of the 900ms cold start was language/runtime init, not
                  waiting for capacity."
               3. Proof at scale, including the honest cost
                  Evidence: p99 latency before/after across your real
                  rollout scope, plus what got worse (memory footprint,
                  snapshot storage cost, etc.) — an optimization talk
                  that reports only gains gets torn apart in Q&A.
```

```
Realization    "We used to think the fix was scheduling more capacity
               ahead of demand. Once we saw where the 900ms actually
               went, we stopped trying to predict traffic and started
               asking why we were re-doing the same init work every
               time at all." — lands at minute 8, end of Pillar 1.
```

```
Time budget    (22 min slot, Q&A outside, 3 min buffer = ~14%)
               0:00-0:02  Hook + stakes
               0:02-0:04  Promise + scope + affiliation disclosure
               0:04-0:08  Pillar 1 — the dead ends
               0:08-0:13  Pillar 2 — the insight
               0:13-0:17  Pillar 3 — proof + tradeoffs
               0:17-0:19  Arrow restated, close
               0:19-0:22  Buffer (A/V handover, laughter, slow chart load)
```

```
Slide skeleton   (14 slides — this is what falls out of the content,
                  not a target. Re-count after your first timed run.)

 1. NEVER CUT — Title: "We cut cold starts 80% — here's what didn't
    work first"
    · Your name, role, [platform name], Velocity Berlin, handle
 2. NEVER CUT — Title: "[your real number] — what a cold start costs us"
    · Stakes framed in $ or SLA terms, not just milliseconds
    · One held beat of silence before you speak over it
 3. Title: "What you'll leave with — and who this isn't for"
    · The one technique to take away
    · Who this doesn't apply to (e.g. long-lived containers)
 4. Title: "I build [platform] — here's where it's the wrong choice"
    · Name 1-2 competing approaches fairly
    · State a case where you'd tell someone not to use it
 5. MARKER (Pillar 1) — Title: "Three things we tried that didn't work"
    · List the 3 dead ends by name only, no detail yet
 6. Title: "[Dead end #1] bought us [X%], not 80%"
    · The number, the cost tradeoff
 7. Title: "[Dead end #2] worked — until traffic spiked"
    · Graph job: the failure mode under load
 8. NEVER CUT — Title: "We were solving the wrong layer"
    · The realization, in your own words, said out loud, no bullets
 9. MARKER (Pillar 2) — Title: "The fix: [your real mechanism]"
    · Diagram job: before/after init sequence
    · First appearance of repo/docs link
10. Title: "[Mechanism] cut init from [X]ms to [Y]ms"
    · The single strongest number — the Sinatra-test evidence
11. MARKER (Pillar 3) — Title: "Rolled out to [scope] — the results"
    · p50/p99 before vs. after, real chart
12. Title: "The honest cost: [what got worse]"
    · Say the tradeoff before Q&A does
13. NEVER CUT — Title: [arrow, verbatim]
    · Restated in the same words as the hook
    · Second appearance of repo/docs/handle — stays up through Q&A
14. (Only if you add a demo) "What you just watched" — recap slide
    placed immediately after, per the demo rules.
```

```
Cut checkpoints   Past 0:08 and still on Pillar 1 → cut slide 7
                  (dead end #2 detail), jump straight to slide 8.
                  Past 0:13 and not yet at Pillar 3 → cut slide 12
                  (tradeoff detail), keep only the headline number
                  on slide 11.
                  Never cut: 1, 2, 8, 13 — title, hook, realization,
                  arrow. Everything else is negotiable under time
                  pressure.
```

```
Rehearsal plan   Accordion: run the talk to a timer at 3 min, 2 min,
                  1 min, then 30 seconds — stay in character, end
                  strong every time. Then expand back up through 1,
                  2, 3 min, adding material back deliberately. What
                  survives the 30-second rep is your real arrow and
                  pillars; whatever reappears on the way back up is
                  your cut list, in cut order — don't rank it
                  yourself, the rehearsal already did.

                  Quality gate before you call this done:
                  - Two consecutive timed runs land at or under 19 min
                    (22 minus the 3-min buffer).
                  - Every slide passes one-idea + title-as-takeaway.
                  - Every pillar carries a real number or incident,
                    not a placeholder — this is the one gate you
                    can't pass yet, since slides 6/7/10/11/12 are
                    still bracketed.
                  - A colleague who's read only this outline states
                    the arrow back in one sentence, unprompted.
```

Send me the real numbers for the three bracketed pillars and I'll fold them straight into this structure — the arc, timing, and cut list stay the same regardless of which specific mechanism you used.