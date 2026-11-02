Here's what's wrong with the page, ranked by how directly each one drives tickets:

**1. Java 21 requirement sits last — move it to the top, before anything else.**
It's a hard blocker. Readers who lack Java 21 currently read the whole page, attempt the upgrade, then fail — and file a ticket instead of stopping at step zero. Put a "Before you upgrade" callout above "What's new" stating the Java 21 requirement.

**2. The npm install command and config-file rename live in FAQ — move them to a dedicated "Migration steps" section.**
FAQ implies optional/supplementary reading; these are mandatory steps. Readers skim past FAQ expecting Q&A, never find the actual command, and open a ticket asking "how do I even install v3." Add a numbered "## How to upgrade" section right after Requirements: install command, config rename, then breaking changes to review.

**3. Breaking changes are sorted alphabetically by class name — sort by required action or migration order instead.**
A-Z tells the reader nothing about whether the change affects them or what order to apply fixes in. Group by action type (renamed / removed / signature changed / behavior changed) or add a scannable table at the top: class name, change type, action needed. Let readers jump straight to what touches their code.

**4. Every entry ends in "update your usage accordingly" with no example — replace with a concrete before/after.**
Two sentences plus a stock phrase repeated 14 times is what's actually generating ticket volume: nobody knows what "accordingly" means for their specific case. Each entry needs a minimal before/after code snippet, the same way the SDK-migration template shows `client.old_method(...)` → `client.new_method(...)`.

**5. "Why we rebuilt the core" is placed before Breaking Changes and Requirements.**
Rationale is legitimate content, but it's not actionable — it shouldn't compete for position with the steps someone needs before they can safely upgrade. Push it down, or collapse it into a details/expander.

**6. No top-of-page summary or checklist.**
There's nothing a support agent can link to and say "read this box, you're done." Add a 4-line checklist at the very top: Java 21 required → run install command → rename config file → review N breaking changes (link to table).

Recommended section order:

1. Quick checklist (new)
2. Requirements (Java 21) — moved from last to first
3. How to upgrade (new — install command + config rename, moved out of FAQ)
4. Breaking changes — resorted by action type, each entry with a before/after snippet
5. What's new in v3
6. Why we rebuilt the core
7. FAQ — actual edge-case questions only, once the mandatory steps are removed from it

The underlying pattern: everything a support ticket asks about (can I upgrade, how do I upgrade, what exactly do I change) was placed last or mislabeled as optional, while everything that can wait (rationale, feature highlights) was placed first.