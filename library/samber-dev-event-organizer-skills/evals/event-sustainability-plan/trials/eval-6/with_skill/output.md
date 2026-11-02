# Cindermoor DevCon 2027: Speaker Travel Policy

Berlin, 800 people. About 25 invited speakers and 12 travel grants, so roughly 37 trips the event books or pays for.

The interview normally runs one question at a time. I couldn't ask here, so the assumptions are listed at the end. Change any of them and the policy needs a second look.

## 1. Verdict on the three proposals

| Proposal | Verdict | Why |
|---|---|---|
| Distance penalty in CFP scoring | ❌ Rejected | It ranks speakers by footprint, which the sustainability skill forbids. It would also push down the speakers the grants exist to bring in, so it contradicts your access commitment. |
| Free remote tickets instead of travel grants | ❌ Rejected | Travel grants win over every carbon lever. A remote ticket removes the thing the grant buys, which is being in the room. |
| Economy for all speaker flights, no exceptions | ⚠️ Kept, with one carve-out | Economy by default is the right policy. "No exceptions" would override access needs, and those belong to the accessibility owner. |

**Why the first two fail on carbon grounds too.** The 12 grantees are mostly long-haul, and the 25 speakers are probably the same. Those 37 trips are the only travel you fully control, so keep them in the inventory and don't cut the people to improve the total.

On numbers: 37 trips are about 4.6% of 800 people. I can't give their share of emissions without your origin data, and I won't invent a factor. Because the grantees are long-haul, the share is likely much higher than 4.6%. The estimate comes first, then the share is stated with a range.

## 2. The policy

### Scope
This policy covers every trip Cindermoor DevCon books or pays for: invited speakers, keynotes and grant recipients. It does not cover attendees or sponsor staff who pay their own way. Those trips are still counted in the footprint estimate.

### Rules

1. **Selection ignores travel.** CFP scoring, speaker selection and grant selection do not consider distance, origin or flight footprint. Reviewers never see a distance field.
2. **Travel grants stay.** There are 12 grants, with the same criteria and amounts as the access commitment. A grant is never replaced by a remote ticket. A grantee can ask for remote attendance as an extra, but never instead of the grant.
3. **Economy by default.** The event books economy for all speakers and grantees.
4. **Direct flights where available.** The event books the direct option unless it costs more than [set threshold, a budget decision for `event-budget`]. A connection adds distance and an extra take-off and landing.
5. **Rail for short journeys.** Where a train journey is under [N] hours, the event books rail. I suggest 6 hours as a starting point. That figure is a policy choice, not a measured value. The 2019 astronomy-meeting survey found a median rail option of about 8 hours among people who had one. Only Berlin-area and near-neighbour origins will trigger this rule.
6. **Regional speakers where the programme allows.** When two proposals are equal on merit and format, the programme team may prefer a speaker already in Europe for the keynote slots. This is a programming choice for keynotes only. It is never a CFP score and is not applied to grants.
7. **Remote speaking is an offer.** Any speaker may choose to present remotely, in the same slot, with the same billing and the same fee. The offer is opt-in, never imposed, and has no effect on acceptance. A speaker who accepts doesn't lose a grant they were awarded.
8. **Access exceptions override rules 3 to 5.** A speaker or grantee with a documented access or medical need may get a direct flight, a premium cabin or no rail leg. `event-accessibility-inclusion` owns these cases and decides them. Every exception is logged, with no questions asked beyond what the access process already collects.

### Data captured for every booked trip
Origin city, destination, cabin class, direct or connecting, rail or air, and nights. This feeds the footprint inventory. These trips are organizer-owned lines, so they are counted even when an employer pays for a flight.

## 3. What this edition changes, and what moves to next edition

| Now | Next edition |
|---|---|
| Policy rules 1 to 8 in force | Compare host cities by train access before signing a venue |
| Remote speaking offered | Decide on a remote attendance tier with `event-format-selection` |
| Booked trips logged with cabin and routing | Review cadence if the footprint estimate shows long-haul dominates |

## 4. Public wording (EU rules apply, since you market in Berlin)

> **How we handle speaker travel.** Speakers and grant recipients fly economy by default, direct where possible, and take the train for shorter journeys. Any speaker can present remotely in the same slot with the same billing. We select talks and grant recipients without regard to where they live. Our 12 travel grants are unchanged: we want developers from outside Europe in the room. We are measuring the footprint of every trip we book and will publish the estimate with its method. Access needs come first; where a speaker or grantee needs a different cabin or routing, we provide it.
>
> We do not call this event carbon neutral.

This wording avoids any numeric reduction target, which needs a verified plan under the EU rules. It also says nothing about offsets or neutrality.

## 5. Hand-offs

- **`event-accessibility-inclusion`:** owns the grants and decides all access exceptions under rule 8. Confirm that the grant criteria and published commitments match rule 2.
- **`event-budget`:** cost of the direct-flight threshold in rule 4. Economy lowers fares, but direct and flexible fares usually raise them, so the policy has a net cost to estimate.
- **`event-format-selection`:** the remote attendance question. Remote engagement evidence is poor, so any remote tier is its decision, and it must not steer grantees' regions towards it.
- **`event-landing-page`:** publishes the section in part 4.
- **`event-debrief`:** receives the post-event inventory.

## 6. Open items

- **Assumed:** a recurring edition with a signed or soon-signed Berlin venue, speakers' current cabin class unknown, and no published commitment that conflicts with rules 1 to 8. If you currently book business class for keynotes, say so; it changes the baseline.
- **Needed from you:** last edition's origin split for speakers and grantees, so we can compute the concentration line and state the share honestly.
- **Needed from you:** your rail threshold [N] and your direct-flight cost cap.
- **Needed from you:** which published access commitments already exist, so rule 8 matches them word for word.
- **Needed from you:** a legal review of the part 4 wording before publishing. This is not legal advice.

**Net:** the team's goal is right, but two of its three proposals would cut the people rather than the emissions. The policy above keeps the one that works (economy by default) and replaces the rest with levers that reduce footprint without touching who gets to come.