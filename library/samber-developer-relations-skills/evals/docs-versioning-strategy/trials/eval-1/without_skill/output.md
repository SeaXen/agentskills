# Recommendation: don't turn on per-release docs versions

I'd skip the four-version dropdown. A single deployment with no pinning means every customer is on 2025.1, so the 2023.2, 2024.1 and 2024.3 docs would describe an API nobody is calling. Here is what I'd do instead, plus the setup and canonicals if you build the dropdown anyway.

## Why per-release versions hurt here

- **The dropdown promises something you don't offer.** Payments APIs have one because customers pin a version and the behavior differs between versions. Your releases are additive and unpinned, so choosing 2023.2 in the dropdown gives a customer no way to get 2023.2 behavior.
- **Old docs can mislead.** A customer reading 2024.1 will see an endpoint or field as missing, when it works fine today. Expect support tickets and wrong "it doesn't support X" conclusions.
- **Maintenance multiplies by four.** Every typo fix, clarification and security note needs backporting to three frozen sets, or those sets drift into being wrong. The platform makes switching versions on free, but the editorial cost is not.
- **It hurts search and AI answers.** Four near-identical copies of each page split ranking signals and give search engines and LLMs outdated content to quote.
- **It sets up a future problem.** If you later introduce a breaking change or version pinning, a dropdown built on release names will have taught customers the wrong mental model.

## What serves the PM's goal instead

The PM's real need is "enterprise customers can see the docs as of the release they evaluated." Because nothing has ever been removed, that equals the current docs filtered by introduction date. You can deliver it on one docs set:

1. **Add "Available since" markers.** Put a small badge such as `Since 2024.1` on every endpoint, parameter, event type and field added after 2023.2. Treat anything unmarked as present since 2023.2. Add the marker to your page template or frontmatter so it stays consistent.
2. **Add a "What's new by release" page.** List each release name (2023.2, 2024.1, 2024.3, 2025.1) with its additions, linking to the affected reference pages. It is a view of the changelog, not a copy of the docs.
3. **Add a one-line explainer to the reference landing page:** "Ferrocast has one live API. All customers use the latest release. Releases only add; nothing is removed. To see what existed at a given release, use the *Since* badges or the release notes."
4. **For sales, create a short "Evaluating an older release?" page.** It says: everything from your release still works, and here is what was added since (linked to the what's-new page). That answers the question the dropdown was meant to answer, and it makes the additive-only guarantee a selling point.
5. **Optional, if the platform supports it:** a client-side "Show docs as of release ▾" filter that hides badged items newer than the chosen release. It gives a dropdown-like experience without separate content. The default stays "Latest".

## If you build the dropdown anyway

**Version setup**

| Dropdown label | URL prefix | Content |
|---|---|---|
| 2025.1 (latest) | `/docs/` (no version segment) | Live docs, the only set you edit |
| 2024.3 | `/docs/2024.3/` | Frozen snapshot |
| 2024.1 | `/docs/2024.1/` | Frozen snapshot |
| 2023.2 | `/docs/2023.2/` | Frozen snapshot |

- Keep the latest set at an unversioned URL so existing links and rankings don't move. Don't use `/docs/2025.1/` as the primary path.
- Order the dropdown newest first, default to latest, and tag the older ones with a banner on every page: "You're viewing docs for release 2024.1. The API is always served at the latest release (2025.1). [View this page in the latest docs]".
- Make the banner link to the same page in latest, not the docs home.

**Canonical tags on the older sets**

- Each older page gets `<link rel="canonical" href="https://<docs-host>/docs/<same-path>">` pointing at its equivalent page in the latest set. For example, `/docs/2024.1/webhooks/retries` canonicalizes to `/docs/webhooks/retries`.
- This works cleanly because nothing was removed: every page in an older set has a counterpart in latest. The reverse isn't true, since newer pages have no older counterpart, so don't generate canonicals for those.
- Latest pages are self-canonical. The older sets must not self-canonical, or you recreate the duplicate-content split.
- A canonical is only a hint to search engines. To get the older sets out of results more reliably, also add `<meta name="robots" content="noindex, follow">` to them and list only latest URLs in `sitemap.xml`. Don't combine `noindex` with a canonical that points somewhere contradictory, and check how your platform emits each. Some hosted platforms set canonicals automatically for versioned docs, so verify the rendered HTML before relying on it.
- Add the same canonical logic to any `llms.txt` or AI-facing index: list only the latest set.
- Verify after launch by fetching a few older URLs and checking the rendered `<head>`. Then watch Search Console for "Duplicate, Google chose different canonical" over the first few weeks.

If the PM still wants the dropdown after weighing the trade-offs, the first step is to limit it to those four frozen snapshots plus a latest banner. Confirm with the platform vendor how it generates canonicals and sitemaps before you publish.