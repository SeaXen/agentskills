# Space program and requirements sheet

The document you hand to every candidate venue. It converts an attendance estimate and a chosen format into rooms, ratios and hard constraints, so that two venues can be compared on the same terms instead of on how good their photos look.

Contents: the space program, the density ratios, the non-space criteria, the overnight and fire-code case, the multi-venue and hybrid gap, and a filled worked example.

## Table of Contents

- [The space program](#the-space-program)
- [Density ratios that decide whether a room is actually usable](#density-ratios-that-decide-whether-a-room-is-actually-usable)
- [Non-space criteria](#non-space-criteria)
- [The overnight case, and a fire-code trap worth its own line](#the-overnight-case-and-a-fire-code-trap-worth-its-own-line)
- [Multi-venue and hybrid: what this sheet does not cover](#multi-venue-and-hybrid-what-this-sheet-does-not-cover)
- [Two operational guardrails carried out of sourcing and into the contract](#two-operational-guardrails-carried-out-of-sourcing-and-into-the-contract)
- [Worked example: a requirements sheet, filled](#worked-example-a-requirements-sheet-filled)
- [Negative example: the requirements sheet that decides nothing](#negative-example-the-requirements-sheet-that-decides-nothing)

## The space program

Size the main room to expected attendance, then build the rest around it. The main room number is not this skill's to invent: it arrives from the demand and growth work upstream. For early editions of a community conference, expect attendance ranges of 70-700 with typical landings around 250; a rough pre-sale heuristic is 2-3x the best-attended local meetup in that city.

Rooms a technical event actually needs:

- **Main room** - sized to expected attendance and to the format's seating (theatre rows pack tighter than rounds or a workshop layout).
- **Breakout rooms** - for open spaces, workshops, or a second track: a mix of small rooms holding 10-20 and larger ones holding 20-40, arranged so chairs can form a circle for discussion. Genuinely separate rooms beat one big room split with partitions, which is noisier in practice. Keep them close together so time is not lost walking between sessions. The main room can double as one of them.
- **Hallway-track space** - named explicitly as a first-class requirement, not spillover: not everyone attends talks, and the hallway track is a real use of the venue. A quiet room or an area near the food serves it.
- **Sponsor space** - tables for at least the top tier, placed near food or the hangout space so foot traffic passes them naturally rather than tucked off to the side.
- **Zones, for a hackathon** - separate areas for working, for listening to talks, for hardware, for food, and for sponsors: a multi-zone requirement rather than one big room.
- **Registration and storage** - a check-in area that does not block the entrance, and secure overnight storage for both organizer and sponsor equipment.

## Density ratios that decide whether a room is actually usable

These are the numbers that turn "the WiFi is fine" into a testable claim. For hackathon audiences (average event around 300 participants), the rules of thumb are:

- **WiFi: about 4 devices per attendee.** A laptop, a phone, a second device, a dev board.
- **Power: at least 2.5 outlets per attendee.**

Treat these as the hackathon baseline. A talk-driven conference where most attendees are listening rather than building may run lower on both axes. Published conference-specific ratios do not appear in most organizer guides, so borrow the hackathon figure as an upper bound rather than trying to present a conference number that may not exist.

A gap on an otherwise-good campus venue is often patchable through another part of the same institution: campus IT for loaner access points or WiFi fortification, campus electricians for fuse-box access, another student organization for extension cords and power strips. Ask before rejecting the venue.

## Non-space criteria

- **Transit and parking** - reachable by public transit, or enough parking, weighted by what is normal locally.
- **Nearby affordable hotels** - a plus for out-of-town attendees. Running the event inside a hotel solves it directly, at the cost of the room-block attrition exposure covered in the contract reference.
- **Catering flexibility** - whether outside catering is allowed or the venue mandates its own. A venue-mandated caterer is a cost constraint to surface during sourcing, not a surprise at contracting.
- **WiFi and internet capacity** - existing capacity, and whether more can be added.
- **Livestream capacity** - whether the connection can push video out, if streaming is planned at all.
- **A/V equipment and staff** - what exists, and whether the venue supplies setup staff or the organizer sources them.
- **Tables and chairs** - quantity, whether the venue supplies them or a rental vendor is needed, and who coordinates the floor plan with that vendor.
- **Accessibility** - can attendees needing physical accommodation reach and use every space, not just the entrance. The bar itself is set by `samber/dev-event-organizer-skills@event-accessibility-inclusion`; this sheet only carries it into the venue conversation.
- **Security** - a secure area for expensive equipment, and whether the venue provides its own security staff or the organizer sources a firm.
- **Loading dock** - whether one exists, and the route from it to the rooms.

## The overnight case, and a fire-code trap worth its own line

For any event running through the night: confirm the venue knows participants will be present overnight, and that a dedicated safe space exists for anyone who needs to sleep.

Ask the question in two parts, because the answer differs by activity at the same address: overnight _working_ is usually permitted where overnight _sleeping_ is against fire code. "Can we run overnight?" gets a yes that does not cover people sleeping on the floor. Ask both explicitly, and get the answer in writing.

## Multi-venue and hybrid: what this sheet does not cover

Multi-venue events (a main venue plus partner hotels plus off-site social venues) inherit this whole sheet once per site, plus the transit time between them and a single named owner per site. That much is straightforward extension.

The genuinely uncovered part: hybrid or multi-venue format decisions require venue-side technical requirements - the bandwidth headroom a two-way remote audience needs, the rigging and camera positions, the redundancy on the uplink, the encoding and control-room space. This skill does not translate format choices into those specifications. Do not manufacture bandwidth figures or an equipment list yourself. Instead, put the requirement to the venue as a question they must answer in writing: "what sustained upstream bandwidth can you guarantee in this room, on what circuit, with what fallback?" Route the specification itself to `samber/dev-event-organizer-skills@event-production` and `samber/dev-event-organizer-skills@event-format-selection`.

## Two operational guardrails carried out of sourcing and into the contract

- **Do not overcommit headcount, and do not pre-pay for the venue until forced to**. Apply the same discipline for food: adding a few extra plates is always cheaper and easier than having already paid for too many. This is a standing posture for every edition, not only for a growth year.
- **Have the organizing entity's legal details ready before the first venue conversation** - legal name, contact details, business or registration number. Some venues require them just to place a hold on a date, so a missing registration number can cost the candidate window while it is being sorted out.

## Worked example: a requirements sheet, filled

Invented and illustrative. The venue names, city and dates are fictional.

```
EVENT: Ourtown Systems Day 2027  - single-track community conference
DATE WINDOWS (from date selection, in preference order):
  1. Thu 15 - Fri 16 Apr    2. Thu 6 - Fri 7 May    3. Thu 20 - Fri 21 May
EXPECTED ATTENDANCE: 180 (edition 3; edition 2 sold 165 of 180)
ORGANIZING ENTITY: Ourtown Tech Community e.V.  - reg. no. VR-00000, contact <name/email>

MUST HAVE
  Main room, 180 theatre-style, stage or raised area, projection + wired sound
  2 breakout rooms: 1 x 15-20, 1 x 30-40, chairs movable into a circle
  Hallway/hangout space adjacent to catering, standing room for ~80
  6 sponsor tables (2m), sited on the food or hangout circulation path
  Step-free access to every room used, accessible toilets on the same level
  WiFi for 180 attendees; state capacity and whether it can be raised
  Power at attendee seating in breakouts; main room powered at stage + tables
  Load-in access for 8 pallets-equivalent of sponsor shipments; dock or ramp
  Secure overnight storage for organizer and sponsor equipment, both nights
  Team access from 15:00 the day before for setup
  Outside catering permitted, OR in-house catering with a written quote

SHOULD HAVE
  Livestream-capable uplink (state guaranteed sustained upstream, and fallback)
  Quiet room, separate from the hangout space
  Hotels within 20 min public transit
  On-site A/V staff for setup

VENUE MUST ANSWER IN WRITING
  Is catering mandated in-house? At what per-head cost band?
  Are catering, security, fire marshal or janitorial staff charged separately?
  Is the quote a guaranteed ceiling, or are there charges not in it?
  What insurance do you require of us, and in what amounts?
  Do you require sponsors or exhibitors to carry their own cover?
  Shipping: from what date, to what address, with what receiving fees?
  Cancellation-fee schedule: what percentage is owed, from which dates?
  Deposit: how much, when, and is any part of it refundable?
  Any restrictions on which companies may sponsor or exhibit on site?
```

The last question exists because a venue that hosts you - especially a company hosting in its own facility - may try to limit other sponsors' presence or claim category exclusivity. Clarify any such limit in writing before selling sponsorships against a category list the venue host could later veto.

## Negative example: the requirements sheet that decides nothing

```
We need a nice venue for about 180 people in April or May, with good WiFi,
somewhere central, ideally with catering. Budget is flexible. Let us know
what you have available and what it would cost.
```

Every failure mode compounds here. "About 180" invites a room that fits 180 seated and nothing else - no hallway track, no sponsor tables. "Good WiFi" cannot be tested or breached. No date preference order means availability cannot rank the windows. "Budget is flexible" is the sentence that removes the ceiling before the negotiation starts. And nothing in it forces the venue to disclose the mandated caterer, the separately-charged fire marshal, or the cancellation schedule - all of which arrive later as surprises, when the alternatives are gone.
