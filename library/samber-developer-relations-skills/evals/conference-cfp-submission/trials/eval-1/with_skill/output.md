# Angle, and what got cut

"Spiciest that'll survive contact with your actual constraints" isn't the same talk as "spiciest, full stop." A true contrarian thesis (something like *"on-call rotations are a symptom of bad architecture, not a fix for it"*) would score higher on originality, but it's out: you said you'd fold under live grilling over a staked-out position, and a thesis that collapses in Q&A is the specific failure mode that angle carries. Deleted.

A pure war story (just the incident, just the 340-a-week grind) was the other option, and it's the lowest-effort path since the material already exists in your head. Not chosen as the shape either, because you told me you want this given four or five times plus a recording plus a write-up after. That's a compounding asset, and a one-off incident narrative doesn't travel across five different rooms as well as a method does. It also hands the room a story, not an action.

What's left, and what I built: **your number and your ownership as the hook, a practical playbook as the structure.** The counter-conventional wedge is "delete, don't tune" — most alert-fatigue talks stop at deduping and threshold tweaks; yours is about killing checks outright, with a receipt (51 vs. 340) that a reviewer can't wave off. It's spicy without being a position you have to defend in the abstract. If someone pushes back in Q&A, your answer is always "here's what we measured on our system," never "here's what I believe about the industry." That's a much easier room to survive than a debate.

Since I can't browse from here, I couldn't pull ScaleNorth's actual CFP page. The constraints block below lists every value I assumed instead of read — confirm each one before you paste anything in.

---

# ScaleNorth — standard session, 25-30 min (assumed) — deadline 2026-09-27 (9 days out)

## Constraints read from the CFP

- **Not read — CFP page unreachable from here.** Everything below is a standard-shape assumption, not a fact about ScaleNorth. Paste the real page back to me if you want these corrected before you submit.
- Format: standard session, 25-30 min (assumed — check whether ScaleNorth also offers lightning slots; a 10-minute version of this exists too and is a cheap second submission if the rules allow more than one)
- Caps (assumed, typical for this size of event): title 100 chars, abstract 1,500 chars, notes to reviewers 1,000 chars, benefit to community 1,200 chars, bio 400 chars
- Review: unknown whether anonymous or named — if anonymous, strip "Northwind Freight" from the title and abstract and keep it only in the bio/notes fields
- Per-person cap: unknown — check before you consider the lightning-talk version as a second submission
- AI policy: unknown — this draft has had one humanizer pass, but you still need to read ScaleNorth's actual policy and rewrite it in your own words before submitting
- Assumption: track named something like "Reliability," "Operations," or "Production/Incident Management." Match the pack's Track section to the real wording once you have it.

## Track

Reliability & Operations (name assumed — confirm the exact track title on the CFP page and quote it here). Matches because this is first-hand production practice with a number attached, not a product pitch and not a research talk.

## Title

Delete, Don't Tune: Cutting Weekly Pages From 340 to 51 (55/100 chars)

Alternates:

1. We Cut Weekly Pages From 340 to 51 by Deleting Alerts, Not Tuning Them (70/100 chars)
2. 289 Alerts We Killed: Cutting Weekly Pages From 340 to 51 (57/100 chars)
3. The Alert Audit That Cut Our Pages by 85 Percent Without Missing an Incident (76/100 chars)
4. 85 Percent of Our Alerts Were Noise. We Deleted Them Instead of Silencing Them. (79/100 chars)

Pick 1 for a vendor-neutral, anonymous-review room — it names no employer and states the method as a claim on its own. Pick 2 if the schedule page rewards a punchy number in the title over a full sentence.

## Abstract (603/1,500 chars, assumed cap)

Northwind Freight's on-call engineers used to field 340 pages a week. Most never changed what anyone did: no ticket, no fix, no action beyond silencing the phone. This session walks through the audit that sorted a month of pages by outcome instead of severity, the test used to decide which alerts to delete outright rather than mute or retune, and the safety net that let the team cut that number to 51 a week without missing a real incident. Attendees leave with the audit method, the deletion test, and the one number to track before trusting a quiet pager: not alert count, but missed-incident rate.

*(Left under the assumed cap on purpose — there's room to add one more concrete detail, like the actual percentage that turned out to be pure noise, once you've confirmed you can publish it.)*

## Takeaways

- Audit a week of pages by outcome, not by service or severity, to find which alerts never changed what a human did
- Apply one deletion test before muting or retuning anything: has this alert changed a human's action in the last several times it fired
- Track missed-incident rate, not alert count, as the number that proves a deletion was safe

## Outline (reviewer-only)

- 0-3 min — the state of on-call before the audit: 340 pages a week, and [the specific night or near-miss that made this undeniable — fill in your own]
- 3-10 min — the audit method
  - pulled a month of pages, classified each by outcome: actioned, ignored, escalated without action
  - [the real split you found — e.g. "X% fell into escalated-without-action"]
- 10-20 min — the deletion test and the safety net
  - the single question used to qualify an alert for deletion, not muting
  - who signed off on a deletion, and how a mistake gets caught
  - [your actual rollback mechanism — e.g. a holding queue before a check is permanently removed]
- 20-26 min — results
  - 51 pages a week, down from 340
  - [MTTA/MTTR movement, if you have it]
  - zero missed SEV1s, or whatever the real safety number is
  - the one alert that should not have been deleted, and what it taught the team
- 26-30 min — the reusable version of the method, and questions

## Notes to reviewers (661/1,000 chars, assumed cap)

I own the on-call rotation and alerting pipeline this talk describes, and the audit behind the 340-to-51 number comes from our own incident tooling, not a vendor benchmark. This is my first conference talk. Before ScaleNorth I plan to run an early version at a local meetup to test the pacing and, ideally, walk in with a recording. The angle is deletion, not tuning: most alert-fatigue talks stop at deduplication or threshold changes. This one shows the test we used to kill checks outright and the rollback net that made that safe to try. No product is pitched; the pipeline runs on tooling I will name once confirmed, but the method itself is tool-agnostic.

## Benefit to the community (422/1,200 chars, assumed cap)

Alert fatigue is one of the most common complaints from on-call engineers, and most existing talks and posts focus on tuning thresholds or adding deduplication, which leaves the underlying noise in place. This talk gives attendees a concrete audit method and a deletion test they can run on their own team's pages within a week, plus the one metric, missed-incident rate, that proves deletion did not trade noise for risk.

## Audience level and prerequisites

Intermediate. Written for anyone who owns or shares an on-call rotation and an alerting pipeline. No specific tool prerequisite — the method is described independently of any one paging or monitoring product.

## Speaker bio (279/400 chars, assumed cap)

[Name] is a staff SRE at Northwind Freight, where they own the on-call rotation and alerting pipeline for the company's logistics platform. They led the audit that cut the team's weekly pager volume from 340 to 51 without missing an incident. This is their first conference talk.

*(Swap "they/their" for your actual pronouns before submitting — left neutral since you didn't specify.)*

## Supplemental materials

- Prior talk recording: none yet. Highest-leverage single thing you can do before the notification date: run this once at a meetup and record it, even on a phone. It fills the weakest part of the Speaker score below.
- Repo / post / benchmark: none published yet — the write-up comes after you've given the talk once, so it can answer the questions the room actually asked instead of the ones you guessed at.

## Self-review

- Content: 4/5 — the outline has minutes and two levels, and the scope matches a 25-30 min slot. Not a 5 because the deletion criteria and rollback mechanism aren't written down yet outside this draft.
- Originality: 4/5 — "delete, don't tune" is a lens most alert-fatigue submissions skip. Not a 5 until the audit method is shown to generalize past Northwind Freight's own stack.
- Relevance: 3/5 — track fit is assumed, not confirmed against ScaleNorth's real track list. Moves to 4 once you match the pack's Track wording to the real page.
- Speaker: 3/5 — clear first-hand ownership of the material, but no recording and no external artifact yet. The notes-to-reviewers field is carrying this score; a meetup recording would move it to 4.

Passes this skill's bar (no axis below 3, Content and Originality both at 4), with Relevance and Speaker flagged as the two to strengthen before you submit, not blockers.

## Before you submit

- [ ] Rewritten in your own voice — this draft is a scaffold, not a final
- [ ] Every bracketed placeholder filled with a real number or removed
- [ ] Track name matched to ScaleNorth's actual track list and description
- [ ] Character counts rechecked against the real form, not the assumed caps above
- [ ] Employer sign-off on publishing "340 to 51" and any system names — get it once, in writing, and it covers this and every later event you give the talk at
- [ ] Per-person submission cap and AI-generated-content policy checked on the real CFP page
- [ ] Anonymity rules checked — if first-round review is blind, pull "Northwind Freight" out of the title and abstract
- [ ] A meetup slot booked before the notification date, so a recording exists before your second submission

---

# The four hours

- 30 min — fill in every bracket above with your real numbers and the near-miss story
- 45 min — rewrite the abstract, notes, and bio in your own voice; read them aloud once
- 30 min — pull the real CFP page: track list, caps, per-person limit, AI policy, anonymity rule
- 30 min — send the "can I publish these numbers" message to whoever owns that sign-off at Northwind Freight; do this today, it's the one step with a wait built in
- 45 min — cut to the real caps, run the self-review one more time, submit
- ~60 min buffer

# The reuse plan

You want four or five events, a recording, and a post. In that order, not built at once:

1. Submit this exact playbook-shaped version to ScaleNorth now. It's the angle that needed no live defense and the least rewriting per event.
2. Give it once at a local meetup, before or right after ScaleNorth's notification date. That's the cheapest way to close your only real weak spot (Speaker: 3/5, no recording) and to pressure-test the pacing before a bigger room.
3. Record that first run. Every submission after ScaleNorth links it — it's the single strongest thing a reviewer checks, and you don't have one yet.
4. Keep one file: event, deadline, track, verdict, feedback. Retarget rejections into the next deadline while the material's still fresh; a rejection here is reusable, not a dead end.
5. Write the post last, after you've stood in front of a room with it at least once. It'll answer the questions people actually asked, not the ones you imagined.

The employer sign-off is the one dependency worth starting today rather than in hour three of your four — waiting on someone else's calendar is the likeliest way this slips past nine days.