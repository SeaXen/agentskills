# PulseConf read: it's probably an execution gap, but you can't confirm that yet

**Do not cancel the track or cut prices this week.** Both are hard to reverse. Each camp is arguing a conclusion that the single number "104 of 380" can't support.

## What the number says

- Assumptions: spine = ticketed, 380 is already net of comps, and the 104 are paid tickets only.
- 104 / 380 = **27%** at one month out.
- The published checkpoint for one month out is 40–50% of expected sales, which is 152–190 tickets. You are 48–86 tickets short.
- A team that skipped or delayed its visibility push lands at **25–30%** at this point (DevOpsDays guide), which is 95–114 tickets. You are inside that band.
- The band is a pattern for community conferences, and the guide says the percentages have shifted. Treat it as a hint, not a verdict.
- If 380 included comps, say 60, then expected sales are 320 and you are at 32%. The shortfall shrinks, but the read doesn't change.

27% points to an execution shortfall rather than missing demand. The two have opposite fixes, and the data below decides which one you have.

## Why each camp's fix is premature

**"Cut prices 40%"** assumes the price is the blocker.
- The reach-versus-conversion split tests that, and you haven't run it.
- A 40% cut means you need about 1.67× the tickets just to match the revenue those tickets would have brought at full price.
- It also penalizes the 104 people who paid full price, and it signals distress.
- Price is `event-ticket-pricing`'s call. If the diagnosis lands there, there are narrower tools (for example, an employer group deal) than a blanket cut.

**"Cancel the third track"** is a cost-sizing decision, not a demand fix. A smaller program doesn't sell tickets. Make this call only if the diagnosis shows real demand shortfall, and then on room, AV and catering numbers. Speakers have likely been announced, so cancelling also costs you credibility.

**"The market doesn't want this"** is the conclusion you reach last. It is only supported if reach and conversion both turn out healthy.

## Diagnose in the next 48 hours

Pull these numbers:

1. **Weekly sales curve.** Did you see a spike at announcement, at early-bird close, and at the speaker announcement? Reference points: about 15% (57 tickets) at early-bird close, then about 25% (95 tickets) after the speaker announcement. You are at 104, so you are probably flat since the speaker announcement. Check whether the announcement actually reached the mailing list.
2. **Registration page traffic by source.** Do you have tracked links? If not, add them now for the remaining window.
3. **Email opens and clicks, and partner referrals.**
4. **Page conversion rate.**
5. **The three communication causes:**
   - late program or speaker announcements
   - a theme narrow enough to exclude part of your audience
   - messaging that never says who is welcome

Then read the result:

| Reach | Conversion | Verdict | Action |
|---|---|---|---|
| Weak | n/a | Execution | Add or re-weight channels (below). Hold price and tracks. |
| Healthy | Low | Price or page | Route to `event-ticket-pricing` or `event-landing-page`. Don't buy more reach. |
| Healthy | Healthy | Real demand shortfall | Route to `event-market-fit`. Right-size the event (Good/Better/Best downgrade). Track cancellation becomes a legitimate option. |

## If the verdict is execution

The four-week runway rules out slow rungs, so skip local relationship-building and list-building from zero.

- **Own mailing list:** the highest-value channel. Send a speaker/agenda push and a reminder. Copy goes to `event-attendee-email-sequences`.
- **Partner channels:** ask partners for their next send. Route to `cross-event-promotion` and `event-media-partnerships`.
- **Comms hub:** make sure it's live. Hand `event-comms-channels` the job of building it.
- **Own social:** keep it running at baseline, routed to `event-social-media`.
- **Paid ads:** only after one owned channel shows a tracked signal worth amplifying. A miss alone is not a reason to spend. I'm assuming a small budget, since I don't know your pole (community- or company-run), cash available, or who approves it.
- **The final-two-weeks surge** is normal, but it can't close this gap unless the diagnosis is a quick fix.

## Reset the forecast

Reaching 380 needs 276 more tickets in 28 days, about 69 a week. Compare that to your last four weeks of sales. If your current pace is far below that, plan for a landing below 380 and decide now what that triggers (downsize, cost cuts). That is a forecast and a planning conversation, not a target to publish. Do this before anyone touches the price or the program.

## Questions that would change the read

1. Is 380 net of comps, and is 104 paid only?
2. Is PulseConf community-run or company-run, and what is the budget?
3. Was there a previous edition? Its own sales curve beats any published ladder.
4. What did the first-week spike look like, and when did early-bird close?

## Which numbers are which

- **Published:** the whole-funnel checkpoints (the 15%, 25% and 40–50% figures, and the 25–30% band).
- **My judgement:** the channel ordering.
- **Set from scratch:** any per-channel target.

## What I couldn't do

- I couldn't confirm the positioning and demand-read inputs this skill expects first. If positioning or market-fit analysis doesn't exist, route there before committing to a channel plan.
- No sales-curve data was provided, so the diagnostic table is a decision tree, not a verdict.

**Next action:** share the weekly sales curve and per-source traffic, and tell the team to freeze irreversible decisions until then.