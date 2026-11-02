## Kill the benchmark. Here's why, then the replacement.

**The benchmark isn't a tradeoff — it's blocked by every constraint you listed, not just one.**

- A benchmark against two named incumbents *is* new data collection (you have to run their tools) *and* new publication (you're putting comparative numbers in public). Legal didn't say "be careful with benchmarks" — they said no to exactly this category. There's no version of "benchmark vs. incumbents" that doesn't require both.
- Even if legal weren't in the picture: one afternoon does not produce a defensible benchmark. Methodology holes are what benchmarks get torn apart over — cache warm state, workload selection, hardware parity, incumbent config flags. A rushed number against two incumbents with bigger eng and marketing teams than you is a free invitation for them to publish a rebuttal the same week as your conference slot. You'd be trading your launch narrative for their rebuttal's news cycle.
- No customer on record means you can't even backstop a weak benchmark with "and here's what it did for X" — the two things that usually make a benchmark land (rigor, or social proof) are both unavailable.

Don't relitigate this with your co-founder as "good idea vs. bad idea." Frame it as: legal already vetoed it, independent of whether it's smart. Put it on the roadmap for next quarter once legal clears new publications — that keeps the idea alive instead of killing it, which is an easier conversation than "I don't think we should."

## The angle: mechanism, not comparison

Pitch **how 2.0 works**, not how it compares. A technical deep-dive on the specific design decision that makes the speedup possible — the one thing in 2.0 you're proudest of solving.

Why this fits every constraint:

- **Zero new data collection.** You're not measuring anything new — you're explaining an architecture you already built. The content is in your team's heads and design docs today.
- **Zero legal exposure.** No claims about competitors, no customer data, nothing "new" to clear — it's a description of your own system.
- **No customers needed.** The credibility comes from the technical reasoning being sound and specific, not from a logo wall.
- **Fits one afternoon.** The eng work isn't code — it's you (or whoever owns the mechanism) narrating the design decision to a writer/marketer, plus one or two diagrams. That's an afternoon of interview + a day or two of writing, not new engineering.
- **Matches the venue.** You already have a stage — the partner conference. A technical narrative is what a conference talk is *for*. A benchmark claim is what gets you cornered in the hallway afterward by the incumbents' engineers.

**Positioning line to work from:** *"Here's the specific problem in build caching that [incumbent category] structurally can't solve, and how 2.0 solves it."* Anchor on a mechanism, not a percentage — cache invalidation correctness, hermeticity guarantees, multi-tenant isolation, cross-monorepo cache sharing, whatever your actual hardest-won 2.0 feature is. You know which one that is better than I do; pick the one where the "why it's hard" explanation is genuinely interesting to a technical reader, not just a feature list item.

## 18-day plan

1. **Today:** pick the one mechanism. One afternoon: the person who built it explains it to whoever's writing, on the record, informally — this is your only eng-time spend.
2. **Days 2–5:** draft the technical post (architecture story, diagrams, design tradeoffs). This is writing/design time, not eng time.
3. **Days 5–10:** turn the same narrative into the conference talk outline. Same content, two formats — don't write two different stories.
4. **Days 10–14:** internal review, tighten claims so every sentence is defensible without external data (no "faster than X," only "solves Y problem this way").
5. **Day 15–16:** publish the post day-of/day-before the conference talk, cross-post to your usual channels (dev.to, HN "Show HN" or direct submission, your blog).
6. **Conference day:** talk delivers the narrative live; post is what people share afterward.
7. **Buffer:** 2 days spare for the inevitable slip — you have none to lose given the fixed date, so don't schedule anything into it.

No new engineering beyond the afternoon, no legal review needed beyond a normal PR pass, no customer asks, and it uses the conference slot as the actual distribution mechanism instead of hoping a benchmark goes viral on its own.