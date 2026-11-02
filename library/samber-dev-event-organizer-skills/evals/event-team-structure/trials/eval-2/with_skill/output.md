# PyCoast rotation plan: staggered rotation over a standing layer

## Read this first

I recommend against the plan as voted ("everyone swaps, all roles, next edition"). Your goals are fair load-sharing and no burnout, and I've kept both. The same-year swap loses things those goals don't depend on, and I've made it a two-edition rotation. **Next action:** show the team Section 1, then ask for a re-vote on Section 3.

I wrote this without asking you the interview questions one at a time. The assumptions are listed at the end. Each choice is labeled **[published]** (documented practice), **[borrowed]** (from another domain) or **[self-set]** (my default for you).

## 1. Why not swap everyone at once

- **You are the structure, and nobody else is.** You sign the venue contract personally and get reimbursed afterwards. Venue relationship, deposit float, liability and probably the accounts all sit with you. If every role changes hands at once, all of that goes with you in one step.
- **Full-team rotation with no standing layer is a documented weak design [published].** DjangoCon Europe does this. It has had recurring trouble finding hosts, and one team ended up running three editions in a row. DjangoCon US has a standing entity with rotating chairs under it, and it has proven more stable. KubeCon also rotates co-chairs, but only over paid foundation staff.
- **You have no continuity layer.** Rotation needs something that holds the institutional knowledge. PyCoast has no entity, no board and no sponsor, and the knowledge lives in six heads.
- **Fairness and burnout are still met.** Rotation works as a structure when each role has a backup and the team rotates in waves. Your six people can do that.

## 2. Current structure (bus-factor map)

| Role | Holder today | Bus factor |
|---|---|---|
| Chair/coordination | You | 1 |
| Finance and contracts | You (de facto) | 1 |
| Program | Fill in | ? |
| Sponsorship | Fill in | ? |
| Logistics/venue | Fill in | ? |
| Marketing, volunteers and CoC | Fill in | ? |

Fill in the "?" rows with your team. Any role where nobody else could run next edition scores 1. You likely hold two roles, chair and finance/contracts, so you are the largest single point of failure. Six people for 380 attendees is a healthy ratio. The JSConf EU team (6 core organizers for 1,600 attendees) was too small by its own account.

## 3. The design

### 3.1 Entity posture [published, self-set choice]

- Today's "no entity" posture is only cheap while there are no contracts, and a signed venue contract ends that. Move up at the first signed contract.
- **Default for you: fiscal sponsor or umbrella.** The umbrella holds the money and signs, and you operate. Ask first whether a Python-community body you already belong to would do this.
- **Own non-profit:** only if PyCoast intends to outlive its founders and you can carry bylaws and annual filings. Decide this before you sign the next venue contract.
- **Until then:** one named treasurer holds the money, and the signer never changes mid-contract. Ask the venue whether the contract can be assigned to the umbrella once it exists. I can't give legal advice, so check with someone qualified.

### 3.2 Decision rights: standing layer plus operational team [published]

- **Standing layer (does not rotate annually):** budget and money, contracts, legal, and CoC escalation.
  - **Seats [self-set]:** two people, the Treasurer and one Standing Member, on staggered two-year terms. Their terms must never end in the same year.
  - **Who:** you are the natural Treasurer/contract holder until the umbrella exists.
  - **CoC escalation:** goes to the standing layer, never to the operational lead who is the subject of a report.
- **Operational team (rotates):** Chair, Program, Sponsorship, Logistics/venue, Marketing/comms, Volunteers/CoC coordinator. Six people hold five operational roles and the two standing seats. Some people hold one of each, so keep each person's total within the workload budget in 3.5.

### 3.3 Rotation waves [self-set]

Rotation runs on two-year terms, with half the roles moving each edition.

- **Wave 1 (edition 4):** Program, Marketing/comms, Volunteers/CoC coordinator. The incoming person takes over at the start of the edition cycle, and the outgoing person stays on as backup.
- **Wave 2 (edition 5):** Logistics/venue, Sponsorship, Chair (you).
  - Sponsor relationships and venue contacts carry cross-edition knowledge, so these roles get a full edition of shadowing first.
  - Your seat as Chair rotates in wave 2, so your word "including mine" still holds. The incoming Chair shadows you for all of edition 4.
- **Standing seats:** terms are staggered and the first change comes after edition 5.
- **Everyone has rotated within two editions.** Nobody holds a role for more than two. In the wave a person's role is not rotating, they act as backup for someone else's.

### 3.4 Handover dates and who briefs whom

Dates are relative to **E**, your edition 4 date. I don't know E, so substitute real dates. The 6-12 month handover figure comes from a meetup-organizer survey [published, small sample]. If E is under about 9 months away, keep wave 1 to the lowest-memory roles (Marketing, Volunteers) and push Program to edition 5.

| When | What | Who |
|---|---|---|
| Within 4 weeks | Re-vote on the staggered plan. Name the incoming lead and backup for every role. | Whole team |
| Within 6 weeks | Charter v1. Domain, socials, ticketing and bank access moved to shared custody with a backup admin. | You, with a backup admin |
| E-12 to E-9 months | Wave 1 handover. Outgoing lead briefs incoming lead (see below). | Outgoing → incoming |
| 2 weeks after each handover | Incoming lead gives a teach-back: reads back the brief and flags gaps. | Incoming → outgoing |
| Through E | Outgoing lead stays reachable as backup and does not run the role. | Outgoing |
| E+4 weeks | Debrief: pleasantness check, bus-factor map re-run, wave 2 shadowing starts. | Whole team |
| E+12 months (edition 5 cycle) | Wave 2 handover, same pattern. Chair handover is last. | Outgoing → incoming |

**Briefing chain:**
- The **outgoing lead** gives the incoming lead a one-page role brief: scope, boundaries (what the role does not absorb), calendar, accounts, contacts, open commitments, and known mistakes.
- The **Treasurer** briefs every incoming lead on budget authority, reimbursement process and what needs a second signature.
- The **Chair** briefs everyone on the charter and the standing-versus-operational split.
- The **backup** is the successor-designate for the next wave, so two-deep and rotation use the same pairing.

### 3.5 Burnout guardrails [published, self-set thresholds]

1. **No role without a backup.** FOSDEM enforces two managers per devroom, and the same rule applies here.
2. **Written role boundaries** in the charter, including what each role will not absorb.
3. **A workload budget per person, reviewed yearly.** The published estimate is 4-8 hours a month at meetup scale. Conference scale is higher, so set your own number. A role over budget gets split, not exhorted.
4. **An annual per-person pleasantness check** ("is organizing still pleasant?"). A "no" triggers a structural response in that edition: shrink the scope, add a backup, or rotate the person out for an edition.
5. **A named return per person**: leads, network, learning or fun. Record it next to the bus-factor map.

### 3.6 Conflict of interest [published]

Keep a team-visible register of each organizer's employer, own company or freelance services, and sponsor ties. People abstain from decisions on their own talk, their employer's talk or sponsorship, and any vendor they have a stake in. Business among attendees is welcome. The charter should state that "business is a consequence, not the goal."

### 3.7 Paid-hire verdict

**Stay volunteer and restructure.** At 380 attendees the paid-hire threshold (low-thousands of attendees or a six-figure budget) isn't met. Re-run the gate every edition and record the verdict.

## 4. If the team still wants a same-year full swap

You can still do it, but these conditions apply first:

1. The entity or umbrella and the shared-custody accounts are in place before anyone hands over.
2. The venue contract signer and the treasurer stay fixed through edition 4.
3. Every incoming lead gets the full briefing chain above, with teach-back, and outgoing leads stay on as backups for the whole edition.
4. You accept the risk that edition 4 is run by people who have never held their role. The DjangoCon Europe record shows where this leads.

## 5. Short pitch for the re-vote

> Rotation is still the rule. Every role changes hands within two editions, including the Chair. Half rotate now and half next year, each new lead gets an overlap with the outgoing one, and the money and the venue contract are held by a small standing layer so nobody inherits personal liability. That keeps the fairness and the burnout protection the vote was for, without everyone starting from zero in the same year.

## Assumptions to confirm

- Edition 4 date, so the relative dates become real ones.
- Whether any organizer works on PyCoast on employer time, or has a commercial interest in the audience.
- Whether a parent body could act as umbrella, and how much legal paperwork the team will tolerate.
- Whether this is a patch for edition 4 or a multi-year institution. That decides umbrella versus own entity.
- Whether anyone on the team answers "no" to the pleasantness check today.
- Whether PyCoast runs parallel tracks or a single track. I assumed a single track.
- Whether you hold any other role besides chair and finance. I assumed that only for the bus-factor map.

**Review cadence:** revisit this design at each debrief. EuroPython reworked its own structure seven years in, so treat this as a revisable draft, not a constitution.