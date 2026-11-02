## Where the file goes

GitHub org pages aren't configured in repo settings — they're rendered from a special repository:

1. Create a new repo **under the Thornpike Data org**, named exactly **`.github`** (not `thornpike-data/.github` as a fork, an actual new repo literally named `.github`). Must be public.
2. Inside it, add **`profile/README.md`**. That specific path is what GitHub looks for.
3. Once that file exists, GitHub swaps the org's "just a repo list" page for this README, above the repo grid. No custom CSS — same Markdown + limited inline HTML you'd use in any repo README (centered `<div>`, `<img>`, badges).
4. This is org-wide and singular — one profile README, separate from each individual repo's own README.

Any engineer with write access to that new repo can ship this without touching the product repos.

## Before porting the homepage copy: the audience is different

Homepage visitors are mostly in a buying cycle — they need to be convinced. Org-page visitors are usually one of three things: a developer evaluating whether to depend on one of your three OSS runtime pieces, someone doing a security/provenance check on a dependency ("who's behind this repo"), or a candidate scoping the company before applying. None of them are mid-funnel. Copy written to move a buyer forward reads as misplaced sales pitch next to a repo grid.

Going through the four requested elements individually:

- **Hero line** — the homepage version is almost certainly pitching business value (throughput, cost, ROI). Rewrite it, don't port it: one sentence stating what Thornpike Data builds and how the three public repos relate to the commercial platform. Technical framing, not a pitch.
- **Three customer logos** — this is social proof for a procurement decision; a developer deciding whether to `go get` a library doesn't need it, and it can read as "we're a vendor, not a project." If it's kept at all, flip the framing from "trusted by our customers" to "these components run in production at ___" — and check with whoever cleared logo usage for the homepage, since that sign-off (which customers agreed to be named, in what context) doesn't automatically extend to a new placement.
- **Product tour** — this is almost always screenshots/GIFs of the full commercial UI, and there's no signup flow to send that traffic into from here. It doesn't have a job to do on this page. Swap it for the thing GitHub visitors actually want: a table of the three OSS repos with a one-line description and status badges each — that *is* the tour, for this audience.
- **Careers CTA** — the one piece that's a genuine fit. Engineers who browse a company's GitHub org are a warm hiring signal. Keep it, but low-key, near the bottom rather than as a headline element.

## The actual file

```markdown
<div align="center">
  <img src="https://raw.githubusercontent.com/thornpike-data/.github/main/profile/logo.svg" alt="Thornpike Data" width="160">

  <h1>Thornpike Data</h1>
  <p><strong>[One sentence: what the commercial stream-processing platform does, written for an engineer, not a buyer]</strong></p>
</div>

---

## Open source

We build a commercial stream-processing platform, and open-source the runtime pieces underneath it. No CLA gate, no bait-and-switch — these are used in production, by us and by others, independent of the commercial product.

| Repo | What it does | |
|---|---|---|
| [`repo-one`](https://github.com/thornpike-data/repo-one) | [one-line description] | ![CI](https://github.com/thornpike-data/repo-one/workflows/CI/badge.svg) ![stars](https://img.shields.io/github/stars/thornpike-data/repo-one?style=social) |
| [`repo-two`](https://github.com/thornpike-data/repo-two) | [one-line description] | ![CI](https://github.com/thornpike-data/repo-two/workflows/CI/badge.svg) ![stars](https://img.shields.io/github/stars/thornpike-data/repo-two?style=social) |
| [`repo-three`](https://github.com/thornpike-data/repo-three) | [one-line description] | ![CI](https://github.com/thornpike-data/repo-three/workflows/CI/badge.svg) ![stars](https://img.shields.io/github/stars/thornpike-data/repo-three?style=social) |

<!-- Optional, only if logo usage is separately cleared for this placement: -->
<!--
## In production at

[logo] [logo] [logo]
-->

Full platform docs (commercial + OSS pieces): [docs.thornpike.io](https://docs.thornpike.io)

## We're hiring

34 people, engineering-led. If you read this repo and thought "I'd fix that differently" — [see open roles](https://thornpike.io/careers).

</div>
```

## Two things to flag back to marketing

- The customer-logo question isn't a copy decision, it's a permissions one — confirm before reusing homepage logos here, don't assume the original sign-off covers this placement.
- Nothing above needs a designer or a deploy: it's a markdown file in a new repo. Whoever has org admin can ship this in under an hour once the three one-liners and repo links are filled in.