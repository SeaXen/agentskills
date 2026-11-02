**Verdict: the 4,200 seats number doesn't hold up. Don't plan around it.**

## Fix the math first

1. **Downloads aren't developers.** 420k npm downloads a month is mostly CI runs, caches, mirrors, and transitive installs. Real unique humans are likely a small fraction of that. Nobody can say how small until you measure it.
2. **1% is far too high.** It's a freemium rate for signed-up users, not for npm downloads of an MIT library. 1% of downloads would be 4,200 seats, about **$122k MRR**. That is 15x your goal, which is a sign the input is wrong.
3. **Work backwards from $8k.**
   - $8,000 ÷ $29 = **about 276 seats**.
   - That is **0.066% of downloads**, or **0.8% of 35k docs visitors** if each visitor were a unique buyer, which they aren't.
   - Buyers are teams. At about 5 seats per account, you need roughly **55 paying accounts**.

| Seat conversion (of downloads) | Seats | MRR |
|---|---|---|
| 0.02% | 84 | $2.4k |
| 0.05% | 210 | $6.1k |
| 0.10% | 420 | $12.2k |

Plan on the 0.02–0.05% band. $8k is reachable but not guaranteed. Treat it as a hypothesis to test in 90 days.

## Two assumptions to check before building

- **Marketplaces:**
  - Cloud marketplaces are built for SaaS, containers, and AMIs, and they run on private offers and long sales cycles.
  - GitHub Marketplace lists Apps and Actions, not licensed npm libraries.
  - I haven't verified current fees or fit for your case. Check both, and don't count marketplace revenue until a listing is live.
- **MIT and Pro:**
  - If the Pro code is MIT, anyone can fork it.
  - Pro needs a separate proprietary license and a license-key check. Per-developer seats are honor-system for a Node library.
  - Decide this before launch.

## The acquisition offer isn't a plain fallback

- **Co-maintainer:** your co-maintainer has a say, so align with them first.
- **Pro roadmap:** an acquirer could stop your Pro roadmap, or change trust and licensing for existing users.
- **Competitor risk:** a PDF-tooling vendor may be a competitor. Don't share revenue numbers with them.
- **Tripwire:** keep it as an option, but write down a tripwire (see below). Otherwise it quietly becomes the plan.

## Dashboard KPIs

**Primary (top row, 3 tiles)**
1. **Paid seats** against the 276 target
2. **MRR** against $8k
3. **Runway in months** (full-time from next month)

**Funnel (weekly)**
4. Docs visitors to pricing-page visits
5. Pricing visits to trial or license requests
6. Trial to paid conversion
7. Seats per account and average revenue per account
8. Estimated unique installers. Use the registry's unique-IP or per-package figures where available, and exclude CI. Don't add telemetry without opt-in.

**Product activation**
9. Share of Pro accounts that ran a bulk render within 7 days
10. Usage per Pro feature (bulk rendering, multi-node coordination, S3 output). This shows which feature people actually pay for.

**Revenue health (monthly)**
11. New, expansion, and churned MRR
12. Seat churn and logo churn
13. Net revenue retention
14. Annual vs monthly plan share

**Channel**
15. Revenue by source: direct, cloud marketplace, GitHub Marketplace
16. Marketplace fee percentage and sales-cycle length, reported separately from direct sales

**Free-tier and community health (so Pro doesn't hurt OSS)**
17. Download trend, ideally with CI filtered out
18. Issue and PR first-response time
19. Support hours per paid account, which is your real cost
20. Forks or complaints about Pro/free boundary changes

Stars and raw downloads are context only. Don't put them in the top row.

## Proposed tripwires

These are starting values to tune against your own numbers, not benchmarks.

- **Day 90:** under 80 seats or $2.3k MRR. Revisit pricing, packaging, and positioning before anything else.
- **Month 6:** under 150 seats while runway is under 6 months. Open the acquisition conversation seriously, with your co-maintainer in the room.
- **Any time:** support hours per account above 2 hours a month. Pricing is too low or onboarding is broken.

## Next actions, in order

1. Replace the 1% assumption with the 0.02–0.05% range above.
2. Decide the Pro license and key model.
3. Align with your co-maintainer on the acquisition offer.
4. Instrument the funnel (items 4–7) before launch day.
5. Verify marketplace fit and fees. Treat them as phase 2.