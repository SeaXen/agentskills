## Bottom line

60 MCQs at 70% is a workable **content format**, but it's the wrong thing to optimize first. With 15 person-hours/week total and a hard Q1 deadline, the real risk isn't "did we write good questions" — it's "did we correctly scope what Northbridge actually needs to sign." Fix that first; everything else is execution.

## Step 1 (this week): Decouple the deal from the full program

Don't let "launch a public certification program" and "unblock Northbridge" be the same deliverable — they have very different scopes and you don't have the hours to do both well by Q1.

- Ask Northbridge procurement directly: how many engineers, by what date, and does an internal/beta assessment satisfy the requirement, or do they need a polished public credential?
- Propose to your CRO/AE: contract signs when N named Northbridge engineers pass an internal "Trellisway Certified Integration Engineer — Beta" assessment. Public launch follows in Q2.
- This alone can cut your Q1 build from "production platform + badges + marketing" down to "a good exam + a PDF certificate," while all the content you write is still reusable for the real launch.

If Northbridge insists on a public, brand-carrying credential before they'll sign, say so now — that changes the timeline and budget math below materially.

## Step 2: Write a blueprint before writing questions

Don't start drafting MCQs. Define 4–6 competency domains first, weighted by what actually breaks Northbridge-style integrations — not evenly split:

- Auth & API keys
- Building/triggering workflows
- Error handling, retries, idempotency
- Webhooks & rate limits/pagination
- Debugging & observability of failed runs
- Versioning/deployment of workflows

Source the weighting and the hard questions from the SE's support tickets and past onboarding calls — that's your real syllabus, not the docs table of contents. This is the SE's highest-leverage 2–3 hours: mine their own ticket history for "what do engineers actually get wrong."

## Step 3: Reconsider MCQ-only

Pure MCQ is fast and cheap, but a sophisticated procurement/technical evaluator can dismiss it as "not real certification." Given your resourcing, don't abandon MCQ — but don't ship it alone either:

- Keep ~50–55 MCQs (cheap, automatable, scales to future candidates).
- Add 3–5 scenario/short-answer items (e.g., "here's a failing workflow config, what's wrong") graded manually by the SE. This is where the credibility comes from, at low incremental cost.
- Build a bank of ~80–90 questions, not exactly 60 — you'll retire weak items after the pilot and want randomized subsets so Northbridge's engineers can't just trade answers internally.

70% as a starting pass mark is fine. Treat it as provisional: recalibrate after your first 20–30 test-takers via basic item analysis (which questions does everyone miss — bad question; which does everyone ace — no signal).

## Step 4: Buy, don't build, the platform

You have $80k and no committed budget past this year — don't lock into anything multi-year or engineering-heavy.

| Need | Recommendation | Rough cost |
|---|---|---|
| Northbridge unblock (Phase 0) | Google Form / Typeform + manually issued PDF certificate | $0 |
| Real quiz engine (public launch) | Off-the-shelf (ClassMarker, ProProfs, or similar) — annual plan | $2–5k |
| Credential/badge | Credly/Acclaim — procurement recognizes this format | $3–6k |
| Content help if bandwidth breaks | Contractor technical writer/instructional designer for question drafting | $10–15k |
| Landing page + launch assets | Contractor or existing site template | $5–8k |
| Buffer / unknowns | — | remainder (~$45k+ unspent — don't feel pressure to spend it, hold it) |

Don't build a custom exam engine or proctoring system. Nothing about a $400k deal requires that, and it would eat your entire hour budget.

## Step 5: Q1 timeline (assuming Phase 0 negotiation succeeds)

| Weeks | DevRel lead (10h/wk) | SE (5h/wk) |
|---|---|---|
| 1 | Get Northbridge's exact requirement; draft blueprint | Mine support tickets for common failure patterns |
| 2–3 | Draft ~55 MCQs off docs + blueprint | Technical review of MCQs; draft 3–5 scenario questions |
| 4 | Stand up Google Form beta version; issue to Northbridge's named engineers | Grade scenario answers; sit the beta exam themselves first as a dry run |
| 5–6 | Item analysis on beta results; fix/retire bad questions; pick real quiz vendor | Second pass technical review |
| 7–8 | Stand up real platform + Credly badge; write landing page copy | Final technical sign-off |
| 9–12 | Public Q1 launch; recalibrate pass mark with real data | Ongoing question review as needed |

This gets Northbridge unblocked by week 4, well ahead of a full public launch, and gives you a real pilot cohort (their own engineers) before you expose the exam to the world.

## Step 6: Don't skip governance

A 60–90 question bank tied to specific API behavior rots the moment you ship a breaking change. Put a standing 2-hour quarterly review on the calendar, triggered by your changelog, and add a "flag this question" link for candidates. Otherwise this becomes a support burden nobody owns by Q3.

## What to escalate now, not later

If by end of week 3 the blueprint + question drafting isn't tracking to this timeline, tell your CRO immediately — the choices are more hours, a contractor from the $80k, or pushing the *public* launch to Q2 while keeping the Northbridge-specific fast path intact. Don't discover that tradeoff in week 7.