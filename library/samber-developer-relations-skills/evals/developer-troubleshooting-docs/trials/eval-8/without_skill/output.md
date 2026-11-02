## The plan as stated has two problems: wrong order, wrong unit of work

You're fusing three separate projects into one 2-week sprint: (1) reconciling three drifted sources of truth, (2) authoring 140 reference pages, (3) migrating the doc platform. Each has a different owner, different risk profile, and a different critical path. Bundling them loses you weeks, not saves them.

## 1. Reconcile before you write anything

`codes.go`, the TS enum, and the wiki (last synced at ~90 codes) have almost certainly diverged in more places than the count suggests — codes with different messages, codes present in one place and not another, retired codes still listed. Writing 140 pages *before* knowing which source is right means writers will faithfully document drift as fact.

- **Write a diff script** (couple hours, not a writer task): parse `codes.go`, the TS enum, and export the Confluence table, produce a three-way diff.
- Declare `codes.go` canonical — it's the only one that ships. TS enum and wiki are downstream copies that already proved they rot.
- Fix the diff findings in code/TS first. Don't let writers silently "resolve" a numbering mismatch — that's an engineering decision, not an editorial one.

## 2. 140 near-identical pages is a generation problem, not a writing assignment

Splitting 140 pages across 2 writers for 2 weeks (35/writer/week) treats this as prose work. It isn't — it's structured data with a couple of fields that need human judgment. Hand-authoring invites exactly the inconsistency (tone, missing fields, format drift) that made the wiki unreliable in the first place, and guarantees a fourth copy to keep in sync.

- Add structured doc-comments above each entry in `codes.go` (code, short message, likely cause, remediation, maybe a related-codes list). This is the same discipline as Go doc comments — put it where it can't drift from the code.
- **Write a generator** that walks the const block and emits a manifest (`errors.yaml` or JSON) — one script, one afternoon of engineering time, not writer time.
- Generate the TS enum from the same manifest instead of hand-maintaining a second copy. Kills the drift structurally, not just for this round.
- Template-render the manifest into Docusaurus MDX pages (or a single data-driven reference page with client-side search — better UX for 140 near-identical entries than 140 separate files; decide based on how users actually search errors today).
- **Writers' real job**: fill in "likely cause" / "remediation" quality prose for each entry, reviewed against the generated skeleton — not lay out 140 pages by hand. Same total prose volume, far less mechanical work, zero formatting inconsistency.
- Add a CI gate: build fails if `codes.go`, the generated TS enum, and the generated manifest disagree. This is what stops you from being back here in 18 months at 200 codes.

## 3. Don't run the platform migration and the content build in the same window

Hugo→Docusaurus is a mechanical, engineering-owned task (themes, redirects, nav config, existing content migration). The error-code reference is a content/generation task. Doing both at once means writers are producing content against a template that's still moving, and any Docusaurus theming bug looks like a content bug and vice versa — bad for debugging, bad for morale.

- **Sequence, don't parallelize**: migrate the existing site to Docusaurus first (mechanical, reversible, no new content risk). Stabilize it.
- Build the error-code generator + manifest in parallel on the engineering side — it doesn't depend on which platform renders it.
- Land the generated error-code section as the first new content shipped on Docusaurus, once the platform is stable. It's actually a good pilot for the new platform, since a data-driven MDX section stress-tests Docusaurus's plugin/templating story better than a straight content port would.
- If the two must overlap for calendar reasons, keep them on separate people: migration is engineering-only; writers never touch Docusaurus internals, they write against the manifest schema regardless of which platform renders it.

## Suggested URL/IA for the reference section

`/docs/errors/{code}` if you go one-page-per-code, or `/docs/errors` as a single searchable/filterable table if 140 entries are short enough — decide by checking how support/users currently search the wiki table (ctrl-F a page vs. deep-link a specific code). Don't nest deeper than that; it's a flat reference, not a guide hierarchy.

## Revised scope, if you need a number

- Week 1: engineering — reconciliation script + fixes, doc-comment schema, generator, CI gate. Writers start drafting cause/remediation prose against the current (unreconciled) list in parallel, expect ~10-15% rework once reconciliation lands.
- Week 2: writers finish prose for all 140 entries against the finalized manifest; engineering wires generation into Docusaurus (started separately, ideally already migrated beforehand).
- Docusaurus migration: treat as its own ticket with its own timeline, ideally *before* week 1 starts, owned by an engineer, not the writers' 2-week clock.

If the 2-week/2-writer deadline is fixed and non-negotiable, cut the migration from this cycle entirely — ship the reconciled, generated reference on the current Hugo site, migrate platforms after, once there's no content deadline pressuring the theming work.