**Next action:** answer the 8 open decisions below (about 10 minutes). Everything after them is a full draft built on stated assumptions.

# Driftmark Office Hours: 12-Month Program plus v4 Launch AMA

## Open decisions (I assumed these, so fix them first)

I had no answers to the skill's gating interview. Every name and region below is a placeholder or an assumption.

1. **Users by region (Q3).** I assumed the skill's worked example: about 70% US (half East, half West), 20% Europe, 10% elsewhere. Hosts are two DevRel staff in Paris. The slot depends on this.
2. **Demand gate (Q2).** Can you name 5 questions from the last month that docs did not answer? I did not check. If you cannot, the skill says to run the async thread only and fix docs first. I kept the live drop-in as the default and made it a pilot with a stop rule.
3. **Staff (Q4).** I assumed 2 DevRel hosts and 4 engineers (E1–E4). They are unnamed and have no manager sign-off yet. Biweekly needs 3–4 engineers.
4. **Recording and roadmap limits (Q6).** I assumed EU attendees exist and that nothing unreleased may be shown. Legal must approve the recording notice and retention wording.
5. **Contacts (Q7).** I need links for support, sales, security disclosure, the issue tracker and the feedback record. They appear as `[SUPPORT]`, `[SALES]`, `[SECURITY]`, `[ISSUES]` and `[FEEDBACK]`.
6. **Promotion channels (Q8).** Unknown. I wrote "every channel you already use".
7. **AMA date.** I set Thu 5 Nov 2026 (the VP's "two weeks"). That assumes v4 has shipped. The VP must confirm the date and the roadmap rule.
8. **Skill limit.** The skill designs standing programs. For the one-off AMA it covers only the scope card and room handling, so section 7 stops there. Stage and stream production belongs to `samber/dev-event-organizer-skills@virtual-event-production`.

**Provisional:** everything after the pilot review on 4 Mar 2027 is provisional. A 12-month calendar is a plan, not a commitment.

## 1. Charter

| Field | Value |
|---|---|
| Program | Driftmark Office Hours |
| Job | Unblock users (first). Docs gaps and product signal are by-products. |
| Audience | Developers building and running functions on the Driftmark edge runtime |
| Format | Async intake thread, always on, plus a biweekly drop-in call |
| Slot | Thursday 12:00 ET / 09:00 PT, every second week (see section 2) |
| Staffing | Host H1, backup host H2, engineers E1–E4, cap 1 session per engineer per month |
| Scope card | Section 6 |
| Recording | Drop-in call is not recorded. The write-up is the record. The AMA is recorded. |
| Outputs | Write-up within 2 business days, docs tickets, feedback records |
| Pilot | 3 Dec 2026 to 25 Feb 2027, 6 sessions |
| Review | Thu 4 Mar 2027 |
| Demand bar | Median ≥ 3 distinct non-staff askers per cycle, live or async. At least 1 merged docs fix or feedback record per 2 sessions. |
| If below the bar | Drop to the async thread for one quarter, publish the repeat answers as docs, then re-test demand. |
| Operating bar | No silent cancellation. No engineer over the cap. Write-ups on time in all but one session. |

The skill sets the bar values, so they are my baselines, not industry figures. Nobody publishes office-hours attendance benchmarks. The bar is our own target.

## 2. Slot plan

- **Overlap.** US 09:00–18:00 and Paris 09:00–18:00 touch at one instant, so the overlap is empty. The cost goes to staff, not users.
- **Slot.** 12:00 ET is 09:00 PT, which puts both US coasts inside their working day. It is 18:00 Paris, so both hosts finish around 19:00 on session days.
- **Local times, winter.** 12:00 ET, 09:00 PT, 17:00 UTC, 18:00 Paris.
- **Local times, summer.** 12:00 ET, 09:00 PT, 16:00 UTC, 18:00 Paris.
- **Europe (20%).** Under the 25% trigger. 18:00 Paris is end of day, so people can join if they can. Their named path is the async intake and the write-up.
- **Elsewhere (10%).** Outside the window at this slot. Their named path is the async intake.
- **Pattern.** One slot plus async intake.
- **Second-slot trigger.** Any other region at or above 25% of active users, and the rotation can staff it within the cap. Then add an alternating Europe-morning slot. Re-run the region split at the pilot review and in Sep 2027.
- **Daylight saving.** Anchor the slot to ET and let Paris time move. The Paris gap shrinks by one hour from 14 to 28 Mar 2027, because the US changes clocks on 14 Mar and the EU on 28 Mar. The 25 Mar session is then at 17:00 Paris. Calendar invites must use the named time zone `America/New_York`.
- **Poll.** Poll the audience before publishing. Publish "12:00 ET / 09:00 PT" with a calendar link.

## 3. Rotation calendar (12 months)

Rules:

- Host and note-taker are H1 and H2. They swap the host role each session, and the other takes notes. If one is away, the host takes notes from chat afterwards.
- The month's spare engineer is the backup for every session that month.
- Engineers are credited by name and team in the session and the write-up.
- Each cycle follows this timeline (all baseline):

| When | Action |
|---|---|
| T-72h (Mon) | Nudge the intake thread with the engineer's name and area |
| T-48h (Tue) | Triage the queue. Send the engineer the prep brief and scope card. |
| T+2 business days (Mon) | Publish the write-up |

The AMA is separate (section 7). It uses the AMA panel in November, so no drop-in runs in November.

| # | Date (Thu) | Engineer | Spare | Host | Status |
|---|---|---|---|---|---|
| AMA | 5 Nov 2026 | Panel E1, E2, E3 | E4 | H1, H2 | v4 launch, section 7 |
| 1 | 3 Dec 2026 | E1 | E3 | H1 | Pilot |
| 2 | 17 Dec 2026 | E2 | E3 | H2 | Pilot |
| – | 31 Dec 2026 | – | – | – | Announced pause. Does not count. |
| 3 | 14 Jan 2027 | E3 | E1 | H1 | Pilot |
| 4 | 28 Jan 2027 | E4 | E1 | H2 | Pilot |
| 5 | 11 Feb 2027 | E2 | E4 | H1 | Pilot |
| 6 | 25 Feb 2027 | E1 | E4 | H2 | Pilot |
| – | 4 Mar 2027 | – | – | – | Pilot review |
| 7 | 11 Mar 2027 | E4 | E2 | H1 | Provisional |
| 8 | 25 Mar 2027 | E3 | E2 | H2 | Provisional (17:00 Paris) |
| 9 | 8 Apr 2027 | E1 | E3 | H1 | Provisional |
| 10 | 22 Apr 2027 | E2 | E3 | H2 | Provisional |
| 11 | 6 May 2027 | E3 | E1 | H1 | Provisional |
| 12 | 20 May 2027 | E4 | E1 | H2 | Provisional |
| 13 | 3 Jun 2027 | E2 | E4 | H1 | Provisional |
| 14 | 17 Jun 2027 | E1 | E4 | H2 | Provisional |
| 15 | 1 Jul 2027 | E4 | E1 | H1 | Provisional (3 sessions this month, 3 engineers) |
| 16 | 15 Jul 2027 | E3 | E1 | H2 | Provisional |
| 17 | 29 Jul 2027 | E2 | E1 | H1 | Provisional |
| – | 12 and 26 Aug 2027 | – | – | – | Announced summer pause. The async thread stays open. |
| 18 | 9 Sep 2027 | E1 | E2 | H2 | Provisional |
| 19 | 23 Sep 2027 | E4 | E2 | H1 | Provisional |
| 20 | 7 Oct 2027 | E2 | E3 | H2 | Provisional |
| 21 | 21 Oct 2027 | E3 | E4 | H1 | Provisional, 12-month review week |

Checks:

- No engineer has more than one session in any month. July is the tightest month, with 3 sessions and 3 engineers, so the spare is the fourth.
- Cap arithmetic: engineers (4) ≥ sessions per month (2) + 1.
- Quarterly checkpoints: 4 Mar 2027 (pilot), 3 Jun 2027 (re-run the region split), 16 Sep 2027 (annual review).
- **Before 1 Dec:** get each engineer's manager to agree to the cap in writing, and count the session as work in their review. Without that, "invited" engineers stop coming by week four.

## 4. Rules of the room

**Opening (every drop-in call).** The host opens with the code of conduct and the no-live-debugging line: "We can't see your systems, so no live debugging. Bring a minimal reproduction with secrets removed." The host also states that the call is not recorded and that the write-up is the record.

**Run of show (45 minutes, adapted from the Kubernetes run sheet):**

| Minute | Segment | Owner |
|---|---|---|
| -10 | Host and engineer in the room, screen-share tested | Host |
| 0 | Welcome, notice, code of conduct, no live debugging | Host |
| 2 | Engineer introduces themself in one line | Engineer |
| 4 | Pre-submitted questions, most widely useful first, 4-minute timebox each | Host reads, engineer answers |
| 25 | Live questions from chat or the room | Host moderates |
| 40 | Parking lot: what goes to the write-up, what was logged for product | Host |
| 43 | Next date, how to submit questions, thanks to the engineer and their team by name | Host |
| 45 | End on time | Host |

**Empty room.**

- Hold the slot even with an empty queue.
- If nobody joins in the first 10 minutes, answer the forum backlog for the write-up, then close. Log it as held with zero askers.
- If the engineer drops out, the spare takes the session. Cancel only when both are out, and announce it publicly.
- After two empty sessions in a row, change the slot and the promotion before the cadence.
- After three sessions under the bar, bring the pilot review forward.

**Difficult attendees.**

- One person with many questions: answer one, then "let's take others first and come back to you."
- Account issue: send them to `[SUPPORT]`.
- Live-debugging request: ask for an issue with a minimal reproduction.
- Sales or recruiting pitch: one warning, then removal.
- Harassment: the host removes first and explains later, under the code of conduct.
- Civil product complaint: log it with their words and say who decides.

**Async intake.** A pinned thread with a six-field form: the question, what you tried, product and version, read-aloud consent, time zone (optional), and follow-up contact (optional). The form never asks for logs, configs or screenshots. The pinned rule says "no logs, keys or customer data", and moderators can redact posts that break it.

**Promotion.** Announce about a week ahead, with the engineer's name and area. Bump the post the day before, and link the last write-up every time. Pin the intake thread the moment the previous write-up is published.

**Pauses and closure.** Announce pauses on every channel used for promotion. To end the program, publish a closure post, point to the async thread, and remove every calendar entry.

## 5. Metrics

| Signal | Target | Basis | Now |
|---|---|---|---|
| Sessions held / planned, and held with zero askers | All held, none cancelled silently | Baseline | Not measured yet |
| Distinct non-staff askers per cycle, live or async | Median ≥ 3 | Baseline, no published benchmark | Not measured yet |
| Questions answered, live and async | Every question answered or redirected | Baseline | Not measured yet |
| Write-up published | Within 2 business days | Baseline | Not measured yet |
| Merged docs fixes plus feedback records | ≥ 1 per 2 sessions | Baseline | Not measured yet |
| Engineer sessions per month | None over 1 | Baseline, after Kubernetes' 1 hour per month cap | Not measured yet |

**Counting rules.**

- Count distinct askers, not questions. One asker can bring ten.
- Do not report recording views as a metric.
- Open a docs ticket the second time any question family appears, in a session or any channel. Label the ticket `Office Hours` so the review can count it.

**Pilot review (4 Mar 2027).**

- Continue only if both demand-bar items hold.
- Operating-bar misses decide what to fix, never whether to stop.
- The AMA does not count toward the pilot. It is a different format with a different audience.
- Quote only sourced figures to leadership. Call the rest "our target".

## 6. Scope card (ready to publish)

The examples in "Bring" are illustrative. Replace them with five real questions from your last month.

> ## What to bring to Driftmark Office Hours
>
> **Bring:**
> - "My function's cold start got slower after upgrading to v4. What changed?"
> - "How do I share state between invocations safely?"
> - "What is the right way to stream a response from a function?"
> - "How do I migrate my v3 config to v4?"
> - "Is this deployment pattern safe at 500 routes?"
>
> **Not here:**
> - Account, billing, plan or contract questions go to `[SUPPORT]`.
> - Pricing, licensing and paid-tier features go to `[SALES]`. We can say what the public docs say. We say nothing about roadmap or price.
> - A suspected security vulnerability goes to `[SECURITY]`. Never raise it live or in a public thread.
> - A bug you can reproduce goes to `[ISSUES]`. Bring it and we will help you write the report.
> - A feature you need: we log it in `[FEEDBACK]`. The product team decides.
> - Debugging your own environment: we can't see it. Bring a minimal reproduction with secrets removed.
>
> Weekly drop-in calls are not recorded. A written summary is published within 2 business days. The launch AMA is recorded, captioned and published at `[where]` for `[retention]`. Our code of conduct applies: `[link]`.
>
> Questions about your own company's contract or code go to your support or account channel.

## 7. v4 launch AMA (one-off, folded in)

The skill designs standing programs, so I give only the scope card and room handling here. For stage, streaming and run production, use `virtual-event-production`.

**Placement.** Thu 5 Nov 2026, 12:00 ET / 09:00 PT / 17:00 UTC (winter-time offset, since US clocks change on 1 Nov), same slot as the program. It is the program's first public moment, so it opens the intake thread and feeds the first drop-in.

**Format.** Livestream panel, recorded and captioned.

- **Length.** 60 minutes. I chose this length. The skill's run sheet is 45 minutes, so add the extra 15 to the live-questions segment.
- **Panel.** Host (H1), notes (H2), three engineers (E1, E2, E3), and a 3-minute VP opening. The VP does not answer questions, which keeps roadmap out of the room.
- **Engineer load.** The panel counts as these engineers' November session. That is why no drop-in runs in November, and E4 is the spare.

**Cycle timeline.**

| When | Action |
|---|---|
| Thu 22 Oct (now) | Open the intake thread, pin the scope card, announce the date |
| Thu 29 Oct (T-7d) | Announce the panel by name and area |
| Mon 2 Nov (T-72h) | Nudge the intake thread |
| Tue 3 Nov (T-48h) | Triage the queue, send the prep brief |
| Wed 4 Nov (T-24h) | Cancel check. If no question has been submitted, cancel publicly or answer the forum backlog on air. |
| Mon 9 Nov | Publish the write-up (T+2 business days) |

**AMA-specific scope rules (decide with the VP):**

- Only shipped v4 behavior and public docs are answerable. Roadmap and unreleased features are logged in `[FEEDBACK]` and not answered.
- Pricing questions go to `[SALES]`.
- Customer-specific contract questions go to account channels.
- Nothing unreleased appears on screen.

**Recording.**

- Before the session, legal approves the notice and the retention period (no program publishes a GDPR template).
- The host reads the notice before recording starts and again when it starts, so late joiners hear it: "This session is recorded and published on `[where]` within 3 days, and kept `[how long]`. Keep your camera off and use the chat if you'd rather not appear, and we will read your question without your name. Don't share a screen showing tokens, customer data or internal hostnames."
- Offer camera-off, chat-only and anonymised questions.
- Before publishing, watch every screen-share for tokens, keys, internal hostnames and customer names. Cut or blur. Revoke any token shown in a demo environment.
- Honour every "don't read my name" request from the intake form.

**Room handling.** Same as section 4, with the VP's opening as the only extra segment. Dominant, off-topic and hostile attendees follow section 4.

**After.** Log every v4 question in the write-up. Open docs tickets for repeats, labelled `Office Hours`. The first drop-in on 3 Dec starts from the AMA write-up.

**Risk.** Pausing the weekly cadence until December leaves a four-week gap after the AMA. The async thread covers it, with answers batched in the write-up.

## 8. Session log and write-up (empty skeletons)

**Session log columns, one row per session:**

| Date | Held or cancelled | Distinct non-staff askers | Answered live | Answered async | Redirected | Docs tickets opened | Docs fixes merged | Feedback records | Engineer present | Write-up lag (days) |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

**Write-up, published where the intake thread lives:**

```
## Driftmark Office Hours - [date], with [engineer], [area]

### Answered
- **[Question, in the asker's words]** - [answer, 2-4 lines] - [docs link or new docs ticket]

### Answered here, not live
- **[Question]** - [answer]

### Redirected
- [Topic] -> [destination]. (No names.)

### Logged for the product team
- [Request or bug, in the user's words] -> [feedback record / issue link]

### Docs we are fixing
- [Page] - [what was missing] - [ticket]

Next session: [date, 12:00 ET / 09:00 PT, calendar link]. Submit questions: [link].
```

After the write-up is published, copy consented handles onto logged feature requests, then delete the raw session log.

## 9. Failure modes this plan guards against

| Failure | Guard in this plan |
|---|---|
| Host-time slot | Slot anchored to ET and PT, not Paris |
| Goodwill rotation | Written manager sign-off, cap, spare per month |
| Cap arithmetic | 4 engineers for a 2-per-month cadence, +1 spare |
| Support shadow | Scope card read at the start of every session |
| Disappearing slot | Drop-in is held even when the queue is empty |
| Silent cancellation | Pauses (31 Dec, August) announced on all channels |
| Answer and forget | Docs ticket on the second sighting of a question family |
| Launch-weekly | Biweekly cadence, pilot, demand gate |

## Do this next

Send me answers to the 8 open decisions, starting with regions (decision 1) and the engineer names (decision 3). Once I have those, I will rewrite the slot, the rotation and the scope card.