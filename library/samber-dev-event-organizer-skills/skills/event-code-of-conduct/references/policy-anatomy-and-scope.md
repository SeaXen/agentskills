# Policy anatomy and scope

What the document itself has to contain, and the clause that decides whether any of it is enforceable.

This guidance draws from two categories of source.

- Mechanics that depend on a venue, a badge, a booth or a date: MLH's policy set, PyCon US's code of conduct and procedures, `confcodeofconduct.com`, and !!Con.
- Enforcement theory, from ongoing open-source or company communities: Contributor Covenant, Django, CNCF, Rust, Ruby, and Aurora and Gardiner's practitioner handbook.

## Sections a working policy needs

Contributor Covenant 2.1's skeleton is the most widely copied structure, used by tens of thousands of projects, and it maps cleanly onto an event:

1. **Pledge** - the commitment to a harassment-free experience, and for whom.
2. **Standards** - expected behavior and unacceptable behavior, both stated concretely.
3. **Enforcement responsibilities** - who holds the power to remove someone, and what they owe in return.
4. **Scope** - which people, spaces and dates the document governs.
5. **Enforcement** - where to report, who receives it, and the confidentiality promise.
6. **Enforcement guidelines** - the consequence ladder.

Contributor Covenant **3.0** renames and re-splits these (Encouraged/Restricted Behaviors, Reporting an Issue, Addressing and Repairing Harm, Other Restrictions). Check which version a borrowed text is before writing its section names into a deliverable.

An event adds a seventh concern the project skeleton has no slot for: **how a reporter physically finds a responder during the event**. Put it in the enforcement section and repeat it in the opening announcement and the printed program.

## The prohibited-behavior list

Three event policies publish substantially the same enumeration: MLH, PyCon US and `confcodeofconduct.com`. They share a lineage rather than having arrived there independently: `confcodeofconduct.com` traces itself to JSConf US 2012 and the Ada Initiative (see Customization rules below). That lineage is why it reads as the field's standard list, and why drafting one from scratch is the weaker option.

The shared list:

- Offensive comments tied to protected characteristics (gender, gender identity and expression, sexual orientation, disability, physical appearance, body size, race, age, religion, nationality).
- Sexual or violent imagery and language in talks, materials or public spaces.
- Deliberate intimidation, stalking, following, brigading, doxxing.
- Harassing photography or recording.
- Sustained disruption of talks and other events.
- Inappropriate physical contact, and unwelcome sexual attention.

**The opt-out "harassing photography or recording" enforces.** `event-accessibility-inclusion`'s colour-coded interaction-consent stickers give attendees a way to signal a photography boundary - a red sticker reads "not interested in talking, or in being photographed." Recording someone who has signalled that boundary, by sticker or by direct request, falls under this clause; route it through the incident pipeline like any other violation.

Two additions worth carrying deliberately:

- **The subjective backstop.** MLH: "If what you're doing is making someone feel uncomfortable, that counts as harassment." A catch-all means a report does not have to match a named category to be actionable - which matters because the enumerated list is always a list of what someone already thought of.
- **The booth-staff clause.** `confcodeofconduct.com`: booth staff, volunteers included, should not use "sexualized clothing, uniforms, costumes, or environments." This is the origin of the clause that most sponsor contracts now carry.

## The scope clause

This is the section events get wrong, and the one that decides whether a sanction is enforceable against the person who violated the policy. It has to answer four questions explicitly.

**Which people.** Name every role, not just ticket-holders - every sourced event policy names sponsors explicitly, so do the same.

- MLH: "Sponsors, judges, mentors, volunteers, organizers, MLH staff, and anyone else participating in the event are also subject to the anti-harassment policy."
- PyCon US: "all staff, attendees, speakers, exhibitors, organizers, and volunteers at any PyCon event."
- `confcodeofconduct.com`: "all attendees, speakers, sponsors and volunteers."

**Which spaces.** MLH: "all hackathon venues, hackathon-related social events, hackathon-supplied transportation, and online interactions related to the event." The transportation clause is easy to forget and covers a real gap - a shuttle is neither the venue nor a social event.

**Which fringe events.** PyCon US's scope names "tutorials, workshops, summits, poster sessions, receptions, conference, sprints, and sponsored or unofficial events." The **unofficial** clause is the one to copy: attendee-organized parties and meetups happening around the conference are where a large share of incidents occur, and a scope clause that stops at the badge line hands those away.

**Conduct outside the event.** Take a position rather than leaving it open. Two defensible stances:

- The Contributor Covenant position: outside conduct violates the policy only when the person is officially representing the community.
- The practitioner position (Aurora and Gardiner): a community cannot enforce anywhere it does not control, but it _can_ act inside its own spaces on evidence from outside them - a racist personal blog post is grounds to refuse a speaking slot without claiming jurisdiction over the blog.

The second travels better to an event, because an event's main lever is admission rather than moderation.

**Which dates.** An online channel that opens two months before doors and stays up afterwards is in scope for that whole window, or it is not. Say which.

## Sponsor and booth staff: in scope, bound differently

Sponsor staff are covered by the policy and bound through a contract their employer signed, not a ticket they bought. The organizer-ejection-right-with-no-refund shape is confirmed across at least six independent sources spanning conference sizes and domains - PSF/PyCon, Write the Docs, the `confcodeofconduct.com` template, several professional-conference organizers, and MLH for hackathons. It is the default clause, not one example, and every sourced version states the ejection right and the no-refund consequence in the same sentence rather than deferring the refund question to a cancellation section.

Write the policy so it names sponsors and booth staff. Do not draft the clause here; it belongs to the sponsorship agreement.

## Franchise and umbrella events

Where a member or franchise agreement exists, the policy is a contract term rather than a choice. MLH's member-event guidelines: "As an organizer of a Member Event, you are expected to adopt, make publicly available, and enforce the MLH Code of Conduct," with scope "all attendees (including volunteers, mentors, sponsors, organizers, judges, etc.)" and a mandatory escalation into the central process. A local organizer's real task is verifying which version binds them and learning the central runbook, not drafting.

## Customization rules

- Adapting a licensed template is expected, not a violation - Contributor Covenant's own FAQ invites communities to rewrite the enforcement section to match their real procedures. Keep the attribution the license requires: `confcodeofconduct.com`'s template is CC BY 3.0 and traces to JSConf US 2012 and the Ada Initiative.
- Rename every role to a title someone actually holds at your event. A reporting sentence that names a "community leader" nobody is cannot be acted on.
- Never adopt a ladder the team has no standing to execute.
- The Berlin Code of Conduct (source at `github.com/rubyberlin/code-of-conduct`, adopted by numerous user groups and conferences) is a second, independent template family: it traces its own lineage to the pdx.rb code of conduct, not to JSConf US 2012/Ada Initiative, and structures itself as Purpose, Open Source/Culture/Tech Citizenship, Expected Behavior, Unacceptable Behavior, Consequences, a witness/reporting section, Addressing Grievances, and Scope. Citing two independently-descended template families, rather than one, is itself useful evidence that the shared shape (behavior expectations, enforcement ladder, scope, grievance process) is convergent practice, not one lineage's idiosyncrasy. The Geek Feminism wiki's policy page remains unverified.

## The policy as a culture document

A policy can carry the event's identity rather than only its prohibitions. !!Con's own text: "where many Codes of Conduct start and stop at preventing harassment, ours is part of an intentional effort to define the culture of !!Con events."

- It frames attendees as "everyone who attends helps construct !!Con" and titles its behavioral section "How to be !!Con".
- It carries concrete cultural norms alongside the harassment rules: pronoun badges as a default expectation, and "assume that all your fellow conference-goers are technical" as an explicit anti-gatekeeping norm.

The Recurse Center's social rules ("no feigning surprise", "no well-actuallys", "no backseat driving", "no subtle -isms") are the adjacent pattern, adopted by !!Con and others. Recurse Center states the distinction itself: the social rules are deliberately **lighter** than a code of conduct and are "not for punishing people". Keep the two layers visibly separate in the document, so the enforcement section stays about harm and the norms section stays about manners.
