# Nordhack Tallinn — Tessellate Sponsorship Plan

Assumes the hackathon runs **Fri Nov 6 – Sun Nov 8, 2026** (7 weeks from today, Sun Sep 20). Confirm exact dates with organizers before locking travel — everything below shifts if it doesn't land on that weekend.

## Three calls to make before anything else

**1. Booth staffing — don't hand mentoring to the agency.**
A hired crew can do setup, swag, queue management, and consent-based badge/lead capture. They cannot debug a student's API integration or answer "why is my request timing out" — that's what "mentor table" in the package actually means, and non-technical staff at that table reads as corporate and kills the value of the sponsorship. Split it:
- Agency: logistics, swag table, lead capture (opt-in — you're in the EU, no scan-without-consent), setup/teardown, photos.
- Engineers: mentor table, on fixed shifts, not 48h solo duty.

**2. Friday's 30 minutes is a demo slot, not a workshop.** A real hands-on workshop needs 60–90+ min, laptops open, individual pacing — undoable in 30 min in front of 400 people in a plenary room. Reframe:
- Friday slot → live demo (something visibly real-time and on a map — much stronger on stage than slides) closing with a literal "get your first response back before I finish talking" quickstart, backed by a QR-code one-pager. This is the whole crowd, passive.
- Ask organizers now for an **add-on 45–60 min Saturday slot** (breakout room or extended mentor-table block) for the actual hands-on workshop, small-group. Workshop slots are usually negotiable for a paying sponsor, and it's worth asking 7 weeks out. If declined, fall back to a self-serve 60–90 min "office hours" block at the mentor table — same content, walk-up format.

**3. Engineers don't need to be there for all 48 hours.** Heads-down on a release means shifts around peak windows (opening, Saturday office-hours block, Sunday final hours + judging), not endurance duty. Cover the dead hours (late night, meals) with the agency crew or skip staffing entirely — nobody's building at 4am Saturday.

## Prep timeline

| Window | Dates | Do |
|---|---|---|
| T-7w | Sep 21–27 | Confirm with organizers: exact Friday slot format/AV, request Saturday add-on slot, prize-track judging process, attendee skill level, exact dates. Get eng lead sign-off on 3 engineers' time (prep + travel) against the release. Tell marketing the staffing split above. |
| T-6w to T-4w | Sep 28–Oct 18 | Build the sandbox: hackathon-only API keys (batch-issued or self-serve signup), safe per-team rate limits, isolated from prod infra. Write the 5-min quickstart one-pager + QR code. Draft Friday demo script. Draft Saturday workshop using prerequisites → skeleton → core feature → checkpoint → troubleshooting structure; pick a project that plausibly extends into a hackathon submission (e.g. a live shuttle/delivery tracker on a map). Lock prize structure and judging rubric. |
| T-3w | Oct 19–25 | Dry-run both the demo and the workshop once, end to end, timed — it's the team's first workshop, rehearse before Tallinn, not during. Brief/scope the agency (logistics only, in writing). Confirm with organizers how the EUR 3,000 payout works (who wires it, to the team or individual, any Estonian tax/reporting step) — don't leave this until Sunday. |
| T-2w | Oct 26–Nov 1 | Book flights/hotel for the 3 engineers. Load-test the sandbox tier. |
| T-1w | Nov 2–5 | Publish the mentor-table "office hours" schedule so students know when to show up. Print quickstart cards. Final AV/room check with organizers. |

## The two days on-site

**Friday evening**
- Arrive, booth setup (agency-led).
- Opening ceremony: 30-min live demo + quickstart close. Hand out quickstart cards / QR at the door as people leave the room.
- Mentor table open for first questions as teams start forming — this is a high-traffic window per typical hackathon rhythm, staff it.
- One engineer (or someone back at HQ) watches sandbox API dashboards from kickoff on — 400 fresh keys hitting the API at once is the first real load spike.

**Friday night**
- Skeleton crew only (agency, if anyone). No engineer needed 1–6am — nobody's shipping yet.

**Saturday**
- Morning: quiet-ish, light staffing.
- Midday/afternoon: the Saturday workshop/office-hours block (from the T-6w prep). This is where actual API integration happens — most teams decide their tech stack Saturday.
- Post-dinner: booth active again, second high-traffic window as energy picks back up.
- Through the day: mentor table on announced shifts, not ad hoc — students plan around a posted schedule better than "find us whenever."

**Saturday night**
- Skeleton crew again. On-call only via the hackathon's Discord/Slack for anyone stuck on an integration bug.

**Sunday**
- Morning through submission deadline: heaviest staffing of the whole event — last-minute integration bugs, API key issues, demo prep. All 3 engineers on for this window regardless of shift plan.
- Judging: pick 1–2 of the 3 engineers as judges (not all 3 — keeps someone neutral/available), score against a written rubric agreed in prep, and have each judge recuse from any team they personally mentored heavily to avoid favoring who they helped.
- Announce "Best Use of the Tessellate API," photos with the winning team, capture a quick testimonial on the spot — this is the easiest, most natural social proof you'll get.

## Budget (beyond the EUR 14,000 already paid)

| Item | Estimate |
|---|---|
| Prize (cash) | EUR 3,000 |
| Travel + hotel, 3 engineers, 2–3 nights | EUR 1,800–2,400 |
| Booth agency (logistics only, 2 days Tallinn) | EUR 1,500–3,000 |
| Quickstart cards / swag | EUR 500–1,000 |
| **Total incremental** | **~EUR 6,800–9,400** |

## Success metrics — agree these before the event, not after

- Teams that actually called the API (not just picked up a key).
- Submissions in the prize track.
- Sandbox-key → real signup conversion at 30/60/90 days post-event (tag these keys distinctly so this is measurable).
- Qualified mentor-table conversations, not badge scans.

## Follow-up

- 24–48h after (Mon Nov 9–Tue Nov 10): personal thank-you to the winning team, offer to feature their project, extended API access.
- Week after (week of Nov 9): light-touch resource email to consenting participants only — no hard sell.
- ~30 days (early Dec): check whether winning/standout teams kept using the API; this is the number that tells you whether to sponsor Nordhack again.

Don't judge "hackathons as a channel" on this one event either way — judge Nordhack on its own, and decide on a repeat after the 30-day number comes in.