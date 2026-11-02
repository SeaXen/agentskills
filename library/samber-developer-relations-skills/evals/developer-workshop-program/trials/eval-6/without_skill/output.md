**Next action:** pick your 3 most frequent prospect types (e.g. platform eng, product/experimentation, regulated enterprise). Section 4's track menu depends on them.

I skipped the interview because you asked for the full answer in one response. Every assumption is marked ⚠️. Every number is my own baseline, not an industry standard. Replace each one with your data after the first 3 workshops.

# Fennick workshop curriculum charter

## 1. Gate verdict

⚠️ **Assumption:** the real pain is SE prep cost (about 1 week per workshop), not that prospects can't learn. The cheapest fix is to **standardise and modularise** what exists. A new academy or credential is not needed.

Likely root causes in the current format:
- Slides are rebuilt per prospect, so there is no reusable asset.
- A from-scratch lab is the riskiest, most variable part of the day. It depends on attendee setup, language and typing speed.
- 3 hours of lecture before any hands-on work. Retention and attention drop.

**Rejected cheaper alternative:** a generic recorded webinar. It fails because prospects need a hands-on proof point to move the deal.

## 2. Audience and motion

External prospects, pre-sale. Engineers evaluating Fennick, plus some buyers and architects.

Success is a technical win in the deal. It is not a course completion.

## 3. Tier

**Chosen: structured curriculum with labs, built as a modular library.**

**Deleted rungs:** badge and certification. No outside party counts them for pre-sale prospects, and they add permanent staffing.

**Escalation trigger to a badge:** a customer or partner contract asks for certified heads, and someone can own the assessment indefinitely.

**Fallback if capacity is thin:** a curated path of existing docs and tutorials, with no labs.

## 4. The curriculum shape

**Core idea:** SEs stop building decks. They **assemble** a day from tested modules and spend prep time only on a prospect overlay.

### Competencies

Derive these from real job tasks. Validate against your support tickets and 3 SE interviews before freezing. ⚠️ The list below is a draft.

| # | Competency (task a practitioner performs) | Module |
|---|---|---|
| C1 | Ship a first flag end-to-end, in SDK and dashboard | M1 |
| C2 | Target and roll out gradually, by segment and percentage | M2 |
| C3 | Kill a bad release in seconds, with no deploy | M3 |
| C4 | Run an experiment and read the result | M4 |
| C5 | Govern flags: RBAC, approvals, audit log, environments | M5 |
| C6 | Operate safely: SDK architecture, caching and streaming, outage fallbacks | M6 |
| C7 | Retire flags and manage flag debt | M7 |

Rule: every module traces to a competency, and every competency to a real task. A module that traces to nothing is cut. If more than 20% of modules fail the trace, you wrote from the feature list.

### Module format (each one identical)

1. 10–15 min concept, **max 8 slides**, with an architecture diagram.
2. 25–35 min lab on a checkpointed starter app.
3. 5 min recap, with the "what you can now do" statement.

One concept per module. Slides never run longer than 15 min before hands-on work.

### Lab design (the biggest change)

- **No from-scratch app.** Attendees start from a **pre-built starter app** in a disposable cloud environment (a browser IDE or Codespaces-style environment). Zero local setup.
- **Each module has a start branch and a solution branch.** An attendee who falls behind jumps to the checkpoint and rejoins.
- **Pick one app and one primary language per track.** Cover the other SDKs with a one-line swap, not separate labs.
- **One shared Fennick sandbox org per cohort,** provisioned automatically. SEs don't hand-create accounts.
- The final "capstone" is a short scenario: *"a bad release hits, find and kill it, then run a safe rollout"*. It chains M2, M3 and M5.

### Day templates (the SE picks one)

| Template | Modules | Length |
|---|---|---|
| Foundations | M1, M2, M3, M5 plus capstone | ~5.5 h |
| Experimentation | M1, M2, M4, M7 | ~5.5 h |
| Enterprise and governance | M1, M3, M5, M6 plus capstone | ~5.5 h |
| Short evaluation (half day) | M1, M2, M3 | ~3 h |

Each is a day of alternating concept and lab blocks, not a morning of slides and an afternoon lab. Add M6 or M7 as optional extras.

⚠️ Pick templates from your top 3 prospect types.

### Prospect overlay (what the SE may still customise)

Cap SE prep at about 4 hours. ⚠️ This is a target; measure it.

- Swap the starter app's domain theme and sample data.
- Add 1–2 slides on their stack and use case.
- Tune the capstone scenario to their pain.
- Pick the template and the language.

The SE does **not** change module content, labs or slide structure. Changes go through the library owner.

## 5. Credential decision

None. A completion email with a "next steps" link is enough.

## 6. Operating model

- **Owner:** you, as the single accountable person for curriculum truth. Not a committee. ⚠️ Plan about 6–8 h/week during the build and 3–4 h/week after.
- **Authoring:** you plus 1–2 senior SEs who already run the best workshops. Reuse their best slides first.
- **Technical review:** one engineer per module, for accuracy.
- **Lab maintenance:** a named owner. Starter apps and solutions live in a repo you own, with CI that runs each lab's solution branch.
- **Refresh trigger:** a release that changes UI, SDK or API used in any module reruns that lab's CI and fixes it within an agreed window (⚠️ propose 2 weeks). CI catches lab drift without anyone reading release notes.
- **Platform:** keep all source (slides, labs, scripts) in your own repo. Any lab-hosting tool is replaceable.
- **Video and localisation:** none yet. Both multiply the refresh cost.

## 7. Budget shape

- **Build:** the main cost is people time. ⚠️ Estimate 6–10 weeks to deliver 3 modules and 2 templates, then extend.
- **Run:** lab environment hosting (small), sandbox org automation (engineering time), and ongoing maintenance hours.
- **Payback:** if SE prep drops from about 40 h to about 4 h, then at ⚠️ 2–3 workshops a month the library pays back in about a quarter.

## 8. Measurement plan

Measure all four levels. Stopping at satisfaction scores is the usual failure.

| Level | Metric | First target (⚠️ own baseline) |
|---|---|---|
| Reaction | Post-workshop score | ≥ 4.3 / 5 |
| Learning | % attendees who reach the capstone checkpoint | ≥ 70% |
| Behaviour | Attendees who create a real flag in a trial or POC within 30 days | Track, then set a target after cohort 3 |
| Results | Workshop-to-POC and workshop-to-close rates vs non-workshop deals | Compare after about 10 workshops |
| Efficiency | SE prep hours per workshop | ≤ 4 h |

**Plumbing to decide before launch:** join attendee email to the Fennick workspace and CRM deal. Without it, the behaviour and results levels cannot be rebuilt later. Also check which kind of "no change" you have: a flat behaviour metric may be a deal-process issue, not a curriculum defect.

## 9. Kill rule

⚠️ At month 6, if SE prep is still above 2 days **or** workshop deals show no better POC rate than the baseline, stop building modules. Return to one flexible deck plus a hosted lab. Own baseline, adjust it.

## 10. First 90 days

1. **Weeks 1–2:** interview 3 SEs and review the last ~5 decks. List the repeated slides and the lab steps that fail most. Confirm the top 3 prospect types and the competency list.
2. **Weeks 3–6:** build M1, M2, M3 and the starter app with checkpoints. Pilot the "Short evaluation" template with one friendly prospect.
3. **Weeks 7–10:** build M5 and the capstone. Add CI for labs. Ship the Foundations template.
4. **Weeks 11–13:** run 3 live workshops. Collect prep hours, checkpoint reach, and feedback. Rebalance. Then build the next template.

## 11. Source of numbers

All numbers are my own baselines, marked ⚠️: the module length, the 8-slide cap, the 4 h prep target, the 70% and 4.3 targets, the 2-week refresh window, and the build time and hours. None are published standards. Replace each with a measured value after cohort 3.

## Open items (ask me, one at a time)

- What are your top prospect types, and what language mix do they use?
- What breaks most in the current afternoon lab?
- Is a lab-hosting platform already in place?
- How many workshops per month today?

**Next:** answer the first question (top 3 prospect types) and I'll tighten the templates.