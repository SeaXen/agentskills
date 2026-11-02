⚠️ Before the draft: two parts of this plan match this skill's documented backlash patterns, not its survivable ones. Flagging both, then delivering the announcement adjusted to survive them — reasoning is in [references/pricing-change-cases.md](skill-wip/samber/developer-relations-skills/skills/devtools-pricing-strategy/references/pricing-change-cases.md).

- **Build-history to $49 plan** is close to word-for-word the skill's own catalogued "negative example": *"We're moving the audit log to the Business tier... it's been free since launch... existing customers move on their next renewal."* That exact shape is named as the failure pattern to avoid, and rule 5 in step 6 is explicit: never move an existing capability from free to paid. If build-history is also how customers watch their own cache usage, it may additionally sit on the never-paywall list ("visibility into the customer's own usage").
- **Cache 10 GB → 2 GB, same-day announce-and-ship** breaks two rules at once: reversing a public "always include 10 GB" promise (the specific detail that made Unity's 2023 Runtime Fee unsurvivable was reversing a stated 2019 promise, not the fee itself), and zero notice between announcement and effect (rule 3: announce *before* shipping).

**Adjusted plan** (same 3-week timeline you gave, restructured so it survives):

| Cohort | Cache storage | Build-history view |
|---|---|---|
| Accounts existing before 2026-10-14 | Stays 10 GB, indefinitely — this is the grandfathering, not "until next renewal" | Stays included at current plan, indefinitely |
| Accounts created on/after 2026-10-14 | 2 GB | Included starting at $49/mo |

- Announce **today**, effective **2026-10-14** (your three weeks, moved from same-day to real notice).
- New-accounts-only is the sanctioned way to shrink a free tier (step 6.6) — it keeps the "always include 10 GB" promise intact for everyone who was actually promised it.
- If you need build-history revenue from the *existing* base too, don't re-gate the current view — ship something genuinely new at $49 (longer retention, export, alerting on build-history) and keep today's view free where it already is. That's a legitimate upsell instead of a retroactive gate.
- Name an owner for the public thread before this goes out, with one pre-approved concession (typically: extending the grandfather window for anyone who asks).

Here's the announcement, written to that adjusted plan:

---

## Changes to Tollgate's free tier and build-history view

*Published 2026-09-23 — effective 2026-10-14 for new accounts. Nothing changes for existing accounts.*

Starting **October 14, 2026**, two things change for new Tollgate accounts:

- **Free tier cache storage** is 2 GB (previously 10 GB).
- **Build-history view** is included starting on the **$49/mo plan** (previously included on every plan).

**If your account exists before October 14, 2026, none of this applies to you.** Your free tier keeps its 10 GB of cache storage for as long as you keep the account — that's a direct continuation of the commitment in our [2024 announcement post](#) (which we've updated with a note pointing here). Your build-history view stays included at your current plan, at no extra cost, indefinitely.

### Why

Cache storage is our largest infrastructure cost, and as Tollgate has grown we've had to size the free tier against what a real side project needs rather than what we could afford to give every signup. We'd rather make that change once, honestly, for new accounts than erode it quietly for everyone.

Build-history moving to the $49 plan lets us keep investing in it — without changing what anyone already using it today relies on.

### FAQ

**I created my Tollgate account before October 14, 2026 — does anything change for me?**
No. Your cache storage limit and build-history access stay exactly as they are today, with no end date.

**Is the 10 GB free-tier limit for my account permanent, or will it shrink later too?**
Permanent, tied to your account. We are not retroactively lowering storage for any account that exists before the date above.

**I'm on a paid plan below $49/mo and I use build-history today — do I lose it if I don't upgrade?**
No. You keep it. We're not moving anything that's already part of your plan to a higher tier.

**What happens if I create a new account, or a teammate does, after October 14?**
New accounts get 2 GB of free cache storage, and build-history view is included starting at $49/mo.

**Who do I talk to if this affects my team in a way this post doesn't cover?**
[support channel] — we're reviewing edge cases individually for the first month after this ships.

---

One more step this needs before publishing: add a short update note at the top of the 2024 post itself, linking here — leaving "always include 10 GB" live and unqualified on that page while this one exists elsewhere reads as a quiet reversal even though the promise is actually being kept for everyone it was made to.