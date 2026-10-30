# Worked sponsorship plan, plus a negative example

## Input

Ferrous Digest is a weekly community newsletter about Kestrel, an open-source message broker. One volunteer editor runs it under the project's fiscal host, which keeps 10% of income. 9,050 delivered addresses, mostly backend and platform engineers in the US and EU, with a sizeable German group. Signup asks for role. The charter allows "at most one sponsor per issue, labelled". A queue-monitoring startup offered to "sponsor the next four issues and get a mention in the news section". The editor can give four hours a month to sponsors and values an hour at 50. The signup page already says issues may carry labelled sponsor content. The startup says it pays about 8 per click in search. No past sponsor exists, but a labelled house ad for the project's conference drew 60% of the clicks of the editorial item beside it. The project's code of conduct forbids token sales.

## Plan

**Answer first:** yes, sell one labelled primary slot per issue, at 360 per issue for four prepaid issues; the card for the next booking is re-priced from the first two reports. Decline the news-section mention.

**Gate result**

| Condition | Evidence | Result |
|---|---|---|
| Measured engagement | 6 issues of per-link data, platform bot-click filter on; editorial item at position 2: median 120 unique human clicks | holds |
| Describable reader | role question at signup: 71% backend or platform engineers | holds |
| Seller with hours | editor, 4 h/month; fiscal host invoices | holds |
| Readers told | signup page mentions labelled sponsor content | holds |

**Acceptance policy:** readers are backend and platform engineers; vetoes: token sales, gambling, products that fork or rebrand Kestrel; the startup passes. No editorial coverage for sale; edits or rejection with a reason up to the copy deadline; one link to the sponsor's domain.

**Sales route:** direct primary slot. Network listing deleted: the list sits under the main marketplace's floor, and its ads would bypass the token-sale veto. Dedicated sends deleted: readers consented to the digest only.

**Inventory and caps:** one primary slot, position 2 (after the lead item), up to 60 words, one link, no image. No secondary slots. No exclusivity by default; category exclusivity for the booked issues costs 25% extra.

**Rate card**

| Method | Working | Result |
|---|---|---|
| Cost-recovery floor | (sending platform 120 + 4 h x 50 self-set) / 4 slots = 80, grossed up for the host's 10% | 89 per issue |
| Comparable ratio (band) | small niche developer titles price a primary slot at roughly 30 to 70 per 1,000 subscribers; 9.05k subscribers | 270 to 630 |
| Click value | 120 editorial clicks at position 2 x 0.6 ad discount (self-set, from the house ad) = 72 expected clicks; x 5 per click (the sponsor's 8 in search, buyer-supplied, discounted for lower intent) | 360 |

Click value sits inside the band and above the floor, so quote it: 360 per issue. The four booked issues keep 360; the next booking is re-priced once the first two reports replace the 0.6 discount with measured sponsor-unit clicks. Every figure the editor did not measure is labelled self-set or buyer-supplied in the kit.

**Label:** `AD · ANZEIGE` before the copy, in HTML, plain text and the archive, because a large share of readers is in Germany; archive link marked `rel="sponsored"`; sponsor kept out of the subject line.

**Booking terms:** four named issues; copy due two working days before each send; late copy runs as name, one neutral line and link; pause clause moves the slot or refunds it; make-good in the next issue; paid before the first copy deadline through the fiscal host; sponsor warrants its claims; aggregate report only.

**Report template:** delivered count, unique human clicks with the filter named, total clicks, link, position; opens marked directional.

**Reply to the sponsor:** the slot, the price, the label and the policy; the news section stays editorial, and their launch can still be submitted like any reader's item and judged by the curation rule.

**Pass thresholds:** all pass.

## Negative example

```
// ✗ Bad - priced on opens: "9,050 subscribers x 48% opens x 50 CPM = 217 per issue"
//   Opens are inflated by mail-privacy features; the sponsor measures clicks.

// ✗ Bad - "Presented by QueueWatch" as the only label
//   Reads as funding, not advertising; German readers need "Anzeige".

// ✗ Bad - "140 clicks on our lead story x 8 per click = 1,120 per issue"
//   Prices an ad on editorial clicks and the buyer's search CPC; the first report will show the gap.

// ✗ Bad - "four issues plus a mention in the news section"
//   Sells editorial coverage, the one thing a sponsor can never buy.

// ✗ Bad - "we guarantee 200 clicks or a free issue"
//   Gateway scanners click every link on arrival, so a raw-click guarantee is met by machines and means nothing.

// ✗ Bad - "we'll send you the list of companies whose engineers clicked"
//   No consent for that use; aggregate counts only.
```
