# Feedback slide review for the Lanternworks VP Eng

**Next action (about 45 min):** recount the "11 of 14" with a stricter rule, then cut the Gartner line. Both are the weak points on this slide.

## Verdict

Don't send the draft as is. Two of the four claims will not survive a VP's first question, and the nine extra metrics would make that worse.

## Claim by claim

**1. "Feedback volume up 40% QoQ"**
- ⚠️ Volume is activity, not a result. It can rise because you grew, had an incident, or added a channel.
- Normalize it: feedback items per 100 active accounts. Split it by Discord, GitHub, and support.
- If accounts grew 40% too, the real change is 0%.
- If the rise is mostly bug reports after an outage, say so.

**2. Gartner "95% / 10% / 5%"**
- ❌ I couldn't verify this as a Gartner figure. Stats shaped like this circulate without a primary source.
- Even if it's real, it describes other companies, not Lanternworks.
- Cut it. If you keep it, link the primary source and footnote it. Check that source before Friday.

**3. "Median first response under 10 minutes"**
- ⚠️ Give the actual number. "Under 10" reads as rounding up.
- A median hides the tail. Add p90, or the share answered within a target (for example 95% within 4 hours).
- State what counts as a response. A bot or auto-acknowledgement shouldn't count.
- Say which channel it covers. Discord replies are fast, and support tickets and GitHub issues usually aren't.

**4. "11 of 14 community-driven"**
- ❌ This is the riskiest claim. "At least one Discord mention" gives 79%, and a skeptic can inflate it further. The mention may have come after the feature was scoped, or from your own staff. It may also have been one person once.
- It also ignores GitHub and support, and in a DBaaS the paying customers mostly sit in support.
- Better rule, written before you recount:
  1. The request exists in a tracker or Discord thread dated before the work was scoped.
  2. It comes from at least 3 distinct external accounts, or from 1 account above an ARR threshold.
  3. Staff mentions are excluded.
  4. The request is linked to the shipped item.
- Report both numbers, for example "11 of 14 touched by feedback, X of 14 driven by it (strict rule)".
- With n=14, one feature moves the figure by 7 points. Say so in a footnote.

## The nine extra metrics

Don't add them. Padding a dashboard to look thorough invites "which of these do you act on?", and you'd have no answer for most of them. A metric earns its place only with an owner, a written definition, a target, and a decision it changes. Add 3 to 4, not 9.

## What the VP asked for: one number

Make the headline the **closed-loop rate**: the share of feedback items from the quarter where the submitter heard back on a decision (shipped, planned, or declined) within 30 days.
- It is the 5% gap from the Gartner line, but measured on your own data.
- It's hard to inflate, and it points at an action.

Supporting cast:
1. Feedback per 100 active accounts, with the trend.
2. First-response p90 and the share within target.
3. Strict feedback-driven shipped share, as in item 4 above.
4. Optional: median age of open requests.

## Rewritten slide (fill the brackets from your data)

> **Headline:** [X]% of this quarter's feedback got a decision back to the customer within 30 days (target: [Y]%).
> - Feedback per 100 active accounts: [A] (was [B] last quarter). Raw volume is up 40%; accounts are up [Z]%.
> - First response: median [m] min, p90 [h] h, [P]% within target. Human replies only.
> - Shipped: 14 features. [X] were driven by feedback under the strict rule, and 11 had at least one Discord mention.

## Questions to settle before Friday

1. Did active accounts grow this quarter, and by how much? This decides whether the 40% is good news.
2. Can you timestamp when each feedback item arrived relative to when the feature was scoped?
3. Does the VP want one number to track every quarter, or a story for this one meeting? A recurring number needs a stable definition, so I'd lock the closed-loop rule now.

Send me the recount and the account growth and I'll tighten the slide.