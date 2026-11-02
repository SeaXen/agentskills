**Not legal advice, and not a contract.** This is a term sheet for a lawyer in your jurisdiction to review. Don't have sponsors sign it as written.

The skill says to interview you one question at a time. You asked for the complete answer in one pass, so I've stated my assumptions and listed what to confirm at the end.

## 1. Cure period: don't copy "PSF 15 days"

**The PSF claim doesn't hold up.** The only public PSF sponsorship contract (PyCon US 2020) has no cure period, no "cure" language and no notice-and-remedy provision. Termination there is at the PSF's "sole discretion… without recourse."

The PSF's current year-round agreement is finalized privately and unpublished. So I can't confirm or refute a 15-day figure for it. Don't write "PSF standard" in the template, in the docs, or to sponsors.

**Recommendation: a 30-day cure period, plus a short event-proximate variant.**

| Situation | Cure period | Verified source |
|---|---|---|
| Normal breach | 30 days after written notice | SAGE World ("not cured within thirty (30) days"), AFCEA FedID ("uncured after thirty (30) days written notice"), American Pets Alive! ("remains uncured 30 days") |
| Breach found close to the event | 3 calendar days. A breach not curable at least 1 day before the event counts as non-remediable. | eXp/AGNT |

- **Why the second tier.** A 30-day cure is useless for a missed logo asset the week before doors open. A single long cure period would also freeze your ejection and de-branding remedies.
- **15 days is a legitimate choice, but not a standard.** 15-day cures exist in the general template market, and a 14-day one appears in a sports-sponsorship agreement. If you want 15, adopt it as your own choice and flag it for counsel. It has no verified precedent in tech-event sponsorship.
- **Keep these outside the cure mechanism:**
  - Payment default. It has its own express late-interest clause (verified range 12–18% per annum) and a de-branding remedy.
  - Code-of-conduct ejection. It is immediate and carries no refund.
  - Editorial refusal. It is not a breach and carries no refund.
- **Note for counsel.** Mark the cure clause 🟢 Decided (30 days, sourced), and mark the 3-day variant 🟠 Open until you confirm you want it.

## 2. Renewal: replace the exhibit, not the agreement

**The mechanic.** Put everything that changes each year (tier, price, perks, deadlines, dates, any deal-specific clauses) into a self-contained Exhibit A. The legal terms then stay untouched.

- **Template shape.** The PSF/PyCon US template renews this way. A new Exhibit A is issued, and the sponsor's approval of it counts as written notice to continue under the original terms for another year.
- **Self-containment rule.** Any perk or deadline written into the body of the agreement instead of the exhibit will carry silently into a year where it no longer applies. Audit the body for those before the template goes to counsel.

**On your "roll over unless they tell us otherwise" goal, I'd steer you away from pure silence-based renewal.** The skill's own source material flags this:

- Auto-renewal on non-objection is convenient for you, and it is the shape sponsors' procurement teams most often strike.
- Requiring affirmative approval of the new exhibit is slower, but far easier to defend.
- Whether silence can bind a sponsor to a new price is also jurisdiction-dependent. That is a 🔴 counsel flag.

**Recommended design: a rollover that is easy for the sponsor, not automatic for you.**
1. At a fixed date before the next edition (for example, 120 days out), you send the sponsor a **new Exhibit A**, pre-filled with last year's tier and the new price and dates.
2. The sponsor approves it by a one-line written reply, and the original terms continue for another edition.
3. **Silence means no renewal, and the slot is released after a stated date.** You can then resell it. This also keeps your published caps honest, since you can't promise a tier slot you've effectively double-booked.
4. For your top sponsors, offer a **right of first refusal** on their slot until that date. It gives them the "we just roll over" feeling without binding anyone by silence.

If you still want true auto-renewal, this is the version to hand counsel:
- Renewal happens only at last year's price, or at a price change notified in the exhibit with a stated lead time.
- The sponsor gets a stated opt-out window, with the notice date in the agreement.
- Each party gets a termination-for-convenience right (the PyCon template has a 60-day one).
- **Mark this version 🔴 Counsel.** Expect sponsors to push back on it.

**Exclusivity does not auto-renew.** Exclusivity is an add-on, drafted only if you actually sold it, and it must be bounded to the paid term. If any sponsor has it, state one of three outcomes:
- It renews with the exhibit.
- It lapses at term end.
- It converts into a right of first refusal.

I recommend the right of first refusal. It also keeps next year's inventory sellable if the sponsor walks.

## Other template-driven points

Because this is a reusable template (interview Q7), the skill promotes the higher-effort options once, since the cost is amortized:
- **Force majeure.** Consider the sponsor-elected credit or refund with a dated window (Linux Foundation 2021 gave 14 days to elect). It keeps both the cash and the sponsor. Pro-rata net of expenses stays the safe community-pole default. Whichever you pick, the remedy must be written out in words. *NetOne* denied a refund on a silent clause; *Sanders* ordered $45,219.28 back on an explicit one.
- **Exhibit as the renewal unit.** This is also where negotiated deltas live, so the body stays clean.
- **Reminder.** Keep sponsor withdrawal and organizer cancellation as two separate clauses. Never merge them into one mutual section.

## Open questions I need from you

1. Contracting entity: incorporated non-profit, company, fiscal sponsor, or unincorporated volunteers? Unincorporated needs counsel before anything else here.
2. Jurisdiction, governing law, and who your counsel is. This is the handoff target.
3. Community-run or company-run? This decides whether any data clause is draftable at all.
4. Were per-tier sponsor caps published? Give me the exact numbers, because the contract must not be looser.
5. Did any sponsor buy exclusivity?
6. Effort ceiling: a volunteer treasurer with a template, or a lawyer with time to negotiate?
7. Alcohol, physical demos or vehicles at PortsConf? This decides the insurance level.
8. By what date must the first sponsor be able to sign?

## Counsel handoff

- **Drafted from published examples:** the 30-day and 3-day cure periods, the exhibit-replacement renewal, and the right of first refusal.
- **Your decisions:** whether silence renews anything, the cure-period length if it differs from 30 days, and the force-majeure remedy.
- **🔴 For counsel:**
  - Enforceability of any silence-based renewal and any price change on renewal.
  - Governing law.
  - The interaction between the cure period and the immediate remedies.
- **Timing.** Get this to counsel before the first sponsor is asked to sign. That is the one failure that can't be fixed afterward.

If you'd like, I can produce the full numbered term sheet with the deliverables exhibit once you've answered the open questions.