## Verdict

Start with neither. Fix the path first — specifically, two things you already told me are broken. Hacktoberfest (this October) and the GSoC org application (next year) both sit on top of a first-contribution path that currently fails two of this skill's four *blocking* checks, and a blocking failure outranks any recruitment decision, whatever the ordering below says.

## Why neither program clears the gate

The scorecard this skill uses has four pass/fail blocking checks. Two of yours already fail, from facts you gave me:

| Check | Status | Evidence | Taxonomy category (Steinmacher et al., 2015) |
|---|---|---|---|
| B2 – documented setup runs cold | **FAIL** | Setup breaks on Windows | Technical hurdles |
| B4 – submissions get answered | **FAIL** | Last outside PR waited 3 weeks for any reply | Social interaction |

A broken setup and a silent review queue are the two failures this skill calls out as invisible from inside the project — nobody files an issue for "I gave up," they just leave. Both a Hacktoberfest wave and a GSoC cohort make these two failures *worse*, not better: more strangers hitting a setup that only works on your machine, more contributors sent into a queue that already goes three weeks dark. That's the named failure mode "optimizing recruitment while review is the bottleneck" — more arrivals at an unstaffed queue produces more abandoned PRs and more resentment on both sides.

## The 80% Outreachy number doesn't support your plan

Two problems, independent of each other:

- **It's the wrong program.** The 80% figure is Outreachy's; the program you're planning to apply to is GSoC. GSoC's own published number is different (63.5% of studied participants reopened a PR to the same project post-program, arXiv:2412.13120) — still worth knowing, but not the number you cited.
- **It doesn't transfer even to Outreachy itself.** It's a 2019 self-reported alum survey with a 37% response rate — survivorship bias built in, no control group. The competing study (Labuschagne & Holmes, MSR 2015, Mozilla data) found the *opposite* direction: contributors whose first contribution was a mentored or good-first-bug were *less* likely to become long-term contributors. Two most-cited studies disagree and neither is causal. Treat "mentorship improves retention" as unproven and measure your own funnel instead (time to first response, second-contribution rate) — that's the only number that will actually tell you if this worked.

## Capacity check kills GSoC for now regardless

4 hours/week total, review included, is under this skill's own "under a day per week" threshold — the point at which a structured mentorship program gets deleted from consideration outright, however appealing it looks. Two concrete reasons that number doesn't stretch to GSoC:

- Hosting a mentor slot is a season-long standing job you can't abandon halfway once a student's summer is attached to it — an under-mentored intern costs you more than no intern.
- The skill's own condition for promoting a structured program is a second reviewer existing *and* your hours clearing a mentor's weekly commitment for a full season. You're a solo maintainer — neither holds.

Applying as an org next year is fine as a horizon; actually running a cohort on 4h/week solo is not.

## What to do instead, in order

1. **Fix the Windows setup (Step 3).** Given your hours budget, don't jump to a container — pick the cheapest tier that removes the actual failure: a pinned toolchain (`rust-toolchain.toml` + `Cargo.lock`, likely already present) plus explicit documentation of whatever's Windows-specific (linker, WASM target install, path handling), verified by an actual cold run on Windows or a `windows-latest` CI job — not by inspection. This is an afternoon, once.
2. **Fix the silence (Step 6), same week.** Adopt the two-clock rule: acknowledge every external issue/PR within a target you can honestly hold at 4h/week (say "within a week," stated in the file) even when the full review takes longer. Silence is the expensive failure, not slowness. This costs nothing ongoing and directly reverses your worst data point.
3. **Re-score before deciding anything else.** Confirm B1 (a CONTRIBUTING file exists), B2, B3 (3+ real, verifiable beginner issues stocked), and B4 all pass. Below that bar, don't ship any of this with a caveat — iterate.
4. **Then, if you still want a volume/recruitment layer:** a bot (stale-PR nag, auto-labeler) is the only thing worth adding at your hours level — an hour to set up, reversible in one commit, absorbs mechanical work without creating a human moment you can't staff.
5. **Hacktoberfest**, if you run it at all this year, only makes sense once step 3 holds — otherwise it's the case this skill names explicitly: an extrinsic reward with no quality gate buys volume you can't review, which is a cost. If you do opt in later, use the `hacktoberfest-accepted` label so only your own prepped, mentored issues count — don't open the whole repo to drive-by PRs into a queue you're still catching up on.
6. **GSoC org application**: keep it as a next-year target, but the actual go/no-go condition is a second reviewer joining you (so review load isn't 100% on the same 4 hours) — not the calendar.

## What to track instead of a program signup

Median time to first human response (against your stated target, not the 48-hour reference point unless you can actually hold it), setup-support questions ("I can't build it" — should drop to near zero once Windows is fixed), and second-contribution rate within 90 days. Those three numbers will tell you whether the path is fixed; a 6-year-old survey of a different program's alumni won't.