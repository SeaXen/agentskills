# Northwind Telemetry: DITA → Diataxis Migration Audit

## Headline finding
Bulk rename won't work. Concept→explanation, task→how-to, reference→reference: mostly mechanical, fast. Tutorial quadrant: empty. Nothing in corpus built as tutorial. That's root cause of support complaint — new customers dropped into task topics, because DITA never had axis for "content built for learner" vs "content built for competent user solving one goal." Diataxis splits exactly on that axis. DITA type system doesn't.

## Why relabel alone fails
DITA's 3 canonical types (concept/task/reference) sort content by shape: background knowledge, procedure, or lookup data. Diataxis 4 modes sort by 2 axes: study vs work, acquisition vs application. Reference and explanation map onto that pair fine. Tutorial and how-to are the split DITA never made — both look like procedures (numbered steps), but tutorial means learner, guaranteed success, single path, narrated, no branching. How-to means competent user, assumes context, may branch, skips explaining why.

Task topics in DITA get written modular, reusable, context-free (DITA minimalism, enables conref/keyref reuse across ditamaps). Tutorials need opposite: single linear non-reusable narrative, dependent step-to-step. Structural conflict, not metadata gap. Rewriting, not retagging, required for tutorial quadrant.

## Mapping rubric, per DITA type

**reference → reference.** Near 1:1. Flag exceptions: any reference topic with embedded "why this matters"/"when to use" prose. Diataxis reference stays austere — split explanatory prose into explanation topic, keep reference topic pure lookup (params, tables, error codes, limits).

**concept → explanation (majority) + tutorial seed (minority) + reference seed (rare).**
- Pure background/architecture/"how it works" topics: explanation, as-is or light edit.
- Topics titled "Overview of X," "Introduction to X," "Getting started with X": don't default to explanation. Check if written as onboarding narrative — if yes, tutorial seed material, needs rewrite.
- Topics with embedded step-like content (numbered list buried inside concept, common DITA hygiene failure): split. Extract steps into proper task/how-to, leave rest as explanation.
- Topics that are disguised glossary/definition lists: reclassify reference.

**task → how-to (majority) + tutorial (minority, needs rewrite, not retag).**
- Task assumes user knows product, solves one goal, has prereq/context pointing elsewhere: how-to. Light edit — strip embedded "why," push to linked explanation topic.
- Task is first-run/setup/"day one" content for user who's never touched product: tutorial candidate. Don't retype — rewrite. Remove branching/options, remove troubleshooting asides, narrate single guaranteed path, state outcome up front.

## Triage method — scale to 1,400 topics
Don't read all 1,400 by hand. Query corpus first, sample-review second.

Signals to query (Oxygen/Saxon/XPath over ditamap + topic prolog):
1. DITA type attribute — already have it, free.
2. Title regex: `^(Introduction to|Overview of|Getting started|Your first|Quickstart|Welcome to)` — onboarding candidates.
3. Map location: topics under existing "Getting Started"/"Quick Start" TOC branch — strong tutorial signal regardless of DITA type.
4. Audience metadata = "novice"/"new" — tutorial signal.
5. Step count + `<choice>`/optional steps inside `<task>` — high branching means how-to, not tutorial.
6. conref/keyref inbound count per topic — high reuse means keep as reusable how-to/reference, don't force into linear tutorial (breaks reuse).
7. `<conbody>` containing `<ol>`-shaped step content — hygiene-failure flag, needs split.

Bucket results: clean-map (auto), needs-split (human), needs-rewrite (human), tutorial-candidate (human, priority). Human-review only buckets 2–4.

## Estimated shape (directional — confirm with triage query, not final)
Typical mature DITA corpus this size:
- reference: 90%+ auto-maps clean.
- concept: 70–80% clean to explanation, 15–20% need split, 5% tutorial seeds.
- task: 85–90% map to how-to with edit, 10–15% tutorial candidates.

Net: expect 2–5% of corpus (~30–70 topics) as raw material for tutorial quadrant, near-zero usable without rewrite. Give VP this number early — it's the resourcing conversation, not just the audit conclusion.

## Onboarding gap: root cause + fix
Support complaint is direct symptom of missing tutorial quadrant. New customer sees only task topics (assumes competence) and concept topics (assumes patience for background reading). No guaranteed-success guided path exists structurally.

1. Pick one onboarding outcome: "new customer does X successfully in one sitting." One, not five, first pass.
2. Draft tutorial as new document. Single narrative, one path, no options, explicit checkpoint each step. Pull facts from existing task/concept topics — don't reuse the topics themselves.
3. Keep it short. One working tutorial beats five half-built.
4. Place as first link in new nav, top of Tutorials quadrant, before reference/how-to/explanation.
5. Expand to 3–5 flagship tutorials over the year, prioritized by support ticket volume per feature area — not by ease of authoring.

## DITA mechanics — protect reuse
1,400 topics, rigorous typing → strong conref/keyref reuse near-certain. Diataxis reorg stays navigational first pass, not physical.

1. Add `<data name="diataxis-mode" value="tutorial|how-to|reference|explanation"/>` to topic prolog. Script-populate from triage buckets. Reversible, scriptable, leaves DITA type attribute untouched.
2. Build 4 new ditamaps (tutorials/how-to/reference/explanation) using `<mapref>`/`<topicref>` pointed at existing topics by diataxis-mode metadata. Topics stay physically where they are.
3. Never fork or duplicate a conref'd/keyref'd topic just to fit one quadrant. Reused topic stays single source, gets referenced from whichever map(s) fit. Physical content splitting only for confirmed hybrids (concept with embedded steps) — real content surgery, not reorg.
4. After metadata + new maps validate on a pilot (few weeks, one feature area): consider physical file/folder reorg for Oxygen project clarity. Optional, not required for Diataxis to work.
5. Tutorial has no native DITA type. Don't force it into `<task>` DTD — its `<choice>`/branching elements fight guaranteed-success narrative. Two options: reuse generic `<topic>` shell with a tutorial authoring convention (fast, fits loosely with existing rigor culture), or build a lightweight specialization enforcing no-branching + required outcome element (more rigorous, bigger lift). Given prior writer's strictness, recommend specialization — confirm team appetite first.

## Phased plan, this year
1. **Weeks 1–3**: run triage query across all 1,400 topics. Produce real bucketed percentages, replacing estimate above.
2. **Weeks 4–6**: pilot one feature area. Tag metadata, build 4 pilot maps, draft one flagship tutorial from scratch.
3. **Months 2–4**: roll metadata tagging + map assembly across rest of corpus — mechanical, scriptable, fast (reference/explanation majority).
4. **Months 3–8** (overlap): rewrite task→how-to edits — strip embedded explanation, add context/prereq links.
5. **Months 2–12** (overlap): author remaining flagship tutorials, prioritized by support ticket volume.
6. **Month 12**: optional physical reorg, retire old concept/task/reference-only nav.

## Risks
- VP expects "migrate everything" to mean a rename job. Correct this before headcount/timeline gets set — tutorial authoring is net-new work, not migration.
- Skipping the reuse-graph audit before physical moves risks silent duplication or broken builds.
- More tutorials ≠ better. One working tutorial beats five unfinished — cap scope hard early.
- Reusing `<task>` DTD verbatim for tutorials reintroduces branching, defeats guaranteed-success property. Watch for this during rewrite.

## Tell VP
"Full migration" is two different jobs. First: reorganize/relabel existing 1,400 topics into reference/explanation/how-to — mechanical, scriptable, low risk, months not a full year. Second: author the tutorial quadrant from scratch — no reusable source material exists, this fixes the onboarding complaint, budget it as new content work, not migration work.