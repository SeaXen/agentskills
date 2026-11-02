8 calls, verdict each:

1. **transactions.md** — File: Reference. Finding: No. One sentence of immutability rationale is normal reference-page framing, not a separate Explanation section.
2. **ADR 0007–0031** — File: Decision record, own bucket (not Reference, not Explanation). Finding: No. Never-edited-after-acceptance is the ADR contract, not a defect. Batch all 25 as same type, skip per-page review.
3. **release-notes/2026-q2.md** — File: Changelog, own bucket. Finding: No.
4. **guides/upgrading-to-v4.md** — File: How-to/Tutorial. Finding: No.
5. **faq.md** — File whole page: FAQ, own bucket. Finding: Yes, 1 finding, scoped to the cert-rotation question only. A 6-step procedure inside an FAQ answer has no dedicated owner, no direct link, easy to miss when the product UI changes. Recommend: extract to a how-to page, leave a one-line answer + link in the FAQ.
6. **troubleshooting/errors.md** — File whole page: Reference (lookup table). Finding: Yes. 12 of 60 rows (20%) carry embedded multi-step fix procedures — a systematic pattern, not a one-off. Recommend: extract each procedure to a linked how-to page, row keeps a pointer only.
7. **docs/index.md** — File: Landing/navigation, own bucket, outside the Reference/How-to/Explanation split. Finding: No.
8. **reference/glossary.md** — File: Reference. Finding: No.

Rule for the remaining pages: flag embedded content only when both hold:
- Real procedure — 3+ ordered steps, not a single line.
- Buried where no one would look to maintain it (table cell, single FAQ answer).

One sentence of rationale inside a reference page is never a finding.

One thing that changes your 190 count: item 6 — do you log that as 1 finding (pattern-level) or 12 (per-error)? Per-instance vs per-pattern convention swings the total a lot across 60 pages of error tables. Which convention are you using?