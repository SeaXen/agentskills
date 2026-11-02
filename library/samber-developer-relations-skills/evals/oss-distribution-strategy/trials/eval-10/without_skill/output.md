Quick note before the plan: you said you have a list of 25 — none was pasted into this task, so I built my own prioritized set of 25 from scratch, scoped tightly to what actually fits a 3-month-old Python CLI for OpenAPI-spec diffing. If your list differs, paste it and I'll re-rank against this same logic instead. Also: I haven't live-verified each submission form/CONTRIBUTING.md today (no web access this pass) — check each one at submission time since these rot and change often.

## Prioritization logic

Ranked by **audience fit** (would someone there actually search for "OpenAPI diff tool"?) first, **effort-to-value** second. OpenAPI-specific ecosystem beats generic Python lists beats generic dev-tool directories beats one-off community posts.

## The 25, in submission order

| # | Target | Type | How you submit | Why it's ranked here |
|---|---|---|---|---|
| 1 | **openapi.tools** | Ecosystem showcase | PR adding an entry to their data file, exact schema required | The single most qualified audience that exists for this tool — people who already work with OpenAPI specs |
| 2 | **awesome-openapi3** (GitHub) | Awesome-list | PR, alphabetical, one-liner format | Second-most targeted OpenAPI audience, low-effort PR |
| 3 | **Terminal Trove** | Dev tool directory | Web form, wants a screenshot/GIF of the diff output | CLI-specific discovery site, high-quality traffic, visual diff output demos well |
| 4 | **console.dev** | Dev tool directory | Web form, pick "CLI" + "API" categories | Curated, newsletter distribution on top of the listing |
| 5 | **awesome-cli-apps** (agarrharr) | Awesome-list | PR, correct category section | Second CLI-specific list, PR cost is low once you've done #2 |
| 6 | **best-of-python** (LukasMasuch) | Ranked/data-driven list | Usually driven by a GitHub topic tag + a PR to their project list — confirm current method before submitting | High-authority Python list, ranked by stars so it'll move as pinmarrow grows |
| 7 | **Awesome Python Applications** (mahmoud) | Awesome-list | PR | Scoped to end-user apps, not libraries — better fit than the flagship list below |
| 8 | **awesome-python** (vinta) | Awesome-list | PR into the right category (CLI/third-party API tools) | Huge reach and domain authority, but competitive and strict — do it once your entry text is polished |
| 9 | **apisecurity.io** tools roundup | Ecosystem showcase / newsletter | Email pitch, not self-serve | Breaking-change detection is exactly their beat; treat as outreach, not a form-fill |
| 10 | **LibHunt** Python trending | Dev tool directory | Mostly auto-populated from GitHub topics; claim/edit the page | Passive but compounding — costs 5 minutes once repo topics are set (see #18) |
| 11 | **AlternativeTo** | Dev tool directory | Add software entry, tag as similar to `oasdiff`, `openapi-diff`, etc. | People who already searched for a competitor land here |
| 12 | **A general "API dev tools" awesome-list** | Awesome-list | PR | Broader API tooling audience than OpenAPI-only lists |
| 13 | **awesome-testing / contract-testing list** | Awesome-list | PR | Spec diffing is a contract-testing/CI concern — different audience than "API tools" |
| 14 | **awesome-devops** | Awesome-list | PR | DevOps engineers running these in CI are a real user segment |
| 15 | **awesome-shell** | Awesome-list | PR | Broader CLI audience, lower fit than #3/#5 but easy once you have your one-liner |
| 16 | **StackShare** | Dev tool directory | Create tool profile | Low traffic today, but free and compounds once anyone "uses" it publicly |
| 17 | **PyPI classifiers/keywords** | Metadata hygiene | **Edit `pyproject.toml` / `setup.cfg` trove classifiers** (`Environment :: Console`, `Topic :: Software Development :: Testing`, relevant keywords) | Not a directory, but it's what makes PyPI's own search/browse surface pinmarrow — 10-minute task, do it same day |
| 18 | **GitHub repo topics** | Metadata hygiene | **Add topics**: `openapi`, `cli`, `python`, `diff`, `api-testing`, `breaking-changes` | Several tools above (LibHunt, GitHub search itself) are driven by topics — do this before anything else on the list |
| 19 | **r/Python** Showcase/Saturday thread | Community showcase | Forum post, follow the sub's self-promo rule for that week | Direct traffic + visibility to people who might submit you to lists you missed |
| 20 | **Hacker News (Show HN)** | Community showcase | One-shot post | Worth it only if you can frame a genuine technical angle (spec-parsing approach, diff algorithm) — a generic "I made a CLI" post gets buried |
| 21 | **Swagger/SmartBear community tools page** | Ecosystem showcase | Community wiki/form if still maintained | Adjacent OpenAPI audience, lower priority than #1/#2 |
| 22 | **Postman API Network** | Ecosystem showcase | Listing/profile | Different workflow (Postman-centric), smaller overlap but free |
| 23 | **DevHunt** | Dev tool directory | Launch-style submission | Product-Hunt-adjacent dev tool audience |
| 24 | **Awesome-list aggregators** (project-awesome.org and similar) | Passive | Nothing to do — they mirror #2/#5/#7/#8 automatically once merged | Free reach once the underlying PRs land; just don't submit here directly |
| 25 | **PyCoder's Weekly / Python Weekly** | Editorial pitch | Email submission, not a form | Long shot, high-value if picked up — low time cost to try |

## The description

You want one line, pasted everywhere. Two options, both exactly 20 words — pick whichever matches what pinmarrow actually does, since I don't have your README in front of me:

**Option A — pure diff framing (safer if there's no CI integration yet):**
> Pinmarrow is a Python CLI that diffs two OpenAPI specs and highlights every breaking change before you ship an update.

**Option B — CI-gate framing (use only if pinmarrow actually has a fail/exit-code mode):**
> Pinmarrow is a Python CLI that diffs OpenAPI specs and fails CI when a breaking API change slips in silently.

One real caveat on "paste it everywhere": the directories that get **indexed and read by AI search engines** (openapi.tools, Terminal Trove, console.dev, AlternativeTo, LibHunt, StackShare) do somewhat better with slight wording variation — identical text across many indexed pages reads as duplicate content. This matters far less than consistency does for a 210-star project, so it's a minor optimization, not a blocker — if you want it, keep Option A/B as your base sentence and only reflow word order for the two formats below rather than writing new copy.

**Formats you'll actually need to adapt to (same sentence, different length):**

- GitHub awesome-list one-liner (~15 words max):
  `- [Pinmarrow](https://github.com/<you>/pinmarrow) — Python CLI for diffing OpenAPI specs and catching breaking changes.`
- Tagline field (Terminal Trove / console.dev / DevHunt, <10 words):
  `Diff OpenAPI specs. Catch breaking changes before they ship.`
- Long description (openapi.tools entries, StackShare, AlternativeTo — 2-3 sentences):
  `Pinmarrow is a Python CLI for diffing OpenAPI specs. It compares two spec versions field-by-field and flags breaking changes — removed endpoints, tightened parameters, changed response shapes — so they're caught before release instead of in production. Built for local use and CI pipelines alike.` (adjust the CI clause if that's not accurate yet.)

## Saturday running order

Do it in this order — highest-value and PR-based items first while you're fresh, batch the quick form-fills for the afternoon slump:

1. **09:00–09:15** — GitHub topics + PyPI classifiers (#18, #17). Five minutes each, unlocks the auto-populated ones later.
2. **09:15–11:00** — Tier 1 PRs: openapi.tools (#1), awesome-openapi3 (#2), awesome-cli-apps (#5), Awesome Python Applications (#7), the API-tools and testing/devops lists (#12–14). Read each CONTRIBUTING.md before opening the PR — rejected PRs waste more time than reading guidelines up front.
3. **11:00–11:30** — awesome-python (#8) on its own: it's the strictest, give it a clean pass separate from the batch.
4. **11:30–13:00** — Terminal Trove and console.dev (#3, #4): these want a screenshot or short GIF of the diff output, so prep that asset first.
5. **13:00–14:00** — LibHunt, AlternativeTo, StackShare, DevHunt (#10, #11, #16, #23): quick form-fills, batch them back to back.
6. **14:00–14:30** — apisecurity.io and PyCoder's Weekly (#9, #25): these are email pitches, not forms — write once, send both.
7. **14:30–15:00** — r/Python post (#19), decide on Show HN (#20) separately — don't post both same-day, spread by a few days so one doesn't cannibalize the other's traffic.
8. **End of day** — log every submission in a simple sheet: date, URL, status (submitted/live/rejected), notes. Awesome-list PRs often merge days or weeks later — "submitted" is a real status, not a failure state. Check back in a week rather than re-submitting.

Skip #21, #22, #24 as active tasks today — #24 needs zero action (it mirrors your merged PRs automatically), and #21/#22 are lower priority than everything above; slot them in next time you have a spare 20 minutes.