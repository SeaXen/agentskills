# KernelDays: between-editions plan (draft for your approval)

I read the skill and its four references. It names your exact proposal as a negative example, so the short answer is **don't ship the points system as designed**. Below is what to do instead and how to keep what's worth keeping.

## Verdict

- **Badges, a monthly leaderboard and levels fail on three counts.** They measure posting, not the outcome. They reward the loudest members, not the returning ones. They need upkeep in exactly the months nobody has hours.
- **The outcome is "this person comes back next edition, and some bring work with them."** KernelDays is annual, so you get one live touch a year. A monthly game loop runs on a contact rhythm you don't have.
- **The photo feature is the highest-risk part.** A public status marker is a publication about a named person. Ask before naming anyone, and offer an opt-out. Putting top-three photos on the homepage also makes the leaderboard a ranking of people on your public face.
- **The ladder to organizing is a good idea, but it needs a different shape.** Keep it. Rebuild it as a participation ladder that works asynchronously (section 3).

## Assumptions to confirm

The skill asks 7 to 9 questions one at a time before picking a menu rung. I could not ask them, so I assumed defaults. Tell me which are wrong, because each changes a rung.

| # | Question | Assumed | Moves |
|---|---|---|---|
| Q1 | How many editions so far? | Annual, 2+ editions | Menu 1 |
| Q2 | Does a forum already exist, and did a decision confirm it belongs in the property set? | Yes | If no, route to `event-portfolio-strategy` first |
| Q3 | Who owns it, and whose account is the platform registered to? | Unknown | Menu 3 |
| Q4 | Does a register exist (`event-cultural-identity`)? | Likely hacker | If none, route there first and label this provisional |
| Q5 | One city or traveling? | Helsinki plus travelers | Local-cohort section |
| Q6 | What carries the audience now (mailing list, talk archive)? | Unknown | Menu 2 |
| Q7 | Is there a hard live-by date? | Unknown | Menu 3 |
| Q8 | Who has recurring hours in the quiet months, and is anyone funded to moderate? | Volunteers only, no funded moderator | Menu 1 and 2 |
| Q9 | Is a next edition intended, and will the team turn over before it? | Yes, and probably | Menu 3 |
| Q10 | What assets exist (chat space, consented member list, archive)? | Forum, archive | Re-ranks all menus |
| Q11 | Is there a legal entity that must show who holds which access? | Unknown | Menu 3 |

The plan assumes the **volunteer-team pole**. Your quiet-month people are the ones who just finished an edition and are recovering.

## 1. Cadence posture

- **Pick: occasional pulse**, with a named owner. The default would be dormant-but-open, but you clearly want the forum alive, and a pulse is the most you can sustain.
- **Condition:** it only holds if someone has recurring gap-month hours (Q8). Without a name, the posture is dormant by decision, not by drift.
- **Pulse plan** (every slot filled from material that already exists):
  1. Post-edition: archive up, talks linked, thank-you.
  2. Mid-gap: digest of what members shipped.
  3. Mid-gap: one-member spotlight.
  4. Build-up opens: hand back to the next edition's channels.
- **Rejected rungs:**
  - Continuous heavy: it needs a funded moderator roster.
  - Continuous light: it needs someone with something to say every cycle.
  - Delete-and-reopen each edition: it discards the member list and archive.
- **Dormancy notice** (the fallback, pinned if the owner lapses): needs a date, a named owner, a working conduct route, and a promise small enough to keep.

## 2. Register delta

I could not check this against a fixed register (Q4). Write the between-editions expression as a delta against it, never a new voice. For a systems-programming crowd that likely means terse, technical and low on hype, with no gamified cheerleading. That is a guess until `event-cultural-identity` confirms it. Label it provisional.

## 3. Conversion mechanism (replaces the points system)

Scoped to non-volunteer members.

1. **Default: single re-engagement touchpoint.**
   - One message to last edition's attendees, timed to the next edition's opening.
   - It names something that happened, asks for one thing (answer the call for talks, name a topic), and is signed by a person.
   - Don't send a bare "tickets are live" email. That is the listed negative example.
2. **Step up: structured participation ladder.** Use it once Q9 says compounding and Q6 says something already carries the audience.

| Rung | Way in (asynchronous) | Reward |
|---|---|---|
| Attendee | Came to an edition | Archive, space, announcements |
| Regular | Posts and answers in the gap | Recognized by name, asked first |
| Contributor | Reviews CFP proposals, hosts a thread, writes for the digest | Stated role, a reference |
| Candidate | none | **Flagged to `event-team-structure`; this skill stops here** |

- **Every rung needs a way in that doesn't require knowing an organizer.** Otherwise it is a clique with a diagram.
- **This ladder is your "feed people toward organizing" path.** Reviewing CFP proposals is the natural contributor step for a systems conference. A past-contributor anniversary slot is the top rung.
- **Volunteer-shaped work stays out.** Past-volunteer alumni belong to `event-volunteer-experience`. Don't build a second nomination path.
- **"Community Champion" as an unpaid title:** use `developer-champions` for intake and perks. Don't re-derive it here.

## 4. Local posture

Helsinki plus travelers means no fed local cohort. If someone asks to run "KernelDays Tampere", apply the test: **does anyone outside the organizing team run an event under your name?** If yes, that is brand governance, which this collection has no playbook for. Say so and stop.

## 5. The prototype bot and the homepage photos

**The bot**
- Keep it only if it feeds the pulse. For example, it could surface unanswered questions or draft the digest.
- Drop points, levels and the leaderboard.
- Its activity tracking is processing of member data. It falls under the member-list owner and retention decision (section 6).

**The top-three photos**
- Drop the ranked top-three. Recognition tied to a rank pushes the loudest members forward.
- If you want a face on the homepage, use the spotlight. Choose it by contribution, not rank, and ask the person first.
- Offer an opt-out that needs no explanation.
- Photos and names of EU residents are personal data. Route the legal basis and retention to your counsel. I name no jurisdiction or period here.

## 6. Member list and handoff

- **Member list:**
  - Owner: a named living person.
  - Basis: what members were told when they joined.
  - Scope: announcing your own next edition, nothing broader.
  - Review or deletion date: a real date.
- **Handoff, written now:**
  1. Fill the asset inventory together: workspace, admins, billing, domain, invite links, list export, archive, conduct route.
  2. Move ownership of record first.
  3. Add a second admin who is neither of you.
  4. Restate the retention decision.
  5. Confirm the conduct route reaches someone reading it.
  6. Announce the change in the space.
  7. Date the document and set a review.
- **The bot's author is probably holding a credential.** Check whether the bot or the platform sits on their personal account. That is the classic orphaning failure.
- **Conduct:** the space binds the same code of conduct as the room. Name the owner and route reporting there.

## 7. Measurement (all thresholds self-set)

- **Carry rate:** the share of one edition's attendees who register for the next. This is the only number that answers the question. Hand it to `event-market-fit`. The ~30% blended trade-show retention figure is context, not a target.
- **Gates, all three must pass:**
  1. **Cadence kept:** posts planned versus made. Two missed cycles is a demotion signal.
  2. **List integrity:** named owner and written retention decision before the gap starts.
  3. **Handoff readiness:** a dated access document naming a living holder per account.
- **Ladder movement:** report the count of members who moved a step, not a rate. The numbers will be small.

## Approval needed (one section at a time)

1. Confirm or correct the Q1 to Q11 assumptions, especially Q3, Q4 and Q8.
2. Approve section 1 (cadence posture and owner name).
3. Approve section 3 (touchpoint now, ladder later).
4. Approve section 5 (drop the leaderboard and top-three photos, keep the bot as a pulse helper).
5. Approve sections 6 and 7.

Nothing member-visible changes until each is approved.

**Routing notes:** the platform decision goes to `event-portfolio-strategy`, the register to `event-cultural-identity`, the carry rate to `event-market-fit`, and candidates to `event-team-structure`.