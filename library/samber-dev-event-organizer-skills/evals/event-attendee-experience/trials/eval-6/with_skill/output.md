# JuniperJS first-timer plan: verdict and revised design

**Verdict:** not solid as written. Two of the four elements are things the skill rules out, and the other two are fixable. About 440 of your 800 registrants are first-timers (55%), so this is the main thing to get right.

Ⓘ I haven't asked you the skill's interview questions: days and buildings, the register the culture work set, the signed floor plan, and whether a welcome slot exists in the grid. The design below assumes a single day, a signed floor plan, and a grid owned by `event-schedule-design`. Answers to those could change it.

## Element by element

| Element | Verdict | Why |
|---|---|---|
| Closing confetti for 30 contributors | ⚠️ Keep the idea, change the design | Subset moment and weak evidence (details below) |
| Auto-assigned "First Conference?" ribbon | ❌ Change | Orientation has to be offered, not assigned |
| Opt-in 8am breakfast in a side room | ⚠️ Change | Opt-in reaches only the people who would have asked anyway |
| First-timer track in Room C all morning | ❌ Delete | The skill says never build orientation as a separate track |

### 1. The peak-moment confetti

- **The 85% figure is a correlation, not a method.** Freeman's 2025 report links a *reported* peak moment to stated return intent, across the whole events industry. It is not causal and not a design target.
- **The useful number is the other one.** 78% of organizers think they deliver peak moments, but only 40% of attendees report having one. Your co-organizer's plan is the pattern that gap describes.
- **It is a subset moment.** 30 people on stage while 770 watch. The skill says never design a moment for a subset, and 440 first-timers who know nobody on that stage are the least likely to feel it.
- **Moments announced as moments land as programming.** A staged "surprise" is closer to a scheduled item than to a peak.
- **Closing is a good slot.** The skill prefers a touchpoint that already exists over a new one.

Keep the closing and the recognition, with these changes (self-set suggestions, not established practice):

- **Pick one moment and give the room a part in it.** Contributors stand where they are, or the whole hall acknowledges them. The confetti then belongs to everyone, not only the stage.
- **Ask the 30 first.** Some will not want to be on stage. You also need a defensible, published definition of "most active". Both are my additions, not the skill's.
- **Check confetti with the venue.** Cleanup and permission are the venue's call (`event-venue-sourcing`), not this skill's.
- **Measure it.** Add one post-event survey question: "Did anything about the day stand out to you, and what?" Do not assume you delivered a peak moment. Whoever owns the survey asks it.

### 2. The auto-assigned ribbon

- **Published practice is offered, not assigned.** The skill points to ICMA telling newcomers to pick one up at registration. A badge that labels you "new" all day turns awkwardness into a label.
- **Offer it at the desk** and make it visibly optional.
- **Use opt-out cues that reach the people who wouldn't ask.** A line on the badge back, or a lanyard colour *offered* (not assigned), with a one-line "new here? start at X".
- **Keep ribbons off the check-in table.** Put them in a basket at the end of the desk. At 800 people, a desk that also hands out ribbons is the one-table-does-everything failure the skill deletes.
- **Check-in model (default, re-rank after the interview):** pre-sorted pickup (last name, then first name) with a slower walk-in lane. Promote to multi-lane if the door rush exceeds one queue or you have separate ticket categories.

### 3. The 8am side-room breakfast

- **Opt-in plus a side room is the wrong shape.** The skill says orientation must be opt-out because only people already inclined to ask use an opt-in sign. A side room also fails the "put it on the path" principle.
- **The skill's real requirement:** give the first twenty minutes a destination, with a person in it. The worst moment is the gap between badge and first talk, standing alone.
- **Scale problem:** 440 first-timers is too many for one small side room. Two published shapes exist:
  - **A standalone welcome session.** PyCon US runs a Newcomer Orientation before the opening reception. It suits a venue with one entrance and one corridor, and room size caps it.
  - **A returning-attendee buddy pairing.** NAPFA and the Electrochemical Society pair newcomers one-to-one with returning attendees. It scales past room size, but you have only about 360 returners for 440 newcomers. That makes 1:1 impossible, so use 1:2 or 1:3 groups led by volunteer returners, or run a hybrid.
- **Recommendation (self-set):** a short welcome session open to anyone, placed on the main path just before the opening, plus a small set of visible "ask me" returning-attendee hosts (volunteers, no desk). Breakfast can stay as a bonus, not the mechanism.
- **Print the three questions nobody asks aloud**, on one side of one card:
  1. Where do I sit?
  2. Is it fine to leave a talk partway?
  3. What actually happens in the hallway track?

### 4. The first-timer track in Room C

- **Delete it.** The skill's rule is "Never build it as a separate track". It also moves the grid, which belongs to `event-schedule-design`.
- **It would segregate.** 440 people marked "new" are sorted into one room all morning, away from speakers and from returners. They would also miss the main-track talks they came for.
- **If you want newcomer-friendly content,** ask `event-schedule-design` to make some existing main-grid talks accessible. Do not build a labelled, separate track.

## Walkthrough rows to run on paper first

Run the audit table once on paper and once on the real building before doors open. These rows are my hypotheses until you walk the venue, so label them as such.

| Touchpoint | Likely pain point | Fix |
|---|---|---|
| Arrival | 440 first-timers don't know which door | One sign before the first choice |
| Check-in | Door-open rush with ribbons and swag at the same table | Ribbons and swag at a separate basket or table |
| First wayfinding decision | The junction right after the desk is the least-signed spot | One A3 sign naming destinations, not room numbers |
| Gap before the first talk | A first-timer stands alone | The welcome session or a host, on the path |
| First session | Nobody says where to sit or whether leaving is fine | The printed three-question card |
| Hallway track | Not obvious that it exists or is acceptable | Space on the path with high tables and coffee |

## Before you commit

1. **Decide the posture first:** orientation opt-out, ribbon offered, no separate track.
2. **Confirm** the sign-off with your co-organizer on the confetti redesign.
3. **Pick two measures** from the skill's list and write down what each would change next edition. Suggested: longest check-in queue with its hour, and the peak-moment survey question.

Items marked self-set are not established practice. The published practices cited are PyCon US, NAPFA, ICMA and the Electrochemical Society.