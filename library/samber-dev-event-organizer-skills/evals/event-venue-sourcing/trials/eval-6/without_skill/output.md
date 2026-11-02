# Should you take Dunmore's offer for HackDunmore?

**Yes in principle, but don't commit yet.** A free main hall and two seminar rooms is a strong offer. But both of IT's answers describe a lecture, not a 300-person, 36-to-48-hour hackathon. Neither answer contains a number, so you can't check either one.

**Next action:** send the question list below, then do a site visit with a live load test. That takes about 1 hour to write and about half a day to visit. You have roughly 4 months, so there is time.

## Why the two answers don't reassure me

### Network: "handles a full lecture"

| | Lecture | Hackathon |
|---|---|---|
| Devices | Laptops mostly idle | About 600-900 (laptop plus phone each) |
| Traffic | Light browsing | `git clone`, Docker and npm pulls, API calls, video calls, demo uploads |
| Duration | 1-2 h | 24-48 h, with peaks at kickoff and before judging |

Common failure points:

- ⚠️ **DHCP pool.** A /24 gives 254 addresses, so 300 people with 2-3 devices each exhausts it.
- ⚠️ **Access point capacity.** Many APs fall over past about 50-100 associated clients each, and a lecture hall may have only a few.
- ⚠️ **Uplink.** A shared uplink in a university is often shared with the whole campus.
- ⚠️ **Guest access.** Visiting students may not get campus credentials. Captive portals, 802.1X (eduroam) and per-user device limits can all block them.
- ⚠️ **Filtering.** Blocked ports (SSH, git over SSH, VPN, WebSockets) and content filters break hackathon tooling.
- ⚠️ **Shared NAT.** One public IP can trip rate limits at GitHub, Docker Hub and npm.
- ⚠️ **Client isolation.** It can break local demos between teammates.

### Power: "sockets all along the walls"

- ⚠️ **Seat access.** In a lecture hall, people sit in tiered rows, far from the walls. A wall socket doesn't power the centre of a row.
- ⚠️ **Load.** Rough estimate: 300 laptops at about 50 W average is about 15 kW, plus phones, monitors and sponsor demo hardware. That is several separate circuits, not a few wall sockets. The socket count says nothing about the circuit capacity behind them.
- ⚠️ **Safety.** Hundreds of extension leads across aisles raise trip-hazard, fire-marshal and insurance issues. They can also block emergency exits.
- ℹ️ **Seating.** Fixed rows with no tables are poor for teamwork. The seminar rooms may suit team space better than the hall does. This is about the room, not just the sockets.

## Questions to send Dunmore (ask for written answers with numbers)

**Network** (send to network engineers, not the helpdesk):
1. How many access points cover each of the three rooms? What is the per-AP client limit?
2. What is the uplink bandwidth, and what share can we count on at peak?
3. How large is the DHCP pool for these VLANs?
4. How do non-Dunmore attendees connect? Is there a guest network, a captive portal, a device limit or an expiry?
5. Which ports and sites are filtered? Is there client isolation?
6. Can we bring our own APs and switches? Can we get a dedicated VLAN or a separate line?
7. Is on-site network staff available during the event?

**Power** (send to Estates or Facilities):
1. How many sockets are in each room, and how many are within reach of seats?
2. How many circuits feed the rooms, at what amperage?
3. Can an electrician add temporary distribution for the event? Who pays for it?
4. What are the rules on extension leads and cable runs? Is there a fire-marshal sign-off?

**Venue and cost:**
1. What is the real capacity of each room? What is the fire-safety limit with tables?
2. Is the building open 24 h? Who is responsible for security, caretakers and heating on a February weekend?
3. What does "free" exclude (security staff, AV technician, cleaning, overnight caretaker)?
4. Are there rules on catering exclusivity, alcohol, sleeping on site, sponsor branding or minors?
5. Who carries insurance and liability? What are the cancellation terms?

## Site visit test

Do this with 20-30 volunteers, on a day the hall is free.

1. Have everyone join the guest network. Note how long it takes and any failures.
2. Run speedtests and `git clone` of a large repo at the same time.
3. Test SSH to GitHub, a Docker pull, a video call and a WebSocket demo.
4. Walk the room, count sockets within reach of seats, and note which are on the same circuit.
5. Ask an electrician or the facilities contact to confirm circuit capacity on the spot.

**Pass signal:** the network stays stable with the volunteer load, and the vendor-side numbers show headroom for about 10 times that load. Power passes if the circuits plus temporary distribution cover about 15-20 kW with safe cable routing.

## Decision rule

- 🟢 **Take it** if the answers are specific and either the network meets your target or you can bring your own network gear and uplink, and power can be extended safely.
- 🟠 **Take it with a patch** if gaps are fixable with budget, such as a rented uplink, your own APs, or temporary electrical distribution. Cost these before accepting.
- 🔴 **Pass or shrink** if the uplink is shared and can't be raised, or power can't be extended safely. Consider capping attendance at what the infrastructure supports, rather than risking a hackathon where nobody can connect.

Also keep Dunmore's offer open while you check. Don't decline it, and don't sign anything until the written answers are in.