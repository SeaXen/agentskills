Two of three moves break this skill's own naming rules. Fix before ship.

## 1. Mass case rename (~140 events) — flag, don't skip

Skill rule: "Renaming shipped event splits its history in two."

Casing isn't mandated by source framework (Segment Object-Action). Segment allows Proper Case for events, only requires consistency. Your current Proper Case scheme already IS consistent — so per skill's own rule ("match existing plan's casing instead of converting it"), no mechanics reason forces this change.

Cost: every dashboard/chart keyed by event name breaks same day, across all ~140 events at once.

Fix:
1. Bump plan version (e.g. v1.0 → v2.0).
2. Log rename in "Known gaps" / changelog with cutover date.
3. Warn every dashboard owner before cutover.
4. Consider emitting old + new name in parallel one reporting period, instead of hard cutover.

## 2. 'Python Quickstart Step 3 Done' → 'quickstart_step_3_completed' — still bad

Skill lists `python_quickstart_step_3_done` verbatim as its canonical bad-name example. Prescribed fix in same skill's worked example: event `quickstart_step_completed`, with properties `step_number` (int), `step_name` (enum), `language` (enum).

Your rename drops "python" — good. Keeps "3" baked into name — still bad. Step 4 becomes a 5th event name; nobody can query "all step completions" without enumerating names.

Fix: rename to `quickstart_step_completed`. Move `3` into `step_number` property. Move language into `language` property.

## 3. Split 'Docs Page Viewed' into 3 events — also bad

`reference_page_viewed` is listed verbatim in skill as bad-example name.

Rules broken: "Put context in properties, never in name." / "Emit same event name for same intent across surfaces, let a `surface` property carry difference."

Same skill's worked example already solves this exact case: single event `docs_page_viewed`, `section` property carries the distinction.

3 events = same intent (page view), different content type. Content type belongs in property. Splitting doesn't buy query power a property doesn't already give — filtering by property value does the same job. It does cost: grows already-large 140-event list further, against skill's "fits on one screen" guardrail.

Fix: keep `docs_page_viewed`. Add/reuse property `content_type`, closed list `reference` / `guide` / `blog`, entered in property registry.

## What's fine

Past tense convention: OK. "Done" → "completed" wording choice: fine either way, house style not mandated.

Next: apply fixes in points 2 and 3 to event table, decide rename-versioning plan for point 1. Want draft of the corrected event rows?