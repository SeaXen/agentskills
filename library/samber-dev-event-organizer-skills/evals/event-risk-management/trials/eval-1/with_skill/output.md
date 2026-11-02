# KestrelConf risk pack for the COO and the board update

**This is not legal or insurance advice.** It is a risk register and a decision framework. It tells you which risks matter, when someone must decide, and which coverage categories to ask a broker about.
- Contract wording (force majeure, cancellation, refunds) goes to counsel. I draft no clause language.
- Whether any policy covers a given loss goes to a licensed broker. Premium figures below are illustrative ranges, not quotes.

I normally interview one question at a time. Since you need the deliverable in one pass, I used your facts and wrote down my assumptions. The open questions are in section 7, with the most urgent first.

## 1. Board summary

**Assumed pole: company-run.** This is a vendor marketing budget with six-figure commitments. The go/no-go owner should therefore sit outside the organizing team, and I assume that is the COO.

| Fact | Value |
|---|---|
| Event date | Fri 14 May 2027, 212 days from today |
| Paid and likely non-recoverable today | 24k venue deposit + 11k flights = **35k (16.7% of 210k)** |
| Next cash cliff | 19k catering payment (50% of 38k) due **Mon 15 Mar 2027** (T-60). That takes committed spend to **54k (25.7%)**. |
| Ceiling if every contract runs to full liability | 80k + 38k + 11k = **129k (61% of budget)** |

- **Ceiling caveat:** it is a worst case, not a forecast. It assumes the flights are non-refundable and that the venue and caterer cancellation fees step up to 100%. Neither schedule is in front of me.
- **Coverage trigger:** this skill's working default is to buy cancellation cover once non-recoverable spend passes about 25% of budget (52.5k). That is a skill default, not an industry standard. You cross it on 15 Mar, and possibly earlier through venue fee steps. **Start the broker conversation now.**
- **Top risks (3 orange, 0 red):**
  - Demand shortfall on a first edition.
  - Key-organizer loss.
  - Organizer discretion, meaning the company itself pulls back.
- **Biggest single insurance decision:** whether a cancellation policy carries the communicable-disease buy-back. Insurers excluded that peril market-wide from January 2020. MWC and SXSW 2020 both held real cover and were still uninsured for what happened. Record the answer either way.

**Asks of the board:**
1. Confirm the COO as go/no-go owner and name any veto holder (CEO or CFO).
2. Approve a broker conversation and a premium budget. For scale, the reference range of 1–3% of the insured budget is about 2.1k–6.3k EUR. This is illustrative, not a quote.
3. Ratify the go/no-go thresholds in section 5 before 1 Feb 2027.

## 2. Assumptions to confirm

- It is a single-day, indoor event with no outdoor element.
- No sponsor money funds the 210k.
- Attendees register through a third-party platform.
- This is an annual asset, so the register is kept and re-scored for edition 2.
- No in-house lawyer, no existing event policy.
- Alcohol is unknown. A reception raises the safety and liability rows (amplifier).

## 3. Scored register

Scale is 5×5, likelihood × impact. Impact is measured against non-recoverable committed spend and reputation, not schedule slip. Bands are 🟢 1–4, 🟡 5–9, 🟠 10–15 and 🔴 16–25. Scores are as of today, at T-212 days. Owners are roles, so please put names on them. Orange rows are reviewed monthly and at every decision date. All other rows are reviewed at each decision date (Feb 1, Mar 1, Apr 5).

| # | Risk | L | I | Score | Owner | Treatment |
|---|---|---|---|---|---|---|
| 1 | Demand shortfall. First edition with no baseline. If 14 May is the Friday before Whit Monday (17 May) in your country, it is a long weekend. | 3 | 4 | **12 🟠** | Marketing lead | Prevention: pace tracking from week 1, customer-success outreach. Contingency below. |
| 13 | Key-organizer loss. A 90-person company likely has 1–3 people holding everything, a single-source dependency. | 3 | 4 | **12 🟠** | COO | Prevention: named deputy, shared vendor accounts, written runbook. |
| 15 | Organizer discretion. Budget cut, funding or strategy change pulls the plug with no external trigger. | 2 | 5 | **10 🟠** | COO | Board-level decision rule (section 5). Cancellation memo (section 6). |
| 4 | Marquee speaker loss, with 11k of flights paid | 3 | 3 | 9 🟡 | Program lead | Name a backup speaker. Move to changeable fares where possible. |
| 11 | Production failure. Workshops put 450 laptops on one venue IP, so your own cloud or WAF may rate-limit it. | 3 | 3 | 9 🟡 | Production lead | Pre-allow-list the venue IP. Rehearse on the venue network. Offline fallback for each workshop. |
| 7 | Communicable disease or public-health restriction. Impact rises as spend rises. | 2 | 4 | 8 🟡 | COO | Transfer: buy-back decision (section 4). Counsel reads the force majeure clause. |
| 9 | Safety, security or medical incident, 450 people | 2 | 4 | 8 🟡 | Ops lead | Emergency plan (Appendix). Adjust score if alcohol is served. |
| 2 | Sponsor withdrawal. Provisional: delete only if no sponsor money exists. | 2 | 3 | 6 🟡 | Sponsorship lead | Confirm the answer (Q-open). |
| 5b | Travel disruption (strikes, airline, rail) | 3 | 2 | 6 🟡 | Logistics lead | Speaker arrival buffer of one day. Changeable fares. |
| 8 | Payment capability, if tickets are paid. A first edition is standing up ticketing, refunds and VAT. | 2 | 3 | 6 🟡 | Finance | Test a refund end to end before launch. |
| 10 | Code-of-conduct or PR incident | 2 | 3 | 6 🟡 | Comms lead | Publish a code of conduct. Name a response owner. |
| 12 | Registration-platform breach (attendee list is customer data) | 2 | 3 | 6 🟡 | Security lead | Confirm who carries the risk contractually. |
| 16 | Catering minimum guarantee. You pay for 450 if 300 come. *(Added row.)* | 3 | 2 | 6 🟡 | Event lead | Read the headcount guarantee and its date. Plan the downsize before it. |
| 17 | Product incident on the day pulls key staff away. *(Added row, observability-specific.)* | 3 | 2 | 6 🟡 | Eng lead | On-call rota that excludes presenters and booth staff. |
| 3 | Venue loss or forced change | 1 | 5 | 5 🟡 | Logistics lead | Single-source amplifier. Have counsel check the venue-default refund wording. |
| 6 | Adverse weather, in progress (indoor) | 1 | 2 | 2 🟢 | Ops lead | Accept. |
| 5 | Adverse weather, pre-event | 2 | 2 | 4 🟢 | Logistics lead | Accept. Region and season are an open question (Q10). |
| 14 | Exhibitor or sponsor defection to owned channels. No exhibitor ecosystem exists yet. | 1 | 2 | 2 🟢 | Marketing lead | Accept and re-open if exhibitors are added. |

**Contingency entries for orange rows.** If the trigger fires, do the following:
- **Row 1, pace below the threshold at a decision date:**
  1. Run a targeted customer push for two weeks.
  2. Cut the catering headcount **before** the guarantee date.
  3. Collapse workshops to fit a smaller room.
  4. Take the go/reduce/no-go decision at the next date.
- **Row 13, organizer unavailable:** the deputy takes over from the runbook within 24 hours. The COO reassigns any vendor account held by one person.
- **Row 15, leadership signals a budget cut:** convene the polled call within five working days. Quantify the exposure on that day's fee step using the section 6 memo.

## 4. Coverage decisions (with reasons)

This ladder is ranked for a company-run event with a hard cash cliff on 15 Mar and a likely annual mandate. A hard date promotes the rungs that bind fast. An annual mandate promotes the durable ones.

| Rung | Decision | Reason to record |
|---|---|---|
| Venue-required liability | **Do.** Check whether the venue contract demands proof and additional-insured status, and whether Kestrel's existing corporate liability policy already covers the event. | It is the default rung. Dropping it can cancel the venue. |
| Event cancellation + communicable-disease buy-back | **Promote. Ask the broker now.** Timeline: quotes by **Fri 30 Oct 2026**, decision recorded by **Fri 13 Nov 2026**. | Spend is 16.7% and passes 25% at the 15 Mar payment. Large events usually bind 12–18 months out, so your 7-month window is compressed and some terms may already be unavailable. Disclosure duty: tell the broker everything you already know (including sales pace). Non-disclosure voids the policy. |
| Non-appearance | **Conditional.** Ask only if one named keynote carries the ticket sales. Otherwise record "declined, program is balanced". It must bind at least 14 days before the event. | Cover is only worth buying where a single person carries the value. |
| Parametric weather | **Decline and delete.** | Indoor event. Reconsider only if an outdoor element appears. |
| Participant accident | **Decline.** | Workshops are laptop-based, with no hands-on hardware and no physical activity. |
| Cyber | **Check, then decide.** Ask who carries registration-platform risk, and whether the corporate cyber policy covers event data. | Cheap if the exposure is real, waste otherwise. |

## 5. Go/no-go calendar

Dates are set just before the contract's fee step-ups. **I do not have your venue's schedule.** The T-90 and T-30 steps below are placeholders borrowed from the reference's representative structure. A step-up at T-180 would land on **15 Nov 2026**, a month from now, so read the schedule first.

| Date | Action |
|---|---|
| **Wed 21 Oct 2026** | Pull the venue and catering contracts and the flight fare rules. Get the fee step-up dates and percentages verbatim. Send both contracts' cancellation and force majeure clauses to counsel. |
| Fri 30 Oct | Broker quotes in. |
| Fri 13 Nov | Coverage decisions recorded, including the buy-back. |
| **Mon 1 Feb 2027** | Go/no-go #1 (before the placeholder T-90 step on Sat 13 Feb). |
| **Mon 1 Mar 2027** | Go/no-go #2 (before the 15 Mar catering payment of 19k). |
| **Mon 5 Apr 2027** | Go/no-go #3 (before the placeholder T-30 step on Wed 14 Apr). |

At each date, re-score the whole register first, then poll.

**Polled call.** Each area owner votes, and a single no-go halts the sequence. The COO holds the final call. A poll is warranted because more than two people's judgment must be reconciled, and a veto holder may exist.
- **Registration pace** (Marketing).
- **Catering headcount guarantee** (Event lead).
- **Speaker confirmation** (Program).
- **Contract exposure and payment integrity** (Finance).
- **Safety, travel and public health** (COO).
- **Brand exposure** (Comms).
- **Company health and budget** (COO).

**Thresholds.** They are fixed before the first date, so sunk cost cannot move them later. The numbers below are **my placeholders**. Re-derive them from your break-even and ratify them before 1 Feb.

| Area | Placeholder threshold | Outcome if missed |
|---|---|---|
| Registration, 1 Feb | ≥ 35% of target (~158) | Go-reduced. Cut headcount and scope. |
| Registration, 1 Mar | ≥ 55% (~248) | Go-reduced, before the catering payment. |
| Registration, 5 Apr | ≥ 75% (~338) | Go-reduced. No-go only if the entity can't absorb the loss. |
| Marquee speaker lost and uninsured | Backup not confirmed | No-go review. |
| Government restriction or credible safety threat | Any | No-go review. |
| Force majeure wording unclear on refunds | Counsel unconfirmed | No-go review. |

Cancelling earlier at a lower step-up can beat waiting for a legal outcome that is never guaranteed.

## 6. Cancellation decision memo (exposure only)

This is the one risk that gets a full assessment, because it is the decision that costs money. Exposure by date, all in EUR:

| Date | Committed and non-recoverable (assumed) |
|---|---|
| Today | 35k |
| 15 Mar 2027 | 54k |
| Ceiling at full fee liability | 129k |

Fill in the venue and caterer fee percentages from the contracts, so each decision date carries a real number.

## 7. Open questions

1. What is the venue fee schedule, verbatim? It sets the whole calendar.
2. What are the caterer's cancellation terms and headcount guarantee date?
3. Are the 11k flights refundable, changeable or neither?
4. Are tickets paid or free, and what is break-even or the pipeline target?
5. Does any sponsor money fund the 210k?
6. What insurance exists today, and did the venue require any?
7. Who holds a veto, and is there an in-house lawyer?
8. What country and city is this? That affects the long-weekend and strike risks.
9. Is alcohol served?
10. How many organizer hours are available, and is anyone willing to talk to a broker?

## Appendix: on-site emergency plan skeleton

This is a **separate printed document** for T-30, built with the venue's own plan. The scenarios are deliberately **not ranked**. Plan all of them, or state which ones the venue's procedures already own.

- **Fire and evacuation:** route, assembly point, and who confirms the building is clear.
- **Power failure:** which circuits the event overloads.
- **Medical emergency:** first-aid provider and the nearest hospital.
- **Theft:** laptops and AV gear.
- **Any other evacuation.**

**Contacts:**
- Venue security, on the number that reaches a human on the day.
- The police non-emergency line, labelled as distinct from the emergency number.
- Every lead organizer, with the hours each is on site.
- The venue on-call contact and the first-aid provider.

**Distribution:** a printed copy on site and a copy for every volunteer, since a drive link fails when power or connectivity does. Notify local emergency services in advance.

## Next actions

1. Assign names to the owner roles in section 3.
2. Get the contracts and send the clauses to counsel by 21 Oct.
3. Book the broker call.

I can also save the register rows, coverage decisions and date calendar to memory so edition 2 starts from a re-scored register. I haven't, because you didn't ask for it: should it go in memory, in CLAUDE.md, or nowhere?