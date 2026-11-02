# Launch plan — Migratr (Kestrel Data)

**Most urgent action, do today:** start trademark search + reserve handles. 3-week window barely covers this. Every day lost here eats fix-time on the real blockers (hygiene scrub, cold run).

## Verdict: go with reduced scope, conditional

Not ready yet. No hard blocker looks unfixable in 3 weeks, but 2 are compressed dangerously tight: name clearance (needs 8wk, has 3) and git-history hygiene (internal tool, first public exposure). Rest of checklist status unknown to me — I have no repo access, so install/first-success/README gate is unverified. Team must cold-run it themselves, week 1.

## Assumptions (confirm or correct — I inferred rather than asking one by one)

- Audience: both individual devs and company evaluators. Schema-migration tooling reads as infra/dev-tool with cross-language appeal.
- Anchor-audience geography: mixed US/EU. Confirm — sets posting hour.
- Press wanted, tied to Series A. If not, drop that track, redirect week 1 hours to hygiene scrub.
- CLA vs DCO: not decided. Recommend DCO — lighter, Apache-2.0 already grants patent rights, no reason for a CLA on a "free forever" project.
- Real differentiator vs golang-migrate, Flyway, Atlas, Bytebase, Liquibase, Sqitch: unknown to me. Needed before Step 3 locks — do not launch without a true, specific answer.

## ⚠️ "No legal angle" — wrong on two points

1. **Domain + npm check ≠ trademark clearance.** You checked 2 surfaces. Real clearance: USPTO TESS, EUIPO, WIPO Global Brand Database, plus common-law search (GitHub, Google, Product Hunt, SourceForge) for phonetic/visual/conceptual near-matches — "Migrator," "Migratrix," etc. Also check `.com` (someone may hold it even though `.dev` was free) and whether any live company, software or not, trades as "Migratr." Free distribution still counts as use in commerce (*Planetary Motion v. Techsplosion*) — "we're giving it away" is not a defense. Any colorable conflict = rename now, before more assets lock the name in further, not a risk you carry into launch.
2. **Git history hygiene.** This tool ran inside Kestrel for a while before anyone planned to open it. Full history — not just current tree — likely has internal hostnames, customer schema names, internal service refs, maybe stray creds in old commits. Scrub with `git filter-repo`/BFG, or cheaper: re-init public history from a clean squash. Decide which this week; this is the one blocker most likely to actually bite.

Apache-2.0 itself: fine, no relicensing risk (already max-permissive, nothing to fork over). Check dependency licenses are compatible for redistribution while you're in there.

## Clearance

| Item | Status | Action |
|---|---|---|
| Trademark | 🔴 not cleared | Full search this week (see above), go/no-go by Sep 29 |
| Domain, GitHub org, social handles | ✅ domain done | Reserve GitHub org, npm name, X, LinkedIn company page today — before repo goes public |
| License | ✅ Apache-2.0 | Verify LICENSE file matches README claim + dep compatibility |
| CLA/DCO | 🔴 undecided | Recommend DCO, decide before first external PR |

## Positioning

Formula: `Migratr is a <category> for <audience> that <capability the alternatives lack>`.

Placeholder — fill with a real, defensible answer, don't launch on a vague one:

> "Migratr is a schema-migration tool for [audience] that [specific capability golang-migrate/Flyway/Atlas/Bytebase don't have]."

Answer "why not golang-migrate / Flyway / Atlas / Bytebase / Liquibase" explicitly, in the README and in the first comment. Dodging it loses to the incumbent by default — staying with what they have costs the reader nothing.

Claim you can already defend honestly: internal production use at Kestrel Data (state since when, rough scale — only if literally true).

Three claims to pre-answer before critics ask (this audience probes infra tools hard):
- Rollback / partial-failure story — what happens mid-migration on failure.
- Dry-run support.
- Auth model — how it talks to the target DB, what permissions it needs.

## Audience & assets

Both individual and company adoption in scope (assumption above).

- Individual: quickstart, demo (asciinema/GIF of a real migration run), zero-config default.
- Company: comparison page (real numbers, at least one row you lose), security policy, release cadence statement, "Apache-2.0, free forever, nothing closed" statement up front — this doubles as Series-A credibility material.

## Shape: single spike

One project, one story. No caravan — no multi-item backlog or conference date given. Keep it that way; a caravan below 3 announceable items just dilutes.

**Keep the Series A news and the Migratr launch as two separate posts, cross-linked.** Skill's own weak-title example is literally "Show HN: Our startup raised $4M" — funding announcements read as ads on HN and get penalized. Company blog post carries the Series A + open-source framing; Show HN carries the tool, technical, first-person, no funding mention beyond maybe one line.

## Channels

| # | Channel | Effort | Notes |
|---|---|---|---|
| 1 | Repo public, tag, package registry, description/topics/social preview | near-zero | T-0, mandatory, nothing else matters if install breaks |
| 2 | Show HN + first comment + stay in thread | most of day 1 | Anchor. Title: `Show HN: Migratr – <plain description>`. No superlatives |
| 3 | Secondary: r/programming, r/database, relevant language sub, Lobsters, DEV.to | ~1hr each | Staggered T+2-6h and T+1-2d. Rewrite context per community, never paste same blurb |
| 4 | Team + company social (esp. LinkedIn — company evaluators read there) | near-zero | T+30-90min, link to the discussion not a duplicate |
| 5 | Newsletters (Changelog, relevant DB/lang weekly, awesome-lists) | ~1hr/outlet | Submit this week — most publish on a lag |
| 6 | Long-form write-up | deleted from launch week | Fixed date kills it here. Push to T+3-10d as second wave — durable value, worth doing once the thread cools |

Product Hunt: optional secondary at most. CLI tool, no strong visual — low priority, skip unless someone wants to own it for the SEO durability.

## Timeline (today = 2026-09-24, target launch Wed 2026-10-14)

**Week 1 (Sep 24–30)**
1. Today: start trademark search, reserve all handles, start press outreach (3wk lead starts now if wanted), assign DRIs, decide DCO.
2. Sep 29: trademark go/no-go. Rename now if needed, not later.
3. Sep 24–30: git-history hygiene scrub, dependency license audit, draft SECURITY.md/CONTRIBUTING.md/issue templates.

**Week 2 (Oct 1–7)**
4. Cold-run install/quickstart with a Kestrel engineer who's never touched it. Fix every hesitation, re-run.
5. Draft positioning, comparison table, company-adoption pages, anchor post + first comment + 3-4 pre-answers.
6. Draft company blog post (Series A + open source), kept separate from Show HN copy.
7. Submit newsletters/curated lists.

**Week 3 (Oct 8–14)**
8. Oct 8-9: re-run cold run with fixes applied.
9. Oct 13 (T-1): freeze branch, capture baseline (see below), full pre-flight checklist, confirm no meeting-heavy morning for Voice/Triage.
10. Oct 14: launch. Repo public + tag + package at T-0. Show HN + first comment within 2 min. Blog post live same morning, cross-linked not merged. Social T+30-90min. Secondary staggered T+2-6h. War room active T+0-4h minimum, hourly checks to EOD.
11. Oct 15-21: ship fixes surfaced, cut patch release, fire long-form write-up + remaining secondary + missed newsletters, thank contributors by name.

## War room

Kestrel has ~60 people — don't run this solo-maintainer style. Assign named DRIs:

- Voice: tool author, owns the HN thread, one person for tone consistency.
- Triage: separate person, incoming issues/PRs, same-hour fixes.
- Amplifier: secondary posts on schedule.
- Watcher: metrics + link/uptime checks.
- Comms/PR: coordinates Series A press timing against the Migratr post so neither cannibalizes the other.

Escalation path named in advance: who can commit publicly to roadmap/licensing statements. Everyone else defers.

Security report protocol if one lands in the thread: stop public discussion, point to SECURITY.md, move private, patch, credit on publish. Needs SECURITY.md live before Oct 14, not written in reaction.

## Measurement

Baseline is effectively zero (new public repo) — capture instead: internal usage numbers you can cite as a claim (only if true), current empty state of stars/downloads for delta tracking.

- Day 1 (Oct 14): HN rank/comments, stars/hr, unique cloners, referrer mix.
- Day 7 (Oct 21): package downloads vs 0, sustained cloners, external issues (strongest early signal), secondary pickups.
- Day 30 (Nov 13): retained download run-rate, first external PR, dependents, posts/talks built on it.

Report stars as bookmarks, not adoption. Downloads/retention are the real number for the board.

## Risks

1. 🔴 Name clearance compressed to <8wk — late conflict forces rename after Series A press already used the name. Fix: search closes by Sep 29, before further asset lock-in.
2. 🔴 Git-history hygiene, first public exposure of an internal tool — real secret/customer-data leak risk. Fix: full-history scrub or clean re-init, decided this week.
3. ⚠️ Merging Series A news into the Show HN post reads as PR, risks flag/kill on HN. Fix: two posts, cross-linked, never merged.
4. ⚠️ Schema-migration tools touching prod DBs draw hard technical scrutiny (rollback, dry-run, auth). Fix: pre-answer in README + first comment.
5. ⚠️ Press-driven overperformance hits a small core team. Fix: agree issue-volume trigger for templates/thread-lock before Oct 14, use rest of the 60 for triage backup.

**Next action:** kick off trademark search today, and tell me the real differentiator vs golang-migrate/Flyway/Atlas/Bytebase so Step 3 (positioning) can lock.