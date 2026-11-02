# VantiqCon standing-team design

## Verdict

- ❌ **Do not form a non-profit association.** VantiqCon is company-run. Vantiq is already the legal entity, the budget owner, and the employer.
- ✅ **Fix decision rights, not the legal entity.** Your problem is that nobody knows who decides the agenda and who decides spend. An association would not fix that.
- 🎯 **Build a two-layer structure inside Vantiq.** A small steering layer owns money, contracts, legal, and code-of-conduct escalation. An organizing team owns program and logistics.

I could not run the skill's one-question-at-a-time interview. The assumptions are listed at the end, with what would change if each is wrong.

## 1. Current structure, as it probably operates

- **Agenda:** whoever drives the program that year decides. That is probably you, but it is not written down.
- **Spend:** whoever holds the marketing budget decides. That is probably a marketing leader above you, but it is not written down.
- **Engineering:** pulled in each year, so engineering knowledge resets every edition.
- **Bus factor:** you are probably 1 on program and on cross-edition memory. The two marketing people are probably 1 on their own areas.
- **Budget line:** it sits in one discretionary pot. The skill's strategy sibling treats "no named line owner" as a failure that stays silent until the pot is empty.

## 2. Entity posture: no entity

For a company-run event the skill deletes the entity menu: no association, no fiscal sponsor, no ranking. Ranking them "invites a volunteer-shaped structure to reappear beside a legal one that already exists."

Reasons it does not fit VantiqCon:

- **Evidence mismatch.** The case for a standing non-profit comes from community-run events. The DjangoCon US standing entity vs. DjangoCon Europe rotation comparison does not transfer. VantiqCon already has a standing body: Vantiq's staff.
- **Cost without a fix.** An association means bylaws, board fiduciary duties, annual filings, and a structure that is hard to unwind. None of that touches your agenda-vs-spend confusion.
- **Independence.** An association funded 100% from Vantiq's marketing budget would not be independent. It would add a second set of approvers.
- **Identity.** This is a positioning and governance question, solved in section 3. Give VantiqCon a public charter, external community members on the program committee, and sponsors who cannot buy agenda slots.
- **Community money.** Sponsors can pay Vantiq under a standard sponsor agreement, with no entity needed. Name who is offering money and what they want before reopening this.

**Reopen the entity question only if** Vantiq decides to hand over the brand and ownership, or several companies want to pool money with none of them as sole counterparty. At that point the event is community-run. Re-run the entity menu then: an umbrella first, an own entity if it is meant to outlive Vantiq's involvement. This conclusion is a published-practice rule from the skill, applied to your case.

## 3. Decision rights: board-plus-organizers split, internal version

This is published practice. Every large durable event in the case record converged on it, across five independent organizations. Here the "board" is a steering group of Vantiq employees.

| Decision | Owner | Consulted | Cannot be overridden by |
|---|---|---|---|
| Event goals, total budget envelope | Steering (executive sponsor + budget owner) | DevRel lead | Anyone in the operating team |
| Spend within the envelope | Budget owner (marketing), within lines steering set | DevRel lead | Program committee |
| Contracts, venue, legal terms | Steering | Logistics lead | Operating team |
| **Agenda: tracks, talks, speakers** | **Program lead (you) + program committee** | Engineering liaison | **Spend owner, sponsors, steering** |
| Sponsor packages | Sponsorship lead, inside steering's price floor | Program lead | Sponsors cannot buy slots |
| Code-of-conduct escalation | Steering, via a named CoC team | CoC team | Operating team |

Rules to write into the charter:

- **Separate the two decisions.** Steering sets the envelope and the goal. The program lead decides what goes on stage within them. Steering may veto a talk only for legal or conduct reasons, and must say so in writing.
- **Keep the steering group small.** The skill's sanity check is one coordinating layer per 5-8 leads. I suggest three people: an executive sponsor, the budget owner, and you (self-set).
- **Don't pay for a vote with money.** If sales or product co-fund later, they get a steering seat scoped to their goal, not a vote on the agenda. The strategy sibling warns that a co-funder without a metric in the goal holds a veto with no accountability.
- **Add a federation only if the event is multi-unit.** A federation fits parallel tracks with their own CFPs or several cities. That is not known here (see assumptions).

## 4. Role taxonomy

Each role gets a one-paragraph written scope that states what it will not absorb. Every role gets a named backup.

| Role | Scope boundary (will not absorb) | Backup |
|---|---|---|
| Event lead / program lead | Owns agenda. Does not approve spend. | To name |
| Budget owner | Spend inside the envelope. Does not choose speakers. | To name |
| Sponsorship | Packages and fulfillment. Does not touch the agenda. | To name |
| Logistics / venue | Venue, production, vendors. | To name |
| Marketing and registration | Landing page, comms, ticketing. | To name |
| Volunteers | Day-of workforce (see `event-volunteers`). | To name |
| Code of conduct | Response team, escalation to steering. | To name |
| Engineering liaison | Speaker sourcing, demos, engineering time. | To name |

- **Sizing.** Your 3 named people plus an annual engineering pull-in is thin. The closest benchmark is JSConf EU 2019: about one core organizer per 270 attendees, 6 for 1,600, a team that called itself unsustainable. At 1,100 attendees that points to roughly 4 core people. It is a strain signal, not a formula.
- **Engineering liaison.** Make this a named role with a time budget agreed with their engineering manager, written down. "Whoever we pull in each year" is a rotation with no continuity.

## 5. Succession, by at-risk role

1. **Two-deep rule, this week.** Name a backup for every role in section 4, including you. The skill's default.
2. **Charter plus shared custody.** Write roles, scopes, and decision rights down. Move the domain, ticketing, social accounts, vendor logins, and bank-card access to company-owned shared accounts with at least one backup admin. Split mailboxes in two tiers: a standing team address, plus a per-event address with per-person aliases.
3. **Planned rotation is allowed.** Rotating program co-chairs or the engineering liaison works because Vantiq's core team is the continuity layer underneath. Do not rotate the whole team, which is DjangoCon Europe's documented fragility.
4. **Lead succession.** Name your successor and run a handover window of 6-12 months. That figure comes from a meetup-organizer survey, so treat it as self-set here.
5. **Pipeline.** Optional, for later. Give external program-committee members a path to co-chair.

## 6. Burnout guardrails

- **Backups.** Covered by the two-deep rule, so nobody works alone.
- **Written boundaries.** Each role's "will not absorb" list.
- **Workload budget.** The 4-8 hours/month figure is a meetup-scale estimate for volunteers. It is not a benchmark for your paid team. Set your own budget per person each year, and split any role that structurally exceeds it.
- **Annual check.** Ask each person, you included: "Is organizing still pleasant?" A "no" gets a structural response within the edition: shrink scope, add a backup, or rotate the person out for a cycle. Owner: the executive sponsor.
- **Named return per person.** Record what each person gets: learning, network, visibility, career. A return that disappears predicts a departure.

## 7. Conflict-of-interest clause

A company-run event is not neutral, and the clause should say so. The skill's version covers an employer's interest as the normal case.

- **Purpose sentence.** "Business is a consequence, not the goal."
- **Content.** Stage talks from Vantiq staff, customers, and partners are expected. Commercial pitches are not.
- **Register.** Each organizer lists employer, own company or freelance work, and sponsor, vendor, or partner ties. The register is visible to the team.
- **Abstain.** Organizers recuse themselves on their own talk, their own team's talk, and any vendor or sponsor they hold a stake in.
- **Public.** Publish the clause with the charter. An opaque team reads as a clique to a technical audience.

## 8. Paid-hire gate

- **Verdict.** Not yet on the published threshold (low-thousands of attendees and/or a six-figure budget, with year-round burden). 1,100 attendees is below it. A B2B conference budget may be six figures, so I need the budget.
- **If the pain is execution capacity,** buy a logistics vendor first. That is the documented middle path. DjangoCon US uses vendors instead of staff.
- **If the pain is year-round burden,** file a headcount request for an **event coordinator or manager**. Every documented first hire in the record except one was an events role, never a community manager. Program and community leadership stay with you.
- **Re-run this gate every edition.** Once it says hire, use `dev-event-hiring` for the scorecard.

## 9. Strategy layer, routed

Goals, budget ownership, and measurement belong to `corporate-event-strategy`, not here. This design needs its outputs. Settle these before registration opens:

- A named budget-line owner. The marketing-only line dies with its champion, so name a successor.
- Goals, each with a metric, an owner, a source system, and a read date.
- The three pre-launch reviews: terms and insurance, attendee data moving into sales systems, and hosting customers and prospects as guests. Send them to counsel.

## Options rejected

- **Own non-profit:** fixes no part of your problem and adds filings and a second approver.
- **Fiscal sponsor or umbrella:** Vantiq is already the entity.
- **Consensus committee:** works under about 5 people and below the money line. You hold contracts and spend.
- **Whole-team rotation without a standing layer:** DjangoCon Europe's documented fragility.
- **Community manager as first hire:** it funds the part volunteers still enjoy.

## Do this week

1. Name the budget owner and the executive sponsor. Estimated time: 30 minutes.
2. Write the section 3 decision table as a one-page charter. Estimated time: 1 hour.
3. Name a backup for every role and move shared accounts off personal ownership. Estimated time: 2 hours.

## Assumptions and open questions

| Assumption | If wrong |
|---|---|
| Single track or few tracks, one city | Parallel CFPs or several cities: add domain-lead federation |
| Budget is six figures | Under that: a vendor, not a hire, becomes the whole paid menu |
| No co-funders today | Sales or product funding: add a scoped steering seat, run the budget-ownership menu |
| You hold agenda authority de facto | Marketing holds both: the split becomes a real political decision, run brainstorming mode with 2-3 candidate designs |
| The "community money" is sponsorship | Donations or grants from other companies: this is the reopen trigger for the entity question |
| Engineering gets pulled in with no agreed hours | A named liaison already exists: keep them |

## Revisit

Review this design after each edition, using the debrief. Treat it as revisable: the EuroPython Society reworked its own structure seven years in. Each choice above is published practice unless marked self-set.