# Arbordyne: fixing the account rollup and the "devrel touch before opportunity" report

## What's actually broken

Two separate defects, both named directly in this failure pattern:

1. **The 4,100-person account is a free-mail domain caught by naive domain matching.** Domain-based rollup with no exclusion list collapses every stranger sharing a public webmail domain into one "account." Check today which domain that is — it is very likely gmail.com, outlook.com, or an equivalent, not a real company. Free-mail domains identify no company and must never enter account matching.
2. **The long tail of one-person accounts is the same bug's mirror image, not proof the rollup works.** Once free-mail signups get excluded, everyone left correctly shows one person per account by coincidence of how few engineers per company sign up on the free tier — but this also hides real misses: subsidiaries on regional TLDs, acquired brands, engineers using a personal-but-non-free domain. Don't read "1 person = 1 account" as validated; report what share of accounts resolved to an enrichment-confirmed company versus a bare domain match.

**Fix 1, today, an hour of work:** pull a free-mail-domain suppression list (gmail.com, outlook.com/hotmail.com/live.com, yahoo.*, icloud.com, proton.me, qq.com, 163.com, and the long regional tail) and exclude every one of those domains from account resolution. Signups on those domains stay person-level with `account_id = null` — they are not "no account," they are "no company can be inferred," which is a different and honest state. Add to the list the moment a new giant account appears; a 4,000-person account is the detector for a missing entry, so re-run this check monthly, not once.

**Fix 2, lower priority:** for domains that do resolve, add an enrichment step (Clearbit-class or manual) to catch the subsidiary/regional-TLD cases, and publish the resolved share (e.g., "68% of paid-tier accounts resolved to a verified company; 32% are single-domain matches, unverified") rather than presenting the rollup as complete.

## Why the lead-source field can't answer sales' question, and what it needs to become

Sales is asking a **timestamp-ordered join between two things**: devrel touches and opportunity creation, at the account level. A single CRM `lead source` field can't carry that, structurally, for three reasons:

- It's a bare channel with no evidence type and no confidence — a journey-linked touch and a sales rep's guess look identical once written to that field.
- It's one value per record, so it gets overwritten. Whatever touched the lead second wins, or whatever the CRM's own attribution rule (first-touch or last-touch, usually undocumented) decided — you cannot tell which, and you cannot recover the ones it overwrote.
- It lives on the Lead/Contact, not on the Account, and it isn't timestamped against the Opportunity's creation date — so "before they became an opportunity" cannot be computed from it at all, only guessed at.

Fix this by carrying three fields on every touch instead of one on the record, per the production runbook this skill cites: `source` (the channel), `source_basis` (`journey_linked` / `self_reported` / `campaign_window`), `source_confidence` (judged on evidence quality, never read off the basis). Concretely:

- Every devrel touch (docs visit, blog visit, webinar registration, conference badge scan, tagged-link click, community answer) becomes its own timestamped event, not a field overwrite.
- **Fail closed.** If a touch can't be tied to a person or account cleanly, record nothing. A missing touch is a visible gap; a wrong merge into someone else's history is silent corruption.
- **Never overwrite.** Backfilling only fills blank sources, never a slot that already holds a journey-linked or self-reported value.
- Push these into the CRM as a related-list/activity object on the Account, not a single field — "this account had a devrel touch before this stage" needs a table you can filter and count, not a category you can only read once.

## The identity spine this actually depends on

Arbordyne's motion is "both at once" — individual self-serve first, company-buying months later — which is exactly the case where person-level and account-level tracking both have to exist and get joined only where a real company resolves:

- `anonymous_id`: set on first visit to docs/blog/marketing, first-party, shared across every owned subdomain.
- `user_id`: assigned at signup, emitted with `anonymous_id` on the signup event so pre-signup history stitches forward.
- `account_id`: resolved from the signup domain **after** the free-mail exclusion above. Re-resolve it when procurement creates a real Account/Opportunity in the CRM, and backfill `account_id` onto that person's prior touch history at that point — this is what lets a docs visit from eight months before procurement started count.

Until this stitch is live and verified in production, expect near-zero attributed accounts, then a step-jump the week it ships. That jump is instrumentation turning on, not a change in what devrel is doing — annotate it, and don't compare pre-stitch and post-stitch periods as a trend.

## The report sales actually gets

Define it as one funnel view, not a CRM field query:

> **Accounts with a devrel touch before opportunity.** Entry: any touch event where `source_basis` is `journey_linked` or `self_reported` and `account_id` is non-null (free-mail excluded). Success: that same `account_id`'s earliest Opportunity `created_date` is later than the touch's timestamp. Segment by touch surface (docs, blog, event, community).

Publish it with its coverage rate attached, every time: *"X% of Opportunities this quarter have a resolvable, non-free-mail `account_id` at all; of those, Y% show a devrel touch before creation."* Never publish Y% alone — an account-level rate computed over a partially resolved population, presented without the resolution share, is exactly the number that gets someone burned in the next board deck.

## Build order

Given the decision on the table is literally "did devrel produce pipeline," this promotes the identity spine ahead of the usual cheap-first default:

1. **Free-mail exclusion list** — today, an hour. Fixes the 4,100-person account immediately and stops future ones.
2. **`source` / `source_basis` / `source_confidence` on every touch, replacing the bare lead-source field** — days, mostly a decision plus a schema change, no new instrumentation surfaces.
3. **Identity spine (`anonymous_id` → `user_id` → `account_id`), stitched into the CRM as an Account-level activity object** — a quarter, most of it re-pointing `account_id` resolution at procurement time and backfilling touch history. This is the expensive piece and the one nothing above it can substitute for.
4. **The funnel view itself** — cheap once 1–3 exist, and worthless before they do.

Don't ship the report before step 3 lands. A version built on the current lead-source field will look plausible and be wrong in a way nobody downstream can detect — which is worse than telling sales it isn't ready yet.