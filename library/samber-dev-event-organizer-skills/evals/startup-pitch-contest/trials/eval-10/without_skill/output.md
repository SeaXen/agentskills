# Vellum Conf startup track: pitch block and meeting programme

## 0. Assumptions and open decisions

I don't have the numbers, so I sized everything for **N = 20 pitching companies** and gave formulas to rescale. Five items need your decision before the sponsor deck goes out.

| # | Open decision | My default |
|---|---|---|
| 1 | Is a Gold sponsor an investor, or a company that wants to meet founders? | Treated as non-investor buyers of founder access |
| 2 | How many Gold slots will you sell? | 3 (G = 3) |
| 3 | Are the "3 guaranteed" meetings guaranteed by investor attendance or by founder opt-in? | Slot guarantee with a written investor commitment (see §4) |
| 4 | Do the pitch block and the meetings happen on the same day? | Same day, pitches first |
| 5 | Is the tool paid by you or by the sponsors? | You pay. Budget is unknown. |

## 1. Capacity maths

Everything else follows from this.

- **Founder slots owed:** 3 × N = 60.
- **Sponsor slots owed:** 5 × G = 15, so 75 slots in total.
- **Slot length:** 25 min of meeting plus 5 min of changeover, so 30 min per slot.
- **Meeting window:** 14:00–17:30 gives 7 slots per table.
- **Tables needed:** ⌈75 / 7⌉ = 11. Add 1 spare, so 12 tables.
- **Per-founder load:** 3 investor slots plus at most 1 sponsor slot is 4 of the 7 slots. Founders keep 3 free slots for networking and rest.
- **Investor supply:** each investor commits to 6 slots (3 hours). The minimum is 60 / 6 = 10 investors.
- **Buffer:** recruit 15 investors, which gives 90 slots against 60 needed, a 1.5× buffer. Investors cancel, and the buffer is what makes "guaranteed" honest.

To rescale, use tables = ⌈(3N + 5G) / 7⌉ and investors = ⌈1.5 × 3N / 6⌉.

## 2. Day-of schedule

| Time | Block |
|---|---|
| 09:30 | Founders check in, tech check, running order confirmed |
| 10:00–11:20 | **Pitch block A**: 10 companies × 8 min (5 pitch, 2 Q&A, 1 changeover) |
| 11:20–11:40 | Break |
| 11:40–13:00 | **Pitch block B**: 10 companies × 8 min |
| 13:00–13:45 | Lunch. Post-pitch pick window opens (see §3). |
| 13:45 | Final schedule locked and pushed to all phones |
| 14:00–17:30 | **Meeting programme**: 7 rounds of 25 min plus 5 min changeover |
| 17:30 | Close. Investor feedback form and founder rating form open. |

Rules for pitch block and meetings:
- Run the pitch block first, so investors have seen every company before the 1:1s.
- Use a visible countdown clock and a hard cut at 5 minutes.
- A bell sounds at the start and end of every meeting round.
- Each table has a numbered card, and the tool shows the table number.
- Run the pitch order by lottery, not by seniority, so no company is permanently last.

## 3. Matching design: 2 algorithmic meetings plus 1 post-pitch pick

Each founder's 3 meetings come from two sources:

1. **Meetings 1 and 2 are matched before the event.**
   - Founders and investors fill a profile: stage, sector, ticket size, geography.
   - Each side ranks its top 8 on the other side.
   - Run a two-sided assignment solver, with a hard constraint of at least 2 meetings per founder and at most 6 per investor. Optimise the sum of mutual-rank scores.
   - Lock this 5 days before the event.
2. **Meeting 3 is an open pick after the pitches.**
   - Between 13:00 and 13:45 each founder requests one investor they now want to meet.
   - Investors can accept or decline. Declined founders get re-assigned to the investor with the most free slots.
   - Founders are guaranteed an accepted meeting. The investor is not guaranteed to be their first choice.

Sponsor meetings (G × 5):
- The sponsor lists the founder profiles it wants, using the same tags.
- The sponsor receives 5 founder introductions, scheduled only with founders who opt in.
- Each founder can take at most 1 sponsor meeting, so the 3 investor slots are never displaced.

## 4. What "guaranteed" means in writing

This is the main commercial risk. You are promising founders time you don't fully control, and you are selling the same founders' time to sponsors.

**For founders** (application terms):
- "Each accepted company receives three 25-minute investor meetings."
- Condition: the founder completes the profile and ranking by the deadline, and attends their pitch.
- Remedy if an investor cancels: standby slots (§5) first, then an extra slot the next morning, then a written follow-up intro.

**For investors** (invitation terms):
- Signed commitment to 6 slots, with 48 hours' notice to cancel.
- Investors who no-show on the day are not invited back.

**For Gold sponsors** (contract wording):
- Do not write "5 founder meetings" without a definition.
- Write: "Up to five 25-minute meetings, scheduled during the meeting programme, with founders who have accepted the request through the platform."
- Add a make-good: any unfilled slot converts to a warm email introduction within 10 working days.
- Add an exclusivity limit: no more than 1 sponsor meeting per founder.
- Say plainly that you can't force a founder to accept. That's why the make-good exists.

## 5. Failure handling

- **Investor cancels before the event:** the solver reruns, and the 1.5× buffer absorbs it.
- **Investor no-shows on the day:** two standby investors per round are kept in a reserve table. Their slots are pre-booked as "floating".
- **Founder no-shows:** their slots are released to waitlisted founders and to sponsors with unmet slots.
- **Tool outage:** printed schedule, one sheet per table and per founder, generated at 13:45.
- **Overrun:** the round timekeeper cuts at 25 minutes. There are no extensions, because the next slot is already booked.

## 6. Tool

I haven't checked current pricing or features, so verify these before committing.

Must-have requirements:
- Two-sided preference ranking and an assignment solver, or CSV export so you can run your own.
- Per-person limits on slots.
- A standby pool.
- Mobile schedule and printable export.
- Sponsor visibility, so sponsors see their own slots only.
- Investor data stays private from other investors.
- GDPR compliance, with a data processing agreement.

Shortlist the event-networking category (Brella, Grip, Swapcard and similar) and run a proof of concept with 5 founders and 3 investors. The fallback is a spreadsheet plus a script for the solver, which works at N = 20 and costs nothing.

## 7. Timeline

| When | Action |
|---|---|
| T-10 weeks | Decide §0 items. Choose the tool. |
| T-8 weeks | Open founder applications. Start investor recruitment (target 15 signed). |
| T-6 weeks | Sponsor contracts signed with the §4 wording |
| T-4 weeks | Founder selection done. Investor commitments signed. |
| T-3 weeks | Profiles and rankings open |
| T-5 days | Pre-event matching locked and sent |
| T-1 day | Tech check, printed fallback schedules, standby investors briefed |
| Event day | §2 |
| T+2 days | Feedback survey sent. Sponsor make-goods start. |
| T+2 weeks | Outcome report to sponsors and investors |

## 8. Success measures

- **Fulfilment:** 100% of accepted founders had 3 meetings. This is the promise, so track it first.
- **Sponsor fulfilment:** the share of the 5 × G slots filled with real meetings.
- **Investor attendance:** the share of committed slots that happened.
- **Quality:** founder rating of each meeting, and the share of investors who say they will follow up. Collect these on the day.
- **Follow-ups:** the number of second meetings 60 days later, collected by survey. Report it as self-reported.

## 9. Risks I'd flag now

- 🔴 **Over-selling founder time:** with a lot of Gold sponsors, 5 meetings each pushes founders past 4 meetings. Cap Gold slots at about 3, or add a second meeting day.
- 🟠 **Investor supply is the binding constraint.** If you can't sign 15 investors by T-4 weeks, reduce the guarantee to 2 meetings, or cut N.
- 🟠 **Low-quality investor matches:** a founder who gets 3 irrelevant investors will see the "guarantee" as empty. Filter investors on stage and sector fit before inviting them.
- 🟠 **Sponsor and investor overlap:** if a Gold sponsor is also an investor, don't count their meetings twice.
- ℹ️ **Scaling:** at N = 40 you need 21 tables, 30 investors and a second meeting day. The same format doesn't scale linearly.

## Next step

Answer the five items in §0, in particular items 1 to 3. They change the contract wording and the numbers. I can then produce the sponsor contract clause, the investor invitation and the founder terms.