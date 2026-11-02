# Halcyon Robotics — DevRel Reorg Plan

## The mismatch you need to resolve first

The CTO's argument ("advocates close to the code") is correct but incomplete. It answers *how DevRel does its job better*, not *why DevRel exists*. You fund six advocates because sales is losing enterprise deals to a competitor with better integration docs — a problem that lives **across** squads, in the buyer's experience of the whole platform, not inside any one squad's sprint. A clean 1-advocate-per-squad split with full reporting lines to five engineering managers optimizes for the first and quietly abandons the second. Also: six advocates, five squads — the CTO's plan doesn't even account for the extra head.

Full decentralization risks, concretely:

- **No one owns the enterprise-docs gap.** Five EMs will each optimize their advocate for their own squad's roadmap and internal demo needs, because that's what they're measured on. The cross-product integration story — the thing enterprise buyers actually evaluate, and the thing you're losing on — has no owner once it's split five ways.
- **The lost-deal feedback loop breaks.** Today you can pattern-match "why did we lose this deal" across all six advocates. Split into five silos, each reporting to a different EM, and that aggregate signal disappears — each EM sees only their own slice.
- **Craft and consistency erode.** Docs voice, sample-code standards, API reference structure — these need a single bar. Five EMs, each managing one advocate as a rare direct report, will calibrate performance differently and have no basis to hold a writing/DX bar.
- **Career path and hiring bar collapse.** An EM managing one advocate for the first time can't develop them as a DevRel professional. Retention risk within two quarters.

None of this means "reject the CTO's plan." Proximity to the code is a real, valid fix for a real problem (advocates currently too far from what they're documenting). The fix is to get proximity **without** giving up ownership of the actual mission.

## Recommendation: matrixed embed, not a clean split

1. **Embed five advocates with the five squads** — co-located, in sprint planning, roadmap-aware. This is the CTO's proximity win, delivered in full.
2. **Keep a solid functional reporting line to you** for all five; the squad EM gets a formal, real say in day-to-day prioritization and a documented input into performance review — not a token dotted line, an actual voice — but you own comp, career development, and the DevRel craft bar.
3. **The sixth advocate does not get assigned to a squad.** Make them the cross-squad integration/enterprise-docs owner — the one person accountable for the multi-product story that shows up in enterprise deals, and the direct channel to sales' lost-deal reasons.
4. **Weekly 30-minute sync, all six advocates + you.** This is the mechanism that keeps craft, voice, and the competitive-docs benchmark from fragmenting once bodies are physically distributed.
5. **Each embedded advocate's quarterly goals are set jointly by you and the squad EM**, and explicitly split: part squad-specific (API ergonomics feedback, sample coverage, launch support), part tied to the named competitor's doc gap in that squad's product area.

This gives the CTO everything "close to the code" was supposed to buy, while keeping a single throat to choke on the actual reason the budget exists.

## Rollout for next quarter

**Weeks 1–2 — align before anyone moves.**
- Take this hybrid model to the CTO as a "yes, and": agree on embedding, propose the matrix reporting structure and the sixth advocate's charter as non-negotiable conditions, not a counter-plan to relitigate the whole idea.
- Get a written success metric agreed with the CTO *before* the move: trend in enterprise deals citing docs/integration quality as a loss reason (pull this from sales' loss-reason field, last two quarters, as your baseline this week).
- Run a fast competitive benchmark: which squads' products actually show up in the lost deals? You likely don't have an even 1-in-5 problem — it's probably concentrated in two or three products. Use this to sequence, not to blanket-assign.

**Weeks 3–4 — pilot, don't big-bang.**
- Embed advocates first with the one or two squads most implicated in the benchmark. Hold the rest under the current central model for now.
- Stand up the sixth advocate's cross-squad role immediately — this seat should exist from day one, not after the pilot proves itself, since it's your only guaranteed coverage of the actual funding rationale during the transition.
- Write a one-page charter per embedded advocate with the squad EM: time split, deliverables, review cadence, what the EM can and can't unilaterally redirect.
- Tell the six advocates directly, before rumor does: what's changing, why, what stays under you, and what their career path looks like. Reporting-line changes read as demotions if unexplained.

**Weeks 5–12 — run it, watch the leading indicators.**
- Biweekly cross-squad sync, led by you: docs consistency, style-guide drift, competitive-gap tracker.
- Monthly pull of sales' lost-deal reasons, tagged by product area, reviewed against the competitor's docs on the same surface.
- Check squad EM satisfaction and advocate satisfaction separately — a model where the EM is happy and the advocate is quietly job-hunting isn't working.

**Week 12–13 — decision point for full rollout.**
- If the pilot squads show docs-gap closure and the EM relationship is functioning, extend embedding to the remaining squads using the same charter template.
- If the loss-reason trend hasn't moved, that's a signal the gap isn't primarily a "distance from code" problem, and the CTO's fix wouldn't have solved it either way — cheaper to learn that from two squads than from five.

## What to bring to the CTO this week

A short, specific ask, not a rejection: agree to the matrix reporting model, agree to the sixth advocate's cross-squad charter, agree to pilot on the two most-implicated squads first, and agree on the loss-reason metric as the shared scoreboard before the quarter starts. That gives him the proximity he wants and gives you a structure that still answers to the reason the six headcounts exist.