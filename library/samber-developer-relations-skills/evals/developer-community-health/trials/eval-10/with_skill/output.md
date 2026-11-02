# Community health – Pallasite Slack – reading period: last full month

## Before the sheet: assumptions I made without an interview

This skill normally runs as an interview before it picks metrics. Since you asked for the finished deliverable directly, here's what I assumed — check these first, they change the sheet:

- **Community type:** chat-only (Slack). Pallasite's GitHub repo/contributor base is a separate surface, not covered here — flagged below.
- **Primary outcome:** not stated by leadership. I've defaulted to **support deflection** (peer/staff help with Pallasite without opening GitHub issues) as the working hypothesis, in SPACES vocabulary. This is the single biggest gap: get leadership to confirm or replace it before the next review, or every number below is answering a question nobody agreed to ask.
- **Baseline:** "roughly like this for 8 months" is a memory, not an export. I've used it as a self-set approximate baseline and flagged every cell that needs replacing with a real Slack pull.
- **Individual-adoption / open source**, not B2B — members join as themselves, not as company seats.

## Primary outcome (unconfirmed — validate with leadership)

Pallasite's Slack exists so users get peer support without filing GitHub issues, so the maintainers' time goes to code, not repeat Q&A.

## Metric sheet

| Metric | Pillar | Definition / formula | Source | Baseline | Threshold (origin) | Owner | Action if breached |
|---|---|---|---|---|---|---|---|
| Non-staff share of activity | Activity | non-staff messages ÷ total messages | Slack analytics/export, staff flag on the 2 team accounts | ~18% (self-set, from last month: 2/11) | < 30% "watch," < 15% "act now" (folklore, unsourced — replace after 3 real periods) | Community lead | Recruit/prompt non-staff answerers; staff stop being first responder |
| Active non-staff participants per period | Activity | distinct non-bot, non-staff identities posting or reacting | Slack analytics/export | 1 (self-set, last month) | < 3 for two consecutive months (self-set) | Community lead | Diagnose before acting — check for venue-move or dead-channel signal |
| Zero-reply rate on real (non-staff) questions | Responsiveness | question threads with 0 human reply ÷ total question threads | Slack export, bots excluded | Below the 30-event floor — report as a dated incident list, not a % | Any unanswered thread open > 2 business days (VMware/CHAOSS internal guideline, cited as one company's rule, not a standard) | Community lead | Answer within 2 business days; escalate if no one available |
| Median time to first human response | Responsiveness | question posted → first non-bot reply, median elapsed | Slack export | N/A — no data point exists yet, the only question on record is still unanswered | > 24h "watch," > 72h "act now" (folklore, unsourced) | Community lead | Add a second timezone-covering answerer |
| Return-poster rate within 90 days | Contributor funnel | first-time posters who post again ÷ first-time posters, per join cohort | Slack export | Baselining — 1 known poster so far, posted twice, still got no reply either time | To be set after 3 real cohorts (self-set) | Community lead | Review whether first-answer delay is the cause |
| Recommendability / lapsed-member pulse | Sentiment | "How likely to recommend this community?" NPS-style, promoters % − detractors %; plus a direct, private note to the one repeat-asker | Quarterly pulse survey + targeted outreach | Not yet run | N/A until first wave; report qualitatively below ~30 responses | Community lead | If low/negative: interview detractors before changing anything else |

6 metrics, all four pillars covered, under the 8-metric ceiling.

Deliberately excluded: **total member count (1,900).** It only goes up and would be the "Member count as the headline" failure mode — it says nothing about whether the community works, and putting it in the sheet invites leadership to read it as proof when the rest of the data says the opposite.

## Reading — last month, vs. approximate 8-month baseline

| Metric | This period | Baseline | Direction | Note |
|---|---|---|---|---|
| Non-staff share of activity | 18% (2/11) | ~same, per "roughly like this for 8 months" | flat | Below floor for reliable %, but the pattern repeats — see findings |
| Active non-staff participants | 1 | ~same | flat | Same person as prior months, by report |
| Zero-reply rate | 2 messages, 0 replies | Same pattern reported for 8 months | flat / bad | Below 30-event floor — treat as an incident, not a rate |
| Median time to first response | N/A (unanswered) | N/A | — | No successful response exists to measure yet |
| Return-poster rate | 1 person posted twice, 0 replies either time | Baselining | — | "Returning" here means they tried again despite silence, not that engagement is healthy |
| Recommendability | Not surveyed | Not surveyed | — | First wave not yet run |

## Findings

1. **The channel functions as a one-way broadcast, not a community.** Evidence: 9 of 11 messages last month came from the 2 staff members (82% staff share), consistent with an 8-month pattern. Confidence: medium — the 8-month figure is recalled, not exported; re-derive it from a real Slack pull before citing it externally.
2. **The one real ask got a complete non-response, twice.** Evidence: the same non-staff user posted 2 messages, 0 human replies to either. Confidence: high — directly reported, unambiguous. This is the most damaging single fact for a "prove the headcount" ask: it's the one moment someone actually tried to use the thing being defended, and nobody showed up.
3. **Non-staff activation against the member base is effectively zero**, not just "mostly lurkers." Evidence: 1 distinct non-staff participant out of 1,900 members (~0.05%) in the period. Nielsen's 90-9-1 baseline still expects roughly 1% to be highly active — this community isn't at the lurker-heavy end of normal, it's below the floor the model expects for *any* size. Confidence: high for the period, medium for "8 months" pending real history.

## Actions

| Action | Owner | By when | Metric it should move |
|---|---|---|---|
| Answer the outstanding question publicly, with an apology for the delay | Community lead | This week | Zero-reply rate |
| Privately reach the repeat-asker — ask what they needed and whether they'd try again (adapted lapsed-member instrument) | Community lead | This week | Sentiment, return-poster rate |
| Pull real month-by-month Slack export for the trailing period; check plan/retention limits before assuming 8 months is actually retrievable | Community lead | 2 weeks | Baseline column, all rows |
| Confirm the 9 "staff" messages are human, not a bot/integration cross-post | Community lead | 2 weeks | Non-staff share of activity |
| Get leadership to name the single primary outcome this Slack is meant to serve, before the next reading is presented as evidence | Community lead + leadership sponsor | Next review | Whole sheet — every metric here answers a guessed outcome until this happens |
| Decide, from the next 1–2 readings, whether to keep staffing it, change format, or fold it into GitHub Discussions (rides on the existing contributor base, near-zero standing cost) | Leadership | Next review | Primary outcome, activity |

## Watch list

- Every baseline above is self-set from memory, not a real export — do not present these externally until replaced.
- Confirm Slack plan: free-tier history typically caps at 90 days, which would make "8 months" partly unrecoverable. Start snapshotting monthly into your own store now regardless.
- Sentiment reads will likely land under 30, possibly under 5, responses — report as qualitative evidence with dates, not a percentage.
- GitHub-side signals (issues, PRs, contributors) for Pallasite itself are out of scope here. If the headcount also covers that work, pull it separately — the Slack being dead does not tell you whether the project is dead, and conflating the two would be as dishonest as inflating this dashboard with member count.

## Next review

2026-10-02 — quick check: was the outstanding question answered, did the repeat-asker respond to outreach.
2026-10-16 — full monthly reading against a real (exported, not recalled) baseline.

---

**The honest read, stated plainly:** on the numbers given, this Slack is not currently delivering peer support or any other outcome — it's two staff talking into a room of 1,900 lurkers, and the one person who tried to use it got ignored twice. A dashboard built to "prove" health from this data would have to lean on member count, which is exactly the failure mode this framework exists to avoid. What this sheet gives you instead is a real baseline, a fixable first miss (answer that question this week), and a decision point in 4 weeks: if non-staff activity and responsiveness move, you have a case for the headcount; if they don't, the defensible recommendation is to fold this into a lighter-weight surface rather than keep a dedicated seat on a room nobody uses.