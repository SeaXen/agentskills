Don't run NPS as the proof. Measure whether trained people did the work in their own environment afterward, then divide the spend by that. Next action: get the all-in cost number and the definition of "activated" (below) before the event, because the baseline can't be rebuilt afterward.

## Why not NPS

- NPS measures how people felt at the end of the day. It says nothing about whether they can do the work.
- At 25 people per session, one or two people move the score by several points. A session score is noise.
- The main conference's NPS isn't comparable. It's a different format with a different audience, and it measures attendance.
- Keep one satisfaction question per session (pacing and instructor) to diagnose a bad session. Don't present it to the board as proof.

## What to measure

The headline is **cost per activated account**. The other metrics explain it.

| # | Metric | Definition | Source | Threshold, with tag |
|---|---|---|---|---|
| 1 | **Checkpoint pass rate** (primary, same day) | Share of attendees who finish the session's last hands-on task unaided. Use an auto-check script or facilitator sign-off. | Lab environment | Expect ≥70% pooled. Under 50% means the session needs a redesign. `hypothesis`, recalibrate to your own median after this event. |
| 2 | **Confidence delta** (diagnostic) | Before and after rating, 1–5, on the three tasks the session teaches. | 2-question form | Median gain ≥1 point. `hypothesis`. Supporting evidence only, since it's self-reported. |
| 3 | **30-day activation** (the key one) | Share of attendees who run the real target action (define it, e.g. first production API call) in their own account within 30 days. | Product analytics, joined by registration email | Gap versus control of 20 points or more. `hypothesis`. |
| 4 | **90-day repeat use** | Share of attendees active at day 90 who did the action again. | Product analytics | Baselining. Set the threshold after the second event. `baseline` once you have it. |
| 5 | **Influenced pipeline or expansion** | Accounts with at least one attendee, with a 180-day lookback. Always call it "influenced", never "sourced". | CRM | Report the raw account list. Fewer than ~30 accounts means no rate. |
| 6 | **Cost per activated account** | All-in cost divided by accounts that hit metric 3. | Finance plus metric 3 | Must beat your cheapest comparable channel, such as the main conference cost per activated account. `baseline`. |

All-in cost means venue share, facilitators, lab infrastructure, travel, and staff hours.

**Break-even for the board:** all-in cost ÷ value of one activated account = the number of activations needed. Use first-year margin or expected contract value for the account value. This tells the board what "worth it" means before the results arrive.

## Make the comparison honest

Attendees chose training, so they were already motivated. Without a control you can't claim the training caused anything.

1. **Best option, if seats are oversubscribed:** draw seats by lottery. The people who didn't get a seat become a real control group.
2. **Otherwise:** compare against people who registered but didn't show up. They have the same motivation and no training.
3. **Weaker option:** compare against main-conference attendees who skipped training. Say plainly that this one is confounded.

Power is limited. With about 120 attendees against about 30 controls, you can only distinguish gaps of roughly 20 points or more. Smaller gaps are directional. State this in the board deck.

## Small-N rules

- A single session has 25 people, which is under the ~30-event floor. Don't set per-session targets.
- Report pass rate pooled across all six sessions, about 150 seats. Count unique people separately if anyone attends more than one session.
- Show each session as raw "x of 25" counts. Use them only to spot an outlier session, then fix that session.
- The sessions are small and concurrent, so one bad instructor or a broken lab can sink a session's numbers. Check the lab environments before the day.

## Before the event (these can't be reconstructed later)

1. Define "activated" in one sentence, and confirm product analytics can see it per account.
2. Collect registration email and get consent to link it to product usage. Needed for GDPR if any attendees are in the EU.
3. Build the auto-check scripts for each session's final task.
4. Record the baseline: activation rate over the last 3 months for comparable signups, and the main-conference cohort rate.
5. Add one signup question, "How did you hear about us?", so you capture off-web influence.

## Reporting cadence

- **Day of:** metrics 1 and 2. This is the first board number.
- **Day 30:** metric 3, with the control comparison.
- **Day 90:** metrics 4 and 6.
- **Day 180:** metric 5. Enterprise cycles run long, so name the 30-day activation as the leading indicator until then.

## What not to claim

- Don't claim causation without the control.
- Don't quote a pipeline dollar figure as "sourced".
- Don't use another company's benchmarks. All thresholds above are my starting hypotheses. Replace them with your own median after this event.

## Kill rule

After two events, if the activation gap versus control is near zero, or cost per activated account is worse than your cheapest alternative channel, change the format or cut it. Only the first part of the rule needs the control group.

## What I assumed and need from you

I assumed attendees can be matched to product accounts, "activated" has a clear definition, and the event happens before any of this is measured. Tell me what Ashgrove's product does, what the training day cost all-in, and whether seats are oversubscribed. I'll turn this into a one-page board sheet with the break-even filled in.