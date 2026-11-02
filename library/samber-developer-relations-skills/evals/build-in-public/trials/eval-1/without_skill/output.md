# Lumenpath /open Page — Plan for CEO Review (Friday)

## Bottom line up front

Buffer's transparency page took years to build and rests on a business Lumenpath doesn't have: bootstrapped-then-lightly-funded, B2C/prosumer SaaS, no institutional board seats, no enterprise customers underwriting payment risk on Lumenpath's balance sheet. Copying the artifact without copying the conditions creates real legal and competitive exposure. Recommend shipping a real, credible page by end of Q1 — but not the literal Buffer spec — and getting three sign-offs (legal, finance, board) before committing to any number publicly.

This is the conversation to have with the CEO before Friday, not after.

---

## 1. Why "just copy Buffer" doesn't transfer cleanly

**Buffer's actual page** (open.buffer.com), as it's run: a revenue dashboard (MRR trend, not raw ARR tied to identifiable contracts), a public salary formula (role × level × location × experience — a calculator, not a raw band table), equity breakdown, diversity data. Buffer has no institutional VC board seat exercising consent rights over disclosure, and its customers are individuals/small teams, not enterprises with vendor-risk committees.

Lumenpath differs on every axis that matters here:

- **Payments infrastructure** — customers underwrite vendor stability before integrating. Public revenue swings (a normal thing in Series B growth) read as risk signals to enterprise procurement and to regulators/banking partners.
- **Institutional cap table** — two leads likely hold information rights, board consent rights, and possibly restrictions on public disclosure of financials under the investment agreements. This is a **legal question, not a marketing one** — check the stock purchase / investor rights agreement before promising anything.
- **Competitive dynamics** — ARR and NRR are the two numbers competitors, industry analysts, and journalists most want. Publishing them live hands competitors a real-time scoreboard; publishing them and later having a bad quarter hands them a headline.
- **Regulatory optics** — payments companies already draw more regulatory and press scrutiny than a social-media scheduling tool. A dip in live ARR or NRR is more likely to become a story here than at Buffer.

None of this means "don't do it." It means the CEO's Q1 deadline needs a scope decision, not just a build plan.

---

## 2. Risk map (walk the CEO through this before scope, not after)

| Area | Risk if shipped as literally requested | Mitigation |
|---|---|---|
| Investor rights | Board/investor consent may be contractually required before public financial disclosure | Legal reviews investor rights agreement + board consent process this week |
| Competitive intel | Live ARR/NRR gives competitors real-time growth-rate and churn signal | Publish lagged (prior quarter) and/or ranges/rates instead of exact live figures |
| Customer perception | Enterprise payments customers may treat visible dips as vendor-risk signal | Frame metrics with context (narrative, not bare number); consider gating full detail behind a customer/investor login for sensitive granularity |
| Compensation/legal | Publishing salary bands without a pay equity audit invites disparate-impact claims if actual pay doesn't match published bands | Run a pay equity audit before publishing; publish bands only where reality matches |
| Regulatory | Payments companies draw outsized scrutiny; a public financial swing can become a story faster than at a typical SaaS company | Finance/Legal/Comms jointly own the metric definitions and update cadence |
| Reversibility | Once a number is public, retracting it is a bigger story than never publishing it | Ship in phases, narrowest-safe scope first; treat each phase as a go/no-go gate |

---

## 3. Recommended phased scope for Q1

Don't present this to the CEO as "yes" or "no" — present it as three independently shippable phases, each defensible on its own, so Q1 has a real deliverable even if legal/board sign-off on the riskiest piece slips past the quarter.

### Phase 1 — Salary bands (lowest legal risk, highest trust payoff, ship first)
- Publish a **salary band table per engineering level**, built the way Buffer builds theirs: a transparent formula (level × location × experience multiplier), not just a static table that goes stale.
- **Gate before publishing:** run a pay equity audit (comp/People team + outside counsel) confirming actual pay matches the bands you're about to publish. Publishing bands that don't match reality is the single biggest source of legal exposure in this whole project — worse than not publishing at all.
- Timeline: audit + band finalization is the long pole, not the page. Realistic: 4–6 weeks for People/Finance to finalize defensible bands, 1 week for the page.

### Phase 2 — Business metrics, lagged and directional (not live, not raw ARR)
- Publish **NRR** and a **growth-rate band for ARR** (e.g., "$40–45M ARR" or a rate, not a live ticking number), updated quarterly on a fixed lag (e.g., one quarter behind, same pattern most public companies use before earnings, minus the SEC filing).
- Avoid "live" entirely for Phase 2. Live implies a real-time feed from finance systems into a public page — that's both a harder engineering lift and the highest-risk version of this feature. Quarterly-updated, board-approved numbers get 80% of the trust signal at a fraction of the risk.
- **Gate before publishing:** legal confirms investor rights agreement doesn't restrict this; board explicitly approves the disclosure and the update cadence.

### Phase 3 — Live ARR dashboard (only if Phase 1–2 land clean and leadership still wants it)
- This is the one to explicitly *not* promise for end of Q1. It requires: board approval for real-time public disclosure, a finance-to-web data pipeline with review controls (no number goes live without a human check), and legal sign-off on a standing basis, not a one-time review.
- Recommend scoping this as a **Q2 stretch goal**, contingent on Phase 1–2 going well and investor sign-off. Don't let the hardest, highest-risk piece anchor the Friday deadline.

---

## 4. What to bring to the CEO Friday

Lead with this, not the build plan:

1. **"We can ship something real and credible by end of Q1 — salary bands with a defensible methodology, plus lagged business metrics. Live, real-time ARR is a Q2 conversation, and it needs board and legal sign-off first, not just a marketing decision."**
2. **Three approvals needed this week, before any page work starts:**
   - Legal: review investor rights agreement for disclosure consent requirements.
   - Finance: define which metrics get published, at what lag, on what update cadence, and who owns the "is this number accurate" check every cycle.
   - People/Comp: commit to a pay equity audit timeline; the audit — not page design — is the critical path for Phase 1.
3. **One explicit ask:** get 30 minutes on the board's calendar this month, not in Q1's final week, to walk investors through the plan before anything is public. Surprising a board with a live-ARR page after the fact is the failure mode to avoid.

---

## 5. Build plan (once scope is approved)

**Page (`lumenpath.com/open`):**
- Static content sections: mission/why-we're-doing-this, salary formula + band table, business metrics (NRR + ARR range/growth rate), update-cadence disclosure ("last updated: [date], next update: [date]").
- No live data feed for Phase 1–2 — these are manually-updated, reviewed numbers on a fixed cadence, published as static content or a lightweight CMS entry. This avoids building (and securing) a real-time pipeline from finance systems to a public webpage before it's actually needed.
- Design: match existing site design system; this is a trust/credibility page, keep it legible and number-forward, not a marketing showpiece.

**Data/process, not engineering, is the critical path:**
- Comp bands: People + Finance + outside counsel (pay equity audit) — 4–6 weeks.
- Business metrics: Finance defines the exact metric methodology (how NRR is calculated, what counts in ARR) and gets board sign-off on the disclosure — 2–4 weeks, parallel to the comp audit.
- Legal: investor rights review — start this week, it can block everything else.

**Suggested Q1 timeline (assuming ~12 weeks left):**
- Weeks 1–2: legal review of investor rights; kick off pay equity audit; draft metric definitions with Finance.
- Weeks 3–6: pay equity audit completes; bands finalized; board conversation on Phase 2 metrics.
- Weeks 6–8: page build (design + content), internal review.
- Weeks 8–10: legal/finance final sign-off on published numbers; soft internal launch (all-hands preview).
- Weeks 10–12: public launch, Phase 1 (bands) + Phase 2 (lagged metrics) live. Phase 3 (live ARR) scoped as Q2 proposal, not shipped.

**Owners:**
- You (Marketing): page, content, launch comms, cross-team coordination.
- Finance: metric definitions, update cadence, accuracy sign-off each cycle.
- People/Comp: band methodology, pay equity audit.
- Legal: investor rights review, ongoing disclosure risk review.
- CEO/Board: final go/no-go on Phase 2 metric disclosure and any future Phase 3 conversation.

---

## 6. The one thing not to do

Don't let "the CEO wants Buffer's page by end of Q1" turn into shipping literal live ARR without legal and board sign-off just to hit the date. A transparency page that has to be walked back after a bad quarter, or that triggers an investor rights dispute, does more brand damage than shipping a narrower, defensible version on time. The phased plan above hits the Q1 deadline with something real — it just isn't the exact spec the CEO read over the weekend, and that's the conversation worth having with him directly before committing to anything publicly.