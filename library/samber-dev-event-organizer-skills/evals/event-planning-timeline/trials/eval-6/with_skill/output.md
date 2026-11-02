# HalfLight: work-back plan, handover rebuild, and what went wrong last year

**What I did not have:** the sheet itself, last year's actual dates, or answers to the skill's interview (team size, paid vs. volunteer, sponsor-funded or not, which dates are announced). I couldn't ask one question at a time, so the assumptions are listed below. The diagnosis in part 3 is inferred from how the handover is built. Check it against last year's real dates before treating it as fact.

⚠️ **Date check.** Today is 14 Oct 2026, so 9 Oct 2026 has already passed. If you mean 9 Oct 2027, you are about 51 weeks out, which is plenty of time. I use offsets from doors-open (**S-n** = n weeks before 9 Oct), so the plan works for whichever year you mean. Tell me the year and I'll convert the offsets to calendar dates.

## 1. Assumptions (correct any that are wrong)

- Recurring edition, so a moved date or a visibly cut program costs trust. Once the date is announced, **the date holds and scope moves**.
- Venue, sponsors, CFP, tickets and marketing all exist as tracks. Meetup-scale shortcuts don't apply to 250 people.
- Plan rung is the **dependency-gated milestone plan**: monthly-grain milestones per track, cross-track gates, latest-safe commitment dates and pre-written checkpoints.
- I am **not** recommending a task-level critical path. A hand-me-down team with volunteer-level hours can't keep 180 tasks re-baselined, and it goes stale within a month.
- I am **not** recommending a weekly per-track variance review unless a standing team meeting already exists. If one does, bolt it on, because the marginal cost is near zero.
- If sponsors fund the event, the **Good/Better/Best scope ladder** applies. Sponsor revenue is not booked until agreements are signed.

## 2. The rebuilt plan

### 2a. Anchor and immovables

- Doors-open: **9 Oct (S-0)**.
- Immovable external deadlines still needed from you or last year's team:
  - venue contract and hold windows
  - sponsor fiscal-year budget cycles (these pull the sponsor track earlier than internal logic would)
  - any co-located event
  - the speaker-travel and visa lead times
- ℹ️ Offsets below are illustrative. Calibrate each to last year's **actual** dates. The sheet's 2025 stamps show planned dates, not real ones.

### 2b. Tracks, owners, work-back (offsets are illustrative)

Every task is written as a **finished state** and filed by **S-n**, never by calendar date. That is what lets the next organizer reuse it unchanged.

| Track | Owner | Work-back from S-0 (finished states) |
|---|---|---|
| **Venue & logistics** | _unassigned_ | Final walkthrough done (S-2) ← build-up/tear-down plan written (S-8) ← deposit paid **(latest-safe, see 2d)** ← contract signed ← venue locked ← requirements sheet current (S-52) |
| **Program** | _unassigned_ | Program announced (S-20) ← speakers confirmed, employer/travel cleared (S-24) ← selection done ← CFP closed ← CFP open ← CFP text reviewed (S-40) |
| **Sponsors & partners** | _unassigned_ | Fulfillment scheduled into marketing and logistics (S-12) ← agreements signed ← outreach started (pulled early by sponsor fiscal cycles) ← prospectus assembled ← tiers priced off the budget gap |
| **Marketing & comms** | _unassigned_ | Final two-week push live (S-2) ← program-driven push live (at program announced) ← date announced (gated, see 2c) ← channels ready |
| **Ticketing & registration** | _unassigned_ | Final headcount frozen (**latest-safe**) ← early-bird closed ← sales open ← pricing set ← payment infrastructure live |
| **Budget & finance** | _unassigned_ | Reconciliation scheduled ← vendor payment deadlines listed ← revenue checkpoints dated ← scope tiers costed ← draft budget approved |
| **Team & volunteers** | _unassigned_ | Volunteers briefed (S-1) ← day-of staffing recruited ← delegation as workload grows ← **every track owner named (first milestone, S-52)** |

Rule: exactly one accountable owner per track. An ownerless track slips without anyone noticing until a gate fails, so name owners first. Day-of detail belongs to `event-run-of-show` and `event-production`, not here.

### 2c. Gates (each names both milestones)

| # | Prerequisite | Blocks |
|---|---|---|
| G1 | Payment infrastructure live (Ticketing) | Date announced (Marketing) |
| G2 | Venue contract signed (Venue) | Date announced (Marketing) |
| G3 | Code of conduct published (Team) | First public listing (Marketing) |
| G4 | Draft budget approved (Finance) | Sponsor prospectus assembled (Sponsors) |
| G5 | Sponsor agreements signed (Sponsors) | Scope tier confirmed (Finance) |
| G6 | Speakers confirmed (Program) | Program announced (Program → Marketing) |
| G7 | Program announced (Program) | Program-driven sales push (Marketing) |
| G8 | Final headcount frozen (Ticketing) | Catering and swag orders placed (Venue/Finance) |
| G9 | Track owner named (Team) | That track's first milestone |

- G1, G2, G3 and G6 come from sourced organizing-guide mechanics.
- G4, G5, G7, G8 and G9 are standard sequencing logic, not published rules.
- Cross-track gates matter most. A venue slip that gates date announcement, which gates marketing, which gates sales, is not equal to a swag slip. A flat list can't show the difference.

### 2d. Latest-safe commitment dates (hold open until then)

Record both the earliest and the latest-safe date for each. Plan to the latest-safe one. Adding plates or seats late is cheap, and unwinding a prepayment is expensive.

| Commitment | Latest-safe rule | Owner |
|---|---|---|
| Venue deposit | Contract's real payment deadline, not the day it could be paid | Venue |
| Catering order | Caterer's real lead time; headcount frozen just before (G8) | Ticketing |
| Swag/badge print run | Printer lead time + artwork lock | Venue/Marketing |
| AV/contractor booking | Vendor's real cancellation terms | Venue |
| Speaker travel purchases | After speakers confirmed (G6) | Program |

Fill in the actual dates from last year's vendor terms. Padding belongs only on external lead times: printing, shipping, visas, venue paperwork. Don't add uniform slack elsewhere, because everyone plans to the padded date.

### 2e. Checkpoints (date, condition, pre-written action, owner)

Dates sit on moments already in the plan. **Thresholds are yours to set**, and I have not invented any. Demand thresholds belong to `event-market-fit`.

| When | Condition | Pre-written action | Owner |
|---|---|---|---|
| Sponsor budget-cycle close | Signed sponsor revenue below tier threshold | Downgrade one tier; cut the named Best/Better item | Finance |
| Date-announcement day | G1, G2 or G3 not met | Announcement does not happen; fix the prerequisite first | Lead organizer |
| Early-bird close | Sales below expectation | Escalate the named outreach push; hold catering at Good-tier quantities | Marketing |
| S-8 | Any gate into the final month unmet | Fire the replan: spend un-slid latest-safe slack, then tier downgrade, then scope cuts at the item that unblocks the most downstream work | Lead organizer |
| S-4 (shared gate) | Sponsor confirmation and speaker announcement status | Lock artwork, confirm speakers' travel | Sponsors + Program owners |

Each row has a date, a condition, an action and an owner. If any of the four is missing, it is a status meeting.

### 2f. Migrating the 180 rows

1. **Do not clean the sheet row by row.** Freeze it as a read-only archive.
2. **Collapse to the 7 tracks.** Merge duplicates ("book AV", "AV quote", "AV confirmed") into one finished-state task.
3. **Re-bucket by S-n.** Convert each row's 2025 date to weeks before that edition's doors-open, then drop the year.
4. **Treat ticked-but-unattributed rows as unverified.** Re-verify only the irreversible ones: contracts, deposits, payments, vendor bookings. Confirm with evidence (an email, an invoice, a signed PDF), and link the evidence in the row. For reversible, low-stakes ticks, accept them.
5. **Tracker columns:** ID · finished-state · track · S-n bucket · owner · gate-in · latest-safe date · evidence link · status. Use the simplest shared tracker the team will actually keep updated, even if that is the same Google Sheet.
6. **Add a short "how this track works" note per track,** plus a decision log. This is what survives to whoever takes over after you. Record owners, gates, latest-safe dates, checkpoint outcomes and buffers spent each edition.

## 3. What was going wrong last year

⚠️ **Inferred from the handover's structure, not from last year's data. Verify against actual dates.**

The final month feeling like a mess despite heroics is a typical symptom of **the unwatched middle**. The final sprint is where drift becomes visible, not where it happened. The structure you inherited makes that drift likely:

1. **One flat list, no tracks.** "Book AV" and "chase sponsors" look equally urgent. Nothing shows that the venue contract gates date announcement, which gates sales. The slip that blocked three other tracks looked the same as one that blocked nothing.
2. **No gates.** Dependencies lived in people's heads. The items that were not done were discovered only when a downstream task failed.
3. **Fixed 2025 dates.** The sheet can't be reused as-is. Every edition's plan has to be rewritten, so nobody checks it against actuals through the quiet months.
4. **Tasks written as instructions** ("sort out badges"). Whether they count as done is a judgment call each time. Hence ticks nobody can attribute: no owner, no evidence, no definition of done.
5. **No owners per track.** Nobody is on duty to notice a slip in the quiet stretch. Work piles up and gets fixed heroically at the end.
6. **No latest-safe dates.** Without them, irreversible commitments (deposits, orders) get made as early as money allows or as late as panic forces. Either way, reversibility is spent without a decision.
7. **No pre-written checkpoints.** With no dated condition and no pre-decided action, scope cuts and tier downgrades happen mid-crisis, under stress, with no agreed options. That is exactly the "heroic but messy" final month.

The heroics probably masked all of the above. A team that sprints well in the last month can look healthy while drift compounded unseen. The test is whether you can reconstruct, from the sheet, which milestones were late in the quiet stretch, and I expect you can't. That is the gap this plan closes.

## 4. What I need from you to finalize

1. Edition year (see the date check).
2. Which dates are already announced or contractually locked. Those are dead levers.
3. Team shape: who exists today, volunteer or paid, and whether any standing meeting exists.
4. Sponsor-funded or ticket-funded, and how much revenue is still unbooked. That decides whether the scope ladder gets built now.
5. Last year's actual milestone dates (even rough), plus the venue, caterer and printer terms for the latest-safe dates.

Once I have those, I'll fill in calendar dates, owners and thresholds, and validate the plan track by track with you. The skill says to confirm each section before finalizing, and this draft is the starting point for that.