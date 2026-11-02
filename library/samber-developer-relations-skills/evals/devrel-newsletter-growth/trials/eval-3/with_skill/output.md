# Copperwell newsletter referral programme: recommendation, tiers and launch email

**Don't launch the Morning Brew programme now.** Run a free test for three issues, then decide. Three facts rule it out today:
- The skill ranks a rewarded referral programme last of nine channels. It costs the most effort, so it loses to everything else at your hours.
- It's worth promoting only when readers already forward the issue, the content gets passed around at work, and someone owns fraud screening. You have none of the three.
- Your ceiling is 5 hours a month. The house rule is that below about 4 hours a month, nothing past talk end cards fits.

This isn't a legal or trust refusal. It's a deletion on effort and evidence. Morning Brew's "over 30% of subscribers" is a consumer business newsletter's figure. It's context, not a target for a 2,100-person developer list.

You still get the tiers and the launch email. The tiers below are the version that fits your constraints, held until the trigger fires. The email to send now is the share-line test.

## 1. Refusals applied

Nothing you've done or proposed is on the refusal table. Two parts of the Morning Brew mechanic need guardrails:

- **"Enter your friends' emails" invite forms** (law, UK/EU/Germany/Canada): this makes you send marketing to people who never consented. Refuse it. Each referred person must sign up through their own form with an unticked box. The referrer shares a link, never an address list.
- **Rewards on raw signups** (trust): they invite self-referral and alias addresses. Count confirmed, activated referrals only (see section 4).

## 2. Growth gate

Evidence is partial, so all three conditions are **unproven**. Proving them is task 1.

| Condition | Status | First task |
|---|---|---|
| Programme holds: named owner and backup, last 3 issues on time and full | Unproven. You gave cadence (monthly) but not owner, backup or the last three sends | Name the owner and backup. Confirm the last 3 issues went out on schedule |
| List consent known | Unproven. Source of the 2,100 is unknown | Classify each segment by collection source and region. Suppress any segment with no basis |
| Sources distinguishable | Unproven | Add a hidden source field to every form |

## 3. Channel ranking at 5 hours a month

The ranking is by confirmed, engaged subscribers per owner hour. Answers that moved rows:
- **Effort ceiling (5 h):** deletes the referral programme, republishing and swaps.
- **No paid budget:** deletes paid acquisition.
- **No talks known:** talk end cards stay in only if a talk is booked. Open question.

| Channel | Owner | Surface | Source tag | Date | Done when |
|---|---|---|---|---|---|
| Owned surfaces | you | quickstart end, changelog footer, docs footer, README | `docs-quickstart-end`, `changelog-footer`, `docs-footer`, `readme-line` | month 1 | four forms live, each tagged |
| Archive and share line | backup owner | public issue pages, one share line per issue | `archive-issue-page` | month 1 | every past issue public, share line in the next issue |
| Item pitch per real release | you | one or two curated observability or Go/infra newsletters | `pitch-<curator>-<release>` | next release | the linked page ends with a tagged signup line |
| Talk end card | you | next booked talk, if any | `talk-<event>-card` | when booked | slide plus a links page live |

Deleted, with reasons:
- **Referral programme:** effort and unproven forwarding.
- **Republishing:** an hour per issue is too much of the budget.
- **Swaps:** a week of coordination each.
- **Paid acquisition:** no budget.
- **Unpaid recommendations:** kept only if Copperwell's sending platform has a recommendation feature. Open question.

Rough month 1 budget:

| Task | Hours |
|---|---|
| Gate fixes (source field, consent classification) | 1.5 |
| Four owned-surface forms | 2 |
| Archive and share line | 1 |
| Pitch, if a release is due | 0.5 |

Later months drop to about 2 hours.

## 4. Referral tiers (conditional design)

Build this only after the trigger in section 6 fires. It's your 3, 5, 10 ladder, trimmed to fit 5 hours a month.

| Tier | Qualifying referrals | Reward | Control |
|---|---|---|---|
| 1 | 3 | Sticker pack | Auto-approved once the count is met |
| 2 | 5 | T-shirt | Manual check of the referral list |
| 3 | 10 | Hoodie | Manual check, **capped at a fixed stock (suggest 15)** |

**What counts as a qualifying referral** (house rule, so label it as one):
- The person used the referrer's link and signed up through their own form.
- They confirmed by double opt-in.
- They have a human click in their first issue, with bot clicks filtered.
- The address isn't a duplicate, alias or same-domain pattern of the referrer.

**Consequence of a monthly list:** the first-issue click can take up to a month. Rewards ship after the referral's first issue. Say that upfront, or referrers will think the programme is broken.

**Why the hoodie is capped:** with 2,100 subscribers, 10 activated referrals from one person is about 0.5% of the list, and fraud concentrates there. A stock cap also gives you a hard budget ceiling, since swag is your only budget.

**Plumbing, kept small:**
- One link per referrer, tagged `ref-<id>`, with source `referral`.
- A manual claim form for rewards. No automation tool at this size.
- A shipping address is personal data. Collect it only at claim time, say what it's for, delete it after shipping, and get the privacy owner to approve the notice. EU and UK delivery and customs terms are the privacy owner's call.
- Publish reward terms: what counts, the cap, "we may refuse fraudulent claims", and no cash value.

## 5. Signup contract (applies to every form, including referral links)

- **Promise:** "Monthly, from the Copperwell team: releases, breaking changes, one deep dive. Read the latest issue first. Privacy notice." Write the cadence you actually hold. Never write "weekly".
- **Choice:** a separate, unticked box.
- **Confirmation:** double opt-in on public forms. The confirmation email is one sentence plus the button.
- **Guard:** honeypot plus a per-IP rate limit.
- **Record:** timestamp, source tag, form version, the consent text shown, and the confirmation click.
- **Welcome:** the latest issue, and how to unsubscribe.
- **Suppression:** unsubscribed addresses stay on the list so they can't be re-added.

## 6. The test to run now, and the trigger

You said nobody has ever mentioned forwarding. Test that first, at no cost.

1. Add the **share line** below to the next three issues.
2. Add one question to the welcome email: "How did you find us? If a colleague forwarded it, tell us who or where." Replies count as evidence.
3. The share line links to the archive page tagged `archive-issue-page`, so forwards show up as tagged signups.

**Promote the referral programme only if all three hold at the re-check, on or about 2027-02-01:**
- Welcome-question replies or tagged archive signups show people forwarding at work.
- At least 30 confirmed signups have come through the share line or archive page. That's the house rule for ranking any source.
- Someone is named as fraud-screening owner.

If it fails, don't build the programme. Spend the hours on pitches and talk cards.

## 7. Emails

### 7a. Send now: share line for the next three issues

Place it one line near the end, with no reward and no urgency:

> Know someone who'd use this? Forward it, or send them the [archive](https://copperwell.example/newsletter/archive?source=archive-issue-page).

### 7b. Hold: referral launch email

Do not send until the trigger in section 6 fires. Subscribers only see it after they're already confirmed, so it's a normal issue block. It isn't a separate marketing blast.

**Subject:** Share the Copperwell newsletter, get swag

> Hi,
>
> A few of you have told us you forward this newsletter to colleagues. So we're adding a thank-you.
>
> **How it works**
> Your personal link is below. When someone signs up through it, confirms their email, and clicks through their first issue, that's one referral.
>
> - 3 referrals: Copperwell sticker pack
> - 5 referrals: Copperwell T-shirt
> - 10 referrals: Copperwell hoodie (limited stock, first come first served)
>
> **Good to know**
> - Referrals count after their first issue lands. The newsletter is monthly, so it can take up to a month.
> - They must sign up themselves with their own address. We don't send anything to addresses you enter for someone else, and we ask nobody to do so.
> - We only ask for a shipping address when you claim a reward. We use it to ship the swag and delete it afterwards. [Privacy notice]
> - We may decline claims that look like self-referrals or fake addresses. [Full terms]
>
> **Your link:** `{{referral_link}}`
>
> If you'd rather not take part, ignore this. Nothing changes in your subscription.
>
> The Copperwell team

Do not add a subscriber count, "exclusive", "don't miss out", or a countdown. Per the skill's rules, a count is allowed only if it's the confirmed, current count.

## 8. Metric sheet

Report per source tag. Never report gross list size, form submissions or open rate.

| Metric | Baseline | Target |
|---|---|---|
| Net confirmed growth per source | next 2 months | set from baseline, labelled house rule |
| Confirmation rate per form | next 2 months | same |
| First-issue click | next 2 months | same |
| Activation (human click in first 4 issues) | next 2 months | same |
| Early churn (gone within 3 issues) | next 2 months | same |
| Unsubscribes and complaints per send | last 6 issues | stay below your platform's complaint limit (Google asks for under 0.1%) |
| One outcome signal | next 2 months | choose with the charter, e.g. agent downloads from newsletter links |

If the programme runs later, compare referral cohorts with organic cohorts on activation and early churn. Pause it if referral churn or complaints run clearly above organic.

## 9. Pass-threshold result

| Threshold | Result |
|---|---|
| Moves checked against the refusal table | Pass |
| Gate with evidence | **Blocked.** All three conditions unproven |
| Forms meet the signup contract | Pass as designed |
| Rows kept have owner, tag, date, done-when; deleted rows named | Pass. Owner names are placeholders |
| Churn reading | **Blocked.** No unsubscribe, complaint or tenure data supplied |
| Metrics per source and confirmed | Pass |

## 10. Open questions

| Question | Owner | Re-check |
|---|---|---|
| Owner, backup and last 3 issues on time? | Marketing lead | before any channel opens |
| Where do the 2,100 subscribers live, and how were they collected? | You, then privacy owner | before any channel opens |
| Does your sending tool tag sources and filter bot clicks? | You | month 1 |
| Last 6 issues' unsubscribes and complaints, by tenure and source | You | month 1 |
| Does your sending platform have a recommendation feature? | You | month 1 |
| Any talks booked this quarter? | Marketing lead | month 1 |
| Who owns fraud screening and swag fulfilment? | Marketing lead | 2027-02-01 |
| Privacy-owner approval of the shipping-address notice and reward terms | Privacy owner | before section 7b ships |

I didn't run the one-question-at-a-time interview. I treated your brief as the answers and listed the gaps above.