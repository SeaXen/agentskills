# [Project Name] Lisbon Meetup — 12-Month Programme

Built with the `developer-meetup-program` skill. You asked for no interview, so the choices below are my best default per the skill's own guidance, not something confirmed with you — **read "Assumptions" first**, since correcting those two or three fields is what actually makes this doc safe to show your manager.

---

## Assumptions made (no interview run — fix these first)

| Field | Assumed | Fix by |
|---|---|---|
| Project / group name | `[Project Name]` placeholder | Find-replace everywhere |
| Host model | **Company-staffed series** — your platform team runs it directly, stated intent to convert to a vendor-backed volunteer chapter once local co-organizers exist (~edition 6) | Confirm this is really the model, not "independent" |
| Second organizer | Not named — CNCF's floor is **two organizers, different responsibilities**; DevOpsDays wants three from different orgs. A one-person group is one departure from dead. | Name a co-organizer before Monday if you can — even provisionally |
| Primary purpose (SPACES) | **Acquisition & advocacy** — grow a real Lisbon user/contributor base for the project | Confirm this is the one outcome you want funded, not "product feedback" |
| Venue, editions 1–3 | Your own company's Lisbon office | If you don't have one, editions 1–3 need a real venue before this plan is bookable |
| Venue, editions 4–12 | Named **candidates**, not contacted, not confirmed — see Step 5 below | Do the outreach; swap in whoever says yes |
| Speaker names | Roles/placeholders (`[Name TBD]`), not real people | Do not present these as confirmed speakers to anyone outside your team |

Per this skill's own rule: *"Mark anything beyond edition three as provisional — say so rather than inventing a year of programming nobody has committed to."* I'm giving you all twelve because you asked for all twelve, but editions 4–12 are a **directional draft for the pitch**, not a bookable calendar. Present it to your manager as "here's the 12-month shape and the logic behind it," not "here are 9 more confirmed speakers" — that's the one line in this document most likely to embarrass you if repeated as fact.

---

## 1. Program charter

```
# [Project Name] Lisbon Meetup

Room:              Backend/platform engineers who use, evaluate, or are curious about
                    [Project Name] — mostly attending on their own time after work;
                    some on work time if their employer already runs it in production.
Host model:         Company-staffed series ([Your Company]) — intent to convert to a
                    vendor-backed volunteer chapter once local co-organizers exist.
Purpose:            Acquisition & advocacy — a live Lisbon user and contributor base for
                    [Project Name] (SPACES). Product feedback is a welcome side effect,
                    not the named outcome.
Format:             Anchor (25 min) + 2 lightning (5 min) by default; fallback is demo
                    night / study group (no external speaker required).
Rhythm:             Second Thursday, 19:00. Twelve editions, one per month, Oct 2026–Sep 2027.
Program decisions:  Two organizers review title, one-line takeaway and slides in advance.
                    Test: "could this talk be given by someone who doesn't work on
                    [Project Name]?" At least one non-host voice every edition from #2 on.
Organizers:         [Your name] (program), [Co-organizer TBD] (venue & sponsors) —
                    recruit the second name before edition 3, not "later".
Venue:              [Your Company] Lisbon office through edition 3, then rotating hosts
                    booked a season (3 editions) at a time.
Money:              ~€300–400/edition, food and drinks only, on [Your Company]'s budget
                    until a rotating host takes over the room.
We don't:           Sell speaking slots, ever. Share the attendee list, ever. Let sponsor
                    staff pitch from stage past 15 minutes. Run an edition with zero
                    non-host speakers past edition 3.
Accounts:           Listing, mailing list and socials shared between at least two people
                    from day one.
```

---

## 2. Twelve-month edition plan

**Editions 1–3 are plan-grade** (internal speakers, in-house venue — near-zero external dependency, matching a fixed near-term date). **Editions 4–12 are a draft arc** — confirm each one two editions ahead as you go, per Step 4 below, not all at once now.

| # | Date | Format | Topic | Speaker | Venue / Sponsor | Status |
|---|---|---|---|---|---|---|
| 1 | Thu 8 Oct 2026 | Anchor + lightning | Why we open-sourced [Project Name], and what's next | Anchor: [Your name / platform lead]. Lightning ×2: platform-team engineers demoing components | [Your Company] Lisbon office — in-house | **Bookable now** |
| 2 | Thu 12 Nov 2026 | Anchor + lightning | Architecture deep dive: how [Project Name] handles [core problem] | Anchor: [platform engineer]. Lightning ×2, ≥1 reserved for an external early adopter if one has surfaced | [Your Company] office — in-house | **Bookable now** |
| 3 | Thu 10 Dec 2026 | Demo night | Show and tell: what people built with [Project Name] in its first two months | Attendees + platform team, no confirmed speaker needed | [Your Company] office — in-house | **Bookable now** — deliberately no-sourcing format for the holiday-adjacent slot |
| 4 | Thu 14 Jan 2027 | Anchor + lightning | Performance & benchmarking: [Project Name] under load | [Name TBD] — internal or community; ≥1 non-host lightning slot | Candidate: [coworking space, e.g. Second Home Lisboa or Heden — not yet contacted] | Draft |
| 5 | Thu 11 Feb 2027 | Anchor + lightning | A production war story | [Name TBD] — target: an early-adopter company running it live | Same candidate host (season 2, ed. 4–6) | Draft |
| 6 | Thu 11 Mar 2027 | Anchor + lightning | Ecosystem & integrations: plugins, SDKs, what's been built on top | [Name TBD] — ≥1 non-host slot required | Same candidate host — season 2 closes | Draft |
| 7 | Thu 8 Apr 2027 | Anchor + lightning | Security & reliability practices in [Project Name] | [Name TBD] | Candidate: [Lisbon tech company in the project's domain — not yet contacted] (season 3, ed. 7–9) | Draft |
| 8 | Thu 13 May 2027 | Lightning night | Community lightning night — all slots sourced from the room | 5–6 attendees, 5 min each | Same candidate host | Draft |
| 9 | Thu 10 Jun 2027 | Anchor + lightning | Roadmap & RFC process: how [Project Name] decides | Maintainer, Q&A-heavy | Same candidate host — season 3 closes | Draft |
| 10 | Thu 8 Jul 2027 | Two-talk classic | External contributor talk + a swapped talk from a neighboring Lisbon meetup | 1 external contributor + 1 traded speaker | Candidate: partner meetup's usual venue or new host (season 4, ed. 10–12) | Draft — only promote to two-talk once the pipeline board (below) actually holds 2 editions ahead |
| 11 | Thu 12 Aug 2027 | Study group | Work through an open RFC/spec together | No speaker needed | [Your Company] office (fallback — August is Lisbon's quietest month, cheapest option for the low-turnout risk) | Draft |
| 12 | Thu 9 Sep 2027 | Anchor + lightning | One-year anniversary: retrospective + year-two roadmap | Anchor: maintainer. Lightning: 2–3 contributor "what I shipped this year" | Largest season-4 venue, invite past hosts back as joint thank-yous | Draft |

Gap between every edition: 28–35 days — inside the 90-day inactivity line with room to spare. Twelve editions in twelve months clears CNCF's six-per-year floor comfortably.

---

## 3. Speaker pipeline board

Health line is **two confirmed editions ahead**. Right now that's true only through edition 2.

| Date | Speaker 1 | Speaker 2 | Status |
|---|---|---|---|
| 8 Oct 2026 | Confirmed — [platform lead] | 2 lightning, internal | Venue confirmed, no external dependency |
| 12 Nov 2026 | Confirmed — [platform engineer] | 1 lightning open to external | Venue confirmed |
| 10 Dec 2026 | n/a | n/a | Fallback format, no speaker needed |
| 14 Jan 2027 | Prospect | — | Source from CFP + edition 1–3 attendees |
| 11 Feb 2027 | Prospect | — | Target: an early production adopter |
| 11 Mar 2027 | Prospect | — | — |
| 8 Apr 2027 | Prospect | — | — |
| 13 May 2027 | n/a | n/a | Fallback format, no speaker needed |
| 10 Jun 2027 | Prospect — maintainer | — | — |
| 8 Jul 2027 | Prospect | Prospect — neighboring meetup trade | Two-talk only if this row is fully confirmed by ~May |
| 12 Aug 2027 | n/a | n/a | Fallback format, no speaker needed |
| 9 Sep 2027 | Prospect — maintainer | 2–3 contributor lightning | — |

Open a standing CFP linked from every listing before edition 1 — it's the only channel that fills editions 4–12 without a monthly panic. Harvest edition 1–3 lightning speakers directly into this board; a lightning slot is the cheapest way to manufacture edition 6–9 anchors.

---

## 4. Edition log skeleton

Fill this the night of each event — attendance at the door, not RSVPs.

| # | Date | Format | Speakers | RSVP | Door | Repeat % | New faces | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | 8 Oct 2026 | | | | | | | |
| 2 | 12 Nov 2026 | | | | | | | |
| 3 | 10 Dec 2026 | | | | | | | |
| ... | ... | | | | | | | |

---

## 5. Scorecard baseline

| Signal | Target | Current |
|---|---|---|
| Attendance at the door | Stable or rising over 3 editions | Not measured yet |
| Show-up rate (attended ÷ RSVP) | ≈ 70% (plan on ~30% no-shows, CNCF figure) | Not measured yet |
| Repeat attendance | ≥ 40% | Not measured yet |
| New faces per edition | > 0 | Not measured yet |
| Speakers sourced from the room | ≥ 1 in 3 | Not measured yet |
| Editions confirmed ahead | ≥ 2 | Currently 2 (editions 1–2) |
| Organizer count / employer spread | ≥ 2 people, ≥ 2 employers | Currently 1 — **open risk** |
| Gap since last edition | ≤ 90 days | n/a — pre-launch |
| Attendees per edition | > 10 | Not measured yet |

---

## Sponsor / venue notes to say out loud to your manager

- **Editions 1–3 cost is internal**: room is free (your own office), food is the only real line, ~€300–400/edition.
- **Editions 4–12 sponsor names above are candidates, not commitments** — none have been contacted. Don't let this slide into "we have sponsors lined up" in the room Monday.
- Whoever hosts gets: logo on the listing, a stage thank-you, a small table, **at most 15 minutes of stage time** — never a bought speaking slot, never the attendee list. State this before any venue conversation starts.
- Book each rotating host a season (3 editions) at a time, not the full year — a single yes for twelve months makes you one relationship away from homeless if it falls through.
- Keep at least one non-host speaker every edition from #2 onward. This is the one guardrail that stops "the team's own meetup" from reading as a thinly-veiled product pitch to the room — and it's the fastest way this specific program dies if skipped.

**Single biggest gap to close before Monday: you're the only named organizer.** Everything else here survives a rough month; a one-person program doesn't survive a role change.