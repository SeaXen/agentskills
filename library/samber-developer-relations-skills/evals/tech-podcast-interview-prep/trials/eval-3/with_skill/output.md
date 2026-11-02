Using the tech-podcast-interview-prep skill (and its prep-brief-template / message-spine step) to turn your paragraph into messages.

Your plan has two problems the skill flags by name. "Five, one per feature" is the exact anti-pattern in its bad-brief checklist: *"Messages that are product features instead of claims about the listener's world."* And your paragraph itself is AAA-shaped — Rust, and mTLS, and Apache 2.0, and stars, and "teams love it" — a pile of facts with no tension, which is what unprepared guests produce. Separately: Microservice Minutes is 25 minutes, video, two co-hosts. That's under 30 minutes, which caps you at **two** messages, not five — a third steals airtime from the first two, and retention on video is worst in the opening minutes, so every message has to earn its seconds.

Here's the ABT spine and the two messages, with your raw facts redistributed to where they actually belong.

## Spine (ABT)

> "Platform teams reach for a service mesh because they need mTLS between every service, and every mesh on the market makes them either hand-roll a cert pipeline or ship with a security gap while they get around to it, but Corvid Mesh's Rust core issues and rotates certs itself with zero config, therefore a platform engineer gets mTLS across the fleet without a quarter-long PKI project.

## Messages

1. **Claim:** Turning on mutual TLS between services is normally a PKI project, not a config flag.
   **Evidence:** [gap — needs a real number: time-to-first-encrypted-hop on a fresh cluster, or lines of cert-manager/YAML config a typical mesh needs vs. zero for yours. Don't say "it's faster," the skill's own rule — pick a number you can say live and defend if a co-host pushes on it.]
   **So-what:** A platform engineer can put mTLS on this sprint, not next quarter's roadmap.

2. **Claim:** Most service-mesh sidecar overhead is a memory/GC tax, not fundamental complexity.
   **Evidence:** [gap — needs a real number: sidecar memory footprint in MB, or added p99 latency per hop in ms, ideally against a named comparison point (Envoy/Istio/Linkerd) since platform engineers will already have that reference in their head.]
   **So-what:** The mesh doesn't become the thing on-call has to watch.

Fill those two brackets before this is usable on air — they're the load-bearing part of each message, and the skill's own bad-brief list flags "evidence the user cannot source live" as the thing that gets a guest caught out mid-answer.

## Where the rest of your paragraph goes

| From your paragraph | Where it actually lands | Why |
|---|---|---|
| "Written in Rust" | Folded into message 2 as the *reason* for the low-overhead claim, not a standalone message | A language choice isn't a claim about the listener's world until it has a consequence attached |
| "4,200 stars" | The one **liftable sound bite**: *"We build Corvid Mesh, an open-source service mesh with mTLS on by default — it's sitting at 4,200 stars on GitHub."* | Names project + category + a spoken number — exactly the liftable-bite shape, and it's the sentence that gets machine-cited later |
| "Open source under Apache 2.0" | Your disclosure line, plus pre-load it as a hard question ("why Apache 2.0 and not AGPL/MIT") | Licensing is one of the standing hard-question classes this skill tracks — better answered once, deliberately, than improvised |
| "Teams love it" | Cut | Unfalsifiable, no number, fails the so-what test outright — it's decoration, and a 25-minute co-hosted show has no airtime to spend on decoration |

Depth calibration note, since the audience is platform engineers: anchor both messages in trade-offs and what breaks at scale (their evaluation lens), not the market-size/adoption framing — save the stars number for the sound bite, not the argument.

To keep building the rest of the brief (opening answer, story bank, hard-question table, disclosure wording, recording-day card) I still need: what the host actually booked you for in their words, whether you're speaking as Corvid Mesh's maintainer/founder or an employee (changes the disclosure line), and anything off-limits — pricing, funding, unnamed users of the 4,200-star count.