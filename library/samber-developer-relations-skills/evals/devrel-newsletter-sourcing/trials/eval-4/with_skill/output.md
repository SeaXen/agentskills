# Candidate sheet: Brackwater July developer newsletter

**Result:** 2 items go in, 3 are held, and there is nothing to cut. I recommend a short issue with no padding.

I read the skill and both of its references. I could not open any pages. Every item came from your pasted list, so the link state is **user-supplied, not opened**. You gave PR numbers but no URLs.

## Header

| Field | Value |
|---|---|
| Window start | Not given. Open question below. |
| Window end | **2026-07-15 12:00 UTC**. I derived it from a 2026-07-16 send (12:00 the day before). It is an assumption. |
| Channels | "Pasted by user" (merged-PR list): 4 items. Every other channel was **not read**, which is not the same as zero. |
| Product Q4 roadmap | 1 item, requested by the PM. |
| Found / kept / held / cut | 5 / 2 / 3 / 0 |
| Own vs external | 2 own, 0 external (0%). Your charter's share is unknown. |
| Charter and last 3 issues | Not supplied. Duplicate and section verdicts are **provisional**. |
| Thin-issue call | **Ship shorter.** See the end. |

## Sheet

| # | Item | Primary link | Date | Rung | Verdict | Reason |
|---|---|---|---|---|---|---|
| 1 | Deprecate pg 13 images (#4455), removal 2026-10-01 | The release notes or deprecation notice for the 2026-07-05 release. **Not the PR.** URL needed. | 2026-07-05 | 1 action required | **keep** (first) | A deprecation with a removal date. The announcement date drives the window, so it is news now. |
| 2 | Free-tier connection limit raised from 20 to 60 (#4402) | The changelog entry or docs limits page for the 2026-07-01 release. URL needed. | 2026-07-01 | 1 action required | **keep** (second) | A limit change readers hit. Nobody has to act on it, but it ranks on rung 1 because readers hit it. It sits below #1 because #1 has a deadline. |
| 3 | Logical replication slots UI (#4471) | Release notes for the 2026-07-22 release, once they exist | 2026-07-03 (merged) | 2 new capability | **hold** | Public gate: merged but unreleased on the send date. Expires when the August window closes. |
| 4 | Fix auth bypass in connection pooler (#4480) | The public advisory page, only after 2026-07-24. **Never the PR or the fix commit.** | 2026-07-08 (merged) | 1 action required (probable) | **hold** | Public gate and your off-limits list. The advisory goes public 8 days after the send. Expires when the August window closes. |
| 5 | Q4 roadmap teaser: branching | The announcement page, once one exists | n/a | n/a | **hold** | Public gate: not announced, so it is off-limits. Expires when the announcement ships. |

## Why each call

**#1 and #2 are the issue.**
- Link the release notes, changelog or docs page, not the merged PR. The reader should land where the claim originates.
- Use the page's own title as the link text.
- Before sending, open both links and confirm the title, date and the 20→60 and 2026-10-01 figures.
- Without a URL I cannot confirm either item. If you can't supply them, they drop to hold. That is the **blocked** state: I am not guessing the URLs.

**#3 is a tempting early mention, but it ships after the send.**
- Writing "coming July 22" announces a feature that isn't released.
- Release dates slip, and a mention then promises something that doesn't exist.
- Source it for August from the 2026-07-22 release notes.

**#4 stays out of this issue in any form.**
- Don't mention it, hint at it, or write "security fix coming".
- A newsletter hint on 2026-07-16 starts the disclosure clock early.
- This sheet is itself sensitive. Keep it out of shared docs and the candidate log that other editors read. Record the item there as "embargoed item, see security team".
- If customers need to act before 2026-07-24, the security team's coordinated-disclosure notice to affected customers is the channel. The skill allows a standalone notice for action-required items, and the security team owns it.
- In August this is rung 1. Link the advisory page, not the fix.
- Open question for the security team: does the hosted fleet already carry the fix? If yes, what must readers do, and does that differ for self-hosted or client-side users?

**#5 isn't a candidate yet.**
- The PM's wish doesn't clear the Public gate. An unannounced feature is not news, and a teaser also tells competitors.
- It becomes eligible when a public announcement page exists, and then it is rung 2.
- If the PM wants a Q4 mention anyway, route it to the roadmap or launch plan, not this sheet. The follow-up skill is samber/developer-relations-skills@devrel-newsletter-program for charter questions.
- Don't use the teaser to fill space.

## Thin-issue call: ship shorter

- Without the charter I treat the whole issue as one section. A two-item issue is probably thin.
- Recommendation: **send the two-item issue.** Don't fill it with #3, #4 or #5, and don't swap in weaker items.
- Skip-and-merge is ruled out because #1 is action-required.
- Evergreen slot applies only if your charter names one, and then it takes about an hour. Demand signals (repeated support questions, empty docs searches) would feed it. I have no access to them, so I can't suggest an item.
- Nothing here is padded. The padding table's rationalizations ("fill the section", "it's close") are the traps to avoid.

## Intake gaps: what I didn't read

Two items from a PR list is thin because only one channel was swept. Before calling the month thin, read these:

1. **Own release feed and changelog.** This also catches releases with no PR label, and satellite repos.
2. **An unlabelled-merge sweep**, to catch any breaking change that shipped without its label.
3. **Ecosystem feeds:** PostgreSQL release and security announcements, plus the pooler and driver releases your readers run.
4. **Submissions.** None are mentioned, so the issue has 0% external content. Check this against your house share.
5. **Event calendar**, if the charter has an events section.

I invented no items for any of these.

## Open questions

1. When did the last issue's sourcing close? This sets the window start.
2. What is in the charter (sections, item ranges, empty-section rule, external share) and in the last three issues? The duplicate check is provisional until then.
3. What are the URLs for the release notes or changelog entries for #4455 and #4402?
4. Is the 2026-07-16 send date fixed? Don't move it to dodge the advisory. The embargo question belongs to the security team.
5. Who approved the PM's roadmap teaser, and is it cleared for any wording at all?

## Hold list and re-open

| Item | Expires | Next step |
|---|---|---|
| #3 logical replication slots UI | End of the August window | Source from the 2026-07-22 release notes. Re-open it then, since releases get yanked. |
| #4 pooler advisory | End of the August window | Link the advisory after 2026-07-24. |
| #5 branching teaser | When announced | Wait for the public page. |

- **Send-day re-open (2026-07-16):** open #1 and #2 again. Confirm the 2026-10-01 date hasn't moved and that neither release was yanked.
- **Record the cutoff:** 2026-07-15 12:00 UTC, so the August run starts from it.