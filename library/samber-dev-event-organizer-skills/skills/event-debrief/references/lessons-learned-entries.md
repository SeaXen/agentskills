# Lessons-learned entries

The format, the two sourced examples, a negative counterpart, the categories that make entries sortable, and the narrow case for going deeper than three parts.

## The three-part entry

Every finding is written as three parts and nothing more:

1. **What happened** - the observable fact, described as a condition or a system, never as a person.
2. **What was done in the moment** - the response during the event, or an explicit "nothing could be done during the event".
3. **What changes next edition** - the concrete change, plus its owner and due date.

This depth is not a compromise. It is the depth of the Write the Docs Prague 2017 retrospective, the most complete published artifact in this field, and it is deliberately shallow: most event findings need a fix and an owner, not a causal chain.

## The two sourced examples

Both are from the Prague 2017 "Recap and Retrospective" post, quoted in substance.

**Vegetarian lunch mixup, day one.**

- What happened: the vegetarian lunch order did not match what attendees needed on the first day.
- In the moment: identified as lunch started, raised with the venue immediately, venue acknowledged the mistake.
- Next edition: "continuously working with the venue to improve and broaden menu options", and continuing to monitor.

**Uncomfortable noise level during unconference sessions.**

- What happened: unconference sessions ran at a noise level attendees found uncomfortable.
- In the moment: nothing - it could not be fixed mid-event.
- Next edition: "made a careful note of this potential issue and will make the necessary adjustments to the venue layout".

Notice what neither entry does: no root cause, no blame, no severity score, no five layers of why. Notice also that the second one openly records that nothing could be done on the day. An entry with an empty middle part is a complete entry, and pretending otherwise pushes teams toward inventing a response they did not have.

## A negative counterpart

> Registration was a disaster. Sam was overwhelmed and the queue was out the door. We need better volunteers next year.

Four failures in three sentences:

- "A disaster" is an adjective, not an observation.
- "Sam was overwhelmed" names a person where the finding is structural.
- "Better volunteers" is a wish with no owner, no date and no mechanism.
- Nothing records what was done at 9:15 that morning, so next edition's team cannot tell whether the improvised fix worked.

The same finding, written properly:

- What happened: the registration desk had one staffed position against roughly 200 arrivals inside the first thirty minutes; the queue reached the building entrance and the first session started nine minutes late.
- In the moment: two volunteers were pulled off floor duty at 09:15, which cleared the queue by 09:40 and left the main room unstaffed for that period.
- Next edition: size the desk against the arrival curve rather than headcount, and roster a named float role for the first hour. Owner: the volunteer lead. Due: at roster build, six weeks before doors.

## Categories, so entries sort into fixes

Sort each finding by the gap that let it reach the debrief. This taxonomy maps real failure modes:

- **Nobody owned it** - the work existed and no name was attached to it.
- **Known risk, no treatment** - it was on the risk register and nothing was actually put in place.
- **First-time failure mode** - genuinely new; nobody could have scored it. This one goes to the risk register as a new category rather than as a fix.
- **Incomplete fix from last edition** - it is in last edition's log, marked done, and it recurred. The most valuable category in the whole list, and the one that only exists from edition two onward.
- **Checklist or review miss** - a process existed and the step was skipped.

Sorting by category is what turns a flat list into a routing decision:

- "nobody owned it" → team-structure finding
- "known risk, no treatment" → risk-register finding
- "checklist miss" → run-of-show or planning finding

The category tells you which sibling receives it.

## What-went-well entries

Same three parts, inverted: what worked, what made it work, and what has to be deliberately preserved next edition. The third part is the one that matters - a practice that worked because one person quietly did it every year is a bus-factor finding wearing a compliment.

## When to go deeper than three parts

Escalate exactly one or two findings per edition to a 5-Whys, and only when all three of these hold:

- The finding recurred, or would recur by default rather than by chance.
- Its cost is structural - money, safety, a person leaving, an audience segment not coming back - not an inconvenience.
- The obvious fix addresses the symptom and the team can feel that it does.

Everything else gets three parts. Forcing five layers onto a catering mixup burns the room's attention before it reaches the finding that needed it, and produces a document whose depth no longer signals anything.

When the deeper pass points at the standing team's design or at an unscored risk category, stop at the diagnosis and route it. This skill surfaces those findings; it does not redesign the team or rewrite the register.
