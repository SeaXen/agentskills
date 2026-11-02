Next action, today: open a ticket for a webhook signature fix, then rotate Dana's keys. Do both before anything else.

I'm assuming "our webhook endpoint" means the endpoint that receives payment events. If it means the receiver in the sample apps, the same fix applies to the sample code, because developers copy it.

## Must finish before Thursday

If any of these is open, Dana does not stream live Thursday. A pre-recorded or sandbox-only episode is the fallback.

**1. Close the webhook hole (eng, ~1–2 days)**
- Verify an HMAC signature with a per-endpoint secret on every request.
- Use a constant-time compare.
- Reject timestamps older than ~5 minutes to block replay.
- Reject unsigned requests with 401.
- Existing customers may rely on unsigned delivery, so run log-only first, then enforce. Enforce at least for new endpoints and sandbox by Thursday. Announce a dated cutoff for the rest.
- Fix the docs and sample apps so they verify signatures.

**2. Check whether anyone abused it (security, ~2 hours)**
- Chat watched Dana fire an unsigned payload, so assume viewers did too.
- Review endpoint logs from last week for unsigned or unknown-IP requests.
- Look for state changes they caused: orders marked paid, refunds, fulfillment triggers.
- Find out whether Dana tested against live or sandbox.

**3. Rotate every key Dana holds (~30 minutes)**
- Rotate both sandbox and live keys.
- Her live key was exposed to a public stream, and the `.env` was sometimes opened on camera.
- Replace live keys with restricted, scoped keys. Streaming does not need live keys at all.

**4. Clean the streaming machine (~half a day)**
- Use a separate OS user or a dedicated laptop, with no work SSO, no password manager, and no admin console login.
- Dana does not log in to the admin console on stream. Customer data and live controls stay off camera.
- Sandbox keys only. Inject them as environment variables, and never open `.env`. Show `.env.example` instead.
- In OBS, capture a single window or a dedicated scene, never the full desktop.
- Turn on Do Not Disturb to silence notifications.

**5. Add a stream delay and chat controls (~1 hour)**
- Set a 30–60 second stream delay.
- Turn on AutoMod and slow mode, and block links.
- Recruit at least one moderator, a colleague or trusted regular. Dana should not be the only one reading chat while she codes.

## Also do this week

- **Audit past VODs and clips.** Skim for `.env`, console, and key flashes. Delete or mute those sections. Rotation already covers keys, but customer data on screen is a separate problem.
- **Write a one-page streaming policy.** Include:
  - Sandbox only.
  - Never run a viewer-supplied payload, URL, or command.
  - Never test a claimed vulnerability live.
  - Say "email security@ and I'll pass it on," then stop.
- **Publish a security contact or disclosure policy.** Chat found this bug and had nowhere to report it. Thank the reporter and invite them to submit it properly. Do not blame Dana.
- **Write a short incident note.** Cover what was exposed, what you checked, and what you fixed.

## Schedule

1. Today and tomorrow: rotate keys (item 3), start the log review (item 2), and ticket the fix (item 1).
2. Tuesday: webhook verification live in log-only mode, plus sandbox and new-endpoint enforcement. Streaming machine ready (item 4).
3. Wednesday: dry run with delay, mods, and scene (item 5). Go or no-go.

## Questions for you

1. Which endpoint did Dana hit on stream: live, sandbox, or a sample app?
2. Does any customer integration depend on unsigned delivery? This sets the enforcement date.

Next: tell me the answer to question 1 and I'll draft the incident note and the one-page streaming policy.