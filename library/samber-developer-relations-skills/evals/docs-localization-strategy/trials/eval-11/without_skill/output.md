**Next (15 min):** DM the marketing lead. Ask for the Shanghai event date and what "Chinese docs live" must include. Everything below hangs on that answer.

## Core problems

1. No one on staff reads Chinese, so you can't check what you publish.
2. A mistranslated install command or a swapped link in an observability agent's docs is a safety problem, not a typo.
3. Discord is blocked in mainland China, so your three volunteers are likely abroad or on a VPN. Mainland developers are probably elsewhere: WeChat, Zhihu, Juejin, Gitee.
4. With no analytics, you can't show Chinese demand. You also can't prove success afterward.
5. Translated docs drift out of date as soon as English changes.

## Recommendation

Don't promise full docs by end of next month. Promise a reviewed core set labelled beta. Core set: install, quickstart, core concepts, and the 5 to 10 most-visited config and troubleshooting pages. Aim for roughly 10 to 15 pages. Keep English as the source of truth.

## Plan (today is Fri 2026-10-30, deadline is Mon 2026-11-30)

Target ship date is Wed 11-25. That leaves a buffer.

**Step 1: Today (about 2 h)**
1. Message the marketing lead and ask for the event date, the must-have pages, and the risk they accept with beta labelling.
2. In Discord, ask the 3 volunteers for hours per week, prior translation or docs work, and where they live (mainland or not). Ask each to translate one sample paragraph.
3. Ask your manager for analytics access, a small budget for paid review, and the ID of whoever owns the docs repo and hosting.

**Step 2: Week 1 (Nov 2 to 6): foundations**
1. Pick the page list. Decide it with the marketing lead and the docs owner.
2. Build a glossary first, before any page. Decide per term: translate or keep in English. Examples: trace, span, metric, log, pipeline, collector, agent, sampling. Copy established Chinese terms rather than inventing them. Check OpenTelemetry's Chinese docs as a reference.
3. Set up the repo structure. Put zh pages in a separate path, such as `/zh/`. Use the Git workflow you already have. Add a banner to each page: "Community translation, based on English version <commit SHA>."
4. Write a one-page contributor guide. Cover the DCO or CLA, credit in the contributors list, and the review rule below.
5. Add a CI check that fails if a translated page changes code blocks, commands, or URLs compared to English. This is your safety net, because you can't read the prose.

**Step 3: Weeks 2 to 3 (Nov 9 to 20): translate and review**
1. Each volunteer takes a page set. They may use machine pre-translation, but a human edits every page.
2. Two-person rule: no page ships unless a different volunteer reviews it.
3. Hire a professional reviewer for a paid pass on the 3 highest-traffic pages: install, quickstart, and one concept page. Budget a few hundred dollars (cost not verified). If no budget exists, ask a Chinese-speaking contact from the event, or a friendly user.
4. Use an LLM back-translation as a smoke test only. It flags obvious meaning drift. It is not review.
5. Check the volunteers' sample from Step 1. If quality is poor, shrink scope now, not on day 28.

**Step 4: Week 4 (Nov 23 to 27): ship**
1. Wed 11-25: publish the reviewed set under `/zh/`, labelled beta. Anything not reviewed stays unpublished. Do not publish it unreviewed.
2. Check page speed from China. Your host may be slow there. Hosting inside mainland China needs an ICP filing, so skip that for now and test latency instead.
3. Prepare an event handout and a Chinese landing page pointing at the docs. Marketing owns this.
4. Mon 11-30: buffer for fixes.

**Step 5: After launch**
1. Re-sync rule: when English changes, a bot opens an issue on the zh page. Stale pages get a visible "may be outdated" banner after 30 days.
2. Name one volunteer as zh docs maintainer with merge rights on `/zh/` only. You still can't verify their changes, so keep the CI check on code blocks and URLs.

## Measuring without analytics

1. Ask for analytics access, and add a `/zh/` view filter from day one.
2. Until access arrives, run a 1-question Discord poll: "Which language do you prefer for docs?"
3. Check GitHub Insights traffic, which shows referrers to the repo, if you have maintainer rights.
4. Define success before launch. Example: X zh page views in 30 days, Y Chinese-speaking Discord joins, Z event leads. Ask the marketing lead for realistic targets.

## Risks

- **Volunteers disappear.** Mitigate with the scope cut and the Step 1 hours question.
- **Quality unverifiable.** Mitigate with the two-person rule and paid review on top pages.
- **Wrong channel.** Discord may not reach Shanghai attendees. Ask marketing what channel the event uses, likely WeChat.
- **Fallback if Step 3 slips.** Ship only install, quickstart, and the glossary, plus the Chinese landing page. English docs stay for the rest.

## Open questions for you

1. Event date, and is "end of next month" before it?
2. Which docs framework do you use (Docusaurus, Mintlify, other), and how many pages are there?
3. Is there any budget for a paid review?
4. When does analytics access arrive?

**Next:** send the marketing-lead message from Step 1.