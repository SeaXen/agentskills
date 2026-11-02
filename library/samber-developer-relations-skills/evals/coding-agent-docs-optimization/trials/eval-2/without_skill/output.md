Here's the draft, plus the two things that determine whether it actually works.

## `/llms.txt` for docs.brightloom.com

```markdown
# Brightloom

> Brightloom is a product-analytics SDK. Teams use it to instrument web, mobile,
> and server applications, track user and product events, and query that data
> through dashboards or a REST API.

Docs cover SDK installation per platform, the event/identity data model, and the
HTTP API for sending and querying data. Full documentation is HTML-rendered at
docs.brightloom.com; this file indexes the pages most useful for understanding
and integrating the product.

## Getting Started

- [Quickstart](https://docs.brightloom.com/getting-started/quickstart): Install an SDK and send your first event in under 10 minutes.
- [How Brightloom Works](https://docs.brightloom.com/getting-started/concepts-overview): Events, properties, users, and the data pipeline, in one page.
- [Choosing an SDK](https://docs.brightloom.com/getting-started/choosing-an-sdk): Which SDK to use for web, mobile, or server-side tracking.

## SDKs

- [JavaScript / Web SDK](https://docs.brightloom.com/sdks/javascript): Browser install, autocapture, and manual event tracking.
- [iOS SDK](https://docs.brightloom.com/sdks/ios): Swift/Objective-C install and lifecycle event tracking.
- [Android SDK](https://docs.brightloom.com/sdks/android): Kotlin/Java install and lifecycle event tracking.
- [React Native SDK](https://docs.brightloom.com/sdks/react-native): Cross-platform mobile install.
- [Node.js Server SDK](https://docs.brightloom.com/sdks/node): Server-side tracking and batching.
- [Python Server SDK](https://docs.brightloom.com/sdks/python): Server-side tracking and batching.

## Core Concepts

- [Events and Properties](https://docs.brightloom.com/concepts/events): Event naming, property types, and payload limits.
- [User Identity](https://docs.brightloom.com/concepts/identity): `identify`, anonymous-to-known merge, and alias resolution.
- [Groups and Accounts](https://docs.brightloom.com/concepts/groups): B2B account-level analytics.
- [Data Governance and PII](https://docs.brightloom.com/concepts/data-governance): What not to send, redaction, and retention controls.

## Guides

- [Funnels](https://docs.brightloom.com/guides/funnels): Building conversion funnels from raw events.
- [Retention Analysis](https://docs.brightloom.com/guides/retention): Cohort retention setup and interpretation.
- [Warehouse Sync](https://docs.brightloom.com/guides/warehouse-sync): Exporting to Snowflake and BigQuery.
- [Migrating from Segment](https://docs.brightloom.com/guides/migrate-from-segment): Mapping Segment's spec to Brightloom's event model.

## API Reference

- [REST API Overview](https://docs.brightloom.com/api/overview): Auth, rate limits, and base URLs.
- [OpenAPI Specification](https://docs.brightloom.com/openapi.json): Machine-readable API schema. Note: some operation descriptions are currently empty — see caveat below.
- [Query API](https://docs.brightloom.com/api/query): Pulling aggregated event data programmatically.

## Optional

- [Changelog](https://docs.brightloom.com/changelog): Recent SDK and API changes.
- [Status Page](https://status.brightloom.com): Uptime and incident history.
- [Integrations Directory](https://docs.brightloom.com/integrations): Slack, Zapier, and webhook destinations.
```

## Two things before this ships

**1. Every URL above is a placeholder guess at your site's structure, not a crawl result** — I don't have live access to docs.brightloom.com from here. Someone needs to swap in real slugs/titles from the actual nav before this goes live. Fastest way to do that without touching all 340 pages: pull the sitemap.xml, filter to the ~30-40 pages that map to the sections above (getting-started, one page per SDK, core concepts, top 3-4 guides, API overview), and skip the long tail — llms.txt is a curated index, not a full-site dump, so 340 pages was never the target link count.

**2. "No markdown versions" doesn't block this.** llms.txt just needs URLs and one-line descriptions — it's fine for those links to point at your existing HTML pages; most LLM clients can fetch and parse HTML directly. Don't burn this week's timeline converting 340 pages to markdown to satisfy a spec that doesn't require it. If you want the upgrade later, the incremental move is Markdown content-negotiation (serve `.md` on `Accept: text/markdown` for the ~30 pages actually linked here) rather than a full static export.

One real blocker, easy to miss: **check robots.txt allows GPTBot, ClaudeBot, PerplexityBot, and Google-Extended.** If any are disallowed, an llms.txt is decorative — those crawlers can read the index but can't follow through to the pages it points at.

On the OpenAPI file: don't fix all ~170 empty descriptions this week. The API Reference entry above already flags the caveat inline so an LLM consuming it isn't misled into treating gaps as "no description exists" vs. "this endpoint does something undocumented." Fast-follow: backfill descriptions for whichever 10-15 endpoints get hit hardest by API-key traffic — that's where a tool-calling agent choosing between your endpoints actually needs the description to disambiguate.