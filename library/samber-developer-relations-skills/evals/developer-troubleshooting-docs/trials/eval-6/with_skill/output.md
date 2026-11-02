## Sequencing the Saltbox troubleshooting-docs / SEO ticket

**Short version: split this into two tickets with different owners, and drop two of the four asks — they don't do what marketing thinks they do. Here's the breakdown and the order to run what's left.**

### Kill two asks first, with sources

**FAQPage structured data — drop it.** Google's FAQ rich result stopped appearing in search entirely on 7 May 2026 (Google Search Central removed the documentation in June 2026). Eligibility had already been cut to well-known government and health sites back in 2023. The competitor marketing is copying either shipped this before the cutoff and never pulled it, or shipped it after and is getting nothing from it. Marking Saltbox's 34 entries as `FAQPage` costs engineering time to implement and QA, for zero search real estate. Don't put it in the ticket.

**Rewriting headings as questions — drop this too.** "Why is my function timing out?" and "Why am I getting a 502?" are written for how *marketing* imagines search intent, not for how the reader actually arrives. A developer hitting a Saltbox timeout doesn't type a question — they paste what's in front of them: the exact error string, an exit code, a stack trace line. "Troubleshooting authentication" (and by the same logic, "Why is my function timing out?") never matches a search for the literal string the product emitted. Question-shaped headings written for search rather than for the string the reader is holding are called out directly as a pattern that no longer works.

The fix that actually earns the ranking-and-landing behavior marketing wants: put the **verbatim error string** — the exact text or code Saltbox emits — in the title, the first heading, and the body of each entry. If Saltbox emits `FUNCTION_TIMEOUT` or a 502 with a specific body, that string is the heading. If you want a human-readable restatement for scannability, it goes as a subtitle *under* the verbatim string, never replacing it.

### Why this isn't one ticket

The remaining four items split cleanly across two different skills with two different owners, and folding them into one ticket is what produces a stalled six-week deliverable instead of two shippable ones:

| Track | Covers | Owner | Skill |
|---|---|---|---|
| **A — Content** | The 34 entries themselves: verbatim-string headings, cause/fix rewrite, verification | Docs/technical writing | `developer-troubleshooting-docs` |
| **B — Site mechanics** | Whole-site crawl audit, canonical cleanup, internal-linking redesign | SEO contractor | `docs-seo` |

Track B's own scope explicitly hands error/troubleshooting *content* back to Track A ("Error and troubleshooting page content → developer-troubleshooting-docs"), and Track A hands site-wide technical SEO back to Track B. That two-way handoff is the sequencing answer: they're not phases of one effort, they're two parallel efforts that happen to touch the same 34 URLs. Run them together and every canonical decision blocks on a content rewrite that isn't done yet, and vice versa.

### The order to actually run it

1. **Track A, now, independent of Track B.** The 34 entries don't need the crawl audit to start. Pull evidence first — support tickets, issue tracker, docs search logs, error telemetry if Saltbox has it — and cluster before writing. Ten tickets about the same timeout cause are one entry, not a rewrite pass over ten existing pages. This also catches cases where "34 troubleshooting entries" is actually 20 real failure clusters plus 14 near-duplicates, which changes the whole scope of the ticket.
2. **Gate each cluster before rewriting it**: is this a page-worthy failure, or is it a defect the product should stop emitting? A "why is my function timing out" entry that exists because Saltbox's own timeout error is unhelpfully generic is a signal to escalate to product, not to document more elaborately.
3. **Rewrite to the six-part shape** (verbatim message, applies-to, cause, fix, confirm-it-worked, still-stuck), verify every fix actually runs against current Saltbox, and stamp each page with a last-verified date and owner.
4. **Track B starts in parallel**, not after — the crawl audit, canonical map, and internal-linking redesign apply to the whole docs site, not just these 34 pages, so there's no reason to wait on Track A's content pass. The one coordination point: Track B's canonical/URL decisions for the troubleshooting section should be agreed with whoever owns Track A before either side locks in URLs, since Track A's pages need stable, addressable identifiers (one page or anchor per error) that a later canonical cleanup shouldn't have to re-break.
5. **Track B's contractor scope stays contained to what only they can do**: crawlability, duplicate-URL resolution across versions, canonical/hreflang, generator title/description templates, and internal linking. Don't let "internal linking redesign" quietly expand into rewriting the troubleshooting content itself — that's Track A's job and the two skills' own routing rules say so explicitly.
6. **Wire the pages back to the product** once both tracks have stable URLs: a `doc_url`-style link in Saltbox's own error payloads, or an `explain <code>` path if there's a CLI. This is the step that actually moves ticket volume, and it's independent of both the FAQ-schema and heading-wording ideas marketing pitched.
7. **Set one coverage target before either track reports "done"** — e.g., 80% of the top-ranked clusters live this cycle — and measure per-error ticket volume and zero-result docs-search rate for the covered strings, not a site-wide "SEO score." That's the number that tells you whether Track A worked; Track B's success criteria (indexation, canonical consistency, internal link health) are separate and shouldn't be blended into the same report.

### What to tell marketing

The competitor's setup isn't a template to copy — either it's stale (pre-May-2026 FAQPage markup nobody removed) or it's actively working against their own readers (question headings that don't match what a developer pastes into search). Point them at the entry-per-error-string result instead: that's what makes Saltbox's pages the first hit when someone pastes `FUNCTION_TIMEOUT` or their 502 body into Google, which is the outcome they actually want from "expanded results."