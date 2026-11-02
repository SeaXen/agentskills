**Verdict: don't publish 94%. Numbers not measured, they're guessed. Fix before printing.**

Four breaks in Marisol's method, each one named in the skill's own "known failure" list:

1. **Maintainer count = wrong population.** GitHub contributors graph counts anyone who ever merged a commit — one-time drivers, bots, employees. Sponsorship fragility depends on npm publish rights, different number, usually smaller. Skill's exact documented failure: "hand-collected figures claimed five-plus maintainers for a package whose registry publish rights list one." slugsafe's "6 maintainers" is likely this same trap — real publish-right count probably 1-2.

2. **"Near-zero downloads" = eyeballed, not measured.** npm downloads have a public API (`api.npmjs.org/downloads/point/last-week/{pkg}`). Skill's exact matching failure: "zero downloads for a package moving 164 million a week." An eyeballed number can be off by orders of magnitude. slugsafe's real weekly downloads: unverified.

3. **"Fine" is not a real assessment state — this is the big one.** Skill requires three buckets: assessed-fine, assessed-flagged, not-assessable-with-reason. Marisol collapsed "couldn't find data" into "fine." That silently inflates coverage and hides exactly the fragile packages sponsorship exists to catch — a low-maintainer, high-dependents package marked "fine" because nobody could confirm it is the worst-case miss, not a neutral one.

4. **94% has no denominator, so it's not an auditable number.** Skill's required form: "resolved X of 310; Y had no source repo, Z marked not-assessable." A bare percentage "survives no audit" (skill's own words). Given point 3, some share of that 94% is "couldn't find → called fine," not "verified covered." Real verified coverage is probably lower, maybe well below 94%.

**Why 94% is implausible on its face:** the only published company to beat 80% coverage reported "95% or greater" — and needed a dedicated program plus a platform integration to get there. One engineer eyeballing 310 packages by hand landing one point below that frontier is a red flag, not a win.

I tried to pull live npm registry + downloads + deps.dev data on slugsafe this session to give you a real number — network calls got blocked by sandbox permissions. Needs rerun with network access.

**Next action:** rerun the spreadsheet through a measured pipeline before touching the annual report:
1. Resolve real dependency tree via deps.dev API (catches transitive deps too, not just the 310 direct ones Marisol listed).
2. Pull maintainer count from registry publish rights, not GitHub contributors graph.
3. Pull real download numbers from npm downloads API.
4. Re-tag every "couldn't find" row as not-assessable-with-reason, not fine.
5. Republish coverage as "X of 310 resolved; Y not-assessable" — never a bare percentage.