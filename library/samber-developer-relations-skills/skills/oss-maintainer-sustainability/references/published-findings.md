# Published findings

Every figure and case the skill cites, with its owner. Quote figures with the owner attached; this field has surveys and cases, not standards.

## Contents

- Burnout base rates
- What drives burnout
- Handover and exit cases
- Explicit end-of-life
- Funding: what it buys and what it does not
- Time and boundary practice
- Figures to avoid
- This skill's own baselines

## Burnout base rates

| Source | Figure |
|---|---|
| Tidelift maintainer surveys, 2021 and 2023 (State of the Open Source Maintainer) and 2024 (Maintainer Impact Report, 437 respondents) | 59% / 58% / 60% quit or considered quitting a project; the 2024 report gives n=350 (2024) and n=265 (2023) for that question |
| Tidelift 2024 | 60% describe themselves as unpaid hobbyists |
| Tidelift 2024, not confirmed against the report itself; check before quoting | 61% of unpaid hobbyists maintain alone versus 26% of paid maintainers; 78% of unpaid hobbyists spend 10 hours or less a week |
| Tidelift 2024 | security work rose from 4% (2021) to 11% of maintainer time |
| Tidelift 2024 | 48% feel underappreciated; 43% say maintaining adds personal stress; two-thirds less trusting of contributors after xz-utils |
| Sovereign Tech Agency survey, 2024 | 77% of maintainers unpaid or unable to make a living from the work |
| Intel open-source community survey, 2023 | 45% name maintainer burnout as their top challenge |
| Avelino, Valente, Hora, 2015 (popularized by Nadia Eghbal) | nearly two-thirds of 133 popular GitHub projects depend on one or two maintainers |

Tidelift sells "pay the maintainers" and recruits partly among its own partners; read its figures as directional. Its top reason for quitting is "other things in my life and work took priority", not drama.

## What drives burnout

- **Miranda Heath, "Burnout in Open Source" (2025, Open Source Pledge)**: six drivers from 50+ maintainer writings: difficulty getting paid, workload, unrewarding maintenance, toxic behaviour, hyper-responsibility, pressure to prove oneself.
- **Miller et al., OSS 2019**: life transitions make disengagement 2.48 times more likely; departure is usually life, not conflict.
- **Raman et al., ICSE 2020; Miller et al., ICSE 2022**: toxic comments, mostly entitlement and demands, as a burnout driver.
- **GitHub Open Source Survey 2017**: 21% of people who saw a negative interaction stopped contributing to that project.
- **opensource.guide, "Maintaining Balance"**: lack of positive feedback, over-commitment, isolation, resource scarcity, employer-versus-community conflict.
- **Nadia Eghbal, _Working in Public_ (2020)**: in the "stadium" shape (high user growth, low contributor growth), attention, not code, is the scarce input.

## Handover and exit cases

| Case | Lesson |
|---|---|
| event-stream, 2018: publish rights given to a volunteer who emailed asking; the new owner added a dependency, flatmap-stream, carrying code that targeted a bitcoin wallet | An unvetted handover is worse than abandonment |
| xz-utils, 2021-2024: multi-year credibility campaign plus sock-puppet pressure on a maintainer who had written about limited capacity and mental health; backdoor found 2024-03-29 (CVE-2024-3094) | Burnout is an attack surface; pressure to hand over is the signal to slow down |
| colors.js / faker.js, 2022: protest releases broke millions of installs; registry reverted, community forked faker | Sabotage gets reverted and destroys trust; a community fork is the recovery |
| core-js: an early fundraising push produced $57 a month; in February 2023 the author reported about $400 a month for 250 million monthly downloads and about 250 hours of work a month | Usage does not convert into funding |
| requests, 2019: moved under the Python Software Foundation | A custodian takes the name and keys out of one person's hands |
| Gorilla toolkit (Go), 2022-2023: archived in December 2022 after volunteers who offered help did not stay; unarchived in 2023 by new maintainers | A clean archive is honest and reversible; a revival needs durable people |
| Jazzband, 2026: a Python collective then holding 71 projects announced its sunset in March with transfers through December; it named AI-generated pull-request spam and its founder being "a single point of failure" as drivers | Custodians need their own admin redundancy; long notice is possible and kind |
| Sovereign Tech Fellowship pilot, 2025 (n=4-5): fellows felt calmer while doubling hours, because focused work replaced firefighting | Time-based funding helps well-being; tiny sample |

## Explicit end-of-life

**Miller et al., ICSE 2025**: of 28,100 widely used npm packages, 14.6% were abandoned. Among dependents still active afterwards, only 18.1% ever removed the abandoned package, and removal was significantly faster when the end-of-life was stated explicitly in the README or repository metadata. The study did not measure npm's deprecation flag; recommend registry signals as a separate step.

## Funding: what it buys and what it does not

- **Overney et al., ICSE 2020** (data predating GitHub Sponsors): 0.04% of GitHub repositories ask for donations; donations rarely fund a full-time position and show no strong association with higher activity.
- **Shimada et al., 2022**: most maintainers get few or no sponsors; sponsorship gives a short-term activity bump.
- **Tidelift 2024**: 81% of maintainers prefer predictable monthly income to a lump sum; paid maintainers are far more often on teams and more likely to make security improvements.
- Jazzband had fiscal sponsorship and still sunset: money did not supply admins.

## Time and boundary practice

- opensource.guide examples: "expect a response within 7 days"; "We only spend about 5 hours per week".
- @danielbachhuber (via opensource.guide): "2-5 hours per week keeps involvement a passion".
- GitHub, February 2026: maintainers can turn pull requests off entirely or restrict them to collaborators with write access.
- curl ended its bug bounty after confirmation rates fell below 5%.

## Figures to avoid

- "Tidelift found 59% of maintainers experienced burnout and 35% harassment" matches no Tidelift report. Say "quit or considered quitting".
- "44% cite burnout as their reason to quit (Tidelift 2024)" appears only in blogs.
- No published study measures how much a stale bot, issue forms or a status line reduce maintainer hours. Present them as mechanisms, not as proven savings.

## This skill's own baselines

Self-set, not sourced: the health-check thresholds (four-week budget check, two holders per publish right), the effort orders of magnitude in the move table, the response-window defaults (half the time on the tracker, 15 minutes per reply), and the notice periods.
