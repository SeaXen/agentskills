**Fix first: 14 May 2027 is a Friday. There is no Thursday 14 May.** Read the date line in the signed contract and check whether doors open Thu 13 or Fri 14. The plan below counts back from the event week, so a one-day shift changes nothing structural. Task F2 settles it.

**Estimates are my assumptions, not your data. Replace them in week 1.**

## Hours

- The plan totals about 446h: 206h for A, 210h for B, and 30h of weekly check-ins.
- At 6h per person per week you have about 340h. The gap is about 105h, before any contingency.
- At 8h per person per week you have about 450h. That fits with no slack.
- Estimates are ±30%. Task F4 fixes your real weekly hours.
- Owners are provisional. A is programme, web, marketing and volunteers. B is money, sponsors, venue and legal. Swap names freely.
- If you stay at 6h, cut in this order (about 30h saved) and keep the rest:
  1. P9, the embedded demo zone
  2. V5, the social evening
  3. M4, half the posts
  4. V6, swag reduced to lanyards
  5. S8, sponsor wave 3

## Weekly rhythm: re-forecast weekly, re-baseline at gates

Re-baselining weekly hides slippage, because each new baseline erases the last slip. So:

1. Freeze the baseline at G0 (end of week 3). Never edit it.
2. Hold one 30-minute check-in at a fixed slot every week.
3. For each task, enter the forecast end week. Compare it with the baseline and log the slip in weeks.
4. A task that slips 1 week is amber. A task that slips 2 weeks is red. A red task gets one decision that same meeting: cut it, buy it, give it to a volunteer, or move the date.
5. Compare hours left with hours available. If hours left exceed 85% of capacity, pull the next item off the cut list now.
6. Re-baseline only at a gate, and only as an explicit decision written in the log.
7. No task starts in weeks 11, 12 or 25 (Christmas and Easter). These weeks are catch-up buffers.

## Gates

| Gate | Date | Pass condition |
|---|---|---|
| G0 | Sun 1 Nov (end W3) | Contract dates extracted, budget v1, hours confirmed, baseline frozen |
| G1 | Mon 30 Nov (W8) | CFP open, blind-bird tickets live, sponsor wave 1 running, insurance bound |
| G2 | Sun 31 Jan (end W16) | CFP closed, at least 3× as many submissions as slots (target; adjust), keynote confirmed |
| G3 | Fri 26 Feb (end W20) | Acceptances out. **Budget go/no-go**: signed sponsors cover X% of fixed costs. Set X in F5 (start at 60%). |
| G4 | Thu 25 Mar (W24) | Schedule public, regular tickets on sale. Speakers confirmed by Fri 12 Mar. |
| G5 | Fri 30 Apr (W29) | Freeze on programme, numbers and signage. Final numbers sent to venue. |
| G6 | Fri 14 May | Event |

- **Ticket checkpoints:** set sold-versus-break-even targets for W20, W24 and W28 in F5. As a starting guess, use 25%, 50% and 85%.
- **Failed gate:** an unmet condition means a scope cut or a date decision. It never means "carry on and hope".

## Gantt

- Each column is one week, in groups of 5.
- `#` marks work. `G` marks a gate.
- Each row shows the owner and estimated hours.

```
    1     6     11    16    21    26    31
    12Oct 16Nov 21Dec 25Jan 01Mar 05Apr 10May
    ..G.. ..G.. ..... G...G ...G. ...G. G

FOUNDATIONS
F1  ##... ..... ..... ..... ..... ..... . B    4h  Extract every contract date/clause
F2  #.... ..... ..... ..... ..... ..... . B    1h  Confirm weekday vs 14 May with venue
F3  #.... ..... ..... ..... ..... ..... . A    2h  Last-year retro -> risk list
F4  .#... ..... ..... ..... ..... ..... . A    3h  Lock format, size, price, weekly hours
F5  .##.. ..... ..... ..... ..... ..... . B    8h  Budget model v1 (low/base/high)
F6  .##.. ..... ..... ..... ..... ..... . A    3h  Tracker + frozen baseline
F7  ..#.. ..... ..... ..... ..... ..... . A    2h  Cut list + kill triggers
F8  ..#.. ..... ..... ..... ..... ..... . A    2h  Check 2027 date clashes (other Rust/embedded events)
LEGAL AND MONEY
L1  ..### ..... ..... ..... ..... ..... . B    6h  Entity, bank, payments, VAT
L2  ...## ###.. ..... ..... ..... ..... . B    5h  Insurance quote + bind
L3  ....# ##... ..... ..... ..... ..... . A    5h  Code of Conduct + response process
L4  ..... ##... ..... ..... ..... ..... . B    3h  Privacy / UK GDPR
L5  ....# #.... ..... ..... ..... ..... . B    4h  Sponsor contract + invoicing
L6  ..... .###. ..... ..... ..... ..... . B    4h  Speaker agreement
L7  ..... ..### ##### ##### ##### ##### . B    9h  Monthly cash check, pay due dates
WEBSITE AND TICKETING
W1  ..##. ..... ..... ..... ..... ..... . A    8h  Site: date, venue, email capture
W2  ...## ..... ..... ..... ..... ..... . A    5h  Brand/social templates
W3  ....# #.... ..... ..... ..... ..... . B    6h  Ticketing platform setup
W4  ..... ...#. ..... ..... ..... ..... . B    3h  Accessibility info page
W5  ..... ..... ..... ..... .###. ..... . A    8h  Schedule + speaker pages
W6  ..... ..... ..... ....# ##### #.... . A    3h  Sponsor page + logos
W7  ..... ..... ..... ..... ...## #.... . B    4h  Visitor guide
PROGRAMME AND SPEAKERS
P1  ...## ..... ..... ..... ..... ..... . A    4h  Tracks, formats, committee spec
P2  ....# ##... ..... ..... ..... ..... . A    4h  Recruit review committee
P3  ..... ##... ..... ..... ..... ..... . A    6h  CFP platform + review rubric
P4  ..... .#... ..... ..... ..... ..... . A    3h  Speaker outreach + diversity plan
P5  ..... ##... ..... ..... ..... ..... . B    3h  Expense / fee / grant policy
P6  ..... ..#.. ..... ..... ..... ..... . A    3h  CFP opens (Mon 30 Nov)
P7  ..... ..### ..... ..... ..... ..... . A    6h  Invite keynotes + 10-15 targets
P8  ..... ..... ..### #.... ..... ..... . A    4h  CFP reminders
P9  ..... ..... ...## ##### ##... ..... . A    8h  Embedded demo zone (optional)
P10 ..... ..... ..... .###. ..... ..... . A   12h  Review rounds
P11 ..... ..... ..... ....# ..... ..... . A    5h  Selection, draft schedule, waitlist
P12 ..... ..... ..... ....# #.... ..... . A    4h  Notify accepted / declined
P13 ..... ..... ..... ..... ###.. ..... . A    5h  Confirm deadline, chase, waitlist
P14 ..... ..... ..... ..... .##.. ..... . A    4h  Speaker pack
P15 ..... ..... ..... ..... ..### ##... . B   10h  Speaker travel, hotels, visa/ETA
P16 ..... ..... ..... ..... ....# ##### . A    6h  Speaker check-ins
P17 ..... ..... ..... ..... ..... ...#. . A    3h  Slides in + backups
SPONSORS
S1  ..##. ..... ..... ..... ..... ..... . B    5h  Tiers, packages, income target
S2  ...## ..... ..... ..... ..... ..... . A    6h  Prospectus
S3  ...## ..... ..... ..... ..... ..... . B    6h  Target list (60 companies)
S4  ..... ##... ..... ..... ..... ..... . B    4h  Renew last year's sponsors
S5  ..... ####. ..... ..... ..... ..... . B    8h  Wave 1 outreach (30)
S6  ..... ..... ..### ##... ..... ..... . B    8h  Wave 2 + follow-ups
S7  ..... .#### ##### ##### ##... ..... . B   20h  Calls, negotiate, contract, invoice
S8  ..... ..... ..... ..... ####. ..... . B    5h  Wave 3 + in-kind swaps
S9  ..... ..... ..... ..... ..### ..... . B    4h  Sponsor onboarding pack
S10 ..... ..... ..... ..... ....# ##### # B    5h  Sponsor fulfilment tracking
MARKETING AND TICKETS
M1  ...## ..... ..... ..... ..... ..... . A    4h  Marketing plan
M2  ...#. ..... ..... ..... ..... ..... . A    3h  Save-the-date to last year's list
M3  ..... ..#.. ..... ..... ..... ..... . B    2h  Blind-bird tickets live
M4  ..... ..### ##### ##### ##### ##### . A   24h  Content, 1 post / 2 weeks
M5  ..... ....# ##### ##### ..... ..... . B    6h  Community partners + group tickets
M6  ..... ..... ..... ...## ..... ..... . A    5h  Speaker wave 1 + early-bird
M7  ..... ..... ..... ..... ...#. ..... . A    4h  Full programme + regular tickets
M8  ..... ..... ..... ..... .#### ###.. . A    3h  Listings + press
M9  ..... ..... ..... ..... ..... ####. . A    8h  Final push, employer groups
M10 ..... ..... ..... ..... ..... .#### # B    5h  Attendee comms (confirm, logistics)
VENUE AND LOGISTICS
V1  ....# #.... ..... ..... ..... ..... . B    6h  Venue kickoff + site visit
V2  ..... ...## ##... ..... ..... ..... . B    8h  AV, recording, wifi plan
V3  ..... ..... ...## #.... ..... ..... . B    5h  Catering + dietary
V4  ..... ..... ..... ..### ##... ..... . B    3h  Attendee hotel guide
V5  ..... ..... ..... ##### ##... ..... . B    5h  Social evening (cut candidate)
V6  ..... ..... ..... ..... .#### #.... . A    4h  Swag, signage, badges: design + order
V7  ..... ..... ..... ..... ...## ###.. . B    4h  Check-in system + badges
V8  ..... ..... ..... ..... .#### ..... . B    5h  Safety, first aid, risk assessment
V9  ..... ..... ..... ..... ..... ..#.. . B    2h  Final numbers to venue
V10 ..... ..... ..... ..... ..... ####. . B    8h  Run-of-show, minute by minute
V11 ..... ..... ..... ..... ..... ...## . B    4h  Supplies kit
PEOPLE ON THE DAY
O1  ..... ..... ...#. ..... ..... ..... . A    3h  Volunteer roles + headcount
O2  ..... ..... ...## ###.. ..... ..... . B    4h  Buy a production manager / AV tech
O3  ..... ..... ..... ##### ##... ..... . A    6h  Recruit volunteers
O4  ..... ..... ..... #.... ..... ..... . B    2h  Photo / video decision
O5  ..... ..... ..... ..... ..... ##### . A    8h  Volunteer brief, rota, training
O6  ..... ..... ..... ..... ..... .#### . A    4h  Comms + incident plan, CoC team
FINAL WEEKS
R1  ..... ..... ..... ..... ..... ...#. . A+B  4h  Freeze programme, numbers, signage
R2  ..... ..... ..... ..... ..... ....# . A+B  8h  Tabletop dry-run + venue walk
R3  ..... ..... ..... ..... ..... ..... # A+B  -   Load-in + tech rehearsal (Wed 12 May)
R4  ..... ..... ..... ..... ..... ..... # A+B  -   EVENT (Fri 14 May). Take leave Wed to Fri, plus Mon 17 May.
```

**After the event, outside the main baseline:**

| Task | Owner | When |
|---|---|---|
| Thank speakers, volunteers and sponsors | A | Mon 17 May, within 48h |
| Attendee survey, then sponsor report | B | W32–33 |
| Publish talk recordings | A | W32–36 |
| Close the books and pay suppliers | B | W32–35 |
| Retro, and a go/no-go on 2028 with the date held | A+B | W34 |

## Top 5 risks

| Risk | Early signal | Action |
|---|---|---|
| Speaker dropout | Confirm deadline missed | Keep a waitlist. Promote within 48h. Hold 2 reserve talks. |
| Sponsor shortfall | G3 below X% | Cut list, then smaller room plan, before spending on swag or social |
| AV or wifi fails | V2 test fails | Pay for AV or a production manager (O2). Test with a full room load in the Wed rehearsal. |
| Tickets below break-even | Misses a checkpoint | Group-ticket push (M5, M9), employer outreach, community discount codes |
| One of you gets ill or burns out | Hours burned over plan 2 weeks running | Run-of-show (V10) must let a stranger run the day. Cut scope before you cut sleep. |

## Tracker columns

Put these in one sheet, with the 83 rows above as the task list:

- ID, task, owner, hours
- baseline start week, baseline end week (frozen at G0)
- forecast end week, slip in weeks (forecast end minus baseline end)
- % done, status (green, amber or red)
- blocker, decision log

Add one summary cell for hours left versus hours available.

## Open questions

1. What are your real hours per person per week?
2. What are the names for A and B?
3. How many days, and how many attendees? I assumed one single-track day of roughly 150–250 people. Change F4 if wrong.

**Next action (5 minutes):** open the signed contract, read the event date line, and tell me whether it says Thu 13 or Fri 14 May. Then send me the answers to the three questions above.

I can turn this into an `.xlsx` with the Gantt, formulas and the weekly forecast sheet if you want.