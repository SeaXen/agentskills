# Error Documentation Program — Business Case

**Ask:** 0.5 FTE, ongoing (not one-off), starting next cycle. Scope: top 20 recurring support failures.

**Problem:** Support handles ~1,400 tickets/quarter. A recurring subset are the same failures, answered from scratch every time, because the fix lives inside a closed ticket instead of a page a developer can find by pasting the error string.

**Objective:** Publish verified troubleshooting entries covering 80% of the top 20 recurring failure clusters by Q3 (this is a self-set baseline, negotiable against actual capacity — not an external benchmark), then track ticket volume per *covered* error against its pre-publication baseline. Not "zero tickets by Q3." No team resolves 100% of contacts through self-service — Gartner's December 2023 survey of 5,728 customers found only 14% of support issues fully resolve in self-service overall, and only 36% even among issues customers rated "very simple." A zero-ticket target sets this program up to be called a failure for hitting a ceiling nobody clears.

**Why the top 20, and not "every error":** clusters are ranked by reader-hours unblocked per hour of writing, not raw frequency — frequent, reproducible failures come first because they cost an afternoon each and empty the queue fastest. Part of the 0.5 FTE's job is triage: some of today's top 20 may turn out to need a product fix, not a page — a recent-release regression, or an error whose text alone can't tell a reader what to do. Those get escalated to engineering, not documented around, which is what keeps this an error-docs program and not a plan to write nice pages over defects. That gate is why this isn't a flat "write 20 pages" ask.

**Cost case:** withholding a number until we have one worth defending. The commonly quoted "$15–$50 per ticket" figure and "60–70% deflection" circulate industry-wide with no traceable source; a business case built on them fails the first fact-check. What we need from Finance instead: Verdant's actual fully-loaded cost per support ticket. With that one number, the savings math is mechanical: (ticket volume for the 20 covered errors, pre-publication) × (cost per ticket) × (reduction observed post-publication, per error, fixed comparison windows). We'll report the real figure once the first entries have a before/after window to measure against.

**The case beyond ticket cost:** Dixon, Freeman & Toman ("Stop Trying to Delight Your Customers," *Harvard Business Review*, 2010, drawing on CEB/Gartner research) found 96% of customers who go through a high-effort service interaction become more disloyal, against 9% for a low-effort one. Every one of the top 20 errors is currently a high-effort interaction — file a ticket, wait, get an answer that isn't written down anywhere. That's a retention argument independent of the ticket-cost math above.

**How we'll know it's working:** cluster coverage (%), ticket volume per covered error before/after on fixed windows, zero-result doc-search queries for the covered error strings (should trend to zero), share of entries touched since the last release (staleness check). We're tracking resolution rate and cost per resolution, not a site-wide "deflection rate" — a deflection number can look good while readers keep failing and re-contacting on the same error.

**Method, so this is auditable and not house style:** entries are captured from real ticket/issue/telemetry evidence (Knowledge-Centered Service model), each one verified by reproducing the failure and running the fix before it ships, and gated against a fix-vs-document decision before any page is written.

---

**What changed from your draft, and why:**

- Dropped the $15–$50/ticket figure and the 60–70% deflection figure — both are unsourced industry folklore, and a CFO's team can find that out in one search. Replaced with a request for Verdant's real cost-per-ticket and a savings formula to run once we have it.
- Dropped "pays for itself in a month" — it was arithmetic built entirely on the two numbers above; it doesn't survive their removal, and re-asserting it without them would cost more credibility than the slide gains.
- Dropped "drive tickets to zero" as the objective — replaced with a coverage target (80% of top 20) plus per-error ticket-volume tracking, and grounded the "why not zero" in Gartner's published self-service ceiling so it's not just our house opinion.
- Added the loyalty/retention argument (Dixon/Freeman/Toman) as a second pillar, since the cost pillar is now honestly provisional pending Finance's number.
- Kept your 1,400 tickets/quarter — that's Verdant's own observed volume, not a borrowed statistic, so it stays.