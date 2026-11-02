# Measurement Plan: Pipeline Sourced from Events — Porto Hackathon & Chicago Platform Engineering Conference (2027)

## 0. The mandate has a flaw — this plan compensates for it, doesn't fight it

"Pipeline sourced from events" as a single board KPI assumes one funnel. Kilnworks runs two, and they don't share a clock or a definition of "pipeline":

- **Self-serve ($0→$29/mo, card, no sales contact):** often has no formal pipeline stage at all — a visitor becomes a paying customer in one session. "Pipeline" has to be defined into existence.
- **Enterprise (4-person team, 9-month cycle):** has a real pipeline, but it won't show a dollar from a September event until Q2–Q3 2028 at the earliest.

Left unaddressed, this produces one of two failures on the board slide: Porto reports ~$0 forever (true, but reads as sponsorship failure) or someone under pressure inflates Chicago's near-term number by counting badge scans as pipeline (false, and it corrodes trust in every future event number).

The fix below keeps leadership's single KPI, but defines it so both motions can feed it honestly, and builds in the maturation curve so a $0 quarter doesn't get misread.

---

## 1. The board KPI, defined

```
Pipeline Sourced from Events (cumulative since event)
  = Σ Enterprise Opportunity Amount, where original-source = event, stage ≥ Qualified
  + Σ Self-Serve ACV-Equivalent, where first-touch source = event, account status = active paid
```

**Self-serve has no native "pipeline" stage — create one.** Define it as the moment a trial/signup activates (first meaningful product use, not just an email address), valued at:

```
ACV-equivalent = plan price × 12 × historical trial→paid conversion rate [Kilnworks: fill in from last 12 months]
```

This mirrors enterprise "Pipeline Created" — a forward-looking, unqualified dollar estimate, not a closed-won number. Don't value it at $29×12 flat; that overstates it the same way counting every enterprise lead as an Opportunity would.

**Sourced, not Influenced, for the headline number.** Enterprise deals touch many things over 9 months; a hackathon and a conference will each show up as one touch among several on some accounts. Use **first meaningful touch that created the account/contact record** as "sourced" — the same rule for both motions. Track "Influenced" (event appears anywhere in the touch history) as a supporting line only, never blended into the headline (per standard attribution model discipline — mixing single-touch and multi-touch credit inside one number is how board metrics quietly become fiction).

**Anchor at the account (domain) level for enterprise, individual (email/GitHub) level for self-serve.** Enterprise deals involve multiple stakeholders; crediting the event only to whichever person filled a form undercounts it. Self-serve is bought by individuals; account-level anchoring would overcount.

---

## 2. Attribution window and reporting cadence — the part that prevents a misread

| Motion | Attribution window | When it shows up |
|---|---|---|
| Self-serve | 90 days from event | Same or next quarter |
| Enterprise | 12 months rolling from event | Starts trickling in ~Q2–Q3 2028 for Chicago |

Report the **same single board number every quarter**, but always with two footnote lines underneath:

```
Pipeline Sourced from Events — 2027: $[X]
  ↳ Self-serve: $[X]  (Porto: $[x] | Chicago: $[x])
  ↳ Enterprise: $[X]  (Porto: $0 expected | Chicago: still maturing — 9-mo cycle, first opps expected Q[n])
```

Give leadership this line to say to the board proactively, before anyone reads a $0 quarter as failure: *"Enterprise pipeline from Chicago is on a 9-month clock by design — we're tracking leading indicators (qualified conversations, meetings booked) until it converts to dollar pipeline."* A board that hears the maturation curve once won't need it explained twice.

---

## 3. Path C — the case a single-event-to-single-motion model misses

Chicago is not a clean enterprise-only event. Platform engineers who attend will also grab the self-serve CLI on their own card, independent of any sales conversation. Two things follow:

1. **Tag by motion at the point of capture, not by which event produced the lead.** A Chicago badge scan can become either a self-serve signup or an enterprise Opportunity — sometimes both, from different people at the same company.
2. **Bottoms-up expansion path:** if a self-serve account's domain later becomes an enterprise Opportunity (a platform engineer's personal $29/mo habit turns into a top-down deal), tag the Opportunity source as `expansion — self-serve-led`, keep the original event in a lineage field, and count the dollar value **once**, in enterprise pipeline. Credit the original event only in the leading-indicator report (§6), not a second time in the board number. Skipping this rule is the most likely way Kilnworks double-counts a single account across both motions.

---

## 4. Event-specific tagging mechanics

**Porto (hackathon, 500 students, self-serve-only in the near term):**
- Event-specific promo/coupon code redeemable at signup (e.g., extra free months) — highest-confidence tag, tie to CLI account directly.
- UTM on any pre/post-event link (workshop signup, swag QR code).
- Self-reported field at signup: "How did you hear about us?" with a dropdown option naming the event, plus free text.
- GitHub identity capture at booth/workshop if participants star or fork a repo — useful for the recruiting/evangelist path, not for the pipeline KPI itself.
- Expect near-$0 same-quarter pipeline. That's correct, not a failure — see hiring/evangelist note in §6.

**Chicago (enterprise conference):**
- Badge scans land in CRM as a raw `Lead`, explicitly **not** an MQL — a scan is a person who walked past the booth, not a qualified contact.
- Structured conversation notes required for anything counted higher than a scan: company, role, pain point, agreed next step. No notes, no upgrade past `Lead`.
- Pre-booked meetings (booked by the sales team before the event) get their own bucket — they're higher-intent than anything generated on the floor and should be tracked separately to judge pre-event outreach effectiveness.
- Self-reported field on any demo-request or contact form.
- **Original-source field is locked at creation.** A common failure mode: a rep updates "lead source" mid-deal to whatever they last did, and the event's credit silently disappears three CRM stages later. Use a separate, non-editable `original_source` field distinct from whatever "last activity source" field the CRM tracks for its own reporting.

---

## 5. CRM field schema (build this before either event, not after)

| Field | Values | Notes |
|---|---|---|
| `event_id` | `porto_hackathon_2027`, `chicago_pe_conf_2027` | Stable, never renamed |
| `motion` | `self_serve` \| `enterprise` | Set at capture, not inherited from event |
| `touch_type` | `scan`, `conversation`, `meeting_booked`, `promo_redemption`, `self_reported` | Determines confidence tier |
| `source_type` | `sourced` \| `influenced` | `sourced` = first meaningful touch only |
| `confidence` | `high` (promo code, booked meeting) \| `medium` (logged conversation) \| `self_reported` | Never blend tiers silently in the headline number |
| `original_source` | locked at creation | Never overwritten by later stage changes |
| `account_domain` | dedup key | Required for expansion-path tracking (§3) |
| `captured_at` | timestamp | |

---

## 6. Leading indicators — what tells you the events are working before the board KPI can

The 9-month enterprise cycle and Porto's realistic ceiling (brand/hiring, not near-term revenue) mean the board KPI alone will leave both teams blind for two-plus quarters. Track these underneath, reviewed monthly, never presented as the headline number:

**Porto:**
- Qualified booth conversations (not scans) ÷ total interactions
- Promo-code signups and 30/60/90-day activation retention
- Hires sourced from the event (a real ROI line for a 500-person student hackathon, distinct from pipeline)
- Any account whose domain later shows up in an enterprise deal (Path C tripwire)

**Chicago:**
- Qualified conversations ÷ badge scans (catches "we scanned everyone, talked to no one")
- Meetings booked (pre-event + onsite), tracked separately
- Opportunities created (count and stage, before dollar value matures)
- **Cost per qualified meeting**, benchmarked against the enterprise team's other channels (outbound, referral) — this is the actual go/no-go number for renewing the Chicago sponsorship in 2028, not the board KPI, which won't have matured by renewal-decision time.

---

## 7. Guardrails

- **Never let a scan count as a lead, and never let a lead count as pipeline.** Each promotion happens only on evidence (conversation notes, code redemption, self-report) — this is the single most common way event ROI gets faked upward.
- **Never pressure Porto to show same-quarter pipeline.** It won't, by design. Forcing it is what produces junk CRM entries from a team trying to hit a number the motion can't produce on that timeline.
- **Never sum "sourced" and "influenced."** Report them as separate lines; blending them is how a board number quietly stops meaning anything.
- **Never let `original_source` be overwritten.** Audit this quarterly — it's the field most likely to get silently clobbered by normal CRM hygiene automations.
- **Dedupe Path C explicitly, every quarter.** Check for domains that appear in both self-serve and enterprise pipeline; resolve to the expansion rule in §3 before the number goes on the slide.