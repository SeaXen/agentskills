Two asks in this task fail the skill's own evidence check. Fixing that first, then handing you the real plan.

**Kill both before building anything:**

1. **Star-history chart for "15% lift"** — that stat is on the skill's folklore list (`references/published-findings.md`): "self-reported on a growth blog, no methodology." Skill rule: never repeat it, tell requester it's unsourced. Not using it.
2. **Stars as the before/after success metric** — skill rule, explicit: "Drop stars from the tracking plan entirely, even when the goal names stars: they only ever go up, so the metric cannot show a regression and reports success for a change that made the page worse." Star count can only go up or flat. It can't prove the rewrite worked — it can't fail either, so it proves nothing.

Real metric per skill: **conversion rate = clones ÷ unique visitors**, from repo traffic insights. That number can rise, fall, or sit flat — actual signal.

**Timing problem, deal with it now:** rewrite shipped Tue 2026-09-16. GitHub traffic insights only retain a rolling 14-day window. Today is 2026-09-23 — 7 days already gone. Pre-ship data older than 2026-09-09 is unrecoverable. Do this today, not later:

1. Open repo → Insights → Traffic on `aubergine-systems/tinshed`.
2. Export/screenshot daily unique visitors + clones for the full visible window (2026-09-09 through today).
3. Split it: **before** = 2026-09-09 to 2026-09-15 (7 days, partial — real baseline lost, this is what's left). **after** = 2026-09-16 to today (7 days so far).
4. Save both as a dated CSV/screenshot outside GitHub (window keeps sliding).

Skill also flags: **re-measure at 4-6 weeks, shorter windows read as noise.** One week post-ship isn't a verdict — it's a checkpoint.

**What to actually show at next week's review (2026-09-30, ~2 weeks post-ship):**

- Conversion rate, before-partial vs after-so-far — label it "early read, not conclusive."
- Support load: count of "how do I install this" / "what does this do" issues opened per month, pre- vs post-ship. Cheapest signal, moves fastest.
- Star count, if leadership wants optics — show it, but label it explicitly as "context, not evidence" and do not attach any percentage claim to it. Stars-as-narrative is legitimate per the skill's own tooling notes ("useful for a launch narrative only"); stars-as-proof is not.
- One line stating the real readout lands at the 4-6 week mark, with a date.

**Full schedule:**

| When | Action |
|---|---|
| Today (2026-09-23) | Snapshot traffic data now, before window slides further |
| Weekly until week 6 | Re-snapshot traffic insights (14-day window keeps eating old data) |
| 2026-09-30 | Review: early conversion read + support-load trend + stars-for-optics, all labeled as directional |
| 2026-10-14 to 2026-10-21 (4-6 wks post-ship) | Real comparison: full pre-ship week vs full post-ship period, conversion rate + support load |
| ~Dec 2026 (quarter out) | Contributor conversion — slowest, most confounded signal, read last |

Annotate confounders when you report the delta — any traffic spike, HN/Reddit mention, other repo change in that window breaks clean attribution.

Next: run step 1-2 above right now, before more of the pre-ship window rolls off.