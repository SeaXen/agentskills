# Hollowmere developer webinar series: charter (draft v0.1, 2026-10-23)

**Decisions needed from you before this is final:** the six open decisions at the bottom. The most important is the **weekly vs monthly** call, which changes the marketing ask.

## Assumed (you didn't say, so please confirm)

- The first episode is **Tue 2026-11-17**, which is 25 days out. If v3 ships earlier, move it to Tue 11-10. That leaves 18 days of registration.
- "6 h/month each" is the bad-month figure, and I plan every month at it. Capacity is 12 h (two advocates) + 6 h (three engineers) = **18 h/month**.
- Hollowmere has no webinar history, so the first two episodes set the baseline.
- No budget has been named. Every money line is an open decision.

## Recommendation to marketing: monthly, not weekly

Cadence comes from capacity, not from the marketing calendar. A rough cost per episode, including follow-up, using this skill's order-of-magnitude figures:

| Format | Staff hours per episode |
| --- | --- |
| Q&A episode | about 3 |
| Live demo | about 4–6 |
| Engineer conversation | about 8 |
| Follow-along lab (first run) | about 16–24 |

- **Weekly means 4–5 episodes a month.**
  - Only Q&A is cheap enough to do weekly, at about 13–15 h/month.
  - That uses almost all 18 h and leaves nothing for the lab, the format with the highest activation value.
  - A Q&A-only series is an office-hours program, not this one.
- **Weekly demos and conversations cost 25–40 h/month.** That is more than double what the team has.
- **What marketing gets instead:** one live episode a month, plus 2–3 clips per episode and a chaptered replay within 48 h. That gives a steady touchpoint without a weekly live show.
- **When bi-weekly becomes possible:** only after a full season's backlog and a named backup for every slot are in place. Review that at the season-one review.

## Charter

```
Series name:        Hollowmere Live (working title)
Job (first):        Activation: a new signup creates their first flag
Secondary jobs:     none in season one
Audience:           Backend and full-stack developers on the free tier or just signed up,
                    beginner to intermediate. 60% North America, 30% Europe, 10% elsewhere.
Format mix:         Alternate live demo and engineer conversation, plus one follow-along lab
                    (the job is activation and the free tier, up to 5 seats, can host
                    the lab). One release episode only (episode 1), under a third of the
                    season. No panel (no one has prep time to moderate). No customer story
                    in season one (approval takes weeks, and the effort is highest for
                    this team).
Cadence, length:    Monthly, 40 minutes. The lab runs 55 minutes.
Slot:               Tuesday 11:00 ET (17:00 Paris, 16:00 London, from 2026-11-01 until 2027-03-08).
                    Test a second slot only on two episodes of the same format, after season one.
                    The rest of the world gets the replay.
Season 1:           4 episodes, 2026-11-17 to 2027-02-16. Review the week of 02-22.
Speaker pool:       Internal: 2 advocates host and demo; 3 backend engineers (2 h/month each,
                    manager-agreed), credited by name. Community: none yet, so recruit
                    forum answerers for season 2. Named backup for every episode (see plan).
Replay policy:      Ungated chaptered copy on the public video channel within 48 h, with
                    captions, transcript, code, and links tagged per episode. 2–3 clips per
                    episode. Only the lab environment and starter repo sit behind free-tier
                    sign-up. That gate is the activation step, so it costs no reach. No gated recordings.
Budget:             Platform <open>; paid promotion $0 in season one (own users first);
                    lab infrastructure <open, near-zero if it runs on free-tier accounts>;
                    captioning <open, or live captions from the platform>; honoraria $0.
Data retention:     Registrant and engagement data deleted 12 months after season end (baseline).
Handoff contract:   Drafted below. Not signed: no named sales owner yet.
Continue bar (set before episode 1):
  - Total reach, live attendance and returning-attendee share: none falls below the
    median of episodes 1–2 on BOTH episodes 3 and 4.
  - Returning-attendee share: 20% or more by episode 4 (baseline).
  - Job metric: attendees' 30-day first-flag rate is ahead of matched non-attendees
    (same signup week and source), pooled over the season. Directional, not causal.
  - Replay published within 48 h on every episode.
  - Next season's topics and speakers booked.
  - Stop rule: two consecutive seasons failing the job metric, or no backlog for a season.
```

## Season 1 plan (provisional)

| # | Date | Format | Problem-titled topic (proposed, validate against forum and onboarding data) | Speaker / backup | Replay | Hours |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 11-17 | Live demo (v3 release) | From signup to your first live flag in 30 minutes | Priya / advocate 2 | Chaptered + clips | ~6 |
| 2 | 12-15 | Engineer conversation | Why a flag check shouldn't slow your request path | Engineer A / engineer B | Chaptered + clips | ~8 (advocate 6, engineer 2) |
| 3 | 01-19 | Follow-along lab | Build a kill switch and a percentage rollout on the free tier | Advocate 2 hosts, Priya answers chat / swap | Chaptered + gated env; EU re-run as scheduled replay | ~22 (prep starts in Dec) |
| 4 | 02-16 | Live demo | Remove a flag six months later without breaking anything | Priya, engineer C in Q&A / advocate 2 | Chaptered + clips | ~6 |

- **Season total:** about 42 h of 72 h available, which leaves about 30 h of slack for backups, replays, and the lab re-run.
- **Lab hours:** the lab month exceeds 18 h on its own, so build the lab in December and January. Cumulatively it fits.
- **Europe is 30% of users**, above the quarter threshold. Run a scheduled replay of the lab at a Europe-friendly morning time, labelled "recorded", with one advocate in chat.
- **Dec 15 sits next to the holidays.** If episode 2's sign-ups lag, move it to 12-08, not later.
- **Not yet drafted:** the scored topic backlog. It needs your top forum questions, docs searches with no result, and the trial step with the biggest drop. Send those and I'll score a season ahead.

## Promotion for episode 1

- **Timing:** registration opens now and stays open until the session starts. In Livestorm's data, 49.6% of registrations arrive in the final 7 days, so put most effort there.
- **Audience:** the job is activation, so aim at people who have signed up but not created a flag.
  - Use an in-app banner and an onboarding email to signups from the last 14 days.
  - Use the newsletter and community channels next.
  - Use paid last, or not at all.

## Handoff contract (draft, for the sales owner to sign)

| Tier | Signal | Route | Timing |
| --- | --- | --- | --- |
| A, hand-raise | Asked for pricing, demo, or contact; clicked a pricing or demo CTA | Sales, with episode and question | 1 business day |
| B, engaged, open account | Engaged attendee or replay registrant at an account with an open opportunity | Account owner notified, no cold call | Next working day |
| C, engaged | Top third by watch share, questions, resource clicks, **and** ticked the marketing box | Product activation nurture (lab link, docs path) | Episode follow-up |
| D, registered | Everyone else | The replay email only | Episode follow-up |

- **"Fine with whatever" isn't a contract.** Until one named sales person signs, hand-raises go through the existing contact-sales path. Tier B is off, and everything else is product nurture only.
- **Form:** collect name and email only. The notice must say five things:
  - the session is recorded and where it is published;
  - attendance, watch time, questions, and clicks are recorded and used to decide follow-up;
  - attendance is **matched to product activity by email**, which the job metric needs;
  - sales may contact them;
  - the retention period.
- **Marketing email:** an unticked opt-in box is the only rule valid in every EU state. With 30% of users in Europe, route marketing email on that box alone.
- **Legal:** have legal review the wording and record a legitimate-interest assessment before any sales call is based on webinar behaviour.
- **No sponsors or partner co-hosts in season one.** That avoids the joint-controller paperwork.

## Episode log (columns; episodes 1–4 empty)

Episode | Registrants by source | Live | Live/registrants | 30-day on-demand (platform + public copy) | Total reach | Returning | Live completion | Replay completion | Questions | Tier A / accepted | Replay published (h) | First-flag rate, attendees vs matched

## Open decisions

1. **Weekly vs monthly:** is marketing OK with monthly plus clips? This one changes the plan.
2. **v3 launch date:** does Tue 11-17 hold, or must episode 1 be 11-10?
3. **Sales owner:** who signs the handoff contract?
4. **Budget:** platform, lab infrastructure, and captioning amounts.
5. **Baseline signup-to-first-flag rate and signup volume:** pull both from product analytics before episode 1. If the eligible list is in the thousands, optionally hold back a random 10–20% from invitations for one season to get a causal read, at some cost to reach.
6. **Host size and registrant mix:** this sets the expected attendance band if you want one before the baseline exists. Small host with cold registrants runs about 20–35%. Large host with its own list runs about 45–60%. Vendor figures all come from platforms measuring their own customers, so treat them loosely.

## Memory note

Keep the charter, backlog, and episode log in `devrel-context.md`, so the next run starts from them.