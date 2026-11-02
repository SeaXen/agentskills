# Pallasgate: Free-Trial-to-Paid Journey Map

**The 340→9 number is wrong, not just ugly.** You're dividing this quarter's top-of-funnel by this quarter's bottom-of-funnel, but those aren't the same cohort — the 9 deals that closed this quarter started their journey 6-8 months ago. Fix the comparison before you fix the story.

## Why the flat ratio lies

Authorization touches every access decision in a customer's stack, so this isn't a self-serve SaaS purchase — it's two journeys stitched together:

1. **Champion journey** (the developer): signup → integrate → prove it works.
2. **Buyer journey** (the org): security review → procurement → contract.

The developer who signs up never signs the contract. They hand off to a security team and procurement, and that handoff alone adds months. Comparing raw signups to closed deals in the same quarter measures noise, not conversion.

## The two-lane map

| Stage | Who drives | What happens | Typical duration | Proof stage is done |
|---|---|---|---|---|
| 1. Signup (free tier) | Champion | Backend engineer hits a build-vs-buy wall on RBAC/ABAC, grabs an API key | Instant | First API call |
| 2. Technical validation | Champion | Integrates into a real service, models actual policies, tests edge cases | 2–6 weeks | Non-trivial policy set running in staging |
| 3. Internal proof | Champion | Shows it to their team, migrates one real service off in-house authz | 2–8 weeks (**biggest drop-off, and normal**) | A non-prod service depends on Pallasgate |
| 4. Champion builds the case | Champion → Buyer handoff | Writes the internal pitch: cost of building vs buying | 2–4 weeks | VP Eng / CTO / Head of Platform agrees to formally evaluate |
| 5. Security review | Buyer org (InfoSec) | Vets SOC2/ISO report, data flow, pen test summary, sub-processors — heavier scrutiny than typical dev tools because you sit in the access-control path | 3–6 weeks | Security sign-off |
| 6. Procurement | Buyer org (Legal/Finance) | Contract terms, DPA, pricing, possibly a competitive bake-off | ~3 months (your stated average) | Signed contract |
| 7. Close / paid conversion | Buyer org | Free-tier account linked to paid contract | — | First paid invoice |

Rough end-to-end, signup to close: **7–9 months**. That alone explains most of why 340 vs. 9 looks catastrophic — most of the 340 haven't had time to reach stage 6 yet, let alone close.

## What to put in front of the board instead

Replace the single ratio with the staged funnel, each stage reported as its own conversion rate:

```
Signups → Technically Validated → Internal Case Built → Security Review Started → Procurement Started → Closed Won
```

This does three things a flat ratio can't:

- Shows the real drop-off point (almost certainly stage 2→3, "many kick tires" — expected in PLG, not alarming).
- Lets you report a **leading indicator**: "X accounts are in security review or procurement right now" — pipeline in motion, not just wins.
- Lets you report **cohort-correct conversion**: take the 340 who signed up ~2 quarters ago, not this quarter's 340, and show how many of *them* closed.

## One next action

Instrument four missing events in your CRM/product analytics this week: `technical_validation_complete`, `internal_case_built`, `security_review_started`, `procurement_started`. Without these, next quarter's board slide is stuck with the same misleading ratio.