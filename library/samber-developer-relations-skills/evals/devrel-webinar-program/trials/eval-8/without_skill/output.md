# Marrowgate developer events program

I didn't read anything under `skill-wip/`. Numbers marked **(assumption)** are planning guesses, not measured baselines. Replace them after event 3.

## 1. Decisions

1. **Program:** one monthly live workshop, "Marrowgate Build Session", 60 minutes, hands-on, with a recording.
2. **Why events:** you have ~750 signups a month (9,000 a year), mostly self-serve from docs and GitHub. A workshop turns quiet signups into named people. It also gives sales the attendee list he asked for.
3. **Sales handoff:** no written lead rule, as he wants. He gets the attendee list as-is, plus plain facts per row (section 3).
4. **Time slot:** Wednesday 16:00 UK / 11:00 ET / 08:00 PT. This is the best single slot for US and UK together.
5. **Staffing:** you run it. Borrowed engineers appear on screen, 4 hours each per event (section 8).

## 2. Calendar (first 6 events)

| # | Date | Topic | Why this audience cares |
|---|------|-------|-------------------------|
| 1 | Wed 2026-11-18 | Add passkeys to an existing app in 45 minutes | High-intent, current topic |
| 2 | Wed 2026-12-09 | Move off a homegrown login without logging anyone out | Migration pain, a common docs/GitHub entry point |
| 3 | Wed 2027-01-20 | Multi-tenant B2B auth: orgs, roles, SSO | Where free-tier apps grow into paid |
| 4 | Wed 2027-02-17 | Session security: token rotation, MFA rollout, abuse limits | Security-minded teams |
| 5 | Wed 2027-03-10 | Auth for AI agents and MCP servers | Fresh topic, good for search and social |
| 6 | Wed 2027-04-14 | What happens at 1,000 MAU: scaling past the free tier | Directly commercial, so run it after trust is built |

**Date traps:**
- **UK clocks change on 2026-10-25 and 2027-03-28. US clocks change on 2026-11-01 and 2027-03-14.**
- For 1–2 weeks around each change the UK/US gap shifts by an hour. I avoided those weeks (Oct 26–30, Mar 15–26).
- I also skipped US Thanksgiving week (Nov 26) and the Dec 21–Jan 1 stretch.
- Put the time in each person's local zone on the registration page and in every email.

**Format of each session:**
- 0–5 min: the problem and the end state.
- 5–45 min: live build with an engineer. Everything runs on the free tier, so attendees can follow.
- 45–55 min: Q&A.
- 55–60 min: one next step and one link, with no pitch.

## 3. Sales handoff without a lead rule

**What he gets:** within 24 hours of each event, a shared sheet with one row per live attendee.

| Column | Source |
|--------|--------|
| Name, work email, company, country | Registration form |
| Minutes attended | Webinar platform |
| Asked a question (Y/N) | Q&A log |
| Has a Marrowgate account (Y/N) | Join on email |
| Current MAU, if account exists | Product data |
| Consent to sales contact (Y/N) | Registration checkbox |

- These are facts, not scores. He can sort and filter however he likes.
- **Only rows with consent = Y go to him.** This isn't a lead rule. It's a legal limit (section 6).
- No-shows get the recording email, not a sales call.

**Risk of having no rule:** in 3 months someone will ask "how many leads did events produce?" and there won't be an agreed answer. Your protection is the sheet. Every number you report is a count of rows or a filter on the facts above. Never call a row a "lead" or "qualified" in your reports. Say "attendees" and "attendees with an account."

**Your private measures** (internal, not a sales rule, he doesn't need to sign off):
- Registrations and attend rate.
- % of attendees with a Marrowgate account.
- Attendees who created an account within 14 days.
- Accounts whose MAU rose in the 30 days after the event.

## 4. Planning model (assumptions)

| Step | Assumption | Per event |
|------|------------|-----------|
| Registrations | 150–250 **(assumption)** | ~200 |
| Live attendance | 35–45% of registrants **(assumption)** | ~80 |
| Consent = Y | 50–70% of attendees **(assumption)** | ~50 |
| Existing accounts | 40–60% of attendees **(assumption)** | ~40 |

**Where registrations come from:**
- Email to the existing signup base. The 9,000 signups are your best list.
- A banner on the docs quickstart and relevant guides.
- A GitHub README link and a pinned Discussions post.
- A single social post a week before.

Review after event 3. If registrations are under 100, change the topic or promotion before changing the format.

## 5. Copy

### Registration page

> **Add passkeys to your app in 45 minutes**
> A live build with a Marrowgate engineer. Bring an app, leave with working passkey login.
> **Wed Nov 18, 16:00 UK / 11:00 ET / 08:00 PT** (shown in your time zone)
> You'll leave with: a working passkey flow, a fallback for older browsers, and the code.
> Free. Works on the free tier (up to 1,000 monthly active users). Recording sent to everyone who registers.
>
> Fields: name, work email, company, country.
> ☐ Marrowgate's team may contact me about my use of authentication. (Optional. Unchecked by default.)
> Privacy line: "We use your details to run this event and send the recording. Unsubscribe any time." Link to the privacy policy.

### Email sequence

**1. Confirmation (instant)**
Subject: You're in: passkeys, Nov 18
> You're registered for Wed Nov 18 at [local time].
> Add to calendar: [link]. Join link: [link].
> Bring an app, or use our starter repo: [link].
> Can't make it? We'll send the recording.

**2. Reminder (24 hours before)**
Subject: Tomorrow: build passkeys live
> Starts [local time] tomorrow. Two things to do beforehand: [create a free account] and [clone the starter repo]. Then you can follow along.

**3. Reminder (1 hour before)**
Subject: Starting in 1 hour
> Join link: [link]. We start on time and answer questions at the end.

**4. Attended (within 2 hours)**
Subject: Recording, code, and your next step
> Thanks for joining. Recording: [link]. Code: [link].
> One next step: [add passkeys to your own app: docs link].
> Questions we didn't get to are answered here: [link].

**5. No-show (next morning)**
Subject: You missed it. Here's the recording
> Recording: [link]. Code: [link]. Reply with questions. I read every one.

All emails go from you, a real person, not a no-reply address. Include an unsubscribe link and a postal address.

## 6. Consent and legal (US and UK)

I'm not a lawyer. Have counsel check this once.

- **UK GDPR and PECR:**
  - Say clearly what registration data is used for.
  - Sales contact needs its own explicit opt-in (the checkbox above), unchecked by default.
  - Marketing email to individuals or sole traders needs consent.
  - Marketing email to corporate addresses is allowed, but you must honor opt-outs.
- **US (CAN-SPAM):** include an unsubscribe link and postal address, and honor opt-outs within 10 business days.
- **Recordings:** announce at the start that the session is recorded. Don't show attendee names or faces.
- **Sharing with sales:** only rows with consent = Y. Log the consent timestamp in the sheet.
- **Retention:** delete registration data you don't use after 24 months.
- **Cookie/tracking:** accept only strictly necessary cookies on the registration page unless you've confirmed otherwise.

## 7. Runbook per event

Time estimates assume one person.

| When | Task | Time |
|------|------|------|
| T-21 days | Pick topic, book the engineer, publish page | 3 h |
| T-14 days | Email the signup base, add docs banner | 2 h |
| T-7 days | Social post, GitHub post, second email to non-openers | 1.5 h |
| T-3 days | Rehearse with the engineer on the free tier | 2 h |
| T-1 day | Reminder, test links and recording | 1 h |
| Day of | Run the session (60 min) plus 30 min setup | 1.5 h |
| T+2 hours | Send attended and no-show emails | 0.5 h |
| T+1 day | Build the sales sheet, send to him | 1.5 h |
| T+7 days | Record your private measures | 1 h |

**Total: about 14 hours per event.** Slide to 12 after event 3 by reusing the page and emails.

## 8. Borrowing engineers

- Ask for named people and fixed hours, not "help when possible."
- Per event: one presenter (1 hour live, 2 hours rehearsal, 1 hour prep) and one backup answering Q&A in chat (1 hour).
- Send the engineers the topic list now so they can plan around releases.
- Give them the questions asked in each session. This is their reward: real product feedback.
- Rule: no live build runs on code that hasn't passed a dry run the day before.

## 9. Success check after event 3 (early January)

- **Keep going if:** registrations hold at 100+ and at least a quarter of attendees have or create accounts.
- **Change the topic or promotion if:** registrations are under 100.
- **Rework the format if:** the attend rate is under 25%.
- Ask sales one question: "Did the sheet help you?" Don't ask him to define a lead.

## 10. Open questions

1. Which webinar platform do you already have? The attendee data in section 3 depends on it exporting minutes attended.
2. Can you join registrations to product data by email, and who owns that query?
3. Is there a privacy policy page that covers events?
4. Who approves the engineers' time, and does it start before Nov 18?

## 11. Next 5 actions

1. Confirm the platform and the product-data join (30 min).
2. Book the engineer for Nov 18 (15 min).
3. Publish the registration page by Oct 28, which gives three weeks of promotion (2 h).
4. Send the signup-base email on Nov 4 (1 h).
5. Send sales a mock of the sheet with fake rows so he can react before the real one arrives (30 min).