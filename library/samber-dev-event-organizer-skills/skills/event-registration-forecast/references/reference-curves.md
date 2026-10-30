# Reference curves

Generic curves for an event with no prior edition, their populations, and how to align any two curves. Each generic curve ships as a share curve (0 to 1 of the final) in `assets/`, readable by `scripts/forecast-registrations.py`.

## Contents

- Pooled lead-time curve
- Free-hackathon target timeline
- Paid-conference checkpoint ladder
- Choosing among them
- Aligning two editions

## Pooled lead-time curve - `assets/curve-pooled-lead-time.csv`

Source: PheedLoop Event Data Lab Report #09, 467 events and 216,282 timestamped registrations on one event platform, mostly North American. Registrations after doors (5.1%) excluded.

| Days out | Share already registered |
| --- | --- |
| 183 | 2.1% |
| 91 | 15.5% |
| 61 | 30.5% |
| 28 | 55.8% |
| 14 | 74.4% |
| 7 | 85.6% |
| 0 | 100% |

- The shares are cumulative sums of the report's lead-time bands; 28 is the four-week band edge, 61 and 91 stand in for the two- and three-month edges.
- The curve ends at doors: the 5.1% who registered after the event started are excluded. An event that sells at the door adds those from its own count, never from this curve.
- Median lead time 35 days pooled, **41 days for paid events, 16 days for free ones**. The pooled curve therefore runs ahead of a free event and slightly behind a paid one. Read a free event against it and expect to look behind until the last two weeks.
- Pooled, not split: the report publishes medians by posture, not a curve per posture.

## Free-hackathon target timeline - `assets/curve-free-hackathon-target.csv`

Source: MLH hackathon organizer guide, worked timeline for a 500-attendee goal (about 1,000 registrations, because about half of free registrants attend). It is a **goal timeline**, not observed sign-up data: a projection from it says where MLH's plan expects you to be, so label it target-shaped.

| Days out | Share of registrations at close |
| --- | --- |
| 91 | 0% (registration opens) |
| 61 | 10% |
| 30 | 25% |
| 14 | 60% |
| 7 | 100% (registration closes) |

- The curve is expressed against registrations at close, which the guide sets at double the attendance goal. Forecast registrations with it; convert to attendance with the free show-up rate, never with the paid one.
- The guide closes partner-event registration a week out, so the curve reaches 100% at 7 days on purpose.

## Paid-conference checkpoint ladder

Source: DevOpsDays organizing guide, against expected sales net of sponsor, speaker, organizer and volunteer comps.

- Early-bird close: about 15% of expected sales.
- Speaker or agenda announcement: about another 10%.
- One month out: 40-50%. A team that skipped its visibility push sits nearer 25-30% at the same point.
- The final two weeks carry a surge; that is normal.

The ladder is tied to milestones, not days-out, so it ships as no CSV. Use it as a check on whichever curve you run: at one month out, a projection implying under 40% already in is reading a surge the ladder does not expect. The guide notes these percentages shifted as social audiences fragmented; treat them as order of magnitude.

## Choosing among them

- Paid conference, first edition: pooled curve as the run reference, ladder as the check.
- Free hackathon: the target timeline as one reference, labelled target-shaped, and the pooled curve as the observed one; never the target timeline alone.
- Free meetup or free conference with open registration: pooled curve, read knowing free events register late (median 16 days).
- Never average two generic curves into one: each measures a different population. Run each as its own reference and let the spread form the band.

## Aligning two editions

- **Days-out, not calendar date.** Convert every reading to days before doors.
- **Moved milestones.** If the early-bird close or the speaker announcement moved, the spike moves with it. Compare the two curves at the same position relative to the milestone, and say which milestone you aligned on.
- **Pull-forward lull.** Every deadline pulls registrations forward and leaves a quiet stretch after it. A lull right after a price step is the step working.
- **Holidays and competing events.** A holiday or a competing conference inside the sale window shifts registrations around it. Name it on the curve rather than adjusting numbers silently.
- **Booking-window drift.** Hotel revenue-management research documents booking windows changing year to year. An older edition's curve can sit earlier than this year's; prefer the most recent edition and widen the band when only an old one exists.
- **Scale change.** A larger room or a new city changes the final, not necessarily the shape. Multiplicative pickup carries the shape across a change in scale; additive pickup does not.
