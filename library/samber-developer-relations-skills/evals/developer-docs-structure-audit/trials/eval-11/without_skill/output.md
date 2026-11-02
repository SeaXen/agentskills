# Ferrite docs structure audit

**Constraint up front:** I have no read access to Ferrite's actual repo — it's not in this working directory, and nothing in this conversation points me at it. Below is a real audit, not a stalling request: a self-diagnostic you run tonight, the failure patterns almost guaranteed at "70 pages, contributor-written, no writer" scale, a target structure, and a prioritized fix list sized to evenings-only bandwidth. Paste `SUMMARY.md` if you want page-by-page placement decisions instead of pattern-matching.

## 1. Run this yourself (15 min, in the mdBook repo)

- **Nesting depth**: `grep -oP '^\s+' src/SUMMARY.md | awk '{print length}' | sort -u` — anything past 2 levels of indent is too deep for a 70-page book; flag it.
- **Orphan pages** (files not linked from nav): `comm -23 <(find src -name '*.md' | sed 's|^src/||' | sort) <(grep -oP '\(\K[^)]+\.md' src/SUMMARY.md | sort)`
- **Dead internal links**: install `mdbook-linkcheck` if it's not already a preprocessor in `book.toml`. If it isn't, that alone explains rot nobody's caught.
- **Concept duplication**: `grep -ril "what is an actor\|actor model" src/` — count how many pages independently re-explain a core term. More than one is duplication, not redundancy.
- **One-click quickstart check**: from `src/SUMMARY.md`'s first entry, is there a page titled Quickstart/Getting Started reachable in one click, runnable in under 5 minutes, with zero prior context assumed?
- **Depth evenness**: `for d in src/*/; do echo "$d: $(find "$d" -name '*.md' | wc -l)"; done` — a subsystem with 1 page next to one with 15 signals contributor interest drove structure, not user need.

## 2. Failure patterns near-guaranteed at this stage

These aren't guesses about your specific pages — they're what happens to *every* contributor-grown, writer-less docs set once it crosses ~50 pages:

- **Concept sprawl**: each contributor who added a page re-explained actors/mailboxes/supervision from scratch because nothing canonical existed to link to. Symptom of the grep above returning >1 hit.
- **Diataxis collapse**: mdBook's default is numbered chapters, which flattens "what is X" (explanation), "how do I do X" (how-to), and "what are X's parameters" (reference) onto the same page. Reference material embedded in tutorial prose punishes both readers.
- **No canonical mental-model page**: actor frameworks live or die on whether the reader understands mailbox/supervision/backpressure semantics before touching code. If that's scattered across three intro pages instead of one, adoption friction starts on page one.
- **Hand-maintained API reference drifting from code**: if any mdBook page hand-documents function signatures or message types instead of linking to rustdoc/docs.rs, it *will* silently go stale — nobody has bandwidth to keep two sources of truth in sync. This is the single highest-leverage fix available: delete hand-written API pages, link out.
- **Orphans**: pages contributors wrote and forgot to wire into `SUMMARY.md`, or wired in but nothing contextually links to — invisible to anyone not already reading linearly.
- **Version drift**: pages written against an older macro/trait API, never revisited because no owner is responsible for docs as a whole, only for whichever page they personally touched last.
- **Missing "why" page**: no page answering "why an actor model, why Ferrite over Actix/Ractor/raw Tokio." This is both an adoption blocker and literally what CNCF TAG reviewers ask first in due diligence.
- **No production-readiness signals**: no benchmarks page, no adopters list, no versioning/MSRV/stability policy. CNCF sandbox review explicitly checks for these; their absence reads as "not production-used" even if that's false.

## 3. Target structure (Diataxis-mapped, sized to ~70 pages)

```
Introduction
├── What is Ferrite & why an actor model      (explanation — canonical, single source)
├── Ferrite vs Actix / Ractor / raw Tokio     (explanation — comparison, CNCF-relevant)
└── Architecture overview (one diagram)        (explanation)

Tutorials (linear, learning-oriented)
├── Quickstart: first actor in 5 minutes
├── Build a chat server
└── Build a supervised worker pool

Core Concepts (explanation, referenced everywhere else)
├── Actors & mailboxes
├── Messages & message passing
├── Supervision & fault tolerance
├── Actor lifecycle
├── Scheduling & the runtime
├── Backpressure & flow control
└── Distributed actors (if supported)

Guides (how-to, task-oriented)
├── Testing actors
├── Observability: logging, tracing, metrics
├── Graceful shutdown
├── Persistence / state recovery
├── Supervision strategies in practice
├── Integrating with the Tokio ecosystem (axum, tonic...)
├── Migrating from Actix / between Ferrite versions
└── Performance tuning

Reference (information-oriented — link out, don't hand-write)
├── API reference → docs.rs (do not duplicate in mdBook)
├── Macro reference (#[actor], #[message]...)
├── Configuration reference
└── Error types reference

Operations
├── Benchmarks
├── Production checklist
├── Known limitations
└── Versioning & stability policy (semver, MSRV)

Project (CNCF-relevant, can be thin pages that link to root-repo files)
├── Governance → GOVERNANCE.md
├── Security → SECURITY.md
├── Roadmap
├── Adopters
├── Contributing → CONTRIBUTING.md
└── FAQ
```

Every Core Concepts page becomes the single link target every Guide and Tutorial points back to instead of re-explaining. That link discipline is what actually kills concept sprawl — the folder structure alone won't.

## 4. CNCF sandbox review — docs-visible gaps

| Reviewer checks for | Where it should live | ⚠️ if missing |
|---|---|---|
| Why this exists / vs. alternatives | Introduction comparison page | Reads as "no differentiated positioning" |
| Architecture diagram | Introduction | Reviewers skim this first |
| Governance model | Project → Governance | Blocks sandbox application directly |
| Security disclosure process | Project → Security | Blocks sandbox application directly |
| Versioning/stability policy | Operations | Signals immaturity if absent |
| Adopters | Project → Adopters | Reviewers weight this heavily; even 2-3 named users help |
| Roadmap | Project → Roadmap | Shows the project isn't abandoned-in-place |

These are usually root-repo files (`GOVERNANCE.md`, `SECURITY.md`) already — the fix is a thin mdBook page linking to each, not new prose. Cheap, and closes a real gap in the same afternoon.

## 5. Priority fixes, ranked for zero writer budget

Reorg and pruning are cheap; new prose is expensive. Sequence accordingly.

| Tier | Effort | Action |
|---|---|---|
| 🎯 Tonight | ~1 hr | Relabel `SUMMARY.md` nav into the five top-level buckets above. Pure regrouping of existing pages, no rewriting. |
| 🎯 This week | Few hrs | Merge duplicate concept pages into one canonical page each; delete or redirect the rest. Fix orphans found by the `comm` command — either link them in or delete if dead. |
| 🎯 This week | ~30 min | Delete any hand-written API reference page; replace with a link to docs.rs. Stops future drift permanently. |
| This month | New content, but small | Write the 4 CNCF-gating pages: why-Ferrite/comparison, architecture overview, versioning policy, adopters. These gate the sandbox application — highest ROI content you'll write this quarter. |
| Ongoing | ~15 min setup | Add `mdbook-linkcheck` to CI. Catches future orphans/dead links automatically — replaces the audit you just ran manually. |
| Ongoing | Zero cost per PR | Add one line to the PR template: "Which section does this page belong in — Tutorial / Concept / Guide / Reference?" Forces the contributor to make the IA decision at write-time instead of you making it at audit-time. |

**Don't do:** a full rewrite, chasing Diataxis purity on every page, or adding net-new content beyond the 4 CNCF-gating pages. With one full-time-equivalent-minus and two evenings-only part-timers, reorganizing what exists and closing the CNCF-specific gaps beats a rewrite every time — a rewrite is exactly the kind of project that stalls forever under this staffing model.

## 6. The actual sustaining fix

No writer, ever, means the fix can't be "someone reviews docs periodically" — that someone doesn't exist. It has to be structural:

1. `mdbook-linkcheck` in CI — machine catches what a writer would have caught.
2. PR-template question above — pushes the IA decision to the person who already has the context (the contributor writing the page), at the one moment it's cheap to get right.
3. One of the three of you owns *nav placement* merge approval only — not content quality, not prose review, just "does this go where the template says it goes." That's a 30-second gate, not a job.