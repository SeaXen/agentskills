# Key Messages — Microservice Minutes

Five messages, ordered for a 25-minute two-host conversation: hook → how it works → why trust it → proof of momentum → human close. Each one is a soundbite you can say in one breath, not a feature description — hosts will ask around these, not read them verbatim, so the wording matters more than the order.

**1. The pain-killer: zero-config mTLS**
> "mTLS is supposed to be table stakes, but in most meshes it's a project on its own — cert rotation, sidecar injection, a YAML file nobody wants to own. In Corvid Mesh it's not a feature you turn on, it's the default. Services get mutual TLS without an engineer writing config for it."
- Why platform engineers care: this is the ticket they've actually filed. Lead with it — it's the most concrete, demo-able claim you have.
- Proof point: name the exact config lines (or lack of them) it replaces. If you can say "zero YAML" or a specific before/after line count, do it on air.

**2. The build choice: Rust**
> "A service mesh sidecar sits in the hot path of every single request in your cluster. A GC pause there isn't an inconvenience, it's a latency spike across your whole fleet. That's why it's Rust, not Go — no GC to stall, and a class of memory bugs that just can't happen."
- Why platform engineers care: they've been burned by tail-latency surprises from infra-layer tools. This answers "why not just use X" before anyone asks it.
- ⚠️ Have one real number ready (p99 latency, memory footprint vs. a named alternative) — "fast because Rust" unsupported is a claim skeptics discount. If you don't have a public benchmark yet, say that plainly rather than asserting a number you can't back up on air.

**3. The trust signal: Apache 2.0, no strings**
> "It's Apache 2.0. Full stop. Platform teams have all watched a tool they standardized on go BSL, get acquired, or get paywalled overnight — we're not doing that. If we vanished tomorrow, your mesh keeps running exactly as it does today."
- Why platform engineers care: they're not just picking a tool, they're picking a bet for the next five years of their infra. This message directly defuses that risk — it's your "enemy" beat (the broken system is vendor lock-in and license bait-and-switch, not a competitor).
- Best used if a host asks "why open source" or "what's the business model" — don't dodge the monetization question, answer it in one sentence and move on.

**4. The momentum signal: traction, reframed as validation**
> "We're at 4,200 stars, but the number that matters more to me is [X production users / X contributors / X companies running it] — that's teams hitting this exact mTLS wall and deciding this solves it."
- ⚠️ Stars alone are a vanity metric to this audience — a platform engineer has seen plenty of well-starred repos that are one maintainer and a README. Fill in the bracket with something you can actually stand behind: contributor count, a named production user, weekly active clusters, PyPI/crates.io-equivalent download count — whatever is real. If nothing beats "stars" yet, say "still early, but growing fast" instead of overselling it.

**5. The human close: one specific story, not "teams love it"**
> "[Specific team/company] was running [specific pain — e.g., a hand-rolled cert-rotation cron job that broke twice] before switching. Now it's [specific outcome — time saved, incidents avoided, lines of YAML deleted]."
- Why platform engineers care: "teams love it" is filler — it answers nothing and invites a skeptical follow-up. One named, specific before/after does the same job and survives scrutiny.
- If you don't have a citable customer yet, don't force it — use a maintainer's or early adopter's story instead, but keep it concrete (a name, a number, a moment), not a vibe.

**Delivery notes for this format**
- 25 minutes, two hosts, video: budget roughly 3–4 minutes of airtime per message including back-and-forth — that's the whole episode, so don't try to also cover roadmap or pricing unless asked.
- Bridge line for when a host goes tangential: "That's a good example of exactly why we went with [Rust / Apache 2.0 / zero-config] — " then land the relevant message.
- Close on message 5, not message 1 — end the episode on the human proof, not the tech spec, since that's what a platform-engineer audience remembers and repeats.
- Skip "revolutionary," "game-changing," "disruptive" — this audience tunes out on contact with those words.