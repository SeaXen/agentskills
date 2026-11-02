## How technical to go: default to "strong mid-level," let the host's questions pull you deeper

Don't pick one fixed depth for the full 55 minutes. Anchor the default explanation at the level of a mid-level backend dev who knows the *vocabulary* of distributed systems (replication, quorum, network partition, leader) but not this protocol's specifics. Treat the principal engineers and the compiler-guy host as people you go deeper *for*, on demand — via their questions and via one dedicated comparison segment — not people you write the whole episode for. That keeps the majority of listeners oriented while still rewarding the people who came for depth.

Rough split: ~70% of airtime at "explain every protocol-specific term, assume the basics" depth, ~20% at real mechanism depth in the Raft-comparison block, ~10% reactive — as deep as the host takes it.

## The real problem: your two visual crutches don't survive audio

A diagram lets a listener hold five states in view while you talk. Code lets you point at a diff. Neither exists here — you have to build both in the listener's head using only sequence and repetition. That's the actual thing to prep, not "define fewer terms."

**Replacing the five-state diagram — narrate a day in the life of one node, not a list of five labels.**
- Don't enumerate "there are five states: A, B, C, D, E" up front — nobody retains a cold list over audio.
- Give each state a memorable, sticky name (not "State 3") so it can be referenced later without re-explaining.
- Walk the states in the order a real node actually visits them, as a mini-narrative: "Say you're a fresh node joining the cluster. You start in X. Something happens — Y — and now you flip to Z. From there, one of two things can happen..." Motion and cause-effect are what audio can carry; static enumeration is what it can't.
- Re-anchor at least twice: once briefly mid-explanation ("so we've gone from X to Z, that's two of the five") and once at the end as a fast recap. Listeners who half-tuned out need a re-entry point.
- If a state has a evocative failure or edge case, attach it to the name on first mention ("Z — this is the one that can get stuck if the network partitions"). Sticky detail beats abstract definition.

**Replacing the Raft code comparison — a one-paragraph semantic diff, never read code aloud.**
- Reading code on audio is close to useless; nobody can hold `if`/`else` branching in their head from speech. Compress it to the *shape* of the difference: "Raft does the commit in one phase once it has a majority ack. We split it into two phases because [specific reason]." One sentence of what, one of why.
- This is the moment to feed the compiler-brained host something precise to chew on — a concrete semantic divergence, not a vibe. He'll likely follow up with a correctness/liveness question; have the answer ready (what invariant you preserve, what you trade away, whether it's been through anything like TLA+ or a proof sketch).
- Don't volunteer the full Raft recap unless you sense the room needs it — a fast one-line reminder ("Raft: leader election, log replication, majority quorum — you know this") lets people who know it skip ahead and people who don't still catch the gist.

## Pre-loaded answers for when the host goes deep

Since the host is a compiler guy, expect him to pull on formal-semantics threads rather than product/use-case ones. Have crisp, short answers ready for:
- What safety/liveness property you're actually preserving, stated precisely (not "it's safe," but *what* can never happen).
- Message/round complexity vs Raft, in the worst case and the common case.
- Whether it tolerates the same fault model (crash-only vs Byzantine) — this is the kind of distinction a compiler person will probe immediately.
- Whether it's been formally specified or model-checked, and if not, why you're comfortable with that.

Keep each answer to 30–45 seconds unless he explicitly asks to go further — a compiler audience will follow you down a rabbit hole, but the mid-level majority is still on the call.

## Time-boxing for 55 minutes

- **0–5 min** — why you built this instead of using Raft/etcd/whatever off the shelf. Motivation story, zero jargon, hooks everyone.
- **5–20 min** — the state-machine narrative (the diagram-replacement above). This is the mid-level-dev core content.
- **20–35 min** — mechanism: leader election, log replication, how correctness holds. Slightly denser, still narrative-driven, define every term on first use.
- **35–48 min** — the Raft comparison block, one-paragraph diff plus reactive depth for the host's follow-ups. This is where the principal engineers and host get their payoff.
- **48–55 min** — practical wrap: where to find the code/paper, what to try, one memorable closing line.

## One thing worth doing regardless of format

Mention on-air that the diagram and code comparison will be in the show notes or a companion post, and actually publish them. It gives visual listeners something to click to, and it means the episode's transcript plus a written companion piece both exist for anyone (or any AI assistant) searching this later — the audio constraint doesn't have to mean the diagram and code never see daylight, just that they're not the thing carrying the live explanation.