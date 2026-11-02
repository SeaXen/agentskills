## hexpath — don't pull it

Skip the pull. The skill's exit rule is explicit: end a sponsorship only for a dependency that's gone, a dormant project, a changed mandate, or a policy breach — **"never for a disagreement over a technical decision — that is exactly the influence the policy promised not to buy."**

A maintainer merging a change and declining to revert it is that maintainer running their own project. It isn't a breach of anything; it's the normal outcome of not having bought roadmap or priority control in the first place. Pulling $9k right after they said no reads as exactly one thing to anyone who notices: *we pay, so you do what we say*. That story costs more than $9k to a company whose developer audience is watching how it treats maintainers — it's the skill's named failure mode, "asking for influence... the fastest way to convert a trust asset into a story about a company buying open-source projects."

Separate the two problems:
- **The broken build** is an engineering problem. Pin to the last good version, patch around the change, or fork — solve it the way you'd solve it with an unsponsored dependency, because that's what it structurally is.
- **The sponsorship** is a relationship decision. If this incident changes your read of hexpath's fragility or relationship value (e.g., a maintainer who won't work with downstream consumers on breaking changes), that's a legitimate input to *next year's* re-scoring — not a reason to cut mid-cycle.

If leadership overrules this and wants it pulled anyway, say so plainly when you do it: tell the maintainer before it lapses, give the real reason, don't dress it as budget timing. A sponsorship "silently dropped at budget close does more relationship damage than one that was never started" — and a dropped-for-a-technical-disagreement sponsorship is worse, because it's discoverable and it confirms the exact fear every maintainer has about corporate money.

## dustmote — end it, but not quietly

Ending it is correct. 26 months with no commits is well past the dormancy line — the skill's own scorecard puts anything with a maintained score of 0–3 at "likely dormant, money changes nothing," and "sponsoring a dead project" is called out by name as a failure mode. This is one of the four valid, stated reasons to exit a sponsorship ("the project is dormant").

What's wrong is the "keep it quiet" part. The rule: **"Tell a maintainer before a sponsorship ends, with a reason and a date. A silent cancellation is remembered far longer than the money was."** Letting it lapse unannounced doesn't avoid an awkward conversation — it just moves the awkward moment to whenever the maintainer notices the payments stopped, with no context attached, which reads worse than a clean message would.

Send something short before you cancel:

> Hi — we've been sponsoring dustmote at $200/mo for the past two years. We haven't seen activity on the repo in a while, so we're planning to end the sponsorship as of [date]. If that's inaccurate, or if you're maintaining it elsewhere, let us know and we'll keep it going. Thanks for the work over the years.

That's a two-minute email, not a review. Send it, then end the sponsorship on the date you gave.

## The other four — decide now, don't defer

No. "We don't have time, let them run" is the one thing the skill explicitly disallows at this point in the cycle: the year-one pass threshold requires **"a renewal decision was made for every target before budget close"**, and separately, **"put every sponsorship's renewal decision before the budget close date, not after; a lapse caused by internal timing reads to the maintainer as a withdrawal."** Deferring by default isn't neutral — from the maintainer's side, a sponsorship that rolls over on autopilot and one that quietly gets forgotten look identical until the money stops.

You don't need a full re-scoring pass (Step 5's exposure/fragility/audience-fit/relationship-value rubric) to clear this bar — that's for building or re-ranking a shortlist, not for a routine renewal. A fast-path renewal is four checks per sponsorship, each answerable in a couple of minutes:

1. Still a real dependency? (nothing removed from the stack)
2. Still active? (no 18+ month dormancy)
3. Any policy breach raised by the sponsee? (no)
4. Mandate unchanged?

If all four are clean, that's a real, explicit "renewed, unchanged" decision — not a default. Record it with today's date next to each of the four. That's the whole task; budget maybe fifteen minutes total, not a strategic review.

## Dependency analysis — re-verify, don't treat last year's list as current

Re-run it. The skill is direct on this: **"Re-run discovery annually. Dependency graphs move, maintainers hand over projects, and funding destinations go stale; last year's verified list is this year's unverified list."**

You don't need to rebuild the shortlist from scratch — the two things that specifically rot are funding destinations (pages 404, maintainers leave platforms) and health signals (a healthy project a year ago can be dormant now, or vice versa). Re-pulling the dependency graph itself is cheap ("near-zero once the resolver runs"), so there's no real cost to doing it in full rather than spot-checking:

- Re-resolve the dependency tree from your current lockfile/SBOM.
- Re-verify every funding link still resolves (a stale link fails silently — you keep paying into a dead destination and no one notices).
- Re-pull maintained/dormancy scores, since that's exactly the signal that would have flagged dustmote earlier instead of two years in.

Worth doing before you finalize the four-sponsorship renewal above, since a dormancy or destination check that only takes a few minutes per project could change one of those four answers.

---

If useful, I can run the full annual review (Step 9) against these six once the above decisions land — that's a short exercise: confirm each placement is still live, log the renewal dates and reasons in one place, and draft the annual report paragraph ("what we got wrong this year" should probably mention the dustmote lapse honestly). Say the word and I'll build it.