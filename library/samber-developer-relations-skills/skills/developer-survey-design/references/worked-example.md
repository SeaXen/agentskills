# Worked example: a first "State of" survey for an open-source database

Fictional case. An open-source distributed SQL database with a managed cloud offering plans its first yearly community survey. Marketing drafted 30 questions and wants "X% of our developers run it in production" in a press release. Results are due in 8 weeks; one DevRel person has about 12 hours. The company is in the EU, respondents are worldwide. Marketing also wants a laptop raffle and a "nurture" email list.

## Contents

- Re-ranking block
- Decision table excerpt
- Claim rewrite
- Channel table
- Incentive decision
- Schedule and hours

## Re-ranking block

```
Answer 2 (publication planned): calibration sample kept first (the default); claim rules become release blockers.
Answer 4 (yearly series, 8 weeks): core module frozen now; nothing demoted, since the date is not under four weeks.
Answer 5 (CLI start message, consented cloud-user list): calibration sample needs little new infrastructure.
Answer 7 (opt-out telemetry reports version, OS, deploy target): version and OS questions deleted; deploy-target mix used as a bias check.
Answer 8 (12 analyst hours): at most two open-text boxes.
Answer 9 (EU, worldwide, raffle idea): prize draw ranked last on compliance cost; partners send invitations, lists never imported.
```

## Decision table excerpt

Kept (22 of 30 drafted, after merges and new items):

| ID | Orig | Question (short) | Decision | Owner | Answer that would change it | Publish | Module |
|---|---|---|---|---|---|---|---|
| Q1 | 13 | Furthest stage reached in last 12 months (tried / dev / staging / production) | Qualifier, segments every cut, production headline | Marketing | Production share differs sharply between self-managed and cloud: headline leads with the segment | publish | core |
| Q6 | 16-18 reworked | What slowed or stopped you (12 options, randomised) | Rank the three roadmap candidates against all blockers | Roadmap | A non-roadmap blocker outranks all three: raise it | internal | core |
| Q7 | 16-18 reworked | If we could improve only one: Kubernetes operator / Postgres compatibility / observability | Final order of the three investments | Roadmap | One option wins in two or more deployment segments: ship it first | internal | rotating |
| Q14 | 19 split | Task where you last got stuck | First docs sprint | Docs | One task area tops two segments: it is the sprint | internal | core |

Cut:

| Orig | Question | Reason |
|---|---|---|
| 1, 2, 30 | Name, email, raffle email | Identifiers out of the response table; contact moves to a separate form |
| 9 | "How much do you love it?" 1-10 | Praise in the stem; no action attached |
| 10 | "It is faster than Postgres" agree/disagree | Agree/disagree inflates agreement; a performance claim needs a benchmark |
| 11, 12 | Version, OS | Telemetry answers both |
| 16-18 | "Would you like X?" three times | Wishlists return yes; replaced by Q6-Q7 trade-off |
| 24, 25 | Cloud budget, demo interest | Lead capture makes the survey marketing; signup link on the thank-you page instead |
| 26 | "What do you think about AI?" | No decision named |

## Claim rewrite

```
// ✗ "X% of our developers run it in production"
// ✓ "X% of the N respondents who used it in the last 12 months run it in production
//    (real users or business processes depend on it). Respondents came mostly from our
//    newsletter, Discord and docs, so the figure describes respondents, not all users."
// ✓ (rung 2, if the calibration group reaches the subgroup minimum)
//    "Among N users invited at random through the CLI, X% ... (invited I, completed C)."
```

## Channel table

| Channel | Tag | Role | Notes |
|---|---|---|---|
| CLI start message, random draw per install | `cli_cal` | Calibration, self-hosted | One invitation per install; reaches interactive users on the new version only, named in the bias sentence |
| Random draw from consented cloud-user list | `cloud_cal` | Calibration, cloud | Sized from the soft-launch completion rate; one reminder to the same draw |
| Newsletter, docs banner, blog, Discord | `newsletter`, `docs`, `blog`, `discord` | Owned | Volume, mostly fans; docs banner skews toward people who are stuck |
| Two partner companies | `partner_a`, `partner_b` | Partner-sent | Partners mail their own lists; the notice names them; they receive aggregates only |

Excluded: imported partner lists, scraped addresses, paid ads (fraud screening exceeds the hour budget).

## Incentive decision

None, with results posted to every recruitment channel before the press release and an optional "email me the results" form. The raffle is rejected: contact data, sweepstakes rules across jurisdictions, more bot entries, and no effect large enough to outweigh those costs. Fallback if completes stall in week 2: a fixed donation per complete to an open-source fund, announced in advance.

## Schedule and hours

| Week | Work |
|---|---|
| 1 | Decision-table session with roadmap, docs and marketing; freeze core wording; build; expert review |
| 2 | Five cognitive interviews; soft launch tagged `pilot`; CLI release carrying the random draw |
| 3-5 | Field window; week-1 check of completes per tag, deploy-target mix against telemetry, median time |
| 6-7 | Clean, analyse, code open text, draft report and methodology |
| 8 | Privacy and claims check; results to channels first, then the press release |

Hours: decision-table session 1, build 1, pilot 4, cleaning 1, analysis 1, open-text coding 1, report and methodology 2, privacy admin 1.
