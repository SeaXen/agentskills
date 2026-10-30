# Worked example: rescue charter and a negative example

Illustrative scenario, not a real company. The numbers show the arithmetic, not targets.

## Scenario

A feature-flag SaaS sends a biweekly developer newsletter to 9,000 subscribers. The co-founder wrote every issue for two years, then moved to a full-time CEO role. The last issue went out seven weeks ago. The last six issues averaged 41% opens, 1.4% clicks, 0.3% unsubscribes, and a handful of replies each. The list is a mix of 6,500 newsletter signups (checkbox at signup, unticked by default) averaging 1.9% clicks, and 2,500 product accounts imported in year one averaging 0.2%. Most imported accounts are individual addresses in the EU and UK, and the signup form offered no newsletter opt-out. The team ships two releases a month, one blog post a month, and runs a monthly community call. One developer advocate can give four hours per issue; a docs writer agrees to be backup.

## Interview answers that moved the ranking

- Effort ceiling about eight hours a month: deletes the curated ecosystem shape at biweekly cadence.
- No one else can write in the founder's voice: deletes the personal editorial letter.
- Compounding mandate, no hard date: no promotion for speed.
- Contributors post integrations in the community forum every week: noted as the condition that later promotes a community-edited section.

## Supply count, last three months

| Source | Items | Own or external |
|---|---|---|
| Release notes | 6 releases, 14 notable changes | own |
| Blog | 3 posts | own |
| Community call recordings | 3 | own |
| Forum integrations and answers worth surfacing | 11 | external |
| Ecosystem news readers would want | ~6 | external |

Rate: about 7 time-bound items a month (releases, call recordings, ecosystem news). Evergreen reserve: about 9 forum integrations and answers still useful in two months. At five to seven items per issue, biweekly needs 10-14 items a month and spends the reserve within weeks. Monthly fills its time-bound sections from the rate and keeps two issues of evergreen reserve at restart.

## Charter

**Gate result.** Consent classified first: the imported segment has no lawful basis for most addresses, so the gate uses the 6,500 newsletter signups, plus any US imported addresses the privacy owner confirms. Supply: holds at monthly, fails at biweekly. Owner and backup: holds, advocate plus docs writer, four hours per issue. Demand: holds, 1.9% clicks and steady replies on the lawful segment. Result: keep, at a slower cadence.

**Shape.** Own-surface digest with one external section. Rejected: feed only (readers reply and click, so curation adds value); curated ecosystem (fails the effort ceiling at biweekly); personal letter (author gone).

**Cadence and rhythm anchor.** Monthly, sent the Tuesday after the monthly community call so the recording and its follow-ups land in the same issue. Slow down after two consecutive thin issues; speed up only after three consecutive full ones.

**Curation rule.** House rule: at least two external items per issue, roughly one external item for every three own items. Include: anything a reader could use this month. Exclude: gated content, announcements without a usage example, comparisons with named competitors. Label any paid or partner item.

**Section template.**

| Section | Source | Owner | Items | When empty |
|---|---|---|---|---|
| Shipped this month | release notes | advocate | 3-5 | never empty at this cadence |
| From the community call | recording, chat log | advocate | 1 | drop the section |
| Built by the community | forum | docs writer | 1-2 | drop the section |
| Elsewhere in the ecosystem | external news | advocate | 1-2 | drop the section |
| One thing to try | docs | docs writer | 1 | evergreen tip from the docs backlog |

**Ownership and handoff.** Owner: developer advocate. Backup: docs writer, who assembles one issue per quarter so the backup role stays practised. Reviewer: one engineer, 30 minutes per issue. The sending account, list export, domain and archive move from the founder's personal account to a company account before the restart. The runbook lives next to the release process and lists the template, the send day, the checklist, account owners, and the curation rule.

**Measurement.** Clicks per delivered email, unsubscribes, complaints and replies per issue, plus unique clickers across the last three issues. Outcome signal for the retention goal: feature-flag rules created from links in the issue. Opens and click-to-open are reported as directional, never targeted. Quarterly review against the list's own trend.

**Pause and sunset rules.**

- Owner and backup both unavailable for a send: publish a one-line hiatus note, never skip silently.
- Two consecutive issues that need padding: merge into the changelog with a monthly feed email.
- Clicks and replies down two consecutive quarters: re-run the gate.
- Community forum takes over the digest's job: close with a final issue pointing there.

**Consent.** Product accounts imported in year one have no recorded newsletter consent, and with no opt-out offered at signup no soft opt-in applies to the EU and UK individual addresses. Segment them out before computing the gate's numbers, and invite them once through the product, separately from account email. US addresses in that segment can stay with a working opt-out; the privacy owner confirms the split.

**Restart.** The first issue back says what changed: monthly, who writes it now, how to unsubscribe in one click.

**Pass thresholds.** All pass after two revisions: the first draft kept biweekly cadence, which failed the supply check; the second omitted the empty-section rule for two sections.

## Negative example: the same scenario planned badly

```
// ✗ Bad - fixes the symptom the team can see, not the cause
Goal: raise open rate from 41% to 50% by Q3.
Cadence: move to weekly to "stay top of mind".
Plan: A/B test subject lines, add emojis, resend to non-openers.
Owner: "the devrel team".
Content: product updates and tips, every issue.
```

What is wrong with it:

- Open rate is the target, and the measure most inflated by mail-privacy features.
- Weekly cadence doubles demand on a supply that barely fills biweekly, and quadruples it against the monthly cadence the supply supports, so issues get padded within a month.
- "The devrel team" is not an owner, and no backup exists: the founder's departure repeats with the next person.
- Own content only, with no curation rule, so the newsletter becomes a product ad.
- No pause or sunset rule, and the imported product accounts stay on the list without consent.

```
// ✓ Good - the charter above: cadence from counted supply, named owner and backup,
// organisation-held accounts, written curation rule, clicks and replies as signals,
// pre-agreed pause and sunset triggers
```
