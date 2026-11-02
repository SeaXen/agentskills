# HaldeCon hospitality brief (draft v1)

400 people, two days. ⚠️ This is a draft. Seven inputs are missing, listed at the end, and I used defaults where I had to. Nothing should be ordered until you approve each section.

**Scope check.** The skill owns five things: service style, break content, alcohol posture, the evening programme, and the shared floor. Your five asks split like this:

| Ask | Owner | What I deliver |
|---|---|---|
| (5) Lunch format | This skill | A decision, in section 1 |
| (4) Lunch 45 → 75 min | `event-schedule-design` | A service-window requirement, in section 2 |
| (3) Meal-line placement and signage | `event-attendee-experience` | Input requirements, in section 3 |
| (1) Speakers' dinner | `event-speaker-experience` | The dietary inputs it needs, in section 4 |
| (2) Attendee hotel block | `event-venue-sourcing` (contract term) or `event-accessibility-inclusion` (means-tested grant) | An argued refusal, in section 5 |

## 1. Lunch format (ask 5)

**Recommendation: individually packaged labelled meals, one item per person, name-matched for every declared restriction.**

- At 400 people, a single buffet line is the main queue risk.
- This style carries a restriction as a labelled object, so no one depends on anyone's vigilance.
- It has the highest throughput per volunteer.
- It matches the separate-table fulfilment model in `event-attendee-experience`.

**Upgrade path.** Move up one rung to a self-serve buffet with posted allergen labelling only if all four of these hold:
1. The 75 minutes is confirmed in the grid.
2. The room has space for several parallel lines.
3. The declared dietary counts are thin enough that a labelled station works without per-person matching.
4. The venue allows the equipment.

For a buffet, allergen detail is posted before the line forms, for example at check-in. Treat that as a hard requirement.

- ❌ **Deleted:** the unlabelled buffet. It looks like the cheap version of the labelled one, but the missing declaration lands on the one person it was for.
- ❌ **Not on the table:** family-style platters (the wrong shape at 400 people) and plated service (it needs seats for everyone, and some suppliers require their own staff to serve).

**Fallback per uncovered restriction:**
1. A one-off addition to the standing order. This is the default.
2. If the supplier cannot cover it, tell the person well in advance and give them a delivery credit.

Never discover a gap at the serving table.

**Handover step.** Name one person to capture allergen and dietary detail when each delivery is received, and carry it through to labelling. Labels fail upstream, at the handover, more often than at the serving line.

## 2. The 45 → 75 minute lunch (ask 4)

- I don't move or lengthen a slot. `event-schedule-design` owns the grid, so the stretch to 75 and the push of afternoon talks goes to it as a change request. You decide it. I only supply the requirement.
- **Requirement handed over:** a service window long enough for 400 people to be served and to eat, in whatever style section 1 settles on.
  - Packaged meals shorten the queue because service is handing over an item. This may mean 45 minutes is workable for packaged service and 75 is only needed for a buffet.
  - **Decide the style first, then the length.** If you keep packaged meals, the case for pushing the afternoon back is weaker. If you choose a buffet, it is stronger.
- If lunch moves, the afternoon break moves with it. Break service times then follow the new grid.
- The venue may also fix catering windows. That is your Q1: take those windows as given.

## 3. Meal-line placement and signage (ask 3)

Floor-plan placement and wayfinding belong to `event-attendee-experience`. Giving it the placement would duplicate its job. What I hand over:

- **Style:** packaged labelled meals, or a labelled buffet if the upgrade conditions hold. This sets how many pickup points it needs.
- **Peak-queue risk:** the lunch peak at 400 people. Record the longest queue in minutes each day. That figure is the evidence for next edition.
- **Declaration rule:** allergen detail is readable before anyone reaches the front of the line, and restricted meals are distinguishable at pickup.
- **Hard constraint to carry into the floor plan:** the corridor must stay clear. The line has to form in a space that can hold it. That choice is theirs to make, not mine.
- **Venue check:** ask whether the corridor is a fire-egress route. If yes, queue space is a safety constraint, and `event-vendor-sourcing` and the venue own the fire-code answer.

## 4. Speakers' dinner (ask 1)

I can't draft a menu. A speakers' dinner is a named population's top-up, and it lives in `event-speaker-experience`. It isn't part of the shared floor, and I don't know which bistro you mean.

What I can supply to that skill:
- Speakers go into the same dietary-count collection as everyone else. Collect their restrictions now, in the same pass.
- Alcohol at the dinner is the bistro's own service. The event-level posture in section 6 governs only event-hosted service.
- Hand `event-code-of-conduct` the venue, time, and attendee list, since an off-site dinner is a scope-clause question.

**Open item:** tell me which bistro and what you want from it. I can route that to the speaker skill with these inputs attached.

## 5. Attendee hotel block (ask 2)

**Not a hospitality decision.** The skill says so deliberately, and I'm not inventing a standard.

- **A room block** is a contract term, owned by `event-venue-sourcing`. It needs a negotiated rate, an attrition clause, and a cutoff date.
- **A discounted-room grant** for particular people is means-tested access, owned by `event-accessibility-inclusion`.
- **Speaker travel** is already covered in `event-speaker-experience`.

Route it to venue sourcing with these inputs: 400 attendees, 2 nights (to confirm), and the expected-show-up figure rather than the registration count.

## 6. Breaks, alcohol, and the evening

**Break content.** Default: owned replenishment at each break. One named person restocks against the grid's break times, with water and hot drinks refilled before each break. Never a station set once in the morning and left. Upgrade to a snack-enhanced break only if a gap is long enough that people leave the building.

**Sizing (catering-industry convention, order-of-magnitude only).** Use the expected-show-up figure, not 400.
- Morning: about 85% drink coffee, at about 1.5 cups each.
- Afternoon: about 50%, at about 1 cup each.
- Add a 10–15% buffer.
- Refresh every 3–4 hours on an all-day event.
- Starting split: 70% regular, 20% decaf, 10% tea or hot water. Adjust it to this audience.
- Check every figure against the caterer's quote.

Examples at 400 people, as an upper bound only: about 510 cups in the morning and about 200 in the afternoon, before the buffer.

**Alcohol posture.** Default: no alcohol served. It is a deliberate posture, not an omission, and it needs no licence or insurance question. Move to bounded hosted service only if you have an evening owner and your audience's norm includes drinking. In that case:
- Alcohol is capped by hours or tokens, with someone named to hold the cap.
- The alcohol-free option is served at the same table, by the same person, and is made, not left over.
- Under-forecasting soft drinks is the usual mistake: alcohol-free events shift volume, they don't reduce it.
- The posture goes to `event-risk-management` and `event-code-of-conduct` before any evening venue is held.

**Evening programme.** Not decided: it needs an owner. If no named person owns the evening, delete everything except "no organised programme" and publish that.
- If you have an owner: a venue-based mixer in your own space, right after the last session. It is free to attend, runs two hours at most, and has a published start and end.
- Either way, publish the decision, including "the day ends at the last session". Silence sends people to an unhosted bar.

## 7. Inputs needed before any order

1. **Expected-show-up number** from `event-no-show-management`. Is 400 registered or expected?
2. **Dietary categories** the event commits to, from `event-accessibility-inclusion`.
3. **Counts from everyone fed:** attendees, speakers, volunteers, organizers, and sponsor staff.
4. **Venue answers:** mandated caterer? Open flame or chafing dishes? Outside food? Who may serve? Seated capacity? Is the corridor an egress route?
5. **Sponsorship:** has anyone bought the coffee or lunch as a branded surface?
6. **Evening owner and budget:** who owns it, and is there a budget line?
7. **Decision dates:** the headcount guarantee date, and the venue hold date for any evening.

## 8. Metrics to record

Pick two and write down beforehand what each would change.
- Longest lunch queue and its peak minute each day.
- Dietary fulfilment: zero misses is the gate.
- Covers ordered against covers eaten, returned to `event-no-show-management`.

If you answer the seven inputs above, I'll turn this into a final brief. I'd start with the venue's mandated-caterer and corridor answers, since they decide the lunch style.