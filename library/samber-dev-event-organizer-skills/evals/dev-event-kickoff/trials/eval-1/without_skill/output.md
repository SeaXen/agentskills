# Braukette Community Hackathon: Questions and Plan

I don't know your product, budget, or community size, so the plan carries my default assumption for each gap. Reply with just the numbers of the answers that differ.

## Part 1: What I need from you

**Blockers** (they change the plan's shape)

1. **Budget.** What's the number, and does it cover prizes only or also swag, tools, and venue? *Default: €3,000 all-in.*
2. **Hours.** What does "a few hours" total across the three of you, between now and the event? *Default: about 12 hours each, 36 in total, spread over 5 months.*
3. **Why do this?** Pick one primary goal:
   - (a) API/SDK adoption
   - (b) product feedback
   - (c) community energy
   - (d) content and PR
   - (e) hiring leads

   *Default: (a) plus (b).*
4. **Community size and channel.** How many users do you have, and where do they live (Discord, Slack, forum, newsletter)? How many are active monthly? *Default: 500 to 2,000 users, about 100 active.*
5. **What can people build on?** Do you have a public API, SDK, webhooks, or sample data? If not, a hackathon will mostly produce support requests. *Default: a public REST API and docs exist.*
6. **Who are your users?** Professional brewers, homebrewers, or brewery software developers? This sets themes and prize appeal. *Default: small-brewery technical staff plus homebrewing hobbyists who code.*

**Format and logistics**

7. **Geography.** Where are your users? Is any one city dense enough for in-person? *Default: global, so online.*
8. **Event owner.** Who is the single accountable person, and who has authority to approve spend?
9. **Date constraints.** What are the product release dates, holidays, and your busiest brewing or industry events in spring 2027?
10. **Legal and finance.** Can the company pay prizes to individuals, including non-EU residents? Is there a template for contest terms? Who signs off?
11. **Existing assets.** Do you have a test or sandbox environment, free-tier or credit capability, and a brand/design person for a banner?

**Decision**

12. **Go/no-go owner and deadline.** Who decides, and by when? *Default: decision by 2026-12-15, with the gate below.*

## Part 2: Go/no-go gate (decide before spending anything)

**Do it only if all four hold.**
- The goal in question 3 is something a hackathon moves. A hackathon won't fix a weak API or docs.
- At least 25 community members would plausibly participate. Test this with a poll (see step 1 of the timeline).
- You can name one owner and 12 hours each.
- Your API can be used by an outsider in under 30 minutes without hand-holding.

**Don't do it if:**
- The poll shows fewer than 15 interested people.
- Your quickstart fails a cold test by a non-team engineer.
- The budget is under about €1,000 and you can't commit time. Run a "build challenge" thread instead (a 2-week community call for projects with a small prize).

**Success definition** (set it before launch, so you can't retrofit it):

| Metric | Target for a 500-2,000 user base |
|---|---|
| Registrations | 60 |
| Teams that submit a working project | 10 |
| Participants who made their first API call | 70% of registrants who start |
| New or reactivated API keys 30 days later | 15 |
| Product feedback items filed | 20 |
| Total cost per submitted project | under €300 |

**Kill rule:** if registrations are under 25 two weeks before the start, postpone or convert to a lighter "challenge thread." Don't run a three-person event.

## Part 3: Recommended format

**An online, asynchronous, 2-week build, with one kickoff call and one demo call.** I recommend this over a 48-hour weekend sprint and over in-person.

- **Why not in-person:** venue, food, insurance, and day-of staffing exceed three first-time organizers with 36 hours total. Brewing also raises alcohol, age, and liability questions you don't need.
- **Why not a 48-hour online sprint:** it needs live, around-the-clock support from you. Async means your support is a few Discord check-ins per day.
- **Why 2 weeks:** participants have day jobs, so a two-week window with a late-evening kickoff and a Sunday demo suits them. Shorter is better only if you have a very active community.

**Proposed timing** (spring 2027, adjust per question 9): kickoff Thursday evening, build period 14 days, submissions due Thursday 23:59 UTC, demo call the following Tuesday, winners announced at the end of that call.

## Part 4: Challenge themes

I'm guessing at your product (brewery operations software). Replace the specifics with what your API really exposes. Offer **four tracks**, because each team picks one and judges compare within a track:

1. **Brew-day automation.** Connect Braukette to the outside world: Slack/Discord alerts for tank temperature or batch stage, calendar sync for brew schedules, voice or chat assistants that log batches.
2. **Data and insight.** Dashboards, forecasting, or anomaly detection on fermentation, yield, inventory, and sales data. Provide an anonymized sample dataset.
3. **Integrations.** Bridges to the tools breweries already use: accounting, POS, e-commerce, distribution, tax and compliance reporting, hardware sensors.
4. **Open track: "Surprise us."** Anything creative that uses Braukette: a homebrew companion app, a recipe-scaling tool, a taproom display, a teaching tool.

**Optional mini-challenges** (cheap bonus prizes that steer behavior):
- **Best docs feedback:** the participant who files the most useful issues about our docs or API.
- **Best use of [newest feature]:** push adoption of something you just shipped.
- **Best newcomer:** a team with nobody who has used Braukette before.

If you have an AI/LLM angle in your roadmap, make it a cross-cutting bonus, not a track.

## Part 5: Prizes

Allocate about 60% of the budget to cash or gift cards, 25% to credits and merchandise, and 15% for contingency (swag, ads, fees). At the €3,000 default:

| Prize | Value |
|---|---|
| 1st place overall | €800 |
| 2nd place overall | €400 |
| 3rd place overall | €200 |
| Track winners (4 tracks, one each) | €150 each = €600 |
| Mini-challenge winners (3) | €100 each = €300 |
| All submitters | Braukette swag, certificate, 3 months of paid plan |
| Reserve | the remainder |

(Sums to €2,300 plus roughly €700 for swag shipping, a design contractor, and contingency. Tune it to your real budget.)

**Non-cash prizes that cost little and matter more to engineers:**
- A 30-minute call with your CTO or product lead.
- Featuring the winning project on your blog and docs ("Built with Braukette").
- Permanent community role, such as a "Builder" badge and early access to betas.
- A direct line to your roadmap: the winner's top feature request gets prioritized in writing.
- Free annual plan.

**Pitfalls:**
- Don't offer a job or internship as a prize without HR sign-off.
- Prizes need legal review in some countries (taxes, sweepstakes law).
- Ship physical prizes only to countries you can ship to. Offering a gift card choice avoids that.
- Alcohol is not a prize.

## Part 6: Judging

**Judges:** the 3 of you plus 2 external judges (a friendly power user and a community or industry figure). Five judges avoid ties and reduce your own bias. Judges cannot score teams they coached or contributed to.

**Criteria** (score each 1 to 5, weight as shown):

| Criterion | Weight | What it means |
|---|---|---|
| Working demo | 30% | It runs, end to end, in the submitted video or live. |
| Usefulness | 25% | Solves a real brewing or brewery-ops problem. |
| Use of Braukette | 20% | Depth and sensible use of the API. Not "one call." |
| Creativity | 15% | A new idea or surprising angle. |
| Polish and docs | 10% | README, setup instructions, clarity. |

**Process:**
1. **Submission requirements:** repo link, 3-minute demo video, 200-word description, track selection, and the API features used.
2. **Eligibility check by one organizer** (rules, project started during the event, working repo).
3. **Round 1: independent scoring.** Every judge scores every project alone on a shared spreadsheet before seeing others' scores. Shortlist the top 6 overall, plus the top of each track.
4. **Round 2: live demos.** The shortlisted teams give a 4-minute demo and 2 minutes of Q&A at the demo call. Judges rescore.
5. **Tie-break:** the "Working demo" score, then the "Usefulness" score.
6. **Publish the rubric before kickoff,** and publish the winning scores' summary afterward.

**Rules that protect you:**
- Participants keep ownership of their code. Braukette gets a license to showcase the project and demo.
- Teams of 1 to 4 people. Employees and relatives of Braukette are not eligible for prizes.
- Code of conduct is posted and enforced. Name one person with power to remove participants.
- Starting from existing personal projects is allowed only if the integration is new during the event. Declare this.

## Part 7: Timeline (working back from kickoff in late April 2027)

Hours are per person unless noted.

| When | Task | Hours |
|---|---|---|
| Now to 2026-12-15 | 1. Answer the questions above. Run a 5-question community poll and an API cold-test by an outsider. Gate decision. | 2 |
| Jan 2027 | 2. Fix the date, write the rules, track descriptions, rubric, and contest terms (legal review). Reserve budget. | 2 |
| Feb | 3. Prepare the dev kit: quickstart, sandbox keys, sample dataset, 3 starter templates, FAQ. This is the biggest lever on outcomes. | 3 |
| Mar | 4. Open registration: landing page (one page), announcement to newsletter, Discord, social, and relevant communities. Recruit 2 external judges. | 1 |
| 4 weeks out | 5. Reminder posts weekly. Direct invites to your top 20 users. | 0.5 |
| 1 week out | 6. Dry run: a teammate registers and submits a dummy project. Prepare judging spreadsheet and kickoff slides. | 1 |
| Kickoff | 7. 45-minute call: rules, tracks, demo of the API, Q&A. | 0.5 |
| 2-week build | 8. Support rota: a 20-minute check on Discord twice daily, split across the three of you. One office-hours call mid-event. | 2 |
| Submission and judging | 9. Round 1 scoring (about 10 projects). | 1.5 |
| Demo call | 10. Live demos and announcement. | 1 |
| Within 2 weeks after | 11. Pay prizes, post a wrap-up blog with the winners, send a feedback survey, triage issues filed, review metrics against the success definition. | 1.5 |
| **Total** | | **about 16 hours each** |

That is above the 12 you said you could give. To get under 12, cut **in this order**: the optional mini-challenges, the mid-event office hours, the third starter template, and Round 2 demos (judge on videos alone).

## Part 8: Budget sketch (€3,000 default)

| Item | Cost |
|---|---|
| Prizes (Part 5) | €2,300 |
| Swag and shipping | €300 |
| Landing page / banner design | €150 |
| Platform (Devpost or a free alternative, optional) | €0 to €150 |
| Reserve | €100 to €250 |

Infrastructure costs (sandbox, API credits) come from existing infrastructure. Check them against free-tier limits to avoid surprise bills from heavy usage.

## Part 9: Risks and mitigations

- **Nobody signs up.** The gate and kill rule handle this. Push direct invites to 20 named users, since personal invitations outperform public posts.
- **Participants get stuck on the API.** The dev kit and twice-daily support cover it. The cold-test is the cheapest protection.
- **Dropout is high (typical 50% to 70% of registrants never submit).** Plan for it: 60 registrations yields about 10 submissions. Send a mid-event nudge with a "what's blocking you?" message.
- **Organizer time overrun.** Name a single owner and cut scope by the list in Part 7.
- **Judging bias or disputes.** The published rubric, independent scoring, and conflict-of-interest rule address this.
- **Legal and tax issues with prizes.** Get legal review in January, not April.
- **Security.** Sandbox keys only, rate-limited, with an expiry date. Never give production credentials.

## Part 10: After the event

1. Pay winners within 14 days and say so in the rules.
2. Publish a wrap-up post with projects, scores summary, and thanks.
3. Turn the best 2 or 3 projects into docs examples and case studies (with permission).
4. Compare results with the success definition and write a one-page retro: what worked, what cost the most hours, whether to repeat.
5. Decide on a repeat only from those numbers.

## Next step

Answer questions 1 to 6 and 12 (the blockers). With those, I can replace the defaults with your real numbers and draft the contest terms, the landing page copy, the announcement posts, and the judging spreadsheet.