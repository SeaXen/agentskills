# Vellum Conf startup track: pitch block and founder-investor meeting programme

Two skills' rules shaped this design. `startup-pitch-contest` owns the pitch block. `event-b2b-matchmaking` owns the 1:1 programme, so Part B applies its rules and builds no booking mechanic of its own. The skills expect an interview, one question at a time. That wasn't possible here, so every unknown is a labelled assumption in § 1 and a question in § 9.

## 0. Verdict

1. ❌ **Don't write "5 founder meetings" into Gold yet.** Four things have to be settled first:
   - who the Gold sponsor is
   - which founders count
   - whether founders can decline
   - whether investor capacity exists

   Until then the only honest rungs are a best-efforts target or no promise (§ 8).
2. ⚠️ **"Three guaranteed 1:1s per company" is a promise made on investors' behalf.**
   - It is honest only once named investors have committed capacity in writing.
   - Capacity must cover three meetings per accepted company, plus reserves for declines and no-shows.
   - Only then can the slate be fixed. Investor capacity caps the slate, so secure it first.
3. ⚠️ **The guarantee turns the meetings into an entry term, not a prize.** The winner's award must be something else.
4. 🔐 **Judges who are investors get structural access to every company.** The meetings make that access explicit. Disclosure is mandatory, and no judge meets a slate company 1:1 before the result is final (§ A5).
5. ⏳ **The pass threshold (six items, zero blanks) is not met.** Blanks are listed in § 9. Don't publish the call until they are closed.

## 1. Inputs

| Input | Status | Source |
|---|---|---|
| 25-minute 1:1 slots | Given. Not validated: a slot needs gaps (§ B5), and this design states no gap length | You |
| Three investor meetings per pitching company | Given | You |
| "5 founder meetings" in Gold | Given, not yet defined | You |
| Booking through a tool | Given | You |
| Event date, grid, pitch block position | **Open** | — |
| Whether Gold sponsors are funds, vendors or both | **Open** | — |
| Whether any sponsor judges, or has a contractual say | **Open** | — |
| Whether any award carries capital | Assumed no. A yes fires gate Q6 | — |
| Recording, streaming or press in the room | **Open** | — |
| One-off or recurring | **Open.** Default: one-off | — |

Today is 2026-10-16. The only published floor is 4-6 weeks between notifying a company and the stage. Check the event date against it before choosing the funnel (§ 6).

## 2. Build order

Each step feeds the next.

1. **Investor commitments in writing** (§ B3). This gives the capacity ceiling.
2. **Awards** (§ A1).
3. **Funnel and published route** (§ A2). The slate can't exceed the capacity ceiling.
4. **Format and block arithmetic** (§ A3).
5. **Rubric, conflict rule, gates.**
6. **Meeting mechanics and tool** (Part B).
7. **Gold wording** (§ 8). Last, because it depends on everything above.

## Part A. Pitch block

### A1. Awards

| Item | Rung | Delivered by | Written status |
|---|---|---|---|
| Three investor 1:1s per accepted company | Committed slot with named third parties | Each named investor, via the organizer | **Blank.** Needs a signed commitment per investor |
| Winner: recognition, with a write-up | Recognition only | You | You control it |
| Winner: named introductions, both sides consenting | Committed introductions | One named organizer, by a published date | **Blank.** Names and date needed |

- No capital is awarded. If that changes, stop and send the structure to counsel before announcing.
- Don't announce investor-meeting commitments the investors haven't signed. This is the failure mode the skill flags most strongly.
- If the winner's introductions overlap with the three meetings, count each meeting once, to one ledger (§ B6).

### A2. Funnel

The default is **open application, single review pass**. Two promotions are checked, and neither is confirmed:

- A **screening call** is promoted if the block is fixed and short relative to demand, or if investors were invited because of who would pitch. Investors are a core selling point of the three-meetings offer, so lean towards promotion. Confirm it against the open questions.
- **Nomination** is promoted only if named referrers already exist.
- **Curated invitation** is deleted if you have already announced a public route.

**Published route (draft, bracketed items open):**

> Companies at [stage, in the call's words] may apply by [date]. Applications are read by [named reviewers] against the criteria and weights below, in [single pass / pass plus screening call]. Nobody else reads them; they are deleted by [date]. Accepted companies are notified by [date], commit to pitching in person on [date], and receive three booked 25-minute meetings with investors who have committed in writing. Meetings are accepted by both sides before they appear on any schedule. The winner receives [named introductions] by [date]; no capital is awarded.

Application form: use the skill's field list. Two additions:

- Ask separately whether the company consents to its profile being shared with investors and Gold sponsors for matching. Application material and matching data are different custody.
- Skip the deck and financial detail. They are custody-bearing and can't be scored in a review.

If investor reviewers read applications, say so in the call.

### A3. Format and block arithmetic

**Format: stage pitch plus judge questions.** Stage-only is deleted because the award commits third parties. The closed-door deep dive is not promoted unless the population is "raising against traction" (Q2).

**Arithmetic.** The formulas come from `hackathon-judging` (`N ≤ W/t`). Only the input is re-measured:

- `t` = published slot + question time + walk-on/off, measured on your stage.
- The panel sits together, so it is one unit. Full coverage holds when `N × t ≤ W`.
- If `N × t > W`, the levers are: cut the field, shorten the slot, extend the block, or pre-score. Never shorten `t` on the day.

**Constraint from Part B:** the slate must also satisfy `3N + reserves ≤ committed investor meeting slots`. Take the minimum of that and the block fit.

### A4. Rubric

Weights are integers summing to 100, published in the call. They are the organizer's decision, so none are proposed here.

| Dimension | Kind | Verified against |
|---|---|---|
| Problem and product legibility | Observable | The block |
| Working product shown live | Observable | The block |
| Answers under question | Observable | The block |
| Evidence of traction | Claimed | Application traction field, checked by a named reviewer |
| Team fit | Claimed | Application team field |
| Fit to the award on offer | Claimed | "What the company wants" field |

- Don't weight a claimed dimension unless a field and a checker exist.
- Score after each company, before the next starts.
- Tell the panel in the brief that company #1 is scored against the scale, not against nothing.

**Tie-break ladder (publish in the call):**

1. Highest score on the top-weighted observable dimension.
2. Most first-place votes.
3. A named judge with no declared interest decides, on the record, in one sentence.
4. A shared award, only if the call said so and the items are divisible.

No re-pitch and no random draw.

### A5. Conflict rule

**Default: recusal plus disclosure to the pitching companies.** At least one active investor will sit on the panel, so "no stated rule" is deleted. The meetings add three rules:

1. **Collect three answers in writing at invitation:**
   - Does the judge or their fund hold a position in an applicant or in a competitor?
   - Is the judge allowed by their institution to sit and to see this material?
   - Does the judge intend to approach companies from this stage, and will they accept the routing below?
2. **Disclose before the block.** Judge interests go on one slide before the first pitch, not after the result.
3. **No judge meets a slate company 1:1 before the result is final.**
   - A 1:1 would give that judge traction detail the other judges don't have. That interest sits upstream of the vote, and recusal doesn't remove it.
   - Schedule the meeting block after the result is final. Alternatively, hold judge-investors' meetings with slate companies until then.

**Contact protocol (the starved rung): recommended, but your call.**

- Its route element is already in place, because the organizer brokers every meeting.
- Promotion is keyed to capital (Q6) or recurrence (Q9). Both are open.
- If you promote it, publish the stand-off window as a date and state that the result is final before the window opens.
- It is the hardest rung to unwind next edition. Decide deliberately.

**Judge brief (adapted from the skill's wording):**

> You will see these companies before most people do, and some of you will meet them 1:1 in the meeting programme. Tell us now if you or your fund hold a position in any applicant or competitor, and if your firm's rules limit your sitting or seeing this material. Meetings with slate companies happen after the result is final. You are judging for the event today, not sourcing for your fund.

### A6. Gates

| Gate | Fires if | Response |
|---|---|---|
| Q6 capital | Any award carries capital, an instrument or equity | Counsel before announcing. This design states no threshold, form or amount. Contest-law classification routes the same way |
| Q7 sponsor say | A signed agreement gives a sponsor a say in who pitches or wins | Confine the say to what was bought. Pair it with neutral judges. Check the result survives dropping those scores. Disclose before the call closes. **A pitch slot is never for sale**, so check the Gold package carries none |
| Q8 recording | Recording, streaming or press in the room | Applicants are told before they apply and re-consent before the block. This can't be retrofitted |

### A7. Announcement and contest path

- Announce from a prepared list.
- Publish the contest path before the call closes: who receives a challenge, a window closing before anything of value changes hands, and what can change (an arithmetic or eligibility error, never a judge's opinion).
- Withhold raw per-judge scores.

## Part B. Meeting programme (applying `event-b2b-matchmaking`)

### B1. Does it run?

Yes. You have two populations invited separately (founders and investors) and a named meeting number. Both are the skill's promotion triggers.

### B2. Matching criterion (draft)

> A meeting is a good match when an investor who stated the stages and sectors they invest in meets a pitching company at that stage in that sector, and both accepted the pairing.

**Mechanism: mutual opt-in, with organizer-brokered pre-assignment of each company's first three.** That is the hybrid scheduling rung, which the skill requires once a contracted number exists. Every pre-assigned pair needs an acceptance step from both sides before it appears on any schedule. Pairing only one side's choice is deleted.

### B3. Investor commitment

You can't guarantee three meetings for every accepted company without this.

**Each named investor commits in writing to:**

- a maximum number of assigned meetings
- stated stage and sector criteria
- a response date for each pairing
- a named replacement person in case they can't attend

**Capacity check.** Let `C` be the sum of committed meeting slots. Then `3N + reserves ≤ C`. Reserves cover declines and no-shows. Don't derive a reserve figure from anyone else's data; measure your own after the event.

**A standing acceptance is not a placement.**

- The deleted rung is a meeting placed on someone's schedule without their acceptance.
- The tool should still show each pair for individual acceptance, and the investor may decline for a declared conflict only.
- **Validate this reading with me before you rely on it.** It is the point where the guarantee and the "no placement without acceptance" rule are closest to colliding.

### B4. Consent

Consent scope is fixed by the wording at submission. Say the following in the founder's and investor's line of sight:

- which fields a counterpart sees
- that they see them only after mutual acceptance
- what they get out of it
- how to withdraw, and what happens to accepted pairings if they do
- when the pool is deleted

Gold sponsors receive meetings with named founders only after mutual acceptance. They never receive a list.

### B5. Scheduling

- **Take the block as given.** It sits in the grid you were handed, and no session moves for it.
- **After the result.** Place it after the result is final (§ A5).
- **Slots.** Use your 25 minutes, equal slots, with gaps between them. This design states no gap length. Choose it from the block and your real pair count.
- **Feasibility check (my construction, not a figure from either skill):**
  - Let `R` be the number of rounds the block holds.
  - Each person's load must be ≤ `R`.
  - Tables `T` must satisfy `T × R ≥ total meetings`.
- **Founder load.** A founder's load is three investor meetings plus any Gold meetings, and it must fit in `R`. This usually binds before table count does.
- **One view per person.** Never publish the full grid.
- **One named organizer on duty** for the block.

### B6. Ledgers

Keep two ledgers and count each meeting once, to the one it was booked against.

- **Ledger A.** The founder guarantee: three per accepted company.
- **Ledger B.** Gold quota meetings.

If a Gold sponsor is a fund and sits in the investor pool, its Ledger B meetings don't also fill a founder's three. Otherwise a paying sponsor's meetings would be passed off as the free guarantee.

### B7. No-show handling

- **Default: reconfirm and remind.** Explicit acceptance at booking, then a reminder before the block.
- **Standby refill is promoted.** A guaranteed count needs refill, and the block should be staffed anyway.
- **Overbooking is deleted.** You hold no measured booked-versus-held figure for this programme.
- **No deposits or penalties** on either side. An investor no-show on a guaranteed meeting triggers a replacement from the reserve.
- **Make-good for a founder.** A post-event introduction to a consenting investor, made by a published date. A fee refund doesn't apply, because founders pay nothing here.
- **Never make good with program access or attendee data.**

### B8. Tool requirements

Choose the tool against these. Don't quote any vendor's fill or no-show figures; they are sales material.

- Enforces mutual acceptance, and refuses to create a pair without both sides.
- Supports pre-assigned slots with an acceptance step.
- Shows each person only their own schedule.
- Doesn't expose a roster to Gold sponsors.
- Shows consent wording in the person's line of sight.
- Deletes the pool on a stated date.
- Exports the outcome record in B9.
- Lets you check who holds the data. Route that question to whoever owns your data obligations; if nobody does, report that absence.

### B9. Meeting brief and outcome record

**One brief for everyone, once:**

- the matching criterion
- who may join, and how
- what data is collected, shared and deleted, and when
- that both sides must accept
- the block position and where meetings happen
- the slot length
- how to decline or cancel
- what happens to a missed slot
- the named organizer on duty

**Outcome record, one row per pairing:**

- the two sides
- which ledger
- whether both accepted
- whether it was held
- whether it was refilled from standby
- which criteria it was checked against

Hand the record on. Per-sponsor tracking belongs to sponsor fulfillment, not here.

## 6. Timeline

Anchors in order: call opens, call closes, slate notified, meeting booking opens, stage.

- **Floor:** 4-6 weeks between slate notification and the stage, because accepted founders need travel and time off.
- **Below the floor** the open rungs stop working and the slate goes to invitation.
- **Early step:** investor commitments (§ B3) must be in before the call closes.
- **Booking opens only after the slate is fixed,** and the schedule stops moving after a published date.
- Check the event date against the floor before choosing the funnel.

## 8. Gold tier wording

**Hold "5 founder meetings" until the following are decided.** Then pick one of the two forms below.

**Four decisions to settle first:**

1. Which founders count: pitching companies only, or other attendees too.
2. Whether those founders are obliged to accept, or may decline per meeting. If they may decline, no count can be guaranteed.
3. Whether the Gold sponsor is a fund or a vendor. A vendor's meetings are sales meetings, which developer-event attendees usually treat as interruptions.
4. Whether pool capacity exists. Let `G` be the number of Gold sponsors and `F` the opted-in founders. Total Gold demand is `5 × G` and must fit within `F` and every founder's load.

**Form 1: best-efforts target (the default).**

> We will aim to arrange five meetings with founders matching the criteria in Schedule X. This is a target, not a guarantee, and no remedy attaches to a shortfall.

**Form 2: guaranteed count with criteria.** Use it only after the four decisions above, with a make-good you can still fund after the event:

> We guarantee five meetings with founders matching Schedule X who accepted the pairing. Where fewer are held, the remedy in Schedule Y applies.

Hand the criteria and remedy to `event-sponsor-agreement` for the clause. Two rules cut across both forms:

- Never print a bare number with no criteria and no remedy.
- Sponsor meetings are access, never a pitch slot, a judging seat or a share of the agenda.

## 9. Pass threshold and open questions

| Item | State |
|---|---|
| Published route onto the stage | Draft. Dates, reviewers and stage blank |
| Criteria and weights | Weights blank |
| Pitch format and block it fits inside | Block unknown |
| Conflict rule and what it doesn't cover | Drafted. Needs the judge list |
| Award list with committing party | Investor commitments blank |
| Three gate answers | Q6, Q7, Q8 unanswered |

**Open questions, ranked by how much they change the design:**

1. Are Gold sponsors funds, vendors, or both? Does any of them judge?
2. Can founders decline a Gold meeting, and are "founders" limited to pitching companies?
3. Do named investors exist who would commit capacity in writing? Is the pitching population pre-product, first customers or raising against traction?
4. What is the event date, and where do the pitch and meeting blocks sit in the grid?
5. Is anything recorded or streamed, and does a sponsor hold a contractual say?
6. Is this one edition or recurring? That decides whether to promote the contact protocol.

## 10. Measurement

All of these are self-set, and they only mean something across your own editions.

- Held against booked, for the whole programme.
- Booked against promised, per sponsor and for the founder guarantee. Never average across sponsors.
- Award items delivered against announced, per party.
- Declared judge interests against those that surfaced later.
- Unwanted-meeting complaints (target zero), and confirmation completeness (every scheduled pair accepted by both sides).
- Applications from companies nobody on the team knew. This is the only read on whether the funnel did more than an invitation list would.

Choose two or three and write down the change each would trigger.