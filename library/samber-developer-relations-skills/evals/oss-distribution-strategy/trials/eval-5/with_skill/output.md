Read the skill and its four reference files in full. Here's the distribution plan for fennelwick.

---

# Distribution plan — fennelwick

## Answering the actual question first

**Stars don't convert into usage because they were never the same funnel stage as usage.** 14,200 stars in eight months, flat weekly downloads (2,100), flat dependents (31), and a 3,400-member Discord with ~6 active people is one signal repeated four times: reach is working and conversion is broken. This is the Step 5 trigger this skill names explicitly — *"star velocity high, usage and retention flat → the announcement travelled and the install did not → that's an onboarding problem, move the budget to docs."*

Another newsletter round and chasing trending both spend more hours on the stage that's already saturated. Neither is refused because it's a bad channel in general — both are refused because they add impressions to a funnel that's already leaking everyone it reaches, downstream of impressions. Fix the leak, then decide if more reach is worth buying.

## Open questions this plan is built without

Confirm these — they each change a section below materially:

- **Ecosystem/registry** — not stated. Metadata mechanics (npm vs crates.io vs pkg.go.dev) differ; I've written the plan registry-agnostic.
- **Adopter type** — not stated. 31 dependents plus awesome-list/newsletter reach reads as individual-developer adoption; if company adoption is a real goal, trust signals and legibility move to the top and this becomes a different plan.
- **Maintainer hours/month** — not stated. Everything below is sequenced by priority, not costed against real capacity.
- **What "usage" should mean** — installs, retained weekly actives, or contributors are three different metrics with three different fixes.

## Position today (from what's given — treat the rest as unmeasured)

- **Stars**: 14,200 / 8 months. Reach and promotion signal, not a usage signal — 3 of 4 developers check star count before adopting, but the same research shows promotion drives stars as much as merit (Borges & Valente, *JSS* 2018). Read it as "the announcement travelled," nothing more.
- **Weekly downloads**: 2,100, flat all year. Flat *despite* the star surge is the finding — not the 2,100 itself.
- **Registry dependents**: 31, flat all year. No structural/integration growth either — nobody is building on top of it, which the star growth would predict if it were converting.
- **Discord**: 3,400 members / ~6 active. A vanity number on a high-recurring-cost channel. This is corroborating evidence, not a separate problem: attention converts to a low-friction action (join, star) far more easily than to sustained use.
- **Awesome lists ("a bunch")** and **2 newsletter mentions**: already-spent creator-seeding and curated-list capital — audit before spending more, don't assume it's still accurate.
- **Not yet known**: registry metadata completeness, days since last release / longest gap in the last year, actual referral sources for the 14,200 stars, whether any awesome-list links or newsletter mentions still point at a current install command.

## Diagnosis, stated plainly

This sits partly outside this skill's boundary — activation and onboarding belong to a different practice, not distribution — but it's the highest-leverage move available and this skill is explicit that a plan should say so rather than stay silent about it (Step 5's own trigger table). The distribution-adjacent slice of that fix — README first screen, working install command, "last published" liveness — is in scope below. Time-to-first-successful-use, quickstart UX, and empty-state/first-run experience are not; hand those to onboarding work once this plan's foundation ring closes.

## Adopter

Treated as **individual adoption** by default, given the channel mix already in play (stars, awesome lists, newsletters are all individual-adoption surfaces). Confirm before running stage 2 — a company-adoption goal reorders trust signals and downstream packaging to the top and this plan does not currently include either.

## Foundation ring (weeks 1–4, before anything else)

Run the audit this skill requires before proposing new channels — none of this has been measured yet, so it's the first hour of work, not a later item:

- **Registry metadata**: description (is it in the problem's vocabulary, or fennelwick's own invented terms — a likely bounce cause if a stranger lands and doesn't recognize the problem being solved), keyword slots, categories, license, links (docs, funding), rendered README first screen, version state.
- **Release stream**: days since last release, longest gap this year. Flat downloads for 12 straight months raises a specific hypothesis worth ruling out first — a stale "last published" field reads as abandoned even to an interested visitor, independent of everything else in this plan.
- **Every awesome-list entry**: link resolves, description current, points at the current name/install command, not an orphaned pre-rename URL.
- **Arrival sources**: pull the repo referrer panel *now* — it keeps only a short rolling window, so this baseline is unrecoverable if skipped. This is the only way to see whether any of the 14,200 stars' traffic sources ever reached the install step at all.

Expect the skill's own default finding here: a half-configured metadata page and two or three wrong listings. That's ~1 hour of fixing, done before the sequence below starts.

## Sequence

1. **Foundation** (above), weeks 1–4.
2. **Close the star→install→retain gap** — the actual priority, not a new channel. Concretely, in scope for this skill: confirm the install command in the README, in every awesome-list entry, and in both newsletter mentions still works against the current package name and version; rewrite the README's first screen to sell "try this in one command," not architecture. This is deliberately placed ahead of any new outward-facing channel, because spending on stage 3 before this closes just adds more people to the same leak.
3. **Active seeding**, only once downloads or dependents move off flat. Not before — it is this skill's most expensive recurring channel and the two mentions already spent haven't moved either number.

## Test ring (starts once foundation is closed, ends next quarter)

- **T1 — Metadata + README fix.** Signal: weekly downloads move off the 2,100 flatline. This is the test that answers the actual question — if fixing legibility and the install path doesn't move downloads, the leak is downstream of distribution entirely (onboarding, not discovery), and no further distribution spend should follow.
- **T2 — Dependency position.** If the ecosystem has an obvious high-fan-in hub project in this space, pitch one first-class integration or adapter. Signal: dependents count moves off 31. Dependency position is the one family that keeps paying with near-zero recurring cost once earned — worth testing precisely because everything else here is flat.

## Core channel

Not decided yet — deliberately. Nothing in the current data says which surface, if any, converts. Crowning one now would be picking a channel because it's already been tried (newsletters, Discord), not because it's shown a signal.

## Refused

- ❌ **Second newsletter round.** Reason: newsletters are the already-fed side of the funnel — flat downloads after 14,200 new stars is evidence the leak is downstream of impressions, not upstream of them. Reopens once downloads move off flat *and* there's a genuine new story (a version, a case study) to pitch on a calendar, not "another round" of the same pitch.
- ❌ **Chasing trending.** Reason: no published mechanism — GitHub's own events firehose gap broke third-party trending tools badly enough that OSSInsight withdrew its trending feature rather than publish numbers it no longer trusted. It's a byproduct, not a channel a maintainer can run.
- ❌ **Growing the Discord further.** Reason: 3,400/6 active is already oversized for what it returns, and it's a high-recurring-cost channel by family. Reopens only if the ~6 active members are worth interviewing first — they're the one group that *did* convert, and finding out why is more useful right now than acquiring more members who won't.

## Release rhythm

Unknown — get the actual cadence data before setting this. The rule holds regardless: commit to a maximum interval, never a minimum; ship notes on every release; security fixes out of band. If the last release is old, that alone is a plausible full explanation for a 12-month flat line, and it's a one-line fix compared to everything above it.

## Review sweep

Quarterly, starting after the foundation ring closes. Re-decide the test ring and core channel at that date — including whether the diagnosis above was right, based on whether T1 actually moved downloads.

## Threshold check

- Sourced (stale listings fixed before new channel work) — ⚠️ not yet run, first action item.
- Metadata 100% filled — ⚠️ unmeasured, blocked on ecosystem confirmation.
- Recurring cost ≤ 60% of capacity — ⚠️ unmeasured, blocked on hours/month.
- Every channel has owner/cost/signal/review date — ✅ for what's listed above; ❌ for anything added before capacity is confirmed.
- No harmful-decay channel without a scheduled sweep — ✅ by design in this draft (Discord and newsletters are explicitly not being expanded).

This plan is runnable for the foundation ring and T1 today. T2, the core-channel decision, and the release-rhythm section need the open questions above answered first.