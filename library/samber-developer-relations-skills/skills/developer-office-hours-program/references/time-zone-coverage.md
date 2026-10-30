# Time-zone coverage

## Contents

1. Overlap method
2. Coverage patterns
3. Daylight-saving trap
4. Worked example: Europe-based hosts, US-based users

## 1. Overlap method

1. Split active users by time zone from product or docs analytics. Group into regions, not countries. Zones one slot can reach inside 09:00-18:00 count as one region.
2. For each region at or above 25% of active users (baseline), write its working window, 09:00-18:00 local.
3. Write the hosts' and the rotation engineers' working windows the same way.
4. Intersect with the largest region first. The overlap is where a live slot costs nobody an evening. Break ties toward the slot cheapest for hosts.
5. Overlap empty or a single instant: push the cost onto staff, not users. Take the slot at the hosts' end of day, agreed with them, and say which part of the audience still sits outside its window.
6. Write the chosen slot in every region's local time. A region outside 09:00-18:00 gets an async path or a second slot, never "watch the recording" alone.

Poll the audience before fixing the slot, as Kubernetes' calendar guidance recommends. Publish it in the largest region's time zone with a calendar link, and give UTC only next to a date.

## 2. Coverage patterns

The ranking and its starve line sit in SKILL.md Step 3, where the choice is made. What each pattern is:

- **One slot + async intake** - one session per cycle, questions accepted all week and answered in the write-up. Kubernetes fed its panel this way.
- **Alternating weeks** - early slot one cycle, late slot the next (Flux, GitLab People Analytics). Same hours as one slot; each region waits twice as long.
- **Two slots per cycle** - Kubernetes 14:00 and 21:00 UTC. Double the staffing; the pattern that broke first when panelists ran out.
- **Regional third edition** - only when a volunteer in that region asks to run it (Flux AEST bug scrub).
- **Follow-the-sun queue** - paid staff across regions (Stripe Discord). A support function, not a DevRel program.

## 3. Daylight-saving trap

- The EU changes clocks on the last Sundays of March and October.
- The US changes on the second Sunday of March and the first Sunday of November.
- Between those dates (two to three weeks in spring, one week in autumn) every Europe-to-US gap is one hour shorter than usual, whatever the host city: Paris to US East goes from 6 to 5 hours, Lisbon or London to US East from 5 to 4.
- Anchor the slot in the audience's time zone and let the hosts' local time move. A slot fixed in host time silently shifts an hour for users twice a year.
- Compute every gap from the hosts' own UTC offset. Never reuse another city's table: Lisbon and London sit one hour behind Paris.
- Calendar invites built on a named time zone handle this. A time typed into an announcement does not.

## 4. Worked example: Europe-based hosts, US-based users

Input: two DevRel staff in Paris (CET/CEST), users roughly 70% US (half East, half West), 20% Europe, 10% elsewhere. Weekly cadence requested. Hosts agree to finish late one day a week.

| Slot in host time | US East | US West | Verdict                                                      |
| ----------------- | ------- | ------- | ------------------------------------------------------------ |
| 14:00 Paris       | 08:00   | 05:00   | West Coast asleep - reject                                   |
| 16:00 Paris       | 10:00   | 07:00   | West outside its window                                      |
| 17:00 Paris       | 11:00   | 08:00   | West outside its window by an hour                           |
| 18:00 Paris       | 12:00   | 09:00   | Both US coasts inside 09:00-18:00; hosts finish around 19:00 |

The US 09:00-18:00 window and the Paris 09:00-18:00 window touch at a single instant (18:00 Paris, 09:00 PT), so the overlap is empty and the cost goes to staff.

Output:

- Anchor at 12:00 US Eastern (18:00 Paris most of the year). One late day a week for two hosts costs less than a 05:00 or 08:00 start for the largest user region.
- Europe at 20% sits under the second-slot trigger. 18:00 Paris is end of day for most of Europe: it gets the live slot when it can make it, and the async intake and write-up when it cannot.
- The 10% elsewhere, mostly outside its window at this slot, gets the async intake as its named path.
- Re-run the split after the pilot; add an alternating Europe-morning slot only if Europe reaches 25%.
- Hosts one hour west (Lisbon, London): the same 12:00 ET anchor lands at 17:00 local, inside the working day, so no late day is needed.
- Publish "12:00 ET / 09:00 PT" with a calendar link, never "18:00". Give a UTC time only next to a date: 12:00 ET is 16:00 UTC in summer and 17:00 UTC in winter.
