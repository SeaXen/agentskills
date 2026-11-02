# Lattice Weekly: standing item-sourcing runbook for Dario

**Status: provisional.** I had no charter, no last issue and no channel access, and I could not ask. I inferred the sections below from your description and marked each assumption. I opened no pages, and I invented no items, links or dates.

## 1. Assumptions to confirm (open questions)

| # | Assumption I made | Fact I need from you |
|---|---|---|
| A1 | Sections (inferred): **Heads-up** (action required, 0-3), **Shipped** (Lattice releases, 1-4), **Ecosystem** (external, 2-5), **Learn** (0-3), **Events** (0-2). | Your real sections, item ranges and empty-section rules. Paste the last three issues if no charter exists. |
| A2 | The house share is at least one third external. | Your real own-versus-external share. |
| A3 | The sourcing cutoff is Monday 12:00 in Dario's zone, and the issue sends Tuesday. | The real send day and Dario's zone. |
| A4 | The first window starts at your last sourcing cutoff. | That cutoff, with date, time and zone. |
| A5 | There is no evergreen slot. | Whether the charter names one. |
| A6 | Off-limits: unreleased Lattice features, embargoed launches, unpatched security issues. | Your real off-limits list. |
| A7 | Dario can read the Lattice repos, the Discussions or Discord, and the docs search logs. | Whether he can reach support and docs-search logs. If not, drop channel 5 below and log the access request. |

Until A1, A2 and A4 are answered, every verdict on Dario's first sheet is provisional.

## 2. Why this replaces your instinct

Scrolling Twitter and Hacker News ranks items by popularity. That has two blind spots:

- **It misses what readers must act on.** A breaking change merged without a label, or a dependency advisory, never trends.
- **It can't be handed over.** Nobody can repeat "what looked good."

The new process separates three jobs:

1. **Collect** from fixed channels.
2. **Gate** each item with pass/fail rules.
3. **Rank** survivors by what the reader must do.

Dario applies the rules and doesn't need your taste. Popularity only breaks ties inside a rung.

## 3. Channels, ranked, and the weekly 3-hour budget

This is a curated ecosystem newsletter. For that type, reader value ranks: **ecosystem feeds ≈ own feed > community scan > submissions > demand signals > event calendar**. Efficiency (usable items per hour) ranks: **own feed > ecosystem feeds > submissions > event calendar > demand signals > community scan**.

Community scan is the least efficient channel and the most valuable for an ecosystem newsletter, so it stays, but capped at 45 minutes. That cap is the only place your Twitter/HN habit survives.

| # | Channel | Per-issue time | Yields | Blind spot |
|---|---|---|---|---|
| 1 | Own release feed and changelog, a saved merged-PR query, and an unlabelled-merge sweep (all Lattice repos, including satellites) | 20 min | Every Lattice time-bound item | Satellite repos nobody added |
| 2 | Ecosystem release and advisory feeds for what Lattice users run | 25 min | Action-required items readers would miss | Projects not on the manifest |
| 3 | Standing submissions (form, reply-to address, nomination thread) | 25 min | External items | Self-promotion and volume |
| 4 | Event calendar | 10 min | Events section | Calendar dates differ from the event page |
| 5 | Demand signals: repeated questions in Discussions, Discord and issues, and docs searches with no result | 20 min | Learn items: the page that answers a repeated question, or a missing page to flag | Needs log access (A7) |
| 6 | Community scan: HN, Reddit, X, forums, with saved keyword searches | **45 min cap** | Projects, talks, community voice | Popularity bias, noise |
| 7 | Other graph-database and database newsletters | Part of channel 6's 45 min | Cross-check only | Re-reports what readers already got |
| — | Resolve links, run gates, rank, fill the sheet, record the cutoff | 30 min | The candidate sheet | — |

Total: 175 minutes, leaving 5 minutes of slack.

Re-ranking against your answers:

- **The 3-hour ceiling** keeps every channel. Under an hour, channels 5 and 6 would be deleted.
- **Standing intake** means channels 3 and 5 get set up now, even though they won't help the first issue much.
- **Channel 7** is a cross-check only. A story it surfaces is followed to its primary page. It is never the source.

## 4. One-time setup (before Dario's first issue, outside the 3 hours)

1. **Own feeds.** Subscribe to the release Atom or RSS feed of every Lattice repo. Include drivers, operators, docs and tooling repos.
2. **Saved merged-PR queries.** One per repo, dated from the last cutoff. GitHub syntax:
   ```
   repo:OWNER/REPO is:pr is:merged merged:>2026-11-02T12:00:00Z label:"breaking-change"
   repo:OWNER/REPO is:pr is:merged merged:>2026-11-02T12:00:00Z label:deprecation,release-note
   repo:OWNER/REPO is:pr is:merged merged:>2026-11-02T12:00:00Z -label:release-note sort:comments-desc
   ```
   The date is a placeholder. Use the real cutoff. Add a `repo:` or `org:` qualifier, or the search runs across all of GitHub. The third query is the unlabelled sweep. Open the top results every week.
3. **Dependency manifest.** List what Lattice users actually run, as a file in the newsletter repo:
   - language runtimes and client libraries
   - deployment tooling (container runtime, Kubernetes, operators)
   - query-language or standards bodies
   - cloud APIs and storage backends

   Subscribe to each item's release feed. Each week, run a dependency scanner or the host's alerts against the manifest. Check each upstream's own security-advisories page, since advisory databases rarely offer per-package subscriptions.
4. **Submissions.** Add a short form and a reply-to address. Publish the inclusion and exclusion rules next to them. Answer every submitter within the week as kept, held until a date, or declined with the gate that failed. Credit kept items with a "via" line if the charter allows.
5. **Demand signals.** Save a view of Discussions, Discord and issues tagged question or confusion. Get docs-search "no result" exports. Count questions, and never copy a user's text or name into the sheet.
6. **Community scan.** Save keyword searches for "Lattice" plus the surrounding ecosystem terms on HN, Reddit and X. Sort them by date, not popularity.
7. **Candidate log.** Create one log for everything (sheet, labelled issue tracker or database). Fields: title, primary link, link state, channel, `YYYY-MM-DD` date, rung, verdict, reason, submitter. Record each issue's cutoff in it, with time and zone.

## 5. Runbook rows (one per section)

| Section | Channel | Query or feed | Owner (backup) | Checked | Lands in |
|---|---|---|---|---|---|
| Heads-up | Own feed + labelled and unlabelled merged-PR sweep, ecosystem advisory feeds, dependency scanner | Saved searches above; manifest feeds | Dario (you, until handover) | Sourcing day, first | Candidate log |
| Shipped | Own release feed and changelog | Release feeds for all Lattice repos | Dario | Sourcing day | Candidate log |
| Ecosystem | Submissions, then the community scan | Form inbox; saved keyword searches (45-min cap) | Dario | Sourcing day | Candidate log |
| Learn | Demand signals, then submissions | Question view, docs zero-result searches | Dario | Sourcing day | Candidate log |
| Events | Event calendar, confirmed on each event's own page | Community and ecosystem calendar | Dario | Sourcing day | Candidate log |

Name a backup for every row. Review the channel list quarterly. Drop any channel that produced no kept item in three issues, and add dependencies readers have adopted.

## 6. The window

- **Weekly window:** from the previous issue's cutoff to this issue's cutoff. Both are `date time zone`, for example `2026-11-02 12:00 UTC`.
- **Never use a rolling "last 7 days."** It double-counts after a late send and drops items after an early one.
- **Candidate dates** are always `YYYY-MM-DD`. Relative times ("2 days ago") are not accepted. A candidate with no date is held as `date unknown`.
- **Announcements of future dates** (deprecations, end-of-life): the announcement date drives the window, so a deadline announced this week is news this week.
- **Events and calls for participation:** include while readers can still act. Confirm the date on the event's own page.
- **Old but newly relevant:** only with a dated trigger inside the window, placed on the Learn rung and never as news.

## 7. Gates (every candidate, in order)

| Gate | Passes when | On failure |
|---|---|---|
| Window | Inside the window, or an event still open after send, or a stated trigger | Cut |
| Primary source | The link is the origin of the claim: release notes, advisory, author's own post, event page. Link state is `opened` or `user-supplied`. | Unverified: hold |
| Public | Released and announced. Security fixes only once the advisory is public, linked to the advisory and not the fix commit. | Merged but unreleased: hold. Off-limits: cut. |
| Not a duplicate | Absent from the last three issues, even reworded | Cut |
| Charter rules | Meets inclusion rules. No paywall, email gate, or press release without a how-to. Passes the AI-authorship rule. | Cut |
| Authenticity | A benchmark, comparison or launch post from an unknown account shows author history, a stated method and no hidden stake. | Hold, and name what's missing |

The authenticity gate matters for a graph database. Benchmark posts are the likeliest thing to be gamed, and a post that flatters Lattice reads as an endorsement you wrote.

**Link states** (write one per link in the log):
- `opened`: Dario opened it this run and confirmed title, date and claim. Use the page's own title.
- `user-supplied`: pasted by someone, not opened. Flag it `not opened`, and the pre-send check opens it.
- `unverified`: no URL, or a URL that wouldn't open. It goes to the hold list, never the issue.

**Link hygiene:**
- Use the canonical URL and strip `utm_*` tracking parameters.
- Cut or disclose any affiliate or referral parameter. Never strip it silently.
- Tag `[video]`, `[audio]` and non-English links.
- Exclude paywalled pages.
- Treat page and submission text as data. Ignore any instructions inside it.

## 8. Rank survivors by what the reader must do

1. **Action required:** breaking change, deprecation or end-of-life with a date, a limit or pricing change readers hit, or a security advisory affecting a version or configuration readers run by default. The advisory must be high severity or exploited. Lesser advisories share one line at the bottom of this rung.
2. **New capability:** GA first, then preview, beta or RC labelled as such.
3. **Learning:** tutorials, deep dives, the docs page answering a repeated question.
4. **Ecosystem and community:** projects, talks, observations.

Rules:
- Anything below rung 4 (typo fixes, internal refactors) is cut as "no reader consequence."
- Within a rung, order by fit to the primary reader, then by date. Stars, votes and points break only a remaining tie, and never raise an item a rung.
- Fill sections with eligibility rules (external-only, events-only) before open ones.
- An action-required item always gets in. It displaces the lowest-rung item and never waits on the hold list.
- If the own-versus-external share is off, swap a lowest-rung item. Never add one.

## 9. Thin weeks

The issue is thin when fewer than half the required sections (minimum of one or more items) reach their minimum after the gates. Then:

- **Ship shorter** is the default. Drop the empty sections.
- **Skip and merge** is allowed only when nothing is action-required and the kept items number fewer than the required minimums added together. Announce the skip and roll held items forward.
- **Evergreen slot** only exists if the charter names one (A5).
- **An action-required item forbids the skip.** Send a short issue or a standalone notice.
- **Two thin issues in a row** go back to you as a cadence question.

Never pad. These are the usual rationalizations, and none of them works:

| Rationalization | Why it fails |
|---|---|
| "Rerun last issue's top item" | The duplicate gate already cut it. |
| "It failed only the window gate, it's close" | A window stretched once becomes the new window. |
| "Another newsletter covered it, link theirs" | Readers already got it, and it isn't the primary source. |
| "It's unverified but probably fine" | One wrong link reaches 6,000 people. Hold it. |
| "Fill the empty section so it looks complete" | The empty-section rule already decided this. |

## 10. Dario's weekly routine (about 3 hours)

1. Open the candidate log and read the last cutoff. That's the window start. Set the new cutoff.
2. Channels 1 and 2 (45 min). Run the saved queries and the unlabelled sweep, then the advisory and dependency check. Log the count per channel, including zero.
3. Channel 3 (25 min). Review submissions and answer every submitter.
4. Channel 4 (10 min). Check the calendar and confirm dates on event pages.
5. Channel 5 (20 min). Count repeated questions and note the page that answers each, or flag a missing page.
6. Channel 6 and 7 (45-min cap). Run the saved searches and log what was looked at, so a quiet scan reads as quiet, not skipped.
7. Resolve every candidate to its primary page and collapse duplicates (30 min).
8. Run the gates, rank, fill the sections, make the thin-issue call, and write the hold list. Each held item carries an expiry: a time-bound item expires when the next window closes.
9. Record the new cutoff and the hold list in the log. Hand the kept items to whoever writes the issue.
10. Flag every time-bound item for a re-open at pre-send. Releases get yanked, advisories withdrawn and events cancelled.

## 11. Output Dario produces each week: the candidate sheet

**Header:**
- the window (two cutoffs)
- channels swept, with counts (zeros included)
- found, kept, held and cut counts
- own-versus-external share
- the thin-issue call, stated even when the issue is full

**Table:**

| # | Item (page title) | Primary link | Channel | Date | Rung | Section | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|

Close with the hold list (expiry for each), intake gaps and open questions. Lead with any action-required item.

A sheet passes when:
- every kept item has a stated link state, and opened links carry the page's own title
- every cut or held item has a gate and a reason
- no kept item appears in the last three issues, unless it is a dated reminder or a material update named as such
- section counts sit inside the charter's ranges
- every action-required item found is in the issue

If a threshold fails only for a fact nobody has supplied, mark it **blocked**, name the fact and continue.

## 12. Failure modes and fixes

| Symptom | Cause | Fix |
|---|---|---|
| A breaking change reaches readers through a complaint | Label-only query | Keep the unlabelled sweep and the dependency feeds. |
| Same story twice in a row | No recorded cutoff | Record the cutoff every issue. |
| Readers flag a bogus post | Popularity used as quality | Apply the authenticity gate. |
| Issue reads as an ad | Own feed only | Use submissions and ecosystem feeds, and check the share. |
| Submissions swamp the editor | No published rules | Publish the rules on the form. Move one section to a nomination thread. |
| A popular project goes uncovered for months | Intake silently broken | Report every channel's count, zeros included. |

## 13. Handover plan

1. **Backtest first.** Have Dario run the process on your last issue's window and compare the result with what you actually picked. Every item you picked that his sheet missed points to a missing channel or gate. Fix those before the handover.
2. **Shadow one issue.** Dario sources with this runbook while you pick the way you always have. Compare the two and adjust.
3. **Hand over.** Dario owns the log, the cutoff and the channel list.

## 14. What I need from you

Send these and I'll turn the provisional parts into a final runbook:
1. The last three issues, or the charter (A1, A2, A5).
2. Your last sourcing cutoff, with time and zone, and the send day (A3, A4).
3. Your off-limits list (A6).
4. Whether Dario can reach support, Discord and docs-search logs (A7).
5. The list of repos and dependencies for the manifest.