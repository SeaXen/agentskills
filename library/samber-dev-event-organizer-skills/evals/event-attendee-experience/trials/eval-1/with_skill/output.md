# DevHarvest 2027: reviewed and tightened day-one arrival plan

I read the skill and all three of its references. The plan has four problems. Each one is a known failure mode, so each gets a specific fix below. Anything I invented rather than took from published practice is marked **(self-set)**.

## Verdict on the four decisions

| Your plan | Verdict | Fix |
|---|---|---|
| One long table for check-in, t-shirts, walk-in registration and questions | ❌ Rejected | The skill deletes this design outright. It fails in the busiest ten minutes of the day. Split it into four stations. |
| Badges alphabetical by first name | ❌ Change | Sort by last name, then first name. Check-in lists, confirmation emails and ID are all keyed to last name. Pre-sort the night before. |
| Shortened walk-in form (name and email) | ❌ Change | Walk-ins fill in the full form, in their own slower lane. Skipping fields saves about 90 seconds and loses the dietary answer, the shirt size and the consent record. |
| Sponsor tables just inside the entrance | ⚠️ Conflict | The desk must sit clear of the sponsor queue. Your entrance hall is single and shared, so this is the main layout risk (see below). |

## 1. Check-in model

Use **pre-sorted pickup with a walk-in lane**, promoted one rung to **multiple lanes**. The skill's trigger for promotion is a door-open rush bigger than one queue, or a real ticket-category split. You have both.

- **Rush size:** 650 people in about 45 minutes is roughly 14 per minute on average. The peak will be higher, because people cluster just before the keynote.
- **Ticket split:** about 40 sponsor-comp tickets.

### Six volunteers, assigned **(self-set)**

| # | Station | Job |
|---|---|---|
| 1 | Pickup A | Last names A–H. Finds the badge, ticks the name on the list, hands over the badge. |
| 2 | Pickup B | Last names I–P. Same job. |
| 3 | Pickup C | Last names Q–Z. Same job. |
| 4 | Walk-in lane | Full form, payment, badge made on the spot. Paid walk-ins only. Expect about 30. |
| 5 | Swag table | Separate from check-in. Attendees pick their own size from stacks sorted by size and style. |
| 6 | Help point and floater | Handles questions, "I can't find my badge" lookups and lost property. Never works the queue. |

- **Adjust the alphabet split to your list.** Count surnames per range from the registration export. Don't assume equal thirds.
- **Surname prefixes:** decide how "van der Berg" and "de Vries" file, and put that rule on a card at each pickup station. This is common in Dutch names.
- **Sponsor-comp badges:** keep them as a separate stack, 40 badges. Build the split to tolerate confusion. Published practice (DevOpsDays) flags that some attendees don't know which ticket category they have.
- **"Not found" fallback:** if a name isn't in the main stack, the volunteer checks the comp stack. If it still isn't found, the attendee goes to volunteer 6 for a searchable lookup.
- **Escalation:** name one organizer on duty (not one of the six). Volunteers send anything they can't resolve to that person.
- **Staffing:** published practice says staff the desk continuously with people willing to miss talks. Name the people and the shifts. Don't assume.
- **Swag:** a separate table is required here. Check-in is your constraint, and the reference says swag goes to the desk only if the desk isn't the bottleneck.

### The walk-in lane in detail

- **Full form:** include dietary needs, shirt size and consent. Those fields have to be collected at the door, or you can't serve those walk-ins properly later.
- **Badge for walk-ins:** badges are already printed for the registered 650. For walk-ins, either bring a printer or keep about 40 blank badges and a marker. **(self-set)** Decide before Saturday which one you're doing.
- **Meals and shirts for walk-ins:** catering headcount and shirt counts must include them. Pad shirt counts by up to 30% per size and style (published practice).
- **Payment:** card terminal tested, and a fallback if it's down. **(self-set)**

## 2. Layout: the sponsor-table conflict

You have one entrance hall, and the sponsor tables sit just inside it. The reference says to place the desk against the opening rush and keep real distance between it and the sponsor tables, so the two queues don't congest each other in the first ten minutes.

1. **Draw the actual floor plan** with the entrance, the sponsor tables, the three pickup stations, the walk-in lane and the swag table.
2. **Run the queue direction** away from the sponsor tables. Count how many people fit in the line before it reaches them.
3. **If it doesn't fit,** move the pickup line out of the entrance hall (into a side corridor or foyer) rather than shrinking the line.
4. **Keep the sponsor tables staffed but not required.** Nobody should have to pass a sponsor table to reach their badge.

I can't tell from the description whether this is fixable without moving something. That is the first thing to check on the floor plan. Don't reopen square footage with the venue. Work inside the signed plan.

## 3. Badge and scanning posture

You didn't say whether any sponsor was promised lead capture. This must be decided before anyone touches the printed badges.

- **Default: name badge, no machine-readable code.** Zero exposure, zero build. This is the published stance (DevOpsDays strongly discourages scannable badges).
- **Rule above everything:** never give or sell attendee contact lists to sponsors. This is also a GDPR matter in the Netherlands.
- **If a sponsor contract already promises scanning:** then all four mitigations apply together:
  1. Informed consent collected at registration, before the badge was printed.
  2. A physical sticker that covers the code, for opt-out.
  3. Sponsors told in writing that scanning without consent is not allowed.
  4. The code on the back, with two-point lanyard attachment so it faces inward.
- **⚠️ Badges are already printed.** If a code is on the front, or consent wasn't collected at registration, you have a problem to fix before Saturday. Check the printed badge and the contracts today.
- **Never encode attendee data directly in a QR.** Any scanner in the building can read it.

## 4. Dietary and t-shirts

Neither came up in your plan, and both fail silently.

- **Dietary:** if you collected restrictions, serve those meals from a separate table with a printed name checklist. Restricted meals in the general line get taken by the wrong person. Walk-ins who declared a restriction at the door must be added to the list that morning.
- **Categories:** use the ones your accessibility bar committed to. I haven't invented a list.
- **Health data:** dietary answers count as health data under GDPR. Keep the distribution list to the meal service and destroy it after the event.
- **T-shirts:** sizes were asked at registration (confirm). Extend past 2XL to 3XL–5XL, and offer a fitted cut that looks the same as the standard shirt.
- **Meal service:** use multiple serving tables, never one. Check names at the head of the line.

## 5. Questions and the help path

Questions move off the check-in table to **volunteer 6** at a visible help point near the entrance. Staff there wear something recognisable. That point answers room locations, schedule changes, lost property and practicalities.

- **Lost property:** give it a named owner and a stated end-of-event disposal.
- **Escalation:** the organizer on duty. If your code-of-conduct plan already names an on-duty responder, make that person the same one. Confirm.

## 6. Wayfinding, quiet room and first-timers

You didn't mention any of these. Check each before Saturday.

- **Signs:** put the first sign before the first choice. People standing with a badge in their hand after check-in need to know where the keynote room is. Sign by destination ("Keynote, main hall"), not by room code. Show the accessible route on the sign itself.
- **Decision points:** count them on the floor plan, not the building's rooms. Add toilets, water, food and the quiet room to the signs.
- **Quiet room:** needs a real door, not a curtain, and must be reachable without crossing the main thoroughfare. Sign it plainly as "Quiet Room". The code-of-conduct team may use it for confidential intake, so it has to work for both purposes. Confirm it exists in the signed plan.
- **First-timers:** offer orientation, don't assign it. Put a line on the back of the badge or offer a different lanyard. Give the first twenty minutes a destination with a person in it. Print the three unasked questions on a card: where do I sit, can I leave a talk partway, and what happens in the hallway track. Never run first-timers as a separate track.

## 7. Day two

Everyone should already have a badge by day two. Don't run the full desk again. Keep one station for lost or forgotten badges and late arrivals. **(self-set)**

## 8. Pre-Saturday checklist

1. **Today:** check the printed badges for any code on the front, and check sponsor contracts for promised scanning.
2. **Today:** count surnames per alphabet range, and write the rule for surname prefixes.
3. **Floor plan:** mark the sponsor tables, the three pickup stations, the walk-in lane, the swag table and the help point. Check the queue direction.
4. **Walk-in kit:** full paper or digital form, blank badges and a marker (or a printer), a tested card terminal.
5. **Pre-sort the badges** the night before, in two stacks (regular and sponsor-comp).
6. **Dietary:** a printed checklist, a separate table, and walk-ins added to the list.
7. **Signage list** keyed to decision points. Get it approved before anything is printed.
8. **Name the organizer on duty,** and the volunteer shifts including breaks.
9. **Do the walkthrough in the actual building** before doors open, using the table below.

## 9. Walkthrough audit: rows I expect to come back bad

| Touchpoint | Pain point | Fix before doors open |
|---|---|---|
| Arrival | One entrance hall shared by 650 arrivals and the sponsor tables | Queue direction away from sponsors, as in section 2. Sign the entrance from outside. |
| Check-in | Alphabet ranges uneven, so one station queues while two sit idle | Split ranges from the real surname count. Floater redirects people. |
| First wayfinding decision | Nothing signed between the desk and the keynote room | One sign at the first junction, by destination. |
| Swag | Shirt sizes run out or the table queues | Pad counts by 30%. Table separate from check-in. |
| Help moment | Questions go to whoever looks least busy | Visible help point, volunteer 6. |

The point of this table is that it's started on paper first, then repeated by physically walking the building. The rows that look fine on paper and fail on the walk are the valuable ones. Keep the finished table for next year.

## 10. Questions I need answered

I assumed defaults where these were open. Each answer could change the design.

1. **Has any sponsor been promised badge scanning or lead capture?** This decides the badge posture. It is the most urgent, because the badges are already printed.
2. **What dietary categories and accessible-route bar were set?** I didn't invent them.
3. **What register did the culture work set** (warm and chatty, or efficient and quiet)? This sets how the volunteers greet people.
4. **Is the quiet room in the signed floor plan,** and does the code-of-conduct plan name an on-duty responder?
5. **Last change dates:** badge reprint, signage print, catering headcount.
6. **Do any ticket categories beyond sponsor-comp** (speakers, press, students) need their own lane? I treated speakers as out of scope. They have their own journey.

## 11. Measure two things

Pick two and write down what each would change next year, before doors open:

- **Longest check-in queue and the hour it happened.** This tells you whether three pickup stations was the right call.
- **Signs added by hand on the day.** Each one is a decision point the wayfinding missed.

If you record only two, record those. Dietary meals that went unclaimed or to the wrong person is a third worth counting. For dietary, the target is zero misses.