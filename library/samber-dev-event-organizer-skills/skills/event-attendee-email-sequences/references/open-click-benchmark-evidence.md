# Open-rate and click-rate benchmark evidence

What exists, what it actually measures, and why it stops short of a target figure for the confirmation, reminder and post-event sends this skill writes.

## The one named-organizer benchmark found

Eventbrite's benchmarking survey of 340-plus event organizers across the US and UK, about half running professional events, meetings and conferences, reports:

- **Open rate: 21-30%** across the surveyed organizers' event email.
- **Click-through rate: 2.1-3%**, with the top 14% of organizers reporting a CTR above 11%.
- **List unsubscribe rate: roughly 25% of a list over the course of a year.**

This is the only figure found anywhere that is scoped to event organizers sending event email, rather than a cross-industry marketing average. It still falls short of a usable target for two structural reasons:

- **It predates the 2021 change to how mail clients pre-load remote images for privacy**, which fires an "open" event whether or not a human ever saw the message. Every open-rate figure measured since reads higher for this reason alone, so the 21-30% floor is not comparable to a number pulled from a modern email platform's dashboard without adjustment.
- **It does not separate promotional list-building sends from post-registration sends.** The surveyed organizers' "event email" almost certainly blends ticket-sale marketing to prospects with the confirmation, reminder and post-event sends this skill covers, sent to people who already registered. The two audiences behave differently: a stranger deciding whether to buy a ticket and a confirmed attendee expecting logistics information are not the same open-rate population.

Read the figures as a rough sanity floor: an event send landing far below 21% open or 2% click is worth a second look. Do not read them as a pass/fail bar, and never report against them as if they measured this skill's own send types.

## What was checked and confirmed absent

- **No reply-rate figure exists for event attendee email in any source found**, published or vendor-claimed. Survey response-rate figures exist (see `samber/dev-event-organizer-skills@event-feedback`) but measure a different behavior: filling out a feedback form, not replying to an operational email.
- **Cvent and Bizzabo do not publish open-rate or click-rate figures for attendee email.** Both vendors' public "state of events" reporting covers attendance, engagement and ROI attribution; a third-party platform comparison names Bizzabo's email engagement analytics specifically as weak relative to Cvent's, which is consistent with neither vendor treating this as a benchmark they compete on.
- **Sender-industry benchmarks (MailerLite, Mailchimp, GetResponse and similar "entertainment and events" categories) do not isolate attendee email.** These figures bucket by the sending business's self-declared industry, not by email type, so they mix any company that happens to sell tickets or run venues with the specific confirmation/reminder/post-event sends this skill is about. Importing one would repeat the exact mistake this skill's measurement section warns against.
- **Transactional-versus-marketing email benchmarks (Omnisend, Experian and similar) confirm that a triggered, expected send outperforms a promotional one by a wide margin**, which supports treating a confirmation email differently from a cold marketing blast in principle. The underlying data is e-commerce order and shipping confirmations, not event registrations, so it is directional support for the general shape of the argument, not a number to cite as an event figure.
