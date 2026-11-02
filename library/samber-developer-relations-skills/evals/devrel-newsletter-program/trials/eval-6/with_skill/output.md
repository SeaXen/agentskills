# Measurement section: Lindqvist Systems developer newsletter

I ran the skill's measurement step against your numbers. I did not run the full charter: the gate, shape, cadence and ownership sections are out of scope here.

## Direct answer to the VP

Don't adopt the 45% open, 8% click-to-open and "reach" targets as written. Each one is built on opens, and opens are the least reliable number you have. Your own two observations explain why. The dashboard should instead track clicks per delivered email with machine clicks removed, unique human clickers across the last 3 issues, and feature adoption from newsletter links.

## What your two observations mean

| Observation | Reading | Status |
|---|---|---|
| Clicks went from 1.3% to about 6% right after three enterprise customers joined | Corporate mail gateways follow every link on arrival to scan it, so this is most likely machine clicks, not interest. A 4-5x jump from adding three accounts is the typical signature. The software-sector median is about 1.15% (MailerLite, 2024-25), so 6% is far above it. | **Unproven.** Do not report 6% as engagement until filtered. |
| Unsubscribes went from about 0.1% to 0.25% over a year | Not alone a content signal. The cross-industry median rose from 0.08% to 0.22% over 2024-25, which MailerLite attributes to Gmail's easier unsubscribe under the 2024 bulk-sender rules. 0.25% sits at the software median of 0.2%. | **Watch, don't alarm.** Segment before concluding. |

The jump to 6% is also a risk to your stated goal of keeping customers using the features you ship. A gateway click looks like feature interest, so unfiltered clicks would make the newsletter look successful while telling you nothing.

## Step 1: validate the 6% before any target is set

Run this before the next issue. It takes one export from the sending platform.

1. Enable the platform's bot-click filter, if it has one. Record which filter you used and report it next to every click figure.
2. Without a filter, discard these clicks:
   - clicks within seconds of delivery, as a starting cutoff (the exact number of seconds is your choice; write it down)
   - sends where the recipient clicked every link in the issue
3. Split the last two issues by recipient: the three enterprise domains versus everyone else.
4. Recompute clicks per delivered email for each segment.

How to read the result:

| Result | Meaning | Action |
|---|---|---|
| Non-enterprise clicks still near 1.3%, enterprise clicks mostly instant | The jump was machine traffic | Report the filtered figure. Treat 1.3% as the baseline. |
| Filtered clicks stay well above 1.3% | Real engagement from the new accounts, or both effects | Keep the filtered figure as the new baseline after 3 filtered issues. |
| Platform has no filter and you cannot timestamp clicks | You cannot measure clicks reliably | Mark clicks **blocked**. Lean on replies, unique clickers by non-gateway segment, and product adoption. |

Also check how your unsubscribe link works. A gateway that follows a one-click unsubscribe link can unsubscribe people who never asked to leave. This check is my addition, not from the skill. If the link works on a plain GET request, move it to a confirmation page.

## Step 2: replace the VP's three metrics

| VP ask | Problem | Replacement |
|---|---|---|
| 45% open rate | Mail-privacy pre-fetching and gateway scanning register opens nobody made. | Report as **directional**. No target. |
| 8% click-to-open | Both numerator and denominator are inflated by machines, so the ratio can hit target for the wrong reason. | Drop it. Clicks per delivered email, filtered, replaces it. |
| "Reach" | If it means subscribers who opened, it is open-based. | **Unique human clickers across the last 3 issues**, divided by delivered subscribers. Same idea as Golang Weekly's multi-issue reach, built on clicks instead. |

Give the VP a "reach" number that is real. Call it "active readers" if the word helps the conversation.

## Step 3: the dashboard

Review quarterly against the list's own trend. Alert on issue-level movement.

| Tier | Metric | Definition | Target |
|---|---|---|---|
| Primary | Clicks per delivered email | Filtered, per send, with the filter named | Provisional floor: 1.3%, the pre-enterprise level. Re-baseline after 3 filtered issues. House rule, not an industry target. |
| Primary | Unique human clickers, last 3 issues | Distinct filtered clickers ÷ delivered subscribers | Set after the first filtered computation. No number yet. |
| Primary | Unsubscribes and complaints | Per delivered, per issue | Compare to the list's own trailing 6-issue median. Proposed house rule: investigate any issue above 2x that median. |
| Primary | Replies | Count per issue | Qualitative. Log forwards too. |
| Outcome | Feature adoption from newsletter links | Accounts that used a featured feature within 14 days of the issue, split by clicked or not clicked | Direction only: clickers should adopt more than non-clickers. |
| Directional | Open rate, click-to-open | As reported by the platform | **None.** Greyed on the dashboard, labeled "inflated by mail-privacy and gateways". |

Rules for the outcome signal:

- Count adoption from product events, never from the click itself. A gateway click would otherwise credit a feature the account never touched.
- The 14-day window is a house rule. Pick another if your release cycle justifies it.
- Tag each newsletter link with a campaign parameter so the product can tie usage back to an issue.
- If you ship a feature with no per-account usage event, flag it as unmeasurable instead of estimating.

## Step 4: unsubscribe diagnosis

Split the 0.1% → 0.25% rise before acting on it:

| Cut | Question |
|---|---|
| By signup cohort | Did older subscribers drift up, or only recent ones? |
| Enterprise domains versus others | Are gateway-driven or mass-onboarded users leaving? |
| By date | Did the rise start in mid-2024-style Gmail changes, or after a specific issue? |
| By send | Did any single issue spike? |

If the rise is spread evenly across cohorts, it matches the industry drift and needs no action. If it concentrates in the enterprise accounts or in one cohort, the likely cause is how those people got on the list. See the consent point below.

## Step 5: exit triggers tied to measurement

| Trigger | Action |
|---|---|
| Filtered clicks and replies fall for two consecutive quarters against your own trend | Re-run the start-or-keep gate. The readers' need may have moved. |
| Unsubscribes exceed 2x the trailing 6-issue median (house rule) | Investigate the segment and last issue before the next send. |
| The platform cannot filter machine clicks and no timestamp export exists | Stop reporting clicks as a primary metric. Fall back to replies and product adoption until fixed. |

## Open questions

- **Consent for the enterprise staff (blocked).** How did the three customers' staff get on the list: self-signup, import, or account provisioning? If they came from account creation, EU and UK individual addresses may have no lawful basis. Owner: whoever holds privacy. Re-check before the next send. Keep newsletter content out of account and billing email.
- **Does the sending platform have a bot-click filter?** If not, can it export click timestamps? Owner: the newsletter sender. Needed before Step 1.
- **Delivered count per issue and enterprise segment size.** Needed to compute reach and the segment split.
- **What does the VP mean by "reach"?** Subscribers, opens, or people who acted? Ask before presenting the replacement.
- **Cadence.** I did not test whether the supply of releases and posts fills a fortnightly send. That belongs to the gate in the full charter, which I have not run.

## Pass-threshold check, measurement items only

- No open-derived metric is primary: **pass**.
- One outcome signal matches the funding answer, retention through feature adoption: **pass**.
- Machine-click filter named and reported: **pending**, blocked on the platform answer.
- Thresholds set from the team's own baseline and labeled as house rules: **pass**, with the 1.3% floor provisional.
- Consent provenance stated: **blocked** on the enterprise list question.