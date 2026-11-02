# Northwind Data Summit: technical requirements for the conference centre

I don't know your track count, whether any speakers present remotely, or your streaming platform. I've assumed **one main room (250 seats) with one live program feed**. Adjust the ⚠️ items if that's wrong.

Your Friday deadline is tomorrow (2026-10-16), so the email-ready block below is the thing to send.

## Email-ready block

**1. Internet (production, separate from attendee Wi-Fi)**
- Dedicated symmetric fibre, **minimum 100 Mbps up / 100 Mbps down** per streamed room. This is about 10x our actual stream (8 Mbps) so a shared uplink can't starve it.
- **Second, independent uplink** (different carrier or physical path) of at least 50/50 Mbps, with automatic or manual failover.
- Latency to major CDNs under 30 ms, jitter under 10 ms, packet loss under 0.1%.
- Static public IP for the production VLAN.
- No captive portal, content filtering, deep packet inspection, or per-client rate limiting on the production VLAN.
- Outbound ports open: TCP 443, TCP 1935 (RTMP), UDP 8801–8810 (Zoom), and UDP 3478 plus UDP 10000–60000 (WebRTC/TURN). We also need a configurable SRT range, so please confirm you can open UDP ports on request.
- Please confirm the contracted bandwidth on the uplink we'd use. Contention ratios and shared-building circuits are what usually fail.

**2. Wired network points (Cat6, not Wi-Fi)**
- 2 at the camera/FOH position.
- 2 in the control position.
- 1 at the stage or lectern.
- 1 spare.
- All on the production VLAN, with a managed switch (gigabit minimum).

**3. Attendee Wi-Fi (separate VLAN)**
- 250 people × roughly 2.5 devices = about 625 concurrent devices.
- Plan for **500 Mbps–1 Gbps aggregate**, around 2 Mbps per active user.
- High-density design: about 1 access point per 50 devices, so 10–12 APs in the room, on 5 GHz or 6 GHz.
- Ask whether they have done a site survey for this room at full occupancy.

**4. Camera positions and sightlines**
- **Camera 1, wide/program:** at the back of the room on a riser of at least 2 m × 2 m, in the centre aisle with a clear sightline. It must not be blocked by standing attendees or by screens.
- **Camera 2, speaker close-up:** at the FOH position or on a stage-left or stage-right side platform, slightly off-axis from the stage.
- **Camera 3, audience and Q&A:** roaming or on a tripod. It is optional if we stay with one wide camera.
- The slides/laptop HDMI or SDI feed goes into our switcher. This is a separate signal, not a camera.
- Cable runs from the cameras to the control position should be neat and trip-free, or flown overhead.

**5. Control position**
- About 3 m × 3 m, quiet, with sightline to the stage and its own power.
- Ideally in the room (back or side) so audio monitoring is accurate.

**6. Power**
- 2–3 dedicated 16 A circuits for production, separate from the lighting dimmer circuits.
- Surge-protected strips at FOH and the control position.

**7. Audio**
- Clean feed from the house mixer to us: balanced stereo, XLR or Dante.
- Mix-minus for remote Q&A, so remote participants don't hear their own echo.
- Return audio from remote speakers into the PA.
- Mic count: 1 lectern, 2 handhelds, 4 lavaliers (adjust to your panel plan).

**8. Lighting**
- Even, flicker-free LED lighting on the speaker position (0° dimmer flicker is the common failure with LED).
- Consistent colour temperature across the stage, ideally 4000–5600 K.
- No strong backlight from windows. Confirm blackout options.

**9. Access and logistics**
- Load-in the day before, 4–6 hours of access, plus a full tech rehearsal.
- Named on-site IT or AV contact for the whole event and the rehearsal.
- Any exclusivity or mandatory-supplier rules for AV, rigging, or network.
- Any fees for extra bandwidth, wired drops, or cable runs.

## Where the numbers come from

| Item | Figure | Reasoning |
|---|---|---|
| Program stream | 6–8 Mbps | 1080p30/60 to platform |
| Backup stream | 6–8 Mbps | Second path |
| Remote speaker in | 3–5 Mbps down | Per guest |
| Required uplink | 100 Mbps | About 10x headroom |
| Attendee Wi-Fi | 500 Mbps–1 Gbps | Capacity, not stream |

## ⚠️ Things to confirm before sending

1. **Remote audience size.** It doesn't change your uplink (one stream goes out; the CDN fans it out). It does change the platform and moderation staffing.
2. **Number of rooms or tracks.** Multiply the uplink by room count (100 Mbps each).
3. **Remote speakers.** If any, add the mix-minus and return-feed requirements above. If none, you can drop those items.
4. **Recording and captioning.** If you need recorded or live-captioned output, add one more audio path.
5. **Platform.** Tell me which one (Zoom, a streaming platform, or a custom one) and I'll tighten the port list.

Send me answers to 1–3 and I'll update the block for your actual setup.