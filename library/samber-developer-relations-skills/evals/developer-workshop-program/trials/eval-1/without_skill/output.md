**Next action (10 min):** Ask the VP what "everything" meant to the CTO, and whether anyone else from Pelorus can join. Both answers change the agenda below.

## Read on the situation

- A full day on all of Pelorus will not fix their frustration. It is about two incidents.
- One SE can't teach 25 people everything in a day. Cover less, and tie it to the incidents.
- No champion and an absent CTO mean the day leaves no trace unless you plan one. Make the output a written artifact the CTO can read.
- Rename "covering everything" to **"Operating Pelorus reliably: lessons from Q3"**. Include a short map of the rest of the platform, and book later sessions for the deep dives. Clear this with the VP before the day.

## Prep (before Tuesday, about 4 hours)

1. Get both incident postmortems from support or engineering. Agree internally on what Pelorus owns and what the customer owns. **Don't improvise blame on the day.**
2. Hold a 30-minute call with 1–2 platform leads. Ask: which topics hurt most, what are the cluster setup, client libraries and versions, and who on-call handled the incidents? Treat the person who engages most as your champion.
3. Build a sandbox cluster that mirrors their setup (version, partitions, client libraries). Provision 25 seats or about 10 pairs.
4. Send the CTO a one-page agenda and a promise of a written summary on Wednesday.
5. Ask for a second Pelorus person (TAM or support engineer) to float during labs. With 25 people and one SE, hands-on stalls without one.

## Agenda (09:00–16:30)

| Time | Block | Output |
|---|---|---|
| 09:00–09:20 | **Kickoff.** Goal: make the next incident shorter or avoidable. Each person votes on topics via sticky notes or a poll. | Ranked topic list |
| 09:20–10:20 | **Incident walkthrough.** Timeline of both incidents, what happened, what Pelorus is changing, what they can change. Q&A. | Shared understanding, trust repair |
| 10:20–10:35 | Break | |
| 10:35–12:05 | **Lab 1: failure modes.** In pairs, reproduce the incident conditions on the sandbox (broker loss, consumer lag, rebalances, or whatever the postmortems show). Diagnose and recover. | Each pair completes recovery |
| 12:05–13:00 | Lunch | |
| 13:00–14:30 | **Lab 2: observability and alerting.** Build the dashboards and alerts that would have caught both incidents earlier. Draft an on-call runbook. | Alert list and runbook draft |
| 14:30–14:45 | Break | |
| 14:45–15:45 | **Config review clinic.** Small groups of 4–5 review their real configs against the voted topics (retention, quotas, client tuning, scaling). Bring your own configs. | Findings list |
| 15:45–16:30 | **Platform map and wrap-up.** 15-minute tour of the rest of Pelorus. Then follow-ups with owners and dates, a named champion, and dates for deep-dive sessions. | Action list with owners |

## Day-of rules

- Stay on schedule. A hands-on day with one SE slips fast. Cut the platform map before cutting a lab.
- Park anything off-topic on a visible "later" list.
- Don't promise roadmap, SLA credits or commercial terms. Route those to the VP.
- Don't demo features that didn't cause the incidents.

## After (Wednesday, about 1 hour)

Send the CTO a one-page summary: what was covered, runbook and alert drafts, findings, owners, and dates for follow-up sessions. This is your evidence for the renewal conversation.

## Open questions

1. Is Tuesday Nov 3, and how many days of prep do you actually have?
2. Do the postmortems exist, and are they cleared to share with the customer?
3. Can you get a second Pelorus person?
4. Can the VP get the CTO to join the first 20 minutes or the wrap-up? Even a short appearance changes whether the team takes the day seriously.

Answer questions 1 and 2 first. They decide whether Lab 1 can be built in time.