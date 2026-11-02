Next: paste the draft below into the report and fill the `[brackets]`. Three of your six plans need changes, and two need a data check first. The report text is in normal prose. The notes around it are terse.

## What changes, in order of risk

1. **Enterprise SSO claim: cut it.** n=38, mostly from the partner mailing, so enterprise and channel are confounded. You can't tell "enterprise cares more" from "partner-mailing people care more". Report the observation, not the cause.
2. **Response rate: you can't compute one.** The link was open, so there's no denominator. Give the CFO the alternatives in section 6 instead.
3. **Weighting: report unweighted as the headline.** Weighted goes in as a sensitivity check. Reasons are in section 5.
4. **Africa, n=7: don't chart it alone.** Merge it into "Other regions" or label it "n<10, not shown". Seven respondents are 0.6% of the sample and a re-identification risk.
5. **25 verbatims: need consent, scrubbing and a stated selection rule.** Check the consent wording before quoting anyone.
6. **4.1 average: fine, but add the distribution.**

## Draft report sections

### 1. About the data

> The survey was open to anyone with the link. We shared it through the newsletter, the documentation, Discord and a partner mailing. We received [N_raw] responses and kept 1,204 after removing [duplicates / incomplete / failed attention check — state your actual rules]. Respondents chose to take part, so results describe respondents, not all Greywater users. Percentages are unweighted unless noted. Confidence intervals show sampling noise only. They do not cover self-selection bias.

### 2. Satisfaction

> Respondents rated overall satisfaction at an average of 4.1 out of 5 (n=1,204). [X]% rated 4 or 5. [Y]% rated 1 or 2. [Insert bar chart of the 1–5 distribution.]

- Fill X and Y from the data. Always show the distribution, because a mean of 4.1 hides a split.
- Add a one-line caveat: people who use the extension often are more likely to answer a link in the docs or Discord.
- Optional: report satisfaction by channel. If the partner mailing differs, say so.

### 3. Top blockers: enterprise and startups

> Among the 38 enterprise respondents, SSO was the most-cited blocker ([a]% selected it, 95% CI [lo–hi]). Among the 610 startup respondents it ranked fifth ([b]%, CI [lo–hi]). Most enterprise respondents came through the partner mailing, so we cannot separate company size from recruitment channel. With 38 responses, the enterprise ranking is also imprecise. We treat this as a signal worth following up, not a finding.

- Compare the share who selected SSO, not just the rank. Rank hides the size of the gap.
- Use Wilson intervals. At n=38 the interval is roughly ±15 points.
- Run one check: how many enterprise respondents did not come from the partner mailing? If it's under about 10, say "too few to compare".
- Suggested follow-up: interview 5–8 enterprise users about SSO.

### 4. Region chart

> Responses by region: North America [n, %], Europe [n, %], Asia [n, %], South America [n, %], Other regions including Africa and Oceania [n, %].

- Alternative: show Africa separately as "n<10, suppressed".
- Add one caveat line: the survey ran in English only [confirm] and through English-language channels, so regional shares reflect reach, not the user base.
- A region chart plus an OS cross-tab can identify individuals. Don't publish cross-tabs with cells under 10.

### 5. Weighting (my recommendation)

Don't swap in the weighted numbers. Do this:

1. Compute satisfaction and the top-5 blockers unweighted and weighted. Linux gets weight 0.61/0.40 ≈ 1.5. Non-Linux gets 0.39/0.60 ≈ 0.65.
2. If no headline number moves by more than about 0.1 points, or the ranking stays the same, write: "Results were not sensitive to reweighting by operating system."
3. If they do move, show both columns and say which you trust and why.

Why not weight blindly:

- **Unit mismatch.** Telemetry counts installs. Survey counts people. CI runners, containers and reinstalls inflate Linux installs.
- **Telemetry coverage.** Opt-in or opt-out telemetry may skew toward certain users, so 61% is itself an estimate.
- **Weighting can't fix self-selection.** It rebalances Linux vs non-Linux but not the engaged vs silent users inside each group.
- **Variance cost.** Report the effective sample size, n / (1 + CV²) where CV is the coefficient of variation of the weights. Trim weights if any exceed about 3.
- **Channel may matter more.** If OS differences come from channel mix (Discord vs partner mailing), weighting on channel or segment is a better lever.

Report line:

> Linux users are 61% of installs by telemetry but 40% of respondents. We checked whether reweighting to match installs changes the results. [It did not change any headline figure by more than [d].] / [Weighted figures are shown alongside.]

### 6. Response rate (for the CFO)

> Because the survey was an open link, a conventional response rate cannot be calculated: the number of people who saw the invitation is unknown.

Give the CFO these instead:

1. **Partner mailing response rate:** kept responses from that mailing ÷ recipients. This is the only channel with a known denominator. Say "[x]% of [N] recipients".
2. **Completion rate:** completed ÷ started. Your survey tool should have it.
3. **Responses per channel,** with the newsletter send count shown as context: "newsletter sent to [N] subscribers", with no rate claimed.
4. **Coverage ratio:** 1,204 kept responses vs [M] active installs from telemetry. Label it "coverage", not "response rate", and note installs ≠ people.

Don't divide 1,204 by newsletter subscribers or Discord members and call the result a response rate.

### 7. Voice of the community

Selection rule (state it in the report):

> We read all [K] free-text answers and grouped them into themes. The quotes below were chosen to illustrate the most common themes, in proportion to how often each theme appeared, plus [2] critical comments. They are not a random sample.

Theme table to build (cap it at five rows):

| Theme | Share of free-text answers |
|---|---|
| [theme 1] | [%] |
| [theme 2] | [%] |

Do this to the 25 quotes:

1. Confirm the survey told respondents their answers might be quoted. If it didn't, quote only people you have contacted for permission, or paraphrase.
2. Strip names, employers, product names and version strings that identify someone. Enterprise and partner-mailing respondents are the easiest to identify.
3. Don't fix grammar silently. Mark edits with brackets and use `[…]` for cuts.
4. Include negative quotes in the same ratio as negative themes.
5. Retitle the section "Selected comments" if you can't meet 1–4 for all 25.

## Pre-send check

- [ ] Every percentage has its n.
- [ ] Every cell under 10 is merged or suppressed.
- [ ] "Enterprise cares more about SSO" appears nowhere.
- [ ] No sentence says "response rate" except the partner-mailing one.

I can't compute any of the `[brackets]`. I haven't seen the data, and I did not read anything under `skill-wip/`, as you asked.

Next: open the data and fill in `N_raw`, the partner-mailing recipient count and the rating distribution. That takes about 15 minutes. Then paste them here and I'll finish sections 2, 3 and 6.