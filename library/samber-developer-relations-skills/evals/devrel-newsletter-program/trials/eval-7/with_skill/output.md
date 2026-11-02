Ask for a backup at the Tuesday 2026-10-27 triage, and run feed-only until someone says yes. That takes 5 minutes. Two start gates are open, and the backup is the only one you can fix this week.

I couldn't run the interview one question at a time, so I carried the missing facts as named open questions at the end. I did not invent any numbers.

## Answer

Run a **monthly own-surface digest**, built so contributors can later become its editors. It is not live yet. Start feed-only now. Launch issue 1 on the first Tuesday after a backup agrees.

Weekly fails your own numbers. It is 12 hours a month with no backup, and it duplicates the Discussions thread. Monthly is 3 hours a month and adds something the thread doesn't: one curated page for people who don't read Discussions.

## Shapes, in efficiency order

1. Feed only
2. Own-surface digest
3. Curated ecosystem
4. Community-edited
5. Personal letter

- **Deleted: curated ecosystem and personal letter.** No backup deletes both. A compounding mandate cannot revive them.
- **Deferred: community-edited.** A 3-hour-a-month ceiling is under 4 hours, which deletes everything except feed-only and the monthly digest. But your Tuesday triage cycle and the contributor thread both favour it.
- **Promoted:** the compounding mandate raises community-edited. I resolve the tension by building the digest as a community-edited-ready template, with promotion triggers under Ownership.
- **Chosen: own-surface digest.** Feed-only is the fallback until the gate passes.

## 1. Gate result: not yet

| Condition | Result | Evidence or missing fact |
|---|---|---|
| Supply fills the sections at monthly, with 2 issues of evergreen reserve | **Unproven** | I have no 3-month counts. Your weekly thread suggests it holds. |
| Named owner and agreed backup, with hours | **Failed** | Owner is you at 3 hours per issue. No backup has agreed. |
| Readers want email over a feed | **Unproven** | There is no list yet. |

- **Supply test (15 minutes):** count the last 3 months by source. Time-bound items are releases, triage decisions, and event recaps. Evergreen items are docs walkthroughs and `help wanted` issues.
- **Passing line:** at least 5 time-bound items a month, plus 4 to 6 evergreen items in reserve.
- **Demand test.** House rule, edit freely: pin a signup link for 6 weeks. The condition holds at 100 confirmed subscribers and 3 or more replies or forwards to issue 1.
- **Next action for the failed condition:** feed-only. Use GitHub Releases or `CHANGELOG.md` plus its Atom feed, with the weekly thread as the pointer. If no changelog exists, build one first.

## 2. Shape

Own-surface digest, monthly.

- **Contributor items count as external.** The skill counts anything community members wrote as external, even on your own Discussions. Your weekly thread is therefore mostly external supply.
- **Promotion trigger.** Move to community-edited when all three hold:
  - a backup has agreed;
  - at least 2 contributors volunteer as section editors;
  - three consecutive issues have been full.
- **Curated trial.** After three digests that each carried one trial external-link section whose items drew clicks, consider curated ecosystem. It needs a backup first.

## 3. Cadence and rhythm anchor

- **Monthly.** Send the Wednesday after the first Tuesday triage of each month.
- **Supply.** The month's weekly threads and the triage notes supply it.
- **Slow down** to every two months after 2 consecutive thin issues. Speed up only after 3 consecutive full ones.
- **Never raise cadence to fix engagement.**
- **Budget per issue, 3 hours:**
  - 0.5 h collect
  - 1.5 h write
  - 0.5 h review
  - 0.5 h send and archive

## 4. Curation rule (house rule)

- **Share:** at least one third of items come from contributors, with author credit. No industry ratio exists, so this is your choice.
- **Include:** anything a reader can use this month.
- **Exclude:**
  - gated content
  - announcements with no usage example
  - named-competitor comparisons
- **Default exclusions, pending your Q9 answer:**
  - unreleased security fixes and embargoed CVEs
  - named adopters without their permission
  - unannounced features
- **Sponsored or partner items:** none until you decide. If you accept them later, each needs a "sponsored" label, the same criteria as editorial items, and a cap of one per issue.

## 5. Section template

| Section | Source | Owner | Items | When empty |
|---|---|---|---|---|
| Shipped this month | releases and changelog | you (backup TBD) | 3-5 | merge into "In brief" |
| Merged by the community | weekly threads | you (backup TBD) | 3-5, with credit | merge into "In brief" |
| Decided in triage | triage notes | you (backup TBD) | 1-3 | drop |
| Help wanted | `good first issue` and `help wanted` labels | you (backup TBD) | 2-3 | evergreen "how to contribute" slot |
| One thing to try | docs backlog | you (backup TBD) | 1 | evergreen docs tip |
| In brief | leftovers and events | you (backup TBD) | 0-3 | drop |

- **Archive:** every issue gets a public URL on the project site. The public archive is the compounding asset, and it outlives the list.
- **Never pad.**

## 6. Ownership and handoff

- **Owner:** you. **Backup:** blocked. The fact missing is a person's agreement. You hold it. The re-check is **2026-11-03**.
- **Reviewer:** one maintainer, 30 minutes per issue. Not yet named.
- **Backup practice:** the backup assembles one issue per quarter to stay practised.
- **Accounts:** the sending platform, list export, domain, and archive belong to the Larkspur organisation. Never use a personal account or card.
- **Runbook:** keep it in the repo, with the template, the send day, the checklist, the account owners, and the curation rule.
- **Running cost:** sending-platform tier, domain, and editor hours. The budget line is an open question.

## 7. Measurement

- **Primary signals:**
  - clicks per delivered email
  - unique clickers across the last 3 issues
  - unsubscribes and complaints
  - replies
- **Machine clicks:** enable the platform's bot-click filter and report which filter you used.
- **Opens:** directional only, never a target.
- **Outcome signal:** contributor submissions per issue. Fallback: first-time-contributor PRs that start from a "Help wanted" link.
- **Baseline:** none exists, so issues 1 to 3 set it. Label every threshold a house rule. Review quarterly.

## 8. Pause and sunset rules

| Trigger | Action |
|---|---|
| Owner leaves and the backup can't take over within one cycle | Send a hiatus note, then hand over or downgrade to feed-only |
| 2 consecutive thin issues (padding needed or a time-bound section empty) | Go bimonthly, or merge into the changelog |
| Clicks and replies fall 2 consecutive quarters against your own trend | Re-run the gate |
| Discussions or a feed now does the job | Send a final issue pointing to it |
| Running cost has no budget line | Close or downgrade before you pay personally |
| List silent for 6 months | Send a re-permission issue, then suppress non-responders |

- **Announce every pause.** Never skip an issue silently.
- **Inactive rule (house rule):** no human click and no reply in 12 months, after bot filtering, gets one re-confirmation, then suppression.

## Consent

- **New list, no import.** Never pull contributor emails from commits or GitHub profiles.
- **Signup:** its own form, with double opt-in to evidence consent.
- **Streams:** keep the newsletter apart from GitHub notifications and any account email.
- **Postal address:** US rules need one in the footer, plus a working one-click opt-out.
- **Rules by region:** UK and EU individuals need explicit consent. Send privacy questions to your privacy owner.

## Open questions

1. **Backup:** who, and by when? Blocked, re-check 2026-11-03.
2. **Primary reader:** contributors or Larkspur users? I assumed contributors and gave the outcome signal for that.
3. **Supply counts:** the 3-month counts by source.
4. **Triage notes:** are they public, and are any embargoed?
5. **Org entity and budget line:** which entity holds the accounts and pays, and what postal address goes in the footer?
6. **Off-limits:** confirm or change the default exclusions.

## Pass thresholds

| Threshold | Result |
|---|---|
| Gate states 3 conditions with evidence and a result | Pass |
| Cadence from rate and hours, with reserve | **Blocked** on supply counts |
| Curation rule, house-rule share, criteria | Pass |
| Template sections each have source, owner, range, empty rule | Pass |
| Named owner and backup, org-held accounts | **Blocked** on backup and org entity |
| No open-based primary metric, outcome signal matches funding | Pass |
| Pause and sunset triggers have thresholds and actions | Pass |
| Consent provenance stated, newsletter apart from transactional email | Pass, with the postal address blocked |

## Next

Do these in order:

1. **Mon 2026-10-26, 15 min:** do the 3-month supply count.
2. **Tue 2026-10-27, 5 min:** ask for a backup at triage.

After that, reply with the counts and the backup's name. I will re-run the gate and fill in the blocked rows.