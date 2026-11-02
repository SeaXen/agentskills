**First move: write activation event spec yourself this week. Borrow engineering days only after spec done. Eng implements, never designs.**

Big picture: clean Amplitude = hardest part already owned. Spend both days inside Amplitude: add activation events, then program identity. No new tool, no warehouse, no CRM fight.

## Order

**1. Activation funnel events — day 1, ~6 hours eng.**
"Hello world" for pipeline product = first successful pipeline run. Emit server-side:
- `quickstart_started`
- `connector_configured` (properties: connector id, method: UI or CLI or IaC)
- `pipeline_created`
- `pipeline_run_succeeded` (property: `first_run` boolean)
- `pipeline_run_failed` (property: error class)

Add entry source property on each: referrer, campaign.
North-star readout: time to first pipeline — signup to first successful run, median plus distribution.
Why first: missed events stay missed forever. Properties backfill later; events never. Every later question needs activated users as denominator.
Keep it clean: snake_case names, enum properties, spec reviewed before eng writes code.

**2. Program identity — day 2 morning, ~3 hours eng.**
Sync program roster into Amplitude:
- user properties: `dev_program_member`, `program_tier`, `program_joined_at`
- group analytics: workspace as account group, if absent

Why second: this = CRM substitute. Makes "members vs non-members: activation rate, day 30 retention, workspace size" one saved chart. Sales ops not involved.

**3. Docs snippet — day 2 afternoon, ~1 hour.**
Docs site lacks analytics? Drop existing Amplitude snippet in. Three signals only: quickstart views, code-copy clicks, search terms. Zero-result searches = content gaps. Docs = top of funnel for pipeline product: many evaluators never sign up.

**4. Free signals — parallel, zero eng.**
Native platform stats, weekly snapshot into one sheet:
- GitHub: traffic API clones and visitors, stars, issues, contributors
- Slack or Discord: members, weekly active, joins

Never build integrations here. Manual snapshot wins.

**5. One dashboard folder — then stop, ~1 hour.**
Five charts: time-to-first-pipeline distribution, funnel by step, activation by entry point, member vs non-member retention, failure error mix.

Total: ~1.5 days eng. Half day margin for QA plus property fixes.

## Why this order

- Events before properties: backfill asymmetry.
- Activation before community or content stats: activation = moment of value. Series B program justification = "members activate and retain better". Steps 1 + 2 prove or kill that claim.
- Free signals never compete for engineering days.

## Not yet

- Anything touching CRM. Blocked, and re-asking burns trust. Park it.
- New tooling: warehouse, reverse ETL, attribution, survey platform. Two days cannot buy them.
- Deep content analytics, social listening, email events. Marketing automation owns those.

## CRM closure workaround

- Define PQL inside Amplitude: workspace with one successful pipeline, two plus members, on-schedule runs two plus weeks.
- Hand sales monthly CSV export of PQL accounts. No CRM field touched.
- Revisit sales ops next quarter with conversion evidence, not access request.

## Quarter-end readout

Two numbers tell leadership whole program story:
1. Median time to first pipeline, plus biggest drop-off step.
2. Members vs non-members: activation rate, day 30 retention.

Whatever those show picks instrument six next quarter. Data picks order, not blueprint.

Next: open spec doc, write one line — event `pipeline_run_succeeded`, property `first_run: boolean`.