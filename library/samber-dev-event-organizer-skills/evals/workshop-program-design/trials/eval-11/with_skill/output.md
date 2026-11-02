# Delivery sheet: tracing tooling hands-on at Corvid Conf

**Diagnosis:** the problem is the cost of asking, not the content. Three people didn't want to ask the principal engineer anything in front of the room. This year's room is mostly first-time conference-goers who are juniors, so the barrier will be higher.

Fix it in the structure of the session. Don't rely on asking him to be nicer.

## 1. Hands-on commitment: full hands-on

- Tracing tooling is a skill reading can't give. Q2 in the skill's interview is "can this be acquired by reading?", and I assume the answer is no.
- Strike **solo instructor** from the options. In a room of people doing the exercise, someone is always stuck while he is mid-sentence.
- ⚠️ **Open check:** does the exercise need a live trace backend or internal service? If yes, and the venue hasn't answered the network question in writing, the skill says to strike full hands-on and run a demo plus published material instead. See section 5.

## 2. Facilitator coverage (this is where most of the fix lives)

My sizing comes from the exercise's shape and not from a published ratio. I'm assuming one linear path at every seat.

1. **Peer pairing, structured.** Twelve people become six pairs.
   - Assign a driver and a navigator, and swap every 5–10 minutes.
   - The first question goes to your pair, so asking a person next to you is the default and asking the room is the exception.
   - Check in on pairs on a cadence. Two stuck people is a stable state that gives no signal.
2. **A roaming troubleshooter who is not the principal engineer.**
   - Pick someone who can debug the setup and is approachable. A logistics volunteer is not enough.
   - Their trigger is to spot people who are falling behind, not to wait for hands.
   - This person is the primary "ask me" target. The principal engineer presents.
3. **Helper rule, decided in advance:** helpers never take the participant's keyboard. Brief them on it.

I'm assuming you have one such person available. If you don't, that is your real constraint, and I'd rather you fix it than pad with logistics volunteers.

## 3. In the room

- **Open with an icebreaker.** A 12-person room is small enough for it. Use name, role, and "something you recently learned."
- **The instructor says this sentence at minute one:** "If you hit an issue, others probably have too." It costs nothing and it is the cheapest mechanic in the skill's evidence.
- **Brief the instructor on the specific risk:** the skill cites guidance to be "extremely aware of how intimidating questions will be for participants." Concretely:
  - Answer "basic" questions without signalling that they're basic.
  - Don't answer a question for the pair before the pair has tried.
  - Name a short pause for questions in the plan, not only at the end.
- **Build recovery time into the schedule.** Breakouts, troubleshooting, and questions get slots next to the content.
- **For any discussion, use small groups, not the whole room.** Splitting into 2 groups of 6 with a convener each is well under the roughly-10 cap. Quiet people who spoke in a small group asked for help more often afterwards. This directly lowers the barrier you're seeing.
- **My own addition, not from the skill's evidence:** give people a low-exposure way to ask, such as a shared channel or a card on the table. Treat it as an extra and not a replacement for the pairing.
- **Close deliberately.** The instructor stays available afterwards. Open a follow-up channel and publish how long it stays open (for example, through the end of the month).

## 4. Capacity: 12, which ceiling bound is not yet known

- **Room ceiling:** unknown. Check seats and power at the seats.
- **Coverage ceiling:** my judgment is that 12 works with pairs plus one roamer plus the instructor.
- **Throughput ceiling:** unknown. Check per-participant logins, licence seats, or any shared backend.

The binding ceiling is whichever of those turns out lowest. The skill asks you to name which one it was and record it.

**Length:** two hours is fixed. Published hands-on sessions run 150–180 minutes, so your session is short for the format. Don't spend the 120 minutes on installs. Make everything installable before arrival, which is section 5.

## 5. Prerequisites and network (sheet to publish)

First-timers on unfamiliar laptops are the risk. Split the page into three classes, with hard requirements marked:

- **Prior knowledge (hard):** state what they must already understand, as capability and not job title.
- **Machine state (hard):** OS, install permission, disk, versions.
- **Accounts (hard, do first):** list every account and keep the list as short as possible. This is the class that fails worst at minute zero, and juniors are the most likely to miss it.
- **Pre-download command:** give one command that pulls everything before they travel. Without it, 12 people install at once on conference WiFi.
- **Known weirdness:** publish the VPN, ad-blocker and port issues. Corporate laptops are a common culprit.
- **Nothing published is struck from the menu.** If anything must be installed or signed into, an empty prerequisites section is a false promise.

**Network posture:** declare the dependency and name a fallback. If the venue hasn't answered in writing (bandwidth, device count, blocked protocols), either get it answered or remove the live dependency. Asking the venue three questions in writing is cheap.

**Provisioned environment:** if many attendees may lack install rights on their laptops, offer a browser-based option as a second path. It costs you two environments to support, and a compliance review if you issue credentials. Decide from the answer to "can every participant bring a capable, installable machine?"

## 6. Materials

Publish the repo and slides, and state how long they stay up. Post-session material helps the shyest people, who can work it out later without asking in front of anyone.

## 7. Measures and revision triggers

Pick these three and write the trigger down beforehand:

1. **Ready at minute zero:** the share of the room that finished the prerequisites. Ask at the door. If it's low, move up the prerequisite menu.
2. **Help latency:** how long a raised hand waits. Split it by who answered, the roamer or the instructor, and see who people actually ask.
3. **Confidence before and after** on the specific skill taught. This is the Carpentries-style convention. Borrow the method, not their figures.

Also ask the same three people from last year, or an equivalent sample, whether asking felt easier. Treat that as your own informal check, because it isn't a published metric.

## Questions that would change this

1. Does the exercise need a live service, and has the venue answered in writing? (This decides whether hands-on stays.)
2. Is there a second competent person for the roaming role?
3. Can all attendees bring a capable laptop they're allowed to install on?
4. Is the instructor open to being briefed on the points in section 3?