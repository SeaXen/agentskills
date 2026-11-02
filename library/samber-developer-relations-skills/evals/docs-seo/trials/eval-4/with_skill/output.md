## What's wrong with Lumendra's docs

**Verdict:** The `/fr/` → `/en/` and `/ja/` → `/en/` canonicals are the root cause of both symptoms. A `rel=canonical` is not a duplicate-content shield between languages — it tells Google "index the other URL instead of this one." Every French and Japanese page is explicitly telling Google not to index itself. That's not a mitigation against a "duplicate content penalty" (that concept doesn't apply to translated content in the first place); it's the mechanism actively deleting both locales from search. On top of that, the incomplete hreflang mesh from the Japanese launch and the unreviewed Portuguese set compound the problem in two different ways.

### 1. Cross-locale canonicals — the blocking defect

`/fr/*` and `/ja/*` pointing `rel=canonical` at `/en/*` is a self-canonical breach, not a safety measure. Google treats the canonical as authoritative about which URL represents the content; pointing a translation at the English original says the French and Japanese pages are non-canonical duplicates of the English one, so Google indexes the English URL and drops the others — exactly the "French traffic near zero, Japanese never appeared" pattern described. This is why French, despite being live long before Japanese, still gets nothing: the canonical has presumably been wrong since the agency set it up, not just since three weeks ago.

The "duplicate content penalty" rationale the previous agency gave is wrong on its own terms. Google has never treated translated content as a penalizable duplicate — that's precisely the problem `hreflang` exists to solve (multiple language/region variants of the same content, each meant to rank in its own market, none penalized for the others existing). Canonicalizing translations to the source language is a known anti-pattern for exactly this reason.

**Fix:** every locale self-canonicalizes. `/fr/guides/webhooks/` canonicals to itself, `/ja/guides/webhooks/` canonicals to itself, `/en/guides/webhooks/` canonicals to itself. No cross-language canonical anywhere.

### 2. Missing/incomplete hreflang mesh

Self-canonicalizing alone isn't enough — without `hreflang`, Google has no signal connecting the three (soon four) language versions of the same page to each other, and no fallback for a visitor whose language doesn't match any of them. Google's own requirements, and where Lumendra currently fails them:

- **Self-reference**: each language version must list itself as well as every other version. Whatever `/ja/` currently emits needs to include `ja` pointing at itself, not just at `en`.
- **Return links (bidirectional)**: if `/en/` lists `/ja/`, then `/ja/` must list `/en/` back, or Google may ignore the whole annotation set. Given `/fr/` was never touched when `/ja/` shipped, French pages almost certainly don't list Japanese, and — if `/en/`'s alternates were regenerated for the Japanese launch — `/en/` may now list `/ja/` without `/ja/` (or `/fr/`) reciprocating correctly. That mismatch is enough to get the annotations discarded outright.
- **`x-default`**: needed for visitors whose browser language matches none of `en`/`fr`/`ja`. Confirm it's present and points at a sensible fallback (typically `/en/`).
- **Hreflang belongs on canonical URLs only**: this is exactly why the current setup is doubly broken — `/fr/` and `/ja/` are canonicalized *away from themselves*, so even if their hreflang tags were otherwise correct, Google is entitled to discard them, since annotations on a non-canonical page aren't trusted.

**Root cause of the launch gap specifically:** shipping `/ja/` regenerated `/ja/`'s own alternate links but nobody regenerated `/fr/`'s. hreflang is a mesh, not a per-locale, per-launch task — adding a locale changes what *every other locale's* alternates should say. `/fr/` today is very likely still advertising a two-way (`en`/`fr`) or even just self-referencing set with no `ja` entry, which is a return-link failure for the new locale, and may be why nothing about Japanese resolved cleanly either.

**Fix:** regenerate the entire hreflang mesh across every locale — `en`, `fr`, `ja` — in the same change, not just the newly-launched one. Any future locale launch (or removal) requires the same full regeneration, every time.

### 3. Unreviewed Portuguese machine translation

This is a different failure mode from the other two and needs a different fix. An unreviewed MT dump shouldn't be self-canonicalized and added to the hreflang mesh like a real locale — it would just compete with the English (or eventually French) page for the same queries while offering nobody a page anyone signed off on. The one legitimate use of a cross-locale-style suppression here is `noindex` on the Portuguese set until it's actually reviewed. Once reviewed and adopted as a real locale, it follows the same self-canonical + full hreflang treatment as French and Japanese — and at that point the mesh gets regenerated again to include `pt`.

### Fix list, in order

1. **Remove** `rel=canonical` from `/en/` on every `/fr/` and `/ja/` page; self-canonical each locale to itself. Blocking defect — nothing else here matters until this ships.
2. **Regenerate the full hreflang set** (`en`, `fr`, `ja`, each listing all three plus `x-default`) across all three locales in one pass, sitemap-delivered given the locale × page count. Verify bidirectionality — every page that lists another must be listed back.
3. **`noindex` the Portuguese set** until someone reviews it; exclude it from the hreflang mesh while it's noindexed.
4. **Re-check after Google recrawls**: `/fr/` and `/ja/` should start appearing as indexed, self-canonical URLs in Search Console, and the cross-canonical warnings should clear. This is a pending outcome, not an immediate one — re-indexing runs on Google's schedule, not Lumendra's.
5. Treat any future locale addition or removal as a trigger to regenerate the mesh for every existing locale, not just the one being added.