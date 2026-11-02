# Halvorsen Data developer digest: curation rule (v1)

## Answers to the PM

**1. Industry-standard ratio of own content to external links: there isn't one.** I know of no reliable published benchmark, and I won't invent a number. Here is a starting rule you can change after data:

- Each issue has 6 editorial items. At most 2 are ours, so own content stays at or below one third.
- At least 4 are external.
- The sponsor slot is not an editorial item, so it doesn't count toward either number.
- After 3 issues, compare click share and unsubscribes by item type, then adjust.

**2. Can the paying partner take the lead slot? No, not the editorial lead.** Let them buy a labeled sponsor placement instead.

- Paid placement must be clearly identifiable as advertising. US FTC guidance and EU/French rules both require it. Ask legal to confirm the exact wording.
- A paid lead styled as editorial turns Ines's picks into ads. That damages the trust behind the 8,000 subscribers.
- Offer the partner a fixed, top-of-issue sponsor block. It has its own format, a "Sponsored" label, and sits above the editorial lead.
- If top placement is the sticking point, you can sell the block above the lead. You can't sell the lead itself.

## The rule

### Roles

- Ines owns selection and has the final say on every editorial item.
- Sales and partners can't pick, rank, or veto editorial items.
- Legal reviews the sponsor block and any item that mentions a product, a customer, or a competitor.

### Issue structure

1. Sponsor block: one slot, at the top, labeled "Sponsored", in a distinct format.
2. Editorial lead: Ines's pick of the month.
3. Five more editorial items: at most 2 ours in total (the lead can be one), at least 4 external.
4. Footer: how we pick links and how sponsorship works.

### What qualifies as an editorial external link

- It is useful to a developer building with vector search, retrieval, or data infrastructure.
- It is a primary source: the author's own post, repo, paper, or talk.
- It isn't marketing for something we have a commercial relationship with, unless it meets all other criteria on merit.
- Ines can say in one sentence why a reader should click.
- Each link appears once per quarter. Each source appears at most once per issue.
- A partner can appear in editorial on merit, but never in the issue where they hold the sponsor slot.

### Sponsor slot

- One slot per issue, sold only to integration partners.
- The partner supplies copy, and we edit for accuracy and length.
- The label says "Sponsored" or "Sponsored by <partner>". Never use "Partner pick" or "Featured".
- Sponsor copy follows the same legal limits as our own writing (see below).
- Payment doesn't buy editorial coverage, a review of the copy beyond accuracy, or early access to the issue.
- Publish the sponsorship policy at a stable URL and link it from the footer.

### Legal constraints applied to curation

- **Customers:** never name them in a blurb, headline, or sponsor copy.
  - Don't link to a piece whose main point is a case study naming one of our customers.
  - Don't link to a partner post that does so either.
- **Competitors:** don't compare Halvorsen Data with competitors in our own words.
  - Don't link to a piece whose main point is comparing us with a competitor, or a benchmark ranking us.
  - Neutral ecosystem content is fine, such as a tutorial on a shared tool or a general architecture post.
  - Ask legal whether links to competitor-authored posts are allowed. I would exclude them by default.
- When in doubt, drop the link. Ines doesn't have to justify a drop.

### Unannounced feature teaser

Curation doesn't cover this. It is our own content, so it goes through an approval gate:

- It can only appear as one of our 2 own items, never in the sponsor block and never in the external links.
- Legal and product both sign off on the exact text before the issue is scheduled.
- State no dates, pricing, or commitments. Describe what developers will be able to do, not when.
- Keep the issue draft from the paying partner until it is sent. This is especially important if the feature touches their integration, because a teaser next to their ad would look like a favor.
- If product won't accept these limits, move the teaser to a later issue.

### Review

- Ines checks each issue against this rule before send, using a 6-line checklist: structure, ratio, labels, customer names, competitor comparisons, and teaser approval.
- After issue 3, review ratio, clicks, and unsubscribes, then revise the ratio.

## Decisions to confirm

1. **Sponsor placement:** is a labeled block above the editorial lead acceptable to the partner? If they insist on the editorial lead, the answer is no.
2. **Competitor-authored posts:** does legal want them excluded?
3. **Teaser:** go ahead in this issue with the gate above, or defer?