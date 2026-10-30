# Page shapes and section sets

Contents: three published section sets · the hero field list · the practical cluster · the manager-forward block · a worked negative example.

Every section set below is what a real conference actually publishes. Where a judgment is added on top, it says so.

## Table of Contents

- [Section set A - ticketed, multi-page (DevOpsDays)](#section-set-a-ticketed-multi-page-devopsdays)
- [Section set B - ticketed, single-CTA front door (PyCon US 2026)](#section-set-b-ticketed-single-cta-front-door-pycon-us-2026)
- [Section set C - free to attend, no registration (FOSDEM 2026)](#section-set-c-free-to-attend-no-registration-fosdem-2026)
- [The hero field list](#the-hero-field-list)
- [The practical cluster](#the-practical-cluster)
- [The manager-forward block](#the-manager-forward-block)
- [Worked negative example](#worked-negative-example)

## Section set A - ticketed, multi-page (DevOpsDays)

Separate pages, each with its own address:

`welcome` (the front door) · `program` plus a page per talk · `speakers` plus a page per speaker · `sponsor` · `registration` · `propose` · `location` · `contact` · `diversity` · `conduct`

Two structural facts worth carrying over:

- **Navigation is config-driven, and two entries route outward.** The propose entry points at the CFP tool's own URL and the registration entry at the ticketing platform's, while every other entry routes to an internal page. CFP and ticketing are normally external tools the site links out to rather than embedded forms - an integration detail, never a vendor name in the page's own instructions.
- **Rows get commented out rather than published empty.** On the live 2026 city page, Program, Speakers and Sponsors sit inside HTML comments while Dates, Location, Register, Propose, Diversity and Contact stay live.

## Section set B - ticketed, single-CTA front door (PyCon US 2026)

Navigation, in published order: About · Sponsor · Speaking · Attend · Venue · Events & Summits · Schedule · Volunteer, plus search, sign-up and sign-in.

Page order, in published order:

1. Hero: event name, date range, location.
2. **"Register Today!"** - one primary CTA, linking straight into the ticketing flow.
3. Venue and address detail.
4. A conference-breakdown timeline: tutorials, sponsor presentations, main conference, job fair, sprints - each with its own date span.
5. A schedule-status banner ("The PyCon US Schedule is now live!") linking to talks and keynotes.
6. A health-and-safety notice.
7. News and social-follow.
8. Footer: support, privacy, copyright.

The schedule banner is the same commented-out-until-real principle in its positive form: it is on the page **because the schedule exists**, not as a permanent fixture waiting to be filled. When the schedule is not real, that banner is not there.

## Section set C - free to attend, no registration (FOSDEM 2026)

Navigation: Home · About · News · Schedule · Stands · Volunteer · Practical.

Page order: a **stats-driven hero** ("8000+ hackers", "65 devrooms", "1013 lectures") with dates, location and a status line · feedback collection · video archive · dated news items · sponsor list · venue and campus map. **There is no registration or ticket flow anywhere on the page, and no CTA.**

The hero substitutes scale and credibility for a value-proposition sentence, which is what a free event has instead of a purchase decision to drive. A first-edition free event has neither, and should lead with the promise and the people instead - see the third menu's delete rule in SKILL.md.

## The hero field list

From the DevOpsDays welcome partial, the always-present block is:

- Event name.
- The date range, formatted as a single day or a range depending on whether start and end share a month.
- The venue name plus a map-linked address.
- A one-line description.
- **Only for a recurring event**: a list of other editions in the same city, linking each past year.

That last field has no first-edition equivalent. Do not invent a placeholder for it - the absence is correct.

A visitor should be able to answer _what, who, when, where, what it costs_ within about five seconds and without scrolling, on a phone. The five-second target is carried over from adjacent landing-page practice, not measured against event data. If a hero element serves none of those five questions, it is decoration competing with the CTA.

## The practical cluster

FOSDEM groups accessibility, code of conduct, during-the-event guidance and its health policy as **one footer block** rather than scattering them through the nav. That is one event's choice; the case for copying it is this skill's own, and it is not aesthetic:

- Those pages are the ones third parties link to and attendees forward to employers, so they need stable addresses.
- Grouping them means an attendee looking for one of them finds all four.

## The manager-forward block

The one trace the who-buys/who-pays split leaves on an event page, and this skill's own construction rather than a published pattern. A short, linkable block an attendee sends to whoever approves their travel budget: what the event is, the dates, the location, the cost, and two or three lines on why attending is worth the time away.

It is a section, not a page shape, and it is written from the positioning statement rather than composed fresh. Skip it entirely for a free local meetup, where nobody is asking permission.

## Worked negative example

Constructed for illustration, not a page any real event published. A first-edition, 200-person regional conference, four months out, no speakers confirmed, tickets not yet on sale:

```
[ HERO ]  "The future of engineering starts here."
          Register Now  |  Submit a Talk  |  Become a Sponsor  |  Subscribe

[ THE PROBLEM ]      Engineering teams are more disconnected than ever...
[ OUR SOLUTION ]     Three days of talks that actually matter.
[ SPEAKERS ]         Coming soon!
[ SCHEDULE ]         Coming soon!
[ TESTIMONIALS ]     "An incredible event." - Attendee
[ TRUSTED BY ]       [six greyed-out logo placeholders]
[ PRICING ]          Early Bird $199  ·  Regular $299  ·  VIP $599
```

Eight things are wrong, and each maps to a rule in SKILL.md:

1. The headline is a generic aspiration, not the positioning statement, and it names no audience.
2. Four permanent CTAs - the bottom rung of the CTA menu. Three of them are inert: registration is not open, and sponsorship is a conversation rather than a button.
3. "Register Now" leads to a page saying registration is not open. This is the stale-CTA failure in advance.
4. Problem → Solution is the imported SaaS narrative. An event page carries identity and program facts.
5. Two "coming soon" placeholders, which are dominated outright by leaving both sections off.
6. A testimonial attributed to "Attendee" - for a first edition, it can only be fabricated.
7. "Trusted by" logo placeholders, borrowed social proof for sponsors who have not signed.
8. A three-rung price ladder including a VIP tier that `samber/dev-event-organizer-skills@event-ticket-pricing` did not set, on a page whose author invented it.

What the same event should have published:

- The positioning statement and its contrast sentence.
- The dates, city and venue if known.
- Who is organising it and why.
- The CFP link if the call is open, or the date it opens.
- A notify-me capture with a privacy line.
- The code of conduct.
- A contact address.

Nothing else. Every other section is either withheld under the omit-entirely default or does not exist yet.
