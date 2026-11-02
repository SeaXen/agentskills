## Short answer

Split it. The early-access-for-$20+ part is a legitimate sponsorware pattern. The CVE-holdback part isn't — it fails this skill's own hard rule, and it's a bigger problem than goodwill. Fix that one piece and the rest works.

## What's fine

Binaries + docs site to $20+ sponsors a month early = **access-shape sponsorware**, textbook case. Sindre Sorhus and Caleb Porzio both run some version of "pay, get it first." It's convenience, not necessity — nobody's blocked from using harborctl v3 without paying, they just wait a month. That's an acceptable gate.

## What's not fine

**Holding back the two CVE patches.** The skill's sponsorware rule is explicit: "Gate convenience, never necessity. Tutorials, templates, early access and tooling are fair game. The core library, its security fixes, and the documentation needed to use it are not." Common failure modes list it again: "Gating the project itself... a paywall on the library, its security fixes or its documentation is a licence-adjacent betrayal of the users who got you here."

This isn't a goodwill nuance, it's a different category of harm than a delayed feature:

- Every non-sponsor running harborctl stays exploitable for a month on a **known, fixed** vulnerability, for a business reason, not a coordination reason. That's not "the fix isn't ready" — it's "the fix is ready and withheld."
- Once a CVE ID exists, there's usually a disclosure timeline attached (yours or a reporter's). Sitting on a public CVE while charging for the fix reads very differently from normal embargo practice — it's monetizing a security disclosure, which is the kind of thing that shows up in a "why does this maintainer hold CVE patches hostage" blog post, not a "great sponsorware launch" one.
- It also creates the worst possible incentive structure: you'd be *financially better off* the longer a known CVE stays unpatched for free users. That's the tell that this crossed from "reward design" into "we broke something to sell the fix."

Practically: if either CVE is remotely exploitable or has any real-world exposure, decouple them from the launch entirely — ship them the moment they're ready, on their own timeline, sponsor status irrelevant. If you want a security-flavored sponsor incentive, sell the thing the skill says you actually can sell here — named security triage/response-time commitments as a paid tier (`references/tier-ladder-examples.md`'s "Infrastructure" tier: 48h triage, named upgrade support) — not *withholding* a fix that already exists.

## The 250 → maybe 400 threshold

Also flagged directly: "Publish the release trigger up front and honour it. A threshold that keeps moving costs more goodwill than the revenue is worth." Deciding in advance that you might extend it if it's going well isn't a private contingency — sponsors will notice the goalpost moved, and "it was going well so we kept charging" is the least defensible reason to move it. Pick 250, publish it, hold it. If you want more runway, price for it up front (higher number, or a second published milestone: "250 opens v3 to everyone, 500 unlocks X"), don't leave the first one soft.

## Net

- Keep: $20+ sponsors get v3 binaries + docs a month early.
- Drop: bundling the two CVE patches into that gate. Ship them on their own schedule regardless of sponsorship.
- Keep, but commit: 250 sponsors opens v3 to everyone, published and final. If you want more, publish a second explicit tier now (e.g. 250 → public v3, 500 → some named next milestone) rather than deciding later.
- If you want a security-money angle, sell forward triage/response commitments as a paid tier, don't sell the absence of an existing fix.