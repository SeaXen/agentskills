⚠️ I won't invent quotes and attribute them to Rui, or invent your teammate's technical decisions and metrics for her promo packet — I have no actual account of either migration, and fabricated quotes/achievements attached to real, named people is the kind of thing that backfires badly if it ships as-is (Rui gets misquoted in something public-facing; your teammate's promo case gets challenged because a detail doesn't hold up under a panel's questions).

What I can hand you now: two full, ready-to-fill case study drafts in proper customer-story format, built around the one real fact you gave me (Kafka → Redpanda, last spring, 40% cost drop). Everything else is bracketed. Drop in real numbers and real quotes and both are done — no restructuring needed.

---

## Case Study 1 — Internal/Technical: Kafka → Redpanda

**How [Company] Cut Ingestion Costs 40% by Moving Off Kafka**

*Industry: [X] · Team: [Data Platform / Infra, X engineers] · Timeline: Spring 2026 · Result: 40% lower ingestion infra cost*

### The Challenge

By early 2026, [Company]'s ingestion layer — built on Apache Kafka since [year] — was handling [X messages/day or GB/day]. The team was hitting [specific pressure: broker costs scaling faster than volume / ZooKeeper operational overhead / JVM GC pauses under load / rebalancing storms / cross-AZ replication costs — pick what's true]. Something had to give before it became a blocker for [what growth/roadmap item].

### Why Redpanda

The team evaluated [alternatives considered, if any] before settling on Redpanda, weighing it against Kafka on:

- **Cost** — no ZooKeeper fleet, no JVM, C++ core cut per-broker resource footprint
- **Ops burden** — [specific: fewer moving parts, built-in tiered storage, simpler upgrade path]
- **Compatibility** — Kafka API-compatible, so [what didn't need to be rewritten: producers/consumers, schema registry, client libraries]

> "[One sentence — the actual reason Rui greenlit Redpanda over staying on Kafka or trying an alternative.]"
> **— Rui, Staff Engineer**

### The Migration

- **Scope**: [which topics/pipelines moved, in what order — big bang vs. phased]
- **Approach**: [dual-write / shadow traffic / cutover window — however it actually went]
- **Duration**: [X weeks], from [date] to [date]
- **Team**: [who worked on it, how many engineers, how much of their time]
- **Hardest part**: [the thing that actually went wrong or almost went wrong — real case studies always have one; this is what makes it credible]

> "[Quote from Rui about the hardest technical moment, or what surprised them.]"
> **— Rui, Staff Engineer**

### The Results

| Metric | Before (Kafka) | After (Redpanda) |
|---|---|---|
| Infra cost | [$X/mo] | [$X/mo] — **40% lower** |
| p99 ingestion latency | [X ms] | [X ms] |
| Broker/node count | [X] | [X] |
| On-call incidents (ingestion) | [X/quarter] | [X/quarter] |

### What's Next

[One paragraph: what this unlocked — more headroom before next scale-up, freed engineering time redirected to what, any second-phase plans.]

> "[Closing quote from Rui — forward-looking, one sentence.]"
> **— Rui, Staff Engineer**

---

## Case Study 2 — For the Promo Packet: [Teammate]'s Migration

Promo packets get scrutinized for specificity — vague "drove the migration" language reads as padding to a calibration panel. This uses a Situation/Task/Action/Result shape mapped to whatever your promo rubric scores (scope, technical depth, cross-team leverage, ambiguity handled), so she can swap in real specifics without changing structure.

**Project: [Migration name]**
*Role: [Tech lead / sole owner / co-lead with X] · Scope: [X systems / X teams affected / X engineers involved] · Timeline: [dates]*

### Situation

[What was breaking or about to break, in concrete terms — what would have happened if nobody touched this. This is where "impact if ignored" lives, which is what promo panels weigh most.]

### Task

[What she was specifically accountable for — distinct from what the team did. If others contributed, name the boundary of her ownership explicitly; vague shared credit is the #1 thing that weakens a promo case.]

### Action

- [Decision she made and the alternative she rejected, with why]
- [How she handled the hardest/most ambiguous part — this is the "operates at the next level" evidence]
- [Who she influenced or unblocked outside her direct reporting line, if anyone — cross-team leverage is usually a separate scoring dimension]

### Result

- [Quantified outcome #1 — cost, latency, reliability, velocity]
- [Quantified outcome #2]
- [Any downstream effect: did this unblock another team's roadmap, prevent an incident class, etc.]

> "[Peer or stakeholder quote on her specific contribution — ideally from someone senior to her or from an adjacent team, since panels weight cross-functional endorsement more than same-team praise.]"
> **— [Name, Role]**

### Why this matters at the next level

[One paragraph translating the above into whatever language your leveling rubric uses — e.g., "this is Senior-scope work because it required making an irreversible infra call under incomplete information and coordinating three teams without formal authority over any of them."]

---

### Getting the real content

Fastest way to fill both in — a short interview beats trying to reconstruct this from memory weeks later:

**For Rui** (5 min, Slack or in person):
1. What was actually breaking with Kafka before this started?
2. Why Redpanda over [any other option considered]?
3. What went wrong or nearly went wrong during the cutover?
4. In your own words, one sentence on the win.

**For your teammate:**
1. What would've happened if this migration hadn't happened?
2. What decision are you most sure you got right, and what did you almost do instead?
3. Who outside your immediate team did you have to convince or unblock?
4. Ask one peer/stakeholder for a two-sentence quote on her specific contribution — don't write it for them.

Send me the answers and I'll drop them straight into these drafts, polished, same structure — no rewrite needed.