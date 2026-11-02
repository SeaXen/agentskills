# Draft email

**Subject:** Technical requirements for [Conference name], [dates], for room pricing

Hello [Name],

Thank you for your patience. Below are the technical requirements for [Conference name], so you can price the rooms. We are happy to refine any figure with your technical team.

**1. Event profile**
- Dates: [dates], 2 days, plus [load-in/rehearsal day(s) to be confirmed]
- About 700 attendees, mostly software developers who will bring a laptop and a phone each, so plan for roughly 1,400 Wi-Fi devices
- 3 rooms: a main room (about 700 seats, theatre style) and two parallel-track rooms (about [X] seats each)
- All sessions in all 3 rooms are recorded. The main room is also live-streamed.

**2. Network**
- **Production uplink (streaming and uploads):** a dedicated, wired, symmetric connection of at least 50 Mbps up, ideally 100 Mbps. It must not be shared with attendee Wi-Fi. A second failover line would be ideal.
- **Attendee Wi-Fi:** a shared downlink of at least 1 Gbps, with an access-point design for high density (700 people in the main room). Please tell us what your standard offer includes and what it costs.
- **Wired drops:** 4 Ethernet drops in the main room (stage, front of house, camera/control position, and one spare), and 2 in each other room. Please confirm whether they are patched to the production line above.
- **Access:** no captive portal or per-device login on the production network, and open outbound ports for streaming (RTMP/SRT). Please confirm your firewall policy.

**3. Video and streaming (main room)**
- Camera positions for 4 cameras: 2 at the back (one wide, one tight on the stage) and 2 at the sides or front. Please tell us whether you have rigging points, with load ratings, or whether we use tripods on platforms.
- Cable paths from camera positions to a control position: please confirm whether conduits or trays exist, or whether we run cable across the floor.
- A control table of about [2 m × 1 m] with a clear view of the stage, near power and a network drop.
- The room's AV feeds (projector/LED signal, house audio mix) should be available at the control position. Please tell us what formats (HDMI/SDI) and outputs your system provides.

**4. Recording (all rooms)**
- A clean audio feed from each room's sound system, plus a slide/presenter-laptop video feed (HDMI/SDI)
- Space for one recording operator or recording rack per side room, near power
- Whether recording gear needs to be your in-house equipment or ours

**5. Power**
- Dedicated circuits (not shared with lighting) for the control position and camera positions in the main room
- At least 2 outlets at each side-room control position
- Please tell us the capacity per circuit.

**6. Access and logistics**
- Load-in and load-out times and routes, loading dock access, and lift dimensions
- Rehearsal or setup time the day before
- Your rules for third-party AV and streaming crews: exclusivity clauses, in-house technician requirements, or fees to bring our own equipment

**7. Questions for you**
- What AV equipment is included in the room price (sound, microphones, projection, lighting)?
- What is billed separately: internet, Wi-Fi, power, technician hours, rigging?
- Can we get a floor plan with ceiling heights and rigging points for the three rooms?
- Is a technical site visit possible before [date]?

Please send a quote broken down by room and by service. We can also set up a call with our technical lead if useful.

Best regards,
[Name]
[Role, organization, phone]

---

# Before you send it

**⚠️ I changed your two numbers.**
- **25 Mbps up:** it covers one 1080p stream (about 8 Mbps), but it leaves no margin and nothing for uploading recordings. If it fails, you can't negotiate more after signing. I asked for 50 to 100 Mbps, dedicated and wired. Asking high costs little, since the venue only quotes.
- **Four cameras rigging:** "rigging" may not be what you need. It usually means hanging points, and most conference cameras sit on tripods. I asked about camera positions, cable paths, and a control table. Say which you want if you do need hanging points.
- **Attendee Wi-Fi:** this was missing, and for 700 developers it's usually the costliest line item. I added a 1 Gbps request.

**ℹ️ Fill in:**
- Conference name, dates, and the side-room capacities
- How many of the 4 cameras are yours versus venue-supplied

**ℹ️ Check with your AV or streaming provider:** the bitrate, Ethernet drop, and circuit numbers are my estimates, not measured needs. If you have a streaming vendor, send them this draft before Friday.