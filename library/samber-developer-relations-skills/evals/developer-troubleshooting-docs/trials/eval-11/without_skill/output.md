## Where to start: the 40 Zendesk macros, not the 400 GitHub issues

The instinct to start with GitHub because it's "where the volume is" is the trap. Volume and signal quality are different axes, and for this business they're inversely related.

### Why volume is the wrong first filter

**GitHub issues (400) are the wrong population.** People who file issues against an OSS client library are developers integrating the SDK — often the most technical, most self-sufficient segment of your user base, frequently pre-sale or free-tier, not your $180k enterprise accounts. Their pain is disproportionately: install errors, auth setup, parsing quirks, version mismatches, feature requests, "how do I—" questions. That's real, but it's the *integration* layer, not the *transaction-failure* layer where EDI gateways actually cause customer pain (failed 850s, ack timeouts, partner-specific mapping errors, retry/queue backups). Support-ticket-style sources also skew toward "problem," not "value" or "typical usage" — expect noise: duplicates, user error, already-fixed-in-a-later-version, and issues nobody ever confirmed as resolved.

**The 40 Zendesk macros are pre-filtered gold.** A macro only gets written when a support agent hits the same real-customer problem enough times to justify templating the answer. That's already: (a) validated as a genuine recurring issue, (b) validated as *solved* — the fix is known and correct, (c) drawn from your actual 60-account population, the one whose renewals you care about, not a public crowd of unknown composition. In the extraction framework, this is the difference between single-source, unconfirmed signal and high-confidence signal (recurring, cross-checked by support pattern, already actioned). 40 high-confidence items beat 400 unfiltered ones.

**Telemetry is the highest-value source and the one you can't touch yet.** It's the only one that tells you *frequency* and *cost* objectively rather than by who happened to complain loudest or file a ticket. But it doesn't exist as exported data today — starting there means an infra project, not a content project. Don't block content work on it; run it in parallel.

### Sequence

**Phase 1 (start now, ~1–2 weeks): mine the Zendesk macros.**
- Get the support lead's sign-off first — "internal" may mean "we never bothered," or it may mean "we don't want this public." Ask; don't assume.
- Sanitize each macro before it becomes anything public-facing: strip account names, trading-partner names, config values, ticket IDs — enterprise contracts likely have confidentiality language covering exactly this kind of derived data.
- Turn each into a troubleshooting article: symptom → likely cause → fix → how to confirm it worked. This is nearly free content — the hard part (figuring out the fix) is already done.
- 40 items is small enough to do by hand with care, which matters given the sanitization risk.

**Phase 2 (parallel or right after, ~2–3 weeks): mine GitHub, but only for the gap.**
- Filter to closed-with-confirmed-fix issues only; discard duplicates, stale/unfixed threads, and pure feature requests.
- Use it for what it's actually good for: integration-layer troubleshooting (auth, connection setup, SDK error codes) that the Zendesk macros won't cover, since support-of-paying-accounts skews toward post-integration problems.
- Bonus use: it's real customer *language* — the literal error strings and phrasing people search for. Good for making Phase 1's content findable, even where it doesn't add new topics.
- Cross-check against Phase 1 output first so you're not duplicating a macro that already covers the same failure mode.

**Phase 3 (kick off now, lands later): get telemetry exported — scoped, not full-fidelity.**
- This is an engineering ask, not a content-mining task — start it now so it's ready when Phases 1–2 are done, not after.
- Export error codes/categories + frequency + which integration point, explicitly *not* transaction payloads (EDI payloads are commercial data — PO numbers, invoice amounts, partner identities — and exporting that is a materially different risk than exporting an error taxonomy).
- Once available, use it to re-rank the article backlog from Phases 1–2 by actual frequency, and — more importantly — to surface high-frequency errors nobody ever complained about. Those are often the more dangerous gap: silent failures that erode confidence and quietly drive churn rather than generating a ticket.

### How the three converge

- **Zendesk macros** → what the validated fix is.
- **GitHub issues** → what customers call it and where the integration-layer gaps are.
- **Telemetry** (once exported) → what's actually worth writing next, ranked by real frequency/cost rather than who was loud enough to file a ticket or open an issue.

Don't average across these sources or treat them as one undifferentiated pile — a topic that shows up in all three is high-confidence and goes first; a topic that only shows up in GitHub needs a sanity check against your actual account base before you invest in it.