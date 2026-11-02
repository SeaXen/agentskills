## Sanity check: tracking plan rename (140 events → snake_case)

**Direction is right.** snake_case matches the object-action convention (`event_name` lowercase, underscores, no spaces) and is what every downstream tool (GA4, Mixpanel, Amplitude, Segment, SQL) expects natively — Proper Case with spaces is a known source of silent query mismatches. Two things in the plan need attention before you touch 140 events.

### 1. The "Docs Page Viewed" split works against your own goal

Splitting into `reference_page_viewed` / `guide_page_viewed` / `blog_page_viewed` violates object-action naming: content-type is *context*, and context belongs in a property, not baked into the event name. Concretely this costs you:

- **No easy "any docs page" rollup.** Every dashboard that currently answers "how many docs views total" now needs `event IN (three names)` instead of `event = 'docs_page_viewed'`.
- **Net +2 events**, not a rename — your "140 events → 140 renamed" framing quietly becomes 141, which matters for anyone reconciling the old and new plans.
- **New failure mode**: three names to keep mutually exclusive and exhaustive. Any docs page that isn't cleanly "reference/guide/blog" (landing page, changelog, FAQ) now needs a decision, where today it didn't.

Better: keep one event, `docs_page_viewed`, add a `doc_type: reference|guide|blog` property. You get per-type querying (filter on the property) *and* the total, for free, and it stays consistent with however the other ~138 events are structured.

If there's a reason to hard-split anyway (e.g., different teams each own a dashboard and want event-level ACLs, or your tool doesn't do fast property filtering), that's a legitimate call — just make it deliberately, not as a side effect of the case-cleanup.

### 2. Check whether "Python Quickstart Step 3 Done" has siblings before dropping "Python"

If there's only one quickstart, `quickstart_step_3_completed` is fine. If there's a JS/Go/Ruby quickstart family too (`JS Quickstart Step 3 Done`, etc.), collapsing them all to `quickstart_step_N_completed` loses the language dimension from the event name — you'd need a `language` property to avoid merging what were previously distinguishable funnels. I didn't look at your actual event list, so this is a check for you: grep the full 140 for `Quickstart` and confirm the plan accounts for every variant, not just the Python one you quoted.

### 3. The bigger risk isn't the naming — it's the cutover

Renaming 140 live production events in place, all at once, breaks things that don't show up until after ship:

- **Trend continuity.** Every dashboard/funnel spanning the cutover date shows a cliff (old name stops, new name starts) unless you either double-emit both names for a transition window, or add a name-mapping layer in the warehouse (view/CTE) rather than relying on the raw event stream to be continuous.
- **Hidden consumers.** Saved reports, alerts, funnels, and any typed event-name enum in frontend/backend code reference the literal old string. A partial deploy (server renamed, client not, or vice versa) silently drops events under the old name while dashboards still query for it. Audit consumers first, not just emitters.
- **QA at this scale needs a diff, not a skim.** Produce an old-name → new-name mapping table (you'll want it anyway for historical joins/backfills), and verify each new event actually fires in debug view — eyeballing 140 renames in code review will miss typos (`competed` vs `completed`).
- **Phase it if you can.** A hard cutover of 140 events in one release is a lot of simultaneous blast radius for something that's purely cosmetic (no new data being captured). Consider batching by domain (docs events, quickstart events, ...) so a bad rename in one batch doesn't take down every dashboard at once.

**Net:** case conversion — ship it. The `quickstart_step_3_completed` rename — ship it, but confirm no sibling-language events get silently merged. The `docs_page_viewed` split — reconsider as a property instead of three events, unless you have a specific reason for hard separation. And treat this as a migration with a mapping table and consumer audit, not a bulk find-replace.