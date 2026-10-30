# Decision communication: sequence, templates, tooling

Contents:

- The notification sequence and why its order matters.
- The de-anonymization asymmetry.
- Accept, decline and waitlist templates.
- Duplicate-acceptance handling.
- The tooling capabilities the flow needs.

## Sequence

1. **Acceptances first**, each with a confirmation deadline. Until acceptances are confirmed, the real slot count is unknown.
2. **Waitlist notices** at the same time as acceptances, not later. A waitlisted submitter who first receives silence and then a promotion has been told, in effect, that they were an afterthought.
3. **Declines** once acceptances are confirmed and the waitlist is fixed. Sending declines first means retracting one if a confirmed speaker drops.
4. **Program announcement** after that. Announcing a partial schedule is acceptable - organizers note it is fine to leave some space until the end - but announcing only a handful of speakers risks unwarranted assumptions about the event's demographics.

The published call already promised a notification date. Missing it costs more trust than any wording choice recovers, because submitters have other CFPs open and are holding calendar space for yours.

## The de-anonymization asymmetry

In a blind process, accepted speakers are de-anonymized because someone has to coordinate logistics. Declined submitters are notified **without the review team ever learning who they were** - identity enters only at the acceptance step, and only for the accepted.

Decide explicitly which of your own people ever sees a declined submitter's name. It is the cheapest fairness commitment available: nobody can hold a grudge, conscious or not, against a name they never read.

## Templates

Adapt the wording; keep the structure. Each template is short on purpose - length reads as justification.

### Acceptance

> Your proposal **"{title}"** has been accepted for {event}, {date}.
>
> Please confirm by **{deadline}** that you can present. If we don't hear from you by then, we'll offer the slot to another speaker.
>
> What you get: {the perks exactly as the call stated them}. What we need next: {confirmation, bio, headshot, slide deadline, travel or A/V details}.
>
> {If they submitted more than one accepted proposal: which of these would you rather give? We can only schedule one.}
>
> One rule for every speaker: no commercial demo or sales pitch. The audience should leave with the lesson, not the product.
>
> {If the program runs a depth gradient: your talk sits {position} in the evening. Open so the whole room follows, and end deep.}

The confirmation deadline is what makes the waitlist function. Without it, the backup list is decorative.

For the commercial-content line and the depth-gradient line, see [program-fit-field-reports.md](program-fit-field-reports.md). Drop the depth-gradient line when the room is not mixed.

### Decline - the default rung, with criteria recap

> Thank you for submitting **"{title}"** to {event}. We're not able to include it this year.
>
> We received {N} proposals for {M} slots, so we declined many talks we'd have liked to program. Selection followed the criteria we published with the call: {restate them in one line}.
>
> {If applicable: this pool was reviewed anonymously - reviewers scored your proposal without seeing who submitted it.}
>
> We'd genuinely like to see you submit again for {next edition}.

The ratio is the load-bearing sentence: it reframes a no as arithmetic rather than a verdict, and it costs nothing per submitter.

### Decline - with per-proposal feedback (the starved rung)

Same as above, plus the reviewer comments edited for tone. Three rules keep this from backfiring:

- Report what reviewers actually wrote. Inventing softer reasons produces feedback a speaker cannot act on, and it will contradict the decision if they ask a follow-up.
- Strip attribution and any reviewer's name. Feedback is from the committee, never from a person.
- Say plainly that the feedback explains this decision, not a general assessment of the speaker. Reviewers score a proposal against one pool on one day.

### Waitlist

> Your proposal **"{title}"** is on our waitlist for {event}.
>
> That means it made our final shortlist and would be programmed if a slot opens. Slots open when a confirmed speaker withdraws, which sometimes happens and sometimes doesn't.
>
> You'll hear from us either way by **{date}**. Please don't hold travel on our behalf before then.

Promise the date, never the odds. No published data exists on how often a waitlisted talk gets promoted, so any number you give a waitlisted speaker is invented - and it is the kind of invention they will remember.

## Duplicate acceptances

If one submitter has more than one proposal reach acceptance, let them choose which to give, or suggest a preference. This is a per-speaker cap applied after review rather than as a submission-time limit, and it keeps the strongest proposal in the pool rather than forcing an earlier arbitrary cut.

## Tooling capabilities the flow needs

Ask for capabilities, not a product - every named platform implements some subset, and the choice is the organizer's regardless of tool:

- Send acceptances and declines separately, with a confirmation request attached to acceptances.
- Attach individual feedback to a decline notification (a built-in capability in at least one common platform, so the constraint is editorial time, not mechanism).
- Group mailings to accepted speakers, plus post-acceptance forms to collect bios, slides, travel and consent details.
- An organizer-to-submitter messaging loop for pre-decision clarification.
- Review-stage anonymization as a togglable mode.
- A scoring mechanism that matches your rubric - comparison, star ratings and yes/no all exist as distinct modes across platforms - with per-track evaluation plans where different tracks need different criteria.
- Exports of scores and comments, so the decision record survives the platform.

If the tool cannot separate the anonymized review stage from the identified logistics stage, run that boundary manually and write down who crosses it.
