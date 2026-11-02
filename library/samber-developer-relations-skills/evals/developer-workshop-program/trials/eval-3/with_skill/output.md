# Lab plan check: Hollin & Rowe half-day workshop

**Verdict: reshape. Don't run the plan as written.** It fails at minute zero in four places. The fixes are cheap if you start this week.

**Assumed (no one to interview, so please confirm):**
- This is a technical-win job: the bank is evaluating the SDK in an open opportunity.
- The SE team delivers.
- The bank's laptops are corporate-managed.
- The VPN is full-tunnel.
- Nothing in the lab needs bank data.
- Today is 2026-10-31 and the workshop falls in November.

## 1. Grant decision

**Reshaped grant, conditional.** The format is a guided lab half-day on vendor-provisioned environments. I can't see the opportunity, so the four grant-rule items stay open until you confirm each in writing. Don't send invitations until they hold.

| Grant-rule item | Status | What to do |
|---|---|---|
| Open, qualified opportunity with a named champion | Unknown | Name the champion and the CRM stage in the brief. |
| Discovery names one use case, mapped to a module | Missing | Write one sentence, e.g. "instrument a service and see traces and logs in the collector within the session". |
| Decision maker attends the opening or the 20-minute readout | Missing | Ask the champion for a name. 18 practitioners with nobody who chooses the vendor is the "wrong room" failure. |
| Next-step agreement written before the date is set | Missing | See section 5. |

If the champion or decision maker can't be named, the fallback is a short virtual follow-along whose agreed next step is naming them. The full rule applies to anything longer.

## 2. What breaks in the plan, ranked by blast radius

1. **Laptop install of the CLI and agent.** Managed bank laptops usually remove install rights, and the VPN is a further unknown. The runbook says to delete laptop installs whenever laptops are corporate-managed or the network is unknown. One lab-platform webinar puts self-provisioning at an hour or two of workshop time. With 18 people in a 4-hour half-day, that is most of the lab.
2. **18 free-trial sign-ups at minute zero.** Each is a failure point:
   - A bank may block sign-ups to outside services from work email, or require approval.
   - Each attendee personally accepts your terms, which is a legal and security-review trigger for a bank.
   - One verification email in a spam quarantine stalls a person for the session.
3. **Cloud logging service with a 1-2 day readiness lag.** Accounts created at the start of the session can't be ready that day. Nothing downstream of logging can pass its checkpoint, and the failure looks like the product's fault. The rule is to find the slowest provisioning step and schedule from it. AWS documents 48 hours for one security workshop, so this lag is a known pattern.
4. **Corporate VPN, even in the office.** A VPN can block the hosted collector or trial cluster outright. Egress domains, ports and IP allow-lists are all unknown. Home and office addresses differ.
5. **18 attendees against a single instructor.** The staffing baseline is one instructor plus one helper per started block of 10 attendees, so you need 1 instructor and 2 helpers.

## 3. Lab environment standard for this workshop

Environment order, efficiency first: vendor-provisioned disposable environment > attendee trial account > shared hosted environment > customer's own environment > laptop installs. Use the first.

| Setting | Decision |
|---|---|
| Environment | One pre-built, least-privilege, auto-expiring environment per attendee, on your infrastructure |
| Access | Browser-based terminal or editor with the CLI and agent pre-installed, so attendees install nothing on the laptop. Check whether your lab tooling can do this. If not, tell me before committing to the date |
| Pool size | 18 confirmed (calendar acceptance) + 2 spares = 20 |
| Cloud logging | Create one vendor-held account now, with per-attendee isolated projects or tenants inside it. One shared cluster is the "one mistake breaks everyone" failure |
| Provisioning schedule | Create the logging account at least 5 business days before the session (baseline). Your "a day or two" is the stated lead time and I haven't verified it. Ask the logging vendor for the documented figure and schedule from the larger number. The buffer covers a stuck verification |
| Time-to-live | Longer than the full session including breaks, e.g. 8 hours for a 4-hour event |
| Data | Synthetic only, matching a bank-like schema. Never ask for bank credentials or data |
| Teardown | Set expiry at creation. Destroy everything the day after the session |
| Trial sign-up | Move it to **after** the session as the take-home path, on attendees' own time, with explicit cleanup steps. Offer trial credits if the lab costs money |

Because the environments are vendor-held with synthetic data, the session shouldn't trigger a customer security review. The original plan (agent on managed laptops, work-email sign-ups) probably would.

## 4. Network and VPN: the dry run decides the date

Send this checklist to the champion in the logistics call (items from the runbook, applied here):

- Attendees stay on the corporate VPN, even on site. Is a full tunnel in force, and is split tunnelling excluded?
- Which outbound domains and ports does the lab need (lab-platform URL, hosted collector endpoint, logging service endpoint)? Please allow-list them.
- Do IP allow-lists apply, and do the addresses differ between home and office?
- Can attendees open our lab URL in a browser on managed laptops, and are WebSockets allowed (needed for browser terminals)?
- Who at the bank can change any of the above on the day, with a phone number?

**Dry run:** one onsite attendee, on the VPN, on a managed laptop, opens the lab, runs prerequisites and completes module 1. Do it at least a week before the session, so there is time for an allow-list change.

**Decision rule:** if the dry run fails and the allow-list isn't fixed by 5 business days before the date, reshape to an instructor-led demo on a shared screen with the take-home lab. Don't run a hands-on session you know will break.

## 5. Workshop brief

```
Account / job / stage:   Hollin & Rowe / technical win / <CRM stage>   (assumed, confirm)
Champion:                <name, role>          Decision maker: <name, role>, attends opening + readout
Use case (one sentence): <to confirm with champion> -> module: instrument a sample app, see signals in the hosted collector
Attendees:               18 confirmed (names, roles, skill level, prior exposure), calendar acceptances in hand
Format / environment:    Guided lab half-day / vendor-provisioned, 20 environments (18 + 2 spares)
Logistics call:          this week          Dry run (bank network, VPN, managed laptop): T-7 days or earlier
Automated checkpoint test: within 24 h before delivery
Logging account created: T-5 business days or earlier
Instructor / helpers:    1 instructor + 2 helpers, all on the certification ladder
AE role:                 opening, readout, next-step conversation with the champion
Follow-up owner:         <name>, champion recap within 1 business day
```

**Next-step agreement** (write it with the champion before the date is final):

```
Success criterion (proposal): at least 12 of 18 attendees reach checkpoint 4
                              (their instrumented sample app's data visible in the collector) unaided
                              [baseline, replace with your own figure after one quarter]
If met:      POC scope session on <date>   Owner (vendor): <name>   Owner (bank): <name>
If not met:  fix the cause (environment, use case, attendees) before a second workshop
Agreed by champion: <name, date>      Agreed by AE: <name, date>
```

**Agenda** (guided lab half-day template, 18 attendees):

```
09:00  Welcome, goal of the day, success criterion (champion + SE)             10 min
09:10  Problem framing: their use case in their words                          10 min
09:20  Module 1 - instrument the sample app (checkpoints 1-3)                  60 min
10:20  Break                                                                   15 min
10:35  Debrief module 1, one concept block under 15 minutes                    15 min
10:50  Module 2 - collector and logging, query the data (checkpoints 4-6)      60 min
11:50  Readout with the decision maker: checkpoint results, next step          20 min
12:10  Close; take-home lab path, trial sign-up instructions, help channel      5 min
Staffing: 1 instructor + 2 helpers (18 attendees)
```

- Every checkpoint is script-verifiable and ships a solution state, so a stuck attendee can skip forward.
- Prerequisites are three lines: knowledge, machine and network state (browser and VPN), accounts (none to create).
- No sign-up at minute zero.

## 6. Rehearsal and checkpoint test

Run these in order:

1. The instructor runs both modules alone on a fresh environment this week.
2. Run the nightly automated check, then check/solve/check on every checkpoint: setup, check fails, solve, check passes.
3. Run the dry run on the bank network (section 4).
4. Run the checkpoint test again within 24 hours before delivery.
5. Confirm the logging account is live and each attendee environment resolves.

If any step fails, the date moves. Don't walk in with an untested lab.

## 7. Follow-up

- Within 1 business day, send the champion the checkpoint results per module, the success-criterion outcome, and the agreed step with its date.
- Attendees get the take-home lab and a help channel. They get technical help, never a sales call or a nurture sequence.
- The AE works the champion and the decision maker.

## 8. Scorecard (this workshop)

| Account | Job | L1 rating | L2 checkpoint completion | L3 active at 30 / 60 days | L4 next step executed in 30 days | Notes |
|---|---|---|---|---|---|---|
| Hollin & Rowe | Technical win | end-of-day rating + 1 open question | x/18 at checkpoints 3 and 6, from check scripts | attendees active in their own trial at 30 / 60 days | POC scope session held on the agreed date | Log against the opportunity today, with attendees linked and the grant decision recorded |

Also record:
- show rate against the 18 confirmed attendees
- lab defect (any checkpoint failing for environment reasons)
- delivery hours spent

This one account is a data point, not proof. Report any pipeline as "influenced", never "caused".

## 9. Open decisions

Please confirm or correct:

1. Champion, decision maker and CRM stage (grant rule).
2. The one use case this workshop proves.
3. That the bank's laptops are managed with removed install rights.
4. That the VPN is full-tunnel.
5. That your lab tooling can offer a browser-based environment with the CLI and agent pre-installed.
6. The logging service's documented provisioning lead time, to confirm or replace "a day or two".
7. Who instructs, plus which two helpers, and where each sits on the certification ladder.
8. The workshop date, so I can fix the T-minus dates.