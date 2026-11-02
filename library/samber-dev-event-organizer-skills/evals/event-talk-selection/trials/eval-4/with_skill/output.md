**Next action:** tell the board "no" on both points (reasons below), then validate the plan section by section before review opens.

This plan assumes things I couldn't ask you. Those assumptions are listed after the plan, and some change it. I assumed a community conference, where the open pool is the program and no slot is bought.

## Two board asks

### 1. "Accept at least 25%"

- 96 slots / 2,100 submissions = **4.6%**. A 25% rate means 525 talks, which is 5.5x your program.
- Working backward, a 25% rate on 96 slots needs a pool of 384.
- CHI's 26.4% does not transfer. Academic venues accept what clears a quality bar. A conference fills a fixed number of slots in a room.
- Better comparisons are PyCon US 2025 at ~15% of 938 and KubeCon EU 2024 at 9% of 2,541.
- Your 4.6% is steeper than both. Oversubscription of 8–30x is normal at popular events, and rejecting most submissions is the healthy state.
- Treat the ratio as a record, not a target. Log it for next edition.
- The board's real worry is wasting good submissions. Three cheap answers:
  - The finalist band gets written feedback (see Section 7).
  - A waitlist exists.
  - Every decline states the ratio, so a no reads as arithmetic.

### 2. Fifth track

**No.**

- A fifth track with 96 fixed slots only shrinks each track from 24 to ~19 slots. The 4.6% rate does not move.
- The track count was fixed before the call opened. Your 32 reviewers signed up by track, so a fifth track has no committee.
- High oversubscription is a demand signal, not a mid-cycle cue to add a track. Read that demand next cycle through `event-market-fit`.
- If the board wants more capacity, that is a slot decision for next edition, driven by rooms, days and budget. It goes through `event-format-selection`.

## Plan

### 1. Committee: multi-tier cascade

- Your pool is too big for one room to read, and the program is multi-track.
- The two of you read ~189 proposals, not 2,100. That fixes last year's problem.

Roles:

- **32 volunteer reviewers** are graders, 8 per track if signups are even. They score only their own track.
- **4 track chairs**, one per track. They do not grade in tier 1.
  - Appoint them from outside the 32 if you can.
  - If they come from the 32, graders drop to 28 and the load rises.
- **2 co-chairs** do the final cut only. They score nothing in tier 1 and are never the anonymizer.
- **Cascade, with the cut stated before anyone sees a ranking:**
  1. Graders score every proposal in their track.
  2. The top **30%** per track advance to track chairs: 630 proposals in total.
  3. Chairs pass **~30%** of those on, with mandatory comments: ~189 in total (9% of the pool).
  4. Co-chairs pick 96 of those 189.

Slots per track:

- Rule: 96 × (track submissions / 2,100), rounded.
- In the balance pass (Section 6), co-chairs may shift at most **±2 slots** between tracks, and must record each shift. The ±2 is my self-set ceiling.

Reviewer load (my estimates, not sourced):

- Minimum **3 reviews per proposal**. This is the one sourced threshold: Pretalx stops resurfacing a submission once it holds 3+ reviews. That's 6,300 reviews, or ~197 per grader.
- At 10 minutes each that is ~33 hours per grader. At 225 reviews, with 28 graders, it is ~38 hours.
- Chairs read ~158 each, about 26 hours.
- Co-chairs read 189, about 16 hours each plus the discussion.
- No published curve links committee size to reviews per proposal. I'm interpolating from the 3-review threshold and your capacity.
- Have each grader time 10 proposals first, then replace my 10-minute guess with the measured figure.
- If 33 hours is too much for volunteers, recruit more graders. Do not cut below 3 reviews.

### 2. Rubric: multi-criteria stars

Your reviewers never meet, so use the star scale. It measures comparability, which an aggregated cut needs.

- Four criteria, 0.5-star steps, scored separately:
  - Content
  - Originality
  - Relevance
  - Speaker fit
- **A written comment on every rating is mandatory.** A score with no rationale cannot go to the next tier or be turned into decline feedback.
- Publish the criteria wording to reviewers before scoring opens. Do not change it afterwards, because that re-scores whatever was read first.
- Reviewers may differ in harshness. Calibrate on 10 shared proposals before opening. That is my own design, not a published step.

### 3. Anonymization (depends on the published call)

- If the call promised **named review**, anonymization is off the menu. Retrofitting it anonymizes nothing.
- If the call promised **blind review**, use **platform-level hiding** as the default.
  - It hides the author field, not what authors wrote in titles, abstracts or outlines. State that limit to the committee.
  - Name one person who owns the setting.
  - Identity re-enters **only at acceptance**, and only for the 96 accepted plus waitlist logistics. Nobody sees declined names.
- A dedicated anonymizer at 2,100 submissions rebuilds the bottleneck you are escaping. Use it only if:
  - the form also carries financial-assistance requests, or
  - last edition had a live fairness complaint.
  - If you do, split it across 4 people, one per track, who never score.
- No evidence shows blind review changes outcomes by demographic. It is a process commitment, not a proven equity outcome. Do not claim otherwise to the board.

### 4. Conflict of interest

Brief reviewers **before scoring opens**:

- Abstain on colleagues, your employer, and organizations you compete with. Review wearing the event's hat.
- Abstain if you suspect you have identified the speaker.
- Lesser conflicts (friend, same employer, topic bias): you may continue, but you must disclose it in the review text. The disclosure rule comes from PyCon DE's published guidelines.

These are honour-system recusals. No registry or audit exists anywhere, so the following escalation is my design:

- A reviewer who won't recuse: the track chair arbitrates.
- A chair conflict: the co-chairs arbitrate.
- A proposal that drops below 3 comparable reviews after recusals: reassign it to a grader from an adjacent track.

Organizer and sponsor-affiliated submissions:

- Disclose, abstain, cap, and allow opt-out for the co-chairs, chairs and organizing team. Decide the cap before the call closes.
- Co-chairs make the final cut, so their own talks have no neutral arbiter. Either they don't submit, or a pair of track chairs decides their proposals.
- Cap sponsor-affiliated speakers and put the editorial-independence wording in the sponsor contract via `event-sponsor-agreement`.
- Record every disclosure and abstention next to the proposal.

### 5. Rounds and timing

- Round 1: graders score all proposals, with comments.
- Round 2: chairs pass 30% of the 630, with comments.
- Round 3: co-chairs hold one decision meeting on the ~189.
- The program-announcement date (Q3) is the open variable. A hard date deletes rungs rather than compressing them, so send me the date and I'll back-schedule.

### 6. Program-fit pass

Run it on the ~189 shortlist only. Check:

- topic spread
- employer spread
- local versus out-of-town
- first-time speakers
- the lesson-transfer test for vendor talks

Lesson-transfer test: if the audience forgot the product name tomorrow, would they keep the lesson? A talk whose takeaway is the product fails.

Rules:

- **Write down every trade.** This is the least documented step in the field. Record what you swapped, which score you passed over and why.
- Decide before review whether each balance target is a goal or a gate. The published example is "at least 50% new speakers", and it was not a line in the rubric reviewers saw.
- Outreach cannot be fixed at review. A balance goal with no pre-call outreach can only be traded for at shortlist.

### 7. Waitlist and notifications

Waitlist:

- ~10–15 backups, ordered. That extrapolates from one documented size of about 5 for a single-track event.
- No conversion data exists, so tell waitlisted speakers the date they will know, never their odds.

Send in this order:

1. **Acceptances** (96), each with a confirmation deadline, plus **waitlist notices** at the same time.
2. **Declines** only after acceptances are confirmed.
3. Then announce the program.

Decline depth:

- **~80 finalists** (the 189 shortlist minus the 96 accepted and ~12 waitlisted):
  - Per-proposal feedback, edited for tone.
  - The comments already exist, so only editing time is left.
  - Strip reviewer names.
  - Say the feedback explains this decision, not a general assessment.
- **~1,900 others:** the default decline with criteria recap. The ratio sentence carries it.

**Draft: acceptance**

> Your proposal **"{title}"** has been accepted for ScaleFest, {date}.
>
> Please confirm by **{deadline}** that you can present. If we don't hear from you by then, we'll offer the slot to another speaker.
>
> What you get: {perks exactly as the call stated}. What we need next: {bio, headshot, slide deadline, travel details}.
>
> {If you have more than one accepted proposal: which would you rather give? We can only schedule one.}
>
> One rule for every speaker: no commercial demo or sales pitch. Name your product once if it matters to the story; the audience should leave with the lesson, not the pitch.

**Draft: waitlist**

> Your proposal **"{title}"** is on our waitlist for ScaleFest.
>
> It made our final shortlist and would be programmed if a slot opens. Slots open when a confirmed speaker withdraws, which sometimes happens and sometimes doesn't.
>
> You'll hear from us either way by **{date}**. Please don't hold travel on our behalf before then.

**Draft: decline (default)**

> Thank you for submitting **"{title}"** to ScaleFest. We're not able to include it this year.
>
> We received 2,100 proposals for 96 slots, so we declined many talks we'd have liked to program. Selection followed the criteria we published with the call: {one-line restatement}.
>
> {If blind: this pool was reviewed anonymously, so reviewers scored your proposal without seeing who submitted it.}
>
> We'd genuinely like to see you submit again for {next edition}.

For finalists, add the edited reviewer comments below the same text.

### 8. Metrics to record before the event

- **Acceptance ratio:** 96/2,100 = 4.6%. Trigger: if it swings hard next edition, check what changed in the call first.
- **Balance outcome:** first-time, employer spread and local share in the accepted set, against what the call promised.
- **Reviewer coverage:** proposals per reviewer, and how many lost reviewers to recusal. Trigger: more grader recruitment if the load breaks the calendar.
- **Declined-submitter return rate:** the only real test of whether the finalist-feedback cost was worth it.

## Assumptions to confirm

These change the plan. Ranked by impact:

1. Does the published call promise blind or named review? It decides Section 3.
2. How many hours can each volunteer actually give? It decides reviewer headcount and review depth.
3. What is the announcement date? It decides the schedule.
4. Are invited or sponsor talks in the same 96 slots? They need their own lane, outside the blind pool.
5. Are the 32 reviewers evenly spread across tracks? Uneven tracks change slot allocation.
6. Does the form carry financial-assistance requests? It decides whether you need a dedicated anonymizer.

**Next:** answer #1 and #2 and I'll finalize Sections 3 and 5.