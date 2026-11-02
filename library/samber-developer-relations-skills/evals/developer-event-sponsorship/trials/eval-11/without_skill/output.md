## Ravenscar Tooling — DevRel Budget Reconciliation

Bottom line up front: these three asks don't fit together as stated. Cutting events to 41%, launching a brand-new owned conference, and folding a new $30K OSS line into "events" are pulling in different directions at once. Below is a plan that gets you to 41%, keeps the conference viable, and gets the OSS money off the events line entirely — because it never belonged there.

---

### 1. Sanity-check the 41% target before you commit to it

Two things to verify with finance before you cut anything:

- **What does the benchmark report count as "events"?** Industry surveys vary wildly on taxonomy — some fold sponsorships, travel, swag, and staff time into "events"; others count only hard event costs and put travel/swag elsewhere. If Ravenscar's 55% and the report's 41% aren't measuring the same basket, you'd be cutting real programs to match a number that isn't comparable. Ask for the report's category definitions before you build a plan around it.
- **A peer average is not a target, it's a data point.** If your cost-per-qualified-meeting at events beats your other channels (ads, outbound), 55% could be the *correct* number for Ravenscar even if the industry median is lower — budget share should follow marginal ROI, not resemblance to a benchmark. Pull your own numbers (cost per qualified meeting/opportunity per event, last 2–3 cycles) before agreeing to 41% as gospel. If the ROI data backs the cut, great — now you're cutting with evidence, not just to match a chart.

⚠️ **Timeline flag:** today is September 20, 2026. If "Q3" means calendar Q3 2026, that's 10 days away — not enough runway to unwind signed sponsorship contracts, plan a new conference, and stand up an OSS program. Confirm whether finance means fiscal Q3 (likely later) or literally this month. If it's the latter, push back now — a rushed cut usually means killing the wrong things (whatever's easiest to cancel, not lowest-ROI) rather than the right ones. Recommend anchoring the *decision and glidepath* by Q3, full realization by Q1–Q2 of the next fiscal year.

---

### 2. The sponsorship → owned conference swap is not a cost-saving move in year one

Stopping conference sponsorships and replacing them with your own one-day event feels like a lateral swap. It isn't:

- Sponsorship buys someone else's already-built audience. An owned conference requires building that audience from zero — invites, promotion, speaker sourcing, content — which is why the events skill rates owned conferences as the highest-effort, highest-risk format, not to be attempted "before you have a community that would attend without being begged."
- First-year owned events routinely run over budget and underperform their steady-state pipeline numbers. Judge it on a 2–3 event trend, not the first run — which also means don't let year-one underperformance be used as an excuse to axe it before it's had a fair shot.
- Per-event cost is often comparable to or *higher* than a single sponsorship once you count venue, catering, AV, content production, and staff time — the savings, if any, come from running one event instead of eight, not from owned being cheaper than sponsored per se.

**Recommendation:** don't treat this as "sponsorship money directly funds the conference." Treat it as two separate decisions:
1. Stop sponsoring — this is a real, immediate saving.
2. Fund a *lean* first-year conference (one day, regional, no marquee keynote fees, 150–300 attendees) as a separate line, sized to leave real savings behind, not to consume 100% of what sponsorships used to cost.

Before fully zeroing out sponsorships: check if any single event in your current portfolio is a disproportionate pipeline generator (the skill's 80/20 rule — a handful of events usually produce most of the pipeline). If one is, carving out an exception costs little and protects a proven channel while you're still unproven on the new format.

---

### 3. The OSS sponsorship doesn't belong in the events budget — say so to your VP directly

This is the cleanest fix available to you, and it resolves most of the arithmetic problem below.

$30K/year to fund dependencies you rely on is **supply-chain risk mitigation and community stewardship, not audience acquisition.** It will never produce a qualified conversation, a booth scan, or a meeting booked — the only metrics events are judged on. Measuring it against an events benchmark guarantees it always looks like waste, and inflates your "events %" every year regardless of how many conferences you actually run, corrupting the benchmark comparison finance is asking you to hit.

**Push for a separate line** — "Open Source Ecosystem Investment" or similar, sitting outside DevRel-events entirely (ideally under Engineering or an OSPO-style budget, since dependency health is arguably an engineering risk line, not a marketing one). Practical design if you own it regardless of where it sits:
- Fund 5–10 *direct, critical* dependencies — pick by criticality + maintainer funding need, not by popularity (don't just top up already well-funded mega-projects).
- Use existing rails: GitHub Sponsors, Open Collective, Tidelift, or thanks.dev — don't build custom payment infrastructure for $30K.
- Revisit annually; this is a goodwill/risk line, not a campaign, so it doesn't need an ROI model — it needs a criteria doc so it doesn't turn into whoever asks loudest.

If the VP insists it stays under events politically, at minimum get agreement that it's reported as a distinct sub-line so it's never silently blamed for (or credited toward) the events percentage.

---

### 4. The reconciled math (illustrative — drop in your real total budget)

Using a representative $600K annual DevRel budget so the mechanics are concrete:

| Line | Now | Target |
|---|---|---|
| Total DevRel budget | $600,000 | $600,000 |
| Events @ 55% / 41% | $330,000 | $246,000 |
| Gap to close | — | $84,000 |

If the $30K OSS line stays inside events (VP's ask), the real gap becomes **$114,000** — a 34.5% cut to actual event activity, not the 14-point cut finance thinks it's asking for. This is the exact contradiction worth surfacing before you start cutting: finance thinks they asked for a modest rebalancing; as structured, they've asked for a much deeper cut plus a new cost center, wrapped in the same number.

Working the swap:
- Killing sponsorships frees roughly $210,000 (illustrative — use your real sponsorship total).
- A lean first-year owned conference runs $130,000–170,000 for 150–300 attendees, one day, no marquee costs.
- Remaining event participation/misc (dinners, small meetups, swag): unchanged, say $120,000.
- New events total: ~$265,000 — still $19,000 over the $246,000 (41%) target.
- **Move the $30K OSS line out entirely** (section 3) — this is what actually closes the gap on paper without cutting real activity further.
- Remaining $19K: trim from lower-ROI misc participation, or tighten the conference AV/catering budget, or accept 44% in year one with a written glidepath to 41% in year two once the conference has real pipeline data behind it and doesn't need first-year overbuild.

---

### 5. What to bring back to finance and your VP

1. **To finance:** confirm the benchmark's category definitions and the real Q3 deadline before committing; propose a two-quarter glidepath instead of an instant cut, backed by your own cost-per-qualified-meeting data rather than pure benchmark-matching.
2. **To your VP:** the OSS $30K should be its own budget line, reported separately — argue it on category-error grounds (it can't be measured by event metrics, so it shouldn't be funded by or count against the event budget). This is the single highest-leverage conversation in this whole plan.
3. **On the conference:** scope it lean for year one, set explicit success metrics up front (qualified conversations, meetings booked, cost-per-qualified-meeting benchmarked against what sponsorships used to cost you), and commit internally to judging it over 2–3 runs, not one.
4. **On sponsorships:** check your last 1–2 years of data for any standout performer before zeroing the whole category out — keep it if the numbers say so, cut the rest.