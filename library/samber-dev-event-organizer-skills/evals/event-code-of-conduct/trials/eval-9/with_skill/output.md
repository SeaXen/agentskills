# PolyglotFest conduct plan: what I'd change

**Disclaimer:** this is not legal advice. Counsel should review three things:
- The ejection-without-refund wording in ticket terms.
- The sponsor clause (see `event-sponsor-agreement`).
- Retention rules for incident records.

Anything involving a crime, a minor, or an imminent physical threat goes to emergency services and counsel first.

I did not interview you, so I assumed the following. Correct me where wrong:
- You are one organizing entity, with no umbrella body above you.
- The event is annual, or you hope it will be.
- You have no hard publication deadline.
- Your effort ceiling is low.
- You have no existing values document.

## Verdict

Your four decisions each have a problem:

| Your plan | Verdict | Change |
|---|---|---|
| Two-person team | ❌ Too small | Add 1–3 people from outside the founder chain (3–6 total). |
| Judgment case by case | ⚠️ Fix the method, keep the judgment | Fix the decision method, ladder, and appeal route before the event. |
| No dry run | ❌ Drop this | Do two or three practice cases, about 2 hours. |
| "10 business days" | ❌ Doesn't fit a 3-day event | Use an on-site clock and a post-event clock. |
| Co-founder stays quiet but votes | ❌ Backwards | He is recused entirely: no discussion, no vote, no files. |

## 1. The spouse rule: recuse fully

Staying quiet while voting keeps the one thing recusal exists to remove.

- A spouse is a **hard conflict** (close relationship). The rule: excluded from discussion, **vote**, and confidential material.
- Recusal starts the moment he realizes it applies, and someone else executes it. They remove him from the documents and open a new channel.
- Say so in the published policy, so a reporter knows it before they report.
- Soft conflicts, such as the same employer or an appearance of conflict, may discuss but not vote. Confirm the grade by majority vote before the investigation starts.

His wife is a speaker, so the "revoke speaker privileges" rung applies to her like anyone else. A policy that quietly shields a founder's family is not worth adopting.

**Consequence for your team size:** with two members, his recusal leaves you deciding alone. That is the "single organizer as sole responder" setup. It's deleted from this design because one person deciding alone at 2am isn't a process. The spouse rule alone forces you to add people.

## 2. Team: 3–6 named people, not 2

The team has to keep working with a third of it unavailable, and at three days that is near-certain. You two are also the most powerful people at the event. A code that won't bind its most powerful people shouldn't be adopted at all.

Do this:

1. Recruit **1–3 people outside the founder chain**. Candidates are trusted community leaders, an advisor, or a speaker-liaison volunteer with no reporting line to you.
2. Publish every member's **name and individual contact**.
3. Make sure at least one contact is outside your organizing chain. A report about either of you then still has somewhere to go.
4. Fix the decision rule in advance, adapted from Django's:
   - At least 2 voting members must agree.
   - Aim for consensus, with a two-thirds majority as the fallback.
   - A conflicted member does not count toward the quorum.
   - When the case stalls, the **outside appeal person** decides. A tie goes to the lighter *interim* measure, such as a separation requirement. Delay is the documented failure.
5. If you can't find independent people, an **external trust-and-safety contractor** is the one rung that answers "no board above us." It costs a retainer and requires handing attendee data to an outside party.

**Anonymous path:** add one. You have a power gradient: volunteers, sponsor booth staff who answer to their employer, and the founders on the team. Write the decision convention for reports with no reporter to go back to *before* the first one arrives.

## 3. Judgment case by case: keep it inside a fixed frame

Judgment is fine for what rung a case lands on. These must be fixed beforehand:

- **A published sanctions ladder.** Suggested rungs:
  1. Warning.
  2. Separation requirement, used as an interim measure alongside action, never as the whole response.
  3. Removal of privileges.
  4. Ejection, with no refund.
  5. Revocation of speaker privileges.
  6. Ban from future editions.

  Pair each rung with its community impact. Cut any rung you lack the standing to execute.
- **Appeals:** state which rungs are appealable, to whom, in what form, and by when. I'd make only ejection and bans appealable, as MLH does. The appeal goes to a named person outside the response team who didn't decide the case. "The organizing team" would be the same people rehearing themselves.
- **Records:** use case codes and person codes, a neutral summary, the consequences applied, and a cross-edition record of prior violations. Without that record, "repeat offences move up" can't work. Write down retention and access rules and restrict access to the team.
- **Public-statement authority:** name one person. Nobody free-lances mid-incident.
- **Never do these:**
  - Mediate between the parties.
  - Require an apology.
  - Let the reported person stay on condition they avoid the reporter.
  - Ask the reporter to pick the penalty or suggest withdrawing the report.
  - Handle a case entirely in private. Everyone who knew about the violation should learn that action was taken, without details.

## 4. No dry run: do a small one

Having never handled an incident is the reason to rehearse. An unrehearsed team invents its decision rule mid-incident. This costs about 2 hours:

1. Run two or three practice cases with the full team.
2. Make one of them a report about a founder.
3. Make one a report where a founder is conflicted, such as one naming a speaker related to a team member.
4. Make one a sponsor booth-staff incident.
5. Check each case against the intake card, the decision rule, the notification order, and the closure message.

Repeat it when a member joins and before each edition.

## 5. The response clock: replace "10 business days"

Ten business days is a decision band for online communities. A day-1 incident would be unresolved when everyone has gone home. The draft also has no acknowledgment promise. Replace it with this:

> **During the event:** Urgent or ongoing incidents get an immediate response. Other reports are acknowledged within [2] hours, and the team meets within 24 hours. We aim to decide before the reported person leaves the venue.
> **After the event:** We acknowledge within 24 hours and tell the reporter the outcome within one week.

The 24-hour meeting and one-week follow-up are PyCon US's bands. The 2-hour on-site acknowledgment is my proposal, and it is yours to set. Pick a number you can meet and publish it. Measure against it: every report acknowledged inside the window, and every reporter told the outcome by the deadline.

## 6. The rest of the package

For 900 people over 3 days, you also need:

- **Base text:** adapt an established template (the JSConf/Ada Initiative family), keeping the attribution it requires. Don't write one from scratch. Rename every role to a real title at your event. If you have a polyglot-community values text, add it as a preamble.
- **Scope clause:** name the following explicitly.
  - **People:** attendees, speakers, volunteers, sponsor and booth staff, press, and contractors.
  - **Spaces:** venues, shuttles, social events, and unofficial or fringe events such as attendee-run parties.
  - **Online:** the chat or event app, and the dates it is in scope, before and after doors.
  - **Conduct outside the event:** you can act inside your own spaces on outside evidence, for example by refusing a talk slot.
- **Reporting channels:**
  - A published email alias.
  - Responders in distinctive shirts, announced in the opening session.
  - Named alternates.
  - A reserved quiet room, with its number on the responder card.
  - The anonymous path.
- **Intake card for responders:**
  1. Offer a quiet space.
  2. Listen without judgment.
  3. Assess safety first.
  4. Document.
  5. Thank the reporter.
  6. Escalate immediately.

  Capture the date, location, the reporter's own words, the reported person's identity, witnesses, whether they want anonymity, and whether anyone is in danger.
- **Notification to the reported person:** four parts: the behavior, its impact, the change expected, and the consequence. Show the target the proposed response privately first, to catch missed facts and retaliation risk, not to seek approval.
- **Sponsors:** name them in the policy. Have counsel confirm the sponsor contract carries the compliance clause and the ejection-without-refund right.
- **Transparency report per edition:**
  - Reports received.
  - Count per ladder rung.
  - Median time to acknowledgment and to resolution against your clock.
  - Any policy changes made as a result.
  - No identities and no narratives.

  Publishing zero reports is a result, but read it as a channel check first.

## Next steps, in order

1. ⏳ Recruit 1–3 independent team members, or decide on a contractor.
2. Write the recusal rule and the decision rule into the policy.
3. Replace the 10-business-day sentence with the two-part clock.
4. Publish the ladder, the appeal route, and the names and contacts.
5. Run the 2-hour rehearsal, including the case where a founder or a founder's spouse is the subject.
6. Confirm the sponsor contract language with counsel.

Questions for you, since they change the plan:
- Is this a one-off or annual? Annual favors a standing rehearsed team and a records regime.
- Is there a fixed date for publishing the policy, such as ticket sales opening?
- Can you recruit independent people, or should I plan around a contractor?
- Is there a parent organization or board that could hold appeals?