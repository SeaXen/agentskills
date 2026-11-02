## What to tell the board

**Don't ratify the enterprise thesis on belief. Ratify a staged bet, gated on data you can pull before the meeting.**

Your co-founder's framing — "demand is obviously there, we never asked" — is exactly the failure mode this kind of decision usually dies from: an expensive, hard-to-reverse motion chosen because it sounds plausible, not because anyone measured it. Here's the case to bring instead.

### The math the claim has to clear

Sourced rule of thumb (Lenny's Newsletter, *The Transition*): a salesperson layered onto a self-serve motion should return **roughly 4x their fully loaded cost** in incremental revenue. That's the bar, not a nice-to-have.

- 2 AEs × $210,000 = **$420,000/year** fully loaded.
- 4x = **$1,680,000** in incremental ARR the two of them need to generate, combined.
- Your current total ARR: 4,100 accounts × $31/mo × 12 = **$1,525,200**.

So the ask is: two reps, hired cold, into a company with no prior sales motion, need to generate *more than your entire current ARR* in year one. That's not disqualifying on its own — a $210k AE with an $840k quota is normal in enterprise B2B — but it means the pipeline behind it has to be real, not assumed.

### What "demand is obviously there" is actually resting on

One number: **96% single-developer accounts** means only **164 accounts (4%)** show *any* multi-developer signal at all. That's the entire ceiling of team-scale accounts you can currently see — before checking whether any of them show the signals that actually predict an organizational buyer (sustained production usage, a security questionnaire request, an SSO/audit-log page visit, a self-hosting or procurement question). You don't have those numbers yet. "More than one developer" is the weakest of the three signals that matter — it tells you a team is using the product, not that anyone with budget wants to buy more than $31/month worth of it.

Sensitivity check on the $1.68M target:

| If qualified accounts convert at... | Accounts needed | Avg. incremental ACV required |
|---|---|---|
| 100% of the 164 | 164 | ~$10,200/account |
| A more realistic ~20% | ~33 | ~$50,900/account |

The second row is a real enterprise deal shape — plausible for a metrics backend — but you have zero evidence today that 33 of those 164 accounts would sign at that price. That's the actual question, and it's answerable in days, not quarters.

### The one fact to get before the meeting

Ask this directly, it's the cheapest test you have: **has any account, ever, asked to pay more than card self-serve pricing** — a security questionnaire, an SSO or audit-log request, a self-hosting or data-residency question, an invoice/PO instead of a card? If yes, count them and bring that number — it's your real qualified pipeline. If the honest answer is "never," then "we just never asked" is wrong: boundary-contact signals show up unprompted, without a salesperson, whenever real buying committees exist. Their absence is itself evidence, not a gap in your asking.

Also check: can you roll usage up to a company today (email domain, at minimum)? If not, an AE has no list to work — that's a build item that has to exist before either hire is productive, independent of how the headcount debate resolves.

### Recommendation

Take the board's approved budget, but spend it staged, not both seats at once:

1. **Hire one AE, not two**, explicitly tied to a written qualification rule (e.g., "2+ active developers on one domain, sustained production usage, or any boundary-contact signal") built from the 164-account pull above.
2. **Defer the second hire**, formally, to a named checkpoint: the first AE's trailing-quarter incremental ARR needs to clear ~$840,000 annualized (their own 4x bar) before the second seat is funded.
3. **Instrument account rollup and the three signal families now** (depth, spread, boundary contact) — this is the prerequisite the whole motion depends on, and it costs engineering time, not $420k.
4. **Don't let either AE contact anyone below the threshold.** Write the do-not-contact line down. Your self-serve base is 96% single-developer accounts at $31/mo — that's a real, working motion; an AE spraying outreach across it teaches your best channel that signing up costs you their inbox.

### What this isn't

Not a vote against your co-founder's instinct, and not a vote to kill the hire — it's a refusal to spend $420k finding out whether the instinct was right when a data pull can tell you first. It's also not a pivot to top-down enterprise sales: self-serve stays the entry point; the AE(s) convert accounts that already show real signal, they don't replace the funnel.

### What would change the recommendation

Fund both seats immediately, no staging, if the pre-meeting data pull already shows a double-digit count of accounts with boundary-contact signals at a deal size that clears $1.68M on its own — at that point the co-founder's instinct is confirmed, not assumed, and staging just slows you down.