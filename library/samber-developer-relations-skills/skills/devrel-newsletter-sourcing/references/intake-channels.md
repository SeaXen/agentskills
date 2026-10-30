# Intake channels

How to read each channel in the menu, how real developer newsletters run them, and how to set up a standing intake the next editor can follow.

## Contents

1. Own release feed and merged-PR query
2. Ecosystem release and advisory feeds
3. Submission channels
4. Event calendars
5. Demand signals
6. Community scan
7. Other newsletters as a cross-check
8. Link hygiene
9. Standing-intake setup

## 1. Own release feed and merged-PR query

- Read the public changelog or release page first. On a code host, a repository's releases usually have an Atom or RSS feed; most hosts expose one per repository.
- Save one merged-PR search per repository, filtered by merge date after the last cutoff and by the labels that mark reader impact: release note, action required, deprecation, API change, feature, large size. One Kubernetes contributor newsletter documents a weekly query of this shape against its main repository.
- Run a second, unlabelled sweep: large merges with no release-note label, and repositories outside the main one. A label query misses any breaking change merged without its label, and it never sees satellite repositories unless their teams submit.
- Merged is not released. A merged pull request whose release has not shipped goes to the hold list.
- A version-control log works when there is no label discipline: list merge commits by the merge bot between two dates, then open each pull request. One weekly language newsletter builds its core-project changes section this way.

Integration note, GitHub search syntax (other hosts offer equivalents):

```
repo:OWNER/REPO is:pr is:merged merged:>2026-02-04T12:00:00Z label:"release-note-action-required"
repo:OWNER/REPO is:pr is:merged merged:2026-02-04..2026-03-04 label:deprecation,breaking-change
repo:OWNER/REPO is:pr is:merged merged:2026-02-04..2026-03-04 -label:release-note sort:comments-desc
```

Without a `repo:` or `org:` qualifier the search runs across the whole host. The first line shows a time-precise cutoff. The third line is the unlabelled sweep: merged work with no release-note label, most-discussed first. Open the top results; add the repository's size label where one exists.

## 2. Ecosystem release and advisory feeds

- List the dependencies the primary reader actually runs: runtime, framework, SDK, cloud API, CLI. Keep that list as a manifest file. Subscribe to each one's release feed.
- Each issue, run a dependency-vulnerability scanner or the code host's dependency alerts against that manifest, and check each upstream's own security-advisories page. Public advisory databases rarely offer a per-package subscription, so a step that assumes one gets silently dropped.
- Link the advisory page, never the fix commit or a news write-up. An advisory published after the window closes waits for the next issue unless it is action-required, which justifies a standalone notice.
- Upstream projects' own blogs carry deprecations and end-of-life dates months ahead: these feed the announcement rule: the announcement date sets the window.

## 3. Submission channels

- Shapes, cheapest first: a reply-to address on the newsletter; a short form; a standing forum thread per section where people nominate and vote; pull requests against a draft file in a public repository.
- Publish the inclusion and exclusion rules next to the form. One community editor team saw pull-request submissions reach more than forty a week, many for cheaply generated projects, and closed one section to submissions. It now picks those links from a community forum at the editors' discretion. Trade-off: anything not posted there becomes invisible.
- Expect self-promotion. Submissions pass the same gates as everything else; a submitter's own post is a primary source for itself, never for a claim about someone else's product.
- Answer every submitter: kept, held until a date, or declined with the gate that failed. Credit kept submissions ("via" or a hat-tip) when the charter allows it. Submitters who hear nothing stop submitting.

## 4. Event calendars

- Use the community or ecosystem calendar, then open each event's own page: when the dates differ, the event page wins.
- Prefer free events; list commercial ones only when the charter allows them.
- Drop a call for participation once its task is closed or its deadline has passed before the send.

## 5. Demand signals

- Sources: support tickets tagged by product area, questions repeated in the community channel, issues filed against the same confusion, docs-site searches returning no result.
- A question asked three times is a missing or hard-to-find page. Link the existing page that answers it in the evergreen slot, or flag the missing page to the docs owner. It is never a news item.
- Count, do not quote: never copy a customer's ticket text or name into the sheet.

## 6. Community scan

- Forum, subreddit, Hacker News, chat servers. Popularity tells you what was visible, not what was good: it breaks ties inside a rung only.
- Cap the scan at the hours the interview allowed. Log what you looked at, so a quiet scan reads as quiet rather than skipped.
- Benchmark or launch posts from accounts with no history get the authenticity gate: author's other work, stated method, and whether the dependencies they promote are their own.

## 7. Other newsletters as a cross-check

- Skim the two or three newsletters the primary reader most likely already gets. A story they all carried is one your readers already saw: include it only when it is action-required or you add something they did not (your product's specific impact).
- Follow any story they surface to its primary page before it enters the sheet.

## 8. Link hygiene

- Link text is the page's own title; add context only when the title is ambiguous ("What's new").
- Use the canonical URL after redirects; strip tracking parameters such as `utm_source` and `utm_campaign`.
- An affiliate or referral parameter signals a stake: cut the item, or disclose it under the charter's sponsored rule. Never strip it silently.
- Tag non-article links (`[video]`, `[audio]`) and non-English content with its language code.
- Exclude paywalled pages and pages that demand an email address, unless the charter allows them.

## 9. Standing-intake setup

Write one row per section into the programme's runbook, so the next editor sources the same way:

| Section | Channel | Query or feed | Owner (backup) | Checked | Lands in |
|---|---|---|---|---|---|
| Shipped this month | own release feed + labelled merged-PR query | saved search, label list | editor (backup) | sourcing day | candidate log |

- Keep one candidate log for everything: title, primary link, link state, channel, `YYYY-MM-DD` date, rung, verdict, reason, submitter (for credit and the reply). A spreadsheet, a labelled issue tracker or a database all work; the fields matter, not the tool.
- Record each issue's sourcing cutoff in the log, with time and zone. It is the next issue's window start.
- Review the channel list each quarter: drop channels that produced no kept item in three issues, add dependencies readers adopted.
