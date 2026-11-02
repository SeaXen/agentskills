# Gridline Systems: response to their indemnity redline

⚠️ **This is a negotiation brief and a term-sheet section for your lawyer. It is not legal advice, and none of the language below is signable.** Every path ends at counsel in your jurisdiction. I haven't seen Gridline's redline text. Everything below assumes it says what you described.

## Short answer

- **Their version isn't wrong.** It isn't automatically right either.
  - Indemnification is a negotiated term with two real shapes: one-sided in the organizer's favor, or mutual. Which one lands reflects bargaining power, not an industry default.
  - Your draft used the one-sided shape: sponsor indemnifies for everything arising from their participation, organizer exposure capped at what they paid. That is the PyCon US 2020 / PSF shape. Their mutual version matches the shape in the Template Republic example: "Each party hereto shall indemnify and hold the others harmless."
  - Sponsor-side counsel routinely asks for this. Expect it.
- **Your treasurer's instinct is half right.** Conceding the one-sided shape to close a $15,000 deal is a legitimate business call. But "just accept it" is not safe, for three reasons:
  1. The real question is whether your **cap** survived. See the first check below.
  2. Indemnity scope and enforceability are jurisdiction-dependent. The template flags this clause 🔴 Counsel.
  3. This is a business decision about uncapped exposure. It should be made on counsel's read, not the treasurer's alone.
- **Recommendation: don't accept as written, and don't reject.** Counter with a bounded mutual clause (below) and keep the deal alive. Counsel reads the exact text before anything goes back to Gridline.

## What to check in their redline

1. **Did the cap on your exposure vanish?**
   - Your cap tied your liability to what they paid you. The PSF contract has no separate liability-cap clause: its protection came entirely from the one-sided indemnity plus that cap.
   - If their mutual clause is silent on caps, you may now owe uncapped indemnity at a 700-person event for a $15,000 fee.
   - This is the biggest risk in the redline, and the one a "just accept it" decision skips.
2. **Is the indemnity scope symmetric in practice?**
   - Sponsor-side guidance says sponsors usually ask for indemnity that also covers the organizer's own negligence, breach and IP infringement.
   - Check whether "mutual" quietly means that.
3. **Did they touch anything else?**
   - Compare the whole document, not just clause 8.
   - Check especially whether they merged sponsor-withdrawal and organizer-cancellation into one symmetric section. That is the most common structural error in this kind of document. The remedy for organizer cancellation must stay narrower (pro-rata net of expenses, or zero after a cutoff).
   - Also check that the force-majeure remedy is still named in words. Silence means a refund can be denied: _NetOne v. Panache_ (D. Haw. 2020) denied a refund on a clause that named none, while _Sanders v. Edison Ballroom_ (N.Y. Sup. Ct. 2021) ordered $45,219.28 returned on a clause that named one.
4. **Insurance link.** A mutual indemnity is only as good as the cover behind it. What does your insurance, or the venue's master policy, actually cover for sponsor-caused injury at a booth or demo? See the insurance section.

## Options for the indemnity clause

| Option | What it is | Fit |
| --- | --- | --- |
| **A. Hold your original** | One-sided indemnity plus organizer cap at fees paid | Strongest for you, most likely to be struck again. Sponsors' counsel push back on it. |
| **B. Mutual, cap preserved** (recommended counter) | Each party indemnifies the other for claims from its own acts, breach and IP; **your liability cap at fees paid stays** | Meets them on mutuality and protects the number that matters. |
| **C. Accept their mutual as written** | Uncapped (if the cap is gone) | Only if counsel confirms the cap or equivalent protection survives elsewhere, or the organizer's insurance covers the exposure. |

My default is **B**. It gives Gridline's legal team the mutuality they asked for. It also keeps the single protection you actually need, the cap, which their text may have dropped.

If your lawyer has time, ask them to also consider these points. All are 🔴 counsel questions, and none is something I can settle from the collection's examples:
- Whether the indemnity should be fault-based ("to the extent caused by") rather than "all claims arising from participation".
- Whether the cap should apply to your indemnity but not theirs, or to both.
- Whether the cap is enforceable under local law and which carve-outs it needs.

## Term-sheet section, ready for counsel

> **8. Liability and indemnification** 🔴
>
> **Position (open).** Organizer's original draft: one-sided sponsor indemnity, organizer exposure capped at fees paid (PyCon US 2020 shape). Sponsor's redline: mutual indemnity (Template Republic shape). Organizer's counter: mutual, each party responsible for its own acts and breaches, **organizer liability cap at fees paid retained**.
>
> _Why:_ both shapes appear in real published terms and the choice reflects bargaining power. The organizer can concede mutuality to close a $15,000 deal, but not the cap.
>
> 🔴 **For counsel:** scope ("arising from participation" vs. "to the extent caused by"); whether the cap is enforceable locally and which carve-outs it needs; whether the sponsor's redline silently removed the cap; interaction with the insurance clause; whether the organizer's own insurance covers the indemnity it is now giving.

## Insurance clause (decide this alongside)

- At 700 people with a booth or demo, the default rung is **$1M per occurrence / $2M aggregate CGL**, naming you as additional insured. This figure is convergent across many exhibitor-requirement documents.
- Tie the **certificate deadline to contract execution**, not event day, and hold the booth until the certificate arrives. A clause nobody collects against is worse than none.
- If the sponsor objects, a single-event policy meeting this standard can be bought for well under a hundred dollars (one vendor publishes $79 for a $1M/$2M booth policy; treat that as an order of magnitude, not a market rate).
- Move up to **layered coverage** only if alcohol is served, demos carry physical risk, or sponsors bring vehicles or heavy equipment. Does the venue contract already flow any of this down to you?

## What to do, in order

1. ⏳ **Don't reply to Gridline or tell the treasurer "accept" yet.** First, send counsel the full redline and this brief. The term sheet must reach counsel before anyone is asked to sign.
2. **Diff the whole redline**, not just the indemnity clause, against your draft (the cancellation, force-majeure and cap checks above).
3. **Confirm the cap's fate.** This one fact decides whether accepting is a concession or a blank check.
4. **Counter with Option B.** Say plainly that you accept mutuality and want your cap retained. Frame it as meeting them halfway.
5. **Get the insurance question answered**: what the organizer's and the venue's cover actually includes.
6. If Gridline refuses any cap, escalate to a named decision-maker with counsel's read of the exposure. Accepting then becomes an informed business decision about a number, not a way to avoid losing the deal.
7. After countersignature, hand the deliverables exhibit to `event-sponsor-fulfillment` and the payment milestones to whoever invoices.

## Questions I need answered

Please answer these so I can re-rank the options and finish the term sheet:

1. **Contracting entity (Q4).** Is it an incorporated non-profit, a company, a fiscal sponsor, or unincorporated volunteers? If unincorporated, personal exposure is the real issue and counsel comes before anything else.
2. **Counsel (Q5).** Do you have a lawyer, a fiscal sponsor's legal team, or nobody yet? And which jurisdiction?
3. **Signing date (Q6).** By when must Gridline sign? A tight date raises the pressure to concede.
4. **Effort ceiling (Q8).** Is it a volunteer treasurer with a template, or a lawyer who can negotiate clause by clause?
5. **Physical risk (Q9).** Is alcohol served, are there sponsor demos with physical risk, and does the venue contract already require insurance?
6. **Pole (Q1).** Is the event community-run or company/foundation-run? A community-run event has less leverage and favors shorter clauses.

## Handoff to counsel

This document is **not a contract and not legal advice.** Drafted from published examples: the two indemnity shapes and the insurance rung. Left for you to decide: indemnity scope, cap enforceability and carve-outs, governing law, and whether the organizer's cover supports the indemnity it gives. The first sponsor signature date is open pending Q3 above.