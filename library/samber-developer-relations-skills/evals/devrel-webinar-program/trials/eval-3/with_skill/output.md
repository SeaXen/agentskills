Do this first: send Fjordline and Northgate the verdicts below before their logos go on the registration page. Estimate: 1 hour to redraft the form and clauses, plus legal review time.

## Verdicts

| Ask | Verdict |
| --- | --- |
| Add "current cloud provider" and "monthly cloud spend" | Provider: yes, one optional dropdown. Spend: no. |
| Full registrant CSV 24 hours after | No. Send only rows that ticked the Fjordline box, plus aggregate counts for everyone. |
| Fjordline runs the follow-up sequence | Yes, only to rows that ticked the Fjordline box. Tidewater sends everyone else the replay email. |
| Northgate "sponsor receives attendee list" | Reject the clause. Replace it with the clause in section 3. |
| 1,900 past registrants to Fjordline | No. They never saw Fjordline's name. Fjordline gets zero of those rows. |

## Assumptions (open decisions, confirm each)

1. Series job is feature depth. Your request names no free tier, trial or open deals, so the skill's default applies.
2. Tidewater is one legal entity and owns the registration page. Fjordline does not run its own form.
3. The past 8 episodes ran on a form that only linked your privacy notice. Registrants saw no sales-contact or partner disclosure and no marketing box.
4. Episode date is next month (November 2026). Slot and time are open.
5. 1,900 is cumulative registrations, not unique people. Dedupe by email before any count.
6. Series was not in "seasons" before. Treat this episode as the start of season 2 and the past 8 as the pilot baseline.

## Why Fjordline is a joint controller

Fjordline asked to decide form fields and to run follow-up. That makes both companies joint controllers (EDPB Guidelines 07/2020). Both need a written arrangement under GDPR Art. 26 before Fjordline's logo goes on the page. The arrangement must say who answers access and deletion requests, and within how long.

## 1. Charter

```
Series name: <Tidewater episode series>   (open decision)
Job (first): feature depth. Secondary: none.   (assumed)
Audience: data and backend engineers, intermediate; region split open decision
Format mix: live demo (feature depth ranks it first). One partner-speaker segment from
  Fjordline inside the demo. No panel.
Cadence and length: monthly, 40 minutes
Slot: open decision. Anchor in the larger developer region's working day.
Season: this episode starts a new season. Plan 4-6 episodes; later rows provisional.
Speaker pool: Tidewater engineer + backup; Fjordline engineer (partner, co-host rules apply)
Replay policy: ungated chaptered copy within 48 h, captions and transcript,
  2 clips, no gate on the recording
Budget: platform, captioning, Fjordline demo infrastructure (who pays: open decision)
Data retention: registrant and engagement data deleted 12 months after season end (baseline).
  Same period binds Fjordline for rows it receives.
Handoff contract: section 3, sign with a named Tidewater sales owner before the page opens
Continue bar (write before episode 1):
  - no metric among total reach, live attendance, returning share below the pilot median
    on two of the later episodes
  - returning-attendee share bar: set from the first two episodes of this season
  - job metric: feature adoption among attendee accounts, ahead of matched non-attendees
  - stop rule: two seasons failing the job metric, or no backlog for a season
Open decisions: Fjordline joint arrangement signed; Northgate contract redrafted;
  past-registrant notice reviewed by legal; slot; sales owner named
```

## 2. Registration form

Fields: name, work email (optional only if Tier B matching is not needed), and one optional qualifying field.

- **Cloud provider:** optional dropdown. Keep it only if Tidewater states a use, such as choosing demo targets.
- **Monthly cloud spend:** drop it. Tidewater has no use for it, and spend questions cut developer registrations. Fjordline can ask spend on its own form, after a hand-raise.
- If Fjordline insists, offer an in-session poll. Share only aggregate results.

Add this notice above the submit button:

> This session is hosted by Tidewater Data with Fjordline Cloud. We record it and publish the recording on our public video channel. We record attendance, watch time, questions and clicks, and use them to decide follow-up. Tidewater's sales team may contact you about this topic. You can opt out any time. We keep this data for 12 months after the season ends. Privacy notices: Tidewater [link], Fjordline [link].

Add three separate boxes. All unticked. None is a condition of registering.

- [ ] Email me product news and future episodes from Tidewater Data.
- [ ] Share my name, email and cloud provider with Fjordline Cloud so Fjordline can email me about its services.
- [ ] Northgate Tooling box: only if section 3 option (b) is chosen. Name Northgate.

Never pre-tick any box.

## 3. Handoff contract

```
Series: <name>                      Season: <dates>
Series job (first): feature depth
DevRel owner: <name>                Sales owner (Tidewater): <name, open decision>

Tier A - hand-raise
  Signal: asked for a demo, pricing or contact; clicked a Tidewater pricing/demo CTA
  Route: Tidewater sales queue   SLA: 1 business day
  Payload: episode, question asked, resources clicked
Tier B - engaged, open account
  Signal: engaged attendee or registered replay viewer AND account has open opportunity
  Route: account owner notification, no cold sequence
Tier C - engaged
  Signal: top third of attendees by watch share, questions, resource clicks (set from
    first two episodes)
  Route: feature-depth nurture, only for registrants who ticked the Tidewater marketing box
Tier D - registered
  Route: the replay email they registered for

Partner rows (Fjordline)
  Signal: ticked the Fjordline box, or clicked a Fjordline CTA during the session
  Route: export of those rows only, at 24 h after the session
  Columns: name, email, cloud provider (if given), box timestamp, episode
  Fjordline sends from its own tools, under its own basis, naming Tidewater as the source
  Fjordline never receives: unticked rows, watch time, questions, other attendees' data
Sponsor rows (Northgate)
  Signal: ticked the Northgate box, or requested contact from Northgate in session
  Route: those rows only. Northgate is a separate controller.

Never routed to sales: Tier C and D, unless they later meet Tier A.
Sales acceptance bar: 50% of Tier A accepted (baseline); read back after each episode.
Review: at season end, tighten Tier A if acceptance stays under the bar.
Opt-out: honoured within 5 business days across Tidewater, Fjordline and Northgate (baseline).
Retention: 12 months after the season ends, at all three parties.
Legitimate-interest assessment for sales calls and account notes: <link, date>. (open decision)
Joint arrangement with Fjordline (GDPR Art. 26): <link, date>. (must exist before launch)
Signed: <DevRel owner> <Sales owner> <date>
```

### Northgate clause

Reject: "sponsor receives attendee list." Replace with:

> Sponsor receives (a) an aggregate report within 5 business days: registrations, live attendance, and clicks on sponsor materials; and (b) contact details of individuals who ticked the box naming Sponsor, or who requested contact from Sponsor during the session. Sponsor acts as an independent controller for those details. No other personal data is disclosed.

Two alternatives that keep the $6k whole:

- **Sponsor-run capture:** attendees click "get Northgate's guide" and land on Northgate's own form. Tidewater shares no personal data.
- **Live slot:** give Northgate a labelled 3-minute segment, with the no-pitch rule and one call to action.

## 4. Past registrants (1,900)

1. Fjordline gets none of them. Consent must name the recipient, and these people never saw Fjordline's name.
2. Do not email them an invitation yet. Tidewater may only follow up under the notice they saw, and a link to a privacy notice may not cover marketing email. Legal reads the old notice (open decision).
3. If legal clears it, send one email with the replay link and the new notice, from Tidewater only.
4. They can still register through the new form and tick the Fjordline box themselves.
5. Fjordline can promote the episode to its own list. Those people register on your form and see both names.

## 5. Season plan (provisional)

| # | Date | Format | Problem-titled topic | Speaker | Backup | Replay type | Job signal to watch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Nov 2026, open | Live demo | Running a streaming SQL job on commodity hosting: state, checkpoints, failure recovery (proposed) | Tidewater engineer + Fjordline engineer | Named by you | Ungated chaptered copy + 2 clips | Feature adoption at attendee accounts |

Rows 2-5 stay empty until you set a backlog. Keep release episodes under a third of the rows.

## 6. Topic backlog

Out of scope for this question, and it needs your community questions and docs search data. Next season is blocked until you have a full season of topics.

## 7. Episode log

Enter the 8 past episodes as the pilot baseline. Future rows stay empty. Pull registrants, live and replay figures from your platform.

| Episode | Registrants by source | Live | Live / registrants | 30-day on-demand (platform + public copy) | Total reach | Returning attendees | Live completion | Replay completion | Questions | Tier A / accepted | Replay published (h) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

I skipped the diagnosis section because you gave no attendance numbers. I did not check any law beyond the skill's reference notes, so legal owns the final wording of the form, the arrangement and the Northgate clause.

Next step: send Fjordline the verdict table and the joint-arrangement request. It takes about 10 minutes.