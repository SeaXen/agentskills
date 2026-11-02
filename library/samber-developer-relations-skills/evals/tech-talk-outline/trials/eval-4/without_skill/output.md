## The math first

"25 minutes with Q&A inside" is not a 25-minute talk. Assume the organizer enforces the wall clock, not your outline — build to **18 minutes on stage**, leaving 7 for Q&A/buffer. Going from 41 → 18 is a **56% cut**. That's not trimming, that's a rewrite using the old deck as a slide bank. Don't try to snip individual sentences out of the existing script — you'll end up with dangling transitions. Rebuild the outline at 18 minutes, then pull surviving material in.

## New budget (18 min talk, 4 blocks)

| Block | Time | Change from original |
|---|---|---|
| Hook (headline numbers, not scene-setting) | 1:00 | new — didn't exist as a discrete beat before |
| Pillar 1 — why it fell over at 400k/s | 4:00 | down from whatever it currently runs |
| Pillar 2 — backpressure model | 6:00 | biggest slice — it's the "how," and DataCouncil's audience is there for the how |
| Demo | 3:00 | down from 4:00 |
| Pillar 3 — cost teardown ($18k/mo) | 2:30 | compressed to headline + one driver |
| Close | 1:00 | one takeaway, no retro |

**Put the hook first, not last.** Open with "our pipeline fell over at 400k events/sec, we rebuilt it, and it now saves $18k a month" in the first 60 seconds. If the moderator cuts you at minute 20 mid-demo, the two numbers everyone will repeat in the hallway already landed. Right now those probably pay off at the end of a 41-minute arc — that structure is fine internally, it's fragile against a hard external stop.

## Cut order — three passes, run each until you hit the target, then stop

**Pass 1 — structural (recovers ~12-14 min): delete whole sections, don't trim them.**
1. Company/team context, org chart, roadmap/"what's next for the team," acknowledgments beyond one credit line. Internal-audience material, zero value to a DataCouncil crowd. (~3-4 min)
2. The incident play-by-play — Slack screenshots, "then we tried X, then we tried Y," 2am timeline. Collapse to one sentence + one graph: "at [time], p99 went from 40ms to 12s — here's the chart." (~4-5 min)
3. The "alternatives we considered" walkthrough for the backpressure redesign. State the chosen architecture; dispose of the rejected ones in a single sentence each ("we also tried token-bucket and static rate limits — both broke under bursty producers"). Don't re-litigate each dead end. (~3-4 min)
4. Standalone "lessons learned" / retro section. Fold the single best insight into the 1-minute close; kill the rest. (~1-2 min)

**Pass 2 — compression (recovers ~6-8 min): keep the section, cut inside it.**
5. Old-architecture deep dive → the 2-3 facts that explain the ceiling (e.g., "single-threaded consumer, synchronous downstream writes"). Drop the full system diagram tour. (~2 min)
6. Backpressure implementation → one architecture diagram, mechanism explained verbally. Cut code/config line-by-line walkthroughs entirely — nobody reads code off a slide in a 25-minute slot. (~2-3 min)
7. Benchmark methodology → headline before/after numbers only. Methodology defense goes in your back pocket for Q&A, not on stage. (~1 min)
8. Cost teardown → before-total / after-total / delta / one biggest driver. Cut the itemized per-service line items. (~1-2 min)

**Pass 3 — polish (recovers ~1-3 min): only touch this if Pass 1+2 didn't get you to 18:00.**
9. Kill every "as I mentioned earlier" recap slide.
10. One anecdote/joke max, not several.
11. Trim the demo script to 3 scripted clicks. Record a backup video in case live AV eats time — if you're running long, cut to the video narrated over, don't extend the live click-through.

## Demo risk

A live demo is the single most common reason technical talks blow their time budget — it's the one segment with no upper bound if something hangs. Script exactly 3 moves, have a recorded fallback cued up, and treat the 3:00 as a hard stop, not a target.

## Escape hatch

Bookmark two slides you can skip live if you're behind at the 10-minute mark — one in Pillar 1 (a secondary failure-mode detail), one in Pillar 2 (a secondary design tradeoff). Rehearsing "I can drop these two and lose nothing load-bearing" beats discovering mid-talk that you have to improvise a cut.

## Verify

Rehearse against a visible timer, at least 3 runs, cutting on the clock, not on feel. Checkpoint: if you're not into Pillar 2 by minute 5, Pass 1 wasn't deep enough — go back and cut more from Pillar 1, since Pillar 2 is the section this audience is paying for.