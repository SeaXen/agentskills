# Matching and slot mechanics

Contents: the matching criterion as one written sentence · the profile field list and what each field is for · the consent wording checklist · the four matching-rule shapes as run sheets · building a slot block inside a grid you do not own · a positive and a negative worked pair · the dominance-check derivations behind the matching-mechanism and scheduling-mechanic rankings.

## Table of Contents

- [1. The matching criterion, written as one sentence](#1-the-matching-criterion-written-as-one-sentence)
- [2. Profile fields, and what each one is for](#2-profile-fields-and-what-each-one-is-for)
- [3. Consent wording checklist](#3-consent-wording-checklist)
- [4. The four matching-rule shapes, as run sheets](#4-the-four-matching-rule-shapes-as-run-sheets)
- [5. Building the slot block inside a grid you do not own](#5-building-the-slot-block-inside-a-grid-you-do-not-own)
- [6. A worked pair](#6-a-worked-pair)
- [7. Ranking derivations](#7-ranking-derivations)

## 1. The matching criterion, written as one sentence

Write it before you write a form. The criterion is the thing you will be judged against afterwards, and a form built before it exists collects fields nobody can act on.

Shape: _"A meeting is a good match when a person from side A who [stated situation] meets a person from side B who [stated capability], and both said so themselves."_

The last clause is the load-bearing one. It is what separates a match from an assignment, and it is the difference between the mechanic and the thing this skill deletes rather than demotes.

- **Positive:** "A meeting is a good match when an attendee who runs a production service and said they are evaluating a change in that area meets a vendor engineer who works on that area, and both accepted the pairing."
- **Negative:** "A meeting is a good match when a sponsor gets in front of a senior attendee." Nothing in it is checkable, nothing in it required the attendee to want anything, and it is satisfiable by handing over a list.

Write the criterion into the sponsor conversation too. A criterion agreed before the event is what makes a missed quota discussable afterwards; a criterion improvised on the day is what makes it an argument.

## 2. Profile fields, and what each one is for

Collect the smallest set that the criterion actually consumes. Every extra field is data you must hold, justify, share correctly and eventually delete - and it lowers completion, which costs you matches directly.

| Field                                          | What it is for                                       | Trap                                                                                      |
| ---------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Side (which population)                        | Decides which pool the person is matched against     | A person who is genuinely both needs to pick one per meeting, not be dual-listed          |
| Role or function, in their words               | The criterion's "situation" half                     | A job-title dropdown flattens the exact distinction the criterion turns on                |
| What they are looking for, free text, one line | The only field that establishes intent               | Making it optional turns the pool into a directory of people who did not ask for anything |
| Topic or area tags, from a short fixed list    | Makes the pool sortable without reading every entry  | A long list produces tags nobody selects and a sparse matrix                              |
| Availability windows within the block          | Feeds every scheduling rung except "no booked slots" | Collecting it before the block is placed means collecting it twice                        |
| What may be shown, and to whom                 | The consent record, not a preference                 | Storing it as a preference rather than a record is how it gets overridden later           |

Two fields to refuse outright:

- **Budget or purchase authority.** It converts an attendee's profile into a qualification record held by the organizer.
- **Anything about a person that they did not type themselves** - an inferred seniority, a company size looked up elsewhere.

Both are the point at which a matching program stops being a service to attendees and becomes lead qualification performed on them.

## 3. Consent wording checklist

Consent scope is fixed at the moment someone submits, by the words they saw - not by what you intended and not by what you decide afterwards. Retrofitting it is the one error in this skill that cannot be undone.

The form must say, in the person's line of sight when they submit:

1. **What is shared** - which of their fields a counterpart sees.
2. **Who sees it** - everyone in the directory, one accepted counterpart, or the organizer only. Name which.
3. **What triggers the sharing** - their own request, a mutual acceptance, or an organizer's judgment.
4. **What they get out of it** - the meetings, stated plainly.
5. **How they stop** - withdrawing from the pool, and what happens to pairings already accepted.
6. **When it ends** - the pool is deleted after the event, and by when.

Two checks worth running before the form goes live:

- Read points 1-3 aloud and ask whether a person would be surprised by any of them on the day.
- Confirm that nothing in the form promises a counterpart's behaviour, since you can promise the pairing and never the conversation.

## 4. The four matching-rule shapes, as run sheets

Each shape below is this skill's own construction: a rule and a sequence of messages, not a documented workflow.

### Open directory

An opt-in list people browse and request against. You host it and do nothing else.

1. Publish the field set and the consent wording; open submissions.
2. Publish the list to the people who are on it, not to the public web.
3. Provide a request path that reaches the recipient, and let them decline silently.
4. Publish nothing about who requested whom.

Its weakness is structural rather than fixable: only the requester chose. Expect a distribution where a small number of listed people absorb most requests and the rest receive none, and say so to anyone who joins expecting meetings.

### Organizer brokering

A named person hand-pairs from stated interests and makes the introduction.

1. Read every entry once, in one sitting, before pairing anything. Pairing as entries arrive biases the whole set toward whoever registered first.
2. Draft pairings on paper with a one-line reason each. The reason is the artifact - it is what you send, and what you check afterwards.
3. Send each side the same introduction, naming the counterpart, the reason, and how to decline without explaining.
4. Keep a decline count per person. Three declines from the same person is a signal your read of their entry was wrong, not that they are difficult. That threshold is this skill's own, not a measured one.

This is the only rung where the pairing quality is a person's judgment, which is why it survives at pair counts a rule cannot be fitted to.

### Mutual opt-in

Both sides state what they want; a pair exists only where both opted in.

1. Collect intent from both sides against the same tag list.
2. Show each person a candidate set drawn from the other side, ordered by nothing more clever than tag overlap and freshness.
3. A request from either side creates a pending pair; an acceptance creates a pair. Nothing else creates a pair.
4. Expire pending requests on a stated date so the pool does not fill with dead intent.
5. Cap outbound requests per person. Without a cap, the highest-volume requester defines everyone else's inbox and the mechanic reads as spam.

### Scored ranking

The organizer scores fit from structured data and pushes ranked recommendations.

1. Write the scoring rule down as a sentence before implementing it, and keep it short enough to explain to a participant who asks why they were recommended someone.
2. Score only on fields the person entered themselves.
3. Use the score to order a candidate list, never to create a pair. A pair still needs both acceptances.
4. Keep a manual override, and log every override with a reason - the overrides are how you find out what the rule is missing.
5. Re-check the rule against a sample of its own top recommendations before anyone sees them. A rule that recommends the same ten people to everyone is a rule fitted to a sparse tag matrix, not a matching engine.

Do not name a platform in any of this. Every rung above is a rule and a set of messages; whichever tool the organizer already has can carry it, and one that cannot is the wrong tool rather than a reason to change the rule.

## 5. Building the slot block inside a grid you do not own

The published grid belongs to `samber/dev-event-organizer-skills@event-schedule-design`. You place meetings inside it and never move a session. Work in this order:

1. **Take the block's boundaries as given.** Ask where the block sits; do not propose a better place for it.
2. **Count the pairs you actually have**, not the pairs you hope for. The block is sized by real accepted pairs plus a margin for late ones.
3. **Divide the block into equal slots.** Equal, because unequal slots make every downstream conflict a special case. Choose the length from the block you were given and the pair count you have - this file states no number, and neither should you.
4. **Leave gaps between slots** rather than running them back to back. A meeting that overruns with no gap pushes every later meeting for both people, and the person who loses is whoever booked last.
5. **Check each person's slots against the sessions they are speaking at or attending.** A conflict here is yours to resolve by moving a slot, never by asking `samber/dev-event-organizer-skills@event-schedule-design` to move a session.
6. **Confirm every pairing with both sides before publishing the schedule.** Publication is the point of no return: after it, a change costs two messages and a lost slot.
7. **Publish one view per person**, not the whole grid. A full pair grid discloses who is meeting whom to everyone in it.
8. **Name one organizer on duty for the block**, and put that name on the brief. An unattended block cannot absorb a single thing going wrong.

## 6. A worked pair

Both cases below are illustrative. The figures in them are constructed to show the shape of each decision, and carry no weight as benchmarks.

**Positive.** A single-track community conference with four sponsors sells no meeting quota, so the program does not run at all. One sponsor asks for introductions to attendees working on a specific problem.

The organizer takes that as a brokering request rather than a program: they ask the sponsor for the criterion in one sentence, mention it from the stage as an open invitation, and introduce the three attendees who come forward. Nothing is published, nothing is scheduled, no data changes hands, and the sponsor gets three conversations with people who volunteered for them.

**Negative.** The same conference decides to "run matchmaking" because a sponsor asked. It exports the registration list, tags attendees by job title, and sends each sponsor twenty names with a booking link.

Attendees receive meeting invitations they never asked for, from a company they have no relationship with, referencing data they gave the organizer to get a badge. Two things went wrong and only one of them is visible: the mechanic was one-sided, and the consent scope was decided after the data was collected. The second is the one that cannot be repaired afterwards.

## 7. Ranking derivations

Full pairwise dominance checks behind the matching-mechanism and scheduling-mechanic rankings in the top-level skill file.

### 7.1 Matching mechanism

Two of the five axis orderings are argued rather than asserted, because a reader will expect both to run the other way:

- **Effort: organizer brokering tops it because it never amortizes.** Every pair costs a fresh judgment and two messages, and the hundredth pair costs exactly what the first did. Scored ranking is expensive once - a schema, a collection pass, a rule - and free per pair after that.
- **Compliance: scored ranking is the only rung that _derives_ new facts about a person and then acts on them, and it holds the largest store.** The open directory ranks second because publishing a profile to everyone has the widest disclosure surface and the least reversibility, since a copied directory cannot be unpublished. Brokering and mutual opt-in each disclose to exactly one counterpart, brokering on the organizer's judgment and opt-in on the person's own.

**Dominance check: 10 pairs, zero strict-dominance relations, accounted for in three groups.**

- **Five pairs** - no-program against each of open directory, brokering, opt-in and scored, and open directory against scored - are blocked because the richer rung wins both value axes but loses on effort _and_ on compliance: the ordinary ladder above doing nothing.
- **Two pairs are blocked by effort alone and deserve to be named**, because they are the ones a careless ordering would get wrong: brokering beats the open directory on both value axes and on compliance, and opt-in beats the open directory on both value axes and on compliance. In each case only effort stops the relation. The open directory survives on this menu because it is cheap, not because it is good.
- **The last three pairs** - brokering against opt-in, brokering against scored, opt-in against scored - are blocked by the two value axes genuinely disagreeing: relevance rewards human judgment, certainty rewards volume and structure, and no rung leads both.

### 7.2 Scheduling mechanic

**The delivered-quota axis is rank-identical to inverse effort, and that is a warning, not a result.** On its own it discriminates nothing: it would make this menu's efficiency line collapse into cheapest-first and the dominance check vacuous. The autonomy axis is what carries the menu, because it runs in the opposite direction - and it is the axis a sponsor-facing organizer is most likely to forget, since nobody is in the room to argue for it.

**Dominance check: 6 pairs, zero strict-dominance relations, one mechanism covering all six.** The three axes are perfectly co-monotonic in a chain - quota and effort ascend together while autonomy descends - so every one of the six pairs is the same trade: more delivered quota, bought with more organizer hours and less of the attendee's control over their own day. No pair escapes it, which also means the check cannot catch an error here. The ordering rests on where the quota gain stops being worth the autonomy it costs, and no general rule fixes that point.

**No compliance-cost axis on this menu.** No rung here collects data or takes on an obligation that the matching menu and the quota menu have not already taken on. The contractual exposure of promising a number belongs where the promise is made, one menu down; adding it here would count the same review twice.
