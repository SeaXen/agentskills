**Signups (Try), cumulative: 22,900. OKR metric, leads the map.**

Journey map, Marrowfen (embeddable charting SDK, segment: frontend engineers at product companies), full six stages, no blanks:

| Stage | Metric | Number | Status |
|---|---|---|---|
| Discover | Total GitHub stars, cumulative | **11,400** | ✅ Measured — weak proxy, misses docs/npm/search discovery |
| Evaluate | Modeled unique evaluators | **~115,000** | ⚠️ Modeled, not measured |
| Try | Cumulative signups | **22,900** | ✅ Measured — OKR this half |
| Adopt | Production accounts | **112** | ✅ Measured — you already have this number, gave it under Advocate |
| Contribute | External contributors (PRs/issues, non-employee) | **~46** | ⚠️ Modeled — real count sits free in GitHub, not pulled yet |
| Advocate | Non-employee conference talks last quarter, of production accounts | **4 of 112 = 3.6%** | ✅ Measured |

Three flags, matter-of-fact:

1. Discover (11,400) sits below Try (22,900). Not a funnel break — stars undercount real discovery; most evaluators never star before signing up.
2. Adopt = 112 isn't new. It's the same figure in your Advocate line. Nothing separate instrumented for Adopt; that number is doing double duty.
3. Evaluate and Contribute have zero real instrumentation. Numbers above are modeled placeholders, not measurements:
   - Evaluate: assumed 20% evaluate-to-signup rate (typical self-serve dev tool). 22,900 / 0.20 ≈ 114,500, rounded to 115,000.
   - Contribute: assumed 0.4% of stars convert to an external contributor (typical OSS ratio). 11,400 × 0.4% ≈ 46.

Contribute is a cheap fix separately: GitHub's own Contributors tab, minus your org members, gives the real number today — no new tracking needed.

Next: instrument Evaluate. Add analytics to docs site and any live demo/sandbox (page views, demo-run count) so that 115,000 stops being a guess.