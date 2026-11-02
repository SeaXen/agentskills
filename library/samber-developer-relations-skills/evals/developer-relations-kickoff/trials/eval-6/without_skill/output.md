# Why the CEO stopped believing you — and how to fix it

The problem isn't that your three tools disagree by a little. It's that **one of them is reporting something mathematically impossible**: CRM claims 190 accounts from a single channel (quickstart readers), but the product database says only 96 accounts were created *company-wide, from every channel combined, last month*. A sub-total can't exceed the total. That's not measurement noise — that's a broken pipe, and once a CEO catches one impossible number, he correctly stops trusting all of them, because he has no way to know which ones are quietly wrong in a way that isn't as obvious.

Fix this in two moves: (1) diagnose and stop the impossible number, (2) rebuild reporting so it's structurally impossible for this to happen silently again.

---

## 1. What each number actually measures (they're not competing answers to the same question)

| Source | What it counts | Ground truth? |
|---|---|---|
| Web analytics: 4,100 | Page *views/sessions* on the quickstart URL | No — proxy for interest, not people. Inflated by bots/crawlers, doc-scraping AI agents, repeat visits, and anyone without deduped unique-visitor logic |
| CRM: 190 | CRM's own guess at which contact/lead records it believes originated from quickstart traffic and later got marked "account" | No — this is attribution *logic*, and it's the broken link |
| Product DB: 96 | Rows in the `accounts` table with `created_at` in that month | **Yes.** An account either exists or it doesn't. This is the only number tied to something real |

Your source of truth is the product database. Full stop. Every other number's job is to *explain* the 96, not to compete with it or exceed it.

Given that, 4,100 → 96 isn't even a contradiction — a ~2.3% read-to-signup rate is plausible for a docs quickstart. The real question was always "of those 96, how many actually came from the quickstart," and nobody in your stack can currently answer that, because there's no reliable join between an anonymous doc-page visit and an eventual account row. The CRM's "190" isn't a wrong answer to that question — it's an answer to a *different, badly-defined* question that happens to look similar.

## 2. Why CRM says 190 — ranked by likelihood, with what to check for each

You need to open the CRM and run these checks, in this order, because the fix depends entirely on which one it is:

1. **"Account" in the CRM isn't gated on product signup at all.** Most likely cause. Check whether the CRM's "became an account" transition fires on a *lead/company record being created or a form fill*, not on any signal from the product database. If a marketing form submit, a sales-created record, or a workflow tag flips a contact to "Account" stage, you'll double- and triple-count people who never touched the product. **Check:** pull the 190 CRM records and see how many have *any* linked product user ID at all. If a meaningful chunk have none, this is your answer.
2. **Attribution window ≠ calendar month.** CRM tools often attribute "became an account this month" based on when the *touch* happened (up to a 30/60/90-day lookback), not when the account record itself was created. Someone who read the quickstart in July and signed up in August can get counted as an August "account from quickstart" while the product DB correctly puts them in July. **Check:** compare the `created_at` field on the CRM records to the CRM's own quickstart-touch timestamp — if they routinely diverge by weeks, this is contributing.
3. **No deduplication on the join key.** If the same person visits the quickstart across multiple sessions/devices/UTM-tagged links, and the CRM ingestion doesn't dedupe on a stable identifier (email, user ID), one human can generate several "new account" events. **Check:** dedupe the 190 by email domain + name similarity — if you find clusters, this is it.
4. **A broken automation (Zapier/HubSpot workflow/CRM sync rule) is over-firing.** Ask whoever owns the CRM automations what rule actually sets the "Account" stage, and audit it for a logic bug (e.g., an OR condition that should be an AND, or a trigger that re-fires on every property update instead of once).
5. **Someone is manually creating CRM placeholder accounts for pipeline/sales tracking** that were never meant to represent real product signups, and nobody flagged that these shouldn't be summed into a "quickstart conversion" report.

Don't guess — pull the actual 190 records and eyeball them against #1 first; it's the highest-probability cause and the fastest to confirm (5 minutes of scrolling a CRM view answers it).

## 3. The structural fix — stop CRM from inventing its own number

The reason this keeps happening: **CRM and product DB independently guess at the same fact** (did this person become an account?) instead of one being the source and the other a mirror. Fix the direction of data flow, not just this month's number:

- **Product database becomes the only writer of "became an account."** The moment a real account row is created, fire a webhook/event that updates the CRM record's stage. CRM should never independently decide someone is an "account" — it should only ever reflect what the product DB already knows.
- **Instrument a real identify/merge join**, so a quickstart page visit and the resulting signup are the same tracked identity, not a fuzzy CRM guess: stamp an anonymous ID on the quickstart visitor, carry it through to signup, and call `identify()` at account creation so the analytics tool can merge the pre-signup browsing history onto the real account. Without this, "how many quickstart readers actually signed up" is structurally unanswerable — 190 was never going to be right, because there was no real join underneath it, just an inference.
- **Once that join exists**, the web analytics tool can report a defensible number of the form "of the 96 accounts created, N had a quickstart page view before signup" — a real, verifiable subset of ground truth, not an independent competing total.

## 4. What to tell the CEO, this month and going forward

**This month**, present it exactly as a caught-and-fixed measurement bug, not a rosy number:

> "Last month: 96 accounts created (verified against the product database — this is our one source of truth for account counts). 4,100 people viewed the quickstart page; we cannot yet reliably say how many of the 96 came from there, because the CRM's channel-attribution logic was double-counting/miscounting and reported an impossible 190 — more than the total number of accounts that exist. We've found the root cause [state which of the 5 above], fixed the CRM logic, and are instrumenting a real tracking join so next month's report can show a true quickstart-to-signup number instead of a guess."

That's a more credible update than any clean-looking chart would have been — it shows you caught an impossible number instead of reporting it.

**Going forward**, replace "three tools, three numbers" with one funnel table, sourced correctly at each stage:

| Stage | Metric | Source of truth | Confidence |
|---|---|---|---|
| Interest | Quickstart page views | Web analytics | High (raw traffic, caveat bots/crawlers) |
| Signal | Unique visitors who viewed quickstart | Web analytics, deduped | Medium |
| Conversion | Accounts created | **Product database** | High — non-negotiable |
| Attribution | Of accounts created, how many had a quickstart touch | Product DB joined via identify/merge to analytics | Medium until join is instrumented; High after |

Two rules to enforce permanently: **never let a channel-level number exceed the ground-truth total it's a subset of** (that check alone would have caught this before it reached the CEO), and **CRM reports what the product DB tells it, never the reverse.**