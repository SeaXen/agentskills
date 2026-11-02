Using the tech-podcast-interview-prep skill's Step 4 (story bank) to build this — with the audio-only, 60-minute format and the guaranteed "worst production incident" question factored in throughout.

Two things gate this before any of these get said on air (skill's own highest compliance-cost item: "customer names, incident detail and unpublished numbers, each cleared individually — and irreversible once spoken"). I've flagged both inline rather than blocking the bank on them.

---

## Story bank

| # | Story | Numbers (real, sourceable) | Five-second moment | What I got wrong | Answers which question |
|---|---|---|---|---|---|
| 1 | Thornbury Logistics — our biggest customer (4,000 seats) — migrated onto our platform; nightly batch window dropped from 6 hours to 40 minutes | 4,000 seats · 6h → 40min (~9x) | *[confirm/replace]* — suggested flip: "we scoped the migration assuming their data volume was the risk; the real bottleneck turned out to be our own scheduler serializing jobs that could run in parallel" — i.e. the fix wasn't about them, it was about us | *[you gave me the win, not the mistake — Dicks' method needs one; the scheduler angle above is a placeholder, swap for what actually went sideways]* | "biggest customer / proof at scale," "how do you handle enterprise migrations," "flagship case study" |
| 2 | Internal (unpublished) benchmark: we beat our main competitor by 3.2x | 3.2x, internal, not yet published | "the moment we didn't believe our own number and reran the whole benchmark three times before trusting it" | *[confirm/replace]* — e.g. a workload you expected to lose on and didn't design the first test to catch | "how do you compare to [competitor]," "why switch," "prove it" |
| 3 | Our own staging cluster ate 2TB of event data over a weekend | 2TB, ~48–60hr window, zero pages the whole time | realizing Monday morning that nothing had alerted for two straight days — the flip from "we have alerting" to "we have alerting for *production only*" | staging treated as non-critical: no on-call coverage, no alert parity with prod | **the guaranteed question** ("worst thing in production"), "biggest mistake," "how do you handle incidents," "what changed after" |

Everything marked `[confirm/replace]` is a placeholder shape, not a fact — fill it with what actually happened before this goes near a card. A story with no real mistake in it gets cut in the edit anyway (per the skill's own bad-brief checklist).

---

## ⚠️ Flag 1 — Story 1, the customer name

Thornbury Logistics is named, and they're your biggest account. Two separate risks, not one:

- **Consent** — an unnamed-customer rule is the default until you say otherwise. Confirm Thornbury's comms/legal side is fine with being named on a public recording, not just that your side is.
- **Revenue-concentration signal** — "our biggest customer, 4,000 seats" is the kind of detail a competitor or a Thornbury competitor can do something with. Decide if the seat count is worth cutting even if the name is cleared.

Safe fallback if you don't get sign-off in time: "a 4,000-seat logistics customer" — the batch-window number still lands without the name.

## ⚠️ Flag 2 — Story 2, the unpublished benchmark

This skill's own hard rule: *"Never claim an unreleased capability, an unapproved customer name, or an unpublished benchmark. The recording outlives the embargo."* A 3.2x figure nobody can go verify is exactly that.

Two ways to keep this story without breaking the rule:

- **Publish it before recording day.** Turns the episode into a promotion hook too — link the post in the show notes (Step 12's evergreen play).
- **Speak directionally instead of citing the multiplier**: "meaningfully faster in our own testing — once we publish the methodology I'll have an exact number for you." Honest, still a story, doesn't overclaim.

Don't say "3.2x" on air until one of those two is true.

---

## The guaranteed question: "worst thing that's happened to you in production"

Story 3 is the answer — but it was staging, not production, and that gap matters more than it costs you. Don't let it get told as if it were prod; that's a fact-check waiting to happen. Told straight, the honest version is the *stronger* answer anyway: it's proof the safety net worked.

**ABC skeleton** (concession before the bridge — this is a self-inflicted-failure question, not an ordinary one):

> **Acknowledge/concede first, real units:** "It wasn't actually production — closest we've come was staging. Our own staging cluster ate 2TB of event data over a weekend, and the reason it's embarrassing isn't the data, it's that nothing paged anyone for two straight days, because our alerting only covered prod."
> **Bridge:** "That's the exact gap that got closed afterward — alert parity between staging and prod isn't optional here anymore, and it's the reason [tie to whichever message this show's spine ends up carrying]."

**Open loop, since you know this question is coming**: mention early in the episode, unresolved — *"there's a data-loss story I'll come back to"* — then land the full version when the host asks their standard question. Costs nothing to plant, and it's the one arc device that survives the host controlling the running order.

---

## One gap to flag

The skill's own default is 5-8 stories; you've given me 3. That's enough to survive the episode but not enough to avoid reusing the same story for two different questions later in the same conversation (reads as a canned pitch). Worth 20 minutes before the recording pulling 2-3 more from the same shape as story 1 — another migration, a scaling win, an origin-story mistake — rather than improvising a fourth one live.