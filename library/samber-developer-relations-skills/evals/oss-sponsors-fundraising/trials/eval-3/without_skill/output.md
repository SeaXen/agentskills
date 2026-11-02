Web search wasn't authorized, so I'm answering from what's reliably documented about how these platforms work — I'll flag the one detail worth a final click-through check before you act on it.

---

## The core problem

GitHub Sponsors cannot satisfy a PO + numbered-invoice requirement. Org-to-org sponsorship on GitHub Sponsors is billed to a credit card on file, and GitHub issues its own receipt for that charge — you (the maintainer) never generate the invoice, and there's no field for a customer PO number. A procurement/AP team that only pays against a PO and a vendor-issued numbered invoice will not process this through GitHub Sponsors, full stop. So the $400/month needs to move over a different rail than your existing 30 individual sponsors — don't try to force Northvale into the same GitHub Sponsors tier as your $5–25 individuals.

Keep the two things separate: **who pays you and how** (needs to change) vs. **who gets public sponsor credit on your README/site** (can stay exactly as it is — you can list Northvale there regardless of which rail the money comes through).

## Two ways to actually collect the money

**Option A — Invoice them directly, yourself.** This is the leaner option if you (or a community non-profit, or any existing consulting entity of yours) already has a registered business identity you invoice clients through.
- Reuse that entity. Issue Northvale a sequential invoice (invoice number, your entity's legal name/address/SIRET + VAT status, description like "Open source sponsorship — [library name]", amount, payment terms, IBAN/BIC for SEPA or wire) with their PO number referenced once they send it.
- If you don't have a billing entity yet, register as auto-entrepreneur (micro-enterprise) — a few days via the guichet unique, no capital needed — before invoicing. Without a SIRET you can't legally issue a compliant French invoice to a company's AP system.
- Use a tool that gives you real sequential invoice numbers and a PO-reference field: Stripe Invoicing, or Indy (common with French micro-entrepreneurs), rather than a hand-edited PDF.
- If you're under the French VAT franchise threshold, put the standard mention on the invoice: *"TVA non applicable, art. 293 B du CGI"*.
- Collect by SEPA transfer/wire to your business account, not by card — most PO-based AP workflows don't pay recurring vendor spend by card anyway.

**Option B — Route it through a fiscal host (e.g. Open Collective / Open Source Collective).** Worth it if you expect more corporate sponsors down the line (you clearly plan to keep growing this), since the PO/invoice friction will repeat with the next one. The host holds the legal/invoicing relationship with Northvale, issues them a proper invoice against their PO, handles VAT, and disburses the money to you as an expense claim. Trade-off: a host fee (commonly around 5–10%) and a bit more setup now, but zero entity paperwork on your side and it's reusable for every future corporate sponsor. Confirm the specific host's current PO/NET-30 support before committing — verify this against their site, since I couldn't cross-check it live this session.

## Recommended sequence

1. **Reply to the platform lead now, not to finance directly.** Ask them for: their PO number once issued, their standard payment terms (NET 30/45 is typical), their AP contact/portal, and whether they can commit annually.
2. **Push for annual prepay ($4,800) instead of monthly.** One PO, one invoice, no chasing 12 late payments — very often an easier ask for their procurement than it sounds, and much less admin for you either way (A or B).
3. **Pick A or B based on one fact only: do you already have a billing entity you invoice through today?** Yes → Option A, fast. No, and you expect this to recur → Option B. No, and this is a one-off → still Option A, register the auto-entrepreneur status first (it's cheap and you'll want it for the next one anyway).
4. **Send the invoice** with their PO number referenced, sequential invoice number, your entity's legal + tax details, and your bank details for SEPA/wire.
5. **Once paid, add them to your sponsors listing** (README/SPONSORS.md, site) — this is independent of which rail carried the payment.
6. **Send a one-paragraph confirmation email** stating amount, cadence, and what they get (logo/name placement) — keeps it unambiguously a sponsorship, not an implied support contract, unless you actually want to offer SLA-backed support at that price.