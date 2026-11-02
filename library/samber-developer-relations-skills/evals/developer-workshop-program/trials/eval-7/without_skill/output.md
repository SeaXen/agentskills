# What should happen now

**Short version:** don't run marketing's plan or the AE's deck as written. Follow up on behavior, through the champion, and keep SDR calls off the developers.

## Why not the current plan

- **Calling all 22 developers is the wrong move.** They came to learn, not to be sold to. An SDR call from the vendor can sour the champion's team and bypass the person who got you in the room.
- **Putting all 22 in the 6-email sequence ignores what you know.** 15 finished lab 2 and 7 didn't. Those groups need different messages.
- **Marketing consent is probably unresolved.** Attending a workshop doesn't clearly opt someone in to marketing. Calloway Health is healthcare, so be stricter. Check the registration form and the lawful basis before anything marketing-flavored goes out.
- **A deck is the wrong artifact for a champion.** They need something they can forward to their security lead, compliance team, and budget owner. A deck makes them translate it themselves.

## This week

**Day 0–1: thank-you from whoever ran the workshop (DevRel or engineer, not sales)**
1. Send all 22 a transactional follow-up. This is service, not marketing.
2. Include the lab repo and solutions, the docs links, and a sandbox or API key that stays active.
3. Add one line: "Reply if you got stuck anywhere."

**Day 1–2: split the 22 by behavior**

| Group | Size | Action |
|---|---|---|
| Finished lab 2 | 15 | Send a technical next step: the production-readiness checklist, a "build X next" guide, and a community or Slack invite. Offer a 30-minute architecture Q&A. |
| Stopped before lab 2 ends | 7 | Ask where they got stuck, from a person, not an automated email. Log the friction. A lab-2 failure pattern is a product or docs finding. |
| Any attendee who has made API calls since | ? | Flag them as the real signal. Check sandbox logs. |

**Day 2–3: AE and champion, one document**
- Skip the deck. Send a short summary the champion can forward internally:
  1. What happened (22 attended, 15 completed, what they built).
  2. What the team can do now (the working integration).
  3. Proposed next step, small and concrete: a scoped pilot, a security and compliance review, or a second session.
  4. What you need from them: who owns security review, who owns budget, and the timeline.
- Ask the champion directly:
  - Which of the 22 would own the integration?
  - Who else must say yes (security, compliance, procurement)?
  - Do they want you to contact the attendees, or do they prefer to route it themselves?
- For healthcare identity, expect questions about a BAA, data residency, audit logging, and the security questionnaire. Offer the security packet before they ask.

**Week 2 onward: nurture, rebuilt**
- Replace the generic 6-email sequence with 3 touches triggered by behavior:
  1. A "next build" guide, sent after lab completion.
  2. A production and compliance guide, sent when they make a second API call or the champion asks.
  3. A customer story or office hours invite.
- Include only people who opted in or whose consent basis is clear.
- Stop the sequence for anyone who replies or whose account is in an active deal conversation.

## Role of the SDRs

- No calls to the 22 developers this week.
- Use them for account mapping instead: who the economic buyer, security owner, and compliance owner are at Calloway, and what other teams have identity problems. Do it through the champion's introductions or LinkedIn.
- A call becomes appropriate when the champion introduces someone or an attendee asks for pricing or a pilot.

## What to measure over 30 days

- Sandbox or API activity per attendee, not email opens.
- Number of attendees still active at day 14 and day 30.
- Whether a second team or an owner beyond the champion appears.
- Whether the security or compliance review has started.
- The champion's own response and speed.

The 15/22 completion rate is a good workshop result. It is not pipeline. The next step that counts is the champion getting a security review, a pilot, or a budget owner in motion.

## Questions to confirm before you send anything

1. Did the registration form include marketing consent, and in which jurisdiction are the attendees?
2. Is Calloway already a paying customer, a trial, or a prospect? That changes who owns the follow-up.
3. Did the champion ask for a deck, or did the AE assume it?
4. Do you have per-attendee lab and sandbox data, or only the headcount?