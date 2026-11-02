Before the heuristics: the plan as stated has one structural risk worth flagging first, because it changes what "threshold" should even mean.

## The risk in the current design

"Score for AI-likelihood, auto-close over threshold, ban repeat submitters" optimizes for the wrong variable. AI-*style* (fluent prose, generic structure) is a weak proxy for AI-*fabrication* (invented function names, mismatched traces). A growing share of legitimate reporters — especially non-native English speakers, which is a large fraction of any Rust crate's global user base — run their reports through an LLM to clean up phrasing before sending. If your gate fires on style, you will eventually auto-close and ban someone who found a real memory-safety bug in a telemetry parser and just wrote it up badly, or too well. That's the failure mode that turns into a CVE-with-no-patch and a bad blog post about Tarnish, not a saved afternoon of triage.

So: score fabrication (falsifiable claims), not authorship (writing style). Route on score; don't auto-close on it. Reserve auto-close for the subset of fabrication signals that are checkable facts, not statistics.

## Heuristics, ranked by how much you should trust them

**Tier 1 — verifiable, cheap, near-zero false-positive rate. These can gate.**

- **Symbol existence.** Extract every `fn`/`struct`/`impl`/`enum`/module path the report cites and grep them against the full git history of the referenced version, not just HEAD (reporters sometimes cite an old tag correctly and a hallucinated name only exists in no commit ever). A cited function that never existed in the repo, in any commit, is close to unambiguous.
- **File:line correctness.** Rust panics and `#[track_caller]` output embed exact `file:line:column`. Check the cited line actually contains the cited construct at the cited commit. Fabricated traces frequently get this right in shape (`src/parser.rs:142:9`) but wrong in content — the line exists, but it's a blank line or an unrelated statement.
- **PoC compiles and reproduces.** If a report includes reproduction code, run it against the cited commit in a sandboxed, network-disabled, timeout-bounded `cargo check` / test harness. If it doesn't compile against the version it claims to target, that's not a style signal, that's a factual falsification. This is your single highest-value check — build it first.
- **Panic/error message format matches your actual output.** Rust's panic strings, `Result` error variants, and `Display` impls have a specific shape. LLMs confidently invent plausible-looking-but-wrong ones (wrong error enum variant name, wrong wording of a message your code doesn't actually emit anywhere).
- **Version/API-shape consistency.** Does the report's described function signature match what that function's signature actually was at the cited version? Crates evolve; a report describing `parse(&self, buf: &[u8])` when that method took `&mut self` at every version in history is a tell.

**Tier 2 — behavioral/meta, needs corroboration, route to a queue rather than gate.**

- **Near-duplicate detection across your own inbox.** Minhash or embedding-cosine on report bodies. Reworded copies of the same fabricated bug from one account, or from many accounts in a short window, is a much stronger signal than any single report's content.
- **Reworded public advisories.** Check whether the "novel" bug is a mad-lib substitution of a already-disclosed CVE from an unrelated crate, with symbol names swapped to yours. This is a very common AI-slop pattern — the underlying "vulnerability class" description is lifted wholesale.
- **Submission velocity per account.** N reports in a short window from one identity, especially if Tier-1 checks fail on more than one of them.
- **Response to one targeted clarifying question.** Ask something a genuine finder can answer from their own testing but that isn't in the report ("what did the parser's cursor position read at the point of panic?", "which crate feature flags did you build with?"). Real reporters answer specifically or say "let me check." Fabricated reports tend to either double down with more invented specifics or go silent. This is cheap (one email), high-signal, and self-labels your training data for free.
- **Severity-language mismatch.** "Critical RCE" language attached to a mechanism that, even taken at face value, doesn't reach that impact (e.g., a described bug that's a panic-on-malformed-input DoS dressed up as RCE). Inflated severity relative to the actual described mechanism correlates with template-driven generation.

**Tier 3 — soft statistical text signals. Use for sort order only. Never gate on these, never cite them in a rejection.**

- Perplexity, burstiness, AI-detector scores (GPTZero-style), boilerplate-phrase matching ("I have identified a critical vulnerability...", fixed Executive Summary/Impact/Steps structure).
- These are trivially defeated by a paraphrasing pass and have a documented, non-trivial false-positive rate against non-native English writers and technical writing in general (technical prose is already low-perplexity and templated even from humans — CVE reports *look like* AI output structurally on their own). Treat a high score here as "check this one's Tier-1/2 signals first," not as evidence in itself.

## Routing instead of a single threshold

Don't collapse this into one weighted score with a magic cutoff. Use tiered actions:

1. **Any Tier-1 check fails (symbol doesn't exist anywhere, PoC doesn't compile against cited commit, trace points at content that isn't there):** auto-tag `unverified`, auto-reply with the one specific falsifiable question that failed, start a 7–14 day clock. Auto-close only on no response — this preserves a paper trail and a recovery path for a genuine report with a sloppy citation.
2. **Tier-1 clean, but Tier-2 signals stack up (near-duplicate, high velocity, reworded public CVE):** low-priority queue, batch human review, no auto-anything.
3. **Tier-1 clean, no Tier-2 flags:** normal queue, same as any report today, regardless of Tier-3 score.
4. **Banning:** never automatic off a score. Reserve for accounts with a track record — e.g., 3+ reports that independently failed Tier-1 *and* went unanswered on the targeted clarifying question — and require a human sign-off before the ban, since it's a one-way door (account/IP bans get evaded anyway; the value is mostly in shrinking the queue, not in punishment).

## Tarnish-specific build notes

- You already have the ground truth for Tier-1 checks in your own repo — this is closer to a linter than an ML problem. A `tree-sitter-rust`-based extractor pulling identifiers out of free-text reports, checked with `rg`/`git grep` across tagged versions, gets you most of the value before you touch anything statistical.
- Sandbox the PoC-compile check hard: no network, resource/time limits, ephemeral container per submission — treat submitted code as hostile input, because some of it will be.
- Log every Tier-1/2 check result per report even when you don't act on it. That log becomes your labeled dataset if you ever want to train something better than heuristics later, and it's your evidence trail if a rejected reporter disputes a close.

## On precedent

This is a documented industry-wide pattern through 2025–2026 — curl's maintainers in particular have written publicly about their HackerOne inbox filling with confident, fabricated, LLM-written reports, and their response leaned on exactly this asymmetry: cheap factual verifiability checks first, human judgment for anything ambiguous, and explicit public refusal to auto-ban on style grounds because of the false-positive cost against genuine (often non-native-English) reporters. Worth reading their write-ups directly for the exact numbers and their escalation policy before you finalize thresholds, since they've been running this longer than a single-project heuristic set can validate against.