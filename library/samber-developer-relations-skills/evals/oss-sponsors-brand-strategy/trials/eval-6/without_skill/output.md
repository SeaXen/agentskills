## Sanity check: the 94% coverage claim is not safe to publish

**Bottom line:** don't put 94% in the annual report. Two independent problems in Marisol's methodology mean the number is likely inflated, and the `slugsafe` data point is measuring the wrong thing even if the specific figures are accurate.

### Problem 1 — "6 maintainers" comes from the wrong graph

GitHub's contributors graph and npm's maintainer list are different, unrelated signals:

- **GitHub contributors** = every account that ever landed a commit on the repo — one-time PR authors, bots (`dependabot[bot]`, `renovate[bot]`), ex-employees, people who fixed a typo once. It says nothing about who can push a new version to npm.
- **npm maintainers** = the accounts with publish rights on the registry, listed in the package's `maintainers` field. This is the number that actually matters for a funding/supply-chain report, because it answers "how many people could ship a malicious or compromised release," not "how many people have ever touched the code."

These two counts routinely diverge by an order of magnitude in either direction: a package can show 40+ GitHub contributors and 1 npm publisher (classic single-maintainer bus-factor risk that the GitHub number *hides*), or it can be part of a monorepo where the contributors graph reflects dozens of unrelated packages, inflating the apparent maintainer count for `slugsafe` specifically. Either way, "6 maintainers" pulled from GitHub is not evidence about npm publish risk — it needs to come from `npm view slugsafe maintainers` or the registry's own `maintainers` array.

"Eyeballed weekly downloads" has the same issue in miniature: a glance at a chart is not a reportable figure. The real number is a single API call away.

**I could not pull the live number myself** — this sandbox has no outbound network access this session (WebFetch, WebSearch, and `curl` via Bash were all blocked pending an approval that never resolved), so I won't guess at `slugsafe`'s actual maintainer count or download volume. Run these yourself (each takes seconds):

```
npm view slugsafe maintainers
npm view slugsafe repository.url
curl -s https://api.npmjs.org/downloads/point/last-month/slugsafe
```
Then cross-check `maintainers` against the GitHub repo's actual contributors tab — if they don't roughly match, that confirms the two-graph problem above.

### Problem 2 — "not found" was coded as "fine," which is what's really driving the 94%

This is the bigger issue, and it's independent of whether any single package's numbers are right. If Marisol couldn't find data for a dependency, marking it "fine" silently merges two different populations into one bucket:

- packages actually checked and found to be fine
- packages **not checked at all**, defaulted to fine by absence of a finding

Whatever produced "94%," you don't currently know how much of that is real verification versus default-pass. If, say, 60 of the 310 deps were "couldn't find, marked fine," the true verified-coverage rate could be closer to 70–75%, not 94% — and you'd be publishing a number that's really measuring "how much we didn't check" dressed up as "how much we confirmed is safe." For an external funding/annual report, that's a credibility risk if anyone (an auditor, a funder's diligence team) re-derives it and gets a different answer.

### What to do before publishing

1. Ask Marisol for the raw split: how many of the 310 were actually found/verified vs. defaulted to "fine" because she couldn't locate data. That single number tells you whether 94% is defensible or needs restating.
2. Re-pull maintainer counts from npm's registry (`maintainers` field), not GitHub contributors — this is a mechanical fix, scriptable across all 310 packages with `npm view <pkg> maintainers` or a loop against `registry.npmjs.org/<pkg>`.
3. Replace "eyeballed downloads" with the actual `api.npmjs.org/downloads/point/last-month/<pkg>` value for each package.
4. Redefine "coverage" explicitly (e.g., "% of dependencies with a verified npm-registry maintainer count and download figure") and recompute — publish that number, with the definition stated in the report, rather than an unlabeled 94%.
5. Anything still unresolved after the re-check should be reported as "unknown / needs follow-up," not folded into the coverage percentage.

If you want, I can write the small script to batch-pull `maintainers` + last-month downloads for all 310 packages from the npm registry once network access is available in this environment — that removes both the eyeballing and the GitHub/npm conflation in one pass.