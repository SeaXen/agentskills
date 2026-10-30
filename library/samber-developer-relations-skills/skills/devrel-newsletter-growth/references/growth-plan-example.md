# Worked growth plan and a negative example

Read this before presenting a plan, to match the output shape. Names are fictional.

## Contents

1. Input
2. Plan
3. Negative example
4. Failure modes

## 1. Input

Quarrystone ships a message-queue SDK. Its monthly developer newsletter has 1,800 subscribers after two years. Owner: Ines (DevRel), backup: Tomasz, both named in a charter; the last three issues went out on time. The list came from a docs footer form (double opt-in) plus 900 addresses imported from a conference Quarrystone sponsored. Ines has six hours a month and no paid budget. She wants 3,000 by the v5 launch in four months, and suggests "adding a signup prompt to the CLI and importing our 9,000 trial accounts".

## 2. Plan

**Answer:** no per-source baseline exists yet, so 3,000 by the launch is a wish, not a forecast. The plan fixes consent and tagging first, opens the four highest-yield channels within six hours, and sets the target after two months of tagged data. The CLI prompt and the trial import are refused.

**Refusals applied:**
- CLI signup prompt (trust): developers read install and run output as theirs. Replacement: one line in `quarry --help` and a `quarry links` subcommand.
- Import of 9,000 trial accounts (house rule): account signup is not newsletter consent, and the import would bury the per-source numbers. Replacement: one in-product invite with an unticked box on the dashboard's settings page.
- The 900 conference imports, already done (law, for the EU and UK addresses among them): reversal task. Suppress the segment. No "do you want to stay?" email: asking for consent by email is itself marketing. Those who are product users see the in-product invite.

**Gate result:**
- Programme holds: pass (charter, owner and backup, three on-time issues).
- Consent known: fail for the 900, fixed by the reversal above.
- Sources distinguishable: fail. The form carries no source field. Add one before any channel opens.

**Churn reading:** unsubscribes per send sit near the list's own average except in the two issues after the conference import, when they tripled and complaints rose. Cause: the imported segment, not the content.

**Signup contract:** promise rewritten from "Weekly tips" to "Monthly: releases, deprecations with dates, one deep dive", with links to the latest issue and the privacy notice; double opt-in kept (public form, German readers); honeypot and rate limit added; record adds source tag and form version; the 900 go on the suppression list.

**Ranked channels** (efficiency order). Month 1 spends most of the six hours setting up rows 1 and 2; after that the rows below cost a few hours a month, which leaves room for unpaid recommendations. Deleted: unpaid recommendations, because Quarrystone's sending platform has no recommendation feature; republishing, an hour every issue that the remaining hours cannot carry next to the launch; swaps and the referral programme, which need more coordination than six hours allow; paid acquisition, because there is no budget.

| Channel | Owner | Surface | Source tag | Date | Done when |
|---|---|---|---|---|---|
| Owned surfaces | Ines | quickstart end, changelog footer, docs footer, README | `docs-quickstart-end`, `changelog-footer`, `docs-footer`, `readme-line` | month 1 | four forms live with tags |
| Archive and share line | Tomasz | issue pages, share line | `archive-issue-page` | month 1 | every past issue public |
| Item pitch for v5 | Ines | two curated newsletters in the SDK's language | `pitch-<curator>-v5` | launch week | the v5 post ends with a tagged signup line; two pitches sent |
| Talk end card | Ines | the one talk booked in month 3 | `talk-<event>-card` | month 3 | slide and links page live |

The v5 launch date fixed the pitch to launch week.

**Metric sheet:** net confirmed growth per source, confirmation rate per form, first-issue click, activation (human click in the first four issues), early churn (gone within three issues), unsubscribes and complaints per send, and product signups from newsletter links. Baseline: the next two months. Every target labelled a house rule.

**Open questions:** how many of the 900 have EU or UK addresses (privacy owner); whether the curators accept the v5 post as an item.

## 3. Negative example

```
✗ "Great goal! Here's how to hit 3,000:
1. Import your 9,000 trial users - instant 5x.
2. Add a friendly 'Subscribe for tips!' after every CLI command.
3. Launch a referral programme with swag tiers (3 referrals = stickers).
4. Gate the v5 migration guide behind an email form.
5. Track open rate weekly; aim for 40%."
```

What is wrong:
- The import and the CLI prompt sit in the refusal table: one breaks the consented stream, the other burns trust.
- A referral programme on a 1,800 list with six hours a month does not fit the ceiling, and swag tiers are a consumer mechanic.
- A gated migration guide blocks existing users from upgrading and gets refused by curators.
- Open rate is inflated by mail-privacy features; the target is meaningless.
- No gate, no source tags, no deletions named, no churn reading, and the 900 imports left in place.

## 4. Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| List jumps, then complaints and early churn follow | Imported accounts or attendees | Suppress the imported segment; invite product users once in the product, never by email |
| "Growth" reported, clicks flat | Gross size or submissions counted | Report confirmed, activated subscribers per source |
| A paid source dominates signups but not clicks | Screening looser than organic | Raise screening to organic first-month behaviour, or stop |
| Pitches land, no subscribers follow | The linked page has no tagged signup line | Add the line to every page you pitch |
| Swap subscribers leave within weeks | No overlap check | Check overlap before agreeing; test one swap before repeating |
