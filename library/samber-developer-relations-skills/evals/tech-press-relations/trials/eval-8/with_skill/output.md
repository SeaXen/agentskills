# Pinebark acquisition — press plan

## Three requests I'm not doing, and why

**⚠️ Promising the exclusive to both writers.** The skill is explicit: "Never promise the same exclusive twice. It is always discovered, and reporters at major tech outlets describe botched exclusives and embargoes as the 'piss-poor execution' they resent most." It's in the failure-modes table by name: *Exclusive double-promised → two outlets discover they both had it.* They don't need to compare emails to catch it — the acquirer's own comms team, other reporters on the beat, or a source at either outlet surfaces it routinely. When it lands, both writers remember it, not just the one who "lost," and both outlets' willingness to take a briefing from Pinebark or the acquirer next time drops. I'll help you choose one real exclusive, or run a proper embargo to both — not a bet with two winners.

**⚠️ Both drafts sent to you before publication "to fix the framing."** That's copy approval, and the skill bans it by name: "Offer a factual check of specific technical claims. Never grant copy approval." Failure-modes table: *Copy approval requested → asking to review the piece before it runs.* What you get instead: a technical fact-check offer (I'll draft the line below), and — more useful — a briefing pack thorough enough that neither writer has an accuracy gap to fill in on their own by guessing.

**⚠️ Demanding "effectively dead" be removed.** If it's inaccurate, that's a factual correction and fair game — send the specific evidence (commit cadence, contributor count, the acquirer's written maintenance commitment) and ask them to check it against the record. If it's accurate, it stays: "Correct factual errors politely and specifically; let unflattering-but-accurate framing stand." And per the acquisition playbook specifically: "**Trap** — silence on the parts users fear. The unanswered question becomes the headline." A writer reaching for "effectively dead" almost always means nobody gave them a dated answer on OSS maintenance. That's fixable before either of them files — see the proof pack below — not after.

Everything past this point is the actual plan, built straight.

---

## Step 1 — Qualification

| Test | Verdict |
|---|---|
| Newness | Pass — real ownership change, not a scheduled step. |
| Consequence | Pass, if you name them: existing OSS users/contributors, paying customers, Pinebark employees, the acquirer's own customers who now inherit this stack. |
| Evidence | Pass, contingent — needs the deal itself confirmable (both companies' announcements, or a filing) by Monday. |
| Conflict/shift | Pass — frame as part of the infra-consolidation trend if that's true for your category; skip it if it isn't. |
| Tellability | **At risk.** Only passes if OSS-project fate, pricing, API, and team commitments are cleared for publication before lift. This is the one to fix this weekend. |

4-5/5 achievable, but tellability is the gate. Don't pitch until it's closed.

## Step 2 / Step 8 — The angle

Acquisitions don't get to pick from the five shapes — the hook is fixed: **"what happens to the open-source project, the pricing, the API and the team. That is the entire story for this audience."** Everything below serves that, not a separate narrative.

Optional secondary frame, only if genuinely true: tie it to a market-consolidation trend for the business/startup-press angle. Don't force it.

## Step 3 — The two writers

You already have two engaged reporters, which is unusual and worth protecting rather than burning. Run the standard verification on both before deciding anything:

- Last 5 bylines — are they actually on this beat, or did they just hear about it secondhand?
- Current employer and section confirmed on the outlet's own site.
- Stated preferences (embargo policy, no-pitch conditions).
- Audience fit against who has to believe this — question 3 from the interview: developers deciding whether to keep using the OSS project, buyers deciding whether the acquirer's roadmap still holds, or both.

That last one usually settles the exclusive-vs-embargo call on its own (see Step 6).

## Step 4 — Proof pack (this is what actually kills "effectively dead")

Standard briefing pack contents (news in one sentence/paragraph, embargo line with timezone, 2-3 approved quotes, interview availability) plus, acquisition-specific:

- [ ] **OSS project fate, with dates** — maintained by whom, under what license, for how long, funded how. This is the single artifact that pre-empts the "dead project" framing with something checkable instead of a request to delete it.
- [ ] Pricing: what existing customers keep, what changes, effective date.
- [ ] API/product roadmap: what's sunset, what's merged, migration path if anything is deprecated.
- [ ] Team: who stays, in what role — only state what's actually confirmed and cleared.
- [ ] Recent commit/release history, contributor count, open-issue response time — the concrete evidence against "dead," if it's false.
- [ ] Comparison table including where the acquisition creates real risk for existing users. Skipping this is what reads as spin.

If any of these boxes can't be filled honestly by Monday, that's the real problem — not the writer's phrasing.

## Step 5 — Fact-check line (replaces the copy-approval ask)

> Happy to do a factual check before you file — hardware, dates, license terms, anything sourced from us. Not asking to see the draft or the framing, just flagging I'm reachable if something needs verifying on deadline.

## Step 6 — Exclusive or embargo: pick one, for real

Given a 3-day runway (today is Friday 2026-09-18, close is Monday 2026-09-21), the skill's normal 1-2 week sequencing (exclusive decided ~2 weeks out, embargo opened ~1 week out) doesn't fit. Two honest options:

**Option A — one real exclusive.** Pick whichever writer's audience matches question 3's priority (developers vs. buyers). Tell the other one, now, that this one's going out under embargo alongside everyone else, not exclusively. Deadline for the exclusive writer to confirm: tomorrow (Sat), so there's still a day to open the embargo to writer two if they pass.

**Option B — embargo both, lift together Monday.** Given the compressed timeline and that both are already engaged, this is the lower-relationship-risk default: both get the story now, both write independently, both publish at the same stated moment. Recommended unless one writer's audience is clearly the one that has to believe this and the other's isn't.

Either way: state day, clock time, and timezone explicitly — "Monday morning" is not an embargo. Suggested lift: **Monday, September 21, 2026, 09:00 [your timezone]**, matching the close.

**Leak check before you commit to that time:** any pending PR, milestone name, changelog entry, or status-page note on the OSS repo that could give this away before Monday? Check now.

## Step 7 — Day-of runbook (Mon Sept 21)

1. Press page and owned post live at lift.
2. Embargoed/exclusive coverage publishes.
3. Community channels (OSS project's own forum/Discord/repo discussions) after, posted by someone who actually works on the project, in that community's register — not a press release pasted in.
4. One person staffed on each channel for the day, named, with a stated check-in cadence.
5. If a thread turns hostile about the OSS project's future, answer with the dated commitment from Step 4 — don't argue framing, don't ask for edits, just supply the fact.

## Pass threshold before either pitch goes out

1. Acquisition passes 4-5/5 qualification — pending tellability (Step 1).
2. Every claim checkable from something public, or shipped with its methodology — pending the OSS/pricing/API facts (Step 4).
3. Both writers verified on-beat, current employer confirmed.
4. Press page + briefing pack + proof pack live before first pitch.
5. Embargo or exclusive chosen (Step 6), lift time stated with timezone, leak check clear.

Not clear to send until the OSS commitment in Step 4 exists. That's the actual fix for the "effectively dead" line — not asking a writer to cut it.