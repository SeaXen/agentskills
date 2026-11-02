# Fixing the afterthought problem, and what coding agents change about the guide

## 1. Gate the guide behind the RFC you already have

Don't build new process. The skill's own governance section is explicit on this: *"If the project has an RFC, KEP or design-doc process, propose the section rather than the guide — it converts every future break into a guide automatically."* You have the process (Motivation / Design / Drawbacks / Alternatives). Add a fifth, required section.

**Add "Migration" as a required RFC section**, filled before the RFC can move to Accepted:

- **Breaking surface** — every symbol this change removes, renames, or changes the behavior/default of. Not exhaustive at RFC time is fine; the RFC author commits to what's known.
- **Path shape** — staged (N-1 gets a warnings-only release first), single hop, or compat build, with the one-line reason. This is a design decision, not a docs decision, and it belongs with the design.
- **Audience** — open-source self-serve, contractual/dated, or internal-mandated. Determines tone and whether a deadline has to exist.
- **Automation plan** — which rung you're shipping (search patterns + literal error text, at minimum; codemod or compat build if the blast radius justifies the engineering cost) and who owns it after release.
- **Telemetry** — do you have usage data on the affected API? If no, say so; that absence is itself a fact the guide has to work around later.

This is Ember's "How we teach this" and Rust RFC 1636's copy of it, and it works for the same reason it works there: it forces path shape, audience, and blast radius to be decided *while the change is still a proposal*, when reversing course costs a comment, not a rewritten guide two days before ship.

**Ownership follows the RFC, not the release**: the engineer proposing the break drafts the Migration section's technical content (what breaks, before/after) at RFC time; DevRel/writer reviews it for clarity the same review pass the Design section gets, and owns turning it into the published entry once the change lands. Nobody is left assuming the other person is drafting, because the section exists before either of them would otherwise start.

**Enforce it, don't just write it down.** Rust's own retrospective on RFC 1636 admits the changelog half of the gate "has not ever been done" — a required section with no enforcement decays into an optional one within two cycles. Two concrete levers, pick whichever fits your tooling:

- Block RFC merge to Accepted if the Migration section is empty for an RFC labeled breaking-change.
- Block the release cut (or the PR that lands the break, if you ship docs-as-code) if a breaking change has no linked migration entry — this is the Kubernetes KEP move: an incomplete KEP is dropped at the enhancements freeze, not shipped with an IOU.

The second lever is the stronger one for your specific symptom. If the migration note has to ship in the same PR as the break — docs-as-code, not a follow-up ticket — the person who broke the API is the first drafter by construction, and "whoever happened to have time" stops being how this gets written, because it's a merge blocker, not a post-hoc chore.

**One thing this doesn't fix by itself**: blast-radius ranking still needs real evidence (telemetry, then dependent-repo search, then maintainer estimate) at the point you *write* the guide, not just at RFC time — usage patterns shift between proposal and release. Keep asking the telemetry question at both points.

## 2. Does the agent thing change what you write — yes, but not into a second document

The same page serves both readers. What changes is which of the skill's existing requirements move from "good practice" to "non-negotiable," plus one new verification step.

**What was already recommended, now load-bearing:**

- **Exact error/warning text, quoted, not paraphrased.** An agent (and a human search box) matches on the literal string. "You'll see a deprecation warning" is not an affected-if line; the DEP0XXX-style exact text is.
- **Complete, runnable before/after snippets with imports.** A fragment the reader "places correctly" is exactly where an agent invents surrounding code that doesn't exist.
- **The detection signal, per entry** — search pattern plus literal text. This is the automation reference's first rung, ranked top on efficiency precisely because it's free (it's the affected-if line you already have to write) and because *"that pair is also exactly what a coding agent needs to do the work unattended, which is why it outranks tooling that only a human can drive."* If you ship nothing else automated, ship this rung — it's the one thing standing between "agent greps for the old pattern and fixes it" and "agent guesses."
- **Self-containment.** "See the blog post for the steps" stops a human for thirty seconds; it strands an agent restricted to the published surface entirely. Everything needed to act has to live on the guide page.
- **Machine-checkable floors** (`Node >= 20.19`, not "a recent Node version") and **stable per-change anchors on one canonical URL**. An agent that can't parse the floor as a comparison will attempt the upgrade on an unsupported runtime and report back a confusing failure; a guide that moves each release breaks whatever the agent (or a support macro) has cached.
- **Explicit escape hatch, every entry, even "there is none."** An agent that can't find a compat flag either invents one or stalls; stating the negative closes that off.

**What's new: run a cold upgrade with an agent, not only a human, before your integrators do it for you.** The skill's pass threshold already requires a cold upgrade — a real project, someone who didn't write the guide, at the keyboard. Your integrators are already running that test in production, uncontrolled, and it's failing. Run it yourself first: point a coding agent at the published guide only (no source, no issue tracker), have it attempt the upgrade on a real consumer project, and log what breaks. Borrow the sibling skill's instrumentation for this rather than inventing your own:

- Zero invented API calls on the changes your blast-radius ranking put first.
- No more than a small, fixed number of documents fetched per breaking change (if the agent is following links out to the changelog or source, self-containment failed).
- Corrective turns per entry — an entry the agent gets right in one pass is validated; one that takes three tries has an ambiguity a human reader is also silently absorbing without telling you.

Where this run fails, the fix is the same fix as always — better detection signal, a completed before/after block, a stated escape hatch — so this doesn't add new work to the entry template. It adds a second, earlier moment where "goes badly" surfaces as a failed test run instead of a support ticket from your biggest integrator's coding agent.

**What doesn't change:** blast-radius ordering, the six-part entry shape, the audience split. An agent triages the same way a rushed human does — top to bottom, stop when the entry doesn't apply — so the ordering that serves your open-source reader serves the agent too. You're not writing an agent edition; you're holding the existing spec to the letter, because for this reader the letter is the whole interface.