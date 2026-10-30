# Shortlist and qualification templates

Templates and worked examples for the sourcing pass. Nothing here is a benchmark; the scoring rubric below sorts candidates by evidence strength and is not calibrated against event data.

Contents:

1. Slot brief template
2. Candidate record template
3. Hot / Warm / Cold / Skip rubric (an uncalibrated sorting scale)
4. Worked example: a shortlist entry that works, and one that does not
5. Sourcing compliance guardrails
6. Handoff packet shape

## Table of Contents

- [1. Slot brief template](#1-slot-brief-template)
- [2. Candidate record template](#2-candidate-record-template)
- [3. Hot / Warm / Cold / Skip rubric](#3-hot-warm-cold-skip-rubric)
- [4. Worked example](#4-worked-example)
- [5. Sourcing compliance guardrails](#5-sourcing-compliance-guardrails)
- [6. Handoff packet shape](#6-handoff-packet-shape)

## 1. Slot brief template

Write one per slot to fill, before sourcing any name. A brief is what turns "impressive person" into "right person".

```
Slot:            Opening keynote, day 1
Format:          30 min talk, single track, no Q&A
Theme:           Why platform teams stall after year two
Audience level:  Senior practitioners and eng managers; not an intro audience
Success looks like:
                 Attendees leave with a shared vocabulary for the failure the
                 rest of the day's talks assume. Sets the edition's argument.
Hard constraints: Must be on stage in person; travel covered, no fee available
Disqualifiers:   Anyone currently selling a platform product to this audience
```

The disqualifiers line does real work. Written before sourcing, it makes a Skip a decision. Written after, it becomes an argument about a specific person.

## 2. Candidate record template

One per candidate on the long list. Every factual claim gets a source link and the date it was checked, because a shortlist is read weeks later by someone who was not there when you found it.

```
Name / handle:
Slot considered:
Where they came from:   channel (referral / directory / prior-talk review /
                        community scouting) + who or which directory
Fit evidence:           what they have done on this theme, with links + dates
Delivery evidence:      recorded talk / transcript / long-form writing, with
                        link, date, and one line on what you actually observed
Reliability signal:     organizer reference if obtained, otherwise "none"
Availability:           known / unknown; dates checked against the event
Travel + lead time:     origin, whether travel is needed, visa question open?
Confidence:             High / Medium / Low, per inferred (not stated) claim
Score:                  Hot / Warm / Cold / Skip
The "why", in one or two sentences, evidence-first:
```

The last field is the deliverable. It is what `samber/dev-event-organizer-skills@event-speaker-cold-outreach` personalizes the invitation with, so it has to survive being pasted into a message with only light editing.

## 3. Hot / Warm / Cold / Skip rubric

This four-band scale borrows the shape sales teams use to score leads. It is a serviceable way to sort candidates by evidence strength, and it is not a speaker-sourcing benchmark: the bands are not calibrated against event data.

- **Hot**: strong fit against the slot brief, direct delivery evidence you personally checked, plausibly available on the dates.
- **Warm**: good fit, but the evidence is one step removed (a referral without a reference, writing without a recorded talk) or availability is unknown.
- **Cold**: loose fit, or evidence thin enough that the invitation would be guessing at what they would actually give you.
- **Skip**: a disqualifier hit: unavailable, a conflict with a sponsor or with the program's independence, a lead time the calendar cannot absorb, or a code-of-conduct concern. Skips leave the list; they do not sit at the bottom of it.

Rank within a slot, not across the whole program. Two Hots for the same slot is the good problem. A Hot with no slot is a name, not a shortlist entry.

## 4. Worked example

**A shortlist entry that works:**

> **Slot:** Opening keynote, day 1 - "why platform teams stall after year two"
> **Channel:** prior-talk review, from the 2025 program of an adjacent regional conference
> **Fit:** Ran platform engineering at a 400-engineer company through exactly this transition; two conference talks and a long write-up on the post-adoption plateau, most recent March 2026 (links + dates recorded).
> **Delivery:** Watched the first twelve minutes of her 2025 recording - opens on a concrete failure, no product pitch, holds a room without slides for the first three minutes.
> **Reliability:** Organizer of that event confirms she arrived with the talk finished a week early and adapted the ending to their audience.
> **Availability:** Unknown. Based in Lisbon, would need travel; no visa question for this destination.
> **Score:** Hot.
> **Why:** She has lived the exact failure this edition argues about and can open on it without selling anything - and the recording shows she can carry a room cold, which this slot needs more than any other.

**An entry that does not work, and why:**

> **Name:** widely followed platform-engineering commentator, 60k followers
> **Fit:** posts about platform engineering constantly
> **Score:** Hot
> **Why:** huge audience, would definitely draw people and be great for ticket sales.

Three failures in four lines: the fit claim is a topic match with no depth behind it and no dated source. The delivery evidence is missing entirely, so the Hot score is fame standing in for qualification, the single most common way an invited program goes wrong. And the "why" is about the organizer's ticket sales, not about what the audience gets, which means the invitation written from it will be about the organizer too, and will read that way to the person receiving it.

## 5. Sourcing compliance guardrails

The same rules that govern sales prospecting apply here, because the legal exposure is identical:

- **Public channels only.** No bulk scraping, no working around access controls or gated data.
- **Retain the source and the date** for every contact detail and every claim. This is the record that shows where a contact route came from if anyone asks.
- **Never infer or target on protected characteristics.** When a program has a diversity goal, source from a directory whose members opted in to being found for that reason - that is the mechanism, and it is the compliant one.
- **A listing is consent to be found, not consent to be pitched.** Follow each directory's stated contact norms and use the route the person published.
- **Community spaces have their own rules.** Many codes of conduct treat recruiting or solicitation in the space as off-limits. Read names there if the rules allow it, then approach through a published contact route rather than the channel itself.
- **Keep reference conversations factual.** Ask what the organizer observed - did they show up, did they hit the brief, how were they with the room? Do not record an opinion about a person you would not repeat to their face.

## 6. Handoff packet shape

What leaves this skill and arrives at outreach, per slot:

```
Slot brief (verbatim, as ranked against)
Ranked candidates:
  1. Name: score; the "why" + evidence links/dates; availability;
     travel/lead-time constraints; contact route
  2. ...
Budget offer, honestly stated:  ticket only / + travel / + lodging / fee: none
                                or unconfirmed; say which, never "probably"
Invited-review lane:            confirmed at invitation (enters the program
                                directly) OR reviewed on its own named track
Long-list-to-shortlist ratio used this round, for next edition's baseline
Channels used, so source effectiveness can be counted after the event
```

The budget line and the review lane are the two fields most often left implicit, and both cost the most later. An unconfirmed budget discovered during negotiation turns an invitation into a walk-back. An undecided review lane means an invited speaker's proposal lands in a blind-review pool where their identity, the entire reason they were invited, cannot be seen.
