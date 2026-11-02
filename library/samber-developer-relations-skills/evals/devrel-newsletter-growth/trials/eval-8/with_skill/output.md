# Fernhollow developer digest: why unsubscribes doubled, and what to do

## Answer

**The signup box makes a promise the newsletter doesn't keep.** Your docs box says "Weekly Go performance tips from our engineers." What arrives is a monthly product-update email. Readers who sign up for performance tips get a product digest, so they leave within one to three issues. That matches your export.

**Don't go weekly to "stay top of mind."** A weekly send of the same product-update content gives disappointed subscribers four chances a month to unsubscribe instead of one. It also doesn't deliver what the box promises, which is Go performance tips. Cadence and format are the newsletter programme's call, so I'm not settling them here. What the growth side can do is stop the mismatch from creating subscribers who leave.

I'm confident about the mismatch and the early-churn pattern. I haven't seen your numbers, so the "doubled over six months" timing is unexplained (see Churn reading).

## Refusals applied

- **Weekly resend to "stay top of mind" (trust).** It isn't in the refusal table. It fails the same way, because the promise and the content still disagree. Replacement: fix the contract first, then let the programme owner decide cadence.
- **No imports, bought lists or re-permission emails are in play.** If anyone suggests emailing the 7,800 to ask if they want to stay, don't. In the UK and EU that email is itself marketing. Use the opt-out and the in-product invite instead.

## Growth gate

| Condition | Status | Evidence / first task |
|---|---|---|
| Programme holds | **Unproven** | I don't know whether a charter, an owner and a backup exist, or whether the last three issues went out on cadence. The monthly-since-last-year switch suggests nobody decided it deliberately. First task: write the charter. Route to `devrel-newsletter-program`. |
| Consent is known | **Unproven, with a flag** | I don't know where the 7,800 came from. If most came through the docs box, the consent text they saw was "weekly Go performance tips." Consent to one stated purpose may not cover a different product-update stream. First task: pull the consent record (timestamp, form version, text shown) and ask whoever owns privacy whether the current content is covered. EU, UK and German readers are the exposed segment. |
| Sources can be told apart | **Probably fails** | If the docs box is the only form, everything is tagged `docs` or nothing. First task: add a source field to every form. |

No new channel opens until these pass. Adding traffic to a form that over-promises just adds more early unsubscribes.

## Churn reading

Run this on your export before anything else. It takes about an hour.

1. **Tenure.** What share of unsubscribes happened within three issues of signup? You say "most." Put a number on it. This is the early-churn baseline.
2. **Source.** Split by form or source. If everything is the docs box, that's expected. If one source stands out (a webinar, a launch, an import), that's a second problem to chase separately.
3. **Issue.** Do unsubscribes spike on particular issues, such as a launch-heavy one, or run flat? A spike means one issue's content. Flat means the contract.
4. **Complaints alongside unsubscribes.** Pull spam complaints per send. Rising complaints with flat unsubscribes means people can't find the unsubscribe link or don't remember subscribing.
5. **The six-month window.** The mismatch has existed for about a year, but unsubscribes only doubled recently. Something changed about six months ago. Check each of these:
   - Did docs traffic or the signup box's placement change, so more mismatched readers reached it?
   - Did a campaign, import or event feed the list?
   - Did Gmail or Yahoo one-click unsubscribe, or a subscription manager, launch inside the window? That shifts complaints into unsubscribes and looks like a content problem.
   - Did the issues themselves change in length, sponsor or format?

   If the cause turns out to be a new source or an inbox-provider feature, the weekly-vs-monthly question matters less.

## Fix the signup contract first

Rewrite the box to match what you actually send:

```
Monthly, from the Fernhollow team: releases, deprecations with dates,
one deep dive. Read the latest issue first. Privacy notice.
```

Checklist for every form:

- **Promise:** says what arrives, how often (monthly), who sends it, and links the latest issue and the privacy notice. Never write a cadence the charter doesn't hold.
- **Choice:** a separate, unticked box, never a condition of anything.
- **Confirmation:** double opt-in on the public docs form, because you can't exclude German readers or bots. The confirmation email is one sentence and a button, nothing else.
- **Guard:** honeypot field and a per-IP rate limit.
- **Record:** timestamp, source tag, form version, the consent text shown, and the confirmation click.
- **Welcome:** the latest issue (or best of the archive) and how to unsubscribe.
- **Suppression list:** unsubscribed addresses stay on it so no later import re-adds them.
- **Unsubscribe:** one click, no login, no required field. Add an optional reason field after it completes.

**Decision for you and the programme owner:** if the team wants to be the "Go performance tips" newsletter, change the programme to deliver that, and then the promise is true. If the team wants to be the product digest, keep monthly product updates and make the promise honest. Either way the box and the content must agree before traffic grows. Don't change the box to match a cadence you haven't committed to.

## What to tell the CEO

- The unsubscribe export shows most leavers were gone within three issues. That points at the promise, not at being forgotten.
- Weekly sending can't fix that. It multiplies the exposure of subscribers who already feel misled.
- "Top of mind" is a reach goal. Reach comes from confirmed, engaged subscribers, which is why the metrics below count those and not list size.
- The fix costs about an hour for the copy and a few hours to set up tagging and the record. After two issues you can compare early churn against today's baseline.
- If the CEO still wants weekly, route it to the programme decision with the charter and issue capacity on the table. Test it as an explicit, labelled change to the promise, not as a silent one.

## Channels

Held until the gate passes. After that the default is the cheap, no-consent-risk set:

| Channel | Owner | Surface | Source tag | Date | Done when |
|---|---|---|---|---|---|
| Owned surfaces | you | quickstart end, changelog footer, docs footer, README | `docs-quickstart-end`, `changelog-footer`, `docs-footer`, `readme-line` | within 2 weeks of the gate passing | forms live with tags and the corrected promise |
| Archive and share line | newsletter owner | public issue pages | `archive-issue-page` | same window | past issues public, subscribe form above the fold |

Re-rank once you know your hours per month, any hard date, and who the new readers should be. Item pitches to curated newsletters come next, with talk end cards after that. A referral programme, paid acquisition and swaps are deleted for now. They need more effort and compliance work than a list fixing its promise should carry.

## Metric sheet

Baselines come from your own export. Every target is a house rule.

- **Early churn:** share of a cohort gone within three issues. Today's number is the baseline.
- **Net confirmed growth** per source.
- **Confirmation rate** per form.
- **First-issue click:** human clicks only, after bot filtering.
- **Activation:** human click in the first four issues.
- **Unsubscribes and complaints per send.**
- **One outcome signal:** for example product signups from newsletter links.

Don't report gross list size (7,800), form submissions or open rate as growth. Opens are inflated by mail-privacy features. Don't rank a source on fewer than about 30 confirmed signups.

## Open questions

| Question | Owner | Re-check |
|---|---|---|
| What share of unsubscribes fall within three issues, by source? | you | this week |
| Is there a charter, owner and backup, and did the last three issues go out on time? | newsletter owner | this week |
| Where did the 7,800 come from, and do EU, UK or German readers signed up under "weekly Go performance tips" need the current content covered? | privacy owner | before any new channel opens |
| What changed about six months ago (traffic, placement, import, one-click unsubscribe, issue format)? | you | this week |
| Does the team want to deliver Go performance content, or stay a product digest? | newsletter owner and CEO | after the churn reading |

## Pass-threshold result

- **Refusals checked:** passed.
- **Gate with evidence:** **blocked.** I need your charter, consent record and form-source data. Re-check next week.
- **Signup contract:** passed in draft, once you pick the content direction.
- **Channel rows with owner, tag, date and done-when:** passed. Deleted rows are named above.
- **Churn reading split by tenure, source and issue, with complaints:** **blocked** on your export numbers. Re-check next week.
- **Metrics per source and confirmed:** passed.