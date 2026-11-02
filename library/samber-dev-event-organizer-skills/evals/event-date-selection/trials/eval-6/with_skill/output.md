# RustAtlantic 4: don't move the date, cut scope

Don't push the event back six weeks. I followed the `event-date-selection` skill, and it names this as a failure mode: **"Moving an announced date to rescue an unready plan."** It burns speaker, sponsor and attendee trust. It costs a recurring event (this is edition 4) far more than a one-off. Its answer is to cut scope instead.

## Why the six-week move is the wrong tool

1. **The date is already a promise.** Two months public means 180 people have paid, and some will have booked travel or time off. The skill's rule is that once a date is published, "the date holds and scope moves instead."
2. **The problems are program problems, not calendar problems.** You have no keynote, a late CFP and no workshop leads. A later date doesn't fill any of those slots. It only gives you more time to fill them, and you can get that time by cutting scope.
3. **"Most would be fine with it" is untested.** The people who aren't fine are the ones with flights, leave approved and an employer travel sign-off. These are working professionals on employer time, and they can't easily re-plan. I'd expect refund requests and no-shows to come from exactly this group, but that's my hypothesis, not data.
4. **A new date can break other things you haven't checked.** Six weeks later changes the season, the venue's availability and the competing-event field.
   - **Venue:** is the contract movable, and at what cost?
   - **Sponsors and speakers:** have they already committed to the current date?
   - **Calendars:** I can't say whether the new window hits holidays, employer quarter-end, school breaks or competing Rust and Atlantic-Canada events. Those checks are **outstanding**, and I won't guess at them. Under the skill's rules, "probably fine" counts as outstanding.
5. **180 of about 900 may not mean you're behind.** Conference sales usually back-load. Compare the 180 with the same point in editions 1 to 3 before treating it as a crisis. I don't have that data.

## How I'd play it instead

**Step 1: Measure before deciding (this week).**
- Plot sales at "date + 2 months" for each prior edition against this one.
- List what is actually missing: a keynote, N CFP talks, a workshop track.
- List what a viable minimum program looks like if nothing else lands.

**Step 2: Fix each gap inside the current date.**
- **Keynote:**
  - Invite directly. Rust core and library-team members, ecosystem maintainers and past RustAtlantic speakers are all candidates.
  - If a headliner doesn't land, run a panel or a "state of Rust in Atlantic Canada" opening, or give the slot to a strong CFP talk.
  - A keynote is rarely what drives ticket sales. A credible program is.
- **CFP:**
  - Don't extend it open-endedly. Set a hard close roughly 3 to 4 weeks out.
  - Pair that with direct invites to known speakers and a reviewed shortlist.
  - Hand any detail on the close date to the `event-cfp-design` skill, which works back from the locked date.
- **Workshops:**
  - Treat the track as optional.
  - Run 2 or 3 workshops, recruited from your own community leads and sponsors. Or move the whole track to a later satellite day or a separate edition.
  - If nothing lands by a set deadline, ship the main conference without it.
- **Tickets:**
  - Announce the program in stages as speakers confirm.
  - Keep early-bird pricing tied to a program announcement date.

**Step 3: Set a tripwire.** Pick a date, for example 4 to 5 weeks before the event, with explicit criteria:
- minimum confirmed speakers
- a minimum ticket-sales curve compared against past editions
- a venue and break-even check

If you miss them, the next move is still scope: a one-day event, a smaller venue room or a reduced track. Postponement is the last resort, not the first.

## If the team still wants to move after Step 1

Only consider it if all of these are true:
- The venue will move the booking cheaply, or you can't hold the original date.
- The program can't reach the minimum even at reduced scope.
- A sample of ticket holders, sponsors and confirmed speakers can actually make the new date.

If you go ahead, do it **once**, never twice. Make it a single announcement that covers the new date, a refund option for everyone and the reason. The new window must pass the full constraint checks first:
- audience calendars
- competing and anchor events
- the venue's availability

## Questions I need answered

1. What are the current date and the six-weeks-later date? That decides whether the season, weather and holiday calendars matter.
2. Is the audience mostly working professionals, with a weekday event? I assumed so.
3. Is the venue contract signed, and what does moving it cost?
4. Where were editions 1 to 3 at "date + 2 months"?
5. How many people are travelling in from outside Halifax, and have sponsors committed to this date?

## Outstanding checks

Nothing below has been verified. I can't browse from here, and your date and audience calendars aren't in the brief.
- Holidays and school breaks for the original and new windows, for Canada and for any country attendees travel from.
- Employer quarter-end and fiscal-year-end freezes.
- Competing events: other Rust conferences, adjacent-topic events and local Halifax events across both windows.
- The venue's alternative availability.

## Recommendation

Keep the date. Cut the program scope down to what you can deliver, hard-close the CFP, use direct invites for speakers, and make the workshop track optional. Set a tripwire for 4 to 5 weeks out. Move the date only if the venue, speaker, sponsor and attendee checks all clear.