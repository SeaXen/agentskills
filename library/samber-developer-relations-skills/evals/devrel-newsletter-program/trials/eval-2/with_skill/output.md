**Next action (today, 10 min):** Ask Dario for a full list export, plus transfer of the sending tool account and the DNS records. His card is the single point of failure for every send.

## Direct answer

Relaunch, but not next week and not as briefed.

- **Timing:** Earliest send is Tue 2026-11-03, target Tue 2026-11-10. Writing is not the blocker. The blockers are owner, accounts and consent.
- **Cadence:** Monthly, not biweekly. Supply does not fill biweekly.
- **Design:** No full redesign. Use a fixed 5-section template. Redesign after issue 3 if clicks justify it.
- **"We're back" issue:** Yes, as a normal-length issue. It is the first issue and also the pause announcement. It carries the 3-month backlog.
- **Target:** Drop 50% opens. Opens are inflated by mail-privacy pre-fetch, so report them as directional only. The target is clicks per delivered email.
- **List:** Mail about 10,670 people, not 14,000. About 3,330 imported EU/UK addresses have no lawful basis (see Consent).

## Gate result: keep, monthly. Two of three conditions unproven.

Consent was classified first. All numbers below use the lawful segment.

1. **Supply: holds at monthly, fails at biweekly.**
   - Own items in 3 months: 12 (6 releases, 3 posts, 3 call recordings), about 4/month.
   - Time-bound rate: about 3/month (about 2 releases + 1 call).
   - External evergreen: 15 forum answers, about 5/month.
   - Biweekly needs 10-14 items/month. The best case is about 9, and that burns the reserve.
   - Monthly fills the time-bound sections from the rate.
   - Reserve at restart: after the restart issue uses 1 post, 1 recording and 3 answers, left over are 2 posts, 2 recordings and 12 answers. That covers issues 2 and 3.
2. **Owner and backup: blocked.** No named people, no hours. Owner of the answer: head of marketing. Re-check Wed 2026-10-28.
3. **Readers want email: unproven.**
   - Evidence: 9,000 opted in via checkbox, and a few replies per issue.
   - The 1.1% clicks is blended across all 14,000. The imported segment likely drags it down.
   - The checkbox segment's own rate is unknown.
   - Test: the restart issue. House-rule threshold: clicks per delivered, bot-filtered, on the lawful segment, at or above the pre-pause baseline recomputed for that segment. Below it, re-run the gate and fall back to feed only or pause.
   - Feed-only fallback needs a public changelog with a feed. Confirm one exists.

## Shape

Own-surface digest, monthly, with a community section.

- **Ranking, most efficient first:** feed only > own-surface digest > curated ecosystem > community-edited > personal letter.
- **Recommended:** own-surface digest. Readers click and reply, so curation adds value over a bare feed.
- **Deleted:**
  - Personal letter: Dario left.
  - Curated ecosystem: no backup yet, and thin supply.
- **Not now:** community-edited. 15 forum answers in 3 months (about 5/month) is too small a base. Revisit when answers or submissions run weekly.
- **Promotion rule:** add an external news section only after 3 digests that each carried a trial external item that drew clicks.

## Cadence and rhythm anchor

- Monthly, the Tuesday after the monthly community call, so the recording lands in the same issue.
- Call date is an open question. If it is irregular, fix a calendar day and cover everything shipped since the last issue.
- Slow down after 2 consecutive thin issues. Speed up only after 3 consecutive full ones. Never raise cadence to fix engagement.

## Curation rule (house rule, no published industry ratio)

- At least 2 external items per issue, about 1 external for every 2-3 own. Community forum answers count as external.
- **Include:** anything a reader can use this month, with a usage example.
- **Exclude:** gated content, announcements with no usage example, named-competitor comparisons, unannounced features, named customers. Confirm the full off-limits list. Question 9 is open.
- Paid or partner items: none for now. If added later, label "sponsored", apply the same criteria, and cap at 1 per issue.

## Section template

| Section | Source | Owner | Items | When empty |
|---|---|---|---|---|
| Shipped this month | release notes | owner (backup B.) | 2-4 | merge into "Try this" |
| From the community call | recording | owner | 1 | drop |
| Built and answered by the community | forum | backup | 2-3 | drop |
| Read | blog | owner | 1 | evergreen docs walkthrough |
| Try this | docs | backup | 1 | evergreen tip from docs backlog |

- Each issue gets a public archive URL. The archive outlives the list.
- **Restart issue contents:** all 6 releases as a brief list (top 2-3 expanded), 1 call recording, 3 forum answers, 1 post, 1 docs tip.
- **Opening note:** what changed. Monthly, who writes it, one-click unsubscribe.

## Ownership and handoff

- **Owner, backup, reviewer** (engineer, 30 min per issue): all unnamed. Hours per issue unknown. Blocked, see Open questions.
- **Backup** assembles one issue per quarter to stay practised.
- **Handoff checklist, Dario to company, before any send:**
  1. Sending tool account moves to a company login and company card.
  2. Full list export, with signup source, date and region per address.
  3. Sending-subdomain DNS records move to company-controlled DNS.
  4. Templates, archive and tool credentials move to a company password vault.
  5. Runbook written next to the release process. It covers template, send day, checklist, account owners and curation rule.
- **Running cost:** platform tier, domain, editor hours. Name the budget line. No budget line means no restart.
- **Deliverability:** the subdomain has been silent for 11 weeks. Whoever owns DNS should verify its auth records after the move. That is outside this charter.

## Consent (send to whoever owns privacy; not legal advice)

- **Checkbox, 9,000:** likely fine. Verify it was unticked by default, separate from terms, and worded as a newsletter. Note double opt-in if present.
- **Imported, 5,000:** about 1,667 each in the EU, UK and US.
  - **EU and UK, about 3,330:** no basis. The form offered no opt-out at collection, so soft opt-in fails. Suppress. Do not delete the records.
  - **US, about 1,670:** keep only if the privacy owner confirms. It needs a working one-click opt-out honoured within 10 business days, a postal address and honest headers.
  - **Region check:** personal gmail-type addresses carry no country. If region cannot be reliably tied to each address, suppress all 5,000.
- **Re-invite once** through the product, such as a settings checkbox or in-app prompt. Do not use email.
- **Past sends:** Dario may already have mailed the imported segment. Flag that to the privacy owner.
- **Stream separation:** the newsletter stays out of billing, security and account email.
- **Standing inactive rule (house rule):** no human click or reply in 12 months, after bot-click filtering, gets one re-confirmation, then suppression. Run it once 12 months of filtered click data exist.

## Measurement

- **Primary:**
  - Clicks per delivered email, with the platform's bot-click filter on. Name the filter used.
  - Unique clickers across the last 3 issues.
  - Unsubscribes and complaints.
  - Replies.
- **Outcome signal:** assumed funding goal is retention of existing SDK users. Signal: upgrades to the latest SDK version from UTM-tagged issue links. Confirm the goal (question 2).
- **Opens and click-to-open:** directional only. Never a target.
- **Baseline:** the pre-pause blended 44% opens and 1.1% clicks, recomputed on the retained segment. Thresholds set from it are house rules.
- **Context, not targets:** software-sender median click rate sits near 1.15% per send.
- Review quarterly against the list's own trend.

## Pause and sunset rules

| Trigger | Action |
|---|---|
| Owner leaves and backup cannot take over within one cycle | One-line hiatus note, then hand over or downgrade to feed only |
| Two consecutive thin issues (a section needed padding) | Slow to the next cadence or merge into the changelog |
| Clicks and replies fall 2 consecutive quarters against own trend | Re-run the gate |
| A forum, chat or feed now does the job | Final issue pointing to the replacement |
| Running cost has no budget line | Close or downgrade before anyone pays personally |
| List silent more than 6 months | Re-permission issue, then suppress non-responders |

Announce every pause. Never skip silently.

## Relaunch timeline (today is Fri 2026-10-23)

1. **Today, 10 min:** ask Dario for export and account transfer.
2. **By Wed 10-28 (go/no-go):** owner and backup named with hours, budget line named, tool and DNS access confirmed, privacy owner briefed.
3. **10-29 to 11-02:** build the restart issue in the template, reviewer pass, segment lists.
4. **Tue 11-03 earliest, Tue 11-10 target:** send to the lawful segment.
5. **2 weeks after send:** read clicks per delivered against baseline, then decide issue 2.

Any item in step 2 still open on 10-28 pushes the send to 11-10 or later.

## Open questions (blocked facts)

- Owner, backup and hours per issue, and who reviews. Owner of the answer: head of marketing. Re-check 10-28.
- Who holds the sending tool, list export and DNS now? Dario's cooperation is unconfirmed.
- Per-segment clicks, unsubscribes and replies for the last 6 issues. Needs tool access. Re-check 10-28.
- Funding goal: retention assumed. Confirm.
- Off-limits list, and whether legal reviews every send.
- Community call date, to set the send day.
- Checkbox wording and how region was recorded for imports. Owner: privacy owner.
- Does a public changelog with a feed exist? It is the fallback.

## Pass-threshold result

- **Pass:** cadence derived from rate with reserve covering 2 issues, curation rule, template with empty rules, no open-based primary metric, pause table with actions, consent provenance stated.
- **Blocked:** named owner and backup, organisation-held accounts, outcome signal confirmation. Each has an owner and a 10-28 re-check.
- **Changed from the brief:** biweekly to monthly, 50% opens to clicks per delivered, redesign deferred, 14,000 to about 10,670 recipients.

**Next:** send Dario the export and transfer request.