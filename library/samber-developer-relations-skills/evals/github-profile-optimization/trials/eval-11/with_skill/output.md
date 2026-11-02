## Short answer: no, and don't put an invented one in the deck

There's no validated, published framework for "org profile page optimization" — on GitHub, Forgejo, or anywhere else. One marketing blog post coined an acronym for this a few years back; it has zero citations from other practitioners, no evidence base, and no adoption outside that single post. Naming it in a leadership deck would borrow authority the practice hasn't earned, and someone senior enough to have seen the source post will notice.

What *does* exist, and what I'd put on the slide instead of a framework name:

- **A body of adjacent research** on how developers actually read code-host profiles (Marlow & Dabbish, CSCW 2013; Montandon et al., MSR 2019) — the consistent finding is that a profile is a *verification* surface, not a discovery one. People who land on it already have a reason to be there (a talk, a crate, a job posting) and are checking whether the claim holds up. Nobody has published evidence that rewriting a profile *generates* interviews, adoption, or contributors — so don't let the deck promise that either.
- **The one figure with a disclosed methodology** (HackerRank's 2018 Developer Skills Report, 39k+ developers): portfolio/public-work weight concentrates at small and founder-led companies; recruiter forum testimony is largely indifferent to it. At 60 engineers doing mostly internal work, your primary audience for this page is other engineers and the handful of people evaluating your two Rust crates — not recruiters.
- **A star-fraud study** (He et al., ICSE '26): ~6 million suspected fake stars across 18,617 repos. Worth one line in the deck as the reason you're *not* chasing vanity metrics — it heads off the inevitable "can we just get more stars" question in the room.

If leadership wants a name for the slide, give it an honest, plain one — "Repo Surface Audit," "Org Page Fix List," whatever matches your internal naming style — and say in the same breath that it's your own checklist, not an industry standard. That's more credible in front of engineers than a made-up acronym, and it's the same posture you'd want your own docs to take.

## What actually transfers to Forgejo, and what doesn't

The tooling behind this is GitHub-specific; the reasoning isn't. Concretely, for a self-hosted Forgejo org:

| GitHub mechanic | Forgejo equivalent | Notes |
|---|---|---|
| `.github` repo, `profile/README.md` → org profile README | `.profile` repo, `README.md` → org profile README | Same idea, inherited from Gitea. Confirm your Forgejo version actually renders it — this landed a few Gitea/Forgejo releases back, and self-hosted instances lag on upgrades. |
| 6 pinned repos (public) + 6 (member-only), drag-ordered | **No equivalent.** Forgejo's org page lists repos, typically sortable by name/recently-updated/stars — there's no manual curation widget. | This is the biggest structural gap. You have exactly **one** editorial lever (the README), not two. The "which repo do I open first" job has to happen entirely in README prose — a short numbered list, flagship first — because there's no second surface to divide the work with. |
| Contribution graph, achievements | Forgejo has a personal activity heatmap for users; nothing equivalent at the org level, no achievements. | Not a decision point for your org page — skip this section of the source material entirely, it doesn't apply. |
| Image proxy (anonymizes visitor IPs to third-party widget services) | **None, by default, since it's self-hosted.** | If anyone suggests a stats/streak badge from an external service, flag that it leaks visitor IPs to that third party directly — a real reason to refuse it here, on top of the usual "it's noise" reason. |
| Verified-domain badge | Not something I can confirm exists on Forgejo. | Don't promise it in the deck; verify against your actual instance/version first. |

I don't have your instance URL or org name, so I haven't audited the actual page — everything above is the mechanism, not a finding about your content. Here's the manual version of the audit, since the script this is normally run through only talks to GitHub's API:

## Run this yourself (15 minutes)

**Blocking checks — any failure means the page is actively wrong, fix these first regardless of anything else:**

1. Does the `.profile/README.md` render at all on the org page? (Confirm the repo name, that it's not empty, and that your Forgejo version supports this — check by comparison against a repo you know renders correctly.)
2. Can a stranger, in the first screen, say what Kestrel Freight Systems builds?
3. Is every claim on the page still true today — dead links, an employee who left, a "currently building X" line about something shipped or shelved months ago?
4. Is there an obvious next click — a specific repo, docs, a contact route?

**Scored checks (rate each honestly, 0/1/2):**

- One positioning sentence, specific enough that a competitor couldn't paste it unchanged
- The two Rust crates named as entry points with a one-line "start here if..." each, since there's no pin widget to do this for you
- Every listed repo (the two public crates, at minimum) has a description and topics — a bare repo wastes the only structured metadata Forgejo gives a visitor
- Reading order: positioning → what's open source vs. internal → proof → next step, in that order, above the fold
- ≤3 visual elements total, and given the no-image-proxy point above, lean toward zero
- Readable with HTML stripped — no meaning carried only by color or an image
- An owner is named and a review trigger exists (next crate release, next hiring push) — not a calendar reminder nobody honors
- A tracked link to wherever you actually want traffic to go (crate docs, careers page, contact)

Ship when the four blocking checks pass and you're at 13/16 or better on the scored ones. Below that, don't present it to leadership as done — iterate first.

**Cold-reader test before you call it finished:** give someone who's never seen the page 45 seconds, then ask: what do we build, which repo should they open first, is this active, what should they do next, and — since you're an organization — what's open source versus commercial. Five right answers out of five is the bar. Every wrong answer tells you which section to fix (positioning, entry points, freshness, call-to-action, the open/closed line, respectively).

## The one line that will do more work than any framework name

Since you open-source two Rust crates and keep everything else internal, the highest-value single sentence on that page is a plain statement of that split: name the crates, say they're open, say the rest of the org's ~60-engineer output is internal, and don't apologize for it. That single sentence is the "S9" question this checklist asks organizations specifically, and it's the one thing a competitor's page can't paste unchanged, because it's a factual claim about *your* repo, not a slogan.

## What to put on the actual leadership slide

1. **Problem statement**, one line: the org page has drifted stale since the Forgejo migration 18 months ago and currently contradicts what a visitor would find by clicking around.
2. **What we're not doing**: chasing stars, buying activity signals, or adopting an "industry framework" — name the fake-star study and the lack of evidence for profile-driven hiring outcomes, so nobody in the room asks for either.
3. **The checklist above**, run against the real page, with the blocking/scored results filled in as evidence, not opinion.
4. **Fix order by return-per-hour**, not by how bad each issue looks: kill false claims and render-breakage first (minutes each), then the entry-point list for the two crates, then the positioning sentence, then structure — full rebuild last.
5. **Owner and review trigger** — name a person and tie the next review to the next crate release or hiring push, not a quarter-end date nobody keeps.
6. **What you'll measure afterward, and what you won't**: tagged links from the org page to crate docs are worth tracking; a stale contribution graph or star count is not, and say why in one sentence so it doesn't come back as a requested metric next quarter.

That's the whole deliverable: no framework to cite, a plain name for your own checklist if the slide needs one, the Forgejo-specific mechanical gaps against the GitHub-authored version of this method, and the exact checklist to run against the real page before the deck goes out.