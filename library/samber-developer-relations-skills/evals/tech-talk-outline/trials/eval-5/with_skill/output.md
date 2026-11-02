Using the tech-talk-outline skill's re-derivation method (§ Invocation: *"Same talk, but it's a 10-minute lightning version now" → re-derive from the arrow; a lightning slot holds one movement, not a compressed three*) to answer this.

# Getting the 10-minute version out of the 30-minute one

## The mechanical answer

**Don't shrink the three sections proportionally.** A lightning slot carries "one point, or one demo — never both" (this skill's slot table). Three ~3-minute pillars is not a lightning talk, it's a rushed session talk, and rushed sections read as rushed, not as tight.

Instead:

1. **Run the Accordion on the 30-minute material you already have.** Speak it to a 3-minute timer, then 2, then 1, then 30 seconds — staying in character, ending strong every time. What survives the 30-second rep is the arrow plus whichever single pillar is carrying it. That survivor *is* your lightning talk's one movement — not a summary of all three pillars, the one that didn't fall off.
2. **Expand that single survivor back up to ~9 minutes**, holding the other two pillars out entirely rather than thinning all three to fit. (Failure-mode table: "The talk runs over → written to the material, not the slot → accordion down; cut a whole pillar, never thin all three." Same logic running in the other direction.)
3. **Reserve 1 minute as buffer** (10–15% of a 10-minute slot rounds to about a minute) for the meetup's inevitable A/V fumble.

Below is that process applied to *Zero-allocation JSON decoding in Go*, reconstructed from the shape you described (three sections + benchmark demo, 30 min). I don't have your actual pillar wording or benchmark numbers, so the specific claims below are placeholders in the pattern real Go alloc talks use — swap in your real arrow, pillar and numbers; the structure and the cut logic are what transfers.

**Assumed 30-minute shape**, arc 1 (problem → dead ends → insight → proof — the default technical arc, and the one three pillars + a benchmark demo naturally maps to):
- Pillar 1 — reflection-based decoding allocates on every field (evidence: `encoding/json` alloc profile)
- Pillar 2 — codegen (easyjson/ffjson-style) helps but copies still allocate (evidence: benchmark + escape analysis)
- Pillar 3 — a hand-rolled decoder that reuses buffers and skips `interface{}` hits zero allocations (evidence: the benchmark demo)
- Arrow — *"Every allocation in your decode path is a GC pause you scheduled yourself."*

Run the accordion on that, and pillar 1 and pillar 2 are what fall off first — they're the *dead ends*, the part of arc 1 that exists to earn the insight, not the insight itself. What survives to 30 seconds is pillar 3 plus the arrow. That's your one movement.

## The 10-minute lightning outline

**Arrow** — *"Every allocation in your decode path is a GC pause you scheduled yourself."* (verbatim, reused as the closing line — unchanged from the 30-minute version; the arrow doesn't get re-derived per slot, only what supports it does)

**Arc** — Insight → proof only, arc 1 stripped of its dead ends. The room doesn't need to be walked through why `encoding/json` and codegen fall short; ten minutes doesn't buy that argument. State the cost in one sentence, then go straight to the fix and the number.

**Pillar (one)** — A hand-rolled decoder that reuses buffers and never boxes into `interface{}` gets to zero allocations. Evidence: the benchmark, run live or shown as a screencast.

**Realization** — Same beat as the 30-minute version, compressed to one line instead of a held silence on a graph: the moment the room sees `0 allocs/op` next to `encoding/json`'s number. Say it, don't dwell on it — there's no minute budget to hold a beat for effect the way the 30-minute version can.

**Time budget**

```
0:00-0:01  hook: the one number — allocs/op or GC pause added per request by encoding/json
0:01-0:02  promise + scope: what to look for in your own decode path afterward; not for you if you're already on a zero-alloc decoder
0:02-0:03  what to watch before the demo starts: name the allocs/op line, not the whole benchmark output
0:03-0:07  the demo: encoding/json vs the zero-alloc path, benchmark numbers on screen
0:07-0:09  arrow restated, same words as the hook, plus the one line of code that was the fix
0:09-0:10  repo/benchmark link held up — hard stop, no Q&A in a lightning slot
```

Buffer: ~1 minute, absorbed into the demo segment if the meetup's A/V runs long.

**Demo fidelity for this slot specifically** — narrated screencast, not live. A 10-minute lightning slot at a first-time outing has the lowest rehearsal ceiling of your four dates, and this skill's ranking deletes live typing outright under a low ceiling regardless of how impressive it looks. A screencast also edits out the dead air of `go test -bench=.` actually running, which a hard 10-minute slot can't afford to sit through live. Since you're re-giving this talk three more times, the screencast is a cost paid once and reused at the conference and both customer sessions — recorded/reusable assets amortize across a re-give, per this skill's ranking of arc and demo choices for talks given more than once.

If A/V is uncertain even for a screencast, fall back to "one point, no demo": drop 0:03–0:07 entirely, replace it with the single before/after pprof allocation graph as a static slide, and hand the audience the repo link to see the benchmark themselves. Never mix the two — a half demo plus a point is the compressed-three mistake again, just with two items instead of three.

**Slide skeleton**

| # | Slide must accomplish | Notes |
|---|---|---|
| 1 | Title + handle | |
| 2 | The one number: allocs/op or GC pause added by `encoding/json` | The hook, no explanation |
| 3 | What you'll be able to spot in your own decode path afterward | The promise, one line |
| 4 | What to watch: the allocs/op line | Say it before starting the demo |
| 5 | DEMO or the before/after graph if no demo | Never cut this slide |
| 6 | "Every allocation in your decode path is a GC pause you scheduled yourself" | Arrow, verbatim from slide 2 |
| 7 | The one line of code that was the fix | Highlight only the changed line |
| 8 | Repo + benchmark + handle | Repeats a link, stays up through the hard stop |

**Cut checkpoints**
- Past 0:04 at slide 4 → skip narrating the "what to watch" line, jump straight to the demo/graph.
- Past 0:07 → cut straight to the arrow slide, skip the code-diff slide.
- Never cut: slide 2 (the hook number), slide 5 (the proof), slide 6 (the arrow).

**Rehearsal plan** — Run the accordion again, but starting from *this* 10-minute draft rather than the 30-minute one: 3 min → 2 min → 1 min → 30 sec, then back up to 9 minutes. What survives the 30-second rep here should be exactly the hook number and the arrow — if something else survives instead, that's the real one-movement lightning talk, not what's drafted above. Quality gate before it's meetup-ready: two consecutive timed runs land inside 9 minutes, the demo (or graph) ends with at least 2 minutes of speaking left, and a colleague who only reads the outline can say the arrow back unprompted.

## Carrying this to the other three dates

Store the arrow, the arc choice, all three pillars, and the cut order from tonight's accordion run — the 30-minute conference version and the two 40-minute customer sessions aren't separate derivations, they're this same material re-expanded to different slot lengths. The 30-minute slot restores pillars 1 and 2 as the "dead ends" that earn the insight; the 40-minute customer sessions likely want a fourth kind of evidence layered in (operational cost, team ramp-up) rather than a fourth pillar, since a customer-site room usually mixes engineers with people who care about risk and cost, not technique alone.