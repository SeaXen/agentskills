I did not extend the early-bird. Your own plan skill says the cutoff comes fixed from `event-ticket-pricing`, and this plan never moves it to suit a campaign. So the calendar below keeps **Fri May 30** as the close, and the extension goes back to pricing as a decision with a case attached.

I also found no APIcon calendar file in this repo, so I couldn't edit one. The calendar is in this answer for you to paste into the real one.

## Open questions

Please check these before sending any of it:

- ⚠️ **Date mismatch:** May 30 is a Friday in 2025. In 2026 it is a Saturday, and today is 2026-10-14. Which year is APIcon?
- Is APIcon ticketed? I assumed yes, so the ladder is percent of expected sales net of comps.
- What are the net-of-comps target, the doors date and the early-bird price? I used placeholders.
- Is APIcon community-run or company-run? I assumed community-run, so barter channels and the owned list come first.

## Calendar (ticketed spine, fixed dates pinned)

| When | Moment | Target |
|---|---|---|
| T-7 months | Marketing live, comms hub up, list building | none |
| Announcement | Tickets on sale | a first-week spike |
| Mon May 19 | Early-bird reminder #1 (email) and LinkedIn run starts | none |
| Fri May 23 | Teaser: first confirmed speaker or keynote (see "Option to propose") | none |
| Wed May 28 | Reminder #2, "48 hours" | none |
| Fri May 30 | **Early-bird closes (fixed)** | about 15% of net expected sales |
| Thu Jun 12 | Speaker announcement | about another 10% |
| T-1 month | Reminder send, sponsor and speaker codes out | 40–50% |
| T-2 weeks | Final surge | a surge |

If you don't see about 15% at the May 30 close, treat it as a weak demand signal. If you land at 25–30% one month out, that points to execution, and the late speaker announcement is one of the three communication causes to check first.

## Option to propose to pricing

The speaker announcement now lands after the early-bird closes, so the two sales spikes are separate. Before asking for an extension, try these inside the fixed date:

1. Announce one or two confirmed speakers or a keynote by May 23, even if the full lineup waits for June 12.
2. Say plainly in the reminders what is fixed and what is coming.
3. If the business still wants more time, send `event-ticket-pricing` a decision request. It should say that moving the cutoff changes the price ladder and revenue, and that the ~15% checkpoint then needs re-baselining. An alternative is a separately named "speaker-reveal" price tier, which is also pricing's call.

## Early-bird reminder email (draft for `event-attendee-email-sequences`)

I wrote this because you asked. That sibling skill owns the final copy, so route it through there for the send.

**Subject:** Early-bird ends Friday: APIcon [year]
**Preview:** Lock in [early-bird price] before it goes to [regular price].

Hi {first_name},

Early-bird pricing for APIcon ends **Friday, May 30**. After that, tickets are [regular price].

APIcon is [one-line promise from `event-positioning`], on [dates] in [city].

- [Confirmed highlight, e.g. keynote or track]
- [Who it's for: roles, levels, who is welcome]
- Full speaker lineup announced **June 12**. Early-bird won't be extended, so decide with what we've already confirmed.

[Get your early-bird ticket]

See you there,
The APIcon team

For the second send (Wed May 28), use the subject "48 hours left" and cut the body to the deadline, the price and one link.

Send this only to people who opted in. Use a tracked link per channel, set up before launch.

## Two weeks of LinkedIn posts (draft for `event-social-media`)

The run is May 19–30, ten weekdays. Every post links with its own tracked code. Bracketed items are placeholders.

| Day | Post |
|---|---|
| Mon May 19 | "Early-bird tickets for APIcon end **Fri May 30**. [Price] now, [regular price] after. [link]" |
| Tue May 20 | Why we built APIcon: [promise], who it's for and who's welcome. |
| Wed May 21 | One session or track preview: "[Topic]: what you'll take back to your team." |
| Thu May 22 | Past-edition photo or number, or a short note on who attends. Skip if this is the first edition. |
| Fri May 23 | Teaser: "First confirmed speaker: [name], on [topic]. Rest of the lineup June 12. Early-bird closes in 7 days." |
| Mon May 26 | "Need to convince your manager? Here's a short justification you can paste." Add a brief employer-approval blurb. |
| Tue May 27 | Attendee-experience post: [format, hallway track, venue]. |
| Wed May 28 | "48 hours left. Early-bird ends Friday." |
| Thu May 29 | "Tomorrow is the last day at [price]. Lineup lands June 12." |
| Fri May 30 | "Last call. Early-bird closes tonight at [time, timezone]. [link]" |

Early-bird sales should lift posts in the last 3 days. Social is weighted low on purpose, so lean on the email list for the close.

## Routing

- Final email copy and sequence: `event-attendee-email-sequences`
- Post calendar and amplification kit: `event-social-media`
- Registration page: `event-landing-page`
- Early-bird date and price decision: `event-ticket-pricing`