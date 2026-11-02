# Halvorsen Data developer digest: programme charter

Draft, 2026-10-23. Ines writes the digest. I couldn't interview anyone, so every fact I didn't have is a named open question at the end. I invented none of them.

## Direct answers to the PM

1. **Industry-standard ratio of own content to external links: none exists.**
   - No curator or vendor publishes a numeric ratio. Stripe's digest mixes own updates with a community slice, GitHub Insider is almost entirely its own content, and HashiCorp mixes product, events and some industry news.
   - The ratio below is a house rule we chose. Don't call it a benchmark in any deck.
2. **Can the paying partner take the lead slot? No, not the editorial lead.**
   - Paid placements need a "sponsored" label, the same inclusion criteria as editorial items, and a per-issue cap.
   - Console.dev keeps ads separate, and Cooperpress tags sponsored links and reviews sponsor copy.
   - The lead is the one position where readers can't tell a pick from a purchase, and we haven't yet shown that external links earn clicks.
   - **What the partner can have:** one labeled "Sponsored" block, visually separate from the editorial sections. I recommend placing it right after the editorial lead.
   - **If the partner insists on the top:** allow a labeled block above the masthead lead, never styled as an item, and never in the subject line or preheader. That is your call as house owner. Golang Weekly runs a primary-sponsor block this way, so it is defensible.
   - **Not decided here:** price and sales terms. They are out of scope for this charter.

## 1. Gate result

| Condition | Result | Evidence or missing fact |
|---|---|---|
| Supply fills the sections at monthly cadence, with an evergreen reserve covering two issues | **Unproven** | No three-month count of own versus external items yet |
| Named owner and an agreed backup | **Partial** | Owner is Ines. Backup and hours per issue are unknown. |
| Readers want email over a feed | **Unproven** | 8,000 subscribers is a size, not demand. Clicks and replies for the last six issues are needed. |

- **Outcome:** keep monthly and add the external section as a trial. Adding external links raises supply needs, so the gate decides before the rule goes live.
- **Test for the next issue:** each condition gets a pre-agreed threshold. Every threshold below is a house rule.
  - **Supply:** the count shows at least 5 own time-bound items and 2 usable external items for the issue.
  - **Backup:** a named person who has agreed.
  - **Demand:** the issue's clicks per delivered email are at or above the average of the last six issues, bot clicks filtered.
- **If a condition fails:** fall back to a feed-only changelog or a pause. This charter says which condition failed.
- **Consent first:** classify the 8,000 before computing any number. Compute every metric on the segment we may lawfully keep mailing.

## 2. Shape

- **Own-surface digest, monthly, plus one trial external section.** This is the skill's default for a vendor with steady releases.
- **Not yet curated ecosystem.** Promote it only after three monthly digests, each with a trial external section whose items drew clicks. It also needs a backup, which we don't have.
- **Sponsored slot:** it sits beside the shape and counts toward neither the own share nor the external share.

## 3. Cadence and rhythm anchor

- Monthly, on a fixed calendar day. The release train anchor is unconfirmed.
- Each issue covers everything shipped since the last one.
- Slow down after two consecutive thin issues. Speed up only after three consecutive full ones.
- Never raise cadence to fix engagement.

## 4. Curation rule (house rule, not an industry standard)

**Share.** Each issue carries 6 to 9 editorial items, split as follows.

- **Own:** about three quarters, 4 to 6 items.
- **External:** at least 2 and at most 3 items, roughly one external for every three own.
- **Sponsored:** at most one block, outside both counts.

| Slot | Count | Counts toward |
|---|---|---|
| Own items | 4 to 6 | own share |
| External editorial links | 2 to 3 | external share |
| Sponsored block | 0 or 1 | neither |

**Reading the share.**
- Anything community members wrote is external, even on our forum.
- A partner's page placed as a sponsored block is sponsored. The same page is external editorial only if Ines would pick it unpaid.
- The partner doesn't get an extra editorial link for paying. Paying never earns an editorial mention.
- If supply falls short, drop the external section for that issue rather than pad it.

**Inclusion criteria (every item, sponsored or not).**
- A reader could use it this month: a tutorial, benchmark methodology, integration walkthrough, talk or release that explains usage.
- It works without sharing an email address (no gated content).
- Vendor-neutral enough to interest the ecosystem, not only users of one product.
- Ines would forward it to a colleague in Slack. That is TLDR's test.

**Exclusion list.**
- **Named customers.** Never name a customer, in our copy or in the link text we write. Excluded links include customer case studies and posts by a named customer about using Halvorsen. Legal to confirm the second case.
- **Competitor comparisons.**
  - No item that compares Halvorsen with a named competitor.
  - No external link whose main point is a head-to-head, "X vs Y" or ranking of named vector databases.
  - Incidental mention in a neutral article is fine.
  - Sponsored copy follows the same rule.
- **Unannounced features.** Excluded by default (see the open questions on the teaser).
- Gated content, and announcements without a usage example.
- Paywalled content.

**Sponsored block rules.**
- It is labeled "Sponsored" in the heading, and never in the subject line or preheader.
- The sponsored page meets the inclusion criteria and the exclusion list, including no gating.
- Ines has the right to reject or edit sponsor copy. The partner sees no other issue content before send.
- The cap is one per issue.
- If the issue is thin and the editorial sections are dropped, the sponsored block still doesn't become the lead.
- Sponsored placements are commercial mail, so the issue keeps the opt-out, postal address and honest headers.

## 5. Section template

Six sections, in fixed order.

| Section | Source | Owner | Items | When empty |
|---|---|---|---|---|
| Shipped this month | release notes, changelog | Ines (backup TBD) | 2 to 4 | merge into "In brief" |
| Editorial lead: one thing to try | docs, tutorial | Ines | 1 | run a named evergreen slot from the docs backlog |
| Sponsored | integration partner | Ines | 0 or 1 | drop the block, no make-good in the lead |
| Built by the community | forum, community answers | Ines | 1 to 2 | drop the section |
| Elsewhere in the ecosystem (trial) | external links | Ines | 2 to 3 | drop the section |
| In brief | events, docs updates, talks | Ines | 2 to 4 | drop the section |

- Never pad. Decide where each issue's public URL and archive live. A public archive outlives the list.

## 6. Ownership and handoff

- **Owner:** Ines. **Backup:** blocked, not named.
- **Reviewer:** blocked, and legal review per send is unconfirmed.
- Hours per issue are unknown.
- The sending account, list export, domain and archive must belong to the organisation, not a personal account or card.
- The runbook holds the template, send day, checklist, account owners and this curation rule.
- Name the running cost (sending platform tier, domain, editor hours) and the budget line that pays it. Does sponsor revenue fund it? That is a decision for you.
- Rotate the backup in for one issue per quarter so the role stays practised.

## 7. Measurement

- **Primary signals:** clicks per delivered email, unique clickers across the last N issues, unsubscribes, complaints and replies.
- Enable the platform's bot-click filter, or discard clicks within seconds of delivery and sends where every link was clicked. Report the filter used.
- Report open rate, click-to-open and open-based reach as directional only, never targets, because mail-privacy features inflate them.
- **Outcome signal:** matches the funding answer, which we don't have. Provisional: clicks on external links, to promote or retire the external section.
- **Sponsor reporting:** report the sponsored block's clicks to the partner, with the same filter.
- **Baseline:** the last six issues. Any threshold set from it is a house rule. Review quarterly against the team's own trend.

## 8. Pause and sunset rules

| Trigger | Action |
|---|---|
| Ines leaves and the backup can't take over within one cycle | Send a short hiatus note, then hand over with the checklist or downgrade to feed only |
| Two consecutive thin issues | Drop to a slower cadence or merge into the changelog |
| Clicks and replies fall for two consecutive quarters against our own trend | Re-run the gate |
| Three digests with the trial external section, and its links draw no clicks | Retire the external section and keep the own-surface digest |
| A sponsored block fails the inclusion criteria after sale | Refuse or edit the copy. Don't run it labeled "sponsored" to get around the rule. |
| Need moved to another channel | Close with a final issue pointing to the replacement |
| Running cost has no budget line | Close or downgrade before anyone pays personally |
| List silent for more than six months | Send a re-permission issue first, suppress non-responders |
| Subscribers with no human click and no reply in twelve months, bot clicks filtered | One re-confirmation, then suppression |

- Announce every pause. Never skip an issue silently.

## Consent

- State how the 8,000 were collected. Individual UK and EU addresses need consent or a valid soft opt-in.
- US mail needs a working opt-out honoured within 10 business days.
- Suppress only the segment with no basis, invite it once through the product, and send the call to whoever owns privacy.
- The newsletter stays out of transactional and account email.

## Open questions

| Question | Owner | Re-check |
|---|---|---|
| **Unannounced feature teaser.** Legal hasn't ruled on it. Recommended default: no teaser until the feature is announced, then run it as a normal own item. If product wants a teaser, a named approver signs off in writing and it stays an own item, never sponsored. | legal and product | 2026-10-30 |
| Backup person and reviewer for each issue, hours per issue | you | 2026-10-30 |
| Supply count for the last three months, split own versus external, rate and evergreen reserve | Ines | 2026-10-30 |
| Consent provenance and date of the 8,000, last send date, clicks, unsubscribes and replies for the last six issues | Ines and privacy owner | 2026-10-30 |
| Why is this funded: retention, reach, contributors or credibility? | you | 2026-10-30 |
| Does legal review every send? Do customer-authored public posts count as naming a customer? | legal | 2026-10-30 |
| Who holds the sending account, list export and domain? | you | 2026-10-30 |

## Pass-threshold result

| Threshold | Result |
|---|---|
| Gate states all three conditions with evidence | **Fails for missing facts: blocked** (supply count, demand numbers) |
| Cadence derived from the time-bound rate and owner hours | **Blocked**: monthly is provisional until Ines supplies the count |
| Curation rule is a stated share plus written criteria, labelled a house rule | **Pass** |
| Every template section has source, owner, items and an empty-section rule | **Pass** |
| Owner and backup named, accounts held by the organisation | **Blocked**: backup and account holder unknown |
| No open-derived primary metric, one outcome signal matched to funding | **Partial**: provisional signal until the funding answer arrives |
| Every pause and sunset trigger has a threshold and an action | **Pass** |
| Consent provenance stated, stream separate from transactional | **Blocked**: provenance unknown |

**Decision needed from you:** the sponsored block's position (after the lead, or a separate labeled block above it). I recommend after the lead.