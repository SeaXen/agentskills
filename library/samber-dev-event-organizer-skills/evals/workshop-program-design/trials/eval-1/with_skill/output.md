# Delivery plan: NordShift Rust session (3 h, 36 registered)

## Answer

**Put the two sponsor engineers in the room as roaming troubleshooters, with the instructor. Put neither steward in the room. Keep the stewards on registration.**

The figure of two is my judgment from the exercise's shape. No ratio or published standard produces it. The skill refuses to give one, and I'm not inventing "1 per 18". The sizing logic is below.

⚠️ **One gate can overturn the whole plan: the venue's written network answer (open question 1).**

## 1. Hands-on commitment: full hands-on, conditional

- The skill's test is whether the content can be learned by reading. Refactoring Rust against a compiler is practice, not reading. Full hands-on stays, subject to the gate below.
- ⚠️ The exercise needs a live network. `git clone` and `cargo build` pull from a git host and crates.io.
- If the venue has not answered in writing about this room's bandwidth, device count and blocked protocols, the skill says to **strike** full hands-on. You would then run a demonstration and publish the repo.
- If the venue has answered, the plan stands. If not, get the answer or cut the rung. Don't carry on hoping.
- Network posture for either case:
  - Ask for pre-downloads. Publish one command that fetches the toolchain and the repo's dependencies before people travel (for example `cargo fetch` in the cloned repo).
  - Name a participant-side fallback, such as phone data.
  - Ask the venue about 36 simultaneous clones and builds, and about blocked ports.
- "Assume the network holds" is struck. A room of 36 building at once is a load case.

## 2. Facilitator coverage: how I got to 2

**Rungs struck or not promoted**
- **Solo instructor is struck.** The session is full hands-on, and someone will be stuck while the instructor is mid-sentence.
- **Stationed helpers are not promoted.** That rung needs distinct stations or physical steps. Yours is one linear path at every seat, so a helper posted at one point covers nothing extra.
- **The default is a roaming troubleshooter,** a recruited person who knows the material.

**Who counts as coverage**
- The skill separates people competent in the material from people competent only in logistics. Your stewards are the second kind. Their value is real but is not debugging.
- The two sponsor engineers are the only people who can diagnose a failed toolchain install, a linker error or a lockfile mismatch.
- So the coverage count is 2, not 4. Headcount is not coverage.

**Why two roamers rather than one**
- The path is linear and ordered. Refactor 2 depends on refactor 1, so a participant stuck at the build step is stuck for everything after it. One unresolved failure costs a person the whole three hours.
- The failures are correlated. All 36 hit clone and build at the same minute, on the same network. A single roamer faces a queue exactly when the queue is longest.
- After setup, most of the room is working at its own pace, and two roamers can work the room.
- This is my sizing, not an external standard. If you can only free one engineer, one roamer is the skill's default. Then the first 30 minutes become the risk to plan around, with pre-downloads and peer pairing.

**Conditions that make the 2 real**
- **Both engineers do the exercise end to end before the day,** on a clean machine. Rust in anger does not mean they know this repo.
- **Brief them on what a helper may do to a participant's machine.** Without a rule, the default is that a helper takes the keyboard.
- **Both stay for the full three hours.**
- **Agree the sponsor conduct line with them:** no pitching during the session.
- **Optional lever: structured peer pairing.** Assign driver and navigator roles, swapped every 5-10 minutes. It scales with the room and halves the number of simultaneous builds. It changes "one path at every seat", so decide it deliberately. Roamers should check in with pairs that go quiet.

## 3. Capacity: 36, no ceiling computed yet

| Ceiling | Status |
|---|---|
| Room | Unknown. I need seats and power at the seats. 36 is at the top of the usual 20-40 breakout band. |
| Coverage | Mine, not external: the instructor plus 2 competent roamers can reach 36. With 1 roamer I'd flag it as at risk. |
| Exercise throughput | Likely not binding, since each person uses their own laptop with no shared kit. Check licence seats or logins if any exist. |

Take the lowest of the three and say which one bound. I can't name it until I have room data.

Registered is not attending. I have no show rate for you, so don't plan on one.

## 4. Prerequisites (draft, three classes)

- **Prior knowledge (hard):** comfortable on the command line and with basic Rust syntax. The refactors assume they can read the borrow checker's messages. Confirm the level with the instructor.
- **Machine state (hard):**
  - A laptop they are permitted to install software on.
  - `rustup` with the pinned toolchain version, named explicitly.
  - Free disk. Rust builds are large, so give a figure after a dry run.
- **Accounts:** none, if the repo is public. If it lives on a private host, that account is your riskiest minute-zero item.
- **Before you travel:** the one pre-download command, with the reason stated (36 people on one network).
- **After:** publish the repo and how long it stays up, plus a follow-up channel and its window.

## 5. How to justify the number to the volunteer lead

Open with their goal, not a ruling.

1. **Registration needs logistics skill. This room needs Rust skill.** The stewards can't debug a failed build. The engineers can. Moving the engineers to registration puts the scarce skill where it isn't needed and leaves the room with none.
2. **The path is linear.** A participant who gets stuck on the build can't skip ahead, because each refactor depends on the previous one. One unresolved failure costs a person the whole session.
3. **Everyone fails at the same minute.** Setup is a simultaneous load on a shared network. The first 30 minutes need the coverage, and registration is quiet by then.
4. **Without them the instructor is the only help.** That is the solo rung, which the skill deletes for hands-on sessions.
5. **What you give them in return:**
   - Both stewards stay on registration, where their skills fit.
   - If registration is quiet once the session starts, they can cover the door, power strips and water. That is logistics, not coverage, and it doesn't count toward the 2.
6. **State the basis honestly.** "Two is our judgment from the exercise's shape. It isn't a standard ratio. We'll revise it from what happens on the day."

Avoid the opposite error. "It's 36 people, so four helpers, one per ten" is invented. The ten is made up, and the four is derived from it.

## 6. What I need from you

1. **Network (blocking):** has the venue answered in writing about sustained bandwidth, device count and blocked protocols for this room? If not, that is the gate in section 1.
2. How many seats does the room have, and is there power at the seats?
3. Can both engineers do a dry run beforehand and stay all three hours?
4. Is the repo public, and can dependencies be fetched ahead of time?
5. Did a previous edition's network fail, and if so, what exactly broke?

## 7. Triggers to revise next edition

- **Ready at minute zero:** the share who finished prerequisites before arriving. Ask at the door. A low share means moving up the prerequisite menu.
- **Started versus finished:** a wide gap in a full room points at coverage. A wide gap in a small room points at prerequisites.
- **Help latency:** how long a raised hand waits. Set your own target before the day.
- **Confidence before and after:** a short self-rated survey at each end.

If your harness keeps memory, record which ceiling bound, the sheet as shipped, what broke, and the venue's written network answer.