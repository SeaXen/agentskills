## Fix the process: make the guide an RFC artifact, not a release artifact

The reason it keeps happening: the RFC template has no line item for it, so it's structurally invisible until someone remembers at ship time. Fix the template, not the people.

**1. Add a fifth required RFC section: Migration.**
Alongside Motivation, Design, Drawbacks, Alternatives. Required whenever the RFC introduces a breaking change — same enforcement level as the other four, not optional prose.

It must contain, at RFC-approval time (weeks before code lands, not two days before release):
- Inventory of every breaking change the design implies (signature changes, removed APIs, default-behavior changes).
- Before/after snippet for each one.
- An owner — the RFC author, by default, since they hold the context. Not "whoever has time at release."

**2. Gate on it twice, not once.**
- RFC review: reject "Migration: TBD." An RFC that changes public behavior without a migration section is incomplete, same as one missing Drawbacks.
- Release checklist: the migration doc must be merged and reviewed before code freeze, not drafted during it. If the design shifts during implementation (it will), the migration section is a living diff updated alongside the code — not rewritten from scratch at the end.

**3. Ship deprecation warnings the moment behavior changes, not at removal.**
A runtime warning pointing at the migration doc, added in the same PR that introduces the replacement, turns the guide into something battle-tested by real usage over months instead of a document nobody has run against real code until launch week.

This is the actual fix: the RFC process already has teeth (Motivation/Design/Drawbacks/Alternatives don't get skipped). Extending the same gate to Migration is cheaper than adding a new process, and it moves authorship to the person with full design context instead of a release-week volunteer.

## Does the agent-consumption problem change what you write? Yes — materially.

Agents don't read a migration guide the way a human does: skim for the relevant section, infer intent, apply judgment on ambiguous steps. They pattern-match instructions and execute them close to literally. Prose written for a skimming human is frequently *wrong* for an agent, in ways that don't show up until someone points an agent at it.

Concrete changes to the writing:

1. **Diffs over descriptions.** "Update your config to use the new auth format" is lossy — an agent has to guess the exact shape. A labeled before/after code block is unambiguous and copy-pasteable. Every breaking change gets one, no exceptions.

2. **No forward/backward references.** "As mentioned above" or "see the previous section" assumes a reader holding context across the page. Agents often retrieve one section, not the whole doc. Each change should be self-contained: state the precondition (what the code looks like before) and postcondition (what it should look like after) inline, every time.

3. **Branch explicitly, never blend.** If migration differs by configuration ("if you use the callback API... if you use the promise API..."), write two separate self-contained blocks. A narrative that interleaves both is exactly how an agent produces a hybrid that compiles but is broken — it lacks the judgment to know the two paths are mutually exclusive unless the doc says so structurally.

4. **Give a verification step per change, not just an instruction.** A command or test snippet ("run X, expect Y") lets an agent confirm its own edit succeeded. Agents don't have the human instinct of "this looks about right" — they rely on execution feedback. Without it, they either stop or hallucinate confidence.

5. **Replace hedges with defaults.** "Usually you'll want to..." or "update as needed" reads as guidance to a human and as an unresolvable branch to an agent — it either skips the step or fabricates specifics. State the default explicitly; call out the edge case as its own explicit branch (see #3).

6. **Ship a machine-readable manifest alongside the prose, where the change is mechanical.** A JSON/YAML list of `old_symbol → new_symbol`, `breaking: true/false`, is exactly what the SDK-DX playbook's codemod tooling wants anyway. Even without shipping a full codemod, that manifest removes the single biggest source of agent error: mis-locating which of several similarly-named symbols to change.

7. **Keep the migration doc and the API reference in lockstep.** An agent will cross-reference the guide against current reference docs mid-task. If a renamed symbol in the guide doesn't resolve in the reference, the agent silently reverts to old behavior or invents a signature. Land both in the same PR; lint that every symbol the guide names actually exists in the current reference.

8. **Add "an agent completes this unsupervised" as a release gate**, the same way a 5-minute-quickstart is already a human-facing bar. Before cutting the release, run a coding agent against the draft guide on a real pre-upgrade checkout. Failures there are cheap to fix pre-release and expensive to hear about from your biggest integrators post-release — which is the exact failure already reported.

The throughline: an agent-safe migration guide is a stricter version of a good migration guide, not a different document. Precision, explicit branching, and verifiable steps are best practice for humans too — agents just have zero tolerance for the shortcuts (hedging, implicit context, "see above") that human readers silently patch over. Write to that stricter bar once, and both audiences benefit.