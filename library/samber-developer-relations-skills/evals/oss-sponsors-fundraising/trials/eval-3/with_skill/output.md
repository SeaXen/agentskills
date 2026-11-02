## The blocker

$400/month = $4,800/year. GitHub Sponsors' invoiced billing has a **$5,000-per-invoice minimum**. Northvale can't send you $400/month against a PO through GitHub's native invoicing — the platform won't generate an invoice that small. This has nothing to do with your org account or your existing 30 sponsors; it's a floor on the *sponsor's* payment method, set by GitHub.

Two things this does **not** require: raising Northvale's price, or you personally issuing an invoice.

## How it actually works

GitHub Sponsors invoiced billing runs on prepaid credit, not per-month invoices. Northvale's finance team buys a block of credit (minimum $5,000) against **one PO and one numbered invoice issued by GitHub to Northvale**, and their $400/month sponsorship draws down against that balance — roughly 12-13 months of runway before they need to top up. This is actually a better fit for a PO process than monthly billing would be: one document through their AP system per year, not twelve.

You are not a party to that invoice. GitHub is the seller of record; you receive the payout the same way you already receive the 30 individual sponsorships. No entity, no numbered-invoice capability, no new tax form on your side — you already cleared that bar to get paid at all.

## Set this up

1. **Create a separate company tier**, don't fold Northvale into your $5-25 individual ladder. Name it for the buyer — "Production Sponsor" or "Company Supporter," not "Gold" — so their platform lead can point at a line item their own approver recognizes. Price it at $400/month and attach one concrete deliverable an approver can defend: logo in the README/docs footer, or a named commitment (security reports acknowledged within N days). Keep it cheap to deliver — a logo commit, not a support contract.
2. **Tell Northvale's platform lead directly**: subscribe to the tier on GitHub Sponsors, choose "pay by invoice" instead of card at checkout, and be ready for GitHub to ask for a minimum $5,000 initial purchase — that becomes their prepaid balance, drawn down at $400/month. Their AP team gets one PO, one numbered invoice, 30-day terms, from GitHub.
3. **Ask them now for the PO number and any billing-contact details** GitHub's invoice flow will want, so their finance team isn't blocked mid-checkout.
4. Nothing changes on your existing GitHub Sponsors setup — the 30 individual sponsors, their tiers, and your payout settings are untouched. Invoiced billing is a property of the *sponsor's* account, not yours.

## If GitHub's invoicing doesn't work for them

Some finance teams won't route a purchase through a platform they don't already have a vendor relationship with, or the $5,000 upfront credit is itself a problem even though it nets out fine over a year. Two fallbacks, in order of effort:

- **A fiscal host** (Open Collective, hosted by Open Source Collective) can issue a numbered invoice for *any* amount — no $5,000 floor — with a PO reference, bank transfer, the works. Costs ~10% of funds received, and money sits in a project account rather than your personal payout, with a public ledger of expenses. Worth it only if Northvale specifically can't or won't pay GitHub directly.
- **Invoice them yourself**, if you already have or are willing to set up a personal-contractor arrangement or a legal entity. Skips all platform fees, but puts the tax form, the numbered invoice, and the liability on you personally, and the sponsorship won't show up in your public GitHub Sponsors count.

Try GitHub's own invoicing first. It's the only path that costs you zero new admin.

## One thing to lock down before the first payment

Write down, even in one line to Northvale, what the $400/month does *not* buy: no say over the roadmap, no priority on merged PRs — priority *triage*, not priority *outcomes*, if you offer that at all. Cheap to say now, expensive to walk back after their platform lead assumes otherwise.

## Open items — confirm these before you tell Northvale it's settled

- Which country you're paid in, and whether GitHub Sponsors invoiced billing is available for sponsors paying into your region (the receiving side is already proven by your 30 sponsors; the invoiced-billing path is a separate GitHub feature worth a quick check with GitHub Sponsors support if you've never used it).
- Whether GitHub's invoice flow lets Northvale attach their PO number to the invoice itself, or only in payment-reference notes — confirm directly with GitHub support since this isn't published anywhere authoritative; if they can't reference the PO on the invoice, that alone may push you to the fiscal-host fallback.