# Haverlock office hours: fix plan

The sessions are fine. What's missing is the step after each session. You answer questions live, and nothing changes afterward. That explains both symptoms:

- **Repeat questions:** a recording link isn't a docs fix. Nothing turns a repeated question into a page, so the question returns every month.
- **The lost May request:** "noted, I'll pass it on" leaves no record, no asker handle and no status. Nobody can answer "was it decided?", including you.

I didn't run the skill's interview, so the points below are my assumptions. Please confirm or correct them.

## Open decisions (confirm or correct)

1. **Job of the program.** I assumed "find docs gaps" first and "hear product feedback" second. Your two symptoms point there.
2. **Where your users are.** I don't know the regional split, so the slot plan below isn't final.
3. **Rotation.** I need host and backup names, which engineers take part, and whether their managers have agreed to a cap of one session per month.
4. **Recording rules.** Can your users share screens with tokens or customer data? Do you have EU attendees? A secrets manager makes this the riskiest part of the current setup.
5. **Feedback record.** I need to know where product requests will live. A spreadsheet or tracker works if product reads it. Who decides, and by when, belongs to the feedback-loop skill (`developer-feedback-loop`).
6. **Support, sales and security.** I need a support link, a sales contact and a private security disclosure channel for the scope card.

## 1. Charter (one page)

```
Program:        Haverlock office hours
Job:            Surface docs gaps (primary); product signal (secondary)
Audience:       Haverlock users, 6-8 per session
Format:         Drop-in call (monthly) + async intake thread open all month
Slot:           [keep current slot; confirm regional split, see section 2]
Staffing:       Host [name], backup host [name]; engineers [names], cap 1 session/month each
Scope card:     section 4
Recording:      Internal only (notes source); the public record is the write-up. See section 6.
Outputs:        Write-up within 2 business days; docs ticket on 2nd sighting; feedback record with asker handle
Pilot:          Next session to +6 sessions (monthly pilot = 2 quarters)
Demand bar:     Median distinct askers per cycle >= 3 (live or async)
                AND merged docs fixes + feedback records >= 1 per 2 sessions
                Below it -> async thread only for a quarter, then re-test
Operating bar:  No silent cancellation; no engineer over cap; write-ups on time in all but one session
```

All of these figures are self-set baselines. Nobody publishes attendance or deflection benchmarks for office hours, so don't quote them as industry numbers.

Demand bar, 2nd half: your current docs-fix count is effectively zero, so you'd fail it today. That's why the catch-up below comes first.

## 2. Slot plan

- Keep the current slot until you have the regional split from analytics or a short poll in Discord.
- Add a second slot only if a second region is at least 25% of users (baseline) and the rotation can staff both.
- Any region outside 09:00-18:00 local gets the async thread as its named path.
- Publish the slot in the largest region's time zone, with a calendar link.

## 3. Rotation calendar (next quarter, skeleton)

Monthly cadence needs at least 2 engineers (1 session plus 1 spare). Use 3 if you can.

| Date | Engineer | Area | Backup | Prep brief sent | Confirmed |
| --- | --- | --- | --- | --- | --- |
| [Nov] | | rotation, locks | | T-48h | |
| [Dec] | | tokens, policies | | T-48h | |
| [Jan] | | namespaces, auth | | T-48h | |

The month's spare engineer is the backup for that session. Get each manager's agreement to the cap in writing.

## 4. Scope card (ready to publish)

```
## What to bring to Haverlock office hours

Bring: "my rotation job fails with a lock timeout", "how do I scope a token to one namespace",
"what's the safe way to roll a root key", "how should I structure policies across teams".
Not here:
- Account, billing, plan or contract questions → [support link]
- Pricing, licensing, paid-tier features → [sales contact]. We can say what the public docs say, not roadmap or price.
- A suspected vulnerability → [security disclosure channel]. Never raise it live or in a public thread.
- A bug you can reproduce → [issue tracker]. Bring it and we'll help you write the report.
- A feature you need → we log it live in [feedback record] with your handle, if you agree,
  so you hear the decision. The product team decides.
- Debugging your own environment → we can't see it. Bring a minimal reproduction with secrets removed.

Never post logs, tokens, keys or customer data in the thread or on screen.
Sessions are not published as recordings. Each session gets a written summary within 2 business days. [Retention note.]
Code of conduct: [link].
```

Also pin a "no logs, keys or customer data" rule at the top of the intake thread, and give moderators a redaction path.

## 5. Close the loop after every session

1. **Write-up** within 2 business days, in the intake thread. Skeleton:

```
## Haverlock office hours - [date], with [engineer], [area]

### Answered
- **[Question in asker's words]** - [answer, 2-4 lines] - [docs link or docs ticket]
### Answered here, not live
- **[Question]** - [answer]
### Redirected
- [Topic] → [destination]. (No names.)
### Logged for the product team
- [Request in user's words] → [feedback record link] - status: [open / decided / shipped / declined]
### Docs we are fixing
- [Page] - [what was missing] - [ticket]

Next session: [date, time in audience zone, calendar link]. Submit questions: [link].
```

2. **Docs ticket on the second sighting** of any question, from any channel. Group variants into one family and add sightings to the family's open ticket. Label tickets `office-hours` so the pilot review can count them.
3. **Log every feature request and bug** in the user's words, with the asker's handle if they consent. Include a status column. "Noted, I'll pass it on" becomes "logged at [link]; you'll hear the decision."
4. **Delete the raw session log** after the write-up is published.
5. **Link the latest write-up** in the next announcement.

## 6. Recording policy

You currently post the Zoom link in Discord. For a secrets manager, that's the highest-risk part of the setup. A screen-share can show a token, an internal hostname or a customer name. The skill says to review every screen-share before publishing, and a recording of a live session usually can't be edited that way.

- **From the next session:** record only with a stated notice, and keep the recording internal as the source for the write-up. The write-up is the public record. Alternatively, drop recording and rely on notes.
- **Notice script:** "This session is recorded for our notes and not published. Keep your camera off and use chat if you'd rather. Don't share your screen if it shows tokens, customer data or internal hostnames."
- **Past recordings in Discord:** watch each one for tokens and hostnames. Revoke anything shown, then pull or replace the link with a write-up. If you have EU attendees, legal review owns the notice and retention wording.

## 7. Catch-up (do these first, in this order)

1. **Lock timeout (~7 sightings if monthly since March; count from recordings).** It already passed the second-sighting trigger long ago. Open the docs ticket now and put every sighting date in it. The troubleshooting-docs skill (`developer-troubleshooting-docs`) writes the page. Publish a short answer in the thread meanwhile.
2. **Namespace-scoped token (2 sightings).** Open a docs ticket today.
3. **The May request.** Go through the May recording and the Discord thread, and ask product directly. Reply to the user with what you find, including "I didn't log it and I should have." Don't invent a decision status. If you can't find the request, ask her to restate it and log it with her handle.
4. **Other requests since March.** Scan the recordings and your pings to product, and build one feedback record. Send each asker a status update.
5. **First write-up.** Publish one for the last session so the format exists before the next announcement.

## 8. Measurement

| Signal | Target | Current |
| --- | --- | --- |
| Sessions held / planned; held with zero askers | All held, none cancelled silently | Not measured |
| Distinct non-staff askers per cycle (live or async) | Median >= 3 (baseline) | Attendees 6-8; askers not measured |
| Questions answered or redirected | All | Not measured |
| Write-up within 2 business days | All but one | 0 (none published) |
| Merged docs fixes + feedback records | >= 1 per 2 sessions | ~0 |
| Engineer sessions per month | No engineer over 1 | Not measured |

Count distinct askers rather than attendees or recording views. One person can bring ten questions, and views measure nothing about changes shipped.

Everything past the pilot is provisional. At the pilot review, judge the demand bar first (continue or stop), then the operating bar (what to fix).