# Sanctions ladder, appeals and transparency

The published consequences, who can appeal which of them, and what the event says afterwards.

This guidance draws from real events (MLH, PyCon US) and ongoing enforcement theory (Contributor Covenant, Django, CNCF, Aurora and Gardiner).

## The ladders, side by side

The shape converges across every source, which is the reason to publish one rather than invent a response per incident.

### MLH - five rungs (a hackathon franchise model)

1. **Warning** - cease the behavior; further reports result in further sanctions.
2. **Separation requirement** - mandated no-contact and no-proximity with the reporter for the remainder of the event.
3. **Removal of privileges** - volunteer responsibilities and privileges end immediately.
4. **Ejection** - "immediately leave the event and not return."
5. **Ban** - from future events, indefinite or time-boxed.

Trigger for any rung: violation of the sanctioning guidelines, the code of conduct, or another official policy. MLH's own document does not name who decides which rung applies. That is a gap in the source, not a detail to invent around - decide it yourself and write it down.

Rung 2 is worth noticing: a separation requirement is close to the "stay away from the target" condition that practitioner doctrine rules out as a _substitute_ for acting. The difference is whether it is the whole response or an interim measure alongside one - use it as the second, not the last.

### PyCon US - a range rather than numbered rungs (a single-organizer conference)

PyCon US's range:

1. No violation found.
2. Warning.
3. Proximity restriction.
4. Exclusion from the event.
5. Revocation of speaker privileges.
6. Ban from future events.

Speaker-privilege revocation has no equivalent in project policies and is the rung a conference specifically needs.

### Contributor Covenant 2.1 - four levels

| Level            | Community impact                                              | Consequence                                                                                                                |
| ---------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 1. Correction    | Inappropriate, unprofessional or unwelcome behavior           | Private written warning naming the violation                                                                               |
| 2. Warning       | A violation through a single incident or a series of actions  | Warning with stated consequences; no unsolicited interaction with affected parties for a set period; breaking it escalates |
| 3. Temporary ban | Serious violation, including sustained inappropriate behavior | Time-boxed ban from interaction and public communication                                                                   |
| 4. Permanent ban | Pattern of violation, sustained harassment, or aggression     | Permanent ban from public interaction in the community                                                                     |

Each level pairs a _community impact_ with a _consequence_. Publish both halves; a ladder that lists only consequences reads as arbitrary. Version 3.0 renames the rungs (Warning / Temporarily Limited Activities / Temporary Suspension / Permanent Ban) and drops 2.1's "a public apology may be requested" line.

### Django - the same shape with explicit durations

Django's ladder:

1. Warning.
2. Short-term suspension of 30-90 days.
3. Extended suspension of 90+ days with conditions attached to any return.
4. Permanent ban.

Plus three non-ladder outcomes:

- No violation found.
- Facilitated communication with everyone's consent.
- Referral for ongoing monitoring.

### CNCF - the wider remedy menu

- Warnings.
- Removal of the harmful content.
- A public or private apology.
- Temporary or permanent suspension.
- **Removal from a leadership role.**
- Education or mentoring.
- **Systemic policy changes addressing the root cause.**

The last two matter at an event too: a ladder that only offers warn-or-eject has no answer for a well-meaning repeat offender, or for a program design that keeps producing the same incident.

## Proportionality rules that hold across all of them

- Aim for the **minimum response that will protect the community**. A ban-everything ladder suppresses reporting; a warn-everything ladder deters nobody.
- Deliver corrections privately by default; escalate to a public statement when the harm was public and the community needs to see the norm defended. This is about the _notification_, not about hiding that enforcement happened.
- **State the duration** of any time-boxed sanction in the notification, and schedule the restoration so a suspension actually ends on time.
- **Repeat offences move up the ladder**, which is why the record of prior violations has to be retained across editions.
- **Publish the ladder before the first incident.** Inventing a sanction after the fact is what turns an incident into a governance crisis.
- A team's public statement carries amplified weight, so describe the behavior **without naming the person** unless people need the name to stay safe - a known serial offender attending an event is the case where naming is right.

## Two preconditions that decide whether a ladder means anything

Both are stated as absolute in practitioner doctrine for online communities, and both transfer directly to an event:

- **The consequences have to be meaningful**, up to and including expulsion, and the people applying them need leadership's backing and confidence they will not be overruled absent a significant mistake. At an event, "meaningful" is concrete: it means the person leaves the building.
- **It has to bind the powerful.** A community that will not apply its policy to its most powerful people should not adopt one at all, since it otherwise becomes another instrument of the existing power structure.
  - At an event, the most powerful person is often the founder, the headline keynote, or the largest sponsor's executive.
  - Decide before publishing what happens when the report names one of them.

## Appeals

Appeals are where most event policies are silently vague. State four things: which rungs are appealable, to whom, in what form, and by when.

MLH's model, worth copying for its explicitness: only **temporary suspensions and permanent bans** are appealable by written email request with `[Appeal]` in the subject line and supporting evidence attached. Warnings, separation requirements and privilege removals carry **no** appeal.

That asymmetry is a design choice, not an oversight, and it is defensible: the light rungs are over before an appeal could be heard, while a ban persists across editions and deserves a second look. What is not defensible is implying a uniform appeal right and then declining to hear one.

For a single-organizer event with no body above the response team, the appeal route is the hard part. Options, in the order they usually make sense: a named person outside the response team who did not decide the original case; the board or fiscal sponsor if one exists; or an external reviewer retained for the purpose. Naming "the organizing team" as the appeal body means the same people rehearing themselves, which is not an appeal.

## Notification of a sanction

MLH's practice: the sanctioned person receives written notice stating the exact cause and the sanction's length. MLH does not disclose the reason to local organizers unless the sanctioned person asks it to.

That privacy rule does not conflict with visible enforcement. Visible enforcement is about the community learning that _action was taken_ - this is about not circulating an individual's case file. Both can be true in the same incident.

## Transparency reporting

Commit to a report per edition, and decide its contents before the first incident so the decision is not made under pressure.

- **Django's model**: publish the manual, statistics every six months, and an annual anonymized trends report; never discuss specific incidents publicly, and route any public statement through the board.
- **CNCF's model**: publish transparency reports excluding reporter, harmed-party and witness identities; the reported person may or may not be named depending on the resolution.

A workable event version: number of reports received, number resulting in each ladder rung, median time to acknowledgment and to resolution against the published clock, and any policy or program change made as a result. No identities, no incident narratives.

Publishing zero reports is a real result and worth publishing as one - but read it as a channel diagnostic first. A silent channel at an event of any size is more often unreachable than evidence of a clean event.
