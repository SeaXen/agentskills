# Sourced format precedents

Named events whose structural choices - and the organizers' own reasons for them - back the menus in SKILL.md. Cite these as per-event precedents, never as industry averages.

## Graduation trajectories: meetup → single-day → multi-day

All figures come from the organizers themselves unless noted.

- **DartUP** - local Dart meetup:
  - by 2017, grown enough to rent an external venue, drawing 250+ people with eight talks
  - over ~5 years, became an international event hosting 500 offline and 1,500 online participants

  (Organizer Anton Anokhin, Medium.)

- **GopherCon** - debuted 2014 with exactly 700 attendees (co-organizer Brian Ketelsen: "In the end, we had 700 attendees"):
  - 1,300+ in 2015, after doubling venue capacity
  - ~800 in 2024

  Attendance fluctuates by host city and year - treat any single figure as point-in-time, not steady state.

- **RailsConf** - inaugural 2006 Chicago edition at roughly 400-600 attendees, "then just kept doubling year over year… something like 1,800 attendees in 2008" (DHH). Successor **Rails World** sold out a 1,000-attendee Toronto edition in under twenty minutes; its 2023 Amsterdam debut sold 700+ tickets in under 40 minutes.
- **North Bay Python** - inaugural single-track regional conference "planned in under 6 months, ran on a $40,000 budget" (PyCon US talk abstract). The budget benchmark for a credible first single-day event.

**What actually gates each jump** (sourced synthesis, not headcount):

- a meetup consistently outgrowing its free or borrowed venue
- enough quality local speakers to fill a curated day
- an organizer team willing to carry financial risk - venue deposits, contracts booked up to three years ahead (Strange Loop's Alex Miller)

The single-day → multi-day jump is gated by content depth and travel justification, not attendance: Strange Loop's own page argues "2-3 days is the sweet spot… 1-day conferences are not worth the travel time."

**Caveat**: RailsConf's and Strange Loop's endings were deliberate organizer-sustainability decisions (per DHH and Alex Miller), not format failures. Never cite either ending as evidence against the structures they ran.

## Single-track manifestos: five independent organizers, same choice

- **Strange Loop** (Alex Miller): "No marketing. Keynotes are never sold to sponsors. The conference mailing lists are never sold or given to sponsors." "Every year we turn down hundreds of excellent talks by excellent speakers in the service of creating a balanced program." (thestrangeloop.com)
- **GOTO**: "All talks are in the same room the first two conference days. The audience has a shared context as the curated story arc unfolds… you will get to know each other and the speakers much better." "Every talk… is chosen by a program committee… not sold to us. No sales pitches from the stage. And the speakers stay. Around 75% of them hang around on the days they're not speaking, so the hallway conversations are as good as the program."
- **Monktoberfest** (Stephen O'Grady, RedMonk): "Believing that some of the best content at any conference is the hallway track, we optimized for that. Start time was 10 AM." "We worked backwards from the capacity of our venue… Some things just work better at a small scale."
- **Deconstruct** (Gary Bernhardt): billed by its organizer as "an unusually independent software development conference"; described by attendees as single-track, no sponsors, hand-selected speakers (that description comes from attendee posts).
- **SmashingConf**: "We believe in thoroughly curated speakers and talks… No fluff, no fillers, no multi-track experience and no large hotel halls."

Five recurring reasons across them:

- shared experience everyone can discuss
- curation as editorial responsibility rather than offloading choice onto attendees
- the hallway track as a deliberate design goal
- refusing sold slots (keynotes, mailing lists, stage pitches) to protect attendee trust
- better speaker experience because speakers stay for the whole event

This is independent convergence - treat multi-track as a scale and attendee-agency decision, never a quality upgrade.

## DevOpsDays day architecture: the single-track/content-mix coupling

From the DevOpsDays organizing guide. Recommended daily order:

1. ~15-minute organizer intro
2. curated ~30-minute talks in the morning ("about 30 minutes have the right balance for content" - a chosen balance point, not a scheduling default)
3. 1-minute Gold-sponsor slots between talks (doubling as presenter setup time)
4. breaks
5. Ignite block after lunch
6. open space all afternoon, scheduled live on the day

Typical volume: four 30-minute talks per day plus a set of Ignites, all attendees in one room for the curated portion.

Two governance rules protect the structure:

- first-time organizers must consult a core organizer before altering it
- no sponsor may ever buy a speaking slot

The content-mix rule is coupled to the track choice: tool- and product-specific talks are steered to open space ("for specific tools talk, there are open spaces, not the main conference talks"), reserving the curated track for conceptual and cultural content.

A second curated track would need its own balance policy - the single track is what makes the rule enforceable. Track count and content mix are one decision, not two.

## Workshop-day ratios: per-event, never an average

Hands-on content is packaged as optional add-on days, not a fixed percentage. Report the ratios below as named-event examples; never invent an industry average.

- **SmashingConf**: "4 days, with 2 workshop days with 8 practical workshops, and 2 conference days… single track with 12 speakers, 300-400 friendly attendees"; San Francisco edition: 2 days, single track, 14 speakers, 8 workshops.
- **PyCon US**: tutorials as separate 3-hour paid sessions (historically ~$150 each) on dedicated days before three days of talks.
- **GOTO**: separates conference days from a masterclass day and frames the choice for attendees: "If you already know which problem you're trying to solve, do the masterclass. If you're scanning the landscape, do the conference."
- **DevOpsDays**: roughly half curated content, half self-organized, plus an optional pre-event workshop day with 45-, 90-, 120-, or 180-minute slots.

The workshop-day-plus-talk-day model is the dominant low-risk pattern once an event outgrows one day: it adds hands-on depth without diluting the curated track, and workshop days are separately ticketable - a real revenue lever, not only a content decision.

## Community vs vendor conferences at the session-selection level

- Community events (CNCF/Linux Foundation, DevOpsDays, NorthSec) run open CFPs and ban sales content explicitly: "Reminder: This is a community conference - so no product and/or vendor sales pitches"; NorthSec: "we do not accept sponsored talks." Blind CFP review is valued but not the norm - swyx (Netlify): "blind CFP review is important for some level of equity… In my experience, most CFP's are NOT blind."
- Vendor/user conferences run more invited content organized around the vendor's architecture, with sponsored keynotes; swyx: "Company sponsored conferences are often around a certain architecture… Scope is a little narrower and more 'vertical.'" (swyx.io)
- CFP economics benchmark (swyx, "CFP Advice", 2020, verbatim): "A rule of thumb is 8-12 speakers per day, per track… So a 3 day single track conference has a max of 36 talks." Applicant pools range "from an average 200 to something like 800-1200 for a JSConf" - an 8-30x oversubscription at a popular single-track conference is normal, not a broken CFP.
