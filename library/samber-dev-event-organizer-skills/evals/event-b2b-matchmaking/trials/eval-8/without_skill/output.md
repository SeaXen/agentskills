# Feedback on the Meridian Exchange report and dashboard

The arithmetic holds, but the report says less than it appears to. The "available on request" line and the 61% benchmark are the two things I'd fix before this goes out. The dashboard needs contract definitions settled first.

## 1. The numbers

- 172 held + 11 saved + 27 no-show = 210 ✅
- 183/210 = 87.1% ✅
- 27/210 = 12.9% ✅

The two headline figures are exact complements (87.1% + 12.9% = 100%). Together they count as one claim, not two.

## 2. Problems in the draft

**a) "Meeting fulfillment 87%" mixes two units.**
- The 11 standby saves are not the 210 accepted pairings. A different person took the slot.
- Pairing fulfillment is 172/210 = **81.9%**.
- Slot utilization is 183/210 = **87.1%**.
- Both are good numbers. Call the 87% "slot fill rate" and give pairing fulfillment next to it. Otherwise a sponsor who works out 172/210 will think you inflated the figure.

**b) The 61% benchmark isn't comparable.**
- Trade-show figures usually measure booth visits or walk-up conversations. Yours measures pre-booked, mutually accepted slots, which should show up far more often.
- No source or definition is given. Readers will challenge it, and "beating" an easy baseline weakens the real result.
- Replace it with your own history: editions 1 and 2, same definition. You're on edition three, so a trend is the strongest evidence you have.
- If you keep an external benchmark, cite it and state its definition.

**c) "Empty-slot rate 12.9%" hides the cause.**
- You have 27 no-shows but not who didn't show. Split them into buyer-side and supplier-side.
- This matters for the quotas. A supplier whose buyers didn't show was not at fault. A supplier who skipped slots was.
- Add the standby save rate: 11 of 38 failed slots were recovered (about 29%). That is evidence the standby line works.

**d) "Per-supplier details available on request" is the main flaw.**
- Five suppliers have contracted quotas. Their numbers are the deliverable that matters to them.
- An aggregate can hide a supplier at 60% behind another at 105%.
- Put a per-supplier table in the report, or an annex if the audience is wider.

Suggested table:

| Supplier | Quota | Held | Saved via standby | No-show (buyer side) | No-show (supplier side) | Quota met? |
|---|---|---|---|---|---|---|

Your five rows are missing from what you sent me, so the table is blank.

## 3. The per-sponsor dashboard with payment milestones

The idea is sound, but settle these before building it:

1. **Define "quota completion" from the contract text.** Decide whether a standby-saved meeting counts. Decide whether a buyer no-show counts as delivered. Decide whether a meeting must reach a minimum duration. The dashboard encodes the answers, so they must match what was signed.
2. **Check which way the balance runs.** If a supplier paid for N meetings and got fewer, you may owe a credit or refund. Finance "chasing balances" would then be wrong. Confirm whether milestones are sponsor payments or organizer obligations.
3. **Add a dispute window and an audit trail.** Attendance needs a source of record, such as check-in scans or host confirmation, and each no-show needs a named side. Money tied to a count that can't be traced will be contested.
4. **Keep the report and the dashboard on one definition.** The report must not say "87% fulfilled" while the dashboard shows one sponsor short and finance chases them. One metrics spec should feed both.
5. **Restrict visibility.** Each sponsor sees only their own row. Finance and the internal view see everything. Don't share live shortfall figures before the data is reconciled.
6. **Confirm who owns the exceptions.** Someone has to rule on edge cases (late arrival, partial attendance, substitute buyer) and note the ruling.

## 4. Suggested rewrite of the report line

> Meridian Exchange (3rd edition): 210 pairings accepted and slotted; 172 held as planned (81.9%). A further 11 slots were recovered from the standby line, giving a slot fill rate of 87.1% (183/210). 27 slots (12.9%) went unfilled after a no-show: [X] buyer-side, [Y] supplier-side. Slot fill rate was [Z] in edition 2 and [W] in edition 1. Per-supplier quota delivery is in Table 1.

Fill in X, Y, Z and W from your records. If you can't, drop the claims you can't support.

## 5. Next steps (about 30–45 minutes if the data exists)

1. Pull the buyer-side vs supplier-side split for the 27 no-shows.
2. Pull the same metrics for editions 1 and 2.
3. Build the five-row supplier table.
4. Read each of the five contracts for the definition of "delivered".
5. Draft the dashboard spec once step 4 is done.

Send me the per-supplier counts and I'll draft the table and the narrative.