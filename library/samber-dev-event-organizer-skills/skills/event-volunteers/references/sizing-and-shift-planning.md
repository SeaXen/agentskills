# Sizing the roster and planning shifts

Everything here is per-post arithmetic. The attendee count never enters it.

## Why a ratio is the wrong instrument

Volunteer-to-attendee ratios do not transfer between community conferences in the 100-1,000 range. The one figure that gets quoted is JSConf EU 2019: 6 core organizers, 8 MCs, 17 volunteers, ~1,600 attendees. That was the event's **final** edition, and its closing statement described the load as beyond "the limit of what can be responsibly handled by our volunteer team".

A ratio taken from an event that shut down under its own staffing is a floor observed at the moment of failure, not a target. Two independent problems come with reusing it:

- It describes one event's room count, format and venue.
- It describes a team that had already concluded the number was too small.

Do not quote it as a norm. If a user asks for a ratio, answer with a post list.

## The arithmetic

For each post (a position someone must physically be standing at):

```
shift-slots(post) = people needed simultaneously
                  x hours the post must be covered
                  / shift length
```

Then:

```
volunteers needed = ( sum of shift-slots across all posts )
                    / shifts one volunteer will take
                    + floater reserve
```

Three inputs. Shift length and per-post headcounts come off a published grid; shifts per volunteer has a published range but no fixed grid - your own sign-up form still answers it best for your event.

- **Shift length**: 2-3 hours is FOSDEM's standard on-site shift, across days running roughly 09:00-19:30 and 08:30-18:30. That gives 3-4 shifts per post per day.
- **People simultaneously, per post**: published anchors below.
- **Shifts one volunteer will take**: published volunteer programs cluster at two to three shifts. TechBBQ requires exactly two 6-7 hour shifts as a firm condition of volunteering; NAECON's sign-up form requires a minimum of three; IEEE's ICC and R5 Conference both treat two back-to-back shifts as the standard commitment, rewarding it with a meal rather than mandating it. Use two to three as a planning-stage anchor before sign-ups exist, but **replace it with your own sign-up form answers once they do** ("how many 2-3 hour shifts can you cover?") and sum the actual answers. Assuming a number after sign-ups have closed is where a roster silently comes out half the size it needed to be.

## Published per-post team sizes

All from FOSDEM's per-role pages (8,000+ attendees, 60+ devrooms, two days):

| Post                  | People per shift           | Notes                                                                      |
| --------------------- | -------------------------- | -------------------------------------------------------------------------- |
| Heralding (room lead) | 1-2 per main-track devroom | Rooms of 50-800+ people                                                    |
| Info desk, on-site    | 2-7 per shift              | Varies by desk; two physical desks, one primary and one secondary          |
| Runner (floater)      | 3-4 per shift              | Based in a staging area, waiting for task calls rather than holding a post |

Read the room-lead figure as per-room, not per-event: the multiplier is the number of rooms running simultaneously, which is why a three-track event needs three to six people standing in rooms at every hour of the programme.

PyCon US publishes a total rather than per-shift team sizes: "over 350 onsite volunteer hours" across the programme. This is the same arithmetic expressed as its output, and a useful sanity check on a roster once built. Multiply your shift-slots by your shift length and see whether the resulting hour count is plausible for your scale.

## The floater reserve

Treat the floater count as a real post, not as slack. FOSDEM's 3-4 runners per shift are exactly this: people with no fixed position, based in a staging area, absorbing whatever the schedule did not predict. Two consequences worth carrying:

- A roster with zero floaters resolves every surprise by pulling someone off a post, which is how a covered post becomes an uncovered one.
- Floaters are the right first place to promote a volunteer who turned out to be reliable, because the role's fit criterion is campus knowledge and willingness rather than a specific skill.

## Shift boundaries and arrival buffers

The shift grid is published with the buffer _inside_ the shift time, not as advice.

- FOSDEM: arrive at the info desk at least **15 minutes** before the shift to collect t-shirt and room assignment; be in the assigned devroom at least **10 minutes** before the first talk.
- PyCon US: Session Chairs in the green room **15 minutes** before the first session, or **30 minutes** if new to the role - a graduated buffer worth copying wherever a roster mixes returning and first-time volunteers.
- PyCon US Session Runners work in **15-minute** intervals per talk: meet the speaker 15 minutes before, walk them to the room 5 minutes before, hand off to the Session Chair.

A grid built without buffers is arithmetically full and operationally short by fifteen minutes at every handover.

## Setup, teardown and out-of-hours posts

These sit outside the event day and are easy to leave out of the arithmetic entirely. FOSDEM schedules them as distinct named tasks across four separate days around the event:

- Van loading: before.
- Buildup and signage: the day before.
- Cleanup: the final evening.
- Van unloading: after.

Each carries its own headcount and its own recruitment, and they are the posts where volunteers work longest and hardest - which is why they are also the ones FOSDEM feeds with full published meals rather than snacks.

Count them as posts. A roster that covers the programme and not the teardown ends with the organizing team carrying chairs at midnight.

## Worked example

A one-day, three-track, 400-person conference, 09:00-18:00, with a registration desk and a teardown.

| Post              | Simultaneous      | Hours | Shift length | Shift-slots |
| ----------------- | ----------------- | ----- | ------------ | ----------- |
| Registration desk | 3 (2 after 11:00) | 9     | 3            | 7           |
| Info desk         | 2                 | 9     | 3            | 6           |
| Room leads        | 3 (one per track) | 8     | ~2.7         | 9           |
| Floaters          | 2                 | 9     | 3            | 6           |
| Teardown crew     | 5                 | 2     | 2            | 5           |
|                   |                   |       | **Total**    | **33**      |

At two shifts per volunteer that is ~17 people, at one shift it is 33. The sign-up form's answer to "how many shifts?" is what decides which, and the honest planning move is to recruit against the pessimistic end and release people rather than to recruit against the optimistic end and cut posts.

This example is constructed to show the method. Its post list, hours and headcounts are illustrative; the shift length, the room-lead range and the floater pattern are FOSDEM's published figures.
