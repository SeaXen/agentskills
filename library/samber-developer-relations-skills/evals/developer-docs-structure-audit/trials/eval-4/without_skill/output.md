## Verdict

Diátaxis (Tutorials / How-to / Reference / Explanation) is the right target shape — it's proven for CI/CD-style dev-tool docs (Kubernetes, Django, Ansible all use it). The problem isn't the destination. It's the sequencing, and "downtime" is the wrong mental model for what's actually being risked.

## What breaks with this plan as written

**1. Sidebar-first, content-later inverts the risk.**
Wiring four new top-level sections into nav next sprint, before the 90 pages are sorted, means real users hit empty or half-stocked sections for most of Q3. Fix: cut over section-by-section as each bucket fills, not all four at once up front. Keep the old sidebar live until a section has real content behind it.

**2. Nobody mentioned redirects — this is the actual landmine, not "downtime."**
Reorganizing into four new sections almost certainly changes URLs. Every changed URL needs a 301 to its new home or you lose backlink equity, break external links (support tickets, blog posts, Stack Overflow answers pointing at old paths), and give Google 90 pages of ranking volatility at once. "Downtime" implies the docs go dark; what actually happens is the docs stay live and indexed while structurally inconsistent — worse for SEO than an outage, because nothing signals "temporary" to a crawler.
→ Build the full old-URL → new-URL map as a first deliverable, before any page moves. Maintain it continuously, not as a Q3-end cleanup task.

**3. Big-bang migration puts all the risk at the finish line.**
"Move all 90, rewrite whatever doesn't fit" over one quarter, then flip, is one giant unvalidated batch. If something's wrong (broken links, orphaned pages, traffic drop), you find out in week 12, not week 2.
→ Batch by product area or by traffic tier. Ship one batch, watch Search Console/analytics for a week, then move the next. Small blast radius per step, matches your own refactor-blast-radius instinct for code — apply it to docs too.

**4. Prioritize by traffic, not by alphabetical convenience.**
Not all 90 pages carry equal weight. Pull top landing pages from Search Console/Ahrefs first. Migrate and rewrite the highest-traffic 20% first and carefully — that's where a mistake costs the most. Low-traffic long-tail pages can wait, or get merged/archived instead of dutifully sorted.

**5. Diátaxis doesn't have a bucket for everything — decide the leftovers now, not mid-Q3.**
Changelog, troubleshooting/FAQ, migration guides, integrations list — these don't map cleanly onto Tutorials/How-to/Reference/Explanation. If "whatever doesn't fit gets rewritten" is the fallback for all of these, that's undefined scope hiding inside a defined-sounding plan. Name the fifth/sixth bucket (or decide they nest under one of the four) before sidebar wiring, so you're not relitigating it page-by-page for a quarter.

**6. Set a baseline before touching anything.**
Snapshot organic traffic, top landing pages, and Search Console impressions/clicks now. Check weekly during Q3. Catching a regression in week 3 is a fix; catching it in week 13 is a post-mortem.

## Net

Target IA: keep it. Rollout: replace "wire sidebar next sprint, migrate all quarter" with "map redirects first → cut over one section at a time as it fills → old nav stays live for unmigrated sections → watch traffic weekly." Same destination, same quarter, most of the risk removed. The CEO signed off on "a quarter of disruption" — make sure that's actually what they're getting, not three months of silently degrading SEO with no rollback point until the end.