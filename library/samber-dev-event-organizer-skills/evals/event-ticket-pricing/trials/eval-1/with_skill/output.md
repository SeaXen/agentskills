# Northline DevOps Day: ticket pricing

**Short answer:** charge a nominal fee, not the commercial price. I'd start at **950 SEK individual, 1,600 SEK corporate, 450 SEK student**, each excluding or including VAT per your accountant. Treat this as provisional. The skill says to take the revenue target from a budget, and I don't have one. Section 1 shows how to check these prices once you do.

The skill is built as a one-question-at-a-time interview, and I couldn't ask. I filled the gaps with labeled assumptions.
- **sourced** means it comes from the skill's references.
- **self-set** means I chose it.
- **assumed** means I guessed an answer you should confirm.

## 1. Revenue target

- **Missing:** I don't have a total expense figure or the share of it that tickets must cover.
- **Formula (sourced):** tickets must raise total expenses minus the sponsorship share.
- **Sponsorship share (sourced):** the devopsdays organizer guide targets 75-80%+ of the budget from sponsors. That leaves roughly 20-25% for tickets if you follow the community model.
- **Next step:** give me the total expense figure and I'll check these prices against it. Without it, the ladder could under-price tier by tier.
- **Your 41,000 SEK overrun is not the target.** It shows a headcount problem, which the posture below addresses.

## 2. Paid capacity after comps

| Group | Seats |
|---|---|
| Gold sponsors (4 × 6 passes, from signed contracts) | 24 |
| Speakers | 14 |
| Organizers | 9 |
| Volunteers | 22 |
| **Total comps** | **69** |
| **Paid seats (300 − 69)** | **231** |

- **Upper bound:** 231 is a ceiling. People who hold two roles, such as a speaker who also organizes, free up seats. Sponsor passes may also go unused.
- **Demand check:** you had 240 attendees last year, and some of them were comps. If demand holds after charging, 231 paid seats could sell out. In that case, run `event-market-fit` before moving the price. If sales are slow, use the same skill to split demand, marketing and price before touching the price.
- **Comps still eat catering.** All 69 need a confirmed headcount too. The fee does not help with those.

## 3. Posture: nominal fee

- **Why a nominal fee:**
  - Your pain is headcount certainty, not funding. A paid registration turns an unpaid RSVP into a headcount you can commit catering against.
  - The devopsdays guide sets the nominal band at **10-20% of a typical commercial ticket in the region** (sourced). Against 9,500 SEK, that is **950-1,900 SEK**.
- **Why not the commercial price:**
  - It needs a brand, an employer-funded audience and sales machinery. The skill promotes it only for a vendor-run event, or for a community event that sold out fast with demand visibly unmet.
  - Neither applies to you today. If this edition sells out quickly, revisit it for next year.
- **Why not stay free:** free is a funding decision, and you want to charge.
- **Compliance:** any price above zero brings accounting and tax handling, and the amount doesn't change that. Check VAT treatment, invoicing and who the legal seller is with an accountant. This is not legal advice.
- **Assumptions to confirm:**
  - Q9: a community-run event.
  - Q7: a recurring event, so keep prices stable and say so publicly.

## 4. Persona ladder

- **Payer split (assumed):** most DevOps attendees in Gothenburg are employer-funded, some are self-funded, and a few are students. Correct me if this is wrong, since the ladder shape depends on it.
- **Ratios:** I used EuroPython's ratios because it is community-run like you (sourced: business:personal 1.7-1.8:1, personal:education 2.1-2.2:1). PyCon US's wider 6.5:1 top-to-floor ratio fits a larger commercial funding model than yours.

| Tier | Price | Ratio |
|---|---|---|
| Corporate | 1,600 SEK (17% of 9,500, self-set) | 1.7:1 over individual |
| Individual | 950 SEK (10% of 9,500, bottom of the sourced band) | 2.1:1 over student |
| Student / education | 450 SEK (self-set) | corporate:student 3.6:1 |

- **Floor check:** set the 450 SEK floor against your catering cost per head. I don't have that figure.
- **Illustrative revenue (all assumed):**
  - Assumed mix: 50% corporate, 40% individual, 10% student. Blended price is about 1,225 SEK.
  - At 231 sold: about 283k SEK.
  - At 150 sold: about 184k SEK.
  - At 120 sold: about 147k SEK.
  - Compare these to the target from section 1 once you have it.

## 5. Date gate

- **Mechanic:** one announced step, published the day tickets go on sale. That's two price points per persona, the maximum.
- **Form:** a **late surcharge** (EuroPython does the same, sourced). I chose it over an early-bird discount because it pulls registrations forward before your catering deadline.

| Tier | Until date D | After D |
|---|---|---|
| Corporate | 1,600 SEK | 2,000 SEK |
| Individual | 950 SEK | 1,200 SEK |
| Student | 450 SEK | 450 SEK (no step, self-set) |

- **Surcharge size:** about +25% is my pick. EuroPython's step is 1.5x, and I went smaller because this is a nominal-fee posture.
- **D:** set D about 6 weeks before the event (self-set). I don't have your event date.
- **Sales close:** close sales at the catering headcount deadline.
- **Disclosure:** never raise a price the buyer couldn't have seen coming.

## 6. Access rungs

- **Student tier:** this is the published rung above. Self-identification or an institutional email check is the only gate.
- **Scholarship:**
  - Offer one only if a named reviewer commits to a stated response time. The skill says an unanswered application is worse than no route.
  - If you do offer it, keep it by email and unpriced, not a public tier. Reserve a small allotment from the 231 paid seats (10 is my number, self-set). Make the ticket non-transferable.
  - I don't know your reviewing capacity (Q8) or whether accessibility is a stated claim (Q10). Without a named reviewer, skip it.
- **Supporter tier:** skip it. It only works with an existing aid program to point at.

## 7. Bulk mechanics

- **Group discount:** 15% off for 5 or more tickets in the same order (sourced from devopsdays Halifax). It applies to the **regular price only**, never the late tier, so one seat is not discounted twice. State this on the page. I did not include an early-bird tier, so the exclusion covers the late tier alone.
- **Invoicing:**
  - Offer pay-by-invoice at full price, on request, only if your organizing entity can issue invoices and reconcile payments.
  - If it can't, delete this rung.
  - It is a payment rail, not a discount.

## 8. Refund and transfer policy (draft)

There is no industry standard beyond one dated cutoff, which all four sourced events share. Every line below is my proposal for you to decide.

> **Refunds:** full refund until **[date R]**. After that, no refunds. **[R = your catering headcount deadline, about 14 days before the event.]**
> **Administrative fee:** none.
> **Hardship:** requests for health, visa or travel reasons are handled by **[named person]** and may be accepted after R.
> **Transfers:** a ticket can be transferred to another named person for free until **[date T]**. If the two tickets' prices differ, the buyer pays the difference. A scholarship or comp ticket cannot be transferred.
> **If we cancel the event:** full refund. **[Check contract and insurance wording separately. Not legal advice.]**

- **Why align R with catering:** the cutoff exists to lock the headcount you pay for.
- **Publication:** publish this beside the price, not in a confirmation email.

## 9. Open items

1. Total expense figure and ticket share, to check the prices against.
2. The payer mix, to confirm the ladder shape.
3. Event date, to set D, R and T.
4. VAT treatment and invoice capacity.
5. Catering cost per head, to check the 450 SEK floor.
6. A named scholarship reviewer, or confirmation that the rung is dropped.

## 10. Next steps

- **No-shows:** a paid ticket reduces the exposure but doesn't remove it. The no-show handling, including unused comps, belongs to `event-no-show-management`.
- **Marketing:** acquisition belongs to `event-marketing-plan`.
- **Measurement:** write these down before tickets go on sale, with what each would change (all self-set):
  - Share of the revenue target banked by date D.
  - Persona mix against plan.
  - Group-order uptake.
  - Refund requests against the deadline.
- **Record after the event:** note what actually sold, so next edition starts from data.