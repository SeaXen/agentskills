# Sanity check: Quillrock troubleshooting page structure

Verdict: don't ship this structure as proposed. All four decisions conflict with explicit, named rules in `developer-troubleshooting-docs` — not close calls, direct hits against worked examples and named failure modes in the skill. Below is each decision against the source text, then what to do instead.

## 1. One page, 28 errors as H3 sections

**Conflicts with the skill's own named failure mode**, `references/discoverability-and-metrics.md`, "What no longer works":

> A single mega "Troubleshooting" page holding thirty issues: only one of them can win the query, anchors get lost in caches, and the page becomes unmaintainable.

That's 28 OAuth errors on one URL, almost verbatim the case called out.

This isn't an absolute ban on one page, though — Step 4's shape table allows "one page per code, **or** one anchored row per code on a codes page" for the error-reference shape, and the skill cites Twilio's and Stripe's single-page catalogs approvingly. The difference between those and the mega-page failure mode is addressing discipline: Twilio/Stripe give every code its own stable, deep-linkable anchor with the code itself as the visible label. If Quillrock's page does that — each of the 28 gets its own stable anchor, and the code is the heading (see #2) — a single catalog page is structurally defensible. If errors get buried under soft topic headers with no stable per-error anchor, it's the mega-page failure mode by definition. Decide this deliberately, not by default, and re-check it if the catalog grows past 28.

## 2. Topic titles instead of the error string ("Authentication problems," "Token problems," "Redirect problems")

**This is the skill's own worked "weak" example, almost word for word.** `references/entry-templates.md`:

```markdown
## Authentication problems

If you have trouble authenticating, make sure your credentials are correct...
```
> Nothing here is searchable (the error string is absent)...

And the failure-modes table in `SKILL.md`:

| Failure | What it looks like | Fix |
|---|---|---|
| Missing error string | "Authentication problems" as the title | Verbatim string in title, heading and body |

Readers of an OAuth error page arrive holding an exact string — `invalid_grant`, `redirect_uri_mismatch`, whatever Quillrock emits — from a stack trace or a failed curl. They search or paste that string, not a category name. Step 8: "Put the error string verbatim in the title, the first heading and the body. 'Troubleshooting authentication' never matches a search for `invalid_grant`."

The writer's instinct — don't scare the reader with raw error codes — isn't wrong, it's just aimed at the wrong surface. `entry-templates.md`, "Microcopy: the string versus the page," draws exactly this line: the *emitted* error message (the string Quillrock's SDK shows in a UI or log) is the place to keep tone soft and jargon-free; "the entry carries the diagnostic depth." Conflating the two — softening the *docs heading* instead of the *product's error text* — is called out as "the most common structural mistake." If Quillrock's raw error strings read as scary, that's a product-copy fix to route to the owning engineer, not a reason to rename the docs headings.

Topic groupings can still exist as navigational sugar (a sidebar grouping, an H2 section wrapper) as long as the actual per-error heading underneath is the verbatim string. Grouping-as-navigation is fine; grouping-as-heading-replacement is the failure mode.

## 3. DRY: one shared "Understanding token validity" section, nine entries link up to it

**Directly contradicted, and the skill anticipates this exact argument by name.** Step 8, `SKILL.md`:

> Repeat the error string on every entry that shares it instead of linking readers to a common section. Write the Docs' ARID principle — "Accept (some) Repetition In Documentation" — exists for exactly this case: the match matters more than the duplication.

The "same as we'd do in code" instinct is the thing this rule exists to override. Docs and code have different failure costs for duplication: in code, DRY prevents divergent logic; in a troubleshooting entry, DRY produces a reader who has to leave the page they landed on (mid-incident) to go read a different section before they can act. Step 5 states the reader-facing reason directly: "a reader who already knows the cause skips to the steps, and a reader who is guessing needs to confirm the cause before running commands" — that requires the cause to be *on the entry*, not one hop away.

There's a second cost beyond human scanning: retrieval. `references/error-catalog-and-ai-surfaces.md`:

> Write blocks that stand alone... A cause-remedy pair that depends on the paragraph above it retrieves as a fragment.

An assistant answering from "Authentication problems" for a query about clock skew, having chunked only the linked-to section, is the exact scenario this rule is written against. Since Quillrock's page will likely get paraphrased by an AI assistant at some point (Step 9's interview question), this isn't a hypothetical cost.

Fix: repeat the two-or-three-sentence clock-skew explanation in the Cause section of each of the nine entries. It's cheap — this is precisely the case ARID is arguing duplication is worth it.

## 4. Error strings in a collapsed "Technical details" accordion at the bottom

**Conflicts with the first-screen rule, twice over.** `references/discoverability-and-metrics.md`:

> Answer in the first screen. Message, cause, first fix — before any preamble about the feature.

And Step 8, `SKILL.md`: "Put the error string verbatim in the title, the first heading and the body." A collapsed accordion at the bottom is neither the first heading nor the first screen — it's the opposite structural choice from what's specified. Combined with #2 (topic titles instead of the string), this means the verbatim string wouldn't appear anywhere until the reader expands a control at the bottom of a section they had to scroll past first — exactly the scenario "nobody browses a troubleshooting section speculatively" (opening line of the discoverability reference) is warning about.

Quoting rules in `entry-templates.md` reinforce why the string needs to be plainly present, not tucked away: "Put it in a fenced block so copy-paste is clean and search engines index it as text." A collapsed accordion doesn't strip search indexing on modern engines, but it does fail the human-scanning bar and the "first screen" placement rule regardless of indexing mechanics.

## What to tell the writer

The instincts behind this proposal — reduce duplication, don't scare readers, keep the page visually clean — are reasonable engineering and UX instincts, applied to the wrong surface for this content type. Recommend instead:

1. **Structure**: pick one — 28 individual pages, or one catalog page with 28 stably-anchored entries (Stripe/Twilio pattern). Either satisfies Step 4; a soft-topic mega-page with no per-error anchor satisfies neither.
2. **Headings**: the verbatim error string, every time, per Step 8 and the "Missing error string" failure mode. Topic labels can live as a sidebar/TOC grouping, never as the entry's own heading.
3. **Clock-skew explanation**: paste it into all nine Cause sections, per the ARID principle. Cheap, and it's what keeps each entry self-contained for both human scanners and retrieval chunking.
4. **Message field**: fenced code block, first screen, not an accordion — per "answer in the first screen" and the quoting rules.

Also worth raising before any of this is written: Step 6 — since these are 28 stable OAuth identifiers, ask whether they're already declared in one machine-readable place in the product (an enum, an error table). If not, that's a smaller, higher-leverage fix than the page structure itself: generate the catalog from one source so the docs and the emitted codes can't drift apart, the way Stripe/Twilio/PostgreSQL do.