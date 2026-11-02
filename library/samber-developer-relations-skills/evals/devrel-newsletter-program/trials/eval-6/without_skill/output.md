**Next action (10 min):** export clicks for the last two issues, split by recipient domain into the three enterprise customers and everyone else, and compare the click rate for each group. This tells you whether the 1.3% → 6% jump is real. Everything below assumes you have not run it yet.

# Measurement: customer newsletter

## 1. Driver and goals

- **Driver:** the newsletter exists to keep current customers using the features we ship. The target for each issue is feature use, not attention.
- **Goal 1:** accounts adopt the features each issue announces.
- **Goal 2:** the newsletter reaches the people in each customer account who decide what gets used.
- **Guardrail:** the list stays healthy and opted-in, which is why unsubscribes are tracked.

## 2. Metric sheet

Every threshold is tagged `baseline` (derived from our own history) or `hypothesis` (a round number we are testing). Nothing here is `sourced`. No published benchmark applies to a B2B IoT customer list.

**Primary metric (product impact)**

1. **Featured-feature adoption lift**
   - Definition: the share of active accounts that use the issue's featured feature at least once within 14 days of send, compared with a holdout.
   - Source: product telemetry joined to the newsletter send list by account ID.
   - Baseline: back-fill the last 3 issues from telemetry history. Until then, mark it "baselining".
   - Threshold: the lift over holdout is above 0. Set the range after 3 issues (`baseline`).
   - Owner: product marketing, with data support.
   - Action: if lift is about 0 for 3 issues in a row, change the format (feature first, link to a quickstart, add an in-product prompt) or move the effort elsewhere.

**Supporting metrics**

2. **Click-to-use rate** (enablement)
   - Definition: of verified-human clickers on the feature link, the share whose account uses the feature within 14 days.
   - Source: the ESP click log plus telemetry.
   - Baseline: baselining.
   - Owner: newsletter owner.
   - Action: a low rate means the landing doc or the call to action is broken, so fix the doc first.
3. **Verified click rate** (engagement)
   - Definition: human clicks divided by delivered, split into enterprise-gateway domains and all other domains.
   - Source: the ESP, with bot filtering from section 3.
   - Baseline: 1.3% for the non-enterprise list, from before the onboarding (`baseline`).
   - Threshold: a range around that baseline, set after filtering.
   - Action: if the filtered rate falls back to about 1.3%, report that as the real rate and retire the 6%. This metric is paired with metric 2, so nobody can raise it with clickbait.
4. **Account coverage** (replaces "reach")
   - Definition: the share of active customer accounts with at least one verified click or reply in the trailing 90 days. It is a rolling window, so it can fall.
   - Source: ESP engagement joined to the CRM account list.
   - Baseline: baselining.
   - Owner: customer success, with the newsletter owner.
   - Action: accounts with zero engagement go to their CSM for direct outreach.
5. **Unsubscribe rate per issue, by cohort, plus complaint rate**
   - Definition: unsubscribes divided by delivered, split into legacy contacts and contacts added with the enterprise onboarding. Spam complaints are reported next to it.
   - Source: the ESP.
   - Baseline: 0.1% a year ago, 0.25% now. The segment split sets the new baseline (`baseline`).
   - Threshold: alert when the rate leaves its trailing range.
   - Action:
     - If only the enterprise cohort drives the rise, fix the list source and consent and offer a preference center.
     - If the legacy cohort also rose, test frequency and content.

**Reported as diagnostics (no target, not counted as metrics)**

- **Open rate:** inbox privacy proxies and gateway image prefetch generate machine opens, so it overstates human reading.
- **Click-to-open:** it divides clicks by those inflated opens, so it is unreliable.
- **Delivered rate by recipient domain:** this shows whether enterprise gateways are quarantining or bouncing the issue.

## 3. Protecting the click and unsubscribe numbers

- **Cause of the jump:** corporate mail gateways pre-scan links, and their scans register as clicks. The timing matches: the jump came right after three enterprise customers joined. This is a hypothesis until your domain split confirms it.
- **Decision rule:**
  - If the non-enterprise rate is still near 1.3%, the jump is a gateway artefact.
  - If it rose too, some of the lift is real.
  - If both rose, report the split.
- **Bot filter:** flag a click when any of these holds:
  - several distinct links are hit in the same few seconds;
  - the click lands within seconds of delivery;
  - the user agent or IP matches a known scanner;
  - it hits a hidden 1-pixel honeypot link that no human can see.

  Calibrate the thresholds on your own data. Check first whether your ESP already offers bot filtering.
- **Unsubscribe link scans:** scanners can also hit unsubscribe links. Use a confirmation page or a POST-based one-click unsubscribe, and exclude unsubscribes that land inside the scanner pattern.
- **Small numbers:** at 0.25%, a list under 12,000 gives fewer than 30 unsubscribes per issue. Below that, report the raw count and date, not a rate.

## 4. Attribution rule (written before the period starts)

- **Method:** pre/post lift plus a holdout.
  - Randomize at the account level, stratified so each enterprise customer sits in one arm.
  - Hold out about 10% of accounts, or fewer if you have few accounts.
  - Send the holdout the issue without the featured item.
- **Lookback window:** 14 days from send.
- **Wording:** always say "influenced". Product prompts, CSMs and release notes share credit for adoption.
- **Selection bias:** engaged readers are probably more active anyway. Compare against the holdout, never against non-clickers.
- **Small numbers:** with three large enterprise accounts, the effect size will be noisy. Report counts of accounts, not only percentages.

## 5. Reporting

- **Per issue:** the owner reads metrics 1 to 5 (diagnostics are for reference). One look, no decisions.
- **Monthly (2 issues):** read trends and the bot-filtered click split.
- **Quarterly:** decisions on format, frequency and budget.
- **Annually:** reset the framework.
- **Dashboard for the VP of marketing:**
  - Put metric 1 on top.
  - Show open rate and click-to-open as labelled diagnostics, with no targets.
  - Say plainly that 45% and 8% are untested round numbers, and that the click-to-open denominator is inflated by machine opens.
  - "Reach" becomes account coverage. A cumulative subscriber count only goes up, so it cannot show failure.
- **Before reporting the 6% click rate upward:** publish the filtered figure alongside it. Reporting an unfiltered figure that later drops will cost credibility.

## 6. Known blind spots

- **Join key:** linking a newsletter click to product use needs an account ID in the link or a CRM join. If it does not exist, metrics 1 and 2 are instrumentation requests, not metrics yet.
- **No click, still adopted:** readers who see the feature and go straight to the product leave no click. The holdout comparison captures them. The click-based metrics do not.
- **Baseline contamination:** only 2 issues exist since the onboarding. Treat every post-onboarding number as provisional.
- **Consent for the enterprise contacts:** if they were imported, not opted in, the extra unsubscribes are expected and the real problem is list sourcing.
- **Causality:** with three enterprise accounts and few active accounts overall, the lift estimate can be wrong. Say so in each report.

## 7. Review and kill rule

- **Remove a metric** that has not changed a decision in two consecutive quarterly reviews.
- **Restate baselines** once 3 post-onboarding issues exist with the segment split.

## Pass check

| Check | Status |
|---|---|
| 5 metrics, no more than 8 | ✅ |
| All six fields per metric | ✅ (baselining marked where there is no history) |
| One metric in product impact | ✅ (metric 1) |
| No monotonic primary | ✅ |
| Attribution rule written, with method and lookback | ✅ |
| Counter-metrics paired | ✅ |
| Thresholds labelled | ✅ |
| Blind spots listed | ✅ |

## Questions that change this plan

1. Do you have a join from newsletter click to product account, and does the product emit a use event for each feature?
2. How big is the list? Under about 12,000 contacts means unsubscribe is reported as raw counts.
3. Were the enterprise contacts opted in or imported?

**Next:** run the domain split from the first line and send me the two rates.