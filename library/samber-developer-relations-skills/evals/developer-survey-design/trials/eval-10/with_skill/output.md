Next action (2 min): ask engineering when the next Driftwood release ships and whether it can carry a survey prompt. Everything below hangs on that release.

I did not run the full interview. I made the assumptions below. I also did not build the decision table (deliverable 1), because I don't know the decision owners yet. This is the channel part of deliverable 2.

## Assumptions (correct me)

- **Population:** people who ran the CLI in the last 12 months.
- **Telemetry:** it exists. 60k monthly active installs implies it. It reports OS and version.
- **Region:** respondents are worldwide, and the organisation may be in the EU or UK.
- **Deadline:** 10 weeks is a deadline.
- **Analyst hours:** about 20.

## Re-ranking block

```
Answer 2 (blog + press planned): calibration sample stays first; claim rules are release blockers.
Answer 4 (first edition, 10 weeks): core module frozen now; nothing demoted, the date is over four weeks away.
Answer 5 (CLI first-run message): calibration promoted to feasible; needs one CLI release.
Answer 7 (telemetry, assumed): OS and version questions deleted; telemetry used as a bias check only. Install counts are machines, not people, so never use them as a weighting benchmark.
Answer 8 (about 20 hours, assumed): paid ads demoted to hold; at most two open-text boxes.
Answer 9 (worldwide, partner involved): privacy step is a release blocker; prize draw deleted; Moorhen sends its own invitation, its list is never imported.
```

## Population sentences (the bias the report must name)

- **Target:** people who used the Driftwood CLI in the last 12 months.
- **Sampled:** people reached by the CLI prompt on a new release (interactive, upgraded in the window), the newsletter, GitHub, Discord, the blog, and Moorhen's list. English readers only.
- **Title risk:** "State of the Toolchain" implies the wider ecosystem. Frame the report as "Driftwood users' toolchains". "X% of developers" is not available from this sample.

## Channel ranking

| Rank | Channel | Tag | Role |
|---|---|---|---|
| 1 | CLI prompt, random draw per install | `cli_cal` | Calibration. Enables "X% of users invited at random through the CLI" (claim rung 2) and a bias measurement. |
| 2 | Owned: newsletter 12k, GitHub 30k stars (pinned Discussion, README, release notes), Discord 9k, blog, docs banner if one exists | `newsletter`, `github`, `discord`, `blog`, `docs` | Volume, mostly fans. Never presented as representative. |
| 3 | Moorhen sends the invitation to its own 50k list | `partner_moorhen` | Second audience with its own skew. |
| 4 | Targeted outreach to a group the data shows is missing | decide in week 4 | Narrows one known gap. |
| 5 | LinkedIn ads ($8k) | hold | Not launched by default. |

**Excluded:** the Moorhen CSV, and emails pulled from the git log.

### Why each decision

- **Moorhen CSV: no.** Passing a list to another organisation needs consent for that specific transfer. Counter-offer: you write the invitation text and a tagged link, Moorhen mails its own list under its own relationship, and Moorhen gets aggregate results only. The notice names Moorhen. Moorhen sees the same outline as everyone else, and the methodology states who could see or change the questionnaire.
- **Git-log emails: no.** Scraped addresses, including commit metadata, break email rules in several jurisdictions and the trust of the people you survey. Do not use them even as a source of analysis. Give your growth lead this instead: a pinned GitHub Discussion, a CONTRIBUTING.md mention, and release notes. They also own the week-4 targeted outreach.
- **LinkedIn $8k: hold.** If the population is CLI users, ads mostly buy people who then screen out as never having used it. Ads also draw bots, and you have limited analyst hours. Release the money only if all three are true after the week-4 bias check:
  1. The check shows a large group that owned channels miss.
  2. Someone screens fraud.
  3. Analyst hours exist.
- **Fallback use of the $8k:** if completes stall at week 4, use it for a fixed donation per complete to an open-source fund. Announce it in advance. This is an incentive, not an ad spend.
- **Incentive:** none. Share results with respondents in every channel before the press release.

## Set up (in order)

### Week 1

1. Confirm the release date and the upgrade curve. Query telemetry: what share of installs upgrade within 2 weeks of a release? The field window must cover that curve.
2. Pick a survey tool that can do unique links, hidden fields, routing, and switch off IP logging. Open item: which tool?
3. Build the CLI prompt.
   - Show it only in an interactive terminal, never in CI.
   - Honour the existing telemetry opt-out.
   - Mark the install as invited once in local state.
   - Hand out single-use tokens from a pre-made list through a small endpoint that stores no install ID.
   - Put the honest length in the message: "Driftwood survey, N min, optional: <url>".
4. Write the privacy notice (first page) and an age gate. Keep identifiers out of the response table. Get the data-protection contact to sign off.
5. Send Moorhen the invitation text, a tagged link, and the aggregate-only terms.

### Sizing the CLI group

- Set the subgroup minimum, self-set: 100 completes per subgroup.
- Calibration target = 100 × the number of subgroups you will compare. For 3 subgroups, that is 300.
- Invites needed = target ÷ completion rate. Illustration only: at an assumed 2%, that is 15k invites. Replace the 2% with the soft-launch rate.
- Print the group's invited, started and completed counts beside every rung-2 number.

### Pilot and field

1. Week 2: expert review (phone and screen reader), then 5 cognitive interviews.
2. Week 3: soft launch to a small newsletter slice, tagged `pilot`. Check median time against the budget, breakoff, and empty answers. Then freeze the wording.
3. Weeks 3-6: field window, about 3.5 weeks.
4. End of week 4: compare completes per tag, the `cli_cal` mix, and the telemetry mix (OS) against respondents. Decide targeted outreach, ads, or the donation fallback.
5. Close Friday of week 6.

### Schedule

| Weeks | Work |
|---|---|
| 1 (Oct 26) | Decision table, build, privacy, CLI code, Moorhen ask |
| 2 | Expert review, interviews, CLI release candidate |
| 3 | Soft launch, freeze, CLI release, full launch |
| 4-6 | Field window, week-4 bias check |
| 7 (Dec 7) | Clean, analyse, code open text, privacy admin, embargoed press pitch |
| 8 (Dec 14) | Report and methodology, claims check, results to channels, then blog and press |
| 9-10 | Buffer |

**Holiday warning:** week 10 ends Jan 1. Press and newsletter attention is dead from about Dec 19 to Jan 2. Publish in week 8, or after Jan 5.

## Risks to the plan

- **CLI release gate.** If no release ships in weeks 2-3, calibration slips and so does rung 2. Fall back to rung 1 and say so.
- **CLI bias.** The prompt misses CI-only and non-interactive users and anyone who does not upgrade in the window. Name this in the bias sentence.
- **Telemetry opt-outs.** The same sentence names opt-out users as missed.
- **English only.** Name the under-sampling of non-English readers in the bias sentence.
- **Title.** Keep it away from ecosystem claims.

## Headline rewrite for the press

- **Wrong:** "X% of developers use <tool>."
- **Right:** "X% of the N respondents who used Driftwood in the last 12 months use <tool> (exact wording, n). Respondents came mostly from our newsletter, GitHub and Discord, so the figure describes respondents, not all developers."
- **Rung 2, if the CLI group reaches its minimum:** "Among N users invited at random through the CLI, X% … (invited I, completed C)."

Never print a margin of error on the open-link data.

## Still open

1. Who owns each decision the survey feeds? This builds the decision table.
2. Which survey tool?
3. What is the analyst hours budget?
4. Where is the organisation based?
5. Is a docs banner available?

Next: send me the owners and the draft questions, and I'll build the decision table.