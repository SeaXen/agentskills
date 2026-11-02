# Ironvale community feedback intake spec (v1)

## 0. Changes to your plan

Your plan has three problems. Fixing them is the main change in this spec.

1. **Logging every request yourself doesn't fit your budget.**
   - Volume is about 59 items a week (35 Discord, 15 support, 9 GitHub).
   - At 3 minutes each, that is 3 hours, your entire budget, before the digest or any content work.
   - At 5 to 8 minutes each with full context, it is 5 to 8 hours.
   - It also makes you the single point of failure, so it won't last a year.
   - **Fix:** log themes, not requests. Each theme is one problem with counted evidence links.
2. **Most of the 59 items aren't feedback.**
   - Many are support questions or bugs.
   - Route those to GitHub issues or support and keep them out of the backlog.
   - I assume about 40% are real product feedback, roughly 24 a week. That is a guess; measure it in week 1.
3. **Don't ask Tomas for a standing planning seat yet.**
   - He agreed to two things: own decisions and sit in a monthly review.
   - A seat in planning is a bigger ask. It is easier to get after two review cycles of evidence than before any.
   - Your leverage is a packet he can't ignore: ranked themes, evidence counts, and a decision needed on each.
   - If he offers a seat, accept it. If not, ask to be invited whenever a theme from the packet is on the planning agenda.

## 1. Principles

- **Evidence stays where it lives.** GitHub issues stay in GitHub, Discord threads stay in Discord, tickets stay in the helpdesk. The backlog holds links, never pasted copies.
- **One theme, one card.** Each new request attaches to an existing card or creates one.
- **Tomas decides, you aggregate.** Every theme ends in a recorded decision with a reason.
- **The loop closes.** Everyone who asked hears the outcome. This is your strongest board evidence.
- **Roles are split.** Support tags, you cluster, Tomas decides. No step depends on one person remembering to do it.

## 2. Intake channels

| Source | Volume | Capture mechanism | Who does it |
|---|---|---|---|
| Discord | ~35/wk | Dedicated `#feedback` forum channel with a post template (problem, what you tried, who is affected). Redirect support questions and bugs out with a canned reply. Add a ✅ reaction when you've carded a post. | Community posts; you sweep |
| Support | ~15/wk | Support tags tickets `product-feedback` in the helpdesk, in place of forwarding to you. You review the weekly tag export. | Support tags; you review |
| GitHub | 8 to 10/wk | Issue forms with a type field (bug / feature / question). Label `feedback` on feature requests. Bugs follow normal SDK triage and never enter the backlog as themes. | You label |

Before launch, support must agree to the tag. Get this agreed this week, because it takes the forwarding work off your plate.

## 3. Theme card (minimum fields)

Keep it to eight fields, or nobody will maintain it.

1. **Title:** the problem, not the solution ("can't filter by metadata at query time", not "add a filter operator").
2. **Evidence links:** one URL per request, not pasted text.
3. **Count:** distinct people or accounts, not messages.
4. **Segment:** free, paid, or enterprise, plus SDK or API surface.
5. **Severity:** blocking, painful, or nice-to-have.
6. **First seen / last seen.**
7. **Status:** `New`, `Needs info`, `Accepted`, `Later`, `Declined`, `Shipped`.
8. **Decision reason:** one sentence, mandatory for `Later` and `Declined`.

Each theme card reaches Tomas's tool only once, as a card. Per-request context stays one click away in the evidence links.

## 4. Weekly routine (target: 2h45)

| Task | Minutes | Notes |
|---|---|---|
| Discord sweep, clustering into cards | 45 | Assume ~24 feedback items; many attach to existing cards |
| Support tag export review | 15 | Tickets arrive pre-tagged |
| GitHub issue labeling | 30 | ~9 issues at ~3 min |
| Card upkeep (counts, severity, merges) | 30 | |
| Close-the-loop replies | 30 | Notify requesters of status changes |
| Weekly digest | 15 | See section 5 |
| **Total** | **165 (2h45)** | 15 minutes of slack |

Re-measure after week 2. If the real total runs above 3 hours, cut in this order:

1. Drop close-the-loop to batch mode (see the template in section 8).
2. Turn the sweep into every other day, with timeboxed 20-minute passes.
3. Have an LLM pre-cluster the raw Discord export, and review only its suggestions.

## 5. Digest

- **Weekly:** replace the long Friday digest with a short one. It holds a link to the live backlog view, the top 3 changes in counts, and any threshold alerts.
- **Threshold alerts (ping Tomas immediately, not on Friday):**
  - a theme reaches 5 distinct requesters
  - a blocking request comes from a paid or enterprise account
  - data loss or security impact (security goes to the security process, not the backlog)
- **Monthly review packet (the main artifact):** one page, sent 2 days before the meeting.
  - Top 5 to 8 themes ranked by count × severity × segment.
  - For each, a proposed decision and the evidence summary.
  - Decisions made last month and their outcomes.

## 6. Monthly review

- **Length:** 45 minutes. Tomas decides; you present evidence and don't argue for outcomes.
- **Output:** every theme in the packet gets a status and a one-line reason, written in the card within 2 business days.
- **Rule:** nothing sits in `New` for more than one review cycle. Tomas must move it to `Accepted`, `Later`, `Declined`, or `Needs info`.
- **Urgent items** go through the threshold alert, not the monthly meeting.

## 7. Closing the loop

1. When a card's status changes, notify the requesters from the evidence links.
2. Declined decisions get the stated reason. A reasoned "no" builds trust.
3. When a theme ships, post it in `#shipped` on Discord and name the theme.
4. Link shipped themes in the changelog as "from your feedback".

## 8. Reply templates (write once)

- **Acknowledgement:** "Thanks, this is logged under [theme]. We review feedback monthly and I'll post the decision here."
- **Support or bug redirect:** a one-line pointer to the right channel.
- **Decision update:** "[Theme] is now [status]. Reason: [one sentence]."

## 9. Four-week plan to the board review

| Week | Do | Done when |
|---|---|---|
| 1 | Get support's tag agreed. Create the `#feedback` channel and GitHub issue forms. Build the card template in Tomas's tool. Fix the review date. | A test item flows from each source to a card |
| 2 | Run the routine live. Measure the real feedback share and the real weekly time. | One full week of cards exists |
| 3 | Send the first monthly packet. Hold the first review, then close the loop on decisions. | Every packet theme has a status and a reason |
| 4 | Collect metrics, build the board slide, rehearse with Tomas. | Slide has real numbers |

**Schedule the first review in week 3, not week 4.** This lets the board see one complete cycle: intake, decision, and requesters notified.

## 10. Board metrics

Report measured numbers only, with baselines from weeks 1 to 4. Targets come after you have data.

- Feedback items received, and how many were actionable themes.
- Share acknowledged within 2 business days.
- Themes decided in the first review (n of N).
- Median days from first report to decision.
- Requesters notified of an outcome.
- One shipped or declined example, told as a story.

## 11. Making it last a year

- **Roles in writing:** support tags, DevRel clusters, Tomas decides. Put this in a one-page runbook so any of them can be replaced.
- **Quarterly hygiene (30 minutes):** archive themes with no new evidence in 6 months, merge duplicates, and re-check the actionable-share assumption.
- **Quarterly audit:** sample 10 closed cards and confirm each has a reason and a notification.
- **Review the process itself every quarter.** If the time budget exceeds 3 hours, cut scope by the order in section 4 rather than working more.
- **Failure signals:**
  - Tomas skips a review twice: escalate to the CEO, who wants this to work.
  - Support stops tagging: this should surface in the weekly tag export before it hurts.

## Open questions

1. What is the backlog tool, and can it link out to GitHub, Discord and the helpdesk?
2. Which helpdesk does support use, and can it export tagged tickets weekly?
3. Can you accept being the only clusterer, or is there a second person for vacations?

Send me those answers and I'll adjust the tool-specific details (channel setup, issue form fields, and the card template).