# Kiln Notes: sponsorship plan, rate card and booking contract

## Direct answer

**You can't accept this week, and you shouldn't promise to.** I can give you the contract and the rate card framework. Three things block signing, and none of them is paperwork:

1. **No decision to take ads.** The skill's first step says to settle this before anything else. Write the policy before the cheque arrives, not after.
2. **Nobody can receive the $4,000.** The project has no foundation and no company. Someone has to invoice, hold the money and handle tax. Until that exists, no sales route is open.
3. **You can't deliver six months.** "Roughly every two weeks when someone has time" means you can't promise a number of sends. A prepaid slot would force sends you may not make.

**Next action today:** send the holding reply below. It costs nothing and keeps the sponsor.

The price is also blocked. I have no delivered count, no click data and no seller-hours figure. I will not invent them. The $4,000 is the sponsor's offer, not your price.

## Holding reply to the sponsor

> Thanks, we're glad Kiln Notes is of interest. We're a volunteer newsletter and have never run sponsor slots, so we're writing our sponsorship policy and rate card first. We expect to reply with a price, terms and a label within [X days]. Every sponsor sees the same price for the same slot. One thing we can say now: a slot buys a labelled ad position, not coverage, a review or a mention in our editorial sections.

Replace `[X days]` with a date the maintainers can actually meet.

## Refused asks

| Ask | Basis | Instead |
|---|---|---|
| "Top sponsor slots" read as including coverage, a review or an editorial mention | Trust and house rule | A labelled slot only. Coverage stays the editor's call. |
| Booking 6 months of issues | House rule | Book a named number of committed issues. A pause clause moves or refunds the rest. |
| Dedicated send for the sponsor | EU/UK law | Not offered. Readers signed up for "the newsletter". |
| Sharing the list or clicker companies | EU/UK law | Aggregate counts only. |
| A click guarantee | Trust | Flat price per issue. |
| "Presented by" or "Sponsored by" as the label | Regulator guidance, German case law | "Ad" on the unit. |

I'll also decline the exclusivity implied by "top" unless it is bought as a priced add-on for the booked issues.

## Gate result: blocked

| Condition | Evidence you've given | Result |
|---|---|---|
| Six issues of per-link human-click data, with a stated bot filter | None | **Blocked.** Owner: whoever runs the sending platform. Fix: enable the bot-click filter and export the last six issues' per-link clicks. |
| A describable reader | None | **Blocked.** Fix: one signup question (role, company size, stack), or a short survey. |
| A seller with hours, plus an entity that can invoice | No named seller. No entity ("no foundation, no company"). | **Blocked, and it blocks every sale.** Fix: name one person to handle sponsors. Get an invoicing entity, such as a fiscal host (Open Collective, Software Freedom Conservancy or similar), and check that it accepts advertising income. |
| Readers told | Unknown | **Blocked, and it blocks every sale.** Fix: add "issues may carry labelled sponsor content" to the signup form and privacy notice. Announce it in an issue before the first paid one. |

If the engagement or reader evidence is the only gap, you can offer a **pilot booking**: one issue at the cost-recovery floor, with the missing data disclosed to the sponsor in writing. It cannot proceed while the seller, entity or "readers told" conditions fail.

## Decision record for the maintainers to adopt

The skill requires this before any sale. Put it to a vote and record it:

```
Kiln Notes sponsorship decision — [date]
1. Do we carry paid placements?            [ ] yes  [ ] no
2. Cap per issue:                          one labelled primary slot (proposed)
3. Who approves sponsors:                  [name, plus a backup]
4. Who sells and services sponsors:        [name], max [N] hours/month
5. Who invoices and receives money:        [entity / fiscal host], host share [X]%
6. Minimum editorial share per issue:      [e.g. all editorial items stay; ad is one unit]
7. Pause rule: if an issue is skipped, a booked slot moves to the next issue or is refunded.
```

If the answer to question 1 is "no", stop here and decline the sponsor. If you want a company to fund the project rather than buy a slot, route that to the open-source sponsorship skills (`oss-sponsors-fundraising`, `oss-sponsors-brand-strategy`). That is a different product with different terms.

## Acceptance policy (adopt this version, then judge the sponsor against it)

```
Kiln Notes accepts sponsors whose product serves developers who use or build with Kiln
[refine once you know the readers: role, stack].
We do not accept: [your vetoes, e.g. gambling, token sales, products that compete with or
rebrand Kiln, claims we cannot verify].
Sponsors buy a labelled slot. They never buy editorial coverage, ranking or a review,
and they do not see the issue before it sends.
We may require edits or decline copy, with a reason, up to the copy deadline.
One link per unit, to the sponsor's own domain. No downloads, no unreadable shorteners.
Questions: [address].
```

Keep an internal refusal log: date, sponsor, rule applied, who decided.

**Competitor rule.** Kiln has no commercial product, so the usual "refuse competitors" default has little to bite on. Replace it with: refuse any product that forks, rebrands or markets itself as a replacement for Kiln. Ask the sponsor now what they sell. A cloud company that offers hosted builds or caching is a likely fit for readers. Whether it is a fit for your maintainers is a vote, not my call.

**Judging the cloud company.** I can't do this yet. I don't know its product, its claims or your vetoes. Run it against the policy once the vetoes are written.

## Sales route

Ranking, best first:

1. One labelled primary slot per issue, sold direct.
2. Ad network listing.
3. Classified lines.
4. Bundles.
5. Dedicated sends.

**Recommendation: the direct primary slot.** The network listing is likely off the table. Networks mostly pass on lists under about 1,000 engaged subscribers, and a network's ads bypass your policy. Dedicated sends are deleted. Bundles need a standing sales job, which a volunteer team doesn't have. You haven't confirmed the direct route yet, so I'm waiting for your decision.

## Inventory and caps

- One primary slot per issue, in a fixed position (proposed: after the lead item).
- Spec (proposed, adjust once you see an issue): up to 60 words, one link, no image, label before the copy.
- No secondary slots until three consecutive issues sell out at the card price.
- Category exclusivity is a priced add-on, limited to the booked issues. Proposed at 25% extra (self-set).

## Rate card

Every number below is a formula or marked **self-set**. None is a quoted price yet.

### Method 1: cost-recovery floor (nothing sells below this)

```
floor per issue = (sending platform cost per issue
                   + seller hours per issue × hourly value, self-set)
                  ÷ (1 − fiscal host share)
```

Fill in the three inputs. Seller hours and hourly value are your call. A volunteer's hour still has a price.

### Method 2: comparable band (frames the price, never sets it)

Published developer-newsletter cards, dated Q2 2024, price a primary slot at about **20–30 per 1,000 subscribers** for lists of 36,000–180,000. A 16,000-subscriber database title charged about **73 per 1,000**. Small niche lists price higher per subscriber.

This band is **provisional** until I have your delivered count. For scale only: 5,000 delivered would give roughly $100–$365 per issue. Don't read that as your price. Use the ratio, not the dollar figures.

### Method 3: click value (sets the price)

```
price per issue = expected sponsor clicks × cost per click
expected clicks = median filtered human clicks on past sponsor units
```

You have no past sponsor units. Fallback: take editorial clicks at the slot's position times an ad discount, labelled self-set. With no labelled unit ever sent, quote the **bottom of the band** until the first report instead of inventing a discount. Any cost per click the cloud company states is buyer-supplied. Mark it and discount it, because a newsletter click carries less intent than a search click.

Until a sponsor reports, click value is capped at the band's top plus a third, and never goes under the floor.

### Quoted card

| Slot | Price rule | Quoted price |
|---|---|---|
| Primary, per issue | Click value, within [floor, band top + ⅓] | **Blocked:** needs delivered count and six issues of click data |
| Category exclusivity, booked issues only | Primary price × 1.25 (self-set) | Follows the primary |
| Secondary slot (not offered yet) | ⅓ to ½ of primary | n/a |
| Classified or job line (not offered yet) | 1/20 to 1/6 of primary | n/a |
| Multi-issue prepaid discount | Offered only for prepaid bookings. Published practice is mid-teens percent. | Set once the primary price exists |

**The $4,000 offer.** It is only comparable once the committed number of issues is fixed. At roughly 13 issues over six months, it works out to about $308 per issue. At 6 committed issues, about $667. Compare that figure against the floor and the quoted price. If the offer is below the quoted price, the answer is the quoted price, not a discount for being first. Every sponsor pays the same price for the same slot and date.

## Label

```
AD · Acme Cloud: [one-line product description]
```

- Add `ANZEIGE` (`AD · ANZEIGE · …`) if the interview shows German readers or a German publisher. I haven't asked that yet.
- Put the label before the copy, in the HTML part, the plain-text part and the web archive.
- Mark sponsor links `rel="sponsored"` in the archive.
- Keep the sponsor's name out of a normal issue's subject line.
- Do not use "Presented by", "Sponsored by", "Together with", or a logo alone.

This is practical guidance, not legal advice. Take real legal exposure to counsel.

## Booking contract (template)

Do not sign this until the decision record, the gate and the price are filled in. Have counsel review it, especially the entity, tax and refund terms.

```
SPONSORSHIP BOOKING AGREEMENT — Kiln Notes

Parties
  Publisher: [invoicing entity or fiscal host, legal name and address], acting for Kiln Notes
  Sponsor:   [legal name, address, VAT/tax ID]

1. Slot and issues
   One labelled primary slot in each of the following [N] issues of Kiln Notes:
   [list by issue number or by earliest sending date: "the next N issues sent
   after the Sponsor's payment clears"]. No issue is promised on a calendar date.
   The Publisher is not obliged to send an issue on any particular day.

2. Price and payment
   Price per issue: [card price, currency]. Total: [N × price]. Same price applies to
   every sponsor for the same slot and date.
   Payment in full before the first copy deadline, by [bank transfer / payment link],
   invoice issued by [entity]. [Tax/VAT treatment: to be confirmed with the entity.]

3. Hold
   A hold on the slot is released if not confirmed in writing within 7 days.

4. Copy
   Sponsor supplies copy within the slot spec (up to [60] words, one link, no image)
   at least 2 full working days before each send.
   Late copy runs as the Sponsor's name, one neutral line and the link, or moves to
   a later issue at the Publisher's choice. The Publisher never writes promotional
   copy for the Sponsor.

5. Acceptance policy and edit rights
   The Sponsor has read the published acceptance policy. The Publisher may require
   edits or reject copy, with a reason, up to the copy deadline, and may pull a unit
   whose claims or link destination change before send.

6. Label
   Every unit carries the fixed house label "AD" [and "ANZEIGE"] before the copy,
   in the HTML part, the plain-text part and the web archive. The label is not
   negotiable.

7. Links
   One link per unit to the Sponsor's own domain. The Sponsor may add its own
   tracking parameters. No downloads, no unreadable shorteners.

8. What the Sponsor does not buy
   Editorial coverage, ranking, a review, a mention in editorial sections, the right
   to preview the issue, or any subscriber data. Exclusivity applies only if bought
   under clause 12.

9. Warranty
   The Sponsor warrants that its claims are truthful and verifiable and that the
   link stays live and safe through the booked issues.

10. Cancellation by Sponsor
    With at least one week's written notice. Fees for issues more than a week away
    are refunded; fees for issues inside that week are not.

11. Pause, skipped issues and unsent issues (Publisher)
    If an issue is skipped, or the project pauses the newsletter, the booked slot
    moves to the next issue sent. If fewer than [N] issues have been sent by
    [end date, e.g. 9 months after payment], the Publisher refunds the unused issues
    in full within [14] days. The charter's pause rule outranks this booking.

12. Exclusivity (optional)
    [None / Category exclusivity for the booked issues only, for an added fee of [X].]

13. Make-good
    A failed send, broken link or missing label is rerun in the next comparable slot
    at no charge. That is the sole remedy for delivery failures.

14. Reporting
    Within one week of each issue, the Publisher sends: delivered count, unique human
    clicks (filter named), total clicks, link, issue and position. Opens, if shown,
    are directional only. No subscriber names, emails or companies.
    The Sponsor shares its measured result (signups, trials) when asked.

15. Performance pay
    None unless agreed in an addendum on top of the flat fee. Any such addendum names
    the Sponsor's tracking, and disputes are settled on the Publisher's filtered
    click count.

16. Data
    No subscriber list, clicker identities or company names are shared. Aggregate
    reporting only.

17. Liability
    [Counsel to complete: cap at amount paid; no liability for mail-delivery failures
    outside the Publisher's control.]

18. Governing law
    [Counsel to complete.]

Signed for Publisher: ____________  Date: ______
Signed for Sponsor:   ____________  Date: ______
```

**Sections the maintainers must fill in before use:** the entity, the number of committed issues, the end date, the price, the label wording, and sections 17–18. I left 17–18 blank on purpose; I can't write liability or governing-law terms for an entity that doesn't exist yet.

## Sponsor report template

Send within a week of each issue.

```
Issue: #[n], sent [date] to [delivered count] delivered addresses
Slot: primary, position [n], label "AD"
Link: [sponsor URL with their utm parameters]
Unique human clicks: [n]  (filter: [name of platform bot-click filter]; clicks within
                           [x] s of delivery and all-links-clicked sends removed)
Total clicks recorded: [n] (before filtering)
Opens: directional only, inflated by mail-privacy features; not reported as reach
Median unique human clicks, last six issues' primary slots: [n]
What we need back: signups or trials you attributed to this link
```

Never add subscriber names, emails or companies.

## Pass thresholds

| Threshold | Result |
|---|---|
| Gate states all four conditions with evidence | **Blocked.** No evidence supplied for any of the four. |
| Named sponsor judged against the written policy | **Blocked.** Vetoes unwritten and the sponsor's product unknown. Refused asks are listed with their basis. |
| Every price traces to the floor, a dated ratio or measured clicks | **Blocked.** Delivered count, click data and the floor inputs are missing. No number was taken from gross subscribers or opens. |
| Every paid unit carries "Ad" before its copy, in HTML, text and archive | **Passes** in the contract (clause 6) and label section. "Anzeige" depends on the reader-region answer. |
| Terms name copy deadline, edit rights, cancellation, pause clause, make-good and payment | **Passes** (clauses 4, 5, 10, 11, 13, 2). |
| Report template names the bot-click filter and holds no identities | **Passes.** |

## What I need from you, in order

The skill asks one question at a time. Answer these in order. Only the first is needed to continue.

1. **Do the maintainers want to carry ads at all, and who decides?** (Fill in the decision record above.) Everything else waits on this.

Then, with owners:

2. **Who receives the money?** Owner: the maintainers. A fiscal host, or a new entity, must exist and accept advertising income.
3. **Delivered count and six issues of per-link human-click data, with the bot filter named.** Owner: whoever runs the sending platform.
4. **Who reads Kiln Notes, and where are they?** Needed to describe the audience and to decide about "Anzeige". Owner: the editor.
5. **Does the signup text mention sponsor content?** If not, change it and announce it in an issue first.
6. **Who sells, with how many hours a month, and what is an hour worth?** Owner: the volunteer who takes this on.
7. **What does the cloud company sell, and what are its dates, slot wanted and any extra asks?** Paste their original message.
8. **How many issues will you commit to sending in the next six months?** This sets the booking size, and the $4,000 per-issue maths depends on it.

When 1–8 are answered, I'll turn the card into numbers and fill in the contract blanks.