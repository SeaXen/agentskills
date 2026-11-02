# Field event plan template

## Contents

- Plan template
- Worked invite math
- Invitation and reconfirmation script
- Follow-up notes: good and bad
- 30/90-day review

## Plan template

```
Event: <format> during <conference>, <date, start-end>, <venue, walking distance from the conference>
Primary objective: <one of: move open deals | open accounts | expand or keep customers | recruit advocates | community ties>
Threshold (set before booking): show rate >= <x>% from past events, or "baseline" if none; guests with agreed next step at 30 days >= <n>; <for deals: stage movement at 90 days vs comparison group>
Why this format: <one line>; formats rejected: <format - reason>, <format - reason>
Host-conference check: sponsor status <y/n>; window <allowed?>; approval <needed / received on date>; invitation wording free of conference name and logo <y/n>
Seats: <total> = <external> + <internal>; invitations: <n> (ratio <x>, list warmth <warm/mixed/cold>); acceptance cap: <external + 1>; waitlist: <names>
Venue: F&B minimum <x>; guaranteed headcount due <date, aligned with last reconfirmation>; cancellation terms <read y/n>; deposit paid only after organizer approval
Internal hosts: <name - role - assigned guests>

Guest list
| Name | Account | Role | Seat reason (owner) | Owner | Compliance flag | Status |
|------|---------|------|---------------------|-------|-----------------|--------|

Schedule: invitations sent <date, 3-5 weeks out>; reconfirm <T-7>, <T-2>; waitlist offers as seats free up, last call <T-1>
Run of show: arrival 20 min; host opening 2 min (who, topic, attribution rule); facilitated discussion; close on topic
Follow-up: notes within 48 h by the host who spoke with each guest; review at 30 and 90 days
```

## Worked invite math

Input: seated dinner for 14, objective "move open deals", list half customers and half prospects who have met the account team once.

Output:

- Seats: 14 = 11 external + 3 internal (host engineer, regional sales lead, one customer-success manager), one host per four guests.
- Ratio: mixed warmth, so 3x the external seats: 33 named invitations.
- Acceptances: about half say yes (16 or so). Accept 12 (11 seats plus one), put the rest on a named waitlist in nomination order.
- Reconfirmation: expect up to a third of the 12 to drop out across the two reconfirmations; offer each released seat to the waitlist the day it frees up, with the day before as last call.
- What the ratio buys: 3x yields the seats plus a waitlist about a third the size of the table, which covers the expected drop-out. With colder names the accept rate drops and the ratio must rise to keep that waitlist.
- Sources: 11 customer advocates first, 14 account-owner nominations with a seat reason, 6 named target accounts confirmed attending, 2 anchor guests (a maintainer of a project the guests run, a customer's principal engineer).
- Comparison group for the 90-day review: the waitlisted accounts that never got a seat.

Input: practitioner roundtable for 10 at a community conference, objective "community ties", all guests contributors to an open-source project the company maintains.

Output: 8 external seats, warm list, 2.5x: 20 invitations sent by the maintainer, not by marketing. No account owners: the objective has no deal step, and follow-up goes to DevRel.

## Invitation and reconfirmation script

```
// ✓ Good - from a named peer, topic and city in the title, no conference name or logo, why them, how many, what it is not
Subject: Stateful workloads dinner, Salt Lake City, Wednesday 11 November

Priya, while we're both in town this week, I'm hosting 10 platform leads for dinner on Wednesday, 19:00, a ten-minute walk from the convention center.
The topic is the one your team wrote about: stateful workloads after the operator rewrite.
No slides, no pitch, Chatham House Rule: we may share themes afterwards, never who said what or who was there. Would you join us?
- Sam, principal engineer, <company>

// ✗ Bad - brand alias, conference logo, product-led, no reason this person
From: events@<company>
Subject: Join <Product> at our exclusive KubeCon VIP Dinner!
Discover how <Product> accelerates your cloud-native journey...
```

Reconfirmation, a week out and two days out, from the same person: one line naming the time and place, an easy "can't make it" reply, and an offer to send a colleague instead.

## Follow-up notes: good and bad

```
// ✓ Good - names what the guest said, offers the step agreed in the room
Priya, thanks for last night. Your point about failover drills after the operator upgrade stuck with everyone.
You mentioned your team would look at our backup tooling: I've asked Lee, who built it, to send you the design doc today.

// ✗ Bad - generic, sales-sequence opener, no next step the guest agreed to
Hi Priya, great to meet you at our KubeCon VIP dinner! I'd love to book 30 minutes to show you how <Product> can help.
```

## 30/90-day review

- 30 days: show rate, guests with an agreed next step, next steps completed. Compare with the threshold.
- 90 days (deal objectives): stage movement of attendee opportunities versus opportunities nominated but not seated. Name the comparison group and its size.
- Verdict: repeat the format, change the guest-list method, or drop the format. Record why, with the show rate, for the next conference.
