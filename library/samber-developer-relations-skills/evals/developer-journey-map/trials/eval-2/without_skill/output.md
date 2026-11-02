Sanity check first: one of your two "broken" numbers isn't broken. Fix that before the VP sees it.

**The math**

| Metric | Northwind actual | Cited benchmark | Verdict |
|---|---|---|---|
| Quickstart → first produce/consume | 28% | 40-60% | Real gap. 12-32 points below range. |
| Signup → activation (topic + 1 message consumed, 7 days) | 22% | 20-40% | **Inside the range.** Low end, but not broken. |

22% sits inside 20-40%. Calling it "broken" is a claim your own citation contradicts — if anyone on the VP's side does this arithmetic live, it undercuts the whole deck, including the quickstart point that IS real.

**Before you use these benchmarks at all, flag this caveat:** "40-60%" and "20-40%" are generic PLG blog figures (Userpilot/Amplitude/OpenView-style roundups), pooled across API products broadly — payments, auth, no-code, analytics. They're not infra-specific. A managed Kafka alternative asks backend engineers to configure networking, security/ACLs, and a client library before they see a message flow — that's inherently higher-friction than a single curl call against a payments API. Comparing against Confluent Cloud, Redpanda, AWS MSK Serverless, or Upstash Kafka's actual quickstart numbers (if obtainable) would be the honest reference class; against generic "API products," 28% may be unremarkable for the category, not a crisis. Recommend saying this out loud in the meeting rather than letting someone else find it.

---

## Northwind Streams — Activation Journey Map
**Segment:** Backend engineers, Series A-C startups | **End state:** Production usage

### Opening framing (corrected)

Two numbers, two different stories:

- **Quickstart completion is a confirmed gap.** 28% finish a first produce/consume call, versus a commonly cited 40-60% for self-serve API products. Even allowing for the caveat above, this is worth root-causing.
- **Activation is in-range, not broken.** 22% hit topic-created + message-consumed within 7 days, against a cited 20-40% band. It's the bottom of the band — an opportunity to move up, not a fire.

The real story: **most of the loss happens between "started" and "first success" inside the quickstart itself**, not after. That's where a fix has the most leverage.

### Stage-by-stage

**1. Discovery / landing**
- Goal: decide if this is worth 15 minutes of my time.
- Signal a backend engineer looks for: can I see a real broker endpoint and a code sample before signing up, or do I hit a gated demo request first.
- Risk: if signup is required before any code is visible, self-selection drops before the funnel even starts — this stage isn't in your 28%/22% numbers at all and is worth measuring separately.

**2. Signup**
- Goal: get credentials fast, get back to the terminal.
- Risk: any field beyond email + password (company size, use case dropdown, "book a call") adds friction disproportionate to an engineer's patience.

**3. Quickstart: first produce + consume — 28% complete**
- Goal: prove the thing works before investing further.
- This is the stage with the largest confirmed gap. Hypotheses worth instrumenting (not yet confirmed by data you've shared):
  - Step-level drop-off: is loss concentrated at cluster provisioning wait time, client library install, auth/ACL setup, or the first produce call itself? Right now "28%" is one number; you need the funnel inside it.
  - Client library maturity/language coverage — if a user's language isn't well-supported, they may abandon silently rather than file a complaint.
  - Local-first engineers may expect a Docker/CLI path and bounce off a console-first UI, or vice versa.
- Recommendation: before the VP meeting, pull the step-by-step funnel for this single stage. That's the number that explains the 28%, and it's the one actionable in the next sprint.

**4. Activation: topic created + 1 message consumed, 7-day window — 22%**
- Goal: convince myself this fits my actual architecture, not just the demo.
- In-range per cited benchmark, but two things worth checking before treating 22% as fine:
  - Is the 7-day window generous or tight relative to how backend engineers actually evaluate infra (often a multi-week POC, not a single sitting)? If your window is tighter than how the category benchmark defines "activation," 22% may be understating you, not the reverse.
  - Trend across quarters — one quarter's 22% could be noise. Ask for the last 3-4 quarters before presenting it as a stable data point.

**5. Integration into their own service**
- Goal: replace a toy topic with a real one from their app.
- Watch for: schema registry setup, consumer group rebalancing behavior, migration effort from an existing Kafka/MSK deployment — this is where "activated" users either commit or quietly stall.

**6. Team rollout**
- Goal: get a second engineer using it without re-explaining everything.
- Booster opportunity: if the first user's config/topics carry over visibly to a teammate's view, that's an endowed-progress moment — the second engineer starts ahead of zero.

**7. Production usage — end state**
- Goal: trust it enough to put customer-facing traffic on it.
- Requires: confidence in uptime/SLA, monitoring/alerting integration, and a support answer for "what happens when this breaks at 3am" — the last gate before this stops being an evaluation and becomes infrastructure.

### What to instrument next

1. Split the 28% quickstart number into its own step-level funnel (provisioning, auth, library install, first produce call).
2. Pull activation rate by quarter, not just last quarter, to confirm 22% is a stable number.
3. Find 2-3 real infra-category peer benchmarks (Confluent, Redpanda, MSK Serverless, Upstash) to replace the generic API-product figures before the VP deck goes out.

Next: pull the step-level quickstart funnel — that's the one number that turns "we look broken" into a specific, fixable stage.