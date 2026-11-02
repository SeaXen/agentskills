**Date check:** my clock says today is 14 Oct 2026, so "9 October" is either already past or means 2027. I've written everything relative to event date (T-minus), so it works either way. If this edition has already happened, hold the retro now while memories are fresh. It's the best input the rebuild can get.

I haven't seen the sheet. Section 1 is inferred from your description and is a hypothesis list. Check it against the team (test at the end of section 1).

## 1. What was going wrong

The final month felt like a mess because the work was invisible until it was urgent. Heroics were the symptom. Your sheet shows the causes:

1. **Tasks are verbs, not outcomes.** "Sort out badges" has no finish line. Is it design, print, stuffing, or on-site reprint? Nobody can say it's late, because nobody can say what done looks like.
2. **No owner, no evidence on ticks.** Half the ticks are unattributed, so a tick means "someone touched it". You can't tell finished from abandoned from fixed by someone else. In the last month you couldn't trust the sheet, so people re-checked everything by hand or by chat.
3. **Absolute dates.** Everything is stamped with a 2025 date, so the plan is a record of one year and not a template. Each year the team rebuilds the timeline from memory.
4. **The critical path is hidden.** "Book AV" depends on venue, floor plan, session count and schedule. "Chase sponsors" decides the budget, and the budget decides catering, AV and badges. A flat list shows none of this, so you discover dependencies when they bite.
5. **Lead times weren't encoded.** Venue, AV, catering minimums, printing and speaker travel have long lead times. A flat list treats them like "send an email", so they start late and become emergencies.
6. **No freeze points.** Without a date after which the schedule, speaker list and floor plan stop changing, every late change cascades into AV, signage, badges, the website and the run-of-show. Late changes are the main source of last-month chaos.
7. **Decisions live in heads and chat.** Why this venue, what the sponsor was promised, which vendor failed. They surface as arguments in the last month.
8. **Single points of failure.** Probably one or two people hold the vendor relationships and sponsor deals. That makes them the bottleneck, and it makes handover fragile.
9. **Heroics get rewarded.** If the last month is celebrated, nobody gets credit for a quiet, boring October, so early risk reviews never get prioritised.

**Test (45-minute retro, before you build anything):** Ask 3-4 past organisers separately: "Which 10 tasks caused the most stress, and when did you first know they were at risk?" If most answers are "in the final 4-6 weeks" for tasks that could have been visible at T-16 weeks, items 4, 5 and 6 are confirmed. If the answer is "when X left or stopped replying", item 8 is the real cause.

## 2. The rebuild

### Principle
Don't migrate 180 rows. Treat the sheet as raw material for a template. A successor needs a **calendar of outcomes, a decision log, and a runbook**. They don't need your task list.

### Step A: Triage the 180 rows (about 2 hours)
Run them through four buckets:

| Bucket | Rule | Action |
|---|---|---|
| Duplicate / vague | Same outcome as another row, or no recognisable outcome | Merge or delete |
| Recurring | Happens every edition | Becomes a template task |
| One-off | Specific to last year | Archive in a tab, don't carry over |
| Unknown tick | Ticked, no owner, no evidence | Treat as **not done** if it is on the critical path (venue, contracts, insurance, AV, catering, speaker travel, sponsor invoices). Verify by finding the contract, email or invoice. Elsewhere, treat as "probably done". |

Expect 180 rows to collapse to roughly 60-80 recurring tasks.

### Step B: Rewrite each recurring task as an outcome

Columns, one row per task:

- **ID** and **workstream**
- **Outcome**, as a checkable statement: "250 badges printed, spell-checked against registration export, boxed by alphabetical block"
- **Owner**, one named person
- **Due**, as T-minus weeks, not a date. Compute real dates from the event date in one cell.
- **Lead time**, how long it takes, so the start date is explicit
- **Depends on**, listing task IDs
- **Done evidence**, a link to the contract, invoice, email or doc
- **Status**: Not started, In progress, Blocked, Done. "Done" requires the evidence link.
- **Risk to event if missed**: High, Medium or Low

Rule: a task isn't done without evidence. That one rule fixes problem 2.

### Step C: Workstreams (suggested: 8)
1. Venue and logistics (venue, floor plan, accessibility, insurance, permits)
2. Programme (CFP, selection, speakers, schedule, speaker travel, rehearsal)
3. Sponsors (prospectus, outreach, contracts, invoices, deliverables owed)
4. Finance (budget, ticket revenue, payments, reconciliation)
5. Attendees (ticketing, communications, badges, accessibility, code of conduct)
6. Production (AV, streaming, recording, signage, catering)
7. Marketing and community (website, email, social, partners)
8. Volunteers and on-site (roles, briefing, run-of-show, safety)

Give each one an owner and a named deputy. The deputy is what makes the plan survive someone leaving.

### Step D: T-minus milestones with freezes
Adjust to your real lead times:

| When | Milestone |
|---|---|
| T-40 wks | Retro done, date and venue contract signed, budget v1, sponsor prospectus ready |
| T-32 | CFP open, sponsor outreach started, ticketing live |
| T-24 | **Budget checkpoint:** sponsor revenue vs target. Go/no-go on scale and spend. |
| T-20 | CFP closed, programme committee decides |
| T-16 | **Programme freeze v1:** speakers confirmed. AV, catering and streaming vendors briefed. |
| T-12 | Speaker travel booked, sponsor contracts signed, floor plan draft |
| T-8 | **Schedule freeze.** After this, changes need the lead's sign-off and a written impact note. |
| T-6 | Badge data export, signage and print orders placed, volunteer roles assigned |
| T-4 | **Hard freeze:** floor plan, catering numbers, run-of-show v1. Only emergencies change. |
| T-2 | Final headcount to caterer, speaker briefing, tech rehearsal, runbook printed |
| T-1 wk | On-site walkthrough, badge check, volunteer briefing |
| Event | Run-of-show with named owners, escalation phone tree |
| T+1 wk | Thank-yous, sponsor deliverables report, invoices settled |
| T+3 wks | Retro and template update |

The freezes at T-8 and T-4 are the main defence against a chaotic final month.

### Step E: Weekly rhythm (30 minutes)
Review only three things: tasks due in the next two weeks, blocked tasks, and High-risk tasks without an owner. If a High-risk item is within its lead time and not started, it gets raised that week.

### Step F: The documents that make it survive

1. **Decision log**: date, decision, options considered, why, who decided. One line each.
2. **Vendor and contact register**: name, role, contract link, what went well or badly, renewal date.
3. **Sponsor commitments register**: what each sponsor was promised and whether it was delivered.
4. **Runbook**: step-by-step for the event day, plus "what to do if" for the top 10 failures (speaker no-show, AV failure, venue issue, medical, Wi-Fi).
5. **Handover README**: one page covering where everything lives, who has the keys (domains, ticketing, bank, accounts), and what the first 30 days of the next cycle look like.
6. **Access register**: who holds admin rights to ticketing, website, bank and email. Make sure two people hold each one.

Keep all of it in one place, not scattered across chat threads.

### Step G: Annual rollover
At T+3 weeks, duplicate the template, change the event date, and fold the retro's changes back in. The template is a living document, and the task list in a given year is just an instance of it.

## 3. Your first 7 days

1. **Day 1 (1 hour):** Find out the actual status of High-risk items from the ticked rows. Look for contracts, insurance, and anything with a deposit.
2. **Day 1-2:** Run the 45-minute retro interviews in section 1.
3. **Day 2-3 (2 hours):** Triage the 180 rows into the four buckets.
4. **Day 3-5:** Build the template sheet and rewrite the recurring tasks as outcomes with owners.
5. **Day 5:** Fill in the T-minus calendar and name workstream owners and deputies.
6. **Day 6-7:** Write the access register and the one-page handover README, since they're the cheapest things to do and the most painful to lack.

## 4. Questions that would sharpen this
- Is the event already past? If so, I'd move straight to the retro and rollover.
- Who owned sponsors and venue last year, and are they still around? That shapes how much to rely on memory vs documents.
- Is it run by volunteers or paid staff? Volunteer teams need shorter weekly rhythm and lighter templates.