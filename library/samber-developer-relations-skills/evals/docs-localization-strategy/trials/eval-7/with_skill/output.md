**Answer: LLM pipeline, with Claire and Yannis as the human review layer. No agency.**

Neither option is right as a pure form. An LLM drafts, a masking and structure check guards the code, and a human signs off every page before it ships. Start with about 25 pages, not 300. French goes live around release 6, about 12 weeks out. That leaves 7 releases of slack inside your 6 months.

Next action: ask Claire and Yannis to confirm three things. They are fluent in French, they will both be named publicly as reviewers, and 5h each per release is firm. The French locale stays `gated` until the ownership table below is closed.

# Docs localization plan - Marrowick, 2026-10-30

## Stored context
- Locale: `fr`, one variant. Reviewers sit in Paris, so France French.
- Owners: Claire and Yannis. Combined capacity is 10h per release (measured).
- Page set rule: critical-path pack first, then traffic-ranked expansion up to the capacity ceiling.
- Pin fields: `source_path`, `source_commit`, `translated_on`, `translation_method`, `reviewed_by`.
- Drift check: `python3 scripts/translation-drift-check.py --source <en tree> --locale fr=<fr tree> --fail-on no-pin,unknown-pin --format csv`. It runs in CI with `fetch-depth: 0`.
- `--far`: set to commits per release on the quickstart, not the default 5 (baseline).
- Kill rule: adoption or freshness below target for two consecutive quarters retires `fr`.

## Assumptions
- ASSUMED: Claire and Yannis are fluent in French and technical enough to review flag-evaluation semantics.
- ASSUMED: about 20% of pack pages change per release. Replace this with docs commit history.
- ASSUMED: about 600 docs-site UI strings, about 2 page-equivalents. Product UI is already French, but the docs-site chrome is separate.
- ASSUMED: no non-language cause explains the 13-point completion gap. Check signup friction, EU region availability, latency and payment first.
- ASSUMED: no contract or regulation names French.
- ASSUMED: no agency budget is committed.
- ASSUMED: SDK, CLI and error strings are English only.
- ASSUMED: one live docs version.
- ASSUMED: release 1 starts the week of 2026-11-02. Six months is about 13 releases, ending about 2027-04-30.

## Decision summary
| Locale | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| fr | gated | Barrier confirmed, two reviewers available. Ownership items 2-6 are open. | Close the gate table below. |

## Source hardening (all markets)
- Glossary owner: Claire proposed, file `glossary.md`. Confirm.
- Style: plain global English, one term per concept, no idioms.
- Flag, rule, segment, environment and SDK terms get explicit "do not translate" or "translate as X" decisions, with who decided.
- Code: `translate="no"` on code. Heading anchors stay English with explicit IDs.

## Locale: fr (gated)

### Evidence
| Signal | Value | Type |
|---|---|---|
| Country share | 22% of sessions (FR, BE, CH) | measured |
| Browser-language ratio | 17% / 22% = 0.77. This is above the 0.5 baseline, so most of these readers do run French browsers. | measured |
| Engagement gap | 61% - 48% = 13 points. This is over the 10-point baseline for a barrier, once non-language causes are ruled out. | measured |
| Demand | about 40 French support tickets per month | measured |
| Product localized | UI is French. SDK and error strings unknown. | measured / ASSUMED |
| Commercial weight | not provided | unknown |

Caveat on the ratio: Belgium and Switzerland are only partly French-speaking, so the 22% denominator is overstated. French readers elsewhere (Canada, Africa) are in the numerator, so the true ratio is likely higher.

Substitutes: browser translation and AI assistants exist. Check whether Google machine-translates French snippets. It is not a replacement for a reviewed quickstart.

Class: barrier confirmed, owner named.

### Candidate bundles
| Bundle | Rung | Page set | Owner | Standing hours | Eliminated by |
|---|---|---|---|---|---|
| A | Critical-path pack, LLM draft + human review | about 25 pages + UI strings | Claire, Yannis | about 3h per release | Chosen |
| B | Reviewed LLM set | A + expansion to about 60-70 pages | Claire, Yannis | 7-10h per release | Next step, once A's KPIs hold for 2 releases |
| C | Agency, full human sync | 300 pages | agency | highest; every source commit becomes a job | No contract names French. Standing cost fits a growing docs set badly. Your reviewers would be idle. |
| D | Continuous labelled MT, unreviewed | 300 pages | nobody | about 0h | Wrong parameter, quota or targeting-rule translations ship unreviewed. A published evaluation of 50 LLM-translated READMEs found structural, code or URL damage in 16-50% of files. |

Chosen: A, then B. Deleted rungs:
- Community program: Marrowick is SaaS, there is no cohort, and cohorts take quarters.
- Full human sync: see C.
- Continuous MT: see D.

Agency fallback: if a reviewer leaves, a vendor with an independent quality reviewer can fill the slot (baseline).

### Page set
- Pages: quickstart, install, authentication, SDK setup, first flag, top task pages by French-reader traffic, and every docs-site UI string. Second wave: concept pages the quickstart links to.
- Steady state: 25 pages × 20% = 5 changed pages × 0.5h = 2.5h ≤ 10h (baseline pace, ASSUMED churn).
- Launch load: (25 pages + 2 UI page-equivalents) × 1h ÷ 10h = 2.7, so 3 releases (baseline pace). Replace with real pace after the pilot.
- Capacity ceiling: 7h of the 10h goes to steady state, so 7h ÷ (0.2 × 0.5h) = about 70 pages. That is the most you can keep current.
- Full 300 pages: 300 × 1h ÷ 10h = 30 releases, over twice your 13. Pages outside the ceiling fall back to English.
- Generated API reference: top-traffic pages only, or not at all.
- Never translated: identifiers, CLI flags, HTTP headers, config keys, product names, contributor docs, docs changelog.
- Error messages and UI labels are quoted verbatim as the product prints them, with French alongside.
- Code is untouched. Screenshots and diagrams are deferred.

### Review model
- Pack: every page is reviewed before publication. One of Claire or Yannis post-edits, the other approves, so nobody approves their own change. If the second sign-off pushes first review past 1h, recompute the launch load.
- Larger set (bundle B): human review before publication for security, auth, billing, quotas, deprecations and rollout/targeting-rule semantics. Other pages are reviewed once they pass a page-view threshold (Azure Translator note, sourced). Threshold value to be set.
- Pipeline: mask code blocks. Check per page that code-fence, link and heading counts match the source.
- Label on every page: "Translated from English with AI assistance, reviewed by <name>. The English page is authoritative. Read it in English → · Report a translation problem →"
- Language suggestion banner is dismissible, with a persistent switcher. No auto-redirect.
- Search exposure: after the first review pass.

### Freshness contract
- A translated page never shows source `tested_with` or `last_verified` stamps unless its pin is `current`.
- Banner on `behind` pages, in French, with the source link in the first line.
- `far` on a critical-path page: serve the English page.
- Retire a page that is `far` for two releases or 180 days (baseline).
- Mintlify caveat: if English sits at the repo root and `fr/` is nested inside it, pass `fr/` as a `--locale` or the script scans it as source pages. Confirm the layout before the first run.

### Ownership gate
| Item | Status | Closing action | Expected |
|---|---|---|---|
| 1. Two fluent reviewers | Pending confirmation | Claire and Yannis confirm | Release 1 |
| 2. Pack + UI strings translated and reviewed | Open | Pilot, then review pack | Release 5 |
| 3. Glossary with "do not translate" decisions | Open | Claire and Yannis draft | Release 1 |
| 4. Pin on every page + drift check running | Open | Add CI step | Release 2 |
| 5. Written retirement threshold + person allowed to pull the locale | Threshold written above; person unnamed | You name one | Release 1 |
| 6. Published owner names + contact | Open | Add to French docs footer | Release 5 |

Person allowed to pull the locale: not named. You decide.

### KPIs and kill rule
| KPI | Pre-launch | Target | Control | Type |
|---|---|---|---|---|
| Quickstart completion, French readers on `fr` pages | 48% | set after release 1 post-launch; aim to approach the 5-point gap | 61%, English readers | measured |
| Adoption: French-browser sessions staying on `fr` pages | none yet | set after release 1 | same market on English pages | measured |
| Freshness: pack `current` by pin | none | ≥ 80% at every release | n/a | baseline |
| Quality: translation reports per 1,000 views | none | set after release 1 | n/a | baseline |
| French support tickets per month | about 40 | track; no target | prior months | measured |

The 13-point gap may not be fully language. Expect to close only the language share of it.

Kill rule: adoption or freshness below target for two consecutive quarters, then redirect all `fr` URLs to English and remove `fr` from the switcher.

## Rollout schedule
| Release | Milestone | Owner |
|---|---|---|
| 1 | Confirm reviewers, glossary, never-translate list, pick the 25 pages from French-reader traffic, rule out non-language causes of the gap, name the person who can pull the locale | You, Claire, Yannis |
| 2 | Build pipeline (masking, structure check), configure Mintlify French nav, add the drift-check CI step | Yannis |
| 2-3 | Pilot on quickstart, install, auth. Record real review minutes per page and replace the baselines. | Claire, Yannis |
| 3-5 | Review the remaining pack pages and UI strings | Claire, Yannis |
| 5 | Gate closes. Publish owner names. Expose to search after the first review pass. | You |
| 6 | **French live** (about week 12, late January 2027). Language suggestion + switcher on. | You |
| 7 | Read KPIs, set first targets | You |
| 8+ | If KPIs held for two releases, expand toward the 70-page ceiling by traffic rank | Claire, Yannis |
| 13 | Deadline slack (about 2027-04-30) | n/a |

Separately: the kill rule cannot fire before two full quarters after launch, so about mid-2027 at the earliest.

**Next:** send Claire and Yannis the three confirmations above and name the person who can pull the locale. About 5 minutes.