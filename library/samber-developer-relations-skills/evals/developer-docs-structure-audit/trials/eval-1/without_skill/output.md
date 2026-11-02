Next: pull Treejack's first-click breakdown for the "webhook retry policy" task before writing a single card sort. That number — not the 52% — tells you which wrong category users guessed, and that's the real design input. Full plan below; this is the document, ready to hand to leadership as-is.

---

# Kestrelpay Docs IA Rebuild — Starting Plan

## 1. What the numbers say, and what they don't

- **84% overall success, 67% direct-path**: a 17-point gap between "got there" and "got there without backtracking." That gap is a *labeling* problem — category names don't match users' search terms — not a pure findability failure. Fix scope: navigation labels and card grouping, not just page count.
- **52% on "find the webhook retry policy"**: the one task worth diagnosing before designing anything. Retry behavior is a cross-cutting concern — it could plausibly live under Webhooks, under Errors/Reliability, or buried inside a specific endpoint's reference page. A near-coin-flip success rate on one task usually means the *test participants split into two roughly equal mental models*, not that the content is simply hard to find.
- **What Treejack has that the headline numbers don't show**: the per-task first-click / "pietree" breakdown. Before running a card sort, pull that breakdown for this one task. If a large cluster of failing participants first clicked "Errors" and another cluster clicked "Webhooks," that confirms the split-mental-model diagnosis and tells you to solve it with cross-linking, not just a rename. If failures scatter randomly across many categories, the problem is deeper (the category doesn't exist yet in any form users recognize) and the fix is a new top-level pillar, not a cross-link.

## 2. Quarter plan (13 weeks)

| Weeks | Work | Output |
|---|---|---|
| 1–2 | Pull first-click data per task. Content-audit all 210 pages: tag by type (concept / reference / guide / troubleshooting / changelog) and by cross-cutting concern (retries, idempotency, rate limits, versioning, auth). | Audit spreadsheet |
| 2–4 | Consolidate audit into ~60–80 representative cards (group near-duplicate reference pages into one card; don't card-sort all 210 individually). | Card set |
| 3–5 | Open card sort, 18–25 participants (external devs + support engineers who read docs daily — support eng sees where real users get stuck). Use OptimalSort or similar. | Grouping + label data |
| 5–6 | Synthesize into 2 candidate trees reflecting the two likely mental models (task/guide-first vs. resource/reference-first). | 2 draft trees |
| 6–7 | Closed tree test (Treejack) on both candidates, same 6 original tasks + 3 new ones targeting retries/idempotency/rate limits specifically. | Comparative scores |
| 7–8 | Pick winner, fix weak labels, run one more validation round if any task is still under target. | Final tree |
| 8–13 | Writers execute: rewrite/merge/split pages, build redirect map, restructure Docusaurus `sidebars.js`, add cross-cutting partials, QA links. | Shipped site |

## 3. Starting-point tree — hypothesis, not the deliverable

Treat this as the first candidate to run through the card sort and closed test, not as final.

```
Home (/docs)
├── Get Started (/docs/get-started)
│   ├── Quickstart (/docs/get-started/quickstart)
│   ├── Authentication (/docs/get-started/authentication)
│   └── Sandbox & Test Data (/docs/get-started/sandbox)
├── Core Concepts (/docs/concepts)
│   ├── Payments (/docs/concepts/payments)
│   ├── Refunds (/docs/concepts/refunds)
│   ├── Payouts (/docs/concepts/payouts)
│   └── Disputes (/docs/concepts/disputes)
├── Guides (/docs/guides)
│   ├── Accept a Payment (/docs/guides/accept-a-payment)
│   ├── Issue a Refund (/docs/guides/issue-a-refund)
│   ├── Handle a Dispute (/docs/guides/handle-a-dispute)
│   ├── Reconcile Payouts (/docs/guides/reconcile-payouts)
│   └── Go-Live Checklist (/docs/guides/go-live)
├── Webhooks & Events (/docs/webhooks)
│   ├── Overview (/docs/webhooks/overview)
│   ├── Event Types (/docs/webhooks/events)
│   ├── Delivery & Retry Policy (/docs/webhooks/retries)   ← canonical home for the weak task
│   ├── Signature Verification (/docs/webhooks/signatures)
│   └── Testing Webhooks (/docs/webhooks/testing)
├── Reliability & Errors (/docs/reliability)
│   ├── Error Codes (/docs/reliability/errors)
│   ├── Rate Limits (/docs/reliability/rate-limits)
│   ├── Idempotency (/docs/reliability/idempotency)
│   └── API Call Retry Behavior (/docs/reliability/api-retries)   ← distinct from webhook retries; cross-link both ways
├── API Reference (/docs/api)   [generated from OpenAPI]
│   ├── Payments / Refunds / Payouts / Disputes / Webhooks endpoints
├── SDKs & Libraries (/docs/sdks)
├── Security & Compliance (/docs/security)
│   ├── PCI DSS (/docs/security/pci-dss)
│   └── KYC/AML (/docs/security/kyc-aml)
├── Changelog & Versioning (/docs/changelog)
└── Support (/docs/support)
```

**Why this targets the weak task directly**: "Delivery & Retry Policy" gets its own named L2 slot under Webhooks — worded the way users phrased the task, not buried in a generic "Webhooks" catch-all page. But if the first-click data shows a real split (some users think "Errors," some think "Webhooks"), don't force one home — keep one canonical page and add a contextual cross-link + short admonition from the other section, and from every endpoint reference page that fires a webhook. One source of truth, multiple entry points.

## 4. Validation loop

Run the closed tree test on the winning candidate with all 6 original tasks plus the 3 new cross-cutting ones. Targets before you call the tree final:

- Overall success ≥ 90%
- Direct-path rate ≥ 80% (closes most of the current 17-point gap)
- Webhook retry task specifically ≥ 85%

Anything below target on a specific task: fix the label or add a cross-link, retest that task only — don't re-run the full battery each time.

## 5. Migration mechanics

- Audit spreadsheet columns: old URL, new URL, page type, action (keep / merge / split / kill / redirect), owner, cross-cutting tags. 210 pages for one payments API is high; expect real consolidation, not just reshuffling.
- Full 301 redirect map, old → new. Crawl the shipped site afterward (Screaming Frog or equivalent) and confirm zero broken internal links and zero orphan pages.
- Rebuild `sidebars.js` categories to mirror the validated tree exactly; Docusaurus breadcrumbs derive from sidebar structure, so getting this right fixes breadcrumbs for free.
- For cross-cutting concerns (retries, idempotency, rate limits): author once as an MDX partial, include it contextually in every reference page it applies to. Prevents the "which page owns this" problem from recurring as content drifts.

## 6. Post-launch measurement

4–6 weeks after launch: re-run a lighter test (first-click test is enough, not a full tree test) on the 3 previously weakest tasks. Pair with real signal: docs-search zero-result rate, support tickets tagged "couldn't find X," and — if available — time-to-first-successful-webhook-integration from product analytics.

---

Next: pull the first-click breakdown for the webhook-retry task from Treejack. That decides whether this is a rename or a cross-link fix, before you spend any writer time.