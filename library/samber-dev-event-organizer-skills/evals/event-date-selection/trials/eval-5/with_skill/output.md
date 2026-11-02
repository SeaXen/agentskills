**Don't use Friday plus Saturday. Pick one audience pole for the dates.** The skill is explicit: a mixed audience has no day type that satisfies both groups. A Friday–Saturday compromise takes the worst half of each rule.

## 1. Day type and why

- **Professionals** go on a weekday. The DevOpsDays organizing guide says work topics belong to work life and weekends are "for refreshing energy with family". Friday is the day they are easiest to pull away from.
- **Students** go on a weekend. The MLH organizer guide says weekdays collide with class, exams and part-time work.
- **Friday and Saturday** is a boundary compromise. Neither guide endorses it, and Friday is the weakest day for both audiences.
- Saturday asks professionals to spend personal time on work. Friday asks students to skip class. Each group loses its own day.

## 2. Pick one of three routes

1. **Weekday pole (my recommendation).** Run Tuesday–Wednesday or Wednesday–Thursday, so neither day is a boundary day.
   - Reason: the compiler engineers at the big employers are the harder audience to move. They are also the likely source of sponsors and speakers.
   - Students get a student ticket and a student track. Expect fewer of them.
   - This is my judgment, not a documented rule. `event-positioning` owns that call.
2. **Weekend pole.** Run Saturday–Sunday and accept fewer professionals, who would be giving up family time.
3. **Split programme.** Run a weekday core for professionals, plus a Saturday student or community day (workshops, a hack day).
   - This costs a second day of logistics and a second volunteer roster.
   - It is the only route that serves both audiences on their own terms.

Whichever you pick, name the pole in the announcement. A mixed-audience date that doesn't name its pole reads as an oversight to everyone it disappoints.

## 3. The percentage estimate: there isn't a defensible one

- Neither source gives the size of the penalty. They say which day to pick, not how much a wrong pick costs. The skill says not to attach a percentage to it.
- Any number I gave you ("you'd lose 30%") would be invented. It would look like data and steer the committee wrongly.
- **How to get a real number, about 2 hours:**
  1. Send a 3-question poll to about 20–30 people from each audience, professionals and students separately.
     - Question A: "Could you attend a Friday + Saturday event? Yes, no or maybe."
     - Question B: "Could you attend Tue–Wed? Yes, no or maybe."
     - Question C: "Could you attend Sat–Sun? Yes, no or maybe."
  2. Ask 2–3 attendees from each group what else they plan to attend that season.
  3. If you have earlier events, compare registrations and no-show rates by day type.
- The poll gives you your own audience's "can attend" rate for each option. The committee can compare those directly.

## 4. Calendar checks: all outstanding

I did not browse or check any calendars, and I won't write dates from memory. Each category below is **outstanding**, not clear.

- **Both universities' published academic calendars** for the target year: exams, breaks, reading weeks.
- **Employer quarter-end and fiscal-year freezes** at the big local employers.
- **School holidays** in the region where attendees' children go to school.
- **England public holidays and bank holiday weekends** for the target year, taken from the official government page.
- **Manchester civic events** in each window: marathons, festivals, trade fairs, big football fixtures. They take venues, hotels and transit.
- **Competing and anchor events**, which I haven't scanned:
  - Check a cross-topic conference calendar (confs.tech is one example) and CFP listings.
  - Include compiler, systems, PL and LLVM/GCC-community events.
  - Include UK events, and the European events your travelling attendees would choose between.
  - Ask 2–3 attendees what else they plan to attend.
- **Piggyback or dodge** each hit:
  - Piggyback if a big event in the same city draws the same people.
  - Dodge if it competes for the same sponsors, speakers or venue.
- **Season:** treat any preferred season as a hypothesis to test against your own history. Short university breaks can raise turnout for a single weekend event, so check the specific break rather than the category.

## 5. Candidate windows

- I can't name valid windows until the checks in section 4 are done. Naming any now would be guessing.
- **Deliverable once they're done:** 3–5 surviving windows, each with the constraint every rejected window failed. Present them to venues as equivalent, not ranked.
- Ask each venue for its quiet periods. Put any counter-offer back through the section 4 checks before accepting.
- Don't fix a date first and then call venues.
- Hand the windows to `event-venue-sourcing`.

## 6. Announcement gate

- **Don't publish a date until you can handle money.** That means ticketing or a payment processor, an entity that can invoice sponsors, and a named owner. Teams that skipped this have rescheduled or cancelled.
- If the gate hasn't passed, decide the date internally and publish nothing.
- Once it passes, use **venue-locked** announcement: publish after the venue contract is signed and the money gate has cleared.
  - Use money-ready (publish before the venue is signed) only if another event is likely to claim your window first.
  - If CompilerCamp is a first edition, check `event-first-edition` before relying on a bare date. Hand the locked date to `event-planning-timeline`.

## 7. What I need from you

I need these answers to finish the date work:
1. **Is the first edition this one?** And is the target year 2027?
2. **Which pole?** Routes 1, 2 or 3 above?
3. **Money handling:** can you take payments today, and who owns it?
4. **Fixed constraints:** any sponsor, venue or anchor event that can't move?
5. **Hard deadline:** is there a date the event must land by?

**Next step (2 minutes):** send the committee the three-question poll from section 3. It replaces the percentage question with real numbers.