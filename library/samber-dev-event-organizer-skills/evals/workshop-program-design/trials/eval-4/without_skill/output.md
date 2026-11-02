# Prerequisites: Hands-on LLM session

**Do the setup before you arrive. It takes about 30 minutes.** The session is 150 minutes, and about 90 of them are hands-on. Venue Wi-Fi can't handle a 2 GB download from many people at once, so we won't do setup in the room.

## What you need

- **A laptop** you can install software on. A locked-down work laptop may block the container runtime.
- **A free [VENDOR] account.** Sign up at [URL] and confirm your email. No credit card is needed. [Confirm this is true before publishing.]
- **A GitHub account.** You'll use it to sign in to the console. A personal account works. If your employer's GitHub enforces SSO, use a personal account instead.
- **A container runtime** ([Docker Desktop / Podman / other], version [X] or later). Install it and check that it starts.
- **About 2 GB of free disk space** for the container images, plus a few GB of headroom.
- **Python familiarity.** You should be able to read a short script and run it from a terminal. You won't write anything from scratch.

## Do this by [DAY, DATE, e.g. Wednesday] (before you travel)

1. Create your [VENDOR] account and sign in to the console once.
2. Sign in to the console with GitHub and check that the dashboard loads.
3. Install the container runtime and start it.
4. Pull the images on home or office Wi-Fi:
   ```
   [docker pull ... / ./pull-images.sh]
   ```
5. Run the check command. It should print `[EXPECTED OUTPUT]`:
   ```
   [check command]
   ```

If step 5 prints the expected output, you're ready.

## If something fails

Email [ADDRESS] with the error message and your OS by [DAY, DATE]. We'll answer before the session. At the venue, the first 10 minutes are for last-minute fixes only. If yours isn't solved by then, you can pair with a neighbor and still do the full exercise.

## Plan for the session

| Time | What happens |
|---|---|
| 0:00–0:10 | Setup check (fixes only) |
| 0:10–0:60 | Concepts and walkthrough |
| 0:60–2:30 | Hands-on exercise (about 90 min) |

[Adjust the middle rows to the real agenda.]

---

## Notes for you (not for the page)

- **Placeholders:** the vendor name, URLs, runtime and version, pull command, check command, deadline, and support email all need real values. I didn't invent any of them.
- **Why it went badly last year (my inference):** "We'll get everyone set up in the first 15 minutes" put all setup in the room. This year it would add a vendor signup, a GitHub login, and a 2 GB pull on shared Wi-Fi, so the new text moves everything before the event.
- **The check command matters most.** Without a pass/fail test that attendees run themselves, "ready" means nothing and you find out in the room. Write one if the exercise doesn't already have it.
- **Timing:** the agenda table is a guess based on 150 minutes total and 90 hands-on. Replace the middle rows with the real schedule or drop the table.
- **Fallback:** I assumed a pairing fallback is acceptable. If the exercise can't be shared, change that line.
- **Before Friday:** have someone who hasn't seen the setup do steps 1–5 on a fresh machine and time it. Replace "about 30 minutes" with what they measure.