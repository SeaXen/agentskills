Ladder structure is sound (cumulative Good-Better-Best, ~2-3x steps between tiers). The problem isn't the price points — it's that three of the five rewards are **open-ended time/scope commitments that don't degrade gracefully if the ladder works**. At 14 sponsors it's fine. At 40+ it isn't, and there's no built-in off-ramp.

**Tier by tier**

- **$10 — name in BACKERS.md.** No issue. Zero marginal cost, standard entry reward.

- **$30 — monthly 30-min 1:1 call.** Recurring, per-sponsor, forever as long as they pay. This is the one that breaks first: 5 sponsors here = 2.5 hrs/month of calendar time, permanently, growing linearly with success. No cap, no expiry. Fix one of:
  - Cap slots ("limited to N people at this tier").
  - Make it quarterly instead of monthly.
  - Convert to a group office-hours call — same value, doesn't scale per-sponsor.

- **$75 — priority support, 24h response.** Two separate risks:
  - **A hard SLA is a promise you can break publicly** (travel, illness, day job crunch) — and a missed SLA on a paid tier is worse for trust than never promising one. Soften to "I prioritize your issues" or "typically within 24h, best-effort" — drop the number as a guarantee.
  - **Visible favoritism on a public issue tracker reads badly in OSS.** Paying for faster treatment in front of the whole community can sour goodwill with everyone else. Consider routing this through a private channel (email/Discord DM) instead of public issue prioritization — same perk, invisible to non-payers.

- **$200 — one custom integration per quarter.** The riskiest one. "Custom integration" is unscoped — could be 2 hours or 2 weeks depending on the ask, and you've pre-committed to doing one every quarter for as long as they sponsor. This is the tier most likely to turn into unpaid part-time contract work. Bound it explicitly: "a small integration/adapter, scoped on a quick call, time-boxed — I'll propose alternatives if the ask is bigger than that." Without a cap, you have no way to say no without breaking the deal you sold.

- **$400 — everything above + logo in README.** Since it's cumulative, a single $400 sponsor inherits the call + support + integration risk above, all stacked. Structurally fine as a top tier — just means the $30/$75/$200 fixes matter even more here, since this is where they compound.

**Cross-cutting**

- Clarify monthly vs. one-time in the copy itself. GitHub Sponsors defaults to monthly recurring — if that's the intent, "monthly call" + "quarterly integration" + "unlimited priority issues" is a standing obligation that renews automatically, not a one-off perk. Sponsors should see that clearly before paying.
- None of the tiers have a stated cap or "subject to availability" clause. Add one to $30/$75/$200 now, while it's easy — retrofitting "sorry, I'm full" onto a tier people already bought into is an awkward conversation you'd rather not have later.
- Price steps themselves ($10→$30→$75→$200→$400, ~2-3x each) are fine, no change needed there.

**Bottom line:** ship $10 and $400-logo as-is. Before publishing $30/$75/$200, add a cap or scope limit to each — otherwise the ladder's success is what breaks it.