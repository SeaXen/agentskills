## Where Marlowe Interchange starts on troubleshooting docs

Using the **developer-troubleshooting-docs** skill (KCS capture model, DITA `<troubleshooting>` entry shape, Nielsen heuristic 9 for prose, Google SRE's document-vs-fix gate — named per the skill so this is auditable, not taste).

### The plan as described has the priority backwards

You're an enterprise EDI gateway — 60 contract accounts, ~$180k ACV each — not a self-serve OSS tool. The skill's audience rule for that profile: *"the loudest failures sit in private tickets and never reach the public tracker. Mining only public sources under-serves exactly the accounts that pay."* Ranking 400 GitHub issues as primary while leaving 40 Zendesk macros untouched and telemetry unexported inverts that. GitHub issues on the client library over-represent vocal, technical, often unpaid integrators — not necessarily the 60 accounts writing the checks.

Also: Step 1 requires at least one *reported* source (shows what people complain about) and one *unreported* source (shows what breaks silently). The plan as stated has one reported source only (GitHub) and treats the other reported source (Zendesk) and the only unreported source (telemetry) as out of scope. That's not "where we have volume" — that's the gap where your paying accounts quietly eat a failure, don't file a ticket because their EDI ops team just re-runs the batch, and don't renew.

### Start here, in this order

**1. Pull the 40 Zendesk macros first — they're nearly free.** A team-maintained macro is already a KCS Contributor-level draft: symptom, cause, fix, in the support team's own words, vetted by the people who resolve these all day. Signal-mining's promote-to-article note applies directly: *"an existing support macro makes a cluster nearly free to publish."* Work here is genericizing, not authoring:
- Strip customer/trading-partner identifiers (ISA/GS sender-receiver IDs, partner names, account numbers) — EDI errors carry this kind of PII/business-identifying detail constantly, more than a typical API error would.
- Check the self-serviceability gate: a macro written for an agent with backend access may assume tooling the customer doesn't have. Those become "still stuck" escalation paths, not fix steps.
- Check what may be published at all — ask support which of the 40 touch anything contractually or competitively sensitive before any of this goes public.

This is "internal, leave alone" only if you mean *leave the raw macro text unpublished as-is* — not "ignore as a signal source." It's the highest-value, lowest-effort 40 entries you have.

**2. Get the telemetry exported — this is the actual gap.** Nobody's touched it, which means it's the one source showing failures your accounts never report: quiet retries, silent rejects, a partner's EDI implementation drifting out of spec. For a $180k/account relationship, the failures that never generate a ticket are the ones that show up as churn instead. Concretely:
- Name an engineering owner for the export (counts per error code, per version, per time window) — this is an engineering ask, not a docs task, same framing the skill uses for Step 6's catalog work.
- While you're in there, ask whether the product already has stable error identifiers (EDI gateways usually do — envelope errors, functional-acknowledgment reject codes) coming from one machine-readable source, or several. If several, that's a second, separate engineering proposal (generate the catalog from one source file — Postgres/Rust/Stripe pattern in Step 6), worth raising now rather than hand-syncing 40+ pages later.

**3. Run the clustering script across all three once exported:**
```bash
python3 scripts/error-cluster.py zendesk-macros.csv github-issues.jsonl telemetry.csv --min-count 3 --top 40
```
Merge clusters that are one failure worded three ways across the three sources; split any that share error text but different causes. A cluster whose `first_seen` lands right after a release is a regression to file, not a page to write (Step 3 gate).

**4. Re-weight the ranked queue for your actual business, not raw counts.** The skill's rubric already has the lever: *"A contract-bound audience promotes the rare, expensive failures that self-serve ranking buries."* A cluster with 3 telemetry hits concentrated on one $180k account, or a failure class recurring across your incident reviews, outranks a 40-occurrence GitHub cluster from anonymous OSS users — even though it loses on raw frequency. Where you can, cross-reference clusters against which accounts hit them; that's the resolution-cost and blast-radius factors in the ratio, not just frequency.

**5. Gate document-vs-fix before writing anything.** EDI failures are disproportionately protocol-conformance bugs (yours or a trading partner's), not reader error. Any cluster that recurs across postmortems or dominates contact-driver analysis gets escalated to product with a named owner — writing a page around it just makes the defect permanent and, per Google SRE's framing, the tolerated-defect fact gets said out loud, not buried in a doc.

### Still open — settle these before the writing pass starts (skill's gating interview, questions 1–7)

- Does the gateway emit stable error identifiers, free text, or both — and from how many declared places? (Determines error-reference vs. how-to shape, and whether Step 6's catalog proposal is worth raising now.)
- First-batch deadline, and is this a one-off pass or a standing capture habit? (A near date promotes frequent/reproducible clusters; a standing-habit mandate promotes wiring the Zendesk macro flow into a weekly capture loop instead of a one-time export.)
- Writing/verification hours per cycle, and whose they are — can whoever writes these actually reproduce an EDI transaction failure in a test environment?
- Who reads these pages: the 60 accounts' own integration engineers, third-party EDI consultants they hire, or both? Changes whether "self-serve" framing is even right for an enterprise-only product.
- Any constraint on what's publishable — this is where the trading-partner-identifier question from step 1 gets a real answer, not an assumption.

### What "done" looks like for this first pass

Four artefacts, per the skill's own output contract:
1. Ranked cluster queue (count, first/last seen, source, proposed shape, routing) — stop and get your sign-off here before writing.
2. Entry drafts — six parts each (message, applies to, cause, fix, confirm, still stuck), Zendesk-sourced ones drafted fastest.
3. Verification log — each fix actually re-run against a real EDI test transaction, not written from the macro's memory of the fix.
4. Wiring plan — link from the gateway's own error payload/logs where possible (a `doc_url`-style field is the Stripe pattern), plus the negotiated coverage target (skill's own baseline is 80% of the top 20 clusters per cycle — confirm that number with your team, don't inherit it silently).

Net: don't leave the macros alone and don't leave telemetry unexported. Those two are your highest-signal, lowest-effort starting point precisely because this is a 60-account contract business, not a high-volume self-serve one — GitHub issues are a useful third input, not the lead.