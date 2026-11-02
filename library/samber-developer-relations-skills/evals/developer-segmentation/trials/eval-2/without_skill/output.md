# Nimbus Relay — H1 SDK Audience Decision

## The decision, stated plainly

"Audience" for an SDK roadmap collapses to two questions, not one:

1. **Which language/runtime gets first-class SDK investment in H1?** (breadth call — where do you point engineering time)
2. **Which capabilities does that SDK need?** (depth call — what does that audience actually block on)

Signup data answers (1). Sales-call notes answer (2). You don't need a survey to answer either — you need to mine what you already have correctly. Here's how, in two afternoons, with the decision rule built in so you don't stall on "the data is ambiguous."

## Afternoon 1 — signup data (answers: who, and are they growing)

Pull three cuts, not one. A single "top language by signup count" query will mislead you — it rewards whoever was popular two years ago, not whoever is compounding now.

1. **Share + trend, split**: language/runtime share of signups in the trailing 90 days vs. the trailing 24 months. A language at 12% today but doubling year-over-year outranks one sitting flat at 20%. Trend beats snapshot.
2. **Language × runtime cross-tab**: e.g., Python-on-Lambda vs. Python-on-long-running-worker. This matters more than language alone for a message queue — serverless callers need stateless, fast-reconnect clients with no persistent pool; long-running consumers need connection pooling, graceful shutdown, backpressure. Two very different SDKs can hide under one language label.
3. **Join to activation, not just signup**: for each language/runtime cohort, what fraction is still sending/consuming messages at day 90? Signup volume tells you who tries you; day-90 activation tells you who a queue is actually load-bearing for. Weight activation over raw signups — tire-kickers inflate the wrong cohort.

Output: one ranked table — cohort × volume share × trend × activation. That's your breadth candidate list.

## Afternoon 2 — 200 sales-call notes (answers: what blocks money)

Don't read 200 notes narratively — you don't have the afternoon for it. Keyword-tag them instead:

- **Language/framework mentions** (Java, Go, Node, .NET, Python, Rust, PHP, Ruby…)
- **Runtime/infra mentions** (Kubernetes, Lambda, ECS, on-prem, VM)
- **Competitor/incumbent mentions** (Kafka, RabbitMQ, SQS, Confluent, NATS) — tells you the bar your SDK is being measured against
- **Explicit SDK-blocker language** ("no client library for X," "had to wrap the API ourselves," "our team writes Go, you don't have a Go SDK") — this is your literal gap list, in the buyer's own words, which is the thing an interview would normally give you
- **Deal outcome** (won/lost/stalled) attached to each note, so a language mention from a closed-won enterprise deal outweighs the same mention from a stalled $29 trial

Output: a second ranked table — cohort × mention count × win-rate-weighted × verbatim capability asks. That's your depth requirements list, and it's also your enterprise-revenue signal, which signups alone can't give you.

## The synthesis rule

Signups tell you where growth compounds. Call notes tell you where revenue concentrates. Don't average them — rank them separately, then apply this rule: **the H1 SDK's primary language is whichever cohort scores well on *both* tables** (real volume/trend from signups, real win-rate pull from calls). If nothing clears both bars, default to the signup winner for the audience call, and treat the call-notes winner as the required capability set layered on top — because self-serve is your growth engine and the SDK is its front door, while enterprise objections tell you what breaks the front door once someone leans on it.

One judgment call I can't make for you: whether H1 is optimizing for growth (self-serve volume) or revenue concentration (enterprise ARR). That's a five-minute conversation with whoever owns the H1 number, not a data question — get that weighting confirmed before you run the two afternoons, or you'll re-litigate it after.

## What to hand the SDK team

A one-page decision doc, not a data dump:

- **Primary audience**: [cohort from the joint-winner rule] — build/harden this SDK first.
- **Required capabilities**: the top 3–4 verbatim blockers from the call-note tags, scoped to that cohort's runtime (serverless vs. long-running matters here).
- **Explicitly deprioritized**: cohorts with low share, flat/declining trend, and no enterprise pull. Naming what you're *not* building is what actually prevents scope creep in H1.
- **Confidence: medium.** This is Mode-1/Mode-2 evidence (existing data, no direct customer conversation) — real signal, but proxy signal. Say so in the doc so nobody mistakes it for validated.

## The blind spot, named honestly

You've never asked a user what they're building or run a PMF check. That's a real gap this exercise doesn't close — it routes around it. Ship a single async question at signup or in-app now ("what are you building with the queue?" or the Sean Ellis "how would you feel if you could no longer use Nimbus Relay?") in parallel with this decision. It won't be ready before day 9, but it means the H2 roadmap isn't made from proxy data again.