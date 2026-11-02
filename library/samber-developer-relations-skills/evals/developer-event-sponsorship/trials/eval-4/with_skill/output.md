**Assumption, confirm now:** primary objective = **Adoption** (hands-on API use during the event), Recruiting logged as secondary signal. Hackathon fits both rows in the skill's objective table, but one primary only — pick Adoption because prize track drives actual API usage, which is what a real-time geospatial API needs proven, not just impressions. If recruiting matters more, say so — changes the threshold in Step 7, not the schedule.

Package already bought (mentor table + self-named prize track + 30-min Friday slot). Skip event selection, tier, negotiation. This is steps 6-7 only: activation design + measurement.

## ⚠️ Three pushbacks before locking anything

**1. Prize name.** "Best Use of the Tessellate API" breaks the skill's own rule: frame prize around the problem, not the product. Rename to something like "Best Real-Time Geo Experience" or "Best Use of Live Location Data". Keep API use as an eligibility requirement — that's fine, normal for sponsor tracks. Just don't brand the category with your product name; entries stay more creative, judging stays defensible.

**2. Agency booth crew.** Mentor table's whole job is debugging strangers' code. Non-technical crew can't do that — this is the exact failure mode the skill flags: "booth ignored, non-technical staff, pitch-first posture." Don't put agency crew at the mentor table or on judging. Do use them for what they're actually good at: registration support, swag/table setup, opt-in capture forms, photos for marketing, coordinating with organizers. That frees your 3 engineers' hours for the one thing only they can do — which is the real fix for "engineers are heads-down," not a swap-out.

**3. Workshop conversion.** Don't do it. Three reasons stack: 7 weeks is inside the skill's own "near date deletes the workshop" threshold (under 2 months); you have no curriculum ("never written one" means building from zero, normally a quarter of prep); slot is 30 minutes, workshops need ~90. Keep the Friday slot as a kickoff/framing talk instead: explain the prize track, run one short demo proving the API works live, point students to the mentor table hours, done. Revisit a real workshop next edition once a curriculum exists — that's what collapses prep from a quarter to a week.

## Lock engineers now, not "if I push"

3 engineers for 48h is tight, not slack. If it drops to 2, cut Sunday-morning redundancy. If it drops to 1, tell marketing the mentor table can't run full hours and judging needs a second engineer regardless — flag this today, don't discover it in week 6.

## Two-day staffing plan

| Block | Hackathon phase | Tessellate coverage |
|---|---|---|
| Fri 18:00–18:30 | Sponsor slot (fixed 30 min) | 1 engineer: kickoff talk + prize framing + short live demo. Other 2 set up mentor table. |
| Fri 18:30–21:00 | Team formation, prize criteria published | Heavy: all 3. Highest-value window — explain eligibility, hand out API keys/promo code. |
| Fri 21:00–24:00 | Early build | 2 engineers, 1 rotates off to rest. |
| Fri 24:00–Sat 08:00 | Overnight | Skeleton: 0 physical, 1 on async Discord/Slack if organizer runs one. |
| Sat 08:00–12:00 | Morning build | 2 engineers rotating. |
| Sat 12:00–24:00 | Peak build (afternoon+evening) | Heavy: all 3, staggered breaks — no one runs 12h straight. |
| Sat 24:00–Sun 08:00 | Overnight | Skeleton, async only. |
| Sun 08:00–10:00 | Pre-submission crunch | Heavy: all 3, last debugging push. |
| Sun 10:00–13:00 | Judging vs published criteria | 2–3 engineers, scoring blind to who visited the mentor table. |
| Sun 13:00–16:00 | Demos, awards, closing | 1–2 engineers present prize, start winner follow-up same day. |

Build in real rest blocks during both overnights — a tired engineer gives worse answers than no engineer.

## Prize track

- Name: problem-framed (see pushback 1).
- Prize: EUR 3,000 cash — good instinct, cash is on the list of prizes people actually want. Optional add: pair it with a fast-track intro to Tessellate engineering for winners interested in internships. Doubles as your recruiting signal without a second budget line.
- Publish judging criteria within 2 weeks, before organizer prints hackathon materials — once published, can't change.
- Judges: 2–3 of your engineers, scored on the published criteria only. Never let booth-desk familiarity move a score.

## Friday slot — demo plan

30 minutes, no rehearsal history, 7 weeks out → default to a recorded demo narrated live (tier 3 on the live-demo-design ladder), with a live one-command fallback ready. Don't attempt a from-scratch live build (tier 0/1) on this timeline. Build the actual runbook via `developer-live-demo-design` — 1–2 hours of work, owner: whoever presents, due 1 week before the event.

## Cost + tracking (fix before Friday)

| Line | Amount |
|---|---|
| Sponsorship fee | EUR 14,000 (sunk, still counts for CPQC) |
| Prize cash | EUR 3,000 |
| Travel/hotel, 3 engineers | [ ] — fill once origin city set |
| Agency crew fee | [ ] — get quote |
| Staff time (loaded rate × prep+travel+onsite+followup days × 3) | [ ] |
| Swag/print | [ ] |
| **Fully loaded total** | [ ] |

Tracking:
- One event-specific promo code / API-key flow ("NORDHACK") for every signup during the event. Never reuse elsewhere.
- Capture baseline: current weekly student-segment signups, 1–4 weeks pre-event.
- Adoption metric: teams/individuals creating a Tessellate key at the event, % still calling the API at 30/60/90 days.
- Mentor-table conversation log: name · team · problem · candidate interest (y/n) · next step · owner · follow-up date. Route candidates to Recruiting, bugs to Engineering, feedback to Product — most student conversations are not sales leads, don't force them into a sales sequence.
- Follow-up: within 48h, personal, referencing the actual conversation. Winners get a separate sequence — feature offer + recruiting intro. 30-day check on cohort activation.
- Set the actual minimum-conversation and target-CPQC/adoption numbers off your current blended CAC, not off the EUR 17,000 total — skill's own rule, don't derive threshold from the fee.

## Next action

Confirm today: (1) objective = Adoption, agreed? (2) 3 engineers actually locked with engineering lead, not conditional? (3) prize renamed — send marketing the 2 alternatives above and get a yes.