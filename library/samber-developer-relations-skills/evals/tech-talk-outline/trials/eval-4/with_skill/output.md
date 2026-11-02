# Talk compression: 41-min internal talk → 25-min DataCouncil slot (Q&A inside)

You're not trimming — you're cutting more than half the talk. Doing that by thinning all three pillars evenly is the standard way this fails; the fix is cutting a whole movement, not shaving words off three.

## The math first

25 min slot, Q&A inside, plus buffer:

| Reserve | Minutes |
|---|---|
| Q&A (DataCouncil audience will push on trade-offs) | ~4 |
| Buffer (A/V, laughter, one slow question) | ~2 |
| **Spoken content budget** | **~19** |

41 measured minutes → ~19-minute target. That's a **54% cut**, not a trim. Flag: I assumed the Q&A split — confirm with the organizer if they specify an exact time inside the 25.

## Arrow (draft — confirm this is what you actually want remembered)

> "When throughput broke us at 400k events/sec, the fix wasn't a bigger buffer — it was signaling back — and it now costs $18k a month less to run."

Everything that doesn't serve this sentence is cut-list material, full stop.

## Arc: Migration (before/after), not three independent pillars

Your three pillars already describe a migration ("the backpressure model we replaced it with"), not three separate arguments. Fold the cost teardown into the evidence for pillar 2 instead of running it as its own act — that removes a whole mode-change, which is where you get most of your 22 minutes back.

- Old system + the constraint that broke it (400k events/sec)
- Forcing function (the outage/incident — this earns the problem, keep it short)
- New system (backpressure model)
- Real cost — **including what got worse.** Right now you have "$18k/month saved" with no downside. A data-eng audience will ask what you traded away (latency? complexity? on-call load? engineering weeks?) in Q&A regardless — name it yourself in one line, or the first question after your talk does it for you and it reads worse live than on a slide.

If you genuinely have nothing that got worse, that's rarer than it sounds — double-check before the slot, because "pure win, no downside" is the exact shape Q&A attacks hardest.

## Pillars (2, not 3 — the third becomes evidence)

| Pillar | Role | Evidence it carries |
|---|---|---|
| 1. Why it fell over at 400k ev/s | Old system + constraint | The number itself, one graph, one cause |
| 2. The backpressure model | New system | Mechanism + **both** numbers: $18k/month saved, and what got worse |

The demo (dashboards) is evidence *for pillar 2*, not a fourth section — it's proof the new system behaves, placed right after the insight lands.

## Realization (5-Second Moment)

Place at the end of pillar 1: "We used to think the fix was more buffer. Then [the specific moment the outage made that false] happened. Now we think: signal the producer before the consumer drowns." One sentence, spoken, not on a slide.

## Time budget (target: 19 min content + 4 min Q&A + 2 min buffer = 25)

```
0:00-0:01  hook: cold open on "400k events/sec, and it fell over"
0:01-0:02  promise + scope: what you'll leave with, who this isn't for
0:02-0:06  pillar 1 — old system + constraint, capped dead-end detail
0:06-0:07  realization — the belief flip, one sentence
0:07-0:13  pillar 2 — the backpressure model (protect this — it's the arrow)
0:13-0:17  demo — narrated, tied directly to proving pillar 2, not a tour
0:17-0:19  the receipt: $18k/month saved + what got worse, arrow restated
0:19-0:25  Q&A
```

Demo fidelity: I don't know if you're planning live or recorded. At 4 minutes inside a 19-minute budget, on an external stage, for a talk you can't afford to blow up mid-slot — go narrated screencast or a scripted demo against seeded data, not unscripted live typing. Budget it at 2x its rehearsed length regardless; if the honest rehearsed length is already 4 min, it'll eat 6-8 unless you cut it to a ~2-minute rehearsed core first.

## Cut order (structural hypothesis — see caveat below)

Cut in this order until you hit ~19 minutes:

1. **Everything that only made sense to colleagues in the room at the internal summit** — team names, internal tool names, org context, "how we rolled this out" asides. This never should have survived the trip from an internal talk to a CFP talk anyway; it doesn't serve the arrow for an external audience.
2. **Blow-by-blow incident narrative under pillar 1.** Keep the number, the graph, the one moment of realization. Cut the timeline of how the on-call rotation discovered it, what got paged, the Slack-thread color.
3. **The cost teardown's methodology walk-through.** Keep the number ($18k/month) and one line on how it's computed. Cut the line-item breakdown — it's a Q&A answer, not a slide.
4. **Demo feature tour.** Keep only the part that proves the pillar-2 claim. Cut any dashboard panel not directly answering "does backpressure work."
5. **Caveats and "we also considered X" footnotes** beyond one line each — these eat buffer without moving the arrow.
6. **Only if still over: thin pillar 1 further**, down to the single before/after number. Do not touch pillar 2 — it's closest to the arrow and the least cuttable thing in the talk.

**Caveat, stated plainly:** this order is my structural read of your material against the arrow — it is not measured. The skill this is built from is explicit that the real cut order comes from running the talk out loud, not from a ranking I compute. Treat the list above as your first rep's starting point, not the final word.

## Rehearsal plan — this is what actually decides the order

Run the Accordion (de Montebello): speak the talk to a timer at 3 min, then 2, then 1, then 30 seconds — staying in character, ending strong every time. Then expand back up through 1, 2, 3 minutes, adding material back deliberately.

- What survives the 30-second rep = your real arrow and pillars.
- What reappears on the way back up, and in what order, **is** the cut list — use that order over mine wherever they disagree. The exercise measures this talk with your voice against your material; a structural guess is a reasonable start, not a substitute.

Quality gate before you consider this outline done:

- Two consecutive timed runs land at or under ~23 minutes (25 minus your buffer).
- The demo ends with at least 2 minutes of talking left before Q&A.
- A colleague who only read the outline (not watched you rehearse) can say the arrow back in one sentence, unprompted.
- Someone outside the team can tell you where they got lost — the internal-summit version had a different curse-of-knowledge baseline than a DataCouncil room will.

One structural note, not a time cut: you work on this pipeline, so say so plainly in the first minute ("this is our production system, these are our numbers") — a data-eng audience assumes affiliation anyway on a war story like this, and stating it up front reads as credibility, not a pitch, especially once you've named what got worse.