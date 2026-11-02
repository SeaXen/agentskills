# Solder & Substrate Conf, edition two: money model approach

**Format and posture (assumed, confirm first):** ticketed, recurring, sponsor-led. I haven't seen last year's files, so every figure below is a labelled placeholder. Each will be filled from last year's actuals or from a new dated quote.

## 0. Starting point: reuse last year's record

- Last year's three costed budget versions become the Good/Better/Best ladder for edition two. Re-cost them with new dated quotes rather than building from scratch.
- Last year's per-line actuals are the baseline for planned-versus-actual variance and for re-sizing the contingency.
- Last year's cash-flow projection is the baseline for the new lowest cash point. Replace the projected inflows with the actual landing dates.
- For each per-head consumable line, record the headcount and the staff/volunteer/speaker mix it was priced against. That tells you what you are adjusting when you scale it.

## 1. Comps: don't adopt 5% as a rule

**The claim "that's what the big conferences allocate" has no source.**

- The only published anchor is PyCon US 2019, at about 4.4% of capacity receiving financial aid.
- That figure divides 2019 recipients by 2018 attendance, so it is an order of magnitude, not a same-year ratio.
- It is one large conference. It does not transfer to a per-city community event.
- DebConf subsidizes nearly everyone through a free-by-default model. That is a different structure, not a comparable.

**How to model it:**

1. Count comps only from agreements actually held:
   - signed sponsor ticket allotments;
   - confirmed speakers;
   - organizers;
   - volunteers.
2. Treat the scholarship program as a separate, deliberate line. It starts as the director's policy decision. It becomes a held commitment once the number is set.
3. Size it from three inputs:
   - last edition's scholarship demand (applications and awards);
   - what the program is for;
   - what funds it.
4. Use about 4–5% only as a sanity check on the order of magnitude. If the director still wants 5%, record it as a self-set policy choice, not as an industry norm.
5. A comp still costs per-head money. Catering, badges and swag follow the expected-show-up number, which includes comps. Hand `event-ticket-pricing` the **paid capacity after comps**, so the ticket target is spread over fewer paying seats.
6. If the program also covers travel or lodging aid, budget that as a separate cash line with its own payment date.

**Questions for the director:**

- What is the scholarship for?
- How many applicants and awards were there last year?
- Is there a dedicated sponsor or fund for it?
- Does it cover the ticket only, or travel too?

## 2. Reporting: replace the single number with per-line variance

"2% under overall" nets overruns against underruns. It cannot tell the board why the result happened, and it hides a bad cash position. Report four things instead:

1. **Variance per line, planned against actual.** `event-debrief` will ask for this. A total teaches nothing.
2. **Lowest projected cash point against lowest actual cash point.**
   - A big gap means the inflow dates were optimistic.
   - That is a different fix from the costs being wrong.
3. **Contingency drawn against contingency held.**
   - Drawing none for several editions suggests the floor is oversized.
   - Drawing all of it suggests the pad is undersized.
4. **Tier planned against tier actually run.** A ladder that never moves is not being used.

The board can still get one headline. It should be a short per-line table with the cash trough and the tier next to it.

Two further points:

- Last year's 2% under may hide offsetting misses. Re-read it against the per-line actuals before anyone repeats it.
- Pick two or three of these observables now. Write down what each would change before the first commitment.

## 3. Risk: two anchors at 70% of sponsorship

"Probably renewing" is not a revenue line. This is the Comdex shape: a few load-bearing sponsors, and a budget that cannot absorb their exit. A single budget cannot answer that. The ladder can.

**Model three sponsor cases against each tier:**

| Case | Sponsorship line |
|---|---|
| A. Both renew | last year's level, at actual payment terms |
| B. One renews | placeholder from the actuals |
| C. Neither renews | the remaining 30%, plus new sales |

- Express the loss as 0.7 × (sponsorship share of last year's total revenue). Take that share from the actuals.
- Count a sponsor only once it is **signed** and the deposit is **in the account**, per Q6.
- Real sponsorship terms skew toward 50–100% at signing. Ask for those terms in the renewal.
- Until signature, carry both anchors at a probability-weighted or zero value, labelled as placeholders. Do not carry them at last year's full amount.

**Decision checkpoints, dated against the cash-flow schedule:**

- **Anchor decision date:** the latest safe date to choose a tier.
- **Venue deposit and attrition dates:** after these, fixed lines can no longer be cut cheaply.
- Commit to Better or Best only after anchor money has landed. Default to Good until then.

**Cut order if the shortfall arrives:**

1. Discretionary extras: the evening event, swag upgrades, sponsored add-ons.
2. Per-head quantities, only before the guarantee lock date.
3. Fixed structural lines last. Attrition and food-and-beverage minimums are owed on the commitment, so the penalty can exceed the saving.

**Rules for this risk:**

- Don't plug the gap by raising ticket prices inside this model. If sponsorship misses, change the target and hand it back to `event-sponsor-pricing` and `event-ticket-pricing`.
- Diversifying the sponsor tiers belongs to `event-sponsor-pricing`. I own only the sponsorship-share target.
- Registration is the only revenue line that scales with the audience rather than sponsor budgets. If the anchors leave, it is the only second lever. Ask whether attendees use employer training budgets (Q10).

## 4. Contingency: three tools, not ranked

Each tool is stated separately. All three are self-set. None is an event-industry convention.

- **Floor:** a flat minimum reserve, set once. The only published example is one hackathon organizer's flat amount. Fill it from last year's smallest certain surprises in the actuals.
- **Pad on estimates:** a percentage added to expense estimates. The usual 20% is a convention borrowed from startup financial modelling, not measured on events. Label it that way every time you quote it.
- **Downgrade ladder:** last year's three tiers with dated checkpoints. This is the only tool that absorbs a whole-event shortfall like the anchor loss.

The pad and floor cover line-item misses. They are not a reserve against losing two sponsors.

## 5. Cash flow

Rebuild the schedule by scenario (A, B, C), with every outflow and inflow on its real date.

- Mark the lowest cash point per scenario.
- Deposits typically run 25–50% at signing. Sponsor money may land later than the deposits leave.
- Re-read the trough whenever a supplier changes its payment terms, not only when a price changes (Vancouver Folk, 2023).
- Default to the latest safe date for each commitment. Stage a commitment only if it carries a threshold owed regardless of turnout and someone can track it through the sale window (Q5, Q8).

## 6. Top-of-budget deductions and the tax question

- Deduct first: fiscal-host share, processing fees on both rails, any parent contribution. Fill the percentages from your actual host's terms.
- **Open tax question, written as a question:** who confirms the tax treatment of ticket revenue and of sponsorship revenue in our jurisdiction, and by what date? Owner and date go in the budget. Record the answer as a line when it arrives.

## 7. Open questions, in priority order

1. Does last year's 2% under hide offsetting line variances?
2. What are the anchors' actual payment terms and renewal dates?
3. Which cost lines have a dated quote, and which are still "no quote yet"?
4. What does the scholarship program aim to do, and what funds it?
5. By what date must sponsor and ticket money be in the account?
6. Who holds the money, and what comes off the top?
7. Who tracks the sale window, and who is the second approver on spend?
8. Do attendees typically use employer training budgets?
9. Does any venue or vendor offer a real early-payment discount?

## 8. Gate before the first go/no-go date

- Every cost line carries a dated quote or an explicit "no quote yet".
- The cash-flow schedule has a computed lowest point for each sponsor case.

If either fails, the budget isn't built yet, whatever its total says.