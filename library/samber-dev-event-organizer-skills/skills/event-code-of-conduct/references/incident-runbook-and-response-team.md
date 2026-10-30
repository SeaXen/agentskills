# Incident runbook and response team

Who receives a report, what they do in the first ten minutes, and how a decision gets made and delivered.

Mechanics that depend on a venue, a badge or a date come from real events (PyCon US, MLH). Enforcement theory comes from ongoing projects and communities (Django, CNCF, Mozilla, Aurora and Gardiner). Aurora and Gardiner's handbook is particularly useful for events: its authors led the 2010 Ada Initiative conference anti-harassment policy that most event codes descend from, so their mechanics transfer to an event more cleanly than other project material.

## Table of Contents

- [Team composition](#team-composition)
- [Conflicts of interest](#conflicts-of-interest)
- [On-site intake: the sequence](#on-site-intake-the-sequence)
- [Capture fields](#capture-fields)
- [Records](#records)
- [The response clock](#the-response-clock)
- [Investigation and decision](#investigation-and-decision)
- [Notification and closure](#notification-and-closure)
- [Responses that make things worse](#responses-that-make-things-worse)
- [Enforcement has to be visible](#enforcement-has-to-be-visible)
- [Public statements](#public-statements)
- [Publish a "what to expect", not the playbook](#publish-a-what-to-expect-not-the-playbook)

## Team composition

- **Three to six people**, sized so it still functions with a third unavailable (practitioner doctrine). PyCon US runs three named leads: the Incident Responder, the PSF Director of Operations, and the Conference Chair - a small fixed committee staffed by conference-specific roles rather than a standing body.
- **Publish the members' names** in the reporting instructions. People report more when they know who receives it.
- **Publish individual contacts for each**, so a report about one member has somewhere else to go. PyCon US does exactly this across its three leads; Django escalates to the foundation board when every chair is conflicted and Mozilla splits contributor reports from reports about employees - the same structural answer, reached independently at events and in projects.
- **Fix the decision method in advance**, including tie and absence rules, and let it err toward taking action. Django's rule:

  - The chair needs at least two members to agree.
  - Consensus is the target.
  - A two-thirds majority is the fallback.
  - Unresolvable cases escalate to the board.

- **Rehearse on a fixed cadence** - annually, when a member joins, and before each edition. An unrehearsed team invents its decision rule mid-incident.

## Conflicts of interest

Recusal starts the moment a member realizes it applies, and someone is assigned to execute it - remove them from the documents, open a new channel. Distinguish two grades (CNCF):

- **Hard conflict**: accused, close relationship, personal interest. Excluded from discussion, vote and confidential material.
- **Soft conflict**: same employer, appearance of conflict. May discuss, may not vote.

Confirm the grade by majority vote before the investigation starts.

## On-site intake: the sequence

PyCon US's staff procedure, in order. This is the part to hand to a responder on a card.

1. **Offer a quiet space.** PyCon US names a specific room number in its own document - a physical private room, not a policy line. Reserve one and put its number on the responder card.
2. **Listen actively, without judgment language.**
3. **Assess safety first.** Any sign of imminent physical danger: run the security plan, summon security or emergency services, and note the action in the report.
4. **Document the report**, asking clarifying questions.
5. **Thank the reporter.**
6. **Escalate immediately** to the response leads by call or SMS.

MLH's procedure adds two explicit prohibitions worth putting on the same card:

- Never suggest that withdrawing the complaint is an option - it is coercive.
- Never ask the reporter for input on the penalty, which is staff's responsibility.

Aurora and Gardiner reach the same second conclusion from the target's side: letting the target set the consequence exposes them to retaliation for the outcome.

Two more from the practitioner checklist (CC BY-SA, adaptable with attribution):

- Find a place others cannot overhear and bring something to write with.
- Promise no outcome on the team's behalf, only that it will protect confidentiality and safety as far as it can.

## Capture fields

- Date and time.
- Location.
- Description in the reporter's own words where possible.
- Identifying information for the reported person.
- Witnesses.
- The reporter's identity and contact, and their relation to the events.
- Whether they want to stay anonymous.
- Whether anyone is in immediate danger.

PyCon US accepts anonymous reports at the capture stage even though it advertises no separate anonymous channel - a useful distinction: the intake form's anonymity option and a published anonymous channel are two different commitments.

## Records

- Assign each case a randomly generated code name, and code names to the people involved, so notes can circulate without identities (Django).
- Record:
  - Report date.
  - Case code.
  - Person codes.
  - A neutral-language summary.
  - The team's scope determination.
  - Safety and harassment risk assessment.
  - The expected behavior change.
  - Consequences applied.
  - All correspondence.
  - Resolution and follow-up.
- Keep a central record of prior violations across editions. The ladder is meaningless without it - rung 2 exists only because someone can check whether this is a repeat.
- Decide retention, access and security in writing, restrict access to the team, and treat a leak as grounds for removal from it.
- Safety outranks privacy: refusing to keep records, or withholding prior-incident context from the people handling a new case, is privacy misapplied.

## The response clock

Publish one. Three sourced bands to choose between:

- **PyCon US**:
  - Responders act immediately on urgent or ongoing incidents.
  - The three leads meet within **24 hours** for non-urgent reports.
  - The reporter is followed up with **within one week**, confirming whether a violation occurred and what action was taken. The one-week figure is a full-resolution promise, not an acknowledgment.
- **Aurora and Gardiner** (written for online communities): 24 hours to acknowledgment, 10 business days to a decision. The clock starts when the team receives the report, and this is the one part of a response guide they say to follow strictly, because the dominant failure is delay rather than haste.
- **Django and CNCF**: acknowledgment "ideally within a day", and "usually within a few business days" respectively.

An event's clock has to fit inside the event. A three-day conference cannot run a ten-business-day decision on an incident that happened on day one, which is the structural reason event clocks compress. Set yours accordingly and then meet it.

## Investigation and decision

Review the evidence; interview the reporter, the reported person and witnesses as appropriate. External investigators or mediators are an option for severe cases (CNCF). A team may open an investigation proactively where there is a serious ongoing safety risk and no formal report.

Argue about impact, not intent. Ask three questions:

- What was the impact?
- How is recurrence prevented?
- What makes the target and the community safer?

Intent survives only as a predictor of future risk: positive intent _plus_ recognition, responsibility and a concrete change lowers risk; positive intent without them does not.

MLH's version at an event:

- The accused gets a chance to give their side.
- The decision is made jointly with the on-site organizer and the local team.
- It stands unless the central body reverses it.

## Notification and closure

The message to the reported person has four parts:

1. The behavior in neutral factual terms.
2. Its impact.
3. The specific change expected.
4. The consequence.

Never disclose the reporter's identity to them.

Order of notification: show the target the proposed response privately **before** announcing it - to catch missed facts and retaliation risk, not to seek approval. Then tell the reported person, whose only required answer is whether they will comply. The decision takes effect immediately even if they contest it.

Close the loop with the reporter: the final resolution, and that the case is closed unless new information appears.

## Responses that make things worse

Listed as failing to prevent harm, or causing it (practitioner doctrine):

- **Requiring an apology, or asking the target to accept one.** A compelled apology destroys the only signal worth having - whether the person would have apologized unprompted. Contributor Covenant 2.1's level-1 line "a public apology may be requested" runs directly against this; 3.0 drops it - a genuine disagreement between two sourced authorities, not an error in either.
- **Mediating between harasser and target.** It reframes "a harmful person in our midst" as "those two don't get along", which absolves the team of acting.
- **Letting the reported person stay on condition they avoid the target.**
- **Assigning people to guard or shadow either party.**
- **Doing nothing because the person left or is unidentifiable.** State publicly what you would have done.

Rust's policy offers an apology-gated unban - moderators may unban a first offender who "offer[s] the offended party a genuine apology". It is a real published counter-example to the rule above rather than a settled practice; note the conflict rather than smoothing it over.

## Enforcement has to be visible

Private-only handling teaches the community nothing and reads, correctly, as non-enforcement. The documented failure case is a chat harassment report handled entirely by private messages: the target concluded nothing had happened, and left.

The minimum bar: everyone who knew about the violation learns that a response occurred. Ideally the response is published, aggregated and anonymized. This does not contradict correcting privately - the _notification_ is private, the _fact that enforcement happened_ is not.

MLH states the same thing from the privacy side: "make sure that everyone aware of the initial incident is also made aware that it is not according to policy and that official action has been taken, while still respecting the privacy of individual attendees... leave out specific details."

## Public statements

One body decides whether anything is said publicly, and agrees wording and timing before anyone speaks. MLH's rule: the incidents team, with the on-site representative, determines whether a public announcement is necessary; where a local organizer delivers it, "this will only occur after close collaboration with MLH on the precise wording and timing."

For an independent event, name whoever holds legal and communications authority and give them the same role. Nobody free-lances a statement mid-incident.

For a widely witnessed incident, a **preliminary announcement** is the right first move:

- Say the team has the report and is working on it.
- Give the contact for anyone with more information.
- Redirect the pile-on.

For attendees upset about an incident or its handling, MLH's three-step script:

1. Acknowledge the feelings.
2. Reassure that it is being taken seriously without disclosing private details.
3. Give a concrete channel for further feedback.

## Publish a "what to expect", not the playbook

Publish what a reporter can expect when they report. Do not publish the internal procedure: a legalistic published process gets weaponized into arguments about whether the team followed its own steps, instead of about what happened.
