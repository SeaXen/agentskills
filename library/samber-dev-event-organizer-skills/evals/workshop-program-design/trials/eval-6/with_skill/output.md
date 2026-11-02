# Delivery sheet: Broadleaf Summit hands-on security session (150 min, RDP jump host + hosted console)

I followed the `workshop-program-design` skill. It normally interviews you one question at a time. Because you asked for the answer now, I filled in what you told me, marked my assumptions, and listed the open questions at the end. I have not seen your live page.

## 1. Verdict

⚠️ **Do not keep promising hands-on on the strength of that one line.**

- **Your session needs a live network service.** Participants must reach the jump host over RDP and the hosted console for all 150 minutes.
- **The venue's answer is not an answer.** "Fast fibre WiFi throughout, no problem" is a bandwidth claim. It says nothing about device count, blocked protocols or blocked device classes. It is also not the written answer the skill requires.
- **The venue has a failure on record.** The same kind of room failed about 20 minutes in, and nobody found the cause.
- **The skill's rule applies.** When the exercise needs a live service and the venue has not answered the network question in writing, **full hands-on is struck** from the menu. It is not demoted.
- **That is reversible.** You have seven weeks, roughly until 5 December. The right move is to get the written answer and a test, then restore hands-on, and to keep a pre-built fallback if you can't.

## 2. Hands-on commitment

- **Today:** hands-on is suspended, not cancelled.
- **Restore it** only if both of these happen:
  1. The venue answers the written questions in section 6.
  2. A test from the real room passes (section 3).
- **If neither happens by the gate date, switch.** My suggested gate is about week 3, around 7 November. That date is my judgment, not a standard. Run a demonstration of the jump host and console from one machine, and publish the lab material. This is the skill's "remove the live dependency" rung.
- **Cost of switching:** it is the only rung that costs content. Weigh that against a room of 150-minute participants who cannot connect.
- **Reason you can't keep hands-on by default:** your prior edition is a trigger on its own. A network failure at a previous edition is a named promotion condition for the demo path.

## 3. What to do about the unexplained failure

I can't tell you what broke two years ago, and the skill doesn't let me guess. The published failure causes are mostly policy, not bandwidth:

- **Blocked protocol.** One published workshop with this same Windows jump-host setup lists "(RDP protocol allowed)" as a prerequisite.
- **Blocked device class.**
- **Access-point device limit.** This is my inference. A room that works at the start and dies about 20 minutes in is consistent with a limit that fills up as devices join. It is still only a hypothesis.
- **Participant VPN or ad-blocker.** One published browser-lab note says "Turn off VPN (we use websockets extensively)" and "pause AdBlock".
- **Peak load that isn't the download.**

Steps:

1. **Ask the venue and anyone who was there.** Ask the venue what their logs show for that room and date. Ask the previous organiser or a speaker from that day. Ask what was running at the 20-minute mark.
2. **Run a rehearsal in the actual room.** Book an on-site test with the venue.
   - Connect as many devices as you can borrow, ideally close to your expected headcount.
   - Hold RDP sessions and the console open for the full 150 minutes, not 10.
   - Test from a laptop with a typical corporate VPN profile.
3. **Record the result.** Whatever happens, you then have evidence instead of a reassurance.

## 4. Capacity, facilitation and environment

**Capacity** is the lowest of three ceilings. I can't state it yet.

- **Room ceiling:** seats and power at the seats. I don't have these.
- **Coverage ceiling:** my sizing, not a standard.
- **Throughput ceiling:** the number of jump-host sessions and console logins. This is the one most often missed. Does the Windows host cap concurrent RDP sessions? Does the console cap seats?

Tell me those and I'll say which one binds.

**Facilitator coverage:**

- **Solo instructor is deleted.** A hands-on room will have someone stuck while you are mid-sentence.
- **Default: one instructor plus one roaming troubleshooter.** This person must be able to debug connection and login problems, not just handle logistics.
- **Sizing basis (mine):** I'm assuming one linear path at every seat. If the exercise has distinct steps people reach in different order, post someone at each step.
- **There is no ratio to apply.**
- **Decide in advance what a helper may do on a participant's machine.** Without a rule, the helper takes the keyboard.

**Environment.** This is a provisioned environment, so the skill's compliance review applies:

- **Terms:** you accept the platform's terms for a room of people. Read the hosted console's third-party and classroom terms before the day.
- **Credentials:** you issue and hold per-participant logins. Decide who holds them and for how long.
- **Teardown:** tear everything down on your schedule inside the window you publish. Participant-created accounts persist, so keep the account list as short as the exercise allows.
- **Minors:** if any participant is a minor, route the acceptance question rather than answering it.

**Second path.** Consider offering a browser-based access route alongside RDP. One published workshop with the same Windows jump-host setup offers both an RDP client and "Chrome Browser to access KASM desktop". A browser path travels over HTTPS and avoids the RDP port. The skill ranks "both paths offered" top for readiness and top for effort, since you maintain two environments. Treat it as optional, and decide after you hear the venue's protocol answer.

## 5. Prerequisites, split by class

Publish all three classes, in this order, and mark which are hard requirements.

**Prior knowledge (hard).** State capabilities, not job titles. Fill these in from your exercise.

**Your machine (hard)**
- A laptop you are permitted to install software on.
- An RDP client, with a named install route for each OS.
- A current Chrome or Edge.

**Accounts (hard, do these first)**
- Any account the hosted console needs, confirmed by email **before travel**. This class fails worst at minute zero, on the room's network, for everyone at once.

**Network conditions (hard)**
- The room's network must allow RDP. Say so, and tell participants what you are doing about it.
- **Turn off corporate VPN and pause ad-blockers** for the session.
- **Fallback:** tether your phone or use your own data. The published wording is "(Use Wi-Fi or your own data)". This fallback survives the venue failing entirely. It is the cheapest remedy on this sheet.

**Before you travel**
- Do the pre-download and sign-in checks at home, on a network you trust. This removes the install burst from the room's network.

**After**
- State how long the material and the environment stay up. Published windows range from 72 hours to a month. Pick one deliberately and name the follow-up channel.

## 6. Network posture and the written questions to send now

The default is to declare the dependency with a fallback, which section 5 does. Because the venue hasn't answered and a prior edition failed, also **clear the network in writing**.

Send this today:

> We run a 150-minute hands-on session in [room] on [date]. Each of [N] participants will keep one remote desktop (RDP, TCP 3389) session and one HTTPS/websocket web console open for the whole session. Please confirm in writing:
> 1. What sustained bandwidth can this room guarantee, on what circuit, with what fallback?
> 2. How many simultaneous devices does this room's access point hold, and what happens at the limit?
> 3. Which protocols and ports are blocked? Can RDP and websockets be opened for the day?
> 4. Are any device classes or client types blocked by default, and who can grant an exception on the day?
> 5. What happened to the network in this room at [previous edition]? Do you have logs?
> 6. Can we book a load test in the room on [date range]?

Treat a non-answer as evidence. Under the skill, a venue that will not answer is the promotion condition for the demo path.

## 7. The live page, this week

The page is public and promises something you can't yet guarantee, so edit it now:

- **Add the network dependency honestly:** internet access with RDP allowed is required. List the three conditions from section 5.
- **Change the guarantee.** Say the final hands-on format is confirmed by your gate date, and that participants will be told by then. Say "venue network being verified", not "guaranteed".
- **Don't over-explain.** Never put internal config or hostnames on a public page, per your own security rule.

## 8. Timeline

| When | Action |
|---|---|
| This week | Send the venue email. Edit the page. Ask the prior-edition contacts what they saw. |
| Week 2 | Venue answers, or you chase and log the silence. Book the load test. |
| Week 3 (about 7 Nov) | **Gate.** Written answers plus a passing test restores hands-on. Otherwise switch to demo plus published material. |
| Weeks 4-6 | Pre-event mail: accounts, pre-download, VPN and ad-blocker warning, fallback instructions. |
| Event | Roaming troubleshooter in the room. Agree the live-failure response with your run-of-show plan. |

The skill leaves the live response to `event-run-of-show` and gives no convention for it. Write it down before the day.

## 9. What would change each choice next edition

- **Hands-on:** if the test passes and the day holds, keep it. If the connection fails in the room, move to demo-only next edition.
- **Capacity:** whichever ceiling bound. Raise it by fixing that one.
- **Coverage:** if help latency is long with a small room, add a second roamer.
- **Prerequisites:** if fewer than most of the room is ready at the door, move up the menu (provisioned path).
- **Network:** keep the venue's written answer on file. If the venue won't answer a second time, change venue.

Measure two or three of these and set the trigger in advance: ready at minute zero (ask at the door), started versus finished, and help latency.

## Questions I need answered

These change the sheet:

1. What is the expected headcount and the room's seat and power layout?
2. What are the console's and the jump host's concurrent-session limits?
3. Does the exercise have distinct steps, or one linear path at every seat?
4. Can your platform's terms be read and accepted on participants' behalf, and will any participant be a minor?
5. Who is available to be the roaming troubleshooter, and can they debug a failed login?
6. Who ran the room two years ago, and do they remember what failed at the 20-minute mark?

Send me those and I'll give you the final capacity, the coverage sizing, and the exact page text.