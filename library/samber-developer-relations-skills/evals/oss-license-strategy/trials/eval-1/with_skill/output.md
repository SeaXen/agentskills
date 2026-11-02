# Licensing decision — `trailcut` (Mirefold Systems)

## Bottom line

⚠️ **No — not as currently built.** The C shim's link against `libtapedrive` (GPL-2.0-only) forces the *distributed `trailcut` binary* to ship under GPL-2.0, not Apache-2.0. This isn't a preference call — it's a legal gate from a shipped dependency, and gates get deleted, not ranked. Apache-2.0 stays available for everything else in your portfolio; it just can't be the label on this particular artifact while it links that library.

There's a second, sharper problem underneath the first one: the FSF has never treated Apache-2.0 as GPLv2-compatible at all (its patent-termination and indemnification clauses), independent of what license your own code carries. If any of the 63 crates are Apache-2.0 rather than MIT and end up statically linked into the same binary as `libtapedrive`, that combination is contested on the FSF's own reading — not just the top-level label, the underlying mix.

## Constraints (Step 1)

| Item | License | Trigger / obligation | Status |
|---|---|---|---|
| `libtapedrive` (linked via C shim) | GPL-2.0-only | Distribution of a derivative work → whole derivative work under GPL-2.0 | **Eliminates pure Apache-2.0 for the shipped binary** |
| 63 Rust crates | "Mostly" Apache-2.0/MIT | Permissive → compatible into anything | Needs 100% enumeration, not "mostly" — see below |
| Vendored CRC routine | BSD-3-Clause | Permissive, but copyright/license notice must be preserved verbatim | Compatible, but not silently absorbable under a blanket LICENSE |
| ~200 lines of AI-assisted retry logic | Unclear provenance | N/A yet — provenance unresolved | Needs a review pass before the license record can call the repo clean |
| Authorship | Presumably Mirefold employees, company time | Employer typically owns it | Confirm with your own legal team — I can't read your employment contracts, and won't guess |

I have not run a scanner against your actual `Cargo.lock`/`go.mod`-equivalent or read `libtapedrive`'s actual `COPYING` file — this is built from what you told me. Before you commit anything, run `cargo license` (or `cargo deny check licenses`) against the real lockfile, and open `libtapedrive`'s own license file to confirm "GPL-2.0-only" rather than "GPL-2.0-or-later" (the "or-later" version matters — see below).

**Why linking matters, not just distributing:** GPL-2.0's copyleft triggers on distributing a derivative work, and the FSF's own position (stated in its license list and the GPL-compatibility guidance) is that linking — static or dynamic — against a GPL-2.0 library creates a combined work, unlike LGPL where dynamic linking is explicitly carved out. `libtapedrive` is GPL-2.0-only, not LGPL, so that carve-out doesn't apply here.

**Why "-only" (not "-or-later") matters:** if `libtapedrive` were "GPL-2.0-or-later," you'd have a path through GPL-3.0 (which Apache-2.0 flows into cleanly — that direction works). "-only" removes that escape hatch. Confirm this from the library's actual license header; don't take my characterization of your own summary as the final word.

**One practical Rust-ecosystem note that doesn't solve the problem but narrows it:** most Rust crates dual-license "MIT OR Apache-2.0," letting a downstream integrator elect MIT for any given crate. If you elect MIT everywhere it's offered, you remove the crate-level Apache/GPLv2 tension entirely — but this does nothing about `libtapedrive` itself, which is the actual blocker.

## What this eliminates, in writing

- **Apache-2.0 for the shipped `trailcut` binary** — eliminated by the GPL-2.0-only link, not merely disfavored.
- **Calling the whole repository "Apache-2.0" while `libtapedrive` stays linked in** — eliminated for the same reason; this would also fail any automated license detector the moment someone runs a real SPDX scan, in public, after release.

## Paths forward — pick one, this isn't a ranking

**A. Ship under GPL-2.0-only. (Recommended default if you want to ship now.)**
Fully compliant today, zero engineering work, no third-party negotiation. Costs you the company-standard label for this one repo — document it as a named exception, not a silent deviation, so nobody re-litigates it next quarter. Your own original source files (the CLI logic, the shim, the retry code) remain your copyright and you're free to reuse *those specific files* elsewhere under Apache-2.0 in a context that doesn't link `libtapedrive` — but the published `trailcut` release, as a whole, ships and must be redistributable under GPL-2.0.

**B. Decouple `libtapedrive` and keep the CLI Apache-2.0.**
Either replace it with a non-copyleft alternative, reimplement the needed subset, or move the integration to a genuinely arm's-length subprocess/IPC boundary instead of an in-process link. The FSF's own carve-out for "mere aggregation" and loosely-coupled processes is the theoretical basis for the last option, but it's fact-specific and contested at the margins — I won't tell you where your shim's actual coupling lands on that line without reading the code, and if the answer matters commercially, get counsel to look at the actual call surface, not a description of it.
This is the only path that gets you Apache-2.0 *and* keeps `libtapedrive`'s functionality, but it's real engineering work, not a licensing decision.

**C. Get a relicense or commercial exception from `libtapedrive`'s copyright holder.**
Worth one email if you don't already know the answer is no. Often impractical for a widely-used third-party library, but costs nothing to ask.

I'd default to **A** if you need to ship soon, and treat **B** as the follow-up work item if Apache-2.0 on this repo is worth the engineering cost to your team — that's a product/roadmap call, not a licensing one, and it's yours to make.

## Contribution policy

No business model or relicensing plan was mentioned, so start at the DCO — Karl Fogel's "probably the minimum amount of CLA a free software project should adopt," near-zero friction, automated check on every PR. No CLA needed unless you later want to dual-license the GPL-2.0 component commercially (MySQL-style) — if that's plausible, introduce the CLA on the GPL-2.0 portion from day one, because collecting it retroactively needs every contributor's consent.

## Artifacts to ship (Path A)

1. **`LICENSE`** at repo root — the unmodified GPL-2.0-only text. **Don't hand-transcribe a document this length from a written description of it** — the skill's own rule is that a modified license file defeats automatic detection, and copying a legal text from memory risks exactly that. Pull it verbatim: `curl -o LICENSE https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt`, or use GitHub's "Add file → Choose a license template" flow, which inserts the canonical text directly.
2. **`NOTICE` / `THIRD-PARTY-LICENSES.md`** — list `libtapedrive` (name, copyright holder, GPL-2.0-only, linked) and the vendored CRC routine with its full BSD-3-Clause notice preserved verbatim, plus its original author and source location. Generate the Rust-crate portion with `cargo about generate` or `cargo license` once the 63-crate audit is complete — permissive code flowing into a GPL binary doesn't erase the upstream attribution duty.
3. **`SPDX-License-Identifier: GPL-2.0-only`** headers on files Mirefold authored; leave the vendored CRC file's own original SPDX header (`BSD-3-Clause`) untouched.
4. **`Cargo.toml`** — `license = "GPL-2.0-only"` on the binary/workspace crate. Dependency crates keep their own license fields as-is.
5. **CI check** — `cargo deny check licenses` (or `reuse lint`) wired into the pipeline, so the dependency graph stays enumerated on every change instead of trusting memory.
6. **Open item, not yet resolved:** have someone review the ~200 lines of AI-assisted retry logic for near-verbatim resemblance to a known codebase before merging it into the now-public repo. I can't clear this from a description — it needs eyes on the actual diff.
7. **Open item:** finish the 63-crate audit to 100% coverage (currently "mostly"); this doesn't block Path A (permissive-into-GPL always works) but it's required before you can honestly report the pass threshold below as green.
8. **Trademark, separate from the code license:** if `trailcut` the name matters to you, that's a different asset with its own clearance timeline — the license governs the code, not who's allowed to call a fork "trailcut."

## Revisit triggers

Reopen this decision if: `libtapedrive` gets replaced or made optional (unlocks Path B), the AI-code review turns up a real provenance problem, the full crate audit finds a copyleft dependency "mostly" missed, or the company decides Apache-2.0-on-this-repo is worth funding the decoupling work.

## Where this stands against the pass bar

- Dependency licenses enumerated at 100%: **not yet** — "mostly" needs to become a real number before this is closed.
- Outbound license recognized and correctly labelled: **yes**, once you land on GPL-2.0-only (OSI-approved, not source-available, no mislabeling risk).
- LICENSE file detector-verified: **pending** — depends on pulling the canonical text rather than transcribing it.
- Contribution policy has an automated check: **pending implementation**, DCO recommended.
- Every claim traceable: yes — FSF's GPL-compatibility position, GPL-2.0 §2's whole-work requirement, and the Rust dual-license convention are all named, not asserted from nowhere.
- Every eliminated option carries a written reason: yes, above.

None of this is legal advice, and the two places it matters most here — whether your shim's actual coupling could support the subprocess/IPC argument in Path B, and whether the AI-generated code carries any encumbrance — are exactly the two questions worth a real lawyer's time before you publish.