# GitHub Discussions — 90-Day Measurement Plan

## Stated targets

- 2,000 members by day 90.
- Never-posted share below 40%, down from ~80% in beta.
- Single readout at end of quarter.

Before locking these as the OKR, four gaps need fixing — they'd otherwise produce a number that looks fine (or fails) for reasons that have nothing to do with community health.

## ⚠️ Fix before launch

**1. GitHub Discussions has no "member" concept — define the proxy now, not at day 90.**
Unlike Discord/Slack, there's no join action and no membership list. The only things GitHub's API actually gives you:
- Distinct accounts that authored a discussion or comment.
- Distinct accounts that left a reaction (👍, ❤️, etc.) without commenting.
- Repo watchers/stargazers — a much blunter number, tied to the whole repo, not Discussions.
- Repo traffic "unique visitors" — admin-only, 14-day rolling window, not separable from other repo traffic, can't be backfilled once the window rolls.

Recommended definition, because it's the only one both computable via API and internally consistent with the lurker metric: **member = any unique GitHub account with at least one detectable footprint in Discussions (started a discussion, commented, or reacted).** Log this in writing before launch — if it's decided post hoc, the day-90 number can be reverse-engineered to hit whichever definition looks best.

This also means true silent readers (no GitHub account, or an account that never even reacts) are invisible to both targets. Track repo traffic/watchers as a **secondary sanity-check number**, not the headline one, so nobody mistakes "2,000 members" for "2,000 people found this useful."

**2. The two targets are mechanically coupled, not independent.**
Never-posted share = never-posted accounts ÷ total members. A brand-new member hasn't had time to post yet, so every new joiner is a lurker at the instant they join. Consequences:
- A late-quarter growth push (e.g., an HN/Reddit spike in week 12) inflates the member count right when you also measure participation — the lurker ratio gets *worse* purely from timing, with zero change in actual behavior.
- Conversely, slow/no growth after week 6 makes the ratio look artificially good, because the denominator is stale, mature, self-selected early adopters.

Fix: pace growth (track a weekly target curve, not just a day-90 cliff) and report the lurker ratio two ways — see metrics below.

**3. One check-in at day 90 means no early warning and no way to course-correct.**
If week 4 shows the ratio moving the wrong way, you want to know at week 4, not week 13. This doesn't have to change what's reported to the VP — it changes what's tracked internally.

**4. The beta 80% baseline probably isn't comparable.**
Beta was a small, invited, hand-picked group evaluating a product pre-release. The public Discussions audience will skew toward people who found the repo via docs/search/social with far more casual intent. Expect the "natural" floor to differ from beta for reasons that have nothing to do with what you build into the launch. Use beta as directional context, not a strict baseline.

## Metric definitions

| Metric | Definition | Why this shape |
|---|---|---|
| **Members (cumulative)** | Distinct accounts with ≥1 discussion, comment, or reaction, all-time | Only membership proxy the API supports |
| **Never-posted share (headline)** | Members with 0 discussions/comments authored ÷ total members, at day 90 | Matches what the VP asked for, directly comparable |
| **Never-posted share (tenure-adjusted)** | Same, restricted to members who joined ≥30 days before the measurement date | Removes the "just joined, hasn't had a chance" bias |
| **Time-to-first-post** | Days between a member's first footprint and their first authored post (discussions/comments only) | The actual lever the team controls via onboarding, not an artifact of measurement timing |
| **Weekly active posters** | Distinct accounts authoring a discussion/comment in a trailing 7-day window | Catches decay a cumulative stock number hides |
| **Reactor-only accounts** | Members who reacted but never authored | Splits "true silent" from "engaged but not writing" — useful when deciding what to fix |

Report the headline and tenure-adjusted lurker numbers side by side every time. A large gap between them is itself a signal: it means growth is outrunning the community's ability to convert readers into posters, or growth is back-loaded.

## Cadence

- **Weekly (internal, ~15 min):** pull the six metrics above via GitHub's GraphQL API, log to a running sheet. No reporting overhead, just a paper trail so day-90 isn't the first time anyone looks.
- **Day 30 / Day 60 (internal checkpoint):** compare actuals against the pacing curve. Flag only if trending off-track by >20%.
- **Day 90 (VP readout):** the single formal check-in she asked for, built from 13 weeks of already-collected data rather than a cold snapshot.

This satisfies "just check in at the end of the quarter" for her — the weekly pull is invisible overhead, not an extra process she has to sit through.

## Day-90 readout — what to hand the VP

1. Members (headline definition) vs. 2,000 target, plus the weekly growth curve (to show whether growth was smooth or back-loaded).
2. Never-posted share — headline number vs. 40% target, tenure-adjusted number next to it, and the gap between them explained in one line.
3. Time-to-first-post median/distribution — this is the number that predicts next quarter's lurker ratio, worth surfacing even though she didn't ask for it.
4. One paragraph on beta-vs-launch comparability, so an 80%→55% improvement isn't read as a shortfall against an apples-to-oranges 80%→40% ask if the tenure-adjusted number tells a better story.

## Guardrails worth tracking alongside the two headline numbers

- **First-reply time** to a new poster's first post (target: <24h). This is the single biggest lever for converting a one-time poster into a repeat one, and for pulling reactor-only accounts into posting.
- **Source of new members** (docs referral, social spike, search) if traceable via UTMs on links into the Discussions URL. Bulk low-intent traffic from a single spike will crater the lurker ratio and shouldn't be read as an engagement problem.
- **Repeat-poster rate**: of members who post once, % who post again within 30 days. Distinguishes "converted a lurker" from "got one drive-by comment."

Happy to build the weekly GraphQL pull as a small script if useful — it's a ~30-line job against `repository.discussions` and would remove the manual pull entirely.