Read the skill and its three references (metric catalog, survey instruments, report template) plus the absence-factor script in full. This skill runs an interview before writing a report, but you've given me enough to build the framework and a usable draft now — I'm flagging the handful of inputs still missing rather than inventing them. One thing surfaced by the skill's own rules before the report itself: **what Ines told you doesn't belong in the board document verbatim.** The skill's privacy gate says aggregate anything person-level and never publish person-level data — that's written for survey respondents, but it applies even harder to a co-maintainer's private disclosure. Below, her signal is translated into a structural metric (contributor absence factor / bus factor) and an action, not quoted. Have the real conversation with her separately, before Friday, not through the board deck.

Also: this skill's own rule (SKILL.md, "Efficiency starves sentiment") says exactly this case — a maintainer showing burnout signals — is when you promote sentiment to the top of the sheet even though it's normally last. That's reflected below.

Two things need a number pulled from your own tools before this goes to the board — marked ⚠️ inline. Everything else is ready to present.

---

# Community health — Brambleweave — Q3 2026

## Primary outcome

**(SPACES: Support.)** Members answer each other's usage questions in Discord and share code-maintenance load through PRs and review, so Sam and Ines's maintainer hours scale sub-linearly with adoption — not one-to-one with it. Every metric below should plausibly move when that does.

## Metric sheet

| Metric | Pillar | Definition / formula | Source | Baseline | Threshold (origin) | Owner | Action if breached |
|---|---|---|---|---|---|---|---|
| Maintainer sustainability signal | Sentiment | Private, direct check-in with both maintainers on workload vs. capacity, energy, and any intent to step back (CHAOSS Project Burnout question areas). Not a survey — the maintainer group is two people, too small for Likert scoring. | Private conversation between Sam and Ines | None — this quarter's finding is the trigger, not a baseline read | Any maintainer expressing serious intent to step back = act immediately, don't wait for the next quarterly cycle (self-set) | Sam | Have the conversation this week; identify one concrete relief (delegated task, second reviewer, planned time off) with Ines naming what would actually help |
| Median time to first human response (Discord) | Responsiveness | Question post → first non-bot human reply | Discord export / bot log, bots excluded | Baselining — first formal pull | < 24h "healthy" / > 72h "act now" (unsourced practitioner folklore — replace with trailing median after 3 quarters) | Ines or Sam, whoever triages | Recruit/rotate answer duty across timezones; pin a "how to ask" note in Discord |
| PR / change-request closure ratio | Responsiveness | Closed (merged + rejected) ÷ opened, same window | GitHub | Baselining — have merged (23), ⚠️ need opened count for the quarter | Ratio persistently < 1 = backlog outrunning the team (this catalog's own interpretive reading, not published). Reference point for first response specifically: VMware's internal guideline, quoted in CHAOSS's starter model, is "every PR gets a human response within two business days" — one company's rule, not a standard | Sam | Triage backlog explicitly; consider a second approver role |
| Active participants & message volume | Activity | Distinct non-bot posters in the period; total messages | Discord analytics | This quarter: 61 posters, 1,140 msgs/mo. Prior period backed out from the stated +40%: ≈814 msgs/mo. Poster count has no prior read. | None yet — 2 reads isn't the 3-period minimum for a real threshold. Note only: confirm the +40% isn't a single-event burst before calling it a trend | Sam | None yet; check for a release/launch/HN mention that quarter before presenting growth as trend |
| Non-maintainer share of Discord answers | Activity | Answers not written by Sam or Ines ÷ total answers | Discord export + staff flag | Baselining — not currently tracked | Falling share vs. its own future baseline = maintainers still the bottleneck (self-set) | Ines/Sam | Publicly credit top peer-answerers; deliberately wait before answering first once someone else has |
| Contributor absence factor | Contributor funnel | Smallest number of people producing 50% of commits, trailing 12 months | `git log`, via this skill's own script (see below) | ⚠️ Not yet run | 1 = single point of failure (published reading: "a lower factor indicates higher dependency on fewer contributors") | Sam | If 1–2: open the review/merge rung to the next most active contributors; start a co-maintainer search |
| First-time contributor second-PR rate (90 days) | Contributor funnel | Share of first-time PR authors this quarter who submit a second PR within 90 days | GitHub | Baselining — break the 23 merged PRs down by distinct author, first-time vs. repeat | If under ~30 events, report as a dated list, not a percentage (small-N floor) | Sam | If low: check whether slow first-PR review is the blocker — ties back to the responsiveness row above |

## This period's reading — Q3 2026

| Metric | This period | Baseline | Direction | Note |
|---|---|---|---|---|
| Maintainer sustainability signal | 1 maintainer (Ines) reporting dread / considering stepping back | none | ⚠️ new | High-confidence, single direct disclosure — treat as urgent, not statistical |
| Median time to first response (Discord) | not yet pulled | — | — | Pull before Friday if possible; else mark "baselining" in the deck |
| PR closure ratio | 23 merged; opened count missing | — | — | Pull opened-PR count from GitHub before Friday |
| Active participants / messages | 61 posters; 1,140 msgs/mo | ≈814 msgs/mo (derived) | up 40% | Confirm no single event drove it — label as burst or trend accordingly |
| Non-maintainer answer share | not yet pulled | — | — | Start counting this quarter even if this quarter's number is late |
| Contributor absence factor | not yet run | — | — | Run script below before Friday |
| First-time contributor return rate | not yet computed | — | — | Needs author breakdown of the 23 merged PRs |

Run this against your own clone to fill the absence-factor row (bots excluded by default):

```
bash scripts/contributor-absence-factor.sh -r /path/to/brambleweave -s "12 months ago"
```

Given a 2-person-led framework, expect this to come back 1 or 2 — confirm the exact number and who's included before the board sees it, since that number, not the Discord growth, is the one that actually tells them whether this quarter's activity is sustainable.

## Findings

1. **Growth is real on the numbers you have, but not yet confirmed as a trend.** Evidence: messages up ~40% (≈814 → 1,140/mo), 61 distinct posters, 23 merged PRs. Confidence: medium — this is one comparison point, not a 3-period baseline, and nothing yet rules out a single release or link-share driving the spike. State it to the board as "this quarter's numbers, with one comparison point" rather than "an established trend."
2. **The community's growth metrics cannot see the risk that actually threatens the project.** Evidence: Ines's direct statement that she's dreading the repo and considering stepping back. Confidence: high as a signal (first-hand, unambiguous), but n=1 — the response is a private conversation and a structural fix, not a chart. This is exactly the case this framework calls out: a community can post record numbers the same quarter its maintainers decide to quit.
3. **Whether the growth is sustainable or is quietly increasing Sam and Ines's load is currently unmeasured.** The contributor absence factor and non-maintainer answer share — the two metrics that would answer this — haven't been pulled yet. Treat this as the single highest-priority gap to close before Friday, not a finding yet.

## Actions

| Action | Owner | By when | Metric it should move |
|---|---|---|---|
| Private conversation with Ines about workload and what relief would actually help | Sam | Before Friday | Maintainer sustainability signal |
| Run the absence-factor script against the Brambleweave repo | Sam | Before Friday | Contributor absence factor |
| Pull opened-PR count and Discord first-response sample for the quarter | Sam | Before Friday | PR closure ratio, time to first response |
| Decide together what to ask the board for — a co-maintainer search, contractor budget, or explicit permission to slow the pace | Sam & Ines | Before Friday | Contributor absence factor (structurally, not just for this report) |
| Start counting non-maintainer answer share and first-time-contributor returns going forward, even informally | Sam | This month | Non-maintainer answer share, second-PR rate |

## Watch list

- +40% message growth not yet confirmed as trend vs. burst — check for a release, blog post or HN/Reddit mention this quarter.
- Five of seven metrics are still "baselining" — this quarter is read 1 or 2 of what the framework needs 3 of before it can set a real threshold.
- No community-wide sentiment instrument exists yet beyond the maintainer check-in. Consider a two-question quarterly pulse to the wider Discord (recommendability + open text) starting next quarter — response rate will likely be low at this size, report it as a count with dates, not a percentage, until it isn't.
- Don't publish a per-member message leaderboard or attribute the sustainability finding to Ines by name anywhere the board can see it.

## Next review

Next quarterly roll-up to the board, plus a lighter monthly check between the two of you on the responsiveness and sentiment rows only — full 7-metric sheet re-read quarterly, given the team's size. Re-check first: whether the +40% held or reverted, whether the absence factor moved, and whether Ines's situation changed.

---

**One framing note for Friday:** don't lead the board with the growth numbers and bury the risk — lead with the honest version: numbers are genuinely good this quarter, one structural risk (maintainer capacity / bus factor) needs board attention now, here's the specific ask. That's a stronger, more credible story than a clean dashboard, and it's the version that gets you help instead of just applause.