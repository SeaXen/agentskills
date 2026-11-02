## 1. Fix identity resolution first — everything downstream depends on it

Before any metric means anything, GitHub activity and Discourse activity need to resolve to the same person.

1. Turn on "Log in with GitHub" as a Discourse authentication provider (Discourse admin → Login settings), if not already live.
2. Require or strongly nudge GitHub SSO for new forum signups going forward.
3. Accept that pre-existing forum accounts won't retroactively link — that's fine, the framework below still works with partial coverage and improves as adoption grows.

Without this, you cannot compute cohort retention, cross-tab a contributor's forum behavior against their PR history, or credit a single person once instead of twice.

---

## 2. Stop treating casual/regular/core and explorer/participant/contributor/advocate as the same ladder

They measure two different axes. Collapsing them into one word per person is what's causing the slide confusion.

| Axis | What it measures | Who owns it | Data source |
|---|---|---|---|
| Casual / regular / core | **Usage intensity** — how often someone uses Cindersmith | Product | Query volume, session frequency, deployment telemetry |
| Explorer / participant / contributor / advocate | **Community investment** — how deep someone goes into GitHub + Discourse | Community/DevRel (this framework) | GitHub + Discourse activity |

A "core" user (heavy query volume) can be a pure "explorer" in community terms (never posts, never opens an issue) — that's a real, useful signal, not a naming collision. It tells you where to focus advocacy outreach: high product value, zero community investment.

**Recommendation:** keep both, never merge them. When a slide needs to show both, use a 4×3 cross-tab grid instead of picking one label:

| | Explorer | Participant | Contributor | Advocate |
|---|---|---|---|---|
| **Core** | prime advocacy-outreach target | | | |
| **Regular** | | | | |
| **Casual** | | | | |

Also flag to product: if "casual/regular/core" has no defined numeric thresholds yet, it's in the same "never measured" state as community — don't assume it's solid ground to build on. Ask them for the actual query/session cutoffs before cross-tabbing.

### Behavioral definition of the Orbit tiers, using signals Cindersmith already produces

| Tier | GitHub signal | Discourse signal |
|---|---|---|
| Explorer | Starred/forked/cloned repo; opened a single bug report and never returned | Read-only visits; Discourse trust level 0 |
| Participant | Opened issues/discussions; commented on others' threads | Posted ≥1 topic/reply; trust level 1–2 |
| Contributor | ≥1 merged PR (code or docs) | Answered others' questions, marked solutions; trust level 2–3 |
| Advocate | ≥3 merged PRs across ≥2 months, or created public content about Cindersmith | Trust level 3–4 (Leader); authored a blog post/talk/tutorial |

Discourse's built-in trust levels (0 New → 4 Leader) already compute from read time, likes, topics entered — use that field directly as your Discourse-side tier input instead of building a scoring model from scratch on day one.

---

## 3. The six-pillar measurement framework

For each pillar: the one metric to start with, plus the fuller set once the pipeline is proven.

### Support deflection

| Metric | Definition | Source |
|---|---|---|
| **Self-resolution rate** ⭐ starter | % of solved Discourse topics whose accepted/last reply is not from a maintainer account | Discourse Data Explorer (posts × solved-plugin field) |
| Community vs maintainer first-response time | Median hours to first reply, split by author type | Discourse API |
| Issue self-closure rate | % of GitHub issues closed without a maintainer comment | GitHub GraphQL, filter `authorAssociation` |
| Repeat-question rate | New topics duplicating an existing solved topic | Manual tag review initially |

### Product feedback

| Metric | Definition | Source |
|---|---|---|
| **Feedback-to-ship ratio** ⭐ starter | % of `feature-request`-tagged issues closed as completed within a quarter | GitHub Issues |
| Feedback volume | New feature-request issues/topics per month | GitHub + Discourse |
| Time-to-first-maintainer-response on feedback | Median hours | GitHub |
| External vs internal feedback mix | % filed by non-maintainer accounts | GitHub `authorAssociation` |

### Contribution growth

| Metric | Definition | Source |
|---|---|---|
| **First-time contributors/month** ⭐ starter | Merged PRs from a GitHub login with no prior merged PR | GitHub API |
| Repeat contributor rate | % of this month's contributors who also contributed last quarter | GitHub API, rolling |
| Time-to-first-review | Median hours from PR open to first maintainer review | GitHub API |
| PR merge rate | merged / (merged + closed-unmerged) | GitHub API |
| Contributor cohort retention | % of month-N contributors still contributing in N+3/N+6 | GitHub API, cohort table |

### Advocacy

| Metric | Definition | Source |
|---|---|---|
| **External content count/month** ⭐ starter | Blog posts, talks, tutorials mentioning Cindersmith | Social listening (e.g. Octolens) + manual sweep |
| Unprompted mentions/recommendations | Positive mentions not solicited by the team | Social listening |
| Advocate → contributor conversion | % of content creators who later submit a PR | Cross-reference identity-linked data |

### Retention

| Metric | Definition | Source |
|---|---|---|
| **Contributor cohort retention** ⭐ starter | Same metric as above, this is the pillar it belongs to | GitHub API |
| Forum retention | % of month-N posters who post again within 90 days | Discourse API |
| Advocate churn/reactivation | Advocates who go quiet then return | Cross-reference over time |

### General engagement

| Metric | Definition | Source |
|---|---|---|
| **Weekly unique actors** ⭐ starter | Distinct GitHub logins with any event + distinct Discourse posters, combined | GitHub + Discourse APIs |
| Topics/replies per week | Discourse volume trend | Discourse API |
| Likes given per active user | Engagement depth proxy | Discourse API |
| Stars/forks growth | Context/vanity metric only — never a headline KPI | GitHub Insights |

---

## 4. Starter scorecard (report this monthly, nothing else, at first)

The ⭐ metric from each pillar above, six numbers total. Resist adding more until this cadence is routine — a 30-metric dashboard nobody reads is worse than six numbers someone actually checks.

## 5. Health thresholds (recalibrate after your first baseline — these are starting guesses for a 30-contributor project, not benchmarks)

| Metric | 🟢 Healthy | 🟠 Watch | 🔴 Act |
|---|---|---|---|
| Self-resolution rate | >50% | 25–50% | <25% |
| Time-to-first-review (PRs) | <48h | 48h–7d | >7d |
| Contributor cohort retention (N+3) | >30% | 15–30% | <15% |
| Feedback-to-ship ratio | >20% | 10–20% | <10% |

---

## 6. Rollout plan

**This week**
1. Enable GitHub login on Discourse.
2. Ask product for casual/regular/core's actual thresholds — don't invent numbers for them.
3. Screenshot GitHub Insights (contributors/pulse/traffic) and Discourse `/admin/dashboard` as your day-zero baseline — free, no new tooling.

**Next 30 days**
4. Build a weekly scheduled pull (GitHub REST/GraphQL + Discourse Data Explorer/API) writing into a spreadsheet, one row per week.
5. Ship only the six-metric starter scorecard.
6. Start labeling issues (`feature-request`, `bug`, `question`) now — pillar 2 and 3 metrics depend on labels existing going forward; you can't reliably backfill this.

**Month 2–3**
7. Backfill ~90 days of history through the same API calls once the pipeline is trusted, to get real trend lines instead of one data point.
8. Move from spreadsheet to a small dashboard (Metabase/Grafana over a Postgres table fed by the same script) — only after the weekly habit sticks.
9. Run the first monthly community health review off the starter scorecard.

**Ongoing**
10. Classify people into Orbit tiers using the signal table in section 2; cross-tab against product's usage tiers once product's thresholds exist.
11. Once advocacy metrics surface 5–10 repeat names, pilot a lightweight recognition motion (public shoutouts, CONTRIBUTORS.md, first-PR celebration) before building any formal champion program — don't build the program ahead of having candidates.