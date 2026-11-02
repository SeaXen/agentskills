# Vaneworth refresh — three asks, three answers

**One — numbers updated.** Done, in the map below, each signal diffed against its prior value.

**Two — declined.** Not folding the enterprise platform-team audience into this map. An indie/small-team engineer configures and pays for Vaneworth themselves; an enterprise platform-team buyer clears a security review and provisions it for other people's pipelines. Different exit events, different owners, different friction — that's two journeys, not two columns on one journey. Merging them would average away exactly the differences a journey map exists to show. Recommend a second, separate map for the enterprise platform-team segment, same method, its own stage cut and its own (real) buyer lane. Not built here — say the word and it's a new interview, not an add-on to this one.

**Three — declined, for this refresh.** Keeping the five-stage API arc. A refresh keeps the previous model unless it actually broke, because comparability against the map's own history is worth more than a better-fitting vocabulary — and nothing below argues the arc stopped fitting; all three updated numbers slot into the same boundaries they did last quarter. Marketing's company-wide AARRR standardisation is a real argument, not a trivial one — it's the reason to fold Vaneworth into AAARRRP on a *future* map, once the audience needs a cross-functional shared funnel or the interesting question becomes revenue/referral rather than "is this running in production." Switch when the arc breaks — production stops being the meaningful terminal stage, or this map needs to reconcile against a company OKR the arc has no vocabulary for. A sibling team's rebrand isn't that trigger. Because this is a refresh, model selection (skill step 1) is skipped entirely — straight to evidence.

---

# Developer journey map - indie and small team, 2026-09-19

## Scope

- **Segment.** Indie developers and small teams running their own CI. Self-serve: the developer decides and pays. The enterprise platform-team audience is explicitly out of scope for this map — see the declined-merge note above.
- **End state.** Production usage — Vaneworth gating merges on the team's default branch.
- **Stage model.** API and platform five-stage arc (awareness → onboarding → integration → production → advocacy), unchanged from the previous map. Kept for continuity; AAARRRP considered and declined this cycle (see above).
- **Refresh scope.** Signals refreshed for onboarding, integration and production, per the values supplied. Awareness and advocacy were not part of this refresh's evidence pass and stay at their previous (inferred / not instrumented) status — flagged in Gaps, not silently carried as if re-verified.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Awareness *(inferred)* | "find a CI runner that doesn't eat my week on config" | search or peer mention | lands on docs or pricing page | search results, comparison posts, community threads | marketing | carried from previous map — not re-collected this refresh | not instrumented this cycle *(inferred)* |
| Onboarding | "get one job green from a clean clone, no yak-shaving" | opens the quickstart / connects a repo | first pipeline run completes green on Vaneworth | quickstart docs, config generator, CLI, dashboard | developer experience | carried from previous map — not re-collected this refresh | **39% of onboarding starters reach first green run**, up from 34% (+5pp) |
| Integration | "wire it into our real pipeline — matrix builds, caching, secrets — not the demo" | first green run reached | pipeline runs on the team's default branch with caching/secrets configured | config reference, error docs, support | product | carried from previous map — not re-collected this refresh | **49% of onboarded users reach integration**, down from 52% (**-3pp — the one stage that moved backwards**) |
| Production | "trust this enough to gate merges on it" | integration reached | sustained use as a required check for 14 days, no manual overrides | status page, limits docs, runbooks, support | product | carried from previous map — not re-collected this refresh | **31% of integrating users reach production**, up from 28% (+3pp) |
| Advocacy *(inferred)* | "tell other indie/small teams this saved us the CI headache" | sustained production use | public talk, post, or unprompted recommendation | community, socials, changelog | DevRel | carried from previous map — not re-collected this refresh | not instrumented this cycle *(inferred)* |

## Buyer lane

None — self-serve. The indie/small-team segment decides and pays without a separate approver; there is no procurement or security-review step in this journey. (The enterprise platform-team segment *would* need a real buyer lane — technical approval, commercial approval — which is a second reason it doesn't belong folded into this map: it would show a healthy self-serve journey next to a lane that's empty for the wrong reason.)

## Moments

- **First success** — first pipeline run completing green from a clean clone. Time-to-first-success not re-measured this cycle; carried from the previous map.
- **Moment of truth** — making Vaneworth the required check that gates merges on the default branch. This is where the team stops evaluating and starts depending on it.
- **Abandonment point** — per the previous map, inside onboarding. Worth re-checking next cycle: onboarding just improved while integration just regressed, which is exactly the pattern that would relocate the real abandonment point downstream without a fresh friction log to catch it.

## Leak

**Integration.** It's the only stage that moved backwards this quarter (52% → 49%), and it has a clear owner able to act (product). Two other candidates considered and set aside:

- **Onboarding** (39%, still the lowest absolute rate among stages with an improving trend) is earlier in the arc, but it's moving the right direction under developer experience's existing fix — the signal this quarter is that the prior fix is working, not that it needs a new one.
- **Production** (31%, the lowest absolute rate on the map) is downstream of integration; fixing integration raises its input quality before production's own rate is worth touching, and production is also trending up on its own.

A regression with a named owner beats a persistently-low-but-improving number — it's the one thing this map didn't expect to see, and the one the prior version can't explain. Compared only against this map's own last version, per this skill's rule; no outside benchmark used.

**What this ordering starves.** Production stays the lowest-converting stage on the map (31%) and doesn't get worked this cycle. Promote it next if integration's fix lands and production's own number stalls or reverses instead of continuing to climb.

## Handoff

- **Owner of the fix.** Product.
- **Signal to watch.** Share of onboarded users reaching integration (currently 49%, down from 52%).
- **Re-read date.** 2026-12-18 (90 days), or sooner if there's a launch, a pricing change, a docs rewrite, or a new SDK before then.

## Gaps

- **Awareness and advocacy** — not refreshed this cycle; still carrying previous-map values, both inferred / not instrumented. Get real numbers here before the next re-read, or they'll be two cycles stale.
- **Friction evidence** — no new friction log or exit interviews ran this refresh; every friction-evidence cell above is carried, not re-verified. If integration's regression persists next cycle, that's the stage to run a fresh friction log against first.
- **No absolute volumes supplied** — only rates. The leak diagnosis above used trend direction plus earliest-owned as a proxy for "developers recovered per fix effort," because no per-stage counts were available to rank candidates properly. Get raw counts alongside rates next cycle so that ranking can be made on evidence instead of a proxy.
- **Enterprise platform-team segment** — no map exists for it. Declined to fold it into this one; it needs its own interview, stage cut and buyer lane.

---

**Quality gate.** Passes, at the threshold: signal coverage is exactly 60% (3 of 5 stages — onboarding, integration, production — carry a real current value; awareness and advocacy are labelled inferred/not instrumented and appear in Gaps). Every stage has one exit event and one owner; two owners (developer experience, product) sit outside DevRel. Exactly one leak nominated, with a named owner and a re-read date. No friction claim this cycle mixes new evidence with hypothesis — all are explicitly marked carried rather than presented as freshly verified.