# Where to push back on the ridgeline.sh/docs move

**Verdict:** the "subfolder inherits authority" argument is the weakest decision in this whole picture, and there are two cheaper, more likely root causes sitting in front of it — one of which is a genuine indexability defect you already have, unrelated to which domain wins. Fix those first; they'll tell you whether the migration is even solving the right problem.

## 1. The domain-shape argument itself is a known weak decision, not a strong one

Subdomain-vs-subfolder is explicitly the lower-value, higher-cost call in this class of problem: a subfolder does pick up some of the parent domain's authority, a subdomain is easier to host independently — but for a site that's *already established and already indexed*, migrating it costs more than that difference is worth. Treat it as an infrastructure preference, not an SEO mandate. That's the frame to hand back to your head of growth: the premise isn't wrong, it's just not worth a 4,000-page migration on its own.

## 2. ⚠️ You already have an unresolved duplicate-domain defect — fix it regardless of the outcome of this debate

`ridgeline.readthedocs.io` and `docs.ridgeline.sh` both serving 200 with identical content, both indexed, is a textbook mirrored-domain problem. The fix is independent of the subfolder question: pick the domain you want to win (almost certainly `docs.ridgeline.sh`, since that's the direction you're already headed), canonical or redirect the `.readthedocs.io` host to it, and make the sitemap agree. That's a config change, not a migration — RTD lets you set this without moving a single URL. Do this first; it removes one whole axis of "Google might be splitting signal between two hosts" before you touch anything bigger.

## 3. ⚠️ The React rewrite is a bigger suspect than the URL shape — this needs to be ruled out before anything else

Canonical tag, page body, and sidebar nav all arriving via JavaScript is a blocking defect, not a stylistic detail: if Google's renderer doesn't reliably see the canonical tag, it can pick its own — which is exactly the kind of thing that produces two indexed hosts with identical content and a slow traffic bleed that started right after a theme swap. Before spending months on a URL migration, check:

- **`curl -s https://docs.ridgeline.sh/some-page | grep -c 'rel="canonical"'`** — confirm the canonical is in the raw HTML, not just the rendered DOM.
- Same check for body text and nav `<a href>`s on a couple of representative pages.
- In Search Console, the **"Duplicate, Google chose different canonical"** bucket — that's the direct readout of whether this is actually happening at scale.

If the canonical isn't in the initial HTML, that alone plausibly explains both the dual-host indexing *and* the traffic slide, and no amount of moving to a subfolder fixes it — you'd just be migrating the same unreadable signal to a new URL.

## 4. The search widget is a separate, compounding risk on a 4,000-page site

A search widget with no plain links means whichever pages aren't reachable through the sidebar nav (also JS-injected) have no crawlable path in unrendered as well as poorly-linked in general — on a reference tree this size, that's exactly the shape that produces orphans and dead ends at scale. Worth confirming there's a complete, accurate `sphinx-sitemap` output covering all 4,000 pages, since that may currently be the *only* crawlable path into large parts of the docs.

## 5. Even granting the authority argument, the migration is the most expensive, least reversible move on the table

A full URL-tree move needs a per-page redirect map (never a blanket redirect to a new root — that reads as a soft 404 and drops page history), 301s kept live for at least a release cycle because external tutorials and cached answers keep sending traffic long after, and a sitemap update in the same deploy. That's a standing project for a site this size, and it's the one move here you can't cheaply undo once external links and search results have re-pointed at the new URLs. Compare that to items 2 and 3 above, which are config/render fixes measured in hours, not months.

## What to actually propose instead

1. Canonicalize/redirect `ridgeline.readthedocs.io` → `docs.ridgeline.sh` now. Cheap, reversible, removes the duplicate-host problem outright.
2. Confirm (via the `curl` checks above and Search Console) whether the JS-injected canonical/body/nav is the actual cause of the traffic slide. This is the finding that should drive the roadmap, not the domain-shape preference.
3. If server-side rendering (or at least SSR/prerendering for canonical, body, and nav) turns out to be the fix, ship that — it's a change that reaches every one of the 4,000 pages at once, same as the migration would, at a fraction of the risk.
4. Only revisit the subfolder move once 1–3 are done and you can see, from a clean baseline, whether there's any indexation or traffic gap left that a URL-shape change would actually close. If there isn't, the migration has no case left to make.

**What I can't verify from here:** Search Console access to confirm which host/canonical Google is actually picking, whether RTD's own canonical-domain setting is currently configured at all, and the `robots.txt`/`X-Robots-Tag` state on both hosts. Pull those before finalizing the sequencing above — they'll confirm or kill the render-defect hypothesis in item 3.