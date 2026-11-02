## What's wrong

**Root cause: every `/fr/` and `/ja/` page tells Google to index the English page instead of itself.** A cross-language `rel=canonical` is not a safe duplicate-content precaution — it is a direct instruction to drop the localized URL from the index and consolidate all ranking signal onto the URL it points to. Google does not treat translated content as duplicate content; canonical exists for exact/near-duplicate URLs in the *same* language (trailing slash, query params, print views), not for language variants. The previous agency applied the wrong tool for the job, and it has been silently suppressing every non-English page since it was set up.

That one misconfiguration explains both symptoms, but it explains them differently for each language — which is the part worth understanding before you fix anything.

### Why French is at zero, not just low

French has two failures stacked, not one:

1. **Wrong canonical** — every `/fr/` page points its canonical at `/en/`, so Google folds it into the English URL in the index.
2. **No hreflang at all** — French was never included in any alternate-links pass. Hreflang is the *only* mechanism Google uses to decide "serve this URL to a French-speaking searcher instead of the English one." Without it, even a page that somehow stayed indexed under its own URL has no signal telling Google to prefer it for `fr` queries.

So French isn't suppressed by one bug, it's absent from two independent systems that would otherwise get it found and served. It's not "basically zero traffic" because French demand is low — it's zero because nothing in the current setup can surface a `/fr/` URL for a French query even when the page itself is fine.

### Why Japanese never appeared at all — a worse failure, not a different one

Japanese got the hreflang pass at launch, which sounds like it should put it ahead of French. It doesn't, because of how canonical and hreflang interact: **Google requires a hreflang annotation to point at the canonical version of a page.** When it crawls a `/ja/` page and finds hreflang links declaring "I'm part of an EN/JA cluster" *and* a canonical tag declaring "actually, ignore me, the real page is `/en/`," Google's documented behavior is to trust the canonical and disregard the hreflang cluster on that URL. The alternates you generated at launch are being invalidated by the same tag that's already suppressing French.

That's a worse failure than French's, not a milder one: French was simply never given a signal. Japanese was given a correct signal that gets cancelled out by a conflicting one on the same page. A hreflang cluster with an internally contradictory member is treated as unreliable, which is consistent with Japanese never surfacing at all rather than surfacing weakly — there was never a clean, self-consistent cluster for Google to trust in the first place.

### Why this drifted instead of being caught

VitePress's `locales` config controls the `lang` attribute and theme/search strings, but it does not generate `hreflang` or `canonical` tags for you — those come from manual `head` entries (via `transformPageData`/`transformHead` or per-page frontmatter), maintained separately per locale. There's no single source of truth enforcing that every locale gets the same treatment, so it's entirely possible for one locale (English, when the site was EN-only) to have a boilerplate canonical block that gets copy-pasted into new locale folders without anyone revisiting whether it still makes sense. That's exactly the shape of this bug: it's a leftover default, not a decision anyone made about French or Japanese specifically, and nothing in the build pipeline would flag two locale folders having inconsistent head tags — it has to be checked by hand across languages, which is what let French sit broken since before Japanese even existed.

### Portuguese is a different failure class, not the same one

The FR/JA problem is a *signal* problem — the pages might be fine, but Google's being told to ignore them. Portuguese is (likely, pending the same check) sitting under the identical canonical bug, but on top of that it has a **content problem**: a bulk machine-translation run with no human review. Fixing canonical/hreflang for Portuguese would remove the suppression signal, but it would then expose unreviewed MT content to indexing — Google's spam policies explicitly cover automatically translated content generated at scale without human oversight or added value (scaled content abuse). That's not a ranking-penalty risk to shrug off; it's the kind of thing that can draw a manual action, and manual actions on one part of a site can chill crawl trust for the rest of it, including the FR/JA pages you're about to fix. Don't flip Portuguese into the index until someone has actually reviewed it — sequence that behind the FR/JA fix, not alongside it.

## What to check before touching anything (confirms this diagnosis with evidence, costs nothing)

- **Search Console → Page Indexing report**, per locale: expect to see `/fr/` and `/ja/` URLs sitting under **"Alternate page with proper canonical tag"** — this is the exact, named GSC status for "we saw this URL, but its own canonical points elsewhere, so we indexed the other one instead." If that's what's there, this diagnosis is confirmed, not just plausible.
- **View-source (not rendered DOM) on one `/fr/` and one `/ja/` page**: confirm the canonical `href` and every `hreflang` `href` in the `<head>`.
- **Check the reciprocal side on the matching `/en/` page**: does it declare an hreflang alternate back to `/ja/`? To `/fr/`? Hreflang has to be fully reciprocal across every version in the cluster — including English — or the whole cluster is invalid, not just the non-English side.
- **Check for `x-default`** — not mentioned as present; if missing, add it when you fix the rest.
- **Confirm the sitemap** actually lists `/fr/` and `/ja/` URLs at all (a canonical-elsewhere page is sometimes quietly dropped from sitemap generation too, which would compound the problem).

## Fix priority

1. **Remove the cross-language canonical.** Every `/fr/`, `/ja/`, and (once reviewed) `/pt/` page needs a **self-referencing canonical** — the page's own URL, not `/en/`.
2. **Build one complete, reciprocal hreflang set covering all shipped locales**, generated from a single config/template rather than hand-maintained per locale — this is what let French get skipped once already and will do it again for the next language if it stays manual. Include `x-default`.
3. **Re-request indexing** for `/fr/` and `/ja/` URLs in Search Console after the fix, and watch the Page Indexing report for the "Alternate page with proper canonical tag" bucket to drain out.
4. **Hold Portuguese out of the fix until reviewed.** Same canonical/hreflang correction applies, but don't let it start ranking on unreviewed MT content — get a human pass on quality first, then bring it in through the same corrected mechanism.