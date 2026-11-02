# Nordhack: what to change in your tooling

**Short answer:** the tooling problem is custody and single points of failure, not which tools you use. Two things are bus-factor 1 today: the identity assets on your personal Google account, and one shared mailbox that carries everything. Fix those first. This follows the `event-team-structure` skill, which says the interview should run one question at a time. I couldn't ask, so the assumptions are flagged below. Each choice is labeled **[published]**, **[borrowed]** or **[self-set]**.

## 1. Diagnosis

| Asset | Today | Risk |
|---|---|---|
| Conference domain | Your personal Google account | If you leave, lose the account, or are locked out, the conference loses its identity. The skill names this exact failure mode. |
| Both social accounts | Your personal Google account | Same risk. Social accounts are often recovered through the email they were created with. |
| hello@nordhack.org | One password shared by 6 people | Three streams share one inbox: sponsor threads, mentor signups and RSVPs. A shared password also means no audit trail, no per-person revocation, and no clean offboarding. |

The gap between the org chart and reality is that you are the single admin of the event's identity, even though the team is six.

## 2. Changes, in priority order

### This week (low effort, high value)

1. **Move the domain, both socials and any registrar, DNS or ticketing logins off your personal Google account.**
   - Create an org-owned identity, such as a Google Workspace for Nonprofits account or equivalent, owned by the organization.
   - Make **at least two admins**, you plus one backup. **[published]**: the skill's "written charter + shared admin access" rung.
   - Do the domain first. It controls email, the website and account recovery for everything else.
   - Order of operations: add the backup admin as co-owner, then transfer, then remove your personal ownership. Don't transfer blind.
2. **Inventory every credential-bearing account.** This means registrar, DNS, ticketing, payment processor, bank access, sponsor CRM and the social accounts. Record the owner and backup admin for each in one list. The skill treats domain, socials, ticketing and bank access held by one person as a bus factor 1 on the event's whole identity.
3. **Adopt a two-deep rule for every named role.** Every role gets a named backup who could run it next edition. **[published]**: FOSDEM enforces two managers per devroom, and this costs near zero effort.

### Next 1-2 months

4. **Split hello@ into two tiers instead of one inbox for everything.** **[published]**: the skill's multi-event rule, which applies directly because you run three events.
   - **Standing team address.** Use it for Nordhack's own affairs and shared tools: banking, registrar, vendor accounts, legal.
   - **One address per event** for that event's outreach: conference (sponsors), hackathon (mentors, participants) and meetup (RSVPs).
   - **Per-organizer aliases** on each event address, so replies show who answered.
   - A shared address that also carries every event's mail is the same bus-factor-1 exposure, just moved into the inbox.
   - Drop the shared password. Use delegated or group-inbox access, so you can revoke one person without rotating a secret for six.
   - **Sponsor threads are the highest-value mail.** Give them their own owner and keep them off the RSVP stream. The skill says sponsor relationships are the institutional knowledge that degrades worst when left informal.
   - Keep the old hello@ address as a forwarder or public contact. Don't break links people already have.
5. **Write a one-page team charter.** **[published]**: role scopes, join-paths and decision rights, in the style of an OSS `GOVERNANCE.md`.
   - For each role, write what it will *not* absorb. Over-acceptance is a burnout pattern.
   - Make it visible to the team. An opaque leadership reads as a clique to the technical audience that legitimizes you.
6. **Add a conflict-of-interest register.** **[published]**: disclose employer, own company or freelance services, and sponsor ties.
   - Organizers abstain on their own talk, their employer's sponsorship, and vendors they have a stake in.
   - Put "business is a consequence, not the goal" in the founding text.
   - This matters because you handle sponsor mail. You need to know who has ties to whom.

### Check, and re-run each edition

7. **Entity posture: confirm what actually holds the money and signs contracts.** You say Nordhack is a non-profit, but I don't know whether that means a registered entity or an informal group.
   - Registered entity: check that the bank account, contracts and domain are in the entity's name, not yours or another individual's. This is the same issue as the Google account, just in a different asset class.
   - No entity yet: at a 900-person annual conference, "no entity" is personal exposure. Contracts and liability sit on whoever signed. The skill's default for a conference is an umbrella or fiscal sponsor, or your own non-profit if you mean to outlive the founders. **[published]**: DjangoCon US, whose standing entity let it outlast rotating chairs, versus DjangoCon Europe, which rotates host teams each edition.
8. **Decision-rights shape. The default at your scale is a board-plus-organizers split.** **[published]**: five independent organizations converged on it.
   - **Standing layer** (money, contracts, legal, Code of Conduct (CoC) escalation): a small group that persists across editions.
   - **Operational layer** (program, logistics): owned by the leads of each event.
   - Six people running three events is the "whoever picks it up" pattern. Name leads per event, and keep one coordinating layer to roughly 5-8 leads. **[borrowed]**
9. **Burnout guardrails. Ask each of the six, individually, "is organizing still pleasant?"** A "no" triggers a structural response this edition, such as shrinking scope, adding a backup or rotating someone out. **[published]**
   - Set a workload budget per organizer, reviewed yearly. The meetup-scale reference is 4-8 hours a month. **[published]**
   - Name each organizer's return (leads, network, learning, fun), because a return that disappears is an early departure signal.
10. **Paid-hire gate. The verdict is no hire yet, but re-run it every edition.**
    - At 900 people you are below the published threshold (roughly low-thousands of attendees and/or a six-figure budget, with organizing a year-round burden). **[published]**
    - If you later hire, the documented first hire is an event coordinator or manager, never a community manager. **[published]**
    - If execution capacity is the pain rather than continuity, vendors are the middle path.
    - If there's no budget, restructuring is the whole menu.

## 3. What I would not do

- **Don't buy new tools as the fix.** Swapping platforms while one person owns the domain changes nothing.
- **Don't rotate the whole team each edition.** Rotation only works over a standing continuity layer. Without one you get DjangoCon Europe's recurring host-recruitment failures.
- **Don't treat the shared password as a team feature.** It is a single point of failure that everyone holds.

## 4. Assumptions to confirm

I couldn't run the interview, so these are open and may change the ranking:

- **Entity status:** is Nordhack a registered entity, and who holds the bank account and signs venue and sponsor contracts? This sets point 7.
- **Deadline:** is there a venue signing or a departure coming up? If so, the fast items (1-3, 5) move ahead of any incorporation work.
- **Your own backup:** who is the second admin? If it's currently nobody, naming one is the first action.
- **Budget and appetite:** how much time and money do you have for Workspace licensing, vendors or paperwork?
- **Commercial interests:** does anyone on the six have freelance or employer ties to sponsors?
- **Pleasantness:** is each of the six still enjoying organizing?

## 5. Suggested measures of success

These are self-set targets, to audit each edition:

- Every credential-bearing account has two admins, and none sits on a personal account.
- Each event has its own address with per-organizer aliases.
- The charter exists and is shared with the team.
- Every role has a backup.
- The conflict-of-interest register is current for all six.
- The pleasantness check ran, and every "no" got a structural response with an owner.
- The hire gate was re-run and its verdict recorded.

A design without the bus-factor map and the guardrails isn't done. Items 1-3 and 9 are the minimum.