**Next action (10 min): email the venue's IT or network contact today with the questions below.** "Fast fibre WiFi" tells you nothing about this load. The room failed at about 20 minutes last time, so the cause is still unknown.

## Why the venue's answer is not enough

- **Fibre is the uplink, not the room.** WiFi capacity is set by the access points (AP) in your room, the channels, and the client limits. Fibre says nothing about any of those.
- **Your load is hard on WiFi.** Every participant holds one long-lived RDP session plus a browser console for 150 minutes. Stalls, jitter and drops hurt interactive RDP far more than low bandwidth does.
- **A failure at about 20 minutes is a real clue.** Likely causes:
  - the room filled up and the APs hit their client limit
  - DHCP leases ran out
  - the venue's firewall or NAT timed out or throttled long-lived sessions
  - the uplink is shared with the rest of the conference
  - the venue blocks outbound RDP (TCP 3389) or flags it as suspicious
  - captive-portal re-authentication or session timeouts
- **Every one of these fits "fast fibre, no problem."** None would show on a speed test.

## Plan

1. **Today: send the questions.** Ask for an answer from a network engineer, not sales.
   - Which APs cover the hands-on room, and how many clients can each handle?
   - Is the room's WiFi dedicated or shared with other rooms and the main hall?
   - What is the uplink capacity, and how much is reserved for us?
   - What happened in the hands-on room two years ago? Ask for a post-mortem, or the name of the engineer who was on site.
   - Are outbound TCP 3389 and HTTPS to your jump host and console allowed? Do they apply any firewall, proxy, throttling or session timeouts?
   - What is the DHCP pool size and lease time?
   - Can they provide wired ports, or a dedicated VLAN or SSID for us?
   - Can they give us a named engineer on site for the whole session?
2. **Week 6: run a test, not a trust exercise.**
   - Ask for access to the room, or run it remotely.
   - Bring about 5 devices, or ideally 20+ volunteers or staff, and hold real RDP sessions to the jump host for 30+ minutes.
   - Log drops and latency.
3. **Week 5: decide the fallback.** Pick one:
   - **Own network (best):** bring a portable router or APs with a mobile-data failover, and put participants on your own SSID. This costs a few hundred euros to rent.
   - **Wired:** use venue Ethernet to a switch you bring, with laptops plugged in. This is the most reliable option.
   - **Mobile hotspots:** use them only as a backup, since they are not reliable for 100+ people.
4. **Week 4: reduce the load on the network.**
   - Pre-warm the jump host and console and size them for the real participant count. This is separate from the network question.
   - Put a cap on RDP session count per user.
   - Prepare an offline mode: a local VM or a recorded walkthrough, so people can keep working if the network drops.
   - Pick an RDP-friendly profile (lower colour depth, no wallpaper, no audio).
5. **Week 2: send the final network-readiness checklist.**
   - Check that DNS and firewall allowlists are in place.
   - Confirm who is on site from the venue.
   - Confirm who owns the decision to switch to the fallback, and by when.
6. **Day of: set up two hours early.**
   - Run a full-room test with everyone's devices on the network.
   - Have a named person on your team watching the network during the session.

## Page already live

- **No retraction is needed.** Add a "Bring" line: a laptop with an RDP client, and a charger.
- **Do not promise the network yet.** Keep wording like "reliable connectivity provided" off the page until step 2 passes.
- **If you choose wired or own network:** tell participants to expect an Ethernet adapter or a dedicated SSID.
- **If the test fails and you cannot fix it:** change the format, for example pre-recorded plus offline labs. Announce it at least 3 weeks out.

## Decision rule

- **If the venue won't answer specifically or won't allow a room test:** treat that as a "no" and bring your own network.
- **If the venue explains the old failure and shows a fix:** still run the test in step 2.

**Next:** draft the email to the venue with the questions in step 1. Send it today, since a vague reply is the signal you are looking for. I can write the draft if you want it.