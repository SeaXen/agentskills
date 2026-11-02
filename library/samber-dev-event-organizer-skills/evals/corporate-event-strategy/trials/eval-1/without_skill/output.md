# VexoraConf 2027: goal and measurement plan

## 1. Recommendation

**Don't commit to a sourced-pipeline number.** Commit to a goal you can defend, and commit to the measurement system now.

- **Why sourced pipeline fails.** Your own mix is 80-85% existing customers, so about 60-80 of 400 seats are non-customers. Many of those are champions, who are already users or advocates.
- **Illustrative math.** Suppose 20 of those people became paying accounts at the $49/month entry plan. That is 20 × $49 × 12 ≈ **$11.8k ARR**. This is my arithmetic, not a forecast. Sourced new-logo pipeline can't carry a 400-seat event, and a number promised on that basis would be missed or padded.
- **What the event can do.** It can plausibly drive **expansion and retention** among customers: upgrades, added seats, more pipelines monitored, and fewer churned accounts. Self-serve has no sales-cycle pipeline, so this is the revenue the event can move.
- **No history yet.** You have no baseline, and registration has never been connected to the CRM. Any number promised today would be a guess.

**Proposed stated goal:**
> VexoraConf 2027 increases paid expansion and retention among attending accounts, measured against a matched non-attending control, read at 90 days post-event. New-logo pipeline is tracked and reported as a secondary, influenced figure.

Frame it to your CRO as a measurement commitment. "Sourced" means you can prove the event created the opportunity. Here, "influenced" is the honest word.

## 2. What to commit to the board

| Commit now | Don't commit |
|---|---|
| Registration connected to CRM and billing before registration opens | A sourced-pipeline dollar figure |
| A written attribution rule (section 4) | An absolute revenue target before any baseline exists |
| A control group for the expansion read | Registrations or opens as "success" |
| A baselined target range, set 60 days before the event | |
| A 90-day readout in the next quarterly review | |

You have time. There is no fixed deadline and the event is about 8 months out, so use it to build the baseline. Pull trailing 6-12 months of expansion and churn for the whole customer list now. That becomes the pre-period.

## 3. Metrics (7)

Each threshold is tagged `baseline` (self-set from your history) or `hypothesis` (a guess to test). None is `sourced`, because no published benchmark applies here.

| # | Metric | Tier | Definition | Source | Threshold | Owner | Action if off |
|---|---|---|---|---|---|---|---|
| 1 | **Primary: expansion lift** | Business | 90-day net expansion MRR per account, attendees vs matched non-attendees | Billing + CRM | `baseline`: set a range after pre-period, 60 days pre-event | Marketing + RevOps | Flat: fix post-event offer and follow-up before funding a 2028 event |
| 2 | 90-day logo retention, attendee vs control | Product | % of accounts still paying | Billing | `baseline` | Marketing | Worse than control: audit agenda and audience fit |
| 3 | Attendee activation depth | Product | Pipelines/sources monitored per attending account, 30 days before vs after | Product analytics | `baseline` | Product marketing | Flat: add hands-on workshops next time |
| 4 | Show rate | Engagement | Attended / registered, by segment | Registration tool | `hypothesis`: use first event as baseline | Events | Low: fix invitation and reminder flow |
| 5 | Qualified conversations | Engagement | Staff-logged, with context and next step. Not badge scans | Event staff form | Raw list (small N) | Sales + marketing | Route hot ones within 48h |
| 6 | Non-customer conversion (influenced) | Business | Non-customer attendees who start a paid plan within 90 days | Registration → billing | Raw list and count, not a rate | Marketing | Few: use the community/champion track for reach, not conversion |
| 7 | Self-reported source | Engagement | One post-event question: "What made you attend / consider upgrading?" | Survey | Response rate tracked | Marketing | Use as the sanity check on the attribution in #1 |

Two guardrails:
- Pair show rate (#4) with attendee quality. A full room of people who never log in again is not a win.
- Report non-customer outcomes (#6) as a raw list. A rate on 60-80 people swings too wildly to mean anything.

## 4. Attribution rule (write it before registration opens)

- **Method.** Matched control. Your 400 seats come from a much larger user list, so invitees who didn't attend, plus similar uninvited accounts, form a natural comparison group. Match on plan, tenure, and trailing usage.
- **Window.** 90 days post-event for expansion and retention; 90 days for non-customer conversion.
- **Language.** Credit is always "influenced", never "sourced". Event touches are multi-touch and shared with product, email and sales.
- **No double-claiming.** Revenue the event influenced stays visible to other teams too. Marketing doesn't take sole credit.
- **Caveat to state.** Attendees self-select. Engaged customers attend and expand more regardless, so a raw attendee-vs-rest comparison overstates lift. The matched control reduces this bias but doesn't remove it. Say so in the readout.

## 5. Setup work (start now)

1. **Join registration to CRM and billing.** Use the account email or domain. Capture company and role at registration.
2. **Tag every attendee** with a `vexoraconf-2027` campaign member status: invited, registered, attended, no-show. Put champions in their own segment.
3. **Snapshot the pre-period** (trailing 6-12 months of expansion, churn and activation for all invitees) before invitations go out. You can't recover it afterwards.
4. **Stand up the staff conversation form** and the post-event self-report survey.
5. **Pre-agree with the CRO** which metrics count and how credit is shared. Do this before the event so the numbers can't be argued afterwards.

## 6. Blind spots to publish

- **No baseline yet.** Targets stay ranges until the pre-period is pulled.
- **Self-selection bias** in attendees (see section 4).
- **Champions** probably produce reach, content and goodwill rather than revenue. Nothing here measures that, so decide if it matters.
- **One event is a weak sample.** The first run underperforms its steady state. Judge on a 2-3 event trend.
- **Long-lag effects**, like reduced churn after a year, won't show in a 90-day read.
- **Email opens** are unreliable and aren't used here.

## 7. What to tell the CRO

> "A 400-seat room that's 80-85% customers is an expansion and retention event, and I'll measure it that way against a control group. At $49/month entry plans, new-logo pipeline from the 60-80 non-customer seats is small, and committing to a number now would be a guess. I'll connect registration to CRM and billing before we open registration, and commit to a baselined expansion range 60 days before the event. You'll get the 90-day readout at the following quarterly review."

If she insists on a pipeline number, the honest fallback is to report only the **influenced new-logo count** from non-customer attendees (#6) after the event. Don't pre-commit a dollar figure.

## 8. Decisions I need from you

1. Does the CRO's pipeline ask include expansion revenue, or only new logos? That decides whether #1 satisfies her.
2. What is the event budget? With it, I can compute the expansion lift needed to break even.
3. Can billing and CRM data be joined on account email today?