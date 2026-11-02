## How technical to go

**Bottom line: aim at the "staff engineer / architect" depth, not "hands-on engineer."** Trade-offs, invariants, and what breaks at scale — never syntax, never the diagram as drawn.

Here's the calibration logic. Depth calibration works by finding the deepest listener and pitching one level below them so the median stays in the room. Your deepest listeners are the host (compiler background — he thinks in invariants and proofs by default) and the two principal engineers. There's no engineering-manager or buyer tier in this audience to also serve, which simplifies things to two rows:

| Listener | Anchor in | Leave out |
|---|---|---|
| Hands-on engineers (your median) | API surface, failure modes, migration cost | org framing, market size |
| Staff/principal, compiler-brained host (your ceiling) | trade-offs, invariants, what breaks at scale | line-by-line syntax |

One below the ceiling lands you on the second row — which is good news, because it's also exactly what audio-only already forces (no code read aloud, no screen-dependent diagram). The format constraint and the audience calibration point the same direction, so you're not fighting yourself.

Concretely:

- **Assume:** the room knows what a distributed system, leader election, and a network partition are, and has at least heard of Raft. Don't re-derive it from scratch.
- **Explain in one sentence each:** the two or three terms that are specific to *your* protocol and don't exist anywhere else — whatever your five states are called, define each in one clause the first time it's said.
- **Never say:** function/type names, wire-format detail, literal code, formal notation. The host will get more from "here's the invariant this buys you" than from syntax he can't see.

## Converting the five-state diagram

Diagram → metaphor + one number, per the format rule for audio. Don't describe boxes and arrows; describe roles and a timeout.

> "At any moment a node is playing one of five roles — think [candidate / leader / follower]-style roles, not five equal peers. The one that matters is how a node moves from [state A] to [state B]: that transition is gated by hearing from a majority, and it typically resolves in under [X ms]."

That's the floor everyone follows. To reward the host and the principal engineers without losing the median, use ADD as a depth ladder rather than just a question-answering shape:

1. **Answer** — the one-sentence metaphor above (median gets this and stays oriented).
2. **Detailed example** — the actual nuance the diagram existed to show: which specific transition is the one that prevents split-brain, stated as an invariant ("a node can only claim [state] if X holds"). This is the beat where the compiler-guy host and the principal engineers lean in — it's real content, just spoken instead of drawn.
3. **Describe relevance** — the so-what for the backend dev majority: what bug class this state machine makes structurally impossible for them, phrased as something they'd otherwise hit in production.

## Converting the Raft comparison

Same rule, no code. Turn "here's the diff in code" into one quantified structural sentence — shape of the call, not the call itself:

> "Where Raft commits after a majority round trip on every entry, ours commits after [N round trips / a different quorum shape], which costs [X] but buys back [Y]."

Round the numbers and always pair each one with a comparison point (a bare number teaches nothing on audio) — e.g., "roughly half the round trips Raft needs, at the cost of a slower recovery after a leader crash: about 2x Raft's worst case." That single sentence is dense enough to satisfy the compiler-guy host's instinct to ask "why," and concrete enough that a mid-level dev can repeat it back.

## Guardrail

Don't overcorrect downward — "mid-level backend dev" is not "junior." Leader/follower/quorum/term/leader-election are safe plain vocabulary; keep them. The thing you're cutting is formalism and syntax, not vocabulary. If you're unsure about a specific term while rehearsing, run it through: *would a mid-level backend dev nod or stall here?* Stall → one-sentence definition or cut it; don't carry a term the definition doesn't earn.