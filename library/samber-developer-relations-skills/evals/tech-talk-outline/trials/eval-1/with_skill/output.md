Built on what you gave me. One pillar needs your input before it's real — flagged below, not blocking the rest.

**Blocking:** Pillar 2 needs your actual pre-migration attempts (pool tuning? prepared-statement caching? a different driver first?). I used placeholders — swap them for what you really tried.

**Confirm or these defaults stand:** room composition (assumed mixed hands-on + staff, platform track), demo (assumed scripted live run of the harness + recorded screencast fallback, no unscripted live typing), recording (assumed yes — check "Klaxis" and the 340ms/61ms numbers are clear to publish), your OSS client's real name (used `[CLIENT]`), whether this gets re-given elsewhere, and whether you have a colleague/room for timed runs or just solo evenings.

---

# Postgres Wire Protocol Without the Driver — ScaleConf Lisbon

25-minute slot, platform track, Q&A is a separate 5 minutes after (not carved out of the 25).

## Arrow

> "The wire protocol was never the bottleneck. The abstraction sitting on top of it was, and you can measure how much it costs before you rip anything out."

Reused verbatim as the closing line.

## Arc

**Problem → dead ends → insight → proof**, recommended over Migration (before/after).

Gate first. Incident is ruled out: there's no outage or failure timeline in your material, just a latency number — no incident, no incident arc. Sparkline and Contrarian are ruled out too: a 25-minute platform-track session isn't a keynote, and nothing in the abstract suggests the room holds an opposing belief strong enough to earn a contrarian structure.

That leaves two real candidates, both fed by the same material (your flame graphs and migration diff):

- **Problem → dead ends → insight → proof** (recommended) — ranks higher on value because it transfers a technique, which is exactly what your abstract promises: "decide whether raw protocol access is worth it... and how to measure it." Walking through what you tried and why it didn't work is what makes the insight earned instead of obvious, and it's what lets someone in the audience replicate your decision process on their own service instead of just admiring your number.
- **Migration (before/after)** — cheaper to draft (pure recall, no dead-end material needed) and maps well onto a room that mostly maintains existing systems, but its shape ends on "the real cost, including what got worse," which serves a "how we did it" talk better than the decision framework your abstract actually sold.

What this ranking starves: Migration's natural honesty about cost. Fold that in anyway — pillar 3 should name what got worse (see Failure modes: a talk that reports only gains reads as marketing), even though Migration isn't the chosen arc.

## Pillars

1. **The tax was in the driver, not Postgres.** Evidence: the *before* flame graph — the call path showing where time actually went (protocol negotiation, marshaling, round trips) versus actual query execution.
2. **The obvious fixes didn't touch it.** Evidence: `[PLACEHOLDER — your real attempts]`. Candidates to confirm or replace: connection pool tuning / PgBouncer in front (cuts connection setup, not per-query protocol tax), ORM-level prepared-statement caching (helps the database re-parse cost, not the driver's own marshaling), batching to cut round trips (helps N+1 patterns, not the fixed per-request tax). Whatever you actually tried, name why each one fell short — an asserted dead end reads as a strawman.
3. **Go direct, and measure it yourself.** Evidence: the migration diff (highlighted lines only), the *after* flame graph at the same scale as pillar 1's, and the benchmark harness as a method the audience can run against their own service — not just your number. Also where this pillar names what got worse (see Migration's starved honesty, above) and where you disclose Klaxis + `[CLIENT]`.

Per-pillar term to define out loud once (curse-of-knowledge guard for a mixed room):
- Pillar 1: what a protocol-level *round trip* actually is (a wire exchange, not an HTTP-style call).
- Pillar 2: driver-level pooling vs. PgBouncer-level pooling — the two get conflated constantly.
- Pillar 3: simple query protocol vs. extended query protocol — this is probably the actual mechanism the whole talk hangs on.

## Realization

Minute ~0:08-0:09, end of pillar 1: "We used to think the network was the tax. Then we flame-graphed the client, not the query, and found the tax was our own driver talking to itself. Now we think: profile the client stack before you blame the server." Hold the flame-graph slide silently for a beat before saying it.

## Time budget

Q&A sits outside the 25, so the full slot is content — nothing carved out for questions.

```
0:00-0:02  hook + stakes         "Our p99 was 340ms. Not because Postgres was slow.
                                  Because our driver was renegotiating the protocol
                                  on every request, and nobody had noticed."
0:02-0:04  promise + scope       what you'll leave able to decide; "not for you if
                                  your p99 already meets SLO, or you don't control
                                  your client library"
0:04-0:09  pillar 1              the tax was the driver → realization at ~0:08
0:09-0:13  pillar 2              the dead ends, and why each fell short
0:13-0:18  pillar 3              go direct + measure it yourself; disclosure lands here
0:18-0:20  demo                  benchmark harness, live or screencast
0:20-0:22  arrow restated, close
0:22-0:30  Q&A (after the timed slot)
```

Buffer: 3 minutes (12% of 25), absorbed across pillars 1-3 — each can run a minute long without eating the demo or the close.

## Slide skeleton

| # | Slide must accomplish | Notes |
|---|---|---|
| 1 | Title + handle + Klaxis + `[CLIENT]` | |
| 2 | "Our p99 was 340ms. Not because Postgres was slow." | The hook. **Never cut.** |
| 3 | What broke, one number | 340ms → 61ms, no explanation yet |
| 4 | The promise | Decide if raw protocol access is worth it, and how to measure it |
| 5 | Scope, out loud | "Not for you if..." |
| 6 | Disclosure | Staff engineer at Klaxis, maintain `[CLIENT]`; name competing drivers fairly; state where `[CLIENT]` is the wrong choice. **Never cut — credibility, not timing.** |
| 7 | Section marker: the driver was the tax | |
| 8 | Before flame graph, full call path | |
| 9 | Where the time actually went | Annotated: parsing, marshaling, round trips — replace with your real breakdown |
| 10 | Realization slide | Hold silently for a beat. **Never cut.** |
| 11 | Pillar 1 landed: "The tax was the driver talking to itself" | |
| 12 | Section marker: the obvious fixes didn't touch it | |
| 13-15 | One dead end per slide, each with why it fell short | `[PLACEHOLDER]` |
| 16 | Pillar 2 landed: "None of it touched the protocol tax" | |
| 17 | Section marker: go direct, measure it yourself | |
| 18 | The migration diff | Highlight changed lines only |
| 19 | After flame graph, same scale as slide 8-9 | Evidence sits next to the claim it proves |
| 20 | "This became `[CLIENT]`" | First link appearance — evidence, not the point |
| 21 | What the harness measures, in three lines | Setup for the demo |
| 22 | DEMO — what to watch: the p99 line, not the query output | Checkpoint: past 0:19 → skip to slide 24 |
| 23 | What you just saw | Insurance if the demo half-works |
| 24 | Arrow, verbatim from slide 4's promise | **Never cut.** |
| 25 | Repo + `[CLIENT]` + docs + handle | Second link appearance, stays up through Q&A |

## Cut checkpoints

Provisional — structural judgment, not an accordion result. Your own timed runs will reorder this; don't treat it as final until you've run the accordion (see below).

- Past 0:11 in pillar 2 → drop to two dead ends instead of three, cut the weakest.
- Past 0:16 in pillar 3 → skip the live demo, show slide 19 + slide 23 instead, keep the arrow.
- Never cut: slides 2, 6, 10, 24.

## Rehearsal plan

Run de Montebello's accordion: speak it to a 3-minute timer, then 2, then 1, then 30 seconds, staying in character, ending strong each time. Then expand back up through 1, 2, 3. What survives the 30-second rep is the arrow and pillars; what only reappears on the way back up is the real cut list, in cut order — not the provisional one above.

Seven weeks, evenings mostly free — enough runway for this shape:
1. Weeks 1-2: lock the arc, fill pillar 2's real dead ends, rough the slides. Don't finish the deck yet.
2. Weeks 3-4: first accordion pass + first timed run in front of a colleague if you can get one.
3. Weeks 5-6: fix what the timed runs actually revealed, not what you assume is weak.
4. Week 7: two consecutive clean timed runs inside 22 minutes (25 minus the 3-minute buffer), dress rehearsal.

Quality gate, iterate until all five pass:
- Two consecutive timed runs land inside 22 minutes.
- Every slide passes one-idea + title-as-takeaway.
- Every pillar carries at least one concrete piece of evidence (pillar 2 currently doesn't — that's the blocking item).
- The demo ends at least 2 minutes before the slot does.
- A colleague who's only read this outline states the arrow back in one sentence, unprompted.

---

Next: send me your real dead-end material for pillar 2 — that's the one gap this outline can't close without you.