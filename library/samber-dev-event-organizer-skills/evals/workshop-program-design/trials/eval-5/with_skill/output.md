# Verdict: yes in principle, not yet

✅ The rung is right. Locked laptops with no installs match the promotion condition for a provisioned environment only. Nothing else gets your 20 students hands-on.

⚠️ "Solves everything" is wrong. It removes the install barrier and puts three new risks in its place. Say yes only when the gates in section 1 are closed.

## 1. Before you say yes (gates, in order)

1. **Test on a real school laptop, in the real room, on the venue network.** Do this for both schools. This is the cheapest check that could kill the plan. Any of these breaks a browser IDE without touching bandwidth:
   - a school content filter or proxy blocking the sponsor's domain
   - blocked WebSockets (browser IDEs lean on them)
   - TLS inspection or a school-managed VPN
   - browser policies that disable features the IDE needs
   - a browser version too old
2. **Get the venue's network answer in writing.** I don't know whether you have it yet. Ask for sustained bandwidth, how many devices the room's access point holds and what happens at the limit, which protocols and ports are blocked, and whether the block can be lifted for a day.
   - Per the skill's rule, if the exercise needs a live service (it does) and the venue hasn't answered in writing, **full hands-on gets struck**. The fallback is a demonstration plus published material.
   - Treat "it's fine" as no answer.
3. **Run a 20-concurrent dry run with the sponsor.** All 20 log in and start a workspace at once. A room of simultaneous logins is a load case, not an assumption.
4. **Close the compliance items in section 3.** Minors are present, so this is the heaviest gate.

## 2. What the offer changes, and what it doesn't

- **Your dependency moves, it doesn't shrink.** Local installs can no longer fail. In exchange, the whole session depends on the room's network and on the sponsor's platform staying up. It is safer only against the failures you named.
- **Single point of failure you don't control.** Ask the sponsor for:
  - an on-call engineer during the session
  - the quotas per workspace and the concurrency cap
  - a written outage plan
- **Your fallback is a demonstration, not a second path.** "Both paths" is impossible here. Prepare the instructor-driven version, with the repo and slides published, as the plan B you can switch to mid-session. Agree the switch trigger with whoever owns the run-of-show.
- **Participant-side fallback is weak.** The usual "use your own data" fix probably doesn't work. Tethering a school laptop to a phone may be blocked or against school rules, and the students are minors. Ask the schools.
- **No self-signup accounts.** Avoid anything needing a GitHub or Google login or a personal email.
  - School-managed Google or Microsoft accounts often block third-party OAuth.
  - An account a student creates because you told them to persists after the event, and you can't delete it for them.
  - Use pre-created logins (`user1`-style) handed out on the day.
- **Their work must leave the platform.** Locked laptops probably can't reach a Git host. Ask for a zip export or a download link that works from the school laptops, plus the sponsor's retention rule for student files.
- **The sponsor shapes the content.** Check that the exercise teaches the topic and not the vendor's product. Ask what the students can do on their own afterwards, since the environment will be gone.
- **Pin and publish the toolchain versions** in the prerequisites, so students can match them to tutorials later.

## 3. Compliance (the part most likely to bite)

You are accepting a vendor's terms on behalf of minors and issuing credentials to them. Send these for review. I'm not giving legal answers.

1. **Platform terms.**
   - Do they allow third-party or classroom use?
   - What is the minimum age? Some platforms set 18 or 13.
   - Who is the contracting party, you or the schools?
2. **Consent for under-18s.** That acceptance is made for someone who cannot make it themselves. The age of digital consent and the need for parental or school sign-off depend on jurisdiction. I don't know where Tallow Conf is held. Route this to the schools and to whoever handles your data protection.
3. **The schools' own approval.** Their IT won't budge on the laptops. Their data-protection or safeguarding lead may also have to approve any third-party service pupils log into. Ask early, because it can take weeks.
4. **Participant data.** Apply the same posture as `event-accessibility-inclusion`:
   - Who holds the credentials, and for how long?
   - Send the sponsor pseudonymous logins, not names or school emails.
   - Put in writing: no marketing contact, no lead capture, no analytics on the students, and no sponsor outreach to them afterwards.
5. **Teardown is the sponsor's schedule, not yours.** The skill's reversibility argument (an environment you built is torn down on your schedule) holds only if the sponsor commits to a deletion date in writing. That reasoning is mine, not a published one. Publish that date to students and teachers.
6. **Adults and minors.** Decide who from the sponsor is in the room, and that no sponsor staff are alone with students. Helpers must not take a student's keyboard, so brief them on that rule.

## 4. Delivery sheet (draft, for your validation)

| Item | Draft |
|---|---|
| **Hands-on commitment** | Full hands-on, provisional. It is struck to demonstration plus published material if gate 1.2 stays unanswered or gate 1.1 fails. |
| **Capacity** | 20 students, fixed by the partnership. I can't say which of the three ceilings binds yet. I need the room size, the coverage figure and the sponsor's login and concurrency cap. If other attendees share the platform, the sponsor's cap may bind first. |
| **Facilitator coverage** | One instructor plus one roaming troubleshooter who knows the material, with a sponsor engineer for platform faults. **This sizing is my judgment, not a standard.** Teachers from the schools are logistics help, not material help. If the exercise has distinct steps, we revisit and post a helper per step. |
| **Prerequisites: knowledge** | Capability statements, for example "comfortable at a command line". Do not assume anything about teenagers' background, so ask the teachers what the students have done. |
| **Prerequisites: machine** | A school laptop with a current browser. Name the browser and the minimum version, and say "no installs needed". |
| **Prerequisites: accounts** | None. Logins are issued on the day. |
| **Network posture** | Declare the dependency, then clear the room in writing. Nothing is installed, so there is nothing to pre-download. The pre-event laptop test replaces it. |
| **Materials and window** | Repository, slides and any recordings stay up indefinitely. The environment is torn down on a date the sponsor commits to, and you announce it. Set up a follow-up channel and publish how long it stays open. |
| **Known failures to publish** | VPN on, an ad-blocker, a blocked domain, a stale browser. Add "if it fails, reload, then raise a hand in the first ten minutes". |

**Session length** is not a figure to copy. Published hands-on sessions run 150-180 minutes in 45-minute blocks. Set yours from the exercise and the school schedule, then pass it to `event-schedule-design`.

**Revision triggers for next edition:**
- Fewer than all 20 logged in at minute zero: move up the prerequisite menu.
- Any outage over 5 minutes (my own threshold): add a second environment path or drop to a demonstration.
- The sponsor can't commit to deletion: don't repeat the arrangement.

**Measures to pick (two or three):**
- Ready at minute zero: the share logged in and running at the start, taken from the dry run and checked again at the door.
- Confidence before and after: a short self-rating survey, borrowed from the Carpentries.
- Started versus finished: how many reached the last exercise.

## 5. What I need from you

These decide how the gates play out:

1. Has the venue answered the network questions in writing?
2. Does the sponsor's login need a personal email or a third-party sign-in, or can they issue plain usernames?
3. Which jurisdiction is Tallow Conf in, and have the two schools approved a third-party tool for pupils?
4. Is the exercise one linear path at every seat, or does it have distinct steps?
5. Who is the second knowledgeable person in the room?
6. What does the sponsor want in return?

Your yes can go to the sponsor now as "yes, subject to the laptop test, written network answer, dry run and signed data terms". That keeps the offer and gives you a clean exit.