## Short answer

Your instinct to *split* revenue across studies (rather than let each study claim the full deal) is correct — it's the one thing that keeps your total from double-counting. But "every deal that touched a study, split evenly" will hand your CMO a number that's both **too confident** and **too flat**. Fix four things before it goes in front of her.

## What's right

Splitting so the numbers sum to your actual closed-won total (not summed across studies) is the correct instinct — it's the same discipline as not letting Google and Meta both claim the same conversion. Keep that.

## What breaks the plan as stated

**1. Equal split treats every touch as equally causal.** A case study a rep CC'd once in a nurture sequence six months out gets the same credit as the one a buying committee explicitly asked for and cited in the final call. Weight by proximity to close instead of splitting flat — e.g., the case study touched closest to close-date gets more weight than ones touched early in the cycle. This is the same logic as time-decay/position-based models: recency-to-conversion carries more signal than raw touch count. With only 6 studies you don't need a fancy formula — even "last-touched study gets 2x weight, the rest split the remainder evenly" beats pure linear.

**2. "Touched in the CRM" undercounts, and it undercounts unevenly.** Two different signals hide behind that phrase: (a) marketing-automation-tracked page visits/link clicks — objective, but only fires if the person is already identified and cookied — and (b) a rep manually logging "sent case study X" — only exists if the rep bothered to log it. Studies pushed mainly through email/sales enablement will look artificially weak next to studies that happen to get auto-tracked. Before trusting the number, audit what fraction of closed-won deals have *any* logged content touch at all — if it's under half, the top-line number is measuring your logging discipline more than your case studies.

**3. It's blind to anything that didn't happen inside the CRM.** A case study forwarded in an internal Slack thread, downloaded as a PDF and shown in a board deck, or found via Google by someone who never filled out a form — none of that logs a touch, and B2B buying committees do this constantly. This is the dark-social gap, and tracking cannot see it structurally. The fix is cheap: add one field to your closed-won/win handoff — *"Did any of our case studies come up during evaluation? Which one(s)?"* — asked of the AE or the buyer directly. Treat it as a second, independent read that corrects the CRM-only number, not as noise to ignore.

**4. It conflates two different jobs a case study can do.** Most of your 6 studies will only ever *influence* deals already in flight (what your plan measures). But if any of them rank in search, get shared on LinkedIn, or get cited in a "best X for Y" roundup, they can also *source* net-new pipeline — someone lands on the case study page cold and later becomes a lead. That's a first-touch/landing-page attribution question, answerable from web analytics, and it's a materially different (and more impressive) claim than "influenced an existing deal." Report them separately. Don't let "influenced" quietly become "generated."

**5. Roll up to the account, not the contact.** In B2B, the person who read the case study and the person who signed are often different people at the same buying committee. Query "did anyone on this account touch a study," not "did the primary contact."

## What the dashboard should actually show her

Structure it as a readout, not a spreadsheet dump — she needs a decision, not a data pull.

**Headline (top of page, one line):**
"$X of FY closed-won revenue touched the case study program (Y% of total), built from Z deals — [confidence: high/medium/low based on logging coverage]."

**Per-study table (6 rows, the core asset):**

| Case study | Attributed revenue (weighted split) | Deals influenced | Deals sourced (net-new, if any) | Self-reported mentions | Segment/industry |
|---|---|---|---|---|---|
| ... | round to nearest $1–5k, not exact cents | count | count | count from the win survey | so she sees which vertical is working |

**Comparative cut (the part that actually moves a budget conversation):** win rate and average sales-cycle length for deals that touched ≥1 case study vs. deals that touched none. Content teams routinely win budget more on "cycle time -X days" and "win rate +Y pts" than on a raw revenue-attribution figure, because the revenue number is inherently modeled and arguable, while cycle-time/win-rate deltas are a cleaner before/after.

**Confidence panel (don't skip this — it's what makes the rest defensible):** state the logging-coverage % the whole thing rests on, name the blind spot (dark social / untracked shares) and how big you think it is from the self-reported survey, and say plainly that the model is a weighted estimate, not a ledger entry. A CMO who's seen attribution numbers before will trust you more, not less, for saying this out loud.

**One trend line:** cumulative studies published vs. cumulative attributed revenue over the year — shows whether the program is compounding (later studies riding on earlier ones' credibility) or each one is a one-off.

Bottom line for the budget conversation: lead with win-rate/cycle-time deltas as the headline claim, use the weighted revenue split as the supporting number with its confidence caveat attached, and use the self-reported survey result to argue for *more* studies if it turns up meaningfully more mentions than the CRM alone caught — that gap is your evidence that the program is undercounted, not overcounted.