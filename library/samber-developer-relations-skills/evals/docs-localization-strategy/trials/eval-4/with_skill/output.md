**Do not run everything through an LLM and let Lotte skim.** Lotte alone cannot finish this, and a skim is not the review the contract needs.

**Next action (today, 15 min):** send five questions to the contract owner or the agency (see "Open questions"). Their answers move the plan more than anything below.

I could not run the interview, so every `ASSUMED` item is listed here. I did not run the drift script, because no German page exists yet. Section order follows the skill's `locale-plan-template.md`.

# Docs localization plan – Bridgewater Signals, 2026-10-30

## Assumptions

- `ASSUMED` In-scope pages (Ingest + Access Control, with the concept pages they link to): 140. I model 60 and 250 too.
- `ASSUMED` 10–15% of the 60 v6 commits per release touch in-scope pages. That is about 6–9 changed pages per release.
- `ASSUMED` Go-live is about 2027-03-30. That gives 10 two-week releases, the last held as buffer.
- `ASSUMED` The agency deploys v6. If it deploys v5, translate v5 instead.
- `ASSUMED` The product UI and error strings are English only. German docs will quote them verbatim with German alongside.
- `ASSUMED` Nobody has answered whether German must track later releases after go-live.
- `ASSUMED` The docs are public, so sending them to an LLM provider and a vendor is allowed. Check this against the contract.

## Decision summary

| Locale/scope | Decision | Reason | Unlock or reopen condition |
|---|---|---|---|
| de, Ingest + Access Control, v6 | **gated, then launch** | The contract names the language and scope. This promotes full human translation of the named scope above the other rungs. | Gate items 1–6 close (see Ownership gate) |
| de, other modules | declined | The contract does not name them, and there is no barrier evidence. | Agency or other German customers ask, or an engagement gap shows |
| v4, v5 | English fallback | The skill says to translate the latest version only. Add a German notice that the version is English-only. | Agency runs one of them |
| Any other language | declined | There is no evidence. | Run Step 1 tests first |

## Source hardening (all markets)

Start now, on the in-scope pages first.

- Owner: docs lead. Lotte approves the German term for each entry.
- Style: plain global English, one term per concept, no idioms.
- Code: mark code `translate="no"`.

This lowers vendor cost and makes the LLM draft cleaner.

## Locale: de (gated)

### Evidence

| Signal | Value | Type |
|---|---|---|
| Trigger | Signed contract naming German for two modules | measured |
| Engagement and browser-language tests | Skipped. The contract decides scope. | – |
| Commercial weight | One federal contract | measured |

Class: barrier confirmed (contractual), owner not yet fully named.

### Candidate bundles

| Bundle | Rung | Owner | Standing hours | Eliminated by |
|---|---|---|---|---|
| A. LLM draft + Lotte skims (your plan) | Reviewed LLM set, single reviewer | Lotte | 6 h/release, not enough | Fails the math below, fails gate item 1, and a skim is not review of security pages |
| B. LLM draft + vendor professional post-edit + vendor independent reviewer + Lotte technical review of high-risk pages | Full human sync of named scope, LLM-assisted | Vendor + Lotte | Lotte ≤ 6 h/release | **Chosen** |
| C. Professional translation from scratch | Full human sync | Vendor | Lotte ≤ 6 h/release | Costs more than B for no extra value. Keep as a fallback for Access Control pages if post-edit quality disappoints. |

Deleted rungs:
- Community program: there is no cohort, and it is a closed contract.
- Continuous labelled MT: unreviewed errors are unacceptable for a public-sector buyer.

### Page set and the math

Pages, in order:
1. Install, auth, quickstart and top task pages for Ingest and Access Control.
2. The concept pages those link to.
3. All site UI strings.
4. Reference prose, only if the contract says reference is in scope. Identifiers stay in English.

Never translate:
- identifiers, CLI flags, HTTP headers, config keys and product names
- changelog and contributor docs
- screenshots (deferred)

Keep heading anchors in English with explicit IDs. Quote error strings verbatim, with German alongside.

**Why Lotte alone fails** (baseline pace: 1 h per page first review, 0.5 h per changed page, `baseline`):

- Steady state: 6–9 changed pages × 0.5 h = 3–4.5 h of her 6 h per release. Only 1.5–3 h per release is left for launch.
- Launch load, Lotte alone, with all 6 h per release (ignoring steady state):

| In-scope pages | Releases needed | Releases available |
|---|---|---|
| 60 | (60+2) ÷ 6 ≈ 10.3 | 9 |
| 140 | ≈ 23.7 | 9 |
| 250 | ≈ 42 | 9 |

All three are over capacity, and that is before steady-state drift eats her hours.

**Plan B load on Lotte:**
- Glossary and pilot: about 6 h in R2.
- Technical review of high-risk pages only: about 30 min each. Access Control, auth, retention and quotas get human review before publication. `ASSUMED` 40 such pages = 20 h across R3–R7.
- Steady-state high-risk deltas after that.

That fits 6 h per release if the high-risk set is 40 pages or fewer. If it is larger, add a second internal technical reviewer. Measure real pace in the R2 pilot and replace the baselines.

### Review model

- Pipeline: mask code → LLM draft with glossary → vendor post-edit → vendor independent review → Lotte for high-risk pages → publish.
- Check structure per page: code-fence, link and heading counts must match the source. Sourced: 16–50% of LLM-translated READMEs had structural damage.
- Label: "Translated from English with AI assistance, reviewed by <name>. The English page is authoritative. Read it in English · Report a translation problem." Check with legal first, because the contract may require German to be authoritative.
- Search: keep German unindexed until the first review pass. Use a suggestion banner and a switcher. Never auto-redirect. Check that site search handles German compounds.

### Freshness contract

- Pin fields: `source_path`, `source_commit`, `translated_on`, `translation_method`, `reviewed_by`. Pin the source commit when translation starts.
- Never copy `tested_with` or `last_verified` onto German pages. Show the source stamps only while the pin is current.
- CI step, ship in R1 (needs full git history):

  `python3 scripts/translation-drift-check.py --source docs/en --locale de=docs/de --far 5 --format csv --fail-on no-pin,unknown-pin`

- `--far 5` is the `baseline` default. Tune it after R3.
- Banner on `behind` and `far`.
- Contract change: for in-scope pages, do not fall back to English silently. English fallback could breach the contract. Instead, a `far` page gets a priority queue and an escalation to the docs lead.
- Include shared partials and snippets in the drift check.

### Ownership gate

| # | Item | Status | Closing action | Expected |
|---|---|---|---|---|
| 1 | Two independent fluent reviewers | Lotte only | Vendor with an independent quality reviewer meets this (`baseline`) | R2 |
| 2 | Critical-path pack + UI strings reviewed | Not started | Tranches R3–R6 | R6 |
| 3 | Glossary with do-not-translate decisions | None | Lotte + docs lead, seeded from the agency's own terms | R2 |
| 4 | Pin on every page + drift check in CI | None | CI step | R1 |
| 5 | Person allowed to pull or pause the locale | Unnamed | Name the docs lead. Under contract, retirement is an account-exec decision. | R1 |
| 6 | Published owner names + problem contact | None | Publish in R8 | R8 |

### KPIs and kill rule

| KPI | Pre-launch figure | Target | Control |
|---|---|---|---|
| Freshness: % of in-scope pages `current` | n/a | ≥ 80% every release (`baseline`); 100% pinned | n/a |
| Quality: reports per 1,000 views | none | set after first release | English readers on the same pages |
| Outcome: quickstart completion for German readers | record at launch | set after one release | English readers |

Kill rule: none while the contract runs, because retiring German would breach it. Replace it with an escalation. Freshness below target for two consecutive releases goes to the exec sponsor. Review the locale at contract renewal.

## Rollout schedule

Dates are approximate and `ASSUMED`.

| Release | Milestone | Owner |
|---|---|---|
| R1 (to ~13 Nov) | Contract answers. Count in-scope changes with `git log --since="3 months ago" --oneline -- <in-scope paths> \| wc -l` (read-only). Vendor RFQ. CI drift check. Name owners. | Docs lead |
| R2 (~27 Nov) | Vendor chosen. Glossary v1. German UI strings. 10-page pilot to measure real pace. | Docs lead, Lotte |
| R3–R7 | Translate in tranches: Access Control and auth first, then Ingest, then concepts. Publish to staging. | Vendor, Lotte |
| R8 (~19 Feb) | All in-scope pages done. Catch up on drift. Freeze scope. Publish owners. | Docs lead |
| R9 (~5 Mar) | Acceptance. Optionally let the agency's German-speaking technical staff review the critical-path pack. Fix findings. Dry-run the gate. | All |
| R10 (~19 Mar) | Buffer. Index German and go live. | Docs lead |

For churn, label PRs that touch in-scope paths. Batch their merges weekly, and from R8 require a translation-delta task on each.

## Open questions

Send these to the agency or contract owner.

1. Exact contract wording on "documentation": does it include API reference, release notes or screenshots?
2. Which product version does the agency deploy?
3. Must German be binding or authoritative, and must it track releases after go-live?
4. Does the agency have a style guide or glossary, such as formal "Sie" or gender rules?
5. Who accepts the German docs, and how?

Separately: do you want me to draft the vendor RFQ and the PR-label and CI setup next?