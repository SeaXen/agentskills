# Naviform Champions — what to do with the $2,500/member/year

## The diagnosis in one line

Every perk you listed — hoodie, sticker pack, Discord badge, 20% discount code — sits on the bottom rung of the perk ladder (**status objects**) or is explicitly flagged as weak (**generic discount codes**). None of it is access, and none of it is funding. For a champion population that is almost entirely unpaid-everything (indie devs, students, hobbyists) with zero employer budget behind them, that's the worst possible perk mix: it's the exact "front-loaded swag, access never materialized" pattern that predicts champions going quiet by month three. The new budget doesn't need to buy *more* of what you have — it needs to fill the two rungs you're currently missing entirely.

Here's the reframe that matters: for a typical vendor champions program, funding (travel, tickets, credits) is usually the *least* efficient perk to run — a budget line, a signature, a tax check, every time. But this skill's own guidance flags two conditions that flip that ranking, and Naviform hits both at once: **individual-adoption audience** (hobbyists, students, indie devs with personal, not corporate, budgets) and **regional cohorts** (Indonesia, Brazil, Nigeria — markets you don't staff). For this specific population, $2,500 in real, spendable money is disproportionately valuable precisely *because* nobody else is expensing anything for them. That's the lever. Spend it there.

## Readiness check (Step 1) — before touching the perk list

| Gate | Status |
|---|---|
| Candidate pool (≥10 nameable, ideally 2-3× cohort) | Not provided — confirm current roster size and how many were visibly active last quarter before locking budget-per-member math |
| Owner with recurring hours | Not provided — flag before committing to any beat (quarterly briefing, review calls) below |
| Something only Naviform can give, beyond swag | **Currently fails.** This is the actual gap the budget should close |
| Feedback capacity (someone who receives and acts on champion input) | Not provided — critical, because access perks below assume this exists |
| Conduct baseline (code of conduct + moderation path) | Not provided — needed before any perk creates implied authority |

None of these block spending the budget well, but confirm them before publishing anything — an unanswered owner-hours question is how a quarterly briefing perk gets promised and then quietly skipped, which is worse than never promising it.

**Archetype:** keep the existing small invite-only circle. Nothing in what you described (no public roster problem, no rejection-fairness complaints) argues for switching to a published-criteria application cohort yet. Fix the engine first; consider graduating the shape only once the pipeline outgrows what a private tap can fairly select from.

## Where the $2,500/member/year actually goes

Structure it as a **menu, not a gift**: each champion gets a $2,500 annual allowance and chooses from the list below, up to the cap. Unused balance is forfeited at term end, not paid as cash, not rolled over — a discretionary allowance stays a recognition perk; a cash-equivalent payout starts to look like compensation for services, which is the employment-classification trap Step 6 warns about.

**Funding tier (this is most of the $2,500 — self-set split, recalibrate after two quarters):**

- **Meetup/workshop hosting budget** (~$300–600) — pay a champion in Jakarta, São Paulo or Lagos to run a local Naviform meetup: venue, food, a small speaker fee for themselves. This is the single highest-leverage line item you have: it buys exactly the "community support capacity in a region you don't staff" outcome directly, not as a side effect.
- **Conference/meetup travel + ticket** (~$400–1,200) — regional and virtual first; a $2,500 ceiling won't cover international travel for most of this cohort, so don't design around it as the default.
- **Cloud/hosting/device credits** (~$100–300) — genuinely on-product: a low-end Android device or a cheap VPS to test sync under flaky connectivity is more useful to a local-first sync engine's champion than almost any other line item, and it's cheap.
- **Data/connectivity stipend** (~$10–20/month) — worth naming explicitly for Indonesia and Nigeria, where intermittent connectivity is a real cost of participating at all, and it's thematically on-brand for a product built around offline-first sync.
- **Course/certification voucher** (~$100–300) — a distributed-systems, CRDT, or local-first-architecture course. Members keep this after they leave.
- **Translation/localization commission** (~$200–500) — pay champions to translate docs into Bahasa Indonesia or Portuguese. This is a funding perk *and* it directly produces the regional-reach outcome your budget should be justified against — track this line separately, it's your strongest ROI story to Finance next cycle.

**Access tier — add these even though they cost $0, because Step 1's "something only you can give" gate currently fails without them:**

- A recurring async-friendly call with an engineer (record it — ID/BR/NG timezones won't all make a live slot).
- A private channel where champions see sync-engine roadmap items before anyone else.
- Pre-release/beta builds.
- A named credit in release notes for champions whose feedback shipped.

**Platform tier — also $0:** reserved guest-post slot on the Naviform blog, cross-posting their content/talks on Naviform's own channels, a referral to conference organizers for a speaking slot.

**What to retire or downgrade:**

- The 20% discount code isn't a real perk to the champion — it's a task performed on Naviform's behalf. Keep it only if intake feedback says members actually value having it to share; don't treat it as part of the recognition value.
- Don't scale up the hoodie/sticker line. Status objects are the tier that costs the least and buys the least — money spent there is money not spent on the two tiers you're missing.

## Regional execution — the part that actually breaks if skipped

With no staff in Indonesia, Brazil or Nigeria, three mechanics decide whether this budget is usable at all rather than theoretical:

- **Payment rail**: use Wise, Payoneer, or direct-to-vendor payment (book the venue yourself, pay the course provider directly) rather than reimbursement-after-the-fact — asking an unpaid hobbyist to front $400 and wait for a wire transfer defeats the purpose.
- **No cross-border shipping for the new spend.** Physical swag already carries customs cost in these markets; don't add more shipped goods. Everything in the funding menu above is either a direct payment, a voucher, or a locally-redeemable credit.
- **Per-region calibration, not one global menu.** Elastic's champions program had to weight contribution points per region because one global table systematically under-recognized whichever market didn't match it — the same logic applies to a spending menu: what's meaningful is different in Lagos, São Paulo and Jakarta. Ask each region's champions what they'd actually use before finalizing the split (this is intake-form data, not a guess).

## Compliance, specific to this budget (Step 6)

- **Age**: students in the cohort may be under 18 in some jurisdictions — confirm age at intake if not already gated.
- **Tax**: a $2,500 annual allowance is large enough to be taxable income to the recipient in some of these jurisdictions. Say so explicitly rather than letting a champion find out from their own tax authority; direct payment-to-vendor (course provider, venue) sidesteps this for those specific line items but not for a cash stipend.
- **Disclosure**: any perk-funded travel, credits, or vouchers are a material connection under FTC-style endorsement rules if the champion posts about the product afterward — supply the wording, don't leave it to them to guess.
- **No quotas attached to the money.** The moment "translate the docs" or "run a meetup" becomes a deliverable with a deadline rather than a menu item a champion opts into, you've converted a discretionary allowance into unpaid work with real employment-classification exposure. Frame every funding line as "available if you want it," never "expected."

## Term, renewal, and the "spend or lose" trap

Because this is real money now, the program needs the exit mechanics it may not have had when the perks were just swag:

- **Term**: 12 months is the self-set default for a vendor program, but this audience churns faster than an enterprise cohort (students graduate, hobbyists' priorities shift) — budget a check-in at 6 months, not just at renewal.
- **Budget follows the term, prorated.** A champion who joins mid-year gets a prorated allowance, not the full $2,500; a champion who leaves mid-term forfeits the unused balance — this needs to be written down before the first person tests the edge case, not decided in the moment.
- **Don't let "use it or lose it" become "spend it badly in Q4."** The classic failure mode of a use-or-lose annual budget is a rushed, unrequested purchase in the last month to avoid returning the money to Finance. Commit this year's allocation against the menu now, spread across the year, and treat any December scramble as a sign the menu needs to be offered earlier next cycle — not as a reason to buy something nobody asked for.
- **Inactivity clause and alumni status**: no visible activity for 6 months → ineligible for the next term's allowance, moved to alumni. Alumni keep the dated title, not the budget.

## What to track next quarter (Step 8, self-set — recalibrate after two quarters)

Add these two to whatever scorecard already exists, because they're the ones that justify the new spend to Finance next cycle:

- **Funding utilization**: % of allowance actually claimed per member, and on which menu line. Low utilization on a line means kill it, not repeat it.
- **Regional output per dollar**: meetups run, translations shipped, per region — this is your renewal argument for the next $2,500 ask, and it's the one metric this budget can produce that swag never could.

## Before you publish anything

Confirm four things you didn't state above, since they change the specifics but not the direction: current roster size and last-quarter activity rate, who owns the program day to day and their monthly hours, whether a code of conduct and moderation path already exist, and whether "regional reach" is in fact the top outcome you'd name if forced to pick one. Everything above holds regardless of the answers; the exact dollar split across the funding menu and the term length are the two pieces worth revisiting once you have them.