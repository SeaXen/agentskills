# Stagpath Analytics — Documentation Audit

## Bottom line

Three of four findings share one root cause: pages and sections mix or omit the standard documentation types (concept, how-to, reference) instead of separating them. That shows up as a landing page with a 71% exit rate, a high-traffic page fighting three jobs at once, and a well-searched SDK with no entry point. The fourth finding — broken Go samples — is a separate, unrelated maintenance gap. None of this is a content-depth problem: the Reference section proves the team can structure docs well when scoped correctly. This is a prioritization and separation problem, not a skills gap.

| # | Finding | Impact | Effort | Priority |
|---|---|---|---|---|
| 1 | Node SDK has no quickstart | 260 zero-result "node getting started" searches / 90 days | Low | 🔴 |
| 2 | `access-control.md` mixes concept, how-to, and reference | #2 search landing page, degraded for most visitors | Medium | 🔴 |
| 3 | Guides landing page: 41 ungrouped links | 71% exit rate on "how to" queries | Medium-High | 🟠 |
| 4 | Go code samples don't compile | Erodes trust across the whole doc set | Low to patch, medium to prevent | 🟠 |

## Findings

### 🔴 1. Node SDK: no quickstart, 260 dead searches in 90 days

The Node SDK has seven how-to pages and an API reference, but nothing that takes a new developer from zero to a working call. Site search shows "node getting started" queried 260 times in 90 days, returning zero results every time.

This is the cheapest finding to fix and the easiest to justify: the demand already exists, arrives with unambiguous intent, and gets silence instead of an answer. A how-to page assumes you already know what you're doing; these 260 searches are from people who don't yet. One quickstart page — install, configure, first successful call, next steps — closes the gap. No restructuring of existing content required.

Open question worth checking before writing it: do other language SDKs already have a quickstart that Node is missing, or is this gap universal? That changes whether this is a one-off fix or a pattern to fix everywhere.

### 🔴 2. `access-control.md` does three jobs on your #2 landing page

The page runs a permissions diagram (concept), nine numbered steps to add a service account (how-to), and a 30-row permission table (reference), all on one page — and it's the second-most-common way developers enter the docs.

On a low-traffic page, this is a minor wart. On the #2 landing page, it degrades the experience for most people who land in the docs at all, regardless of which of the three things they came for. Someone checking a permission scope scrolls past setup steps to find the table; someone mid-setup has to skip a diagram and a 30-row table to find step 4.

Fix: split into three pages — concept, how-to, reference — cross-linked, matching the pattern the Reference section already uses successfully. The content exists; this is decomposition and linking, not new writing.

### 🟠 3. Guides landing page: same problem, one layer up

41 links, no grouping — 14 conceptual, 27 procedural, mixed together. Site search shows "how to" queries landing here and leaving 71% of the time.

Same root cause as Finding 2, at the scale of a navigation hub instead of a single page. Visitors arrive with clear procedural intent ("how to") and land on a wall of undifferentiated links where barely more than half are even the right type. Fix this after Finding 2: prove the concept/how-to split works on one page first, then apply the same split here — group by task or use case, not alphabetically, and consider whether some of the 14 conceptual links belong in Guides at all.

### 🟠 4. Go code samples don't compile

Separate root cause from the three findings above — this is a maintenance gap, not an information-architecture one.

A developer who copy-pastes one broken sample stops trusting every other sample on the site, including the working ones. This is worth root-causing (version bump with no regression coverage? no CI on doc code at all?) rather than just patching the current breakage, because the same failure mode will hit the new Node quickstart from Finding 1 the moment something in the SDK changes, unless samples get automated compilation checks in CI.

## What's working

The Reference section is genuinely well organized. Keep it as the internal template for the concept/how-to/reference split recommended in Findings 2 and 3 — the team doesn't need to learn a new pattern, just apply the existing one more consistently.

## Recommended sequence

1. **Node quickstart** (Finding 1) — quantified, low-effort, no dependencies. Ship first.
2. **Go sample CI check** (Finding 4) — bounded fix, and puts a safety net under new content (including the quickstart from step 1) before it can rot the same way.
3. **Split `access-control.md`** (Finding 2) — highest-value single-page fix, sets the template.
4. **Regroup the Guides landing page** (Finding 3) — same fix pattern at scale, sequenced after step 3 so the split is already proven on one page.