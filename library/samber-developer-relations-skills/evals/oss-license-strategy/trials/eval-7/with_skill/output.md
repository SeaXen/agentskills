# Ridgeblack licensing audit — short answer: **not fine, and one issue is serious enough to fix before diligence starts.**

Refusing legal advice on enforceability throughout — routing that to counsel where it matters. This is a Step 7 artifact audit (`oss-license-strategy` skill), run against the six-item pass threshold and the mixed-repo checklist.

## ❌ Critical: the LICENSE file is not MIT anymore

You're calling it MIT while it isn't one. That gap is exactly what a diligence lawyer's license scanner exists to catch, and exactly what the skill's own artifact rule warns about:

> "A root LICENSE file with unmodified text is what automated detection reads; modified or bundled text defeats it." — GitHub's licensing documentation

Three concrete consequences, not abstractions:

- **Detection breaks or lies.** GitHub's `licensee`, FOSSA, and every SPDX-based scanner an investor's counsel will run either fail to classify the file or fuzzy-match it as "MIT" anyway, hiding the training restriction from anyone trusting the badge. Either outcome is worse than a clean answer.
- **This is the "fauxpen source" pattern, aimed at your own repo.** The OSI board's objection to SSPL applies word-for-word: adopters "claim that their product continues to remain 'open' … but the new license actually has taken away user rights." A field-of-endeavor restriction (no training) tacked onto MIT text is structurally the same move, just undocumented as such.
- **It's a bespoke license now, and that's a cost you're handing to every evaluator** — including the Series A counsel reviewing this repo. The skill's own rule: "Never draft, modify, or invent a license — a bespoke license forces every evaluator's legal team into an unbudgeted review." That review is about to happen to *you*, at the worst possible time.

One more thing that needs a direct answer before I can size the damage: **when was the ML-training paragraph added — at first publication, or appended to an already-public MIT repo?** If it was added later, every prior tagged release is still forkable under plain, unrestricted MIT — the paragraph protects nothing retroactively, and diligence will ask this exact question.

## ❌ Scope creep: one LICENSE, four different artifacts

A single root LICENSE silently claims everything under it — this is a named failure mode, not a hypothetical:

| Path | What it is | Problem |
|---|---|---|
| `docs/` (90-page handbook) | Prose, not code | Docs want a content license (typically CC-BY-4.0), not a code license. Right now the handbook inherits a modified MIT text it was never designed for. If the training-restriction was actually aimed at the handbook, it's on the wrong instrument — no CC license currently has an AI-training clause, so this needs either a bespoke content term (counsel) or a non-license control (crawler blocking, site ToS), not the code LICENSE. |
| `examples/` (8 sample apps) | Copy-paste reference code | Example code exists to be maximally adoptable. A training restriction here works against your own goal and was almost certainly inherited by accident, not intent. |
| `packages/ridgeblack-sdk/` | npm package | Same accident, higher stakes — see below. |
| `server/` | Container image | Unclear if this is meant to be open at all. If it's your commercial core, it probably shouldn't share a LICENSE with the SDK in the first place. |

Ask yourself which of these four you actually meant to restrict. My guess: none of them, and the paragraph was written with the whole repo in mind without checking what "the whole repo" contains. That's the scope-creep failure mode by name.

## ❌ The mislabeling propagates into metadata

- `packages/ridgeblack-sdk/package.json`'s `license` field almost certainly says `"MIT"` or `"SEE LICENSE IN LICENSE"`. If it says `"MIT"`, that's a false claim in machine-readable metadata that every consumer's dependency scanner reads and trusts — this is the same problem as the LICENSE file, duplicated. If it says `"SEE LICENSE IN LICENSE"`, it's honest but non-SPDX, which fails procurement allowlists outright: "OSI approval is the marker most procurement allowlists filter on… expect a bespoke legal review at every adopting company." That's a tax on every developer trying to get your SDK approved at a company with a legal review gate — the exact PLG funnel you presumably want the SDK to drive.
- `server/`'s container image labels (`org.opencontainers.image.licenses`) need the same honesty check — whatever they currently say, verify it matches what's actually enforceable for that artifact once you draw the boundary above.

## ✅ What's actually fine

- **Copyright line** — `Copyright (c) 2024 Ridgeblack Inc. and contributors` is a normal, acceptable form (companies from Meta to countless startups use "Company, Inc. and contributors"). No fix needed. The stricter form from the Linux Foundation's guidance ("Copyright The Ridgeblack Authors") is a nicety, not a gap.
- **Year staying "2024"** — correct behavior. LICENSE copyright years mark first publication; they're not meant to be bumped annually like a website footer.

## Two ways to actually fix the critical issue

1. **Drop the paragraph, ship real unmodified MIT.** If the AI-training concern is really about the handbook, solve it there specifically — crawler controls, a site ToS, or a content-specific term reviewed by counsel — not by contaminating the code license every downstream adopter and every diligence scanner reads.
2. **Keep the restriction, but stop calling it MIT anywhere.** Rename it, apply it *only* to the directory it's meant for (not `examples/`, almost certainly not the SDK), give it a `LICENSING.md` explaining the per-directory boundary the way a mixed repo requires, and label it plainly as source-available — never open source — in the README, `package.json`, and anywhere else the term currently appears. Expect this path to cost you SDK adoption friction and an OSI-approval line item flagged in diligence regardless; that's the honest trade, not a bug in the fix.

Either way, the fix is not "reword the paragraph" — it's "decide what you're actually trying to protect, and use an instrument that says so honestly."

## Before I'd call this closed, I still need:

1. Dependency audit — has anyone enumerated what `packages/ridgeblack-sdk/` and `server/` actually ship, including transitive deps? A single copyleft dependency changes what's even available as an outbound license, independent of the MIT question.
2. Who wrote the code — employees on company time, contractors, or a mix? Standard question, routes to your counsel, matters for whether Ridgeblack Inc. actually owns what it's licensing.
3. Confirmation on timing — was the ML-training paragraph present at first publication or appended later? This determines whether older tags are already an unrestricted fork vector.
4. Is `server/` meant to be open at all, or is this monorepo mixing an OSS SDK with a proprietary backend that happens to share a LICENSE file by default?

Answer those four and I'll turn this into a full decision record (artifact-by-artifact) rather than an audit of what's currently broken.