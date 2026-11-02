# Pellworth Systems: documentation code-sample benchmarks for Tuesday's board slide

## Answer: no industry standard exists for any of the three numbers

I checked all three against the skill's source register. No standards body, vendor or survey publishes a required percentage for any of them. If a slide says "industry standard: X%", someone on the board can ask for the source, and there isn't one.

| Your question | Industry-standard figure | What exists instead |
|---|---|---|
| % of samples that should compile | **None published.** | A self-set recommendation of **≥90% compile/run pass rate**. It is a baseline, not a standard. |
| % of samples covered by tests | **None published.** | A self-set recommendation of **≥80% of the corpus** at tier Run or Compile-only, executed by CI. The nearest public vendor requirement is Google Cloud's: integration tests for critical paths, with no percentage. |
| Cross-language parity number | **None published.** | A self-set recommendation of **≥90% parity coverage** across tier-1 languages. |

Two further self-set baselines belong on the slide:
- **100%** of samples on the primary adoption path (quickstart, auth, first call) at tier Run and green in CI.
- **Zero** P0 findings (credential leaks, destructive commands, insecure defaults).

I'm leaving out the 100% cross-language target you may have seen. It is not a standard either.

## What is published (citable)

These are measurements of how ungoverned sample corpora perform. They back the baselines above as reasonable targets, but they are not targets themselves.

| Finding | Source |
|---|---|
| About 3M accepted Stack Overflow snippets: **1.00%** of Java snippets compile, **0.12%** of C#. **25.61%** of Python and **20.00%** of JavaScript run. (The dynamic languages were measured as "runnable", so they are not directly comparable to the Java and C# figures.) | Yang, Hussain & Lopes, "From Query to Usable Code", MSR 2016 |
| **24.4%** of 10,259 public Python gists ran without error out of the box. | Horton & Parnin, "Gistable", ICSME 2018 |
| **43%** of the Stack Overflow posts investigated contained deprecated APIs. Automated detection reached 100% precision and 86% recall on a 200-question sample. | Zhou & Walker, FSE 2016 |
| Of 323 professional developers surveyed, ambiguity, incompleteness and incorrectness were the severest API-documentation problems. Six of ten problem types were rated "blockers". (The survey covers API docs as a whole, not only samples.) | Uddin & Robillard, "How API Documentation Fails", IEEE Software 2015, DOI 10.1109/MS.2014.80 |
| "Better examples in the documentation" was the most-requested enhancement from API producers, at **63.5%**. | Postman State of the API, 2019 wave |
| Google Cloud requires integration tests for critical paths. | Google Cloud sample principles |

## Suggested slide wording

> **The bar we are measured against (our own, not an industry mandate)**
> - ≥90% of samples compile or run in CI
> - ≥80% of samples executed by CI (Run or Compile-only)
> - ≥90% parity across tier-1 languages
> - 100% of quickstart/auth/first-call samples at Run
> - Zero samples that harm the reader who copies them
>
> *Context: no published industry standard exists. Ungoverned public corpora compile 1–25% of the time (MSR 2016, ICSME 2018).*

Calling these "the bar we are being measured against" is accurate only if someone at Pellworth actually set that bar. If an outside party, such as a customer, auditor or exec, has named a number, get their source before Tuesday. Otherwise present these as your proposed targets.

## Warnings for the board

- **Don't cite the "94% of developers consider API documentation quality a key factor" statistic.** It is widely attributed to SlashData but is not confirmed in any SlashData report.
- **Don't present the 43% deprecated-API figure as a target.** It is a measured rate on Stack Overflow posts. The skill uses it only as a gate: a governed corpus above 43% has a detection problem.
- **I did not audit Pellworth's actual corpus.** I have no current pass rate, tested share or parity figure for you. I can run `scripts/sample-audit.py` on your docs directory to get them, which would let the slide show "we are at X% vs target Y%".
- **The thresholds are tunable.** The skill says to override them with your own data. A near deadline, no CI, or an existing test suite would change which tier to push first.

## Questions that would sharpen this before Tuesday

1. Is there any CI today that runs or compiles the samples, or are they all hand-maintained in Markdown?
2. Which languages do you publish, and which is the tier-1 set?
3. Can I run the mechanical audit on a docs directory to get your real baseline?