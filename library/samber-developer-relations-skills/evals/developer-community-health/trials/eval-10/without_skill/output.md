## Community health dashboard — Pallasite

### Read the data before building the dashboard

11 messages/month in a 1,900-member Slack, 9 from your own two staff, 2 from one unanswered user, steady for 8 months — that's not a "measurement gap," that's a dead channel. Any honest dashboard built from Slack metrics alone will show a flatlined community and undercut the headcount case, not support it. Two honest paths forward:

- **Reframe the ask.** For an OSS library, Slack is one venue, not the community. The real community lives in GitHub (issues, PRs, discussions, dependents) and the package registry (downloads). Build the dashboard around *project* health, with Slack as one input, not the whole picture.
- **Or run it as a diagnostic, not a justification.** Present the numbers straight, propose a 90-day revival plan with a clear go/no-go metric, and let leadership decide with real data. A dashboard that leadership later discovers was cherry-picked to hide a dead channel costs more credibility than one honest quarter of bad numbers.

Below is a dashboard that works either way — it surfaces the truth and gives you the inputs to make either case.

---

### 1. Slack-specific vitals (diagnostic, not vanity)

| Metric | Definition | Why it matters | Current signal |
|---|---|---|---|
| Non-staff message share | % of messages not from staff accounts | Staff-to-staff chat isn't community activity — it's two people using the wrong tool | ~18% (2/11), and that 18% went unanswered |
| Question response rate | % of questions that get any reply within 72h | Direct measure of whether the channel delivers value to the one person who shows up | 0% last month |
| Response time (median) | Time from question to first staff/community reply | Slow answers train people to stop asking | Unmeasured — start logging it now |
| DAU/MAU | Daily active / monthly active members | Standard stickiness signal | Effectively 0% — 3 unique posters out of 1,900 |
| Monthly active ratio | Unique posters ÷ total members | Size of the channel relative to activity | 0.16% (3/1,900) |
| New-member 7-day post rate | % of new joiners who post within a week | Tests whether onboarding creates any activation | Likely near 0 — check invite/join logs |
| Lurker ratio | Members with 0 messages in 90+ days | Quantifies the gap between "members" and "community" | Almost certainly >99% |

These numbers exist to be shown as-is. Don't average them into something softer — leadership needs the real shape of the problem to fund the right fix (or make the right call to stop funding it).

### 2. Where the actual Pallasite community lives (GitHub / repo)

| Metric | Source | Why it belongs on this dashboard |
|---|---|---|
| Issues opened / closed per month | GitHub Issues API | Real signal of active usage and unresolved pain |
| Median time-to-first-response on issues | GitHub Issues | This is the support metric that actually matters for an OSS lib |
| PRs opened / merged, external vs. staff | GitHub PRs | Contribution health — the strongest "is this alive" signal |
| Unique external contributors (rolling 90d) | GitHub PRs/commits | Bus-factor and community depth, not headcount |
| Discussions activity (if enabled) | GitHub Discussions | Many OSS users prefer async GitHub threads over Slack — check if this is where your 1,900 Slack members actually went |
| Stars growth rate (30/90d) | GitHub API | Discovery/awareness proxy, weak but standard |
| Dependents / reverse-dependency count | GitHub "Used by," package registry | Best proxy for how many people rely on the library in production |

### 3. Adoption (does the library matter, independent of chat)

| Metric | Source |
|---|---|
| Downloads/installs, monthly trend | PyPI/npm/crates stats, whichever registry Pallasite ships on |
| Download growth rate (MoM, YoY) | same |
| Geographic / org diversity of adopters | registry stats or telemetry if opted-in |

If downloads are flat or growing while Slack is dead, that's a real story: **the community didn't leave, it never needed the chat channel.** That's a legitimate finding, and a much stronger basis for a staffing conversation than inflated Slack numbers.

### 4. Support load and deflection (this is what headcount usually gets justified on)

| Metric | Why |
|---|---|
| Support requests per week, by channel (GitHub issues, Slack, email, Stack Overflow, Reddit) | Shows where the actual support burden sits — probably not Slack |
| % resolved without staff (community-answered) | Measures whether *any* channel is self-sustaining |
| Time staff spend on community/support per week (self-reported log) | Direct input to the headcount argument — hours in, value out |

### 5. Leading indicators (catch decline before it's this bad next time)

| Metric | Threshold to flag |
|---|---|
| 3-month rolling non-staff message trend | Declining 2 months running |
| Days since last unanswered question got a reply | >7 days = escalate |
| New-member count vs. active-member count divergence | Growing gap = churn hidden by new joins |

---

### How to present this to leadership

1. **Lead with the GitHub/adoption numbers**, not Slack — that's where Pallasite's real signal is, and it's likely a much better story.
2. **Show Slack as a specific, named problem**: "1,900-member Slack, <0.2% monthly active, 0% response rate — this channel is not delivering value and is costing us [X hours/month] to maintain for no return."
3. **Propose one of two concrete moves**, not "more metrics":
   - Sunset or archive the Slack, redirect that headcount time to GitHub Discussions/issues where the actual usage signal is.
   - Or commit to a 90-day, resourced revival (weekly prompts, staffed office hours, active issue triage funneled into Slack) with a stated success bar (e.g., non-staff message share >50%, response rate >90%) — and agree upfront to sunset it if the bar isn't met.
4. **Don't dress up the current Slack numbers.** A dashboard leadership later finds was massaged to hide a dead channel is a worse outcome for you than an honest one that shows the community's energy is just somewhere else.