# Corbelline docs: AI visibility slide and measurement section

**I can't support "AI citations up 31%, on track for +40% next quarter" as written.** Three claims in it fail:

- **The 31% is not a citation count.** It measures chatgpt.com *referral visits*, meaning clicks. A citation is a mention in an answer, and most citations never produce a click. Calling referrals "citations" invites a challenge in the room.
- **The +40% has no basis.** It extrapolates from a single 5-day delta. A template change is a one-time step, not a growth rate, so nothing compounds into a quarterly trend.
- **The 140 Copilot citations have no baseline.** Without a prior week, they show neither growth nor decline.

Below is a slide your director can present safely, then the measurement section.

---

## Slide (Thursday)

**Title: Versioned titles shipped on all 900 docs pages. Early AI-referral signal is positive, not yet proven.**

| Signal | Result | Confidence |
|---|---|---|
| chatgpt.com referrals to /docs/ | **+31%** (5 days after vs 5 days before; [X] → [Y] sessions) | Early, unvalidated against normal variation |
| Copilot citations (Bing Webmaster AI report) | **140 this week** | Baseline set; no trend yet |
| Google AI surfaces | No AI-specific reporting exists in Search Console | Not measurable |

**What we do next**
1. Read the 4-week result on **[date]**, against a control and normal weekly variation.
2. Add a weekly fixed-prompt citation check to measure citations directly.
3. Set the Q1 target from the 4-week baseline, not from this 5-day delta.

**Speaker line:** "The first week is encouraging. We'll know in four weeks whether it's the template change or noise, and we'll set the target then."

If your director insists on a number, use "+31% chatgpt.com referrals, 5-day read". Put the window on the slide and don't add a forecast.

---

## Measurement section (quarterly report)

### 1. What we changed
On [ship date], we added the product version to the `<title>` and H1 of all ~900 pages under /docs/. The goal is that AI assistants can match version-specific questions to the correct page and cite it.

### 2. What we measure
We track three separate quantities, because they answer different questions.

| Metric | Definition | Source | Cadence |
|---|---|---|---|
| **AI referrals** | Sessions to /docs/ with referrer chatgpt.com, copilot.microsoft.com, perplexity.ai and similar | Web analytics | Daily, reported weekly |
| **Citations (Bing)** | Count of Corbelline URLs cited in Copilot answers | Bing Webmaster AI report | Weekly |
| **Citation rate (direct)** | Share of a fixed set of [40] version-specific doc questions where an assistant cites a Corbelline /docs/ page, and whether the cited version is correct | Manual or scripted weekly run in ChatGPT, Copilot and Perplexity | Weekly |

Referrals measure clicks and citations measure mentions. We do not add them together or call one by the other's name.

### 3. Current readings
- **chatgpt.com referrals:** +31% over the 5 days after the change versus the 5 days before ([X] → [Y] sessions).
- **Copilot citations:** 140 in the week of [date]. This is the first baseline, so there is no change figure.
- **Google:** Search Console has no AI-specific reporting, so we have no direct reading there.

### 4. Why these readings are provisional
- **Short window.** Five days is one weekday/weekend cycle, and we have not measured normal week-to-week variation in this series.
- **Small base.** If [X] is small, a +31% change can come from a handful of sessions. We report absolute counts beside every percentage.
- **No control group.** All 900 pages changed at once, so nothing on /docs/ remained unchanged to compare against.
- **Other causes are possible.** ChatGPT product or model changes, release-driven interest and seasonality can all move referrals.
- **Referrals are not citations.** Many answers cite a page without producing a click, and some referrals come from non-citation features.
- **Possible side effects.** Version strings lengthen titles and may be truncated in search results, and old-version pages may compete with current ones. We check Search Console clicks, impressions and average position on /docs/ for regressions.

### 5. How we will validate
1. **Establish noise.** Pull the previous 8 to 12 weeks of daily chatgpt.com referrals to /docs/. Compute the typical week-over-week swing. If +31% falls within it, the signal is not distinguishable from normal variation.
2. **Add a control.** Compare chatgpt.com referrals to a non-docs area untouched by the change (for example /blog/ or marketing pages) over the same windows. Report the docs change net of the control change.
3. **Compare matched windows.** Use whole weeks or matched weekdays, with a 4-week post-change window against the 4 weeks before.
4. **Track Copilot trend.** Record the weekly Bing citation count from this week onward, plus the prior weeks if the report offers them.
5. **Run the fixed-prompt check.** Run the same question set weekly and log which page is cited and whether the version is right. This is our only direct citation measurement across assistants.

### 6. Decision rule (set before the data arrives)
We call the change effective if, over the 4-week window:
- docs referrals from AI sources rise by more than the largest normal weekly swing found in step 1, **and**
- the net increase over the control area is positive, **and**
- Search Console shows no meaningful decline in organic clicks or position on /docs/.

If the criteria are not met, we report "no measurable effect". If organic metrics regress, we review the title format.

### 7. Targets
We do not state a Q1 growth target now. A single 5-day delta cannot support one. After the 4-week read we set the target from the measured baseline, with a range, and we state which of the three metrics it applies to.

### 8. Limitations
Assistant citation behavior changes without notice, and neither Bing nor Google exposes complete data. Bing's report covers Copilot only. We cannot see ChatGPT citations that produce no click. Direct prompt checks use a sample of questions, so they indicate a trend, not a population rate.

---

## Fill in before Thursday (about 30 minutes)
1. **Absolute counts** for the 31%: [X] and [Y].
2. **8 to 12 weeks of history** of chatgpt.com referrals to /docs/. This is the most important check, because it tells you whether 31% is unusual.
3. **The same referral series for a non-docs section**, as the control.
4. **Bing's prior-week citation counts**, if the report shows them.
5. **Search Console /docs/ clicks and position**, before versus after.

If the history shows 31% is within normal swing, tell your director before Thursday and use the "baseline set" version of the slide.