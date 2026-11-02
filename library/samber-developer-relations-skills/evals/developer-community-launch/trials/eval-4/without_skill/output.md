# Quillstack User Forum — Launch Plan

## Date: confirmed, with one caveat

- Nov 4, 2026 is a Wednesday — fine as a slot, no conflict on your end.
- Nov 3, 2026 is the US midterm election. Nov 4 is the day after, when US news/social attention is saturated with election coverage. 60% of your installs are NA + APAC, so a meaningful chunk of the audience you're announcing to is distracted that exact week. Not a blocker, but flag it to marketing — ask whether shifting to Nov 11 costs them anything in the quarterly push, or whether they'd rather eat the reduced day-one reach.
- The bigger open question isn't the date, it's readiness: 7 weeks (Sept 18 → Nov 4) at 7 hrs/week is tight but workable *if* scoped to an existing platform, not a custom build. See below.

## The real risk isn't the date — it's coverage

Two structural gaps a launch date can't fix:

1. **Answerer bench is 2 people, not 24.** Of the 24 named invitees, only Priya and one other are people you'd actually trust to answer setup questions correctly. A 2-person bench is a single point of failure — one sick week and the forum goes visibly quiet, which reads worse than not having a forum at all.
2. **Timezone mismatch.** Both trusted answerers sit in Central Europe. 60% of installs are NA + APAC, whose business hours barely overlap Central European hours (NA) or don't overlap at all (APAC). Expect most questions from your two biggest install bases to sit many hours before a trusted answer shows up — which undermines the deflection goal directly, since a slow answer doesn't stop someone from also filing a ticket.

Neither is fixed by moving the date. Both are fixed by changing who you recruit and what exists on day one.

## Fix: recruit where the gap is, not just who you already know

The dozen duplicate questions per quarter are already being answered by users, in your repo, right now — that's your real answerer bench, and it's already sitting in the timezones you're short on.

- Before sending invites, pull the last two quarters of repo issues/discussions and identify who answered setup questions unprompted, more than once. That's evidence-based NA/APAC coverage, not a guess.
- Invite them as founding members or early moderators alongside the Central Europe 24. Offer something real — early roadmap access, a contributor badge, a direct line to Priya. It's the only lever that closes the timezone gap without adding headcount.
- Treat the 24 as members and seeders, not as the coverage plan.

## Platform: GitHub Discussions, not a new destination

Audience is technical, async-preferred, and already living in your repo, which is where the duplicate questions happen today. A separate Discourse/Slack/Discord instance adds a context-switch for both askers and the two answerers you can least afford to spread thin.

- Zero new infrastructure — fits inside Priya's 7 hrs/week.
- Google-indexed and searchable, which matters more than community feel here: deflection requires surfacing in search *before* someone files a ticket.
- Gate the issue template on it: "Setup question? Search Discussions first." That gate is the actual deflection mechanism — the forum only cuts tickets if it intercepts them before filing, not just by existing.

## Seed before announcing — don't launch empty

An empty forum on announcement day fails immediately.

- Mine the 40+ repeat questions from last quarter (especially the dozen duplicates), pre-write canonical Q&A threads for the top 10–15, authored by Priya, the other trusted answerer, and any newly recruited NA/APAC answerers.
- Pin a "Start Here" thread mapping symptoms/error messages to the right canonical thread.
- Soft-open to already-engaged repo users roughly 3 weeks before the public date (mid-October) to stress-test categories and surface gaps while it's low-stakes. Point the marketing push at a forum that already has depth, not a blank page.

## Structure — minimal, matched to a setup-support forum

- **Announcements** — Priya-only.
- **Setup & Getting Started** — the deflection target; canonical threads live here first.
- **Troubleshooting** — everything past initial setup.
- **General / Show & Tell** — optional, don't staff it at launch.

Skip anything past this. More categories than answerers means half the forum looks dead on day one.

## Measuring the actual goal

"Cut duplicate setup tickets in half in two quarters" needs a fixed baseline or it's unmeasurable at the retro.

- Baseline: turn "40+ repeat, a dozen duplicates" into an exact count over an exact date range before launch, so "half" has a denominator.
- Ongoing: tag new setup issues as "answered in Discussions" vs. net-new; compare quarterly against baseline.
- Leading indicator, check monthly rather than waiting for quarter-end: % of new Discussions questions answered within 24h. If that drops below ~75%, the timezone/bench gap is already costing the deflection goal — that's Priya's cue to escalate for more moderator hours, not a surprise at the two-quarter mark.

## Sequence

| When | What |
|---|---|
| Now – early Oct | Mine repo for NA/APAC answer-history candidates; invite them plus the Central Europe 24. Stand up Discussions categories. |
| Early–mid Oct | Seed canonical threads from the top 10–15 repeat questions. |
| Mid Oct (~3 wks pre-launch) | Soft-open to engaged repo users only; fix gaps. |
| Nov 4 (confirm election-week overlap with marketing) | Public announcement; issue-template gate goes live. |
| Ongoing | Priya's 7 hrs/week = triage + escalate anything unanswered past 24h + monthly canonical-thread refresh. |

## Bottom line

The date works on its own terms — the only real caveat is the US-election-week attention dip for a NA-heavy audience, worth one line to marketing, not a hard blocker. What actually determines whether you hit "half the duplicate tickets in two quarters" is fixing the answerer bench and timezone coverage before launch. Recruit from your repo's own answer history, seed the forum before anyone sees it, and gate the issue tracker into it. Launched as-is — 24 Central Europe invitees, no seeding — the forum most likely goes quiet during NA/APAC hours and the ticket number doesn't move.