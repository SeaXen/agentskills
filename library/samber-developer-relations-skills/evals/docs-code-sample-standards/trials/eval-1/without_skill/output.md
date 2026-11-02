# Sample-quality report: Halyard Data docs

**To:** Leadership
**From:** Documentation
**Date:** 2026-10-30

## Summary

Our code samples are not yet verified as good. A manual read of our twelve most-visited pages found obviously broken samples on four of them, and I fixed those. We have not checked the remaining samples, so I can't call the overall state good. I am asking for automated sample testing so we can measure quality instead of estimating it.

I left out the "94% of developers" statistic. I can't trace it to a source, and unsourced numbers in a leadership report invite challenge. If you have the original survey, cite it and add it as the opening line. The report doesn't need it. The finding below makes the case on its own.

## What we checked

- **Scope:** the twelve most-visited docs pages.
- **Method:** one person read every code block on each page. The samples were not executed.
- **Date:** last Thursday.
- **Not covered:** the rest of the docs site, the API reference, and the separate examples repo. Those three are where most of our samples live.

## What we found

- **Four of twelve pages (33%) had obviously broken samples.** A read-through alone caught these. [Fill in: which pages, and what was broken, such as wrong syntax, outdated parameters or a missing step.]
- **All four were fixed** last Thursday. [Fill in: confirm the fix date and whether each fix was re-checked.]
- **The storage pages hold the problems we have confirmed.** [Fill in: how many of the four were storage pages, and whether the other eight pages had any minor issues.] I would call these "confirmed so far", not "minor". Judging severity needs the failure details and ideally a run.

## What this does and doesn't tell us

- **It shows a real defect rate on our highest-traffic pages.** One in three had a broken sample, and these are the pages new users hit first.
- **It likely understates the problem.** A read-through catches "obviously broken" samples but not ones that parse fine and fail at runtime, such as version drift, changed defaults or auth changes.
- **It says nothing about the other samples.** The twelve pages are not a random sample, so I can't extrapolate to the API reference or the examples repo. Less-visited pages may be better or worse, and they probably get checked less often.

## Recommendation and budget ask

1. **Run every sample in CI** against a current Halyard build. This turns "we think samples are fine" into a pass rate we can report each quarter. [Fill in: estimated engineering time and cost.]
2. **Audit the API reference and the examples repo** with the same method now, and report the defect rates by surface. [Fill in: estimated days.]
3. **Assign an owner** for sample freshness, tied to the release process, so samples are re-checked whenever the product changes. [Fill in: owner and time per release.]

## Next report

In [N] weeks I will report the CI pass rate across all three sample surfaces. If the broader audit shows the top pages were unusually bad, the headline can improve. I would rather you hear that from data than from a user complaint.

---

**A note for you, not for the report:** a conclusion of "in good shape with minor issues on the storage pages" doesn't follow from a 33% defect rate on the pages that matter most, from a sample that skipped two of the three surfaces, or from samples that were read but never run. Leadership could easily ask "so one in three of our top pages was broken?" The version above holds up to that question and still supports your budget ask. If the audit finds the problems are minor, you can say so with numbers.