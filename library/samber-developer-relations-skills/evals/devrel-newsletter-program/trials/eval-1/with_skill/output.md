**Answer: don't go weekly. Weekly fails the supply gate and the backup gate. Keep monthly, fix the three gaps below, and re-test cadence after three full issues.**

Next action: name Tomasz's backup and pull click, unsubscribe and reply numbers for the last 6 issues. Both are due 2026-11-06.

## Why weekly fails

- Supply: last quarter you shipped 4 releases, 2 posts and 1 webinar. That is 7 own items, about 2.3 per month.
- A weekly issue with 5 items needs about 21 items per month. That is roughly 9x current supply.
- Even monthly is thin. 2.3 time-bound items per month does not fill a 5-item issue. The evergreen reserve and a trial external section have to cover the rest.
- Owner hours: 3h per weekly issue is about 13h per month, all on one person. Monthly costs 3h.
- No backup exists. Nobody else has touched the newsletter.
- Open rate (38% to 29%) cannot justify the change. Opens are inflated by mail-privacy pre-fetching, so the number is directional only. The skill's rule applies: never raise cadence to fix engagement. Weekly padding usually lowers clicks and raises unsubscribes.
- Rates elsewhere in the field: vendor newsletters (Stripe, Supabase, GitHub Insider) run monthly or twice monthly. Weekly newsletters are community or paid-curator teams.

Tell the CMO: "top of mind" depends on each issue being worth opening. Padding makes issues worse.

## Charter

### 1. Gate result

| Condition | Status | Evidence |
|---|---|---|
| Supply fills the sections at the cadence | Weekly: fails. Monthly: holds only with a trial external section plus evergreen reserve | 2.3 own time-bound items per month |
| Named owner and backup, with hours | Owner holds. Backup **blocked** | Tomasz, 3h per issue. Backup unnamed |
| Readers want email over a feed | **Unproven** | No click data yet. Opens are not evidence |

Result: keep, monthly. Weekly is rejected.

Test for the demand condition: clicks per delivered email across the next 2 issues stay at or above the average of the last 6 issues. This is a house rule. If it fails, move to feed only. That requires a public changelog with a feed; if you have none, build it first (changelog-writing skill).

### 2. Shape

Ranking, most efficient first: feed only, own-surface digest, curated ecosystem, community-edited, personal letter.

- Recommended: own-surface digest, monthly, with one trial external section.
- Deleted: curated ecosystem and personal letter. No backup exists, and either shape depends on one person's judgment.
- Deleted for now: community-edited. I have no evidence of a contributor base. Re-open it if one exists.
- Fallback: feed only, if the demand test fails.
- Promotion path: move to curated ecosystem only after 3 monthly digests, each with one trial external section whose items drew clicks, and after a backup exists.

### 3. Cadence and rhythm anchor

- Monthly, sent on a fixed day, the first Tuesday after the month's last release.
- If releases are irregular, cover everything shipped since the last issue.
- Slow down after 2 consecutive thin issues.
- Speed up only after 3 consecutive full issues. A full issue has every section filled without padding.
- The first candidate step up is twice monthly, not weekly.

### 4. Curation rule (house rule, no industry ratio exists)

- Target: at least 2 external items per issue, about 1 external for every 2-3 own items.
- Include: anything a reader can use this month.
- Exclude: gated content, announcements with no usage example, named-competitor comparisons, unannounced features, named customers. Confirm the off-limits list with the CMO; it is still an open question.
- Paid or partner items: not accepted unless labelled "sponsored", held to the same criteria, and capped at 1 per issue.

### 5. Section template

| Section | Source | Owner | Items | When empty |
|---|---|---|---|---|
| Shipped | release notes | Tomasz (backup TBD) | 1-3 | merge into "In brief" |
| From our blog and events | posts, webinar recording | Tomasz | 0-2 | drop |
| Elsewhere in the ecosystem | external links | Tomasz | 2-3 | drop |
| One thing to try | docs or tutorial | Tomasz | 1 | run a named evergreen slot |
| In brief | small changes, docs updates | Tomasz | 2-4 | drop |

- Keep a public archive URL per issue. Put the archive on a company domain.
- Seed an evergreen reserve of at least 2 issues' worth of items before the next send.

### 6. Ownership and handoff

- Owner: Tomasz, 3h per issue.
- Backup: **blocked**. Name one person who agrees. They assemble one issue per quarter so they stay practised.
- Reviewer: one engineer or product person, 30 minutes per issue, to be named.
- Sending account, list export, domain and archive: held by the organisation, not a personal account or card.
- Runbook: send day, template, checklist, account owners, curation rule. Store it next to the release process.
- Running cost: platform tier plus 3h of editor time. Name the budget line.

### 7. Measurement

- Primary signals: clicks per delivered email, unique clickers across the last 3 issues, unsubscribes, complaints, replies.
- Apply the platform's bot-click filter and report which one you used.
- Report open rate and click-to-open as directional only, never as a target.
- Outcome signal, provisional: feature adoption from newsletter links (a retention goal). Confirm with the CMO why the newsletter is funded; if the goal is reach, use signups from non-users instead.
- Review quarterly against the list's own trend. Set the baseline from the last 6 issues.

### 8. Pause and sunset rules

| Trigger | Action |
|---|---|
| Tomasz leaves or is out and the backup cannot cover within one cycle | Send a hiatus note, then hand over with the checklist or downgrade to feed only |
| 2 consecutive thin issues (2 or more sections dropped or padded) | Slow cadence or merge into the changelog |
| Clicks and replies fall for 2 consecutive quarters against your own trend | Re-run the gate |
| A forum, chat or feed now does the job | Close with a final issue pointing to it |
| Running cost has no budget line | Close or downgrade |
| List silent more than 6 months | Re-permission issue, then suppress non-responders |

Announce every pause. Never skip an issue silently.

### 9. Consent and inactive subscribers

- **Blocked:** I don't know how the 6,200 addresses were collected, or when. Owner: whoever holds the list (probably marketing ops) and privacy.
- Classify consent before judging any metric. Product signups added without consent need a lawful basis by region. UK and EU individuals need consent or a valid soft opt-in. US needs a working opt-out and a postal address.
- Suppress only the segment with no basis, and invite it once through the product. Keep the newsletter out of transactional email.
- Inactive rule (house rule): no human click and no reply in 12 months, after bot filtering, means one re-confirmation, then suppression.
- A stale or partly non-consented list is a likely cause of the open-rate slide. Check that before blaming content.

## Open questions and re-checks

| # | Question | Owner | Re-check |
|---|---|---|---|
| 1 | Backup name and agreement | devrel lead | 2026-11-06 |
| 2 | Clicks, unsubscribes, replies for last 6 issues | Tomasz | 2026-11-06 |
| 3 | List consent provenance, collection date, last-send date | list owner and privacy | 2026-11-06 |
| 4 | Why funded (retention, reach, contributors or credibility) | CMO | 2026-11-06 |
| 5 | Effort ceiling in hours per month, plus off-limits list | CMO and devrel lead | 2026-11-06 |
| 6 | Does a public changelog with a feed exist? | Tomasz | 2026-11-06 |

## Pass-threshold result

| Threshold | Result |
|---|---|
| Gate states 3 conditions with evidence | Pass (1 unproven) |
| Cadence derived from rate and hours, evergreen reserve covers 2 issues | Pass in design; reserve must be built before the send |
| Curation rule: share plus criteria, labelled house rule | Pass |
| Template sections have source, owner, range, empty rule | Pass |
| Owner and backup named, accounts held by the organisation | **Fail:** backup blocked (#1) |
| No open-derived primary metric, one outcome signal | Pass (signal provisional, #4) |
| Pause and sunset triggers have thresholds and actions | Pass |
| Consent provenance stated, transactional email separate | **Blocked** (#3) |

## For the CMO conversation

1. Weekly needs about 9x today's own output and 4x Tomasz's monthly hours, with no backup.
2. A weekly plan with this supply gets padded within a month.
3. The 29% open rate is a weak signal until we see clicks and clean the list.
4. The plan is monthly now, with a defined path to twice monthly after 3 full issues.

I haven't checked your list or sending platform. All numbers above come from your message.