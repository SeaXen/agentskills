**Do now (about 15 minutes):** ask marketing for the exact event date. Ask the three volunteers for their weekly hours and whether they read Simplified Chinese technical text. Request analytics access today. The rest of this plan depends on those answers.

# Docs localization plan - Pellbrook, 2026-10-30

## Stored context
- Locale: `zh-Hans`. Decision: `gated`, critical-path pack only.
- Owner: you (Pellbrook DevRel). Person allowed to pull the locale: you.
- Pin fields: `source_path`, `source_commit`, `translated_on`, `translation_method`, `reviewed_by`.
- Drift check: `python3 scripts/translation-drift-check.py --source docs/en --locale zh-Hans=docs/zh-hans --far 5 --format csv --fail-on no-pin,unknown-pin`. This is a CI step to ship before any page is translated.
- Page set rule: quickstart, install, auth, top task pages, site UI strings.
- Kill rule: adoption or freshness below target for two consecutive quarters retires the locale.

## Assumptions
No analytics access and no Chinese reader on staff, so every figure below is `ASSUMED` or `baseline` unless marked otherwise.
- ASSUMED: "end of next month" means 2026-11-30, and the Shanghai event falls on or after that date.
- ASSUMED: the docs are Markdown in a mirrored tree (`docs/en`, `docs/zh-hans`) with front matter.
- ASSUMED: Pellbrook's CLI output and error messages are English-only.
- ASSUMED: the three volunteers can give about 3 h/week each. Only two of them count as reviewers.
- ASSUMED: about 300 UI strings, which is 1 page-equivalent (baseline pace).
- ASSUMED: the docs licence lets translations inherit it. Confirm this.
- ASSUMED: release cadence unknown, so capacity is counted per week.

## Decision summary
| Locale | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| zh-Hans | gated | Volunteers and the event are demand signals. No data shows source English is a barrier. No staff member can verify quality. | All 6 ownership-gate items closed by 2026-11-23. Week-1 evidence check does not kill it (see Evidence). |

Tell marketing now what "Chinese docs live" means. It means about 12 reviewed pages plus site UI strings, each labelled, with English authoritative. It does not mean the whole docs set. A whole-tree machine dump is not on the ladder, because it has no pins and no review.

## Source hardening (all markets)
- Glossary owner: you. Location: `docs/GLOSSARY.md`. Volunteers decide each Chinese term, and the glossary records who decided.
- Style rules: plain global English, one term per concept, no idioms.
- Code marked non-translatable: `translate="no"` on code blocks.
- This work helps every non-native reader and lowers the cost of every later locale.

## Locale: zh-Hans (gated)

### Evidence
| Signal | Value | Type |
|---|---|---|
| Country share of sessions | unknown until analytics access | ASSUMED (no data) |
| Browser-language ratio | unknown until analytics access | ASSUMED (no data) |
| Engagement gap vs English readers | unknown until analytics access | ASSUMED (no data) |
| Demand in the language | 3 volunteers offered. Chinese posts in Discord and GitHub issues: count by hand, about 1 h. | measured (volunteer count); rest pending |
| Commercial weight | 1 Shanghai event. Pipeline unknown. | measured (event); pipeline pending |

Class: provisional. It is not a confirmed barrier. Treat it as `gated`, since the default is "not yet" until signals 1-3 say otherwise.

Do these four checks by Fri 2026-11-06, about 2 h in total:
1. Count Chinese-language posts in Discord and GitHub over the past 6 months.
2. Ask a volunteer to open the docs site from mainland China and report load time and any blocked assets. Latency or blocking is a non-language cause that translation would not fix.
3. Ask marketing for the event's registrant and attendee profile.
4. Ask the volunteers where they read docs now and how they read English.

If there is no Chinese demand and no mainland readership, downgrade to `source hardening only`. Hand out an English quickstart at the event instead.

### Candidate bundles
| Bundle | Rung | Page set | Owner | Standing hours | Eliminated by |
|---|---|---|---|---|---|
| A | Source hardening only | none | you | about 1 h per new page | Misses the event ask. Kept in every bundle. |
| **B** | **Hardening + critical-path pack** | **about 12 pages + UI** | **2 volunteers + you** | **launch about 6 reviewer h/week; steady about 1.5 h/week** | **Chosen** |
| C | Reviewed LLM set | about 40 pages | volunteers | 40 h ÷ 6 h/week ≈ 6.7 weeks | Misses the date. Reviewers unverified. |
| D | Community program | full set | volunteers | governance job | Deleted: a date inside one quarter, and cohorts take quarters to form. |
| E | Continuous labelled MT | full set | nobody | pipeline upkeep | Unreviewed errors on auth, retention and sampling pages. Nobody on staff can catch them. |
| F | Full human sync | full set | vendor | highest | No contract or budget (ASSUMED). |

Chosen: B, because it is the only bundle that fits about 4 weeks and 6 reviewer hours a week. It also keeps a path to D after the event. Confirm B with me before week 2.

### Page set
- Pages: quickstart, install, auth and token setup, connect to a backend, basic config, common-errors page, and about 5 top task pages. Pick the task pages from Discord's most-asked questions. Swap in traffic ranking once analytics access arrives. Second tier, only if time is left: concept pages the quickstart links to.
- Steady state: ~3 changed pages per release × 0.5 h = 1.5 h ≤ ~6 reviewer h (baseline pace, ASSUMED capacity).
- Launch load: (12 pages + 1 UI page-equivalent) × 1 h ÷ 6 h/week ≈ 2.2 weeks (baseline pace). It fits, with about 1.5 weeks of slack, if the gate closes in week 1.
- Never translated: identifiers, CLI flags, config keys, metric names, HTTP headers, the product name, generated API and config reference, changelog, contributor docs, screenshots and diagrams. Code stays unchanged.
- Error strings and UI labels appear verbatim as the product prints them, with a Chinese translation alongside, so readers can search what they see.
- Keep heading anchors in English, with explicit IDs.
- Check that site search tokenizes Chinese, and that fonts and layout render correctly.
- Glossary file: `docs/GLOSSARY.md`.

### Review model
- Human review before publication: every page. The pack is small enough that no tiering is needed. Security, auth, retention, sampling and quota pages get the strictest read.
- Draft: an LLM translates with the glossary and with code blocks masked. You run it, since you only operate the pipeline. Per page, check that code-fence, link and heading counts match the source.
- Review: volunteer 1 post-edits. Volunteer 2 reviews. Nobody approves their own change.
- Page-view threshold review: not used, because the set is reviewed in full.
- Label on every page (in Chinese): "Translated from English with AI assistance, reviewed by <name>. The English page is authoritative. Read it in English → · Report a translation problem →".
- Search exposure: only after the first review pass. Keep `noindex` until then. URL, canonical and hreflang work goes to `docs-seo`.
- Language switch: a dismissible suggestion plus a persistent switcher. No auto-redirect.

### Freshness contract
- Pin fields: see Stored context. Pin each page's last source commit when translation starts, never HEAD at the end. Use `translation_method: llm-reviewed`.
- Drift check: runs in CI with `fetch-depth: 0`. `--far 5` is a baseline. Replace it with commits per release once you have the history.
- Banner: shown in Chinese on any page whose source moved. Its first line links to the English page.
- Fallback: a `far` critical-path page serves the English page until re-reviewed.
- Retirement (baseline): a page `far` for two releases or 180 days goes to a redirect. The locale retires after two quarters below target. If the last reviewer leaves with no replacement in a quarter, freeze it read-only, then retire.
- Tested-version stamps are never copied. A page shows the source's stamps only while its pin is `current`. Otherwise the banner replaces them.

### Ownership gate
| Item | Status | Closing action | Expected date |
|---|---|---|---|
| 1. Two named fluent reviewers | open | Confirm 2 of the 3 volunteers by name and hours. The third is the backup. Add one paid 2 h spot-check of the 3 riskiest pages if budget allows, since no staff can verify. | 2026-11-06 |
| 2. Pack and UI strings translated and reviewed | open | Weeks 2-3 | 2026-11-20 |
| 3. Glossary with do-not-translate decisions | open | Volunteers decide, you record | 2026-11-09 |
| 4. Pin on every page, drift check in CI | open | Ship the CI step and the script first | 2026-11-09 |
| 5. Written retirement threshold, named person to pull | open | Use the thresholds above. Name yourself. | 2026-11-06 |
| 6. Published owner names and a contact | open | Page footer plus a Discord channel. Get each volunteer's consent to be named. | 2026-11-13 |

Community add-ons (all open):
- Review permissions scoped to `docs/zh-hans`.
- A progress page.
- An escalation path if a volunteer goes silent.
- Contribution terms the volunteers accept. Translations inherit the docs licence.

### KPIs and kill rule
| KPI | Pre-launch figure | Target | Control | Type |
|---|---|---|---|---|
| Adoption: share of zh sessions staying on zh pages | none; capture the first week | set after 1 release | same market on English pages | baseline |
| Outcome: quickstart completion for zh readers | unknown until analytics access | set after 1 release | English readers, same market | ASSUMED |
| Freshness: pack pages `current` | 0% | ≥ 80% at every release | none | baseline |
| Quality: problem reports per 1,000 views | none | set after 1 release | none | baseline |

Kill rule: adoption or freshness below target for two consecutive quarters retires the locale. Redirect every URL to the English page and remove it from the switcher.

## Rollout schedule
| Week | Milestone | Owner |
|---|---|---|
| W1 (Nov 2-6) | Event date confirmed. Four evidence checks done. Reviewers named. Go/no-go on `gated` vs downgrade, Fri Nov 6. | you |
| W2 (Nov 9-13) | Glossary and CI drift check live. UI strings and pages 1-6 drafted and post-edited. Contact published. | you, volunteer 1 |
| W3 (Nov 16-20) | Pages 7-12 drafted. Volunteer 2 reviews all pages. Spot-check of the risky pages. | volunteers 1-2 |
| W4 (Nov 23-27) | Gate review Mon Nov 23. If all 6 items close, go live Wed Nov 25 on staging, then public and indexable. Nov 26-30 is buffer. | you |
| After event | Read KPIs. Decide whether to move up to the community program. | you |

If the gate is not closed on Nov 23, the locale stays `gated`. Show English docs at the event.

## Open questions, ranked
1. What is the exact event date?
2. Can you get analytics access this week?
3. What is the docs generator and repo layout?
4. How fast does the source change (commits per week, release cadence)?
5. Is the product itself localized (CLI output, errors, console)?

**Next:** send the event-date question to marketing and the hours-and-fluency question to the volunteers. About 10 minutes.