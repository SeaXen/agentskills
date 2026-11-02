# Candidate sheet: Orrin newsletter, issue sending Wednesday 2026-06-17

**Status: provisional, and no item is cleared to ship yet.** I could read neither the release feed nor the community calendar, and you pasted no export or URL. So every item below comes from your message, not from an opened page. I invented no link, date or version.

## Lead findings

1. **"Past 7 days" would drop Orrin 1.9.0.** Seven days back from 06-17 is 06-10, and 1.9.0 shipped 06-09. The skill forbids a rolling window. It double-counts after a late send and drops items after an early one, and last week's Monday-to-Friday gap shows the failure.
2. **Anchor the window on the last cutoff instead.** That cutoff is the Monday 2026-06-08 link-list close, which also makes 1.9.0 the first item after it.
3. **The Berlin event date is unresolved.** The calendar says 2026-07-02 and the meetup page says 2026-07-09. The event's own page wins, but I have not seen it.
4. **The 2024 backfill guide may be stale.** It qualifies only as old-but-newly-relevant, and it needs checking against 1.9.0.

## Header

- **Window start:** 2026-06-08 12:00 UTC. This is the previous sourcing cutoff.
  - Assumption: you gave no time or zone, so I used 12:00 UTC. Tell me your zone if it differs.
- **Window end:** 2026-06-16 12:00 UTC. This is 12:00 the day before the send, under the same assumption. The window is 8 days, not 7.
- **Event horizon:** through 2026-07-17, one month after the send. The charter sets no horizon in weeks, so I used your "next month".
- **Charter:** none supplied. I inferred sections from your message: Releases, Reading, Events. Item ranges, empty-section rules and the own-versus-external share are unknown. This marks the thin-issue and share verdicts **provisional**.
- **Last issue:** its contents are unknown. The duplicate gate is **provisional**, especially because that issue went out late, on 06-12. If it carried 1.9.0 (released 06-09), cut 1.9.0 here.

## Channels

| Channel | Count | Note |
|---|---|---|
| Own release feed | not read | no access in this run, and no export pasted. This is not a zero. |
| Community calendar | not read | same reason |
| Pasted by user | 4 | the four items below, with no URLs |
| Ecosystem and security-advisory feeds | not swept | recommended default, outside the two channels you named |
| Submissions | not swept | recommended default, outside the two channels you named |

**Found:** 4. **Kept:** 0. **Held:** 4. **Cut:** 0.

## Candidates

All four are **unverified** (no URL given), so all four are held. They are listed in the section each would take once cleared.

| # | Item | Primary link | Channel | Date | Rung | Section | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | Orrin 1.9.0 release notes | not given | pasted by user (own feed) | 2026-06-09 | 2 new capability (provisional) | Releases | **hold** | Inside the window. It needs the release-notes URL, and I have not read them. Check for breaking or deprecation entries: a breaking change would make it rung 1 (action required). |
| 2 | Orrin connector internals (contributor write-up) | not given | pasted by user | 2026-06-11 | 3 learning | Reading | **hold** | Inside the window. It needs the author's own post URL. Authenticity gate: confirm the author history, a stated method, and no hidden stake. |
| 3 | Backfilling with Orrin (2024 guide) | not given | pasted by user | 2024 (exact date unknown) | 3 learning | Reading | **hold** | Old but newly relevant. Trigger: 1.9.0, 2026-06-09, brought the backfill command back. It needs its URL, and its steps must be confirmed accurate on 1.9.0 before it runs. |
| 4 | Orrin Day Berlin | not given | pasted by user (calendar) | 2026-07-09 per meetup page; 2026-07-02 per calendar | n/a | Events | **hold** | Both dates fall inside the horizon. The date is unresolved, and the event page wins over the calendar. Open that page, confirm the date, and check that registration or the call is still open after the send. |

- **Item 3 placement:** it goes on the learning rung and is never presented as news. The Reading blurb must state the trigger. If the 1.9.0 notes show backfill behavior changed, the guide is not "still accurate". Then hold it and flag a docs update to the owner.
- **Item 4:** if the 07-09 page is confirmed, list 07-09 and fix the calendar entry. Never print both dates.

## Thin-issue call (provisional)

- **No charter, so no verdict on whether the issue is thin.**
- **Best case:** if items 1 to 4 clear, Releases gets 1, Reading gets 2 and Events gets 1. That looks like a normal short issue. Sections whose minimum I could not see are untested.
- **If only 1.9.0 and the event clear:** ship shorter and drop any empty section. Do not pad.
- **Skip is blocked if 1.9.0 is action-required.** Send the short issue or a standalone notice instead.

## Hold list and expiries

- **1.9.0, connector write-up and backfill guide:** each expires at the next window close. Items 1 and 2 are time-bound. Item 3 is tied to the 1.9.0 trigger.
- **Orrin Day Berlin:** expires when registration or the call closes, or on the event date.

## Intake gaps and open questions

Paste these and I will turn the holds into keeps:

1. **URLs.** I need the 1.9.0 release-notes URL, the connector write-up URL, the backfill guide URL, and the Orrin Day meetup page URL. Pasted URLs keep, flagged `not opened`, so your pre-send check opens them and swaps in each page's own title.
2. **Release feed export.** Paste everything from 2026-06-08 onward. Only the three items you remembered are covered. A 1.9.1 patch, a deprecation notice or an unlabelled breaking merge would be missed. If you can, add a sweep of large merges with no release-note label.
3. **Community calendar export.** I need every entry through 2026-07-17, not just Berlin.
4. **Last issue (sent 06-12).** I need it, for the duplicate check and for your charter's sections, ranges and own-versus-external share. Does it already carry 1.9.0?
5. **Cutoff time and zone.** I assumed 12:00 UTC.
6. **Off-limits.** Is there anything embargoed or unreleased, such as security fixes not yet published?
7. **Wider intake.** Do you want ecosystem advisory feeds for dependencies Orrin users run, and a submissions inbox? Both are default channels. They also protect against a missed breaking change.

## Fixing the lateness

- **Record the cutoff.** Store 2026-06-16 12:00 UTC as the start of the next window. I will keep it as project context, not as a finished task.
- **Why it was late.** The sourcing cutoff was Monday and the send was Friday. That gap is a send-date problem, not a sourcing one. Fix it in the programme's cadence, not by widening the window.