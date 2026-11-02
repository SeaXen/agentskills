# Decisions: sponsor main-stage speaker, and cost governance session

I read `event-speaker-sourcing` and both of its references. I couldn't run the interview, so I assumed the following:

- Halcyon Cloud owns the event, so this is the vendor/user conference pole.
- Roughly all 20 sessions are invited, so this skill is the main intake.
- Travel and lodging budget is unconfirmed.
- I don't know the event date or whether the sponsor package is already signed.

## Answers

1. **Main-stage slot: don't accept the sponsor's speaker as a package deliverable.** ❌ The sponsor's speaker can still enter the program, but through the same qualification as everyone else, and not for this slot.
2. **Cost governance session: go with the customer's staff engineer, on conditions.** 🎯 She is the default pick. The FinOps vendor's architect is a good second voice, and he can't be the only voice.

## Decision 1: sponsor-offered main-stage speaker

**Why not as offered**

- On a vendor/user conference the skill doesn't ban sponsor speakers outright. It does require that a sponsor-routed name be qualified on the same evidence as any other, or stay off the shortlist.
- A slot given as part of a package means the sponsor chose the speaker before any slot brief existed. The skill's failure mode is "sourcing names with no slot brief", and this is that case.
- The main stage is the highest-risk slot you have. The skill promotes prior-talk review and an organizer reference for keynote and headline slots.
- A monitoring vendor on your main stage is a vendor pitch by default. The skill says a vendor pitch is never the default fill. It fills a slot only when no practitioner is available, or as a second voice.
- The effort you'd save is the qualification work, which is the part the skill says not to skip.

**What to do**

1. Write the main-stage slot brief first: theme, audience level, what attendees walk away knowing, and a disqualifier line. A sample disqualifier: "currently selling a monitoring product to this audience as the core of the talk."
2. Tell the sponsor the slot is filled by invitation against a brief. Offer them one of these instead:
   - a workshop or niche session
   - a second-voice seat on a panel
   - a co-presented talk with a joint customer, which is the strongest format for a vendor
3. If they insist on the 40-minute slot, accept their speaker only if they pass the same gates as everyone else: a fit screen against your brief, then ten minutes of recorded delivery evidence or a transcript. If a customer practitioner could fill the slot, the practitioner comes first.
4. Treat this as a reversibility call. Whether you've already promised the slot in writing decides how hard this conversation is. I can't verify that from here, so check the package terms before you reply.

**What would change my answer:** a named sponsor speaker who has a strong recorded talk, fits your brief, and isn't pitching. That person scores Hot like anyone else, and you take the slot on the evidence.

## Decision 2: cost governance session

| | FinOps vendor architect | Customer staff engineer |
|---|---|---|
| Fit to the topic | Product pitch for the topic | Ran the whole migration |
| Delivery evidence | Polished, presumably observed | None yet, never spoken |
| Skill default | Fills the slot only if no practitioner is available, or as second voice | Screen first |
| Main risk | Slot becomes a vendor pitch | Talk is unwritten, or stage delivery is rough |

**Recommendation**

- Make the staff engineer the lead voice. The skill says to screen the practitioner who lived the topic before a vendor pitching a product for it. On your own user conference, a customer story is also what the audience came for.
- Keep the architect as a second voice. A short co-seat or a panel role completes the discussion without owning it, and it is a good spot for the FinOps tooling angle.
- Don't drop the architect entirely. File him as a vendor candidate worth tracking, for a workshop or niche session.

**Condition: get evidence before she goes on the shortlist.** The skill says a name goes to outreach with evidence or it doesn't go. Until you have some, score her **Warm**. Any one of these gets her to Hot:

- an internal talk recording, or a written migration postmortem long enough to show she can structure an argument
- a 15–20 minute call where she walks through the migration (an informal delivery check)
- a reference from someone who watched her present internally

**Conditions on the invitation**

- Make the first ask light. Quiet practitioners often say yes to a shorter format, a co-speaker seat, or a call to shape the topic. That fits her well.
- Check availability early. Her employer may need to approve a talk that discusses their cloud costs, and that approval could block her.
- Budget stays "unconfirmed" until you confirm it. If it is, say in the invitation that she may be funding her own trip.
- Rehearsal and briefing come after she confirms. That belongs to `event-speaker-experience`, and it's the answer to "never spoken before."

## Shortlist entries to carry forward

```
Slot 1: Main stage, 40 min
  Brief: to write before sourcing (see Decision 1, step 1)
  Sponsor's speaker: Cold until fit + delivery evidence exist; Skip if a
    disqualifier hits. Channel: sponsor relationship, so name it as such.
  Next step: source 3+ practitioner candidates via prior-talk review and
    referral asks, plus the organizer reference (keynote-grade slot).

Slot 2: Cost governance session
  1. Customer staff engineer: Warm today, Hot once evidence is in hand.
     Why: ran the full migration, so the session comes from lived detail.
     Evidence: pending, none dated yet.
  2. FinOps architect: second voice, Warm. Why: polished delivery, tooling angle.
  Budget offer: unconfirmed (state it, never "probably")
  Invited-review lane: decide it now. My suggestion is "confirmed at
    invitation" for the customer, since her story is the reason for the invite.
```

Two numbers I did not invent: speaker fees and an invite-to-confirmation rate. Both are unknown for you, so record your own ratio this edition.

## Two questions I'd ask you next

1. What is the event date, and is the sponsor package already signed with this slot in it?
2. Does your budget confirm travel or lodging for a customer speaker?

Present the slot-by-slot shortlist to yourself for validation before any invitation goes out. An invitation is hard to walk back.