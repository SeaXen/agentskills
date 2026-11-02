# HollowPine Summit email program: benchmarks and measurement for next year

## 1. Don't call 52% a win yet

The 52% vs 21% comparison has three problems.

1. **Open rates are inflated by machine opens.** Apple Mail Privacy Protection and some security scanners load the tracking pixel without a person opening the email. Depending on your audience, opens can be overstated by 10–30+ points. The "21% industry average" is distorted the same way, so you're comparing two noisy numbers.
2. **The audience is different.** The 21% average is mostly cold-to-warm marketing and newsletter sends. Your practical-info email went to people who paid or registered and need the logistics. For that audience, 50–70% opens is typical. Your 52% may be average or even low for this kind of email.
3. **A higher open rate isn't the goal.** The practical-info email exists so attendees show up informed, with fewer "where do I go?" questions. An open doesn't show that happened.

What the numbers do tell you:

- The day-before reminder got 48% against 52% for practical info. Attendees are still opening these emails, so engagement is healthy and no obvious problem showed up.
- **Three unsubscribes can't be judged without the send size.** On 2,000 recipients that's 0.15%, which is fine. On 150 recipients it's 2%, which is a problem. Send me the list size and I'll give you a verdict.
- The unsubscribes came on the final reminder, which is the last chance to leave before the event. Check two things:
  - Whether those three attended anyway.
  - Whether reminders are marked "required event communications", so people can opt out of marketing without losing logistics.

## 2. Benchmarks to set for next year

I can't give you a reliable public benchmark. Vendor "industry averages" mix very different sender types and are MPP-distorted. Use these as **starting hypotheses**, then replace them with your own baselines after the first 2–3 sends. The ranges are my estimates, not sourced statistics.

| Email type | Open rate (directional) | Unique click rate, % of delivered | Unsubscribe per send | Spam complaints |
|---|---|---|---|---|
| Registration confirmation (transactional) | 70–90% | 25–50% (add-to-calendar, manage ticket) | ~0% | <0.05% |
| Practical info / logistics | 50–70% | 10–25% | <0.2% | <0.1% |
| Day-before / day-of reminder | 45–65% | 10–20% | <0.3% | <0.1% |
| Pre-event promotion to registrants (agenda, speakers) | 35–55% | 5–12% | <0.3% | <0.1% |
| Promotion to prospects not yet registered | 20–35% | 1.5–4% | <0.5% | <0.1% |
| Post-event follow-up (recap, survey) | 40–55% | 5–15% on survey/recording | <0.3% | <0.1% |

**Treat opens as a deliverability check, not a success metric.**

- Use a unique click rate based on delivered emails as your primary engagement number.
- Use click-to-open only as a secondary diagnostic.
- Set an alarm threshold for each metric (for example, click rate falling more than 25% below your own baseline) rather than a "win" threshold.

## 3. Measuring whether attendee emails work

Start from the job each email has, then measure whether the job got done.

| Email | Job | Outcome metric |
|---|---|---|
| Confirmation | Reduce ticket anxiety, get calendar adds | Add-to-calendar rate, ticket-resend support requests |
| Practical info | Attendees arrive knowing where and when | Share of attendees who clicked the venue/schedule link, plus count of "where/when/how" support messages and on-site questions per 100 attendees |
| Reminder | Convert registrants into attendees | Show-up rate (checked in ÷ registered), compared across people who clicked vs. didn't |
| Pre-event promotion | Drive session planning and engagement | Agenda saves, session sign-ups, app downloads |
| Post-event | Capture feedback and extend the relationship | Survey response rate, recording views, next-year interest signals |

Practical steps:

1. **Segment machine opens.** Flag Apple MPP and bot-like opens (opens within seconds of delivery, or opens with no clicks anywhere) and report opens with and without them.
2. **Track show-up rate as your headline metric.** Show-up rate is checked-in attendees ÷ registrants, reported by ticket type. Compare it against past years and against attendees who engaged with the emails and those who didn't. Engagement is correlated with attendance, not proven to cause it, so treat that gap as a signal.
3. **Run holdouts.** Withhold the day-before reminder from a random 10% of registrants. Compare show-up rates to see the reminder's actual lift. Don't hold out critical logistics emails. Test this on reminders only.
4. **Add a measurable ask to each email.** Put one tracked link per email, such as "Add to calendar", "Save your agenda", or "Get venue directions". A click on that link shows the email was useful, which an open does not.
5. **Ask attendees.** Add a post-event question such as "Did you have the information you needed before arriving?" (1–5). Combine it with a free-text "what was missing?". Target 4.3+ on the 5-point scale, but set the real target after your first baseline.
6. **Count the negative signals.** Track logistics questions in support, and on-site help desk queries that the email should have answered. Falling counts show better emails.
7. **Watch deliverability.** Track bounce rate (<2%), spam complaints (<0.1%), and inbox placement on a seed list before each big send.
8. **Segment everything.** Report by registrant type (attendee, speaker, sponsor, VIP, first-timer vs. returning). Blended averages hide the failures.
9. **Tag for revenue.** Tag email-sourced registrations (UTM + registration source) and use self-reported "how did you hear about us" to avoid over-claiming (see the attribution approach in the events skill). Judge the program on a 2–3 event trend, since one summit is a small sample.

## 4. Unsubscribe policy for event emails

- Split emails into two classes: required event communications (ticket, logistics, schedule changes, safety) and optional marketing (promotion, newsletters, sponsor offers).
- Give unsubscribers a preference center with "logistics only" as an option instead of a single all-or-nothing unsubscribe.
- Review each unsubscriber's context: did they attend, and which email triggered it? Three unsubscribes is a prompt to investigate, not a conclusion.
- Alarm thresholds: unsubscribe rate above 0.5% on any send, or complaints above 0.1%, triggers a content and targeting review before the next send.

## 5. Plan for next year

1. **Now:** pull the send counts, bot-filtered open rates, click rates, and show-up rate from this year. Those become your baseline.
2. **Before the next summit:** add the tracked "job" link to each email, set up the logistics-only preference option, and add a post-event "did you have what you needed?" question.
3. **During the campaign:** run the 10% holdout on the day-before reminder and A/B test subject lines on promotion emails only.
4. **After the summit:** compare against the baseline. Set next year's targets as improvements on your own numbers (for example, +3 points show-up rate, support questions per 100 attendees down 20%) rather than against an industry average.

**Open item:** I need the registrant count and delivered counts for each send to judge the 3 unsubscribes and set specific baselines.