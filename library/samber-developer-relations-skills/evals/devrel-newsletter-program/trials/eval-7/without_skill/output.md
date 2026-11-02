**Next action:** create `docs/newsletter/` in the Larkspur repo and paste in the template from step 3 below. About 20 minutes.

I didn't run a full interview. The DevRel skill collection has no newsletter skill, so this answer comes from your constraints alone.

## Recommendation

Run a **monthly project digest**, written once and published in two places:
- The canonical copy is a markdown page on your own site, with RSS.
- The email goes out from the same markdown through Buttondown.

Don't run a curated Kubernetes-ecosystem news roundup. Curation costs more than 3 hours a month, and many existing newsletters already do it. Your only unfair advantage is the inside view: what the Tuesday triage decided, what shipped, and what needs help.

**Why monthly.** One person with no backup can't sustain a weekly or fortnightly cadence. A monthly digest rolls up the weekly merge threads you already have, so most of the raw material is written. A missed month is also cheap to recover from.

**Why it compounds.**
- Each issue is an indexed permalink on your own domain, so the archive grows in search value.
- The "Help wanted" section feeds contributor recruitment every issue.
- The "Decisions" section is a public record of why Larkspur works the way it does. Nobody else can write it.

## Issue format (5 sections, fixed order)

1. **One thing to know.** A release, a breaking change, or a deprecation. Write "Nothing this month" if there is none.
2. **Merged.** The 5–8 most meaningful PRs from the weekly threads, each with one sentence on why it matters and the contributor's handle.
3. **Decided in triage.** Decisions made, questions still open, and where to weigh in. This is the section nobody else can copy.
4. **Help wanted.** 3–5 issues, each with size, a mentor name, and a link.
5. **Next release.** The expected scope and a rough date.

Keep each issue to a 5-minute read. Do not add more sections.

## Setup (about 4 hours, one time)

1. **Pick the platform (30 min).** Use Buttondown, which takes markdown and has an API and RSS. Put the canonical page on your site at `/newsletter/YYYY-MM`.
2. **Capture inputs during the year (10 min).** Add a standing "newsletter notes" item to the Tuesday triage agenda. The note-taker writes down decisions as they happen. This turns a 3-hour scramble into a small habit.
3. **Write the template (45 min).** Create `docs/newsletter/TEMPLATE.md` with the five sections as empty headings. Put the monthly runbook in `docs/newsletter/RUNBOOK.md`. Make it good enough that a stranger could run an issue from it.
4. **Add signup surfaces (45 min).** Add the signup link to the README, the docs site footer, a pinned Discussion, and the release-note footer.
5. **Backfill issue 1 (about 3 hours, counts as your first issue).** Cover the last 2–3 months. A first issue with real content beats an announcement.
6. **Pilot quietly.** Send 3 issues to early subscribers before you promote it widely.

## The 3-hour budget per issue

| Task | Time |
|---|---|
| Collect: skim the weekly threads and triage notes | 30 min |
| Draft all 5 sections | 70 min |
| Contributor review: a 48-hour comment window on a draft PR | 15 min of your time |
| Edit | 25 min |
| Publish and share (site, email, Discussions) | 20 min |
| Buffer | 20 min |

## The no-backup problem

You can't fix this by finding a backup now. Design around it instead:

- **Skip rule.** If a month is missed, publish a two-line "skipped this month" note. Never go silent.
- **Pause rule.** After two missed months, announce a pause openly and don't let it die quietly.
- **Runbook in the repo** (step 3), so anyone can pick it up.
- **Section ownership as the on-ramp to a backup.** Ask one triage regular to own "Help wanted", and another to own "Merged" notes. Whoever does it three times in a row is your candidate backup. Offer them a co-byline.

## Measure only three things

Set baselines after issue 3. Don't set targets before that.
1. **Subscriber growth** month over month.
2. **Help-wanted clicks**, and how many of those issues get claimed within 14 days.
3. **First-time contributors** who say they found their issue through the newsletter. Add an optional "How did you find this issue?" line to the PR template.

Ignore open rates. Mail-client privacy features inflate them.

**Kill or change rule.** If help-wanted clicks stay near zero for 3 issues in a row, change the format. Don't just push on.

## Not now

- **Weekly cadence.** Revisit it only once a named backup exists.
- **Sponsor slots or ads.** Revisit them after the list has a baseline.
- **Ecosystem news section.** Add it only if readers ask for it.

Next action: do step 3 now. Paste the five section headings into `docs/newsletter/TEMPLATE.md`.