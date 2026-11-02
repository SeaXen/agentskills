# Sanity check: MosaicJS Meetup code-of-conduct plan

**Verdict: ❌ don't ship the plan as written.** It has three separate problems. Two are the skill's named failure modes, and the third is a metric that works against its own purpose.

Not legal advice. Sponsor contract wording goes to counsel through `event-sponsor-agreement`. Retention and access rules for incident records go to whoever holds your privacy obligations. Anything involving a crime, a minor, or an imminent threat goes to emergency services first.

## 1. "Zero reports in three years = healthy" ❌

Zero reports is weak evidence of a healthy community. The skill's rule is to read a silent channel as a channel diagnostic first. At an event of any size it is more often unreachable than clean.

Check your three-year record against this list:

- Is the reporting path one email address on a web page?
- Were any responders visible in the room, and did the opening announcement say who they were?
- Is there an anonymous path?
- Is there a person other than the founder to report to?
- Has anyone ever tested the channel?

If most answers are "no", the zero says nothing about conduct. It says only that nobody reported.

**Do this before the season starts:**

1. Send a fake report to the current channel and time the answer. Check who sees it and who replies.
2. Add a sentence to your next post-event survey, such as "Did you see or experience anything that made you uncomfortable? Did you know how to report it?" This is a lightweight, anonymous signal.
3. Treat the first real report as a trust signal, not a failure.

## 2. You as single point of contact ❌

You are the founder and lead organizer, so you are the person most likely to be the subject of, or too close to, a report. The skill **deletes** this option for any event where the sole responder is also its most senior person. The channel then cannot receive the one report most likely to need it, and one person deciding alone is not a process.

It also fails the two preconditions the skill sets for a ladder to mean anything. The policy has to bind the powerful, and a decision on a report about you needs someone outside your chain. A report about a close friend of yours has the same problem.

"Simplify" is the wrong goal here. The skill's goal is a pipeline of named people who can act before the event ends.

**Replace with:**

- **A named, published team of 3-6.** Two or three volunteers you trust, plus at least one person outside the organizing team's chain, such as a regular community member, a speaker alumnus, or a sponsor-independent peer-meetup organizer.
- **Individual contacts for at least two people besides you,** so a report about you or about another member has somewhere to go.
- **A recusal rule.** A member steps out the moment they realize a conflict applies. Hard conflict (accused, close relationship) means no discussion, no vote. Soft conflict (same employer) means discussion but no vote.
- **A fixed decision method with tie and absence rules.** The skill's Django-style default is at least two members agreeing, consensus first, then a two-thirds fallback, leaning toward action. The dominant failure is delay, not haste.
- **An appeal route outside the team** (see section 4).

If you can't find a truly independent person, an external trust-and-safety contractor is the only rung that answers this. It is high effort, so try a peer-meetup organizer first.

## 3. Your email in the PDF footer ❌

A footer address is the cheapest channel and the weakest one. It fails in three ways:

- **No one can find it in the moment.** An alias in a PDF is useless to someone in distress in a hallway. Add visible on-site responders, such as colored lanyards or shirts, announced at the opening, with a quiet space.
- **No anonymous path.** Your attendees include people with a power gradient: sponsor booth staff, speakers who want future slots, and junior developers facing a founder they know. Add a way to submit without a name. At minimum, accept anonymous reports at intake and say so.
- **A personal address is a single point of failure.** Use a role alias such as `conduct@…` that reaches the whole team, and publish the team's names beside it. Vacations, a full inbox, or a spam filter must not be able to silence it.

Also write the two-part confidentiality promise into the policy: reports are confidential, and the reporter's identity stays confidential unless they say otherwise.

## 4. The sponsor's "keep reports at zero" KPI ❌

Decline it. The skill's measurement rule is that any target for reports received is self-set and **never managed downward**.

A zero target creates the wrong incentive:

- It pays the team for suppressing, discouraging or downgrading reports.
- It tells attendees that reporting is unwelcome, and some will notice.
- It puts a sponsor's interest into the enforcement process. Sponsor and booth staff are in scope of your policy, and could be the subject of a report.
- A rise in reports after you improve the channel is a trust signal, not a deterioration.

**Offer instead:** the pipeline measures the skill recommends. These are measurable, you control them, and they are an honest commitment to a sponsor.

| KPI | Target |
| --- | --- |
| Reports acknowledged inside the published window | 100% |
| Reporters who received a closing message with the outcome | 100% |
| Response-team rehearsal completed before doors open | Yes/No |
| Transparency report published after the edition | Yes/No |
| Reports per 100 attendees | Reported, **no target** |

Keep the sponsor out of the loop on cases. Give them the aggregate report only, with no identities and no narratives.

Also confirm the sponsor agreement says booth staff are covered by the policy and that you can eject them without a refund. Counsel owns that wording.

## 5. Things the plan is missing

- **A published response clock.** An event's clock must fit inside the event. The PyCon US band is the model: act at once on urgent incidents, meet within 24 hours for non-urgent ones, and follow up with the reporter within one week.
- **A sanctions ladder, published before the first incident.** For example: warning, separation requirement, removal of privileges (speaker or volunteer), ejection, ban. Say which rungs carry an appeal. MLH allows appeals only for suspensions and bans.
- **A scope clause.** Name the people (speakers, volunteers, sponsor staff), the spaces (venue, after-party, any unofficial meetups, chat before and after), and the dates. Take a position on conduct outside the event.
- **Retention rules for incident records.** Decide who can read them, how long they are kept, and a central record across editions so a repeat offence is visible.
- **A rehearsal.** Walk the team through two or three practice cases before doors open.
- **A transparency report per edition.** Count reports, count outcomes per rung, and give times against your clock, with no identities. If you publish zero, label it as a channel diagnostic, not a clean bill.

## Proposed plan for next season

1. **Test the current channel** (the fake report above).
2. **Recruit a team of 3-6**, with one person outside the organizing chain. Publish names and individual contacts.
3. **Replace your personal footer email** with a role alias that reaches the team.
4. **Add visible responders and a quiet space** on the day. Announce both at the opening.
5. **Add an anonymous path.**
6. **Publish** the clock, the ladder, the appeal rules and the "what to expect" page. Don't publish the internal playbook.
7. **Rehearse** before the first event.
8. **Counter the sponsor** with the pipeline KPIs and no zero target.
9. **Publish a transparency report** after the edition.

## Questions I need answered to finalize this

I haven't asked these yet. I assumed the answers shown, so tell me where I'm wrong.

1. **Format:** one-day evening meetup of about 150, in one venue? (Assumed yes.)
2. **Bound beyond attendees:** speakers, volunteers, sponsor booth staff, and an online chat? (Assumed all four.)
3. **Entity:** one organizing entity, with no umbrella or franchise body above you? (Assumed yes.)
4. **Who could be reported while on the team:** you, and anyone else with budget or a headline name?
5. **Publication deadline:** is it fixed by ticket sales or the sponsor contract?
6. **Annual:** you intend to keep running it? (Assumed yes, which favors a rehearsed standing team over a one-off page.)
7. **Effort ceiling:** how many organizer hours, and is anyone willing to staff a channel live on the day?
8. **Existing assets:** a peer meetup team, a foundation, a lawyer, a written values document, or a trained volunteer pool?