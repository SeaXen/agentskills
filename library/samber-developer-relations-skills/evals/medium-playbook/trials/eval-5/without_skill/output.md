# Lattice Engineering on Medium: what to fix before the three steps

Yes, there are fixes. I didn't browse anything, so the Medium and Towards Data Science (TDS) details below come from memory. Medium and TDS policies changed several times in 2023–2025. Confirm each ⚠️ item on the live help page before you act on it.

## Fixes, most important first

### 1. Boost Nomination Program ❌ probably doesn't fit as stated
- Boost is a story-level distribution boost. As I understand it, a story must be paywalled in the Medium Partner Program (MPP) to qualify.
- MPP enrollment is per individual writer. A publication or a brand account can't earn or enroll, and the nominator must be a Medium member in good standing.
- **Fix:** have the editor apply as a person, from their own Medium account, and confirm the exact eligibility on Medium's current Boost page. Don't apply from the brand account.
- **Check the fit:** paywalled stories reach only people who read behind the paywall. That works against a goal of free, linkable brand content, so decide which posts are worth that trade-off.
- **Don't build the plan around Boost.** Nominations are curated and not guaranteed, and you can't promise anyone a result.

### 2. Towards Data Science ⚠️ the premise may be outdated, and the content fit is poor
- As I remember it, TDS left Medium in 2025 and now takes submissions through its own site and form. Check the current process before you send anything.
- TDS has historically rejected promotional, vendor-pitch content. A piece from a data-catalog startup about data catalogs is the profile most likely to be rejected.
- **Fix:** submit a vendor-neutral technical piece instead. Good topics are lineage, metadata quality, or an engineering lesson. Keep product mentions to a bio line, and disclose your affiliation.
- Don't use your "best piece" if it's a product pitch. Keep that one on your own publication.
- If TDS requires unpublished work, don't publish the piece on Lattice Engineering first. If it allows republication, set the canonical link, and ask them which to use.

### 3. `eng.lattice.io` pointed at the publication ❌ likely blocked
- ⚠️ As far as I know, Medium stopped setting up new custom domains for publications around 2023. Existing ones were grandfathered.
- If that's still true, you can't do this step at all. Check Medium's help page on custom domains before you touch DNS.
- **If it's blocked:** use the `medium.com/lattice-engineering` URL, or the `lattice-engineering.medium.com` subdomain. Put the writing on `eng.lattice.io` itself (Ghost, Astro, or similar) and cross-post to Medium with the canonical link pointing at your own domain.
- **Why this matters:** a Medium-hosted domain builds Medium's SEO, not yours. If search traffic matters to marketing, an owned domain is the better home.

### 4. Google Analytics ⚠️ weak on Medium
- Medium's GA support was historically tied to Universal Analytics and to custom domains. Universal Analytics is shut down. I'm not sure GA4 is supported.
- **Fix:** check that the publication settings still offer a Google Analytics field and accept a GA4 `G-` ID. If they don't, use these instead:
  - Medium's built-in stats.
  - UTM-tagged links from each post to lattice.io, tracked in your own analytics.
  - A canonical blog on your own domain, where GA works normally.
- Tell marketing what the measurement will actually cover (views and reads, not full-funnel tracking) before they build dashboards around it.

### 5. Ownership and account hygiene (no paid plan)
- Make sure the owner is a real account with a named human behind it. Add 2FA to it, and keep recovery access in your password manager. Losing the brand login means losing the publication.
- Add a second admin or editor now, so the publication doesn't depend on one login.
- A publication needs no paid plan to publish. The paid piece is individual membership, which gates Boost and MPP eligibility for the people involved.

## Suggested order
1. Check the custom-domain and GA help pages. This decides whether step 3 exists. ⏳ 15 minutes.
2. Decide where the canonical home lives: Medium, or your own domain with Medium as a mirror.
3. Pick a vendor-neutral piece for TDS and confirm their current submission path.
4. Have the editor apply to Boost as an individual, only if you're willing to paywall stories.

I can draft the TDS pitch or the cross-posting and canonical setup next, if you want either.