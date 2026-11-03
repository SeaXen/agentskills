# Next.js dual-deploy vs static-spa-library-site — decision matrix

Both skills help you ship a self-hosted web UI to Docker + Vercel. They differ on whether you need React server-side rendering. Pick the right one based on the user's actual requirement.

## Quick rule

- **User wants React components, hooks, server actions, or any Next.js-specific feature** → `nextjs-dual-deploy`
- **User wants a static HTML/CSS/JS site with no React runtime** → `static-spa-library-site`
- **User is ambiguous** → default to `nextjs-dual-deploy` if the data is dynamic (trades, status, ops metrics). Use `static-spa-library-site` only if all content is known at build time and never changes without a redeploy.

## Side-by-side comparison

| Dimension                    | `nextjs-dual-deploy`                                  | `static-spa-library-site`                            |
|------------------------------|-------------------------------------------------------|------------------------------------------------------|
| Runtime                      | Node.js server (Next.js standalone) + nginx optional  | nginx only (static HTML/CSS/JS)                      |
| Docker image size            | ~150-300 MB (Alpine + standalone)                     | ~30-50 MB (nginx:alpine)                             |
| Cold start                   | 1-3 seconds                                           | <100 ms                                              |
| Server-side rendering        | Yes (App Router Server Components)                    | No — all rendering is client-side JS or pre-rendered HTML |
| API routes                   | Yes (`app/api/*/route.ts`)                            | No — would need a separate backend                   |
| Forms with server actions    | Yes                                                   | No — must POST to external backend                   |
| Database integration         | Easy — `lib/data.ts` + Prisma/Drizzle/SQLite           | Harder — needs separate API server                   |
| Auth (NextAuth, sessions)    | First-class                                           | External service required                            |
| Hot reload during dev        | Yes (`next dev`)                                      | No — pure HTML, edit and refresh                     |
| Vercel deploy                | Zero-config (Next.js preset auto-detected)            | Zero-config (static preset auto-detected)            |
| Build time for ~50 pages     | ~30-90s                                               | ~5-15s (Python static generator)                     |
| Live data refresh            | Server-side polling, Server Actions, RSC              | Client-side fetch from external API                  |

## When the user says X, do Y

| User phrase                                              | Skill                | Why                                                 |
|----------------------------------------------------------|----------------------|-----------------------------------------------------|
| "Make me a Next.js app"                                  | `nextjs-dual-deploy` | Explicit library choice                             |
| "Make me a React app"                                    | `nextjs-dual-deploy` | React implies JSX runtime, server-side possible    |
| "Trading journal with live data"                         | `nextjs-dual-deploy` | Live data + forms (trade entry)                      |
| "Status page showing service health"                     | `nextjs-dual-deploy` | May need API routes + auto-refresh logic            |
| "Admin panel for user management"                        | `nextjs-dual-deploy` | Auth + DB integration required                      |
| "Static website for my docs"                             | `static-spa-library-site` | No server logic, just browse                      |
| "Landing page for my product"                            | `static-spa-library-site` | No app logic                                     |
| "Personal blog / portfolio"                              | `static-spa-library-site` | No auth, no forms                               |
| "Site that mirrors this Notion page"                     | `static-spa-library-site` | Read-only content                               |
| "Dark dashboard like the screenshot"                     | Either — see below   | Depends on whether data is dynamic                   |

## Edge cases

### "Dark dashboard like the screenshot" with no live data

If the dashboard is purely a static visualization (e.g. a one-time report, a fixed dataset the user has), `static-spa-library-site` works and ships smaller. The Tradingx example is **not** static — it has a calendar that updates, trade entries, daily reviews — so `nextjs-dual-deploy` was correct.

When in doubt, ask the user: "Will the data change over time, or is this a one-time view?"

### "I want to deploy to Vercel and Docker"

Both skills handle this. `nextjs-dual-deploy` requires Vercel to detect Next.js (auto-works). `static-spa-library-site` requires Vercel to detect static files (auto-works). For both, no `vercel.json` is strictly required for the default deployment.

### "Can I use Next.js for a static site?"

Yes — you can `output: "export"` to produce static HTML, but then you lose API routes and server actions. If you don't need those, `static-spa-library-site` is simpler (no node_modules, faster builds, smaller image). If you might add auth or API routes later, start with `nextjs-dual-deploy` and add `output: "export"` only if the user explicitly wants static export.

### Migrating from one to the other

- `static-spa-library-site` → `nextjs-dual-deploy`: rewrite pages as React Server Components, add `app/api/*/route.ts` for any backend logic, rebuild Dockerfile.
- `nextjs-dual-deploy` → `static-spa-library-site`: replace Client Components with vanilla JS, remove `app/api/*/route.ts`, switch to a Python static generator. Most dynamic features require rewriting.

For most users, pick one and stay with it. Migration is real work.

## TL;DR

- **Tradingx, monitoring tools, ops dashboards, anything with live data, forms, or auth → `nextjs-dual-deploy`**.
- **Marketing sites, docs, portfolios, content libraries → `static-spa-library-site`**.

If you're still unsure, default to `nextjs-dual-deploy` — it's slightly more overhead but supports everything `static-spa-library-site` does and more.