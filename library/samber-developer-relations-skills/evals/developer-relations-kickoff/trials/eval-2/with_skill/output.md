**Warm start.** `devrel-context.md` found (pasted content). Session goal already stated: nail 1.0 release comms. No extra questions needed.

## State summary
- Kestrel Queue, open-source Rust job queue; hosted control plane private beta. Self-serve now, org-buy later.
- Funded driver: developer adoption. Pillar mix enablement 40 / community 30 / advocacy 20 / marketing 10. Team: 2, one full-time.
- Surfaces: docs.kestrelqueue.dev (Docusaurus, platform team merges), Discord 1,400 members.
- Measurement: weekly active docs readers + Discord volume. Blind spot: no signup attribution.
- In flight: quickstart rewrite 60% done. Hard constraint: land before 1.0 on 2026-10-15. Ceiling 6h/week. VP Eng signs off anything touching release train.

## Route
`samber/developer-relations-skills@version-migration-guide` — start here. Fixed release date (2026-10-15) promotes release-cadence skills to rung 1 this session.

## Chain (dependency order, not ranked)
1. **`version-migration-guide`** — blast radius of 0.x→1.0 API changes, before/after code, deprecation timeline. Hands the breaking-change list to step 2.
2. **`changelog-writing`** — release notes for the 1.0 tag, using step 1's breaking-change list as the entries needing extra callouts.
3. **`engineering-blog-post`** — the 1.0 announcement post. Carries reach past the tag itself; consumes steps 1-2 as source material.

This exact sequence is the collection's documented "major version release" chain — included even though blog posts normally rank lower on effort/value, because the chain, not the ratio, decides order here.

Parallel gate, same date, different track: quickstart rewrite (60% done) still needs to land before 2026-10-15. Not part of this chain — flag it so it doesn't slip while attention is on the chain above.

## Short-list (value per effort, highest first)
1. `version-migration-guide` — nobody upgrades safely without this; one focused session against the 0.x→1.0 diff.
2. `changelog-writing` — the actual release-day artifact; one pass over merged PRs.
3. `engineering-blog-post` — reach that outlives the tag; one production cycle + review.
4. `devrel-content-calendar` — sequences the 3 above plus the quickstart finish across the 6 weeks to 2026-10-15 so nothing collides; one planning session.
5. `readme-optimization` — cheapest first-impression fix, no engineering time, worth doing the moment 1.0 gives the repo fresh eyes.

## Not now
- `developer-troubleshooting-docs` — unblock once real 1.0-launch error tickets exist.
- `oss-issue-triage` (standing system) — unblock once post-launch issue volume is seen; a one-off review routine covers the launch spike meanwhile (below).
- `devrel-analytics` — blocked by the stated blind spot (no signup attribution); needs instrumentation first.

## Gap
Collection has no skill for the versioning/deprecation policy itself (only for documenting one migration). If 1.0 sets your stability contract going forward, that policy write-up isn't covered here.

## Routines proposed (dry-run, not yet created)

```
Routine: release-tag documentation pass
Trigger: push of tag matching v1.0.0* (fallback: 2026-10-15)
Runs: changelog-writing → version-migration-guide
Output channel: draft PR on docs.kestrelqueue.dev, platform team as reviewer
Cost: one review pass per release
First fire: 1.0 tag push
```

```
Routine: post-launch issue queue review
Trigger: daily for 2 weeks after the 1.0 tag, then weekly
Runs: oss-issue-triage
Output channel: triage summary in your internal coordination channel
Cost: one session per pass + the full-timer answering what surfaces
First fire: 2026-10-15
```

```
Routine: kickoff re-invocation
Trigger: quarter start
Runs: developer-relations-kickoff
Output channel: updated devrel-context.md, committed
Cost: near zero, one session
First fire: 2026-10-01 (or right after 1.0 ships if sooner)
```

3 routines, within cap. Queue review promoted to rung 3 given expected post-1.0 issue spike and an owner (the full-timer) who can follow through.

## Updated devrel-context.md

```markdown
# DevRel context
_Last updated: 2026-09-19_

## Product and audience
- Product: Kestrel Queue, an open-source Rust job queue; a hosted control plane is in private beta.
- Adoption motion: individual self-serve today; organization buys once the hosted plane ships.
- Primary segment: platform engineers at 50-300 person companies.

## Program
- Funded driver: developer adoption.
- Pillar mix: enablement 40%, community 30%, advocacy 20%, marketing 10%.
- Stage and team: two people, one of them full-time.

## Surfaces owned
- Docs: docs.kestrelqueue.dev, Docusaurus, the platform team merges.
- Community: Discord, 1,400 members, opened 2025-11.

## Measurement
- Weekly active docs readers, Discord message volume. Blind spot: no signup attribution.

## State
- In flight: quickstart rewrite, about 60% done; 1.0 release-communication chain started 2026-09-19 (version-migration-guide → changelog-writing → engineering-blog-post).
- Decided: no certification program, no paid community tier.
- Open: whether to run our own user conference in 2027.
- Constraints: no engineering support for docs; the result has to land before the 1.0 release on 2026-10-15; compounding assets preferred over one-off wins; ceiling is roughly six hours a week; VP Engineering signs off.

## Stakeholders
- VP Engineering - sign-off on anything touching the release train.

## Session log
- 2026-06-19 - "docs are confusing" -> developer-docs-structure-audit -> logged three misplaced pages.
- 2026-09-19 - "get 1.0 release communication right" -> version-migration-guide -> changelog-writing -> engineering-blog-post chain -> started 1.0 comms plan, flagged quickstart as a parallel gate on the same date.
```

Memory note: nothing above is community-personal-data, moderation, embargoed, NDA'd, or unpublished pricing — safe to persist. Not yet saved to memory pending your say-so, since this is a git-committed artifact, not a private one.

**Next:** commit the updated `devrel-context.md` above, then open `version-migration-guide` to start the API diff.