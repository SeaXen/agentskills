# Hestbury DevRel Plan: Enablement Without a Roadmap Seat or a Chat Queue

## The actual constraint, stated plainly

DevRel here has one job: **make the docs answer the question before a partner opens a ticket.** Not community-building for its own sake, not brand awareness, not a new engineering surface. The roadmap freeze and the no-Discord rule aren't obstacles to work around — they're the spec. They rule out the two most common (and laziest) DevRel moves: "ask eng for a better SDK" and "stand up a chat server and see what happens." Everything below fits inside what already exists: the docs, the API as it is today, and channels Hestbury doesn't have to staff or own.

## Three pillars

**1. Docs as the support tier.** Every ticket that could have been a doc is a docs bug, not a support win. Treat the support queue as the docs team's QA log.

**2. Async, unowned channels over owned real-time ones.** Public, searchable, indexable, no on-call. GitHub Discussions on the public API repo and a Stack Overflow tag do the job a Discord would, without the staffing model the founder is right to avoid — a chat server implies someone always watching it; a Discussions thread doesn't.

**3. Partners answer partners.** A small, unglamorous champion track turns your three or four most capable integrators into first responders on Discussions/Stack Overflow, so answers scale without headcount or a new platform.

## The mechanism: ticket-to-docs feedback loop

This is the load-bearing process. Without it, "improve docs" stays a slogan.

1. **Tag every inbound ticket** at intake with one of: `docs-gap` (answer should exist, doesn't), `docs-findability` (answer exists, wasn't found), `product-behavior` (working as intended, confusing), `bug`. Support does this in under 10 seconds per ticket — it's a dropdown, not a project.
2. **Weekly triage (30 min, DevRel + one support lead):** pull everything tagged `docs-gap` or `docs-findability` from the past 7 days, cluster by topic.
3. **48-hour docs SLA** on any topic that recurs 3+ times in a rolling 30 days: DevRel ships a fix (new page, expanded example, clarified error table) within 2 business days of the cluster crossing threshold.
4. **Close the loop publicly**: reply to the original ticket-filer with a link to the new/updated doc. This is also your best cold indicator that the fix worked — track whether that topic recurs in month two.
5. **No engineering asks beyond DX polish.** DevRel may request clearer error messages, a complete OpenAPI spec, or better field descriptions — these are docs-adjacent, not roadmap items, and should be filed as low-priority DX tickets, not features. If eng says no, the fallback is always "document the workaround," never "wait for the fix."

## Channel model: enablement without an owned queue

| Need | Owned-chat instinct | What to do instead | Why it fits the constraint |
|---|---|---|---|
| Real-time-feeling Q&A | Discord/Slack server | GitHub Discussions on the public API repo | Async, public, SEO-indexed, no 24/7 staffing implied |
| Long-tail "how do I" questions | Support ticket | Stack Overflow tag (`hestbury-api`), monitored not owned | Existing audience, existing moderation, zero infra |
| Partner-to-partner help | Community manager in a chat | Champion track answering in Discussions/SO | Distributes load without adding a channel |
| "I need to talk to a human now" | Discord support channel | Keep this on the existing support ticket system | Founder's actual objection is scope creep into support — don't blur that line |
| Recurring live-feeling touchpoint | Weekly community call | Monthly async "office hours" post: top questions from the past month, answered in writing, indexed like a doc | Gives the ritual without the standing calendar commitment |

GitHub Discussions specifically: it's already adjacent to a public-API product, it doesn't need a new tool contract, and unlike Discord/Slack, nobody expects an answer in 4 minutes — which is exactly the expectation the founder is trying to avoid creating.

## Champion track (lightweight, not a program with a logo)

- Identify 3–5 partner engineers already answering questions unprompted, filing sharp bug reports, or building visible integrations.
- Personal outreach, not an application form. Offer: early changelog access, a monthly 20-minute call with DevRel (not a support line — a feedback line), public credit on the Discussions leaderboard and in the monthly changelog.
- Ask in return: nothing mandatory. No quotas. The only real ask is "when you see a question you know the answer to, answer it before support has to."
- This is the whole community strategy. No tiers, no swag budget, no separate platform — it exists inside Discussions and Stack Overflow.

## 90-day rollout

- **Weeks 1–2:** Ship ticket-tagging taxonomy in the support tool. Pull last 90 days of closed tickets, retroactively tag, and produce the first top-20 recurring-topic list — this is your backlog, not a guess.
- **Weeks 3–6:** Docs remediation sprint against that top-20 list. Open GitHub Discussions on the API repo, seed it with 10 real answered questions pulled from the ticket backlog (so it doesn't launch empty). Start monitoring the Stack Overflow tag.
- **Weeks 7–9:** Personal outreach to champion candidates. First monthly async office-hours post. Dashboard (below) goes live with baseline numbers from weeks 1–2 as month zero.
- **Weeks 10–13:** First full monthly cycle closed end to end: tickets tagged → triaged → docs shipped → loop closed → dashboard reported. Review what didn't work before scaling anything.

## Monthly KPI dashboard

Ten metrics, all answerable from data Hestbury already has (support tool, docs analytics, API logs, GitHub). No new instrumentation contract required beyond the ticket-tagging dropdown and a "was this helpful" widget on docs pages.

| # | Metric | Definition / formula | Source | Direction |
|---|---|---|---|---|
| 1 | Docs-attributable ticket volume | Count of tickets tagged `docs-gap` in the month | Support tool | ↓ month over month |
| 2 | Ticket deflection rate | % of `docs-gap` topics from month N that do NOT recur as new tickets in month N+1 | Support tool (topic-tagged) | ↑ toward 100% |
| 3 | Docs SLA adherence | % of qualifying topic clusters (3+ tickets/30d) fixed within 48 business hours | Triage log | ↑ toward 100% |
| 4 | Docs page helpfulness | % thumbs-up on "Was this helpful?" widget, site-wide and for the top 20 pages by traffic | Docs analytics | ↑ |
| 5 | Internal docs search zero-result rate | % of on-site doc searches returning no results | Docs search analytics | ↓ |
| 6 | Time-to-first-successful-API-call (TTFAC) | Median time from API key creation to first 2xx response | API logs | ↓ |
| 7 | Quickstart completion rate | % of new API keys reaching a first successful call within 24h of creation | API logs | ↑ |
| 8 | Self-serve resolution rate | % of GitHub Discussions / Stack Overflow questions resolved without an escalation to a support ticket | Discussions + SO tag + support tool cross-reference | ↑ |
| 9 | Champion-answered share | % of Discussions/SO questions answered by a non-employee champion before staff responds | Discussions/SO activity log | ↑ |
| 10 | Activation depth | % of partners who call a second, distinct endpoint within 30 days of first successful call (proxy for "enabled," not just "onboarded") | API logs | ↑ |

**Reporting format:** one page, one row per metric, this month vs. last month vs. 3-month trend, plus a two-line "what we shipped" note tying movement to specific docs fixes. No metric on this list requires a product change to move — every one of them moves on docs, content, or the champion track alone, which is the actual test of whether this plan respects the constraints it was built under.

## Guardrails (what this plan deliberately does not do)

- No Discord, Slack, or any owned real-time channel — not "for now," a permanent constraint per founder direction.
- No feature requests to engineering framed as roadmap asks; only DX/docs-adjacent tickets (error messages, OpenAPI completeness), filed as low-priority and never blocking on a response.
- No community program with quotas, tiers, or a budget line that needs sign-off to sustain — the champion track survives if DevRel is a team of one.
- No vanity metrics (follower counts, star counts, event attendance) on the monthly dashboard — every metric above ties directly to the stated problem: partners filing tickets docs should have answered.