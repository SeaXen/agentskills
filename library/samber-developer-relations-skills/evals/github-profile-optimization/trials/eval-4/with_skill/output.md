Followed `github-profile-optimization` (SKILL.md + all four references) end to end. One caveat up front: I can't run `scripts/profile-audit.py` against a real account here — "Thornpike Data" has no live GitHub org I can query, and even if it did, pin data needs a `GITHUB_TOKEN` I don't have. Everything below is built from what you told me (org page = bare repo list, i.e. no `.github` README exists, pins are unset) plus reasonable assumptions I've flagged inline. Confirm or correct those before you ship.

## Where the file goes

Two variants, pick based on who should see it:

| Variant | Repo (must be exact name) | Path | Visible to |
|---|---|---|---|
| Public org profile | `.github` — **public** repo | `profile/README.md` | Everyone, logged out included |
| Member-only | `.github-private` — private repo | `profile/README.md` | Signed-in org members |

You want the public one. Skip the member-only variant — nobody's been named as its owner, and an unowned internal page just rots faster than the public one, invisibly.

**Mechanical setup, in order:**
1. **Create a public repo named exactly `.github`** under the Thornpike Data org (org owners only — pins and this repo both require owner permission).
2. **Add `profile/README.md`** with the content below.
3. Fill the org's **bio field** (160-char limit) with a compressed version of the positioning line, not the full sentence.
4. **Verify your domain(s)** (thornpikedata.com and any `www.` variant used in the org's website/email fields) via DNS TXT record — up to 72h to propagate, adds a "Verified" badge next to the name.
5. **Set 6 public pins deliberately** — see below. Leave them unset and GitHub auto-fills "Popular repositories," which routinely surfaces something abandoned.

## Scoring the current state (blocking checks)

An org page that's "just a repository list" fails the checks that matter most:

```
B1 renders             FAIL — no .github public repo exists, so there's no README to render
B2 identifiable        FAIL — repo list alone names no sentence a visitor can read
B3 claims true         PASS (vacuous — nothing false is currently claimed, because nothing is claimed)
B4 next step           FAIL — org-specific blocking rule: visitor must know which repo to open
                        first without scrolling into the list; a bare list doesn't answer that
```

Nothing here needed guessing — it follows directly from "just a repository list." Good news: all four are the top of the fix-order ratio (false claims / render prerequisites tie for cheapest-and-highest-value), so this is an afternoon of work, not a project.

## Pushing back on the four items marketing wants ported

Your instinct is right, and the skill names this exact failure mode: *"Writing the organization profile as a second marketing site — the visitor came to GitHub for the code."* Here's what each item becomes on this surface instead of a straight port:

- **Hero line → the one positioning sentence**, not marketing copy as-is. It has to survive one test: could a competitor's GitHub org paste it unchanged? A homepage hero line is usually written to pass through marketing review, not that test. I drafted three candidates below — pick one, or send it back to marketing with that constraint attached.
- **Three customer logos → cut.** Logo images are decoration that counts against a 3-element budget, and they're the specific thing this skill warns readers discount: reviewers here want checkable adoption evidence (named users in prose, download counts, release cadence), not a logo strip. If the three customers are nameable publicly, one line of prose ("in production at X, Y, Z") replaces the logos at zero visual cost and is actually stronger evidence. If they're not nameable without a case-study sign-off, drop the claim entirely rather than illustrate it. Logos belong on the homepage, which is built for that; the GitHub visitor didn't come here for a trust badge wall.
- **Product tour → the repo entry-point list.** This *is* the tour, translated for this audience: not screenshots, but "open this repo first, then this one" against the actual runtime architecture. That's the section below titled "Start here."
- **Careers CTA → demoted, not deleted.** The skeleton rule is one primary CTA, not three of equal weight — "docs, blog, Discord, Twitter, newsletter, careers" all bolded together is the named weak example. Question 4 (who lands here) matters: most visitors to an org page with three OSS runtime repos are developers evaluating whether to depend on them, not job seekers — so docs should be the bolded primary route, and careers becomes one small line at the bottom. If hiring is genuinely the current priority (active urgent headcount push), that's a legitimate override, but it should be an explicit decision, not a default win because it was on the homepage.

## Positioning sentence — three candidates, pick one

1. **Mechanical**: "The stream-processing platform for real-time event pipelines — ingest, query and connectors run as open source; the managed service is what you pay for."
2. **Problem removed**: "Thornpike removes the operational burden of running your own streaming stack — the runtime is open source, so you can see exactly what you're depending on."
3. **What the reader can stop doing**: "If you're maintaining a hand-rolled streaming stack, Thornpike lets you stop babysitting it — three of its runtime components are open source, so nothing about it is a black box."

**Recommend #1.** It names the category, the surface area, and the licensing stance in one breath — same shape as the Supabase example the skill cites ("The Postgres development platform — hosted Postgres with auth, storage and realtime, most of it open source"), and it's the easiest of the three to falsify-check against the repo list itself.

## The README (drop into `profile/README.md`)

Bracketed items are facts only you have — real repo names, license, actual URLs. Everything else is ready to ship as written.

```markdown
# Thornpike Data

The stream-processing platform for real-time event pipelines — ingest, query and
connectors run as open source; the managed service is what you pay for.

## Open source vs. commercial

- **Open source (<LICENSE, e.g. Apache-2.0>)**: [`<ingest-runtime-repo>`](<url>),
  [`<query-engine-repo>`](<url>), [`<connector-sdk-repo>`](<url>) — the runtime
  components. Run them yourself, read them, fork them.
- **Commercial**: the managed service, control plane, and enterprise features
  (SSO, multi-region, support SLAs). That's Thornpike the product, at
  [thornpikedata.com](<url>).

## Start here

- [`<ingest-runtime-repo>`](<url>) — start here if you want to see how events get
  into the platform.
- [`<query-engine-repo>`](<url>) — start here if you're evaluating processing
  semantics or throughput.
- [`<connector-sdk-repo>`](<url>) — start here if you're writing a source or sink
  connector.

**[Read the docs →](<docs-url>)**

Questions or bugs: open an issue on the relevant repo above. Elsewhere: we're
hiring — [careers](<careers-url>).
```

Notes on what's deliberately absent: no stats widgets, no streak/trophy cards, no visitor counter, no logo strip. None of the three shipped-org profiles the reference file documents (Supabase, Grafana Labs, Vercel) use any of those either — all three lead with a one-line positioning statement and a verified domain badge instead.

## Pins (6 public slots)

Pins should extend past what the README prose already names, not repeat it — that's the difference between an "entry-point tour" and a leaderboard:

1–3. The three OSS runtime repos (still fine to pin what's named in prose — the rule is against wasting *all six* slots on repeats, not against any overlap).
4. A quickstart/examples repo, if one exists — the fastest path from curiosity to a running thing.
5. A client library or the repo that best shows engineering judgement at low stars — this is the one credibility/hiring readers actually weigh.
6. Whatever else genuinely helps someone get from zero to running — never an archived repo, a barely-modified fork, or an empty placeholder to fill the slot.

Give every pinned repo a description and topics before pinning — a bare pin wastes the slot (scored check S3).

## Before you ship

- Hit **all 4 blocking checks** plus **13/16** on the scored checklist (S1–S8, full list in `references/profile-scorecard.md`) before publishing — don't ship with a caveat below that line.
- Run the **cold-reader test**: 45 seconds on the page, then ask someone with zero context five questions — what does this org do, which repo do I open first, is this active, what do I do next, what's open source vs. commercial. Five of five is the pass; a fresh Claude session with no prior context on the account is an acceptable stand-in if no person is free.
- **Name an owner and review triggers**, not a calendar reminder: next OSS runtime release, a newly-nameable customer, a careers-page change, a funding announcement. Put that list as a comment at the bottom of the README source so it travels with the file.
- Since you (eng lead) are driving this against marketing's original ask, get a one-line sign-off from marketing specifically on the open-source/commercial wording and the careers link — not the whole page, just the two spots where their scope and yours actually overlap.

## What not to bother tracking

Skip a view-counter badge (counts bot/proxy image loads, not visitors) and skip watching star count after shipping (unattributable, and known to track promotion rather than the page). If you want one real number: a tagged link from the README to your docs — that's the only metric here whose data you actually own.