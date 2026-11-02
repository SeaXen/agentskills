**Next (15 min):** read "Open decisions", answer the five marked ⚠️, then send the sales one-pager (§5) to your head of sales.

# Marrowgate developer webinar series: full program

## Open decisions and assumptions

You gave no interview answers, so I inferred them. Correct any wrong one and the plan changes where noted.

| # | Item | Status | Changes if wrong |
|---|---|---|---|
| 1 | Job = **activation** (you named a free tier). Secondary: feature depth | assumed | Format ranking |
| 2 | ⚠️ No past episodes, so no baseline and no diagnosis | assumed | Add past episodes to the log (§6) |
| 3 | ⚠️ DevRel gives ≤25 h/month at peak. Three borrowed engineers give ≤3 h/month each, on a bad month | assumed | Cadence (§2) |
| 4 | ⚠️ Region split: 60% US, 30% UK, 10% other | assumed | Slot, second-region repeat |
| 5 | ⚠️ No partner or sponsor co-hosts this season | assumed | Joint-controller arrangement needed before any partner logo |
| 6 | 🔴 **Sales owner for a handoff: none.** Your head of sales refuses a written rule | open | Sales route stays off (§5) |
| 7 | Job metric = first successful end-user login through the API within 30 days of registering | assumed | Swap in your real "first meaningful action" |
| 8 | Budget amounts, platform choice, captioning vendor | open | Fill the §2 budget line |
| 9 | Topics are hypotheses until checked against real GitHub issues, discussions and docs-search misses | open | Re-score the backlog in week 1 |
| 10 | Legal review of the form notice and retention period | open | Wording in §5 |

---

## 1. Diagnosis

You brought no attendance numbers, so there is nothing to diagnose. The inputs and what to do with them:

- **Signups:** 9,000/year is about 750/month. Registrants come from docs and GitHub, so they are your own users and community. That is the best-intent source, and paid ads are not needed.
- **Benchmark:** no vendor figure fits your mix. Do not judge episode 1 against ON24's 60% or Demio's 22%. Use the median of episodes 1 and 2 as your baseline.
- **Refused statistics:** if anyone quotes "38% of attendees become MQLs" or "35-45% average attendance", refuse them. They trace to no study.
- **First read after each episode:** run the Step 6 pattern check.
  - Low registration and low attendance: the topic is wrong.
  - Healthy registration, low live, healthy replay: your audience prefers on demand.
  - Healthy registration, low live, low replay: the registrants came from the wrong source.
- **Tag every registration link by source:** docs banner, GitHub README, GitHub Discussions, onboarding email, newsletter, social. Attendance per source is the diagnostic that matters.

---

## 2. Charter

```
Series name: Marrowgate Auth Sessions
Job (first): activation of free-tier developers
Secondary: feature depth for existing users
Audience: backend and full-stack developers adding auth to an API; intermediate;
  ~60% US, ~30% UK, ~10% other (assumed)
Format mix: live demo and engineer conversation alternating; one follow-along lab
  per season on the free tier. Moved by Q1 (activation) and Q4 (free tier exists).
  Panel deleted (no moderator prep time). Customer story deferred to season 2
  (approval wait, 6-8 weeks).
Cadence and length: monthly, 40 min; lab 55 min
Slot: Tuesday 11:00 ET (16:00 UK). Test slot: Thursday 11:00 ET, episodes 3 and 5 only.
  16 Mar 2027 falls in the US/UK clock gap (US moves 14 Mar, UK 28 Mar): announce
  15:00 UK for that episode.
Season 1: 5 episodes, 19 Jan to 18 May 2027
Speaker pool: 3 borrowed engineers (manager-agreed, 3 h/month each),
  1 community answerer from GitHub; named backup per episode (§3)
Replay policy: ungated chaptered copy on the public video channel within 48 h;
  captions + transcript; 2 clips per episode; lab starter repo open; recording never gated
Budget (fill amounts): platform __ ; paid promotion 0 (owned channels only);
  lab infrastructure ~0 (attendees use their own free-tier account, plus one fallback
  tenant); captioning __ ; honoraria 0 (swag for the community speaker)
Data retention: registrant and engagement data deleted 12 months after season end (baseline)
Handoff contract: drafted, UNSIGNED, sales route OFF (§5)
Continue bar (written before episode 1):
  - total reach, live attendance, returning share: none below the median of episodes 1-2
    on two of episodes 3-5. From season 2: against the prior season, three in a row
  - returning-attendee share: 20% or more by episode 4 (baseline; replace after season 1)
  - job metric: attendees' 30-day first-login rate ahead of matched non-attendees
    (same signup week, same source), pooled over the season
  - stop rule: two seasons failing the job metric, or no backlog for a season
Open decisions: see table above
```

### Why monthly

Cadence is set from capacity, not the marketing calendar. Effort figures are baseline orders of magnitude.

| Episode | Format | Staff hours incl. replay and clips |
|---|---|---|
| 1 | Demo | ~7 |
| 2 | Engineer conversation | ~11 |
| 3 | Lab, first run | ~24 |
| 4 | Engineer conversation | ~11 |
| 5 | Demo | ~7 |

- Season total is about 60 h, or about 12 h/month on average. Peak is about 24 h in March, which fits your 25 h ceiling.
- Bi-weekly doubles that and needs a full-season backlog plus a backup speaker per slot. You have neither yet, so stay monthly.
- The lab sits in episode 3 so it gets eight weeks of prep.

### Promotion

Rank: own users and newsletter, then community channels, then speakers' audiences, then social. No paid in season 1.

1. Open registration 3-4 weeks ahead and keep it open until the start. About half of registrations arrive in the final 7 days (Livestorm: 49.6%).
2. Put most effort into the final week.
3. Add a docs banner and a GitHub README line to the onboarding email sent to new signups.
4. Post in GitHub Discussions.
5. Ask each speaker to promote to their own audience.

### Causal read

Hold back a random 15% of the onboarding-email invite for the whole season. Over 5 months that is about 3,750 signups, so about 560 are held out.

The docs banner and GitHub can't be held out, so read the result as directional.

---

## 3. Season plan (season 1 firm; season 2 provisional)

| # | Date | Format | Topic (titled by problem) | Speaker | Backup | Replay | Job signal |
|---|---|---|---|---|---|---|---|
| 1 | Tue 19 Jan 2027 | Live demo | Add signup and login to a Node API in 30 minutes, no password table | DevRel (you) | Eng A + recorded fallback | Chaptered + 2 clips | First-login rate of attendees |
| 2 | Tue 16 Feb | Engineer conversation | Refresh token rotation: stopping a stolen token from living for 30 days | Eng A | Eng B | Chaptered + 2 clips | Docs visits to token pages |
| 3 | Tue 16 Mar (15:00 UK) | Follow-along lab, 55 min | Build a protected API with scoped tokens and MFA step-up on the free tier | DevRel + Eng B in chat | Eng C | Chaptered, re-runnable lab | Lab completions, first logins |
| 4 | Tue 20 Apr | Engineer conversation | Migrating off a homegrown password table without forcing a reset | Eng C | Eng A | Chaptered + 2 clips | Returning share ≥20% |
| 5 | Tue 18 May | Live demo + 20-min community guest | Debug a 401 end to end: reading auth logs | DevRel + community answerer | Eng B | Chaptered + 2 clips | First login after docs search |

- ⚠️ Confirm Marrowgate ships scoped tokens, MFA step-up and token rotation before announcing episodes 2 and 3. I assumed they exist.
- No release episode this season (limit: under a third). Keep a swap slot: if a major release lands, swap episode 5 and clip it within days.
- Episode 3 gets the Thursday test slot for the lab only if you can support two time zones. Otherwise skip the test.
- Run each live demo through the live-demo reliability checks: checkpoints, reset, recorded fallback.
- Episode skeletons:
  - **Engineer conversation:** 0-3 min the problem; 3-25 min five prepared questions; 25-35 min audience; 35-40 min one next step.
  - **Demo:** same shape, with one realistic scenario in the middle.
  - **Lab:** 0-5 min setup check; 5-35 min build with checkpoints and copy-paste catch-ups; 35-45 min questions.
- Pre-lab email with the final reminder: free-tier account, tool versions, a test command.
- Open every episode with the problem and the payoff, not housekeeping.

### Speaker handling

- Agree hours with each engineer's manager before the first ask. Credit engineer and team by name on the page.
- Send the brief one week ahead: the episode's takeaway, audience level, three likely questions, no pitch, and what the host may say about follow-up.
- Get a recording release from every speaker, staff included.
- Community guest: invite your top GitHub issue or Discussions answerer. Offer setup, recording and promotion, and a copy of the recording.
- Customer for season 2: if you want one, start approval by 1 Mar 2027, which is 6-8 weeks ahead.
- Speaker outreach email, internal engineer:
  > Subject: 40 minutes on token rotation for our Auth Sessions on 16 Feb
  > <Name>, developers keep asking how to stop a stolen refresh token from living for 30 days. You built the part that answers it. Would you join me for a 40-minute conversation on Tue 16 Feb at 11:00 ET? Prep is one 30-minute call and five questions sent a week ahead. <Manager> has agreed the time. Backup date: 23 Feb.

---

## 4. Topic backlog

Hypotheses. Re-score against real GitHub issues, Discussions, docs-search misses and the signup step with the biggest drop. Scores are 0-2 per column.

| Topic | Job fit | Devs affected | Speaker exists | Replay life > 1 quarter | Total | Slot |
|---|---|---|---|---|---|---|
| Debug a 401 end to end | 2 | 2 | 2 | 2 | 8 | Ep 5 |
| Login on a Node API in 30 min | 2 | 2 | 2 | 1 | 7 | Ep 1 |
| Refresh token rotation | 2 | 2 | 1 | 2 | 7 | Ep 2 |
| Scoped tokens + MFA step-up lab | 2 | 2 | 2 | 1 | 7 | Ep 3 |
| Homegrown password table migration | 2 | 2 | 1 | 2 | 7 | Ep 4 |
| Sessions or JWTs: pick in 10 minutes | 1 | 2 | 2 | 2 | 7 | S2 |
| Rate limits and lockout without locking out real users | 1 | 2 | 1 | 2 | 6 | S2 |
| Ask the auth engineers: top 10 GitHub questions | 1 | 2 | 2 | 1 | 6 | S2 (needs standing question backlog) |
| Multi-tenant auth: one user, many orgs | 1 | 1 | 1 | 2 | 5 | S2 |
| What the next release changes in your app | 1 | 1 | 2 | 0 | 4 | Reserve |

- Ep 5 holds the top score on purpose. By May, four months of 401 questions have piled up in GitHub to ground it. It also costs the least prep, so it can move earlier on a bad month.
- Sources, in order: repeated community questions, onboarding friction, engineering war stories, releases.
- Scan monthly: top GitHub questions, no-result docs searches, the biggest trial drop.

---

## 5. Handoff contract

🔴 Your head of sales will not sign a written rule. So the sales route is **off**. The series ships, attendee data goes to product nurture only, and the open decision is logged.

### Contract (drafted, unsigned)

```
Series: Marrowgate Auth Sessions          Season: 19 Jan to 18 May 2027
Series job (first): activation
DevRel owner: <you>                       Sales owner: NONE (open decision)

Tier A - hand-raise
  Signal: attendee asks for a demo, pricing or contact
  Route: SUSPENDED until signed. Interim: the in-session CTA links to the
         existing contact-sales form, tagged by episode. The attendee fills it
         in themselves. The webinar tool passes nothing to sales.
  Once signed: sales queue, within 1 business day, with episode + question asked
Tier B - engaged, open account
  Route: SUSPENDED. Once signed: account owner notified, no cold call, next working day
Tier C - engaged (top third by watch share, questions, resource clicks)
  Route: product activation nurture (lab link, docs path), ONLY if the marketing box
         is ticked. Owner: DevRel
Tier D - registered
  Route: the replay email they registered for

Never routed to sales: Tiers C and D, unless they later meet Tier A.
Acceptance bar (once signed): __% of Tier A accepted; read back each episode.
Opt-out: honoured within 5 business days across every tool (baseline).
Retention: data deleted 12 months after season end (baseline).
LIA for sales calls and account notes: not needed while the route is off.
  Required before it turns on.
Signed: ____ ____ date ____
```

Define "engaged" after episodes 1-2, so it holds roughly the top third of attendees.

### Registration form

Fields: name, email, and one qualifying field: **primary language** (Node, Python, Go, other). Its use is to pick the lab and demo language. Work email is not required, since hobbyists and students have none.

Notice (legal review needed):
> Hosted by Marrowgate. The session is recorded and the recording is published on our public video channel. We record attendance, watch time, questions and clicks to decide what follow-up to send you. Your details are not passed to our sales team from this registration. [Privacy notice link]. Data is kept 12 months after the season ends. Opt out any time.
>
> ☐ Send me product emails from Marrowgate. *(unticked)*

- Never pre-tick the box.
- Route marketing email on the box alone. That rule holds in every region, and the form can't tell the registrant's country.
- The lab's free-tier sign-up needs its own privacy notice.
- Region notes for your US/UK audience, for legal to confirm:
  - **US:** opt-out regime (CAN-SPAM). Identify the sender, give a working unsubscribe, honour it within 10 business days.
  - **UK:** corporate addresses may rely on notice plus opt-out (PECR). Sole traders and some partnerships need consent.
  - **UK guidance:** check current ICO guidance after the Data (Use and Access) Act 2025.
  - **EU or Canada registrants:** the unticked box already covers them.
- If a partner later co-hosts: name them on the form, add their own unticked box, and sign a joint-controller arrangement first. Never hand a sponsor the full list.

### Sales one-pager (send this)

> **Subject: Webinar series: what you get from episode 1**
>
> Attendee lists don't go to sales without a rule, because registrants were never told sales would contact them. So from episode 1 you get:
> 1. Anyone who wants pricing or a demo reaches you through the contact-sales form, tagged by episode.
> 2. A per-episode report with counts, and the questions asked (anonymised).
>
> If you'll sign four lines (hand-raise → you within 1 business day; open-account attendees → notify the account owner; nobody else), I turn on named hand-raises and open-account notes from the next episode. You get a few named leads with their questions, not 66 cold ones. Template attached.

- Why not "every attendee is an MQL": sales works leads that never asked, developers who get a call after a technical session stop registering, and the series gets judged on volume its job doesn't need.
- If he says "they gave us their email, so they expect a call": the form's notice and local email rules decide that, not the registration.

---

## 6. Episode log

Past episodes (pilot baseline): none. Future rows empty.

| Episode | Date | Registrants by source (docs / GitHub / email / newsletter / social / community) | Live | Live / registrants | 30-day on-demand (platform + public copy) | Total reach | Returning attendees | Live completion | Replay completion | Questions per 10 live | Tier A / accepted | Replay published (h) | Job metric (30-day first login) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 19 Jan 2027 | | | | | | | | | | | | |
| 2 | 16 Feb | | | | | | | | | | | | |
| 3 | 16 Mar | | | | | | | | | | | | |
| 4 | 20 Apr | | | | | | | | | | | | |
| 5 | 18 May | | | | | | | | | | | | |

- Label views from a public video copy "upper bound" when unique viewers aren't reported.
- Tag every link in the replay description and follow-up email by episode.
- Never report registrations alone.
- Season review (the week after 18 May): continue unchanged only if all four hold.
  1. No reach, live-attendance or returning-share metric is below baseline.
  2. The job metric moved in attendees' favour.
  3. Every replay shipped within 48 h.
  4. The next season's backlog and speakers are booked.
- If one fails, apply the fix: topic and format first, then slot, then cadence.

---

## Season 2 (provisional)

- Starting ~1 Mar 2027 (provisional), approve one customer story if a customer is willing.
- Topics: sessions vs JWTs, rate limits and lockout, Q&A on top GitHub questions (only once a standing question backlog exists), multi-tenant.
- If the contract is signed, Tier A and B turn on and acceptance is read back each episode.

## Timeline for you

| When | Task | Time |
|---|---|---|
| This week | Answer ⚠️ decisions, send §5 one-pager | 30 min |
| This week | Ask managers for the engineer hours, send the three outreach emails | 1 h |
| By 15 Nov | Re-score the backlog on real GitHub, Discussions and docs-search data | 2-3 h |
| By 15 Dec | Build the registration page with the §5 form and UTM tags | 2 h |
| Mon 21 Dec to Fri 1 Jan | Hold: don't schedule anything | None |
| From 22 Dec | Open registration for episode 1 (4 weeks ahead) | 30 min |

Next: send the sales one-pager and the first outreach email.