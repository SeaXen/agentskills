# Portico Summit: Foundry Compute expedition brief (Sintra, day before the conference)

I followed the `event-learning-expedition-design` skill and its evidence reference. I did not read the sibling skills it hands off to, so those parts are inputs to hand off, not finished deliverables. Each section needs your validation before anything goes to Foundry or to attendees.

## Status

⚠️ **Not ready to announce to attendees.** The skill's single pass gate needs four items in writing with zero blanks. You have one and a half.

| Required item | State |
|---|---|
| Host's yes and its conditions | ✅ Written yes. Conditions: no photography in data halls, escort at all times. |
| Named counterpart inside the host | ⚠️ Director of infrastructure is named. Unknown whether they can commit colleagues' time, or only their own (Q4). |
| Access posture and the restriction list behind it | ⚠️ Posture drafted below. The restriction list is incomplete. |
| Person who handles anything an attendee wants to publish | ❌ Blank. |

## 1. Routing: what belongs to another skill

| Your item | Owner | What happens here |
|---|---|---|
| (1) Backup datacenter | This skill (host dependency) | Answered below. The skill says no to a standby host. |
| (2) NPS uplift and pipeline | `corporate-event-strategy` | Not defined here. Only the skill's own signals are listed. |
| (3) Transport and boxed lunches | `event-hospitality`, `event-vendor-sourcing` | Hand-off inputs only. |
| (4) Code of conduct on the coach | `event-code-of-conduct` | I can't confirm it. See §5. |

## 2. Backup datacenter: don't line one up as a substitute

❌ **Don't hold a second datacenter on standby the way you hold backup venues.**

- A venue that falls through costs you a room you can re-book. A host that falls through deletes the programme, because Foundry's halls and staff are the programme.
- The skill states it directly: "A second host is not a substitute for the first. It is a different event."
- A second datacenter would need its own cold approach, screening, escort rules, restriction list and brief. It would not be a drop-in.
- The skill also warns against copying the several-venues-against-several-dates mechanic from venue sourcing.

**What to do instead: make a Foundry cancellation survivable.**

1. **Pick your fallback for a lost host now.** The only fallback is a degraded version of this expedition, not an equivalent.
   - Ask Foundry's director whether an engineer would speak in your room if the site closes.
   - That option is weak. Q2 probably names a physical thing: the halls, the hardware, the scale. If so, the skill deletes the "host representative in your own room" rung as a real alternative. Treat it as a consolation prize and label it that way to attendees.
2. **Fix a go/no-go date with Foundry** after which you commit transport and lunches. This is a date for Foundry to state, not one I invent.
3. **Make cancellation cheap.** Ask the hospitality and vendor owners for contract terms that release the bus and the boxed lunches without penalty if Foundry withdraws before that date.
4. **Keep the seats as a soft offer.** Tell the 35 attendees the visit is "confirmed by the host, subject to the host's operational needs," not guaranteed.
5. **Optional second host.** Pursue one only as a separate, later-decided event, and only if you already have a standing relationship with that company (Q9). A cold approach on top of this ops plan is the configuration the skill warns against.

**What would flip this:** a second operator you already have a relationship with and real runway (Q8, Q9). That gets you an independent second expedition, not a backup.

## 3. Success metrics (NPS uplift, influenced pipeline)

Both belong to `corporate-event-strategy`, so I'm not defining them here. Three notes for that hand-off:

- **NPS uplift on 35 of 600 people** is a small, self-selected group. Settle the baseline and comparison group in that skill before promising a number.
- **Influenced pipeline** needs an attribution rule written before the day. Foundry's own sales interest is also a conflict risk (see "marketing team writes the agenda" in §4).
- **The skill's own measurement is self-set, not an external benchmark.** Record these after the event:
  - Did Foundry withdraw, and at what notice?
  - Did the agenda that ran match the brief you sent?
  - How many attendees asked to publish something, and how long did each wait?
  - Would Foundry receive you again? This is the only signal that compounds, so write it down.

## 4. Posture decisions and host brief

**Host-dependency posture: one host site, host-led (default).**
- Promote it to a negotiated agenda only if your attendees' question is specific (Q3) and the director can commit their colleagues' time (Q4). Both must hold.
- Delete the negotiated-agenda rung if Q4 fails.
- Multi-host circuit: not applicable.

**Access posture: named ground rules, no instrument.**
- ✅ **"Open on the record" is deleted.** Foundry stated restrictions through someone who speaks for them (Q5).
- ❌ **The per-attendee undertaking is not promoted.** It needs a bounded attendee list (Q6) and a host yes conditioned on it (Q1). Foundry's conditions are photography and escort, not signatures. Revisit if Foundry asks for signatures.
- ❌ **Relayed clearance is not viable until someone is named to run the queue (Q7).**

**Restriction list so far:**
1. No photography in the data halls.
2. The group stays with an escort at all times.

**Gaps to close (silence is not permission):**
- Is photography allowed anywhere else on site, such as the lobby or the car park?
- May attendees write notes, post, or name Foundry afterwards?
- Does the escort impose a group size or a movement order?
- Are there customer-name or equipment restrictions?

State the ground rules to attendees before they travel, not at the door.

**Host brief to send Foundry** (draft; send it before their internal approvals start):

> Portico Summit brings 600 infrastructure practitioners to Lisbon. On [day before], 35 attendees visit your Sintra facility. They want to understand how a production datacenter operates: [fill from Q2/Q3]. We ask your people to: [fill: host, escort, speak]. Attendees will be told before travel: no photography inside data halls; the group stays with your escort throughout; [add any further rules you confirm]. Please tell us who handles any request to publish or share afterwards, what group size and timings you can accommodate, and whether anything else is restricted.

Check the agenda against the "coming to understand" sentence so it doesn't become a product demo.

## 5. Transport, boxed lunches, code of conduct

**Transport and lunches** go to `event-hospitality` and `event-vendor-sourcing`. I'm not designing them. Hand over these inputs:
- Headcount of 35, which cannot be corrected after the bus leaves.
- Foundry's escort-at-all-times condition. Ask the director how it limits timing and group splitting.
- Whether Foundry allows boxed lunches on site, and where eating is permitted.
- Dietary needs, collected before the headcount is fixed.
- Release terms if Foundry withdraws (see §2).

**Code of conduct on the chartered bus: I can't confirm it.** I haven't seen your code. The skill's rule is that a shuttle is neither the venue nor a social event, so coverage must be named in the scope clause. Read your scope clause for these three points:
1. Does it name transport you provide (the chartered bus)?
2. Does it name third-party sites you take attendees to, such as Foundry's premises?
3. Does it say which rules win when the host's own rules (escort, no photography) apply?

If any answer is no, hand the sites and the vehicle to `event-code-of-conduct` for the clause. MLH's scope is an example of explicit wording: "hackathon-supplied transportation".

## 6. Handoffs

- Sites and vehicle: `event-code-of-conduct` (scope clause).
- Per-site requirements sheet: `event-venue-sourcing`.
- Transport, catering, headcount: `event-hospitality`, `event-vendor-sourcing`.
- Anything recorded: `event-production` (master file, then `event-content-repurposing` with its rights gate).
- Goals and measurement: `corporate-event-strategy`.

## 7. What would flip each choice

| Choice | Flips if |
|---|---|
| Host-led becomes negotiated agenda | The attendees' question is specific (Q3) and the director can commit colleagues' time (Q4). |
| Ground rules become an undertaking | Foundry asks for signatures (Q1) and the attendee list is bounded and known (Q6). |
| Ground rules gain a clearance queue | You name someone who will still be running it when requests arrive (Q7). |
| No standby host becomes a second expedition | You have a standing relationship with another operator and real runway (Q8, Q9). |

## Questions I need you to answer

1. Q2/Q3: What do the 35 want that a talk can't give them, and is their question specific?
2. Q4: Can the director commit colleagues' time?
3. Q5: What other restrictions did Foundry state or imply?
4. Q6: Is the list of 35 fixed and known before the day?
5. Q7: Who by name handles publish requests, and for how long after the event?
6. Q8: How many people own this, and how much runway do you have?
7. Q9: Do you have any other standing relationship with a datacenter operator?
8. Can you paste your code of conduct's scope section?