# Migratr Launch Plan — Kestrel Data OSS Release

## Flag before locking the date

Three things worth resolving before you lock the 3-week timeline — none blockers, all cheap to check now, expensive to discover after the repo is public:

- **Domain + npm name-check ≠ trademark clearance.** "Migratr" being unregistered on npm and the .dev domain being free doesn't mean the name is free to use commercially. Run a quick USPTO TESS + EUIPO search before the name goes on a press release. Also grab the GitHub org, Twitter/X handle, and check no other schema-migration tool is already using "Migratr" or a confusing variant.
- **Apache-2.0 solves the *outbound* license, not repo hygiene.** Before the repo goes public: strip internal hostnames, Slack webhook URLs, CI credentials, internal ticket references, and employee emails from code, commit messages, and issue history. Run a secrets scanner (gitleaks/trufflehog) on full history, not just HEAD — if secrets ever touched the repo, squash/rewrite history rather than just deleting the file. Also audit third-party dependencies for GPL/AGPL contamination — Apache-2.0 doesn't protect you if a dependency's license is incompatible.
- **Bundling with Series A news risks cannibalizing both stories.** One press cycle, two announcements, competing for the same journalist attention — funding news usually wins, OSS launch becomes a footnote. Recommend sequencing instead: Series A lands on the wire/TechCrunch on day X, Migratr launches on HN/Reddit/dev channels on day X+1 or X+2, with the funding post linking to the OSS release as a proof point ("here's what we just open-sourced"). Ask the board which they'd rather protect.

Also decide now, since it affects Week 1 setup: **CLA or DCO for external contributors?** DCO (sign-off, no paperwork) is lower friction and standard for infra tools; CLA needs a form + likely a lawyer's ten minutes. Pick one before the first external PR arrives.

---

## Readiness gate (SLC check)

Migratr's presumably already Simple/Lovable/Complete internally — it's been running in prod at Kestrel. The gate that matters here is different: **is it complete as an *open-source* project**, not just as an internal tool? Check:

- [ ] Works from a clean clone with zero Kestrel-internal config/env assumptions
- [ ] Quick start gets a stranger to a working migration in under 5 minutes
- [ ] Docs don't assume Kestrel's specific stack/DB setup
- [ ] License, NOTICE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md present
- [ ] Issue/PR templates in place

If any of these are missing, that's Week 1 work, not launch-day work.

---

## Week -3 (this week): repo readiness + internal alignment

- **Secrets/history scrub** — gitleaks over full history, rewrite if anything's found.
- **License audit** — Apache-2.0 header on every source file, NOTICE file, dependency license scan.
- Decide **DCO vs CLA**, add the relevant bot/check.
- Write README to the OSS bar: one-liner, why-Migratr, quick start (<5 lines to value), install, examples, docs link, contributing link. Include a GIF/screenshot of an actual migration run.
- Write CONTRIBUTING.md + 5-10 genuinely approachable "good first issue" tickets — don't launch with zero ways to contribute.
- Set GitHub repo topics (schema-migration, database-tools, devops, etc.), a one-line description, social preview image.
- **Coordinate with whoever owns Series A comms** — lock the sequencing decision (bundled vs. staggered) this week, not week 3. This determines your embargo dates for press.
- Trademark spot-check on "Migratr" (30-minute TESS search) — flag to legal if anything looks contested.

## Week -2: content + channel prep

- Write the launch blog post: "Why we open-sourced Migratr" — real motivation (dogfooded at Kestrel for [X time], solving [specific pain]), not generic OSS-goodwill copy.
- Draft HN "Show HN" post (descriptive title, no hype) and a first comment explaining the technical backstory — this is what HN readers actually engage with.
- Draft 2-3 subreddit posts (r/database, r/devops, whichever fits) — read each subreddit's self-promo rules first.
- Draft launch thread for X/LinkedIn: problem → solution → demo GIF → link.
- Identify 3-5 people/newsletters in the data-infra space who might genuinely find this useful (borrowed channel) — send them early access this week, not launch day, so they have something to say when it goes live.
- Set up GitHub Discussions for Q&A.
- If Series A is being staggered, finalize both press embargoes now with your comms/PR contact.

## Week -1: dry run + internal roll call

- Full dry-run: fresh clone, fresh machine, follow your own quick start literally — fix every point of friction.
- Confirm CI is green and public (badge in README).
- Brief the whole 60-person team: what's launching, when, and ask everyone to like/share/comment on launch day — coordinated but not fake (no bot engagement, no vote manipulation on HN — it gets launches killed).
- Schedule social posts, but plan to post the HN/Reddit ones live, not scheduled (need to be present to respond).
- Final check: no leftover internal Slack/Jira links, no internal-only badges, LICENSE file matches what's stated in the README.

## Launch day

Aim for Tuesday-Thursday, ~6-8am PT for HN.

- Post to HN first, first comment ready with the "why we built this" context.
- +1-2h: publish blog post, push the X/LinkedIn thread.
- +2-3h: post to the chosen subreddits.
- All day: respond to every comment, everywhere, in real time — this is the actual job today, not a checkbox.
- If staggered from Series A: cross-link — funding post references Migratr, Migratr post/README references the funding news as context ("we just raised our Series A and we're marking it by open-sourcing the tool we built to solve X").
- Send the internal team the direct links so they engage genuinely, not a copy-paste blast.

## Post-launch (weeks +1 to +4)

- Week +1: triage every issue/PR that came in, fix anything embarrassing fast, thank every contributor publicly.
- Week +2: "what we learned from the launch" follow-up post — genuinely useful retention content, cheap to write, keeps momentum.
- Week +3-4: ship one visible improvement based on launch feedback and announce it — signals the project is alive, not a one-and-done PR stunt.
- Track real signals, not vanity ones: issue/PR velocity and returning contributors matter more than star count.