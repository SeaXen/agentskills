## Audit: Halloway Queue v2→v3 upgrade guide

**Diagnosis in one line:** this page reproduces the skill's own documented anti-pattern outline almost exactly — `references/guide-outline-examples.md` names this precise section order (`What's new` → `Why we rebuilt the core` → alphabetical `Breaking changes` → `FAQ` hiding the real steps → `Requirements` last) as the worked negative example. That's not a coincidence worth restating gently: it's why support is drowning.

### Score against the six pass-threshold criteria

| # | Criterion | Verdict | Why |
|---|---|---|---|
| 1 | Completeness | **Unverifiable** | Two-sentence entries with no code give no way to diff against the v2→v3 API surface. Need the real tag-to-tag diff before this can even be scored. |
| 2 | Detectability | **Fail** | None of the 14 entries has a search pattern or literal error/warning text. A reader can't tell if a given class is even affected without reading all 14. |
| 3 | Sufficiency | **Fail** | "Update your usage accordingly" is the skill's own documented bad example, verbatim in spirit. Nothing the reader can type comes from this guide. |
| 4 | Automation honesty | **Fail** | The one real fix material that exists (config-file rename steps) is stranded in FAQ, disconnected from the entry it fixes, with no stated coverage boundary. |
| 5 | Path validity | **Fail** | No path shape is stated anywhere — not staged, not single-hop. With 14 breaking changes landing at once and no mention of an interim warning release, the reader has to guess they're taking the single-hop path. |
| 6 | Self-containment | **Fail** | The reader must leave the breaking-changes list and dig through FAQ to find the install command and the config migration steps — the exact "self-containment" failure the skill calls out. |

**0 of 6 pass outright, 1 unverifiable.** This guide would not survive a cold-upgrade run as written.

### The four defects, in order of what's costing you the most tickets

1. **The real migration steps are in the FAQ.** The npm install command and the config-file rename steps are the two things a reader actually needs to type, and they're in the one section nobody reads top-to-bottom. Move the install command to a dedicated `## Install` section near the top, and turn the config-file rename into its own `### Changed: config file renamed to X` breaking-change entry (or, if it's the cause behind several of your 14 entries, one grouped entry per the skill's grouping rule — don't fix this by splitting it into more scattered pieces).

2. **All 14 breaking-change entries fail the entry anatomy.** Two sentences plus "update your usage accordingly" is short for: no detection signal, no before/after code, no fix command, no escape hatch. Per the skill's own template, an entry needs six parts in this order — verb-prefixed heading with a stable anchor, an affected-if line (search pattern *and* literal error/warning text), a three-sentence why, before/after code, the fix (codemod command or numbered steps, never "or do it manually"), and an explicit escape hatch or "none." Rewriting these is the highest-cost fix on this list, but it's also the one directly named in the skill's failure-mode table as generating support tickets instead of preventing them — do this even though it's expensive.

3. **Breaking changes are ordered alphabetically by class name.** That's an organizing principle for you, not for a reader triaging "does this hit me." Reorder by blast radius — whichever change the most call sites hit goes first — using telemetry if you have it, dependent-repo search if you don't, maintainer estimate as the last resort. Alphabetical order means someone hitting your highest-impact break has to read past 13 irrelevant entries first.

4. **Requirements (Java 21) is the last section.** A reader who fails that floor never reaches any of your 14 entries or the install command — everything above it was wasted reading. Move Requirements to the top, right after scope, before the breaking changes. State it as a machine-checkable comparison (`Java >= 21`, not prose), and while you're there: an npm install command alongside a Java 21 requirement is worth double-checking — if this is a Node client that shells out to a Java-based server/CLI component, say that explicitly, because right now the guide reads as if the two requirements belong to different products.

### What to cut, not fix

**"What's new in v3" and "Why we rebuilt the core"** are, per the skill's own reference, "a marketing section on a work document" and "rationale that belongs in a blog post." A reader arrives here because their build is already broken — this screen space was theirs. Cut both to a two-line teaser at most ("v3 buys you X and Y") or move them out entirely to the release blog post, and link to it from one line at the top instead.

### Structural rebuild — target outline

```markdown
# Upgrading from v2 to v3

<Scope: package(s) covered, measured effort once you've run a cold upgrade>

## Before you start
<Path shape: single-hop or staged. If single-hop, say so plainly — 14 changes land at once.>

## Requirements
- Java >= 21
<any other floors: runtime, peer deps, build tooling>

## Install
<exact npm command, pulled out of FAQ>

## Automated migration
<codemod if one exists; if none, say so explicitly — "no codemod exists" is information>

## Breaking changes
<14 entries, ordered by blast radius, each with all six parts — including the
config-file-rename entry currently stranded in FAQ>

## New deprecations
## Behavior changes
## Housekeeping
## Troubleshooting
<keyed by literal error text — this is where support tickets get self-served>

## Full changelog
<link only, never the migration path itself>
```

### What I need from you to finish this

I only have the page's structure, not the actual prose of the 14 entries or the FAQ content — I can't rewrite specific entries or produce the inventory table without that text. To close this out:

1. Paste (or point me to) the actual text of the 14 breaking-change entries, the FAQ's install/config-rename steps, and the "Why we rebuilt the core" section.
2. Answer the four questions that change the shape of the fix: who upgrades (open-source choosing their own moment, or paying customers under a deadline)? Is there telemetry on which of the 14 changes gets hit most, or do we rank by dependent-repo search / your own estimate? Does a codemod exist or is manual-only the honest answer? Did v2 already emit deprecation warnings for any of these, or does v3 break cold?
3. Once entries 1–3 above are rewritten, run a cold upgrade — a real consumer project, upgraded using only the rewritten guide, by someone who didn't write it — before republishing. That run is also where "40 minutes" or whatever the real number is comes from; don't publish an effort estimate you haven't measured.

Hand me the actual entry text and the answers to (2), and I'll rewrite the top three highest-blast-radius entries in full six-part form as the next step.