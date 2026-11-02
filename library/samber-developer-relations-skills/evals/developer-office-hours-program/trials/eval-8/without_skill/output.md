Fix: office hours produce two outputs, a docs backlog and a request ledger. Right now both go to Zoom and Discord, where nobody can search them.

**Next action (15 min):** Create one shared table with two tabs, `Requests` and `Questions`. Use whatever your team already owns (Notion, Airtable, a GitHub Project). Then do the steps below.

## 1. Repeated questions become docs pages

Two questions repeat: "rotation job fails with a lock timeout" and "scope a token to one namespace". Both are already ranked. Neither needs a product fix unless a gate below says so.

1. Write two pages, one per question. Use the lock timeout first, since it has come up every month since March.
2. Give each page the same six parts, in this order:
   - Message: the error string, verbatim.
   - Applies to: versions and configs.
   - Cause: one or two sentences.
   - Fix: numbered steps, one branch per cause.
   - Confirm it worked: the output that proves the fix.
   - Still stuck: where to escalate and what to attach.
3. Run the fix yourself before you publish. If you can't reproduce it, say "reported, not reproduced" on the page.
4. Put the error string in the title, the first heading, and the body. People paste the error into search.
5. Gate the lock timeout on one question: is it a product defect? If the same failure recurs in 7 months of sessions, it probably is.
   - Publish the page as a stopgap.
   - File a product ticket with the session count as evidence.
   - Name an owner. Without one the page becomes the permanent answer.
6. Link the pages from the rotation docs. Ask product whether the error payload can carry the docs URL.

**Capture habit:** add every new question to `Questions` within 24 hours of the session. Use these columns: date, question, verbatim error text, count, page link. A question seen 2 or more times gets a page. Do the page before the next session.

Time: about 1 hour per page if you can reproduce the failure. An afternoon if you must rebuild the environment.

## 2. Feature requests need a ledger

"Noted, I'll pass it on" has no record behind it, so the May question had no answer. Add one row to `Requests` per ask, and never accept a request without a row.

| Column | Content |
|---|---|
| ID | stable number |
| Date | when asked |
| Asker | name, plus contact if they agree |
| Request | their words, plus the underlying problem |
| Product ticket | link, once filed |
| Status | `new` / `filed` / `under review` / `accepted` / `declined` / `shipped` |
| Decision date | when product answered |
| Reason | one line, filled when declined or deferred |
| Last told | the last time you told the asker |

1. Fill the row during the session, or within an hour.
2. File the product ticket yourself. Don't just ping product. Put the ticket link in the row.
3. Ask product for a decision cadence. Monthly, one 20-minute pass over every `filed` row, is enough. A request with no decision after 60 days gets escalated.
4. Close the loop with the asker. A "declined, here's why" counts. A silent request is the worst outcome.
5. Open the next session with a 5-minute readout: decided since last time, shipped, still open.

**Right now (30 min):** Rebuild the backlog from memory, Discord, and Zoom recordings. Start with the May request. Give her an honest answer this week. If product never decided, say so, say you are filing it today, and give her the date of the next readout.

## 3. Recordings are an archive, not a record

1. After each session, post a short summary next to the Zoom link in Discord, in the same message:
   - questions answered, each with a docs link;
   - requests logged, each with its ID;
   - decisions since last session.
2. Pin the latest summary.
3. If Zoom gives you a transcript, search it for "feature", "wish", and "can you", and add anything you missed to the ledger. Run this once per session, and don't automate it yet.

## 4. Check it works

Measure at month 3:
- the lock timeout stops appearing at sessions, or its count drops;
- no request is older than 60 days without a decision;
- you answer "what happened to my request?" in under a minute.

If the lock timeout still comes up after the page exists, people aren't finding it. Check the title and the links before you write more pages.

**Next:** open the ledger and enter the May request, with the asker's name and date.