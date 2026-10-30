# Show-up and no-show figures, with their scopes

Every figure below is reported with the document it came from and the question it was written to answer. They are not interchangeable, and several of them come from the same organisation while measuring different things. Pick the one whose scope matches your event and say which one you used.

## Contents

- The three distinct hackathon-network figures
- Why they must not be blended
- Paid versus free bands
- Corroborating RSVP figure
- A larger, check-in-verified sample
- The nominal-fee lever, and whose it is
- Applying these figures to a format none of them covers

## The three distinct hackathon-network figures

All three come from the MLH hackathon organizer guide, from three different files, and each answers a different question.

**Figure 1 - the show-up trendline and the operational instruction.** From `general-information/managing-registrations/registrations.md`:

> "Statistically about 50% of hackers that register for events show up. They may make plans, decide not to attend last minute, or feel like there is no loss not coming to a free event they previously signed up for. Take this into account and aim for double the amount of registrations. Also make a plan for what to do if you have more sign ups than your event is being planned for. Do not go over double of your aimed attendance. If you exceed your initial goals you might need to make a waitlist."

- **Backing**: the guide's own aggregate chart, described as "Stats from 323 events we have worked with to show the 50% trendline".
- **Scope**: free hackathons.
- **Job**: the only one of the three stated as an operational instruction, and the figure to use when the question is "what overbooking multiplier do I set".

Note that the instruction has two halves, aim for double and do not exceed double; the ceiling is the half that gets dropped in retelling.

**Figure 2 - the drop-off range.** From `general-information/marketing-your-event/marketing-goals-and-timelines.md` ("we expect about a 50% drop-off rate for free hackathons") and, independently, `general-information/marketing-your-event/promoting-your-event/README.md` ("most events have a 30-50% drop-off in attendance", with an instruction to "over-market and overbook").

- **Scope**: free hackathons.
- **Job**: a **descriptive range**, reported as 30-50% rather than resolved to one number. It describes what happens; it does not tell you what ceiling to set.

**Figure 3 - the registration signup curve.** From the same `marketing-goals-and-timelines.md`: aim for 100% of the attendance goal signed up two weeks before the event, and 200% signed up one week before, with a worked timeline for a 500-attendee goal (100 signups at two months, 250 at one month, 600 at two weeks, 1,000 at one week).

- **Scope**: free hackathons.
- **Job**: a **campaign calendar spine**, telling a marketing plan whether registrations are on pace, not how many to accept. It belongs to `samber/dev-event-organizer-skills@event-marketing-plan`; it is recorded here only so it is not mistaken for an overbooking instruction.

The same guide also requires partner-event registration to close one week before the event, so the network can run its own pre-event mailing and bad-actor check. That is a hackathon-network-specific external deadline; do not generalise it into a rule about when registration should close.

## Why they must not be blended

Figures 1 and 2 both look like "50%" and are not the same claim: one is a point estimate on an aggregate chart used to justify a doubling instruction, the other a descriptive range across events with no instruction attached. Figure 3 is a percentage of a _goal at a date_, not a percentage of anything that shows up.

Averaging any two of them produces a number that answers no question anyone asked, and the resulting ratio cannot be defended to whoever signs the venue contract. Report each with its scope, and use figure 1 when setting a ceiling.

## Paid versus free bands

Attributed to Event Tech Live:

- **Paid events convert 90-97% of tickets to actual attendance** - a 3-10% no-show rate.
- **Free events see 40-60% no-shows.**

- Read as no-show rates (3-10% against 40-60%), the gap is close to an order of magnitude.
- Read as the show-up rate you divide capacity by, it roughly halves the ceiling.

State which of the two a quoted multiple refers to. Either way, it is the split every downstream count depends on.

Both figures are population bands, not targets. An event landing inside its band is normal; an event outside it has something to explain. Neither number is a goal to manage toward.

## Corroborating RSVP figure

A major RSVP platform's own organizer guidance tells organisers to expect roughly **50% of confirmed RSVPs** to actually show for a free event. It is a third independent source landing inside the free band, worth citing because it comes from a general-audience meetup population rather than a hackathon one. That is what makes the free-event figure look like a property of free registration rather than a property of hackathons.

## A larger, check-in-verified sample

An analysis of 860-plus events with matched registration and check-in data (narrowed to a 195-event follow-up under stricter inclusion criteria) lands inside the same free-versus-paid split at a lower median:

- Free events: ~96% median registration completion, ~28% no-show rate.
- Paid events: ~86% median registration completion, ~17% no-show rate.
- Blended across the wider pool this draws on: ~20% median no-show rate.

Two findings sharpen the picture beyond the two-source band above:

- **Registration friction is not the driver.** Among paid events only, no-show rates stay flat (~16-19%) regardless of how easy or hard registration is - "whether a paid event completes at 65% or 98%, roughly the same proportion of registrants show up." Easier registration only looks correlated with worse attendance because free events also tend to run the simplest forms; controlling for the free/paid split erases the apparent effect.
- **Most of the gap is which events are free, not what price does to one registrant.** A follow-up analysis found payment's effect on an individual's own odds of showing is closer to a 2-4 percentage point difference within a single event - well under the 11-point gap the event-level comparison (28% minus 17%) implies. Use the population bands to set a ceiling; do not read them as proof that changing one event's price would move that same event's show-up rate by the full margin.

This sample carries no comped/scholarship-ticket breakout and no split by who paid the ticket (employer versus attendee) - it only ever separates free from paid, same as every other figure on this page.

## The nominal-fee lever, and whose it is

A community conference network's organizing guide (devopsdays, `content/page/organizing.md`) gives the budget-side reason to charge a token fee rather than going free: "the financial risk for venue/catering cost is spread out". Its recommended fee is 10-20% of what a commercial tech conference in the same region would charge, with the expectation that sponsorship covers 80%+ of expenses regardless. The trade-off named in the same source is administrative: charging anything pulls in accounting and tax handling, and a cross-border event may need a tax registration whose cost eats a meaningful share of the event's money.

This is the sourced lever that moves an event from the free band toward the paid one. It is a **pricing decision** and belongs to `samber/dev-event-organizer-skills@event-ticket-pricing`. React to whichever posture that skill already picked; do not propose a price here.

## Applying these figures to a format none of them covers

Every operational figure above is a free hackathon's; the paid and free bands are industry-blended across event types. A single-track community conference, a paid workshop day, or a company-run free event with a marketing budget behind it is covered by none of them directly. The four rules below are this skill's own construction, not a measured procedure.

- Start from the band the **price posture** puts you in, not from the format.
- Treat the hackathon ceiling as an upper bound rather than a target when the format differs - it was written for an audience with the loosest possible commitment to a free seat.
- Where you have your own prior edition's registered-versus-attended count for the same event in the same format, that number beats every figure on this page for your event and only for your event. Hold it under the sourced ceiling anyway; one edition is a sample of one.
- Say which figure you started from and what you changed. A number whose origin goes unrecorded cannot be corrected next edition.
