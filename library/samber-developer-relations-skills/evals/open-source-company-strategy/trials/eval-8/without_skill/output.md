# Ostrava Mobility — Open Source Decision-Rights Model

## One change before the model: don't make OSPO the sole approver

A single approver for every release just moves today's bottleneck, it doesn't remove it. Two FTE and a fractional attorney reviewing every request from 600 engineers across six BUs will still take three weeks — the queue just has one line instead of six. The three-week delay isn't caused by *having too many approvers*; it's caused by **every request being negotiated from first principles**, because there's no pre-agreed answer for the common cases.

The fix is a **decision-rights model**, not a single decision-maker: OSPO owns the *policy* and is the decider for the small set of cases that genuinely need judgment. Everything routine gets a pre-cleared, self-serve path. That's what gives BUs a consistent, fast answer without 2.5 people reviewing 600 engineers' work line by line.

---

## Design principles

1. **Default is a checklist, not a conversation.** Most releases (internal tooling, SDKs with no proprietary logic, docs, bug-fix contributions upstream) should clear in a day via self-certification against fixed criteria — no OSPO time spent.
2. **OSPO's time goes to the exceptions.** Reserve OSPO/Legal review for the requests that actually carry risk: IP, export control, trademark, competitive exposure, or anything touching regulated/safety data.
3. **One policy, six business units.** The criteria are identical everywhere. What varies is who's authorized to apply them — not what the answer is.
4. **Every "no" comes with a reason and a next step.** No open-ended holds. If a request is blocked, the requester gets the specific gate it failed and what would clear it.
5. **Rights are earned, not assumed.** A BU gets broader self-serve authority once it demonstrates it applies the checklist correctly (see Delegation, below) — this is how the model scales without OSPO headcount scaling 1:1 with engineering headcount.

---

## The three tiers

| Tier | What it covers | Who decides | Target turnaround |
|---|---|---|---|
| **Green — Self-serve** | Passes every item on the pre-cleared checklist (below) | BU engineering lead (self-certifies) | Same day |
| **Amber — Standard review** | Fails one checklist item, or is ambiguous | OSPO | 5 business days |
| **Red — Strategic review** | Trips a hard-stop criterion | OSPO + Legal, escalates to exec sponsor if unresolved | 10 business days, with interim written status at day 5 |

### Green-tier checklist (all must be true to self-certify)

- No patented or patent-pending technique invented at Ostrava.
- Not part of a system that handles vehicle safety, braking, or collision logic.
- Contains no live customer telemetry, location data, or data schemas tied to a specific fleet customer.
- Uses a standard, pre-approved license (Apache-2.0 or MIT — OSPO publishes the list; no custom or copyleft license without amber review).
- No third-party code of unclear provenance is being contributed back (i.e., it's Ostrava-authored or already-open code).
- Doesn't reference unannounced products, unreleased roadmap, or unreleased customer names.
- Repo name/branding doesn't imply an official product (avoids trademark exposure).

If every box is checked, the BU lead files a one-page self-certification (template owned by OSPO) and publishes. OSPO gets a copy for its register — informed, not consulted.

### What always escalates to Red, regardless of BU

- Anything touching GPS/location precision, mapping, or telemetry protocols with potential export-control exposure (ITAR/EAR-adjacent).
- Anything that could preview material nonpublic information — since Ostrava is listed, a repo that signals an unannounced acquisition, partnership, or product direction is an IR/disclosure question, not just a legal one.
- Anything a competitor could use to infer fleet customer names, volumes, or contract terms.
- Dual-licensing or any commercial-open-core structure (revenue-model decision, not a publishing decision).

---

## RACI by tier

| Activity | BU Eng Lead | OSPO | Legal (part-time) | Security | Exec Sponsor | IR/Corp Comms |
|---|---|---|---|---|---|---|
| Apply green-tier checklist | **R/A** | I | – | – | – | – |
| Maintain/update the checklist & license list | C | **R/A** | C | C | I | – |
| Amber review | C | **R/A** | C (as needed) | C (as needed) | I | – |
| Red review | C | **R/A** | **R** | C | **A** (final call if OSPO/Legal split) | C |
| Publish decision log / register | I | **R/A** | – | – | I | – |
| Quarterly policy review | C | **R/A** | C | C | **A** | C |

R = Responsible (does the work), A = Accountable (owns the outcome), C = Consulted, I = Informed.

Note Legal only holds an **R** in Red tier — the part-time attorney's time is the scarcest resource in this office, and the whole point of the tiering is to stop spending it on green-tier requests.

---

## Delegation: how BUs earn broader self-serve rights

- Every BU starts on the standard checklist above.
- After a BU logs **10 consecutive green-tier releases with zero OSPO-identified errors on spot-check** (OSPO audits ~20% of green submissions retroactively, not gating), that BU's lead can self-certify one additional category — e.g., third-party contributions back to upstream projects — without escalating it to amber.
- Any BU that has a green-tier release later found to be misclassified (should have been amber/red) loses self-serve rights for that category for one quarter and returns to full OSPO review. This is a control, not a punishment — it's what makes it safe to delegate at all.

---

## Escalation and disagreement

- If a BU disagrees with an amber/red decision, it escalates once — to the OSPO lead directly, not around them.
- If still unresolved after that conversation, it goes to the exec sponsor (whoever on the exec team owns this proposal) for a final call within 5 business days. No request sits in limbo past that.
- OSPO logs every escalation and its resolution. If the same category of request escalates 3+ times in a quarter, that's a signal the checklist itself needs to change — not that the BU is being difficult. Feed it back into the quarterly policy review.

---

## Governance cadence

- **Quarterly:** OSPO reviews the decision log with Legal and Security — which categories are escalating, which BUs are ready for delegation, whether the checklist needs new hard-stops (e.g., a new regulation, a new product line with new data sensitivity).
- **Annually:** Exec sponsor reviews aggregate metrics and re-affirms or adjusts OSPO's mandate.

---

## Metrics to report to the exec team

| Metric | Why it matters |
|---|---|
| % of requests resolved green (self-serve) | Shows the model is actually absorbing volume, not routing everything to OSPO anyway |
| Median turnaround by tier | The number the BUs actually feel — replaces "three weeks" |
| Escalation rate to Red | Should be low and stable; a spike means a new risk category has appeared and the checklist needs updating |
| Misclassification rate on audited green submissions | The safety valve — proves delegation isn't quietly increasing risk |
| Requests per BU vs. BU engineering headcount | Flags whether one BU is systematically under- or over-using the fast path, worth a conversation either way |

---

## Rollout

1. **Weeks 1–2:** OSPO finalizes the checklist and hard-stop list with Legal and Security; circulate to all six BU eng leads for comment.
2. **Weeks 3–4:** Pilot with two BUs (one high-volume, one with the most safety/telemetry-adjacent code, to stress-test the hard-stops).
3. **Week 5:** Adjust based on pilot friction; publish self-certification template and decision log.
4. **Weeks 6–8:** Roll out to remaining four BUs.
5. **Week 12:** First metrics review with exec sponsor — this is the moment to confirm the three-week problem is actually solved, not just relabeled.

---

**The pitch to the exec team, in one line:** give OSPO the authority to set the rules and decide the exceptions, not the job of personally reading every line of code six business units want to publish — that's the version of "single approver" that actually survives contact with 600 engineers.