Not dead — cadence broke, not content. Weekly log has zero slack: one bad month becomes a visible gap, and a visible gap reads as death. That's what happened at week 11.

## Do this now, before January

1. Post one short status note, anchor surface (wherever weekly posts lived). Say: not dead, ~30 PRs merged since April, contract work ate the writing time (not the maintenance), full write-up and restart in January.
2. Reply to both "is this dead" issues, link that note, close or leave open per your norm.
3. Point both at something checkable — commit log, closed-PR list, or a milestone page. Words alone don't fix "is this dead"; a link a skeptic can click does.

Costs under 20 minutes. Stops the bleeding without touching the January plan.

## January: the actual restart

One catch-up post, not a quiet resume:

- What shipped in the gap (pull highlights from the ~30 PRs — 3 to 5 real ones, not a count).
- What stalled (the newsletter itself) and why (contract work), stated once, no over-apologizing.
- What changes going forward (new cadence below).

Restarting at the old weekly frequency reproduces the same collapse. Don't.

## New cadence — sized to the worst month, not the best week

Weekly log failed because it has no relationship to actual output — it demands a post whether or not there's something to say. Replace it:

- **Backbone: release-anchored log.** Post when a release ships. No release, no post. Cadence follows work you're already doing, degrades gracefully instead of producing filler.
- **Ceiling: monthly roundup**, not weekly. One substantial post beats four thin ones, and you already have the raw material (merged PRs) — this is closer to a rollup than new writing.
- Budget the reply thread time too, not just drafting — usually the bigger cost.

If you don't know your real monthly hours for this, ballpark now: draft + review + replies, per post, times posts per month. If that's over ~10% of your time on sift, cut frequency further, not depth.

## Pause rule — write this down now, while nothing's on fire

Trigger: any outside contract or obligation expected to eat sift time for 2+ weeks.
Action: post a one-paragraph pause notice within 7 days of knowing that — reason, expected return, where releases stay visible meanwhile.

This is the actual fix. Last time, the pause was real but silent; the silence is what read as abandonment, not the pause itself. Announced gaps cost nothing.

## Charter

```markdown
# Build-in-public charter - sift

## Goal
Adoption confidence / contributor trust. (Assumed — confirm: is the real
priority contributors, sponsors, or just "stop looking dead to evaluators"?)

## Context
Solo maintainer. No co-founder, investor, or customer consent needed.

## Audience
Individual developers evaluating a log-parsing tool for their own use,
plus engineers who need to vouch for it inside a company (release
cadence and responsiveness matter more to that second group than any post).

## Rung
Rungs 1-2: shipping log, decisions. Rung 3 (failure/postmortem posts)
allowed when something breaks - don't force one.
Rung 4-5 excluded: no revenue involved, no operational-metrics dashboard
worth the standing obligation yet.

## Stop condition
N/A at rungs 1-2 - nothing here needs a stop test. If financial or
usage-metric disclosure is ever added, run Chen's four-condition test
first.

## Boundaries
No unfixed-vulnerability detail, ever (coordinated disclosure only).
No dates for unshipped features - direction only, following GitHub's
roadmap disclaimer pattern.
No named user data without consent.

## Cadence
Release spine (post per release) + monthly roundup. No fixed weekly slot.

## Surfaces
Anchor: existing blog/changelog. One amplifier max, wherever you
already read and post today - don't add a second platform this cycle.

## Support plan
State maintenance is part-time in README. Feature requests routed to a
public issue/discussion, not DMs.

## Measurement
Quarterly: contributor PRs, issue first-response time, adoption
signals (downloads, named deployments) - never stars. Reviewed each
quarter against the Goal line above.

## Pause rule
Any outside obligation expected to consume sift time for 2+ weeks
triggers a pause notice within 7 days: reason, expected return, where
work stays visible.
```

## Assumptions to correct

- Goal: guessed adoption/contributor trust. If it's sponsorship or a personal-credibility angle, the rung and measurement columns change.
- No revenue or sponsorship involved — if that's wrong, rungs 4-5 and the stop test come back into play.
- Solo maintainer, no one else's consent needed — confirm still true.

Next: send the two issue replies and the status note today — everything else waits for January.