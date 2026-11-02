**There is no industry-standard number for any of these three metrics.** I know of no standards body, RFC, ISO standard or widely adopted framework (CHAOSS, Write the Docs, Diátaxis, Google, Microsoft or Stripe style guides) that sets a required percentage for compiling, test coverage or cross-language parity of documentation code samples. If a slide says "industry standard: X%", the board or an analyst can ask for the source, and none exists. I didn't run a web search for this answer, so check anything below before it goes on a slide.

## What exists

| Metric | Published numeric standard? | What actually exists |
|---|---|---|
| % of samples that compile | No | Some ecosystems enforce 100% by tooling, not by a published benchmark. Rust's `rustdoc` compiles and runs every doc-comment example by default. Go example functions (`ExampleXxx`) compile with the package, and those with an `// Output:` comment are also run. Python `doctest` runs docstring examples. In these ecosystems a non-compiling sample fails the build, so the effective bar is 100%. |
| % covered by tests | No | "Covered" is ambiguous for docs. It can mean the share of samples executed in CI, or the share of API surface that has a sample. No source defines it or sets a target. |
| Cross-language parity | No | No accepted number. Parity is usually tracked per product as "languages × endpoints/features with a sample". SDK-generation vendors and large API companies manage it internally, and I'm not aware of any published target. |

## What you can put on the slide

Call these targets Pellworth Systems chose, not industry benchmarks:

- **Compile or execute rate: 100% of samples built or run in CI on every change.** Rust and Go make this the default, so it's the only number with a defensible reference point. Cite the `rustdoc` documentation and the Go `testing` package documentation (Examples section) for the mechanism, not for a percentage.
- **Test coverage: define it first.** The most defensible definition is "share of published samples executed by CI", and 100% follows from the compile rule. Coverage of API surface by samples is a separate metric. Set it from your own baseline.
- **Parity: define it as a matrix.** Use "(language, feature) pairs with a verified sample ÷ pairs promised", with a target by tier. For example, 100% for the primary languages and a lower figure for the long tail. Choose the numbers yourselves and label them as policy.

## Suggested slide wording

> "No published industry standard exists for docs code-sample quality. We are measured against our own bar: 100% of samples built and run in CI, with parity tracked as a language × feature matrix."

That wording holds up under questioning. A fabricated "industry standard 95%" would not.

## If you still want external references

I can run a proper web search for published practices to cite as precedent, with no invented percentages. Candidates are Google Cloud's sample-testing guidance, Stripe and Twilio docs-testing write-ups, and Rust and Go doc-test documentation. I'd confirm each source is live before it goes on a slide.

I can also draft the measurement definitions so the targets are auditable.