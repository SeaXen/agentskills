Read the skill and its four references in full (`channel-catalog.md`, `coverage-audit.md`, `distribution-plan-example.md`, `published-findings.md`). Two things in the plan as described trip named failure modes in the skill before I even get to prioritizing, so I'm addressing those first rather than silently complying, then giving you the actual reworked deliverable. (WebSearch/WebFetch aren't authorized in this session, so I couldn't pull pinmarrow's live PyPI/GitHub page or verify the 25 URLs — flagged inline wherever that matters.)

---

## Two flags before Saturday

**"25 in one weekend" is the skill's textbook spray-and-pray case.** Per the worked example in `references/distribution-plan-example.md`, a "directory sprint (20+ submissions)" is a named *Refused* item: at low maintainer-hours, the quarterly sweep alone eats the budget, and stale listings actively damage the project rather than sitting neutral. Curated lists (family 3) are explicitly a **harmful-decay** channel — a dead link or a description that predates your next release doesn't fade quietly, it tells every future reader nobody's home. 25 listings means 25 things you now owe a quarterly check to, forever, for one maintainer's spare hours.

**"One description pasted everywhere" is a named trap for this exact family** ("one description reused verbatim everywhere," `channel-catalog.md` §3). Different surfaces score differently — an awesome-list entry has a fixed one-line shape, a directory has a paragraph field, a showcase site often wants a differentiator sentence. A single blob reads as thin copy on the ones expecting more, and looks copy-pasted to a curator who's seen the same line on three other lists this month.

Neither kills the Saturday push — it means: fewer, verified, well-matched submissions, one base description with 3 format variants, and a sweep date written down before you start.

## Foundation check (do this before any submission — ~20 min)

Every listing will send evaluators back to pinmarrow's own surfaces. Confirm these are current first (Step 1 of the skill, non-negotiable):

- PyPI page: description matches current positioning, all classifier/keyword fields filled, docs/repo/changelog links present.
- README first screen: states what it diffs (OpenAPI 2 vs 3? YAML/JSON both?), one install command, no stale screenshot.
- GitHub topics set (`openapi`, `cli`, `python`, `api-tooling`, `diff` — whatever actually matches).

If any of these are half-done, fix them first — a directory link pointing at a thin PyPI page wastes the listing.

## Applying the adoption test to "curated lists," for pinmarrow specifically

| Question | Answer for this family |
|---|---|
| Recurring cost | 30–60 min per submission entered correctly the first time; ~15 min per listing per quarterly sweep |
| Decay behavior | Harmful — dead link, stale "v0.x" mention after your next release, superseded name |
| Observable signal | Referral arrivals per listing (repo traffic → referring sites, if you have that panel open) |
| Kill date | Recheck every quarter; a listing with no measurable referral after 2 sweeps gets dropped or removed |

That sweep obligation is the real cost of 25 — it's not the Saturday, it's every quarter after.

## Scoring rubric — run every item on your 25 through this

Straight from the skill's selection test (`channel-catalog.md` §3). Score each yes/no; anything scoring 3/5 or below goes to Refused, not "later":

1. **Do target developers actually browse it** (not just "it exists")?
2. **Is the link dofollow on a domain with real authority?**
3. **Was it touched recently** (commits/updates in the last ~3–6 months)?
4. **Are comparable projects already listed** (openapi-diff tools, spec-linters, API-contract-testing CLIs)?
5. **Can arrivals from it be measured** (referrer visible in your traffic panel)?

A list that "accepts anything" or hasn't merged a PR in a year fails #1 and #3 regardless of its domain authority — that's the generic-directory trap named explicitly in the skill.

## My read of the space for this niche (I can't see your actual 25 — cross-check these against it)

Since I couldn't verify your list, here's a tiered read of the surfaces I'd expect to score highest for a Python OpenAPI-diff CLI, individual-developer adoption. Confirm each URL and its `contributing.md` yourself before submitting — list rules change without notice.

**Tier A — submit this Saturday (targeted, active, comparable projects already there):**
- **openapi.tools** — the category's own curated directory, not a generic list. Highest-fit single entry on this whole exercise; check its submission format (usually a PR to its own data file).
- **An "awesome-openapi" / "awesome-openapi3"-style GitHub list**, if one is current — verify it's been merged into recently, not abandoned since OpenAPI 3.0.
- **Awesome Python** (`vinta/awesome-python`) — huge audience, but only if there's a CLI-tools or API-tools section where a diff tool fits; match the exact entry format from its `contributing.md`.
- **Awesome CLI apps** list (e.g. `agarrharr/awesome-cli-apps`) — check recent merge activity first.
- **Terminal Trove** — an actively maintained CLI-tool showcase with its own submission form; good fit for a terminal-first tool.
- One CLI/dev-tools weekly roundup or directory specific to Python if you already know one is active (LibHunt-style trending pages count as low-effort, low-certainty; treat as Tier B).

**Tier B — test ring, 2–3 max, time-boxed to end of next quarter:**
- Directory/comparison sites like AlternativeTo or Stackshare — real domains, but audience overlap with "CLI diff tool for OpenAPI" is unproven. Set a signal (referral arrivals >0 within 60 days) and an end date; drop if it doesn't clear it.

**Refuse outright, name the reason, don't park at the bottom:**
- Any "top 100 dev tools 2026" SEO-farm site with no visible curation, no contributing process, and no recently merged entries — fails criteria #1 and #3 above regardless of what's on your list under that shape.
- Generic "submit your startup" directories with a paid-placement upsell and no visible browsing audience — named trap, "paid placement with no visible audience."
- Anything you can't find a `contributing.md` or recent merged PR for — you can't verify it's alive, and a stale listing is worse than no listing.

That's realistically **6–9 submissions**, not 25 — matching the skill's own claim that "three maintained surfaces outperform twenty stale ones and cost less."

**Before self-submitting to any GitHub-hosted awesome-list**, fix one unrelated thing in it first (a dead link, a stale entry) — `channel-catalog.md` explicitly notes this improves reception of your own entry afterward and costs less than the submission itself.

## Submission text — base description + format variants, not one blob

Base (yours to refine, ~19 words):
> pinmarrow is a Python CLI that diffs OpenAPI specs, flagging breaking changes, added/removed endpoints, and schema drift before deploy.

**Awesome-list format** (fixed shape per `sindresorhus/awesome` convention — match this exactly, don't editorialize):
```
- [pinmarrow](https://github.com/<org>/pinmarrow#readme) - Diffs OpenAPI specs from the CLI, flagging breaking changes and schema drift before deploy.
```

**Directory / showcase paragraph** (1–2 sentences, room for the differentiator a one-liner can't carry):
> pinmarrow is a Python CLI for diffing OpenAPI specs — it flags breaking changes, added/removed endpoints, and schema drift so you catch API contract breaks in CI, before they hit production.

**Short tagline** (character-capped fields, e.g. a directory's "one-line pitch"):
> Catch breaking API changes before you ship them.

Use the awesome-list line verbatim where the format is fixed; use the paragraph where there's a free-text field; never drop the paragraph into a fixed-shape awesome-list entry — that's the mismatch curators reject on sight.

## Revised Saturday plan

1. **Morning (~30 min):** foundation check above.
2. **Next ~3 hrs:** Tier A submissions, one at a time — read each `contributing.md`, match its format, make the one unrelated fix first where it's a GitHub-hosted list.
3. **Log Tier B as a test ring**, not submitted today: pick 2, set the 60-day signal and end date now, in writing.
4. **Write down today's date as sweep-date-minus-one-quarter** for every Tier A listing you land — that's the debt you're taking on.

## Threshold check

- Stale/incomplete foundation fixed before new listings ✓ (pending your confirmation)
- Total submissions sized to what a quarterly sweep can actually hold, not to the list's original count of 25 ✓
- Every accepted channel has a cost, a signal, and a review date — not just a URL ✓
- One base description, format-adapted per surface rather than pasted verbatim ✓