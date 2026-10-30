# Published schedule benchmarks

Two real published conference schedules, read as structural evidence. Read them as two different answers to the same congestion problem, not as defaults to copy.

## Contents

- FOSDEM 2026: density at ceiling scale
- PyCon US 2026: slack bought by staggering
- The two strategies side by side
- Energy-curve pacing and graveyard slots: named sources
- What a published grid does not tell you

## FOSDEM 2026: density at ceiling scale

FOSDEM 2026 published schedule (the canonical `fosdem.org/2026/schedule/` redirects to `archive.fosdem.org/2026/schedule/`).

**Scale**

- 37 rooms, 71 tracks, 1,079 events across two days.
- Two designated main tracks ("Janson" and "K.1.105 (La Fontaine)") run both days - even at 37 rooms, a small number of flagship rooms function like a mini shared track inside the wider grid.
- A separate "room occupation by track" overview is published alongside the grid. FOSDEM treats room-to-track capacity mapping as its own artifact rather than something you read off the schedule.

**Session lengths**

- Times published in CET (UTC+1).
- Keynotes run 50 minutes. The opening keynote is a shorter special case at 09:30-09:50; the slot following runs 10:00-10:50.
- Lightning talks are capped at 15 minutes per presenter - the shortest standardized format on the grid.
- Standard developer-room talks follow the same ~50-minute pattern.
- Closing keynote sits late on the final day, 17:00-17:50. The plenary bookends anchor the grid rather than floating mid-schedule.

**Buffer**

- The visible gap between the 09:30-09:50 opening keynote and the 10:00-10:50 slot that follows is 10 minutes, in a venue spanning 37 rooms.

**How to read it.** Standardized short session lengths are what let FOSDEM pack 1,079 events into two days; the 10-minute inter-slot gap is what that density costs. Cite the pairing as a trade-off, not the 10 minutes as a recommendation - a tighter buffer across a larger footprint than most events will ever have is the aggressive end of the spectrum, not the middle of it.

## PyCon US 2026: slack bought by staggering

PyCon US 2026 published schedule (`us.pycon.org/2026/schedule/`).

**Track layout**

- Five primary rooms on the main talk days (Friday-Sunday): Room 103ABC, Room 104AB, Room 104C, Grand Ballroom A, Grand Ballroom B, plus additional open and specialized spaces.
- Standard talk length: 45 minutes.

**Staggered starts**

- Session start times are staggered rather than synchronized across the five rooms. Observed starts: 11:00, 11:45, 12:30, 1:45, 2:45, 3:30, 4:30 - roughly hour-long blocks once transition time is folded in.
- The effect: not every attendee moves at the same moment. When one track's session ends, another's may be mid-run, so room-transition foot traffic spreads across the hallway instead of concentrating into one mass movement per slot.

**Plenary sync points**

- The day opens with coffee (Hall AB) at 8:00, then "Welcome" and keynotes at 9:00-9:45 - pulling all tracks into one room before the day splits.
- Breaks in the Expo Hall mid-morning (~10:30) and mid-afternoon (~4:00): 15-30 minute windows.
- Lunch (Hall AB) anchors midday (~12:30-1:15) as a full-attendee pause between the morning and afternoon blocks.
- Keynotes run in a dedicated large room (Pacific Ballroom - Arena) that gathers every track's attendees. The multi-track day is bookended and interrupted by single-track plenary moments rather than being purely parallel end to end.

**How to read it.** Staggering is a congestion tool distinct from clash avoidance and distinct from room-capacity matching: it manages doorway and hallway throughput, which no clash check looks at. The plenary moments do double duty - they gather the audience, and they reset whatever per-track schedule drift accumulated before the next block starts.

## The two strategies side by side

Both events face the same problem - several hundred to a thousand people changing rooms repeatedly in one building - and answer it differently:

|                   | FOSDEM 2026                               | PyCon US 2026                           |
| ----------------- | ----------------------------------------- | --------------------------------------- |
| Rooms in parallel | 37                                        | 5 main                                  |
| Standard talk     | ~50 min                                   | 45 min                                  |
| Slot alignment    | Uniform lengths, aligned slots            | Staggered per-track starts              |
| Congestion lever  | Short uniform sessions, tight gap         | Spread the moment of movement           |
| Visible buffer    | 10 min between the observed keynote slots | Folded into ~hour-long staggered blocks |

Neither is a default. The lever you can afford depends on the venue: staggering needs the grid to tolerate ragged block boundaries, and a tight uniform gap needs rooms close enough together to walk between in the time it gives you.

## Energy-curve pacing and graveyard slots: named sources

Unlike room-capacity and clash reasoning below, pacing and graveyard-slot avoidance do have named, checkable sources outside the manufacturing analogy this skill otherwise borrows from (see `references/production-scheduling-concepts.md` § Levelled pacing for that analogy and what it still adds).

**Deliberate pacing across the day**

- DevOpsDays' own organizing guide runs structured talks (traditionally 30 minutes) in the morning, then 5-minute Ignite talks with auto-advancing slides, then fully self-organized Open Space in the afternoon - a published, currently-used format gradient from high structure to low structure, not a fixed format held constant all day (`devopsdays.org/organizing/`, "Setting your program").
- Strange Loop's founder Alex Miller states the conference interspersed 10-minute non-technical "Strange Passion" talks among the technical program specifically to vary the day's cognitive load, rather than clustering density together (`thestrangeloop.com/about.html`).
- The post-lunch alertness dip is circadian, not just a reaction to eating: it occurs "even when the individual has had no lunch and is unaware of the time of day," which is the physiological basis for avoiding dense content immediately after lunch (Timothy H. Monk, "The Post-Lunch Dip in Performance," _Clinics in Sports Medicine_ 24(2), 2005, DOI 10.1016/j.csm.2004.12.002).

**Graveyard slots**

- "Graveyard slot" has an academic definition: a session slot that, due to its timing, carries a high probability of low attendance. The paper that coins it for conference programming argues that who gets assigned one is not a neutral scheduling choice (Emily F. Henderson and Holly Henderson, "The graveyard slot is political," _Australian Feminist Studies_ 34(101), 2019, DOI 10.1080/08164649.2019.1688641).
- At economics conferences, a paper presented in the last slot of the last day has the lowest probability of later journal publication, while second-day mornings score highest - a concrete empirical worst-slot and best-slot pair, from a different conference culture than a developer event (Gorodnichenko, Pham and Talavera, NBER Working Paper 26240, 2019, summarized at `cepr.org/voxeu`).
- Hynek Schlawack writes about presenting to a visibly empty room at PyCon US, and about social media actively encouraging attendees to skip talks for the hallway track at a later edition of the same conference - a graveyard slot created by competing informal programming, not by clock position alone (`hynek.me/articles/hallway-track/`).
- DevOpsDays' organizing guide treats a whole day as a graveyard-slot-equivalent risk: it recommends weekdays only, reasoning that a weekend day competes with time people protect for family and rest (`devopsdays.org/organizing/`, "Selecting a date").

**How to read these.** The organizer guides (DevOpsDays, Strange Loop) are the strongest sources here because they are named practitioners' own published, currently-used playbooks, closer in kind to FOSDEM and PyCon US's published grids above than to a research finding. Henderson and Henderson, and the NBER paper, are peer-reviewed and empirical but not developer-conference-specific: cite their direction, not their magnitude, at a different kind of event. Schlawack's account is a named individual's experience, not a measured pattern.

## What a published grid does not tell you

- **Room-capacity matching.** A grid names the room and never the seat-count reasoning behind the match. FOSDEM's separate room-occupation overview likely carries part of it.
- **Clash avoidance reasoning.** A grid does not record which pairings were deliberately kept apart, or why.
- **Energy-curve pacing.** A published grid's visible times do not state its own pacing logic; the section above draws that from named organizer guides and peer-reviewed sources instead.
