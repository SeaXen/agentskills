# Backend Days standing-team design

I couldn't run the skill's interview (it asks one question at a time), so I filled the gaps with the assumptions listed in section 1. Each choice is labelled **[published]** (observed at other events), **[borrowed]** (from open-source or corporate practice) or **[self-set]** (my number, and yours to calibrate).

## 1. Diagnosis and assumptions

**Current structure.** Nine people run a consensus committee. Consensus works for about 5 people with no money and no contracts **[published]**. You have 900 attendees, EUR 180k of sponsorship, three tracks and a venue contract signed 14 months out. The committee routes every decision through one room, including decisions that belong to a single person. That is the finding, and the three-hour call and the dropouts are what it costs.

The dropouts are a structural signal, not a mood. The skill treats "organizing is no longer pleasant" as a tripwire **[published]**.

⚠️ **Assumptions to confirm.** Any "no" changes the design:
- The event is community-run, not a company marketing program.
- No legal entity exists yet. Contracts are signed personally or by one person.
- The event is meant to outlive its current organizers.
- Nobody on the team is paid.
- The curators' deputies, if any, are not yet named.

## 2. Verdict

Use a **board-plus-organizers split**, with a **domain-lead layer for the three tracks** underneath it.

- A small standing board holds money, contracts, legal and code-of-conduct (CoC) escalation.
- Track curators get full autonomy over content, plus a budget envelope.
- They do not get autonomy over money, contracts or sponsors.

The board split is the shape every large durable event converged on **[published]**. It applies from the moment an event holds money and contracts, and you passed that point already. Three tracks with their own CFPs also meet the promotion condition for domain-lead authority. FOSDEM works this way: devroom managers have full content autonomy, while the central team keeps shared infrastructure and track acceptance **[published]**.

**Rejected:**
- **Staying a consensus committee.** It has no one who can hold a contract, and it spends the whole group's attention on every decision.
- **Pure federation with full track autonomy.** Federations and franchises work when each unit has its own money, such as a local team running a licensed brand. Your three tracks share one venue contract, one sponsor pool and one budget. Autonomy over those would let two curators commit money the other seven are liable for.

## 3. Entity posture

You crossed the "no entity" line when the venue contract and five-figure sponsorship appeared. Today the exposure sits on whoever signs.

**Recommendation: incorporate your own non-profit now.** Aim to have it registered at least three months before the venue signing. Fourteen months is enough time in most jurisdictions.

- **Why:** the standing-entity design (DjangoCon US) proved more stable than full rotation (DjangoCon Europe) **[published]**, and you intend to outlive the founders.
- **Cost:** bylaws, board duties and annual filings. These are hard to unwind.
- **Fallback:** if a parent foundation or fiscal sponsor will umbrella you, take that. It is near-free and removes the filing burden. It does not fix team continuity on its own.
- **Reserve:** once the entity exists, build a reserve sized to survive losing one edition's budget. EuroPython's is the benchmark **[published]**.
- **Interim:** before the entity or umbrella is in place, name one signer and a backup signer in writing. Don't leave the signature with whoever happens to be on the call.

## 4. Decision rights: standing layer vs operations

| Layer | Who | Decides |
|---|---|---|
| **Board** (3 seats **[self-set]**: chair, finance, contracts/legal) | non-curators where possible | Total budget and track envelopes, venue and all signed contracts, sponsor rate card and exceptions, legal, CoC escalation, any spend above the lead thresholds |
| **Track curators** (3) | one per track, each with a deputy | Their CFP, review panel, talk selection and speaker line-up, within their envelope |
| **Functional leads** | sponsorship, logistics/venue, comms/marketing, volunteers, CoC team | Day-to-day work within their approved budget line |

The board has 3 seats, and none is held by a curator. A curator on the board would approve their own envelope. Curators still get a say: they present their envelope request at the annual budget meeting, and the board must answer in writing.

The board coordinates about 6–7 leads, inside the 5–8 range **[borrowed]**.

### Your three Sunday-call decision types

**Sponsorship quotes**
- The board approves a rate card once per edition.
- The sponsorship lead quotes anything on the card alone.
- Only exceptions go to the board: discounts beyond a threshold, exclusivity, or anything touching track naming.
- Sponsors never buy talk slots. That keeps the curators' autonomy credible.

**Talks**
- Each curator decides, backed by a review panel of at least 2 people.
- The board and CoC hold a veto on conduct and brand grounds only. The board never reviews the program.

**Spend above EUR 200.** Replace the flat threshold with budget lines, since EUR 200 is far too low for EUR 180k. The numbers below are **[self-set]**:

- Inside an approved line, the owner decides alone up to EUR 1,000 per item.
- From EUR 1,000 to EUR 5,000, the owner needs one co-sign (the finance lead or the deputy), with a 48-hour async window.
- Above EUR 5,000, or any commitment that outlives the edition, the decision goes to the board.
- A new budget line needs board approval.

Calibrate these against last year's actual spend. The point is that the full group stops seeing routine items.

### Meetings that replace the Sunday call

- **Board:** 60 minutes a month with a written agenda.
- **Leads' sync:** 30–45 minutes, every two weeks, on a weekday.
- **Whole team (all 9):** one 90-minute review per quarter, for information and budget state, not for decisions.
- **Async decisions:** logged in one place. After 48 hours of silence, the proposal is treated as approved **[self-set]**.

### The curators' request for full autonomy

Give the answer in two parts:

- **Yes to content autonomy.** CFP, selection and line-up are theirs. This is the FOSDEM pattern.
- **No to full autonomy.** Money, contracts, sponsors and CoC stay with the board.

Offer the same charter to all three curators. A two-tier arrangement would create the next fight. Ask the two curators one concrete question: "What decision do you want that this charter doesn't give you?" If the answer is their own sponsors, their own budget or their own brand, they are asking to become a separate event. That is a different shape (franchise or peer network) and a different conversation.

## 5. Role taxonomy and bus-factor map

Each role gets a one-paragraph written scope that says what it will not absorb **[published practice]**. Every role needs a backup. FOSDEM enforces two managers per devroom for this reason **[published]**.

| Role | Backup rule |
|---|---|
| Curator A, B, C | Cyclic: A backs B, B backs C, C backs A. Each also names a deputy curator, who becomes the pipeline for the next edition. |
| Sponsorship lead | Backed by the contracts/legal seat. |
| Finance | Backed by the chair. |
| Logistics/venue | Backed by the volunteer lead. |
| Comms/marketing | Backed by a curator. |
| CoC team | At least 2 people, and neither is the chair. |

With nine people, each person is primary on one role and backup on another. Fill in the real names. The map is not done until the lead's own role has a named backup and every account has a second admin.

**Shared access.** Move the domain, bank, ticketing, socials and sponsor CRM off personal accounts. Each gets a backup admin. Use two mailbox tiers:
- a standing team address;
- a separate per-edition address with personal aliases.

## 6. Succession, in order of priority

1. **Two-deep rule.** Do it this week. It costs almost nothing.
2. **Written charter plus shared admin access.** Do it this month. Make the charter visible to the team, with public join-paths, so the leadership doesn't read as a clique.
3. **Groomed handover for the chair.** Name a successor and a handover window inside 6–12 months **[published]**.
4. **Deputy curators as a contributor pipeline.** Each deputy shadows for an edition, then can take over. This is the starter version of the EuroPython ladder.
5. **Curator rotation.** Allow it only now that the board exists, as time-boxed terms (for example two editions). Rotation over a standing continuity layer works (KubeCon) **[published]**. Rotation with no such layer is DjangoCon Europe's fragility, and the skill deletes it as an option in that case.

## 7. Burnout guardrails (owner: chair)

1. **Per-person pleasantness check now.** Ask each of the nine directly. A "no" gets a structural response this edition: shrink scope, add a backup, or rotate the person out.
2. **Written role boundaries.** Each charter says what the role will not absorb.
3. **Workload budget per role.** Measure real hours for two months, then set a budget. A role that structurally exceeds it gets split. The published 4–8 hours per month is for meetups and is too low for you.
4. **Named return per organizer.** Examples are leads, network, learning, less isolation or fun. Record each next to the bus-factor map. A return that disappears predicts a departure.
5. **Surface positive feedback deliberately.** Quiet satisfied attendees plus loud complaints distort the team's sense of impact.

## 8. Conflict-of-interest clause (in the charter)

- "Business is a consequence, not the goal." Put this sentence in the founding text.
- Business among attendees is welcome, such as hiring and freelancing.
- Organizers don't run the event mainly to prospect for themselves.
- Every organizer keeps an entry in a team-visible register: employer, own company or services, and sponsor ties.
- Organizers abstain on decisions about their own talk, their employer's talk or sponsorship, and any vendor they have a stake in. For curators, that means abstaining on submissions from their own employer.
- No commercial demos on stage. Enforce this in the talk guidelines.

## 9. Paid-hire verdict

**Not yet. Stay volunteer and restructure this edition.** The gate has two parts:

- Your budget is six figures, which meets one criterion.
- 900 attendees is below the observed low-thousands threshold, and your pain is decision load, not year-round logistics. The restructure above targets that directly.

If you have money available and the logistics lead is overloaded, **outsource** venue and hotel contracting to a vendor. DEFNA took this route. If the gate trips later, the first hire is an **event coordinator or manager**, never a community manager **[published]**. Program and community leadership stay volunteer. Re-run the gate at every edition debrief.

## 10. Measurement (all thresholds self-set, audit per edition)

- Every role, including the chair, has a bus factor of at least 2.
- The charter exists, is visible to the team, and gives each role a scope, a join-path and decision rights.
- The chair's successor is named, with a handover window inside 6–12 months.
- The pleasantness check ran, and every "no" got a structural response with an owner.
- The paid-hire gate was re-run this edition and the verdict is recorded.
- The conflict-of-interest register is current for all nine people.
- **Time on decisions:** the full-group call is replaced by the cadence in section 4, and total decision time per organizer is down. Track it.
- Review the whole design at the next debrief, then yearly. EuroPython reworked its own structure seven years in **[published]**.

## 11. Order of work

1. This week: name the signer and backup signer, apply the two-deep rule, and move accounts to shared custody.
2. Within a month: write the charter, rate card, line budgets and thresholds, and run the pleasantness check.
3. Within 3 months: stop the Sunday call, and start the board and leads cadence.
4. Before the venue signing: have the entity registered, or the umbrella agreement signed.

Please confirm or correct the five assumptions in section 1, especially the legal-entity status and the multi-year intent. Those two change sections 3 and 6.