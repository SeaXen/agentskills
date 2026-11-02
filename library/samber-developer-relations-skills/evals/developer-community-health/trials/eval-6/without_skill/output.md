# Quarrystone Slack Community — Monthly Health Report

**Reporting period:** [Month Year] · **Prepared for:** VP review · **Community:** Private Slack Connect, 41 customer accounts / 187 members

---

## 1. Headline metrics

| Metric | Value | Status | Note |
|---|---|---|---|
| Monthly Active Users (MAU%) | **18.2%** (34 of 187 posted) | 🟠 | Below typical healthy-community range (25–35% for a paid customer Slack) |
| NPS | **+33** (n=6, last quarterly survey) | 🟢 score / 🔴 confidence | Score is solid for B2B software (industry norm ~30–40), but n=6 is too small to trust as a trend signal |
| Message growth (MoM) | **Not available this cycle** | ⚠️ | No prior-month message count on hand — see Data Gaps below |

**One-line summary for the VP:** engagement participation is low relative to headcount, satisfaction among the few who responded is good, and we can't yet report a growth trend because the baseline data hasn't been captured.

---

## 2. MAU% — detail

- 34 / 187 individual members posted at least once = **18.2%**.
- Denominator caveat: 187 is *people*, not *accounts*. A VP-relevant secondary cut is **account-level reach** — how many of the 41 customer accounts had at least one poster. That number isn't in hand yet; pull it from Slack member-to-account mapping and add it next cycle. Account-level reach is usually the more actionable number for a VP (it flags *which accounts* have gone quiet, not just how many individuals are quiet).
- Benchmark: Slack communities for B2B tools typically run 20–35% monthly posting rate among all invited members. 18.2% sits at the low edge — worth a comment in the report, not yet a red flag on its own.

## 3. NPS — detail

- Last survey: **+33**, from **6 responses**.
- Response rate context: 6/187 members = 3.2%; if the survey targets one contact per account, 6/41 accounts = 14.6%. Confirm which denominator applies before presenting the rate to the VP — the story is very different (3% vs 15%).
- **Confidence caveat to state explicitly in the report:** n=6 is not statistically reliable. A single detractor or promoter flips the score by ~17–33 points at this sample size. Present +33 as "directional, low-confidence" rather than a KPI to trend month over month.
- Recommendation: don't report NPS *monthly* off this sample — keep it quarterly (as planned) but fix the response-count problem before the next cycle (see Section 5).

## 4. Message growth — data gap

Can't compute this without a comparison point. To close this section next cycle, need one of:
- Total messages sent in the community this month vs. last month (Slack analytics export, or admin API `conversations.history` counts), **or**
- At minimum, active-poster count for the prior 2–3 months, so MAU% itself becomes a trend line even before message-volume data is wired up.

Recommend the VP report carry a placeholder row until this is instrumented, rather than skip the metric silently — flags it as "known gap, being fixed" instead of "forgotten."

## 5. Quarterly NPS survey — planning notes for the next cycle

Current state: 6 responses, +33. Two problems to fix before the next send, not after:

- **Response count is the real risk, not the score.** Target at least 15–20 responses (roughly triples current n) before treating quarter-over-quarter NPS movement as meaningful.
- Tactics to raise response count:
  - Send from a named person (CS lead or founder), not a bot/generic sender — response rates roughly double with a human sender in B2B contexts.
  - Two reminders (day 3, day 7), not one-and-done.
  - Post the survey link directly in the Slack channel in addition to email/in-app — Slack Connect members are already there, lowest-friction channel.
  - Keep it to the single 0–10 NPS question + one optional open-text "why" — anything longer suppresses completion.
  - Consider a light incentive (swag, credit) only if response count doesn't improve after one cycle of the above — don't reach for incentives first.
- **Segment the next result by account**, not just individually — a +33 blended score can hide 3 detractor accounts sitting on a renewal decision. With 41 accounts, this is cheap to do and far more actionable for the VP than the topline number.

---

## 6. Recommended monthly report template (going forward)

Reuse this structure every month so the VP sees a consistent format and a growing trend line:

| Month | Members | Active Posters | MAU% | Accounts Reached | Messages | Msg Growth MoM | NPS (quarterly only) |
|---|---|---|---|---|---|---|---|
| [This month] | 187 | 34 | 18.2% | TBD | TBD | TBD | +33 (n=6, [survey date]) |

Fill "TBD" cells once account-level reach and message-count exports are pulled — flagged above as the two concrete follow-ups before next month's report.