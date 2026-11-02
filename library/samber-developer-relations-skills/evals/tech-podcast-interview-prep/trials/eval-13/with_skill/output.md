## Your angle

**Candidates on "observability at scale," checked against the show's own back catalogue:**

| # | Angle | Shape | Why it survives or dies |
|---|---|---|---|
| 1 | "Your observability stack is sized for average load, not incident load — and that's exactly backward" | contrarian thesis | **Survives.** Neither OTel episode nor the log-cost episode covered resilience of the observability layer itself. This is genuinely uncovered ground. |
| 2 | Practical rundown of how you redesigned tracing ingestion (sampling, load-shedding, backpressure) since April | practical how-we-do-it | **Weak, not dead.** Useful as a message inside angle 1, but alone it reads too close to "another OTel migration story" — the exact thread this show has already run twice. |
| 3 | Narrate the April Black Friday outage directly, findings and all | war story | **Removed.** The incident review is under NDA until January. Per the angle-selection rule, an incident still under embargo removes the war-story shape entirely rather than getting shortlisted and hedged around live. |
| 4 | "Cost control makes you fragile during incidents" (tie-in to the log-cost episode) | contrarian | **Discard.** Too close to an angle the show already ran — you'd be relitigating their own episode, not bringing something new. |

**Recommendation: Angle 1.**

It's the only angle that's (a) not already covered twice, (b) something only you can back with a real experience, and (c) tellable without touching a single fact from the NDA'd review. The trick is where you draw the line: you can say the outage happened, when, and what class of failure it was (your tracing backend buckled under your own peak-traffic day — that's your operational experience, not the vendor's confidential findings). You can't cite the vendor's name, the review's root-cause conclusions, remediation commitments made jointly with them, or any number that originated in that document. If you're not sure which side of that line a fact falls on, default to "it's not mine to say until January" — check with whoever signed the NDA before recording, not live on air.

**Spine (ABT), built on angle 1:**

> "We sized our tracing pipeline for normal traffic, and it worked fine for a year, but the exact day we needed it most — our highest-traffic day — was the day it fell over under its own load, therefore observability capacity has to be provisioned for your worst day, not your average one."

**If they ask about the outage directly, don't dodge — bridge (ABC, concession first):**

> "Yes — it was bad, and it happened on the one day we couldn't afford it. There's a formal review with our vendor that's still under NDA until January, so I can't get into the root-cause specifics or numbers from that yet. What I can tell you, because it's ours to say: the failure mode was completely generic — trace volume scales with the traffic you're trying to observe, so your observability system is under maximum load at the exact moment everything else is already stressed. That's the part every team running at scale should plan for, regardless of which vendor is involved."

That's a full, honest answer with a real concession in it — not a "no comment," which is the failure mode that actually costs trust on a technical audience.

**One sound bite to rehearse (passes the cold-read test, no vendor name, no NDA content):**

> "The day you need your tracing pipeline most is the day it's carrying the most load — most teams provision for the other 364 days."

**Sequencing note:** don't burn the full incident story now. Bank it — with the vendor named, the numbers, the actual root cause — for a return visit after January. These hosts have gone back to this topic three times in twelve episodes; a second appearance built entirely on "here's what we couldn't tell you last time" is a stronger booking than trying to squeeze it into this one under restriction.

To take this further into a full recording-day brief (messages, story bank, sound bites, hard-question table, opening answer), I'd need the show format basics: episode length, solo host or co-hosts, audio/video/live, and the audience level.