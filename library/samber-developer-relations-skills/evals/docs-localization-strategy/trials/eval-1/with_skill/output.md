**Decision: no to Japanese docs now. The plan on the table is rejected. Reopen ja when one fluent reviewer is named and a Japanese-browser engagement gap appears in the data.**

# Docs localization plan - Ironvale, 2026-10-30

## Stored context
- Locale `ja`: **declined**. Reopen conditions are below.
- Owner: none.
- Page set rule (if reopened): critical-path pack only.
- Pin fields (if reopened): `source_path`, `source_commit`, `translated_on`, `translation_method`, `reviewed_by`.
- Drift-check command (CI step for a reopened locale, not run): `python3 scripts/translation-drift-check.py --source content/en --locale ja=content/ja --format csv --fail-on no-pin,unknown-pin`
- Kill rule (if reopened): adoption or freshness below target for two consecutive quarters retires the locale (baseline).

## Assumptions
- ASSUMED: no Japanese support tickets, forum posts or search queries. Nobody has counted them.
- ASSUMED: no named deal or pipeline in Japan.
- ASSUMED: the product (console, CLI output, errors) is English-only.
- ASSUMED: no contract or regulation names Japanese.
- ASSUMED: nobody inside or near the team can review Japanese.

## Decision summary
| Locale | Decision | Reason | Reopen condition |
|---|---|---|---|
| ja | declined | Quickstart gap is 3 points (measured), under the 5-point baseline. Also no reviewer. | See below |

Reopen ja when any one of these holds:
1. Quickstart completion for ja-browser readers trails English-browser readers by more than 5 points. Per Step 1, rule out signup, payment and latency causes first.
2. Japanese tickets, posts or search queries appear in volume.
3. A named Japan deal or a contract requires Japanese.

Even then, launch needs two fluent reviewers first (gate below).

## Evidence
| Signal | Value | Type |
|---|---|---|
| Japan share of docs sessions | 38% | measured |
| Browser language `ja` share | 12% | measured |
| Ratio, `ja` browser ÷ Japan share | 12 ÷ 38 = 0.32 | measured |
| Quickstart completion, Japan vs English-browser | 41% vs 44%, gap 3 points | measured |
| Demand in Japanese (tickets, posts, queries) | unknown | ASSUMED none |
| Commercial weight in Japan | unknown | ASSUMED none |

What each signal says:
- **Country share is not need.** 38% says where readers sit, not that they need a translation.
- **Browser ratio.** 0.32 is under the one-half baseline. Most Japan readers likely run a non-Japanese browser. This is weak evidence alone: many developers keep English settings yet read Japanese faster.
- **Engagement gap.** 3 points is under the 5-point baseline. Japan readers already finish the quickstart almost as often as English readers. This is the strongest signal, and it says no comprehension barrier.
- **Caveat.** The 41% covers all Japan sessions, not only `ja`-browser sessions. Re-cut by browser language, which is the cheap test below.

Class: **no barrier shown**, and **no owner**.

## Why the CEO plan fails
Plan: LLM-translate all 800 pages once, publish under `/ja/`, fix on complaint.

- **Off the ladder.** A one-shot machine-translated dump has continuous MT's accuracy risk and none of its freshness.
- **No pins.** Without a source-commit pin per page, no page can be shown current. Every page goes stale on the next docs commit.
- **Complaints cannot work.** Nobody on the team reads Japanese. The team cannot read the complaint, judge it or verify the fix. Silent errors on auth, quotas, billing and deprecations never get reported.
- **Structural damage.** In a published evaluation of 50 LLM-translated READMEs, manual checks found broken code, URLs or Markdown in 16-50% of files (sourced, Adejumo et al.). That is on files where semantic scores looked fine.
- **Cost scale.** Reviewing 800 pages at 1 h each is 800 reviewer hours (baseline pace). At 4 reviewer hours per release (ASSUMED), that is about 200 releases.
- **Precedent.** MDN cut 21 locales in 2021 for lacking maintainers, with under 2% traffic loss (sourced estimate). It removed German in 2022 as unmaintained. Kubernetes refuses a locale without two contributors.

## Candidate bundles (ja)
| Bundle | Rung | Page set | Owner | Standing hours | Eliminated by |
|---|---|---|---|---|---|
| A | Do nothing | none | none | 0 | Leaves a 38% market on the status quo with no improvement |
| B | Source hardening | all 800 pages, incrementally | docs owner (name needed) | style review on new pages | Chosen |
| C | Critical-path pack | ~12 pages + UI strings | none | ~14 h first review, then per release | No owner; no barrier shown |
| D | CEO plan (dump) | 800 pages | none | unbounded | Off the ladder; fails gate items 1-6 |
| E | Reviewed LLM set / continuous MT / full human | wide | none | high | No owner; efficiency ranks below B and C |

**Chosen: B.** It serves every non-native reader, including Japan's 88% of sessions that use a non-`ja` browser. It rots with nothing and makes any later translation cheaper. Deleted rungs: all translation rungs, because rule 1 says no owner deletes every rung except source hardening.

## Source hardening (all markets)
- Glossary: one file in the repo, one named owner, with "do not translate" decisions (identifiers, CLI flags, HTTP headers, config keys, product names).
- Style rules: plain global English, one term per concept, no idioms.
- Code non-translatable: add `translate="no"` to code blocks and inline code through the Hugo render hook. This also stops browser machine translation from mangling code. Effort: half a day (ASSUMED).
- Hugo anchors: set explicit heading IDs so links survive any future locale.

## Reopen path: what a ja launch would cost
Pack: quickstart, install, auth, top ~9 task pages, all site UI strings. Pick the top task pages from Japan session data.

- **Launch load:** (12 pages + ~2 UI page-equivalents = 14) × 1 h ÷ 4 reviewer hours per release = 3.5, so about **4 releases** (baseline pace, ASSUMED reviewer hours).
- **Steady state:** changed pack pages per release × 0.25-0.5 h must fit within reviewer hours per release. Pull the changed-page count from source history.
- **Review model:** human-review every pack page before publication; the pack is small enough.
- **Never translated:** code, flags, headers, config keys, product names, generated API reference, changelog. Quote error strings verbatim with translation alongside.
- **Label:** "Translated from English with AI assistance, reviewed by <name>. The English page is authoritative." Add a link to the English page and a "report a translation problem" link.
- **Search exposure:** only after the first review pass. No auto-redirect by browser language.

## Ownership gate (ja): all 6 items open
| Item | Status | Closing action | Expected date |
|---|---|---|---|
| Two fluent named reviewers | open | contractor or hire | needs CEO decision |
| Critical-path pack and UI strings reviewed | open | starts after reviewers | after reviewers |
| Glossary with do-not-translate list | open | build in source hardening | ~1 week |
| Pin field and drift check in CI | open | add CI step above | after pack exists |
| Retirement threshold and person who can pull the locale | open | name person | with reviewers |
| Published owner names and contact | open | after reviewers | with launch |

The launch-load clock starts when all six close. A vendor with an independent quality reviewer can meet item 1 (baseline).

## KPIs and kill rule (if reopened)
| KPI | Pre-launch figure | Target | Control | Type |
|---|---|---|---|---|
| Quickstart completion, Japan sessions | 41% | set after one release | English-browser readers, 44% | measured |
| Adoption: Japan sessions staying on `/ja/` | none yet | set after one release | same readers on English pages | n/a |
| Freshness: critical-path pack `current` | none yet | at least 80% each release | n/a | baseline |
| Translation problem reports per 1,000 views | none yet | set after one release | n/a | n/a |

Kill rule: adoption or freshness below target for two consecutive quarters retires the locale and redirects to English pages (baseline).

## Rollout schedule
| When | Milestone | Owner |
|---|---|---|
| This week | Tell CEO: ja declined, with reopen conditions | you |
| Week 1 | Pull `ja`-browser vs `en`-browser quickstart completion; count Japanese tickets and queries | analytics owner |
| Week 1-2 | Hugo `translate="no"` render hook; glossary file | docs owner |
| Week 2 | If the gap is over 5 points, or demand appears: start the ownership hunt (contractor or hire) | you |
| After reviewers | 4 releases to launch the pack | named reviewers |

## Message for the CEO
Japan is 38% of docs sessions, but Japan readers finish the quickstart 3 points behind English readers (41% vs 44%). That is not a language barrier. Only 12% of sessions use a Japanese browser, so most Japan readers already read English. Nobody on the team can check Japanese, so a bulk translation would publish errors on auth and billing pages that nobody can catch. We will improve English docs for all non-native readers, and test the `ja`-browser cohort this week. If that cohort trails by more than 5 points, or Japan demand shows up, we hire a reviewer and launch a small pack.

## Next action
Pull quickstart completion split by browser language `ja` vs `en` (under 30 minutes in your analytics tool, ASSUMED). That number decides whether this answer changes.