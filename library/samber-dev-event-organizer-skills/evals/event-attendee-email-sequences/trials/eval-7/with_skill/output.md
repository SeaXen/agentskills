# QueryCraft Conf email segmentation: recommendation

**Decision:** Reject Plan A. Do a trimmed version of Plan B. Collect the three form fields, but don't use them to segment every email. Segment on role and registration state instead, using fields your newsletter tool can filter on.

I read the skill and all four of its references. I haven't drafted any email copy, so there is no humanizer pass yet.

## Inputs I'm assuming (correct me if wrong)

- **Event:** Wed 3 March to Thu 4 March 2027, Berlin. You didn't give the year. That is roughly 20 weeks from today, so the runway is not compressed.
- **Team:** two volunteers. The newsletter tool can filter a list by a field, but has no behavioural automation.
- **Registration:** open until sold out. There is no dated early-bird or price cutoff, so there is no last-call email.
- **Dates and positioning:** the announcement date, agenda-release date and the weight email carries come from your marketing plan. I take them as given. I haven't set or moved any date.

## Plan A: resend to non-openers after 3 days. Don't do it.

1. **It's a behavioural trigger.** The skill deletes behavioural drips and behavioural segments outright. Every send here fires on a calendar date, not on what a recipient did.
2. **"Non-opener" is unreliable.** Mail clients have pre-loaded images since 2021 and fire a false "open". Some real readers also never register as openers. You would resend to the wrong people.
3. **It nearly doubles your volume.** The only event-organizer benchmark found is 21-30% opens. Taken at face value, 70-79% of the list would be "non-openers" and get everything twice. That is the countdown-chain pattern, which exceeds every sourced cap and teaches people to ignore the one email that matters.
4. **"Every email" includes the wrong sends.** That would cover the confirmation (transactional), the know-before-you-go and the day-before nudge. A tweaked subject on those makes the email harder to find in an inbox. Subjects should name the event plainly.
5. **Your tooling doesn't support it.** The skill expects a plain filtered list, not open-tracking logic.

If registrations are behind your checkpoint, the sourced fix is the **registration follow-up**: at most 1-2 sends to people who have not registered, cross-referenced against the registered list. It is date-based and capped, and no registrant is ever asked to register. A soft curve is a marketing-plan diagnosis, not a reason for a fifth reminder.

## Plan B: collect the fields, but don't segment on them

**Attribute segments are the skill's "starved option".** They rank top on value and effort, so efficiency never picks them for a 2-person team. They also carry the only compliance cost on this menu. Applying them to every email is the wrong shape.

**Dietary and accessibility needs:**
- Collect them, but as operations data. The caterer and venue need them.
- Every attendee gets the same line in the know-before-you-go email. Dietary handling and accessibility are both required content.
- State what must be requested and by when. Dietary and accessibility requests often need about two weeks' notice, so the email must ask early.
- Don't make them filterable fields in the newsletter tool. Keep them in the registration export and share them only with the caterer and venue contact.
- These are health-adjacent personal data, and Berlin means EU rules. Before you go live, get sign-off on:
  - the lawful basis and explicit-consent wording on the form
  - a retention and deletion date, for example deleted a fixed number of days after the event
  - who can see the data

  I'm not giving a legal ruling here. The skill says to check the current rules and get sign-off, and a field once collected cannot be un-collected.

**First-timer vs returning:**
- Only worth building if first-timers are a large share and orientation is an explicit goal for the event, or if many attendees travel internationally. I need your answer to the question below to decide.
- If yes, send one extra "first time? start here" paragraph in the know-before-you-go email only. Don't create a parallel sequence.
- If no, drop the field.

## Setup that fits two volunteers

**Fields in the newsletter tool:**

| Field | Values | Why |
|---|---|---|
| `role` | attendee / speaker / sponsor / volunteer / judge | Role split at the week-before send. You write the attendee variant only. Speakers and sponsors have their own comms owners. |
| `registered_2027` | yes / no | Registration-state segments. This stops "register now" reaching a paid attendee. |
| `prior_edition` | yes / no | Separates last year's attendees. Only mail them if their opt-in is documented. |
| `consent_marketing` | yes / no | A ticket purchase is not marketing consent. |
| `consent_source`, `consent_date` | form name and edition, date | Provenance per address, so the list survives an audit. |

**Saved segments:**

- **S1, registered attendees:** `role=attendee AND registered_2027=yes`. Gets confirmation, know-before-you-go, day-before nudge and post-event thank-you.
- **S2, not yet registered:** `registered_2027=no AND consent_marketing=yes`. Gets announcement, agenda release and at most 2 follow-ups.
- **S3, prior edition:** only addresses with a recorded opt-in. If the opt-in is missing, don't send. This is the one send here that can't be taken back.

**Process:**
- Before each S2 send, re-export registrations from your ticketing tool and refresh `registered_2027`. There are few sends, so manual is fine.
- Volunteer 1 builds the filter. Volunteer 2 checks the recipient count against the expected number and confirms no registrant is in S2.

## Dated send map

Announcement and agenda-release dates are from your marketing plan and are shown as TBC.

| Send | Date | Segment |
|---|---|---|
| Announcement | TBC (marketing plan) | S2, plus S3 if consent passes |
| Registration confirmation | On registration (transactional) | Each registrant |
| Agenda / speaker release | TBC (marketing plan) | S2 |
| Registration follow-up, max 2, only if the curve is behind | Date-based, your call | S2, cross-checked against registered |
| Know-before-you-go | Wed 24 Feb 2027 | S1 (attendee variant) |
| Day-before nudge | Tue 2 Mar 2027, evening | S1 |
| Post-event thank-you | Fri 5 Mar 2027 | Everyone who registered, no-shows included |

- **Last call:** dropped, because there is no dated cutoff. A true live figure such as "X% of seats taken" can go in the announcement or agenda release. Don't build a countdown to "sell out".
- **Cap check:** a registered attendee gets about 4 sends after registering (the know-before-you-go, the day-before nudge, the post-event thank-you, plus the confirmation). A non-registrant gets at most 4 (announcement, agenda release, two follow-ups). That is inside the sourced 2-4 reminder cadence.
- **Second automated email:** if a separate tool will email attendees, for example a code-of-conduct reporting tool, name it and its timing in the send before it. Otherwise it gets reported as phishing.

## Questions that would change this

1. Is the event ticketed or free? Free carries a 30-50% signup-to-attendance drop-off, which makes the reminders more important.
2. Is there a prior-edition list, and where did each address come from? Which form, which box was ticked, and when?
3. What share of attendees are first-timers, and how many travel internationally? This decides whether the first-timer field is worth building.
4. Where do the on-site facts come from? Check-in location, badge policy, dietary mechanics and accessibility provisions must come from your attendee-experience plan. I haven't invented any of them.

## Measure after the event

Pick two of these before the event and write down what each would change next edition:
- desk questions the email already answered, counted at check-in
- late dietary or accessibility requests (the email asked too late)
- unsubscribes and complaints per send

Don't set an open-rate target. The one benchmark is too weak to use as a pass/fail bar.

## If the real worry is no-shows

The reminder emails above are the lever this skill owns. Overbooking, waitlists and deposits belong to `event-no-show-management`. That handoff was written from this skill's side only and isn't agreed from the other side.