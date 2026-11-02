# KernelKraft Conf (Porto, June 2027): budget model v0.1

**Format: ticketed two-day conference, sponsor-led.** Sponsors carry the bulk and tickets cover the per-attendee cost. Every number is labelled *quote*, *self-set* or *no quote yet*.

## 0. Read this first

I did not fill in market prices, so the budget is a complete model rather than a complete set of figures. A board reads an invented catering or AV number as a quote, and it then becomes the number. I carry those lines as "no quote yet" with a range. You enter the range, and the arithmetic below recomputes.

Four other things need your attention:

1. **The venue quote has no amount.** You gave me the date but not the figure. 14 October is two days from today (12 Oct 2026), so please confirm the year. If the quote is from 2025, it has probably expired.
2. **Hold the date announcement.** The bank account isn't live, and an event shouldn't go public with a date before it can process money (§8).
3. **The ticket price is not set here.** Ticket pricing is a separate decision. I give the *ticket revenue target* and the arithmetic in §5, and `event-ticket-pricing` turns that into a price ladder.
4. **500 is interest, not registrations.** The 78% show-up rate applies to registrants. Treat 390 as a ceiling for planning, not a forecast.

## 1. Head count

- 500 interested × 78% = **390 expected show-ups** (self-set, from your network's rate).
- Caveats: the 78% comes from other events, probably not at your price point, and the conversion from interest to paid ticket is unknown. `event-no-show-management` owns the final number.
- Catering and badges are budgeted on show-ups, never on 500. Speakers, sponsor staff, organizers and volunteers are added on top.
- **Comps: 0 confirmed.** Count them only from agreements actually held (speakers, sponsor allotments, volunteers).

## 2. Cost lines

Taxonomy used: conference (not hackathon).

| Line | Side | Driver | Status |
|---|---|---|---|
| Venue: main hall + 2 breakouts | Fixed | the room set | **Quote, 14 Oct. Amount missing.** Also confirm deposit schedule, attrition and F&B minimum, mandated caterer, cancellation dates. |
| Catering (breakfast, breaks, lunches, 2 days) | Per-head | show-ups + staff | No quote yet. Range: ___ to ___ |
| AV, internet, media (recording, captions) | Fixed (set-up), partly per-room | rooms, tier | No quote yet. Range: ___ to ___ |
| Badges and lanyards | Per-head | show-ups + staff, plus spares | No quote yet. Range: ___ to ___ |
| Swag | Per-head | show-ups | No quote yet. Range: ___ to ___ |
| Signage | Fixed | rooms | No quote yet. Range: ___ to ___ |
| Speaker expenses | Per-speaker | speaker count | No quote yet. Range: ___ to ___ |
| Evening event | Fixed + per-head | show-ups | No quote yet (Best tier only). Range: ___ to ___ |
| Admin: insurance, accounting, tax handling | Fixed | none | No quote yet. Range: ___ to ___ |

Fill the ranges with your own low and high bounds, marked "self-set". The better route is three quotes per line on one identical requirements sheet, which `event-vendor-sourcing` and `event-venue-sourcing` own.

**Off the top (on all money in):**
- Fiscal sponsor: **8%** of everything, tickets and sponsorship.
- Card processing: **p**, no quote yet. Ask the fiscal sponsor or processor which rail and what rate, and whether the 8% applies before or after processing fees.
- Every €1 raised therefore nets about **(0.92 − p)**. The gross-up is at least 1/0.92 = **1.087×**, before processing fees.

## 3. Contingency (self-set, three tools stacked)

No event-industry standard exists for any of these three, and I won't present one as such.

1. **Floor:** one flat cash reserve, decided once. No sourced conference figure exists. The only published reference is one hackathon guide's flat 1,000–3,000 USD, which is a US hackathon recommendation, not a convention.
2. **Pad:** +20% on the *placeholder* lines only, not the quoted venue. This is borrowed from startup financial modelling and was never measured on events.
3. **Downgrade ladder:** the tiers in §4, with checkpoints driven by cash received (§7).

Contingency = floor + 20% × (sum of placeholder lines). It becomes a number once §2 is filled.

## 4. Scope tiers

Let F be fixed cost, c the per-head cost and N the show-ups.

| Tier | Contents | Break-even driver |
|---|---|---|
| **Good** (runs at all) | Venue as quoted, basic catering, AV without recording, minimal badges, no swag, no evening event, no speaker dinner | F_good + c_good·N |
| **Better** | Good + recording, fuller catering, basic swag, speaker dinner | F_better + c_better·N |
| **Best** | Better + captions or livestream, evening event, swag upgrade | F_best + c_best·N |

Venue is the fixed structural line, so it stays constant across tiers. Ask the venue for a smaller-room option in the quote request if you want a Good tier that shrinks it.

## 5. Revenue targets and the ticket arithmetic

Let E be the tier's expenses including pad, and N_paid the show-ups minus comps. Then:

- Gross to raise: **G = E / (0.92 − p)**
- Sponsorship target: **S = s × G**. Sponsor pricing splits this into tiers, and you haven't defined "most", so s is open.
- Ticket target: **T = (1 − s) × G**
- Ticket revenue needed per paying head: **T / N_paid**

Let **k = G / N_paid**, the grossed-up cost of one paying attendee. Ticket revenue needed per head is then (1 − s) × k:

| Sponsor share s | 60% | 70% | 80% |
|---|---|---|---|
| Ticket revenue needed per paying head | 0.40·k | 0.30·k | 0.20·k |

- Each 10 points of sponsor shortfall adds **0.10·k** to the ticket target.
- Sponsor commitments today: **none identified.** The ticket line stays open until sponsorship is booked, and sponsorship is the revenue line that moves the ticket price most.
- Hand `event-ticket-pricing` T and N_paid. It returns the price ladder and the sold total, and I don't set the price here.
- Sensitivity: rerun at N = 390, 300 and 250. Fixed costs don't shrink, so the break-even per head rises as N falls.

## 6. Commitment posture

- **Default is latest safe date:** commit each line at its last safe date, because adding capacity late is cheap and unwinding is not.
- **Staged commitment applies only if** the venue contract carries an attrition or F&B minimum owed regardless of turnout *and* someone owns a standing tracking job through the sale window. Both conditions are required. Ask for the contract terms.
- Ask every counterparty whether it gives a real early-payment discount. If none does, don't pay early.

## 7. Cash-flow schedule

| Date | Event | Cash |
|---|---|---|
| 14 Oct 2026 (confirm year) | Venue quote | none |
| Next few weeks | Bank account live | none until the **realistic time-to-spend** is known |
| Before signing | First go/no-go | sponsor *cash received* checked against deposit |
| Venue signing (date TBD) | Deposit, typically 25–50% (generic, not measured) | **outflow of 25–50% of V** |
| After account live | Sponsor money, often 50–100% at signing (published terms vary) | inflow |
| After announcement | Ticket money across the sale window | inflow, latest and riskiest |
| 14–30 days before the event | Venue balance (generic) | outflow |
| Venue-set lock date | Catering guarantee | outflow, fixed from here |

**Lowest cash point: the day the venue deposit leaves**, unless sponsor cash of at least the deposit has already landed. Trough ≈ −(deposit + other early non-refundables) + sponsor cash received by then. A profitable bottom line doesn't help if that day arrives first.

**Ladder checkpoints** (dates fill in from the venue contract):
1. Before signing: sponsor *cash* covers the deposit, or the organizers choose to carry that risk.
2. End of early-bird: ticket revenue against target decides Better versus Good.
3. Catering lock date: the last point where per-head cuts are free.

**Cut order**, as pre-priced in the tiers:
1. Discretionary extras (evening event, swag upgrade, sponsored add-ons).
2. Per-head quantities, only before the guarantee locks.
3. Fixed structural lines last. Attrition and F&B minimums are owed on the commitment, so cutting the venue late can cost more than keeping it.

## 8. The announcement and the bank account

Settle three things before the date goes public:
- Who holds the money.
- How fast it can be spent once it arrives.
- Whether a sponsor can pay and a ticket can be bought today.

**Recommendation:** announce only once the account is live and a test invoice and ticket sale have gone through. If next week is fixed, announce "Porto, June 2027" with a waitlist, with no day and no sales. Also ask whether the fiscal sponsor can invoice sponsors through its own processor in the meantime.

If an organizer must pay the deposit personally and be reimbursed later, a second organizer who isn't the spender must approve it.

## 9. Open tax question

I have not stated any rate or rule. The question is for the fiscal sponsor, a Portuguese accountant or counsel:

> Who confirms the tax treatment of ticket revenue and of sponsorship revenue for an event held in Portugal and run through a fiscal sponsor (possibly based elsewhere), and by when? Does the sponsor need a Portuguese tax registration, and is the 8% fee tax-inclusive?

Owner and date are to be assigned. Carry "tax handling" as a named line in §2, and itemize sponsorship separately from any booth or space element.

## 10. Inputs I need to finish

1. The venue quote amount, its year, and its terms.
2. The sponsorship share you consider "most" (60%, 70% or 80%).
3. Processing fee p, and whether the 8% applies before or after it.
4. Your own range per placeholder line, or three quotes.
5. Comps held, and the speaker count.
6. Whether the venue has an F&B minimum, an attrition clause, or a mandated caterer.
7. Who tracks sales through the window.

**Binary gate status: not yet passed.** The venue amount is missing and the placeholder lines have no ranges. The lowest cash point is expressed symbolically, not as a number.