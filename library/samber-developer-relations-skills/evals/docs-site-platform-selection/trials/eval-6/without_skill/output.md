# Docs platform recommendation: Halvane Robotics

## Recommendation

**Build on Next.js, but not a custom docs app.** Use an existing Next.js docs framework inside your own repo and design system. My pick is **Fumadocs**, with **Nextra** as the alternative. Both are MDX-based and give you routing, sidebar, search, versioning hooks, and a code-block UI out of the box. Your 3 web devs spend their weeks on the three things that make the docs yours:

1. **Theming:** reuse the marketing site's design tokens and components.
2. **Portal SSO:** one auth integration.
3. **Doxygen pipeline:** C++ reference generation.

This gives the CTO what they asked for (Next.js, a pixel-match with the marketing site, portal login) without the 10-week risk of writing navigation, search, MDX rendering, versioning, and a C++ reference renderer from scratch.

I did not verify current framework versions, features, or pricing. Run the week-1 spike below before committing.

## Why not a fully custom app

- **The schedule is tight.** About 150 pages, 10 weeks, and 2 writers who must also finish content. Every week the web team spends on docs chrome is a week not spent on the parts that differ from a standard docs site.
- **The Doxygen reference is the hard part.** Doxygen output is a large, link-dense C++ tree: namespaces, classes, overloads, templates. It is not a few pages of markdown. Budget the web team's time here, not on a sidebar.
- **You would own the maintenance.** A custom app means you own search, accessibility, mobile nav, versioning, and redirects after launch, with 3 devs who also have the marketing site and portal.

## Why not a hosted platform (Mintlify, ReadMe, GitBook)

They are the fastest path to launch. They fall short on your two stated requirements:

- **"Matches the marketing site exactly"** is limited by their theming.
- **"Plugs into our customer portal login"** is usually paid-tier and constrained to the protocols they support.

If the answer to both questions below turns out to be "no", a hosted platform becomes the better choice. See the decision gate.

## Architecture

| Concern | Approach |
|---|---|
| Framework | Fumadocs (or Nextra) in a Next.js app, in the same monorepo as the marketing site if one exists |
| Look and feel | Share the marketing site's design tokens and component package. Don't re-skin by copying CSS |
| Content | MDX in git. Writers use PRs with preview deployments |
| SDK guides | Hand-written MDX, owned by the 2 writers |
| C++ API reference | Doxygen XML, converted to MDX in CI (see below) |
| Search | Start with the framework's built-in search. Move to Algolia DocSearch or similar only if quality is poor |
| Auth | Next.js middleware validating the portal session via OIDC or shared-session cookie. Details below |
| Hosting | Wherever the marketing site runs, with preview builds per PR |

### Doxygen strategy: two tiers

1. **Launch-safe fallback (week 2).** Run Doxygen to HTML, restyle with a CSS theme, and serve it under `/api/`. This gives full reference coverage early, but the look and navigation won't match the rest of the site.
2. **Target (weeks 3-8).** Generate Doxygen XML, then convert it to MDX pages with a script or an existing converter, so the reference shares the site's nav, search, and styling. Evaluate existing converters in the spike before writing your own.

If tier 2 slips, ship tier 1 at launch and migrate after. That is the main schedule protection in this plan.

### Auth: decide what actually needs gating

Putting everything behind login hurts search-engine discovery, AI-assistant retrieval, and prospect evaluation. This is the one place I'd push back on the CTO's framing. My suggestion:

- **Public:** quickstarts, concepts, most SDK guides, and the API reference.
- **Gated (portal login):** only content that is customer-only, such as downloads, licensed or beta SDK material, and private release notes.

This also shrinks the auth surface and the launch risk. The integration itself is small if the portal speaks OIDC/OAuth. It becomes a larger task if the portal uses a proprietary session, so check that first.

## 10-week plan

| Weeks | Work | Owner |
|---|---|---|
| 1 | **Spike and decision gate** (see below). Inventory the 150 pages, tag each public or gated, and pick the framework | 1 dev, 1 writer |
| 2 | Skeleton app, theming from the marketing site, CI and preview deploys. Doxygen HTML fallback live on staging | 2 devs |
| 3-4 | Portal SSO behind middleware. Doxygen XML to MDX pipeline prototype. Content migration starts | 1 dev auth, 1 dev Doxygen, writers migrate |
| 5-7 | Reference pipeline hardened (overloads, templates, cross-links). Search tuned. Redirects. Writers finish content | devs and writers |
| 8 | Content freeze. Accessibility, mobile, performance, broken-link and SEO checks | all |
| 9 | Load test, auth edge cases (expired session, deep links after login), staging review with the CTO and support | all |
| 10 | Launch buffer. No new features | all |

Weeks 9-10 are deliberately left as slack. Do not plan work into them.

## Decision gate (end of week 1)

Answer these before committing. They decide between this plan and a hosted platform:

1. **What protocol does the customer portal login use?** OIDC/OAuth means the integration is small. A proprietary session means add 1-2 weeks.
2. **Does the marketing site already use Next.js and a shared component library?** If yes, "match exactly" is cheap. If no, it is a real cost.
3. **How much of the content must be gated?** If most is public, the auth requirement is minor.
4. **Does the Doxygen XML to MDX spike produce acceptable output for your three messiest headers?** If not, ship tier 1 (styled HTML) at launch.
5. **Do you need versioned docs (several SDK versions live) at launch?** If yes, confirm the framework's versioning approach in the spike.

**Fall back to a hosted platform** if (1) is proprietary, (2) is no, and the web team can't commit 3 devs at roughly half time. In that case you trade exact visual match for a launch you can trust.

## Risks

| Risk | Mitigation |
|---|---|
| Doxygen conversion eats the schedule | Tier 1 fallback shipped at launch, tier 2 after |
| Web team is pulled onto marketing or portal work | Get written capacity commitment from the web lead in week 1 |
| Writers blocked on tooling | Preview deploys per PR from week 2. Writers write MDX in git, with a short authoring guide |
| Auth edge cases (deep links, expiry) found late | Test them in week 9 at the latest, and build the happy path in week 3-4 |
| Scope creep ("while we're at it" features) | Freeze scope at week 1. Anything beyond nav, search, SSO, and reference goes to a post-launch backlog |
| Gating hurts discoverability | Gate by content tag, not by site |

## Next steps

1. Confirm the five gate questions with the CTO and web lead this week.
2. Get the web team's weekly capacity in writing.
3. Run the week-1 spike on the three messiest C++ headers, and on one SSO round trip against staging.
4. Come back with the go/no-go and a decision on Fumadocs vs. Nextra.

## What I assumed

You didn't tell me, so I assumed:

- The marketing site is probably Next.js.
- The portal supports a standard auth protocol.
- Most docs can be public.
- No multi-version docs are needed at launch.

If any of these is wrong, the plan changes. The decision gate is built to catch that in week 1.