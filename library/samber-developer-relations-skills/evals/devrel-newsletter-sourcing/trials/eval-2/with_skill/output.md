# Candidate sheet: Tesselate CLI digest

**Status: provisional.** I had no charter, no last issue, no URLs and no feed access in this run. Nothing below is opened. I did not invent any link, date or version.

## Thin-issue call

**Ship shorter.** I would not pad it.

- Four sections require at least one item: Shipped (2), Fixes (1), Learn (1) and Community (1). Events can be 0, so it doesn't count.
- After the gates, only Fixes can reach its minimum, which is 1 of 4. Under half is thin.
- Ship Fixes (2.3.1, 2.3.2) and Events (Lisbon). Drop Shipped, Learn and Community under the default empty-section rule. I applied that default because I haven't seen your charter.
- Skip-and-merge is also allowed. It needs two things: nothing action-required turns up, and fewer kept items than the 5 minimums added together (2+1+1+1).
- Skip-and-merge is not the pick. Skipping is the worse option on effort. Shipping shorter costs the same reader trust and almost no work.
- The evergreen slot is available only if your charter names one. I don't know whether it does.
- Your manager's "it has to look full" is a charter question. If the charter forbids empty required sections, send that question to `devrel-newsletter-program`. A second thin issue in a row goes there too, as a cadence question.

## Header

| Field | Value |
|---|---|
| Window | **Open.** Start is the last issue's sourcing cutoff (date, time, zone). I don't have it. End is this issue's cutoff. |
| Assumption | Today is 2026-10-30. Cutoff is 12:00 the day before your send date, in your zone. Send date unknown. |
| Channels swept | Own release feed: not read, 2 items pasted by you. Ecosystem advisories: not read. Submissions: not read. Event calendar: 1 item pasted by you. Demand signals: not read. Community scan: not read. |
| Found | 6 |
| Kept (provisional) | 3 |
| Held | 0 |
| Cut | 3 |
| Own vs external | 2 own, 1 meetup of unknown organiser. The house share is unknown. |

## Table

| # | Item | Primary link | Channel | Date | Rung | Section | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | Tesselate CLI 2.3.1 release notes | **needed** | pasted by you (own feed) | unknown | TBD | Fixes | keep, provisional | Unverified until you paste the page, so it sits on hold until then. Rung 1 only if the notes show a security fix or breaking change. |
| 2 | Tesselate CLI 2.3.2 release notes | **needed** | pasted by you (own feed) | unknown | TBD | Fixes | keep, provisional | Same as #1. If 2.3.2 supersedes 2.3.1, write one item, not two. |
| 3 | Lisbon meetup | **event's own page needed** | pasted by you (calendar) | about 2026-11-20 (unconfirmed) | n/a | Events | keep, provisional | Include while registration is still open after the send. The event page's date overrides your "three weeks". |
| 4 | April's top plugin-authoring post (rerun) | n/a | your request | 2026-04 | n/a | n/a | **cut** | Window gate: it is outside the window. Rerunning a past top item is the first row of the padding table. |
| 5 | Hottest links from TLDR and Console | none, not opened | other newsletters | unknown | n/a | n/a | **cut** | Other newsletters are a cross-check only. Hotness is popularity, which never moves an item up. Your readers likely saw them already. |
| 6 | Docs pages added to pad Learn | none | your request | unknown | n/a | n/a | **cut** | Window gate, with no dated trigger inside the window. |

## What would put #4, #5 and #6 back

- **#4 and #6, trigger:** a dated trigger inside the window, for example "2.3.2 changes the plugin API, so the April guide now applies". Then the item goes on the Learn rung as a learning item, not as news.
- **#4 and #6, evergreen slot:** this works only if your charter names one. The item must pass every gate except the window, and still be accurate on 2.3.2.
- **#6, demand:** docs searches returning nothing, or the same question asked three or more times. Count them, don't quote tickets.
- **#5, resolve to the origin:** if a TLDR or Console story matters to a Tesselate CLI user, open its primary page, run all the gates, and add it as one Community item. Don't link the newsletters.

## Hour of sourcing worth doing before you ship thin

None of these has been run yet. Each can add a legitimate item.

1. **Unlabelled merges:** sweep large merges since the cutoff, including satellite repos. A breaking change merged without its label is the classic miss.
2. **Advisories:** check security advisories for the runtime and dependencies your CLI users run. Any action-required item **must** go in, and it forbids skipping.
3. **Submissions inbox or form:** it feeds Community, and about a third of items at some newsletters arrive this way.
4. **Docs search logs and support questions:** this is the legitimate way to fill Learn.
5. **Merged but unreleased work:** hold it with an expiry until the next window closes.

## Hold list

Empty. Items #1 to #3 move here, each with an expiry at the next window close, until you paste their pages.

## Intake gaps

- The release feed, advisory feeds, submissions, demand signals and community scan were not read. I couldn't reach them from here.
- The Events horizon is unknown. If your charter sets one in weeks, check Lisbon against it.

## Open questions

I need these before the sheet is final. Questions 1 to 3 matter most.

1. Paste the 2.3.1 and 2.3.2 release-note URLs and the Lisbon event page. Is the meetup yours or a community event?
2. What was the last issue's sourcing cutoff (date, time, zone), and what is this issue's send date? Paste the last three issues' item lists for the duplicate gate.
3. What does the charter say about empty sections, an evergreen slot and the own-versus-external share?
4. Is anything off-limits, such as unreleased features or an unfixed security issue?
5. Can you reach the support tickets and docs search logs? How many hours do you have before tonight?

## Hand-off

Once the pages are confirmed, send items #1 to #3 to `devrel-newsletter-issue` for the copy. Re-open every time-bound link at pre-send. Releases get yanked and events get cancelled. Record this issue's cutoff with its time and zone, so next month's window starts from it.