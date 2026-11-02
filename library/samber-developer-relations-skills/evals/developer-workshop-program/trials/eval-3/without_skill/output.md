**Next action (10 min):** email Hollin & Rowe IT today with the four questions in section 3. Don't wait for the workshop plan to firm up.

**Verdict:** ❌ Plan fails as written. Two blockers are near-certain, and one of them is hard.

## 1. Blockers

1. 🔴 **The cloud logging service needs 1–2 days to become ready.** If attendees sign up at the start, nobody has a working lab. Create the accounts or tenant at least 7 days ahead. Check them again 3 days ahead.
2. 🔴 **Bank work laptops probably cannot install your CLI and agent.** Expect no admin rights, application allowlisting, EDR flagging unsigned binaries, and blocked downloads from unknown domains. Without IT approval, 18 people stall in the first hour.
3. 🟠 **The VPN probably blocks the hosted collector.** Corporate VPNs often force all traffic through a proxy or firewall. These can block unknown domains and non-443 ports. They can also break gRPC/OTLP, or break TLS through inspection with a custom CA. Test this from a real bank laptop on the VPN before the day.
4. 🟠 **Trial signup with work emails is fragile.**
   - Bank mail filters may quarantine your verification emails.
   - 18 signups from one domain in minutes can trip your own abuse or rate limits.
   - Employees accepting your terms individually may breach bank vendor and legal policy.

## 2. Fixes

1. **Pre-provision one tenant with 18 seats.** Invite attendees by email 1 week ahead. They then only click "accept" on the day. Ask if SSO fits.
2. **Package installs for IT review.** Send signed binaries, checksums, the domain list, ports, and what the agent collects. Offer an internal mirror, or a zip on a USB stick.
3. **Prepare an install-free fallback.** Use a pre-built dev container or a remote VM that IT approves. You could also bring loaner laptops, but only if IT confirms they may join the VPN.
4. **Use sample app data only.** Send no real bank telemetry or logs to your hosted collector. State this in writing to IT.
5. **Add an offline fallback.** Use a local collector profile or a recorded demo, so a network failure does not kill the session.
6. **Load-test the collector and logging service** with 18 concurrent clients. Do not let the workshop be the first load test.
7. **Run a pilot with 1–2 Hollin & Rowe engineers** about 10 days ahead. Use their real laptop, on the VPN, doing the full install and instrument flow.

## 3. Questions for their IT

1. Can engineers install unsigned or third-party CLIs and agents? What is the approval path and lead time?
2. Which outbound domains and ports are allowed on the VPN? Is TLS inspected? Which CA is used?
3. May employees sign up for third-party trials with work emails, or must your side provision accounts?
4. Are loaner laptops or remote dev environments allowed on the VPN?

## 4. Timeline

| When | Action |
|---|---|
| Now (T-4 weeks) | Send the IT questions and the security package. |
| T-3 weeks | Get answers. Pick laptop install or fallback environment. |
| T-10 days | Run the pilot with 1–2 attendees. |
| T-7 days | Provision the tenant and logging service. Send invites. |
| T-3 days | Verify the logging service is ready. Run the load test. |
| T-1 day | Send attendees a pre-flight checklist (VPN on, invite accepted, CLI check). |
| Day | Allow 30 min for a pre-flight check at the start, with fallback seats ready. |

Without the pilot, you only learn about a VPN or IT block when the room is full.

## 5. Day-of agenda

Don't plan the install and signup for the start of a half-day session. If the pre-flight passes, the first 30 minutes cover setup and the rest is hands-on. If it fails, switch to the fallback environment and do not debug laptops live.

**Step 1 of 4 done (plan review).** Next: send the section 3 email. Draft it from the four questions if you want.