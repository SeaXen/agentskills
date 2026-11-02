**Do first:** tell the growth lead and Moorhen "no" to the contributor-email mailing and the 50k CSV. Then ship the CLI survey message in your next release.

## ⚠️ Timeline problem

10 weeks from today (2026-10-23) lands on 2027-01-01, in the press dead zone. Move publication to Tue 2027-01-12 and add 2 slack weeks. Fielding stays the same. Decide this before week 1.

## Ranking

Yields are my assumptions, not data. Recalibrate after the week-3 pilot numbers.

| # | Channel | Verdict | Est. clean completes |
|---|---|---|---|
| 1 | CLI first-run message (60k MAU) | Do | 100–400 |
| 2 | Newsletter (12k), 3 sends | Do | 150–350 |
| 3 | Moorhen sends to its own list | Do, reframed | 100–400 |
| 4 | Discord (9k) | Do | 100–250 |
| 5 | GitHub surfaces (README banner, pinned Discussion, release notes) | Do | 50–150 |
| 6 | Third-party communities (HN, Reddit, Lobsters, Mastodon, other maintainers) | Do, wave 2 | 100–500, high variance |
| 7 | LinkedIn ads | Small test only | about 60 per $1.5k |
| 8 | Contributor emails from git log | ❌ No | none |
| 9 | Moorhen 50k CSV mailed by you | ❌ No | none |

Expected total is about 800–1,800 completes before cleaning. Target at least 800 clean ones.

**Why the two ❌:**
- **Git-log emails:** people gave those addresses for commit attribution, not marketing. That is cold mail without consent, which is a GDPR problem and a bad look for a 30k-star project. Replace it with a README banner and a pinned Discussion.
- **Moorhen CSV:** those contacts consented to Moorhen, not to Driftwood. You would need your own lawful basis, and spam complaints would hurt your newsletter's deliverability. Ask Moorhen to send to its own list, from its own sender, with your copy and a unique link. No data changes hands. Get written confirmation of their opt-in basis, plus their send count and open rate afterward.

**LinkedIn, $8k plan:**
- Spend $1.5k in week 3 on a test aimed at developer job functions outside your current users.
- Judge it by cost per *qualified* complete (it must pass a screener question).
- Scale to $4k at most, and only if that cost stays under about $15. Otherwise sponsor 2–3 developer newsletters instead.
- Put $2k into a charity pledge: "we donate $X per complete, up to $2k". It avoids a cash-prize fraud magnet.
- Hold the rest unspent as reserve.

## Setup list, in order

1. **Survey tool (about 1 day).** Pick one with EU data hosting and CSV export.
   - Draft the questions in 2–3 days.
   - Pilot with 20 people from Discord.
   - Cap it at 10–12 minutes.
   - Use plain English, because many respondents are non-native speakers.
2. **Redirect link (about 1 hour).** Put a short redirect on your own domain, so you can retarget it or show "survey closed" after the CLI ships. Add one `src=` tag per channel: `cli`, `nl1`, `nl2`, `discord`, `gh`, `moorhen`, `hn`, `li`.
3. **CLI message (2–3 days of work, plus waiting for a release).** Details:
   - Print one line, once per release, on first run.
   - Print only when the session is an interactive TTY and not CI.
   - Write to stderr.
   - Respect `DO_NOT_TRACK` and a dedicated opt-out env var.
   - Collect no identifiers.
   - It must ship in a release by end of week 2. If your cadence is slower, cut a patch release.
4. **Newsletter plan.** Send on week 3, week 5, and a final call in week 6. The reminders go to non-clickers only.
5. **Discord and GitHub (about 2 hours).** Announce and pin in Discord, and ask the mods to cross-post. Add a README banner and a pinned Discussion on GitHub.
6. **Moorhen agreement.** Send them the copy, the unique link, and a send date in week 4.
7. **Quality controls.**
   - Minimum completion time.
   - One attention-check question.
   - Cookie plus hashed-IP duplicate detection.
   - A "did you already answer this?" question, because the owned channels overlap.
8. **Privacy.**
   - Write a short notice.
   - Collect no email by default.
   - Use a separate, optional checkbox for "email me the results".
   - Set a retention date.
9. **Daily tracker.** One sheet with completes per `src`, checked every morning.
10. **Methodology page, drafted before launch.** Say plainly that the sample is self-selected, English-only, and skewed toward Driftwood users. Report results by source. Do not claim "representative". Press asks for this first, and the Moorhen and third-party channels exist to reduce the owned-channel skew.

## Schedule (W1 = week of 2026-10-26)

- **W1–2:** items 1–3 and 7–10. Ship the CLI release.
- **W3–6:** fielding. Week 3 is the pilot and first newsletter. Moorhen sends in week 4. Third-party communities and the LinkedIn test run in weeks 3–4.
- **W6:** close the survey and flip the redirect.
- **W7–8:** clean the data, analyze, write the blog post.
- **W9:** send an embargoed brief to 3–5 outlets with a headline stat, the methodology, and aggregate data.
- **W10 (or the Jan 12 shift):** publish.

**Next, in under 2 minutes:** send Moorhen one line: "We can't take the CSV, but we'd love you to send this to your own list. Can you?" Then tell me which publication date you pick (Jan 1 or Jan 12) and I'll turn this into the dated checklist.